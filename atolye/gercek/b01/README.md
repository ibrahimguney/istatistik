# B01 · Gerçek veri çalışma paketi

Bu paket 395 matematik öğrenci kaydını kapsar; beş yapay kayıtlı başlangıç
örneği değildir. Analiz bir satırı bir öğrenci kaydı olarak ele alır.
İki okul için betimleme yapılır; rastgele örnekleme, bağımsızlık veya
nedensel etki buradan doğrulanmaz. Bu yerel önizleme GitHub'a gönderilmedi.

## Çalıştırma

ZIP'i çıkarın. Çalışma dizinini bu README'nin bulunduğu `b01-gercek`
klasörü yapın. `companion` alt klasörünü taşımayın. Bu paket kitap
projesi olmadan çalışacak biçimde hazırlanmıştır.

- Python: `python dogrula.py` (Python 3, pandas, numpy ve scipy gerekir).
  Kitaptaki Python kodu gerçekten çalıştırılır; ham veri eşleştirmesi,
  Excel'in veri hücreleri, 20 betimsel değer, dört frekans ve 10 eksik
  değer sütunu kontrol edilir. JSON standart çıktıya yazılır.
- Yalnız kitap Python kodu: `python companion/spss/python/b01.py`.
- R: `Rscript companion/spss/r/b01.R` (temel R yeterlidir).
- SPSS: önce açık çalışmanızı kaydedin; çalışma dizinini paket köküne
  ayarlayın. `companion/spss/syntax/b01.sps` dosyasını Syntax penceresinde
  açıp tamamını çalıştırın. CSV açma dosyası otomatik çağrılır.
  Etkin veri, filtre/ağırlık/bölme ayarları değişir; `sav/b01.sav` yazılır.
  Önceden aynı adlı SAV varsa üzerine yazılabilir; ayrı kopyada çalışın.
- Excel alternatifi: `companion/spss/syntax/open-b01-excel.sps` yalnız
  veriyi açıp SAV yazar. Sonra `DISPLAY DICTIONARY`, `FREQUENCIES` ve
  `DESCRIPTIVES` analiz komutlarını uygulayın. `b01.sps` bütünü yeniden
  çalıştırılırsa CSV tekrar açılır; Excel içe aktarımını sınamış olmazsınız.

## Çıktıyı karşılaştırma

`ciktilar/python/` bu teslimde gerçekten çalıştırılmış Python çıktısıdır.
`betimsel.csv` içindeki `std`, n−1 paydalı örneklem standart sapmasıdır.
`frekans.csv` yüzdeleri 395 kayıt üzerinden hesaplanır. R/SPSS tablolarını
aynı değişkenler ve özetlerle karşılaştırın; yuvarlama basamaklarını belirtin.
R/SPSS bu yeni paketle burada çalıştırılmadı; `.spv` veya R çıktısı üretilmedi.
Kitapta 12 Eylül tarihli paylaşılan çıktı karşılaştırması anlatılır; o kayıt
bu yeni dağıtımın yeniden çalıştırma onayı olarak kullanılmaz.

## Kaynak ve uyarlama

Cortez, P. (2008). Student Performance [Dataset]. UCI Machine Learning
Repository. DOI: 10.24432/C5TG7T.

- Kaynak: https://archive.ics.uci.edu/dataset/320/student+performance
- Veri lisansı: CC BY 4.0, https://creativecommons.org/licenses/by/4.0/
- Resmî sayfa kontrol tarihi: 13 Eylül 2026.

UCI iki Portekiz okulunun okul kayıtları ve anketlerinden elde edilen
matematik ve Portekizce dosyalarını ayrı sunar. Burada yalnız yerel
`student-mat.csv` kullanılır; sayfadaki 649 kayıt bilgisi bu matematik
dosyasının boyutu olarak alınmaz. Ham dosya yeniden indirilmedi; yerel
kopyanın hash'i ve GitHub ZIP'iyle eşleşmesi üretim kaydında tutulur.

Uyarlama: sekiz kaynak sütunu seçildi; GP/MS ve F/M açık kodlarla dönüştürüldü;
not adları küçük harfe çevrildi; yerel `id` ve öğretim amaçlı `pass10`
eklendi. 395 satırın tamamı ve sıfır notlar korundu. `id` özgün kişi kimliği
değildir; başka ders dosyasıyla eşleştirme anahtarı değildir.
`studytime` saat değil sıralı kategoridir; `absences` için gün/saat varsayılmaz.
Kaynak kategori sınırları yeniden yorumlanmadan sözlüğe aktarılmıştır.
`pass10` kurumun gerçek geçme kararının kanıtı değildir.

Veri atfını, lisans bağlantısını ve uyarlama bilgisini türevlerde koruyun.
Bu veri lisansı kitabın metnine veya bütün kodlara yeni bir lisans atamaz.
Üretim SHA-256 kayıtları `KAYNAK.json`, bu yeni paketin dosya listesi
`manifest.json` içindedir. Eski proje manifestleri değiştirilmedi.
