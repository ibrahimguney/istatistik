# B12 SPSS dışa aktarım düzeltmesi — V2

Kullanıcının IBM SPSS 29 ekranında Pearson ki-kare = 5,3333333333,
p = 0,0209213353, Cramér V = 0,2581988897 ve N = 80 görüldü.
Ardından `FORMATS` komutunda `alfa` değişkeni bulunamadı (hata 4820).
`ERROR=STOP` akışı durdurduğu için `spss-ozet.csv` oluşmadı; Python
karşılaştırıcısı eksik dosyayı doğru biçimde başarısız saydı.

V2 `spss-dogrula.sps`, aynı analiz hesaplarını tek dosyada yürütür.
Dört hücre henüz aktifken `spss-satirlar.csv` yazılır. Sonra AGGREGATE ve
mevcut COMPUTE hesapları ile tek özet satırı oluşturulup `spss-ozet.csv`
yazılır. Dışa aktarımda iç içe INSERT ve iki veri seti arasında geri dönüş
kullanılmaz. Referans değerler ve karşılaştırma toleransları değiştirilmedi.

Güncel ZIP'i yeni bir klasöre ayıklayın veya güncel `spss-dogrula.sps`
dosyasını mevcut `ornek-01` klasöründeki aynı adlı dosyanın yerine koyun.
V2'nin ilk satırında `B12 disari aktarim v2` yazmalıdır.
SPSS'te çalışma klasörünü ayarlayıp dosyanın tamamını yeniden çalıştırın.
Ardından `py spss_karsilastir.py --surum 29 --rapor spss-sonuc.json` çalıştırın.

V2 IBM SPSS'te bu ortamda çalıştırılmadı; kullanıcıdaki tekrar ve
`GECTI: 32 kontrol` sonucu bekleniyor. Eski Python/R günlüğü o tarihteki
kaynak hash'lerini içerir; V2 syntax için bir SPSS çalışma kanıtı değildir.
