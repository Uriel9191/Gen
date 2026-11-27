# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j20_html_part3_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

src = src.replace("main_data_j20_part3.json", "main_data_j20_part4.json")
src = src.replace("gen_data_j20_part3.json", "gen_data_j20_part4.json")

new_monograph_chapters = """
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XIII: Finał Procesu Spadkowego Wsi Blinów (skany 76–81)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 36r–38v</code> zamykają wielki proces spadkowy poddanych ze wsi <strong>Blinów</strong> po zmarłym <strong>Tomaszu Rzepce</strong> i jego pierwszej żonie <strong>Agnieszce</strong> (<code>48</code> lat wspólnego pożycia, <code>#79</code>). Po powołaniu wcześniejszego dekretu przed J.P. <strong>Janem Świderskim</strong> z 8 III 1658 r. (z własnoręcznym podpisem i udziałem wójta blinowskiego <strong>Jana Rzepki</strong>, <strong>Łukasza</strong> i <strong>Stanisława Reszków</strong>, <strong>Pawła Brożka</strong> oraz <strong>Mateusza Kłosa</strong>, <code>#77</code>) oraz repliki z 14 X 1658 r. przed dzierżawcą <strong>Bartłomiejem Janorowskim</strong> (<code>#78</code>), Sąd Wójtowski wydał ostateczny dekret działowy (<code>#79–#81</code>), przyznając córkom <strong>Jadwidze</strong> i <strong>Katarzynie</strong> po <code>17 złp</code> za sprzęty i połowę z <code>130 złp</code> długów, a wdowie <strong>Katarzynie Rzepkowej</strong> trzecią część nowego dorobku.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XIV: Lata 1666–1668 i 1681 — Kanonicy Regularni, Spory Jarmarczne i Przyjęcia Prawa Miejskiego (skany 82–89)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 39r–42v</code> księga przechodzi przez trzy wyraźne warstwy chronologiczne: <strong>1666</strong>, <strong>1668</strong> i <strong>1681</strong>. Z 20 XII 1666 r. pochodzi uroczysta kwitacja sumy <code>100 złp</code> wypłaconej przez prepozyta kraśnickiego ks. <strong>Ludwika Jastrzębskiego [?]</strong> i konwent Kanoników Regularnych dla <strong>Anny Dubitowej</strong> i jej syna <strong>Wojciecha Tuszyńskiego</strong>, uwalniająca dom ławnika <strong>Macieja Konięgi</strong> (<code>#84–#85</code>). W roku <strong>1668</strong> odnotowano głośną awanturę jarmarczną o czerwony rękawik turecki między Żydem <strong>Mamelem</strong> a <strong>Kłopotem</strong> (<code>#82–#83</code>), proces szewca <strong>Kanaszka</strong> z <strong>Jakubem Krasnodębskim</strong> z Urzędowa o kontusz z Turobina (<code>#82–#83</code>), testament szpitalny <strong>Andrzeja Węgorzowica</strong> (<code>#86</code>) oraz kontumację rajcy <strong>Marcina Sitarskiego</strong> z pozwu Żyda <strong>Andzela</strong> (<code>#87</code>). Warstwa z <strong>1681 r.</strong> (<code>#88–#89</code>) rejestruje przyjęcia prawa miejskiego (m.in. <strong>Paweł</strong> i <strong>Jan Kłopotkowie</strong>, <strong>Michał Piotrowski</strong>, <strong>Andrzej Kantorek</strong>, <strong>Mikołaj Zbrończyk</strong>) oraz areszt Żydówki <strong>Moszkowej</strong>.</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XV: Nowa Księga z 1683 r. i Elekcja Pisarza Miejskiego Jana Rogalowskiego (skany 90–93)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 43r–45v</code> otwierają nową część księgi z roku <strong>1683</strong> pod auspicjami ordynata <strong>Marcina Zamoyskiego</strong> i jego żony <strong>Doroty z Leszczkowa Zamoyskiej</strong> (<code>#90–#91</code>). Dnia <strong>23 kwietnia 1683 r.</strong> w domu wójta <strong>Ubalda Floriana Janaszkowicza</strong> w obecności administratora <strong>Jakuba Skrzeszowskiego</strong>, burmistrza <strong>Stanisława Gomuzy</strong>, rajców, ławników (wicewójt <strong>Paweł Stankowski</strong>) oraz delegacji kahału żydowskiego (starsi <strong>Dawid Mucda</strong>, <strong>Lejzor Achiaszowicz</strong> i szkolnik <strong>Mojżesz Majer Jozwowicz</strong>) wybrano jednogłośnie patrycjusza <strong>Jana Rogalowskiego</strong> na pisarza miejskiego (<code>#92–#93</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XVI: Wielka Skarga Byłego Burmistrza Stanisława Nawrockiego i Proces Szpitala Św. Ducha (skany 93–100)</h2>
          <div class="chapter-content">
            <p>Dnia <strong>28 kwietnia 1683 r.</strong> stary rajca i były burmistrz <strong>Stanisław Nawrocki</strong> wniósł obszerną skargę (<code>#93–#99</code>) przeciwko poddanemu <strong>Jakubowi Wardędze</strong> (zbiegłemu przed kontrybucjami do Dzierzkowic i na Budzyń pod protekcję podstarościego <strong>Pana Młodowskiego</strong>), odsłaniając kulisy ciężkich rekwizycji wojennych z czasów ordynata <strong>Jana Zamoyskiego</strong>, poboru fantów przez egzaktorów oraz nadużyć podstarościego. Tego samego dnia prowizorowie <strong>Szpitala Świętego Ducha</strong> (w tym podwójci <strong>Paweł Stankowski</strong>) pozwali sukcesorów zmarłego przedmieszczanina <strong>Stanisława Turka</strong> (<strong>Tomasza</strong> i <strong>Marcina Turków</strong>) o zaległy czynsz wyderkafowy <code>5 złp</code> rocznie od <code>100 złp</code> na półłanku <em>Popielczanka [?]</em> (<code>#99–#100</code>).</p>
          </div>
        </article>'''"""

assert "        </article>'''" in src, "Brak kotwicy monograph_html"
src = src.replace("        </article>'''", "        </article>" + new_monograph_chapters, 1)

new_analytics_cards = """
        <article class="analytic-card">
          <h2 class="card-title">🕊️ 13. Fundacja Szpitalna i Konwent Kanoników Regularnych (skany #84–#86, #99–#100)</h2>
          <div class="card-content">
            <p>Księga dokumentuje gospodarkę instytucji kościelnych i charytatywnych Kraśnika: w 1666 r. prepozyt ks. <strong>Ludwik Jastrzębski [?]</strong> wypłacił <code>100 złp</code> w imieniu Konwentu Kanoników Regularnych (<code>#84–#85</code>), w 1668 r. mieszczanin <strong>Andrzej Węgorzowic</strong> przebywający w szpitalu św. Ducha zapisał mu <code>50 złp</code> (<code>#86</code>), a w 1683 r. prowizorowie szpitala dochodzili czynszu wyderkafowego od sukcesorów <strong>Stanisława Turka</strong> (<code>#99–#100</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏛️ 14. Wspólna Elekcja Pisarza Miejskiego z Udziałem Kahału Żydowskiego w 1683 r. (skan #92)</h2>
          <div class="card-content">
            <p>Unikatowym świadectwem ustrojowym jest protokół elekcji pisarza <strong>Jana Rogalowskiego</strong> z 23 IV 1683 r., w której obok administratora dóbr, wójta, burmistrza, rady i ławy miejskiej pełnoprawnie uczestniczyli reprezentanci gminy żydowskiej: starsi <strong>Dawid Mucda</strong> i <strong>Lejzor Achiaszowicz</strong> oraz syndyk/szkolnik <strong>Mojżesz Majer Jozwowicz</strong>.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚔️ 15. Kontrybucje Wojenne i Nadużycia Podstarościego Młodowskiego (skany #93–#98)</h2>
          <div class="card-content">
            <p>Skarga byłego burmistrza <strong>Stanisława Nawrockiego</strong> przeciw <strong>Jakubowi Wardędze</strong> stanowi barwną kronikę obciążeń wojennych miasta (cotygodniowe składki na żołnierzy, rekwizycje wołów, krów, kożuchów i koni w drodze do Lublina) oraz konfliktu kompetencyjnego między samorządem miejskim a podstarościm <strong>Panem Młodowskim</strong>, który bez sądu miejskiego wymusił od rajcy zapłatę za świnie i groził mu gąsiorem.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🧥 16. Awantura Jarmarczna o Czerwony Rękawik i Sprawa o Kontusz z Turobina (skany #82–#83)</h2>
          <div class="card-content">
            <p>Zapisy ze stycznia 1668 r. ukazują codzienność jarmarków kraśnickich: bójkę na rynku wywołaną znalezieniem czerwonego rękawika tureckiego przez <strong>Andrzeja [Kłopota]</strong> i oskarżeniem Żyda <strong>Mamela</strong> o pobicie sprzedawczyni białego chleba, a także proces szewców <strong>Kanaszków</strong> z <strong>Jakubem Krasnodębskim</strong> z Urzędowa o sukno i kontusz szyty w Turobinie.</p>
          </div>
        </article>'''"""

idx = src.rfind("        </article>'''")
assert idx != -1
src = src[:idx] + "        </article>" + new_analytics_cards + src[idx + len("        </article>'''"):]

with open('/home/ubuntu/workspace/Gen/generate_j20_html_part4_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Utworzono generate_j20_html_part4_authentic.py")
