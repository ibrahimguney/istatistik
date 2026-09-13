import contextlib
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import platform
import runpy
import statistics
import xml.etree.ElementTree as ET
import zipfile


COLUMNS = ['id', 'school', 'sex', 'age', 'studytime', 'absences', 'g1', 'g2', 'g3', 'pass10']
RAW_SHA256 = '041d88ddca1da9fb8a1a9261bbf090d2f7c75625c228392e1077c2cf656051e8'
CSV_SHA256 = 'b71d797eb8f1d0584d8afaa27ff9b8a942bd44d615688224b4252659a5c30bd1'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def source_rows(root):
    raw_bytes = (root / 'companion/spss/raw/student-mat.csv').read_bytes()
    csv_bytes = (root / 'companion/spss/csv/b01.csv').read_bytes()
    require(hashlib.sha256(raw_bytes).hexdigest() == RAW_SHA256, 'Ham dosya hash farkı')
    require(hashlib.sha256(csv_bytes).hexdigest() == CSV_SHA256, 'B01 CSV hash farkı')
    raw = list(csv.DictReader(io.StringIO(raw_bytes.decode()), delimiter=';'))
    reader = csv.DictReader(io.StringIO(csv_bytes.decode()))
    require(reader.fieldnames == COLUMNS, 'Sütun sırası farklı')
    rows = list(reader)
    require(len(raw) == len(rows) == 395 and len(raw[0]) == 33, 'Kaynak boyutu farklı')
    require(all(len(row) == 33 and all(value not in (None, '') for value in row.values()) for row in raw), 'Eksik ham hücre')
    expected = []
    for number, row in enumerate(raw, 1):
        selected = {'id': str(number), 'school': {'GP': '1', 'MS': '2'}[row['school']],
                    'sex': {'F': '1', 'M': '2'}[row['sex']]}
        selected.update({name.lower(): row[name] for name in ['age', 'studytime', 'absences', 'G1', 'G2', 'G3']})
        selected['pass10'] = str(int(int(row['G3']) >= 10))
        expected.append(selected)
    require(rows == expected, 'Ham kaynaktan 395 × 10 eşleştirme farklı')
    return rows


def independent_summary(rows):
    summary = []
    for name in ['age', 'g1', 'g2', 'g3']:
        values = [int(row[name]) for row in rows]
        for measure, value in [('count', len(values)), ('mean', statistics.mean(values)),
                               ('std', statistics.stdev(values)), ('min', min(values)), ('max', max(values))]:
            summary.append({'variable': name, 'measure': measure, 'value': value})
    return summary


def check_excel(root, rows):
    namespace = {'sheet': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(root / 'companion/spss/excel/b01.xlsx') as archive:
        require(archive.testzip() is None, 'Excel CRC hatası')
        xml = ET.fromstring(archive.read('xl/worksheets/sheet1.xml'))
        table = []
        for row in xml.findall('sheet:sheetData/sheet:row', namespace):
            table.append([cell.findtext('sheet:is/sheet:t', namespaces=namespace)
                          if cell.get('t') == 'inlineStr' else cell.findtext('sheet:v', namespaces=namespace)
                          for cell in row])
        require(table == [COLUMNS] + [[row[name] for name in COLUMNS] for row in rows], 'Excel hücreleri CSV ile farklı')
        for number in [2, 3]:
            ET.fromstring(archive.read(f'xl/worksheets/sheet{number}.xml'))
    return True


def verify(root=Path('.')):
    rows = source_rows(root)
    check_excel(root, rows)
    require(root == Path('.'), 'Analiz paket kökünden çalıştırılmalı')
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        namespace = runpy.run_path('companion/spss/python/b01.py')
    frame = namespace['d']
    require(frame.shape == (395, 10), 'Python çıktı boyutu farklı')
    require(not frame.isna().any().any(), 'Python eksik değer kontrolü geçmedi')
    computed = frame[['age', 'g1', 'g2', 'g3']].agg(['count', 'mean', 'std', 'min', 'max'])
    reference = independent_summary(rows)
    for item in reference:
        require(math.isclose(float(computed.loc[item['measure'], item['variable']]), item['value'],
                             rel_tol=1e-12, abs_tol=1e-12), 'Python/standart kütüphane farklı')
    frequencies = []
    for name, mapping in [('school', {'1': 'GP', '2': 'MS'}), ('sex', {'1': 'F', '2': 'M'})]:
        for code, label in mapping.items():
            count = sum(row[name] == code for row in rows)
            require(int(frame[name].value_counts()[label]) == count, 'Frekans farklı')
            frequencies.append({'variable': name, 'category': label, 'count': count, 'percent': 100 * count / len(rows)})
    require([item['count'] for item in frequencies] == [349, 46, 208, 187], 'Kitap frekansları farklı')
    return {'python_executed': True, 'r_executed': False, 'spss_executed': False,
            'rows': 395, 'columns': 10, 'source_mapping_pass': True, 'excel_cell_comparison_pass': True,
            'numeric_comparisons': 24, 'missing_column_checks': 10,
            'python_version': platform.python_version(), 'pandas_version': namespace['pd'].__version__,
            'numpy_version': namespace['np'].__version__, 'scipy_version': __import__('scipy').__version__,
            'summary': reference, 'frequencies': frequencies, 'python_stdout': capture.getvalue()}


if __name__ == '__main__':
    print(json.dumps(verify(), ensure_ascii=False, indent=2))
