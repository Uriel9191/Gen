import json
import sys

HTML_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

m_prefix = 'const mainData = '
m_start = text.find(m_prefix)
g_prefix = 'const genData = '
g_start = text.find(g_prefix)
m_end = text.rfind('];', m_start, g_start) + 1
g_end = text.find("\n];", g_start) + 2

main_data = json.loads(text[m_start + len(m_prefix):m_end])
gen_data = json.loads(text[g_start + len(g_prefix):g_end])

print(f"Załadowano bazę: mainData={len(main_data)}, genData={len(gen_data)}")

def search_gen_data(query):
    q = query.strip().lower()
    if not q:
        return []
    words = [w for w in q.split() if w not in ['wdowa', 'sukcesor', 'sukcesorowie', 'z', 'plac', 'pusty', 'pole', 'ogród', 'żona', 'synem', 'dziećmi', 'żyd', 'sławetny', 'uczciwy', 'starszy', 'wtóry', 'drugi', 'wpis/ogród', 'pan', 'jp']]
    if not words:
        words = q.split()
    hits = []
    for d in gen_data:
        searchable_parts = [
            str(d.get('lp', '')),
            d.get('nazwisko', ''),
            d.get('imie', ''),
            d.get('miejsce', ''),
            d.get('funkcja', ''),
            d.get('funkcja_zawod', ''),
            d.get('wariant_nazwiska', ''),
            d.get('notatka_biograficzna', ''),
            d.get('uwagi', '')
        ]
        blob = ' '.join(p for p in searchable_parts if p).lower()
        if all(w in blob for w in words):
            hits.append(d)
    return hits

TEST_QUERIES = [
    # 1. Nowe profile Partii 12 (lp 938-956)
    'Michał Wyszyński',
    'Baron Michał Wyszyński',
    'Major Wyszyński',
    'Antoni Okoń',
    'Antoni Okuń',
    'Szafarz Okoń',
    'Exaktor Okoń',
    'Augustyn Starkiewicz',
    'Augustyn Chartkiewicz',
    'Augustyn Charkiewicz',
    'Pisarz Chartkiewicz',
    'Pikuwiński',
    'Burgrabia Pikuwiński',
    'Broniszewski',
    'Rewizor Broniszewski',
    'Grzegorz Dybicki',
    'Grzegorz Zdybicki',
    'Jan Potokowicz',
    'Piotr Potokiewicz',
    'Podcechmistrz Potokiewicz',
    'Grzegorz Leśniowski',
    'Cechmistrz Leśniowski',
    'Jan Kołakiewicz',
    'Podcechmistrz Kołakiewicz',
    'Hieronim Kozakowicz',
    'Podcechmistrz Kozakowicz',
    'Mikołaj Jażdżykowski',
    'Mikołay Jażdżykowski',
    'Szymon Lewkowicz',
    'Szymon Lefkowicz',
    'Wojciech Drusiołka',
    'Woyciech Drusiołka',
    'Józef Żyd',
    'Jozef Żyd',
    'Wdowa Łazarzowa',
    'Łazarzowa',
    'Wdowa Błażejowa',
    'Błażejowa',
    'Jan Frankowicz',
    'Jan Frankiewicz',
    'Pan Frampolski',
    'Frampolski',
    'Imć Pan Frampolski',
    
    # 2. Główni urzędnicy i mieszkańcy występujący w Partii 12
    'Józef Paszkiewicz',
    'Wójt Paszkiewicz',
    'Józef Paszkiewicz Wójt',
    'Franciszek Barankiewicz',
    'Wójt Barankiewicz',
    'Barankiewicz',
    'Łukasz Dybicki',
    'Łukasz Zdybicki',
    'Szafarz Dybicki',
    'Andrzej Wyszyński',
    'Sędzia Wyszyński',
    'Franciszek Frankiewicz',
    'Burmistrz Frankiewicz',
    'Kazimierz Celej',
    'Burmistrz Celej',
    'Jan Wilczyński',
    'Burmistrz Wilczyński',
    'Jakub Gąska',
    'Burmistrz Gąska',
    'Franciszek Chrzanowski',
    'Dyrektor Chrzanowski',
    'Zofia Chrzanowska',
    'Kazimierz Rycerz',
    'Maciej Rycerz',
    'Kotton',
    'Woźny Kotton',
    'Kazimierz Wojtas',
    'Kazimierz Wojtan',
    'Aleksander Alkiewicz',
    'Walenty Łukasik',
    'Walenty Pilaszkiewicz',
    'Sebastian Latosiewicz',
    'Wojciech Latosiewicz',
    'Stanisław Bosoniak',
    'Paweł Frużyński',
    'Mikołaj Łapczyński',
    'Franciszek Matuszkiewicz',
    'Jędrzej Barankiewicz',
    'Andrzej Zamoyski',
    'Jan Zamoyski',
    'Rubin',
    'Arendarz Rubin',
    'Łuczyński',
    'Pisarz Łuczyński',
    'Piotr Młynarczyk'
]

passed = 0
failed = 0
failures = []

for q in TEST_QUERIES:
    hits = search_gen_data(q)
    if hits:
        passed += 1
    else:
        failed += 1
        failures.append(q)

print(f"Wyniki testu onomastycznego Partii 12: {passed}/{len(TEST_QUERIES)} ({passed/len(TEST_QUERIES)*100:.1f}% PASS)")

if failed > 0:
    print("NIEPOWODZENIA:")
    for f in failures:
        print(f"  - Brak trafienia dla: '{f}'")
    sys.exit(1)
else:
    print("ŻELAZNA ZASADA 100% SYNCHRONIZACJI ONOMASTYCZNEJ SPEŁNIONA DLA PARTII 12!")
