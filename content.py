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

# ---------------------------------------------------------------------------
# ZESPÓŁ – sylwetki na /zespol (dane od klientki + profile ZnanyLekarz)
# Zdjęcia: wrzuć plik do public/assets/img/zespol/<slug>.jpg (kwadrat, min. 400×400)
#          – build.py sam go wykryje; bez pliku pokazuje się kółko z inicjałami.
# bio:     lista akapitów (życiorys). Pusta lista = sekcja się nie wyświetla.
# links:   (etykieta, url)
# ---------------------------------------------------------------------------
ZL_MPP = "https://www.znanylekarz.pl/profil/malgorzata-pinkowska-prasal"

TEAM = [
  dict(slug="malgorzata-pinkowska-prasal", title="lek. dent.", name="Małgorzata Pińkowska-Prasał",
       role="Specjalista chirurgii stomatologicznej", note="Założycielka OzODent",
       bio=["Absolwentka Uniwersytetu Medycznego w Łodzi (2005). W latach 2008–2012 zdobywałam doświadczenie zawodowe w klinice stomatologicznej w Kopenhadze, a następnie, w latach 2012–2025, pracowałam w Instytucie Stomatologii w Łodzi, gdzie uzyskałam tytuł specjalisty chirurgii stomatologicznej.",
            "Praca z młodymi lekarzami i dzielenie się wiedzą zawsze dawały mi ogromną satysfakcję. Trzykrotnie, w latach 2024, 2025 i 2026, zostałam wyróżniona tytułem „Najlepszy wśród Najlepszych Nauczycieli”.",
            "Chirurgia stomatologiczna jest moją zawodową pasją. W pracy najważniejsze są dla mnie precyzja, bezpieczeństwo oraz zaufanie i dobra relacja z pacjentem.",
            "Prywatnie jestem miłośniczką psów, jazdy na rowerze i ceramiki, która pozwala mi rozwijać kreatywność i zamiłowanie do pracy wymagającej cierpliwości oraz precyzji.",
            "OzODent to miejsce, które stworzyłam z myślą o stomatologii opartej na doświadczeniu, nowoczesnych rozwiązaniach i indywidualnym podejściu do każdego."],
       links=[("Opinie na ZnanyLekarz", ZL_MPP)]),
  dict(slug="julia-stokowska", title="lek. dent.", name="Julia Stokowska",
       role="Lekarz dentysta", note="PWZ 4555183",
       bio=["Absolwentka kierunku lekarsko-dentystycznego, który ukończyła w 2024 roku na Uniwersytecie Medycznym w Łodzi. W październiku 2025 roku ukończyła staż podyplomowy w Instytucie Stomatologii w Łodzi, zdobywając doświadczenie kliniczne i rozwijając swoje umiejętności zawodowe.",
            "W codziennej praktyce zajmuje się przede wszystkim stomatologią zachowawczą oraz leczeniem chorób przyzębia. Wykonuje również zabiegi z zakresu chirurgii stomatologicznej o niewielkim stopniu skomplikowania oraz pierwotne leczenie kanałowe.",
            "Szczególną wagę przywiązuje do komfortu i dobrego samopoczucia pacjentów. Doskonale rozumie, że wizyta u dentysty może wiązać się ze stresem i lękiem, dlatego stara się tworzyć atmosferę spokoju, zaufania i wzajemnego zrozumienia. Z cierpliwością pomaga pacjentom przełamywać dentofobię, dbając o to, aby każda wizyta przebiegała w możliwie bezstresowych warunkach. Z łatwością nawiązuje również kontakt z młodszymi pacjentami, dostosowując sposób komunikacji do ich wieku i potrzeb.",
            "W swojej pracy stawia na profilaktykę, edukację i indywidualne podejście do każdego pacjenta. Wierzy, że świadomość dotycząca zdrowia jamy ustnej oraz odpowiednie nawyki pozwalają nie tylko zapobiegać chorobom, ale także budować zdrowy uśmiech na lata.",
            "Prywatnie jest miłośniczką kotów, górskich wędrówek i dobrej herbaty. Ceni chwile spędzone blisko natury, które pozwalają jej odpocząć i nabrać energii do kolejnych wyzwań."],
       links=[("Profil na ZnanyLekarz", "https://www.znanylekarz.pl/profil/julia-stokowska")]),
  dict(slug="marcelina-malinowska", title="lek. dent.", name="Marcelina Malinowska",
       role="Lekarz dentysta, lekarz medycyny estetycznej", note="",
       bio=["Absolwentka kierunku lekarsko-dentystycznego na Uniwersytecie Medycznym w Łodzi. W swojej codziennej pracy zajmuje się głównie stomatologią zachowawczą, pedodoncją oraz chirurgią stomatologiczną. W swojej pracy kieruje się głównie starannością oraz dbałością o komfort pacjenta. Lekarz z świetnym podejściem do pacjentów, zarówno dorosłych jak i najmłodszych. Uczestniczy w licznych kursach i konferencjach, aby świadczyć usługi na najwyższym poziomie.",
            "Absolwentka studiów podyplomowych w zakresie medycyny estetyczno-naprawczej na Śląskiej Wyższej Szkole Medycznej w Katowicach. W codziennej pracy wykonuje zabiegi z użyciem toksyny botulinowej, zabiegi mezoterapii igłowej oraz zabiegi z użyciem osocza bogatopłytkowego i fibryny."],
       links=[]),
  dict(slug="barbara-ziaber", title="lek. dent.", name="Barbara Ziąber",
       role="Lekarz dentysta", note="",
       bio=["Absolwentka kierunku lekarsko-dentystycznego na Uniwersytecie Medycznym w Łodzi. Szczególnie interesuje się stomatologią zachowawczą, estetyczną oraz chirurgią stomatologiczną. Regularnie rozwija swoje umiejętności i poszerza wiedzę, uczestnicząc w kursach i szkoleniach. Obecnie kształci się również na studiach podyplomowych z zakresu medycyny estetycznej. W pracy stawia na komfort pacjenta i indywidualne podejście, dbając o spokojną i przyjazną atmosferę podczas każdej wizyty.",
            "W wolnym czasie uwielbia podróżować i odkrywać nowe miejsca. Chętnie sięga po dobrą książkę, a zimą lubi spędzać czas na nartach."],
       links=[]),
  dict(slug="agnieszka-wladysiak", title="lek. dent.", name="Agnieszka Władysiak",
       role="Lekarz dentysta – endodoncja", note="",
       bio=["Jestem absolwentką Uniwersytetu Medycznego w Łodzi. Na co dzień zajmuję się głównie stomatologią zachowawczą z endodoncją. Stale podnoszę swoje kwalifikacje, uczestnicząc w kursach. Do każdego pacjenta podchodzę indywidualnie, z należytą starannością i cierpliwością.",
            "Pacjenci z dentofobią nie mają się czego obawiać – wszystkie zabiegi wykonuję z zapewnieniem jak największego komfortu."],
       links=[]),
  dict(slug="martyna-dabrowska", title="", name="Martyna Dąbrowska",
       role="Higienistka stomatologiczna", note="5 lat doświadczenia · praca w powiększeniu",
       bio=["Stomatologia to dla mnie nie tylko zawód, ale przede wszystkim pasja, którą każdego dnia rozwijam z zaangażowaniem i uśmiechem. Ukończyłam WSCKZiU w Koninie na kierunku higienistka stomatologiczna. Jestem również technikiem sterylizacji medycznej oraz nauczycielem w szkole medycznej, gdzie dzielę się swoją wiedzą i doświadczeniem z przyszłymi higienistkami stomatologicznymi.",
            "Na co dzień współpracuję z różnymi gabinetami stomatologicznymi, otaczając pacjentów opieką w zakresie profilaktyki jamy ustnej, profesjonalnej higienizacji, wybielania zębów oraz leczenia estetycznego metodą ICON. W swojej pracy stawiam na indywidualne podejście, komfort pacjenta i edukację, ponieważ wierzę, że zdrowy i piękny uśmiech zaczyna się od świadomej profilaktyki.",
            "Największą satysfakcję daje mi możliwość obserwowania efektów wspólnej pracy oraz pomaganie pacjentom w dbaniu o zdrowie i pewność siebie.",
            "Prywatnie uwielbiam aktywnie spędzać czas, a moją pasją są długie trasy rowerowe, które pozwalają mi odpocząć, nabrać energii i odkrywać nowe miejsca."],  # <- koniec zdania ucięty na zrzucie od klientki – potwierdzić
       links=[("Instagram", "https://www.instagram.com/martynadabrowska.higienistka")]),
  dict(slug="aleksandra-szewczyk", title="", name="Aleksandra Szewczyk",
       role="Dyplomowana higienistka stomatologiczna", note="",
       bio=["W gabinecie OzODent jestem „prawą ręką” lekarza dentysty i dobrym duchem gabinetu. Dbam o to, aby każda wizyta przebiegała sprawnie, bezpiecznie i w bezstresowej atmosferze. Doskonale rozumiem, że wizyta u dentysty może wiązać się ze stresem, dlatego zawsze witam pacjentów uśmiechem i dbam o ich dobre samopoczucie od progu gabinetu. Szczególne miejsce w moim sercu zajmuje praca z dziećmi – poprzez zabawę i cierpliwe tłumaczenie uczę najmłodszych, jak dbać o zęby.",
            "Ponadto specjalizuję się w profilaktyce i profesjonalnej higienizacji jamy ustnej. Moim priorytetem jest pełen komfort pacjenta oraz bezbolesne przeprowadzanie zabiegów. Do każdego pacjenta podchodzę indywidualnie, dobierając rozwiązania dopasowane do jego stylu życia i potrzeb.",
            "Stomatologia jest moją nie tylko pracą, ale również pasją, dlatego regularnie uczestniczę w kursach i szkoleniach, aby stale podnosić swoje kwalifikacje i poznawać najnowsze trendy w profilaktyce stomatologicznej.",
            "Prywatnie interesuję się sportem, turystyką i cukiernictwem artystycznym."],
       links=[]),
]

# Logopedzi / neurologopedzi, z którymi współpracujemy (podcinanie wędzidełek)
PARTNERS = [
  dict(slug="natalia-dobierzewska", title="mgr", name="Natalia Dobierzewska",
       role="Logopeda, neurologopeda, audiofonolog", note="Gabinet logopedyczny – Ozorków",
       links=[("logopedaozorkow.pl", "https://logopedaozorkow.pl/")]),
  dict(slug="anna-misztal-szczerbakowicz", title="mgr", name="Anna Misztal-Szczerbakowicz",
       role="Logopeda, neurologopeda", note="LogomAnia – Gabinet Logopedyczny, Kutno",
       links=[]),   # <- brak linku od klientki (Facebook: „LogomAnia Kutno – Gabinet Logopedyczny”)
  dict(slug="katarzyna-kowalewska", title="mgr", name="Katarzyna Kowalewska",
       role="Neurologopeda – noworodki i niemowlęta", note="Gabinet neuro.logopedki – Włocławek",
       links=[("Profil na ZnanyLekarz", "https://www.znanylekarz.pl/profil/katarzyna-kowalewska-2")]),
]

# ---------------------------------------------------------------------------
# OPINIE – wybrane opinie z profilu ZnanyLekarz lek. dent. M. Pińkowskiej-Prasał
# (stan na 2026-10-16: 5,0 / 59 opinii). Teksty dosłowne, skróty oznaczone […].
# Pomijamy opinie wspominające NFZ lub inny gabinet (Amadent), żeby nie wprowadzać w błąd.
# ---------------------------------------------------------------------------
ZL_RATING = ("5,0", 59, "16.10.2026")
REVIEWS = [  # kolejność = priorytet; strona główna pokazuje 5 pierwszych
  ('Magdalena', '2026-05', 'Mimo stresu pod jej opieką czuje się spokój i pewność, że wszystko jest pod kontrolą. Widać doświadczenie, brak miejsca na zawahanie, a jednocześnie pełne zaangażowanie i skrupulatność. […] każdy etap leczenia jest jasno tłumaczony.'),
  ('Katarzyna', '2026-06', 'Do Pani Doktor trafiłam z dwumiesięczną córką z polecenia. Córka musiała mieć podcięte wędzidełko językowe. Zabieg odbył się w miłej atmosferze, zostałam poinformowana jak będzie przebiegał, udzielono mi wskazówek jak ćwiczyć z córką po zabiegu. […] Serdecznie polecam Panią Doktor'),
  ('Nikola', '2026-06', 'Do Pani doktor trafiłam z okropnym utrudniajacym juz przełykanie sliny bolem ósemki, Pani doktor nie czekala ani chwili zostalam przyjeta expressowo. […] Wizyta u Pani Małgorzaty również zmienila moje nastawienie do stomatologow poniewaz mialam traume. Dziekuje'),
  ('Ilona', '2026-02', 'Byliśmy z córką na podcięciu wędzidełka. Pani Doktor bardzo miła i przyjazna z super podejściem do dzieci. Pani Doktor wykonała zabieg szybko i bezboleśnie a po skończonym zabiegu pokazała jak masować miejsce po zabiegu. Bardzo dziękujemy :)'),
  ('Angelika', '2025-11', 'Byliśmy z Synkiem na podcięciu wędzidełka sam zabieg trwa krótko Pani doktor naprawdę przyjemna i bardzo sympatyczna :) kontakt z Panią doktor przed zabiegiem jaki po był naprawdę bardzo dobry gdybym miała wybierać jeszcze raz wybrałabym Panią doktor. Polecam'),
  ('Aneta', '2026-07', 'Pani doktor jest wspaniałym człowiekiem […] zawsze mogłam na nią liczyć jest wspaniałym lekarzem z powołania. Z całego serca dziękujemy za to że Pani doktor w tych ciężkich chwilach była z nami.'),
]
