# B02 gerçek veri paketi
Bu paket B01 ile aynı 395 kaydı kullanır; bağımsız yeni örneklem değildir.
KAYNAK.json ve sozluk.csv B01'den aynen korunur; yeni lisans atanmaz.
ZIP'in tamamını ayrı klasöre çıkarın. Çalışma dizini içinde companion olan
b02-gercek klasörüdür. Hazır SAV veya Excel dağıtılmaz.

Python: python companion/spss/python/b02.py (pandas, numpy, scipy).
R: Rscript companion/spss/r/b02.R (temel R).
SPSS: açık çalışmalarınızı kaydedip ayrı oturum kullanın; paket kökünü
çalışma dizini yapıp companion/spss/syntax/b02.sps çalıştırın.
Bu kod open-b01.sps üzerinden CSV okur ve sav/b01.sav üretir; aynı adlı
SAV üzerine yazabilir. Etkin veri kümesi ve filtre/ağırlık/split ayarları değişir.

Okul 1=GP/2=MS; kaynak cinsiyet kodu 1=F/2=M; çalışma süresi kategorileri
1:<2, 2:2–5, 3:5–10, 4:>10 saat. Kodlar saat miktarı değildir.
G3=0 eksik kodu değildir. Beklenen N=395; okul frekansı 349/46;
cinsiyet 208/187; çalışma süresi 105/198/65/27.
Yaş ortalaması 16.696203, örneklem SS 1.276043, min 15, max 22.
G3 ortalaması 10.415190, örneklem SS 4.581443, min 0, max 20.
Üretici analiz çalıştırmaz. R/SPSS burada yeniden çalıştırılmış sayılmaz.
Kayıtlar Türkiye'deki bütün lise öğrencilerine doğrudan genellenemez.
