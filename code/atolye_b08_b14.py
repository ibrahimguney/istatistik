"""B07–B14 öğrenci sayfalarını ve indirilebilir paketleri yerel kaynaktan üretir."""
from pathlib import Path
import csv
import hashlib
import html
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'atolye'
E = html.escape
DATA = {
7: dict(title='Nokta tahmini', subtitle='Bir oran, ne kadar değişebilir?', scope='10 yapay ikili yanıt + 10.000 kayıtlı benzetim tekrarı',
 question='On yanıtın altısı olumluysa örneklem oranı 0,60 olur. Başka bir örneklemde aynı oranı bulmayı bekler miyiz?',
 theory='Örneklem oranı p̂ = X/n; yerine koyma standart hatası √[p̂(1−p̂)/n]. Benzetimde yanlılık, varyans ve MSE farklı soruları yanıtlar.',
 interpretation='On yanıtta p̂ = 0,60 ve yaklaşık SE = 0,154919. Ayrı Binom(50; 0,40) benzetiminde ampirik MSE 0,00484828, kuramsal MSE 0,0048’dir.',
 caution='On yanıt ile 10.000 benzetim tekrarı iki ayrı veri yapısıdır. Tekrarlanan simülasyonlar gerçek katılımcı sayısını artırmaz. Aynı CSV’yi kullanın; yeni R çekimlerinin Python çekimleriyle aynı olması beklenmez.',
 exercise='p̂ sabitken n, 25’ten 400’e çıkarsa yaklaşık standart hata nasıl değişir?',answer='Örneklem hacmi 16 katına çıktığı için standart hata dörtte birine iner: 0,097980 → 0,024495.', count=21),
8: dict(title='Güven aralıkları', subtitle='Tahmine bir belirsizlik aralığı ekle.', scope='n = 25, ortalama = 72, s = 10 · tek özet satırı',
 question='Örneklem ortalaması 72 ise evren ortalamasını hangi aralıkla tahmin ederiz? Daha yüksek güven düzeyinin bedeli nedir?',
 theory='Güven aralığı: x̄ ± t* × s/√n. Burada SE = 2 ve serbestlik derecesi 24’tür. %95 için t* = t(0,975; 24), %99 için t* = t(0,995; 24).',
 interpretation='%95 güven aralığı [67,8722; 76,1278], %99 güven aralığı [66,4061; 77,5939]. Aynı veriyle güven düzeyi yükseldikçe aralık genişler.',
 caution='CSV’nin bir satırı bir öğrenciyi değil 25 gözlemin özetini temsil eder. %95 güven, yöntemin tekrarlanan örneklemelerdeki kapsama özelliğidir; bireysel puanların %95’ini kapsayan bir aralık değildir.',
 exercise='Standart sapma 10’dan 5’e düşer, n ve güven düzeyi aynı kalırsa aralık genişliği ne olur?',answer='Standart hata ve hata payı yarıya iner. Aralık merkezi 72 kalır; %95 aralık yaklaşık [69,9361; 74,0639] olur.', count=19),
9: dict(title='Hipotez testleri', subtitle='Aynı istatistik, farklı araştırma soruları.', scope='Fark = 2,1 · SE = 1 · sd = 49 · α = 0,05',
 question='Gözlenen fark, sıfır fark varsayımıyla ne ölçüde uyumludur? Testin yönü sonucu nasıl değiştirir?',
 theory='t = (tahmin − H₀ değeri)/SE. Çift yönlü test iki kuyruğu, önceden belirlenmiş tek yönlü test ilgili kuyruğu kullanır.',
 interpretation='t = 2,1; çift yönlü p = 0,040900. H₀, α = 0,05 düzeyinde reddedilir; α = 0,01 düzeyinde reddedilemez. %95 fark aralığı [0,0904; 4,1096] sıfırı içermez.',
 caution='Veriyi gördükten sonra anlamlı sonuç elde etmek için testin yönünü değiştirmeyin. p değeri, H₀’ın doğru olma olasılığı değildir; istatistiksel anlamlılık pratik önemi tek başına göstermez.',
 exercise='Üst yönlü p = 0,020450 iken alt yönlü p neden yaklaşık 0,979550’dir?',answer='t pozitif olduğundan sağ kuyruktaki alan küçüktür. Sürekli t dağılımında iki tek yönlü p değeri toplamı 1’dir. Araştırma yönü analizden önce seçilir.', count=20),
10: dict(title='Hata, güç ve tek örneklem t testi', subtitle='Testi yorumla, yeni çalışmayı planla.', scope='Test: n = 25 · Güç planı: d = 0,50, α = 0,05, hedef = 0,80',
 question='Ortalamanın 50’den farklı olup olmadığını test ettik. Gelecekte 5 puanlık farkı yakalamak için kaç gözlem gerekir?',
 theory='Test için t = (55−50)/(10/√25) = 2,5. Güç planında merkez dışı t dağılımı ve önceden belirlenen d = 5/10 = 0,50 kullanılır.',
 interpretation='Testin çift yönlü p değeri 0,019654’tür. Planlanan etki için n = 33’te güç 0,795366; n = 34’te 0,807778’dir. %80 hedefine ulaşan en küçük tam sayı n = 34’tür.',
 caution='Test özeti veri.csv, ileriye dönük tasarım plan.csv içindedir. Planlanan etkiyi gözlenen sonuçtan türetilmiş “gözlenen güç” gibi sunmayın. SPSS’te güç hesabı iki kuyruğu da içerir.',
 exercise='n = 33 neden %80 güç hedefi için yeterli kabul edilmiyor?',answer='Güç 0,795366’dır ve 0,80’in altındadır. İki ondalığa yuvarlayıp 0,80 görmek yeterli değildir; karar tam duyarlıklı değerle verilir.', count=30),
11: dict(title='Bağımsız ve eşleştirilmiş t testleri', subtitle='Önce ölçümlerin ilişkisini belirle.', scope='Bağımsız: n₁ = 30, n₂ = 28 · Ayrı eşleştirilmiş örnek: 20 çift',
 question='İki farklı grubun ortalamalarını karşılaştırmak ile aynı kişilerin önce–sonra farkını sınamak neden farklıdır?',
 theory='Welch testi bağımsız grupların iki varyans katkısını birleştirir. Eşleştirilmiş testte analiz birimi kişi içi farktır; SE = s_fark/√n_çift.',
 interpretation='Welch: fark = 6, t = 2,512074, sd ≈ 51,7113, p = 0,015163. Ayrı eşleştirilmiş örnek: fark = 4,2, t = 3,756594, sd = 19, p = 0,001336.',
 caution='Bunlar aynı veriye uygulanan rakip testler değildir; iki ayrı tasarımın özetleridir. Eşleştirilmiş analizde ön ve son ölçümlerin ayrı standart sapmaları, farkların standart sapmasının yerine geçmez.',
 exercise='20 kişinin iki ölçümü varsa eşleştirilmiş testte n ve serbestlik derecesi kaçtır?',answer='n = 20 çift, sd = 19’dur. 40 ölçümü 40 bağımsız gözlem gibi saymak yanlıştır. Buradaki eşleştirilmiş %95 fark aralığı [1,8599; 6,5401]’dir.', count=34),
12: dict(title='Kategorik veriler ve ki-kare testi', subtitle='Sayıları doğru ağırlıkla karşılaştır.', scope='2 × 2 tablo · 4 hücre · toplam 80 gözlem',
 question='Birinci grupta başarı oranı %75, ikinci grupta %50. Grup ile sonuç arasında ilişki olduğuna dair kanıt var mı?',
 theory='Beklenen frekans = satır toplamı × sütun toplamı / N. Pearson χ² = Σ(O−E)²/E. Bu örnekte süreklilik düzeltmesi uygulanmaz.',
 interpretation='χ²(1) = 5,333333; p = 0,020921; Cramér V = 0,258199. En küçük beklenen frekans 15’tir. α = 0,05 düzeyinde bağımsızlık hipotezi reddedilir.',
 caution='CSV’de dört hücre vardır; katılımcı sayısı 80’dir. SPSS CROSSTABS sırasında frekans ağırlığı kullanılır ve sonra kapatılır. Pearson satırını karşılaştırın; Yates düzeltmesi veya Fisher testi başka bir hesap verir.',
 exercise='Birinci grubun başarılı hücresinde gözlenen 30, beklenen 25 ise χ² katkısı ve Pearson artığı nedir?',answer='Katkı = (30−25)²/25 = 1; Pearson artığı = (30−25)/√25 = 1. İlişki bulunması nedensellik kanıtı değildir.', count=32),
13: dict(title='Korelasyon ve basit regresyon', subtitle='İlişkiyi çiz, tahminin sınırını gör.', scope='16 yapay gözlem · çalışma saati ve puan',
 question='Çalışma süresi ile puan arasındaki ilişkiyi nasıl özetleriz? Altı saat çalışan yeni bir kişi için belirsizlik ne kadardır?',
 theory='Doğru: ŷ = 44,598039 + 3,137255 × saat. Ortalama yanıt aralığı ile tek yeni gözlem için öngörü aralığı farklı belirsizlikleri ölçer.',
 interpretation='r = 0,980618; R² = 0,961611. Altı saatte tahmin 63,4216; %95 ortalama yanıt aralığı [62,6385; 64,2047], yeni birey aralığı [60,7387; 66,1044].',
 caution='Yüksek korelasyon nedensellik göstermez. Saçılım, artık ve Q–Q grafiklerini birlikte inceleyin. Küçük örneklemde tanı grafiklerinin gücü sınırlıdır. Çok küçük p değerini p = 0 olarak raporlamayın.',
 exercise='Yeni birey için öngörü aralığı, ortalama yanıt aralığından neden geniştir?',answer='Yeni bireyin hatası, ortalama yanıt tahmininin belirsizliğine eklenir: SE_birey² = MSE + SE_ortalama². Aynı merkez çevresinde daha geniş bir aralık oluşur.', count=62),
14: dict(title='Genel sınava hazırlık', subtitle='Yöntemi seç, bulguyu gerekçelendir.', scope='24 çift · son − ön farkı = −3,2 · farkların s değeri = 6',
 question='Aynı kişilerin önce ve sonra ölçülen değerleri değişmiş mi? Negatif bir farkı nasıl yorumlarız?',
 theory='Son−ön farkları için tek örneklem t hesabı: t = −3,2/(6/√24). Eşleştirme korunur; sıfır fark hem test hem güven aralığında değerlendirilir.',
 interpretation='t(23) = −2,612789; p = 0,015558. %95 fark aralığı [−5,7336; −0,6664], d_z = −0,533333. Ortalama son ölçüm, ön ölçümden 3,2 birim düşüktür.',
 caution='Azalmanın iyi veya kötü olması ölçülen değişkene bağlıdır. Kontrol grubu ve uygun tasarım olmadan değişimi müdahalenin nedensel etkisi olarak yorumlamayın. Özetler varsayımları tek başına sınamaz.',
 exercise='Farkı ön−son olarak tanımlasaydık t, p ve güven aralığı nasıl değişirdi?',answer='t ve d_z işaret değiştirir; çift yönlü p aynı kalır. Aralık [0,6664; 5,7336] olur. Araştırma yorumu seçilen fark yönüyle tutarlı yazılmalıdır.', count=17),
}
TITLES={1:'İstatistiksel araştırma süreci',2:'Evren, örneklem ve veri türleri',3:'Betimsel istatistik',4:'Örnekleme dağılımları',5:'Merkezi limit teoremi ve standart hata',6:'Örnekleme yöntemleri',**{n:d['title'] for n,d in DATA.items()}}


def manifest(folder):
    files={p.relative_to(folder).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(folder.rglob('*')) if p.is_file() and p.name!='MANIFEST.json' and '__pycache__' not in p.parts}
    (folder/'MANIFEST.json').write_text(json.dumps({'algorithm':'SHA-256','files':files},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def chapter(n,d):
    code=f'b{n:02}'; package=ROOT/'bolumler'/code; example=package/'ornek-01'; prefix=f'bolumler/{code}/ornek-01'
    current=f'''# {code.upper()} — güncel çalışma kaydı · 17 Eylül 2026

Python ve gerçek R 4.3.3 yorumlayıcısında `{d['count']}` referans değeri karşılaştırıldı.
İki yazılımın hesapladığı sonuçlar ayrıca birbirleriyle karşılaştırıldı (bağıl tolerans 1e-9,
mutlak tolerans 1e-15). `--check --grafik` çalıştırıldı; grafik üretimi denetlendi.
Değiştirilmiş referans ve eksik veri iki yazılımda da hata verdi.
Grafikler geçici çalışma klasöründe üretildi; dağıtımdaki özgün Python grafikleri korunur.

**IBM SPSS çalıştırılmadı.** Kaynak incelemesi ve Python/R eşleşmesi SPSS kabulü değildir.
'''
    if n>=8:
        current+='''`ornek-01/spss-dogrula.sps` SPSS sonuçlarını CSV olarak dışa aktarır.
`ornek-01/spss_karsilastir.py` dışa aktarımları referanslarla karşılaştırır.
Adımlar: [SPSS kontrol rehberi](SPSS-KONTROL.md).
'''
    current+='''
Eski DOGRULAMA.md içindeki 9 Eylül kaydı tarihsel denetimi açıklar.
Güncel tam çalıştırma günlüğü depo kökündeki
`dogrulama/python-r-2026-09-17.json` dosyasındadır.
Kod, veri ve paket dosyalarının SHA-256 değerleri güncel MANIFEST.json içindedir.
Ham veri/özet ayrımı, örnekleme varsayımları ve yorum sınırları devam eder.
'''
    (package/'GUNCEL-DOGRULAMA.md').write_text(current,encoding='utf-8')
    for path,link in [(package/'DOGRULAMA.md','GUNCEL-DOGRULAMA.md'),(package/'README.md','GUNCEL-DOGRULAMA.md'),(example/'README.md','../GUNCEL-DOGRULAMA.md')]:
        text=path.read_text(encoding='utf-8')
        if not text.startswith('> **17 Eylül'):
            path.write_text(f'> **17 Eylül 2026 güncellemesi:** Python ve R çalıştırıldı; IBM SPSS çalışma kabulü bekliyor. [Güncel kayıt]({link}). Aşağıdaki eski çalışma/yayın durumları tarihsel kayıttır.\n\n'+text,encoding='utf-8')
    if n>=8:
        shutil.copy2(ROOT/'code/spss_karsilastir.py',example/'spss_karsilastir.py')
        guide=f'''# {code.upper()} — IBM SPSS 29 kontrolü

Bu paket SPSS'te henüz çalıştırılmadı. Kontrol için:

1. ZIP'i tamamen ayıklayın; açık SPSS çalışmalarınızı kaydedin.
2. Syntax penceresinde gerçek klasörünüze göre `CD 'C:/.../{code}/ornek-01'.` çalıştırın.
   Syntax dosyasını açmak çalışma klasörünü otomatik değiştirmez.
3. `spss-dogrula.sps` dosyasının tamamını çalıştırın. `analiz.sps` içeri alınır;
   veri ve plan girdileri aynı klasörden okunur. Hata/uyarıları inceleyin.
4. `spss-ozet.csv`{' ve `spss-satirlar.csv`' if n in [12,13] else ''} dosyası oluşur.
   Önceki dışa aktarımlar varsa üzerlerine yazılır; analiz kaynakları değişmez.
5. Aynı `ornek-01` klasöründe terminal açıp çalıştırın:

   ```bash
   py spss_karsilastir.py --surum 29 --rapor spss-sonuc.json
   ```

   Gerçek sürüm numaranızı yazın. Yalnız Python standart kitaplığı gerekir.
   Beklenen: **GECTI: {d['count']} kontrol**. Hatalı/eksik dışa aktarım başarı sayılmaz.
   Yeni denemede yeni rapor adı verin; mevcut raporun üzerine yazılmaz.
6. SPSS Viewer çıktısını `{code}-spss.spv` ve mümkünse PDF olarak kaydedin.
   SPV, JSON raporu ve dışa aktarılan CSV'leri birlikte inceleme için paylaşın.

Karşılaştırma bağıl 1e-8 ve mutlak 1e-14 tolerans kullanır; SPSS dışa aktarımı
16 ondalıklı bilimsel gösterimle yapılır. Görüntüde yuvarlatılmış değerleri CSV'ye elle yazmayın.
Çok küçük p değerleri sıfır kabul edilmez. SPSS sürümü kullanıcı beyanıdır;
CSV'nin kökeni ve SPV uyarıları bu sayısal betik tarafından doğrulanmaz.
B12'de düzeltmesiz Pearson satırı esas alınır. B13'te REGRESSION yordamının
16 tahmini ve 16 artığı açık formül sonuçlarıyla ayrıca karşılaştırılır.

**Yorum:** {d['caution']}
'''
        (package/'SPSS-KONTROL.md').write_text(guide,encoding='utf-8')
    manifest(package)
    target=SITE/'bolumler'/code
    if target.exists(): shutil.rmtree(target)
    shutil.copytree(package,target,ignore=shutil.ignore_patterns('__pycache__'))
    with zipfile.ZipFile(SITE/'indir'/f'{code}-ogretim.zip','w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(package.rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts:
                info=zipfile.ZipInfo(f'{code}/'+p.relative_to(package).as_posix(),date_time=(2026,9,17,0,0,0))
                info.compress_type=zipfile.ZIP_DEFLATED
                z.writestr(info,p.read_bytes())
    refs=list(csv.DictReader((example/'beklenen-sonuclar.csv').open(encoding='utf-8-sig')))
    rows=''.join(f'<tr><td>{E(r["degisken"])}</td><th scope="row">{E(r["olcu"])}</th><td>{float(r["deger"]):.10g}</td></tr>' for r in refs)
    graph=next((example/'ciktilar/python').glob('*.png'))
    figure=f'<figure><img class="chapter-figure" src="{prefix}/ciktilar/python/{graph.name}" alt="{E(d["title"])}: hesaplanan sonuçların grafiği; sayısal değerler aşağıdaki sonuç tablosundadır."><figcaption>Ortak veriden üretilen Python grafiği. <a href="{prefix}/grafik-aciklamasi.md">Grafiğin ayrıntılı açıklaması</a></figcaption></figure>'
    links=''.join(f'<a href="{prefix}/{name}">{label}</a>' for name,label in [('veri.csv','Ortak CSV'),('veri-sozlugu.csv','Veri sözlüğü'),('cozum.py','Python kodu'),('cozum.R','R kodu'),('analiz.sps','SPSS syntax'),('beklenen-sonuclar.csv','Beklenen sonuçlar'),('README.md','Çalıştırma rehberi')])
    spss=(f'<p><a href="bolumler/{code}/SPSS-KONTROL.md">SPSS 29 adım adım kontrol rehberi</a></p><pre><code>CD \'C:/.../{code}/ornek-01\'.\nINSERT FILE=\'spss-dogrula.sps\' ERROR=STOP.</code></pre><p>Sonra aynı klasörde terminalden:</p><pre><code>py spss_karsilastir.py --surum 29 --rapor spss-sonuc.json</code></pre><p>SPSS dışa aktarımı olmadan bu kontrol geçmez. SPV çıktısını ve JSON raporunu birlikte saklayın.</p>' if n>=8 else f'<p>SPSS’te çalışma klasörünü <code>{code}/ornek-01</code> yapıp <code>analiz.sps</code> çalıştırın; <a href="{prefix}/README.md">bölüm rehberindeki tabloları</a> karşılaştırın.</p>')
    page=f'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{E(d['title'])}: Python, R ve IBM SPSS uygulaması, ortak veri ve doğrulama."><title>{code.upper()} · {E(d['title'])} · İstatistik Atölyesi</title><link rel="stylesheet" href="assets/site.css"><link rel="stylesheet" href="assets/chapters.css"></head>
<body><a class="skip" href="#icerik">İçeriğe geç</a><header class="masthead"><a class="brand" href="index.html"><span class="mark">İ.</span>İstatistik Atölyesi</a><nav aria-label="Ana gezinme"><a href="index.html#bolumler">14 bölüm</a><a href="#uygula">Uygula</a><a href="#dogrulama">Doğrulama</a></nav><span class="tag">{code.upper()} · PYTHON / R / SPSS</span></header>
<main id="icerik" class="wrap"><p class="breadcrumb"><a href="index.html">Ana sayfa</a> / {code.upper()} · {E(d['title'])}</p><header class="lesson-head"><p class="eyebrow">{n:02} / {E(d['title']).upper()}</p><h1>{E(d['subtitle'])}</h1><p class="lead">{E(d['scope'])}</p><div class="actions"><a class="button primary" href="indir/{code}-ogretim.zip" download>Veri ve kod paketini indir</a><a class="button" href="#sonuclar">Sonuçları incele</a></div></header>
<div class="workbench"><aside><nav aria-label="Bölüm içeriği"><p class="eyebrow">ÇALIŞMA ROTASI</p><a href="#soru">01 · Soru ve yöntem</a><a href="#sonuclar">02 · Görsel ve yorum</a><a href="#uygula">03 · Yazılımda uygula</a><a href="#dene">04 · Kendini sına</a><a href="#dogrulama">05 · Kontrol kaydı</a></nav></aside><div class="lesson">
<section id="soru"><h2>Sorudan yönteme</h2><p class="lead">{E(d['question'])}</p><div class="notice"><strong>Hesaplama fikri</strong><p>{E(d['theory'])}</p></div></section>
<section id="sonuclar"><h2>Gör, karşılaştır, yorumla</h2>{figure}<blockquote>{E(d['interpretation'])}</blockquote><div class="notice caution"><strong>Yorum sınırı</strong><p>{E(d['caution'])}</p></div><details><summary>{d['count']} referans değerinin tamamı</summary><div class="detail-body"><p>Gösterim yuvarlatılmıştır; kodlar tam duyarlıklı CSV’yi kullanır.</p><div class="table-wrap"><table><caption>Ortak Python / R / SPSS hedefleri</caption><thead><tr><th scope="col">Grup</th><th scope="col">Ölçü</th><th scope="col">Değer</th></tr></thead><tbody>{rows}</tbody></table></div></div></details></section>
<section id="uygula"><h2>Aynı veri, üç yazılım</h2><p>ZIP’i tamamen ayıklayın. Çalışma klasörü <code>{code}/ornek-01</code> olmalıdır. Kodlar bilgisayarınızda çalışır.</p><details open><summary>Python</summary><div class="detail-body"><pre><code>py cozum.py --check --grafik</code></pre><p>NumPy, pandas, SciPy ve Matplotlib gerekir. Beklenen: {d['count']} kontrol değeri eşleşiyor.</p></div></details><details><summary>R / RStudio</summary><div class="detail-body"><pre><code>Rscript --vanilla cozum.R --check --grafik</code></pre><p>Standart R yeterlidir. RStudio konsolunda <code>source("cozum.R")</code> yalnız hesapları gösterir; otomatik kontrol için:</p><pre><code>kontrol_et(sonuc, read.csv("beklenen-sonuclar.csv", stringsAsFactors=FALSE))</code></pre></div></details><details><summary>IBM SPSS 29 · çalışma kabulü bekliyor</summary><div class="detail-body">{spss}</div></details><div class="links">{links}</div></section>
<section id="dene"><h2>Önce tahmin et, sonra açıkla</h2><p>{E(d['exercise'])}</p><details><summary>Gerekçeli yanıtı göster</summary><div class="detail-body"><p>{E(d['answer'])}</p></div></details><div class="links"><a href="bolumler/{code}/alistirmalar.md">Bölüm alıştırmaları</a><a href="bolumler/{code}/cozumler.md">Gerekçeli çözümler</a><a href="{prefix}/cozum.md">Tam çözüm tablosu</a></div></section>
<section id="dogrulama"><h2>Doğrulama durumu</h2><div class="table-wrap"><table><thead><tr><th scope="col">Ortam</th><th scope="col">Durum</th></tr></thead><tbody><tr><th scope="row">Python</th><td>{d['count']} referans değeri; grafik üretimi ve hatalı girdi kontrolleri geçti.</td></tr><tr><th scope="row">R 4.3.3</th><td>{d['count']} referans değeri ve Python–R sonuç karşılaştırması geçti.</td></tr><tr><th scope="row">IBM SPSS</th><td>Syntax hazır. Gerçek SPSS çalıştırması ve çıktı kabulü bekliyor.</td></tr></tbody></table></div><p>17 Eylül 2026. Sayısal uyum, araştırma varsayımlarının sağlandığını kanıtlamaz.</p><div class="links"><a href="bolumler/{code}/GUNCEL-DOGRULAMA.md">Güncel kayıt</a><a href="dogrulama/python-r-2026-09-17.json">Tam çalıştırma günlüğü</a><a href="bolumler/{code}/MANIFEST.json">Dosya bütünlüğü</a></div></section></div></div>
<footer><div class="between"><a href="b{n-1:02}.html">← {n-1}. bölüm</a><a href="{'b'+str(n+1).zfill(2)+'.html' if n<14 else 'index.html#bolumler'}">{'Sonraki bölüm →' if n<14 else '14 bölüme dön →'}</a></div><p>İbrahim Güney · İstatistik Atölyesi · Ortak veri, yeniden üretilebilir hesaplar.</p></footer></main></body></html>'''
    (SITE/f'{code}.html').write_text(page,encoding='utf-8')


def main():
    report=json.loads((ROOT/'dogrulama/python-r-2026-09-17.json').read_text())
    if not report['gecti']: raise SystemExit('Python/R doğrulaması başarısız; yayın üretilemez.')
    for n,d in DATA.items(): chapter(n,d)
    (SITE/'assets/chapters.css').write_text('.chapter-figure{display:block;max-width:100%;height:auto;border:1px solid var(--line);border-radius:8px;background:white}.chapter-catalog .card:last-child{grid-column:auto}.lesson{min-width:0}.lesson .table-wrap td:last-child{font-variant-numeric:tabular-nums}.lesson-head .lead{max-width:850px}@media print{details{display:block}.chapter-figure{max-height:100mm;object-fit:contain}}\n')
    index=(SITE/'index.html').read_text(encoding='utf-8')
    index=index.replace('B01 öğretim uygulamaları.','14 bölümde Python, R ve IBM SPSS öğretim uygulamaları.')
    index=index.replace('B01 · YAYIN SÜRÜMÜ V4.2','14 BÖLÜM · İSTATİSTİK ATÖLYESİ')
    # Ana sayfayı tüm bölümlere erişilen tek katalogla başlat; mevcut sayfalar korunur.
    import re
    index=re.sub(r'<main id="icerik">.*?(?=<section class="hero wrap">)','<main id="icerik">\n',index,flags=re.S)
    cards=''.join(f'<article class="card"><p class="eyebrow">B{n:02}</p><h3>{E(title)}</h3><p>{E(DATA[n]["scope"]) if n in DATA else "Öğretim verileri, yazılım kodları ve bölüm uygulamaları."}</p><a class="card-link" href="b{n:02}.html">Çalışma sayfasını aç →</a></article>' for n,title in TITLES.items())
    catalog=f'<section class="wrap section" id="bolumler"><p class="eyebrow">14 BÖLÜM · ORTAK VERİ VE KOD</p><h2>Bir bölüm seç, birlikte inceleyelim.</h2><p>B07–B14 için Python ve R çalıştırma kontrolleri tamamlandı. IBM SPSS çalışma kabulü bekliyor. İlk bölümlerin kanıt kapsamı kendi sayfalarında yer alır.</p><div class="cards chapter-catalog">{cards}</div><h3 style="margin-top:2rem">Gerçek veri ve benzetim uygulamaları</h3><div class="links"><a href="b01-gercek.html">B01 · Gerçek veri</a><a href="b02-gercek.html">B02 · Gerçek veri</a><a href="b03-gercek.html">B03 · Gerçek veri</a><a href="b04-benzetim.html">B04 · Benzetim</a><a href="b05-benzetim.html">B05 · Benzetim</a><a href="b06-gercek.html">B06 · Gerçek veri</a></div></section>'
    index=re.sub(r'<section class="wrap section" id="bolumler">.*?</section>',lambda m:catalog,index,flags=re.S)
    if 'assets/chapters.css' not in index:index=index.replace('</head>','<link rel="stylesheet" href="assets/chapters.css">\n</head>')
    (SITE/'index.html').write_text(index,encoding='utf-8')
    (SITE/'dogrulama').mkdir(exist_ok=True)
    shutil.copy2(ROOT/'dogrulama/python-r-2026-09-17.json',SITE/'dogrulama/python-r-2026-09-17.json')
    publication=SITE/'yayin-manifest.json'
    doc=json.loads(publication.read_text())
    doc['files']={p.relative_to(SITE).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(SITE.rglob('*')) if p.is_file() and p!=publication}
    publication.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
