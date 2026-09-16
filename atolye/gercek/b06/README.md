# B06 gerçek veri — ayrı test V1 (15 Eylül 2026)

395 kayıtlı uygulamadır; 12 kişilik öğretim paketi değildir.
Canlı site veya Git aktarım paketi değildir. Depoya kopyalamayın.
Seçimleri yeniden üretmeyin. Kaynak ve kodlamalar: KAYNAK.md.

## İlk analiz: Python

ZIP'i tamamen ayıklayın. Bu README ile companion klasörünü birlikte
gördüğünüz b06-gercek-test-v1 klasöründe PowerShell açın:

    py companion/spss/python/b06.py

NumPy ve pandas gerekir. Hata olursa paket kurmadan hata metnini paylaşın.
Özgün betikte --check seçeneği yoktur. Veri boyutu, eksiksizlik ve iki
örneklem büyüklüğü assert ile denetlenir; sonra sonuçlar yazdırılır.
29 otomatik kontrol ifadesi bu pakete değil, öğretim paketine aittir.

Beklenen değerler (eski kullanıcı Python/R çıktılarındaki değerler):

| Ölçü | Tam dosya | Basit rastgele |
|---|---:|---:|
| Kayıt sayısı | 395 | 40 |
| G3 ortalaması | 10.41518987342 | 10.27500000000 |
| G3 örneklem standart sapması | 4.58144261100 | 5.56540366449 |

Tabakalı seçim: GP=35, MS=5; %87,5 ve %12,5.
Gerçek örneklem büyüklüğü 40; ağırlık toplamı 395;
ağırlıklı G3 ortalaması 10.45634719711. Ekran yuvarlaması farklı olabilir.
Python çıktısını paylaşın; R ve SPSS sonraki ayrı adımlardır.

## Sonraki adımlar

Çalışma klasörü her yazılımda bu README ile companion klasörünü içeren
paket köküdür; analiz betiğinin bulunduğu alt klasör değildir.
Doğru çalışma klasörü ayarlandıktan sonra R konsolunda:

    source("companion/spss/r/b06.R")

SPSS dosyası: companion/spss/syntax/b06.sps.
Açık çalışmalarınızı kaydedin. Çalışma klasörü ayarlandıktan sonra baştan
çalıştırılır. Filtre ve ağırlık başlangıçta ve sonda kapatılır.
Bu teslim R/SPSS'in yeni ortamda çalıştırıldığı iddiası taşımaz; SAV/SPV yoktur.

## Kanıt sınırı ve bütünlük

395 kayıt yalnız bu uygulamanın sonlu çerçevesidir. Seçim göstergeleri
öğretim amaçlıdır; kaynak araştırmanın özgün örnekleme tasarımı değildir.
Ağırlık toplamı örneklem büyüklüğü değildir. Ağırlıklı ortalama, tasarıma
uygun standart hata veya güven aralığı denetimi değildir. Tek bir seçim,
yöntem üstünlüğünü veya daha geniş evrene genellenebilirliği kanıtlamaz.

CSV ve üç analiz dosyası mevcut companion/spss/manifest.csv değerleriyle
birebir doğrulandı. Python/R'nin eksik son LF baytı yalnız özgün hash ile
birebir eşleşen biçimde bellekte tamamlandı. SPSS bloğu kitap kaynağından
alındı ve özgün syntax/b06.sps hash'iyle eşleşti. Kaynaklar değiştirilmedi.
MANIFEST.json yalnız bu yeni test teslimine aittir; eski manifestlerin
yerine geçmez. Üretici ZIP ve altı içerik dosyasının hash'ini denetler.
