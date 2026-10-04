# -*- coding: utf-8 -*-
"""Generator statycznej strony OzODent -> katalog public/.
Uruchom: python3 build.py   (wynik commitujemy; Vercel serwuje public/ bez budowania)

ZASADA: na stronie są wyłącznie informacje dostarczone przez klienta
(cenniki, ulotki, makieta). Nie dopisujemy cen ani faktów z głowy."""
import html, os, datetime, json, re
from data import PRICES, ICON, TOOTH, svg
from content import SERVICES

e = html.escape
OUT = "public"
SITE = "https://ozodent.vercel.app"  # zmień na https://www.ozodent.pl po podpięciu domeny
TEL = "572 555 193"
TEL_HREF = "tel:+48572555193"
MAIL = "kontakt@ozodent.pl"
ADDR = "ul. Listopadowa 9A, Ozorków"
MAP_Q = "https://www.google.com/maps?q=ul.+Listopadowa+9A,+Ozork%C3%B3w&output=embed"
MAP_LINK = "https://www.google.com/maps/search/?api=1&query=ul.+Listopadowa+9A+Ozork%C3%B3w"
PRICE_BY_ID = {p[0]: p for p in PRICES}
SV = {s["slug"]: s for s in SERVICES}
CUR = ' aria-current="page"'

# ---- dodatkowe, wyraźnie różne ikony (żeby obok siebie nie stały podobne) ----
ICON.update({
  "drill":   svg('<circle cx="30" cy="16" r="10"/><circle cx="30" cy="16" r="5.5"/><path d="M23 23L8 40"/>'),
  "scalpel": svg('<path d="M6 42l17-17"/><path d="M23 25L37 7c4 4 4.5 10 .5 14.5L27 29z"/>'),
  "drop":    svg('<path d="M24 6s12 14 12 23a12 12 0 01-24 0C12 20 24 6 24 6z"/><path d="M18 30c0 4 3 6.5 6.5 6.5"/>'),
  "crown":   svg('<path d="M12 22c0-8 5-13 12-13s12 5 12 13v5H12z"/><path d="M14 27l3 13h14l3-13"/><path d="M19 21h10"/>'),
  "mouth":   svg('<path d="M5 24c6-8 12-10 19-6 7-4 13-2 19 6-6 8-12 11-19 11S11 32 5 24z"/><path d="M5 24h38"/>'),
  "brush":   svg('<path d="M4 34h22c2 0 3-1 4-2h14v6H30c-1-1-2-2-4-2H4z"/><path d="M31 32V20M35 32V18M39 32V20M43 32V22"/>'),
  "scan":    svg('<rect x="6" y="10" width="36" height="28" rx="3"/><path d="M12 29c4-6 8-8 12-8s8 2 12 8"/><path d="M16 27v4M20 24v5M24 23v5M28 24v5M32 27v4"/>'),
  "award":   svg('<circle cx="24" cy="18" r="11"/><path d="M17 27l-4 15 11-6 11 6-4-15"/><path d="M19 18l4 4 7-7"/>'),
  "clipboard": svg('<rect x="11" y="8" width="26" height="34" rx="3"/><path d="M18 8V5h12v3"/><path d="M17 20h14M17 27h14M17 34h8"/>'),
})
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
        cur = ' class="active"' + CUR if key == active else ""
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
    <a class="hdr-call" href="{TEL_HREF}" aria-label="Zadzwoń: {TEL}">{ICON["phone"]}</a>
    <button class="burger" aria-label="Otwórz menu" aria-expanded="false" aria-controls="menu">{ICON["menu"]}</button>
  </div>
</header>'''

def cta(full):
    feats = ""
    if full:
        feats = f'''<div class="cta-feats">
      <div class="rv"><div class="ic">{ICON["pin"]}</div>Dogodna lokalizacja<br>w Ozorkowie</div>
      <div class="rv"><div class="ic">{ICON["car"]}</div>Parking<br>przed i za budynkiem</div>
      <div class="rv"><div class="ic">{ICON["clock"]}</div>Dogodne<br>godziny wizyt</div>
      <div class="rv"><div class="ic">{ICON["heart"]}</div>Przyjazna<br>atmosfera</div>
    </div>'''
    return f'''<section class="cta{'' if full else ' cta-slim'}">
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
    {feats}
  </div>
</section>'''

def footer():
    svc = "".join(f'<li><a href="/uslugi/{s["slug"]}">{e(s["name"])}</a></li>' for s in SERVICES)
    nav = "".join(f'<li><a href="{h}">{l}</a></li>' for _, h, l in NAV)
    return f'''<footer>
  <div class="wrap f-grid">
    <div class="f-about">
      {logo("f")}
      <p>Ozorków, ul. Listopadowa 9A<br>(dawny Inkubator), koło Lidla</p>
      <p>Parking przed i za budynkiem<br>(wjazd przez bramę po lewej stronie paczkomatu)</p>
    </div>
    <div><h4>Nawigacja</h4><ul>{nav}</ul></div>
    <div><h4>Usługi</h4><ul class="f-svc">{svc}</ul></div>
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
    <nav><a href="/polityka-prywatnosci">Polityka prywatności</a></nav>
  </div></div>
</footer>'''

SCHEMA = '<script type="application/ld+json">' + json.dumps({
  "@context": "https://schema.org", "@type": "Dentist", "@id": SITE + "/#gabinet",
  "name": "OzODent Centrum Stomatologii", "url": SITE, "image": SITE + "/assets/img/og.jpg",
  "telephone": "+48572555193", "email": MAIL,
  "address": {"@type": "PostalAddress", "streetAddress": "ul. Listopadowa 9A", "addressLocality": "Ozorków", "addressCountry": "PL"},
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "20:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "08:00", "closes": "14:00"}],
  "employee": {"@type": "Physician", "name": "lek. dent. Małgorzata Pińkowska-Prasał", "medicalSpecialty": "Chirurgia stomatologiczna"},
  "hasMap": MAP_LINK, "medicalSpecialty": "Dentistry"}, ensure_ascii=False) + "</script>"

_CRUMBS = []
def page(path, title, desc, active, body, extra_head="", cta_full=False):
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
{cta(cta_full) if path != "/404" else ""}
{footer()}
<script src="/assets/js/main.js" defer></script>
</body>
</html>'''
    fp = os.path.join(OUT, "index.html" if path == "/" else path.strip("/") + ".html")
    os.makedirs(os.path.dirname(fp) or ".", exist_ok=True)
    open(fp, "w", encoding="utf-8").write(doc)
    return path

def page_hero(crumbs, h1, sub="", img="korytarz.jpg"):
    global _CRUMBS
    _CRUMBS = list(crumbs)
    c = ['<a href="/">Strona główna</a>']
    for href, label in crumbs[:-1]:
        c += ['<span aria-hidden="true">/</span>', f'<a href="{href}">{label}</a>']
    c += ['<span aria-hidden="true">/</span>', f'<span>{crumbs[-1][1]}</span>']
    subh = f"<p>{sub}</p>" if sub else ""
    return f'''<section class="page-hero" style="--ph:url(/assets/img/{img})">
  <div class="wrap"><nav class="crumbs" aria-label="Okruszki">{"".join(c)}</nav>
  <h1>{h1}</h1>{subh}</div>
</section>'''

def rows_html(rows, notes):
    lis = "".join(f'<li><div class="pl-name">{e(t)}{f"<small>{e(s)}</small>" if s else ""}</div><div class="pl-price">{e(p)}</div></li>' for t, s, p in rows)
    nh = ""
    if notes:
        nh = '<div class="pl-notes">' + "".join(
            f'<div class="pl-note"><span class="chk">{ICON["check"]}</span><p><strong>{e(a)}</strong>{(" " + e(b)) if b else ""}</p></div>' for a, b in notes) + "</div>"
    return f'<ul class="pricelist">{lis}</ul>{nh}'

def resolve_prices(spec):
    if isinstance(spec, str):
        _, name, rows, notes = PRICE_BY_ID[spec]
        return name, rows, notes
    return spec

def price_tabs():
    tabs, panels = [], []
    for i, (pid, name, rows, notes) in enumerate(PRICES):
        sel = "true" if i == 0 else "false"
        tabs.append(f'<button class="tab" role="tab" id="t-{pid}" aria-controls="p-{pid}" aria-selected="{sel}" tabindex="{0 if i==0 else -1}" data-tab="{pid}">{e(name)}</button>')
        hidden = "" if i == 0 else " hidden"
        panels.append(f'<div class="panel" role="tabpanel" id="p-{pid}" aria-labelledby="t-{pid}" tabindex="0"{hidden}>{rows_html(rows, notes)}</div>')
    return f'<div class="tabs" role="tablist" aria-label="Kategorie cennika">{"".join(tabs)}</div>{"".join(panels)}'

def offers_ld(rows):
    out = []
    for t, sub, p in rows:
        nums = [int(n) for n in re.findall(r"\d+", p.replace(" ", ""))]
        if not nums: continue
        o = {"@type": "Offer", "name": t, "priceCurrency": "PLN"}
        if len(nums) == 1 and not p.startswith("od"): o["price"] = nums[0]
        else:
            ps = {"@type": "PriceSpecification", "priceCurrency": "PLN", "minPrice": nums[0]}
            if len(nums) > 1 and "/" not in p: ps["maxPrice"] = nums[-1]
            o["priceSpecification"] = ps
        out.append(o)
    return out

def promo_cards():
    def card(icon, title, who, items, price):
        lis = "".join(f'<li>{I("check")}{x}</li>' for x in items)
        return f'<article class="card rv"><div class="ci">{ICON[icon]}</div><h3>{title}</h3><div class="for">{who}</div><ul>{lis}</ul><div class="price">{price} <small>zł</small></div></article>'
    return '<div class="cards">' + \
        card("clipboard", "Konsultacja stomatologiczna", "dla dorosłych", ["przegląd jamy ustnej", "omówienie planu leczenia", "kosztorys", "zdjęcie pantomograficzne (OPG)"], 200) + \
        card("scan", "Przegląd z ewaluacją ortodontyczną", "dla dzieci w okresie wymiany uzębienia", ["przegląd stomatologiczny", "ocena rozwoju uzębienia i zgryzu", "zdjęcie pantomograficzne (OPG)"], 150) + \
        card("baby", "Przegląd stomatologiczny", "dla dzieci", ["ocena stanu uzębienia", "wskazówki profilaktyczne", "indywidualne zalecenia"], 80) + '</div>'

def li_feat(icon, title, text):
    return f'<li><span class="ic">{ICON[icon]}</span><div><strong>{title}</strong><span>{text}</span></div></li>'

def map_block():
    return f'''<div class="map rv" id="map"><div class="map-ph">
  <span style="width:46px;height:46px;color:var(--gold-d)">{ICON["pin"]}</span>
  <strong style="color:var(--ink)">OzODent – {ADDR}</strong>
  <p>Mapa Google zostanie załadowana po kliknięciu.</p>
  <button class="btn btn-dark" type="button" data-map="{MAP_Q}">Pokaż mapę</button>
  <a class="more" href="{MAP_LINK}" target="_blank" rel="noopener">Otwórz w Google Maps →</a>
</div></div>'''

pages = []

# ================= STRONA GŁÓWNA (krótko) =================
SPECS6 = [("stomatologia-zachowawcza", "Stomatologia zachowawcza", "Leczenie próchnicy, odbudowa zębów, nowoczesne wypełnienia"),
          ("stomatologia-dziecieca", "Stomatologia dziecięca", "Przyjazne podejście, profilaktyka, leczenie dzieci w każdym wieku"),
          ("endodoncja", "Endodoncja", "Jednoetapowe leczenie kanałowe z najwyższą starannością"),
          ("chirurgia", "Chirurgia", "Pełen zakres zabiegów chirurgicznych, usuwanie ósemek, implanty"),
          ("protetyka", "Protetyka", "Korony, mosty, protezy, odbudowy z bondingiem i estetyką"),
          ("medycyna-estetyczna", "Medycyna estetyczna", "Kwas hialuronowy, botoks, poprawa owalu twarzy")]
specs_html = "".join(f'<a class="spec rv" href="/uslugi/{k}"><div class="ic">{ICON[SV[k]["icon"]]}</div><h3>{t}</h3><p>{d}</p></a>' for k, t, d in SPECS6)
also = '<span class="dot" aria-hidden="true">·</span>'.join(f'<a href="/uslugi/{k}">{e(SV[k]["name"])}</a>' for k in ["periodontologia", "implanty", "podcinanie-wedzidelek", "higienizacja-wybielanie", "diagnostyka-rtg"])

home = f'''<section class="hero hero-full">
  <div class="hero-bg"><img src="/assets/img/recepcja.jpg" alt="Recepcja gabinetu stomatologicznego OzODent w Ozorkowie" width="554" height="454" fetchpriority="high"></div>
  <div class="wrap">
    <div class="hero-copy">
      <p class="eyebrow">Dentysta Ozorków · Centrum Stomatologii</p>
      <h1>Nowoczesna stomatologia <em>dla całej rodziny</em></h1>
      <p class="lead">Kompleksowa opieka stomatologiczna w nowoczesnym gabinecie wyposażonym w najnowsze technologie.</p>
      <ul class="hero-feats">
        <li><span class="ic">{ICON["scan"]}</span><div><strong>Nowoczesna diagnostyka</strong>CBCT, OPG, RVG</div></li>
        <li><span class="ic">{ICON["award"]}</span><div><strong>Doświadczenie</strong>i indywidualne podejście</div></li>
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
    <p class="also rv">Także: {also}</p>
  </div>
</section>

<section class="split">
  <div class="about">
    <div class="rv">
      <h2>O nas</h2>
      <p><b>OzODent Centrum Stomatologii</b> to nowoczesny gabinet w Ozorkowie, stworzony z myślą o komforcie i bezpieczeństwie Pacjentów.</p>
      <p>Kieruję się pasją do chirurgii stomatologicznej i wieloletnim doświadczeniem, które zdobywałam, pracując przez 10 lat w tym mieście.</p>
      <div class="sig">Małgorzata Pińkowska-Prasał</div>
      <div class="sig-role">Lek. dent. – specjalista chirurgii stomatologicznej</div>
      <p class="about-more"><a class="more more-light" href="/o-nas">Poznaj nas bliżej →</a></p>
    </div>
    <div class="about-img"><img src="/assets/img/zab.jpg" alt="" width="194" height="312" loading="lazy"></div>
  </div>
  <div class="why"><h2 class="rv">Dlaczego my?</h2>
    <ul>
      {li_feat("tooth", "Kompleksowa opieka", "Wszystkie dziedziny stomatologii w jednym miejscu")}
      {li_feat("syringe", "Możliwość sedacji", "Farmakologicznej – dla większego komfortu")}
      {li_feat("chat", "Współpraca z neurologopedą", "Podcinanie wędzidełek u dzieci i dorosłych")}
    </ul>
  </div>
</section>

<section class="promo-band">
  <div class="wrap">
    <div class="pb-head rv">
      <div class="eyebrow">Z początkiem listopada</div>
      <h2>Promocja na otwarcie gabinetu</h2>
      <p>Trwają zapisy przedwstępne.</p>
      <a class="btn" href="/aktualnosci">Szczegóły promocji</a>
    </div>
    <ul class="pb-list rv">
      <li><b>200 zł</b><span>Konsultacja stomatologiczna<br><small>dla dorosłych</small></span></li>
      <li><b>150 zł</b><span>Przegląd z ewaluacją ortodontyczną<br><small>dla dzieci</small></span></li>
      <li><b>80 zł</b><span>Przegląd stomatologiczny<br><small>dla dzieci</small></span></li>
    </ul>
  </div>
</section>'''
pages.append(page("/", "OzODent Centrum Stomatologii – Dentysta Ozorków",
     "OzODent – nowoczesny gabinet stomatologiczny w Ozorkowie, ul. Listopadowa 9A (dawny Inkubator, koło Lidla). Stomatologia zachowawcza i dziecięca, endodoncja, chirurgia, protetyka, implanty, diagnostyka CBCT. Zapisy: 572 555 193.",
     "home", home, cta_full=True))

# ================= O NAS =================
onas = page_hero([("/o-nas", "O nas")], 'Twój uśmiech <em>w najlepszych rękach</em>', "Nowocześnie. Profesjonalnie. Blisko Ciebie.", "recepcja.jpg") + f'''
<section class="section alt">
  <div class="wrap doc">
    <div class="doc-card rv">
      <small>Lek. dent. · Specjalista chirurgii stomatologicznej</small>
      <h2>Małgorzata Pińkowska-Prasał</h2>
      <p>Doświadczenie. Precyzja. Zaufanie.</p>
    </div>
    <div class="prose rv">
      <h2>Nowe miejsce na mapie Ozorkowa</h2>
      <p><b>OzODent Centrum Stomatologii</b> to nowoczesny gabinet w Ozorkowie, stworzony z myślą o komforcie i bezpieczeństwie Pacjentów.</p>
      <p>Kieruję się pasją do chirurgii stomatologicznej i wieloletnim doświadczeniem, które zdobywałam, pracując przez 10 lat w tym mieście.</p>
      <p>Moim celem jest kompleksowa opieka stomatologiczna na najwyższym poziomie.</p>
      <div class="sig sig-dark">Małgorzata Pińkowska-Prasał</div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2 class="title rv">Nasz gabinet</h2><div class="title-rule"></div>
    <div class="gallery">
      <figure class="rv"><img src="/assets/img/recepcja.jpg" alt="Recepcja OzODent Centrum Stomatologii w Ozorkowie" loading="lazy"></figure>
      <figure class="rv"><img src="/assets/img/korytarz.jpg" alt="Korytarz gabinetu OzODent" loading="lazy"></figure>
      <figure class="rv"><img src="/assets/img/gabinet.jpg" alt="Wnętrze gabinetu stomatologicznego OzODent" loading="lazy"></figure>
    </div>
  </div>
</section>
<section class="section sand">
  <div class="wrap">
    <div class="values">
      <div class="rv"><div class="ic">{ICON["tooth"]}</div>Kompleksowa opieka</div>
      <div class="rv"><div class="ic">{ICON["people"]}</div>Indywidualne podejście</div>
      <div class="rv"><div class="ic">{ICON["micro"]}</div>Nowoczesny sprzęt</div>
      <div class="rv"><div class="ic">{ICON["heart"]}</div>Przyjazna atmosfera</div>
      <div class="rv"><div class="ic">{ICON["shield"]}</div>Komfort i bezpieczeństwo</div>
    </div>
  </div>
</section>'''
pages.append(page("/o-nas", "O nas – lek. dent. Małgorzata Pińkowska-Prasał",
     "OzODent Centrum Stomatologii w Ozorkowie – lek. dent. Małgorzata Pińkowska-Prasał, specjalista chirurgii stomatologicznej.", "o-nas", onas))

# ================= USŁUGI =================
cards = "".join(f'<a class="svc rv" href="/uslugi/{s["slug"]}"><div class="ic">{ICON[s["icon"]]}</div><h3>{e(s["name"])}</h3><p>{e(s["short"])}</p><span class="more">Więcej →</span></a>' for s in SERVICES)
uslugi = page_hero([("/uslugi", "Usługi")], 'Zakres <em>usług</em>', "Diagnostyka · Leczenie · Profilaktyka · Estetyka") + f'''
<section class="section"><div class="wrap">
  <div class="svc-grid">{cards}</div>
</div></section>'''
pages.append(page("/uslugi", "Usługi stomatologiczne", "Usługi OzODent w Ozorkowie: stomatologia zachowawcza i dziecięca, endodoncja, chirurgia, periodontologia, protetyka, implanty, podcinanie wędzidełek, higienizacja, medycyna estetyczna, diagnostyka CBCT i OPG.", "uslugi", uslugi))

for s in SERVICES:
    intro = "".join(f"<p>{e(p)}</p>" for p in s["intro"])
    blocks, all_rows = "", []
    for spec in s["prices"]:
        name, rows, notes = resolve_prices(spec)
        all_rows += rows
        blocks += f'<div class="price-block rv"><h2>Cennik – {e(name)}</h2><div class="panel static">{rows_html(rows, notes)}</div></div>'
    if not s["prices"]:
        blocks = f'<div class="ask rv"><p>Zapytaj o termin i szczegóły zabiegu.</p><a class="btn btn-dark" href="{TEL_HREF}">{I("phone")}{TEL}</a></div>'
    link = ""
    if s.get("link"):
        slug, label = s["link"]
        link = f'<p class="svc-link rv"><a class="more" href="/uslugi/{slug}">{e(label)} →</a></p>'
    idx = SERVICES.index(s)
    rel = [SERVICES[(idx + k) % len(SERVICES)] for k in (1, 2, 3)]
    rel_html = "".join(f'<a class="svc rv" href="/uslugi/{x["slug"]}"><div class="ic">{ICON[x["icon"]]}</div><h3>{e(x["name"])}</h3><span class="more">Zobacz →</span></a>' for x in rel)
    ld = {"@context": "https://schema.org", "@type": "Service", "name": s["name"] + " Ozorków", "serviceType": s["name"],
          "description": s["short"], "areaServed": {"@type": "City", "name": "Ozorków"},
          "provider": {"@id": SITE + "/#gabinet"}, "url": f"{SITE}/uslugi/{s['slug']}"}
    offers = offers_ld(all_rows)
    if offers: ld["offers"] = offers
    extra = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>"
    intro_html = f'<div class="prose rv">{intro}</div>' if intro else ''
    body = page_hero([("/uslugi", "Usługi"), ("", e(s["name"]))], e(s["name"]), e(s["short"])) + f'''
<section class="section alt"><div class="wrap narrow">
  {intro_html}
  {blocks}
  {link}
</div></section>
<section class="section"><div class="wrap">
  <h2 class="title rv">Inne usługi</h2><div class="title-rule"></div>
  <div class="svc-grid rel">{rel_html}</div>
</div></section>'''
    pages.append(page(f"/uslugi/{s['slug']}", f"{s['name']} Ozorków", f"{s['name']} w OzODent Ozorków. {s['short']} Zapisy: {TEL}.", "uslugi", body, extra))

# ================= CENNIK =================
cennik = page_hero([("/cennik", "Cennik")], 'Cennik <em>usług</em>') + f'''
<section class="pricing"><div class="wrap">
  {price_tabs()}
  <p class="price-promo rv">Promocja na otwarcie gabinetu: konsultacja dla dorosłych 200 zł · przegląd z ewaluacją ortodontyczną 150 zł · przegląd dla dzieci 80 zł – <a href="/aktualnosci">szczegóły</a></p>
</div></section>'''
pages.append(page("/cennik", "Cennik – dentysta Ozorków", "Cennik OzODent Ozorków: stomatologia zachowawcza, chirurgia, periodontologia, podcinanie wędzidełek, higienizacja i wybielanie, RTG i tomografia CBCT.", "cennik", cennik))

# ================= AKTUALNOŚCI =================
akt = page_hero([("/aktualnosci", "Aktualności")], 'Aktualności', "Nowe miejsce na mapie Ozorkowa!") + f'''
<section class="promo"><div class="wrap">
  <div class="promo-head rv">
    <h2>Promocja <span>na otwarcie gabinetu</span></h2>
    <div class="title-rule"></div>
    <p class="promo-when">Z początkiem listopada</p>
  </div>
  <div class="promo-strip rv">Trwają zapisy przedwstępne <a href="{TEL_HREF}">{I("phone")}{TEL}</a></div>
  {promo_cards()}
</div></section>
<section class="section alt"><div class="wrap news-open">
  <figure class="rv"><img src="/assets/img/gabinet.jpg" alt="Nowy gabinet stomatologiczny OzODent w Ozorkowie" loading="lazy"></figure>
  <div class="prose rv">
    <h2>Nowopowstały, nowoczesny gabinet stomatologiczny</h2>
    <p>Otwarcie już jesienią 2026 – przy ul. Listopadowej 9A w Ozorkowie (dawny Inkubator, koło Lidla).</p>
    <p>Diagnostyka CBCT i OPG na miejscu. Parking za i przed budynkiem.</p>
  </div>
</div></section>'''
pages.append(page("/aktualnosci", "Aktualności – promocja na otwarcie", "Promocja na otwarcie OzODent w Ozorkowie: konsultacja dla dorosłych 200 zł, przegląd z ewaluacją ortodontyczną 150 zł, przegląd dla dzieci 80 zł. Zapisy przedwstępne: 572 555 193.", "aktualnosci", akt))

# ================= KONTAKT =================
opts = "".join(f"<option>{e(s['name'])}</option>" for s in SERVICES)
kontakt = page_hero([("/kontakt", "Kontakt")], 'Kontakt <em>i dojazd</em>', "Zapraszamy do zapisów przedwstępnych.") + f'''
<section class="contact"><div class="wrap">
  <div class="rv">
    <ul class="c-list">
      <li><span class="ic">{ICON["pin"]}</span><div><strong>Ozorków</strong><span>ul. Listopadowa 9A<br>dawny Inkubator – koło Lidla</span></div></li>
      <li><span class="ic">{ICON["phone"]}</span><div><strong>Zapisy przedwstępne</strong><a href="{TEL_HREF}">{TEL}</a></div></li>
      <li><span class="ic">{ICON["mail"]}</span><div><strong>E-mail</strong><a href="mailto:{MAIL}">{MAIL}</a></div></li>
      <li><span class="ic">{ICON["clock"]}</span><div><strong>Godziny otwarcia</strong><span>Pon – Pt: 8:00 – 20:00<br>Sobota: 8:00 – 14:00</span></div></li>
      <li><span class="ic">{ICON["car"]}</span><div><strong>Parking</strong><span>Przed i za budynkiem (wjazd przez bramę po lewej stronie paczkomatu)</span></div></li>
    </ul>
  </div>
  {map_block()}
</div></section>
<section class="section alt"><div class="wrap narrow">
  <h2 class="title rv">Napisz do nas</h2><div class="title-rule"></div>
  <p class="lead-c">Formularz otworzy Twój program pocztowy z gotową wiadomością.</p>
  <form class="form rv" id="contact-form" data-mail="{MAIL}" novalidate>
    <div class="row">
      <label>Imię i nazwisko<input name="name" required autocomplete="name"></label>
      <label>Telefon<input name="phone" type="tel" required autocomplete="tel" pattern="[0-9 +()-]{{9,}}"></label>
    </div>
    <div class="row">
      <label>E-mail (opcjonalnie)<input name="email" type="email" autocomplete="email"></label>
      <label>Usługa<select name="service"><option>Konsultacja / przegląd</option>{opts}</select></label>
    </div>
    <label>Wiadomość<textarea name="message" placeholder="Preferowane dni i godziny wizyty…"></textarea></label>
    <label class="consent"><input type="checkbox" name="consent" required> <span>Zapoznałem/am się z <a href="/polityka-prywatnosci" style="text-decoration:underline">polityką prywatności</a>.</span></label>
    <div class="form-msg" role="status" aria-live="polite"></div>
    <div><button class="btn btn-dark" type="submit">{I("mail")}Wyślij wiadomość</button></div>
  </form>
</div></section>'''
pages.append(page("/kontakt", "Kontakt i dojazd", "Kontakt z OzODent: ul. Listopadowa 9A, Ozorków (dawny Inkubator, koło Lidla). Tel. 572 555 193, kontakt@ozodent.pl. Pon–Pt 8:00–20:00, Sob 8:00–14:00.", "kontakt", kontakt))

# ================= POLITYKA PRYWATNOŚCI (do weryfikacji przez klienta) =================
privacy = page_hero([("/polityka-prywatnosci", "Polityka prywatności")], "Polityka prywatności") + f'''
<section class="section alt"><div class="wrap legal prose">
<h2>Administrator danych</h2>
<p>OzODent Centrum Stomatologii, {ADDR}, e-mail: <a href="mailto:{MAIL}">{MAIL}</a>, tel. {TEL}.</p>
<h2>Formularz kontaktowy</h2>
<p>Formularz na stronie nie wysyła danych na serwer – otwiera Twój program pocztowy z przygotowaną wiadomością. Dane otrzymujemy dopiero, gdy wyślesz e-mail.</p>
<h2>Pliki cookie i usługi zewnętrzne</h2>
<p>Strona nie używa plików cookie analitycznych ani marketingowych. Czcionki ładowane są z Google Fonts. Mapa Google ładuje się dopiero po kliknięciu przycisku „Pokaż mapę”. Stronę hostuje Vercel Inc.</p>
<h2>Twoje prawa</h2>
<p>Zgodnie z RODO przysługuje Ci prawo dostępu do danych, ich sprostowania, usunięcia, ograniczenia przetwarzania, przenoszenia, sprzeciwu oraz skargi do Prezesa Urzędu Ochrony Danych Osobowych.</p>
</div></section>'''
pages.append(page("/polityka-prywatnosci", "Polityka prywatności", "Polityka prywatności OzODent Centrum Stomatologii.", "", privacy))

err = f'''<section class="err"><div class="wrap">
  <div class="big">404</div><h1 style="font-size:36px;margin:12px 0">Nie znaleziono strony</h1>
  <p style="color:var(--muted);margin:0 0 28px">Strona mogła zostać przeniesiona lub nie istnieje.</p>
  <a class="btn" href="/">Wróć na stronę główną</a>
</div></section>'''
page("/404", "Nie znaleziono strony", "Strona nie istnieje.", "", err, '<meta name="robots" content="noindex">')

# usuń stare pliki, których już nie generujemy
for old in ["regulamin.html"]:
    p = os.path.join(OUT, old)
    if os.path.exists(p): os.remove(p)

today = datetime.date.today().isoformat()
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f'  <url><loc>{SITE}{"" if p=="/" else p}</loc><lastmod>{today}</lastmod><priority>{"1.0" if p=="/" else "0.8" if p.count("/")==1 else "0.7"}</priority></url>\n' for p in pages) + "</urlset>\n"
open(f"{OUT}/sitemap.xml", "w").write(sm)
open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("Wygenerowano", len(pages), "stron")
