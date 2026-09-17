* Bu dosyayi ornek-01 calisma klasorunden calistirin.
* Mevcut acik verilerinizi once kaydedin.
SET DECIMAL DOT.
INSERT FILE='analiz.sps' ERROR=STOP.

DATASET ACTIVATE B09Ozet.
WEIGHT OFF.
FORMATS alfa alt_sinir fark genislik guven_duzeyi hata_payi kritik_t null_aralikta null_degeri p_alt p_cift p_ust reddet_alfa001 reddet_alt reddet_cift reddet_ust serbestlik standart_hata t_degeri ust_sinir (E25.16).
EXECUTE.
SAVE TRANSLATE OUTFILE='spss-ozet.csv'
 /TYPE=CSV /ENCODING='UTF8' /REPLACE /FIELDNAMES /CELLS=VALUES
 /KEEP=alfa alt_sinir fark genislik guven_duzeyi hata_payi kritik_t null_aralikta null_degeri p_alt p_cift p_ust reddet_alfa001 reddet_alt reddet_cift reddet_ust serbestlik standart_hata t_degeri ust_sinir.
