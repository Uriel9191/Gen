# -*- coding: utf-8 -*-

with open('/home/ubuntu/workspace/Gen/generate_j19_html_part2_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

replacements = [
    ('main_data_j19_part2.json', 'main_data_j19_part3.json'),
    ('gen_data_j19_part2.json', 'gen_data_j19_part3.json'),
    ('Partie 1–2 (skany 1–50 z 120)', 'Partie 1–3 (skany 1–75 z 120)'),
    ('Partie 1–2: skany 1–50 z 120 (fol. 1r–23v)', 'Partie 1–3: skany 1–75 z 120 (fol. 1r–36r)'),
    ('Rozdziały I–VIII', 'Rozdziały I–XII'),
    ('Karty 1–8', 'Karty 1–12'),
    ('8 kart analitycznych • 8 rozdziałów syntezy', '12 kart analitycznych • 12 rozdziałów syntezy'),
]

for old, new in replacements:
    assert old in src, f"Missing replacement target: {old}"
    src = src.replace(old, new)

new_chapters = '''
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział IX: Rok 1659 — Spory o Spadki, Nieruchomości i Protestacje Obyczajowe (skany 51–57)</h2>
          <p>Po dubletowym ujęciu elekcji 1659 r. (skan <code>#51</code> = <code>#50</code>) księga rejestruje obsadzenie urzędów egzaktorskich (<strong>Jan Skarzyk [Skarzyński?]</strong> i <strong>Maciej Jarzębek [?]</strong>, <code>#52</code>) oraz długotrwałe rozliczenia spadkowe rodziny <strong>Pezików</strong> (<strong>Sebastian</strong>, <strong>Wawrzyniec</strong>, <strong>Zofia Kowalikowa</strong>, <strong>Anna</strong>, <strong>Maryna</strong>, <strong>Katarzyna</strong>) z <strong>Janem Batusikiem [Batusiem]</strong> (<code>#52–#54</code>). Na wiosnę 1659 r. odnotowano kupno placu przy ul. Lubelskiej przez Żyda <strong>Mosia Srulowicza [?]</strong> od <strong>Wojciecha i Agnieszki Batusików</strong> (<code>#55–#56</code>) oraz domu na Przedmieściu przez <strong>Wawrzyńca Chudzika</strong> i <strong>Katarzynę Kępiance</strong> od <strong>Bartłomieja Świderka</strong> (<code>#56–#57</code>).</p>
          <p>Niezwykle barwnym dokumentem życia codziennego magistratu jest protestacja burmistrza <strong>Macieja Tharasy</strong> przeciw koledze rajcy <strong>Marcinowi Sitarskiemu</strong> o najście domu burmistrza i stłuczenie palca ożogiem (<em>sine krwawią raną</em>, poświadczone przez ławników <strong>Jana Kłodnickiego [Kłodczyńskiego?]</strong> i <strong>Macieja Kozicę</strong>, <code>#57</code>).</p>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział X: Jesień i Koniec Roku 1659 — Spór Cichonia z Olkowskim i Atestacja z Borowa (skany 58–63)</h2>
          <p>W drugiej połowie 1659 r. pisarz aktowy <strong>Jan Cichoń</strong> wniósł obszerną polską protestację przeciw <strong>Marcinowi Kotlarzykowi alias Olkowskiemu</strong>, ukazującą kulisy korespondencji i rozliczeń między Kraśnikiem, Urzędowem, Lwowem i Krakowem (<code>#58–#59</code>). Dawny wójt <strong>Wojciech Szafraniec [Szafrankowic]</strong> prowadził liczne egzekucje długów przeciw przedmieszczanom (<strong>Krzysztof Trojak</strong> — <code>19 fl 18 gr</code>, <strong>Marcin Jach [?]</strong> — <code>9 fl</code>, <strong>Piotr Dzionek</strong> — <code>5 fl</code>, <code>#59–#61</code>).</p>
          <p>Rok 1659 zamyka głośny proces wdowy <strong>Moniki Kościekowskiej [?]</strong> przeciw szl. <strong>Piotrowi Świątkowi [?]</strong> o <code>60 złp</code> (<code>#61–#62</code>) oraz zeznania poddanego <strong>Stanisława Grasia</strong> ze wsi <strong>Borów</strong> o kupnie sukna na jarmarku w Kraśniku i pożyczce <code>22,5 gr</code> u Żyda <strong>Mosia Łazarowicza</strong> w obecności ławnika <strong>Wawrzyńca Kowala</strong> (<code>#62–#63</code>, formuła <em>Finis huius anni</em>).</p>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XI: Elekcja 1660, Procesy Jarmarczne i Laudum Pasienia Trzody (skany 64–70)</h2>
          <p>Uroczysta elekcja z 16 I 1660 r. (<code>#64–#65</code>) za zgodą wojewody <strong>Jana Zamoyskiego</strong> i tenutariusza <strong>Krzysztofa Brzozowskiego [Brzostowskiego?]</strong> utrzymała stabilny skład kolegium rajców (<strong>Tharasa</strong>, <strong>Sitarski</strong>, <strong>Nawrocki</strong>, <strong>Kurowic</strong>) i wójta <strong>Sebalda [Ubalda] Janaszkowica</strong>. Wiosną 1660 r. księga rejestruje procesy o skradzione bydło (szl. <strong>Marina Serkówna</strong> vs <strong>Bartosz Boryszowski [Boryszkowski?]</strong> o krowę z jarmarku w Zaklikowie, <code>#65–#66</code>; <strong>Wojciech Gąska</strong> z Polichny za atestacją <strong>JMP Brzezickiego</strong> ze Słodkowa, <code>#69–#70</code>) oraz znieważenie rajcy bełżyckiego <strong>Wojciecha Poniatowskiego</strong> przez urzędowianina <strong>Rudborka</strong> na targu kraśnickim (<code>#67–#68</code>).</p>
          <p>18 IV 1660 r. Sąd Łączony wraz z cechmistrzami i pospólstwem uchwalił <strong>Laudum Pasienia trzody</strong> (<code>#68–#69</code>), ustalając taksy dla pastuchów (<code>2 gr</code> od bydlęcia starego, <code>1 gr</code> od roczniaka i wieprza) oraz prawo zajmowania lub zabijania trzody czyniącej szkody w ogrodach. Z kolei 22 V 1660 r. ławnik <strong>Błażej Kołodziejczyk</strong> uzyskał wyrok chłosty pod pręgierzem i <code>5 grzywien</code> winy na <strong>Krzysztofie Stanisławku</strong> z Wilkołaza za kradzież żyta i grochu (<code>#70</code>).</p>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XII: Sprawa Lipy przed Trybunałem, Szpital Ubogi i Laudum o Liquorach (skany 71–75)</h2>
          <p>W czerwcu 1660 r. szl. <strong>Dorota Lubszycka</strong> ze Starej Wsi przeprowadziła zaprzysiężone zeznania świadków (szl. <strong>Leon Włostek [Włodek?]</strong>, <strong>Mikołaj Włodek [?]</strong>, <strong>Jakub Kurowski [?]</strong>) w sprawie skradzionej krowy odnalezionej u Żyda <strong>Izaaka Grzybka [?]</strong> (<code>#70–#72</code>). Szczególne znaczenie ma kwitacja z 22 VI 1660 r. wystawiona przez Żydów lubelskich <strong>Chaima Moskowicza</strong> i <strong>Lewka Izraelowicza</strong> (w obecności starszych zboru kraśnickiego: <strong>Heliasza Izaakowicza</strong>, <strong>Matka Dławskiego [?]</strong> i <strong>Moska Jarosławskiego</strong>) dla szl. <strong>Tymowskiego [Zymowskiego?]</strong>, dzierżawcy wsi <strong>Lipa</strong>, zrzekająca się pretensji do Trybunału Lubelskiego po zabójstwie Żyda przez poddanego <strong>Wawrzyńca</strong> (<code>#72–#73</code>).</p>
          <p>W lipcu 1660 r. ślusarz i cechmistrz szpitala ubogich <strong>Szymon Pyrek</strong> obronił przed <strong>Adamem Dziwkowskim</strong> z Lublina cesję <strong>Benedykta Nowaka</strong> na sad zagołoborski obciążony czynszem dla szpitala (<code>10 złp</code>) i Bractwa Różańca NMP (<code>25 złp</code>, <code>#74–#75</code>). Partię 3 zamyka początek wielkiego wilkierza miejskiego z 20 VIII 1660 r. — <strong>Laudum o liquorach</strong> (<code>#75</code>).</p>
        </article>'''

anchor_ch = '<h2 class="chapter-title">Rozdział VIII: Otwarcie Roku 1659 i Elekcja Magistratu z Wójtem Janaszkowicem (skany 49–50)</h2>'
idx_ch = src.find(anchor_ch)
assert idx_ch != -1, "Missing anchor_ch"
end_ch = src.find('</article>', idx_ch) + len('</article>')
src = src[:end_ch] + new_chapters + src[end_ch:]

new_cards = '''
        <article class="analytic-card">
          <h2 class="card-title">🐄 9. Uchwały Gospodarcze 1660: Laudum Pasienia Trzody i Laudum o Liquorach (skany #68–#69, #75)</h2>
          <p><strong>Laudum Pasienia trzody (18 IV 1660, #68–#69):</strong> przyjęte przez burmistrza Stanisława Nawrockiego, wójta Sebalda Janaszkowica, ławników, cechmistrzów i pospólstwo w celu ochrony ogrodów i pól od św. Wojciecha. Ustalono opłaty dla pastucha: <code>2 gr</code> od starego bydlęcia, <code>1 gr</code> od roczniaka, <code>1 gr</code> od wieprza, oraz prawo zajmowania lub zabijania szkody w ogrodach.</p>
          <p><strong>Laudum o liquorach (20 VIII 1660, #75):</strong> uchwała rady, ławy, cechmistrzów i pospólstwa w domu burmistrza Macieja Tharasy regulująca wyszynk trunków, czopowe i miary miejskie (dokończenie w Partii 4).</p>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 10. Sprawa ze Wsi Lipa i Kwitacja Żydów Lubelskich pod Wadium 300 Grzywien (skany #72–#73)</h2>
          <p>Dnia 22 VI 1660 r. Żydzi lubelscy <strong>Chaim Moskowicz</strong> i <strong>Lewek Izraelowicz</strong>, w obecności starszych zboru kraśnickiego (<strong>Heliasza Izaakowicza</strong>, <strong>Matka Dławskiego [?]</strong>, <strong>Moska Jarosławskiego</strong>), skwitowali dzierżawcę wsi <strong>Lipa</strong> (dóbr wojewody Jana Zamoyskiego) szl. <strong>Tymowskiego [Zymowskiego?]</strong> po zabójstwie Żyda przez poddanego <strong>Wawrzyńca</strong>. Zrzeczenie opatrzono wysokim zakładem <code>300 grzywien</code> i odniesieniem do Trybunału Koronnego Lubelskiego.</p>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🏛️ 11. Sieć Handlowa i Kradzieże Bydła na Jarmarkach (skany #62–#72)</h2>
          <p>Księga z lat 1659–1660 odsłania zasięg regionalnych powiązań Kraśnika: Zaklików (kupno krowy przez <strong>Bartosza Boryszowskiego</strong> za <code>20 złp</code> od <strong>Jana Mączewskiego</strong>, <code>#66</code>), Bełżyce i Urzędów (zniewaga rajcy bełżyckiego <strong>Wojciecha Poniatowskiego</strong>, <code>#67</code>), Lublin (świadkowie <strong>Marcin Lipnicki</strong> i <strong>Walenty Radachowski</strong>; spór <strong>Adama Dziwkowskiego</strong> o sad, <code>#74</code>), a także Borów, Polichna, Słodków, Stara Wieś i Wilkołaz.</p>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🧾 12. Skład Elekcyjny Magistratu z 1660 r. oraz Dublet #51 = #50 (skany #51, #64–#65)</h2>
          <p><strong>Skan #51 (fol. 23v)</strong> stanowi identyczny dublet mikrofilmowy skanu <strong>#50</strong> (Elekcja 1659). W <strong>Elekcji 1660 r. (16 I, #64–#65)</strong> tenutariusz Krzysztof Brzozowski zatwierdził rajców <strong>Macieja Tharasę</strong>, <strong>Marcina Sitarskiego</strong>, <strong>Stanisława Nawrockiego</strong> i <strong>Wojciecha Kurowica</strong>, wójta <strong>Sebalda [Ubalda] Janaszkowica</strong>, ławników (<strong>Starzyński</strong>, <strong>Kołodziejczyk</strong>, <strong>Sienkowic</strong>, <strong>Chmielowic</strong>, <strong>Kozica</strong>, <strong>Joch [Fox]</strong>), pisarza <strong>Jana Cichonia</strong>, cechmistrzów (<strong>Tharasa</strong>, <strong>Sitarski</strong>, <strong>Chmara</strong>, <strong>Szarek</strong>, <strong>Kozicki</strong>) i egzaktorów (<strong>Paweł Stokowski</strong>, <strong>Andrzej Piecznik</strong>).</p>
        </article>'''

anchor_card = '<h2 class="card-title">🏛️ 8. Pełne Składy Elekcyjne Magistratu z Lat 1658 i 1659 (skany #38–#39, #50)</h2>'
idx_card = src.find(anchor_card)
assert idx_card != -1, "Missing anchor_card"
end_card = src.find('</article>', idx_card) + len('</article>')
src = src[:end_card] + new_cards + src[end_card:]

with open('/home/ubuntu/workspace/Gen/generate_j19_html_part3_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Utworzono generate_j19_html_part3_authentic.py")
