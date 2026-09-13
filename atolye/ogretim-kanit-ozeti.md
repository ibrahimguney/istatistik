# Beş yapay kayıtlı B01 — kullanıcı kanıtı özeti

13 Eylül 2026; V4.2 sunum güncellemesi. Bu kayıt yalnız beş yapay
kayıtlı öğretim örneğine aittir. 395 kayıtlı uygulamanın ayrı
[kanıt özeti](kanit-ozeti.md) bunun yerine geçmez.

## R — kullanıcı konsolu, 18:23:43 UTC

Paylaşılan karşılaştırma bloğu hata vermeden tamamlandı ve
`DOGRULANDI: 18 kontrol degeri eslesiyor.` mesajı görüldü.
Blok, hesaplanan ve beklenen tabloların 18 satırını, değişken ve ölçü
adlarının aynı olduğunu ve sayısal değerleri `all.equal` ile
`tolerance = 1e-9, check.attributes = FALSE` kullanarak karşılaştırıyor.
Konsolda görülen son iki değer program B frekansı 2, oranı 0.4'tür.

Tam 18 satırlık tablo paylaşılmadı; kabul gösterilen kontrol bloğuna
dayanır. Bu bir R Console karşılaştırmasıdır; `Rscript --check`
çalıştırıldığı ileri sürülmez. Kaynak yankısındaki `[TRUNCATED]`
ifadesi hata değildir; sonraki açık karşılaştırma bloğu tam görünür.

Paylaşılan oturum bilgisi: R 4.6.1, Windows 11 x64 build 26200,
LC_NUMERIC=C. Ek namespace'ler yüklüdür; temiz oturum iddiası yoktur.
Kullanıcı veri/kod dosyalarının hashleri alınmadı. Burada R yeniden
çalıştırılmadı; kullanıcının ortamı bağımsız olarak doğrulanmadı.

## SPSS — kullanıcı ekran görüntüsü, 18:26:33 UTC

Etkin veri kümesi B01Ornek; devam_saati ve basari Scale, program Nominal.

| Alan | Görüntüde okunan ve beklenenle eşleşen değerler |
| --- | --- |
| Değişkenler | devam_saati, basari, program |
| Devam | N=5, minimum=7, maksimum=12, ortalama=9.20 |
| Başarı | N=5, minimum=64, maksimum=83, ortalama=72.40 |
| Program | Geçerli=5, eksik=0; A=3 (%60), B=2 (%40) |
| Listwise geçerli N | 5 |

Bu, gösterilen tabloların karşılaştırmasıdır; otomatik 18 satırlık SPSS
doğrulaması değildir. Tam komut/hata günlüğü, SPSS sürümü, kullanıcı
veri/kod hashleri ve bu küçük örneğe ait SPV alınmadı. Burada SPSS
yeniden çalıştırılmadı. Gerçek veri uygulamasının SPV'si kullanılmadı.

## Değişmeyenler ve kapsam

Python'un önceki 18 kontrol kaydı korunur. Veri, analiz kodları, CSS,
iki analiz indirme ZIP'i ve özgün manifestler değiştirilmedi. ZIP'lerdeki
eski R/SPSS bekliyor ifadeleri ilk üretim aşamasının tarihsel kayıtlarıdır;
bu belge sonraki kullanıcı kontrolünü açıklar, eski çıktıları yeniden
üretilmiş gibi sunmaz. Siteye ham konsol kaydı, SPV veya ekran görüntüsü
eklenmez. Bu eşleşme bilimsel genelleme, öğrenci pilotu veya öğrenme
etkisi kanıtı değildir; diğer bölümleri doğrulamaz.
