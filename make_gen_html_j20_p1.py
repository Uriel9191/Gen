# -*- coding: utf-8 -*-

with open('/home/ubuntu/workspace/Gen/generate_j19_html_part1_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

replacements = [
    ('main_data_j19_part1.json', 'main_data_j20_part1.json'),
    ('gen_data_j19_part1.json', 'gen_data_j20_part1.json'),
    ('krasnik_j19_kompendium_calosc.html', 'krasnik_j20_kompendium_calosc.html'),
    ('Jednostka 19 – Akta Miasta Kraśnika (1657–1661)', 'Jednostka 20 – Akta Miasta Kraśnika (1656–1700)'),
    ('Sygn. 35/40/0/1/19 (dawny Tom 9 / mikr. 110358) [1657–1661]', 'Sygn. 35/40/0/1/20 (dawna sygn. 7 / mikr. 110399) [1656–1700]'),
    ('Akta Miasta Kraśnika – Protocollum Causarum et Actionum Officii Consularis', 'Akta Miasta Kraśnika – Acta Officii Advocatialis et Scabinalis'),
    ('Protocollum causarum et actorum officii consularis (1657–1661) • Partia 1 (skany 1–25 z 120) • Sygn. 35/40/0/1/19', 'Księga Sądu Wójtowskiego i Ławniczego (1656–1700) • Partia 1 (skany 1–25 z 283) • Sygn. 35/40/0/1/20'),
    ('Postęp Indeksacji Jednostki 18', 'Postęp Indeksacji Jednostki 20'),
    ('Partia 1: skany 1–25 z 120 (fol. 1r–11r) • AP Lublin', 'Partia 1: skany 1–25 z 283 (fol. 1r–10v) • AP Lublin'),
    ('1657–1827 r.', '1656–1700 r.'),
    ('https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989899', 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914'),
    ('35/40/0/1/19', '35/40/0/1/20'),
]

for old, new in replacements:
    assert old in src, f"Missing replacement target: {old}"
    src = src.replace(old, new)

# Podmiana filtra lat
old_years = '''            <option value="1657">Rok 1657</option>
            <option value="1658">Rok 1658</option>
            <option value="1659">Rok 1659</option>
            <option value="1660">Rok 1660</option>
            <option value="1661">Rok 1661</option>
            <option value="1827">Rok 1827 (poświadczenie)</option>'''

new_years = '''            <option value="1656">Rok 1656</option>
            <option value="1657">Rok 1657</option>
            <option value="1658">Rok 1658</option>
            <option value="1664">Rok 1664</option>
            <option value="1668">Rok 1668</option>
            <option value="1683">Rok 1683</option>
            <option value="1686">Rok 1686</option>
            <option value="1695">Rok 1695</option>
            <option value="1697">Lata 1697–1700</option>'''
assert old_years in src, "Missing old_years"
src = src.replace(old_years, new_years, 1)

# Podmiana monograph_html
idx_m1 = src.index("monograph_html = '''")
idx_m2 = src.index("analytics_html = '''")
new_monograph = """monograph_html = '''        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział I: Kodykologia i Metryka Księgi Sądu Wójtowskiego (skany 1–5)</h2>
          <div class="chapter-content">
            <p>Jednostka archiwalna o sygnaturze <strong>35/40/0/1/20</strong> (dawna sygn. <strong>Nr 7 / Nr 465</strong>, mikrofilm nr <code>110399</code> z 30 X 1959 r., format 33 × 21 cm, łącznie 283 skany) stanowi księgę Sądu Wójtowskiego i Ławniczego miasta Kraśnika (<em>Acta officii advocatialis et scabinalis</em>, w metryce: <em>Książka różnych czynności cywilnych</em>). Właściwy blok rękopisu poprzedzają: klatka początkowa mikrofilmu (#1), formularz Wzór Nr 1 (#2), karta informacyjna z wykazem stron pustych niefotografowanych (#3), szyld tytułowy z zakresem lat 1657–1699 (#4) oraz wtórna XIX-wieczna karta ochronna z drukowanym formularzem przesłuchania świadka (#5).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział II: Pierwsze Sprawy Sądu Wójtowskiego z Listopada–Grudnia 1657 r. (skany 6–15)</h2>
          <div class="chapter-content">
            <p>Początkowe karty (<code>fol. 1r–5v</code>) rejestrują intensywną działalność Sądu Wójtowskiego i Ławniczego w listopadzie i grudniu 1657 r. z udziałem ławników przysięgłych <strong>Błażeja Kołodziejczyka</strong>, <strong>Macieja Konięgi</strong>, <strong>Augustyna Kurowica</strong> i <strong>Grzegorza Foxa</strong>. Dominują spory o długi pieniężne i dostawy zboża (<strong>Stanisław Trela</strong> vs <strong>Anna Łapczyńska [?]</strong> o <code>6 fl 20 gr</code>, #9–#10; <strong>Barbara Kuśnierz [?]</strong> vs <strong>Kudła [?]</strong> o <code>43 złp</code> na gruncie, #12; <strong>Augustyn Kurowic</strong> o <code>23 fl</code> i <code>11 fl</code>, #14–#15), spory opiekuńcze <strong>Pawła Łycka</strong> z wdową <strong>Anną Łyckową</strong> o <code>30 złp</code> (#8–#10) oraz szczegółowa obdukcja ran <strong>Mikołaja Pisaka [?] alias Ruska [?]</strong> pobitego w domu <strong>Jana Lecha</strong> (#9).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział III: Odkrycie Kart z Grudnia 1656 r. i Sprawa Jerzego Espena (skany 16–18)</h2>
          <div class="chapter-content">
            <p>Kluczowym odkryciem kodykologicznym Partii 1 jest obecność na kartach <code>fol. 6r–7r</code> (#16–#18) oryginalnych wpisów z <strong>grudnia 1656 roku</strong> (9 XII, 13 XII, 15 XII i 18 XII 1656 r.), wyprzedzających datę 1657 r. podaną na okładce i w katalogu SwA. Obok spraw majątkowych (dział dóbr po <strong>Bochanie [?]</strong> i <strong>Andrzeju Szpakowskim</strong>, #16; protestacja wdowy <strong>Maryny Młodnickiej</strong> przeciw ślusarzowi <strong>Andrzejowi Pieniążkowi</strong>, #17), zapisano tu głośną protestację <strong>Jerzego Espena [?]</strong>, sługi mieszczanina lubelskiego <strong>Jakuba Deserta</strong>, przeciw rajcy kraśnickiemu <strong>Marcinowi Sitarskiemu</strong> o pobicie w domu rajcy <strong>Stanisława Nawrockiego</strong> podczas rozmowy w języku niemieckim (#18).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IV: Procesy Rzemieślników, Bójka u Paździechy i Sąd Wielki Gajony (skany 19–25)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 7v–10v</code> powracają do grudnia 1657 r., przynosząc areszt opiekunów <strong>Jana Kulki</strong> i <strong>Szymona Jajczyka</strong> na dobrach po śp. <strong>Jakubie Jajczyku</strong> w domu <strong>Tomasza Larkowskiego</strong> (#19), zeznania świadków (<strong>Michał Brzostek [?]</strong>, <strong>Adam Kapica</strong>, <strong>Wojciech Rogalowski [?]</strong>, <strong>Maciej Rzepka [?]</strong>) w długotrwałym sporze o pobicie i zniewagi między <strong>Wawrzyńcem Sydkowicem</strong> a <strong>Szymonem Jasielskim</strong> (#21–#24) oraz otwarcie Sądu Wielkiego Gajonego (<em>Judicium Magnum Bannitum</em>) z 7 XII 1657 r. ze sprawą <strong>Macieja Konięgi</strong> o najem izby (#25).</p>
          </div>
        </article>'''\n\n"""

idx_a_end = src.index("main_data_json = json.dumps")
new_analytics = """analytics_html = '''        <article class="analytic-card">
          <h2 class="card-title">📅 1. Odkrycie Chronologiczne: Wpisy z Grudnia 1656 r. Przed Datą Tytułową (skany #16–#18)</h2>
          <div class="card-content">
            <p>Choć inwentarz archiwalny oraz XIX-wieczna okładka (#4) datują księgę od roku <strong>1657</strong>, karty <code>fol. 6r–7r</code> zachowały wszyte protokoły z <strong>9–18 grudnia 1656 r.</strong> (Sąd Łączony z 9 XII 1656 r. i Sąd Wójtowski z 13, 15 i 18 XII 1656 r.), przesuwając rzeczywisty początek chronologiczny woluminu o rok wstecz.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🗣️ 2. Konflikt Językowy i Pobicie Sługi Lubelskiego w Domu Nawrockiego (skan #18)</h2>
          <div class="card-content">
            <p>Dnia <strong>18 XII 1656 r.</strong> <strong>Jerzy Espen [?]</strong>, sługa mieszczanina lubelskiego <strong>Jakuba Deserta</strong>, oskarżył rajcę kraśnickiego <strong>Marcina Sitarskiego</strong> o napaść w domu rajcy <strong>Stanisława Nawrockiego</strong> z powodu rozmowy prowadzonej po niemiecku (<em>„czego po niemiecku gadam”</em>). Ławnicy <strong>Marcin Starzyński</strong> i <strong>Błażej Kołodziejczyk</strong> odnotowali podbite lewe oko, zakrwawioną rękę i guzy na głowie.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🩹 3. Obdukcje Sądowe i Konflikty Sasiedzkie na Jarmarkach (skany #9, #11, #21–#24)</h2>
          <div class="card-content">
            <p>Księga wójtowska dokładnie dokumentuje obdukcje ran (<strong>Mikołaj Pisak [?] alias Rusek [?]</strong> pobity w domu <strong>Jana Lecha</strong>, #9) oraz przesłuchania świadków z jarmarków w Łęcznej i Kraśniku (zeznania szewca <strong>Wojciecha Olęckiego</strong>, #11; <strong>Adama Kapicy</strong> i <strong>Michała Brzostka [?]</strong> w sporze <strong>Wawrzyńca Sydkowica</strong> z <strong>Szymonem Jasielskim</strong>, #21–#24).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 4. Funkcjonowanie Sądu Wójtowskiego i Wielkiego Gajonego w 1657 r. (skany #6–#25)</h2>
          <div class="card-content">
            <p>W odróżnieniu od księgi radzieckiej (J19), Sąd Wójtowski (w składzie m.in. <strong>Błażej Kołodziejczyk</strong>, <strong>Maciej Konięga</strong>, <strong>Augustyn Kurowic</strong>, <strong>Grzegorz Fox</strong>, woźny <strong>Jakub Rogalka</strong>) rozstrzygał bieżące spory rzemieślnicze (roboty kołodziejskie i ślusarskie, skóry butowe), opieki nad sierotami (<strong>Jajczykowie</strong>, <strong>Łyckowie</strong>) oraz sprawy czynszowe na sesjach <em>Judicium Magnum Bannitum</em> (#25).</p>
          </div>
        </article>'''\n"""

src = src[:idx_m1] + new_monograph + new_analytics + src[idx_a_end:]

with open('/home/ubuntu/workspace/Gen/generate_j20_html_part1_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Utworzono generate_j20_html_part1_authentic.py")
