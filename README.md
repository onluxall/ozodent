# OzODent – Centrum Stomatologii (strona www)

Statyczna strona gabinetu OzODent w Ozorkowie. Hosting: Vercel (katalog `public/`, bez kroku budowania).

## Struktura
- `public/` – gotowa strona (HTML, CSS, JS, obrazy) – to serwuje Vercel
- `build.py` – generator wszystkich podstron (szablon, nawigacja, stopka, SEO)
- `data.py` – cennik i ikony SVG
- `content.py` – treści podstron usług (opisy, zakres, FAQ)
- `vercel.json` – czyste adresy URL (`/cennik`, `/uslugi/chirurgia`), nagłówki, cache

## Edycja treści
1. Zmień ceny w `data.py` (lista `PRICES`) lub treści w `content.py`.
2. Uruchom `python3 build.py` – podstrony w `public/` zostaną wygenerowane ponownie.
3. `git commit` + `git push` – Vercel automatycznie opublikuje nową wersję.

Podgląd lokalny: `npx serve public`

## Domena
Po podpięciu domeny (np. ozodent.pl) zmień `SITE` w `build.py` i uruchom `python3 build.py` (canonical, sitemap, og:image).
