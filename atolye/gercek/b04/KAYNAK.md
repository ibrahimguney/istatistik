# Kaynak ve dönüşüm

Cortez, P. (2008). Student Performance [Dataset]. UCI Machine Learning
Repository. DOI: 10.24432/C5TG7T.
Kaynak: https://archive.ics.uci.edu/dataset/320/student+performance
Lisans: CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/

Bu atıf/lisans bilgisi yerel companion/spss/README.md kaydından aktarılmıştır;
orada kontrol tarihi 9 Eylül 2026'dır. Bu teslimde çevrim içi lisans
denetimi yeniden yapılmadı. UCI veya veri yazarının bu paketi onayladığı
iddia edilmez. İşleme ve paketleme: İstatistik kitabı eşlikçi projesi.

Kaynak student-mat.csv, 395 öğrenci ve 33 alan içerir. Dönüşümde G3 notları
kullanılır; sıfır notlu 38 kayıt korunur. SEED=2026 ile NumPy default_rng
üzerinden 2000×100 geri koymalı çekim yapılır. Her satırın ilk 5 ve ilk 30
değerinin ortalaması ort5/ort30 olarak kaydedilir; rep 1–2000 sıra numarasıdır.
İki sütun ortak çekimler içerir. Bu hazır çıktı 2000 yeni öğrenci değildir.

Bu test paketi yalnız hazır b04.csv'yi okur; benzetimi yeniden çalıştırmaz.
Ham veri ve genel build_package.py çalıştırma bağımlılığı değildir ve bu
teslimde bulunmaz. Kaynak hashleri/üretim düzeni URETIM-KAYDI.json içindedir.
Sabit tohum, farklı yazılımların aynı rastgele çekimleri üreteceği iddiası
değildir. R/SPSS yeniden çalıştırması ve yayın kabulü ayrıca değerlendirilir.
