* Bu dosyayi ornek-01 calisma klasorunden calistirin.
* Mevcut acik verilerinizi once kaydedin.
SET DECIMAL DOT.
INSERT FILE='analiz.sps' ERROR=STOP.

DATASET ACTIVATE B13Ozet.
WEIGHT OFF.
FORMATS birey_alt birey_ust egim egim_alt egim_ust hacim korelasyon kritik_t mse ongoru ortalama_alt ortalama_ust p_egim puan_ort r_kare saat_ort sabit sabit_alt sabit_ust se_birey se_egim se_ortalama se_sabit serbestlik sse sxx sxy syy t_egim yeni_saat (E25.16).
EXECUTE.
SAVE TRANSLATE OUTFILE='spss-ozet.csv'
 /TYPE=CSV /ENCODING='UTF8' /REPLACE /FIELDNAMES /CELLS=VALUES
 /KEEP=birey_alt birey_ust egim egim_alt egim_ust hacim korelasyon kritik_t mse ongoru ortalama_alt ortalama_ust p_egim puan_ort r_kare saat_ort sabit sabit_alt sabit_ust se_birey se_egim se_ortalama se_sabit serbestlik sse sxx sxy syy t_egim yeni_saat.

DATASET ACTIVATE B13Veri.
WEIGHT OFF.
FORMATS artik satir uydurulan uydurulan_spss artik_spss (E25.16).
EXECUTE.
SAVE TRANSLATE OUTFILE='spss-satirlar.csv'
 /TYPE=CSV /ENCODING='UTF8' /REPLACE /FIELDNAMES /CELLS=VALUES
 /KEEP=artik satir uydurulan uydurulan_spss artik_spss.
