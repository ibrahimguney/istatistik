"""Yayın manifesti, B07–B14 kopyaları/ZIP'leri ve yerel HTML bağlantıları."""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "atolye"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for attr in ("href", "src"):
            if attr in attrs:
                self.links.append(attrs[attr])


def main():
    manifest = json.loads((SITE / "yayin-manifest.json").read_text(encoding="utf-8"))
    actual = {p.relative_to(SITE).as_posix() for p in SITE.rglob("*") if p.is_file()}
    assert actual == set(manifest["files"]) | {"yayin-manifest.json"}, "Yayın dosya listesi farklı"
    assert manifest["algorithm"] == "SHA-256"
    for name, expected in manifest["files"].items():
        path = PurePosixPath(name)
        assert not path.is_absolute() and ".." not in path.parts
        assert hashlib.sha256((SITE / name).read_bytes()).hexdigest() == expected, name
    for n in range(7, 15):
        code = f"b{n:02}"
        source = ROOT / "bolumler" / code
        files = {p.relative_to(source).as_posix(): p.read_bytes() for p in source.rglob("*")
                 if p.is_file() and "__pycache__" not in p.parts}
        package_manifest = json.loads(files["MANIFEST.json"])
        assert set(files) == set(package_manifest["files"]) | {"MANIFEST.json"}, code
        for name, expected in package_manifest["files"].items():
            assert hashlib.sha256(files[name]).hexdigest() == expected, (code, name)
        with zipfile.ZipFile(SITE / "indir" / f"{code}-ogretim.zip") as archive:
            assert set(archive.namelist()) == {code + "/" + name for name in files}
            assert archive.testzip() is None
            for name, content in files.items():
                assert archive.read(code + "/" + name) == content
                assert (SITE / "bolumler" / code / name).read_bytes() == content
    for page in [SITE / "index.html", *[SITE / f"b{n:02}.html" for n in range(7, 15)]]:
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8"))
        for link in parser.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = page.parent / unquote(url.path) if url.path else page
            assert target.is_file(), (page.name, link)
            if url.fragment and target.suffix == ".html":
                dest = Links()
                dest.feed(target.read_text(encoding="utf-8"))
                assert unquote(url.fragment) in dest.ids, (page.name, link)
    print(f"GECTI: {len(actual)} yayın dosyası; 8 bölüm paketi/ZIP ve yeni sayfaların bağlantıları.")


if __name__ == "__main__":
    main()
