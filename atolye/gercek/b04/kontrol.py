"""Dağıtılan B04 benzetim dosyalarını ve on betimsel özeti kontrol eder."""
import csv
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import statistics
import sys

CSV_SHA256 = '30b1cef70e82d1a602d86b60966d3fea32222b7e72f9454fafc0410f024a5984'


def check(folder):
    record = json.loads((folder / 'manifest.json').read_bytes())
    if record['algorithm'] != 'SHA-256' or len(record['files']) != 11:
        raise ValueError('Manifest kapsamı farklı.')
    for name, expected in record['files'].items():
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or '\\' in name or ':' in name:
            raise ValueError('Manifest yolu uygun değil.')
        if hashlib.sha256((folder / name).read_bytes()).hexdigest() != expected:
            raise ValueError('Dosya hash eşleşmedi: ' + name)
    data_path = folder / 'companion/spss/csv/b04.csv'
    if hashlib.sha256(data_path.read_bytes()).hexdigest() != CSV_SHA256:
        raise ValueError('Sabit B04 CSV hash eşleşmedi.')
    with data_path.open(encoding='utf-8', newline='') as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ['rep', 'ort5', 'ort30']:
            raise ValueError('CSV sütunları farklı.')
        rows = list(reader)
    if len(rows) != 2000 or [row['rep'] for row in rows] != [str(index) for index in range(1, 2001)]:
        raise ValueError('Tekrar sayısı veya sırası farklı.')
    with (folder / 'beklenen-sonuclar.csv').open(encoding='utf-8', newline='') as stream:
        references = list(csv.DictReader(stream))
    if [row['degisken'] for row in references] != ['ort5', 'ort30']:
        raise ValueError('Referans kapsamı farklı.')
    for reference in references:
        values = [float(row[reference['degisken']]) for row in rows]
        if not all(math.isfinite(value) and 0 <= value <= 20 for value in values):
            raise ValueError('Geçersiz tekrar ortalaması.')
        actual = dict(n=len(values), ortalama=statistics.mean(values),
                      orneklem_std=statistics.stdev(values), minimum=min(values), maximum=max(values))
        for label, value in actual.items():
            if not math.isclose(value, float(reference[label]), rel_tol=0, abs_tol=1e-9):
                raise ValueError('Özet eşleşmedi: ' + reference['degisken'] + '/' + label)
        print(reference['degisken'], actual)
    print('DOGRULANDI: 2000 tekrar; 10 betimsel deger eslesiyor.')
    print('R/SPSS veya grafik kontrolü yapılmadı.')


if __name__ == '__main__':
    try:
        check(Path(__file__).parent)
    except (ValueError, OSError, KeyError, TypeError, csv.Error) as error:
        print('HATA:', error, file=sys.stderr)
        sys.exit(1)
