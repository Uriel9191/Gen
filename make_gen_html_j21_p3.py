# -*- coding: utf-8 -*-
with open("generate_j21_html_part2_authentic.py", "r", encoding="utf-8") as f:
    src = f.read()

src = src.replace("main_data_j21_part2.json", "main_data_j21_part3.json")
src = src.replace("gen_data_j21_part2.json", "gen_data_j21_part3.json")
src = src.replace("Partie 1–2 (skany 1–50 z 606)", "Partie 1–3 (skany 1–75 z 606)")
src = src.replace("Partie 1–2: skany 1–50 z 606 (fol. 1r–23v) • AP Lublin", "Partie 1–3: skany 1–75 z 606 (fol. 1r–36r) • AP Lublin")

new_chapters = """        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IX: Wyrok 100 Grzywien Vadium i Spory Listopadowo-Grudniowe 1671 r. (skany 51–58)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 24r–27v</code> zamykają rok <strong>1671</strong> kilkoma przełomowymi orzeczeniami. W przewlekłym konflikcie między byłym rajcą <strong>Stanisławem Nawrockim</strong> a ławnikiem <strong>Matyjaszem Bielaszkowicem alias Ratusznym</strong> zapadł surowy wyrok skazujący Nawrockiego na <code>30 grzywien</code> (po połowie na kościół parafialny i szpital św. Ducha), 4 tygodnie aresztu domowego oraz założenie bezprecedensowego <em>vadium</em> w wysokości <code>100 grzywien</code> (<code>#53</code>). Z kolei sługa rajcy <strong>Szymona Wiązkowica</strong>, <strong>Stanisław Berecki</strong>, oskarżony przez Nawrockiego o kradzież <code>20 złp</code> i żelaz płużnych w drodze sokalskiej, oczyścił się uroczystą przysięgą przy gospodarzu (<code>#53–#58</code>). Pod datą 14 XII 1671 r. zapisano również nakaz osadzenia w wieży <em>Baba</em> kuśnierza <strong>Tomasza Łążkowica</strong> za dług <code>40 złp</code> wobec Żyda <strong>Andrzeja Ablika</strong> (<code>#56</code>) oraz zeznania starszych zboru kraśnickiego <strong>Kopla</strong> i <strong>Heliasza Korzennika</strong> o zakupie pasa srebrnego dla organisty <strong>Jana Grzebuskiego</strong> (<code>#57</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział X: Otwarcie Roku 1672 — Kontrakt przy ul. Lubelskiej i Pożar u Kuśmierza (skany 59–64)</h2>
          <div class="chapter-content">
            <p>Karta <code>fol. 28r</code> (<code>#59</code>) otwiera nowy rok uroczyście nagłówkiem <em>NOVUS ANNUS Dni 1672</em> oraz kontraktem z 12 I 1672 r., w którym szlachetny <strong>Stanisław Sebastian Skarbek</strong> jako opiekun małoletnich siostrzeńców sprzedał podwojciemu <strong>Wojciechowi Kurewicowi</strong> dom przy ul. Lubelskiej za <code>70 złp</code>. Zima i wiosna 1672 r. przyniosły sprawę o <code>7</code> korali powierzonych w trakcie pożaru (<code>#60</code>), zeznania świadków o pożarze wybuchłym z komina <strong>Bartosza Kuśmierza</strong> (<code>#60</code>), spór młynarza <strong>Wojciecha Łazińskiego</strong> z krawcem <strong>Wawrzyńcem Żydkiem</strong> (<code>#61–#62</code>), a także wyrok o pobicie kuśnierza <strong>Bartłomieja Grudnia</strong> w domu <strong>Baltazara Szafra [Szafrankowica]</strong> (<code>#63–#64</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XI: Proces o Czary Przeciw Balasionie i Egzekucja Długów Rajcy Foxa (skany 65–70, 73)</h2>
          <div class="chapter-content">
            <p>Jednym z najciekawszych wątków obyczajowo-prawnych Partii 3 jest proces wytoczony w lipcu 1672 r. przez przedmieszczanina <strong>Bartosza Kłopota</strong> z żoną przeciw wdowie <strong>Marynie Balasionie [Balaowej]</strong> o publiczne posądzenie żony powoda o czary i odbieranie krowom mleka (<code>#66–#67, #73</code>). Sąd po przesłuchaniu świadków oddalił podejrzenie czarów, dopuścił Kłopotów do przysięgi oczyszczającej, a oszczerczynię skazał na <code>6 niedziel</code> posługi w Szpitalu św. Ducha, <code>4 niedziele</code> w klatce (ostatecznie zamienione na <code>3 dni</code> wieży i <code>2 grzywny</code>) oraz publiczne przeprosiny. W tym samym czasie Bractwo Różańcowe uzyskało dekret intromisji w dobra rajcy <strong>Grzegorza Foxa</strong>, który z zaciągniętego długu wpłacił zaledwie <code>2 złp</code> (<code>#68, #70</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XII: Spory Piwowarskie z Żydem Dawidem Muszą i Rozbój na Poddanych z Krężnicy (skany 71–75)</h2>
          <div class="chapter-content">
            <p>Końcowe karty Partii 3 (<code>fol. 34r–36r</code>) dokumentują wielki spór piwowarski z 5 IX 1672 r. między mieszczaninem <strong>Walentym Sitarskim</strong> a Żydem <strong>Dawidem Muszą</strong> o <code>24</code> beczki piwa po <code>4 złp</code>, w którym zeznawali piwowarzy <strong>Wawrzyniec Zając</strong>, <strong>Jędrzej Piwowar</strong> i <strong>Wojciech Lisowski</strong>, ujawniając produkcję słodu i handel piwem także ze Stróżą (<code>#71–#72</code>). Pod dniem 18 VII 1672 r. (<code>#74</code>) odnotowano brutalny napad sług szlacheckich (od P. <strong>Żabickiego</strong> i <strong>Łojowskiego [?]</strong>) na trzech poddanych ze wsi Krężnica (<strong>Jakuba Kutkę</strong>, <strong>Błażeja Wierzbickiego</strong> i <strong>Stefana Latoszka</strong>), a 29 VII 1672 r. sędzia kraśnicki <strong>Piotr Dzierżek</strong> złożył zaprzysiężone zeznania w sprawach kredytowych Żyda <strong>Mośka</strong> przeciw winiarzowi <strong>Wawrzyńcowi Fajglowi</strong> (<code>80 złp</code>) i <strong>Matyjaszowi Kowalikowi</strong> (<code>60 złp</code> za parę koni, <code>#75</code>).</p>
          </div>
        </article>'''"""

assert "        </article>'''\n\nanalytics_html" in src, "Nie znaleziono kotwicy monografii!"
src = src.replace("        </article>'''\n\nanalytics_html", new_chapters + "\n\nanalytics_html", 1)

new_cards = """        </article>

        <article class="analytic-card">
          <h2 class="card-title">🧙‍♀️ 9. Proces o Czary i Pomówienie o Odbieranie Mleka Krowom (skany #66–#67, #73)</h2>
          <div class="card-content">
            <p>Sprawa <strong>Bartosza Kłopota</strong> przeciw wdowie <strong>Marynie Balasionie [Balaowej]</strong> z 1672 r. ilustruje racjonalne podejście sądu miejskiego do oskarżeń o czary: wobec braku dowodów na czarowanie krów sąd oczyścił pomówioną kobietę przysięgą, a oszczerczynię skazał na posługę w Szpitalu św. Ducha, wieżę i karę pieniężną.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🍺 10. Gospodarka Piwowarska i Słodownie Kraśnickie w 1672 r. (skany #71–#72)</h2>
          <div class="card-content">
            <p>Zeznania w procesie <strong>Walentego Sitarskiego</strong> z Żydem <strong>Dawidem Muszą</strong> o <code>24</code> beczki piwa (po <code>4 złp</code> za beczkę) odsłaniają współpracę chrześcijańskich słodowników i piwowarów (<strong>Wawrzyniec Zając</strong>, <strong>Jędrzej Piwowar</strong>) z kupcami żydowskimi z Kraśnika i ze Stróży (<strong>Izaak</strong>), jak również ówczesne standardy jakości trunku.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 11. Rekordowe Vadium 100 Grzywien i Egzekucja Wobec Rajcy Foxa (skany #53, #68, #70)</h2>
          <div class="card-content">
            <p>Aby powstrzymać eskalację konfliktu między <strong>Stanisławem Nawrockim</strong> a ławnikiem <strong>Matyjaszem Bielaszkowicem alias Ratusznym</strong>, sąd nałożył <code>30 grzywien</code> kary na rzecz kościoła i szpitala oraz niezwykle wysokie <em>vadium</em> <code>100 grzywien</code> (<code>#53</code>). Z kolei długi bractwa różańcowego były egzekwowane bez wyjątku nawet wobec urzędujących rajców — jak w przypadku intromisji w dobra <strong>Grzegorza Foxa</strong> (<code>#68, #70</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚔️ 12. Przemoc na Drogach i Ochrona Poddanych z Krężnicy (skan #74)</h2>
          <div class="card-content">
            <p>Obdukcja z 18 VII 1672 r. dokumentuje rolę sądu miejskiego jako forum rejestracji przestępstw popełnianych na okolicznej ludności wiejskiej: trzej chłopi z Krężnicy (<strong>Jakub Kutka</strong>, <strong>Błażej Wierzbicki</strong>, <strong>Stefan Latoszek</strong>) pobici i obrabowani przez sługi szlacheckie <strong>Żabickiego</strong> i <strong>Łojowskiego [?]</strong> obdukowali rany przed wójtem <strong>Ubaldem Janaszkowicem</strong>.</p>
          </div>
        </article>'''"""

assert "        </article>'''\nmain_data_json" in src, "Nie znaleziono kotwicy kart analitycznych!"
src = src.replace("        </article>'''\nmain_data_json", new_cards + "\nmain_data_json", 1)

with open("generate_j21_html_part3_authentic.py", "w", encoding="utf-8") as f:
    f.write(src)

print("Zapisano generate_j21_html_part3_authentic.py")
