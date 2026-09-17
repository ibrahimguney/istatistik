* Bu dosyayi ornek-01 calisma klasorunden calistirin.
* Mevcut acik verilerinizi once kaydedin.
SET DECIMAL DOT.
INSERT FILE='analiz.sps' ERROR=STOP.

DATASET ACTIVATE B10Test.
WEIGHT OFF.
FORMATS alfa alt_sinir beta cohen_d genislik gereken_guc gereken_hacim guc hacim hata_payi hedef_guc kritik_t merkezdisilik onceki_guc ortalama p_cift plan_alfa plan_d plan_fark plan_hacim plan_kritik_t plan_sapma plan_serbestlik reddet_cift referans serbestlik standart_hata standart_sapma t_degeri ust_sinir (E25.16).
EXECUTE.
SAVE TRANSLATE OUTFILE='spss-ozet.csv'
 /TYPE=CSV /ENCODING='UTF8' /REPLACE /FIELDNAMES /CELLS=VALUES
 /KEEP=alfa alt_sinir beta cohen_d genislik gereken_guc gereken_hacim guc hacim hata_payi hedef_guc kritik_t merkezdisilik onceki_guc ortalama p_cift plan_alfa plan_d plan_fark plan_hacim plan_kritik_t plan_sapma plan_serbestlik reddet_cift referans serbestlik standart_hata standart_sapma t_degeri ust_sinir.
