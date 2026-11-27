# -*- coding: utf-8 -*-
with open("generate_j20_html_part1_authentic.py", "r", encoding="utf-8") as f:
    src = f.read()

# 1. Podmiana sciezek i metadanych J20 -> J21
replacements = [
    ("main_data_j20_part1.json", "main_data_j21_part1.json"),
    ("gen_data_j20_part1.json", "gen_data_j21_part1.json"),
    ("krasnik_j20_kompendium_calosc.html", "krasnik_j21_kompendium_calosc.html"),
    ("krasnik_j20_slownik_genealogiczny.csv", "krasnik_j21_slownik_genealogiczny.csv"),
    ("krasnik_j20_indeks_skanow.csv", "krasnik_j21_indeks_skanow.csv"),
    ("Jednostka 20 – Akta Miasta Kraśnika (1656–1700)", "Jednostka 21 – Akta Miasta Kraśnika (1662–1685)"),
    ("AP Lublin • Zespół 35/40/0 • Sygn. 35/40/0/1/20 (dawna sygn. 7 / mikr. 110399) [1656–1700]",
     "AP Lublin • Zespół 35/40/0 • Sygn. 35/40/0/1/21 (dawna sygn. 10 / mikr. 110402) [1662–1685]"),
    ("Akta Miasta Kraśnika – Acta Officii Advocatialis et Scabinalis",
     "Akta Miasta Kraśnika – Księga Wójtowsko-Ławnicza i Burmistrzowsko-Radziecka"),
    ("Księga Sądu Wójtowskiego i Ławniczego (1656–1700) • Partia 1 (skany 1–25 z 283) • Sygn. 35/40/0/1/20",
     "Księga Wójtowsko-Ławnicza i Burmistrzowsko-Radziecka (1662–1685) • Partia 1 (skany 1–25 z 606) • Sygn. 35/40/0/1/21"),
    ("Partia 1: skany 1–25 z 283 (fol. 1r–10v) • AP Lublin",
     "Partia 1: skany 1–25 z 606 (fol. 1r–11r) • AP Lublin"),
    ("6989914", "6989934"),
    ("Otwórz Jednostkę 20", "Otwórz Jednostkę 21"),
]

for old, new in replacements:
    src = src.replace(old, new)

# 2. Podmiana monograph_html
start_m = src.index("monograph_html = '''")
end_m = src.index("analytics_html = '''")

j21_monograph = '''monograph_html = \'\'\'        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział I: Kodykologia i Metryka Księgi Nr 10 (skany 1–4)</h2>
          <div class="chapter-content">
            <p>Jednostka archiwalna o sygnaturze <strong>35/40/0/1/21</strong> (dawna sygnatura <strong>Nr 10</strong>, mikrofilm nr <code>110402</code> z <code>3 XI 1959 r.</code>, przygotowana do mikrofilmowania <code>10 IV 1959 r.</code>, format <code>34 × 23 cm</code>, łącznie <code>606</code> skanów) nosi w katalogu tytuł <em>[Księga wójtowsko-ławnicza i burmistrzowsko-radziecka]</em> (w metryce archiwalnej: <em>Księga m. Kraśnika różnych czynności cywiln.</em>). Karta informacyjna (<code>#3</code>) wymienia 14 stron pustych niefilmowanych (m.in. <code>67v, 85, 100</code>), a oryginalny szyld okładkowy (<code>#4</code>) podaje zakres lat <code>1671–1685</code> oraz objętość <code>391</code> kart (katalog SwA: <code>1662–1684</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział II: Odkrycie Brulionu i Czystopisu Protokołów z 1671 r. (skany 5–10, 21–25)</h2>
          <div class="chapter-content">
            <p>Analiza porównawcza pierwszych 25 skanów ujawniła unikalną strukturę kancelaryjną: karty <code>fol. 1r–8v</code> (<code>#5–#20</code>) tworzą pierwotny brulion protokołów Sądu Wójtowskiego i Ławniczego z września i października <strong>1671 r.</strong>, natomiast od karty <code>fol. 9r</code> (<code>#21</code>, noszącej równoległą numerację <code>1</code>) pisarz rozpoczął systematyczny czystopis tych samych akt. W czystopisie poprawiono m.in. błędną datę roczną <code>1670</code> na <code>1671</code> w sprawie <strong>Kazimierza Szklarza</strong> przeciw <strong>Janowi Kowalikowi</strong> (<code>#5</code> vs <code>#21</code>) oraz podwyższono i sprecyzowano dług <strong>Grzegorza Foxa</strong> dla Bractwa Różańcowego z <code>30 złp</code> (<code>#9</code>) na <code>60 złp / 65 złp</code> (<code>#24</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział III: Spory Szewskie na Jarmarku w Urzędowie i Relacje Sąsiedzkie (skany 6–14, 22–25)</h2>
          <div class="chapter-content">
            <p>Centralnym procesem rzemieślniczym września 1671 r. jest spór szewców <strong>Stanisława Partyki</strong> i <strong>Wojciecha Nogaja</strong> o pomieszanie skór na jarmarku w Urzędowie obok szewca z Opola (<code>#6–#8, #10–#12, #22–#23, #25</code>), rozstrzygnięty na podstawie zeznań <strong>Reginy Grymuzyny</strong>, <strong>Wojciecha Potockiego</strong> i <strong>Stanisława Magierowskiego</strong> nakazem przeprosin przy 6 świadkach w Zarzeczu lub przed zamkiem. Równolegle toczył się wielowątkowy konflikt byłego rajcy <strong>Stanisława Nawrockiego</strong> z <strong>Adamem Łeżykiem</strong> i <strong>Piotrem Kępką</strong> o szkody w zbożu na niwie krakowskiej i odbicie zajętych wołów (<code>#9–#11, #14, #23–#25</code>), a także przysięga poddanych z Budzyna <strong>Szymona Łatki</strong> i <strong>Jana Wronki</strong> w dzierżawie <strong>Jana Zana</strong> (<code>#10, #13, #25</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IV: Obdukcje Ran, Kredyt Zastawny i Handel Nieruchomościami (skany 8, 14–20)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 5v–8v</code> dokumentują liczne obdukcje ran dokonywane przez ławników <strong>Pawła Smarowica</strong>, <strong>Sebastiana Balusika</strong>, <strong>Błażeja Kołodziejczyka</strong>, <strong>Wojciecha Kurewica [?]</strong>, <strong>Tomasza Pałęgę</strong> i <strong>Macieja Bielaszkowica</strong>: pobicia brzemiennej <strong>Marianny Nawrockiej</strong> (<code>#16</code>), <strong>Zofii Maraszkowej</strong> (<code>#12</code>), ławnika <strong>Wojciecha Kurewica [?]</strong> z żoną i furmanem (<code>#15</code>), <strong>Jakuba Tatara</strong> ze wsi Kiełczowice (<code>#15</code>), <strong>Krzysztofa Trojczaka</strong> z ramienia wójta <strong>Ubalda Janaszkowicza</strong> (<code>#18</code>) oraz sługi rajcy <strong>Grzegorza Foxa</strong> (<code>#19</code>). W dziedzinie obrotu kredytowego odnotowano zastawy u Żyda <strong>Wygdora</strong> przez ślusarza <strong>Andrzeja Pieniążka</strong> (<code>14 złp</code>, <code>#8, #23</code>), wycenę srebra guzikowego próby <code>9</code> (<code>#14</code>), sprawę <strong>Józefa Grota</strong> z Żydem <strong>Zeldą</strong> (<code>#20</code>) oraz zeznanie burmistrza <strong>Michała Dubielowica</strong> o sprzedaży domu za <code>160 złp</code> (<code>#16</code>).</p>
          </div>
        </article>\'\'\'\n\n'''

src = src[:start_m] + j21_monograph + src[end_m:]

# 3. Podmiana analytics_html
start_a = src.index("analytics_html = '''")
end_a = src.index("main_data_json = json.dumps")

j21_analytics = '''analytics_html = \'\'\'        <article class="analytic-card">
          <h2 class="card-title">📑 1. Kodykologia: Brulion (fol. 1r–8v) i Czystopis (fol. 9r–11r) w Jednym Tomie (skany #5–#25)</h2>
          <div class="card-content">
            <p>Porównanie skanów <code>#5–#10</code> ze skanami <code>#21–#25</code> dowodzi, że pierwsze 8 kart woluminu stanowiło roboczy brulion protokołów z IX–X 1671 r., przepisany następnie na czysto od <code>fol. 9r</code>. W czystopisie skorygowano omyłkę roczną <code>1670 → 1671</code> (<code>#5</code> vs <code>#21</code>) oraz zaktualizowano dług <strong>Grzegorza Foxa</strong> z <code>30 złp</code> na <code>60/65 złp</code> (<code>#9</code> vs <code>#24</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">👞 2. Handel Skórami na Jarmarku w Urzędowie i Cech Szewski (skany #6–#8, #10–#12, #22–#23, #25)</h2>
          <div class="card-content">
            <p>Zeznania świadków w sporze <strong>Stanisława Partyki</strong> z <strong>Wojciechem Nogajem</strong> odsłaniają realia jarmarków w Urzędowie w Poniedziałek Przewodni: wspólne stoiska szewców kraśnickich i opolskich pod ratuszem oraz procedurę oczyszczenia z zarzutu kradzieży wraz z publicznymi przeprosinami przy 6 świadkach w Zarzeczu.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">💍 3. Zastawy Rzemieślnicze i Taksa Srebra Próby 9 (skany #8, #14, #20, #23)</h2>
          <div class="card-content">
            <p>Akta z września–października 1671 r. ukazują funkcjonowanie kredytu zastawnego w Kraśniku: ślusarz <strong>Andrzej Pieniążek</strong> zastawił pierścień i narzędzia u Żyda <strong>Wygdora</strong> na <code>14 złp</code> (<code>#8, #23</code>), a na sesji z 2 X 1671 r. złotnicy i sąd dokonali urzędowej taksy srebra guzikowego próby <code>9</code> (<code>3 łuty po 50 gr</code>) z zastawu <strong>Jana Pieniążka</strong> (<code>#14</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🩹 4. Obdukcje Sądowe i Konflikty Elit Miejskich Jesienią 1671 r. (skany #12, #15–#19)</h2>
          <div class="card-content">
            <p>Aż sześć obdukcji ran w ciągu jednego miesiąca (IX–X 1671 r.) dokumentuje napięcia w mieście: pobicie brzemiennej <strong>Marianny Nawrockiej</strong> przez ławnika <strong>Macieja Bielaszkowica</strong> (<code>#16</code>), napaść na ławnika <strong>Wojciecha Kurewica [?]</strong> i jego furmana (<code>#15</code>), a także udział wójta <strong>Ubalda Janaszkowicza</strong> i burmistrza <strong>Michała Dubielowica</strong> w rozstrzyganiu sporów (<code>#16, #18</code>).</p>
          </div>
        </article>\'\'\'\n'''

src = src[:start_a] + j21_analytics + src[end_a:]

with open("generate_j21_html_part1_authentic.py", "w", encoding="utf-8") as f:
    f.write(src)

print("Zapisano generate_j21_html_part1_authentic.py")
