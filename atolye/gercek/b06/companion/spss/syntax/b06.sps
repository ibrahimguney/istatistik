SET DECIMAL=DOT.
GET DATA /TYPE=TXT
 /FILE='companion/spss/csv/b06.csv'
 /ENCODING='UTF8'
 /ARRANGEMENT=DELIMITED /DELCASE=LINE
 /DELIMITERS="," /QUALIFIER='"'
 /FIRSTCASE=2
 /VARIABLES=id F8.0 school F8.0 sex F8.0 age F8.0
 studytime F8.0 absences F8.0 g1 F8.0 g2 F8.0
 g3 F8.0 pass10 F8.0 srs40 F8.0 strat40 F8.0
 strw F20.12.
FILTER OFF.
WEIGHT OFF.
SPLIT FILE OFF.
VARIABLE LABELS
 g3 'Yil sonu matematik notu'
 srs40 'Basit rastgele orneklem secimi'
 strat40 'Tabakali orneklem secimi'
 strw 'Tabaka agirligi'.
VALUE LABELS school 1 'GP' 2 'MS'.
VALUE LABELS srs40 strat40 0 'Secilmedi' 1 'Secildi'.
VARIABLE LEVEL
 id school sex pass10 srs40 strat40 (NOMINAL)
 studytime (ORDINAL)
 age absences g1 g2 g3 strw (SCALE).
FORMATS g3 strw (F12.6).
EXECUTE.
DESCRIPTIVES VARIABLES=g3 /STATISTICS=MEAN STDDEV.
FILTER BY srs40.
DESCRIPTIVES VARIABLES=g3 /STATISTICS=MEAN STDDEV.
FILTER OFF.
FILTER BY strat40.
FREQUENCIES VARIABLES=school.
WEIGHT BY strw.
DESCRIPTIVES VARIABLES=g3 /STATISTICS=MEAN.
WEIGHT OFF.
FILTER OFF.
EXECUTE.
