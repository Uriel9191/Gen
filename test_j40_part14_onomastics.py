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
g_end = text.find('\n];', g_start) + 2

main_data = json.loads(text[m_start + len(m_prefix):m_end])
gen_data = json.loads(text[g_start + len(g_prefix):g_end])

print(f"Załadowano bazę: mainData={len(main_data)}, genData={len(gen_data)}")

def search_gen_data(query):
    q = query.strip().lower()
    if not q:
        return []
    words = [w for w in q.split() if w not in ['wdowa', 'sukcesor', 'sukcesorowie', 'z', 'plac', 'pusty', 'pole', 'ogród', 'żona', 'synem', 'dziećmi', 'żyd', 'sławetny', 'uczciwy', 'starszy', 'wtóry', 'drugi', 'wpis/ogród', 'pan', 'jp', 'wielmożny', 'imść']]
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
    # 1. Nowe profile Partii 14 (lp 970-975)
    'Felicjan Jełowicki',
    'Felician Mirosz',
    'Pisarz Jełowicki',
    'Szczepan Popiołek',
    'Szczepan Popiel',
    'Exaktor Popiołek',
    'Antoni Gąska',
    'Podcechmistrz Gąska',
    'Andrzej Zdybicki',
    'Andrzey Zdybicki',
    'Podcechmistrz Zdybicki',
    'Wawrzyniec Gołębiowski',
    'Cechmistrz Gołębiowski',
    'Stanisław Potokowicz',
    'Cechmistrz Potokowicz',
    
    # 2. Główni urzędnicy i postacie Partii 14
    'Aleksander Leopold Baron Wyszyński',
    'Baron Wyszyński',
    'Burgraf Wyszyński',
    'Józef Paszkiewicz',
    'Wójt Paszkiewicz',
    'Jakub Gąska',
    'Wójt Gąska',
    'Jan Frankiewicz',
    'Burmistrz Frankiewicz',
    'Walenty Piłaszkiewicz',
    'Walenty Pielaskiewicz',
    'Jan Wilczyński',
    'Burmistrz Wilczyński',
    'Piotr Potokowicz',
    'Piotr Potolicewicz',
    'Franciszek Barankiewicz',
    'Deputat Barankiewicz',
    'Franciszek Matuszkiewicz',
    'Ławnik Matuszkiewicz',
    'Wojciech Pielaszkiewicz',
    'Woyciech Pielaszkiewicz',
    'Ławnik Pielaszkiewicz',
    'Piotr Szydłowski',
    'Ławnik Szydłowski',
    'Grzegorz Latosiewicz',
    'Ławnik Latosiewicz',
    'Krzysztof Szulczerzyński',
    'Krzysztof Szuliczyński',
    'Cechmistrz Szulczerzyński',
    'Jędrzej Barankiewicz',
    'Andrzey Barankiewicz',
    'Łukasz Zdybicki',
    'Sługa Zdybicki',
    'Herszek Lewkowicz',
    'Cechmistrz Krawiecki',
    'Stanisław Doliński',
    'Sędzia Doliński'
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

print(f"Wyniki testu onomastycznego Partii 14: {passed}/{len(TEST_QUERIES)} ({passed/len(TEST_QUERIES)*100:.1f}% PASS)")

if failed > 0:
    print("NIEPOWODZENIA:")
    for f in failures:
        print(f"  - Brak trafienia dla: '{f}'")
    sys.exit(1)
else:
    print("ŻELAZNA ZASADA 100% SYNCHRONIZACJI ONOMASTYCZNEJ SPEŁNIONA DLA PARTII 14!")
