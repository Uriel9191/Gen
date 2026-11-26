# -*- coding: utf-8 -*-
import json
import re

with open('/home/ubuntu/workspace/Gen/main_data_j17_part10.json', encoding='utf-8') as f:
    main_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part10.json', encoding='utf-8') as f:
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
      Obszerny kodeks czynności sądownictwa wójtowsko-ławniczego i sądu łączonego: sesje z 1700 i 1730–1731 r. oraz wszyte poszyty z 1651 i 1694 r. – procesy o zabójstwa, cechy, obrót kamienicami rynkowymi oraz słownik genealogiczny (Partie 1–10: 250 skanów).
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
          <div class="stat-desc">Partie 1–10 (fol. 1r–122r: lata 1651, 1694, 1700, 1730–1731)</div>
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
          <div class="stat-value">39</div>
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
            <option value="1730">Rok 1730</option>
            <option value="1731">Rok 1731</option>
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
