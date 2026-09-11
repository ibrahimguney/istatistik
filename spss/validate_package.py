"""Read-only checks: XLSX round trip, raw-data computations and package links.
Does NOT execute SPSS or claim Excel/SPSS application compatibility.
"""
from pathlib import Path
import hashlib
import json
import re
import zipfile
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'companion/spss'
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def check():
    source = pd.read_csv(OUT / 'raw/student-mat.csv', sep=';')
    assert source.shape == (395, 33)
    assert not source.isna().any().any()
    assert source.school.value_counts().to_dict() == {'GP': 349, 'MS': 46}
    assert source.sex.value_counts().to_dict() == {'F': 208, 'M': 187}
    for col in ['G1', 'G2', 'G3']:
        assert source[col].between(0, 20).all()
    assert (source.G3 == 0).sum() == 38
    result = json.loads((OUT / 'results/checks.json').read_text())
    values = {key: item['value'] for key, item in result['values'].items()}
    y = source.G3.to_numpy(dtype=float)
    mean, sd = np.mean(y), np.sqrt(np.sum((y-y.mean())**2)/(len(y)-1))
    se = sd/np.sqrt(len(y))
    t = (mean-10)/se
    independent = {'MatMean': mean, 'MatSD': sd, 'MatSE': se,
                   'MatT': t, 'MatP': 2*stats.t.sf(abs(t),len(y)-1),
                   'MatPHat': np.mean(y>=10)}
    for key, val in independent.items():
        assert np.isclose(values[key], val, rtol=1e-12, atol=1e-12), key
    X = np.column_stack([np.ones(len(y)), source.G1])
    intercept, slope = np.linalg.lstsq(X, y, rcond=None)[0]
    assert np.isclose(values['RegSlope'], slope)
    assert np.isclose(values['RegIntercept'], intercept)
    obs = np.array([[75, 133], [55, 132]])
    expected = obs.sum(1)[:,None]*obs.sum(0)[None,:]/obs.sum()
    assert np.isclose(values['Chi'],np.sum((obs-expected)**2/expected))
    assert np.array_equal(result['crosstab'], obs)
    assert len(result['sampling_ids']['srs']) == 40
    assert len(set(result['sampling_ids']['srs'])) == 40
    assert len(set(result['sampling_ids']['stratified'])) == 40
    for name, info in result['sources'].items():
        assert hashlib.sha256((OUT/'raw'/name).read_bytes()).hexdigest() == info['sha256']
    for i in range(1,15):
        code=f'b{i:02d}'
        csv = pd.read_csv(OUT/'csv'/f'{code}.csv')
        with zipfile.ZipFile(OUT/'excel'/f'{code}.xlsx') as z:
            assert z.testzip() is None
            for name in z.namelist():
                if name.endswith('.xml') or name.endswith('.rels'): ET.fromstring(z.read(name))
            book = ET.fromstring(z.read('xl/workbook.xml'))
            assert [s.attrib['name'] for s in book.find('s:sheets',NS)] == ['veri','sozluk','kaynak']
            root = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
            rows=[]
            for row in root.findall('s:sheetData/s:row',NS):
                vals=[]
                for cell in row.findall('s:c',NS):
                    if cell.attrib.get('t') == 'inlineStr': vals.append(cell.find('s:is/s:t',NS).text)
                    else: vals.append(float(cell.find('s:v',NS).text))
                rows.append(vals)
            assert rows[0] == list(csv.columns), code
            assert len(rows)-1 == len(csv), code
            assert np.allclose(np.asarray(rows[1:]),csv.to_numpy(),rtol=1e-12,atol=1e-12),code
        if i not in [4,5]:
            assert len(csv) == 395 and np.array_equal(csv.g3, source.G3)
            assert np.array_equal(csv.pass10,(source.G3>=10).astype(int))
        else: assert len(csv)==2000 and 'rep' in csv
        sps=(OUT/'syntax'/f'{code}.sps').read_text()
        opening=(OUT/'syntax'/f'open-{code}.sps').read_text()
        assert f"INSERT FILE='companion/spss/syntax/open-{code}.sps'" in sps
        assert f"/FILE='companion/spss/excel/{code}.xlsx'" in opening
        assert f"SAVE OUTFILE='companion/spss/sav/{code}.sav'." in opening
        for flag in ['FILTER OFF.','WEIGHT OFF.','SPLIT FILE OFF.']: assert flag in opening
        if 'REGRESSION' in sps:
            reg=sps[sps.index('REGRESSION'):]
            assert reg.index('/STATISTICS') < reg.index('/DEPENDENT') < reg.index('/METHOD')
        chapter = ROOT/'chapters/spss'/f'{code}.tex'
        assert chapter.exists()
        assert f'companion/spss/syntax/{code}.sps' in chapter.read_text()
    definitions=set(re.findall(r'\\newcommand\{\\(SP[A-Za-z]+)\}',(OUT/'results/values.tex').read_text()))
    uses=set()
    for p in (ROOT/'chapters/spss').glob('b*.tex'):
        uses.update(re.findall(r'\\(SP[A-Za-z]+)',p.read_text()))
    assert uses <= definitions, uses-definitions
    manifest=pd.read_csv(OUT/'manifest.csv')
    for item in manifest.itertuples():
        assert hashlib.sha256((OUT/item.file).read_bytes()).hexdigest() == item.sha256,item.file
    print('PASS: 14 XLSX/CSV round trips, raw-data checks, numerical cross-checks,')
    print('28 SPSS file paths and regression ordering, 14 chapter listings, source/manifest hashes.')
    print('IBM SPSS and Excel were not executed; runtime/import validation remains external.')

if __name__ == '__main__':
    check()