#!/usr/bin/env python3
"""
Vygeneruje sekce „Co nám píší klienti“ a „Pro koho jsme hráli“ z recenze.json a reference.json
do index.html, en/index.html a de/index.html (mezi značky <!-- RECENZE:START/END --> a
<!-- REFERENCE:START/END -->). Spouští ho GitHub Actions po každé změně JSON souborů.
Videoukázky: z videa.json zapíše seznam videí do media.js (mezi značky // VIDEA:START a // VIDEA:END);
náhledy z YouTube si podle ID vybírá až stránka sama.
"""
import json, re, sys, html, datetime, pathlib

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
SITE = (ROOT / 'CNAME').read_text(encoding='utf-8').strip()
ENS = {'jazzduo.cz': 'duo', 'jazztrio.cz': 'trio', 'jazzquartet.cz': 'quartet', 'jazzcombo.cz': 'combo'}[SITE]
LABEL = {
    'duo': {'cs': 'jazzové duo', 'en': 'jazz duo', 'de': 'Jazz-Duo'},
    'trio': {'cs': 'jazzové trio', 'en': 'jazz trio', 'de': 'Jazz-Trio'},
    'quartet': {'cs': 'jazzový kvartet', 'en': 'jazz quartet', 'de': 'Jazz-Quartett'},
    'combo': {'cs': 'Jazz Combo', 'en': 'Jazz Combo', 'de': 'Jazz Combo'},
}[ENS]
PAGES = {'cs': 'index.html', 'en': 'en/index.html', 'de': 'de/index.html'}
STARS_LABEL = {'cs': 'Hodnocení {n} z 5 hvězdiček', 'en': '{n}/5', 'de': '{n}/5'}
MONTH_EN = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
CHYBY = []


def chyba(msg):
    CHYBY.append(msg)


def esc(s):
    return html.escape(s, quote=False)


def prelozit(pole, jazyk, kde):
    """pole může být text, nebo {"cs": …, "en": …, "de": …}; chybí-li překlad, použije se čeština."""
    if isinstance(pole, str):
        return pole, 'cs'
    if not isinstance(pole, dict) or not pole.get('cs'):
        chyba(f'{kde}: chybí český text („cs“)')
        return '', 'cs'
    if pole.get(jazyk):
        return pole[jazyk], jazyk
    return pole['cs'], 'cs'


def datum(iso, jazyk, kde):
    try:
        d = datetime.date.fromisoformat(iso)
    except Exception:
        chyba(f'{kde}: datum „{iso}“ musí být ve tvaru RRRR-MM-DD, např. 2026-10-22')
        return ''
    if jazyk == 'cs':
        return f'{d.day}. {d.month}. {d.year}'
    if jazyk == 'en':
        return f'{d.day} {MONTH_EN[d.month - 1]} {d.year}'
    return d.strftime('%d.%m.%Y')


def nacti(nazev, klic):
    p = ROOT / nazev
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        sys.exit(f'CHYBA v {nazev}, řádek {e.lineno}, sloupec {e.colno}: {e.msg}. '
                 'Nejčastěji chybí čárka mezi položkami nebo uvozovka.')
    if not isinstance(data.get(klic), list):
        sys.exit(f'CHYBA v {nazev}: chybí seznam "{klic}": [ … ]')
    return data[klic]


def recenze_html(seznam, jazyk):
    vystup = []
    serazene = sorted(enumerate(seznam), key=lambda x: (x[1].get('datum', ''), -x[0]), reverse=True)
    for i, r in serazene:
        kde = f'recenze.json, položka {i + 1} ({r.get("jmeno", "?")})'
        if not r.get('jmeno'):
            chyba(f'{kde}: chybí „jmeno“')
        text, tj = prelozit(r.get('text'), jazyk, kde)
        akce, aj = prelozit(r.get('akce', ''), jazyk, kde) if r.get('akce') else ('', jazyk)
        if aj != jazyk:
            akce = ''  # bez překladu typu akce ukážeme na EN/DE jen název sestavy
        kdy = datum(r.get('datum', ''), jazyk, kde)
        n = r.get('hvezdy')
        hv = ''
        if n:
            if n not in (1, 2, 3, 4, 5):
                chyba(f'{kde}: „hvezdy“ musí být číslo 1 až 5, nebo položku vynechte')
            else:
                hv = f'<div class="stars" role="img" aria-label="{STARS_LABEL[jazyk].format(n=n)}">{"★" * n}</div>'
        lang_attr = f' lang="{tj}"' if tj != jazyk else ''
        popis = ' · '.join(x for x in [esc(akce), LABEL[jazyk]] if x)
        vystup.append(
            f'<figure class="review">{hv}<p{lang_attr}>{esc(text)}</p>'
            f'<figcaption class="who"><b>{esc(r.get("jmeno", ""))}</b><span>{popis}</span>'
            f'<span class="when">{kdy}</span></figcaption></figure>')
    return '\n        '.join(vystup)


def reference_html(seznam, jazyk):
    vystup = []
    for i, r in enumerate(seznam):
        kde = f'reference.json, položka {i + 1}'
        nazev, _ = prelozit(r.get('nazev'), jazyk, kde) if r.get('nazev') else ('', jazyk)
        if not nazev:
            chyba(f'{kde}: chybí „nazev“')
        popis, _ = prelozit(r.get('popis', ''), jazyk, kde) if r.get('popis') else ('', jazyk)
        vystup.append(f'<li class="ref-card"><span class="ref-name">{esc(nazev)}</span><span class="ref-occ">{esc(popis)}</span></li>')
    return '\n          '.join(vystup)


def vloz(s, znacka, obsah, odsazeni, soubor):
    pat = re.compile(rf'(<!-- {znacka}:START[^>]*-->)(.*?)(<!-- {znacka}:END -->)', re.S)
    if len(pat.findall(s)) != 1:
        sys.exit(f'CHYBA: v {soubor} chybí značky <!-- {znacka}:START --> a <!-- {znacka}:END -->')
    return pat.sub(lambda m: m.group(1) + '\n' + odsazeni + obsah + '\n' + odsazeni + m.group(3), s)


def sekce_recenzi(s, pocet):
    """Bez jediné recenze se celá sekce skryje (atribut hidden), s první recenzí se sama ukáže."""
    return re.sub(r'(<section class="[^"]*" id="reviews")( hidden)?',
                  lambda m: m.group(1) + ('' if pocet else ' hidden'), s)


def sipky(s, pocet):
    """Šipky u recenzí jen tehdy, když jsou aspoň dvě."""
    for idv in ('revPrevBtn', 'revNextBtn'):
        s = re.sub(rf'(<button type="button" class="rev-arrow [a-z]+" id="{idv}")( style="display:none")?',
                   lambda m: m.group(1) + ('' if pocet > 1 else ' style="display:none"'), s)
    return s


YT_ID = re.compile(r'(?:youtu\.be/|[?&]v=|/shorts/|/embed/|/live/)([A-Za-z0-9_-]{11})(?![A-Za-z0-9_-])')


def yt_id(url):
    m = YT_ID.search(url or '')
    return m.group(1) if m else None


def text_nebo_preklady(pole, kde, nazev_pole):
    """Text, nebo {"cs": …, "en": …, "de": …} (stačí "cs"; chybějící jazyk stránka nahradí češtinou)."""
    if isinstance(pole, str):
        return pole.strip()
    if isinstance(pole, dict) and isinstance(pole.get('cs'), str) and pole['cs'].strip():
        return {k: pole[k] for k in ('cs', 'en', 'de') if isinstance(pole.get(k), str) and pole[k].strip()}
    chyba(f'{kde}: „{nazev_pole}“ musí být text, nebo {{"cs": …, "en": …, "de": …}} s českým textem')
    return ''


def videa_js(seznam):
    """Řádky seznamu videí pro media.js."""
    if not seznam:
        chyba('videa.json: seznam videí je prázdný, nechte tam aspoň jedno video')
    radky = []
    videna = {}
    for i, v in enumerate(seznam):
        kde = f'videa.json, položka {i + 1} ({v.get("nazev", "?") if isinstance(v.get("nazev"), str) else "?"})'
        if not isinstance(v, dict):
            chyba(f'videa.json, položka {i + 1}: položka musí být ve složených závorkách {{ … }}')
            continue
        url = v.get('url', '')
        vid = yt_id(url)
        if not vid:
            chyba(f'{kde}: v „url“ není platný odkaz na YouTube video („{url}“)')
            continue
        if vid in videna:
            chyba(f'{kde}: stejné video už je v položce {videna[vid]}')
        videna[vid] = i + 1
        if not v.get('nazev'):
            chyba(f'{kde}: chybí „nazev“ (název skladby)')
            continue
        polozka = {'name': text_nebo_preklady(v['nazev'], kde, 'nazev')}
        if v.get('misto'):
            polozka['place'] = text_nebo_preklady(v['misto'], kde, 'misto')
        polozka['yt'] = vid
        na_vysku = v.get('na_vysku')
        if na_vysku is None:
            na_vysku = '/shorts/' in url
        elif not isinstance(na_vysku, bool):
            chyba(f'{kde}: „na_vysku“ musí být true nebo false (bez uvozovek), nebo položku vynechte')
        polozka['vert'] = bool(na_vysku)
        nahled = v.get('nahled')
        if nahled:
            if not re.match(r'^video/[^/]+$', nahled):
                chyba(f'{kde}: „nahled“ musí být soubor ve složce video, např. „video/route66.webp“')
            elif not (ROOT / nahled).exists():
                chyba(f'{kde}: soubor „{nahled}“ v repozitáři neexistuje')
            else:
                polozka['thumb'] = nahled[len('video/'):]
        radky.append('    ' + json.dumps(polozka, ensure_ascii=False) + ',')
    return '\n'.join(radky)


def vloz_media(s, obsah):
    # značky platí jen na začátku vlastního řádku (zmínka v komentáři o kus výš se nepočítá)
    pat = re.compile(r'(^[ \t]*// VIDEA:START[^\n]*\n)(.*?)(^[ \t]*// VIDEA:END[ \t]*$)', re.S | re.M)
    if len(pat.findall(s)) != 1:
        sys.exit('CHYBA: v media.js chybí značky // VIDEA:START a // VIDEA:END')
    return pat.sub(lambda m: m.group(1) + obsah + '\n' + m.group(3), s)


def main():
    vsechny = nacti('recenze.json', 'recenze')
    # položka s "vzor": true je jen ukázka, jak recenzi vyplnit; na web se nedostane
    recenze = [r for r in vsechny if not r.get('vzor')]
    reference = nacti('reference.json', 'reference')
    videa = nacti('videa.json', 'videa')
    media = ROOT / 'media.js'
    m_puvodni = media.read_text(encoding='utf-8')
    m_novy = vloz_media(m_puvodni, videa_js(videa))  # videa se kontrolují dřív, než se cokoli zapíše
    for jazyk, soubor in PAGES.items():
        p = ROOT / soubor
        s = p.read_text(encoding='utf-8')
        s = vloz(s, 'RECENZE', recenze_html(recenze, jazyk), '        ', soubor)
        s = vloz(s, 'REFERENCE', reference_html(reference, jazyk), '          ', soubor)
        s = sipky(s, len(recenze))
        s = sekce_recenzi(s, len(recenze))
        if not CHYBY:
            p.write_text(s, encoding='utf-8')
    if not CHYBY and m_novy != m_puvodni:
        media.write_text(m_novy, encoding='utf-8')
    llms = ROOT / 'llms.txt'
    if llms.exists() and not CHYBY:
        t = llms.read_text(encoding='utf-8')
        jmena = ', '.join(prelozit(r.get('nazev'), 'cs', 'llms')[0] for r in reference)
        t2 = re.sub(r'^(- Reference [^:]*: ).*$', lambda m: m.group(1) + jmena, t, count=1, flags=re.M)
        if t2 != t:
            llms.write_text(t2, encoding='utf-8')
    if CHYBY:
        sys.exit('Nic jsem nezměnil, v souborech jsou chyby:\n- ' + '\n- '.join(dict.fromkeys(CHYBY)))
    vzory = len(vsechny) - len(recenze)
    print(f'Hotovo: {len(recenze)} recenzí, {len(reference)} referencí, {len(videa)} videí ({SITE}).'
          + (f' Vzorů, které se nezobrazují: {vzory}.' if vzory else ''))


if __name__ == '__main__':
    main()
