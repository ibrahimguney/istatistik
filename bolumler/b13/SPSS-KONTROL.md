# B13 — IBM SPSS 29 kontrolü

Bu paket SPSS'te henüz çalıştırılmadı. Kontrol için:

1. ZIP'i tamamen ayıklayın; açık SPSS çalışmalarınızı kaydedin.
2. Syntax penceresinde gerçek klasörünüze göre `CD 'C:/.../b13/ornek-01'.` çalıştırın.
   Syntax dosyasını açmak çalışma klasörünü otomatik değiştirmez.
3. `spss-dogrula.sps` dosyasının tamamını çalıştırın. `analiz.sps` içeri alınır;
   veri ve plan girdileri aynı klasörden okunur. Hata/uyarıları inceleyin.
4. `spss-ozet.csv` ve `spss-satirlar.csv` dosyası oluşur.
   Önceki dışa aktarımlar varsa üzerlerine yazılır; analiz kaynakları değişmez.
5. Aynı `ornek-01` klasöründe terminal açıp çalıştırın:

   ```bash
   py spss_karsilastir.py --surum 29 --rapor spss-sonuc.json
   ```

   Gerçek sürüm numaranızı yazın. Yalnız Python standart kitaplığı gerekir.
   Beklenen: **GECTI: 62 kontrol**. Hatalı/eksik dışa aktarım başarı sayılmaz.
   Yeni denemede yeni rapor adı verin; mevcut raporun üzerine yazılmaz.
6. SPSS Viewer çıktısını `b13-spss.spv` ve mümkünse PDF olarak kaydedin.
   SPV, JSON raporu ve dışa aktarılan CSV'leri birlikte inceleme için paylaşın.

Karşılaştırma bağıl 1e-8 ve mutlak 1e-14 tolerans kullanır; SPSS dışa aktarımı
16 ondalıklı bilimsel gösterimle yapılır. Görüntüde yuvarlatılmış değerleri CSV'ye elle yazmayın.
Çok küçük p değerleri sıfır kabul edilmez. SPSS sürümü kullanıcı beyanıdır;
CSV'nin kökeni ve SPV uyarıları bu sayısal betik tarafından doğrulanmaz.
B12'de düzeltmesiz Pearson satırı esas alınır. B13'te REGRESSION yordamının
16 tahmini ve 16 artığı açık formül sonuçlarıyla ayrıca karşılaştırılır.

**Yorum:** Yüksek korelasyon nedensellik göstermez. Saçılım, artık ve Q–Q grafiklerini birlikte inceleyin. Küçük örneklemde tanı grafiklerinin gücü sınırlıdır. Çok küçük p değerini p = 0 olarak raporlamayın.
