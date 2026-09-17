* Bu dosyayi ornek-01 calisma klasorunden calistirin.
* Mevcut acik verilerinizi once kaydedin.
SET DECIMAL DOT.
INSERT FILE='analiz.sps' ERROR=STOP.

DATASET ACTIVATE B08Ozet.
WEIGHT OFF.
FORMATS alpha95 alpha99 alt95 alt99 duzey95 duzey99 genislik95 genislik99 hata95 hata99 kritik95 kritik99 n ortalama s serbestlik standart_hata ust95 ust99 (E25.16).
EXECUTE.
SAVE TRANSLATE OUTFILE='spss-ozet.csv'
 /TYPE=CSV /ENCODING='UTF8' /REPLACE /FIELDNAMES /CELLS=VALUES
 /KEEP=alpha95 alpha99 alt95 alt99 duzey95 duzey99 genislik95 genislik99 hata95 hata99 kritik95 kritik99 n ortalama s serbestlik standart_hata ust95 ust99.
