# B05 — 2.000 tekrarlı ampirik benzetim testi V1

15 Eylül 2026. Bu paket, tamamladığınız 10.000 tekrarlı üstel öğretim
örneğinden ayrıdır. Eski `b05/ornek-01` klasörüne dosya kopyalamayın.
Site veya GitHub aktarımı değildir.

## Paketi açma ve ilk kontrol

Güncel `B05-HAZIRLIK-PLANI.md` dosyasını indirin. Bulunduğu klasörde
PowerShell açın ve çalıştırın:

```powershell
py B05-HAZIRLIK-PLANI.md --benzetim
```

Yanında `b05-benzetim-test-v1.zip` oluşur. Tamamını yeni bir klasöre
ayıklayın. İçindeki `b05-benzetim` klasöründe `kontrol.py`, `README.md`
ve `companion` yan yanadır. **Bu klasörde** PowerShell açıp çalıştırın:

```powershell
py kontrol.py
```

Beklenen son mesaj: `DOGRULANDI: 2000 tekrar; 33 kontrol degeri eslesiyor.`
Bu kontrol ek Python paketi istemez. Dosya hash'lerini, tekrar numaralarını,
altı sütunun beşer özetini, üç kapsama değerini ve standartlaştırmayı
denetler. Kaynak CSV'yi değiştirmez veya yeni benzetim verisi üretmez.
Manifestteki dosyaları değiştirmeyin; günlükleri başka adlarla saklayın.

## Python analizi ve grafik

Aynı klasörde:

```powershell
py companion/spss/python/b05.py
```

Bu özgün betik NumPy, pandas, SciPy ve Matplotlib gerektirir; otomatik
kurulum yapmaz. `--check` veya `--grafik` seçeneği yoktur. Özetleri
yazdırır ve iki histogram gösterir. Grafik penceresini kapatınca terminale
döner. Grafik penceresinin kaydet düğmesiyle resmi saklayabilirsiniz.

## R analizi ve grafik

R veya RStudio **konsolunda** aşağıdakileri çalıştırın. Dosya seçme
penceresinde bu paketin `b05-benzetim` klasöründeki `README.md` dosyasını
seçin; öğretim paketinin README dosyasını seçmeyin.

```r
dosya <- file.choose()
setwd(dirname(dosya))
options(digits = 12)
source("companion/spss/r/b05.R")
sessionInfo()
```

Ek R paketi gerekmez. Grafik R grafik penceresinde veya RStudio Plots
panelinde görünür. Çıktı ve grafiği paylaşın. Eski öğretim örneğindeki
`cozum.R --check --grafik` komutu bu uygulamaya ait değildir.

## SPSS

Açık çalışmalarınızı kaydedin. Yeni Syntax penceresinde aşağıdaki yer
tutucuyu **README.md ve companion'ın bulunduğu b05-benzetim klasörünün
tam yolu** ile değiştirip bu tek satırı çalıştırın:

```spss
CD 'BURAYA_B05_BENZETIM_KLASORUNUN_TAM_YOLU'.
```

Yalnız yolun başında ve sonunda birer tek tırnak olsun; OneDrive veya
boşluk içeren klasör adlarının çevresine ayrıca tırnak koymayın.
Yolun sonuna `companion` veya dosya adı eklemeyin.

File → Open → Syntax ile `companion/spss/syntax/b05.sps` dosyasını açın.
**Run → All** ile tümünü çalıştırın. CD satırını bu özgün dosyaya kaydetmek
yerine ayrı Syntax penceresinde tutun; böylece manifest hash'i korunur.
Çıktıyı `B05-benzetim-SPSS.spv` adıyla saklayın. Betik dört değişken için
betimsel tablo, z5/z100 histogramları ve kapsama frekanslarını verir.
SPSS komutları kitaptaki bloktan değiştirilmeden alınmıştır; bu yeni
paket henüz kullanıcı ortamında SPSS ile doğrulanmış değildir.

## Beklenen değerler ve kapsam

Her sütunda 2.000 tekrar vardır. Standart sapmalar tekrarlar üzerinde
`n-1` böleniyle hesaplanır. Tam hassasiyetli altı sütun referansları
`beklenen-sonuclar.csv` içindedir.

| Değişken | Ortalama | Örneklem standart sapması |
|---|---:|---:|
| ort5 | 10.3678000000 | 2.0788564121 |
| ort30 | 10.4190500000 | 0.8445122380 |
| ort100 | 10.4152500000 | 0.4589141953 |
| z5 | -0.0231589432 | 1.0159157226 |
| z100 | 0.0001314059 | 1.0029509123 |

`ABS(z100)<=1.96`: içeride **1.892 (%94,6)**, dışarıda **108 (%5,4)**.
Bu, mevcut benzetimin sonucudur; genel bir kapsama garantisi değildir.
Grafiklerin dilimler ve görsel ayarları yazılımlar arasında aynı değildir;
piksel eşitliği beklenmez. Sayısal karşılaştırma aynı hazır CSV'ye dayanır.

Kaynak, 395 öğrencinin matematik G3 notlarının ampirik dağılımıdır;
sıfır notlu 38 kayıt korunmuştur. Ampirik ortalama 10.415189873417722,
N bölenli sigma 4.57563964146053'tür. Kuramsal standart hatalar n=5,30,100
için 2.046288255769702, 0.8353936822142609, 0.457563964146053'tür.
Tohum 2026 ile geri koymalı 2.000×100 çekim yapılmıştır. Aynı satırdaki
ort5/ort30/ort100 ilk 5/30/100 çekimden gelir: **iç içedir ve bağımsız
üç örneklem değildir**. Satırlar yeni öğrenci kayıtları değildir.
Ham öğrenci verisi pakete eklenmez; kaynak hash'leri üretim kaydındadır.

Yerel Python denetimi ile eski Python/R günlükleri karşılaştırılmıştır.
Eski günlükler yeni test paketinin R/SPSS kabulü sayılmaz. Önce
`py kontrol.py` sonucunu paylaşın; ardından analiz ve grafiklere geçelim.
