# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j20_html_part6_authentic.py', 'r', encoding='utf-8') as f:
    src = f.read()

src = src.replace("main_data_j20_part6.json", "main_data_j20_part7.json")
src = src.replace("gen_data_j20_part6.json", "gen_data_j20_part7.json")

new_monograph_chapters = """
        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXV: Księga z 1698 r. — Obdukcje Ran, Szkody Polne i Spór o Sukcesję po Wójcie Janaszkowiczu (skany 151–160)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 75r–79v</code> otwierają serię wpisów z przełomu wiosny i lata <strong>1698 r.</strong> (z wplecioną protestacją z 23 VI <strong>1695 r.</strong> przedmieszczanina z Piasków <strong>Szymona Olchowskiego [?]</strong> przeciw Żydowi <strong>Ickowi [?]</strong> synowi <strong>Biernasia [?]</strong>, <code>#159</code>). Wśród obdukcji na plan pierwszy wysuwa się pobicie młynarza <strong>Jana Łacińskiego [Łazińskiego?]</strong> przez <strong>Jana i Wojciecha Żydków [?]</strong> (<code>#151–#152</code>, <code>#171</code>) oraz ciężkie rany <strong>Stanisława Soleckiego</strong>, <strong>Matyasza Boruckiego [?]</strong> i <strong>Pawła Dąbrowskiego</strong> oglądane przez ławników i cyrulika <strong>Mojżesza Abramowica</strong> (<code>#160</code>). Odnotowano też wizję szkody 40 snopów w życie <strong>Katarzyny Nowackiej</strong> (<code>#152</code>) oraz kontumacje z udziałem Żyda <strong>Berka Moszkowicza</strong> (<code>#157–#158</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXVI: Spory Przedmieszczan o Rolę Tudorkowską i Zaginiony Wóz Podwodny (skany 161–167)</h2>
          <div class="chapter-content">
            <p>Na kartach <code>fol. 80r–83v</code> utrwalono sąsiedzkie procesy z czerwca i lipca <strong>1698 r.</strong>: dekret z 26 VI 1698 r. przyznający <strong>Annie Tudorkowej</strong> córce zmarłego <strong>Stanisława Tudorka</strong> kwaterę roli na Piaskach przeciw <strong>Jadwidze Gąskowicowej [?]</strong> (<code>#161–#162</code>) oraz wielowątkowe śledztwo w sprawie wozu przeznaczonego na podwodę do Zamościa pod <strong>P. Deputata</strong> (<code>#162–#164</code>, <code>#166–#167</code>). Z zeznań <strong>Marcina Rymarczyka</strong>, <strong>Katarzyny Kozakowej</strong>, jej syna <strong>Kozakowicza</strong> i <strong>Tomasza Starego Kmiecia</strong> wyłania się obraz poszukiwań wozu odnalezionego ostatecznie w stodole <strong>Szymona Olchowskiego</strong> (Kuśmierza), zwieńczony ugodą i vadium 50 grzywien (<code>#167</code>). Wklejona luźna karta z 26 IX 1698 r. dokumentuje ugodę płócienniczki <strong>Jadwigi Taborówny</strong> z pasierbami (<code>#165</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXVII: Warstwa z 1698 r. (fol. 84–85) — Tumult u Karola Mrozowskiego i Regestr po Annie Kempionce (skany 168–171)</h2>
          <div class="chapter-content">
            <p>Karty <code>fol. 84r–85v</code> rozpoczynają osobny dział roku <strong>1698</strong> (<em>Annus 1698. Cum Dei Auxilio Sit Felix</em>) od manifestacji <strong>Karola Mrozowskiego</strong> z 23 I 1698 r. o złożeniu 200/300 zł dla <strong>Stanisława Soleckiego</strong> i <strong>Adama Potokowica</strong> oraz relacji o nocnym tumultcie w jego domu z udziałem parobka <strong>Stasia</strong> od <strong>Pani Mundajnej [?]</strong> z Izdebna (<code>#168–#169</code>). Pod datą 22 IV 1698 r. wpisano cenny regestr spadkowy po zmarłej <strong>Annie Kempionce [?]</strong>, żonie <strong>Matyjasza Piotrowczyka</strong>, z podziałem klaczy ze źrebięciem dla syna <strong>Babiarczyka [?]</strong> oraz krów dla młodszych dzieci (<code>#169</code>). Dalsze karty zawierają spory o kulbakę (<code>#170</code>) i pozew przez brewe od <strong>Katarzyny Nowackiej</strong> (<code>#171</code>).</p>
          </div>
        </article>

        <article class="monograph-chapter">
          <h2 class="chapter-title">Rozdział XXVIII: Wielki Proces o 802 złp 15 gr między Pawłem Słomkowskim a Nowackimi (skany 172–175)</h2>
          <div class="chapter-content">
            <p>Końcowe karty Partii 7 (<code>fol. 86r–87v</code>) wypełnia zacięty proces przed Sądem Złożonym Radziecko-Wójtowsko-Ławniczym między podwojcim/wicewójtem kraśnickim <strong>Pawłem Słomkowskim</strong> a landwójtem urzędowskim <strong>Wojciechem Nowackim</strong> i jego żoną <strong>Katarzyną Janaszkowicową</strong> o dług w wysokości <strong>802 złp 15 gr</strong> z dóbr po zmarłym wójcie <strong>Ubaldzie Janaszkowiczu</strong>. Obok profesjonalnych pełnomocników — adwokata <strong>Jana Onufrego Kieniewicza [Onupkiewicza?]</strong> i mistrza malarstwa <strong>Adama Karola Mrozowskiego</strong> (<code>#172</code>) — w aktach odnotowano próbę komplanacji w domu rajcy <strong>Jana Majowskiego</strong> (<code>#173</code>), plenipotencję dla pasierba <strong>Wojciecha Słomkowskiego</strong> (<code>#173–#174</code>) oraz dekret z 21 XI 1698 r. skazujący Słomkowskiego na 15 grzywien i 15 dni wieży, od którego złożył on apelację do Trybunału Zamojskiego wraz z protestacją o znieważające słowa w sądzie (<code>#174–#175</code>).</p>
          </div>
        </article>'''"""

mono_anchor = "        </article>'''\n\nanalytics_html"
assert mono_anchor in src, "Brak kotwicy monograph_html"
src = src.replace(mono_anchor, "        </article>" + new_monograph_chapters + "\n\nanalytics_html", 1)

new_analytics_cards = """
        <article class="analytic-card">
          <h2 class="card-title">🩺 25. Cyrulik Mojżesz Abramowic i Procedura Obdukcji Ran w 1698 r. (skany #151–#153, #160, #171)</h2>
          <div class="card-content">
            <p>Księga z 1698 r. ukazuje drobiazgowy protokół oględzin sądowo-lekarskich: delegowani ławnicy (<strong>Stefan Kwasowic</strong>, <strong>Wojciech Grzymałowski</strong>, <strong>Wawrzyniec Bielaszkowic</strong>, <strong>Wojciech Bożkowic</strong>) wraz z cyrulikiem <strong>Mojżeszem Abramowicem</strong> mierzyli głębokość ran (<em>o półtora członka</em>, <em>aż do kości</em>) i odnotowywali podbite oczy, pręgi od kijów oraz pociętą odzież (<code>#160</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">⚖️ 26. Sukcesja po Wójcie Ubaldzie Janaszkowiczu i Sąd Złożony (skany #155, #172–#175)</h2>
          <div class="card-content">
            <p>Spadek po zmarłym wójcie kraśnickim <strong>Ubaldzie Florianie Janaszkowiczu</strong> wywołał serię procesów między jego córką <strong>Katarzyną</strong> (żoną landwójta urzędowskiego <strong>Wojciecha Nowackiego</strong>) a wicewójtem kraśnickim <strong>Pawłem Słomkowskim</strong> (o 802 złp 15 gr) oraz ławnikiem <strong>Wojciechem Grzymałowskim</strong>. W sprawach tych orzekał Sąd Złożony z udziałem zawodowych pełnomocników i z prawem apelacji do Trybunału Zamojskiego.</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">🐎 27. Podwody do Zamościa i Mobilność Mieszczan na Wiśle (skany #162–#164, #166)</h2>
          <div class="card-content">
            <p>Zeznania w sprawie wozu <strong>Marcina Rymarczyka</strong> i <strong>Sebastiana Brząsa [?]</strong> odsłaniają ciężary transportowe mieszczan kraśnickich (podwody pod deputata do Zamościa w obliczu przemarszu żołnierzy) oraz sezonową aktywność handlową: przedmieszczanin <strong>Szymon Olchowski</strong> uzyskał w lipcu 1698 r. odroczenie procesu z powodu wyjazdu na <strong>Wisłę</strong> (<code>#164</code>).</p>
          </div>
        </article>

        <article class="analytic-card">
          <h2 class="card-title">📜 28. Wklejki Archiwalne i Regestry Spadkowe Kobiet (skany #165, #169)</h2>
          <div class="card-content">
            <p>Partia 7 zachowała luźną kartę wszytą jako <code>fol. 82r</code> z ugodą płócienniczki <strong>Jadwigi Taborówny</strong> z pasierbami (<code>#165</code>) oraz pośmiertny inwentarz ruchomości po <strong>Annie Kempionce [?]</strong>, żonie <strong>Matyjasza Piotrowczyka</strong>, precyzyjnie rozdzielający bydło między dzieci z pierwszego i drugiego małżeństwa oraz środki na godny pogrzeb (<code>#169</code>).</p>
          </div>
        </article>'''"""

ana_anchor = "        </article>'''\nmain_data_json"
assert ana_anchor in src, "Brak kotwicy analytics_html"
src = src.replace(ana_anchor, "        </article>" + new_analytics_cards + "\nmain_data_json", 1)

with open('/home/ubuntu/workspace/Gen/generate_j20_html_part7_authentic.py', 'w', encoding='utf-8') as f:
    f.write(src)

print("Wygenerowano generate_j20_html_part7_authentic.py")
