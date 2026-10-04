# -*- coding: utf-8 -*-
# Treści podstron usług – WYŁĄCZNIE informacje z materiałów klienta
# (cenniki, ulotka „Nowe miejsce na mapie Ozorkowa”, ulotka promocyjna, makieta strony).
#
# prices: lista identyfikatorów cennika z data.py (np. "chirurgia")
#         albo krotka ("Tytuł", [(nazwa, opis, cena), ...], [(notatka, dopisek), ...])

SERVICES = [
  dict(slug="stomatologia-zachowawcza", name="Stomatologia zachowawcza", icon="drill",
    short="Leczenie próchnicy, odbudowa zębów, nowoczesne wypełnienia.",
    intro=["Wykonujemy kilka wypełnień na jednej wizycie – szybko, skutecznie i komfortowo, oszczędzając Twój czas."],
    prices=["zachowawcza"]),

  dict(slug="stomatologia-dziecieca", name="Stomatologia dziecięca", icon="baby",
    short="Delikatna opieka i leczenie dzieci – przyjazne podejście, profilaktyka, leczenie dzieci w każdym wieku.",
    intro=["Pracujemy w przyjaznej atmosferze, z cierpliwością i indywidualnym podejściem.",
           "Zdrowy uśmiech Twojego dziecka to nasz priorytet!"],
    prices=[("Promocja na otwarcie gabinetu", [
               ("Przegląd stomatologiczny dla dzieci", "ocena stanu uzębienia, wskazówki profilaktyczne, indywidualne zalecenia", "80 zł"),
               ("Przegląd z ewaluacją ortodontyczną", "dla dzieci w okresie wymiany uzębienia – przegląd, ocena rozwoju uzębienia i zgryzu, zdjęcie pantomograficzne (OPG)", "150 zł"),
             ], []),
            ("Zęby mleczne", [
               ("Usunięcie zęba mlecznego", "", "250–300 zł"),
               ("Usunięcie zęba mlecznego w reinkluzji", "", "400 zł"),
             ], [])],
    link=("podcinanie-wedzidelek", "Podcinanie wędzidełek u niemowląt i dzieci")),

  dict(slug="endodoncja", name="Endodoncja", icon="tooth-root",
    short="Jednoetapowe leczenie kanałowe z najwyższą starannością.",
    intro=["Diagnostyka na miejscu: zdjęcia RVG, OPG oraz tomografia CBCT."],
    prices=[("Zabiegi powiązane", [
               ("Odbudowa ściany do leczenia endodontycznego", "", "200 zł"),
               ("Resekcja wierzchołka korzenia", "", "600 zł"),
             ], [("Zdjęcia punktowe wykorzystywane w trakcie leczenia – GRATIS", "")])],
    link=("diagnostyka-rtg", "Cennik diagnostyki RTG i CBCT")),

  dict(slug="chirurgia", name="Chirurgia stomatologiczna", icon="scalpel",
    short="Pełen zakres zabiegów chirurgicznych, usuwanie ósemek, implanty.",
    intro=["Zabiegi wykonuje lek. dent. Małgorzata Pińkowska-Prasał – specjalista chirurgii stomatologicznej."],
    prices=["chirurgia"]),

  dict(slug="periodontologia", name="Periodontologia", icon="drop",
    short="Kiretaż poddziąsłowy, leczenie zmian na błonie śluzowej, drenaż ropni przyzębnych.",
    intro=[],
    prices=["periodontologia"]),

  dict(slug="protetyka", name="Protetyka", icon="crown",
    short="Korony, mosty, protezy, bonding – odbudowa estetyczna i funkcjonalna.",
    intro=[],
    prices=[]),

  dict(slug="implanty", name="Implanty", icon="implant",
    short="Nowoczesne implanty – trwałe rozwiązania.",
    intro=[],
    prices=[],
    link=("diagnostyka-rtg", "Diagnostyka CBCT na miejscu")),

  dict(slug="podcinanie-wedzidelek", name="Podcinanie wędzidełek", icon="mouth",
    short="U niemowląt, starszych dzieci oraz dorosłych – we współpracy z neurologopedą.",
    intro=[],
    prices=["wedzidelka"]),

  dict(slug="higienizacja-wybielanie", name="Higienizacja i wybielanie", icon="brush",
    short="Nowoczesna higienizacja wykonywana przez wykwalifikowany personel: skaling, piaskowanie, fluoryzacja, wybielanie.",
    intro=[],
    prices=["higienizacja"]),

  dict(slug="medycyna-estetyczna", name="Medycyna estetyczna", icon="face",
    short="Zabiegi odmładzające i upiększające: kwas hialuronowy, botoks, poprawa owalu twarzy.",
    intro=[],
    prices=[]),

  dict(slug="diagnostyka-rtg", name="Diagnostyka CBCT i OPG", icon="scan",
    short="Diagnostyka CBCT – precyzyjna diagnostyka 3D dla skutecznego leczenia. Diagnostyka OPG – panoramiczne zdjęcia dla pełnego obrazu zdrowia.",
    intro=[],
    prices=["rtg"]),
]
