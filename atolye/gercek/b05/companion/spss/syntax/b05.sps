SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='companion/spss/csv/b05.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS="," /QUALIFIER='"'
 /FIRSTCASE=2
 /VARIABLES=rep F8.0
 ort5 F20.12 z5 F20.12 ort30 F20.12 z30 F20.12
 ort100 F20.12 z100 F20.12.
FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.
VARIABLE LABELS
 rep 'Benzetim tekrar numarasi'
 ort5 '5 cekimin ortalamasi'
 ort30 '30 cekimin ortalamasi'
 ort100 '100 cekimin ortalamasi'
 z5 'Standartlastirilmis 5 cekim ortalamasi'
 z30 'Standartlastirilmis 30 cekim ortalamasi'
 z100 'Standartlastirilmis 100 cekim ortalamasi'.
VARIABLE LEVEL rep (NOMINAL)
 ort5 ort30 ort100 z5 z30 z100 (SCALE).
FORMATS ort5 ort30 ort100 z5 z30 z100 (F12.9).
EXECUTE.
DESCRIPTIVES VARIABLES=ort5 ort30 ort100 z100
 /STATISTICS=MEAN STDDEV.
GRAPH /HISTOGRAM(NORMAL)=z5.
GRAPH /HISTOGRAM(NORMAL)=z100.
COMPUTE kapsama=(ABS(z100)<=1.96).
VALUE LABELS kapsama
 0 'Aralik disinda' 1 'Aralik icinde'.
VARIABLE LEVEL kapsama (NOMINAL).
FORMATS kapsama (F1.0).
FREQUENCIES VARIABLES=kapsama.
