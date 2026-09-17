# B13 — güncel çalışma kaydı · 17 Eylül 2026

Python ve gerçek R 4.3.3 yorumlayıcısında `62` referans değeri karşılaştırıldı.
İki yazılımın hesapladığı sonuçlar ayrıca birbirleriyle karşılaştırıldı (bağıl tolerans 1e-9,
mutlak tolerans 1e-15). `--check --grafik` çalıştırıldı; grafik üretimi denetlendi.
Değiştirilmiş referans ve eksik veri iki yazılımda da hata verdi.
Grafikler geçici çalışma klasöründe üretildi; dağıtımdaki özgün Python grafikleri korunur.

**IBM SPSS çalıştırılmadı.** Kaynak incelemesi ve Python/R eşleşmesi SPSS kabulü değildir.
`ornek-01/spss-dogrula.sps` SPSS sonuçlarını CSV olarak dışa aktarır.
`ornek-01/spss_karsilastir.py` dışa aktarımları referanslarla karşılaştırır.
Adımlar: [SPSS kontrol rehberi](SPSS-KONTROL.md).

Eski DOGRULAMA.md içindeki 9 Eylül kaydı tarihsel denetimi açıklar.
Güncel tam çalıştırma günlüğü depo kökündeki
`dogrulama/python-r-2026-09-17.json` dosyasındadır.
Kod, veri ve paket dosyalarının SHA-256 değerleri güncel MANIFEST.json içindedir.
Ham veri/özet ayrımı, örnekleme varsayımları ve yorum sınırları devam eder.
