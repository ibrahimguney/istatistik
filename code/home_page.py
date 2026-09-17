"""İstatistik Atölyesi ana sayfası; yerel veriden SVG ve erişilebilir katalog."""
import csv
from html import escape as esc
from pathlib import Path

DESCRIPTIONS = {
1: 'Bir araştırma sorusunu ölçülebilir değişkenlere ve anlamlı bir analize dönüştürün.',
2: 'Kimi inceliyoruz? Evreni, örneklemi ve değişken türlerini ayırt edin.',
3: 'Verinin merkezini, yayılımını ve aykırı gözlemlerini birlikte keşfedin.',
4: 'Aynı evrenden gelen örneklemlerin neden farklı sonuçlar verdiğini görün.',
5: 'Örneklem büyüdükçe değişen dağılımı ve standart hatayı inceleyin.',
6: 'Basit rastgele ve tabakalı örneklemeyi aynı çerçevede karşılaştırın.',
7: 'Bir tahminin yanlılığını, değişkenliğini ve ortalama karesel hatasını araştırın.',
8: 'Nokta tahmininden aralık tahminine geçin; güven düzeyinin etkisini görün.',
9: 'Hipotezi kurun, testin yönünü seçin ve p değerini doğru yorumlayın.',
10: 'Test sonucunu yorumlayın; bir sonraki araştırmanın örneklemini planlayın.',
11: 'Bağımsız grupları ve eşleştirilmiş ölçümleri uygun yöntemle karşılaştırın.',
12: 'Frekanslardan ilişkiye ulaşın; ki-kare testi ve etki büyüklüğünü inceleyin.',
13: 'İlişkiyi modelleyin; regresyon doğrusunu, artıkları ve öngörü aralıklarını keşfedin.',
14: 'Doğru yöntemi seçerek hesaplamayı, yorumu ve araştırma tasarımını birleştirin.',
}
GROUPS = {**{n:('temeller','Temeller') for n in range(1,4)}, **{n:('ornekleme','Örnekleme') for n in range(4,8)}, **{n:('cikarim','İstatistiksel çıkarım') for n in range(8,13)}, **{n:('iliski','İlişki ve tekrar') for n in range(13,15)}}
ICONS = {
 'temeller':'<path d="M4 19h16M7 15v-4m5 4V5m5 10V8"/>',
 'ornekleme':'<circle cx="6" cy="6" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/><path d="M8 8l8 8M8 16l8-8"/>',
 'cikarim':'<path d="M3 17c4 0 4-11 9-11s5 11 9 11M7 20V10m10 10V10"/>',
 'iliski':'<path d="M4 4v16h16M7 15l4-5 4 2 5-7"/>',
}

def icon(group):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[group]}</svg>'


def scatter(root):
    with (root/'bolumler/b13/ornek-01/veri.csv').open() as f:
        data=[(float(r['saat']),float(r['puan'])) for r in csv.DictReader(f)]
    mx=sum(x for x,y in data)/len(data);my=sum(y for x,y in data)/len(data)
    slope=sum((x-mx)*(y-my) for x,y in data)/sum((x-mx)**2 for x,y in data)
    intercept=my-slope*mx
    px=lambda x:60+(x-1)/8*384
    py=lambda y:250-(y-45)/30*198
    grids=''.join(f'<line x1="60" x2="444" y1="{py(y):.2f}" y2="{py(y):.2f}"/><text x="46" y="{py(y)+4:.2f}" text-anchor="end">{y}</text>' for y in [45,55,65,75])
    ticks=''.join(f'<text x="{px(x):.2f}" y="274" text-anchor="middle">{x}</text>' for x in [2,4,6,8])
    points=''.join(f'<circle cx="{px(x):.2f}" cy="{py(y):.2f}" r="5.5"><title>{x:g} saat, {y:g} puan</title></circle>' for x,y in data)
    return f'''<svg class="scatter" viewBox="0 0 480 305" role="img" aria-labelledby="plot-title plot-desc"><title id="plot-title">Çalışma süresi ile puan arasındaki ilişki</title><desc id="plot-desc">B13’teki 16 yapay gözlemin saçılım grafiği ve en küçük kareler doğrusu. Bazı gözlemler üst üste gelir. Saat arttıkça puan yükselir; korelasyon yaklaşık 0,981’dir. Bu ilişki nedensellik göstermez.</desc><g class="plot-grid">{grids}</g><g class="plot-ticks">{ticks}<text x="60" y="29">Puan</text><text x="252" y="300" text-anchor="middle">Çalışma süresi (saat)</text></g><path class="fit" d="M {px(1.5):.2f} {py(intercept+slope*1.5):.2f} L {px(8.5):.2f} {py(intercept+slope*8.5):.2f}"/><g class="plot-points">{points}</g></svg>'''


def build_home(root, titles):
    root=Path(root);site=root/'atolye'
    cards=[]
    for n,title in titles.items():
        group,label=GROUPS[n]
        search=f'B{n:02} {title} {DESCRIPTIONS[n]} {label}'
        cards.append(f'''<article class="course" data-group="{group}" data-search="{esc(search)}"><div class="course-top"><span class="course-icon {group}">{icon(group)}</span><span class="course-number">B{n:02}</span></div><p class="course-category">{label}</p><h3><a href="b{n:02}.html">{esc(title)}</a></h3><p class="course-description">{DESCRIPTIONS[n]}</p><div class="course-foot"><span>Veri · Kod · Uygulama</span><span aria-hidden="true">↗</span></div></article>''')
    filters=''.join(f'<button type="button" data-filter="{key}" aria-pressed="false">{label}</button>' for key,label in [('temeller','Temeller'),('ornekleme','Örnekleme'),('cikarim','İstatistiksel çıkarım'),('iliski','İlişki ve tekrar')])
    html=f'''<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="İbrahim Güney’in istatistik kitabına eşlik eden 14 bölümlük uygulama atölyesi. Python, R ve IBM SPSS ile veriyi keşfedin, analiz edin ve yorumlayın."><meta name="theme-color" content="#123e34"><title>İstatistik Atölyesi · İbrahim Güney</title><link rel="stylesheet" href="assets/home.css"><script src="assets/home.js" defer></script></head>
<body><a class="skip" href="#icerik">İçeriğe geç</a>
<header class="site-header"><div class="shell header-inner"><a class="home-brand" href="index.html" aria-label="İstatistik Atölyesi ana sayfa"><span class="brand-mark">İ.</span><span>İstatistik <strong>Atölyesi</strong></span></a><nav aria-label="Ana gezinme"><a href="#bolumler">Bölümler</a><a href="#rota">Nasıl çalışırım?</a><a href="#dogrulama">Doğrulama</a></nav><a class="header-start" href="b01.html">Atölyeye başla <span aria-hidden="true">↗</span></a></div></header>
<main id="icerik"><section class="home-hero shell" aria-labelledby="hero-title"><div class="hero-copy"><p class="eyebrow"><span class="status-dot"></span> İBRAHİM GÜNEY · KİTAP EŞLİKÇİSİ</p><h1 id="hero-title">Veriden<br><em>anlama.</em></h1><p class="hero-subtitle">İstatistiği uygulayarak öğrenin.</p><p class="hero-description">Soruyu kurun, veriyi keşfedin, sonucunuzu yorumlayın. 14 bölüm boyunca Python, R ve SPSS ile teoriyi uygulamaya dönüştürün.</p><div class="hero-actions"><a class="btn btn-dark" href="#bolumler">Bölümleri keşfet <span aria-hidden="true">↓</span></a><a class="text-link" href="#rota">Nasıl çalışır? <span aria-hidden="true">↗</span></a></div><div class="tool-row" aria-label="Kullanılabilen yazılımlar"><span>TERCİH SİZİN</span><b>Python</b><i aria-hidden="true"></i><b>R</b><i aria-hidden="true"></i><b>IBM SPSS</b></div></div>
<div class="hero-visual"><div class="visual-grid" aria-hidden="true"></div><div class="plot-card"><div class="plot-head"><div><p class="eyebrow">VERİDEN BİR HİKÂYE</p><h2>Birlikte nasıl değişirler?</h2></div><span class="plot-code">B13</span></div>{scatter(root)}<div class="plot-bottom"><span><i class="legend-point"></i>16 yapay gözlem</span><span><i class="legend-line"></i>Regresyon doğrusu</span></div><a href="b13.html" class="plot-link">Korelasyon ve regresyonu keşfet <span aria-hidden="true">↗</span></a></div><div class="correlation-note"><span class="tiny-check" aria-hidden="true">↗</span><div><small>PEARSON KORELASYONU</small><strong>r = 0,981</strong><p>İlişkiyi gör. Nedenselliği sorgula.</p></div></div><span class="visual-caption">Her sayının arkasında bir soru var.</span></div></section>
<section class="stats-shell shell" aria-label="Atölyeye genel bakış"><div><strong>14<span> bölüm</span></strong><p>Temellerden istatistiksel çıkarıma</p></div><div><strong>3<span> yazılım</span></strong><p>Python, R ve IBM SPSS</p></div><div><strong>214<span> kontrol</span></strong><p>B08–B14 · SPSS sayısal eşleşmesi</p></div><a href="#dogrulama"><span class="verified-icon" aria-hidden="true">✓</span><span>Açık ve izlenebilir<br><b>doğrulama kayıtları</b></span><span aria-hidden="true">↗</span></a></section>
<section class="catalog-section shell" id="bolumler" aria-labelledby="catalog-title"><div class="section-heading"><div><p class="eyebrow">ÖĞRENME ROTANIZ</p><h2 id="catalog-title">Merak ettiğiniz<br>yerden başlayın.</h2></div><p>Baştan sona ilerleyin veya ihtiyacınız olan konuya geçin. Her bölümde veri, kod ve gerekçeli yorum bir arada.</p></div>
<div class="catalog-tools" id="catalog-tools" hidden><div class="filter-list" role="group" aria-label="Bölümleri konuya göre filtrele"><button type="button" data-filter="all" aria-pressed="true">Tüm bölümler <span>14</span></button>{filters}</div><label class="search-box"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/></svg><span class="sr-only">Bölüm veya konu ara</span><input id="chapter-search" type="search" placeholder="Bölüm veya konu ara…" autocomplete="off"></label></div><p class="catalog-count" id="catalog-count" role="status" aria-live="polite">14 bölüm · Kendi hızınızda öğrenin</p>
<div class="course-grid" id="course-grid">{''.join(cards)}</div><div id="no-results" class="no-results" hidden><h3>Bu aramayla eşleşen bölüm bulunamadı.</h3><p>Başka bir sözcük deneyin veya tüm bölümlere dönün.</p><button class="btn btn-dark" type="button" id="reset-search">Tüm bölümleri göster</button></div></section>
<section class="practice-band" aria-labelledby="practice-title"><div class="shell practice-inner"><div><p class="eyebrow">BİR ADIM DAHA İLERİ</p><h2 id="practice-title">Gerçek veriler.<br>Yeni sorular.</h2><p>Öğretim örneklerinden gerçek veri uygulamalarına ve benzetimlere geçin.</p></div><div class="practice-links"><a href="b01-gercek.html"><span><small>B01–B03 · GERÇEK VERİ</small><strong>395 öğrencinin verisini keşfedin</strong></span><span aria-hidden="true">↗</span></a><a href="b05-benzetim.html"><span><small>B04–B05 · BENZETİM</small><strong>Örneklem büyüdükçe ne değişir?</strong></span><span aria-hidden="true">↗</span></a><a href="b06-gercek.html"><span><small>B06 · ÖRNEKLEME</small><strong>Aynı çerçeveden iki seçim yolu</strong></span><span aria-hidden="true">↗</span></a></div></div><div class="shell other-practice"><span>Diğer uygulamalar</span><a href="b02-gercek.html">B02 · Gerçek veri</a><a href="b03-gercek.html">B03 · Gerçek veri</a><a href="b04-benzetim.html">B04 · Benzetim</a></div></section>
<section class="route-section shell" id="rota" aria-labelledby="route-title"><div class="section-heading"><div><p class="eyebrow">DÖRT ADIMDA ATÖLYE</p><h2 id="route-title">Hesaplayın.<br>Bir de nedenini sorun.</h2></div><p>Üç yazılımda uzman olmanız gerekmiyor. Bir araç seçin; soruyu, yöntemi ve yorumu birlikte düşünün.</p></div><ol class="route-steps"><li><span>01</span><h3>Soruyu ve veriyi tanıyın</h3><p>Her satır neyi temsil ediyor? Hangi soruya yanıt arıyorsunuz?</p></li><li><span>02</span><h3>Paketi indirin</h3><p>Ortak veriyi ve kodları alın. Python, R veya SPSS’te çalıştırın.</p></li><li><span>03</span><h3>Sonuçları karşılaştırın</h3><p>Hesaplarınızı bölümdeki referans değerlerle kontrol edin.</p></li><li><span>04</span><h3>Yorumunuzu savunun</h3><p>Varsayımları ve sınırları belirtin. Alıştırmalarla pekiştirin.</p></li></ol></section>
<section class="verification shell" id="dogrulama" aria-labelledby="verification-title"><div class="verification-intro"><span class="verified-icon" aria-hidden="true">✓</span><p class="eyebrow">YENİDEN ÜRETİLEBİLİR ÇALIŞMA</p><h2 id="verification-title">Sonuç kadar,<br>nasıl elde edildiği de önemli.</h2><p>B08–B14’te 214 referans değer Python ve R ile karşılaştırıldı. Kullanıcının SPSS sayısal kontrolleri de 214/214 eşleşme gösterdi.</p><a class="text-link" href="dogrulama/spss-kullanici-kabulu.json">SPSS doğrulama kaydını incele <span aria-hidden="true">↗</span></a></div><div class="verification-details"><div><span class="verification-label">PYTHON + R</span><strong>Çalıştırıldı ve karşılaştırıldı</strong><p>Hesaplanan sonuçlar, referanslar ve iki yazılımın çıktıları karşılaştırıldı.</p><a href="dogrulama/python-r-2026-09-17.json">Çalıştırma günlüğü ↗</a></div><div><span class="verification-label">IBM SPSS 29</span><strong>Kullanıcı ortamında 214/214</strong><p>Başarılı kontrol mesajları paylaşılan konsol görüntülerinde görüldü. Ham JSON/CSV ve tam SPV dosyaları ayrıca incelenmedi.</p></div><p class="verification-note">Doğrulama kapsamı bölüm bazındadır. Sayısal eşleşme, araştırma varsayımlarının sağlandığını veya nedenselliği kanıtlamaz. İlk bölümlerin kayıtları kendi sayfalarındadır.</p></div></section>
<section class="closing shell"><p>Bir soruyla başlayın.</p><a href="b01.html">İlk bölüme geçin <span aria-hidden="true">↗</span></a></section></main>
<footer class="site-footer"><div class="shell footer-inner"><div><a class="home-brand" href="index.html"><span class="brand-mark">İ.</span><span>İstatistik <strong>Atölyesi</strong></span></a><p>İbrahim Güney<br>Olasılıktan Veriye ve İstatistiksel Çıkarıma</p></div><div class="footer-links"><a href="https://github.com/ibrahimguney/istatistik">GitHub deposu ↗</a><a href="YAYIN-DURUMU.md">Yayın ve doğrulama kapsamı</a><a href="yayin-manifest.json">Dosya bütünlüğü</a><a href="#icerik">Yukarı dön ↑</a></div></div><div class="shell footer-bottom"><span>2026 · Öğrenmek, uygulamak ve sorgulamak için.</span><span>Python · R · IBM SPSS</span></div></footer></body></html>'''
    (site/'index.html').write_text(html,encoding='utf-8')
