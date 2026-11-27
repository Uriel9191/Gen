# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j20_html_part2_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

src = src.replace("main_data_j20_part2.json", "main_data_j20_part3.json")
src = src.replace("gen_data_j20_part2.json", "gen_data_j20_part3.json")

new_monograph_chapters = """
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IX: Inkwizycje Sądowe, Suplika Wawrzyńca Prokopka i Spory o Spadek po Wojciechu Maruszkowicu (skany 51–56)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 23v–26r</code> dokumentują sesje Sądu Wójtowskiego i Ławniczego z listopada 1658 r. (m.in. <code>feria 4ta</code> i <code>feria 6ta post festum S. Martini Episcopi 1658</code>). Obok spraw o pobicia (<strong>Stanisław Poszłygarczyk</strong> vs <strong>Wojciech Oleszek</strong>, <code>#51</code>) i relacji woźnego <strong>Jana Kłębskiego [?]</strong>, na plan pierwszy wysuwa się spór wierzycieli o majątek po zmarłym <strong>Wojciechu Maruszkowicu</strong>. Przesłuchano 8 zaprzysiężonych mężów (w tym <strong>Stefana Dębskiego [?]</strong>, <strong>Macieja Kozaka [?]</strong>, <strong>Szymona Kuśmierza [?]</strong>, <strong>Daniela Łysika [?]</strong>, <code>#52</code>) w sprawie długów na <code>200 złp</code> i <code>30 złp</code> ławnika <strong>Grzegorza Foxa</strong>, a do księgi wszyto oryginalną, własnoręcznie podpisaną suplikę <strong>Wawrzyńca Prokopka</strong> (<code>#54–#55</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział X: Sprawy Szlacheckie, Wyderkafy, Handel Jabłkami z Lublinem i Kredyt Żydowski (skany 57–65)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 26v–30v</code> ukazują szeroki przekrój kontaktów gospodarczych i procesowych miasta w listopadzie 1658 r. Szlachta okoliczna (<strong>Piotr Słodzarski [Zadzarski?]</strong>, <strong>Wojciech Zarzycki [?]</strong>, <strong>Szymon Szarek</strong>) stawała przed sądem miejskim w sporach o konie, szkody na <code>200 złp</code> oraz wykup ogrodów (<code>#58</code>, <code>#60</code>, <code>#64–#65</code>). Odnotowano także handel jabłkami wiezionymi do Lublina (<strong>Walenty Słodki [?]</strong> vs <strong>Grzegorz Orlak [?]</strong>, <code>#63</code>), wyderkafy <strong>Macieja Konięgi</strong> i <strong>Ewy z Łopacina [?]</strong> na <code>50 złp</code> (<code>#61–#62</code>, <code>#64</code>) oraz wierzytelności Żydów kraśnickich: <strong>Izaaka [?]</strong> (<code>#57–#58</code>), <strong>Iczka Łobody [Łabędzia?]</strong> (<code>#59</code>) i <strong>Icka</strong> (<code>#65</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XI: Oryginalna Plenipotencja Ewy Koźmianowej do Trybunału Zamojskiego i Obdukcja Wawrzyńca Żydkowica (skany 66–69)</h2>
          <div class="chapter-content">
            <p>Na karcie <code>fol. 31r</code> (<code>#66</code>) zachowała się wklejona oryginalna plenipotencja podpisana własnoręcznie przez <strong>Ewę Koźmianową</strong> (datowana 9 XI 1657 r.), ustanawiająca sławetnego <strong>Macieja Saraczkowica [?]</strong> jej pełnomocnikiem przed Trybunałem Zamojskim w sporze z <strong>Grzegorzem Foxem</strong> o dobra po zmarłej <strong>Zofii Kowalowej</strong>. Kolejne karty przynoszą obdukcję ran <strong>Wawrzyńca Żydkowica [Sydkowica]</strong> pobitego przez <strong>Baltazara Żydkowica</strong> i <strong>Macieja Konięgę</strong> (28 XI 1658 r., <code>#68</code>) oraz zeznania Żyda <strong>Dawida Łazarza [?]</strong> i <strong>Jana Kurzy [?]</strong> o handlu skórami i końmi (<code>#69</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XII: Wielki Proces Spadkowy Poddanych ze Wsi Blinów i Inwentarz Tomasza Rzepki (skany 70–75)</h2>
          <div class="chapter-content">
            <p>Ostatnia część Partii 3 (<code>fol. 33r–35v</code>) stanowi bezpośrednią kontynuację i rozstrzygnięcie procesu ze wsi <strong>Blinów</strong> (w Partii 2 odczytanej wariantowo jako <em>Ślinów [Słodków?]</em>) za zezwoleniem dzierżawcy <strong>Bartłomieja Janorowskiego</strong> (własnoręczny podpis na <code>#73</code>). Córki zmarłego <strong>Tomasza Rzepki</strong> i <strong>Agnieszki</strong> — <strong>Jadwiga</strong> (żona <strong>Wojciecha Staroszka</strong>) i <strong>Katarzyna</strong> (żona <strong>Macieja Łysaka</strong>) — dochodziły działu spadkowego przeciw wdowie <strong>Katarzynie Rzepkowej</strong>. Księga zachowała unikatowy podwójny inwentarz zasiewów i dobytku z 1658 r. (<code>#71</code>: m.in. 14 sztuk bydła, 8 koni, 36 owiec, długi <code>200 złp</code> i <code>130 złp</code>) oraz zaprzysiężone zeznania poddanych z Blinowa: <strong>Jana Skórki [?]</strong>, <strong>Pawła Rzepki</strong>, <strong>Jana Rzepki</strong>, <strong>Andrzeja Grątki [?]</strong>, <strong>Stanisława Rzepki</strong>, <strong>Jana Karpińskiego</strong> i <strong>Stefana Kondli</strong> (<code>#72</code>, <code>#74–#75</code>).</p>
          </div>
        </article>'''"""

assert "        </article>'''" in src, "Brak kotwicy monograph_html"
src = src.replace("        </article>'''", "        </article>" + new_monograph_chapters, 1)

new_analytics_cards = """
        <article class="analytic-card">
          <h2 class="card-title">📜 9. Oryginalne Wklejki Kancelaryjne: Suplika Prokopka i Plenipotencja Koźmianowej (skany #54–#55, #66–#67)</h2>
          <div class="card-content">
            <p>Księga wójtowska zachowała wszyte oryginalne dokumenty prywatne z własnoręcznymi podpisami mieszczan: suplikę <strong>Wawrzyńca Prokopka</strong> przeciwko ławnikowi <strong>Grzegorzowi Foxowi</strong> o majątek po <strong>Wojciechu Maruszkowicu</strong> (<code>#54</code>) oraz pełnomocnictwo <strong>Ewy Koźmianowej</strong> z 9 XI 1657 r. dla <strong>Macieja Saraczkowica [?]</strong> do reprezentowania jej przed Trybunałem Zamojskim (<code>#66</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🌾 10. Identyfikacja Wsi Blinów i Pełny Inwentarz Gospodarstwa Chłopskiego z 1658 r. (skany #70–#75)</h2>
          <div class="card-content">
            <p>Kontynuacja procesu spadkowego po <strong>Tomaszu Rzepce</strong> pozwala jednoznacznie zidentyfikować wieś jako <strong>Blinów</strong> (dzierżawca <strong>Bartłomiej Janorowski</strong>, <code>#70</code>, <code>#73</code>) oraz nazwisko rodu jako <strong>Rzepka</strong> i <strong>Kondla</strong>. Inwentarz na <code>#71</code> szczegółowo wylicza zasiewy (15 korcy żyta, 30 kop jęczmienia, 17 kop owsa, 10 kop pszenicy) oraz stado (14 sztuk bydła, 8 koni, 36 owiec).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 11. Spory Szlachty Okolicznej i Handel Jabłkami z Lublinem (skany #58, #60, #63–#65)</h2>
          <div class="card-content">
            <p>Przed Sądem Wójtowskim w Kraśniku stawała w 1658 r. także okoliczna szlachta (<strong>Piotr Słodzarski</strong> w sporze o konia i <code>200 złp</code> szkód, <strong>Wojciech Zarzycki</strong>, <strong>Szymon Szarek</strong>), a w sprawach handlowych odnotowano transport jabłek z Kraśnika do Lublina w sporze <strong>Walentego Słodkiego [?]</strong> z <strong>Grzegorzem Orlakiem [?]</strong> (<code>#63</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🩹 12. Obdukcja Ran Wawrzyńca Żydkowica i Świadkowie Żydowscy w Sądzie Miejskim (skany #68–#69)</h2>
          <div class="card-content">
            <p>Dnia 28 XI 1658 r. urząd dokonał szczegółowej obdukcji ran <strong>Wawrzyńca Żydkowica [Sydkowica]</strong> zadanym mu przez <strong>Baltazara Żydkowica</strong> i ławnika <strong>Macieja Konięgę</strong> (<code>#68</code>), a w kolejnym dniu zaprzysiężony świadek Żyd <strong>Dawid Łazarz [?]</strong> zeznawał w sprawie <strong>Macieja Zielińskiego</strong> o handel skórami (<code>#69</code>).</p>
          </div>
        </article>'''"""

assert "\n        </article>'''\n" in src or "        </article>'''" in src, "Brak kotwicy analytics_html"
# Zastępujemy drugie wystąpienie "        </article>'''" (czyli koniec analytics_html)
idx = src.rfind("        </article>'''")
assert idx != -1
src = src[:idx] + "        </article>" + new_analytics_cards + src[idx + len("        </article>'''"):]

with open('/home/ubuntu/workspace/Gen/generate_j20_html_part3_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Utworzono generate_j20_html_part3_authentic.py")
