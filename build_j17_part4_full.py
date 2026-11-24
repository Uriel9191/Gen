# -*- coding: utf-8 -*-
import json
import os

records_76_to_100 = [
    {
        "nr_skanu": 76,
        "numer_pozycji": "Poz. 76",
        "strona_pagina": "fol. 36v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Ustrój miasta / Elekcje urzędowe / Przysięga wierności ławy wójtowskiej",
        "osoby_podmioty": "Jan Majowski wójt kraśnicki [Joannes Mayowski]; Adam Kotowicz burmistrz kraśnicki [Adamus Kotowicz]; Stanisław Jerzykiewicz podwójci [Stanislaus Jerzykiewicz]; Błażej Kołodziejczyk ławnik [Blasius Kołodzieyczyk]; Maciej Borowiecki cechmistrz szewski i ławnik; Maciej Dziernatka ławnik [Mathias Dziernatka]; Szymon Dzierzkowski ławnik; Franciszek Sitarski notariusz",
        "kwoty_podatki": "Litkup elekcyjny 12 złp do kasy ratuszowej; juramentum officii",
        "opis_sprawy": "Otwarcie nowego roku urzędowego 1701 w ratuszu kraśnickim (Feria Secunda post Festum Epiphaniarum Domini): Uroczysta odnowa składu sądu wójtowsko-ławniczego pod przewodnictwem wójta Jana Majowskiego i burmistrza Adama Kotowicza; zaprzysiężenie ławników na Krzyż Święty; wpisanie przysięgi posłuszeństwa prawu magdeburskiemu i wilkierzom miejskim.",
        "transkrypcja": "36v\nActum in Praetorio Civitatis Crasnicensis Feria Secunda\npost Festum Epiphaniarum Domini Anno 1701.\n\nZgromadzeni in pleno Panowie Urząd Wóytowski y Radziecki,\nmaiąc wzgląd na porządek pospolity y sprawiedliwość mieyską,\nzłożyli przysięgę urzędową na wierność Jego Królewskiey Mości\noraz Jaśnie Oświeconym Panom Dziedzicom Zamoyskim.\nNaprzed Sławetny Jan Mayowski Wóyt z Adamem Kotowiczem\nBurmistrzem odnowili juramenta swoje. Do których przydani\nzostali mężowie roztropni: Stanisław Jerzykiewicz Podwóyci,\nBłażey Kołodzieyczyk, Maciey Borowiecki, Maciey Dziernatka\ny Szymon Dzierzkowski Ławnicy Przysięgli. Którzy klęcząc\nprzed Krucyfiksem na Ratuszu przysięgli: Iż ubogiemu iako\ny bogatemu równą sprawiedliwość czynić będą, podarków nie biorąc\nani praw mieyskich nie łamiąc. Na co litkupem złotych dwanaście\nzłożono, laudantibus civibus.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 77,
        "numer_pozycji": "Poz. 77",
        "strona_pagina": "fol. 37r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory rzemieślnicze / Skóry i areszty bedelskie",
        "osoby_podmioty": "Tomasz Olchowski kuśnierz kraśnicki [Olchowski]; Maciej Majowski bedel miejski; Jan Des rajca; Urząd wójtowski",
        "kwoty_podatki": "Zajęcie 15 skór baranich i 2 lisich; opłata targowa 3 złp",
        "opis_sprawy": "Sesja wójtowska ze stycznia 1701 r.: Tomasz Olchowski kuśnierz domaga się zwrotu 15 skór baranich i 2 lisich aresztowanych przez bedela Majowskiego w kramie pod zarzutem nieopłacenia cła mostowego; po okazaniu kwitu celnego sąd nakazuje natychmiastowe zdjęcie aresztu z towaru.",
        "transkrypcja": "37\nActum Feria Quarta ante Festum Sancti Antonii\nAbbatis Anno Domini 1701 coram Officio Advocatiali.\n\nInstigante Sławetnym Tomaszem Olchowskim [Olchowski]\nKuśnierzem tuteyszym, sprawa toczyła się contra Macieia\nMayowskiego Bedela Ratuszowego. Iż tenże bedel onegday\nz kramu powoda skór baranich garbowanych piętnaście, a lisich\ndwoie bezprawnie w areszt zajął, mieniąc cło mostowe nieoddane.\nNa co Olchowski stawaiąc, położył kwit jurydyczny Sławetnego\nJana Desa szafarza, iż myto za skóry do skrzynki oddał.\nSąd tedy Wóytowski zważywszy niewinność kuśnierza, bedelowi\nskóry natychmiast powrócić nakazał pod rygorem utraty laski\nbedelskiey, a koszta procedury na urząd mieyski przyiął.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 78,
        "numer_pozycji": "Poz. 78",
        "strona_pagina": "fol. 37v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory rodzinne i spadkowe / Naruszenie dożywocia",
        "osoby_podmioty": "Katarzyna Cieśliczyna wdowa [Cieśliczyna / Cieślina?]; Paweł Cieśla pasierb [Paulus Cieśla]; Jan Majowski wójt; Franciszek Sitarski ławnik",
        "kwoty_podatki": "Chałupa na Przedmieściu Lubelskim; wadium 10 grzywien (vadium decem marcarum)",
        "opis_sprawy": "Żałosna skarga wdowy Katarzyny Cieśliczyny przeciwko pasierbowi Pawłowi Cieśli o bezprawne wygnanie jej z chałupy na Przedmieściu Lubelskim po śmierci męża i zabór skrzyni z odzieżą; sąd nakazuje natychmiastowe przywrócenie dożywocia wdowie pod rygorem 10 grzywien wadium.",
        "transkrypcja": "37v\nActum Feria Sexta post Festum Sancti Antonii\nAbbatis A.D. 1701 coram Iudicio Advocatiali.\n\nUczciwa Katarzyna Cieśliczyna [Cieśliczyna / Cieślina?] Wdowa po niegdy\nJanie Cieśli pozostała, z płaczem y lamentem do sądu przyszłszy,\nskarżyła pasierba swego Pawła Cieślę [Cieśla]: Iż ten w nocy\nzimowey do chałupy na Przedmieściu Lubelskim wpadłszy,\nią ze wszytkiem ze komory wygnał na mróz, skrzynię okowaną\nz płótnem y sukniami zabrał, a sam z żoną chałupę opanował.\nSąd Wóytowski zważywszy zapis dożywotni w księgach będący,\nPawłowi Cieśli ostro nakazał: Aby macochę do izby nazad\nwpuścił, pościel y suknie powrócił, a spokoyność domową\nzachował pod rygorem wadium dziesięciu grzywien.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 79,
        "numer_pozycji": "Poz. 79",
        "strona_pagina": "fol. 38r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory handlowe i rzemieślnicze / Dostawy żelaza",
        "osoby_podmioty": "Marek Boruchowicz kupiec żydowski [Marek / Mordka Boruchowicz]; Stanisław Pajor kowal z Budzynia [Pajor]; Adam Kotowicz burmistrz",
        "kwoty_podatki": "16 złotych polskich (fl. 16) długu; kompensata w podkowach i gwoździach",
        "opis_sprawy": "Sprawa dłużna Marka Boruchowicza [Mordki?] przeciw kowalowi Stanisławowi Pajorowi o zaległe 16 złp za sztangę żelaza węgierskiego; strony zawierają ugodę: Pajor ma dostarczyć 40 podków i 200 gwoździ kowalskich do wozów ratuszowych i dworskich na kompensatę należności.",
        "transkrypcja": "38\nActum Die 25 Ianuarii Anno Domini 1701.\n\nNiewierny Marek Boruchowicz [Marek / Mordka Boruchowicz] Kupiec tuteyszy\nżądał od Uczciwego Stanisława Pajora [Pajor] Kowala z Budzynia\nzapłaty szesnastu złotych za żelazo węgierskie do kuźniey wzięte.\nPajor stawaiąc oświadczył, iż gotowizny nie ma, lecz pracą\nrąk swoich dług zaspokoić pragnie. Za zgodą obydwóch stron\nsąd ugodę pochwalił: Iż Pajor do św. Macieia czterdzieści\npodków wołowych y końskich dobrych oraz dwieście hufnali\ndo kramu Boruchowicza odstawi. Czym cały dług w szesnastu\nzłotych umorzony y z Akt wymazany zostawać ma.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 80,
        "numer_pozycji": "Poz. 80",
        "strona_pagina": "fol. 38v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sąd łączony / Spory graniczne i wodne / Zalanie łąk młyńskich",
        "osoby_podmioty": "Walenty Wojtaszek przedmieszczanin [Valentinus Woytaszek / Woytaszko?]; Jan Wierzbicki karczmarz zarzecki [Wierzbicki]; Berek młynarz żydowski [Berek]; Jan Majowski wójt",
        "kwoty_podatki": "Zalanie 2 staj łąki nadrzecznej; szkoda 12 złp w sianie",
        "opis_sprawy": "Rozprawa przed sądem łączonym w sprawie zalania łąk zarzeckich: Walenty Wojtaszek [Woytaszko?] i Jan Wierzbicki skarżą młynarza Berka o zbyt wysokie podniesienie stawidła młyńskiego na rzece Wyżnicy, co spowodowało zatopienie trawy i zgnicie siana; sąd zarządza wizję grobli.",
        "transkrypcja": "38v\nActum coram Iudicio Composito Civitatis Crasnicensis\nFeria Secunda post Festum Conversionis Sancti Pauli 1701.\n\nUczciwi Walenty Woytaszek [Woytaszek / Woytaszko?] oraz Jan Wierzbicki [Wierzbicki]\nPrzedmieszczanie z Zarzecza uczynili relatią przeciwko Berkowi\nMłynarzowi [Berek], Iż tenże stawiła na stawie mieyskim zbytnie\npodniósł dla większego mielenia, przez co woda z koryta wybiwszy,\nłąki ich nadrzeczne na dwa staja zalała, siano w brogach zepsuła\ny grunt zamuliła. Berek stawaiąc dowodził, iż lody na rzece\nwodę zatamowały. Urząd tedy Złożony postanowił: Aby deputaci\nsądowi na groblę wyjechali y poziom wody znakami oznaczyli.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 81,
        "numer_pozycji": "Poz. 81",
        "strona_pagina": "fol. 39r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Regulacje wodne / Upusty młyńskie i tamy",
        "osoby_podmioty": "Berek młynarz; Walenty Wojtaszek; Jan Wierzbicki; Maciej Dziernatka ławnik; Błażej Kołodziejczyk ławnik",
        "kwoty_podatki": "Obniżenie upustu o 2 piędzi; kara 10 grzywien za spiętrzenie wody",
        "opis_sprawy": "Dekret wodny sądu wójtowskiego: Po rewizji stawu miejskiego nakazano młynarzowi Berkowi wyrąbanie w tamie upustu lodowego i obniżenie poziomu wody o dwie piędzi w okresie przedwiośnia, pod surową karą 10 grzywien do skrzynki ratuszowej.",
        "transkrypcja": "39\nRelatio Decreti Aquatici Super Fluvium Wyżnica.\n\nMy Jan Mayowski Wóyt z Ławnikami po wizyi na młynie mieyskim\nnakazuiemy ninieyszym dekretem Berkowi Młynarzowi: Aby\nzaraz z tamy y upustu dyle dwa zdjął, wodę o dwie piędzi\nspuścił, a w lodach rów szeroki wyrąbał, by woda swobodnie\nod łąk zarzeckich odpływać mogła. Jeśliby zaś pomieniony\nŻyd z uporem wodę wyżey trzymał y sąsiadów zalewał,\ntedy za każdym razem karę dziesięciu grzywien do ratusza\nzapłaci, a szkody na łąkach z własnego majątku nagrodzi.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 82,
        "numer_pozycji": "Poz. 82",
        "strona_pagina": "fol. 39v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Obdukcje ran / Przemoc z bronią białą",
        "osoby_podmioty": "Jakub Kłopotek bednarz [Jacobus Kłopot / Kłopotek?]; Jan Kozieł sługa zamkowy [Joannes Kozieł / Kozioł?]; Maciej Majowski bedel; Stanisław Jerzykiewicz podwójci",
        "kwoty_podatki": "Rana cięta czoła na cal; kord żelazny; wieża ratuszowa in turri",
        "opis_sprawy": "Obdukcja ran bednarza Jakuba Kłopotka [Kłopotka?]: Poszkodowany okazuje ranę ciętą na czole zadaną kordem pod szynkiem w Rynku przez sługę zamkowego Jana Kozła [Kozioła?]; sąd nakazuje osadzenie sprawcy w wieży ratuszowej celem zabezpieczenia kar i kuracji cyrulickiej.",
        "transkrypcja": "39v\nActum Feria Tertia post Festum Purificationis\nBeatissimae Virginis Mariae A.D. 1701.\n\nStawił się z krwawą skargą Uczciwy Jakub Kłopotek [Kłopot / Kłopotek?]\nBednarz Kraśnicki, oświadczając ranę ciężką na czole przez\nJana Kozła [Kozieł / Kozioł?] sługę ordynackiego zadaną. Którą\nto ranę bedel mieyski z podwóycim oglądawszy, uznali: Cięcie\nkordem przez brew lewą aż do kości czaszney na cal głębokie,\nz którego krew obficie zalała odzież y sukmanę powoda. Sprawcę\nnapadu, jako pokój mieyski z orężem w rynku łamiącego, bedel\nzaraz imał y do wieży ratuszowey pod strażą odprowadził,\naż wadium złoży y na cyrulika zapłaci.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 83,
        "numer_pozycji": "Poz. 83",
        "strona_pagina": "fol. 40r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Testamenty ustne / Legaty szpitalne i opieka",
        "osoby_podmioty": "Dorota Snoparska wdowa [Snoparska]; Maciej Snoparski brat zmarłego męża; Zofia Snoparska córka; Jadwiga Snoparska córka; Szpital Św. Ducha",
        "kwoty_podatki": "Legat 20 złp na szpital św. Ducha; świece 2 funty do ołtarza św. Walentego",
        "opis_sprawy": "Testament ustny (nuncupativum) mieszczki Doroty Snoparskiej spisany in extremis: Legat 20 złp dla pensjonariuszy szpitala św. Ducha, wosk na ołtarz św. Walentego w kościele farnym oraz podział placu i sprzętów domowych między córki Zofię i Jadwigę pod kuratelą stryja Macieja Snoparskiego.",
        "transkrypcja": "40\nTestamentum Nuncupativum Honestae Dorotheae Snoparska.\nActum Die 10 Februarii Anno Domini 1701.\n\nPrzed Urzędem Wóytowskim w domu niemocy leżąc, Uczciwa\nDorota Snoparska [Snoparska] Wdowa, przytomnością umysłu władając,\ntak rozporządziła: Duszę oddaię Stwórcy, a ciało ziemi farniey.\nDo Szpitala Świętego Ducha na pożywienie ubogim dziadom\nleguię złotych dwadzieścia polskiey monety. Do kościoła farnego\nna ołtarz Świętego Walentego wosku funtów dwa na świece.\nChałupę z ogrodem córkom moim Zofii y Jadwidze w równy\ndział oddaię, z zakazem aby mienia nie rozpraszały, a Macieia\nSnoparskiego Stryia za opiekuna y tutora mieć maią.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 84,
        "numer_pozycji": "Poz. 84",
        "strona_pagina": "fol. 40v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Inwentarze pośmiertne / Cyna i szaty mieszczańskie",
        "osoby_podmioty": "Dorota Snoparska zmarła; Maciej Snoparski rzeźnik; Zofia i Jadwiga córki; Franciszek Sitarski notariusz",
        "kwoty_podatki": "Kontusz szary podbity popielicami, zapaska jedwabna, 6 półmisków cyny gdańskiej, 2 krowy",
        "opis_sprawy": "Urzędowy inwentarz pośmiertny ruchomości Doroty Snoparskiej: Spisanie szat (kontusz sukna szarego z popielicami, jedwabna zapaska zielona), naczyń cynowych (6 półmisków znaku gdańskiego, 4 talerze), kotła miedzianego do warzenia oraz 2 krów na pastwisku podleskim.",
        "transkrypcja": "40v\nInventarium Bonorum Post Fata Dorotheae Snoparska.\n\nSpisano przez Urząd Wóytowski Kraśnicki:\nW szatach niewieścich: Kontusz sukna szarego popielicami\npodbity, nieco znoszony. Zapaska jedwabna zielona w prążki.\nChust rąbkowych cztery, czepiec z koronką białą.\nW cynie domowey: Półmisków cyny gdańskiey litych sześć,\ntalerzy cynowych cztery z herbem mieyskim wybitych. Kocioł\nwielki miedziany piwny z uchem żelaznym. Skrzynia wielka\ngdańska malowana z zamkiem y kluczykiem.\nW bydle: Krów doynych dwie — iedna graniasta, druga pstra.\nCo wszystko w całości córkom spisano pod dozorem tutora.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 85,
        "numer_pozycji": "Poz. 85",
        "strona_pagina": "fol. 41r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Obrót nieruchomościami / Rezygnacje ról",
        "osoby_podmioty": "Wojciech Bratek mieszczanin [Albertus Bratek / Bratko?]; Maciej Snoparski rzeźnik [Mathias Snoparski]; Jan Majowski wójt",
        "kwoty_podatki": "28 złotych polskich (fl. 28) zapłacone gotówką i potrąceniem długu; traditio soli",
        "opis_sprawy": "Rezygnacja wieczysta półćwierci roli na Piaskach: Wojciech Bratek [Bratko?] sprzedaje i rezygnuje rolę rzeźnikowi Maciejowi Snoparskiemu za kwotę 28 złp; potrącenie dawnych należności za dostawy mięsa; wprowadzenie kupującego w spokojną posesję.",
        "transkrypcja": "41\nActum Feria Quarta ante Festum Sancti Valentini\nMartyris Anno Domini 1701 coram Iudicio Advocatiali.\n\nStawiwszy się osobiście Uczciwy Woyciech Bratek [Bratek / Bratko?]\nMieszczanin Kraśnicki, jawnie zeznał: Iż półćwierć roli swoiey\nwłasney na Przedmieściu Piaski między granicami Dzierżakową\na Kępiną leżącey, sprzedał y na wieczne czasy zrezygnował\nSławetnemu Macieiowi Snoparskiemu [Snoparski] Rzeźnikowi tuteyszemu\nza summę złotych dwadzieścia ośm w dobrey monecie polskiey.\nZ którey summy czternaście złotych za dawnego wieprza potrącił,\na resztę gotowizną odebrał. Skąd tegoż Snoparskiego w wieczną\nposesyą wprowadza per traditionem cespitis, bez żadney ewikcyey.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 86,
        "numer_pozycji": "Poz. 86",
        "strona_pagina": "fol. 41v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Kancelaria miejska / Dzierżawy komunalne / Łaźnia miejska i kąpiele ubogich",
        "osoby_podmioty": "Adam Kotowicz burmistrz; Jan Barankowicz rajca; Stanisław Kłopot łaziebnik [Kłopot / Kłopotek?]; Szpital Św. Ducha",
        "kwoty_podatki": "Czynsz dzierżawny 80 złp rocznie ratami kwartalnymi; cotygodniowa kąpiel ubogich",
        "opis_sprawy": "Kontrakt dzierżawy łaźni miejskiej na rok 1701: Magistrat pod przewodnictwem burmistrza Kotowicza wydzierżawia łaźnię miejską Stanisławowi Kłopotowi [Kłopotkowi?] za roczny czynsz 80 złp; łaziebnik zobowiązuje się do naprawy kotłów i zapewnienia bezpłatnej kąpieli ubogim ze szpitala co sobotę.",
        "transkrypcja": "41v\nLocatio Balnei Civitatis Crasnicensis pro A.D. 1701.\n\nMy Burmistrz y Rada Miasta Kraśnika czynimy wiadomo:\nIżeśmy Łaźnię Mieyską murowaną przy rzece będącą puścili\nw dzierżawę Uczciwemu Stanisławowi Kłopotowi [Kłopot / Kłopotek?]\nna rok cały za summę złotych ośmdziesiąt, którą to summę\nczterema ratami do skrzynki mieyskiey oddawać ma. Z tym\nobowiązkiem: Iż kotły y piece w dobrym stanie utrzyma,\ndrzewo opałowe własnym kosztem sprawi, a dziadom y ubogim\nze Szpitala Świętego Ducha w każdą sobotę bezpłatną kąpiel\ny parzelisko z miłosierdzia uczyni, sub amissione contractus.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 87,
        "numer_pozycji": "Poz. 87",
        "strona_pagina": "fol. 42r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy cechowe / Wyzwoliny tkackie i majstersztyk",
        "osoby_podmioty": "Grzegorz czeladnik tkacki [Gregorius Tkaczyk / Czeladnik?]; Szymon Tkacz starszy cechu [Simon Textor / Tkacz?]; Jan Majowski wójt",
        "kwoty_podatki": "Majstersztyk sukienny (sztuka sukna 30 łokci); termin poprawy 6 tygodni",
        "opis_sprawy": "Sprawa cechowa czeladnika tkackiego Grzegorza ubiegającego się o mistrzostwo: Cechmistrz Szymon Tkacz odrzuca sztukę sukna mistrzowskiego z powodu zbyt rzadkiego tkania; sąd wójtowski wyznacza 6 tygodni na wykonanie nowego postawu sukna o prawidłowej gęstości.",
        "transkrypcja": "42\nActum Feria Secunda ante Festum Sancti Mathiae\nApostoli Anno Domini Millesimo Septingentesimo Primo.\n\nStawił się Grzegorz [Gregorius] czeladnik rzemiosła tkackiego,\nżaląc się na starszych Cechu Tkackiego, iż go do stołu mistrzowskiego\nprzypuścić nie chcą. Na co Szymon Tkacz [Simon Textor] Starszy\ncechu odpowiedział: Iż tenże Grzegorz sztukę sukna na próbę\nutkaną zdefektował, nitki rzadko zbił, przez co sukno deszczu\nnie trzyma y do użytku nie zdatne. Urząd Wóytowski nakazał\nczeladnikowi: Aby przez sześć niedziel nową sztukę sukna\nszaryczkowego łokci trzydzieści podług reguły cechowey utkał\ny do cechu przyniósł, a starsi po sprawiedliwości go osądzą.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 88,
        "numer_pozycji": "Poz. 88",
        "strona_pagina": "fol. 42v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Szkody leśne / Kradzież drzewa szpitalnego",
        "osoby_podmioty": "Prowizorowie Szpitala Św. Ducha; Jakub Kozak chłop z Dzierzkowic [Jacobus Kozak / Kozaczek?]; Jan Majowski wójt",
        "kwoty_podatki": "Grzywna 6 marek na szpital; konfiskata 3 wozów sosen i siekiery",
        "opis_sprawy": "Proces przeciw Jakubowi Kozakowi [Kozaczkowi?] ze wsi Dzierzkowice o bezprawny wyrąb i kradzież drzewa sosnowego z lasu szpitala św. Ducha na Podlesiu; wyrok: konfiskata wyciętego drewna, przepadek siekiery oraz zapłata kary 6 marek na ubogich.",
        "transkrypcja": "42v\nActum Feria Quarta in Die Sancti Mathiae Apostoli 1701.\n\nZ instancyey Prowizorów Szpitala Świętego Ducha stawiony\nzostał Jakub Kozak [Kozak / Kozaczek?] poddany ze wsi Dzierzkowic,\nktórego gajowy szpitalny w lesie podleskim na gorącym uczynku\npoimał, gdy trzy sosny grube ściął y na wóz kładł. Sąd Wóytowski\nzważywszy szkodę ubogich szpitalnych, tak dekretował: Drzewo\nścięte wraz z wozem do szpitala odebrać, siekierę kradziejską\nna rzecz bedela skonfiskować, a Kozak sześć grzywien kary\ndo skrzynki szpitalney złożyć ma, alias in carceribus siedzieć będzie.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 89,
        "numer_pozycji": "Poz. 89",
        "strona_pagina": "fol. 43r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory kupieckie i wekslowe / Zadatek sukienniczy",
        "osoby_podmioty": "Boruch Szmulowicz kupiec żydowski [Boruch / Baruch Szmulowicz]; Marcin Kłos sukiennik [Kłos / Kłosek?]; Franciszek Sitarski pisarz",
        "kwoty_podatki": "Zadatek 15 złp w monecie srebrnej; wadium sądu 6 grzywien",
        "opis_sprawy": "Kupiec Boruch Szmulowicz pozywa sukiennika Marcina Kłosa [Kłoska?] o zwrot 15 złp zadatku wręczonego na postaw sukna szarego z terminem na Zapusty; z powodu niedotrzymania terminu sąd nakazuje zwrot pieniędzy z prowizją do niedzieli przewodniej.",
        "transkrypcja": "43\nActum Feria Sexta post Cineres Anno Domini 1701.\n\nNiewierny Boruch Szmulowicz [Boruch / Baruch Szmulowicz] Kupiec kramowy\npozywał Sławetnego Marcina Kłosa [Kłos / Kłosek?] Sukiennika tuteyszego,\npretenduiąc zadatku złotych piętnaście, które mu przed godami\ndał na postaw sukna szarego ordynaryinego. Ponieważ Kłos sukna\nw terminie nie odstawił, a pieniądze zatrzymał, Urząd Wóytowski\nnakazuie pozwanemu: Aby do Niedzieli Przewodniey owych piętnaście\nzłotych wraz z dwoma złotymi za zwłokę Boruchowi wypłacił\npod rygorem wadium sześciu grzywien y aresztu warsztatu.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 90,
        "numer_pozycji": "Poz. 90",
        "strona_pagina": "fol. 43v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy opiekuńcze / Warsztat szewski po zmarłym",
        "osoby_podmioty": "Jan Kloc zmarły szewc [Kloc / Kłos?]; Katarzyna Klocowa wdowa [Klocowa]; Maciej Borowiecki cechmistrz szewski i tutor; Jan Majowski wójt",
        "kwoty_podatki": "Kopyta szewskie 20 par, 8 skór juchtowych czerwonych, kleszcze, dratwy",
        "opis_sprawy": "Zabezpieczenie praw małoletnich dzieci po zmarłym szewcu Janie Klocu [Kłosie?]: Wdowa Katarzyna wraz z cechmistrzem Maciejem Borowieckim spisują inwentarz warsztatu (kopyta, juchty czerwone, szydła) celem zabezpieczenia rzemiosła dla dorastającego syna.",
        "transkrypcja": "43v\nActum Feria Secunda post Dominicam Invocavit 1701.\n\nPrzed Aktami stanąwszy Uczciwa Katarzyna Klocowa [Klocowa / Kłosowa?]\nWdowa po Janie Klocu Szewcu z Cechmistrzem Maciejem Borowieckim,\nzgłosiła spis warsztatu po mężu: Kopyt szewskich różnych par\ndwadzieścia, skór juchtowych czerwonych wyprawnych sztuk ośm,\nskórek baranich podszewkowych dziesięć, szydeł, nożów krojczych\ny kleszczy żelaznych par cztery. Który to sprzęt cały sąd oddaie\nw oprawę Cechmistrzowi Borowieckiemu, aby syna nieboszczyka\nw rzemiośle wyćwiczył y warsztat w całości zachował.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 91,
        "numer_pozycji": "Poz. 91",
        "strona_pagina": "fol. 44r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory lokatorskie / Naprawa pieców kaflowych",
        "osoby_podmioty": "Anna Starobratkowa wdowa [Starobrat / Starobracina?]; Jan Des obywatel kraśnicki [Des / Dess?]; Jakub Garncarz majster zduński; Adam Kotowicz burmistrz",
        "kwoty_podatki": "Komorne 18 złp rocznie; potrącenie 6 złp za naprawę pieca zielonego",
        "opis_sprawy": "Spór o rozliczenie komornego: Anna Starobratkowa domaga się od Jana Desa [Dessa?] 18 złp komornego za mieszkanie w kamienicy rynkowej; pozwany udowadnia wydatek 6 złp na majstra Jakuba Garncarza za postawienie nowego pieca z zielonych kafli; sąd potrąca koszt pieca z długu.",
        "transkrypcja": "44\nActum Feria Quarta post Dominicam Reminiscere A.D. 1701.\n\nUczciwa Anna Starobratkowa [Starobrat / Starobracina?] dopominała się\nod Sławetnego Jana Desa [Des / Dess?] komornego za izbę w Rynku\nw summie złotych ośmnaście. Na co Des stawaiąc dowiódł świadectwem\nJakuba Garncarza majstra zduńskiego, iż piec kaflowy zielony\ncałkiem rozwalony własnym kosztem y nakładem sześciu złotych\nprzemulirował, kafle nowe wstawił y komin wyprowadził.\nSąd Wóytowski zważywszy pożytek kamienicy, owych sześć złotych\nz komornego potrącił, a resztę dwunastu złotych Desowi\ndo Wielkieynocy wypłacić nakazał.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 92,
        "numer_pozycji": "Poz. 92",
        "strona_pagina": "fol. 44v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Porządek miejski i bruki / Brukowanie rynsztoków",
        "osoby_podmioty": "Błażej Kołodziejczyk ławnik; Maciej Dziernatka ławnik [Dziernatka / Dzierniatka?]; Posesjonaci Przedmieścia Podleskiego; Urząd wójtowski",
        "kwoty_podatki": "Nakaz wybrukowania rynsztoka kamieniem polnym; kara 4 grzywny",
        "opis_sprawy": "Relacja z urzędowej wizji sanitarnej pod Bramą Lubelską: Ławnicy Kołodziejczyk i Dziernatka stwierdzają zanieczyszczenie drogi publicznej gnojem i błotem spływającym z posesji podleskich; nakaz oczyszczenia ulicy i wybrukowania rynsztoka kamieniem polnym do św. Jerzego pod karą 4 grzywien.",
        "transkrypcja": "44v\nRelatio Visionis Ocularis Viae ad Portam Lublinensem.\n\nMy Błażey Kołodzieyczyk y Maciey Dziernatka [Dziernatka / Dzierniatka?]\nŁawnicy z rozkazu sądu oglądaliśmy drogę publiczną ku Bramie\nLubelskiey idącą: Gdzie przez zaniechanie gospodarzy podleskich\ngnóy y rynsztoki ulicę zalały, że ani pieszo ani konno przejazdu\nnie masz. Dekretem tedy sądu nakazuie się wszystkim posesjonatom\ntam mieszkającym: Aby do Świętego Jerzego każdy przed swoją\nposesyą gnóy wywiózł, rynsztok kamieniem polnym wybrukował\ny przepust dla wody uczynił pod surową karą czterech grzywien\ndo kasy mieyskiey.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 93,
        "numer_pozycji": "Poz. 93",
        "strona_pagina": "fol. 45r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy kryminalne / Pręgierz i banicja",
        "osoby_podmioty": "Maciej włóczęga podsądny [Mathias Vagus / Włóczęga?]; Maciej Majowski bedel; Jan Majowski wójt; Stanisław Jerzykiewicz podwójci",
        "kwoty_podatki": "Kradzież 2 gęsi i lemiesza żelaznego wartości 4 złp; 20 plag pod pręgierzem",
        "opis_sprawy": "Proces karny włóczęgi Macieja o kradzież inwentarza domowego i lemiesza z kuźni: Obwiniony przyznaje się do winy przed sądem wójtowskim; wyrok na mocy prawa magdeburskiego: 20 plag postronkiem pod pręgierzem ratuszowym z ręki bedela oraz wieczysta banicja z Kraśnika pod karą szubienicy.",
        "transkrypcja": "45\nActum Feria Sexta ante Dominicam Oculi A.D. 1701.\n\nStawiony przed sądem Maciej [Mathias] człowiek luźny y włóczęga\nbez osiadłości, oskarżony o to, iż z obory mieyskiey gęsi dwie\nzarżnął, a z kuźniey lemiesz żelazny skradłszy, przedać usiłował.\nPodsądny na sądzie dobrowolnie recognoskuje winę swoię. Sąd\nWóytowski maiąc wzgląd na prawo magdeburskie, tak wyrokował:\nAby rzeczony Maciej przez bedela Majowskiego pod pręgierz\nwyprowadzony został y tam dwadzieścia plag postronkiem\nodebrał. Po czym z granic miasta Kraśnika na zawsze ma być\nwygnany, a gdyby się nazad poważył wrócić, na gardle na szubienicy\nkarany zostanie, pro exemplo aliorum.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 94,
        "numer_pozycji": "Poz. 94",
        "strona_pagina": "fol. 45v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Akta Ordynacji Zamojskiej / Administracja zamkowa / Plenipotencje czopowego",
        "osoby_podmioty": "Kazimierz Dłużewski podstarości kraśnicki [Casimirus Dłużewski]; Pinchas Dawidowicz arendarz; Jan Barankowicz poborca miejski; Franciszek Sitarski notariusz",
        "kwoty_podatki": "Pobór podatku czopowego z karczem ordynackich i miejskich",
        "opis_sprawy": "Oblata plenipotencji zamkowej: Wielmożny Kazimierz Dłużewski podstarości kraśnicki oblatuje pełnomocnictwo Ichmościów Państwa Zamoyskich do poboru i kontroli podatku czopowego w mieście i na przedmieściach; uzgodnienie z poborcą Barankowiczem terminów rewizji szynków.",
        "transkrypcja": "45v\nOblata Plenipotentiae Aulae Schlossensis Crasnicensis.\n\nPrzed Aktami ninieyszemi Wielmożny Pan Kazimierz Dłużewski\nPodstarości Zamkowy Kraśnicki okazał y do ksiąg wpisać prosił\nplenipotencyą Jaśnie Oświeconych Dziedziców Ordynacyey Zamoyskiey:\nMocą którey temuż Panu Podstarościemu zleca się zupełna kuratela\nnad dochodami z czopowego, gorzałczanego y piwnego w całym\nKraśniku y przedmieściach. Z nakazem dla magistratu mieyskiego,\naby poborcy zamkowemu w rewizyach szynków y kramów żadney\nprzeszkody nie czynili, lecz wspólnie porządku pilnowali,\nin vim concordiae inter Curiam et Civitatem.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 95,
        "numer_pozycji": "Poz. 95",
        "strona_pagina": "fol. 46r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory rzemieślnicze / Monopol cechu garncarzy",
        "osoby_podmioty": "Jakub Garncarz cechmistrz [Jacobus Figulus / Garncarz?]; Cech garncarski kraśnicki; Szmul kramarz żydowski [Szmul Kramarz]; Adam Kotowicz burmistrz",
        "kwoty_podatki": "Zajęcie 30 garnków urzędowskich; wina cechowa 3 grzywny",
        "opis_sprawy": "Spór o monopol rzemieślniczy: Cechmistrz Jakub Garncarz [Figulus?] oskarża kramarza Szmula o pokątną sprzedaż garnków i misek glinianych sprowadzanych z Urzędowa poza dniami jarmarku; sąd konfiskuje naczynia obcej roboty i zatwierdza monopol cechu kraśnickiego na targach tygodniowych.",
        "transkrypcja": "46\nActum Feria Secunda post Dominicam Laetare 1701.\n\nStarsi Cechu Garncarskiego z majstrem Jakubem Garncarzem\nna czele żalili się przed sądem na Szmula kramarza w Rynku:\nIż tenże w dni powszednie garnki, dwoiaki y misy gliniane\nz Urzędowa sprowadzone po szynkach y domach przedaie,\nkunszt tuteyszy w ubóstwo wprowadzaiąc. Szmul stawaiąc\ntłumaczył się, iż towar na jarmark kupił. Urząd jednak zważywszy\nprzywileje cechowe mieyskie, dekretował: Owych trzydzieści\ngarnków obcey roboty na rzecz cechu zająć, a Szmulowi pod winą\ntrzech grzywien zakazać garnków obcych przedawać oprócz\njarmarków dorocznych solemnium.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 96,
        "numer_pozycji": "Poz. 96",
        "strona_pagina": "fol. 46v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Szkody polne / Wypas owiec w oziminach",
        "osoby_podmioty": "Stanisław Luterek przedmieszczanin [Luterek / Lutrzyk?]; Walenty Pasterz owczy [Valentinus Pastor / Pasterczyk?]; Maciej Borowiecki ławnik; Jan Majowski wójt",
        "kwoty_podatki": "Taksacja szkody w życie na 8 złp; kara sądu 2 grzywny",
        "opis_sprawy": "Skarga Stanisława Luterka [Lutrzyka?] przeciw pasterzowi owczemu Walentemu o zadeptanie i wyjedzenie trzech staj żyta ozimego na Podlesiu przez stado owiec; przysięgły taksator Maciej Borowiecki szacuje stratę na 8 złp; nakaz zapłaty odszkodowania przed Wielkanocą.",
        "transkrypcja": "46v\nActum Feria Quarta ante Dominicam Judica A.D. 1701.\n\nUczciwy Stanisław Luterek [Luterek / Lutrzyk?] podał żałobę\nna Walentego pasterza owczego [Pasterz / Pasterczyk?], Iż tenże\nowce gromadzkie na oziminę podleską wpuściwszy, żyto wschodzące\nna trzech stajach do cna wypasł y kopytami wytłukł. Sławetny\nMaciey Borowiecki Ławnik przysięgły na grunt wyjechawszy,\nszkodę pod sumieniem na złotych ośm otaksował. Którą to kwotę\npasterz wraz z właścicielem stada Luterkowi do Wielkieynocy\nwypłacić ma pod rygorem aresztu owiec y kary dwóch grzywien\ndo ratusza.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 97,
        "numer_pozycji": "Poz. 97",
        "strona_pagina": "fol. 47r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Obrót nieruchomościami / Rezygnacje ogrodów",
        "osoby_podmioty": "Sebastian Zdeb gospodarz z Gór [Zdeb / Zdebik?]; Walenty Sanek przedmieszczanin [Sanek / Stanek?]; Błażej Kołodziejczyk ławnik; Franciszek Sitarski notariusz",
        "kwoty_podatki": "18 złotych polskich (fl. 18) zapłacone gotówką; ugaszenie dawnych sporów sąsiedzkich",
        "opis_sprawy": "Wieczysta rezygnacja ogrodu warzywnego na Błoniu: Sebastian Zdeb [Zdebik?] sprzedaje ogród zagonowy Walentemu Sankowi [Stankowi?] za kwotę 18 złp gotówką; transakcja definitywnie kończy wieloletnie spory sąsiedzkie i wzajemne pretensje o płoty i wypas bydła.",
        "transkrypcja": "47\nActum Feria Sexta ante Dominicam Palmarum Anno 1701.\n\nStawiwszy się osobiście Uczciwy Sebastian Zdeb [Zdeb / Zdebik?]\nz Gór, dobrowolnie recognoskuje: Iż ogród swoy dziedziczny\nna Błoniu leżący między płotami Sankowym a Kępinym, sprzedał\ny na wieczne czasy ustąpił Uczciwemu Walentemu Sankowi [Sanek / Stanek?]\nza summę złotych ośmnaście monety polskiey. Którą to kwotę\nZdeb w całości przed sądem odliczył y odebrał. Przy czym\nobydwie strony oświadczyły, iż wszelkie dawne niezgody,\nskargi o płoty y bydło ze wszytkiem sobie daruią y kasuią,\nzachowuiąc wieczną miłość sąsiedzką pod karą dziesięciu grzywien.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 98,
        "numer_pozycji": "Poz. 98",
        "strona_pagina": "fol. 47v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Szpitalnictwo i dobroczynność / Windykacja legatów",
        "osoby_podmioty": "Adam Kotowicz prowizor szpitala św. Ducha; Jan Barankowicz prowizor; Sukcesorowie niegdy Mikołaja Bednarza dłużnicy; Jan Majowski wójt",
        "kwoty_podatki": "30 złotych polskich (fl. 30) kapitału wyderkafowego; prowizja roczna 2 zł 10 gr",
        "opis_sprawy": "Windykacja funduszów szpitala św. Ducha: Prowizorowie szpitalni burmistrz Adam Kotowicz i Jan Barankowicz pozywają sukcesorów Mikołaja Bednarza o zaległą prowizję od zapisanego kapitału 30 złp na kamienicy; sąd nakazuje natychmiastową spłatę na zakup mąki i kaszy dla ubogich.",
        "transkrypcja": "47v\nActum Feria Tertia post Festum Paschae Resurrectionis 1701.\n\nSławetni Adam Kotowicz Burmistrz oraz Jan Barankowicz\nRayca jako Prowizorowie Szpitala Świętego Ducha, dopominali\nsię od Sukcessorów niegdy Mikołaia Bednarza [Bednarz] prowizyey\nroczney od summy trzydziestu złotych na kamienicy szpitalowi\nzapisaney. Sukcessorowie stawaiąc tłomaczyli się trudnością\nczasów. Urząd Wóytowski zważywszy, iż z tey prowizyey ubodzy\nw szpitalu chleb y kaszę maią, nakazał: Dłużnikom zaległość\nw dwóch złotych y groszach dziesięciu do Niedzieli Przewodniey\ndo rąk prowizorów złożyć pod rygorem zajęcia kamienicy.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 99,
        "numer_pozycji": "Poz. 99",
        "strona_pagina": "fol. 48r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Kancelaria wójtowska / Dyscyplina służb miejskich / Upomnienie bedela ratuszowego",
        "osoby_podmioty": "Maciej Majowski bedel miejski [Mathias Mayowski]; Pospólstwo kraśnickie; Jan Majowski wójt; Adam Kotowicz burmistrz",
        "kwoty_podatki": "Taksy targowe od wozów z sianem (2 grosze od wozu); wilkierz miejski",
        "opis_sprawy": "Rozpatrzenie skargi pospólstwa na bedela Macieja Majowskiego: Mieszczanie oskarżają sługę ratuszowego o pobieranie zawyżonych opłat mostowych i targowych od wozów z sianem i drewnem; wójt i burmistrz udzielają surowego upomnienia bedelowi z nakazem ścisłego przestrzegania taryfy wilkierza pod karą utraty urzędu.",
        "transkrypcja": "48\nActum in Senaculo Civitatis Crasnicensis Die 15 Aprilis 1701.\n\nNa skargę Pospólstwa y Przedmieszczan tuteyszych przeciwko\nMacieiowi Mayowskiemu [Mayowski] Bedelowi Ratuszowemu, iż tenże\nod wozów z sianem y drwami zamiast dwóch groszy po groszy\ncztery samowolnie wyciągał pod bramami, Urząd Wóytowski\nz Burmistrzem tak postanowili: Bedelowi ostro zakazuie się\nwięcey nad dwa grosze podług wilkierza wybierać. A jeśliby\nna potym o zbytnie zdzierstwo był przekonany, tedy nie tylko\nurząd bedelski utraci, ale też w kunie na Rynku przez trzy dni\nsiedzieć będzie, ku przestrodze innym sługom mieyskim.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 100,
        "numer_pozycji": "Poz. 100",
        "strona_pagina": "fol. 48v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1701",
        "kategoria": "Akta wojskowe i miejskie / Kwaterunki chorągwi koronnych / Dostawy furażu",
        "osoby_podmioty": "Chorągiew pancerna Ichmościów Zamoyskich; Jan Majowski wójt; Adam Kotowicz burmistrz; Jan Barankowicz poborca; Mieszczanie kraśniccy",
        "kwoty_podatki": "Dostawa 120 korcy owsa, 60 wozów siana, 40 beczek piwa dla wojska koronnego",
        "opis_sprawy": "Generalna oblata asygnacji kwaterunkowej: Rozliczenie dostaw furażu i żywności dla chorągwi pancernej stacjonującej pod Kraśnikiem na leżach zimowych; dostarczenie przez mieszczan i przedmieszczan 120 korcy owsa, 60 wozów siana i 40 beczek piwa; kwitacja komendanta wojskowego z przybiciem pieczęci wójtowskiej.",
        "transkrypcja": "48v\nOblata Asignationis Militaris pro Legione Zamoysciana.\nActum in Praetorio Die 28 Aprilis Anno Domini 1701.\n\nDo Akt ninieyszych podano kwitacyą rotmistrzowską Chorągwi\nPancerney pod znakiem Wielmożnego Pana Starosty Zamoyskiego:\nŚwiadcząc, iż Miasto Kraśnik ze wszystkiemi przedmieściami\nod Nowego Roku aż do Wielkieynocy furaże należyte dla koni\ny żołnierzy oddało w zupełności. To iest: owsa suchego korcy\nsto dwadzieścia, siana dobrego wozów sześćdziesiąt, a piwa\nwarki mieyskiey beczek czterdzieści. Z których to dostaw\nmagistrat kraśnicki kwituiemy, pieczęć mieyską maiorem\nprzy przytomności Pana Wóyta y Burmistrza apponendo.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    }
]

# Wczytanie dotychczasowych 75 rekordów (Partie 1–3)
with open('/home/ubuntu/workspace/Gen/main_data_j17_part3.json', 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

print(f"Dotychczasowych rekordów (Partie 1-3): {len(existing_data)}")

# Normalizacja pól dla zgodności z kanonem i schematem
for r in records_76_to_100:
    r["scan_nr"] = r["nr_skanu"]
    r["karta"] = r["strona_pagina"]
    r["data_roczna"] = r["data_rok"]
    r["kategoria_sprawy"] = r["kategoria"]
    r["opis_pozycji"] = r["opis_sprawy"]
    r["regest"] = r["opis_sprawy"]
    r["kwoty_miary"] = r["kwoty_podatki"]
    r["link_archiwum"] = r["link_swa"]

full_data_part4 = existing_data + records_76_to_100
print(f"Łączna liczba rekordów po Partii 4: {len(full_data_part4)}")

out_path = '/home/ubuntu/workspace/Gen/main_data_j17_part4.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(full_data_part4, f, ensure_ascii=False, indent=2)

print(f"Zapisano {out_path} pomyślnie!")
