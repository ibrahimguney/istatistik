# Kaynak ve dönüşümler

Aşağıdaki kayıt companion/spss/README.md belgesinden alınmıştır.
Bu teslimde yeni çevrimiçi kaynak/lisans denetimi yapılmadı.

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

