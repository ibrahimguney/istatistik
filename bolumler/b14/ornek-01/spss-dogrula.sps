* Bu dosyayi ornek-01 calisma klasorunden calistirin.
* Mevcut acik verilerinizi once kaydedin.
SET DECIMAL DOT.
INSERT FILE='analiz.sps' ERROR=STOP.

DATASET ACTIVATE B14Ozet.
WEIGHT OFF.
FORMATS alfa alt_sinir cift_sayisi dz fark_sapmasi genislik guven_duzeyi hata_payi kritik_t ortalama_fark p_cift reddet serbestlik sifir_aralikta standart_hata t_degeri ust_sinir (E25.16).
EXECUTE.
SAVE TRANSLATE OUTFILE='spss-ozet.csv'
 /TYPE=CSV /ENCODING='UTF8' /REPLACE /FIELDNAMES /CELLS=VALUES
 /KEEP=alfa alt_sinir cift_sayisi dz fark_sapmasi genislik guven_duzeyi hata_payi kritik_t ortalama_fark p_cift reddet serbestlik sifir_aralikta standart_hata t_degeri ust_sinir.
