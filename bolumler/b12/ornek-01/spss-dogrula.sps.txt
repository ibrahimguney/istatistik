* B12 disari aktarim v2 - hucreler ve ozet sirasiyla kaydedilir.
* Calisma klasoru b12/ornek-01 olmalidir.
SET DECIMAL DOT.
GET DATA /TYPE=TXT /FILE='veri.csv' /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE /DELIMITERS="," /QUALIFIER='"'
 /FIRSTCASE=2 /VARIABLES=grup A12 sonuc A12 frekans F24.0.
DATASET NAME B12Hucreler.
FILTER OFF.
USE ALL.
WEIGHT OFF.
SPLIT FILE OFF.
VARIABLE LEVEL grup sonuc (NOMINAL) frekans (SCALE).
AGGREGATE OUTFILE=* MODE=ADDVARIABLES /BREAK=grup /satir_toplam=SUM(frekans).
AGGREGATE OUTFILE=* MODE=ADDVARIABLES /BREAK=sonuc /sutun_toplam=SUM(frekans).
AGGREGATE OUTFILE=* MODE=ADDVARIABLES /BREAK= /genel_toplam=SUM(frekans).
COMPUTE beklenen=satir_toplam*sutun_toplam/genel_toplam.
COMPUTE katki=(frekans-beklenen)**2/beklenen.
COMPUTE pearson_artik=(frekans-beklenen)/SQRT(beklenen).
COMPUTE satir_orani=frekans/satir_toplam.
FORMATS frekans beklenen katki pearson_artik satir_orani satir_toplam sutun_toplam genel_toplam (F16.10).
SORT CASES BY grup sonuc.
EXECUTE.
DISPLAY DICTIONARY.
LIST VARIABLES=grup sonuc frekans beklenen katki pearson_artik satir_orani satir_toplam sutun_toplam genel_toplam.
WEIGHT BY frekans.
CROSSTABS /TABLES=grup BY sonuc
 /FORMAT=AVALUE TABLES /STATISTICS=CHISQ PHI /CELLS=COUNT EXPECTED ROW SRESID.
WEIGHT OFF.

WEIGHT OFF.
FORMATS beklenen frekans katki pearson_artik satir_orani satir_toplam sutun_toplam (E25.16).
EXECUTE.
SAVE TRANSLATE OUTFILE='spss-satirlar.csv'
 /TYPE=CSV /ENCODING='UTF8' /REPLACE /FIELDNAMES /CELLS=VALUES
 /KEEP=beklenen frekans grup katki pearson_artik satir_orani satir_toplam sonuc sutun_toplam.

* Hucreler kaydedildi; simdi tek satirlik ozet hesaplanir.
AGGREGATE OUTFILE=* /BREAK= /toplam=SUM(frekans) /ki_kare=SUM(katki) /min_beklenen=MIN(beklenen).
COMPUTE serbestlik=1.
COMPUTE p=SIG.CHISQ(ki_kare,serbestlik).
COMPUTE cramer_v=SQRT(ki_kare/toplam).
COMPUTE alfa=.05.
COMPUTE reddet=(p<alfa).
VALUE LABELS reddet 0 'H0 reddedilemez' 1 'H0 reddedilir'.
FORMATS toplam ki_kare serbestlik p cramer_v min_beklenen alfa (F16.10).
EXECUTE.
LIST VARIABLES=toplam ki_kare serbestlik p cramer_v min_beklenen alfa reddet.

WEIGHT OFF.
FORMATS alfa cramer_v ki_kare min_beklenen p reddet serbestlik toplam (E25.16).
EXECUTE.
SAVE TRANSLATE OUTFILE='spss-ozet.csv'
 /TYPE=CSV /ENCODING='UTF8' /REPLACE /FIELDNAMES /CELLS=VALUES
 /KEEP=alfa cramer_v ki_kare min_beklenen p reddet serbestlik toplam.
