# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j20_html_part8_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

src = src.replace("main_data_j20_part8.json", "main_data_j20_part9.json")
src = src.replace("gen_data_j20_part8.json", "gen_data_j20_part9.json")

new_monograph_chapters = """
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXIII: Kontynuacja Fascykułu z 1664 r. — Jajczykowie, Muszka i Smazanowski (skany 201–203)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 100v–101v</code> zawierają dalsze wyroki sądu wójtowskiego z <strong>1664 r.</strong>: ugodę <strong>Kaspra i Sebastiana Jajczyków</strong> o spłatę <code>220 złp</code> długu po zmarłym ojcu (w ratach po jarmarku po niedzieli <em>Laetare</em> i na św. Michała, <code>#201</code>), dekret dla <strong>Katarzyny i Agnieszki Łosików [?]</strong> przeciw <strong>Magdalenie Piotra Łownej</strong> (<code>#201–#202</code>), dramatyczny proces <strong>Piotra Muszki</strong> przeciw <strong>Tomaszowi Jajczykowi</strong> (mieszkańcowi u <strong>Jakuba Smazanowskiego</strong>) o nocne włamanie do komory, worki, siekierkę i pobicie na drodze z kościoła (<code>#202–#203</code>) oraz spór <strong>Macieja Lisika</strong> z <strong>Andrzejem Macalem</strong> o dziesięcinę jęczmienia po <strong>Gabrielu Bąku [?]</strong> (<code>#203</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXIV: Cech Kuśnierski, Dziesiętnik Kłopot i Dublet Mikrofilmu (skany 204–211)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 102r–105r</code> księga powraca do roku <strong>1698</strong>: od dekretu z 22 X 1698 r. dla <strong>Stanisława Luterskiego</strong> w sporze z cechem kuśnierskim (<code>#204</code>), przez obdukcję ran <strong>Pawła Kozaka</strong> pobitego przez <strong>Rdzonków [Rozdzeniów?]</strong> (<code>#205</code>) i skargi na dziesiętnika przedmiejskiego <strong>Pawła Kłopota</strong> o składkę gromadzką i pobicie <strong>Matyjasza Skarza [?]</strong> (<code>#208</code>, z dubletem mikrofilmowym na <code>#209</code>, oraz zeznanie o wygnaniu z kijem przez żonę Skarza na <code>#210</code>), po skargę <strong>Piotra Tokarczyka</strong> przeciw opiekunom o sprzedaż domu w Rynku rajcy <strong>Janowi Majowskiemu</strong> (<code>#211</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXV: Kantor Synagogi Izaak, Elżbieta Okoniowa i Sprzedaż Roli Dubaja (skany 212–218)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 105v–108v</code> dokumentują sprawy z marca, kwietnia i lipca <strong>1698 r.</strong>: ugodę kowala <strong>Jana Rygara [?]</strong> z <strong>Jakubem Józefkowicem</strong> (<code>#213</code>), pozew kantora synagogi kraśnickiej <strong>Izaaka</strong> (<em>Isaac Cantoris Sinagogae</em>) przeciw <strong>Janowi Grymuzie</strong> (<code>#214</code>), wyrok zasądzający <code>85 złp</code> dla wdowy <strong>Elżbiety Okoniowej</strong> i jej syna <strong>Jana Okonia</strong> od <strong>Adama Wilka</strong> (<code>#215–#216</code>) oraz sprzedaż ćwierci roli ojcowskiej przez <strong>Jakuba Dubaja</strong> i <strong>Annę Zdębiównę [?]</strong> małżonkom <strong>Stanisławowi Rakowskiemu</strong> i <strong>Mariannie Piotrowczykównie</strong> za <code>180 złp</code> z prawem odkupu (<code>#218</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXVI: Procesy o Sukcesję (Studziccy vs Stachowice, Grymuza vs Gucka) i Hymn Maryjny (skany 219–225)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 109v–112r</code> zamyka seria spraw spadkowych z kwietnia i lipca <strong>1698 r.</strong>: ugoda ślusarza <strong>Grzegorza Kaczorkowica</strong> z dawnym rajcą <strong>Stefanem Kwasowicem</strong> po kondemnacie w Trybunale Zamojskim (<code>#220</code>), spór <strong>Jana Grymuzy</strong> z wdową po <strong>Grzegorzu Guckim</strong> o sukcesję (<code>#223</code>) oraz wielowątkowy proces <strong>Sebastiana i Anny Studzickich</strong> z <strong>Błażejem i Anną/Katarzyną Stachowicami</strong> o dobra po <strong>Wojciechu i Katarzynie Nogajach</strong>, zakończony kompromisem z 29 IV 1698 r. (<code>#221–#222</code>, <code>#224</code>). Wyjątkowym zabytkiem literackim jest wpisany u góry <code>fol. 112r</code> łaciński hymn maryjny <em>Reparatrix Consolatrix Desperantis Animae</em> (<code>#225</code>).</p>
          </div>
        </article>'''"""

mono_anchor = "        </article>'''\n\nanalytics_html"
assert mono_anchor in src, "Brak kotwicy monograph_html"
src = src.replace(mono_anchor, "        </article>" + new_monograph_chapters + "\n\nanalytics_html", 1)

new_analytics_cards = """
        <article class="analytic-card">
          <h2 class="card-title">✡️ 33. Kantor Synagogi Kraśnickiej Izaak przed Sądem Wójtowskim (skan #214)</h2>
          <div class="card-content">
            <p>Wpis z wiosny 1698 r. poświadcza bezpośredni udział urzędników gminy żydowskiej w życiu prawnym miasta: <strong>Izaak</strong>, określony jako <em>Cantor Sinagogae Crasnicensis</em> (kantor synagogi kraśnickiej), skutecznie pozwał przez bedela <strong>Wojciecha Ornatowskiego</strong> mieszczanina <strong>Jana Grymuzę</strong>, uzyskując na nim karę 3 grzywien.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🧥 34. Cech Kuśnierski, Ślusarze i Kowale w Aktach z 1698 r. (skany #204, #213, #220–#221, #223)</h2>
          <div class="card-content">
            <p>Akta Partii 9 odsłaniają strukturę rzemiosła kraśnickiego: rewizję ksiąg i przywilejów cechu kuśnierskiego z udziałem cechmistrzów <strong>Stanisława Jesurkiewicza</strong> i <strong>Wawrzyńca Bielaszkowica</strong> oraz brata cechowego <strong>Stanisława Luterskiego</strong> (<code>#204</code>), działalność kowala <strong>Jana Rygara [?]</strong> (<code>#213</code>) oraz ślusarza <strong>Grzegorza Kaczorkowica</strong> (<code>#220–#221</code>, <code>#223</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 35. Łaciński Hymn Maryjny Pisarza Miejskiego i Dublet Mikrofilmu (skany #209, #225)</h2>
          <div class="card-content">
            <p>Na górnym marginesie <code>fol. 112r</code> (<code>#225</code>) pisarz zapisał ośmiowersowy łaciński hymn rymowany do Matki Bożej (<em>Reparatrix Consolatrix Desperantis Animae</em>) o czystość serca i opiekę w godzinie sądu — rzadki przykład osobistej pobożności kancelaryjnej. Pod względem kodykologicznym skan <code>#209</code> stanowi dublet mikrofilmowy karty <code>fol. 104r</code> (<code>#208</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 36. Poszlaki Kradzieży w 1664 r. i Prawa Sieroce w 1698 r. (skany #202–#203, #211, #215–#216)</h2>
          <div class="card-content">
            <p>Proces <strong>Piotra Muszki</strong> przeciw <strong>Tomaszowi Jajczykowi</strong> z 1664 r. (<code>#202–#203</code>) ilustruje rygorystyczne prawo dowodowe: same poszlaki (porzucone worki i siekierka) nie wystarczały do skazania bez przysięgi oczyszczającej. W 1698 r. sąd chronił zaś majątek sierot i wdów — od nakazu spłaty <code>85 złp</code> dla <strong>Elżbiety Okoniowej</strong> (<code>#215–#216</code>) po kontrolę opiekunów sprzedających dom w Rynku (<code>#211</code>).</p>
          </div>
        </article>'''"""

ana_anchor = "        </article>'''\nmain_data_json"
assert ana_anchor in src, "Brak kotwicy analytics_html"
src = src.replace(ana_anchor, "        </article>" + new_analytics_cards + "\nmain_data_json", 1)

with open('/home/ubuntu/workspace/Gen/generate_j20_html_part9_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Wygenerowano generate_j20_html_part9_authentic.py")
