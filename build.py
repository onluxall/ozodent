# -*- coding: utf-8 -*-
"""Generator statycznej strony OzODent -> katalog public/.
Uruchom: python3 build.py   (wynik commitujemy; Vercel serwuje public/ bez budowania)"""
import html, os, datetime, json, re
from data import PRICES, ICON, TOOTH
from content import SERVICES

e = html.escape
OUT = "public"
SITE = "https://ozodent.vercel.app"  # zmień na https://www.ozodent.pl po podpięciu domeny
TEL = "572 555 193"
TEL_HREF = "tel:+48572555193"
MAIL = "kontakt@ozodent.pl"
ADDR = "ul. Listopadowa 9A, 95-035 Ozorków"
MAP_Q = "https://www.google.com/maps?q=ul.+Listopadowa+9A,+95-035+Ozork%C3%B3w&output=embed"
MAP_LINK = "https://www.google.com/maps/search/?api=1&query=ul.+Listopadowa+9A+Ozork%C3%B3w"
PRICE_BY_ID = {p[0]: p for p in PRICES}
CUR = ' aria-current="page"'
I = lambda k: f'<span class="i">{ICON[k]}</span>'

NAV = [("home", "/", "Strona główna"), ("o-nas", "/o-nas", "O nas"), ("uslugi", "/uslugi", "Usługi"),
       ("cennik", "/cennik", "Cennik"), ("aktualnosci", "/aktualnosci", "Aktualności"), ("kontakt", "/kontakt", "Kontakt")]

def logo(uid):
    return f'''<a class="logo" href="/" aria-label="OzODent Centrum Stomatologii – strona główna">
  <svg class="logo-mark" viewBox="0 0 48 52" aria-hidden="true"><defs><linearGradient id="lg{uid}" x1="0" x2="1"><stop offset=".52" stop-color="currentColor"/><stop offset=".52" stop-color="#c49a62"/></linearGradient></defs>
  <path d="{TOOTH}" fill="none" stroke="url(#lg{uid})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
  <span class="logo-text"><span class="logo-name">OzO<b>Dent</b></span><span class="logo-sub">Centrum Stomatologii</span></span>
</a>'''

def header(active):
    items = []
    for key, href, label in NAV:
        cur = ' class="active" aria-current="page"' if key == active else ""
        if key == "uslugi":
            sub = "".join(f'<li><a href="/uslugi/{s["slug"]}">{e(s["name"])}</a></li>' for s in SERVICES)
            items.append(f'<li class="has-sub"><a href="{href}"{cur}>{label}</a><ul class="sub">{sub}</ul></li>')
        else:
            items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return f'''<a class="skip" href="#main">Przejdź do treści</a>
<header>
  <div class="wrap nav">
    {logo("h")}
    <nav aria-label="Menu główne"><ul class="menu" id="menu">{"".join(items)}</ul></nav>
    <a class="btn" href="{TEL_HREF}">{I("cal")}Zapisy</a>
    <button class="burger" aria-label="Otwórz menu" aria-expanded="false" aria-controls="menu">{ICON["menu"]}</button>
  </div>
</header>'''

def footer():
    svc = "".join(f'<li><a href="/uslugi/{s["slug"]}">{e(s["name"])}</a></li>' for s in SERVICES[:8])
    nav = "".join(f'<li><a href="{h}">{l}</a></li>' for _, h, l in NAV)
    return f'''<section class="cta">
  <div class="wrap">
    <div class="cta-main rv">
      <div class="ic">{ICON["tooth"]}</div>
      <div>
        <h2>Zadbaj o swój uśmiech!</h2>
        <p>Umów się na wizytę już dziś.</p>
        <div class="cta-btns">
          <a class="btn" href="{TEL_HREF}">{I("cal")}Zapisz się na wizytę</a>
          <a class="tel" href="{TEL_HREF}">{I("phone")}{TEL}</a>
        </div>
      </div>
    </div>
    <div class="cta-feats">
      <div class="rv"><div class="ic">{ICON["pin"]}</div>Dogodna lokalizacja<br>w Ozorkowie</div>
      <div class="rv"><div class="ic">{ICON["car"]}</div>Parking<br>przed i za budynkiem</div>
      <div class="rv"><div class="ic">{ICON["clock"]}</div>Dogodne<br>godziny wizyt</div>
      <div class="rv"><div class="ic">{ICON["heart"]}</div>Przyjazna<br>atmosfera</div>
    </div>
  </div>
</section>
<footer>
  <div class="wrap f-grid">
    <div class="f-about">
      {logo("f")}
      <p>Ozorków, ul. Listopadowa 9A<br>(dawny Inkubator), koło Lidla</p>
      <p>Parking przed i za budynkiem<br>(wjazd przez bramę po lewej stronie paczkomatu)</p>
    </div>
    <div><h4>Nawigacja</h4><ul>{nav}</ul></div>
    <div><h4>Usługi</h4><ul>{svc}</ul></div>
    <div class="f-contact">
      <h4>Kontakt</h4>
      <ul>
        <li><span class="ic">{ICON["phone"]}</span><a href="{TEL_HREF}">{TEL}</a></li>
        <li><span class="ic">{ICON["mail"]}</span><a href="mailto:{MAIL}">{MAIL}</a></li>
        <li><span class="ic">{ICON["pin"]}</span><a href="{MAP_LINK}" target="_blank" rel="noopener">Wyznacz trasę</a></li>
        <li><span class="ic">{ICON["clock"]}</span><span>Pon – Pt: 8:00 – 20:00<br>Sobota: 8:00 – 14:00</span></li>
      </ul>
    </div>
  </div>
  <div class="f-bottom"><div class="wrap">
    <span>© {datetime.date.today().year} OzODent Centrum Stomatologii. Wszystkie prawa zastrzeżone.</span>
    <nav><a href="/polityka-prywatnosci">Polityka prywatności</a><a href="/regulamin">Regulamin</a></nav>
  </div></div>
</footer>
<a class="float-call" href="{TEL_HREF}" aria-label="Zadzwoń: {TEL}">{ICON["phone"]}</a>'''

SCHEMA = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Dentist","@id":"{SITE}/#gabinet","name":"OzODent Centrum Stomatologii","alternateName":"OzODent Ozorków","description":"Nowoczesny gabinet stomatologiczny w Ozorkowie – stomatologia zachowawcza i dziecięca, endodoncja, chirurgia stomatologiczna, protetyka, implanty, podcinanie wędzidełek, diagnostyka CBCT.",
"image":"{SITE}/assets/img/og.jpg","telephone":"+48572555193","email":"{MAIL}","url":"{SITE}",
"address":{{"@type":"PostalAddress","streetAddress":"ul. Listopadowa 9A","addressLocality":"Ozorków","postalCode":"95-035","addressCountry":"PL"}},
"openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"20:00"}},{{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"08:00","closes":"14:00"}}],
"areaServed":["Ozorków","Zgierz","Łęczyca","Łódź"],"hasMap":"{MAP_LINK}",
"employee":{{"@type":"Physician","name":"lek. dent. Małgorzata Pińkowska-Prasał","medicalSpecialty":"Chirurgia stomatologiczna"}},
"medicalSpecialty":"Dentistry","priceRange":"$$","currenciesAccepted":"PLN"}}</script>'''

_CRUMBS = []
def page(path, title, desc, active, body, extra_head=""):
    global _CRUMBS
    url = SITE + ("" if path == "/" else path)
    if path not in ("/", "/404") and _CRUMBS:
        items = [{"@type": "ListItem", "position": 1, "name": "Strona główna", "item": SITE + "/"}]
        for i, (h, l) in enumerate(_CRUMBS, 2):
            items.append({"@type": "ListItem", "position": i, "name": html.unescape(l), "item": SITE + (h or path)})
        extra_head += '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}, ensure_ascii=False) + "</script>"
    _CRUMBS = []
    full = title if path == "/" else f"{title} | OzODent Ozorków"
    doc = f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<script>document.documentElement.classList.add("js")</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:locale" content="pl_PL">
<meta property="og:title" content="{e(full)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#121212">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600&family=Montserrat:wght@400;500;600;700&family=Great+Vibes&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
{SCHEMA}{extra_head}
</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="/assets/js/main.js" defer></script>
</body>
</html>'''
    fp = os.path.join(OUT, "index.html" if path == "/" else path.strip("/") + ".html")
    os.makedirs(os.path.dirname(fp) or ".", exist_ok=True)
    open(fp, "w", encoding="utf-8").write(doc)
    return path

def page_hero(crumbs, h1, sub, img="korytarz.jpg"):
    global _CRUMBS
    _CRUMBS = list(crumbs)
    c = ['<a href="/">Strona główna</a>']
    for href, label in crumbs[:-1]:
        c += ['<span aria-hidden="true">/</span>', f'<a href="{href}">{label}</a>']
    c += ['<span aria-hidden="true">/</span>', f'<span>{crumbs[-1][1]}</span>']
    return f'''<section class="page-hero" style="--ph:url(/assets/img/{img})">
  <div class="wrap"><nav class="crumbs" aria-label="Okruszki">{"".join(c)}</nav>
  <h1>{h1}</h1><p>{sub}</p></div>
</section>'''

def price_list(pid, static=True):
    _, name, rows, notes = PRICE_BY_ID[pid]
    lis = "".join(f'<li><div class="pl-name">{e(t)}{f"<small>{e(s)}</small>" if s else ""}</div><div class="pl-price">{e(p)}</div></li>' for t, s, p in rows)
    nh = ""
    if notes:
        nh = '<div class="pl-notes">' + "".join(
            f'<div class="pl-note"><span class="chk">{ICON["check"]}</span><p><strong>{e(a)}</strong>{(" " + e(b)) if b else ""}</p></div>' for a, b in notes) + "</div>"
    return f'<ul class="pricelist">{lis}</ul>{nh}'

def price_tabs():
    tabs, panels = [], []
    for i, (pid, name, rows, notes) in enumerate(PRICES):
        sel = "true" if i == 0 else "false"
        tabs.append(f'<button class="tab" role="tab" id="t-{pid}" aria-controls="p-{pid}" aria-selected="{sel}" tabindex="{0 if i==0 else -1}" data-tab="{pid}">{e(name)}</button>')
        hidden = "" if i == 0 else " hidden"
        panels.append(f'<div class="panel" role="tabpanel" id="p-{pid}" aria-labelledby="t-{pid}" tabindex="0"{hidden}>{price_list(pid)}</div>')
    return f'<div class="tabs" role="tablist" aria-label="Kategorie cennika">{"".join(tabs)}</div>{"".join(panels)}'

def li_feat(icon, title, text):
    return f'<li><span class="ic">{ICON[icon]}</span><div><strong>{title}</strong><span>{text}</span></div></li>'

def promo_cards():
    def card(icon, title, who, items, price):
        lis = "".join(f'<li>{I("check")}{x}</li>' for x in items)
        return f'<article class="card rv"><div class="ci">{ICON[icon]}</div><h3>{title}</h3><div class="for">{who}</div><ul>{lis}</ul><div class="price">{price} <small>zł</small></div></article>'
    return '<div class="cards">' + card("tooth", "Konsultacja stomatologiczna", "dla dorosłych",
        ["przegląd jamy ustnej", "omówienie planu leczenia", "kosztorys", "zdjęcie pantomograficzne (OPG)"], 200) + \
        card("tooth-root", "Przegląd z ewaluacją ortodontyczną", "dla dzieci w okresie wymiany uzębienia",
        ["przegląd stomatologiczny", "ocena rozwoju uzębienia i zgryzu", "zdjęcie pantomograficzne (OPG)"], 150) + \
        card("baby", "Przegląd stomatologiczny", "dla dzieci", ["ocena stanu uzębienia", "wskazówki profilaktyczne", "indywidualne zalecenia"], 80) + '</div>'

VALUES = f'''<div class="values">
  <div class="rv"><div class="ic">{ICON["tooth"]}</div>Kompleksowa opieka</div>
  <div class="rv"><div class="ic">{ICON["people"]}</div>Indywidualne podejście</div>
  <div class="rv"><div class="ic">{ICON["micro"]}</div>Nowoczesny sprzęt</div>
  <div class="rv"><div class="ic">{ICON["heart"]}</div>Przyjazna atmosfera</div>
  <div class="rv"><div class="ic">{ICON["shield"]}</div>Komfort i bezpieczeństwo</div>
</div>'''

WHY = f'''<ul>
  {li_feat("micro","Nowoczesny sprzęt","CBCT, OPG, RVG – najwyższa jakość diagnostyki")}
  {li_feat("tooth","Kompleksowa opieka","Wszystkie dziedziny stomatologii w jednym miejscu")}
  {li_feat("doctor","Indywidualne podejście","Dbamy o komfort, bezpieczeństwo i zaufanie")}
  {li_feat("people","Możliwość sedacji","Farmakologicznej – dla większego komfortu")}
  {li_feat("chat","Współpraca z neurologopedą","Podcinanie wędzidełek u dzieci i dorosłych")}
</ul>'''

ABOUT_TXT = '''<p><b>OzODent Centrum Stomatologii</b> to nowoczesny gabinet w Ozorkowie, stworzony z myślą o komforcie i bezpieczeństwie Pacjentów.</p>
<p>Kieruję się pasją do chirurgii stomatologicznej i wieloletnim doświadczeniem, które zdobywałam, pracując przez 10 lat w tym mieście.</p>
<p>Moim celem jest kompleksowa opieka stomatologiczna na najwyższym poziomie.</p>'''

def map_block():
    return f'''<div class="map rv" id="map"><div class="map-ph">
  <span style="width:46px;height:46px;color:var(--gold-d)">{ICON["pin"]}</span>
  <strong style="color:var(--ink)">OzODent – {ADDR}</strong>
  <p>Mapa Google zostanie załadowana po kliknięciu (Google może zapisać pliki cookie).</p>
  <button class="btn btn-dark" type="button" data-map="{MAP_Q}">Pokaż mapę</button>
  <a class="more" href="{MAP_LINK}" target="_blank" rel="noopener">Otwórz w Google Maps →</a>
</div></div>'''

pages = []

# ---------------- HOME ----------------
SPECS6 = ["stomatologia-zachowawcza", "stomatologia-dziecieca", "endodoncja", "chirurgia", "protetyka", "medycyna-estetyczna"]
SHORT = {"stomatologia-zachowawcza": "Leczenie próchnicy, odbudowa zębów, kilka wypełnień na jednej wizycie",
         "stomatologia-dziecieca": "Przyjazne podejście, profilaktyka, leczenie dzieci w każdym wieku",
         "endodoncja": "Jednoetapowe leczenie kanałowe z najwyższą starannością",
         "chirurgia": "Pełen zakres zabiegów chirurgicznych, usuwanie ósemek, implanty",
         "protetyka": "Korony, mosty, protezy, odbudowy z bondingiem i estetyką",
         "medycyna-estetyczna": "Kwas hialuronowy, botoks, poprawa owalu twarzy"}
SV = {s["slug"]: s for s in SERVICES}
specs_html = "".join(
    f'<a class="spec rv" href="/uslugi/{k}"><div class="ic">{ICON[SV[k]["icon"]] if k!="chirurgia" else ICON["implant"]}</div><h3>{"Chirurgia" if k=="chirurgia" else e(SV[k]["name"])}</h3><p>{SHORT[k]}</p></a>' for k in SPECS6)

home = f'''<section class="hero hero-full">
  <div class="hero-bg"><img src="/assets/img/recepcja.jpg" alt="Recepcja gabinetu stomatologicznego OzODent w Ozorkowie" width="554" height="454" fetchpriority="high"></div>
  <div class="wrap">
    <div class="hero-copy">
      <p class="eyebrow">Dentysta Ozorków · Centrum Stomatologii</p>
      <h1>Nowoczesna stomatologia <em>dla całej rodziny</em></h1>
      <p class="lead">Kompleksowa opieka stomatologiczna w nowoczesnym gabinecie w Ozorkowie – z diagnostyką CBCT na miejscu i specjalistą chirurgii stomatologicznej.</p>
      <ul class="hero-feats">
        <li><span class="ic">{ICON["tooth"]}</span><div><strong>Nowoczesna diagnostyka</strong>CBCT, OPG, RVG</div></li>
        <li><span class="ic">{ICON["people"]}</span><div><strong>Doświadczenie</strong>i indywidualne podejście</div></li>
        <li><span class="ic">{ICON["shield"]}</span><div><strong>Komfort i bezpieczeństwo</strong>na najwyższym poziomie</div></li>
      </ul>
      <div class="hero-cta">
        <a class="btn" href="{TEL_HREF}">{I("cal")}Zapisz się na wizytę</a>
        <a class="tel" href="{TEL_HREF}">{I("phone")}{TEL}</a>
      </div>
    </div>
  </div>
  <a class="badge-open" href="/aktualnosci">Otwarcie gabinetu<b>z początkiem listopada 2026</b></a>
  <a class="scroll-hint" href="#specjalizacje" aria-label="Przewiń do specjalizacji"><span></span></a>
</section>

<section class="specs" id="specjalizacje">
  <div class="wrap">
    <h2 class="title rv">Nasze specjalizacje</h2>
    <div class="title-rule"></div>
    <div class="spec-grid">{specs_html}</div>
    <p class="also rv">Także: <a href="/uslugi/periodontologia">Periodontologia</a> · <a href="/uslugi/implanty">Implanty</a> · <a href="/uslugi/podcinanie-wedzidelek">Podcinanie wędzidełek</a> · <a href="/uslugi/higienizacja-wybielanie">Higienizacja i wybielanie</a> · <a href="/uslugi/diagnostyka-rtg">Diagnostyka CBCT i OPG</a></p>
  </div>
</section>

<section class="split">
  <div class="about">
    <div class="rv">
      <h2>O nas</h2>
      <p><b>OzODent Centrum Stomatologii</b> to nowoczesny gabinet w Ozorkowie, stworzony z myślą o komforcie i bezpieczeństwie Pacjentów – prowadzony przez specjalistę chirurgii stomatologicznej z 10-letnim doświadczeniem w tym mieście.</p>
      <div class="sig">Małgorzata Pińkowska-Prasał</div>
      <div class="sig-role">Lek. dent. – specjalista chirurgii stomatologicznej</div>
      <p style="margin-top:26px"><a class="more more-light" href="/o-nas">Poznaj nas bliżej →</a></p>
    </div>
    <div class="about-img"><img src="/assets/img/zab.jpg" alt="" width="194" height="312" loading="lazy"></div>
  </div>
  <div class="why"><h2 class="rv">Dlaczego my?</h2>{WHY}</div>
</section>

<section class="promo-band">
  <div class="wrap">
    <div class="pb-head rv">
      <div class="eyebrow">Promocja na otwarcie gabinetu</div>
      <h2>Pierwsza wizyta w&nbsp;cenie na start</h2>
      <p>Trwają zapisy przedwstępne – otwarcie z początkiem listopada.</p>
    </div>
    <ul class="pb-list rv">
      <li><b>200 zł</b><span>Konsultacja dla dorosłych<br><small>z OPG i kosztorysem</small></span></li>
      <li><b>150 zł</b><span>Przegląd z ewaluacją ortodontyczną<br><small>dzieci, z OPG</small></span></li>
      <li><b>80 zł</b><span>Przegląd stomatologiczny<br><small>dla dzieci</small></span></li>
    </ul>
    <div class="pb-cta rv"><a class="btn" href="/aktualnosci">Szczegóły promocji</a><a class="more" href="/cennik">Pełny cennik →</a></div>
  </div>
</section>'''
pages.append(page("/", "OzODent Centrum Stomatologii – Dentysta Ozorków | Chirurgia stomatologiczna",
     "OzODent – nowoczesny gabinet stomatologiczny w Ozorkowie (ul. Listopadowa 9A, koło Lidla). Stomatologia zachowawcza i dziecięca, endodoncja, chirurgia, protetyka, implanty, podcinanie wędzidełek, CBCT. Zapisy: 572 555 193.",
     "home", home))

# ---------------- O NAS ----------------
onas = page_hero([("/o-nas", "O nas")], 'Twój uśmiech <em>w najlepszych rękach</em>',
    "Nowopowstały, nowoczesny gabinet stomatologiczny w Ozorkowie – doświadczenie, precyzja i zaufanie.", "recepcja.jpg") + f'''
<section class="section alt">
  <div class="wrap doc">
    <div class="doc-card rv">
      <small>Lek. dent. · Specjalista chirurgii stomatologicznej</small>
      <h2>Małgorzata Pińkowska-Prasał</h2>
      <p>Doświadczenie. Precyzja. Zaufanie.</p>
      <div class="sig" style="margin-top:28px">Małgorzata Pińkowska-Prasał</div>
    </div>
    <div class="prose rv">
      <div class="eyebrow">O nas</div>
      <h2 style="margin-top:10px">Nowe miejsce na mapie Ozorkowa</h2>
      {ABOUT_TXT}
      <p>W OzODent łączymy specjalistyczną wiedzę chirurgiczną z kompleksową opieką dla całej rodziny – od profilaktyki i leczenia dzieci, przez stomatologię zachowawczą i endodoncję, po protetykę, implanty i medycynę estetyczną.</p>
      <p>Pracujemy w przyjaznej atmosferze, z cierpliwością i indywidualnym podejściem. Na miejscu wykonujemy pełną diagnostykę radiologiczną: RVG, OPG i tomografię CBCT.</p>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2 class="title rv">Nasz gabinet</h2><div class="title-rule"></div>
    <p class="lead-c">Nowoczesne, jasne wnętrza zaprojektowane z myślą o Twoim komforcie.</p>
    <div class="gallery">
      <figure class="rv"><img src="/assets/img/recepcja.jpg" alt="Recepcja OzODent Centrum Stomatologii w Ozorkowie" loading="lazy"></figure>
      <figure class="rv"><img src="/assets/img/korytarz.jpg" alt="Korytarz i poczekalnia gabinetu OzODent" loading="lazy"></figure>
      <figure class="rv"><img src="/assets/img/gabinet.jpg" alt="Wnętrze gabinetu stomatologicznego OzODent" loading="lazy"></figure>
    </div>
  </div>
</section>
<section class="section sand">
  <div class="wrap cols">
    <div class="why" style="padding:0;background:none"><h2 class="rv">Dlaczego my?</h2>{WHY}</div>
    <div class="box dark rv">
      <h3>Zapisy przedwstępne</h3>
      <p>Otwarcie gabinetu z początkiem listopada 2026. Zadzwoń i zarezerwuj termin już dziś.</p>
      <a class="tel" href="{TEL_HREF}">{I("phone")}{TEL}</a>
      <a class="btn" href="/aktualnosci">Promocja na otwarcie</a>
    </div>
  </div>
</section>
<section class="section alt"><div class="wrap">{VALUES}</div></section>'''
pages.append(page("/o-nas", "O nas – lek. dent. Małgorzata Pińkowska-Prasał",
     "Poznaj OzODent Centrum Stomatologii w Ozorkowie i lek. dent. Małgorzatę Pińkowską-Prasał – specjalistę chirurgii stomatologicznej.", "o-nas", onas))

# ---------------- USŁUGI ----------------
cards = "".join(f'<a class="svc rv" href="/uslugi/{s["slug"]}"><div class="ic">{ICON[s["icon"]]}</div><h3>{e(s["name"])}</h3><p>{e(s["short"])}</p><span class="more">Więcej →</span></a>' for s in SERVICES)
uslugi = page_hero([("/uslugi", "Usługi")], 'Zakres <em>usług</em>', "Wszystkie dziedziny stomatologii w jednym miejscu – od profilaktyki po zaawansowaną chirurgię.") + f'''
<section class="section"><div class="wrap">
  <h2 class="title rv">Kompleksowa opieka stomatologiczna</h2><div class="title-rule"></div>
  <div class="svc-grid">{cards}</div>
</div></section>'''
pages.append(page("/uslugi", "Usługi stomatologiczne", "Zakres usług OzODent w Ozorkowie: stomatologia zachowawcza i dziecięca, endodoncja, chirurgia, periodontologia, protetyka, implanty, wędzidełka, higienizacja, medycyna estetyczna, CBCT.", "uslugi", uslugi))

for s in SERVICES:
    scope = "".join(f'<li>{I("check")}{e(x)}</li>' for x in s["scope"])
    intro = "".join(f"<p>{e(p)}</p>" for p in s["intro"])
    ben = "".join(f'<div class="benefit rv"><div class="ic">{ICON[i]}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, t, d in s["benefits"])
    faq = "".join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in s["faq"])
    prices = ""
    for pid in s["prices"]:
        prices += f'<div class="price-block"><h3>Cennik – {e(PRICE_BY_ID[pid][1])}</h3><div class="panel static">{price_list(pid)}</div></div>'
    if not s["prices"]:
        prices = '<div class="price-block"><h3>Cena</h3><p>Koszt ustalamy indywidualnie po konsultacji i diagnostyce. W promocji na otwarcie konsultacja stomatologiczna z OPG i kosztorysem – <b>200 zł</b>.</p></div>'
    side = "".join(f'<li><a href="/uslugi/{x["slug"]}"{CUR if x is s else ""}>{e(x["name"])}<span>→</span></a></li>' for x in SERVICES)
    faq_ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]}, ensure_ascii=False) + "</script>"
    idx = SERVICES.index(s)
    rel = [SERVICES[(idx + k) % len(SERVICES)] for k in (1, 2, 3)]
    rel_html = "".join(f'<a class="svc rv" href="/uslugi/{x["slug"]}"><div class="ic">{ICON[x["icon"]]}</div><h3>{e(x["name"])}</h3><p>{e(x["short"])}</p><span class="more">Więcej →</span></a>' for x in rel)
    offers = []
    for pid in s["prices"]:
        for t, sub, p in PRICE_BY_ID[pid][2]:
            nums = [int(n) for n in re.findall(r"\d+", p.replace(" ", ""))]
            if not nums: continue
            o = {"@type": "Offer", "name": t, "priceCurrency": "PLN"}
            if len(nums) == 1 and not p.startswith("od"): o["price"] = nums[0]
            else:
                ps = {"@type": "PriceSpecification", "priceCurrency": "PLN", "minPrice": nums[0]}
                if len(nums) > 1 and "/" not in p: ps["maxPrice"] = nums[-1]
                o["priceSpecification"] = ps
            offers.append(o)
    svc_ld = {"@context": "https://schema.org", "@type": "Service", "name": s["name"] + " Ozorków", "serviceType": s["name"],
              "description": s["short"], "areaServed": {"@type": "City", "name": "Ozorków"},
              "provider": {"@id": SITE + "/#gabinet"}, "url": f"{SITE}/uslugi/{s['slug']}"}
    if offers: svc_ld["offers"] = offers[:20]
    faq_ld += '<script type="application/ld+json">' + json.dumps(svc_ld, ensure_ascii=False) + "</script>"
    body = page_hero([("/uslugi", "Usługi"), ("", e(s["name"]))], e(s["name"]), e(s["hero"])) + f'''
<section class="section alt"><div class="wrap cols">
  <article class="prose rv">
    <h2>{e(s["name"])} w OzODent</h2>
    {intro}
    <h3>Zakres zabiegów</h3>
    <ul class="ticks">{scope}</ul>
    {prices}
    <p style="margin-top:24px"><a class="more" href="/cennik">Pełny cennik →</a></p>
  </article>
  <aside class="aside">
    <div class="box dark"><h3>Umów wizytę</h3><p>Zapisy przedwstępne – otwarcie z początkiem listopada 2026.</p>
      <a class="tel" href="{TEL_HREF}">{I("phone")}{TEL}</a><a class="btn" href="{TEL_HREF}">{I("cal")}Zadzwoń teraz</a></div>
    <div class="box"><h3>Usługi</h3><ul>{side}</ul></div>
  </aside>
</div></section>
<section class="section"><div class="wrap">
  <h2 class="title rv">Dlaczego OzODent?</h2><div class="title-rule"></div>
  <div class="benefits">{ben}</div>
</div></section>
<section class="section sand"><div class="wrap">
  <h2 class="title rv">Najczęstsze pytania</h2><div class="title-rule"></div>
  <div class="faq">{faq}</div>
</div></section>
<section class="section alt"><div class="wrap">
  <h2 class="title rv">Zobacz także</h2><div class="title-rule"></div>
  <div class="svc-grid">{rel_html}</div>
</div></section>'''
    pages.append(page(f"/uslugi/{s['slug']}", f"{s['name']} Ozorków", f"{s['name']} w OzODent Ozorków – {s['short']} Zapisy: {TEL}.", "uslugi", body, faq_ld))

# ---------------- CENNIK ----------------
cennik = page_hero([("/cennik", "Cennik")], 'Cennik <em>usług</em>', "Przejrzyste ceny zabiegów. Dokładny koszt leczenia ustalamy indywidualnie podczas konsultacji.") + f'''
<section class="pricing" style="padding-top:64px"><div class="wrap">
  {price_tabs()}
  <p class="disclaimer">Cennik ma charakter informacyjny i nie stanowi oferty handlowej w rozumieniu art. 66 § 1 Kodeksu cywilnego.</p>
</div></section>
<section class="promo" style="padding-top:40px"><div class="wrap">
  <div class="promo-head rv"><div class="eyebrow">Promocja na otwarcie</div><h2 style="font-size:36px">Pakiety na start</h2><div class="title-rule"></div></div>
  {promo_cards()}
</div></section>'''
pages.append(page("/cennik", "Cennik – dentysta Ozorków", "Cennik OzODent Ozorków: stomatologia zachowawcza, chirurgia, periodontologia, podcinanie wędzidełek, higienizacja i wybielanie, RTG i CBCT.", "cennik", cennik))

# ---------------- AKTUALNOŚCI ----------------
akt = page_hero([("/aktualnosci", "Aktualności")], 'Aktualności', "Nowości z OzODent Centrum Stomatologii.") + f'''
<section class="section alt"><div class="wrap">
  <div class="news">
    <article class="post rv" id="promocja-na-otwarcie">
      <div class="post-img"><img src="/assets/img/recepcja.jpg" alt="Recepcja OzODent – promocja na otwarcie gabinetu" loading="lazy"></div>
      <div class="post-body">
        <time datetime="2026-10-01">Październik 2026</time>
        <h2>Promocja na otwarcie gabinetu</h2>
        <p>Z początkiem listopada otwieramy OzODent Centrum Stomatologii w Ozorkowie. Z tej okazji przygotowaliśmy specjalne ceny na pierwsze wizyty. Trwają zapisy przedwstępne pod numerem <a href="{TEL_HREF}"><b>{TEL}</b></a>.</p>
        <ul class="ticks prose" style="list-style:none;padding:0;display:grid;gap:8px">
          <li>{I("check")}<span>Konsultacja stomatologiczna dla dorosłych z OPG i kosztorysem – <b>200 zł</b></span></li>
          <li>{I("check")}<span>Przegląd z ewaluacją ortodontyczną dla dzieci z OPG – <b>150 zł</b></span></li>
          <li>{I("check")}<span>Przegląd stomatologiczny dla dzieci – <b>80 zł</b></span></li>
        </ul>
      </div>
    </article>
    <article class="post rv">
      <div class="post-img"><img src="/assets/img/gabinet.jpg" alt="Nowy gabinet stomatologiczny OzODent w Ozorkowie" loading="lazy"></div>
      <div class="post-body">
        <time datetime="2026-09-15">Wrzesień 2026</time>
        <h2>Nowe miejsce na mapie Ozorkowa</h2>
        <p>Nowopowstały, nowoczesny gabinet stomatologiczny przy ul. Listopadowej 9A (dawny Inkubator, koło Lidla). Na miejscu diagnostyka CBCT i OPG, pełen zakres zabiegów chirurgicznych, endodoncja jednoetapowa, stomatologia dziecięca i podcinanie wędzidełek we współpracy z neurologopedą.</p>
        <p>Parking dostępny przed i za budynkiem.</p>
        <a class="more" href="/o-nas">Poznaj gabinet →</a>
      </div>
    </article>
  </div>
</div></section>
<section class="promo"><div class="wrap">{promo_cards()}</div></section>'''
pages.append(page("/aktualnosci", "Aktualności – promocja na otwarcie", "Promocja na otwarcie OzODent w Ozorkowie: konsultacja z OPG 200 zł, przegląd ortodontyczny dziecka 150 zł, przegląd dziecka 80 zł. Zapisy przedwstępne: 572 555 193.", "aktualnosci", akt))

# ---------------- KONTAKT ----------------
opts = "".join(f"<option>{e(s['name'])}</option>" for s in SERVICES)
kontakt = page_hero([("/kontakt", "Kontakt")], 'Kontakt <em>i dojazd</em>', "Zapraszamy do OzODent – ul. Listopadowa 9A w Ozorkowie, dawny Inkubator, koło Lidla.") + f'''
<section class="contact"><div class="wrap">
  <div class="rv">
    <ul class="c-list">
      <li><span class="ic">{ICON["pin"]}</span><div><strong>Ozorków</strong><span>ul. Listopadowa 9A<br>dawny Inkubator – koło Lidla</span></div></li>
      <li><span class="ic">{ICON["phone"]}</span><div><strong>Zapisy przedwstępne</strong><a href="{TEL_HREF}">{TEL}</a></div></li>
      <li><span class="ic">{ICON["mail"]}</span><div><strong>E-mail</strong><a href="mailto:{MAIL}">{MAIL}</a></div></li>
      <li><span class="ic">{ICON["car"]}</span><div><strong>Parking</strong><span>Przed i za budynkiem (wjazd przez bramę po lewej stronie paczkomatu)</span></div></li>
    </ul>
    <div class="box"><h3>Godziny otwarcia</h3>
      <table class="hours"><tr><td>Poniedziałek – Piątek</td><td>8:00 – 20:00</td></tr><tr><td>Sobota</td><td>8:00 – 14:00</td></tr><tr><td>Niedziela</td><td>nieczynne</td></tr></table>
    </div>
  </div>
  {map_block()}
</div></section>
<section class="section alt"><div class="wrap cols">
  <div class="rv">
    <div class="eyebrow">Formularz</div>
    <h2 style="font-size:34px;margin:10px 0 10px">Napisz do nas</h2>
    <p class="form-note" style="margin-bottom:24px">Najszybciej umówisz wizytę telefonicznie: <a href="{TEL_HREF}"><b>{TEL}</b></a>. Formularz otworzy Twój program pocztowy z gotową wiadomością do gabinetu.</p>
    <form class="form" id="contact-form" data-mail="{MAIL}" novalidate>
      <div class="row">
        <label>Imię i nazwisko<input name="name" required autocomplete="name"></label>
        <label>Telefon<input name="phone" type="tel" required autocomplete="tel" pattern="[0-9 +()-]{{9,}}"></label>
      </div>
      <div class="row">
        <label>E-mail (opcjonalnie)<input name="email" type="email" autocomplete="email"></label>
        <label>Usługa<select name="service"><option>Konsultacja / przegląd</option>{opts}</select></label>
      </div>
      <label>Wiadomość<textarea name="message" placeholder="Preferowane dni i godziny wizyty, krótki opis problemu…"></textarea></label>
      <label class="consent"><input type="checkbox" name="consent" required> <span>Zapoznałem/am się z <a href="/polityka-prywatnosci" style="text-decoration:underline">polityką prywatności</a> i wyrażam zgodę na kontakt w celu umówienia wizyty.</span></label>
      <div class="form-msg" role="status" aria-live="polite"></div>
      <div><button class="btn btn-dark" type="submit">{I("mail")}Wyślij wiadomość</button></div>
    </form>
  </div>
  <aside class="aside"><div class="box dark"><h3>Zadzwoń</h3><p>Zapisy przedwstępne – otwarcie z początkiem listopada 2026.</p>
    <a class="tel" href="{TEL_HREF}">{I("phone")}{TEL}</a><a class="btn" href="{TEL_HREF}">{I("cal")}Zadzwoń teraz</a></div></aside>
</div></section>'''
pages.append(page("/kontakt", "Kontakt i dojazd", "Kontakt z OzODent: ul. Listopadowa 9A, Ozorków (dawny Inkubator, koło Lidla). Tel. 572 555 193, kontakt@ozodent.pl. Pon–Pt 8–20, Sob 8–14.", "kontakt", kontakt))

# ---------------- PRAWNE ----------------
privacy = page_hero([("/polityka-prywatnosci", "Polityka prywatności")], "Polityka prywatności", "Informacje o przetwarzaniu danych osobowych (RODO).") + f'''
<section class="section alt"><div class="wrap legal prose">
<h2>1. Administrator danych</h2>
<p>Administratorem danych osobowych jest OzODent Centrum Stomatologii, {ADDR}, e-mail: <a href="mailto:{MAIL}">{MAIL}</a>, tel. {TEL}.</p>
<h2>2. Cele i podstawy przetwarzania</h2>
<ul>
<li>umówienie wizyty i kontakt z Pacjentem – art. 6 ust. 1 lit. b i f RODO;</li>
<li>udzielanie świadczeń zdrowotnych i prowadzenie dokumentacji medycznej – art. 9 ust. 2 lit. h RODO w zw. z ustawą o prawach pacjenta i Rzeczniku Praw Pacjenta;</li>
<li>rozliczenia i obowiązki podatkowe – art. 6 ust. 1 lit. c RODO;</li>
<li>dochodzenie lub obrona roszczeń – art. 6 ust. 1 lit. f RODO.</li>
</ul>
<h2>3. Okres przechowywania</h2>
<p>Dokumentację medyczną przechowujemy przez okres wymagany przepisami (co do zasady 20 lat od ostatniego wpisu). Dane z korespondencji – do czasu zakończenia sprawy, a następnie przez okres przedawnienia ewentualnych roszczeń.</p>
<h2>4. Odbiorcy danych</h2>
<p>Dane mogą być przekazywane podmiotom wspierającym działalność gabinetu (np. dostawcom systemów IT, poczty e-mail, hostingu, biuru rachunkowemu, laboratoriom) wyłącznie w niezbędnym zakresie oraz organom uprawnionym na podstawie przepisów prawa.</p>
<h2>5. Prawa osoby, której dane dotyczą</h2>
<p>Przysługuje Ci prawo dostępu do danych, ich sprostowania, usunięcia, ograniczenia przetwarzania, przenoszenia oraz wniesienia sprzeciwu, a także prawo wniesienia skargi do Prezesa Urzędu Ochrony Danych Osobowych (ul. Stawki 2, 00-193 Warszawa).</p>
<h2>6. Formularz kontaktowy</h2>
<p>Formularz na stronie nie wysyła danych na serwer – otwiera Twój program pocztowy z przygotowaną wiadomością. Dane przetwarzamy dopiero po otrzymaniu wiadomości e-mail.</p>
<h2>7. Pliki cookie i usługi zewnętrzne</h2>
<p>Strona nie używa własnych plików cookie analitycznych ani marketingowych. Czcionki ładowane są z Google Fonts. Mapa Google ładuje się dopiero po kliknięciu przycisku „Pokaż mapę” – wówczas Google może przetwarzać dane zgodnie z własną polityką prywatności. Hostingiem strony jest Vercel Inc., który może rejestrować techniczne logi serwera (np. adres IP).</p>
<h2>8. Zmiany</h2>
<p>Polityka może być aktualizowana. Aktualna wersja jest zawsze dostępna na tej stronie.</p>
</div></section>'''
pages.append(page("/polityka-prywatnosci", "Polityka prywatności", "Polityka prywatności i informacja RODO OzODent Centrum Stomatologii.", "", privacy))

reg = page_hero([("/regulamin", "Regulamin")], "Regulamin", "Zasady korzystania ze strony i rejestracji wizyt.") + f'''
<section class="section alt"><div class="wrap legal prose">
<h2>1. Postanowienia ogólne</h2>
<p>Strona internetowa ma charakter informacyjny i prezentuje usługi OzODent Centrum Stomatologii, {ADDR}.</p>
<h2>2. Rejestracja wizyt</h2>
<p>Wizyty umawiane są telefonicznie pod numerem {TEL} lub poprzez kontakt e-mail. Termin wizyty jest wiążący po jego potwierdzeniu przez rejestrację gabinetu.</p>
<p>W przypadku braku możliwości przybycia prosimy o możliwie wcześniejsze odwołanie lub przełożenie wizyty.</p>
<h2>3. Ceny</h2>
<p>Ceny podane na stronie mają charakter informacyjny i nie stanowią oferty handlowej w rozumieniu art. 66 § 1 Kodeksu cywilnego. Ostateczny koszt leczenia ustalany jest indywidualnie, po konsultacji i diagnostyce.</p>
<h2>4. Promocje</h2>
<p>Warunki promocji na otwarcie gabinetu określone są w zakładce <a href="/aktualnosci">Aktualności</a>. Promocje nie łączą się, o ile nie wskazano inaczej.</p>
<h2>5. Treści na stronie</h2>
<p>Treści zamieszczone na stronie nie zastępują konsultacji lekarskiej. Prawa do treści i grafik przysługują ich właścicielom.</p>
<h2>6. Kontakt</h2>
<p>Pytania i uwagi dotyczące strony prosimy kierować na adres <a href="mailto:{MAIL}">{MAIL}</a>.</p>
</div></section>'''
pages.append(page("/regulamin", "Regulamin", "Regulamin strony i rejestracji wizyt OzODent Centrum Stomatologii.", "", reg))

err = f'''<section class="err"><div class="wrap">
  <div class="big">404</div><h1 style="font-size:36px;margin:12px 0">Nie znaleziono strony</h1>
  <p style="color:var(--muted);margin:0 0 28px">Strona mogła zostać przeniesiona lub nie istnieje.</p>
  <a class="btn" href="/">Wróć na stronę główną</a> &nbsp; <a class="btn btn-dark" href="{TEL_HREF}">{I("phone")}{TEL}</a>
</div></section>'''
page("/404", "Nie znaleziono strony", "Strona nie istnieje.", "", err, '<meta name="robots" content="noindex">')

# ---------------- SEO files ----------------
today = datetime.date.today().isoformat()
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f'  <url><loc>{SITE}{"" if p=="/" else p}</loc><lastmod>{today}</lastmod><priority>{"1.0" if p=="/" else "0.8" if p.count("/")==1 else "0.7"}</priority></url>\n' for p in pages) + "</urlset>\n"
open(f"{OUT}/sitemap.xml", "w").write(sm)
open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("Wygenerowano", len(pages), "stron")
