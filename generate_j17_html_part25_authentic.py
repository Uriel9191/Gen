# -*- coding: utf-8 -*-
import json
import re

with open('/home/ubuntu/workspace/Gen/main_data_j17_part25.json', encoding='utf-8') as f:
    main_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part25.json', encoding='utf-8') as f:
    gen_data = json.load(f)

# Wczytujemy szkielet referencyjny z J40
with open('/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html', encoding='utf-8') as f:
    j40_html = f.read()

# Wyodrębniamy nagłówek z J40
head_end = j40_html.find('</head>')
head_part = j40_html[:head_end].replace('Akta Miasta Kraśnika (1761–1788)', 'Akta Miasta Kraśnika (1651–1759) – Księga wójtowsko-ławnicza i sądu łączonego')
head_part = re.sub(r'<title>.*?</title>', '<title>Jednostka 17 – Akta Miasta Kraśnika (1651–1759) | Cyfrowe Kompendium Źródłowe</title>', head_part)

# Rozdziały monografii dla J17 (rozbudowane o Partie 1–5)
monograph_html = """
      <div class="monograph-content">
        <h2>🏛️ Pełna Synteza Monograficzna Jednostki 17</h2>
        
        <h3>Rozdział I: Kodykologia, Proweniencja i Identyfikacja Archiwalna Woluminu</h3>
        <p>
          Jednostka archiwalna oznaczona współczesną sygnaturą <strong>35/40/0/1/17</strong> w zespole <em>Akta miasta Kraśnika</em> (dawny Tom 12 z rejestru mikrofilmowego nr 110404 Archiwum Państwowego w Lublinie) stanowi jeden z najobszerniejszych i najważniejszych zabytków sądownictwa miejskiego Kraśnika przełomu XVII i XVIII stulecia. Rękopis liczący w obecnym układzie 776 skanów cyfrowych (355 kart w oryginalnej foliacji papieru czerpanego o wymiarach 33 × 20,5 cm) posiada na oprawie inskrypcję tytułową: <em>„№ 12. Książka rożnych czynności lepistnych Miasta Kraśnika Do onucu N 465. Z Lat 1700, 1756–1759”</em>.
        </p>
        <p>
          Autopsja źródłowa pierwszych 250 skanów woluminu (karty 1r–122r) wykazuje, że zasadniczy zrąb protokołów otwiera się kompletną serią sesji sądu wójtowsko-ławniczego oraz sądu łączonego z <strong>roku 1700</strong>, w którą introligator włączył zarówno oryginalną, dwukartkową składkę siedemnastowieczną z <strong>roku 1651</strong> (skany 111–114, fol. 53r–54v), jak i składkę z <strong>roku 1694</strong> (skany 229–231, fol. 111r–112v) oraz obszerną warstwę z lat <strong>1730–1731</strong> (od skanu 232, fol. 113r). Wyjaśnia to ostatecznie wielowarstwowy charakter woluminu.
        </p>

        <h3>Rozdział II: Skład Personalny i Elity Urzędnicze Kraśnika w 1700 r.</h3>
        <p>
          Protokoły z 1700 r. ujawniają pełną hierarchię korporacji rządzącej miastem. Wokandzie przewodniczy <strong>Jan Majowski – wójt kraśnicki</strong>, wspierany przez podwójciego <strong>Stanisława Jerzykiewicza</strong> oraz landwójta <strong>Wojciecha Nowakowicza (Nowackiego)</strong>. W składzie orzekającym połączonego sądu wójtowsko-radzieckiego zasiadają wybitni przedstawiciele patrycjatu kraśnickiego:
        </p>
        <ul>
          <li><strong>Adam Kotowicz</strong> – burmistrz urzędujący (Proconsul), prowizor szpitala św. Ducha, zamożny posesjonat gruntowy na Podlesiu.</li>
          <li><strong>Jan Barankowicz</strong> – burmistrz urzędujący i radny, reprezentant interesów bractw religijnych i posesjonat kamienicy rynkowej.</li>
          <li><strong>Wojciech Szymatowski</strong> – burmistrz i rezydent kraśnicki, rewizor podymnego, zaangażowany w wielkie transakcje gruntowe i spory z klerem.</li>
          <li><strong>Stefan Gostkowicz</strong> – dawny burmistrz, radca miejski oraz mistrz cechu kowalskiego.</li>
          <li><strong>Stanisław Płechowicz</strong> oraz <strong>Jan Onuszkowicz</strong> (zmarły przed majem 1700 r., wdowa Ewa) – rajcy i burmistrzowie kraśniccy.</li>
          <li><strong>Wojciech Borkiewicz (Borkowicz)</strong> oraz <strong>Laurenty Pielaszkowicz</strong> – wieloletni ławnicy przysięgli sądu wójtowskiego i kryminalnego.</li>
        </ul>

        <h3>Rozdział III: Spory Rodzinne, Mir Miejski i Wymiar Karny</h3>
        <p>
          W sprawach karnych i deliktowych dominuje kategoria obrony miru miejskiego (<em>pax civitatis</em>) oraz dyscyplinowania gwałtownych konfliktów wewnątrzrodzinnych. Modelowym przykładem jest proces braci Hardyszów (fol. 1r, 2v), w którym sąd za pobicie ojca i zgorszenie publiczne nałożył karę 14 grzywien (po połowie na więzienie ratuszowe i Bramę Lubelską). Z kolei na skanach 76–77 wdowa Krystyna Puklina uzyskała areszt dla zięcia Tomasza Oczapki, a na skanie 122 odnotowano drastyczną obdukcję ran zadanych siekierą i obuchem Maciejowi Starykowi przez własnego brata Andrzeja Bregczyka.
        </p>

        <h3>Rozdział IV: Sieć Szpitalna, Obligi Prepozytury Św. Ducha i Opieka nad Chorymi</h3>
        <p>
          Obok kapitałów prepozytury szpitala św. Ducha z 1700 r. (Adam Kotowicz, Jan Kruszelnicki, legat młynarza Sawinowica), wszytka z 1651 r. odsłania funkcjonowanie tej samej instytucji pół wieku wcześniej pod zarządem prowizora <strong>Stanisława Szafrańskiego</strong> (skan 111, proces o 80 złp przeciw Marcinowi Szczerbicowi). Z kolei skan 118 ilustruje praktykę zapisów na łożu śmierci w zamian za opiekę szpitalną: chora Maryna Frużyna, porzucona przez sąsiadów, zapisała dobytek Matyaszowi Pionowi za przewiezienie do szpitala i wyprawienie pogrzebu.
        </p>

        <h3>Rozdział V: Sprawa Karna Szymona Kuparki: Wymiar Sprawiedliwości i Wyrok Śmierci na Stosie</h3>
        <p>
          Wstrząsającym przełomem badawczym woluminu jest kompletny protokół procesu kryminalnego z września i października 1700 r. (fol. 14r–15r, 21v–22r) przeciwko Szymonowi Kuparce, pasterzowi ze wsi Wilkołaz. Oskarżony o grzech sodomii/bestializmu, po czterokrotnych torturach kata miejskiego, został skazany przez sąd łączony (wójt Majowski, burmistrz Kotowicz, deputat Płechowicz) na <strong>spalenie żywcem na stosie wraz ze zwierzęciem</strong> na mocy Prawa Saskiego i Magdeburskiego.
        </p>

        <h3>Rozdział VI: Relacje Patrycjatu z Klasztorem Kanoników Regularnych i Zamkiem Kraśnickim</h3>
        <p>
          Konwent Kanoników Regularnych Lateraneńskich pod zwierzchnictwem preora i dyrektora kościoła <strong>ks. Pawła Wilhelma Pajeckiego</strong> (przy aprobacie prałata i generała zakonu <strong>ks. Franciszka Starskiego</strong>, skan 119) stanowił kluczową instytucję kredytowo-własnościową miasta, zarządzającą funduszami Arcybractwa i placami rynkowymi. Zamek Kraśnicki reprezentowany przez wojewodzinę <strong>Annę z Gnińskich Zamoyską</strong> oraz administratorów klucza (Kazimierz Błędowski, Jan Smoleński, Jan Zaorski) egzekwował asygnacje i arendy.
        </p>

        <h3>Rozdział VII: Odkrycie Rzemiosła Artystycznego: Malarze Kraśniccy Siudziński i Mrokowski</h3>
        <p>
          Skany 31v–35r, 77r oraz 50v (skan 106) odsłaniają środowisko malarzy kraśnickich u progu XVIII w.: zmarłego Adama Karola Siudzińskiego, czynnego mistrza Adama Karola Mrokowskiego oraz wdowę Barbarę Mrokowską po Karolu Mrokowskim (proces z Żydem Leybusiem o półtorej beczki piwa).
        </p>

        <h3>Rozdział VIII: Posesje przy Jatkach Żydowskich, Konflikty o Ogrody i Gospodarka Młyńska</h3>
        <p>
          Skany 51–125 dokumentują intensywny obrót nieruchomościami oraz zatargi z udziałem młynarza miejskiego <strong>Józefa Wilka (Molitora)</strong>, którego tożsamość (Wilk = Molitor) jednoznacznie potwierdza dopisek nadpisany na skanie 116.
        </p>

        <h3>Rozdział IX: Spory Sukcesyjne Patrycjatu i Najwyższy Trybunał Miast Zamoyskich</h3>
        <p>
          Karty 37r–37v (skany 78–79) dokumentują wielki proces spadkowy po zmarłym wójcie ordynaryjnym Ubaldim Janaszkowicu między Pawłem Słomkowskim a landwójtem Wojciechem Nowakowiczem i Katarzyną z Janaszkowiców przed Najwyższym Trybunałem Miast Ordynacji Zamoyskiej.
        </p>

        <h3>Rozdział X: Obrót Kamienicami w Rynku Kraśnickim i Integracja Kupców Żydowskich</h3>
        <p>
          Karty 46r–48r (skany 97–100) zawierają wieczystą transakcję sprzedaży i dzierżawy murowanej kamienicy rynkowej (Dóbr Paweckich) przez ks. przeora Pawła Wilhelma Pajeckiego i burmistrza Jana Barankowicza kupcom żydowskim Borkowi Herszkowiczowi i Berenszowi Koplowi z czynszem wieczystym na św. Michała.
        </p>

        <h3>Rozdział XI: Odkrycie Najstarszej Warstwy Woluminu – Wszyty Poszyt z 1651 roku (skany 111–114)</h3>
        <p>
          Przełomowym odkryciem kodykologicznym Partii 5 jest zidentyfikowanie dwóch wszytych kart z maja i czerwca <strong>1651 roku</strong> (fol. 53r–54v, spisanych siedemnastowieczną kursywą kancelaryjną pod wójtem <strong>Andrzejem Grzybowskim</strong>). Zabytek z epoki powstania Chmielnickiego dokumentuje m.in. działalność cechmistrza kowali w karczmie Żyda Kopla (skan 112), oblig Adama Kafranka na 50 złp, sprzedaż gruntu między Kiderlami a Grzegorzkami (skan 113) oraz wstrząsający proces o zabójstwo chłopca Kubosia siekierą przez Tomasza, syna Jadwigi Bartoszkowej (skan 114), rozstrzygany na zasadzie przysięgi oczyszczającej matki i oszacowania głowszczyzny przez ośmiu mężów.
        </p>

        <h3>Rozdział XII: Cech Kowalski, Nadużycia Samorządowe i Bezpieczeństwo Jarmarczne w 1700 r.</h3>
        <p>
          Skany 115–125 ukazują mechanizmy samorządowe cechów oraz patologie władzy na przedmieściach. Na skanie 124 mistrz kowalski i były burmistrz <strong>Stefan Gostkowicz</strong> wraz z kowalem Wawrzyńcem Staficą rozstrzygają spór przed sądem wójtowskim pod karą wosku (3 i 2 funty wosku na Cech Kowalski). Na skanie 125 świadek Jan Więckowicz ujawnia kulisy wymuszeń wójta przedmiejskiego Marcina Dymarczyka, który miał obiecać byłemu burmistrzowi Stefanowi Kwaśnicowi krowę za stronnicze poparcie w sporze z Tomaszem Kobcem. Z kolei skany 122–123 ukazują zagrożenia na jarmarkach kraśnickich (kradzieże koni z dóbr Świdnik Stanisława Linowskiego, pogoń sługi szlacheckiego Stanisława Wichra oraz zatargi Żyda Mośka Jarosławskiego na Ratuszu).
        </p>
        <h3>Rozdział XIII: Procesy o Czary, Bezpośrednie Dowody Korupcji i Zatargi Patrycjatu z Klerem (skany 126–150)</h3>
        <p>
          Kolejna partia akt z maja–lipca 1700 r. (fol. 60v–72v) przynosi bezcenne świadectwa funkcjonowania wymiaru sprawiedliwości i życia codziennego Kraśnika. Na skanie 130 ławnik przysięgły <strong>Wojciech Borkowicz</strong> złożył pod przysięgą bezpośrednie zeznanie potwierdzające, że w trakcie rozmowy na komornym u byłego burmistrza Stefana Kwaśnica <strong>Marcin Dymarczyk</strong> obiecał mu krowę za przychylność w procesie przeciw Tomaszowi Kopcowi (na skanie 148 Kopeć uzyskał wadium 14 grzywien). Z kolei na skanach 141 oraz 147–148 odnotowano pełny proces o zadanie czarów i otrucie dziecka między winiarzem Marcinem Chudzikiem a małżonkami Wojciechem i Maryną Kłotkami, zakończony wyznaczeniem dla Maryny Kłotkowej roty przysięgi oczyszczającej z dwoma świadkami pod rygorem kary kryminalnej za złamanie pokoju.
        </p>

        <h3>Rozdział XIV: Jurysdykcja Zamku Zamoyskiego, Cech Szewski i Obrazy Przemocy Codziennej</h3>
        <p>
          Protokoły z czerwca i lipca 1700 r. ukazują częste krzyżowanie się kompetencji sądu miejskiego z <strong>Sądem Skarbowym Komisarskim Zamku Zamoyskiego</strong>. Arendarz <strong>Pinchas Dawidowicz</strong> w sporze z rzeźnikiem Józefem Mazałą (skany 126–127, 135, 143, 149) odwoływał się do komisji zamkowej pod zwierzchnictwem Podskarbiny Wielkiej Koronnej Zamoyskiej, usprawiedliwiając niestawiennictwo wyjazdem służbowym do Lublina z polecenia ekonoma ordynackiego. Równolegle narastały napięcia na linii patrycjat–klasztor: przeor ks. Paweł Pajecki wniósł na skanie 144 dramatyczną protestację przeciw burmistrzowi Wojciechowi Szymatowskiemu o bluźnierstwa i brak szacunku dla krucyfiksu na stole sądowym, a na skanach 132 i 147–148 Cech Szewski pod przewodnictwem cechmistrza Stanisława Bieleckiego dochodził zapisanej testamentowo ćwierci roli Łukasza Baranowskiego za odprawianie kwartalnych mszy żałobnych. Skany 137, 142, 144–146 i 150 dokumentują ponadto serię szczegółowych obdukcji krwawych bójek (m.in. napaść Dymarczyków na młynarza Jędrzeja Wilka i Smoków na grobli, bójkę przed domem Żyda Szmula oraz potyczkę Dudka, Mazurka i Rępki).
        </p>
        <h3>Rozdział XV: Otwarcie Roku 1700 (<em>Annus 1700 Incipit</em>) i Przemieszanie Składek Introligatorskich (skany 151–175)</h3>
        <p>
          Analiza kodykologiczna skanów 151–175 (fol. 73r–84v) ujawnia kluczowy fakt dla rekonstrukcji układu księgi: na karcie 77r (skan 159) znajduje się oryginalny nagłówek otwierający rok sądowy <strong><em>„Annus 1700. Incipit. In Nomine Domini Amen”</em></strong> z datą <strong>8 stycznia 1700 r.</strong> (piątek po święcie Trzech Króli), kiedy sądom przewodniczył jeszcze żyjący wójt ordynaryjny <strong>Jan Onuszkowicz</strong> (zmarły przed majem 1700 r.). Oznacza to, że introligator łączący poszyty zszył w tym miejscu najwcześniejszą chronologicznie składkę księgi ze stycznia–kwietnia 1700 r. za sesjami z czerwca i lipca 1700 r. Ponadto na skanie 171 zidentyfikowano dokładny dublet mikrofilmowy karty 82v (skan 170).
        </p>

        <h3>Rozdział XVI: Śledztwo w Sprawie Zofii Skatkównej, Spór Malarza Mrokowskiego i Obrót Gruntami</h3>
        <p>
          Sesja styczniowa ze skanów 160–164 dokumentuje drobiazgową inkwizycję sześciu świadków (m.in. kowala Jana Zająca, dziada ze Szpitala św. Ducha Wojciecha Mazura, winiarza Marcina Chudzika i młynarza Józefa Wilka) dotyczącą okoliczności nagłej śmierci służącej Zofii Skatkównej ze Stróży i zatargu o spadek po niej (kabat, spodnie, płótno, dwie krowy i ogród). Skany 157–158 ukazują z kolei obdukcję pobicia Żydówki Franki Habukowej przez Zuzannę Grzańską oraz bezskuteczną próbę egzekucji 402 złp 15 gr przez braci Słomkowskich od landwójta Nowakowicza według wyroku Trybunału Zamojskiego. Na skanie 172 malarz <strong>Adam Karol Mrokowski</strong> bronił swojego honoru w sporze z podwójcim Stanisławem Jerzykiewiczem, a na skanach 174–175 Wojciech Starzykiewicz sprzedał stodołę z gruntem za Bramą Lubelską Żydowi Ickowi Dawidowiczowi i jego żonie Feygli za 60 złp, podczas gdy cały sąd wniósł protestację przeciw Grześkowi rzeźnikowi o wtargnięcie z szablą i zniewagę urzędu.
        </p>

        <h3>Rozdział XVII: Finał Procesu o Czary, Śmierć Malarza Mrokowskiego i Ojcowizna Kopciów (skany 176–200)</h3>
        <p>
          Kolejna partia akt z lipca oraz października–listopada 1700 r. (fol. 85r–96v, w tym dublety mikrofilmowe skanów 183/184 i 185/186) przynosi rozstrzygnięcia najgłośniejszych procesów miasta. Na skanach 180–181 Sąd Obojny ujawnił genezę sporu między <strong>Tomaszem Kopciem</strong> a wójtem przedmieścia Piaski <strong>Marcinem Dymarczykiem</strong>: żoną Kopcia była <strong>Marianna z Jasieńskich</strong>, córka zmarłego Augustyna Jasieńskiego i Reginy, a Dymarczyk był jej ojczymem. Dekret z 30 lipca 1700 r. przyznał Kopciom prawo wykupu ojcowizny (ćwierci roli i stodoły) za <strong>120 złp</strong> płatnych na św. Marcina; 12 listopada 1700 r. (skan 190) Kopeć złożył uroczystą protestację z okazaniem gotówki przy świadkach (Macieju Łędańskim, Tomaszu Anczerku i młynarzu Józefie Wilku). Na skanach 181–182 zapis z 27 października 1700 r. dokumentuje śmierć mistrza malarskiego <strong>Adama Karola Mrokowskiego</strong> (żyjącego jeszcze w marcu 1700 r.) oraz ponowne małżeństwo jego wdowy <strong>Barbary z Janaszkowiców</strong> z przybyłym z Podlasia <strong>Wawrzyńcem Broskowskim</strong>, któremu zapisała dożywocie z zastrzeżeniem ochrony dóbr dla swojego syna <strong>Antoniego Mrokowskiego</strong>. Z kolei na skanie 183 (29 października 1700 r.) po wykonaniu przysięgi oczyszczającej przez Wojciecha i Marynę Kłotków w procesie o czary przeciw Marcinowi Chudzikowi sąd nałożył surowe <strong>wadium 120 grzywien</strong> pod karą <strong>banicji wiecznej i karą cielesną</strong>.
        </p>

        <h3>Rozdział XVIII: Wykup Roli po Kondupie, Śledztwo Krawca Dalmaczyka i Kontakty ze Wsią Budzyń</h3>
        <p>
          Listopadowe sesje ze skanów 185–200 ukazują również wieloetapowy proces <strong>Tomasza Zdeba</strong> z <strong>Andrzejem Pankiem</strong> o wykup ćwierci roli na Zarzeczu i Podlesiu po wuju Zdeba, Wojciechu Kondupie. Po urzędowej wizji burmistrza Adama Sokołowicza i ławnika Wojciecha Borkiewicza (skan 196, oszacowanie 30 młodych gruszek i jabłonki) Zdeb złożył przed sądem pełną sumę <strong>100 złp</strong> (50 + 50 złp, skan 200), żądając intromisji. Równolegle na skanach 191–195 i 199 toczyło się drobiazgowe śledztwo z powództwa krawca <strong>Wojciecha Dalmaczyka</strong> przeciw Janowi i Agnieszce Barankowicom o pieniądze jego córki Anny (zeznania m.in. Maryny Lubelszczanki o piciu miodu i Matyasza Zydaczyka o czterech groszach na kluski). Na skanie 197 woźny miejski <strong>Maciej Pełka</strong> zrelacjonował doręczenie pozwu do Sądu Zamkowego w Zamościu (w imieniu Anny z Gnińskich Zamoyskiej) z instancji burmistrza Wojciecha Grymałowskiego i Teresy z Janaszkowiców przeciw Żydowi Herszkowi, po czym Maciej i Agnieszka Pionowie sprzedali dom i ogród na Piasku Adamowi i Agnieszce Bielakom za 50 złp. Wreszcie zeznania ze skanów 198–200 dokumentują sprawę o białą spódnicę zastawioną za 15 zł u Żydówki Hesi, zatarg Wojciecha Dubaja z Żydem Abramem o konia za 14 zł oraz wątki z udziałem <strong>młynarza z Budzynia</strong> (skan 199).
        </p>

        <h3>Rozdział XIX: Intromisja Zdeba, Szpital Św. Ducha i Kwitacja Szlachecka Wolanowskich (skany 201–218)</h3>
        <p>
          Grudniowe protokoły z 1700 r. (fol. 97r–105v) przynoszą kulminację egzekucji majątkowych oraz rzadkie świadectwa relacji szlachecko-żydowskich i opieki szpitalnej. Dnia 4 grudnia 1700 r. (skany 204–205) burmistrz <strong>Adam Sokołowicz</strong>, ławnicy Wojciech Borkiewicz i Wawrzyniec Pielaszkowicz oraz pisarz Adam Michał Chmielowicz w asyście licznych sąsiadów dokonali uroczystej intromisji <strong>Tomasza Zdeba</strong> w ćwierć roli Kondupowską na Zarzeczu Podlesiu, wywołanej publicznie w czterech rogach gruntu przez sługę miejskiego Matyasza Mozielaka (<em>nemine impugnante</em>). Trzy dni później (7 XII 1700 r., skany 206–207) <strong>Katarzyna Kukiełkowa</strong>, wdowa po Wawrzyńcu Kukiełce mieszkająca jako <em>„Baba Szpitalna”</em> w Szpitalu św. Ducha, sprzedała w asyście opiekuna podwójciego Stanisława Jerzykiewicza dwie kwatery roli z chałupą, stodołą i ogrodem za <strong>200 złp</strong> (dwie raty po 100 złp) Tomaszowi Kopcowi i Mariannie z Jasieńskich. Z kolei 20 grudnia 1700 r. (skany 217–218) szlachcianka <strong>Konstancja z Zamiechowskich Wolanowska</strong>, wdowa po Franciszku Wolanowskim, wraz z synem <strong>Jakubem Wolanowskim</strong> stawili się dobrowolnie przed sądem miejskim (odstępując od własnego forum szlacheckiego) i własnoręcznymi podpisami pokwitowali Starszych Synagogi Kraśnickiej (<strong>Pinchasa Dawidowicza</strong> i <strong>Wigdora Markowicza</strong>) ze spłaty kapitału i prowizji powierzonych Bożnicy Kraśnickiej. Równolegle sesje z 13–23 grudnia ukazują surowe wyroki chłosty na zbiegłego z rękojmi Marcina Hapaka oraz chłopca pastucha (skan 215), zeznanie 20-letniego parobka Wojciecha z Borowa o mące ze młyna Józefa Wilka (skan 210), protestację burmistrza Szymatowskiego przeciw Starszym Synagogi (skan 207) oraz obdukcję krwawych ran i rabunku 15 złp na Żydzie <strong>Abusiu Jakubowiczu</strong> dokonanego przez Jana Rysiewicza z Wilkołaza po jarmarku w Urzędowie (skany 211–212).
        </p>

        <h3>Rozdział XX: Przemieszanie Składek Introligatorskich i Pełny Wyrok w Sprawie Roli Kondupowskiej (skany 219–225)</h3>
        <p>
          Analiza kodykologiczna skanów 219–225 (fol. 106r–109r) odsłania kolejne przemieszanie chronologiczne składek: bezpośrednio po wpisach z 23 grudnia 1700 r. introligator wszył składkę zawierającą pierwotną ustną propozycję <strong>Tomasza Zdeba</strong>, replikę <strong>Andrzeja Panka</strong> (powołującego się na objęcie gruntu po teściu <strong>Szymonie Wójciku</strong>) oraz pełne uzasadnienie i sentencję dekretu Sądu Obojnego Kraśnickiego w sporze o ćwierć roli Kondupowską, wraz z jego wykonaniem datowanym na <strong>24 listopada 1700 r.</strong> (skan 225). Wyrok rekonstruuje historię zadłużenia tej ćwierci aż od <strong>1690 r.</strong> (dług 50 złp zaciągnięty przez Wojciecha Kondupa u Brabanta, 10 złp kosztów i przejęcie roli przez Szymona Wójcika za 60 złp), nakazuje Zdebowi wypłatę <strong>100 złp</strong> (50 + 50 złp) za nakłady Panka i ustanawia wadium 100 złp pod rygorem banicji.
        </p>

        <h3>Rozdział XXI: Nowe Warstwy Chronologiczne: Składka z 1694 r. i Przejście do Lat 1730–1731 (skany 226–235)</h3>
        <p>
          Skany 226–250 (fol. 109v–122r) dokumentują wielowarstwową budowę kodeksu. Po zamknięciu sekwestru 100 złp w worku skórzanym i nakazu intromisji Tomasza Zdeba z 24–29 listopada 1700 r. (skany 226–228) introligator wszył trzy karty z <strong>1694 roku</strong> (skany 229–231, fol. 111r–112v). Odsłaniają one wcześniejszy skład władz miejskich za wójtostwa <strong>Ubaldiego Janaszkowicza</strong> (ławnicy Stefan Jerzykiewicz, Jan Majowski, Grzegorz Kłopotek, rajca Paweł Słomkowski) oraz wczesny spór wójta Janaszkowicza z malarzem <strong>Karolem Mrokowskim</strong> o zniesławienie na tablicy (14 VI 1694 r.). Bezpośrednio po nich (od skanu 232, fol. 113r) księga przechodzi do nowej epoki: saskich protokołów z lat <strong>1730–1731</strong> (z nagłówkiem <em>ANNUS NOVUS 1731</em> na skanie 234). Na czele władz miejskich stoją wówczas prezydent <strong>Szymon Jankowski</strong>, burmistrzowie <strong>Benedykt Szmatkowski</strong> i <strong>Maciej Ruszyński</strong> oraz wójt Gór i Podlesia <strong>Jan Jardzyk</strong>. Dramatycznym wątkiem przełomu 1730 i 1731 r. jest obdukcja i śledztwo z 22 XII 1730 – 10 I 1731 r. (skany 233–235) w sprawie zbrojnej napaści szlachcica z Urzędowa, syna Kazimierza Pikulskiego, na wracających saniami z Wieniawy burmistrza Szmatkowskiego, byłego burmistrza Jana Barankowicza, pannę Szydłowską i Żyda Abrama Szlomowicza pod Konopnicą.
        </p>

        <h3>Rozdział XXII: Pożar Kraśnika, Taksy Garderoby Szlachecko-Mieszczańskiej i Kredyt Żydowski w 1731 r. (skany 236–250)</h3>
        <p>
          Protokoły z stycznia i lutego 1731 r. dostarczają bezcennych realiów gospodarczych i społecznych miasta. Na skanie 238 wdowa <strong>Janowa Chudzikowa</strong> dochodziła komornego od Jana Malborskiego, ujawniając przy tym świadectwo niedawnego <strong>pożaru Kraśnika</strong> (<em>„podczas spalenia się Kraśnika nie mając się gdzie podzieć Boruch y z żoną swoją”</em> znalazł schronienie w jej chałupie), zaś na skanie 239 <strong>Augustyn Zbydniowicz</strong> <em>„budując się de novo”</em> uzyskał od rady miejskiej roczną wolniznę podatkową (1 rok i 6 niedziel). Szczególnym zabytkiem kultury materialnej jest urzędowa taksa garderoby z 25 stycznia 1731 r. (skany 246–247): dwa kontusze niebieskie z jedwabnymi potrzebami (Tomasza Tyrańskiego na 22 złp i Matyasza Latosłowicza na 19 złp), żupan granatowy (16 złp) i trzeci kontusz (18 złp). Równolegle wokanda zdominowana jest przez sprawy kredytowe żydowskich wierzycieli (Maryany, Mośka Rubinsteyna, Leybusia Ayzykowica, Lachmana Slomowicza, Judy Kowiena) z przysięgami w bóżnicy na Rodale oraz przez głośny proces <strong>Boruchowej Jaskowej</strong> przeciw zadłużonemu <strong>Wojciechowi Frankiewiczowi</strong> o pobicie nogą od stołka podczas sporu o zatrzymany kożuch, zakończony zasądzeniem 35 złp na ogrodzie, 10 złp nawiązki i 5 złp 18 gr dla cyrulika (skany 237, 242–246).
        </p>

        <h3>Rozdział XXIII: Sprawa Paserstwa u Maryanki, Szlacheckie Rękojmie i Spory Rynkowe Wiosną 1731 r. (skany 251–265)</h3>
        <p>
          Sesje z przełomu lutego i marca 1731 r. (fol. 122v–129v) odsłaniają rozległą sieć powiązań kredytowych i kryminalnych w Kraśniku. W sprawach szynkarza <strong>Lachmana Słomowicza</strong> z <strong>Kazimierzem Barankowiczem</strong> oraz <strong>Grzegorzem Kępką (Rępką)</strong> pojawia się rękojmia szlachecka urodzonych <strong>Andrzeja Błażejowskiego</strong> i <strong>Antoniego Janickiego</strong> na 25 złp oraz sprzeciw szafarza Jana Kidackiego wobec dopuszczania do przysięgi osoby podejrzanej o częste krzywoprzysięstwo (skany 251–252). Wokanda odnotowuje też głośną bójkę w gospodzie u <strong>Maryanki</strong> między <strong>Tomaszem Tyrańskim (Tyrawskim)</strong> a winiarzem <strong>Matyaszem Kopytkowiczem</strong> o zarzut kradzieży żupana, zakończoną podwójnym wyrokiem więzienia i 4 grzywnami kary (skany 258, 260), oraz wypadek na rynku, gdzie Żyd <strong>Zisman</strong> rzucił z górnego sklepu murowanego półkosek wprost na głowę żony Jana Radczka (skan 256). Kulminacją marca 1731 r. był wielowątkowy proces z powództwa <strong>Lejbusia Boruchowicza</strong> o kradzież kożuchów, spódnic, burek, koszul, płótna i siekier przez syna <strong>Marcinowej Pańkowej</strong>: sąd uznał Kopytkowicza i Antoniową za paserów (15 złp i 5 złp kary plus więzienie), rodzicom Pańkom nakazał ustąpić z chałupy za długi u młynarki podmiejskiej (46 złp i 40 złp), a na pokrycie roszczeń Boruchowicza i Maryanki zajął aresztem 30 złp długu <strong>Kazimierza Tokarczyka</strong> (skany 259, 263–265).
        </p>

        <h3>Rozdział XXIV: Podziały Spadkowe Przedmieszczan, Wolnizna Placowa i Intromisje z Kwietnia 1731 r. (skany 266–275)</h3>
        <p>
          Zapisy z końca marca i kwietnia 1731 r. (fol. 130r–134v) ukazują intensywny obrót nieruchomościami przedmiejskimi i sądownictwo obyczajowe. W dniu 28 III 1731 r. pełny skład magistratu (wójt <strong>Stanisław Wawrzyniec Pilaszkowicz</strong>, prezydent <strong>Szymon Szandrowicz</strong>, burmistrzowie <strong>Benedykt Szmatkowski</strong> i <strong>Szymon Marszałek</strong>, pisarz <strong>Andrzej Sadowski</strong>) dokonał intromisji ubogiego małżeństwa żydowskiego <strong>Chelmana Beniaszowicza</strong> i <strong>Ewy Zelmanowiczowej</strong> w pusty plac blisko furtki na Podlesiu za 15 złp na budowę izby (skan 267). Tego samego dnia oraz w kwietniu spisano szczegółowe komplanacje rodzinne: podział spadku po zmarłym <strong>Julianie</strong> między sześcioro dzieci (skany 268–269), kwitację <strong>Jakuba i Maryanny Łazarskich</strong> na 16 złp po rodzicach Sobestyanie i Katarzynie Brysiach (skan 262), zabezpieczenie długów i roli Olchowskiej przez <strong>Marcina Kępę</strong> dla dzieci z dwóch małżeństw (skan 272) oraz wieloetapową sprawę o dziedziczenie kwatery pola, chałupy i stodoły po bezpotomnym <strong>Stanisławie Wiatrku</strong> — zwieńczoną oszacowaniem na 60 złp, odjęciem 20 złp dożywocia i intromisją nabywcy <strong>Wojciecha Kozy</strong> przez woźnego Jana Ślusarczyka pod zieloną rózgą 25 IV 1731 r. (skany 270–271, 273–275). Wątek obyczajowy dopełnia kara woskowa do Kaplicy NMP Różańcowej i przeprosiny w cechu za awanturę o wstążkę między rodzinami <strong>Rokickich</strong> i <strong>Bogutów</strong> (skany 266–267) oraz skazanie <strong>Jana Chorążyńskiego</strong> na 4 złp 15 gr i dobrowolne więzienie za samosąd nad kozą Lewka Abramowicza (skany 270–271).
        </p>

        <h3>Rozdział XXV: Wyrok Śmierci na Wawrzyńca Pańka, Taksa Zbóż i Obrót Ogrodem Grymuzińskim (maj–czerwiec 1731 r., skany 276–287)</h3>
        <p>
          Wiosenne i wczesnoletnie protokoły z maja i czerwca 1731 r. (fol. 135r–140v) przynoszą zarówno spory majątkowe przedmieszczan, jak i najwyższy wymiar kary kryminalnej. Na skanie 276 rozliczono ogród Grymuziński ku Podlesiu (60 złp) między <strong>Augustynem Zdybiowiczem (Zdybem)</strong> a jego ojcem <strong>Andrzejem Zdybiowiczem</strong>, a na skanach 279–283 spisano podziały ogrodów i izby Ślusarowskiej przez wdowy po <strong>Bartłomieju Piaseckim</strong> i <strong>Pawle Pańsku</strong> (Agnieszka Jardzykowa zabezpieczyła 50 złp dla dzieci z pierwszego małżeństwa oraz dożywocie trzeciego męża Wawrzyńca Jardzyka). W sądownictwie karnym na uwagę zasługują grzywny miejskie i kościelne zasądzone od <strong>Mikołaja Biegaja</strong> i <strong>Stanisława Rejniaka</strong> (skany 278–280, m.in. po 2 grzywny na reparację murów i do kaplicy NMP) oraz przede wszystkim jednomyślny wyrok Sądu Obojnego, ławy i cechmistrzów z 20 VI 1731 r. (skan 287), skazujący recydywistę <strong>Wawrzyńca Pańka</strong> na powieszenie (<em>„aby był obwieszony”</em>) za wieloletnie kradzieże, trzykrotne ucieczki z łańcucha i groźby podpalenia. Tę samą kartę uzupełnia bezcenna taksa targowa zbóż z 25 VI 1731 r. (pszenica ozima po 9 złp, jara po 8 złp, żyto po 6 złp, groch po 9 złp, jęczmień i tatarka po 5 złp, owies po 3 złp) oraz urzędowa wycena zastawów odzieży Pani Gurowskiej dokonana przez krawca Wolfa Jaśkowicza (skan 286).
        </p>

        <h3>Rozdział XXVI: Oblata Pożyczki z Podpisem Hebrajskim, Tumult Jarmarczny z Dziadem Kościelnym i Ekspansja Rynkowa (lipiec–sierpień 1731 r., skany 288–300)</h3>
        <p>
          Lipiec i sierpień 1731 r. (fol. 141r–147r) ukazują złożone relacje wyznaniowe, gospodarcze i sąsiedzkie miasta. Na skanach 288–289 wpisano oblatę dokumentu z 1729 r., mocą którego <strong>Herszko Jakub Chaimowicz</strong> i <strong>Chaia Lachmanowiczówna</strong> za poręką syndyka synagogi <strong>Majera Moskowicza</strong> zaciągnęli 200 złp u ks. plebana na budowę domu w żydowskiem, opatrując akt oryginalnymi podpisami hebrajskimi. Tuż obok (skany 289–291) toczyła się sprawa z plenipotencji ks. proboszcza przez ks. <strong>Wawrzyńca Lednickiego</strong> o pobicie dziada kościelnego przez żydowskich kramarzy i piekarzy podczas niedzielnego jarmarku (11 sinych ran). Z kolei w sferze majątkowej odnotowano wykup dwóch łąk na Piaskach przez <strong>Wawrzyńca Jeśa</strong> po spłacie Rymarzów (skany 291–292), sprzedaż domku z ogródkiem za Bramą Lubelską naprzeciw kościoła św. Ducha przez Macieja Różyńskiego <strong>Maciejowi Latosłowiczowi</strong> i Katarzynie Piechowczance za 90 złp (skany 292–293) oraz sprzedaż placu Postrzygaczowskiego przy Bramie Krakowskiej przez Katarzynę Rabakową (Marcinową Kozinę) Janowi Jisiowi za 16 złp (skan 293). Ważnym świadectwem relacji dworsko-miejskich jest poręczenie pięciorga przedmieszczan za zbiegłego poddanego <strong>Jana Długockiego</strong> ze Słupkowic w dobrach dzierżawcy klucza wilkołaskiego Franciszka Sokołowskiego (skany 294–295), zaś serię zamykają krwawe obdukcje z sierpnia 1731 r. — w tym nocny napad na <strong>Manella Abramowicza</strong> z żoną przed kamienicą na rynku z rabunkiem 18 bitych talarów i 3 złp 6 gr (skan 300).
        </p>

        <h3>Rozdział XXVII: Przekłady Dekretów Rabinackich z Hebrajskiego (1726–1731), Dom Grymałowskich (2450 złp) i Kompromis na 2000 złp (skany 301–317)</h3>
        <p>
          Ostatnia część warstwy z 1731 r. (fol. 147v–155v) przynosi wyjątkowe źródła do historii gospodarczej i ustrojowej żydowskiej gminy kraśnickiej oraz wielkiego obrotu nieruchomościami. Na skanach 302–303 dokonano intromisji małżonków <strong>Ayzyka Herszkowicza</strong> i <strong>Rochli Dawidowiczówny</strong> w dom rogowy w Kraśniku ku Bramie Lubelskiej, sprzedany przez zmarłego <strong>Wojciecha Grymałowskiego</strong> i <strong>Teresę z Ubaldich</strong> z córką Katarzyną za wysoką sumę <strong>2450 złp</strong> (potwierdzoną kwitacją dorosłego syna Andrzeja Grymałowskiego w Trybunale Zamojskim). Jeszcze cenniejszym zabytkiem kancelaryjnym są dwa dosłowne przekłady z języka hebrajskiego na polski (<em>„z Chebrayskiego na Polski przetłumaczony de Verbo ad Verbum”</em>): dekret sądu rabinackiego z <strong>5 VII 486 r. [1726 r.]</strong> podpisany przez rabina Mojżesza, Wigdora Markowicza i Szymona Józefowicza z Lublina o przyznaniu ławki w synagodze <strong>Oszyi Moskowiczowi</strong> za utrzymanie sierot po Icku Dawidowiczu (skan 307) oraz kwitacja <strong>Judki Leybusia Chaimowicza</strong> na 930 złp sukcesji (skany 315–316). Dopełnia je kompromis na <strong>2000 złp</strong> między Berkiem Nachymowiczem a Szymonem Eliaszowiczem pod wadium 50 czerwonych złotych (skan 317), komplanacja Wawrzyńca Drąsia z czterema siostrami (skany 311–312) oraz kupno chałupy Stupskiego ze skarbu przez ławnika Franciszka Wietrzyckiego za 80 złp (skan 313).
        </p>

        <h3>Rozdział XXVIII: Warstwa z Lat 1753–1754 — Cechy Kraśnickie, Trybunał Zamojski i Śledztwo Obyczajowe Anny Jazdzikówny (skany 318–325)</h3>
        <p>
          Od skanu 318 (fol. 156r) księga przechodzi do nowej epoki chronologicznej — protokołów i inkwizycji z lat <strong>1753–1754</strong>. Cechy rzemieślnicze reprezentuje skarga starszego cechu kuśnierskiego i mistrza krawieckiego <strong>Walentego Kieprzyckiego</strong> przeciw towarzyszowi krawieckiemu Piotrowi Gołębiowskiemu o pobicie żony i wyrwanie sukna (skan 318) oraz komplanacja braci szewców <strong>Adama i Michała Łasoniaków</strong> na 25 złp przed rajcą Antonim Skórkowskim i ławnikiem Antonim Kuliczyńskim (skany 318–319). W wymiarze sądowym z 1753–1754 r. wyróżniają się: pozew <strong>Trybunału Zamojskiego</strong> dla burmistrza <strong>Łukasza Krzeszowskiego</strong> i wójta Banaczowskiego przeciw apelantowi (skan 321), rewizja domowa <em>de furto</em> u ławnika Szymona Krzeszowskiego oraz przesłuchania w sprawie podejrzanych zakupów odzieży od chłopa (skany 322–323). Szczególnie barwnym świadectwem obyczajowości mieszczańskiej jest śledztwo z listopada–grudnia 1753 r. w sprawie <em>de crimine delicti</em> (cudzołóstwa) <strong>Anny Jazdzikówny</strong> z <strong>Grzegorzem Pitaszkiewiczem</strong> (skany 324–325), ujawniające rolę włożenia czepca, schadzek w sadzie i w gospodzie Żydówki Bralowej oraz zeznań sąsiedzkich, a także grudniowa kłótnia w gospodzie Aleksego Bujarskiego z wymianą zdań po łacinie (skan 325).
        </p>


        <h3>Rozdział XXIX: Kryzys w Cechu Tkackim 1754 r. oraz Dekrety Chłosty i Wyświecenia (skany 326–340)</h3>
        <p>
          Kolejna partia protokołów z przełomu 1753 i 1754 r. (fol. 160r–167r) odsłania gwałtowny rozłam wewnątrz <strong>cechu tkackiego</strong>. Podczas sesji 2 stycznia 1754 r. (skany 328–333) wokół wyzwolin Jakuba, syna <strong>Wawrzyńca Wróbla</strong>, doszło do otwartego buntu mistrza <strong>Marcina Morela</strong> przeciwko burmistrzowi i cechmistrzowi <strong>Łukaszowi Krzeszowskiemu</strong> oraz wicecechmistrzowi <strong>Antoniemu Łatosiewiczowi</strong> (spory o „dwa talary bite”, sprzedaż płótna chłopom i wyrób płótna przez kobiety za 8 złp na skanie 343, w tym ostre słowa pod adresem prawa cechowego). Równolegle sąd wójtowsko-ławniczy na podstawie prawa brandenburskiego wydawał surowe wyroki w sprawach obyczajowych: 29 XI 1753 r. <strong>Jakubowa Krasowska</strong> i <strong>Szymon Wójcik</strong> zostali skazani na 200 i 100 plag oraz wyświecenie z miasta i leżenie krzyżem w kościele (skany 327–328), a 9 IV 1754 r. <strong>Jan Mech</strong> i <strong>Marianna Zdybkówna</strong> — na 200 plag i wyświecenie (skan 335). Wśród spraw majątkowych wyróżnia się rozliczenie po zmarłym w Zamościu <strong>Augustynie Piotrowskim</strong>, pochowanym sumptem tamtejszego ślusarza (skany 339–340).
        </p>

        <h3>Rozdział XXX: Suplika Pospólstwa, Garnizon Koronny i Konflikty o Areszt Miejski w 1754 r. (skany 341–350)</h3>
        <p>
          Skany 341–350 (fol. 167v–172r) przynoszą bezcenne źródła do relacji miasta z dominium i wojskiem koronnym. Na karcie 167v (skan 341) znajduje się unikatowy wpis odwrócony o 180° — uroczysta <strong>suplika Miasta z Pospólstwem Kraśnickim</strong> do Jaśnie Wielmożnego Pana i Dobrodzieja o uwolnienie od niezwyczajnych robocizn i podwód wobec upadku bydła. Z kolei protokoły z kwietnia–października 1754 r. dokumentują napięcia z kadrą wojskową: 15 IV 1754 r. na instancję porucznika infanterii buławy wielkiej koronnej <strong>Piotra Gomulińskiego</strong> przesłuchano świadków w sprawie groźby spalenia domostwa przez Adama Radłę (skan 342), a wójt i sędzia kraśnicki <strong>Szymon Marczukowski</strong> wniósł skargę przeciw podchorążemu <strong>Skowrońskiemu</strong>, którego żołnierze w gospodzie Żydówki Kali grozili odcięciem kłódki i uwolnieniem więźniów z aresztu (skan 350). Obraz życia codziennego uzupełniają dochodzenia w sprawie bójki u Żyda Welusia w obecności burmistrza Krzeszowskiego i Pana Prezydenta (skan 349) oraz sprawa Marianny Tkaczykówny przeciw malarzowi i kucharzowi (skan 348).
        </p>


        <h3>Rozdział XXXI: Napaść Żołnierzy na Wójta Marczukowskiego, Kontrakty Lubelskie i Proces Spadkowy Piotrowczyków (skany 351–363)</h3>
        <p>
          Pierwsza część skanów z jesieni 1754 r. (fol. 172v–178v) ukazuje dramatyczną eskalację konfliktu z wojskiem koronnym: w gospodzie Żydówki Kali jeden z żołnierzy podchorążego <strong>Skowrońskiego</strong> dobył pałasza i uderzył wójta <strong>Szymona Marczukowskiego</strong> w plecy, gdy ten odmówił wydania kluczy do aresztantów osadzonych z woli ks. Proboszcza (skany 351–352), a inny świadek ujawnił najście żołnierzy na komorę u Żyda Dawidka (skan 353). W sprawach majątkowych na uwagę zasługują: proces o handel śliwkami w sadzie Adama Radła z udziałem Katarzyny Mnichowskiej i Mikołaja Kutka z Turobina (skany 354–356), ujawnienie rozmów rajcy Szymona Szankiewicza (podającego się za Wielkopolanina) z kapitanem Gomulińskim w Lublinie o stancji przy dworze kolarzów (skan 360) oraz pięcioświadkowe śledztwo z 25 X 1754 r. w sporze spadkowym <strong>Matyasza Piotrowczyka</strong> przeciw Antoniemu Pankowi i macosze z domu Zdybów o testament ojca Augustyna (skany 358–359, 361).
        </p>

        <h3>Rozdział XXXII: Cech Szewski, Rewizje Domowe i Ugody Grudniowe 1754 r. (skany 364–375)</h3>
        <p>
          Zamykająca rok 1754 partia protokołów (fol. 179r–184v) dokumentuje zarówno ostre spory sąsiedzkie (wielowątkowe procesy rodzin Wróblów i Bryszkiewiczów na skanach 363–368 oraz rozliczenie 23 snopków jęczmienia odnalezionych w komorze Grzegorza Jurdzika na skanach 372–374), jak i dyscyplinę wewnątrzcechową oraz międzygrupową. 26 XI 1754 r. mistrz szewski <strong>Szymon Zajowski</strong> złożył manifestację przeciw cechmistrzowi <strong>Wojciechowi Potokowiczowi</strong> o pobicie za uwagę o wosku na świece (skan 368), a szewc <strong>Antoni Okoń</strong> wyjednał urzędową wizję swojego domu przez ławnika Szaliczyńskiego i pisarza Michała Krzyżanowskiego celem oczyszczenia żony z zarzutu kradzieży płótna (skan 370). Grudniowe sesje z 2–13 XII 1754 r. przyniosły wyrok na Jana Tokarczyka za zabranie worków poddanemu z Wilkołaza Stanisławowi Rzepce (skan 371), nakaz dopłaty 5 złp przez Jana Wiaterka bratu Wojciechowi (skany 374–375) oraz przyjacielską ugodę rodzonych braci <strong>Łukasza i Wojciecha Pełków</strong> (skany 371–372, 375).
        </p>


        <h3>Rozdział XXXIII: Otwarcie Akt Roku 1755 — Prowizja Szlachecka, Procesy Marcina Morela i Sprawa Szlachectwa Przesławskiego (skany 376–391)</h3>
        <p>
          Przełom lat 1754 i 1755 (fol. 185r–192v) przynosi ważne wyroki finansowe oraz eskalację konfliktów wewnątrzmiejskich. W dniu 20 XII 1754 r. (skany 376–377) sąd rozstrzygnął sprawę starozakonnego <strong>Hajka Lejzorowicza</strong> przeciw przedmieszczaninowi <strong>Janowi Łysemu</strong> o dług z 1741 r., wyliczając od kapitału 24 złp 15 gr trzynastoletnią prowizję szlachecką na 28 złp 15 gr (łącznie z 5 złp dawnego długu 55 złp, rozłożone na trzy raty w 1755 r.), a w wigilię Bożego Narodzenia 24 XII 1754 r. (skany 377–378) odnotowano obdukcję <strong>Agnieszki i Wojciecha Busiów</strong> pobitych przez dyrektora podstarościego na cmentarzu w drodze na jarmark na Nowy Kazimierz pod Lublin. Od skanu 378 (<strong>3 stycznia 1755 r.</strong>) księga otwiera nowy rok sądowy serią inkwizycji z udziałem mistrza <strong>Marcina Morela</strong>: spory o zakup wieprzków przed domem Żydówki Sary i Lejbusia Struskiego oraz o zbłąkanego ślepego konia z Andrzejem Kraskowskim (skany 378–384), oskarżenie żony rajcy Łukasza Krzeszowskiego o żydowskie pochodzenie (skany 380–381), zeznania w sprawie szlachectwa i metryki <strong>Jana Przesławskiego</strong> przed szlachetnym <strong>Józefem Cynewskim</strong> (skan 384), a także drastyczną obrazę całego urzędu kraśnickiego i żony ławnika Szaliczyńskiego (skany 385–386) oraz skargi na wyganianie braci cechowych z potoku do skrobania gnoju mimo wyprawy skór do trzech folwarków (skany 390–391).
        </p>

        <h3>Rozdział XXXIV: Bójka Taneczna u Żyda Dawida (Grzegorz Pilaszkiewicz vs Koza i Mikołajczyk) oraz Spór Cechmistrza Szankiewicza z Kawczyną (skany 392–400)</h3>
        <p>
          Wiosenno-letnie sesje z 1755 r. (fol. 193r–196v, z dokładnym dubletem mikrofilmowym karty 193r na skanie 393) koncentrują się wokół głośnej, wieloświadkowej bójki w gospodzie niewiernego <strong>Dawida</strong> z 13–23 V 1755 r. (skany 392–399). Spór o taniec ze ślusarczanką pomiędzy młodzianem <strong>Michałem Mikołajczykiem</strong> a <strong>Stanisławem Pilaszkiewiczem</strong> (który miał twierdzić „jestem szlachcic, a ty chłop”) przerodził się w krwawe starcie, w którym <strong>Grzegorz Pilaszkiewicz</strong> wraz z żoną i synami Stanisławem oraz Wawrzyńcem pobili Mikołajczyka i jego towarzysza <strong>Józefa Kozę</strong>, nim interweniował tokarz <strong>Łukasz ze Stróży</strong> i kowal <strong>Wojciech Pankowski</strong>. Z kolei na skanach 399–400 (18 VI 1755 r.) rajca i cechmistrz krawiecki <strong>Szymon Szankiewicz</strong> oraz brat cechowy <strong>Piotr Gołembiowski</strong> opisali wtargnięcie <strong>Mikołajowej Kawczyny</strong> do domu cechmistrza w czasie jarmarku św. Antoniego, gdzie oskarżała ona komornicę Bednarkę o kradzież spódnicy, rzuciła garnkiem barszczu pod nogi rajcy i dopuściła się obscenicznej zniewagi.
        </p>

        <h3>Rozdział XXXV: Spory o Jęczmień, Bójka u Żyda Izraela na Motkowym oraz Śledztwo Ławników o Dwie Szkatuły i Wosk (skany 401–414)</h3>
        <p>
          Druga połowa 1755 r. (fol. 197r–203v) dokumentuje intensywną serię inkwizycji gospodarczych, obyczajowych i urzędowych. Po dokończeniu zeznań w sprawie Kawczyny z Szankiewiczem (28 VI 1755 r., skan 401) sąd rozpatrzył skargę <strong>Jana Przesławskiego</strong> przeciw <strong>Józefowi Putkowi</strong> o spasienie jęczmienia i zniknięcie zboża w stodole ojca <strong>Maryannowej Latosiewiczowej</strong>, zakończoną ugodą zawartą w gospodzie przy <strong>Antonim Pilaszkiewiczu</strong> na 1 złp 27 gr oraz ćwierć żyta (skany 401–403). Równolegle 9 VII 1755 r. rozgorzała sprawa pobicia grabarza <strong>Franciszka Choteckiego</strong> przez <strong>Tomasza Pilaszkiewicza</strong> w gospodzie niewiernego <strong>Izraela</strong> na Motkowym, gdzie interweniowała <strong>Żydówka Motkowa</strong> słowami „pódźcie bronić to katolik”, a burmistrz i cyrulik <strong>Grzegorz Pilaszkiewicz</strong> sam wymierzył synowi dwa policzki i wygnał go z gospody (skany 403–405, 408–409). W lipcu i sierpniu odnotowano też sprawę <strong>Wawrzyńca Tokarczyka</strong> oskarżanego przez żonę o bicie (skany 405–406), zatarg <strong>Sebastiana Zdyblika</strong> z <strong>Michałem Mikołajczykiem</strong> i komornicą Zofiją u Żydówki Heleny (skany 406–407) oraz rozliczenia <strong>Bartłomieja Zdyba</strong> z braćmi <strong>Posuniakami</strong> o 40 złp i 24 złp pożyczki od <strong>Józefa Gąski</strong> na pogrzeb matki (skany 409–411). Jesienią (31 X – 18 XI 1755 r., skany 411–414) rozwinął się głośny proces między ławnikami <strong>Szymonem Krzeszowskim</strong> a <strong>Janem Szubertowskim</strong> o dwie szkatuły (zieloną i czerwoną), zdeptane 12 snopów na niwie, siedem skradzionych kur oraz rewizję w skrzynce matki <strong>Małgorzaty Krzeszowskiej</strong> u <strong>Antoniego Zdyblika</strong>, w której znaleziono trzy kawałki wosku od <strong>Boguciny</strong>.
        </p>

        <h3>Rozdział XXXVI: Otwarcie Roku 1756 — Kryzys Władzy Cechmistrza Kazimierza Młynarskiego i Manifestacje Szlachty oraz Przedmieszczan (skany 415–425)</h3>
        <p>
          Na karcie 204r (skan 415) księga otwiera warstwę z <strong>roku 1756</strong> serią gwałtownych manifestacji i protestacji ukazujących głębokie napięcia w elicie miejskiej. Cechmistrz szewski <strong>Kazimierz Młynarski</strong> został pozwany zarówno przez nieznanego z imienia manifestanta, jak i przez ławnika <strong>Szymona Krzeszowskiego</strong> (skany 415–418) za zniewagę sądu wójtowskiego („nie masz Pana Boga, ponieważ P. Wójt schował”), nieprzyjęcie apelacji do Trybunału Zamojskiego, osadzenie pod posłuszeństwem w wieży miejskiej oraz trzaskanie drzwiami w izbie sądowej; osobno Młynarski sam protestował przeciw ławnikowi <strong>Janowi Lubartowskiemu</strong> za spoliczkowanie w gospodzie (skany 422–423). Na skanach 419–422 wpisano dwie protestacje szlacheckie: <strong>Adam Marcinkowski</strong> skarżył ławnika <strong>Adama Zandla</strong> i <strong>Krzysztofa Pilaszkiewicza</strong> o rugowanie ze stancji, zjedzenie obroku przez świnie i spór o zagubiony fartuch, natomiast bracia <strong>Jędrzej i Samuel Kofeccy</strong> oskarżyli wójta <strong>Michała Krzywińskiego</strong> o dwukrotne pobicie Samuela w obecności <strong>Marcina Morela</strong> i <strong>Walentego Forgieła</strong>, przymuszenie do ucieczki i zakaz rozmowy z manifestantami pod klątwą, mimo ugody na 24 złp. Całość Partii 17 zamykają manifestacja burmistrza <strong>Jana Pilaszkiewicza</strong> przeciw rezydentowi <strong>Łukaszowi Krzeszowskiemu</strong> o nieoddanie rezydencji miejskiej (listopad 1756 r., skan 423) oraz spory przedmieszczanina <strong>Wojciecha Cwieki</strong> z <strong>Łukaszem Pałką</strong> o miedzę i z deputatem <strong>Marcinem Morelem</strong> o pomówienie o zabójstwo <strong>Antoniego Maruszkiewicza</strong> (skany 418–419, 424–425).
        </p>

        <h3>Rozdział XXXVII: Pozwy Trybunału Zamojskiego, Sprawy Poddanych z Rzeczycy i Spory Przedmiejskie w Listopadzie 1756 r. (skany 426–438)</h3>
        <p>
          Listopadowe sesje z 1756 r. (fol. 209v–215v) przynoszą obfity materiał apelacyjny i międzyjurysdykcyjny. Woźny przysięgły kraśnicki <strong>Andrzej Surowiak</strong> wpisał do księgi w dniu 10 XI 1756 r. dwa pełne tenory pozwów przed <strong>Najwyższy Trybunał Zamoyski</strong> wystawionych w imieniu Opiekunów Ordynacji Zamojskiej (<strong>Jana Jakuba Zamoyskiego</strong>, dziekana infułata zamojskiego <strong>Jana Aleksandra Trembińskiego</strong>, <strong>Franciszka Dzierżanowskiego</strong> oraz starosty lubelskiego <strong>Józefa Klemensa Zamoyskiego</strong>): pierwszy na instancję <strong>Wojciecha Cwieki</strong> przeciw <strong>Łukaszowi Pałce</strong> o niewykonanie dekretu i zniewagę przy szwagrze <strong>Marcinie Morelu</strong> (skany 431–433), drugi na instancję braci <strong>Jędrzeja i Samuela Kofeckich</strong> przeciw wójtowi <strong>Michałowi Krzywińskiemu</strong> o dług, wygnanie z posesji i pobicie (skany 433–435). Równolegle na skanach 427–429 rozpatrzono obdukcję i wyrok w sprawie poddanego ze wsi <strong>Rzeczycy</strong> (dóbr skarbnika <strong>Suchodolskiego</strong>) <strong>Macieja Chorąbały</strong>, pobitego w lesie przez dwóch ludzi i pozbawionego siekier przez <strong>Wawrzyńca Antoszczuka</strong> oraz <strong>Wojciecha Kawkę</strong> (uwolnionego przysięgą od bicia, lecz skazanego na zwrot siekiery i grzywny). Ponadto odnotowano protestację <strong>Antoniego Urbańskiego</strong> przeciw <strong>Józefowi Gąsce</strong> o przyjęcie na świadka jego szwagra <strong>Marcina Budzyńskiego</strong> (skan 428), skargę <strong>Mikołaja i Józefa Nowaków</strong> na pobicie przez <strong>Pawła Frugę</strong> i jego syna (skany 429–430) oraz serię remanifestacji między braćmi Kofeckimi a wójtem Krzywińskim, Marcinem Morelem i <strong>Walentym Jorgiełem</strong> (skany 435–438).
        </p>

        <h3>Rozdział XXXVIII: Sprawa Kramarki Rosołowskiej, Napięcia w Magistracie, Zastaw Klina Wróbla i Ugoda Kofeckich (skany 439–450)</h3>
        <p>
          Druga połowa listopada 1756 r. (fol. 216r–221v) ukazuje zarówno ochronę ubogich mieszczanek przed samowolą kupiecką, jak i ostre tarcia w łonie samego magistratu kraśnickiego. W dniu św. Marcina (11 XI 1756 r., skany 439, 442–445) sąd ukarał <strong>Sebastiana Sedelskiego</strong> karą 3 grzywien sądowych oraz zwrotem zrabowanego towaru na rzecz ubogiej wdowy i kramarki <strong>Janowej Rosołowskiej</strong>, której kram rozbił przed pierwszą mszą, a dziecko kopnął nogą, co poświadczyła szlachetna <strong>Zofija Chrzanowska</strong>; cztery dni później (15 XI, skan 445) kramarze <strong>Jan Gronczewski</strong>, Sedelski i <strong>Adam Konowski</strong> manifestowali się przeciw <strong>Wojciechowi Potokowiczowi</strong> o wypędzenie z gospody. W samym magistracie ławnik <strong>Antoni Szaliczyński</strong> pozwał mistrza szewskiego <strong>Antoniego Okonia</strong> za napaść w gospodzie (skany 439–440), burmistrz <strong>Łukasz Krzeszowski</strong> skarżył <strong>Grzegorza Pilaszkiewicza</strong> o przetrzymywanie rezydencji dla pisarza zamojskiego (skany 440–441), a burmistrz <strong>Stanisław Pruszkiewicz</strong> manifestował się przeciw wójtowi <strong>Michałowi Krzywińskiemu</strong> za publiczne nazwanie go w gospodzie „pisarzem i praktykarzem żydowskim” (skany 441–442). Z kolei 24–29 XI 1756 r. wpisano obdukcję <strong>Jakuba Grzybka</strong> pobitego na miedzy przez poddanego z Janowa <strong>Wawrzyńca Jazdyka</strong> spod jurysdykcji kanoników regularnych (skany 445–446), własnoręczną kwitację <strong>Jędrzeja Kofeckiego</strong> dla wójta Krzywińskiego (skan 446), obligację <strong>Jakuba Wróbla</strong> dla sługi kościelnego <strong>Wawrzyńca Biegaja</strong> na 16 złp pod zastaw półtora sznura klina Tokarskiego (skan 447) oraz finalną ugodę braci Kofeckich z Morelem i Jorgiełem przez przyjaciół (burmistrzów Pruszkiewicza i Krzeszowskiego oraz ławnika Tokarczyka) na 4 złp (skany 447–450).
        </p>

        <h3>Rozdział XXXIX: Grudzień 1756 r. — Uniwersał Starosty Zamoyskiego o Szynku Miodnym, Wyrok za Granie na Weselu Żydowskim i Kwitacja Hebrajska (skany 451–463)</h3>
        <p>
          Grudniowe sesje z 1756 r. (fol. 222r–227v, z dokładnym dubletem mikrofilmowym karty 222v na skanie 453) otwiera podpisanie ugody przez braci <strong>Samuela i Jędrzeja Kofeckich</strong> (1 XII 1756 r., skan 451), po czym następuje seria dekretów porządkowych i aktów normatywnych o wyjątkowej doniosłości ustrojowej. W dniu 4 XII 1756 r. (skan 454) sąd na rekwizycję <strong>Kustosza kościoła kraśnickiego</strong> skazał <strong>Pawła Kacperskiego</strong> (syna Augustyna) na 4 grzywny na rzecz Najświętszej Panny Różańcowej oraz karę kruchty za to, że wbrew zakazowi ogłaszanemu z ambony nie tylko patrzył, ale i grał na weselu żydowskim, nie słuchając przestróg własnej matki. Bezpośrednio po tym wpisano na karcie 223v (skan 455) oryginalny <strong>Uniwersał starosty lubelskiego Józefa Klemensa Zamoyskiego</strong> wydany w Zwierzyńcu 30 XI 1756 r., zakazujący Żydom kraśnickim kupowania miodów przaśnych poza dyspozycją ekonoma Ordynacji Zamojskiej <strong>Morszkowskiego</strong>, oraz zastrzeżenie dawnego rajcy <strong>Antoniego Tokarza</strong> w sprawie testamentu ojca <strong>Wojciecha Tokarza</strong>. Na skanie 456 odnotowano kwitację <strong>Herszka Eliaszowicza</strong> (z własnoręcznym podpisem w alfabecie hebrajskim) i Antoniego Sandowskiego dla Mikołaja Nowaka, na skanach 457–462 serię dylacji, aresztów i wyroków (m.in. oczyszczenie przysięgą <strong>Antoniego Kołtona</strong> przeciw burmistrzowi <strong>Grzegorzowi Pilaszkiewiczowi</strong> o 14 złp oraz wyrok na <strong>Wojciecha Stachowicza</strong> za odkupywanie wołów <strong>Adama Posuniaka</strong>), a na skanie 463 (15 XII 1756 r.) dobrowolną konfesatę <strong>Sebastiana Wojciechowskiego</strong> ze sprzedaży kradzionego owsa i grochu.
        </p>

        <h3>Rozdział XL: Otwarcie Działu Inkwizycji (7 XII 1756 r.), Bójka o Śliwki w Sadzie Morela, Zamiana Domostw Wójta Krzywińskiego i Sprawa Rzeźników (skany 464–475)</h3>
        <p>
          Od karty 228r (skan 464, <strong>7 grudnia 1756 r.</strong>) rozpoczyna się w woluminie nowy dział zatytułowany <em>Incipiuntur Acta Inquisitionum ac Delationum</em>, obejmujący drobiazgowe przesłuchania świadków z listopada i grudnia 1756 r. (fol. 228r–233v). Obok zeznań w sporze <strong>Łukasza Pałki</strong> z <strong>Wojciechem Cwieką</strong> o 40 snopów pszenicy i ćwierć panieńską (zeznania <strong>Katarzyny Grzybczyny</strong>, <strong>Wojciecha Pałki</strong>, <strong>Mikołaja Nowaka</strong> i służącej <strong>Marianny Gąsiorowczanki</strong>, skany 464–466, 473) oraz zajścia <strong>Kazimierza Młynarskiego</strong> z <strong>Janem Lubartowskim</strong>, wpisano wieloświadkową inkwizycję w sprawie <strong>Marcina Morela</strong> przeciw <strong>Samuelowi Kofeckiemu</strong> (skany 466–469), w której <strong>Grzegorz Jazdyk</strong>, <strong>Antoniowa Bojarska</strong> i <strong>Jan Szubertowski</strong> opisali wtargnięcie Kofeckiego do sadu po śliwki, kopnięcie <strong>Marcinowej Morelowej</strong> (pozostawiające siniak na trzy cale) i interwencję <strong>Walentego Jorgieła</strong>. Na skanach 469–470 świadkowie <strong>Agnieszka Wysolińska</strong>, <strong>Jakub Szafrański</strong> i <strong>Janowa Gronczewska</strong> przedstawili kulisy bójki kramarki <strong>Janowej Rosołowskiej</strong> z <strong>Sebastianem Sedelskim</strong>, a na skanach 470–471 wpisano kontrakt wieczystej zamiany domostw (<em>per commutationem</em>) na podsieniu między wójtem <strong>Michałem Ignacym Krzywińskim</strong> a <strong>Michałem Matuszkiewiczem</strong> za dopłatą 80 złp. Całość Partii 19 wieńczą wizja na podkopanym gruncie wdowy <strong>Katarzyny Gronczyny</strong> przez <strong>Wawrzyńca Jazdyka</strong>, inkwizycja rzeźnika <strong>Joela Lejzorowicza</strong> o zapowietrzone bydło w lesie borzechowskim (skan 472) oraz zeznania <strong>Wojciecha Potokowicza</strong>, <strong>Wojciecha Pankiewicza</strong> i <strong>Grzegorzowej Latosiewiczowej</strong> o kłótniach w rodzinie Pilaszkiewiczów i oskarżeniu Antoniego Kołtona (skany 474–475).
        </p>

        <h3>Rozdział XLI: Śledztwa z Grudnia 1756 r. – Spory Pałki z Cwieką, Sukcesja Mydła i Konflikt Cechmistrzów Szewskich z Posuniakami (skany 476–494)</h3>
        <p>
          W drugiej połowie grudnia 1756 r. (fol. 233v–241v) dział inkwizycji i delacji wypełniają gęste przesłuchania w kilku równoległych sporach miejskich i przedmiejskich. W sprawie <strong>Łukasza Pałki</strong> przeciw <strong>Wojciechowi Cwiece</strong> zeznają m.in. <strong>Teresa Tryzakowa</strong>, <strong>Marianna Szymonowiczowa</strong>, niewierne <strong>Litwinowa</strong> i krawcowa <strong>Ilkowa</strong> (o sprzedaż brenny), <strong>Matyasz Łapka</strong>, <strong>Jakub Bielenicki</strong>, <strong>Krzysztof Wójcik</strong> oraz <strong>Matyasz Fruga</strong>, przybliżając kulisy podróży i dokumentów z Zamościa (skany 477–481, 484–486). Równolegle toczy się proces o pobicie w gospodzie wytoczony przez <strong>Mikołaja Nowaka</strong> przeciw <strong>Maciejowi Frugie</strong> (zeznania <strong>Bartłomieja Kilianka</strong>, młodziana <strong>Wojciecha Wiatrka</strong> i ławnika <strong>Wawrzyńca Kochania</strong> z 17 XII 1756 r., skany 480–482) oraz sprawa <strong>Wojciecha Pałki</strong> przeciw <strong>Mikołajowi Nowakowi</strong> o sukcesję po <strong>Stanisławie Mydle</strong> (24 i 30 złp), zakończona ugodą na 10 złp poświadczoną przez <strong>Jana Kobę</strong>, <strong>Bartłomieja Zdyba</strong> i <strong>Józefa Mazura</strong> (skany 483–484, 487–488). Od skanu 486 narasta ostry zatarg z <strong>Adamem Posuniakiem</strong> (oskarżanym przez <strong>Wojciecha Stachowicza</strong> o skóry wołowe i mieszanie jurysdykcji dworskiej), który 27–28 XII 1756 r. wybucha gwałtowną bójką w gospodzie między braćmi <strong>Adamem</strong>, <strong>Michałem</strong> i <strong>Wawrzyńcem Posuniakami</strong> a cechmistrzami szewskimi <strong>Kazimierzem Młynarskim</strong> i <strong>Antonim Okoniem</strong> (obdukcje podartego zielonego kontusza Młynarskiego oraz zeznania <strong>Antoniego Dudka</strong> i <strong>Szymona Nowackiego</strong>, skany 489–494). Ponadto w toku mikrofilmowania karty 234v i 237r zostały powtórnie sfotografowane jako dublety (skany 479 i 485).
        </p>

        <h3>Rozdział XLII: Wyroki, Areszty i Manifestacje Apelacyjne do Trybunału Zamojskiego (skany 495–500)</h3>
        <p>
          Ostatnie karty Partii 20 (fol. 242r–244v) przynoszą serię dekretów, dylacji, aresztów i uroczystych manifestacji. W wyroku z <strong>18 grudnia 1756 r.</strong> sąd rozstrzyga sprawę <strong>Wojciecha Cwieki</strong> przeciw <strong>Mikołajowi Nowakowi</strong> (odrzucenie przysięgi, pijaństwo w chwili obelgi, grzywny i deprekacja, skany 495–496). Na skanach 489 i 496–498 rozgrywa się spór o sukcesję Rogozowską (rolę po zmarłym <strong>Janie Gąsce</strong>) między opiekunami jego dzieci pod przewodem <strong>Piotra Kilianka</strong> a <strong>Janem Czelejem</strong>. Zapisano również areszt <strong>Samuela Kofeckiego</strong> na 37 złp z ogrodu <strong>Szymona Krzeszowskiego</strong> i <strong>Jana Przesławskiego</strong> (skany 491–492), dylację <strong>Adama Kochanowskiego</strong> przeciw <strong>Janowi Wiatrowskiemu</strong> oraz ławnika <strong>Jana Lubartowskiego</strong> przeciw <strong>Augustynowi Piaseckiemu</strong> o zginione zboże (skan 499). Całość wieńczą manifestacja <strong>Stanisława Wójcika</strong> przeciw <strong>Marcinowi Morelowi</strong> z 19 XII 1756 r. o przewlekanie apelacji do <strong>Trybunału Zamojskiego</strong> oraz trzy kolejne manifestacje <strong>Łukasza Pałki</strong> przeciw <strong>Wojciechowi Cwiece</strong> po dekrecie Trybunału (skany 498–500).
        </p>

        <h3>Rozdział XLIII: Pożar Młyna Grebieńskiego, Walka o Jurysdykcję Dworską i Konflikty Władz Miejskich (skany 501–515)</h3>
        <p>
          W księdze od karty 245r (skan 501) pisarz wprowadza datację roku <strong>1757</strong> (<em>Actum In Officio Composito Jurato Crasn. Fra 6ta Ante Festum S. Thomae Apostoli proxima 1757 Anno</em>), dokumentując serię dramatycznych konfliktów miejskich. Wśród samych urzędników wybucha spór ławnika <strong>Antoniego Lubrzyńskiego</strong> z cechmistrzem szewskim <strong>Kazimierzem Młynarskim</strong> o rzekome spalenie ekstraktu dekretu (rozstrzygnięty w obecności ławnika <strong>Szymona Krzeszowskiego</strong> wyrokiem nakazującym Lubrzyńskiemu grzywny i deprekację, skany 501, 507–508), a także zderzenie wójta <strong>Michała Krzywińskiego</strong> z <strong>Wawrzyńcem Starobratem</strong> (o kiwanie laską w domu sądowym i spory majątkowe z ojczymem <strong>Mikołajem Nowakiem</strong>, skany 502–505). Centralnym wydarzeniem obyczajowo-gospodarczym jest katastrofa <strong>Młyna Grebieńskiego</strong>: najpierw <strong>Józef Radkowski</strong> oskarża o groźby podpalenia <strong>Bartłomieja Czeleja</strong> (skany 506–507), a następnie młynarczyk <strong>Wojciech Świdziński</strong> składa dramatyczne zeznanie pod sumieniem, opisując, jak pijany Żyd piekarz rozpalił nocą głownię w młynie, zatrzasnął drzwi i zgubił klucze, doprowadzając do całkowitego spalenia młyna (skany 510–511). Równolegle cech szewski wstrząsa ostry konflikt <strong>Wojciecha Stachowicza</strong> z <strong>Adamem Posuniakiem</strong> o podkupienie 4 skór wołowych u <strong>Wojciecha Kozy</strong> oraz o złamanie prawa magdeburskiego i przywilejów fundatorów miasta poprzez apelowanie do <strong>dworu stróżkiego</strong> i sprowadzenie służby dworskiej (skany 501, 511, 513–515). Odnotowano także obdukcję <strong>Józefowej Kozyny</strong> pobitej przez <strong>Stanisława Kowalika</strong> (skan 512) oraz dublet mikrofilmowy karty 245v (skan 503 powtarzający skan 502).
        </p>

        <h3>Rozdział XLIV: Sukcesje, Zastawy Wielopokoleniowe i Mandaty Ordynacji Zamoyskiej (skany 516–525)</h3>
        <p>
          Kolejne karty woluminu (fol. 252r–255v, z omyłkową foliacją 256 na skanie 524 poprawioną na 255v na skanie 525) przynoszą z okresu Wielkiego Postu i Wielkanocy 1757 r. ważne procesy majątkowe oraz świadectwa zwierzchności ordynackiej. Sługa miejski <strong>Jędrzej Surowicki</strong> z żoną <strong>Jadwigą z Kaczmarskich</strong> (1v. <strong>Pawłową Biegonową</strong>) procesują się z jej bratem <strong>Baltazarem Kaczmarskim</strong> o pobicie w domu sądowym (4 grzywny sądowi, 2 stronie, 2 dni aresztu) i o dopuszczenie do podziału sukcesji po rodzicach (skany 516–517). <strong>Szymon Marszałkowski</strong> wygrywa po długim sporze z braćmi <strong>Maciejem i Mikołajem Kawkami</strong> proces o niwkę Błuczorską trzymaną od <strong>22 lat</strong> w zastawie za 110 złp (skany 519, 524–525, z dopuszczeniem apelacji do <strong>Trybunału Zamojskiego</strong>), a także pozywa <strong>Grzegorza Pilaszkiewicza</strong> o kopanie na gruncie <strong>Jana Kofeckiego</strong> (skan 520). Bezpośrednie związki Kraśnika z Zamościem dokumentują plenipotencja <strong>Mośka Pinkwasowicza</strong> dla brata <strong>Szłomy Pinkwasowicza</strong> w sprawie z <strong>Aronem Lejbowiczem</strong> (skany 518–519) oraz wpisany <em>in extenso</em> mandat opiekuńczy <strong>Ordynacji Zamoyskiej</strong> (wystawiony przez <strong>Jana Jakuba Zamoyskiego</strong>, <strong>Jana Aleksandra Granowskiego</strong> i <strong>Franciszka Grzymałę Dzierżanowskiego</strong>) na termin 26 IV 1757 r. przed <strong>Sądem Komisarskim Zamku Zamoyskiego</strong> na instancję <strong>Szlomy Aronowicza</strong> z Bełżyc (skany 521–522). Całość zamykają procesy <strong>Bartłomieja Zdyba</strong> z zięciem <strong>Jakubem Węgorkiem</strong> (40 złp na wesele), krwawa bójka <strong>Antoniego Szafrańskiego</strong> z <strong>Wawrzyńcem Posuniakiem</strong> i <strong>Augustynem Jordykiem</strong> (skany 523–524) oraz wizja na gruncie <strong>Szymona Bieleckiego</strong> (skan 525).
        </p>

        <h3>Rozdział XLV: Wiosna 1757 r. – Sprawa 37 Czerwonych Złotych Habusia, Konflikt Deputata Morela i Wizje Gruntowe (skany 526–543)</h3>
        <p>
          Wiosenne sesje sądu złożonego z <strong>kwietnia i maja 1757 r.</strong> (fol. 256r–264v) przynoszą szereg spektakularnych sporów granicznych, karnych i ustrojowych. Trzykrotna kondescensja urzędowa z udziałem burmistrzów <strong>Antoniego Petrykowskiego</strong> i <strong>Antoniego Tokarza</strong>, pisarza <strong>Stanisława Brzyskiego</strong> oraz ławników rozsądza wieloletni spór o miedzę i chlewek między <strong>Szymonem Bieleckim</strong> a ślusarzem <strong>Jakubem Wojciechowskim</strong>, potwierdzony starymi kołkami granicznymi i zeznaniami poprzednika <strong>Stanisława Jańczyka</strong> (skany 526, 532–536). W sferze jurysdykcyjnej <strong>Kazimierz Młynarski</strong> pozywa <strong>Wojciecha Frankiewicza</strong> o skargę jego żony do gubernatora stróżkiego <strong>Jana Chrzanowskiego</strong> i chłostę hajduka na grebieniu (skany 528–529, 532). Tenże gubernator <strong>Jan Chrzanowski</strong> wraz ze starszymi kahału kraśnickiego zasiada jednak wspólnie z sądem miejskim w głośnym procesie starozakonnego <strong>Habusia</strong> przeciw <strong>Jędrzejowi Rymarczykowi</strong> i jego żonie o woreczek z <strong>37 czerwonymi złotymi i 37 tynfami</strong>, znaleziony na pogrzebie <strong>Katarzyny córki Maliny</strong> i ukryty przed mężem (wyrok nakazuje zwrot 4 czerwonych złotych i przysięgę żony w kościele kraśnickim, skany 530–532). Zapisano również lustracyjną wizję pękniętej ściany murowanej kamienicy <strong>Lebusia Nachymowicza</strong> (skany 536–537), gwałtowny zatarg deputata na Trybunał Zamoyski <strong>Marcina Morela</strong> z sądem miejskim o rzekomą korupcję i kupno wieprza za 24 złp u <strong>Jacka Szafrańskiego</strong> (skany 537–542), spór obywatela lubelskiego <strong>Jakuba Węgorka</strong> z <strong>Adamem Posuniakiem</strong> o 40 złp (skany 540, 542–543) oraz zapiskę z <strong>14 maja 1757 r.</strong> o ucięciu palca <strong>Bartłomiejowi z Budzynia</strong> przez <strong>Jana Chlebowskiego z Sandomierza</strong> (skan 543).
        </p>

        <h3>Rozdział XLVI: Wszyta Składka z Maja 1756 r. – Powołanie Kominiarza Generalnego i Ochrona Przeciwpożarowa Miasta (skany 544–550)</h3>
        <p>
          Od karty 265r (skan 544) introligator włączył w wolumin oryginalną składkę protokołów z <strong>maja 1756 r.</strong> (<em>Feryia Tercya ante Festi Ascensionis Domini 1756</em> – <em>Feryia 5ta post Festum Ascensionis 1756</em>), zawierającą bezcenny dokument ustrojowo-porządkowy: wspólne postanowienie <strong>całego urzędu miejskiego i synagogi kraśnickiej</strong> o powołaniu <strong>Jakuba Latosiewicza</strong> na urząd <strong>generalnego starnika i kominiarza</strong> do wymiatania kominów za tygodniowym wynagrodzeniem wypłacanym według regestru panów kahałnych (skany 544–545). Skuteczność i potrzeba tej uchwały ujawniły się natychmiast podczas rewizji przeciwpożarowej w domu <strong>Gierszona Catowica</strong> (od komornicy <strong>Sztenzli Pośrybawczowej</strong>), gdzie deputowani ławnicy <strong>Jan Lubartowski</strong>, <strong>Szymon Krzeszowski</strong> i <strong>Adam Zadel</strong> znaleźli zapieczoną sadzę i słomę w kominie oraz odparli zuchwałe uwagi <strong>Krengli Osypowiczowej</strong> (skany 545–546). Ponadto składka dokumentuje wcześniejszą fazę sporów <strong>Jakuba Wojciechowskiego</strong> z <strong>Szymonem Bieleckim</strong> (skany 547–548), sukcesję <strong>Antoniego Trzcińskiego</strong> i <strong>Tomasza Grabowskiego</strong> przeciw <strong>Krzysztofowi Kofeckiemu</strong> (15 złp i 2 złp na mszę za antecesorów, skany 548–549) oraz wizje na gruntach <strong>Antoniego Okonia</strong> i <strong>Józefa Gąski</strong> przeciw <strong>Antoniemu Wilczyńskiemu</strong> o przeoranie trzech zagonów i zabór wrót (skany 544, 549–550).
        </p>

        <h3>Rozdział XLVII: Dalszy Ciąg Składki z 1756 r. – Rewizja Ksiąg Wieczystych i Procesy Obyczajowe (skany 551–561)</h3>
        <p>
          Dalsze karty włączonej składki z <strong>1756 r.</strong> (fol. 268v–274v) przynoszą zarówno dramatyczne sprawy obyczajowe, jak i pierwszorzędne źródło do dziejów kancelarii miejskiej. W obszernym zeznaniu (<em>Interrogatorya Uxoris Josephi Nowak contra Paulum Fruga</em>) żona <strong>Józefa Nowaka</strong> opisuje napaść ze strony <strong>Pawła Frugi</strong> w drodze powrotnej z gospody „na łysą kuszczę”, za co sąd wójtowski skazuje Pawła Frugę na 12 grzywien do kościoła Najświętszej Panny Różańcowej, 10 grzywien Nowakowi, 4 grzywny sądowi i 3 dni wieży, a samego Józefa Nowaka i świadka <strong>Wawrzyńca Tokarza</strong> na grzywny za samosąd (skany 553–556). Na skanie 556 zapisano także skargę chorążego lubelskiego <strong>Jerzego Pietrowskiego</strong> przeciw burmistrzowi <strong>Stanisławowi Bryśkiewiczowi</strong> o pobicie poddanego, areszty kahału na chałupkę kupioną przez <strong>Grzegorza Zdyba</strong> przy starym kierkucie oraz młodziana <strong>Jana Wolaczka</strong> (skany 556–557), a także rewizję eksaktora <strong>Antoniego Marachiewicza</strong> u <strong>Marcinowej Cwiekowej</strong>. Kluczowym znaleziskiem kodykologicznym jest protokół <strong>rewizji ksiąg wieczystych</strong> z poniedziałku po Niedzieli Exaudi 1756 r. (skany 559–560): wójt kraśnicki prezentuje przed urzędem i pospólstwem opłakany stan akt — brak porządku, brak skrzyni i klucza, pobutwiałe protokoły „w koszuli”, z wyjątkiem jednego 16-kartkowego protokołu zapisów wieczystych i podrocznika. Część z 1756 r. zamykają ugody <strong>Jakuba Wojciechowskiego</strong> z <strong>Szymonową Bielecką</strong> (skany 558–559), <strong>Jana Lubartowskiego</strong> z <strong>Marcinem Morelem</strong> oraz <strong>Stanisława Bryśkiewicza</strong> z winiarzem <strong>Tomaszem Renkasem</strong> (skany 560–561).
        </p>

        <h3>Rozdział XLVIII: Lato 1757 r. – Architekt Klasztorny Józef Herbst, Szafarstwo Bez Przysięgi i Procesy Przedmieszczan (skany 562–575)</h3>
        <p>
          Od karty 275r (skan 562) protokoły wracają do roku <strong>1757</strong> (maj–czerwiec, okres od Zielonych Świątek do Świętej Trójcy). Wśród licznych sporów przedmiejskich wyróżnia się wielowątkowy proces <strong>Józefa Gąski</strong> przeciw braciom <strong>Antoniemu i Matyaszowi Wilkom (Wilczyńskim)</strong> o przeoranie miedzy, zabór snopów pszenicy i postrzelenie psa (zeznania <strong>Jana Cwieki</strong>, <strong>Tomasza Grabowskiego</strong>, <strong>Matyasza Łypka</strong>, <strong>Grzegorza Wolaka</strong> i <strong>Antoniego Wilczka</strong>, zakończone apelem Gąski do <strong>Trybunału Zamoyskiego</strong>, skany 562–564, 567–570). Odnotowano także manifestację burmistrza <strong>Łukasza Krzeszowskiego</strong> przeciw bratu ławnikowi <strong>Szymonowi Krzeszowskiemu</strong> o wyłączenie z sądu (skan 564), wizję szkody konia <strong>Walentego Jorgieła</strong> w sadzie <strong>Szymona Pągka</strong> (skan 566), manifestację wójta <strong>Michała Krzywińskiego</strong> przeciw <strong>Jędrzejowi Kofeckiemu</strong> o zniewagę (skany 571–572) oraz pretensje chłopów księcia <strong>Jabłonowskiego</strong> ze wsi Zakrzowa o dwa worki z żytem i sukmanę (30 V 1757 r., skan 572). Bezcenną wartość historyczno-artystyczną ma karta 280v (skan 573), na której obok notatek o objęciu szafarstwa bez przysięgi przez <strong>Szymona Szymkowskiego</strong> i <strong>Mikołaja Kawkę</strong> wpisano własnoręcznie podpisaną ugodę honorową między burmistrzem <strong>Stanisławem Bryśkiewiczem</strong> a <strong>Józefem Herbstem, architektem klasztoru kraśnickiego</strong> pracującym wówczas przy robotach klasztornych. Partię zamykają dekret finansowy <strong>Mikołaja Nowaka</strong> z niewierną <strong>Fejdlą Szyjową</strong> o 60 złp z jarmarków (zasądzono <em>per medium</em> 29 złp) oraz inkwizycja ławnika <strong>Jana Przesławskiego</strong> przeciw <strong>Piotrowi Potokowiczowi</strong> i jego żonie (skany 574–575).
        </p>

        <h3>Rozdział XLIX: Konflikt Wójta z Burmistrzem, Oblaty Kofeckich i Spory o Zboże i Wapno (skany 576–590)</h3>
        <p>
          Na przełomie maja i czerwca 1757 r. (fol. 282r–289r) nasiliły się tarcia w łonie samego magistratu kraśnickiego oraz spory kredytowe. Obok dokończenia inkwizycji ławnika <strong>Jana Przesławskiego</strong> przeciw <strong>Piotrowi Potokowiczowi</strong> i jego żonie o paciorki oraz procesu z niewierną <strong>Haimową Janklowiczową</strong> o skórę za 7 złp 15 gr (skany 576–578), wójt <strong>Michał Krzywiński</strong> manifestował przeciw burmistrzowi <strong>Łukaszowi Krzeszowskiemu</strong> o publiczny zarzut wyrywania kart z protokołów i sprzedawania ich deputatowi <strong>Marcinowi Morelowi</strong> (skan 580). Z kolei burmistrz i pisarz przysięgły <strong>Stanisław Bryśkiewicz</strong> dokonał kwitacji z <strong>Michałem Stachowiczem</strong>, poddanym OO. Franciszkanów w posesji chorążego lubelskiego <strong>Jerzego Pietrowskiego</strong> (skan 580), po czym oskarżył ławnika <strong>Jana Lubartowskiego</strong> z żoną o trzyletnie zniesławianie swojej małżonki i najście na dom (skan 581). W sprawach majątkowych odnotowano oblatę skryptu dłużnego <strong>Andrzeja (Jędrzeja) Kofeckiego</strong> na 158 złp 12 gr z 17 VI 1756 r. na rzecz brata <strong>Samuela Kofeckiego</strong> oraz areszt na dobrach <em>Tyrawczyzna</em> i niwie od <strong>Szymona Marszałkowskiego</strong>, uzupełniony aresztem starozakonnego <strong>Gierszona Catowica</strong> na 4 złp (skany 582–584). Od karty 286v (skan 585) rozpoczyna się blok kart zapisanych i zmikrofilmowanych <strong>do góry nogami</strong>, obejmujący m.in. spór starozakonnego <strong>Mośka Lewkowicza</strong> z <strong>Franciszkiem Czubrowskim</strong> i <strong>Adamem Posuniakiem</strong> o trzy korce wapna gaszonego i niegaszonego po 4 złp (skany 586–587), ugodę <strong>Jana Antoniego Marakiewicza</strong> z wdową <strong>Marcinową Ćwiekową</strong> (skan 587), bójkę <strong>Nowaków</strong> z <strong>Antonim Pawłowskim</strong> i <strong>Pawłem Frugą</strong> (skan 588) oraz wyrok na <strong>Macieja Frugę</strong> w sprawie z proboszczem <strong>ks. Jakubem Maliszewskim</strong> i Konwentem Kanoników Regularnych o 33 korce żyta (202 złp 15 gr, po potrąceniu 176 złp 9 gr w 4 ratach, skany 589–590).
        </p>

        <h3>Rozdział L: Kodykologia Odwróconego Raptularza Inkwizycyjnego z 1752 r. i Powrót do 1759 r. (skany 591–600)</h3>
        <p>
          Skany 591–599 (fol. 289v–294v), zachowujące odwróconą orientację kart w obrębie poszytu, przynoszą najpierw dokończenie materiałów z 1757 r. (wizja szkody w sadzie <strong>Jakuba Wojciechowskiego</strong> przez świnię <strong>Szymona Szelichowskiego</strong>, skan 591; początek sporu o sukcesję gruntów między <strong>Antonim Trojczakiem</strong> a <strong>Krzysztofem Rusakiem</strong>, skany 591–592; interogatoria <strong>Pawła Frugi</strong> w sprawie z żoną <strong>Józefa Nowaka</strong>, skan 592), po czym odsłaniają wszyty odwrotnie <strong>raptularz inkwizycyjny z 1752 r.</strong> (na skanie 599 opisany jako <em>Sextern tych Raptularz Inkwizycyj Zaczęwszy a d. 26 Martij 1752 Anno</em>). Dokumentuje on m.in. manifestację deputata <strong>Marcina Morela</strong> przeciw <strong>Kazimierzowi Młynarskiemu</strong> o podkupienie wieprza za 24 złp u <strong>Franciszka Wstruskiowskiego</strong> (skany 593–594, 596), wielowątkową bójkę weselno-karczemną <strong>Pawła Frugi</strong> z <strong>Nowakami</strong> i <strong>Wawrzyńcem Tokarzem</strong> (skany 594–595, 597), inkwizycję <strong>Adama Sołoniaka</strong> przeciw <strong>Antoniemu Dudkowi</strong> o górę Sowińską i pożyczony kożuch (skan 598), ugodę <strong>Marcina Budzyńskiego</strong> z <strong>Wawrzyńcem Tokarzem</strong> o pole z chałupą za 62 złp (skany 598–599) oraz śledztwo z wyjazdu na Wyźnicę po trzcinę i egzekucję podatku kahalnego w sprawie <strong>Wolfa Jeszkowica</strong> (skan 599). Na karcie 295r (skan 600) księga powraca do normalnej orientacji i roku <strong>1759</strong> (<em>Feria 3tia ante Dominicam Paschae</em>), odnotowując objęcie ćwierci po <strong>Hudrikowskiej</strong> przez <strong>Benedyka Kawkę</strong> oraz manifestację <strong>Antoniego Ławickiego</strong> przeciw <strong>Matyaszowi Szymarczykowi</strong> o pobicie matki na drodze publicznej.
        </p>

        <h3>Rozdział LI: Zatarg Cechmistrza Kowalskiego z Magistratem i Manifestacja Kramarzy Przeciw Arendarzowi Targowemu (skany 601–620)</h3>
        <p>
          Skany 601–620 (fol. 295v–304r) zamykają wpisy z wiosny 1759 r. (kondemnata na <strong>Grzegorza Pilaszkiewicza</strong>, wyroki na <strong>Grzegorza Jardzyka</strong> i <strong>Franciszka Kościeleckiego</strong>, areszt <strong>Marcina Zdyba</strong> na ćwierci Łysiakowskiej, skany 601–603) i przechodzą do obszernej serii protokołów z lata i jesieni <strong>1758 roku</strong> (z dwiema wszytymi zapiskami z października 1756 r., skany 611–612). W życiu korporacyjnym miasta wyróżnia się burzliwa akcja na ratuszu, podczas której cechmistrz kowalski i ślusarski <strong>Kazimierz Młynarski</strong> publicznie znieważył urząd i wójta przed krucyfiksem oraz spierał się ze sławetnym <strong>Antonim Siekierzyńskim</strong> i rotmistrzem <strong>Wojciechem Okuńskim</strong> (dublet mikrofilmowy na skanach 606–607), a także późniejsza skarga na tegoż cechmistrza ze strony <em>konter-magistra</em> kowalskiego <strong>Franciszka Bielickiego</strong> (skan 618). W sferze handlu miejskiego kluczowe znaczenie ma protestacja kramarza <strong>Kazimierza Żebrowskiego</strong> w imieniu wszystkich kolegów kramarzy przeciw niewiernemu arendarzowi targowemu <strong>Aznerowi</strong> o samowolne wybieranie przedjarmarcznego, podjarmarcznego i targowego niedzielnego (dublet mikrofilmowy na skanach 619–620). Liczne inkwizycje i obdukcje dokumentują ponadto spory przedmiejskie <strong>Joachima Karabacza</strong> z <strong>Wojciechem Pałką</strong>, <strong>Józefa Jardzyka</strong> z <strong>Wojciechem Zdybem</strong> i <strong>Jędrzejem Piotrowczykiem</strong> oraz pobicie ławnika <strong>Jana Przesławskiego</strong> przez <strong>Peryńskiego</strong> i <strong>Kazimierza Siemaśkowskiego</strong> (skany 610–611).
        </p>

        <h3>Rozdział LII: Proces Spadkowy Petrykowskich ze Słomkowską i Roszczenia Żołnierza Artylerii Koronnej Kazimierza Tokarskiego (skany 621–625)</h3>
        <p>
          Ostatnia część partii (fol. 304v–306v, skany 621–625) przynosi niezwykle precyzyjny wykład prawa spadkowego stosowanego przez sąd obopólny w Kraśniku. W procesie szlachetnego <strong>Antoniego Petrykowskiego</strong> (działającego w imieniu żony <strong>Reginy z Grzymułów</strong>, <em>1mo voto</em> za <strong>Pawłem Słomkowskim</strong>) przeciw wdowie <strong>Teresie Słomkowskiej</strong> po <strong>Kazimierzu Słomkowskim</strong> sąd przeanalizował trzy konkurencyjne testamenty (Pawła Słomkowskiego na 150 złp, ciotki <strong>Zofii Popławskiej</strong> oraz Kazimierza Słomkowskiego na 50 złp), po czym anulował wcześniejszy kompromis przyjaciół (wyceniający połowę niwki na 60 złp) i dopuścił Petrykowskiego do przysięgi o połowę gruntu oraz zwrot 39 złp 10 gr (skany 621–624). Równolegle urodzony <strong>Kazimierz Tokarski</strong>, żołnierz artylerii koronnej i sukcesor po ojcu <strong>Tomaszu Tokarzu</strong>, prowadził szeroki proces windykacyjny przeciw <strong>Janowi Łypie</strong>, <strong>Wojciechowi Wojtczakowi</strong>, <strong>Jakubowi Bielickiemu</strong>, <strong>Wojciechowi Wilczyńskiemu</strong> i <strong>Jędrzejowi Rypkowskiemu</strong>, w którym sąd nakazał mu przedłożenie autentycznego ekstraktu z ksiąg radzieckich (skany 617–618, 621, 624–625). Partię zamyka pozew rzemieślnika <strong>Melchiora Piotrowczyka</strong> przeciw ławnikowi <strong>Szymonowi Krzeszowskiemu</strong> i pisarzowi <strong>Stanisławowi Bryśkiewiczowi</strong> o niedotrzymanie kontraktu i szkodę w rzemiośle (skan 625).
        </p>
      </div>
"""

# Karty analityczne dla J17 (24 karty)
analytics_html = """
      <div class="analytics-content">
        <h2>🔍 Kluczowe Odkrycia i Przełomy Badawcze Jednostki 17</h2>
        
        <div class="analytics-card">
          <h4>💡 1. Demistyfikacja Kodykologiczna: Faktyczny Początek Woluminu w 1700 r.</h4>
          <p>
            Mimo że dawna etykieta introligatorska na okładce (skan #4) podaje lata <em>1756–1759</em> (z przekreśloną cyfrą 1700), autopsja źródłowa dowodzi, że księga otwiera się kompletną serią protokołów z <strong>roku 1700</strong>, przemieszaną z wszytkami wcześniejszymi.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⚖️ 2. Finansowanie Infrastruktury Obronnej z Grzywien Sądowych (Brama Lubelska)</h4>
          <p>
            Na karcie 1r (skan #5) połowę grzywny z bójki rodzinnej (7 grzywien) nakazano przekazać na <em>„Oprawę Bramy Lubelskiej”</em>, łącząc sądownictwo z utrzymaniem fortyfikacji miejskich.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏥 3. Kapitały Szpitala Św. Ducha w 1651 i 1700 roku</h4>
          <p>
            Ciągłość działalności prowizorów szpitala św. Ducha dokumentuje zarówno zapis z 1651 r. za prowizora Stanisława Szafrańskiego (80 złp na skanie #111), jak i rachunki burmistrza Adama Kotowicza z 1700 r. (skany #9–#10, #95).
          </p>
        </div>

        <div class="analytics-card">
          <h4>🤝 4. Pełna Integracja Prawna Społeczności Żydowskiej w Sądzie Miejskim</h4>
          <p>
            Wokanda ukazuje Żydów kraśnickich (Pinchas Dawidowicz, Herszek Tokarski, Mosiek Jarosławski, Leybuś Markowicz, Borek Herszkowicz, Berensz Kopel, Hapas, Kantorowa) korzystających z pełnej ochrony prawa magdeburskiego. Na skanie #119 mieszczanin Maciej Rzeźnik wygrał proces z arendarzem Pinchasem, uzyskując 20 złp kosztów i restytucję honoru.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🔥 5. Wyrok Śmierci przez Spalenie na Stosie za Sodomię (Szymon Kuparka, 1700 r.)</h4>
          <p>
            Skany #31–#33 i #46–#47 zawierają kompletny protokół procesu pasterza Szymona Kuparki z Wilkołaza, skazanego na mocy Prawa Saskiego na spalenie żywcem na stosie wraz ze zwierzęciem.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⛪ 6. Finanse Klasztorne i Fundacja Zegara Ściennego</h4>
          <p>
            Skany #27–#29 oraz #119 ukazują aktywność preora ks. Pawła Wilhelma Pajeckiego oraz generała zakonu ks. Franciszka Starskiego w egzekucji czynszów Arcybractwa i legatów (100 złp na zegar klasztorny).
          </p>
        </div>

        <div class="analytics-card">
          <h4>👑 7. Podskarbina Anna Zamoyska i Asygnacje Finansowe</h4>
          <p>
            Na skanie #91 oblatowano oryginalną asygnację Anny z Gnińskich Zamoyskiej z 3 sierpnia 1700 r. na wypłatę 43 złp burmistrzowi Barankowiczowi i 80 złp radcy Pielaszkowiczowi przez arendarza Pinchasa.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🎨 8. Kraśnicki Warsztat Malarski (Siudziński i Mrokowski)</h4>
          <p>
            Protokoły z 1700 r. ujawniają dwóch mistrzów malarskich: Adama Karola Siudzińskiego (skan #67) i Adama Karola Mrokowskiego (skany #72, #77) oraz wdowę Barbarę Mrokowską po Karolu Mrokowskim (skan #106).
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏛️ 9. Spór o Spadek Wójta Janaszkowica przed Trybunałem Zamoyskim</h4>
          <p>
            Skany #78–#79 dokumentują proces Pawła Słomkowskiego z landwójtem Wojciechem Nowakowiczem i Katarzyną z Janaszkowiców o majątek zmarłego wójta Ubaldiego przed Najwyższym Trybunałem Miast Zamoyskich.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏰 10. Kamienica Murowana w Rynku dla Kupców Żydowskich (Borek i Kopel)</h4>
          <p>
            Na skanach #97–#100 ks. przeor Pajecki i burmistrz Barankowicz oddają w wieczyste posiadanie kamienicę rynkową kupcom Borkowi Herszkowiczowi i Berenszowi Koplowi z czynszem na św. Michała.
          </p>
        </div>

        <div class="analytics-card">
          <h4>📜 11. Odkrycie Wszytego Poszytu z 1651 roku (skany #111–#114)</h4>
          <p>
            Wewnątrz akt z 1700 r. zachowały się dwie oryginalne karty z maja i czerwca <strong>1651 roku</strong> (fol. 53r–54v) spisane siedemnastowieczną ręką za wójtostwa Andrzeja Grzybowskiego. Potwierdzają one dolną granicę chronologiczną jednostki (1651 r.) z inwentarza archiwalnego.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🩸 12. Proces o Zabójstwo Chłopca Kubosia i Głowszczyzna w 1651 roku</h4>
          <p>
            Skan #114 (czerwiec 1651 r.) dokumentuje oskarżenie wniesione przez szlachcica Atanazego Gorczyckiego przeciw Jadwidze Bartoszkowej, której syn Tomasz miał zabić siekierą chłopca Kubosia. Sąd wyznaczył przysięgę oczyszczającą matki oraz ośmiu mężów do oszacowania i zapłaty głowszczyzny za śmierć dziecka.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🔨 13. Cech Kowalski i Wykupy Woskowe w Sporach Rzemieślniczych</h4>
          <p>
            Skan #124 ujawnia, że dawny burmistrz Stefan Gostkowicz był jednocześnie Mistrzem Cechu Kowalskiego. W sporze z kowalem Wawrzyńcem Staficą o źrebca i robotę kowalską sąd nałożył typowe dla statutów cechowych kary kościelno-cechowe: 3 funty wosku od Staficy i 2 funty wosku od mistrza Gostkowicza.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🐄 14. Oskarżenie o Korupcję Urzędniczą („Krowa dla Burmistrza Kwaśnica”)</h4>
          <p>
            Skan #125 zawiera sensacyjne zeznanie zaprzysiężone Jana Więckowicza, który zeznał, że wójt Marcin Dymarczyk przymuszał Tomasza Kobca do sprzedaży ojcowizny i obiecał byłemu burmistrzowi Stefanowi Kwaśnicowi krowę w zamian za trzymanie jego strony w procesie.
          </p>
        </div>
        <div class="analytics-card">
          <h4>⚖️ 15. Zeznanie Ławnika Borkowicza: Bezpośredni Dowód Przekupstwa Krową</h4>
          <p>
            Skan #130 przynosi bezpośrednie zeznanie ławnika przysięgłego Wojciecha Borkowicza, który potwierdził w pierwszej osobie, że Marcin Dymarczyk na komornym u Stefana Kwaśnica obiecał mu krowę za stronniczość przeciw Tomaszowi Kopcowi (a żona Dymarczyka mówiła o mleku i cielęciu).
          </p>
        </div>

        <div class="analytics-card">
          <h4>🔮 16. Proces o Czary i Przysięga Oczyszczająca Maryny Kłotkowej (1700 r.)</h4>
          <p>
            Skany #141 oraz #147–#148 dokumentują proces o zadanie czarostwa między winiarzem Marcinem Chudzikiem a Wojciechem i Maryną Kłotkami. Pełny skład sądu z wójtem Janem Majowskim nakazał Marynie Kłotkowej złożenie przysięgi oczyszczającej z dwoma świadkami pod rygorem kary kryminalnej.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏰 17. Spór Arendarza Pinchasa z Rzeźnikiem Mazałą przed Zamkiem Zamojskim</h4>
          <p>
            Skany #126–#127, #135, #143 i #149 ukazują wielomiesięczną batalię o łopatkę mięsa, oddalenie przez sąd miejski zawyżonych kosztów pisarskich arendarza oraz pozwy przed Sąd Skarbowy Komisarski Zamku Zamoyskiego.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⛪ 18. Zatarg Przeora Pajeckiego z Burmistrzem Szymatowskim o Zniewagę Krucyfiksu</h4>
          <p>
            Na skanie #144 przeor kanoników regularnych ks. Paweł Pajecki wniósł uroczystą protestację przeciw burmistrzowi Wojciechowi Szymatowskiemu o bluźnierstwa, znieważenie stanu duchownego oraz brak uszanowania dla krucyfiksu stojącego na stole sądowym.
          </p>
        </div>

        <div class="analytics-card">
          <h4>👞 19. Legat Ćwierci Roli dla Cechu Szewskiego za Kwartalne Msze Żałobne</h4>
          <p>
            Skany #132, #146–#148 odtwarzają na podstawie zeznań dawnego ławnika Wojciecha Kunuśkiewicza i szewca Tomasza Nowackiego testamentowy zapis Łukasza Baranowskiego dla Cechu Szewskiego pod cechmistrzem Stanisławem Bieleckim.
          </p>
        </div>
        <div class="analytics-card">
          <h4>📜 20. Kodykologia: Oryginalny Początek Księgi „Annus 1700 Incipit” (8 I 1700 r.)</h4>
          <p>
            Skan #159 (fol. 77r) otwiera oryginalną składkę ze stycznia 1700 r. jeszcze za życia wójta ordynaryjnego Jana Onuszkowica (przed jego śmiercią wiosną tegoż roku), dowodząc przemieszania poszytów w oprawie introligatorskiej. Na skanie #171 zidentyfikowano dublet mikrofilmowy karty 82v (#170).
          </p>
        </div>

        <div class="analytics-card">
          <h4>🕯️ 21. Śledztwo Sądowe w Sprawie Nagłej Śmierci Zofii Skatkównej (6 Świadków)</h4>
          <p>
            Skany #160–#164 zawierają sześć zeznań (w tym dziada ze Szpitala św. Ducha Wojciecha Mazura i winiarza Marcina Chudzika) badających, czy Zofia Skatkówna ze służby u młynarza Łaty zmarła wskutek choroby, czy zatargu z bratem Wojciechem Skatką o chałupę i spadek.
          </p>
        </div>

        <div class="analytics-card">
          <h4>💰 22. Egzekucja Dekretu Trybunału Zamojskiego na 402 złp 15 gr (Słomkowscy v. Nowakowicz)</h4>
          <p>
            Skany #157–#158 dokumentują protestację braci Pawła i Wojciecha Słomkowskich przeciw landwójtowi Wojciechowi Nowakowiczowi i Katarzynie z Janaszkowiców o niewypłacenie do zachodu słońca zasądzonej przez Trybunał Zamojski kwoty 402 złp 15 gr ze spadku po wójcie Ubaldim Janaszkowicu.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🎨 23. Obrona Honoru Malarza Adama Karola Mrokowskiego i Atak z Szablą na Sąd</h4>
          <p>
            Na skanie #172 malarz kraśnicki Adam Karol Mrokowski złożył uroczystą reprotestację przeciw podwójciemu Stanisławowi Jerzykiewiczowi w obronie swojej sławy, natomiast na skanie #175 cały urząd oskarżył Grześka rzeźnika o profanację sądu i rzucenie się z szablą na ławnika Jana Barankowicza.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏡 24. Sprzedaż Stodoły za Bramą Lubelską Ickowi Dawidowiczowi i Feygli (60 złp)</h4>
          <p>
            Skany #174–#175 rejestrują sprzedaż stodoły i gruntu Łożałowska za Bramą Lubelską przez Wojciecha i Ewę Starzykiewiczów obywatelowi żydowskiemu Ickowi Dawidowiczowi oraz jego żonie Feygli za 60 złp, w bezpośrednim sąsiedztwie posesji kupca Herszka.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⚖️ 25. Rozwiązanie Zagadki Dymarczyka i Kopciów: Ojcowizna Marianny z Jasieńskich (120 złp)</h4>
          <p>
            Skany #180–#181 oraz #190 ujawniają podłoże wielomiesięcznego procesu: żona Tomasza Kopcia, Marianna, była córką Augustyna Jasieńskiego i Reginy, a Marcin Dymarczyk był jej ojczymem. Sąd Obojny przyznał Kopciom wykup ojcowizny za 120 złp, które Kopeć okazał uroczyście 12 XI 1700 r. przy świadkach.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🎨 26. Śmierć Malarza Adama Karola Mrokowskiego i Małżeństwo Wdowy z Broskowskim</h4>
          <p>
            Zapis z 27 X 1700 r. (skany #181–#182) potwierdza zgon malarza Adama Karola Mrokowskiego w ciągu 1700 r. oraz nowe małżeństwo wdowy Barbary z Janaszkowiców z Wawrzyńcem Broskowskim z Podlasia, z zabezpieczeniem praw majątkowych jej syna Antoniego Mrokowskiego.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🕯️ 27. Finał Procesu o Czary Kłotków z Chudzikiem: Wadium 120 Grzywien i Groźba Banicji</h4>
          <p>
            Na skanie #183 (dublet mikrofilmowy #184) po złożeniu przysięgi oczyszczającej przez Wojciecha i Marynę Kłotków sąd zamknął proces o czary wyrokiem z 29 X 1700 r., grożąc winiarzowi Marcinowi Chudzikowi wadium 120 grzywien, banicją wieczną i karą cielesną.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🌳 28. Lustracja Sadów na Zarzeczu i Wykup Roli po Kondupie przez Tomasza Zdeba (100 złp)</h4>
          <p>
            Skany #185–#188, #196 (wizja burmistrza Sokołowicza i ławnika Borkiewicza z opisem 30 drzewek gruszy i jabłoni) oraz #200 dokumentują spór o ćwierć roli po Wojciechu Kondupie, zakończony złożeniem przez Tomasza Zdeba pełnej sumy 100 złp przeciw Andrzejowi Pankowi.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🧵 29. Śledztwo Krawca Dalmaczyka, Kontrakt Pionów na Piasku i Zastaw u Hesi (skany #191–#200)</h4>
          <p>
            Listopadowe sesje przynoszą przesłuchania świadków w sprawie pieniędzy Anny Dalmaczykówny u Barankowiczów, sprzedaż domu na Piasku przez Pionów Bielakom za 50 złp (#197), sprawę zastawionej za 15 zł białej spódnicy u Żydówki Hesi (#199–#200) oraz relację woźnego Macieja Pełki o pozwie do Zamku Zamoyskiego.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏡 30. Uroczysta Intromisja Tomasza Zdeba w Rolę Kondupowską (4 XII 1700 r.)</h4>
          <p>
            Skany #204–#205 opisują szczegółowo zjazd urzędowy burmistrza Adama Sokołowicza, ławników Borkiewicza i Pielaszkowica oraz pisarza Chmielowicza z udziałem 10 sąsiadów (m.in. Kopcia, Anczerka, Wilka, Wójcika, Rępki i Kłopotów) oraz głośne wywołanie intromisji w czterech rogach gruntu przez woźnego Matyasza Mozielaka (<em>nemine impugnante</em>).
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏥 31. „Baba Szpitalna” Katarzyna Kukiełkowa i Transakcja na 200 złp dla Kopciów</h4>
          <p>
            Dnia 7 XII 1700 r. (skany #206–#207) Katarzyna Kukiełkowa, wdowa po Wawrzyńcu Kukiełce mieszkająca jako baba szpitalna w Szpitalu św. Ducha, w asyście opiekuna podwójciego Stanisława Jerzykiewicza sprzedała Tomaszowi Kopcowi i Mariannie z Jasieńskich dwie kwatery roli z chałupą, stodołą i ogrodem za 200 złp.
          </p>
        </div>

        <div class="analytics-card">
          <h4>👑 32. Kwitacja Szlachecka Wolanowskich dla Starszych Synagogi Kraśnickiej (20 XII 1700 r.)</h4>
          <p>
            Skany #217–#218 dokumentują dobrowolne poddanie się jurysdykcji miejskiej szlachcianki Konstancji z Zamiechowskich Wolanowskiej i jej syna Jakuba Wolanowskiego, którzy własnoręcznymi podpisami pokwitowali Starszych Synagogi (Pinchasa Dawidowicza i Wigdora Markowicza) ze spłaty kapitału i prowizji po śp. Franciszku Wolanowskim.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🩸 33. Napaść na Abusia Jakubowicza w Urzędowie i Wyrok Chłosty w Kraśniku</h4>
          <p>
            Skany #211–#212 zawierają obdukcję krwawych ran i rabunku 15 złp dokonanego na Żydzie Abusiu Jakubowiczu przez Jana Rysiewicza z Wilkołaza podczas jarmarku w Urzędowie, natomiast skan #215 dokumentuje wyrok publicznej chłosty na zbiegłego z rękojmi Marcina Hapaka oraz chłopca pastucha ze sprawy wójta pastewnego Biernatka.
          </p>
        </div>

        <div class="analytics-card">
          <h4>📜 34. Kodykologia: Przestawiona Składka z Pełnym Wyrokiem w Sprawie Kondupa (skany #219–#225)</h4>
          <p>
            Po wpisach z 23 XII 1700 r. (#218) introligator wszył wcześniejszą składkę (#219–#225, fol. 106r–109r) zawierającą pełny wywód stron oraz sentencję wyroku Sądu Obojnego w sprawie roli Kondupowskiej (sięgającą długów z 1690 r. i cesji Szymona Wójcika za 60 złp), zwieńczoną wykonaniem dekretu z 24 XI 1700 r.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🕰️ 35. Kodykologia: Odkrycie Składki z 1694 r. i Wójta Ubaldiego Janaszkowica (skany #229–#231)</h4>
          <p>
            Skany #229–#231 (fol. 111r–112v) tworzą nieznaną dotąd wszytą składkę z 1694 roku za wójtostwa Ubaldiego Janaszkowica, dokumentującą skład ławy (Stefan Jerzykiewicz, Jan Majowski, Grzegorz Kłopotek), spór z malarzem Karolem Mrokowskim o zniesławienie na tablicy oraz obdukcje Grzegorza Boguty i Stanisława Pękały.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⚔️ 36. Napad Szlachcica Pikulskiego na Burmistrza Szmatkowskiego pod Konopnicą (1730–1731)</h4>
          <p>
            Skany #233–#235 otwierają warstwę z lat 1730–1731 (<em>ANNUS NOVUS 1731</em>): relację i inkwizycję (Jan Barankowicz, Abram Szlomowicz, Marcin Ćwióka) o zbrojnym napadzie z dobytymi szablami na sanie burmistrza Benedykta Szmatkowskiego pod karczmą w Konopnicy podczas powrotu z Wieniawy.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🔥 37. Świadectwo Pożaru Kraśnika i Wolnizna Budowlana w 1731 r. (skany #238–#239)</h4>
          <p>
            Wyrok w sprawie wdowy Janowej Chudzikowej z Janem Malborskim (#238) ujawnia skutki pożaru miasta (<em>„podczas spalenia się Kraśnika”</em> pogorzelec Boruch z żoną znalazł schronienie w jej chałupie), natomiast na skanie #239 Augustyn Zbydniowicz budujący się <em>de novo</em> otrzymał roczną wolniznę podatkową (1 rok i 6 niedziel).
          </p>
        </div>

        <div class="analytics-card">
          <h4>🧥 38. Taksa Kontuszów i Żupana przed Sądem Radzieckim (25 I 1731 r., skany #246–#247)</h4>
          <p>
            Sąd radziecki pod prezydencją Szymona Jankowskiego, cechmistrza krawieckiego i burmistrza Benedykta Szmatkowskiego oszacował odzież męską Tomasza Tyrańskiego i Matyasza Latosłowicza: kontusze niebieskie z jedwabnymi potrzebami na 22 złp, 19 złp i 18 złp oraz żupan granatowy na 16 złp.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⚖️ 39. Proces Boruchowej Jaskowej z Wojciechem Frankiewiczem o Kożuch i Nawiązkę (skany #237, #242–#246)</h4>
          <p>
            Wielowątkowy proces o pobicie Żydówki Boruchowej Jaskowej nogą od stołka przez podpitego Wojciecha Frankiewicza podczas sporu o kożuch zatrzymany za długi po śp. Kacprze Frankiewiczu, zakończony zapisem 35 złp na ogrodzie, 10 złp nawiązki oraz 5 złp 18 gr dla cyrulika.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🕵️ 40. Śledztwo w Sprawie Paserstwa i Zajęcie Długu Tokarczyka na Areszty (skany #259, #263–#265)</h4>
          <p>
            Proces z powództwa Lejbusia Boruchowicza ujawnił szajkę kradnącą kożuchy, spódnice, burki i siekiery przez syna Marcinowej Pańkowej. Sąd skazał Matyasza Kopytkowicza i Antoniową jako paserów (15 złp i 5 złp kary oraz więzienie), a 30 złp wierzytelności Kopytkowicza u Kazimierza Tokarczyka przekazał bezpośrednio wierzycielom (19 złp 10 gr Boruchowiczowi i 13 złp 24 gr Maryance).
          </p>
        </div>

        <div class="analytics-card">
          <h4>📜 41. Testament Wojciecha Dudaja z Choroby i Rozliczenie Zięcia z Bychawy (skany #254–#255)</h4>
          <p>
            Zapis ostatniej woli chorego Wojciecha Dudaja złożony wobec sądu obojnego ujawnia realia majątkowe mieszczanina (90 złp przechowywanych „pod głowami”, 16 złp za śrubkę, stopione srebro zabrane przez zięcia Macieja z Bychawy) oraz zabezpieczenie majątku na rzecz żony i modlitwy za duszę.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏘️ 42. Intromisja Chelmana Beniaszowicza i Ewy Zelmanowiczowej w Plac przy Furtce (28 III 1731 r., skan #267)</h4>
          <p>
            Pełny skład władz miejskich (wójt Stanisław Wawrzyniec Pilaszkowicz, prezydent Szymon Szandrowicz, burmistrzowie Benedykt Szmatkowski i Szymon Marszałek) przekazał ubogiemu małżeństwu żydowskiemu pusty, nieprzynoszący dotąd dochodu plac przy furtce na Podlesie pod budowę izby za 15 złp, wprowadzając ich pod zieloną rózgą przez woźnego Jana Ślusarczyka.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🕯️ 43. Spór o Wstążkę w Kościele i Grzywna Woskowa do Kaplicy Różańcowej (skany #266–#267)</h4>
          <p>
            Zatarg między Kazimierzem Rokickim a Andrzejem Bogutą o zdartą w kościele wstążkę i najście domu zakończył się surowym wyrokiem dyscyplinarnym: 1 grzywna dla sądu za nieutrzymanie żony w ryzach, 1 grzywna na wosk do Kaplicy NMP Różańcowej od córki Boguty oraz obowiązkowe publiczne przeprosiny w cechu przy braci.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🌾 44. Sukcesja Kwatery po Stanisławie Wiatrku i Samosąd nad Kozą (skany #270–#275)</h4>
          <p>
            Komplanacja czterech przysięgłych mężów (Tokarza, Głowackiego, Żyśki, Okunia) wyceniła kwaterę pola z chałupą i stodołą po Stanisławie Wiatrku na 60 złp (z potrąceniem 20 złp dożywocia dla Wojciecha Kozy i spłatą 40 złp Pawłowi Wiatrkowi pod rękojmią Wawrzyńca Kozy). W tym samym czasie ławnik Jan Chorążyński został skazany na 4 złp 15 gr i dobrowolne więzienie za samowolne zabicie kozy Lewka Abramowicza mimo braku szkody w śliwach.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⚖️ 45. Wyrok Śmierci przez Powieszenie na Recydywistę Wawrzyńca Pańka (20 VI 1731 r., skan #287)</h4>
          <p>
            Sąd Obojny Kraśnicki wraz z ławą i cechmistrzami wydał jednomyślny wyrok śmierci (<em>„aby był obwieszony”</em>) na niepoprawnego złodzieja Wawrzyńca Pańka, który przez kilkanaście lat okradał mieszczan i Żydów, trzykrotnie zrywał się z łańcucha i więzienia oraz odgrażał się podpaleniem miasta.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🌾 46. Urzędowa Taksa Targowa Zbóż i Taksy Garderoby z Czerwca–Lipca 1731 r. (skany #286–#287, #295)</h4>
          <p>
            Protokół z 25 VI 1731 r. (#287) utrwalił pełne ceny zbóż w Kraśniku: pszenica ozima 9 złp, jara 8 złp, żyto 6 złp, groch 9 złp, jęczmień 5 złp, tatarka 5 złp, owies 3 złp. Uzupełniają go wyceny zastawionej odzieży Pani Gurowskiej (żupan niebieski 8 złp, spódnica wiśniowa 12 złp, jupka żółta kamlotowa 4 złp – skan #286) oraz Adama Tokarczyka i Sokołowskiego u Leybusia Boruchowicza (żupan granatowy 18 złp, jubka granatowa 10 złp – skan #295).
          </p>
        </div>

        <div class="analytics-card">
          <h4>✡️ 47. Kredyt Kościelny dla Żydów: Oblata 200 złp z Podpisem Hebrajskim (1729/1731, skany #288–#289)</h4>
          <p>
            Wpisana w 1731 r. oblata kontraktu z 1729 r. dokumentuje pożyczkę 200 złp udzieloną przez ks. plebana kraśnickiego małżonkom Herszkowi Jakubowi Chaimowiczowi i Chai Lachmanowiczównie (za poręką syndyka synagogi Majera Moskowicza) na budowę domu w dzielnicy żydowskiej, uwierzytelnioną własnoręcznym podpisem w alfabecie hebrajskim.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⛪ 48. Tumult Jarmarczny i Proces o Pobicie Dziada Kościelnego (9 VII 1731 r., skany #289–#291)</h4>
          <p>
            Ks. Wawrzyniec Lednicki z ramienia proboszcza kraśnickiego przeprowadził zaprzysiężoną inkwizycję trzech świadków (Andrzeja Jeśa, Marcina Marcewicza, Adama Pożniakowskiego) w sprawie pobicia dziada kościelnego (11 sinych ran) przez piekarza Chudego i kramarza Icka Figlarza w niedzielę jarmarczną.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏡 49. Obrót Nieruchomościami (Dom za Bramą Lubelską 90 złp, Plac Postrzygaczowski 16 złp) i Rękojmia Poddańcza (skany #292–#295)</h4>
          <p>
            Lipcowe intromisje rejestrują sprzedaż domku z ogródkiem naprzeciw kościoła św. Ducha za 90 złp Maciejowi Latosłowiczowi (#292–#293), sprzedaż placu Postrzygaczowskiego przy Bramie Krakowskiej za 16 złp (#293) oraz poręczenie pięciorga mieszczan za zbiegłego ze Słupkowic poddanego Jana Długockiego w dobrach dzierżawcy Franciszka Sokołowskiego (#294–#295).
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏰 50. Sprzedaż Domu Rogowego przy Bramie Lubelskiej za 2450 złp (Grymałowscy – Herszkowiczowie, skany #302–#303)</h4>
          <p>
            Jedna z najwyższych transakcji nieruchomościowych w księdze: intromisja Ayzyka Herszkowicza i Rochli Dawidowiczówny w dom rogowy przy Bramie Lubelskiej kupiony od śp. Wojciecha Grymałowskiego i Teresy z Ubaldich z córką Katarzyną za 2450 złp, potwierdzona kwitacją syna Andrzeja Grymałowskiego w Trybunale Zamojskim.
          </p>
        </div>

        <div class="analytics-card">
          <h4>📜 51. Przekłady Dekretu Rabinackiego z 1726 r. (486 r. żyd.) i Kwitu na 930 złp (skany #307, #315–#316)</h4>
          <p>
            Do księgi miejskiej wpisano dosłowne polskie tłumaczenia dwóch dokumentów hebrajskich (<em>de Verbo ad Verbum</em>): dekretu rabina Mojżesza, Wigdora Markowicza i Szymona Józefowicza z Lublina (5 VII 1726 r.) o ławce w synagodze dla Oszyi Moskowicza oraz kwitu Judki Leybusia Chaimowicza na 930 złp po wuju Icku Dawidowiczu.
          </p>
        </div>

        <div class="analytics-card">
          <h4>💰 52. Wielki Kompromis Handlowy na 2000 złp pod Wadium 50 Czerwonych Złotych (skan #317)</h4>
          <p>
            Wpis z 1731 r. dokumentuje rozliczenie membranu na 2000 złp i 383 złp 10 gr w kramarni między Berkiem Nachymowiczem a Szymonem Eliaszowiczem przed starszym synagogi Wigdorem Markowiczem, z poręką Pinkwasa Dawidowicza na 1000 złp i zabezpieczeniem na kramnicy.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🔨 53. Przełom Kodykologiczny 1753–1754: Cechy Kuśniersko-Krawiecki i Szewski (skany #318–#321)</h4>
          <p>
            Od skanu #318 księga przechodzi do lat 1753–1754, odsłaniając organizację cechową za starszeństwa Walentego Kieprzyckiego (cech kuśnierski i krawiecki) oraz Antoniego Banikiewicza, komplanację braci szewców Adama i Michała Łasoniaków na 25 złp przed rajcą Antonim Skórkowskim i ławnikiem Antonim Kuliczyńskim, a także pozew Trybunału Zamojskiego dla burmistrza Łukasza Krzeszowskiego.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🕯️ 54. Śledztwo Obyczajowe de Crimine Delicti i Obdukcje z 1753 r. (skany #322–#325)</h4>
          <p>
            Protokoły inkwizycji z końca 1753 r. odsłaniają rewizję domową u ławnika Szymona Krzeszowskiego, sprawę kupna podejrzanej odzieży od chłopa, proces o zagryzienie gęsi przez psa oraz szczegółowe przesłuchania Anny Jazdzikówny i Żydówki Bralowej w sprawie cudzołóstwa z Grzegorzem Pitaszkiewiczem.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🧵 55. Bunt w Cechu Tkackim 1754 r.: Wyzwoliny za 2 Talary Bite i Spory z Marcinem Morelem (skany #328–#333, #343)</h4>
          <p>
            Seria inkwizycji ze stycznia i maja 1754 r. dokumentuje wewnętrzny kryzys cechu tkackiego wokół wyzwolin Jakuba Wróbla, zarzuty Marcina Morela przeciwko burmistrzowi i cechmistrzowi Łukaszowi Krzeszowskiemu o sprzedaż prawa cechowego i wyrób płótna przez kobiety (8 złp), a także spory w gospodzie u Struszki z udziałem Antoniego Łatosiewicza i Jana Szubertowskiego.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⚖️ 56. Wyroki Chłosty i Wyświecenia z Miasta według Prawa Brandenburskiego (skany #327–#328, #335, #348)</h4>
          <p>
            Sąd miejski w 1753–1754 r. stosował surowe kary publiczne w sprawach o cudzołóstwo: 200 plag cielesnych i wyświecenie z miasta dla Jakubowej Krasowskiej (100 plag i 3 dni leżenia krzyżem dla Szymona Wójcika, 10 grzywien dla spóźnionego delatora Cełca), 200 plag i wyświecenie dla Jana Mecha i Marianny Zdybkówny oraz egzekucję na Mariannie Tkaczykównej.
          </p>
        </div>

        <div class="analytics-card">
          <h4>📜 57. Odwrócona Suplika Miasta z Pospólstwem przeciw Robociznom i Upadkowi Bydła (skan #341)</h4>
          <p>
            Na fol. 167v znajduje się unikatowy wpis odwrócony o 180 stopni — błagalna suplika Miasta z Pospólstwem Kraśnickim do Jaśnie Wielmożnego Pana i Dobrodzieja o ulżenie w niezwyczajnych drogach i robociznach ponad powinność skarbową z powodu masowego upadku bydła i zubożenia domostw.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⚔️ 58. Wojsko Koronne w Kraśniku 1754 r.: Porucznik Gomuliński i Podchorąży Skowroński (skany #342, #350)</h4>
          <p>
            Inkwizycje z 1754 r. rejestrują bezpośrednie tarcia między garnizonem a samorządem: śledztwo na instancję porucznika infanterii buławy wielkiej koronnej Piotra Gomulińskiego o groźby Adama Radła oraz skargę wójta Szymona Marczukowskiego przeciw podchorążemu Skowrońskiemu o groźbę odbicia więźniów z aresztu u Żydówki Kali.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🗡️ 59. Dobycie Pałasza na Wójta Marczukowskiego i Kontrakty w Lublinie (skany #351–#353, #360)</h4>
          <p>
            Zeznania Piotra Panka, Franciszka Czubkowskiego i Andrzeja Potokowicza odsłaniają napaść żołnierzy podchorążego Skowrońskiego z pałaszem na wójta Szymona Marczukowskiego w gospodzie Żydówki Kali oraz najście na komorę u Żyda Dawidka. Z kolei skan #360 ujawnia lubelskie rozmowy rajcy Szymona Szankiewicza z kapitanem Gomulińskim dotyczące stancji w dworze kolarzów naprawionym przez Adama Zandla.
          </p>
        </div>

        <div class="analytics-card">
          <h4>📜 60. Spadek po Augustynie Piotrowczyku i Ród Zdybów (skany #358–#359, #361)</h4>
          <p>
            Pięciu świadków (Bartłomiej Kilianek, parobek Matyasz Łysak, Mikołaj Biegaj, Józef Laska, Stanisław Wolak) oraz ławnik Jan Szubertowski zrekonstruowali szczegółowo ostatnią wolę zmarłego Augustyna Piotrowczyka, rozliczenia 101 złp 15 gr za woły z Rudnika, 20 złp danych na Mszę św. ze Stanisławem Kiliankiem oraz pozycję macochy z domu Zdybów („de gente Zdybionka”).
          </p>
        </div>

        <div class="analytics-card">
          <h4>👞 61. Kryzys w Cechu Szewskim i Urzędowa Rewizja Domu Antoniego Okonia (skany #368–#370)</h4>
          <p>
            W dniu 26 XI 1754 r. mistrz szewski Szymon Zajowski wniósł skargę przeciw cechmistrzowi Wojciechowi Potokowiczowi o pobicie w gospodzie po uwadze o wosku na świecę. Tego samego dnia szewc Antoni Okoń zażądał urzędowej wizji swego domu przez ławnika Antoniego Szaliczyńskiego i pisarza Michała Krzyżanowskiego, oczyszczając żonę z pomówień Jadwigi Potokowiczowej o kradzież płótna.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🌾 62. Sprawy Grudniowe 1754 r.: Poddany z Wilkołaza, Kradzież 23 Snopków i Bracia Pełkowie (skany #371–#375)</h4>
          <p>
            Grudniowe wyroki z 1754 r. obejmują ochronę poddanego z Wilkołaza Stanisława Rzepki przed Janem Tokarczykiem (zwrot 2 worków i 4 grzywny kary), proces Walentego Jorgiela przeciw Grzegorzowi Jurdzikowi o 23 snopki jęczmienia odnalezione w komorze, nakaz zapłaty 5 złp reszty długu przez Jana Wiaterka bratu Wojciechowi oraz przyjacielską ugodę braci Łukasza i Wojciecha Pełków.
          </p>
        </div>

        <div class="analytics-card">
          <h4>💰 63. Prowizja Szlachecka za 13 Lat i Niewypłacalność Długu z 1741 r. (skany #376–#377)</h4>
          <p>
            Dekret z 20 XII 1754 r. w sprawie starozakonnego Hajka Lejzorowicza przeciw Janowi Łysemu stanowi precyzyjny wzorzec sądowego rozliczania zaległości wieloletnich: do kapitału 24 złp 15 gr sąd doliczył 13-letnią prowizję szlachecką (28 złp 15 gr) oraz 5 złp dawnego długu z 1741 r., zasądzając łącznie 55 złp płatnych w trzech ratach w 1755 r. (20 + 20 + 15 złp).
          </p>
        </div>

        <div class="analytics-card">
          <h4>⚖️ 64. Otwarcie Roku 1755 i Seria Procesów Marcina Morela (skany #378–#386, #390–#391)</h4>
          <p>
            Od 3 I 1755 r. (skan #378) protokoły dokumentują falę procesów Marcina Morela: spory z Andrzejem Kraskowskim o wieprzki i zbłąkanego gniadego konia, obronę metryki Jana Przesławskiego przed szlachetnym Józefem Cynewskim, oskarżenia wyznaniowe wobec żony Łukasza Krzeszowskiego („kapcanka alias żydówka”), znieważenie całego urzędu i żony ławnika Antoniego Szaliczyńskiego oraz protest cechu szewskiego przeciw wyganianiu rzemieślników do robót folwarcznych.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🎻 65. Bójka Taneczna u Żyda Dawida i Spór Stanowy „Szlachcic vs Chłop” (skany #392–#399)</h4>
          <p>
            Siedem zeznań świadków (Franciszek Pełka, Żyd Dawid, Wojciech Żukowski, Grzegorz Grzonka, Tomasz Krupiak ze Stróży, Walenty Szafrański, Sebastian Zdybkiewicz) oraz dublet mikrofilmowy karty 193r (skan #393) odtwarzają bójkę z maja 1755 r. między Józefem Kozą i Michałem Mikołajczykiem a rodziną Grzegorza Pilaszkiewicza, wywołaną zatargiem o taniec ze ślusarczanką i sporami o szlachectwo Stanisława Pilaszkiewicza.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🧵 66. Cechmistrz Krawiecki Szymon Szankiewicz i Awantura na Jarmarku Św. Antoniego (skany #399–#400)</h4>
          <p>
            Zeznania Anny Krzeszowskiej oraz brata cechowego Piotra Gołembiowskiego (18 VI 1755 r.) potwierdzają pełnienie przez rajcę Szymona Szankiewicza urzędu cechmistrza kunsztu krawieckiego oraz dokumentują gwałtowny zatarg Mikołajowej Kawczyny z komornicą Bednarką o kradzież spódnicy, zakończony rzuceniem garnkiem barszczu pod nogi rajcy.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⚖️ 67. Bójka Grabarza Choteckiego z Pilaszkiewiczami u Żyda Izraela na Motkowym (skany #403–#405, #408–#409)</h4>
          <p>
            Wieloświadkowa relacja kotlarza Antoniego Bojarskiego, podcechmistrza kuśnierskiego Jana Zdyba, Pawła Prużyńskiego i niewiernego Izraela z 9 VII 1755 r. ukazuje mechanizm miejskiej samopomocy sąsiedzkiej: gdy Tomasz Pilaszkiewicz gonił grabarza Choteckiego z laską do komory, Żydówka Motkowa wzywała obecnych słowami „pódźcie bronić to katolik”, a cyrulik i burmistrz Grzegorz Pilaszkiewicz sam spoliczkował syna i wygnał go z gospody.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🔍 68. Proces Ławników Krzeszowskiego i Szubertowskiego o Dwie Szkatuły, Wosk i Siedem Kur (skany #411–#414)</h4>
          <p>
            Jesienne inkwizycje z 31 X – 18 XI 1755 r. odsłaniają konflikt w ławie miejskiej: śledztwo dotyczyło plotki o zielonej i czerwonej szkatule (bednarzowej, nie żydowskiej), wydeptania 12 snopów zboża na niwie oraz rewizji w domu przedmieszczanina Antoniego Zdyblika, gdzie w skrzynce matki Małgorzaty Krzeszowskiej znaleziono trzy kawałki wosku od Boguciny.
          </p>
        </div>

        <div class="analytics-card">
          <h4>⛓️ 69. Otwarcie Roku 1756: Cechmistrz Szewski Kazimierz Młynarski w Wieży i Spór o Apelację (skany #415–#418, #422–#423)</h4>
          <p>
            Od fol. 204r (1756 r.) księga rejestruje bunt cechmistrza szewskiego Kazimierza Młynarskiego przeciw sądowi wójtowskiemu i ławnikowi Szymonowi Krzeszowskiemu: odrzucenie apelacji do Trybunału Zamojskiego, areszt w wieży miejskiej, wyzwiska („bodaj go jedenaście kłotek chwyciło w serce”) oraz kontrmanifestację Młynarskiego przeciw ławnikowi Janowi Lubartowskiemu.
          </p>
        </div>

        <div class="analytics-card">
          <h4>📜 70. Protestacje Szlachty (Marcinkowski, Bracia Kofeccy) i Spory Graniczne na Przedmieściu (skany #419–#425)</h4>
          <p>
            Rok 1756 przynosi ostre skargi szlachty rezydującej w mieście: Adama Marcinkowskiego przeciw ławnikowi Adamowi Zandlowi i Krzysztofowi Pilaszkiewiczowi o rugowanie ze stancji oraz braci Samuela i Jędrzeja Kofeckich przeciw wójtowi Michałowi Krzywińskiemu o pobicie przy urzędnikach i ugodę na 24 złp, a także pozwy przedmieszczanina Wojciecha Cwieki z Łukaszem Pałką i Marcinem Morelem.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏛️ 71. Tenory Pozwów Trybunału Zamojskiego i Opiekunowie Ordynacji (skany #431–#434)</h4>
          <p>
            Relacje woźnego przysięgłego Andrzeja Surowiaka z 10 XI 1756 r. zachowały in extenso pełną intytulację kolegialnych Opiekunów Ordynacji Zamojskiej (Jana Jakuba i Józefa Klemensa Zamoyskich, dziekana infułata Jana Aleksandra Trembińskiego oraz Franciszka Dzierżanowskiego) w sprawach apelacyjnych Wojciecha Cwieki oraz braci Kofeckich.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🪵 72. Spór Leśny z Rzeczycy i Ochrona Poddanych Szlacheckich (skany #427–#429)</h4>
          <p>
            Obdukcja i dekret w sprawie Macieja Chorąbały, poddanego ze wsi Rzeczycy dóbr skarbnika Suchodolskiego, dokumentują procedurę oczyszczenia się przysięgą przez Wojciecha Kawkę od zarzutu pobicia w lesie oraz nakaz zwrotu dwóch siekier i uiszczenia grzywny sądowej za niestawiennictwo.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🧺 73. Ochrona Ubogi Wdowy i Kramarki Janowej Rosołowskiej na Jarmarku Św. Marcina (skany #439, #442–#444)</h4>
          <p>
            Wyrok z 11 XI 1756 r. w sprawie zrabowania kramu ubogiej wdowy Janowej Rosołowskiej przez Sebastiana Sedelskiego (wsparty zeznaniem szlachetnej Zofii Chrzanowskiej) dowodzi surowej ochrony drobnego handlu jarmarcznego i karania samowoli grzywną sądową.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🤝 74. Kwitacja Własnoręczna Kofeckich, Zastaw Klina Tokarskiego i Ugoda za 4 złp (skany #446–#450)</h4>
          <p>
            Koniec listopada 1756 r. zamyka głośny konflikt szlachty z urzędem miejskim: Jędrzej Kofecki własnoręcznie skwitował wójta Michała Krzywińskiego (26 XI), Jakub Wróbel zastawił klin Tokarski słudze kościelnemu Wawrzyńcowi Biegajowi za 16 złp (29 XI), a burmistrzowie Pruszkiewicz i Krzeszowski wraz z ławnikiem Tokarczykiem doprowadzili do ugody Morela i Jorgieła z Kofeckimi za 4 złp.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🍯 75. Uniwersał Starosty Józefa Klemensa Zamoyskiego o Szynku Miodnym i Zakaz Wesel Żydowskich (skany #454–#455)</h4>
          <p>
            Karty 223r–223v z początku grudnia 1756 r. łączą dyscyplinę kościelną z monopolem dworskim: sąd na rekwizycję Kustosza ukarał Pawła Kacperskiego grzywną na NMP Różańcową za granie na weselu żydowskim, a starosta lubelski Józef Klemens Zamoyski (30 XI 1756 r. w Zwierzyńcu) zakazał Żydom kraśnickim kupowania miodów przaśnych poza dyspozycją ekonoma Morszkowskiego.
          </p>
        </div>

        <div class="analytics-card">
          <h4>✍️ 76. Kwitacja Hebrajska Herszka Eliaszowicza i Dublet Mikrofilmowy Karty 222v (skany #453, #456)</h4>
          <p>
            Skan #453 stanowi dokładny dublet mikrofilmowy karty 222v (#452), natomiast na karcie 224r (#456) starozakonny Herszek Eliaszowicz złożył własnoręczną kwitację dla Mikołaja Nowaka sygnowaną jednocześnie po polsku i w alfabecie hebrajskim.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🏡 77. Zamiana Domostw na Podsieniu (Wójt Krzywiński vs Michał Matuszkiewicz) za Dopłatą 80 złp (skany #470–#471)</h4>
          <p>
            Kontrakt zamiany (per commutationem) zawarty przed sądem w listopadzie 1756 r. w obecności rajców Grzegorza Pilaszkiewicza i Mikołaja Biegaja oraz ławników Szubertowskiego i Szaliczyńskiego dokumentuje obrót nieruchomościami rynkowymi w Kraśniku wraz z własnoręcznym podpisem wójta Michała Ignacego Krzywińskiego i znakiem krzyża Matuszkiewicza.
          </p>
        </div>

        <div class="analytics-card">
          <h4>🐄 78. Sprawa Rzeźników o Zapowietrzone Bydło w Lesie Borzechowskim i Otwarcie Acta Inquisitionum (skany #464, #472–#475)</h4>
          <p>
            Nowy dział inkwizycji otwarty 7 XII 1756 r. odsłania spór rzeźnika żydowskiego Joela Lejzorowicza z rzeźnikami i burmistrzem Krzeszowskim o pędzenie zapowietrzonego bydła przez las borzechowski oraz drobiazgowe zeznania w sporze Antoniego Kołtona z rodziną Pilaszkiewiczów (34 złp i 15 złp).
          </p>
        </div>
        <div class="analysis-card">
          <h4>👞 79. Zatarg Cechmistrzów Szewskich z Braćmi Posuniakami i Jurysdykcja Dworska (skany #486–#494)</h4>
          <p>
            Dekret w sprawie Wojciecha Stachowicza przeciw Adamowi Posuniakowi o skóry wołowe i mieszanie jurysdykcji dworskiej oraz seria obdukcji i inkwizycji z 27–28 XII 1756 r. odsłaniają krwawy konflikt cechmistrzów szewskich Kazimierza Młynarskiego (z podartym zielonym kontuszem) i Antoniego Okonia z braćmi Adamem, Michałem i Wawrzyńcem Posuniakami.
          </p>
        </div>
        <div class="analysis-card">
          <h4>⚖️ 80. Apelacje do Trybunału Zamojskiego i Procesy Pałki z Cwieką oraz Nowakiem (skany #477–#481, #495–#500)</h4>
          <p>
            Zeznania kilkunastu świadków (w tym niewiernych Litwinowej i krawcowej Ilkowej), wyrok z 18 XII 1756 r. między Wojciechem Cwieką a Mikołajem Nowakiem oraz manifestacje Stanisława Wójcika i Łukasza Pałki z 19 XII 1756 r. dokumentują bezpośrednie powiązania sądowe mieszczan kraśnickich z Trybunałem w Zamościu.
          </p>
        </div>
        <div class="analysis-card">
          <h4>🌾 81. Sukcesje po Stanisławie Mydle i Janie Gąsce (Rola Rogozowska) (skany #483–#484, #487–#489, #496–#498)</h4>
          <p>
            Protokoły dokumentują spór Wojciecha Pałki z Mikołajem Nowakiem o 24 i 30 złp po Stanisławie Mydle (zakończony ugodą na 10 złp) oraz wielowątkową walkę opiekunów dzieci Jana Gąski (Piotra Kilianka i innych) z Janem Czelejem o rolę Rogozowską.
          </p>
        </div>
        <div class="analysis-card">
          <h4>🎞️ 82. Kodykologia Mikrofilmu: Dublety Klatek 234v i 237r (skany #479, #485)</h4>
          <p>
            Weryfikacja klatek Partii 20 wykazała dwa dokładne dublety mikrofilmowe: skan #479 powtarza kartę 234v (skan #478), a skan #485 powtarza kartę 237r (skan #484). Zachowano je w rejestrze z jednoznacznym oznaczeniem w celu pełnej zgodności numeracji 776 skanów z AP Lublin.
          </p>
        </div>
        <div class="analysis-card">
          <h4>🔥 83. Pożar Młyna Grebieńskiego – Zeznanie Młynarczyka Wojciecha Świdzińskiego (skany #506–#507, #510–#511)</h4>
          <p>
            Unikatowy protokół śledczy z grudnia 1756/1757 r.: po wstępnych podejrzeniach rzucanych na Bartłomieja Czeleja, młynarczyk Wojciech Świdziński zeznaje szczegółowo, jak pijany Żyd piekarz rozpalił głownię w młynie, zatrzasnął drzwi i zgubił klucze, doprowadzając do doszczętnego spłonięcia Młyna Grebieńskiego.
          </p>
        </div>
        <div class="analysis-card">
          <h4>🏰 84. Zakaz Apelacji do Dworu Stróżkiego i Mandaty Ordynacji Zamoyskiej (skany #513–#514, #521–#522)</h4>
          <p>
            Manifestacja Wojciecha Stachowicza przeciw Adamowi Posuniakowi przywołuje przywileje fundatorów miasta zakazujące pod grzywnami i więzieniem odwoływania się do dworu stróżkiego, a wpisany in extenso mandat opiekunów Ordynacji Zamoyskiej (Jana Jakuba Zamoyskiego, Jana Aleksandra Granowskiego i Franciszka Dzierżanowskiego) ukazuje procedurę Sądu Komisarskiego Zamku Zamoyskiego.
          </p>
        </div>
        <div class="analysis-card">
          <h4>🌾 85. Dwudziestodwuletni Zastaw Niwki Błuczorskiej i Sukcesja Kaczmarskich (skany #516–#517, #519, #524–#525)</h4>
          <p>
            Dekret między Szymonem Marszałkowskim a braćmi Maciejem i Mikołajem Kawkami rozlicza 22-letnie użytkowanie zastawionej niwki Błuczorskiej (110 złp kapitału, po 5 złp rocznego pożytku, spłata 95 złp na ratuszu), a proces sługi miejskiego Jędrzeja Surowickiego i Jadwigi z Kaczmarskich (1v. Biegonowej) z Baltazarem Kaczmarskim odsłania walkę o równe działy spadkowe sióstr.
          </p>
        </div>
        <div class="analysis-card">
          <h4>🎞️ 86. Kodykologia Partii 21: Dublet #503 (fol. 245v) i Błąd Foliacji 256/255v (skany #502–#503, #524–#525)</h4>
          <p>
            W Partii 21 zidentyfikowano dublet mikrofilmowy skanu #503 (powtarza kartę 245v ze skanu #502) oraz pomyłkę foliacyjną pisarza na końcu składki: skan #524 oznaczono liczbą 256 mimo że kolejny skan #525 wraca do poprawnej foliacji 255v.
          </p>
        </div>
        <div class="analysis-card">
          <h4>🧹 87. Powołanie Generalnego Kominiarza przez Urząd Miejski i Synagogę (skany #544–#546)</h4>
          <p>
            Włączona składka z maja 1756 r. ujawnia wspólne postanowienie rady, ławy i kahału kraśnickiego o powołaniu Jakuba Latosiewicza na generalnego kominiarza za tygodniową pensją z regestru kahałnego — oraz natychmiastową rewizję pożaru sadzy i słomy w kominie Gierszona Catowica.
          </p>
        </div>
        <div class="analysis-card">
          <h4>🪙 88. Proces Starozakonnego Habusia z Rymarczykiem o 37 Czerwonych Złotych (skany #530–#532)</h4>
          <p>
            Nadzwyczajne posiedzenie sądu miejskiego z udziałem gubernatora klucza kraśnickiego Jana Chrzanowskiego i starszych synagogi bada sprawę zgubionego woreczka z 37 czerwonymi złotymi i tynfami, znalezionego przez żonę Jędrzeja Rymarczyka na pogrzebie Katarzyny córki Maliny.
          </p>
        </div>
        <div class="analysis-card">
          <h4>⚖️ 89. Konflikt Deputata Trybunału Marcina Morela z Sądem Miejskim o Zarzuty Korupcji (skany #537–#542)</h4>
          <p>
            Zatarg o podkupienie wieprza za 24 złp między deputatem na Trybunał Zamoyski Marcinem Morelem a Kazimierzem Młynarskim przeradza się w uroczystą remanifestację całego sądu radzieckiego i ławniczego przeciw Morelowi za publiczne zarzucenie sędziom korupcji.
          </p>
        </div>
        <div class="analysis-card">
          <h4>📐 90. Trzy Kondescensje Graniczne i Lustracja Pękniętej Kamienicy Nachymowicza (skany #526, #533–#537, #547–#548)</h4>
          <p>
            Protokoły dokumentują trójstopniową procedurę wizji gruntowej (odnalezienie starych kołków w miedzy między Szymonem Bieleckim a ślusarzem Jakubem Wojciechowskim) oraz techniczną lustrację murowanego domu Lebusia Nachymowicza, którego tylna ściana odeszła na łokieć od ścian pobocznych.
          </p>
        </div>
        <div class="analysis-card">
          <h4>🏛️ 91. Architekt Klasztoru Kraśnickiego Józef Herbst – Autograf z 1757 r. (skan #573)</h4>
          <p>
            Na karcie 280v zachował się unikatowy wpis ugody honorowej z własnoręcznym podpisem Józefa Herbsta, architekta pracującego w 1757 r. przy robotach w klasztorze kraśnickim, który pojednał się z burmistrzem Stanisławem Bryśkiewiczem i jego żoną.
          </p>
        </div>
        <div class="analysis-card">
          <h4>📚 92. Rewizja Ksiąg Wieczystych i Brak Skrzyni Aktowej (skany #559–#560)</h4>
          <p>
            Protokół z maja 1756 r. odsłania dramatyczny stan archiwum miejskiego: wójt kraśnicki stwierdza wobec pospólstwa brak skrzyni i klucza do ksiąg wieczystych oraz pobutwienie protokołów „w koszuli”, z wyjątkiem jednego 16-kartkowego protokołu i podrocznika.
          </p>
        </div>
        <div class="analysis-card">
          <h4>⚖️ 93. Proces Obyczajowy Żony Józefa Nowaka i Surowe Kary Więzienia (skany #553–#556)</h4>
          <p>
            Szczegółowe interrogatoria żony Józefa Nowaka oraz dekret sądu wójtowskiego przeciw Pawłowi Frugie (12 grzywien dla obrazu NMP Różańcowej, 10 Nowakowi, 4 sądowi, 3 dni wieży podczas mszy) ukazują rygor karny miasta wobec przestępstw przeciw obyczajności i samosądów.
          </p>
        </div>
        <div class="analysis-card">
          <h4>🌾 94. Chłopi Księcia Jabłonowskiego z Zakrzowa i Szafarstwo Bez Przysięgi (skany #572–#575)</h4>
          <p>
            Zapiska z 30 V 1757 r. o chłopach ze wsi Zakrzowa księcia Jabłonowskiego, notatka o objęciu szafarstwa bez przysięgi przez Szymona Szymkowskiego i Mikołaja Kawkę oraz rozliczenie jarmarczne Mikołaja Nowaka z Fejdlą Szyjową dokumentują codzienne relacje gospodarcze miasta z dobrami sąsiednimi.
          </p>
        </div>

        <div class=analysis-card>
          <h4>⚖️ 95. Spór Wójta z Burmistrzem o Karty z Protokołów i Kwitacja w Posesji Chorążego (skany #580–#581)</h4>
          <p>
            Skany #580–#581 ukazują ostre napięcia w elicie urzędniczej Kraśnika w czerwcu 1757 r.: wójt <strong>Michał Krzywiński</strong> oskarżył burmistrza <strong>Łukasza Krzeszowskiego</strong> o pomówienie dotyczące wyrywania kart z protokołów miejskich i ich sprzedaży deputatowi <strong>Marcinowi Morelowi</strong>. Równolegle burmistrz i pisarz <strong>Stanisław Bryśkiewicz</strong> spisał kwitację z poddanym franciszkańskim <strong>Michałem Stachowiczem</strong> (w posesji chorążego lubelskiego <strong>Jerzego Pietrowskiego</strong>) oraz manifestował przeciw ławnikowi <strong>Janowi Lubartowskiemu</strong> za trzyletnie zniesławianie jego żony.
          </p>
        </div>

        <div class=analysis-card>
          <h4>📜 96. Oblata Skryptu Braci Kofeckich i Areszt na Dobrach Tyrawczyzna (skany #582–#584)</h4>
          <p>
            Na skanach #582–#584 oblatowano skrypt dłużny z 17 czerwca 1756 r., w którym <strong>Andrzej (Jędrzej) Kofecki</strong> przyznał bratu rodzonemu <strong>Samuelowi Kofeckiemu</strong> dług w wysokości 158 złp 12 gr (plus 23 gr za wóz). Wobec sporów o spłatę u wójta Krzywińskiego, Samuel Kofecki zabezpieczył wierzytelność aresztem na dobrach <em>Tyrawczyzna</em> i niwie od <strong>Szymona Marszałkowskiego</strong>, a własny areszt na 4 złp u Kofeckiego dołożył starozakonny <strong>Gierszon Catowic</strong>.
          </p>
        </div>

        <div class=analysis-card>
          <h4>⛪ 97. Proces Klasztoru Kanoników Regularnych z Maciejem Frugą o 33 Korce Żyta (skany #589–#590)</h4>
          <p>
            Karty 288v–289r (skany #589–#590) dokumentują obszerny dekret sądu łączonego w sprawie proboszcza kraśnickiego <strong>ks. Jakuba Maliszewskiego</strong> i całego Konwentu przeciw <strong>Maciejowi Frudze</strong> o 33 korce żyta wycenione po 6 złp na 202 złp 15 gr. Po odliczeniu uznanych przez dłużnika 26 złp 6 gr sąd rozłożył pozostałe 176 złp 9 gr na cztery raty po 44 złp 2 gr (1757–1759), uwzględniając także rozliczenia za dwuletnią pracę Frugi w winiarni klasztornej.
          </p>
        </div>

        <div class=analysis-card>
          <h4>🔄 98. Odwrócona Sekcja Księgi i Raptularz Inkwizycyjny z 1752 r. (skany #585–#600)</h4>
          <p>
            Karty 286v–294v (skany #585–#599) zostały zapisane i zmikrofilmowane do góry nogami względem reszty kodeksu. Wewnątrz tej odwróconej części obok akt z 1757 r. (m.in. sprawa Mośka Lewkowicza o wapno na skanach #586–#587) znajduje się wszyty <strong>raptularz inkwizycyjny z 1752 r.</strong> (#593–#599), zawierający m.in. spór o podkupienie wieprza za 24 złp u Franciszka Wstruskiowskiego, zeznania z bójki karczemnej Pawła Frugi z Nowakami i Wawrzyńcem Tokarzem oraz inkwizycję o górę Sowińską. Od skanu #600 (fol. 295r) księga wraca do normalnej orientacji i roku 1759.
          </p>
        </div>

        <div class=analysis-card>
          <h4>🔨 99. Zatarg Cechmistrza Kowalskiego Kazimierza Młynarskiego z Urzędem i Rotmistrzem (skany #606–#607, #618)</h4>
          <p>
            Zapis z soboty 1758 r. (zdublowany na skanach #606–#607) odsłania gwałtowny konflikt w elicie rzemieślniczej: cechmistrz kowalski i ślusarski <strong>Kazimierz Młynarski</strong> na ratuszu przed krucyfiksem oświadczył, że <em>„Pana Wójta się nie boię”</em>, lżąc sławetnego <strong>Antoniego Siekierzyńskiego</strong> oraz rotmistrza miejskiego <strong>Wojciecha Okuńskiego</strong>. Wątek powraca na skanie #618 w skardze <em>konter-magistra</em> kowalskiego <strong>Franciszka Bielickiego</strong> na tegoż cechmistrza.
          </p>
        </div>

        <div class=analysis-card>
          <h4>🏪 100. Protestacja Kramarzy Przeciw Arendarzowi Aznerowi o Targowe Niedzielne (skany #619–#620)</h4>
          <p>
            Na skanach #619–#620 (dublet mikrofilmowy) kramarz <strong>Kazimierz Żebrowski</strong> w imieniu wszystkich kolegów kramarzy wniósł uroczystą manifestację przeciw niewiernemu arendarzowi <strong>Aznerowi</strong>, który wbrew dawnemu zwyczajowi i kontraktowi wybierał od kupców nie tylko jarmarczne, ale także przedjarmarczne, podjarmarczne oraz targowe niedzielne.
          </p>
        </div>

        <div class=analysis-card>
          <h4>⚖️ 101. Anulowanie Kompromisu i Analiza Trzech Testamentów w Sprawie Petrykowskiego (skany #621–#624)</h4>
          <p>
            Wyrok w sprawie szlachetnego <strong>Antoniego Petrykowskiego</strong> przeciw wdowie <strong>Teresie Słomkowskiej</strong> (#621–#624) stanowi unikatowy przykład kontroli sądowej nad sądownictwem polubownym: po zbadaniu testamentów Pawła Słomkowskiego (150 złp), ciotki Zofii Popławskiej i Kazimierza Słomkowskiego (50 złp) sąd obopólny anulował kompromis przyjaciół (wyceniający połowę niwki na 60 złp z dopłatą 20 złp 20 gr) i przyznał sukcesorom prawo do połowy gruntu pod warunkiem złożenia przysięgi.
          </p>
        </div>

        <div class=analysis-card>
          <h4>🎖️ 102. Żołnierz Artylerii Koronnej Kazimierz Tokarski w Sporach Sukcesyjnych (skany #617–#618, #621, #624–#625)</h4>
          <p>
            Urodzony <strong>Kazimierz Tokarski</strong>, żołnierz artylerii koronnej, wystąpił w czerwcu 1758 r. jako sukcesor po ojcu <strong>Tomaszu Tokarzu</strong> przeciw grupie mieszczan i przedmieszczan (<strong>Jan Łypa</strong>, <strong>Wojciech Wojtczak</strong>, <strong>Jakub Bielicki</strong>, <strong>Wojciech Wilczyński</strong>, <strong>Jędrzej Rypkowski</strong>). Wobec okazania dokumentów przez pozwanych sąd zobowiązał żołnierza do przedstawienia autentycznego ekstraktu rezygnacji z ksiąg radzieckich pod rygorem upadku w sprawie (#625).
          </p>
        </div>
      </div>
"""

main_data_json = json.dumps(main_data, ensure_ascii=False)
gen_data_json = json.dumps(gen_data, ensure_ascii=False)

html_template = f"""{head_part}
</head>
<body>

  <!-- 1. NAGŁÓWEK Z LINKIEM POWROTNYM -->
  <header>
    <a href="index.html" class="portal-back-link">← Powrót do Portalu Głównego Jednostek</a><br>
    <div class="header-badge">ARCHIWUM PAŃSTWOWE W LUBLINIE • SYGN. 35/40/0/1/17 (DAWNY TOM 12 / MIKR. 110404)</div>
    <h1>Akta Miasta Kraśnika (1651–1759)</h1>
    <p class="header-subtitle">
      Obszerny kodeks czynności sądownictwa wójtowsko-ławniczego i sądu łączonego: sesje z 1700, 1730–1731 i 1753–1754 r. oraz wszyte poszyty z 1651, 1694, 1726 i 1729 r. – procesy o zabójstwa, cechy, obrót kamienicami rynkowymi oraz słownik genealogiczny (Partie 1–13: 325 skanów).
    </p>
  </header>

  <!-- 2. PASEK GŁÓWNYCH ZAKŁADEK -->
  <nav class="tabs-nav">
    <button class="tab-btn active" onclick="switchTab('main-tab', this)">
      <span>📊 Tabela Indeksowa Skanów</span>
      <span class="tab-badge" id="mainTabBadge">{len(main_data)}</span>
    </button>
    <button class="tab-btn gold-tab" onclick="switchTab('genealogy-tab', this)">
      <span>🌳 Słownik Genealogiczny Mieszkańców</span>
      <span class="tab-badge" id="genTabBadge">{len(gen_data)}</span>
    </button>
    <button class="tab-btn" onclick="switchTab('monograph-tab', this)">
      <span>🏛️ Pełna Synteza Monograficzna</span>
    </button>
    <button class="tab-btn" onclick="switchTab('analytics-tab', this)">
      <span>🔍 Kluczowe Odkrycia i Przełomy</span>
    </button>
  </nav>

  <!-- 3. WYCENTROWANY KONTENER GŁÓWNY -->
  <main class="container">
    
    <!-- ZAKŁADKA 1: TABELA GŁÓWNA SKANÓW -->
    <section id="main-tab" class="tab-content active">
      <div class="stats-grid">
        <div class="stat-card gold">
          <div class="stat-title">Zindeksowane Skany</div>
          <div class="stat-value" id="kpiMainCount">{len(main_data)}</div>
          <div class="stat-desc">Partie 1–13 (fol. 1r–159v: lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1754)</div>
        </div>
        <div class="stat-card purple">
          <div class="stat-title">Unikalne Profile Mieszkańców</div>
          <div class="stat-value" id="kpiGenCount">{len(gen_data)}</div>
          <div class="stat-desc">Wariant 2 (0 duplikatów tożsamości)</div>
        </div>
        <div class="stat-card cyan">
          <div class="stat-title">Transkrypcje In Extenso</div>
          <div class="stat-value">100%</div>
          <div class="stat-desc">Pełny odczyt całych kart bez wycinków</div>
        </div>
        <div class="stat-card success">
          <div class="stat-title">Karty Analityczne</div>
          <div class="stat-value">54</div>
          <div class="stat-desc">Kluczowe odkrycia źródłowe</div>
        </div>
      </div>

      <div class="controls-panel">
        <div class="search-box">
          <input type="text" id="mainSearchInput" placeholder="Szukaj w indeksie skanów (nazwisko, sprawa, kategoria, kwoty)..." oninput="filterMainData()">
        </div>
        <div class="filter-group">
          <select id="mainCategoryFilter" onchange="filterMainData()">
            <option value="">Wszystkie kategorie akt</option>
          </select>
          <select id="mainCenturyFilter" onchange="filterMainData()">
            <option value="">Wszystkie lata / okresy</option>
            <option value="1651">Rok 1651 (wszytka poszytowa)</option>
            <option value="1694">Rok 1694 (wszytka poszytowa)</option>
            <option value="1700">Rok 1700</option>
            <option value="1726">Rok 1726 (dekret rabinacki)</option>
            <option value="1729">Rok 1729 (oblata)</option>
            <option value="1730">Rok 1730</option>
            <option value="1731">Rok 1731</option>
            <option value="1753">Rok 1753</option>
            <option value="1754">Rok 1754</option>
          </select>
          <button class="btn btn-secondary" onclick="resetMainFilters()">Resetuj filtry</button>
          <button class="btn btn-gold" onclick="exportMainCSV()">Eksportuj Tabelę (CSV)</button>
        </div>
      </div>

      <div class="pagination-bar">
        <div class="pagination-info" id="mainPaginationInfo">Pokazywanie pozycji...</div>
        <div class="pagination-controls">
          <button class="btn btn-secondary btn-sm" id="mainPrevBtn" onclick="prevMainPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="mainPageIndicator">1 / 1</span>
          <button class="btn btn-secondary btn-sm" id="mainNextBtn" onclick="nextMainPage()">Następna ›</button>
          <span style="font-size:0.8rem; color:var(--text-muted); margin-left:0.5rem;">Skocz do:</span>
          <input type="number" id="mainJumpInput" min="1" value="1" style="width:55px; padding:0.2rem 0.4rem; background:var(--bg-primary); border:1px solid var(--border); color:#fff; border-radius:4px; text-align:center;">
          <button class="btn btn-secondary btn-sm" onclick="jumpMainPage()">Idź</button>
        </div>
      </div>

      <div class="table-wrapper">
        <table id="mainTable">
          <thead>
            <tr>
              <th onclick="sortMainTable('nr_skanu')">Skan ↕</th>
              <th onclick="sortMainTable('strona_pagina')">Pagina ↕</th>
              <th onclick="sortMainTable('data_rok')">Rok ↕</th>
              <th>Osoby i Podmioty</th>
              <th onclick="sortMainTable('kategoria')">Kategoria ↕</th>
              <th>Opis Sprawy / Treść Aktu</th>
              <th>Kwoty / Podatki</th>
            </tr>
          </thead>
          <tbody id="mainTableBody">
            <!-- Renderowane dynamicznie -->
          </tbody>
        </table>
      </div>

      <div class="pagination-bar" style="margin-top:1rem;">
        <div class="pagination-info" id="mainPaginationInfoBot">Pokazywanie pozycji...</div>
        <div class="pagination-controls">
          <button class="btn btn-secondary btn-sm" id="mainPrevBtnBot" onclick="prevMainPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="mainPageIndicatorBot">1 / 1</span>
          <button class="btn btn-secondary btn-sm" id="mainNextBtnBot" onclick="nextMainPage()">Następna ›</button>
          <span style="font-size:0.8rem; color:var(--text-muted); margin-left:0.5rem;">Skocz do:</span>
          <input type="number" id="mainJumpInputBot" min="1" value="1" onchange="jumpMainPage(this.value)" style="width:55px; padding:0.2rem 0.4rem; background:var(--bg-primary); border:1px solid var(--border); color:#fff; border-radius:4px; text-align:center;">
          <button class="btn btn-secondary btn-sm" onclick="jumpMainPage()">Idź</button>
        </div>
      </div>
    </section>

    <!-- ZAKŁADKA 2: SŁOWNIK GENEALOGICZNY -->
    <section id="genealogy-tab" class="tab-content">
      <div class="stats-grid">
        <div class="stat-card gold">
          <div class="stat-title">Zindeksowane Osoby</div>
          <div class="stat-value" id="genStatCount">{len(gen_data)}</div>
          <div class="stat-desc">Wariant 2: 1 osoba fizyczna = 1 rekord</div>
        </div>
        <div class="stat-card purple">
          <div class="stat-title">Łączna Liczba Wzmianek</div>
          <div class="stat-value" id="genMentionsCount">0</div>
          <div class="stat-desc">Zeznania, dekrety, transakcje, asysty</div>
        </div>
        <div class="stat-card cyan">
          <div class="stat-title">De-duplikacja Tożsamości</div>
          <div class="stat-value">100%</div>
          <div class="stat-desc">Zero duplikatów tożsamości</div>
        </div>
        <div class="stat-card success">
          <div class="stat-title">Warianty Onomastyczne</div>
          <div class="stat-value">100%</div>
          <div class="stat-desc">Pełna synchronizacja z wyszukiwarką</div>
        </div>
      </div>

      <div class="info-box">
        <strong>🌳 Zasady Metodyczne Słownika Genealogicznego (Wariant 2):</strong><br>
        Każda osoba fizyczna posiada dokładnie <strong>jeden unikalny profil</strong> w bazie (z rozróżnieniem epok 1651 i 1700 r.). Wszelkie warianty fonetyczne i oboczności paleograficzne odnotowane w nawiasach kwadratowych transkrypcji zostały zintegrowane w dedykowanym polu wariantów i są w pełni przeszukiwalne przez poniższą wyszukiwarkę na żywo. Kliknij w wiersz osoby, aby otworzyć szczegółowy modal z wykazem wszystkich jej wystąpień w kodeksie.
      </div>

      <div class="controls-panel">
        <div class="search-box">
          <input type="text" id="genSearchInput" placeholder="Szukaj osoby (nazwisko, imię, wariant, zawód, przedmieście, rola)..." oninput="filterGenData()">
        </div>
        <div class="filter-group">
          <select id="genRoleFilter" onchange="filterGenData()">
            <option value="">Wszystkie role i urzędy</option>
          </select>
          <select id="genDistrictFilter" onchange="filterGenData()">
            <option value="">Wszystkie dzielnice / przedmieścia</option>
          </select>
          <button class="btn btn-secondary" onclick="resetGenFilters()">Resetuj filtry</button>
          <button class="btn btn-gold" onclick="exportGenCSV()">Eksportuj Słownik (CSV)</button>
        </div>
      </div>

      <div class="pagination-bar">
        <div class="pagination-info" id="genPaginationInfo">Pokazywanie profili...</div>
        <div class="pagination-controls">
          <button class="btn btn-secondary btn-sm" id="genPrevBtn" onclick="prevGenPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="genPageIndicator">1 / 1</span>
          <button class="btn btn-secondary btn-sm" id="genNextBtn" onclick="nextGenPage()">Następna ›</button>
          <span style="font-size:0.8rem; color:var(--text-muted); margin-left:0.5rem;">Skocz do:</span>
          <input type="number" id="genJumpInput" min="1" value="1" style="width:55px; padding:0.2rem 0.4rem; background:var(--bg-primary); border:1px solid var(--border); color:#fff; border-radius:4px; text-align:center;">
          <button class="btn btn-secondary btn-sm" onclick="jumpGenPage()">Idź</button>
        </div>
      </div>

      <div class="table-wrapper">
        <table id="genTable">
          <thead>
            <tr>
              <th onclick="sortGenTable('lp')">Lp. ↕</th>
              <th onclick="sortGenTable('nazwisko')">Nazwisko ↕</th>
              <th onclick="sortGenTable('imie')">Imię ↕</th>
              <th onclick="sortGenTable('miejsce')">Miejsce zamieszkania ↕</th>
              <th onclick="sortGenTable('funkcja')">Funkcja społeczna ↕</th>
              <th>Roboczo: Nr skanów ↕</th>
              <th onclick="sortGenTable('zakres_lat')">Zakres lat ↕</th>
            </tr>
          </thead>
          <tbody id="genTableBody">
            <!-- Renderowane dynamicznie -->
          </tbody>
        </table>
      </div>

      <div class="pagination-bar" style="margin-top:1rem;">
        <div class="pagination-info" id="genPaginationInfoBot">Pokazywanie profili...</div>
        <div class="pagination-controls">
          <button class="btn btn-secondary btn-sm" id="genPrevBtnBot" onclick="prevGenPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="genPageIndicatorBot">1 / 1</span>
          <button class="btn btn-secondary btn-sm" id="genNextBtnBot" onclick="nextGenPage()">Następna ›</button>
          <span style="font-size:0.8rem; color:var(--text-muted); margin-left:0.5rem;">Skocz do:</span>
          <input type="number" id="genJumpInputBot" min="1" value="1" onchange="jumpGenPage(this.value)" style="width:55px; padding:0.2rem 0.4rem; background:var(--bg-primary); border:1px solid var(--border); color:#fff; border-radius:4px; text-align:center;">
          <button class="btn btn-secondary btn-sm" onclick="jumpGenPage()">Idź</button>
        </div>
      </div>
    </section>

    <!-- ZAKŁADKA 3: MONOGRAFIA -->
    <section id="monograph-tab" class="tab-content">
      {monograph_html}
    </section>

    <!-- ZAKŁADKA 4: ANALITYKA -->
    <section id="analytics-tab" class="tab-content">
      {analytics_html}
    </section>
  </main>

  <!-- 4. MODAL POP-UP (3 ZAKŁADKI DLA SKANU / MODAL OSOBY UKRYWA PASKI) -->
  <div id="detailModal" class="modal">
    <div class="modal-content">
      <div class="modal-header">
        <h3 id="modalTitle">Szczegóły</h3>
        <button class="modal-close" onclick="closeModal()">&times;</button>
      </div>
      <div id="modalTabsBar" class="modal-tabs-bar" style="display: none;">
        <button class="modal-tab-btn active" id="tabBtnMeta" onclick="switchModalTab('meta')">📋 Opis i metadane</button>
        <button class="modal-tab-btn" id="tabBtnTrans" onclick="switchModalTab('trans')">📜 Transkrypcja</button>
        <button class="modal-tab-btn" id="tabBtnLink" onclick="switchModalTab('link')">🔗 Link do oryginału</button>
      </div>
      <div class="modal-body" id="modalBody">
        <!-- Wstrzykiwane dynamicznie przez JS -->
      </div>
    </div>
  </div>

  <script>
    // DANE ŹRÓDŁOWE J17
    const mainData = {main_data_json};
    const genData = {gen_data_json};

    // DYNAMICZNA SYNCHRONIZACJA LICZNIKÓW (ZERO HARDCODOWANIA)
    if (document.getElementById('mainTabBadge')) document.getElementById('mainTabBadge').innerText = mainData.length;
    if (document.getElementById('genTabBadge')) document.getElementById('genTabBadge').innerText = genData.length;
    if (document.getElementById('kpiMainCount')) document.getElementById('kpiMainCount').innerText = mainData.length;
    if (document.getElementById('kpiGenCount')) document.getElementById('kpiGenCount').innerText = genData.length;
    if (document.getElementById('genStatCount')) document.getElementById('genStatCount').innerText = genData.length;

    let totalMentionsCalc = 0;
    genData.forEach(p => {{
      totalMentionsCalc += (p.wystapienia ? p.wystapienia.length : (p.liczba_wystapien || 1));
    }});
    if (document.getElementById('genMentionsCount')) {{
      document.getElementById('genMentionsCount').innerText = totalMentionsCalc;
    }}

    // ZMIENNE STANU PAGINACJI I FILTROWANIA
    let filteredMain = [...mainData];
    let mainCurrentPage = 1;
    const mainPageSize = 25;
    let mainSortCol = 'nr_skanu';
    let mainSortAsc = true;

    let filteredGen = [...genData];
    let genCurrentPage = 1;
    const genPageSize = 25;
    let genSortCol = 'lp';
    let genSortAsc = true;

    let currentModalScan = null;

    // PRZEŁĄCZANIE ZAKŁADEK GŁÓWNYCH
    function switchTab(tabId, btn) {{
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      const target = document.getElementById(tabId);
      if (target) target.classList.add('active');
      if (btn) btn.classList.add('active');
    }}

    // POMOCNICZA FUNKCJA ESCAPE HTML
    function escapeHtml(str) {{
      if (str === null || str === undefined) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }}

    // FILTROWANIE I RENDEROWANIE TABELI GŁÓWNEJ
    function filterMainData() {{
      const q = (document.getElementById('mainSearchInput').value || '').toLowerCase().trim();
      const cat = document.getElementById('mainCategoryFilter').value;
      const year = document.getElementById('mainCenturyFilter').value;

      filteredMain = mainData.filter(d => {{
        if (cat && d.kategoria !== cat) return false;
        if (year && !String(d.data_rok).includes(year)) return false;
        if (!q) return true;
        const opis = d.opis_pozycji || d.opis_sprawy || '';
        const kwoty = d.kwoty_miary || d.kwoty_podatki || '';
        return (
          String(d.nr_skanu).includes(q) ||
          (d.strona_pagina && d.strona_pagina.toLowerCase().includes(q)) ||
          (d.osoby_podmioty && d.osoby_podmioty.toLowerCase().includes(q)) ||
          (d.kategoria && d.kategoria.toLowerCase().includes(q)) ||
          opis.toLowerCase().includes(q) ||
          kwoty.toLowerCase().includes(q) ||
          (d.transkrypcja && d.transkrypcja.toLowerCase().includes(q))
        );
      }});

      mainCurrentPage = 1;
      renderMainTable();
    }}

    function resetMainFilters() {{
      document.getElementById('mainSearchInput').value = '';
      document.getElementById('mainCategoryFilter').value = '';
      document.getElementById('mainCenturyFilter').value = '';
      filteredMain = [...mainData];
      mainCurrentPage = 1;
      renderMainTable();
    }}

    function sortMainTable(col) {{
      if (mainSortCol === col) {{
        mainSortAsc = !mainSortAsc;
      }} else {{
        mainSortCol = col;
        mainSortAsc = true;
      }}
      filteredMain.sort((a, b) => {{
        let vA = a[col], vB = b[col];
        if (col === 'nr_skanu') {{
          vA = parseInt(vA) || 0;
          vB = parseInt(vB) || 0;
        }} else {{
          vA = String(vA || '').toLowerCase();
          vB = String(vB || '').toLowerCase();
        }}
        if (vA < vB) return mainSortAsc ? -1 : 1;
        if (vA > vB) return mainSortAsc ? 1 : -1;
        return 0;
      }});
      renderMainTable();
    }}

    function renderMainTable() {{
      const tbody = document.getElementById('mainTableBody');
      const totalPages = Math.ceil(filteredMain.length / mainPageSize) || 1;
      if (mainCurrentPage > totalPages) mainCurrentPage = totalPages;

      const start = (mainCurrentPage - 1) * mainPageSize;
      const end = start + mainPageSize;
      const pageData = filteredMain.slice(start, end);

      const infoText = `Pokazywane ${{filteredMain.length > 0 ? start + 1 : 0}}–${{Math.min(end, filteredMain.length)}} z ${{filteredMain.length}} pozycji`;
      const pageText = `${{mainCurrentPage}} / ${{totalPages}}`;

      ['mainPaginationInfo', 'mainPaginationInfoBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.innerText = infoText;
      }});
      ['mainPageIndicator', 'mainPageIndicatorBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.innerText = pageText;
      }});
      ['mainJumpInput', 'mainJumpInputBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) {{ el.max = totalPages; el.value = mainCurrentPage; }}
      }});
      ['mainPrevBtn', 'mainPrevBtnBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.disabled = (mainCurrentPage <= 1);
      }});
      ['mainNextBtn', 'mainNextBtnBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.disabled = (mainCurrentPage >= totalPages);
      }});

      if (pageData.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:2rem; color:var(--text-muted);">Brak wyników spełniających kryteria.</td></tr>';
        return;
      }}

      let html = '';
      pageData.forEach(r => {{
        const opis = r.opis_pozycji || r.opis_sprawy || '';
        const kwoty = r.kwoty_miary || r.kwoty_podatki || '—';
        html += `
          <tr onclick="openMainModal(${{r.nr_skanu}})">
            <td style="font-family:'JetBrains Mono', monospace; font-weight:700; color:var(--gold-primary);">#${{r.nr_skanu}}</td>
            <td style="font-family:'JetBrains Mono', monospace; font-size:0.8rem;">${{escapeHtml(r.strona_pagina)}}</td>
            <td><span class="badge-years">${{escapeHtml(r.data_rok)}}</span></td>
            <td>${{escapeHtml(r.osoby_podmioty || '—')}}</td>
            <td><span style="font-size:0.8rem; font-weight:600; color:#cbd5e1;">${{escapeHtml(r.kategoria)}}</span></td>
            <td style="color:#cbd5e1; font-size:0.85rem;">${{escapeHtml(opis)}}</td>
            <td style="font-family:'JetBrains Mono', monospace; font-size:0.8rem; color:#e2e8f0;">${{escapeHtml(kwoty)}}</td>
          </tr>
        `;
      }});
      tbody.innerHTML = html;
    }}

    function prevMainPage() {{ if (mainCurrentPage > 1) {{ mainCurrentPage--; renderMainTable(); }} }}
    function nextMainPage() {{ const totalPages = Math.ceil(filteredMain.length / mainPageSize); if (mainCurrentPage < totalPages) {{ mainCurrentPage++; renderMainTable(); }} }}
    function jumpMainPage() {{
      const val = parseInt(document.getElementById('mainJumpInput').value);
      const totalPages = Math.ceil(filteredMain.length / mainPageSize);
      if (val >= 1 && val <= totalPages) {{
        mainCurrentPage = val;
        renderMainTable();
      }}
    }}

    // FILTROWANIE I RENDEROWANIE TABELI GENEALOGICZNEJ
    function filterGenData() {{
      const q = (document.getElementById('genSearchInput').value || '').toLowerCase().trim();
      const role = document.getElementById('genRoleFilter').value;
      const dist = document.getElementById('genDistrictFilter').value;

      filteredGen = genData.filter(d => {{
        if (role && (!d.funkcja || !d.funkcja.includes(role))) return false;
        if (dist && (!d.miejsce || !d.miejsce.includes(dist))) return false;
        if (!q) return true;
        return (
          (d.nazwisko && d.nazwisko.toLowerCase().includes(q)) ||
          (d.imie && d.imie.toLowerCase().includes(q)) ||
          (d.wariant_nazwiska && d.wariant_nazwiska.toLowerCase().includes(q)) ||
          (d.miejsce && d.miejsce.toLowerCase().includes(q)) ||
          (d.funkcja && d.funkcja.toLowerCase().includes(q)) ||
          (d.skany_roboczo && d.skany_roboczo.toLowerCase().includes(q))
        );
      }});

      genCurrentPage = 1;
      renderGenTable();
    }}

    function resetGenFilters() {{
      document.getElementById('genSearchInput').value = '';
      document.getElementById('genRoleFilter').value = '';
      document.getElementById('genDistrictFilter').value = '';
      filteredGen = [...genData];
      genCurrentPage = 1;
      renderGenTable();
    }}

    function sortGenTable(col) {{
      if (genSortCol === col) {{
        genSortAsc = !genSortAsc;
      }} else {{
        genSortCol = col;
        genSortAsc = true;
      }}
      filteredGen.sort((a, b) => {{
        let vA = a[col], vB = b[col];
        if (col === 'lp') {{
          vA = parseInt(vA) || 0;
          vB = parseInt(vB) || 0;
        }} else {{
          vA = String(vA || '').toLowerCase();
          vB = String(vB || '').toLowerCase();
        }}
        if (vA < vB) return genSortAsc ? -1 : 1;
        if (vA > vB) return genSortAsc ? 1 : -1;
        return 0;
      }});
      renderGenTable();
    }}

    function renderGenTable() {{
      const tbody = document.getElementById('genTableBody');
      const totalPages = Math.ceil(filteredGen.length / genPageSize) || 1;
      if (genCurrentPage > totalPages) genCurrentPage = totalPages;

      const start = (genCurrentPage - 1) * genPageSize;
      const end = start + genPageSize;
      const pageData = filteredGen.slice(start, end);

      const infoText = `Pokazywane ${{filteredGen.length > 0 ? start + 1 : 0}}–${{Math.min(end, filteredGen.length)}} z ${{filteredGen.length}} profili`;
      const pageText = `${{genCurrentPage}} / ${{totalPages}}`;

      ['genPaginationInfo', 'genPaginationInfoBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.innerText = infoText;
      }});
      ['genPageIndicator', 'genPageIndicatorBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.innerText = pageText;
      }});
      ['genJumpInput', 'genJumpInputBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) {{ el.max = totalPages; el.value = genCurrentPage; }}
      }});
      ['genPrevBtn', 'genPrevBtnBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.disabled = (genCurrentPage <= 1);
      }});
      ['genNextBtn', 'genNextBtnBot'].forEach(id => {{
        const el = document.getElementById(id);
        if (el) el.disabled = (genCurrentPage >= totalPages);
      }});

      if (pageData.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:2rem; color:var(--text-muted);">Brak wyników spełniających kryteria.</td></tr>';
        return;
      }}

      let html = '';
      pageData.forEach(p => {{
        let surnameDisplay = `<strong>${{escapeHtml(p.nazwisko)}}</strong>`;
        if (p.wariant_nazwiska) {{
          surnameDisplay += `<div style="font-size:0.75rem; color:#94a3b8; margin-top:2px; display:inline-block; padding:1px 5px; background:rgba(255,255,255,0.05); border-radius:3px; border:1px solid #334155;">wariant: ${{escapeHtml(p.wariant_nazwiska)}}</div>`;
        }}

        html += `
          <tr onclick="openGenModal(${{p.lp}})">
            <td style="font-family:'JetBrains Mono', monospace; font-weight:700; color:var(--gold-primary);">${{p.lp}}</td>
            <td>${{surnameDisplay}}</td>
            <td><strong>${{escapeHtml(p.imie)}}</strong></td>
            <td><span class="badge-district">${{escapeHtml(p.miejsce)}}</span></td>
            <td><span class="badge-role">${{escapeHtml(p.funkcja)}}</span></td>
            <td style="font-family:'JetBrains Mono', monospace; font-size:0.8rem; color:var(--gold-primary);">${{escapeHtml(p.skany_roboczo)}}</td>
            <td><span class="badge-years">${{escapeHtml(p.zakres_lat)}}</span></td>
          </tr>
        `;
      }});
      tbody.innerHTML = html;
    }}

    function prevGenPage() {{ if (genCurrentPage > 1) {{ genCurrentPage--; renderGenTable(); }} }}
    function nextGenPage() {{ const totalPages = Math.ceil(filteredGen.length / genPageSize); if (genCurrentPage < totalPages) {{ genCurrentPage++; renderGenTable(); }} }}
    function jumpGenPage() {{
      const val = parseInt(document.getElementById('genJumpInput').value);
      const totalPages = Math.ceil(filteredGen.length / genPageSize);
      if (val >= 1 && val <= totalPages) {{
        genCurrentPage = val;
        renderGenTable();
      }}
    }}

    // OBSŁUGA MODALI
    function openMainModal(scanNr) {{
      const item = mainData.find(d => parseInt(d.nr_skanu) === parseInt(scanNr));
      if (!item) return;

      currentModalScan = item;
      document.getElementById('modalTitle').innerText = `SKAN #${{item.nr_skanu}} (${{item.strona_pagina || ''}}) – ${{item.data_rok || ''}}`.toUpperCase();
      
      const tabsBar = document.getElementById('modalTabsBar');
      if (tabsBar) tabsBar.style.display = 'flex';
      switchModalTab('meta');

      const transFormatted = item.transkrypcja ? escapeHtml(item.transkrypcja).replace(/\\n/g, '<br>') : '<em style="color:#94a3b8;">Brak transkrypcji tekstowej dla tego skanu.</em>';
      const opis = item.opis_pozycji || item.opis_sprawy || '';
      const kwoty = item.kwoty_miary || item.kwoty_podatki || 'Brak danych finansowych';

      document.getElementById('modalBody').innerHTML = `
        <div id="modalTabContentMeta" class="modal-tab-content">
          <div class="modal-section">
            <div class="modal-section-title">Identyfikacja archiwalna i kodykologiczna</div>
            <div><strong>Jednostka:</strong> AP Lublin, Akta miasta Kraśnika, sygn. 35/40/0/1/17 (dawny Tom 12 / mikr. 110404)</div>
            <div><strong>Oznaczenie skanu:</strong> Skan #${{item.nr_skanu}} &nbsp;|&nbsp; <strong>Paginacja oryginalna:</strong> ${{escapeHtml(item.strona_pagina)}}</div>
            <div><strong>Datacja zapisu:</strong> <span class="badge-years">${{escapeHtml(item.data_rok)}}</span> &nbsp;|&nbsp; <strong>Kategoria:</strong> <span class="badge-role">${{escapeHtml(item.kategoria)}}</span></div>
          </div>
          
          <div class="modal-section">
            <div class="modal-section-title">Regest i opis historyczno-dyplomatyczny</div>
            <p style="line-height:1.6; color:#e2e8f0; font-size:0.95rem;">${{escapeHtml(opis)}}</p>
          </div>

          <div class="modal-section">
            <div class="modal-section-title">Występujące osoby, instytucje i urzędy</div>
            <p style="color:#cbd5e1; font-size:0.9rem;">${{escapeHtml(item.osoby_podmioty || 'Brak danych')}}</p>
          </div>

          <div class="modal-section">
            <div class="modal-section-title">Wymiary finansowe, taksy i jednostki monetarne</div>
            <p style="font-family:'JetBrains Mono', monospace; color:var(--gold-primary); font-size:0.9rem;">${{escapeHtml(kwoty)}}</p>
          </div>
        </div>

        <div id="modalTabContentTrans" class="modal-tab-content" style="display:none;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
            <span style="font-size:0.85rem; color:var(--text-muted);">Transkrypcja dyplomatyczna in extenso (rygor dosłowności ze wskazaniem wariantów [?]):</span>
            <button class="btn btn-secondary btn-sm" onclick="copyTranscription()">📋 Kopiuj tekst</button>
          </div>
          <div class="transcription-viewer" id="transcriptionText">${{transFormatted}}</div>
        </div>

        <div id="modalTabContentLink" class="modal-tab-content" style="display:none;">
          <div class="modal-section">
            <div class="modal-section-title">Dostęp do skanu cyfrowego w zasobie Archiwum Państwowego</div>
            <p style="color:#cbd5e1; font-size:0.9rem; margin-bottom:1rem;">
              Oryginalny skan w pełnej rozdzielczości dostępny jest w państwowym portalu <strong>SzukajwArchiwach.gov.pl</strong> w zespole <em>35/40/0 Akta miasta Kraśnika</em>.
            </p>
            <div style="display:flex; gap:1rem; flex-wrap:wrap; margin-bottom:1.5rem;">
              <a href="${{escapeHtml(item.link_swa || 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801')}}" target="_blank" rel="noopener" class="btn btn-gold">
                🏛️ Otwórz całą jednostkę w Szukaj w Archiwach ➔
              </a>
              <a href="https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/1890" target="_blank" rel="noopener" class="btn btn-secondary">
                📂 Zespół 35/40/0 (Akta m. Kraśnika)
              </a>
            </div>
            <div style="background:rgba(255,255,255,0.03); border:1px solid var(--border); border-radius:8px; padding:1rem; font-size:0.85rem; color:var(--text-muted); line-height:1.5;">
              <strong>ℹ️ Wskazówka nawigacyjna:</strong><br>
              Portal Szukaj w Archiwach otwiera jednostkę jako całość. Aby wyświetlić ten konkretny dokument, przejdź do zakładki <em>„Skany”</em> i wybierz miniaturę oznaczoną numerem <strong>#${{item.nr_skanu}}</strong> (${{escapeHtml(item.strona_pagina)}}).
            </div>
          </div>
        </div>
      `;

      document.getElementById('detailModal').style.display = 'block';
    }}

    function openGenModal(lp) {{
      const p = genData.find(d => parseInt(d.lp) === parseInt(lp));
      if (!p) return;

      currentModalScan = null;
      const tabsBar = document.getElementById('modalTabsBar');
      if (tabsBar) tabsBar.style.display = 'none';

      const imieStr = p.imie || '';
      const funkcjaStr = p.funkcja || p.funkcja_zawod || '';
      const isWidow = imieStr.endsWith('owa') || imieStr === '[Wdowa]' || funkcjaStr.toLowerCase().includes('wdowa');
      const mentions = p.liczba_wystapien || (p.wystapienia ? p.wystapienia.length : (p.skany_list ? p.skany_list.length : 1));

      let occsHtml = '';
      if (p.wystapienia && p.wystapienia.length > 0) {{
        occsHtml = `
          <table class="occs-table" style="width:100%; border-collapse:collapse; margin-top:1rem; font-size:0.85rem;">
            <thead>
              <tr style="background:rgba(255,255,255,0.05); text-align:left; border-bottom:1px solid var(--border);">
                <th style="padding:0.6rem; width:14%;">Skan</th>
                <th style="padding:0.6rem; width:14%;">Rok</th>
                <th style="padding:0.6rem; width:34%;">Zapis w rękopisie</th>
                <th style="padding:0.6rem; width:38%;">Rola / Kontekst</th>
              </tr>
            </thead>
            <tbody>
              ${{p.wystapienia.map(o => `
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                  <td style="padding:0.6rem; font-family:'JetBrains Mono', monospace; font-weight:700; color:var(--gold-primary);">
                    <a href="javascript:void(0)" onclick="closeModal(); setTimeout(() => openMainModal(${{parseInt(o.skan)}}), 150);" style="color:var(--gold-primary); text-decoration:none; cursor:pointer;">#${{o.skan}} ➔</a>
                  </td>
                  <td style="padding:0.6rem;"><span class="badge-years">${{escapeHtml(o.rok)}}</span></td>
                  <td style="padding:0.6rem; color:#cbd5e1;"><em>${{escapeHtml(o.zapis_oryginalny || (imieStr + ' ' + (p.nazwisko || '')))}}</em></td>
                  <td style="padding:0.6rem; color:#94a3b8;">${{escapeHtml(o.rola || '—')}}</td>
                </tr>
              `).join('')}}
            </tbody>
          </table>
        `;
      }} else {{
        occsHtml = `<p style="color:var(--text-muted); margin-top:0.5rem;">Występuje na skanach: <strong>${{escapeHtml(p.skany_roboczo)}}</strong> (lata: ${{escapeHtml(p.zakres_lat)}}).</p>`;
      }}

      document.getElementById('modalTitle').innerText = `${{imieStr}} ${{p.nazwisko}} (${{p.miejsce || 'Kraśnik'}})`.toUpperCase();
      document.getElementById('modalBody').innerHTML = `
        <div class="modal-section">
          <div class="modal-section-title">Dane biograficzne i status społeczno-prawny</div>
          <div style="font-size:1.05rem; margin-bottom:0.5rem;">
            <strong>${{escapeHtml(imieStr)}} ${{escapeHtml(p.nazwisko)}}</strong>
            &nbsp;•&nbsp; <span class="badge-district">${{escapeHtml(p.miejsce || 'Kraśnik')}}</span>
            &nbsp;•&nbsp; <span class="badge-role ${{isWidow ? 'badge-widow' : ''}}">${{escapeHtml(funkcjaStr)}}</span>
          </div>
          <div style="font-size:0.88rem; color:var(--text-muted);">
            Zakres poświadczeń w księdze: <strong>${{escapeHtml(p.zakres_lat || '—')}}</strong> &nbsp;|&nbsp; Łączna liczba wzmianek źródłowych: <strong>${{mentions}}</strong>
          </div>
          ${{(p.wariant_nazwiska || p.warianty_nazwiska) ? `
            <div style="background:#1e293b; border-left:3px solid var(--gold-primary); padding:0.6rem 0.85rem; border-radius:4px; margin-top:0.75rem; font-size:0.88rem; color:#e2e8f0;">
              <strong style="color:var(--gold-primary);">💡 Lekcje i warianty zapisu w rękopisie:</strong> ${{escapeHtml(p.wariant_nazwiska || p.warianty_nazwiska)}}
              <div style="font-size:0.78rem; color:#94a3b8; margin-top:3px;">Wpisanie dowolnej z tych form w wyszukiwarce natychmiast filtruje ten profil (zasada 1 osoba = 1 rekord).</div>
            </div>
          ` : ''}}
        </div>

        <div class="modal-section">
          <div class="modal-section-title">Wystąpienia w źródłach jednostki (poświadczenia)</div>
          ${{occsHtml}}
        </div>
      `;

      document.getElementById('detailModal').style.display = 'block';
    }}

    function switchModalTab(tabKey) {{
      document.querySelectorAll('.modal-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.modal-tab-content').forEach(c => c.style.display = 'none');

      if (tabKey === 'meta') {{
        document.getElementById('tabBtnMeta').classList.add('active');
        document.getElementById('modalTabContentMeta').style.display = 'block';
      }} else if (tabKey === 'trans') {{
        document.getElementById('tabBtnTrans').classList.add('active');
        document.getElementById('modalTabContentTrans').style.display = 'block';
      }} else if (tabKey === 'link') {{
        document.getElementById('tabBtnLink').classList.add('active');
        document.getElementById('modalTabContentLink').style.display = 'block';
      }}
    }}

    function closeModal() {{
      document.getElementById('detailModal').style.display = 'none';
    }}

    window.onclick = function(event) {{
      const modal = document.getElementById('detailModal');
      if (event.target === modal) {{
        closeModal();
      }}
    }};

    function copyTranscription() {{
      const el = document.getElementById('transcriptionText');
      if (!el) return;
      navigator.clipboard.writeText(el.innerText).then(() => {{
        alert('Transkrypcja skopiowana do schowka!');
      }}).catch(err => {{
        alert('Nie udało się skopiować transkrypcji: ' + err);
      }});
    }}

    function downloadBlob(content, filename, contentType) {{
      const blob = new Blob([content], {{ type: contentType }});
      const url = URL.createObjectURL(blob);
      const pom = document.createElement('a');
      pom.href = url;
      pom.setAttribute('download', filename);
      pom.click();
      URL.revokeObjectURL(url);
    }}

    function exportMainCSV() {{
      const headers = ['Nr skanu', 'Paginacja', 'Datacja', 'Kategoria', 'Opis / Regest', 'Osoby / Podmioty', 'Kwoty / Miary'];
      let csv = "\\ufeff" + headers.join(';') + "\\r\\n";
      filteredMain.forEach(r => {{
        const opis = r.opis_pozycji || r.opis_sprawy || '';
        const kwoty = r.kwoty_miary || r.kwoty_podatki || '';
        const row = [r.nr_skanu, r.strona_pagina, r.data_rok, r.kategoria, opis, r.osoby_podmioty, kwoty]
          .map(val => `"${{String(val || '').replace(/"/g, '""')}}"`)
          .join(';');
        csv += row + "\\r\\n";
      }});
      downloadBlob(csv, 'krasnik_j17_indeks_skanow.csv', 'text/csv;charset=utf-8;');
    }}

    function exportGenCSV() {{
      const headers = ['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'];
      let csv = "\\ufeff" + headers.join(';') + "\\r\\n";
      filteredGen.forEach(p => {{
        const row = [
          p.lp,
          p.nazwisko,
          p.imie,
          p.miejsce,
          p.funkcja || '',
          p.skany_roboczo || '',
          p.zakres_lat,
          p.liczba_wystapien || 1,
          p.wariant_nazwiska || ''
        ].map(val => `"${{String(val || '').replace(/"/g, '""')}}"`).join(';');
        csv += row + "\\r\\n";
      }});
      downloadBlob(csv, 'krasnik_j17_slownik_genealogiczny.csv', 'text/csv;charset=utf-8;');
    }}

    // DYNAMIC COUNTERS & INITIAL RENDER
    const catSelect = document.getElementById('mainCategoryFilter');
    if (catSelect) {{
      const categories = [...new Set(mainData.map(d => d.kategoria))].filter(Boolean).sort();
      categories.forEach(cat => {{
        const opt = document.createElement('option');
        opt.value = cat;
        opt.innerText = cat;
        catSelect.appendChild(opt);
      }});
    }}

    const roleSelect = document.getElementById('genRoleFilter');
    if (roleSelect) {{
      const roles = [...new Set(genData.map(d => d.funkcja))].filter(Boolean).sort();
      roles.forEach(role => {{
        const opt = document.createElement('option');
        opt.value = role;
        opt.innerText = role;
        roleSelect.appendChild(opt);
      }});
    }}

    const distSelect = document.getElementById('genDistrictFilter');
    if (distSelect) {{
      const dists = [...new Set(genData.map(d => d.miejsce))].filter(Boolean).sort();
      dists.forEach(d => {{
        const opt = document.createElement('option');
        opt.value = d;
        opt.innerText = d;
        distSelect.appendChild(opt);
      }});
    }}

    renderMainTable();
    renderGenTable();
  </script>
</body>
</html>
"""

output_path = '/home/ubuntu/workspace/Gen/krasnik_j17_kompendium_calosc.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Generated {output_path} successfully ({len(html_template)} bytes).")
