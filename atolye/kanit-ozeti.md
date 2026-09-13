# B01 gerçek veri — yazılımlar arası karşılaştırma

Kontrol tarihi: 13 Eylül 2026. Kapsam: 395 matematik öğrenci kaydının
betimlenmesi; beş yapay kayıtlı uygulama ve diğer bölümler kapsam dışıdır.

| Yazılım | Kanıt | Sonuç |
| --- | --- | --- |
| Python | V3 paketinin kayıtlı çalıştırması ve bağımsız sayısal kontrolü | 20 betimsel değer, dört frekans ve eksik değer kontrolleri geçti |
| R | Kullanıcının R Console görüntüsü; R 4.6.1, Windows 11 x64 | 20 özet değer altı ondalık düzeyinde, dört frekans ve on sütunun eksik sayıları Python ile eşleşti |
| SPSS | Kullanıcının tablo görüntüsü ve yüklediği SPV | Gösterilen N, minimum, maksimum, ortalama, standart sapma ve frekanslar gösterim hassasiyetinde Python ile eşleşti |

R ve SPSS kullanıcı bilgisayarında çalıştırıldı; yayın hazırlama ortamında
yeniden çalıştırılmış gibi sunulmaz. SPV'nin CRC kontrolü ve XML başlıkları
incelendi; ikili tablo hücreleri tam çözümlenmedi. SPSS sayısal karşılaştırması
görüntüye dayanır. SPV sürüm alanı `32000000`; tam ürün/yama sürümü ayrıca
doğrulanmadı. R sürümü görüntüdeki `sessionInfo()` beyanıdır.

| Ölçü | age | g1 | g2 | g3 |
| --- | ---: | ---: | ---: | ---: |
| N | 395 | 395 | 395 | 395 |
| Ortalama | 16.696203 | 10.908861 | 10.713924 | 10.415190 |
| Örneklem standart sapması | 1.276043 | 3.319195 | 3.761505 | 4.581443 |
| Minimum | 15 | 3 | 0 | 0 |
| Maksimum | 22 | 19 | 19 | 20 |

Frekanslar GP=349, MS=46, F=208, M=187. R ve Python'da on sütunda
eksik sayı sıfır; SPSS görüntüsünde okul/cinsiyet eksik sayıları sıfırdır.

Kullanıcı çalıştırmalarının CSV/kod hashleri görüntülerden doğrulanmadı.
Tam R metin günlüğü yoktur. Excel'in SPSS'e aktarımı sınanmadı. Sayısal
uyum temsil, nedensellik veya öğrenme etkisi kanıtı değildir.

## Kanıtların kimliği ve dağıtım sınırı

- R görüntüsü: `image_96.png`; SPSS görüntüsü: `image_95.png`.
- Yüklenen çıktı: `b01-spss-sonuc.spv`, 13.193 bayt;
  SHA-256 `e17e2e288b2ebdcfa78faaa68d1c398d73e2dd7799d4e7630e0b848086b5c15e`.
- Bu dosyalar yerel denetim kanıtlarıdır; görüntüler ve yerel dosya yolu
  içeren SPV, bu halka açık aktarım adayına eklenmedi.

İndirilen analiz ZIP'leri V3 ile bayt düzeyinde aynıdır. İçlerindeki
R/SPSS çalıştırılmadı kayıtları ilk üretim aşamasına aittir; 13 Eylül
kullanıcı karşılaştırması bu ayrı özetle izlenir. Python çıktı dosyaları
R/SPSS çıktısı olarak yeniden adlandırılmadı. Yeni lisans atanmadı.
