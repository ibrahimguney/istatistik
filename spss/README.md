# IMO301 — Literatür verisiyle SPSS uygulamaları

Ders sürümünün 14 bölümüne ait uygulama kodları b01–b14'tür. Kapsamlı
sürümde basılı bölüm numaraları değişse de uygulama kodları değişmez.
Kaynak matematik verisi tüm gözlemsel uygulamalarda ortaktır; dosyalar
14 farklı araştırmanın verileri veya 14 bağımsız örneklem değildir.

## Kaynak, lisans ve dönüşümler

Cortez, P. (2008). Student Performance [Dataset]. UCI Machine Learning
Repository. DOI: 10.24432/C5TG7T.
Kaynak: https://archive.ics.uci.edu/dataset/320/student+performance
Lisans: CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
Kaynak/lisans kontrol tarihi: 9 Eylül 2026.

Yüklenen student-mat.csv: 395 satır, 33 değişken. raw/student-mat.csv özgün
sütunları korur. Analiz dosyalarında seçilmiş sütunlar yeniden kodlanır;
yapay sıra numarası id ile öğretim amaçlı pass10=(g3>=10) eklenir.
Sıfır notlar korunur, boş hücre yoktur. school: GP=1/MS=2; sex: F=1/M=2.
studytime ordinaldir; 1–4 kodları saat sayıları değildir. absences için gün
veya saat birimi varsayılmamıştır. Tüm değişken tanımları Excel'in sozluk
sayfasındadır. Her çalışma kitabının kaynak sayfasında atıf/lisans vardır.
İki okulun gözlemsel verisinden genelleme/bağımsızlık/nedensellik sonucu
kendiliğinden çıkarılamaz. Testler bağımsız gözlemler modeliyle öğretim içindir.
İleride student-por.csv eklense bile bu paketin 14 uygulaması matematik
verisini kullanır; iki dosya id üzerinden birleştirilmez.

## SPSS'te çalıştırma

1. Paketi klasör düzeni korunacak biçimde açın. Çalışma dizini, depo kökü
   olmalıdır; doğrudan syntax klasörü değil.
2. SPSS Syntax penceresinde CD komutunu kendi proje klasörünüzü gösterecek
   şekilde çalıştırın. Komutta dizin adı tek tırnak içinde, sonunda nokta
   olmalıdır. Bilgisayara özel bir dizin bu pakete sabitlenmemiştir.
3. File > Open > Syntax ile syntax/b01.sps dosyasını açın; Run > All seçin.
4. INSERT komutu open-b01.sps'i çağırır. Excel'in veri sayfası açılır,
   etiket ve ölçme düzeyleri tanımlanır, sav/b01.sav kaydedilir, analiz yapılır.
5. Her uygulamaya kendi bXX.sps dosyasını baştan çalıştırarak başlayın.
   Bazı uygulamalarda SELECT IF veya AGGREGATE aktif veri yapısını değiştirir.
6. Oluşan SPSS çıktısını kendi bilgisayarınızda .spv olarak kaydedin.
   sav klasörü pakete dahildir; SAVE OUTFILE aynı adlı dosyayı günceller.

Burada IBM SPSS çalıştırılmamıştır: hazır .sav/.spv veya SPSS ekran görüntüsü
sunulmuyor. .sav dosyaları komutları SPSS'te çalıştırınca oluşur. Sayısal
kontrol değerleri bağımsız Python hesaplarıdır. XLSX ZIP/XML ve hücre kontrolü,
Excel ya da SPSS programında gerçek içe aktarma testinin yerine geçmez.
Güç analizi komutu POWER MEANS ONESAMPLE SPSS 27+ gerektirir; eski sürümlerde
b10.sps'in bu son komutunu atlayıp diğer hesapları çalıştırın.
Resmi sözdizimi kaynağı: IBM SPSS Statistics 31 Command Syntax Reference.
https://www.ibm.com/docs/en/SSLVMB_31.0.0/pdf/IBM_SPSS_Statistics_Command_Syntax_Reference.pdf

## Dosyalar

LaTeX derlemesinde bir `syntax/bXX.sps` dosyası eksikse kitap ilgili
komut listesinin yerine eksik dosya uyarısı basar ve derlemeye devam eder.
Komut listelerinin de basılması için özgün `.sps` dosyalarını
`spss/syntax` klasörüne ekleyip kitabı yeniden derleyin.

- excel/bXX.xlsx: veri, sozluk, kaynak sayfaları.
- csv/bXX.csv: aynı veri sayfasının taşınabilir kopyası.
- syntax/bXX.sps: bağımsız başlatılan analiz; open-bXX.sps: veri açma/kayıt.
- results/values.tex: kitabın kullandığı kontrol değerleri.
- results/checks.json: yuvarlanmamış değerler, sürümler ve kaynak SHA-256.
- chapter-map.csv: uygulama kodu, kaynak, satır ve değişken sayısı.
- manifest.csv: dosya bütünlüğü özetleri.

b04/b05: kaynak G3 dağılımından geri koymalı 2.000 benzetim; satırlar öğrenci
DEĞİL. PCG64 tohum 2026, 2000x100 çekim; ilk 5/30/100 notun ortalamaları.
Ampirik sigma N böleniyle hesaplanır. b06: 395 kayıtlık sonlu öğretim
çerçevesinden 40 basit rastgele ve 35 GP + 5 MS tabakalı seçim; WEIGHT BY
sadece ağırlıklı nokta tahminini gösterir, tasarım-temelli SE sağlamaz.
b10: ileriye dönük planlama farkı 1 puan, sigma=4.581442611, iki yönlü
alfa=.05, güç=.80; gözlenen etki üzerinden geriye dönük güç değildir.
b14: g3>0 alt grubunun incelemesi sadece duyarlılık analizi; sıfırları
silmenin doğru olduğu iddia edilmez.

## Yeniden üretim ve denetim

Proje kökünde, mevcut numpy/pandas/scipy ile:

    python spss/build_package.py
    python spss/validate_package.py

Betiği tekrar çalıştırmak üretilmiş Excel, CSV, SPSS ve sonuç dosyalarını
yeniler; öğrencilerin özgün yüklemesi değiştirilmez. Kitaptaki metinler
bu matematik veri sürümüne göre yazılmıştır. Başka veriyle değiştirmek
metinlerdeki bağlam ve sabit sayıların da yeniden incelenmesini gerektirir.