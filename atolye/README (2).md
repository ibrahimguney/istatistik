# B04 — gerçek veriye dayalı benzetim testi V1

14 Eylül 2026. Bu paket küçük {2,4,6,8} öğretim örneği değildir.
B01/B02/B03'teki 395 öğrencinin matematik notlarının ampirik dağılımından
geri koymalı çekimlerle hazırlanmış **2000 tekrar** içerir. Yeni öğrenci
verisi toplanmamıştır. Kaynak notları sıfır olan 38 kayıt üretim evreninde
korunmuştur. Ham öğrenci dosyası bu test paketinde dağıtılmaz ve çalıştırma
bağımlılığı değildir. Kaynak ve dönüşüm ayrıntıları `KAYNAK.md` ve
`URETIM-KAYDI.json` içindedir.

## 1. Üretin ve tamamını çıkarın

Bilgisayarınıza indirdiğiniz `B04-BENZETIM-TEST-OLUSTUR.py.txt` dosyasının
bulunduğu klasörde terminal açın:

```powershell
py B04-BENZETIM-TEST-OLUSTUR.py.txt
```

Tek dosyalık üretici internet/ek paket istemez; analiz veya rastgele
çekim çalıştırmaz. Yanında `b04-benzetim-test-v1.zip` oluşturur.
Aynı çıktıyı korur, farklı mevcut çıktı varsa durur. Böyle bir durumda
üreticiyi yeni bir klasörde çalıştırın; mevcut dosyayı silmeniz gerekmez.

ZIP'in tamamını yeni bir klasöre çıkarın. İçindeki **`b04-benzetim`**
klasörü çalışma köküdür: `README.md`, `kontrol.py` ve `companion` burada
yan yana bulunur. 12 dosyalık bu paket site veya GitHub aktarımı değildir.
Küçük örneğin `b04/ornek-01` klasörünü burada kullanmayın.

## 2. Önce bütünlük ve sayısal kontrol

`b04-benzetim` klasöründe terminal açın:

```powershell
py kontrol.py
```

Bu yeni kontrol aracı yalnız standart Python kütüphanesini kullanır.
Manifestteki dosyaları, sabit CSV hash'ini, sütunları, 2000 satırı,
1–2000 tekrar numaralarını ve aşağıdaki **10 özeti** kontrol eder.
Beklenen mesaj: `DOGRULANDI: 2000 tekrar; 10 betimsel deger eslesiyor.`
Bu, küçük örneğin 28 değerlik kontrolünden ayrıdır. Manifestte listelenen
dosyaları değiştirmeyin. Ek ekran görüntüsü/günlükler kapsam dışında kalır.

## 3. Özgün Python analizi ve grafik

Aynı çalışma kökünde:

```powershell
py companion/spss/python/b04.py
```

NumPy, pandas, SciPy ve Matplotlib gereklidir. Betik paket kurmaz.
Bu özgün analizde `--check` veya `--grafik` seçeneği yoktur: özetleri
yazdırır, iki histogramı bir grafik penceresinde gösterir. Kaydetmek
isterseniz pencerenin kaydet düğmesini kullanın. Özetleri ve grafiği
paylaşın. Pencereyi kapatınca terminal komut satırına döner.

## 4. R

R konsolunda aşağıdaki ilk komutla dosya seçme penceresini açın.
**Bu paketin kökündeki `README.md` dosyasını seçin**, sonra devam edin:

```r
dosya <- file.choose()
setwd(dirname(dosya))
options(digits = 12)
source("companion/spss/r/b04.R")
sessionInfo()
```

R standart kütüphanesi yeterlidir. Grafik R'nin grafik penceresinde veya
RStudio Plots panelinde görünür; otomatik PNG kaydı yoktur. Çıktıyı ve
grafiği paylaşın. Burada `kontrol_et(sonuc, ...)` kullanılmaz; o fonksiyon
yalnız küçük öğretim örneğine aittir. R özetlerini aşağıdaki tabloyla
karşılaştırın; `kontrol.py` çalışması R'nin çalıştığını kanıtlamaz.

## 5. SPSS

Açık çalışmalarınızı kaydedin; tercihen ayrı oturum açın. Dosya Gezgini'nde
`companion` klasörünü içeren **`b04-benzetim` klasörünün yolunu** kopyalayın.
Yeni Syntax penceresinde aşağıdaki yer tutucuyu o yolla değiştirin:

```spss
CD 'BURAYA_B04_BENZETIM_KLASORUNUN_TAM_YOLU'.
```

Yolun sonuna `b04.sps` eklemeyin. Tek tırnakları ve son noktayı koruyup
CD satırını seçerek çalıştırın. Ardından File → Open → Syntax ile
`companion/spss/syntax/b04.sps` dosyasını açın; çok satırlı `GET DATA`
kodunu gördüğünüzde Run → All ile tamamını çalıştırın.
`.sps.txt` aynı içerikli yedektir. Kod hazır CSV'yi doğrudan okur;
B01 SAV dosyası veya `open-b01.sps` gerekmez. Etkin veri kümesi,
ondalık, filtre, ağırlık ve bölme ayarları değişir.

Descriptive Statistics tablosunda her iki değişken için **N=2000** ve
aşağıdaki özetler beklenir. İki histogramı, tabloyu ve varsa uyarıları
paylaşın; mümkünse tam çıktı günlüğünü ve SPSS sürümünü de saklayın.

## Beklenen özetler

| Ölçü | ort5 | ort30 |
| --- | ---: | ---: |
| Tekrar sayısı | 2000 | 2000 |
| Ortalama | 10,36780000000 | 10,41905000000 |
| Örneklem standart sapması | 2,07885641207 | 0,84451223803 |
| Minimum | 2,80000000000 | 7,36666666667 |
| Maksimum | 16,20000000000 | 13,00000000000 |

Kontrol toleransı mutlak 1e-9'dur. SPSS'in gösterdiği ondalık basamaklara
yuvarlayarak karşılaştırın. SS hesabının böleni 1999'dur; küçük örneğin
tam dağılım varyansındaki 16 böleni burada kullanılmaz.

## Grafik ve yorum sınırları

- `ort30` dağılımı `ort5` dağılımından daha dar; merkezler yaklaşık 10,4
  civarında beklenir. Bunlar bireysel notlar değil tekrar ortalamalarıdır.
- Python/R histogramları yoğunluk, SPSS histogramları frekans ölçeğindedir.
  Python/R sınıf genişliği 0,5 ve yatay aralık 0–20 olsa da sınırdaki
  değerlerin sınıfa atanma kuralları farklı olabilir. Piksel eşitliği
  veya bütün sütun yüksekliklerinin eşitliği beklenmez.
- Çizilen normal eğri, o sütunun örneklem ortalaması ve SS'siyle görsel
  karşılaştırmadır; normallik testi veya kuramsal dağılım kanıtı değildir.
- Tekrardaki ilk 5 ve ilk 30 çekim aynı 100 çekimlik diziden gelir;
  iki sütun bağımsız gruplar olarak test edilmez. Tüm yazılımlar aynı
  hazır CSV'yi okur; tohum eşitleme veya yeniden benzetim gerekmiyor.

Önceki R/Python metinleri tarihsel karşılaştırmadır; bu teslimin yeni
R/SPSS çalışması sayılmaz. Küçük örneğin kullanıcı kontrolleri de bu
uygulamanın yerine geçmez. Bu paket B04 yayın kabulü değildir.
