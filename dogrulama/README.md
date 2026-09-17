# B08–B14 — ortak doğrulama ve SPSS kabulü

17 Eylül 2026: Python ve R 4.3.3 ile **214** referans sonucu doğrulandı.
B07'nin 21 değeri de ayrıca doğrulandı ve eksik öğrenci sayfası eklendi.
B08–B14 için 214 SPSS sayısal kontrolünün geçtiği kullanıcı konsol görüntülerinde görüldü.
[SPSS kabul kaydı](spss-kullanici-kabulu.json). Ham JSON/CSV ve tam SPV dosyaları
bu kayıt için teslim alınmadı; ekran görüntüsü kapsamı ile tam çıktı incelemesi ayrıdır.

| Bölüm | Konu | Python/R eşleşen değer | IBM SPSS |
|---|---|---:|---|
| B08 | Güven aralıkları | 19 | Kullanıcı ekranında geçti |
| B09 | Hipotez testleri | 20 | Kullanıcı ekranında geçti |
| B10 | Hata, güç, tek örneklem t | 30 | Kullanıcı ekranında geçti |
| B11 | Bağımsız ve eşleştirilmiş t | 34 | Kullanıcı ekranında geçti |
| B12 | Kategorik veriler, ki-kare | 32 | Kullanıcı ekranında geçti |
| B13 | Korelasyon, basit regresyon | 62 | Kullanıcı ekranında geçti |
| B14 | Genel sınava hazırlık | 17 | Kullanıcı ekranında geçti |

## Yeniden çalıştırma

Depo kökünde Python, NumPy, pandas, SciPy, Matplotlib ve Rscript hazırken:

```bash
python code/dogrula_b08_b14.py --rapor dogrulama/yeni-sonuc.json
python code/atolye_kontrol.py
```

Betikler kaynak veriyi değiştirmez. Grafikler ve olumsuz testler geçici klasörde çalışır.
Python/R sonuçları ayrı hesaplanıp doğrudan karşılaştırılır. Bozuk referans ve eksik
veri iki yorumlayıcıda da reddedilir. R 4.3.3 standart paketleri yeterlidir.
[Çalıştırma günlüğü](python-r-2026-09-17.json) yazılım sürümlerini, kaynak hash'lerini,
standart çıktı/hata metinlerini ve iki yazılımın ayrı sonuç tablolarını içerir.

GitHub Actions aynı denetimi yeniden çalıştırır; gerçek CI günlüğü iş akışının
`python-r-dogrulama` çıktısında saklanır. CI, IBM SPSS çalıştırmaz.

## IBM SPSS 29 — tamamlanan kontrolü yeniden çalıştırma

1. Atölyeden bölüm ZIP'ini indirin ve tamamen ayıklayın.
2. SPSS çalışma klasörünü paketin `b08/ornek-01` (veya ilgili bölüm) klasörü yapın.
3. `spss-dogrula.sps` dosyasının tamamını çalıştırın.
4. Aynı klasörde `py spss_karsilastir.py --surum 29 --rapor spss-sonuc.json` çalıştırın.
5. JSON, dışa aktarılan CSV ve SPV/PDF dosyalarını birlikte inceleyin.

Her paketteki `SPSS-KONTROL.md` bölümün ayrıntılarını açıklar. Sayısal karşılaştırıcı
uydurulmuş test CSV'leriyle sınandı: doğru değer kabulü, değiştirilmiş değer ve eksik
çıktı reddi. Bu, IBM SPSS'in çalıştırıldığı anlamına gelmez. CSV kökeni ve SPV uyarıları
manuel inceleme gerektirir. B13'te SPSS REGRESSION yordamının tahmin/artıkları ayrıca
formül sonuçlarıyla karşılaştırılır. Ortak hedefler düzeltilmemiştir; yalnız eksik
SPSS uzantıları ve özgün manifestlerin öngördüğü satır sonları geri getirildi.

## Kapsam

Mevcut GitHub/QR adresi ve B01–B06 sayfaları korunur. B07–B14 öğretim örnekleri
veya özet istatistiklerdir; yeni gerçek veri üretildiği iddia edilmez. Kitabın Prism
kaynağı/PDF'si bu depoda olmadığı için değiştirilmedi. Özetlerden ham gözlem üretilmez.
Eski doğrulama belgeleri tarihsel olarak korunur; güncel kayıt ayrı gösterilir.
