# -*- coding: utf-8 -*-
# Generates index.html for OzODent Centrum Stomatologii
import html

TEL = "572 555 193"
TEL_HREF = "tel:+48572555193"

# ---------- PRICE DATA (from the client's price boards) ----------
PRICES = [
  ("zachowawcza", "Stomatologia zachowawcza", [
    ("Wypełnienie na jednej powierzchni", "", "300–400 zł"),
    ("Wypełnienie na dwóch powierzchniach", "", "350–450 zł"),
    ("Rozległa odbudowa korony zęba kompozytem", "", "500–600 zł"),
    ("Ubytek klinowy (niepróchnicowy)", "", "od 300 zł"),
    ("Odbudowa ściany do leczenia endodontycznego", "", "200 zł"),
    ("Licówka kompozytowa bezpośrednia", "", "600 zł"),
    ("Licówka kompozytowa iniekcyjna", "flow injection", "800 zł"),
    ("Bonding (1 ząb)", "", "od 600 zł"),
    ("ICON (1 ząb)", "", "300 zł"),
    ("Szynowanie zębów kompozytem (1 ząb)", "", "300 zł"),
    ("Gingiwektomia / koagulacja dziąsła do leczenia zachowawczego", "", "250 zł"),
    ("Zaświadczenie przed zabiegiem szpitalnym", "+ koszt RTG", "200 zł"),
  ], [("Pracujemy na najnowszych nanokompozytach", "dających efekt kameleona – niewidocznego wypełnienia."),
      ("Znieczulenie w cenie zabiegu", "")]),
  ("chirurgia", "Chirurgia", [
    ("Konsultacja chirurgiczna", "", "200 zł"),
    ("Usunięcie zęba", "", "300–500 zł"),
    ("Usunięcie zęba ze wskazań ortodontycznych", "", "400–500 zł"),
    ("Usunięcie zęba ósmego", "w zależności od stopnia zatrzymania", "500–1000 zł"),
    ("Germektomia", "usunięcie zawiązka zęba całkowicie zatrzymanego ósmego do leczenia ortodontycznego", "600–900 zł"),
    ("Usunięcie zęba mlecznego", "", "250–300 zł"),
    ("Usunięcie zęba mlecznego w reinkluzji", "", "400 zł"),
    ("Zdjęcie szwów zakładanych w innym gabinecie", "", "50 zł"),
    ("Plastyka połączenia ustno-zatokowego", "", "600 zł"),
    ("Nacięcie ropnia", "", "od 200 zł"),
    ("Płukanie zębodołu + opatrunek chirurgiczny", "", "100 zł"),
    ("Wyłuszczenie torbieli", "", "500–800 zł"),
    ("Wycięcie kieszonki patologicznej (kaptur)", "", "400 zł"),
    ("Resekcja wierzchołka korzenia", "", "600 zł"),
    ("Wycięcie zmian na błonie śluzowej", "wraz z badaniem histopatologicznym", "400 zł"),
  ], [("Znieczulenie do każdego zabiegu – GRATIS", ""),
      ("Szwy po zabiegu w OzODent – wizyta kontrolna GRATIS", "")]),
  ("periodontologia", "Periodontologia", [
    ("Konsultacja zmian na błonie śluzowej / kwalifikacja do zabiegu", "", "100 zł"),
    ("Kiretaż poddziąsłowy obejmujący 1–3 zęby", "", "150 zł"),
    ("Kiretaż poddziąsłowy obejmujący jedną ćwiartkę", "pół łuku zębowego", "200 zł"),
    ("Kiretaż jednego łuku zębowego", "", "300 zł"),
    ("Kiretaż całego uzębienia", "", "400–500 zł"),
    ("Drenaż ropnia przyzębnego z aplikacją leku", "", "150–250 zł"),
    ("Leczenie zmian na błonie śluzowej", "w tym korekta protezy wykonanej poza gabinetem i aplikacja leku na odleżynę", "200 zł"),
    ("Plastyka wyrostka zębodołowego wraz z aplikacją leku", "", "500 zł"),
    ("Wycięcie zmiany wraz z badaniem hist-pat", "", "400–800 zł"),
  ], [("Znieczulenie do zabiegu – GRATIS", "")]),
  ("wedzidelka", "Podcinanie wędzidełek", [
    ("Konsultacja / kwalifikacja do podcięcia wędzidełka", "", "100 zł"),
    ("Podcięcie wędzidełka u noworodków i niemowląt", "frenotomia", "300–400 zł"),
    ("Powtórne podcięcie wędzidełka – wycięcie zrostu u niemowląt", "", "500 zł"),
    ("Miofrenuloplastyka – podcięcie wędzidełka języka u starszych dzieci (od 5 r.ż.) i dorosłych", "uwzględniająca podcięcie mięśni bródkowo-językowych", "550–600 zł"),
    ("Podcięcie wędzidełka wargi górnej", "", "300–500 zł"),
  ], [("Wszystkie zabiegi wykonywane są w porozumieniu z neurologopedą i logopedą", "oraz w ramach prowadzonej terapii neurologopedycznej / logopedycznej."),
      ("W razie potrzeby możliwa sedacja farmakologiczna przed zabiegiem", "")]),
  ("higienizacja", "Higienizacja i wybielanie", [
    ("Skaling", "", "200 zł"),
    ("Piaskowanie", "", "200 zł"),
    ("Higienizacja", "skaling nad- i poddziąsłowy, piaskowanie, lakierowanie", "300–500 zł"),
    ("Wybielanie nakładkowe (2 łuki zębowe)", "", "od 1000 zł"),
    ("Fluoryzacja 1 łuk / 2 łuki", "", "100 / 150 zł"),
    ("Znieczulenie do zabiegu", "", "50 zł"),
  ], []),
  ("rtg", "RTG", [
    ("Zdjęcie punktowe RVG", "jako osobne zdjęcie", "50 zł"),
    ("Zdjęcie pantomograficzne", "", "100 zł"),
    ("Tomografia wycinkowa", "", "150 zł"),
    ("Tomografia 1 łuk (szczęka / żuchwa)", "", "200 zł"),
    ("Tomografia całkowita (szczęka + żuchwa)", "", "300 zł"),
  ], [("Zdjęcia punktowe wykorzystywane w trakcie leczenia – GRATIS", "")]),
]

e = html.escape

def price_tabs():
    tabs, panels = [], []
    for i, (pid, name, rows, notes) in enumerate(PRICES):
        sel = "true" if i == 0 else "false"
        tabs.append(f'<button class="tab" role="tab" id="t-{pid}" aria-controls="p-{pid}" aria-selected="{sel}" data-tab="{pid}">{e(name)}</button>')
        trs = []
        for title, sub, price in rows:
            subh = f'<small>{e(sub)}</small>' if sub else ""
            trs.append(f'<li><div class="pl-name">{e(title)}{subh}</div><div class="pl-price">{e(price)}</div></li>')
        nh = ""
        if notes:
            nh = '<div class="pl-notes">' + "".join(
                f'<div class="pl-note"><span class="chk">{ICON["check"]}</span><p><strong>{e(a)}</strong>{(" " + e(b)) if b else ""}</p></div>'
                for a, b in notes) + "</div>"
        hidden = "" if i == 0 else " hidden"
        panels.append(f'<div class="panel" role="tabpanel" id="p-{pid}" aria-labelledby="t-{pid}"{hidden}><ul class="pricelist">{"".join(trs)}</ul>{nh}</div>')
    return "".join(tabs), "".join(panels)

# ---------- ICONS (line style, inherit currentColor) ----------
def svg(body, vb="0 0 48 48", sw="1.6"):
    return f'<svg viewBox="{vb}" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>'

TOOTH = "M16 7c-6 0-10 5-10 11 0 6 2.5 9 4 14 1.6 5.5 2.5 12 6.5 12 3.5 0 3.3-10 7.5-10s4 10 7.5 10c4 0 4.9-6.5 6.5-12 1.5-5 4-8 4-14 0-6-4-11-10-11-4 0-5.5 2.5-8 2.5S20 7 16 7z"
ICON = {
  "tooth": svg(f'<path d="{TOOTH}"/>'),
  "tooth-fill": svg(f'<path d="{TOOTH}"/><path d="M15 15c2 3 4 4 9 4s7-1 9-4"/>'),
  "tooth-kid": svg(f'<path d="{TOOTH}" transform="translate(-4 -2) scale(.82)"/><circle cx="34" cy="30" r="4"/><path d="M27 44c0-4 3-7 7-7s7 3 7 7"/>'),
  "tooth-root": svg(f'<path d="{TOOTH}"/><path d="M20 22v14M28 22v14"/>'),
  "implant": svg('<path d="M14 8c0-2 3-3 10-3s10 1 10 3c0 4-3 6-10 6S14 12 14 8z"/><path d="M18 17h12M19 22h10M20 27h8M21 32h6M22 37h4M24 37v6"/>'),
  "crown": svg('<path d="M10 14c0-4 3-6 7-6 3 0 4 2 7 2s4-2 7-2c4 0 7 2 7 6 0 5-3 7-4 11-1 5-2 13-6 13-3 0-2.5-8-4-8s-1 8-4 8c-4 0-5-8-6-13-1-4-4-6-4-11z"/><path d="M17 8c0 5 2 8 7 8s7-3 7-8"/>'),
  "face": svg('<path d="M30 42v-6c5-1 8-4 8-9v-3l3-1-3-5c0-8-6-13-14-13S10 11 10 19c0 5 2 8 5 10v13"/><path d="M33 10l1.2 2.6L37 14l-2.8 1.3L33 18l-1.2-2.7L29 14l2.8-1.4z"/>'),
  "shield": svg('<path d="M24 5l15 6v10c0 10-6 18-15 22C15 39 9 31 9 21V11z"/><path d="M17 24l5 5 9-10"/>'),
  "people": svg('<circle cx="18" cy="16" r="6"/><circle cx="33" cy="19" r="5"/><path d="M6 40c0-7 5-12 12-12s12 5 12 12"/><path d="M29 30c5 0 13 2 13 10"/>'),
  "micro": svg('<path d="M20 6l8 4-7 14-8-4z"/><path d="M15 32h18M12 42h24M24 32v10M30 18c6 2 8 7 6 14"/>'),
  "doctor": svg('<circle cx="24" cy="14" r="7"/><path d="M10 42c0-8 6-14 14-14s14 6 14 14"/><path d="M19 29v6a5 5 0 0010 0v-6"/>'),
  "chat": svg('<path d="M8 10h32v22H22l-9 7v-7H8z"/>'),
  "pin": svg('<path d="M24 44s14-13 14-24a14 14 0 10-28 0c0 11 14 24 14 24z"/><circle cx="24" cy="20" r="5"/>'),
  "car": svg('<path d="M8 30l3-10c1-3 3-4 6-4h14c3 0 5 1 6 4l3 10v8H8z"/><circle cx="15" cy="32" r="2.5"/><circle cx="33" cy="32" r="2.5"/><path d="M8 38v4M40 38v4M12 24h24"/>'),
  "clock": svg('<circle cx="24" cy="24" r="18"/><path d="M24 13v11l7 5"/>'),
  "heart": svg('<path d="M24 41S7 30 7 18a9 9 0 0117-4 9 9 0 0117 4c0 12-17 23-17 23z"/>'),
  "phone": svg('<path d="M14 6l6 1 3 9-4 3c2 5 6 9 11 11l3-4 9 3 1 6c0 3-3 5-6 5C20 40 8 28 8 12c0-3 3-6 6-6z"/>', sw="2"),
  "cal": svg('<rect x="7" y="10" width="34" height="31" rx="3"/><path d="M7 19h34M16 6v8M32 6v8M15 27h4M22 27h4M29 27h4M15 33h4M22 33h4"/>', sw="2.4"),
  "mail": svg('<rect x="6" y="11" width="36" height="26" rx="2"/><path d="M6 13l18 13 18-13"/>'),
  "globe": svg('<circle cx="24" cy="24" r="17"/><path d="M7 24h34M24 7c-6 6-6 28 0 34M24 7c6 6 6 28 0 34"/>'),
  "check": svg('<path d="M10 25l9 9 19-20"/>', sw="3"),
  "baby": svg('<circle cx="24" cy="22" r="14"/><path d="M19 22h.01M29 22h.01M19 28c3 3 7 3 10 0M22 8c0 3 4 3 4 6"/>', sw="2"),
  "brain": svg('<circle cx="18" cy="22" r="12"/><path d="M14 18c2-2 6-2 8 0M12 24c3 2 9 2 12 0M30 14h12v10h-6l-4 4v-4h-2z"/>'),
  "syringe": svg('<path d="M30 8l10 10M35 13L17 31l-6 1 1-6 18-18M22 18l8 8M9 39l5-5"/>'),
  "fb": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M22 12a10 10 0 10-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7A10 10 0 0022 12z"/></svg>',
  "menu": svg('<path d="M8 15h32M8 24h32M8 33h32"/>', sw="2.4"),
}

