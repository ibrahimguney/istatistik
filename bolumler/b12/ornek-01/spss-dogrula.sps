* Bu dosyayi ornek-01 calisma klasorunden calistirin.
* Mevcut acik verilerinizi once kaydedin.
SET DECIMAL DOT.
INSERT FILE='analiz.sps' ERROR=STOP.

DATASET ACTIVATE B12Ozet.
WEIGHT OFF.
FORMATS alfa cramer_v ki_kare min_beklenen p reddet serbestlik toplam (E25.16).
EXECUTE.
SAVE TRANSLATE OUTFILE='spss-ozet.csv'
 /TYPE=CSV /ENCODING='UTF8' /REPLACE /FIELDNAMES /CELLS=VALUES
 /KEEP=alfa cramer_v ki_kare min_beklenen p reddet serbestlik toplam.

DATASET ACTIVATE B12Hucreler.
WEIGHT OFF.
FORMATS beklenen frekans katki pearson_artik satir_orani satir_toplam sutun_toplam (E25.16).
EXECUTE.
SAVE TRANSLATE OUTFILE='spss-satirlar.csv'
 /TYPE=CSV /ENCODING='UTF8' /REPLACE /FIELDNAMES /CELLS=VALUES
 /KEEP=beklenen frekans grup katki pearson_artik satir_orani satir_toplam sonuc sutun_toplam.
