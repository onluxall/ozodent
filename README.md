# OzODent – Centrum Stomatologii (strona www)

Statyczna strona gabinetu OzODent w Ozorkowie. Hosting: Vercel (katalog `public/`, bez kroku budowania).

## Struktura
- `public/` – gotowa strona (HTML, CSS, JS, obrazy) – to serwuje Vercel
- `build.py` – generator wszystkich podstron (szablon, nawigacja, stopka, SEO)
- `data.py` – cennik i ikony SVG
- `content.py` – treści podstron usług (opisy, zakres, FAQ)
- `deploy.sh` – jednorazowy push na GitHub (onluxall/ozodent) i deploy na Vercel
- `vercel.json` – czyste adresy URL (`/cennik`, `/uslugi/chirurgia`), nagłówki, cache

## Edycja treści
1. Zmień ceny w `data.py` (lista `PRICES`) lub treści w `content.py`.
2. Uruchom `python3 build.py` – podstrony w `public/` zostaną wygenerowane ponownie.
3. `git commit` + `git push` – Vercel automatycznie opublikuje nową wersję.

Podgląd lokalny: `npx serve public`

## Zespół (/zespol)
- Dane osób: `content.py` → `TEAM` (lekarze, higienistka) i `PARTNERS` (współpracujący logopedzi).
- Zdjęcia (kółka): wrzuć `public/assets/img/zespol/<slug>.jpg` (kwadrat, min. 400×400), np. `julia-stokowska.jpg`, i uruchom `python3 build.py` – bez pliku wyświetlają się inicjały.
- Życiorys: wpisz akapity do `bio=[...]` danej osoby. Życiorys i zdjęcie dr Pińkowskiej-Prasał pokażą się też na /o-nas.

## Domena
Po podpięciu domeny (np. ozodent.pl) zmień `SITE` w `build.py` i uruchom `python3 build.py` (canonical, sitemap, og:image).
