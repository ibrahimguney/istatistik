# B05 V1 — sınırlı aktarım kapsamı (15 Eylül 2026)

Kabul edilen V3 önizlemesi, yayımlanmış B04 V1 tabanına uyarlanmıştır.
35 yeni dosya eklenir; yalnız index.html ve yayin-manifest.json güncellenir.
Silme yoktur. Birleşmiş site 185 dosyadır; sınırlı ZIP 37 dosyadır.
B04 sayfaları, yayın etiketleri, eski belgeler, CSS ve sekiz eski indirme
bayt düzeyinde korunur. Ana sayfanın eski içeriğine yalnız B05 bölümü eklenir.
B05'in iki sayfasında V3 önizleme etiketi V1 olur; bu canlı kabul değildir.
Beş SVG, tablolar, veri/kod dosyaları ve iki indirme kabul edilen V3 ile aynıdır.

Kullanıcı tablolar ve indirmeler için onay verdi. Evdeki depo ekranında
e070b99 ve temiz çalışma ağacı görüldü; manifest B04 V1 ile eşleşti.
Bu ekran kaydı uzak deponun güncel durumunun sorgulandığı anlamına gelmez.
Üretici ayrıca yerel 150 dosyanın tamamını manifestle denetler.
R/SPSS yeniden çalıştırılmaz; yeni sayısal veya canlı yayın kabulü yoktur.

Sınırlı ZIP tek başına site değildir. Depoya henüz kopyalamayın;
önce teslim çıktısını paylaşın. Tam V3 önizlemesi depoya aktarılmamalıdır.
Eski B04 belgeleri tarihsel olarak korunur; güncel B05 kapsamı bu başlıktır.
Üretici mevcut depoyu yalnız okur; commit/push veya ağ bağlantısı yapmaz.
Aşağıdaki V3 rehberi tarihsel önizleme kaydıdır, yeni aktarım talimatı değildir.

---

# B05 küçük önizleme V3 — 15 Eylül 2026

ZIP'in tamamını ayıklayın; istatistik-b05-onizleme/index.html açın.
İki B05 sayfası, beş grafik, iki B05 indirmesi ve B01–B04 bağlantılarını
kontrol edin. Görünüm kullanıcı kabulünü bekler; canlı yayın değildir.

## Taban ve kapsam

Taban, kullanıcının yüklediği özgün B04 ÖNİZLEME ZIP'idir; canlı sitenin
güncel kopyası değildir. B04'ün sayfaları ve tarihsel önizleme etiketleri
bilerek aynen korunur. Bunlar B04'ün daha sonraki canlı kabulünü geri almaz.
Eski ONIZLEME.md/YAYIN-DURUMU.md belgeleri de tarihsel kayıtlardır.
150 taban dosyasından yalnız index.html ve genel manifest değişir;
35 yeni dosya eklenir, silme yapılmaz. 185 dosya, 11 HTML sayfası ve
10 indirme ZIP'i vardır. Önceki sekiz indirme ve CSS bayt düzeyinde korunur.
Bu tam yerel önizlemedir; GitHub'a doğrudan yüklemeyin. Yayın için daha
sonra gerçek yerel depo tabanı ayrıca denetlenerek sınırlı aktarım gerekir.

## İki ayrı test

Öğretim: üstel evren, 10.000 tekrar, n=1/5/30; satırdaki örneklemler
bağımsızdır. ZIP'i ayıklayın; b05/ornek-01 içinde py cozum.py --check:
24 kontrol değeri beklenir. Özgün 15 dosya ve başlangıç rehberi korunur.

Ampirik: 395 G3 notu, 2.000 tekrar; satırdaki n=5/30/100 ortalamaları
iç içedir, bağımsız değildir. ZIP'i ayıklayın; b05-benzetim içinde
py kontrol.py: 33 kontrol değeri beklenir. |z100|<=1,96: 1892/2000=%94,6.
Bu benzetim sonucu bütün örneklemler için garanti değildir.
Özgün 10 dosya korunur; ham öğrenci verisi dağıtılmaz.

## Kanıt ve sınırlar

Öğretim: image_171 Python 24 kontrol; image_175–176 R 24 kontrol;
image_177 R grafikleri; image_180–183 SPSS grafik ve gösterilen 24 değer.
Ampirik: image_184 Python 33 kontrol; image_185–188 Python/R çıktı ve
grafikleri; image_191–194 SPSS özetleri ve 1892/108 kapsaması.
image_189–190 önceki yol hatalarıdır; başarı kanıtı olarak kullanılmaz.
Bu adlar projedeki ekran görüntülerine ait kayıt referanslarıdır;
kişisel yerel yollar içeren görüntüler dağıtımın içine konmaz.
Yeni otomatik SPSS denetimi veya .spv dosyası incelemesi iddiası yoktur.
Özgün paketlerdeki eski üretim kayıtları değiştirilmez; kullanıcı kabulü
daha sonraki, ayrı kayıttır. Üretici R/SPSS çalıştırmaz, veri üretmez.
Beş SVG hazır CSV'den çizilir; R/SPSS ekran çıktısı değildir.
SPSS frekans ve Python/R yoğunluk eksenlerini aynı ölçek sanmayın.
Kitap, eski üreticiler ve canlı site değiştirilmez; ağ bağlantısı kurulmaz.

## Önceki teslim sorunu

image_195–196 ekranlarında eski hazırlık planı --onizleme/--surum
seçeneklerini tanımıyordu. Büyük gömülü önizleme mevcut proje kopyasında
bulunamadı; nedeni bilinmiyor. V3, üç hazır ZIP'i okuyan küçük ayrı
üreticidir; önceki v1/r2 ile aynı çıktı hash'i iddiası yoktur.
