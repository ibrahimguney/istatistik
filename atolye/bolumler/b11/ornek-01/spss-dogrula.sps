* Bu dosyayi ornek-01 calisma klasorunden calistirin.
* Mevcut acik verilerinizi once kaydedin.
SET DECIMAL DOT.
INSERT FILE='analiz.sps' ERROR=STOP.

DATASET ACTIVATE B11Ozet.
WEIGHT OFF.
FORMATS alfa cift_sayisi dz es_alt es_df es_genislik es_kritik es_p es_pay es_reddet es_se es_t es_ust fark_sapmasi hacim_1 hacim_2 katki_1 katki_2 ortalama_1 ortalama_2 ortalama_fark standart_sapma_1 standart_sapma_2 w_alt w_df w_fark w_genislik w_kritik w_p w_pay w_reddet w_se w_t w_ust (E25.16).
EXECUTE.
SAVE TRANSLATE OUTFILE='spss-ozet.csv'
 /TYPE=CSV /ENCODING='UTF8' /REPLACE /FIELDNAMES /CELLS=VALUES
 /KEEP=alfa cift_sayisi dz es_alt es_df es_genislik es_kritik es_p es_pay es_reddet es_se es_t es_ust fark_sapmasi hacim_1 hacim_2 katki_1 katki_2 ortalama_1 ortalama_2 ortalama_fark standart_sapma_1 standart_sapma_2 w_alt w_df w_fark w_genislik w_kritik w_p w_pay w_reddet w_se w_t w_ust.
