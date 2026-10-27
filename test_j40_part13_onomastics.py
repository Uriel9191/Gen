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
    # 1. Nowe profile Partii 13 (lp 957-969)
    'Aleksander Leopold Baron Wyszyński',
    'Aleksander Leopold Wyszyński',
    'Baron Wyszyński',
    'Burgraf Wyszyński',
    'Daniel Walczyński',
    'Dominik Walczyński',
    'Ławnik Walczyński',
    'Kazimierz Frankowicz',
    'Cechmistrz Frankowicz',
    'Jan Reszkiewicz',
    'Podskarbi Reszkiewicz',
    'Stanisław Wojtaszek',
    'Cechmistrz Wojtaszek',
    'Józef Kwieciński',
    'Podskarbi Kwieciński',
    'Maciej Młynarski',
    'Maciey Młynarski',
    'Cechmistrz Młynarski',
    'Antoni Kuśnierz',
    'Podskarbi Kuśnierz',
    'Szymon Cieślicki',
    'Cechmistrz Cieślicki',
    'Bartłomiej Kozłowski',
    'Bartłomiey Kozłowski',
    'Cechmistrz Kozłowski',
    'Gmusiel',
    'Pisarz Gmusiel',
    'ks. Dziekan kraśnicki',
    'ks. Proboszcz dziekan kraśnicki',
    'Dziekan Kraśnicki',
    'Proboszcz Kraśnicki',
    'Jan Alkiewicz',
    'Śp. Jan Alkiewicz',
    
    # 2. Główni urzędnicy i mieszkańcy występujący w Partii 13
    'Michał Baron Wyszyński',
    'Major Wyszyński',
    'Franciszek Barankiewicz',
    'Wójt Barankiewicz',
    'Marcin Wilczyński',
    'Exaktor Marcin Wilczyński',
    'Felix Mirosz',
    'Feliks Mirosz',
    'Pisarz Mirosz',
    'Jakub Gąska',
    'Burmistrz Gąska',
    'Walenty Bielaszkiewicz',
    'Walenty Pielaszkiewicz',
    'Walenty Łukasik',
    'Burmistrz Łukasik',
    'Piotr Potokowicz',
    'Piotr Potolicewicz',
    'Burmistrz Potokowicz',
    'Franciszek Frankiewicz',
    'Deputat Frankiewicz',
    'Paweł Latyszowicz',
    'Paweł Latosiewicz',
    'Exaktor Latyszowicz',
    'Wojciech Latosiewicz',
    'Ławnik Latosiewicz',
    'Franciszek Matuszkiewicz',
    'Ławnik Matuszkiewicz',
    'Matuszewski',
    'Dyrektor Matuszewski',
    'Jan Szulczerzyński',
    'Pisarz Szulczerzyński',
    'Jan Cichocki',
    'Woźny Cichocki',
    'Antoni Zabłocki',
    'Antoni Zaboklicki',
    'Delegat Zabłocki',
    'Łukasz Zdybicki',
    'Łukasz Dybicki',
    'Antoni Okoń',
    'Exaktor Okoń',
    'Aleksander Alkiewicz',
    'Pisarz Alkiewicz',
    'Jan Zamoyski',
    'Ordynat Andrzej Zamoyski',
    'Szymon Lewkowicz'
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

print(f"Wyniki testu onomastycznego Partii 13: {passed}/{len(TEST_QUERIES)} ({passed/len(TEST_QUERIES)*100:.1f}% PASS)")

if failed > 0:
    print("NIEPOWODZENIA:")
    for f in failures:
        print(f"  - Brak trafienia dla: '{f}'")
    sys.exit(1)
else:
    print("ŻELAZNA ZASADA 100% SYNCHRONIZACJI ONOMASTYCZNEJ SPEŁNIONA DLA PARTII 13!")
