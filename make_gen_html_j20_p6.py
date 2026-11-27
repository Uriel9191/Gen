# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j20_html_part5_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

src = src.replace("main_data_j20_part5.json", "main_data_j20_part6.json")
src = src.replace("gen_data_j20_part5.json", "gen_data_j20_part6.json")

new_monograph_chapters = """
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXI: Kontynuacja Spraw z Jesieni 1684 r. — Obdukcja Sługi Miejskiego i Finał Procesu o Czary (skany 126–135)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 62r–66v</code> zamykają rok <strong>1684</strong> bogatą serią dekretów: wyrokiem zaocznym w sprawie <strong>Stanisława Nawrockiego</strong> przeciw <strong>Wojciechowi Dziwanowskiemu [Dzierżanowskiemu]</strong> (<code>#126</code>, <code>#130</code>), sprawą kupca <strong>Aleksandra Mantemberka</strong> przeciw <strong>Wojciechowi Jurdzikowi</strong> (<code>#127</code>), obdukcją krwawej rany głowy sługi miejskiego <strong>Marcina Pietruszczaka</strong> (<code>#129</code>) oraz obdukcją ciężkich ran młodzieńca <strong>Jakuba Chruścika [?]</strong> z 28 X 1684 r. (<code>#135</code>). Dnia 27 X 1684 r. kontynuowano głośny spór o oszczerstwo o czary i spalenie młyna (<strong>Wojciech Bartoszek</strong>, <strong>Stanisław Babarczyk</strong> i <strong>Wojciech Zychko</strong> vs młynarz <strong>Bartłomiej Wilk</strong>, <code>#128</code>, <code>#132</code>), a <strong>Bartłomiej Rodzonek</strong> oczyścił się przysięgą z zarzutu kradzieży wieprzka (<code>#134</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXII: Elekcja Magistratu Miejskiego i Cechmistrzów z 12 Stycznia 1686 r. (skany 136–138)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 67r–68r</code> zachował się pełny protokół uroczystej elekcji władz miejskich z <strong>12 stycznia 1686 r.</strong> w domu rajcy <strong>Macieja Bielaszkowica</strong> z udziałem komisarzy pani dożywotniej <strong>Doroty Zamoyskiej</strong> (szl. <strong>Jakub Łębowski [?]</strong> i <strong>Kazimierz Toruński [?]</strong>). Wybrano wówczas czterech rajców rezydujących (<strong>Paweł Stankowski</strong>, <strong>Stanisław Grymuza [Gomuza]</strong>, starszy cechów <strong>Jerzy Gucki</strong> oraz z wyboru pospólstwa <strong>Sebastian Batusiowic [Banaszowicz]</strong>), siedmiu ławników (w tym <strong>Szymon Kościński</strong> jako asesor do Trybunału Zamojskiego), trzech egzaktorów oraz cechmistrzów szewców, kuśnierzy i kowali (<code>#136–#137</code>). W lutym 1686 r. odnotowano poręczenie <strong>Wojciecha Butki</strong>, wdowy <strong>Jadwigi Więckowej [?]</strong> i <strong>Stefana Nagórnego</strong> za <strong>Katarzynę Chmielównę</strong> więzioną w sprawie syna Żyda <strong>Moszka Berela</strong> (<code>#138</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXIII: Warstwa z 1694–1695 r. — Burmistrzowie Solecki i Potokowicz, Ugoda Piaseckich i Procesy Żydowskie (skany 139–146)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 69r–72v</code> dokumentują sądownictwo z lat <strong>1694–1695</strong>. Obok spraw majątkowych i rozliczeń finansowych burmistrzów <strong>Stanisława Soleckiego</strong> i <strong>Stanisława Szymkiewicza [?]</strong> (12 V 1694, <code>#141</code>) oraz manifestacji burmistrza <strong>Adama Potokowicza [Potockiego]</strong> (29 IV 1695, <code>#145</code>), zachowała się ugoda spadkowa sierot po <strong>Janie Piaseckim</strong> (25 II 1695, <code>#143</code>), poręczenie <strong>Józefa Madeja</strong>, <strong>Szymona Kuśmierza</strong> i <strong>Doroty Tutkowej</strong> za <strong>Józefa Wilczka</strong> (22 III 1695, <code>#144</code>) oraz liczne sprawy kredytowe z udziałem Żydów kraśnickich: <strong>Herszka</strong>, <strong>Moszkowica</strong>, <strong>Abla Anzela</strong>, <strong>Abusa [?]</strong>, <strong>Itralowej [?]</strong> i <strong>Abusiowej</strong> (<code>#139–#141</code>, <code>#146</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXIV: Wpisy z 1697 r. i Rejestracja Kontumacji z 1694 r. (skany 147–150)</h2>
          <div class="chapter-content">
            <p>Końcowe karty Partii 6 (<code>fol. 73r–74v</code>) zawierają protokoły z roku <strong>1697</strong> (protestacja <strong>Wawrzyńca Kąkoły [?]</strong> ze wsi <strong>Sulów</strong> o pobicie na drodze przez <strong>Stanisława Kowala [?]</strong>, skarga <strong>Tomasza Nowaka</strong> na szwagra <strong>Franciszka Grątka [?]</strong> o groźby podpalenia i obcięcia rąk, oraz skarga <strong>Macieja Rzepki [?]</strong> przeciw zięciowi <strong>Maciejowi Śliwińskiemu [?]</strong> z 18 XII 1697 r., <code>#147–#148</code>), a także wplecione karty z lutego <strong>1694 r.</strong> z rozliczeniem pogrzebowym <strong>Macieja Piotrowczyka</strong> i serią kontumacji żydowskich i mieszczańskich (<code>#149–#150</code>).</p>
          </div>
        </article>'''"""

assert "        </article>'''" in src, "Brak kotwicy monograph_html"
src = src.replace("        </article>'''", "        </article>" + new_monograph_chapters, 1)

new_analytics_cards = """
        <article class="analytic-card">
          <h2 class="card-title">🏛️ 21. Pełna Elekcja Władz Miejskich i Starszych Cechów z 12 Stycznia 1686 r. (skany #136–#137)</h2>
          <div class="card-content">
            <p>Protokół elekcji z 1686 r. przedstawia trójczłonową strukturę władzy Kraśnika: komisarze pani dożywotniej <strong>Doroty Zamoyskiej</strong> powołali dwóch rajców (<strong>Paweł Stankowski</strong>, <strong>Stanisław Grymuza</strong>), wójt z ławą wybrali starszego cechów <strong>Jerzego Guckiego</strong>, a pospólstwo wskazało <strong>Sebastiana Batusiowica [Banaszowica]</strong>. Zaprzysiężono też asesora do Trybunału Zamojskiego (<strong>Szymon Kościński</strong>) i cechmistrzów.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🔗 22. Poręczenia Sądowe (Fideiussiones) jako Mechanizm Zwolnień z Więzienia (skany #138, #144)</h2>
          <div class="card-content">
            <p>Księga z lat 1686 i 1695 pokazuje praktykę zwolnień z aresztu za poręczeniem solidarnym sąsiadów i rodziny: 11 II 1686 r. <strong>Wojciech Butka</strong>, <strong>Jadwiga Więckowa [?]</strong> i <strong>Stefan Nagórny</strong> poręczyli za <strong>Katarzynę Chmielównę</strong> (<code>#138</code>), a 22 III 1695 r. <strong>Józef Madej</strong>, <strong>Szymon Kuśmierz</strong>, <strong>Adam Wilczek</strong> i matka <strong>Dorota Tutkowa</strong> ręczyli za <strong>Józefa Wilczka</strong> (<code>#144</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🌾 23. Kontakty ze Wsią Sulów i Sądownictwo Łączone z 1695–1697 r. (skany #141, #143, #147–#148)</h2>
          <div class="card-content">
            <p>Przed sądem kraśnickim regularnie stawali także poddani ze wsi <strong>Sulów</strong>: <strong>Jakub Janczarek [?]</strong> w 1695 r. (<code>#141</code>) oraz <strong>Wawrzyniec Kąkoła [?]</strong> pobity na drodze przez <strong>Stanisława Kowala [?]</strong> w 1697 r. (<code>#147</code>). Ważnym aktem rodzinnym jest ugoda sierot po <strong>Janie Piaseckim</strong> przed Sądem Łączonym z 25 II 1695 r. (<code>#143</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🩺 24. Obdukcje Sługi Miejskiego Pietruszczaka i Młodzieńca Chruścika (skany #129, #135)</h2>
          <div class="card-content">
            <p>Październik 1684 r. przyniósł dwie drastyczne obdukcje ran w księdze wójtowskiej: sługi miejskiego <strong>Marcina Pietruszczaka</strong> uderzonego aż do kości nad lewym okiem przez <strong>Marcina Kurca [?]</strong> (<code>#129</code>) oraz młodzieńca <strong>Jakuba Chruścika [?]</strong> zranionego na głowie aż do błony mózgowej przez <strong>Jakuba Żytę [?]</strong> (<code>#135</code>).</p>
          </div>
        </article>'''"""

idx = src.rfind("        </article>'''")
assert idx != -1
src = src[:idx] + "        </article>" + new_analytics_cards + src[idx + len("        </article>'''"):]

with open('/home/ubuntu/workspace/Gen/generate_j20_html_part6_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Utworzono generate_j20_html_part6_authentic.py")
