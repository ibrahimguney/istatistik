GET DATA /TYPE=XLSX
 /FILE='companion/spss/excel/b01.xlsx'
 /SHEET=NAME 'veri' /CELLRANGE=FULL /READNAMES=ON.
FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.
VARIABLE LABELS id 'Dosya ici sira numarasi; ozgun ogrenci kimligi degildir'.
VARIABLE LEVEL id (NOMINAL).
VARIABLE LABELS school 'Okul'.
VARIABLE LEVEL school (NOMINAL).
VARIABLE LABELS sex 'Kaynak dosyasindaki cinsiyet kodu'.
VARIABLE LEVEL sex (NOMINAL).
VARIABLE LABELS age 'Yas'.
VARIABLE LEVEL age (SCALE).
VARIABLE LABELS studytime 'Haftalik calisma suresi kategorisi; saat sayisi degildir'.
VARIABLE LEVEL studytime (ORDINAL).
VARIABLE LABELS absences 'Devamsizlik sayisi'.
VARIABLE LEVEL absences (SCALE).
VARIABLE LABELS g1 'Birinci donem notu'.
VARIABLE LEVEL g1 (SCALE).
VARIABLE LABELS g2 'Ikinci donem notu'.
VARIABLE LEVEL g2 (SCALE).
VARIABLE LABELS g3 'Yil sonu notu'.
VARIABLE LEVEL g3 (SCALE).
VARIABLE LABELS pass10 'Egitim amacli turetilmis esik gostergesi'.
VARIABLE LEVEL pass10 (NOMINAL).
VALUE LABELS school 1 'GP' 2 'MS'
 /sex 1 'F' 2 'M'
 /studytime 1 '<2 saat' 2 '2-5 saat' 3 '5-10 saat' 4 '>10 saat'
 /pass10 0 'G3<10' 1 'G3>=10'.
FORMATS id school sex age studytime absences g1 g2 g3 pass10 (F8.0).
EXECUTE.
SAVE OUTFILE='companion/spss/sav/b01.sav'.
