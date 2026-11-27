# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j20_html_part9_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

src = src.replace("main_data_j20_part9.json", "main_data_j20_part10.json")
src = src.replace("gen_data_j20_part9.json", "gen_data_j20_part10.json")

new_monograph_chapters = """
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXVII: Kwitacja Sukcesji po Wójcie Janaszkowiczu i Czynsze Konwentu z 1699 r. (skany 226–233)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 113r–116v</code> łączą końcówkę sesji z marca <strong>1698 r.</strong> (kwitacja ławnika <strong>Wojciecha Bożkowica</strong> dla <strong>Jakuba Lisa</strong> na <code>20 złp</code> i obdukcja pobicia <strong>Jana Smoka</strong>, <code>#226–#227</code>) oraz fragment z listopada <strong>1697 r.</strong> (<code>#231</code>) z ważnym przełomem z roku <strong>1699</strong>. Dnia 16 VI 1699 r. ławnik i deputat Trybunału Zamojskiego <strong>Wojciech Grzymałowski</strong> wraz z żoną <strong>Teresą Janaszkowicową</strong> skwitowali <strong>Wojciecha i Katarzynę Nowackich</strong> z inwentarza po zmarłym wójcie <strong>Ubaldzie Janaszkowiczu</strong>, uznając spłatę <code>500 złp</code> długów z własnych środków Nowackich (<code>#228–#229</code>). Dnia 18 IX 1699 r. przeor kanoników regularnych ks. <strong>Paweł [?]</strong> wyegzekwował zaległe czynsze wyderkafowe od rajców <strong>Jana Majowskiego</strong>, <strong>Macieja Bielaszkowica</strong>, <strong>Stanisława Soleckiego</strong> i <strong>Adama Karola Mrozowskiego</strong> (<code>#232–#233</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXVIII: Spory Sąsiedzkie z Jesieni 1699 r. — Stawy, Tatarka i Długi (skany 234–240)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 117r–120r</code> dokumentują procesy z września i początków października <strong>1699 r.</strong>: dochodzenie podwojciego <strong>Pawła Słomkowskiego</strong> przeciw <strong>Augustynowi Bielaszkowicowi</strong> o kopanie przy stawie i zabranie tatarki (<code>#234–#235</code>, <code>#238</code>, <code>#240</code>), sprawę <strong>Sebastiana Kowalika</strong> z <strong>Jakubem Zajączkiem [Zającem?]</strong> o 80/20 snopów tatarki (<code>#235–#238</code>), proces dawnego rajcy <strong>Stanisława Jesurkiewicza</strong> przeciw <strong>Józefowi Macalowi</strong> o <code>60 złp</code> (<code>#237</code>) oraz pożyczkę <code>5 złp</code> i zboża <strong>Agnieszki Guckiej</strong> dla <strong>Bartosza Wilka</strong> (<code>#235</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXXIX: Wicecechmistrz Tkacki Jan Dumański i Rola Dąbrowskiego (skany 240–245)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 120r–122v</code> z przełomu września i października <strong>1699 r.</strong> głównym wątkiem jest gwałtowny zatarg wicecechmistrza cechu tkackiego <strong>Jana Dumańskiego</strong> z jego szwagrem <strong>Tomaszem Celejem</strong> o zniesławienie w gospodzie i pobicie na Rynku, zakończony wyrokiem 3 dni wieży, przeprosin i 14 grzywien vadium na podstawie zeznań <strong>Jana Szarpy [?]</strong>, <strong>Szymona</strong> i <strong>Matyjasza Piotrowczyków</strong> (<code>#240–#242</code>, <code>#244–#245</code>). Odnotowano także wizję roli przedmieszczanina <strong>Franciszka Dąbrowskiego</strong> nabytej od <strong>Jana Piwoty [?]</strong> po <strong>Marinie Strużynie [?]</strong> (<code>#243–#244</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XL: Tumult Szlachecki na Jarmarku św. Franciszka w 1699 r. (skany 246–250)</h2>
          <div class="chapter-content">
            <p>Ostatnie karty Partii 10 (<code>fol. 123r–125r</code>) przynoszą dramatyczny obraz jarmarku na św. Franciszka (4–5 X <strong>1699 r.</strong>). Obok bójki <strong>Macieja Skarzyka [Skarza]</strong> z <strong>Grzegorzem Michalikiem alias Wosikiem [?]</strong> ze wsi <strong>Wilkołaz</strong> (<code>#246</code>) oraz pobicia <strong>Stanisława Franikowicza [Francyka?]</strong> ze <strong>Stróży</strong> przez czeladź Żyda <strong>Borucha</strong> (<code>#249</code>), w mieście doszło do zbrojnego tumultu szlacheckiego przeciw rezydencji dworzanina Marszałka Wielkiego Koronnego <strong>Jana Wawrzyńca Chmielowskiego</strong> (komisarza dóbr ordynackich <strong>Anny z Gnińskich Zamoyskiej</strong>), w którym porąbano drzwi i okna oraz śmiertelnie poraniono sługę <strong>Michała Pawłowskiego</strong> i raniono <strong>Jana Dumańskiego</strong> przed domem Skarbnika Bełskiego <strong>Stanisława Węglińskiego [?]</strong> (<code>#247–#248</code>, <code>#250</code>).</p>
          </div>
        </article>'''"""

mono_anchor = "        </article>'''\n\nanalytics_html"
assert mono_anchor in src, "Brak kotwicy monograph_html"
src = src.replace(mono_anchor, "        </article>" + new_monograph_chapters + "\n\nanalytics_html", 1)

new_analytics_cards = """
        <article class="analytic-card">
          <h2 class="card-title">🕊️ 37. Finał Sporu o Sukcesję po Wójcie Janaszkowiczu (skany #228–#229)</h2>
          <div class="card-content">
            <p>Akt z 16 VI 1699 r. zamyka wieloletni konflikt majątkowy wokół spadku po wójcie <strong>Ubaldzie Janaszkowiczu</strong>: druga córka wójta, <strong>Teresa</strong> (żona ławnika <strong>Wojciecha Grzymałowskiego</strong>), skwitowała swoją siostrę <strong>Katarzynę</strong> i szwagra <strong>Wojciecha Nowackiego</strong>, potwierdzając, że długi przewyższały aktywa i Nowaccy dopłacili <code>500 złp</code> z własnej kieszeni.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⛪ 38. Czynsze Wyderkafowe Konwentu Kanoników Regularnych (skan #232–#233)</h2>
          <div class="card-content">
            <p>Protokół z 18 IX 1699 r. ukazuje skalę kredytu kościelnego w Kraśniku: przeor konwentu kanoników regularnych pozwał czołowych rajców i mieszczan o wieloletnie zaległości od zapisanych kapitałów wyderkafowych (<code>500 złp</code> u <strong>Macieja Bielaszkowica</strong>, <code>200 złp</code> u <strong>Adama Karola Mrozowskiego</strong>, <code>100 złp</code> i <code>50 złp</code> u <strong>Jana Majowskiego</strong>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🧵 39. Cech Tkacki i Wicecechmistrz Jan Dumański (skany #240–#242, #244–#245, #248)</h2>
          <div class="card-content">
            <p>W aktach z 1699 r. po raz pierwszy pojawia się imiennie wicecechmistrz cechu tkackiego (<em>Vicecechmistrz Cechu Tkackiego</em>) <strong>Jan Dumański</strong> — zarówno jako strona sporu honorowego ze szwagrem <strong>Tomaszem Celejem</strong>, jak i ofiara październikowego tumultu przed domem Skarbnika Bełskiego.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚔️ 40. Tumult Szlachecki na Jarmarku i Dobra Ordynacji Zamoyskiej (skany #247–#250)</h2>
          <div class="card-content">
            <p>Obdukcja przy cyruliku <strong>Jakubie</strong> (<code>#248</code>) i protestacja dworzanina <strong>Jana Wawrzyńca Chmielowskiego</strong> (<code>#250</code>) rzucają światło na relacje Kraśnika z dworem ordynackim <strong>Anny z Gnińskich Zamoyskiej</strong> (Podskarbiny Wielkiej Koronnej) oraz na zagrożenie bezpieczeństwa podczas jarmarku św. Franciszka ze strony uzbrojonej szlachty z powiatu i gości ze <strong>Stróży</strong> oraz <strong>Wilkołaza</strong> (<code>#246</code>, <code>#249</code>).</p>
          </div>
        </article>'''"""

ana_anchor = "        </article>'''\nmain_data_json"
assert ana_anchor in src, "Brak kotwicy analytics_html"
src = src.replace(ana_anchor, "        </article>" + new_analytics_cards + "\nmain_data_json", 1)

with open('/home/ubuntu/workspace/Gen/generate_j20_html_part10_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Wygenerowano generate_j20_html_part10_authentic.py")
