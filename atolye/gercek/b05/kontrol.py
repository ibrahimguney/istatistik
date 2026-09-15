"""B05 ampirik test paketini veri üretmeden denetler."""
import csv
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import statistics
import sys

CSV_SHA256 = 'e4bc608bc97a675dd4617c63bf8be0c72ed4151ab697be8df6e804d46358bada'
VARIABLES = ['ort5', 'z5', 'ort30', 'z30', 'ort100', 'z100']
MU = 10.415189873417722
SIGMA = 4.57563964146053


def check(folder):
    manifest = json.loads((folder / 'manifest.json').read_bytes())
    if manifest['algorithm'] != 'SHA-256' or len(manifest['files']) != 9:
        raise ValueError('Manifest kapsami farkli.')
    for name, expected in manifest['files'].items():
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or '\\' in name or ':' in name:
            raise ValueError('Manifest yolu uygun degil.')
        if hashlib.sha256((folder / name).read_bytes()).hexdigest() != expected:
            raise ValueError('Dosya hash eslesmedi: ' + name)
    data_path = folder / 'companion/spss/csv/b05.csv'
    if hashlib.sha256(data_path.read_bytes()).hexdigest() != CSV_SHA256:
        raise ValueError('Sabit B05 CSV hash eslesmedi.')
    with data_path.open(encoding='utf-8', newline='') as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ['rep'] + VARIABLES:
            raise ValueError('CSV sutunlari farkli.')
        rows = list(reader)
    if len(rows) != 2000 or [row['rep'] for row in rows] != [str(number) for number in range(1, 2001)]:
        raise ValueError('Tekrar sayisi veya sirasi farkli.')
    columns = {name: [float(row[name]) for row in rows] for name in VARIABLES}
    if not all(math.isfinite(value) for values in columns.values() for value in values):
        raise ValueError('Sonlu olmayan deger.')
    with (folder / 'beklenen-sonuclar.csv').open(encoding='utf-8', newline='') as stream:
        references = list(csv.DictReader(stream))
    if [row['degisken'] for row in references] != VARIABLES:
        raise ValueError('Referans kapsami farkli.')
    for reference in references:
        values = columns[reference['degisken']]
        actual = dict(n=len(values), ortalama=statistics.mean(values),
                      orneklem_std=statistics.stdev(values), minimum=min(values), maximum=max(values))
        for label, value in actual.items():
            if not math.isclose(value, float(reference[label]), rel_tol=0, abs_tol=1e-9):
                raise ValueError('Ozet eslesmedi: ' + reference['degisken'] + '/' + label)
        print(reference['degisken'], actual)
    for size in (5, 30, 100):
        for mean, standardized in zip(columns[f'ort{size}'], columns[f'z{size}']):
            if not 0 <= mean <= 20 or not math.isclose(
                    (mean - MU) / (SIGMA / math.sqrt(size)), standardized, rel_tol=0, abs_tol=1e-12):
                raise ValueError('Standartlastirma eslesmedi.')
    inside = sum(abs(value) <= 1.96 for value in columns['z100'])
    outside = len(rows) - inside
    percent = 100 * inside / len(rows)
    if (inside, outside) != (1892, 108) or not math.isclose(percent, 94.6, rel_tol=0, abs_tol=1e-12):
        raise ValueError('Kapsama eslesmedi.')
    print('Kapsama:', inside, 'iceride;', outside, 'disarida;', percent, '%')
    print('R/SPSS veya grafik kontrolu yapilmadi.')
    print('DOGRULANDI: 2000 tekrar; 33 kontrol degeri eslesiyor.')


if __name__ == '__main__':
    try:
        check(Path(__file__).parent)
    except (ValueError, OSError, KeyError, TypeError, csv.Error) as error:
        print('HATA:', error, file=sys.stderr)
        sys.exit(1)
