# -*- coding: utf-8 -*-
with open("generate_j20_html_part10_authentic.py", "r", encoding="utf-8") as f:
    src = f.read()

# 1. Podmiana sciezek JSON i komunikatow
src = src.replace("main_data_j20_part10.json", "main_data_j20_part11.json")
src = src.replace("gen_data_j20_part10.json", "gen_data_j20_part11.json")
src = src.replace("Partie 1–10 (skany 1–250 z 283)", "Komplet: skany 1–283 z 283 (100% woluminu)")
src = src.replace("Partie 1–2 (skany 1–50 z 283) • Sygn. 35/40/0/1/20", "Komplet: skany 1–283 z 283 (100% woluminu) • Sygn. 35/40/0/1/20")
src = src.replace("Partie 1–2: skany 1–50 z 283 (fol. 1r–23r) • AP Lublin", "Komplet: 283 / 283 skanów (fol. 1r–140v + metryki) • AP Lublin")

# 2. Dopisanie Rozdzialow XLI–XLIV monografii
new_chapters = """        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XLI: Echa Tumultu Październikowego i Spory Majątkowe Jesieni 1699 r. (skany 251–260)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 125v–130r</code> dokumentują dalszy ciąg dochodzenia po tumulcie na jarmarku św. Franciszka (<code>#251–#253</code>): obdukcje ran <strong>Michała Pawłowskiego</strong>, <strong>Aleksandra Subkowskiego [?]</strong>, <strong>Jana Dumańskiego</strong>, <strong>Jakuba Świątka</strong> oraz poddanego ze Stróży <strong>Stanisława Franikowicza</strong> pobitego przez czeladź Żyda <strong>Borucha</strong> w obecności administratora starostwa <strong>Kazimierza Długopolskiego [?]</strong>. Równolegle w październiku i na początku listopada <strong>1699 r.</strong> toczyły się procesy kucharza konwentu <strong>Jakuba Wojtkowica [?]</strong> przeciw <strong>Matyjaszowi i Tomaszowi Kępom</strong> o szkodę w rzepie i życie (<code>#253–#254</code>), aresztowy spór <strong>Adama Ziętaka [Zietakiego?]</strong> z <strong>Pawłem Nowackim</strong> (<code>#254–#255</code>), wpis starszego synagogi kraśnickiej <strong>Kopla Moszkowica</strong> z synem <strong>Abrahamem</strong> (<code>#256</code>), początek procesu <strong>Stanisława Jesurkiewicza</strong> i <strong>Marianny Komiesanki</strong> przeciw <strong>Józefowi Macalowi</strong> o <code>60 złp</code> (<code>#255, #257–#258</code>) oraz protestacja <strong>Tomasza Celeja</strong> przeciw sprzedaży gruntu po <strong>Szymonie Branku</strong> (<code>#257</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XLII: Proces Braci Wardęgów, Egzekucja u Macalów i Zapisy Budzyńskie (skany 261–271)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 130v–135v</code> z listopada i początku grudnia <strong>1699 r.</strong> rozgrywa się zacięty spór braci <strong>Wojciecha</strong> i <strong>Jakuba Wardęgów</strong> (<code>#260–#262, #265, #267–#268</code>) z udziałem licznych świadków (<strong>Franciszka Sitarskiego</strong>, <strong>Józefa Wilczka</strong>, <strong>Zachariasza Kozaka [?]</strong>, <strong>Anny Skrzybkowej [?]</strong>, <strong>Józefa Madejczyka</strong>) ujawniający oskarżenia o kradzieże i napaść z kosą przez syna Jakuba — <strong>Adama Wardęgę</strong>. W tym samym czasie zapadł wyrok nakazujący intromisję w dobra <strong>Józefa i Anny Macalów</strong> po przysiędze w synagodze i sądzie (<code>#263–#264</code>), rozpatrywano kłótnię sąsiedzką <strong>Pawła Mazurka</strong> z <strong>Matyjaszem i Katarzyną Wolakami</strong> o kurę zakończoną vadium <code>14 grzywien</code> (<code>#264–#267</code>), a także sfinalizowano kwitację <strong>Jana Dumańskiego</strong> i <strong>Agnieszki Soborówny</strong> dla <strong>Tomasza, Szymona i Katarzyny Olchowskich</strong> za rolę <em>Soborowską</em> w Budzyniu za <code>70 złp</code> (<code>#268–#270</code>) oraz własnoręczną zgodę (<em>mpp</em>) plebana <strong>ks. Tomasza Jaszynki</strong> na intromisję Macalów w dobra <em>Butkowskie</em> (<code>#271</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XLIII: Śmierć Zofii Skałczonki i Śledztwo Przeciw Młynarzowi Janowi Lacie (skany 272–280)</h2>
          <div class="chapter-content">
            <p>Najobszerniejszą sprawą kryminalną schyłku <strong>1699 r.</strong> (<code>fol. 136r–140r</code>) jest dochodzenie w sprawie śmiertelnego pobicia <strong>Zofii Skałczonki [Wikówny?]</strong>, siostry przedmieszczanina <strong>Jana/Wojciecha Skałki</strong>. Po urzędowej obdukcji zwłok z 2 XII 1699 r. (<code>#272</code>) i poręczeniu pięciu sąsiadów za niewinność brata (<code>#274–#275</code>), zaprzysiężeni świadkowie — <strong>Marianna Zdebiowa</strong>, <strong>Katarzyna Wolakowa</strong>, <strong>Elżbieta Pacykowa [?]</strong>, <strong>Franciszek Sitarski</strong>, <strong>Szymon Łupas [?]</strong> ze Stróży i <strong>Piotr Cholewiak</strong> (<code>#277–#278, #280</code>) — jednoznacznie wskazali młynarza i gospodarza <strong>Jana Latę [Zającowego]</strong> oraz jego parobka <strong>Grzegorza Błażkowiaka [?]</strong> jako sprawców brutalnego pobicia o kapustę na błoniach, po którym wywieziono umierającą do wsi <strong>Bielany [Bielin?]</strong>. Obok śledztwa zapisano spory czynszowe <strong>Bractwa Różańcowego</strong> z udziałem prokuratora <strong>Adama Karola Mrozowskiego</strong> (<code>#274, #276, #279</code>) oraz proces <strong>Marcina Rymarczyka</strong> z <strong>Wawrzyńcem Kochankiem</strong> (<code>#273, #275, #279–#280</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XLIV: Sesja ze Stycznia 1700 r. i Zamknięcie Woluminu (skany 281–283)</h2>
          <div class="chapter-content">
            <p>Ostatnia zapisana karta rękopisu (<code>fol. 140v</code>, <code>#281</code> oraz jej dublet mikrofilmowy <code>#282</code>) przenosi akta na próg nowego stulecia — sesję z poniedziałku po Święcie Trzech Króli <strong>11 stycznia 1700 r.</strong> (<em>Feria Secunda post Festum Trium Regum Anno Domini 1700</em>). Rozstrzygnięto wówczas spór <strong>Marcina Rymarczyka</strong> z <strong>Wawrzyńcem Kochankiem</strong>, odroczono sprawę braci <strong>Wojciecha i Jakuba Wardęgów</strong>, rozpatrzono dług <strong>Wojciecha Szymonka</strong> przeciw <strong>Kazimierzowi Stasiakowi</strong> o <code>2 złp</code> na chleb oraz wpisano kontumacje <strong>Stanisława Szafranka</strong> i wdowy <strong>Zofii Wolakowej</strong> przeciw <strong>Janowi Trawińskiemu</strong> o <code>15 złp</code> za sól. Całość tomu zamyka metryczka końcowa mikrofilmu nr <code>110399</code> z <strong>30 października 1959 r.</strong> (<code>#283</code>).</p>
          </div>
        </article>'''"""

assert "        </article>'''\n\nanalytics_html" in src, "Nie znaleziono kotwicy monografii!"
src = src.replace("        </article>'''\n\nanalytics_html", new_chapters + "\n\nanalytics_html", 1)

# 3. Dopisanie Kart Analitycznych 41–44
new_cards = """        </article>

        <article class="analytic-card">
          <h2 class="card-title">✒️ 41. Autograf Plebana ks. Tomasza Jaszynki i Funkcja Tutor Naturalis (skan #271)</h2>
          <div class="card-content">
            <p>Na karcie <code>fol. 135v</code> z 2 XII 1699 r. zachował się rzadki własnoręczny podpis (<em>manu propria</em>) duchownego — <strong>ks. Tomasza Jaszynki</strong>, plebana dzierzkowskiego (<em>Pleban Dziekhowski [?]</em>), występującego w charakterze naturalnego opiekuna (<em>Tutor Naturalis</em>) przy zapisie i intromisji rzeźnika <strong>Józefa Macala</strong> oraz <strong>Anny z Wierzbickich</strong> w dobra <em>Butkowskie</em>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🕯️ 42. Śledztwo w Sprawie Śmierci Zofii Skałczonki i Ekspurgacja Brata (skany #272, #274, #277–#278, #280)</h2>
          <div class="card-content">
            <p>Akta z grudnia 1699 r. prezentują pełną procedurę kryminalną sądu miejskiego w sprawie zabójstwa: od komisyjnej obdukcji zwłok przy wójcie i 9 mieszczanach (<code>#272</code>), przez poręczenie majątkowe 5 sąsiadów za podejrzanego brata (<code>#274</code>), po przesłuchanie 6 zaprzysiężonych świadków z Kraśnika i Stróży (<code>#277–#278, #280</code>), którzy zrekonstruowali pobicie przez młynarza <strong>Jana Latę [Zającowego]</strong> i wywiezienie ofiary do wsi <strong>Bielany</strong>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 43. Mikrohistoria Konfliktów Rodzinnych i Sąsiedzkich: Wardęgowie i Wolakowie (skany #260–#268)</h2>
          <div class="card-content">
            <p>Zeznania w sprawach <strong>Wojciecha i Jakuba Wardęgów</strong> oraz <strong>Pawła Mazurka</strong> z <strong>Matyjaszem i Katarzyną Wolakami</strong> ukazują realia dnia codziennego przedmieść Kraśnika w 1699 r.: spory o szkodę w ogrodzie przez świnię i wygnanie ze stodoły o kurę, oskarżenia o kradzież wołów i gryki w Lublinie oraz Sandomierzu, a także stosowanie sądowego zakładu (<em>vadium</em> <code>14 grzywien</code>) dla powstrzymania przemocy sąsiedzkiej.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 44. Chronologia Graniczna Woluminu (1656–1700) i Metryczka Mikrofilmu (skany #281–#283)</h2>
          <div class="card-content">
            <p>Ukończenie 100% woluminu (283/283 skanów) potwierdza, że mimo tytułowego szyldu „1657–1699” (<code>#4</code>), księga obejmuje okres od <strong>9 XII 1656 r.</strong> (<code>#16</code>) aż po <strong>11 I 1700 r.</strong> (<code>#281</code>). W warstwie technicznej mikrofilmu nr <code>110399</code> z 30 X 1959 r. (<code>#283</code>) zidentyfikowano końcowy dublet fotograficzny karty <code>fol. 140v</code> (<code>#282 = #281</code>).</p>
          </div>
        </article>'''"""

assert "        </article>'''\nmain_data_json" in src, "Nie znaleziono kotwicy kart analitycznych!"
src = src.replace("        </article>'''\nmain_data_json", new_cards + "\nmain_data_json", 1)

with open("generate_j20_html_part11_authentic.py", "w", encoding="utf-8") as f:
    f.write(src)

print("Zapisano generate_j20_html_part11_authentic.py")
