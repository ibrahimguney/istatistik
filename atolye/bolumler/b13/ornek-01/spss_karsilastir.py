"""SPSS spss-dogrula.sps dışa aktarımlarını ortak referansla karşılaştırır.

Tek başına SPSS çalıştırmaz. SPSS çıktısı bulunmadan başarılı sonuç üretmez.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import sys
from datetime import datetime, timezone


def read(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return [{k.lower().strip(): v.strip() for k, v in r.items()} for r in reader]


def same(a, b):
    try:
        return math.isfinite(float(a)) and float(a) == float(b)
    except ValueError:
        return a == b


def compare(folder):
    config = json.loads((folder / "spss-esleme.json").read_text(encoding="utf-8"))
    expected = read(folder / "beklenen-sonuclar.csv")
    refs = {(r["degisken"], r["olcu"]): float(r["deger"]) for r in expected}
    keys = [(m["degisken"], m["olcu"]) for m in config["mappings"]]
    if len(keys) != len(set(keys)) or set(keys) != set(refs) or len(refs) != len(expected):
        raise ValueError("Eşleme ve referans anahtarları birebir değil.")
    inputs, errors, comparisons = {}, [], []
    for name, count in config["expected_rows"].items():
        data = read(folder / name)
        if len(data) != count:
            raise ValueError(f"{name}: beklenen {count}, bulunan {len(data)} satır.")
        inputs[name] = data
    for m in config["mappings"]:
        candidates = [r for r in inputs[m["file"]] if all(same(r[k], v) for k, v in m["where"].items())]
        if len(candidates) != 1:
            raise ValueError(f"Tekil SPSS satırı bulunamadı: {m}")
        value = float(candidates[0][m["column"]])
        target = refs[(m["degisken"], m["olcu"])]
        passed = math.isfinite(value) and math.isclose(value, target, rel_tol=1e-8, abs_tol=1e-14)
        item = {"degisken": m["degisken"], "olcu": m["olcu"], "beklenen": target,
                "spss": value, "gecti": passed}
        comparisons.append(item)
        if not passed:
            errors.append(item)
    # B13: SPSS REGRESSION yordamının tahmin/artıklarını ayrıca kontrol et.
    for r in inputs.get("spss-satirlar.csv", []):
        for actual, formula in [("uydurulan_spss", "uydurulan"), ("artik_spss", "artik")]:
            if "satir" in r and (actual not in r or not math.isclose(float(r[actual]), float(r[formula]), rel_tol=1e-8, abs_tol=1e-14)):
                errors.append({"satir": r["satir"], "yordam_farki": actual})
    files = ["beklenen-sonuclar.csv", "spss-esleme.json", "analiz.sps", "spss-dogrula.sps", *inputs]
    return {"tarih_utc": datetime.now(timezone.utc).isoformat(), "gecti": not errors,
            "kontrol_sayisi": len(comparisons), "rel_tol": 1e-8, "abs_tol": 1e-14,
            "kapsam": "Kullanıcının sunduğu CSV dışa aktarımlarının sayısal karşılaştırması; SPV veya yazılım kökeni otomatik doğrulanmaz.",
            "sha256": {n: hashlib.sha256((folder / n).read_bytes()).hexdigest() for n in files},
            "sonuclar": comparisons, "hatalar": errors}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--klasor", default=".")
    p.add_argument("--surum", required=True, help="Çıktıyı üreten IBM SPSS sürümü, örn. 29.0.2")
    p.add_argument("--rapor", default="spss-sonuc.json")
    args = p.parse_args()
    target = Path(args.rapor)
    if target.exists():
        p.error("Rapor zaten var; yeni bir ad seçin.")
    try:
        result = compare(Path(args.klasor))
    except (OSError, ValueError, KeyError, TypeError) as e:
        print(f"KONTROL BAŞARISIZ: {e}", file=sys.stderr)
        return 1
    result["spss_surumu_kullanici_bildirimi"] = args.surum
    with target.open("x", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"{'GECTI' if result['gecti'] else 'BASARISIZ'}: {result['kontrol_sayisi']} kontrol; rapor: {target}")
    return 0 if result["gecti"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
