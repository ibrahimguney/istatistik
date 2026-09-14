# B03 gerçek veri — yerel test paketi

ZIP'i tam çıkarın. Çalışma dizini companion klasörünü içeren b03-gercek
klasörü olmalıdır. B01/B02 ile aynı 395 kayıt kullanılır; yeni bağımsız
örneklem değildir. Kaynak ve kullanım koşulları KAYNAK.json içindedir.
Eksik değer yoktur; sıfır notlu 38 kayıt ve 75 devamsızlık kaydı korunur.

Python: py companion/spss/python/b03.py
Analiz için pandas, numpy, scipy ve matplotlib gerekir.
R konsolu: source("companion/spss/r/b03.R")
SPSS: açık çalışmaları kaydedin; ayrı oturumda çalışma dizinini paket
kökü yapıp companion/spss/syntax/b03.sps dosyasını çalıştırın.
open-b01.sps CSV'den sav/b01.sav üretir; evdeki dosya gerekmez.
Aynı adlı SAV üzerine yazılabilir; etkin veri/oturum ayarları değişir.

Python/R kodları özgün B03 kaynaklarıdır. SPSS kodu kitap bloğudur.
Beklenen değerler beklenen-sonuclar.csv içindedir; küçük öğretim
örneğindeki --check bu kodlarda yoktur. Grafikler ekranda gösterilir.
Python histogramı 15 sınıflıdır; R/SPSS otomatik sınıfları ve kutu
grafiği yöntemleri farklı olabilir. Piksel eşitliği beklenmez.
Ortalama güven aralığı bireylerin %95'ini kapsayan aralık değildir.
Kodlardaki t işlemlerinden yalnız ortalama güven aralığı okunur;
sıfıra karşı test veya Türkiye geneline genelleme yorumu yapılmaz.
Bu üretici analiz çalıştırmaz. R/SPSS bu teslimde yeniden çalıştırılmadı.
