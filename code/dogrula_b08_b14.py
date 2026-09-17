"""B07–B14: gerçek Python/R çalıştırması, referans ve hata algılama denetimi.

Çalıştırma: python code/dogrula_b08_b14.py --rapor dogrulama/sonuc.json
Kaynak paketler değiştirilmez. SPSS bu betikle çalıştırılmaz.
"""
import argparse
import csv
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]


def run(command, cwd):
    p = subprocess.run(command, cwd=cwd, text=True, encoding="utf-8",
                       errors="replace", capture_output=True, timeout=180,
                       env=dict(os.environ, MPLBACKEND="Agg", PYTHONDONTWRITEBYTECODE="1"))
    return {"exit_code": p.returncode, "stdout": p.stdout, "stderr": p.stderr}


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def check_chapter(code, rscript):
    package = ROOT / "bolumler" / code
    source = package / "ornek-01"
    expected = rows(source / "beklenen-sonuclar.csv")
    record = {"bolum": code, "kontrol_sayisi": len(expected), "spss": "calistirilmadi",
              "source_sha256": {p.relative_to(package).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in sorted(source.iterdir()) if p.is_file()}}
    manifest = json.loads((package / "MANIFEST.json").read_text(encoding="utf-8"))
    record["manifest_gecti"] = all((package / n).is_file() and hashlib.sha256((package / n).read_bytes()).hexdigest() == h
                                  for n, h in manifest["files"].items())
    with tempfile.TemporaryDirectory(prefix=code + "-") as temp:
        work = Path(temp) / "ornek-01"
        shutil.copytree(source, work)
        extra = ', pd.read_csv("benzetim.csv")' if code == "b07" else ', pd.read_csv("plan.csv")' if code == "b10" else ''
        (work / "driver.py").write_text('import pandas as pd\nimport cozum\n'
            + f'cozum.hesapla(pd.read_csv("veri.csv"){extra}).to_csv("python-actual.csv", index=False)\n', encoding="utf-8")
        (work / "driver.R").write_text('source("cozum.R", encoding="UTF-8")\n'
            'write.csv(sonuc, "r-actual.csv", row.names=FALSE)\n', encoding="utf-8")
        commands = {"python": [sys.executable, "cozum.py", "--check", "--grafik"],
                    "r": [rscript, "--vanilla", "driver.R", "--check", "--grafik"]}
        for language, cmd in commands.items():
            result = run(cmd, work)
            result["gecti"] = result["exit_code"] == 0 and bool(re.search(rf"DOGRULANDI:\s*{len(expected)}\s+kontrol", result["stdout"]))
            record[language] = result
        export = run([sys.executable, "driver.py"], work)
        record["python_export"] = export
        differences = []
        if record["python"]["gecti"] and record["r"]["gecti"] and export["exit_code"] == 0:
            py, r = rows(work / "python-actual.csv"), rows(work / "r-actual.csv")
            if len(py) != len(expected) or len(r) != len(expected):
                differences.append("Satır sayıları farklı")
            else:
                for a, b in zip(py, r):
                    x, y = float(a["deger"]), float(b["deger"])
                    if (a["degisken"], a["olcu"]) != (b["degisken"], b["olcu"]) or not math.isclose(x, y, rel_tol=1e-9, abs_tol=1e-15):
                        differences.append({"python": a, "r": b})
            record["python_r_eslesmesi"] = {"gecti": not differences, "farklar": differences,
                "rel_tol": 1e-9, "abs_tol": 1e-15, "python_sonuclari": py, "r_sonuclari": r}
        reference = work / "beklenen-sonuclar.csv"
        original = reference.read_bytes()
        altered = [dict(x) for x in expected]
        altered[0]["deger"] = str(float(altered[0]["deger"]) + 1)
        with reference.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["degisken", "olcu", "deger"])
            writer.writeheader()
            writer.writerows(altered)
        record["degistirilmis_referans"] = {lang: run(cmd, work) for lang, cmd in commands.items()}
        reference.write_bytes(original)
        (work / "veri.csv").unlink()
        record["eksik_veri"] = {lang: run(cmd, work) for lang, cmd in commands.items()}
    record["gecti"] = (record["manifest_gecti"] and record["python"]["gecti"] and record["r"]["gecti"]
                       and record.get("python_r_eslesmesi", {}).get("gecti", False)
                       and all(r["exit_code"] != 0 for kind in ("degistirilmis_referans", "eksik_veri") for r in record[kind].values()))
    return record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rapor", required=True)
    args = parser.parse_args()
    target = Path(args.rapor)
    if target.exists():
        parser.error("Yeni bir rapor dosyası adı kullanın.")
    rscript = shutil.which("Rscript")
    if not rscript:
        parser.error("Gerçek Rscript bulunamadı; R doğrulandı olarak işaretlenemez.")
    report = {"tarih_utc": datetime.now(timezone.utc).isoformat(),
              "kapsam": "B08–B14 ve siteye eklenen B07; ortak CSV, Python/R, grafik üretimi ve negatif kontroller. IBM SPSS çalıştırılmadı.",
              "python": platform.python_version(),
              "versions": {p: importlib.metadata.version(p) for p in ("numpy", "pandas", "scipy", "matplotlib")},
              "r_session": run([rscript, "--vanilla", "-e", "sessionInfo()"], ROOT), "bolumler": []}
    for n in range(7, 15):
        result = check_chapter(f"b{n:02}", rscript)
        report["bolumler"].append(result)
        print(result["bolum"], "GECTI" if result["gecti"] else "BASARISIZ", flush=True)
    report["gecti"] = all(c["gecti"] for c in report["bolumler"])
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("x", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return 0 if report["gecti"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
