# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j17_part9.json', 'r', encoding='utf-8') as f:
    part9_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"

part10_scans = [
    {
        "nr_skanu": 226,
        "numer_pozycji": "Poz. 226",
        "strona_pagina": "fol. 109v (109v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Złożenie 100 złp w worku skórzanym przez Tomasza Zdeba (24 XI 1700 r.)",
        "osoby_podmioty": "Tomasz Zdeb [Zdeb]; Wojciech Kondup zmarły [Kondup]; Andrzej Panek [Panek]",
        "kwoty_podatki": "100 złp (50 złp w pierwszym i 50 złp w drugim terminie) w worku skórzanym",
        "opis_sprawy": "Dokończenie wpisu z 24 XI 1700 r.: Tomasz Zdeb (powołując się na dekret z 10 XI 1700 r.) składa przed sądem 50 złp oraz drugie 50 złp w worku skórzanym na spłatę Andrzeja Panka i jego żony za dobra po wuju Wojciechu Kondupie, żądając zapisu rękojmi od impetycji. Poniżej nagłówek sesji Sądu Obojnego z 29 XI 1700 r. (wigilia św. Andrzeja).",
        "transkrypcja": "109 v\n...należącego z Aktami prawem naturalnym po niegdy Wojciechu Kondupie [Kondup] wuiu rodzonym na lewey ćwierci [?] quod niesłusznie [?] dotąd z pożytkami [?] albo nie z rezygnacyi do swey stroni na te dobra tak przed Antecessorami moimi jako i sobie otrzymanych nie pokazał. W prawo y przywilej wprowadzając gdzie mogą wyrozumieć ferowanego dekretu a to w poniedziałek przed świętem świętego Marcina Biskupa Roku 1700 dnia 10 listopada [10 XI 1700 r.] ferowanego [?] od pozwanych Panków [Panek] Małżonków. Na które to [?] Ten Przedmieszczanin Kraśnicki do odbioru żeby byli gotowi odebrać stawili się do Akt y Urzędu Mieyskiego Kraśnickiego y summę złotych 50 według dekretu na okazane do odbioru z odebrania gotowali na drugie zaś złotych pięćdziesiąt [?] zapisania się od impetycyi prawnych y nieprawnych na dobrach się zapisać albo one lokować będą summy gotowey Aktor zwykłe [?] złotych 50 prezentował summę które prezentował w worku skórzanym tandem [?] protestatus est de damnis et litis expensis in causa subsecutis et subsequendis.\n\nActum Coram Officio Composito et Scabinali Crasnicensi Feria Secunda in Vigilia festi Sancti Andreae Apostoli Anno Domini Millesimo Septingentesimo [29 XI 1700 r.].",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 227,
        "numer_pozycji": "Poz. 227",
        "strona_pagina": "fol. 110r (110)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Egzekucja dekretu Tomasza Zdeba przeciw Andrzejowi Pankowi (29 XI 1700 r., karta uszkodzona)",
        "osoby_podmioty": "Andrzej Panek [Panek]; Zofia z Wójcików Pankowa [Pankowa]; Tomasz Zdeb [Zdeb]; Wojciech Kondup zmarły [Kondup]",
        "kwoty_podatki": "Złożenie 100 złp do sekwestru sądowego (prawy brzeg karty naderwany)",
        "opis_sprawy": "Sesja z 29 XI 1700 r. (karta z dużym ubytkiem prawego marginesu): Andrzej Panek i Zofia z Wójcików nie stawili się po raz drugi (`secunda contumacia`) do odbioru pieniędzy złożonych przez Tomasza Zdeba za ćwierć roli Kondupowskiej; sąd kieruje 100 złp do sekwestru urzędowego.",
        "transkrypcja": "110\n...Andrzej Panek [Panek] Przedmieszczanin Kraśnicki y Zofia de gente Woycikowa [Pankowa] małżonkowie [?] do odbioru pieniędzy z dóbr videlicet ćwierci roli Kondupowska nazwaney [?] Przedmieszczaninowi Thomaszowi Zdebowi [Zdeb] iako wuiu rodzonym [?] na dzień dzisieyszy przed Sąd ninieyszy do odebrania pieniędzy summy dekretem nakazaney nie stanęli secundo contumaces exhibentur.\n\nSecunda contumacia.\nNa którego nieposłuszeństwo ad legitimam Instantiam Affectationem Ponieważ Aktor w czas naznaczony w dekrecie wyrażony summę prezentował nadto do odebrania sąsiadów wezwał y [?] Jednak iż pozwani in protractionem causae et meram vexationem nie stawiają się do odebrania [?] do lepszey prosekucyi od Wyższego Sądu [?] którey summae [?] Sąd ninieyszy [?] do sekwestru [?] dekretem nakazanej [?] otrzymać summy złotych sto polskich...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 228,
        "numer_pozycji": "Poz. 228",
        "strona_pagina": "fol. 110v (110v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Nakaz intromisji w dobra Kondupowskie (29 XI 1700 r.)",
        "osoby_podmioty": "Jan Majowski wójt [Majowski]; Tomasz Zdeb [Zdeb]; Andrzej Panek [Panek]; Wojciech Kondup zmarły [Kondup]",
        "kwoty_podatki": "Sekwestr sumy w sądzie i delegacja ławników do intromisji",
        "opis_sprawy": "Dokończenie sesji z 29 XI 1700 r.: Sąd Obojny Kraśnicki stwierdza niestawiennictwo Andrzeja Panka do odbioru pieniędzy, nakazuje złożenie sumy przy wójcie Janie Majowskim i deleguje urząd wójtowski do dokonania realnej intromisji Tomasza Zdeba w dobra Kondupowskie.",
        "transkrypcja": "110 v\n...przed Sławetnego Pana Jana Majowskiego [Majowski] Wójta Kraśnickiego [?] rzetelnie złożone [?] Odłożenia [?] Intromissią [?] całey sobie na [?] na Podlesiu.\n\nSąd ninieyszy Oboyny Kraśnicki uważając iż pozwany ani przez się ani przez subordynowanego [?] na termin sobie dany nie stawa Aktorowi [?] nie broni [?] in protractam [?] iako mu z dawna [?] na [?] które [?] summę [?] Officio praesenti subiacere debet ac omnino [?] Iuri communi et Affectationi [?] ad haec Intromissią cum pacifica et reali possessione adhaerendo Decretis Aktorowi w te dobra Kondupowskie nazwane o które rzecz idzie pozwolił [?] de medio Officii [?] Officiales suos Licitalis advocatus [?] deputabit Qui quidem deputati [?] realiter ac actualiter [?] Intromissia byta relacyą uczynić powinni.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 229,
        "numer_pozycji": "Poz. 229",
        "strona_pagina": "fol. 111r (111)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1694",
        "kategoria": "Sądownictwo miejskie (Kodykologia: wszyta składka z 1694 r.) / Składki poborowe, rachunki i protestacje z 1694 r.",
        "osoby_podmioty": "Szymon Skopik [Skopik?]; Grzegorz Kłopotek [Kłopotek]; Paweł Słomkowski [Słomkowski]; Stefan Jerzykiewicz ławnik [Jerzykiewicz]; Jan Barankowicz [Barankowicz]; Jan Majowski ławnik [Majowski]; Adam Kotowicz [Kotowicz]",
        "kwoty_podatki": "7 złp 8 gr ze składek poborowych oraz 2 kwatery owsianej dziesięciny",
        "opis_sprawy": "Kodykologicznie wyodrębniona składka z 1694 r.: (1) sesja z 8 VII 1694 r. (`Feria 5ta post Festum Visitationis BMV 1694`): wyrok między Szymonem Skopikiem a Grzegorzem Kłopotkiem o zaległe składki poborowe (7 złp 8 gr); (2) sprawa Pawła Słomkowskiego z egzaktorami o porachunki; (3) sesja z 20 XII 1694 r. (`Feria 2da in Vigilia Sti Thomae Appli 1694`): protestacja ławnika Stefana Jerzykiewicza przeciw Janowi Barankowiczowi o długi oraz ławnika Jana Majowskiego przeciw Adamowi Kotowiczowi.",
        "transkrypcja": "111\nFeria 5ta post Festum Visitationis BMV 1694 [8 VII 1694 r.].\nInter Simonem Scopik [Skopik?] Actorem personaliter et Gregorium Kłopotek [Kłopotek] Scabinos.\nSąd ninieyszy uwagiwszy kontrowersyi wysłuchanych a że zapis zarzecz nie [?] po uchwaloney wielkiey składce na Ratuszu aby Aktor in toto ją wypłacał to się tycze składek poborowych nakazuje aby pozwany dał fl 7 gr 8 a zaś po skonczeniu składki wszystkich którekolwiek zajdą pozwany powinien będzie płacić z kwatery owsianey obie dwie przypisać et e converso [?] Janowi Jardzykowi [?] Actores et Regestr [?]\n\nPonieważ pozwany submittował się wyrobie przedmieyskiej poddać.\nInter Paulum Słomkowski [Słomkowski] Consul. et Exactores [?]\nDatur dilatio do wszystkich porachunków.\n\nFeria 2da in Vigilia Sti Sancti Thomae Appli 1694 [20 XII 1694 r.].\nFam. Stephanus Jerzykiewicz [Jerzykiewicz] Scabinus Protest. contra Fam. Joannem Barankowicz [Barankowicz] ratione duorum [?] et [?] Officio Proconsuli contra eundem ratione [?] fl 8.\nFam. Joannes Majowski [Majowski] Scabinus in eodem dato.\nFam. Adamus Kotowicz [Kotowicz] tam ratione huius [?] conservat [?] summę płaci [?] Protest. demum contra eundem.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 230,
        "numer_pozycji": "Poz. 230",
        "strona_pagina": "fol. 112r (112)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1694",
        "kategoria": "Sądownictwo i obdukcje (składka 1694 r.) / Spór wójta Ubaldiego Janaszkowica z malarzem Karolem Mrokowskim oraz obdukcja Grzegorza Boguty",
        "osoby_podmioty": "Ubaldi Janaszkowicz wójt [Janaszkowicz]; Karol Mrokowski malarz [Mrokowski]; Boruch Jozwowicz arendarz [Jozwowicz?]; Łaba [Łaba]; Węglarz [Węglarz]; Grzegorz Boguta [Boguta]",
        "kwoty_podatki": "Sprawa o obrazę na tablicy przed wójtem Janaszkowiczem; obdukcja ran Grzegorza Boguty",
        "opis_sprawy": "Ciąg dalszy składki z 1694 r. (fol. 112r): (1) wpis na górze strony; (2) sesja w oktawie Bożego Ciała 1694 r. (`Feria 2da infra Octavas Sacratissimi Corporis Christi 1694`): spór między sławetnym wójtem Ubaldim Janaszkowiczem a malarzem Karolem Mrokowskim o zniesławienie na tablicy i najście domu; (3) skarga arendarza żydowskiego Borucha Jozwowicza przeciw poddanym Łabie, Węglarzowi i innym o niewydanie konia oraz obdukcja krwawych ran na głowie, ręce i łokciu Grzegorza Boguty.",
        "transkrypcja": "112\n...wielu na teraz [?] na Sąd Króla [?] relacya w którym to [?] przed [?] do Sądu [?] zapisana.\n\nFeria 2da infra Octavas Sacratissimi Corporis Christi Domini Anno eiusdem 1694 [14 VI 1694 r.].\nInter Spectabilem Ubaldum Janaszkowicz [Janaszkowicz] Advocatum [?] et Hon. Carolum Mrokowski [Mrokowski] in causa [?]\nW sprawie o obrażenie pozwanego przez Aktora o diffamacyą na Tablicy kogo byli Aktora [?] też Protestanti także o najście domu sądowego [?] Aktora.\n\nFeria 2da [?] in Festum SS. Petri [?] Anno Dni 1694 [29 VI 1694 r.].\nBoruch Jozwowicz [Jozwowicz?] Arendarz Gościeradzki [?] Kasztelana Kamienieckiego [?] przeciwko Łabie [Łaba], Węglarzowi [Węglarz] et alios [?] ratione konia [?] nigdy nie nabytego [?] przed [?] Świadkami [?] tak że y [?] dla niepuszczenia konia [?] Protestat [?]\n\nDo tegoż Sądu Grzegorz Boguta [Boguta] razy prezentował naprzód raz wielki na głowie [?] na rogu z lewey nad okiem lewym krwawy, drugi raz niedaleko tego [?] z prawej [?] tłuczona sina krwawa, żyła druga prawa nad łokciem [?] na lewej ręce [?] palce lewej ręki trzy sinych [?] na boku raz [?] łykowi piersiowi napuchły na lewej nodze.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 231,
        "numer_pozycji": "Poz. 231",
        "strona_pagina": "fol. 112v (112v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1694",
        "kategoria": "Obdukcje i protestacje (składka 1694 r.) / Obdukcja Stanisława Pękały i skarga o najście na stół piekarski",
        "osoby_podmioty": "Stanisław Pękała [Pękała / Piekala?]; Szymon Piotr [Piotr?]; Borowski [Borowski?]",
        "kwoty_podatki": "Obdukcja ciężkich ran głowy, ucha i palca",
        "opis_sprawy": "Dokończenie składki z 1694 r.: (1) obdukcja ciężkich ran głowy, kości ucha, wargi i palca prawej ręki Stanisława Pękały (Piekali?) z oskarżeniem Szymona Piotra; (2) skarga na najście na stół piekarski i obrazę słowną.",
        "transkrypcja": "112 v\nStanisław Pękała [Pękała / Piekala?] rany prezentował naprzód raz cięty [?] na kości w głowie [?] kość naruszona przecięta na rogu, lewym okiem na lewej ręce raz jeden siny krwawy przebijony [?] drugi raz na łokciu [?] napuchły [?] przy łokciu raz uderzony krwawy siny napuchły, na ręce u palców raz napuchły stłuczony dużo, na prawej ręce na palcu serdecznym raz przecięty na członku krwawy, oto winę daje Szymkowi Piotrowi [Piotr?].\n\nBorowski [Borowski?] contra eundem ratione intromissionis et conculcationis że oni siedzieli u swego stołu pańskie [piekarskie?] [?] chwalił [?] że on zapłacił jednego drugiego [?] tym niemniey [?] aż oddał...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 232,
        "numer_pozycji": "Poz. 232",
        "strona_pagina": "fol. 113r (113)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1730",
        "kategoria": "Sądownictwo łączone (Kodykologia: warstwa 1730–1731) / Wyroki w sprawach Żydówki Maryany przeciw winiarzowi, Bogucie, Truskawce i Wojciechow Sawkę",
        "osoby_podmioty": "Maryana [Maryana]; Jan Boguta [Boguta]; Szymon Truskawka [Truskawka]; Wojciech Sawka [Sawka]",
        "kwoty_podatki": "Dług 13 złp 15 gr od winiarza, 2 złp 16 gr od Szymona Truskawki, 4 złp od Jana Boguty oraz 6 złp 15 gr + 3 złp 15 gr od Wojciecha Sawki",
        "opis_sprawy": "Kolejna warstwa chronologiczna woluminu (1730 r.): (1) wyrok w sprawie Niewiernej Maryany przeciw winiarzowi, Janowi Bogucie i Szymonowi Truskawce o dług za wieprze i różne trunki (nakaz przysięgi Maryany w bóżnicy na Rodale oraz spłaty 2 złp 16 gr i 4 złp + 4 złp za wieprze); (2) wyrok w sprawie Maryany przeciw Wojciechowi Sawce o dług za gotowe pieniądze i parobka (6 złp 15 gr i 3 złp 15 gr, z przysięgą w piątek).",
        "transkrypcja": "113\n...na Maryankę [Maryana] Aktorkę z pomienionym [?] racyo że wieprze na które pożyczyła Aktorka winiarzowi swemu złp 13 gr 15 a temu Janowi Bogucie [Boguta] winien był od lat kilku złp 13/15 których nie mógł oddać przez te lata póki prawie violenti modo zagrabił tegoż winiarza któremu powinien słowo dobre dać a złotych cztery z tych wieprzów Maryance [Maryana] oddać resztę Aktorka ma się upominać u swego winiarza złotych 4. Tenże pomieniony Jan Boguta [Boguta] y Szymon Truskawka [Truskawka] mają dług sprzeczny to jest Szymon Truskawka złp 2/16 a Jan Boguta złp 4 rożnymi czasy nabranymi jako to y [?] Sąd Ninieyszy sprawy między stronami wysłuchawszy nakazuje aby Aktorka w piątek da [?] przyszły Jurament wypełniła w Bóżnicy na Rodale jako jej winien a pozwani powinni oddać in instanti jeden złp 2/16 drugi zaś jako sprzeczne złp 4 tak y za wieprze złp 4 a o resztę niechaj się upomina winiarzowi.\n\nSub Eodem Actu.\nW sprawie y Akcyi między Niewierną Maryanką [Maryana] Aktorką a Pozwanym Uczciwym Wojciechem Sawką [Sawka] ratione długu tak pieniędzmi gotowemi nabranego tak y [?] tudzież y za parobka którego długu złp 17 gr [?]\nSąd Ninieyszy sprawy między stronami wysłuchawszy nakazuje aby pozwany dług swój przyznany oddał to jest złp 6/15 za parobka złp 3/15 a o złotych siedm ma Jurament wykonać Aktorka w piątek blisko przyszły a pozwany in instanti aby oddał dług...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 233,
        "numer_pozycji": "Poz. 233",
        "strona_pagina": "fol. 113v (113v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1730",
        "kategoria": "Obdukcje i sądownictwo (1730 r.) / Sprawa Maryany z Marcinem Skórą oraz obdukcja burmistrza Benedykta Szmatkowskiego pobitego przez syna Kazimierza Pikulskiego",
        "osoby_podmioty": "Maryana [Maryana]; Marcin Skóra [Skóra]; Benedykt Szmatkowski burmistrz [Szmatkowski]; Kazimierz Pikulski [Pikulski / Pikuła?]",
        "kwoty_podatki": "2 złp dla Maryany od Marcina Skóry (wobec żądanych 3 złp 15 gr) oraz wadium sądowe",
        "opis_sprawy": "(1) Dokończenie sprawy Maryany z Wojciechem Sawką (grzywny w razie niewykonania dekretu). (2) Wyrok w sprawie Maryany przeciw Marcinowi Skórze o dług za miód (3 złp 15 gr — sąd zasądza 2 złp, na trzeci złoty przysięga lub ugoda). (3) Sesja z 22 XII 1730 r. (`Feria 6ta post Festum Sancti Thomae Apostoli 1730`): dramatyczna obdukcja ran burmistrza kraśnickiego Benedykta Szmatkowskiego, napadniętego na drodze bez żadnej okazji przez syna szlachcica Kazimierza Pikulskiego z Urzędowa (rany głowy, palców lewej ręki ciętej szablą wraz z pochwą, łopatki i pięści prawej ręki).",
        "transkrypcja": "113 v\n...na który Aktorka przysięgła Inquantum by [?] którekolwiek strona nie uczyniła zadość temu dekretowi ta strona ma dać grzywien nieodpuszczonych per medium Kosztowi y Sądowi y prawne koszta wrócić powinna.\n\nSub Eodem Actu.\nW sprawie y Akcyi między Niewierną Maryanką [Maryana] Aktorką a Pozwanym Uczciwym Marcinem Skórą [Skóra] ratione długu za miód złp 3 gr 15 co pozwany nie przyznaje z swoją Małżonką tylko 2 złp czyni patrzona Sąd Ninieyszy sprawy między stronami zważywszy nakazuje aby pozwani dali Aktorce złotych dwa y koszta prawne wrócili złoty zaś jeden y gr 15 to z [?] między stronami co większego pozwany ma iść na wino [?] którego nie wyjdzie aż albo Aktorkę uspokoi albo sam zapłaci pozwany jako odda złotych dwa.\n\nActum Crasnicy Coram Officio Composito Jurato Crasnicensi Feria 6ta post Festum Sancti Thomae Apostoli 1730 Ano [22 XII 1730 r.].\nPrzed tenże Urząd personaliter stanąwszy Zacnie Sławetny Benedykt Szmatkowski [Szmatkowski] Burmistrz Kraśnicki Obducyą uczynił który podprzysiągł na Urząd swój takowe widzieli razy naprzód na głowie na lewej stronie nad skronią raz z szabli przecięty na półtora członka ręka lewa tłuczona szablą y z pochwami opuchła aż po łokieć którzy ręki obducent y do głowy donieść nie może ani żadnym palcem ruszyć łopatka także tłuczona, na prawej ręce sama kostka u pięści stłuczona y napuchła, o które to obducent ma świadectwo jako nic nie winien był ani żadnej okazyi nie dał ale na dobrowolnej drodze idąc postrzeliwszy y tego szablą będąc bity aż się pochwy przetrąciły którego pobicia daje winę Synowi Sławetnego Pana Kazimierza Pikulskiego [Pikulski / Pikuła?] mieszczanina Urzędowskiego.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 234,
        "numer_pozycji": "Poz. 234",
        "strona_pagina": "fol. 114r (114)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Śledztwo kryminalne (ANNUS NOVUS 1731) / Protestacja Mośka Moszkowica oraz inkwizycja z 10 I 1731 r. o napaść pod Konopnicą na burmistrza Szmatkowskiego",
        "osoby_podmioty": "Maryana [Maryana]; Wojciech Sawka [Sawka]; Mosiek Moszkowic [Moszkowic]; Szymon Truskawka [Truskawka]; Benedykt Szmatkowski burmistrz [Szmatkowski]; Jan Barankowicz były burmistrz [Barankowicz]; Panna Szydłowska [Szydłowska]; Abram Szlomowicz [Szlomowicz]",
        "kwoty_podatki": "Obrażenia i rozbój z dobytymi szablami pod Konopnicą",
        "opis_sprawy": "(1) Przełożenie przysięgi Maryany z Wojciechem Sawką na niedzielę. (2) Protestacja Mośka Moszkowica przeciw Szymonowi Truskawce o najście na dwór w asyście dwóch ludzi z siekierą i zabranie drzewa. (3) Otwarcie roku 1731 (`ANNUS NOVUS`, sesja z 10 I 1731 r.): inkwizycja z instancji burmistrza Benedykta Szmatkowskiego w sprawie napadu pod Konopnicą — zeznanie pierwszego świadka, byłego burmistrza Jana Barankowicza, opisującego powrót saniami z Wieniawy z burmistrzem Szmatkowskim, panną Szydłowską i Żydem Abramem oraz napaść urzędowian z dobytymi szablami.",
        "transkrypcja": "114\nSub Eodem Actu.\nJurament Maryanki [Maryana] odłożony iest do Niedzieli Czerwca [?] do dzisiejszego z Uczciwym Wojciechem Sawką [Sawka].\n\nSub Eodem Actu.\nPrzed tenże Urząd personaliter stanąwszy Niewierny Mosiek Moskowicz [Moszkowic] solennie się protestował przeciw Uczciwemu Szymonowi Truskawce [Truskawka] który zastawszy czyli w swojej prośbie [?] w cudzej ważył się do swego domu te drwa [?] zawieść y do tego jeszcze te drwa przywiózłszy na jego podwórze siekierę wziął violenti modo co dwóch ludzi [?] całą drogę miarę [?]\n\nActum Crasnicy Coram Officio Composito Jurato Crasnicensi Feria 4ta post Festum Circumcisionis Domini 1731 [10 I 1731 r.].\nANNUS NOVUS\nNa Instancyą Sławetnego Pana Benedykta Szmatkowskiego [Szmatkowski] Burmistrza Kraśnickiego wysłuchana iest Inkwizycya której Inkwizycyi sequitur tenor talis:\n\n1mus Testis Sławetny Jan Barankowicz [Barankowicz] quondam Burmistrz przysięgły Kraśnicki tacto pectore haec formalia recognovit: Iż ia jadąc z Wieniawy z Panem Szmatkowskim [Szmatkowski] na jednej saniach na których siedziała Panna Szydłowska [Szydłowska] y Żyd [Szlomowicz] czarny y za nami było sani troie Kraśnickich dognałszy nas Urzędowscy ludzie wołali z drogi tego wołania było nie raz ani dwa my rozumieli że to Pana Frankiewicza parobek sobie żartuje potem nas mijając dobył szabli y gdyby był dostał kogo jak się za most to by był kogo rozpłatał tylko że dosiądz nie mógł potem przyjachawszy nad Konopnicę aż nadybaliśmy ich co się wywrócili aż z temi słowy odezwał Pan Szmatkowski...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 235,
        "numer_pozycji": "Poz. 235",
        "strona_pagina": "fol. 114v (114v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Śledztwo kryminalne i protestacje (1731 r.) / Dalsze zeznania o napadzie pod Konopnicą (Abram Szlomowicz, Marcin Ćwióka) oraz skarga burmistrza Ruszyńskiego",
        "osoby_podmioty": "Jan Barankowicz [Barankowicz]; Abram Szlomowicz [Szlomowicz]; Marcin Ćwióka [Ćwióka / Ćwika?]; Benedykt Szmatkowski burmistrz [Szmatkowski]; Kazimierz Pikulski [Pikulski]; Maciej Ruszyński burmistrz [Ruszyński]; Adam Słowacki pisarz szafarski [Słowacki]",
        "kwoty_podatki": "Rozliczenie 3 tynfów i 2 tynfów przy rachunkach szafarskich",
        "opis_sprawy": "Dokończenie inkwizycji w sprawie napadu pod Konopnicą: (1) koniec zeznania Jana Barankowicza (o zabraniu szabli ze śniegu przed karczmą w Konopnicy i szarpaniu za piersi); (2) zeznanie 2. świadka Żyda Abrama Szlomowicza o groźbach wobec syna Pikulskiego; (3) zeznanie 3. świadka Marcina Ćwióki. Poniżej sesja po 6 I 1731 r.: protestacja radnego i burmistrza Macieja Ruszyńskiego przeciw byłemu pisarzowi szafarskiemu Adamowi Słowackiemu o obelgi przy rachunkach miejskich.",
        "transkrypcja": "114 v\n...też Panie Szlachcicu niech ci się szabla w śniegu oskry [?] pojechaliśmy coś tam Panowie Szlachta wzięli szablę [?] y pojechaliśmy Oni nas dognawszy przed karczmą Konopnicką bił szablą co się mu podobało mówiąc ty skurwysynu co tobie do moiej szabli po drugi raz w lesie zastąpiwszy [?] zastraszywszy na drodze wziąwszy mnie za piersi y wyciągnął mnie z sani tylko nie wiem kto [?] aby szablę oddać coś my powiedzieli że szabla nie zginie swego czasu oddamy.\n\n2dus Testis Niewierny Abram Szlomowicz [Szlomowicz] Obywatel Kraśnicki similia recognovit y to zeznał że kiedy Aroner począł mówić do syna Pana Pikulskiego [Pikulski] że choć ja Żyd to bym ja tego nie wytrzymał jako Pan Szmatkowski cicho skurwysynu Żydzie bo z ciebie dostanie.\n\n3us Testis Uczciwy Marcin Ćwióka [Ćwióka / Ćwika?] tacto pectore haec formalia recognovit że kiedyś my przyjachali do Konopnicy to już [?] na chataż tylko żem widział w lesie po drugi raz że zastąpili y mówili oddajcie szablę tego zaś nie słyszał z czego się [?] pierwszy starosta.\n\nActum Crasnicy post Festum SSS Regum Coram Officio Composito Jurato Crasnicensi 1731 [po 6 I 1731 r.].\nPrzed tenże Urząd personaliter stanąwszy Sławetny Maciej Ruszyński [Ruszyński] Radca y Burmistrz Kraśnicki solennie się protestował przeciw Uczciwemu Adamowi Słowackiemu [Słowacki] przeszłemu Pisarzowi Szafarskiemu który nie mając względu in primis na Bojaźń Bożą a potem na miłość bliźniego ważył się Protestanta słowy nieuczciwemi znieważyć a to z tej racyi że on przyszedłszy...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 236,
        "numer_pozycji": "Poz. 236",
        "strona_pagina": "fol. 115r (115)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Sądownictwo łączone (1731 r.) / Dokończenie skargi burmistrza Ruszyńskiego oraz wyrok na Matyasza Nagórnego (10 grzywien i więzienie)",
        "osoby_podmioty": "Maciej Ruszyński burmistrz [Ruszyński]; Adam Słowacki [Słowacki]; Matyasz Nagórny [Nagórny]; Józef Baradziejowski [Baradziejowski / Baradziogoski?]",
        "kwoty_podatki": "Tynfy 3 i 2 tynfy za rachunki; 10 grzywien kary i tydzień więzienia dla Matyasza Nagórnego",
        "opis_sprawy": "Dokończenie protestacji burmistrza Macieja Ruszyńskiego przeciw Adamowi Słowackiemu (o 3 tynfy za rachunki, groźby zabicia na środku Rynku). Poniżej: komplanacja przy Urzędzie Obojnym między Matyaszem Nagórnym a Józefem Baradziejowskim (skaleczenie w głowę i przewrócenie ławy przy prezydencji sądu — skazanie Nagórnego na 10 grzywien nieodpuszczonych i tydzień więzienia).",
        "transkrypcja": "115\n...do domu Protestanta podczas tych czasów kiedy [?] czyniono y tenże pomieniony nocuje [?] i lamentem narzekał żeby potrzeba dać temu słuchając rachunków przynajmniej tynfów trzy co protestant dał tynfów dwa y czterech groszy za jego rozkazaniem upominając się protestant przy Uczciwych wiarygodnych słowy nieuczciwemi obsyłał protestanta na co protestant ma świadectwo mówiąc te słowa że postęp młodszych do siebie y kazał ich pograbić że na swoje imię datkiem a on odpowiedział ty skurwysynu co cię zabiję choćby na środku Rynku.\n\nSub Eodem Actu.\nMiędzy Uczciwemi Osobami z jednej strony Uczciwego Matyasza Nagórnego [Nagórny] z drugiej strony Uczciwego Józefa Baradziejowskiego [Baradziejowski / Baradziogoski?] ta się komplanacya przy Urzędzie Obojnym który będzie ten że Józef skaleczony w głowę który sobie przy Urzędzie publiczną deprekacyą uczynili y Vadia na nich który by miał okazyą dać ta strona ma dać nieodpuszczonych grzywien 10 y więzienia tydzień siedzieć. Za Akcyą zaś którą uczynił Uczciwy Matyasz Nagórny [Nagórny] że się ważył na prezydencyi naprzód wyszedł ręką bić y pchnąć pomienionego Józefa że się aż ława wywróciła [?] za pchnięcie Urząd nakazuje aby dał grzywien nieodpuszczonych cztery y deprekacyą jako stronie tak Urzędowi uczynił y więzienia ma dzień siedzieć jako wyptasza swą winę należącą według tego Aktyu.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 237,
        "numer_pozycji": "Poz. 237",
        "strona_pagina": "fol. 115v (115v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Obdukcje i długi (1731 r.) / Obdukcja pobicia Boruchowej Jaskowej przez Wojciecha Frankiewicza oraz spór Leybusia ze Stanisławem Grasiem",
        "osoby_podmioty": "Boruchowa Jaskowa wdowa [Jaskowa]; Wojciech Frankiewicz [Frankiewicz]; Leybuś Ayzykowicz [Ayzykowicz]; Stanisław Graś winiarz [Graś]",
        "kwoty_podatki": "Dług 15 złp i 1,5 korca żyta (zasądzone 9 złp 6 gr i ćwierć żyta)",
        "opis_sprawy": "Sesja z 12 I 1731 r. (`Feria 6ta post Festum SS. Trium Regum 1731`): (1) obdukcja i protestacja Żydówki Boruchowej Jaskowej wdowy o ciężkie pobicie i rozcięcie czoła do kości przez Wojciecha Frankiewicza; (2) wyrok w sprawie Leybusia Ayzykowicza przeciw winiarzowi Stanisławowi Grasiowi o 15 złp, półtora korca żyta i 4 złp długu (pozwany przyznaje 9 złp 11 gr; sąd zasądza 9 złp 6 gr i ćwierć żyta albo przysięgę).",
        "transkrypcja": "115 v\nActum Crasnicy Coram Officio Composito Jurato Crasnicensi Feria 6ta post Festum Sanctorum Trium Regum 1731 Ano [12 I 1731 r.].\nObductio Niewierney Boruchowey Jaskowey [Jaskowa] Wdowy Obywatelki Kraśnickiey która takową pokazała ranę na czole na lewej wzdłuż od ławy przeciętą aż do kości od którego przecięcia y uderzenia twarz jej opuchła co ledwo oczy znać o opuchliny któremu pobiciu daje winę Wojciechowi Frankiewiczowi [Frankiewicz].\n\nSub Eodem Actu.\nTaż obductantka solennie się protestowała przeciw temu Wojciechowi Frankiewiczowi [Frankiewicz] iż bez dania okazyi jeszcze będąc winnym obductantce y nie upominając się natrząsa onemu a tak ciężko iest poraniony y skaliczony.\n\nSub Eodem Actu.\nW sprawie y Akcyi między Niewiernym Leybusiem Ayzykowicem [Ayzykowicz] Aktorem a Pozwanym Stanisławem Grasiem [Graś] Winiarzem ratione długu Aktorskiego co sobie pretenduje u pozwanego złotych piętnaście y żyta półkorca na to wziął Aktor złotych cztery od pozwanego pozwany zaś nie przyznaje tylko złp 9 gr 11.\nSąd Ninieyszy sprawy między stronami zważywszy unikając obrazy Bożej nakazuje aby pozwany oddał Aktorowi złp 9 gr 6 y żyta ćwierć albo przysięga za to co żyto. Pozwany zaś ma iść na więzienie którego nie wyjdzie póki albo tego nie odda...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 238,
        "numer_pozycji": "Poz. 238",
        "strona_pagina": "fol. 116r (116)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Sądownictwo i długi (1731 r.) / Wyrok dla wdowy Chudzikowej (wzmianka o pożarze Kraśnika), dług u Eliasza Moskowica oraz kontumacja Kozy",
        "osoby_podmioty": "Leybuś Ayzykowicz [Ayzykowicz]; Stanisław Graś winiarz [Graś]; Janowa Chudzikowa wdowa [Chudzikowa]; Jan Malborski [Malborski]; Boruch [Boruch]; Eliasz Moskowicz [Moskowicz]; Wojciech Koza [Koza]; Ficmanowa [Ficmanowa / Fielmanowa?]",
        "kwoty_podatki": "16 złp komornego i 5 złp 12 gr za siano (zasądzone 17 złp 12 gr); 9 złp 6 gr i ćwierć żyta dla Eliasza; 2 grzywny kary dla Kozy",
        "opis_sprawy": "(1) Dokończenie wyroku Leybusia ze Stanisławem Grasiem. (2) Wyrok w sprawie wdowy Janowej Chudzikowej przeciw Janowi Malborskiemu o 16 złp komornego i 5 złp 12 gr za siano — z niezwykle cenną wzmianką o pożarze Kraśnika (`podczas spalenia się Kraśnika nie mając się gdzie podzieć Boruch z żoną przyjęty do chałupy`); sąd zasądza 17 złp 12 gr. (3) Zapis długu Stanisława Grasia wobec Eliasza Moskowica (9 złp 6 gr i ćwierć żyta). (4) Kontumacja Wojciecha Kozy w sprawie Ficmanowej (2 grzywny i więzienie).",
        "transkrypcja": "116\n...albo się nie zaręczy takowym jako odda na czas którego się uprosi Aktorowi.\n\nSub Eodem Actu.\nW sprawie y Akcyi między Uczciwą Janową Chudzikową [Chudzikowa] Wdową Aktorką a Pozwanym Uczciwym Janem Malborskim [Malborski] y Małżonką Jego ratione złotych szesnastu za komorne y za siano złotych pięć gr 12 które by był powinien oddać do tych czas pozwany ale że zaś podczas spalenia się Kraśnika nie mając się gdzie podzieć Boruch [Boruch] y z żoną swoją że lubo jego Aktorka przyjęła do tej chałupy w której pozwani mieszkają y tenże Boruch mieszkał [?] Sąd Ninieyszy sprawy między stronami kontrowersyi zważywszy nakazuje pozwanemu aby oddał złotych 12 a cztery złote wytrąca się Aktorce za mieszkanie Borucha y przyznanych złp 5 gr 12 za siano co uczyni złp 17 gr 12 co aby pozwany oddał bez wszelkiej turbacyi y prawnych terminów od Aktu dzisiejszego za tydzień.\n\nSub Eodem Actu.\nZa dług Stanisława Grasia [Graś] Winiarza siedzącego na więzieniu ręczył Niewierny Eliasz Moskowicz [Moskowicz] jako za swym więźniem co powinien będzie oddać złp 9 gr 6 y żyta ćwierć.\n\nSub Eodem Actu.\nBędąc przypozwanym Uczciwy Wojciech Koza [Koza] trzema pozwami a nie stawa do sprawy na Instancyą Niewierney przeszłego Małżeństwa Ficmanowey [Fielmanowa / Ficmanowa?] za jego nieposłuszeństwo Contumax in Cujus Contumationem decernitur poena duo Marcarum parti et Judicio y więzienia dzień.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 239,
        "numer_pozycji": "Poz. 239",
        "strona_pagina": "fol. 116v (116v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Długi i ulgi podatkowe (1731 r.) / Sprawa Fielmanowej z Wojciechem Kozą (32 złp 15 gr) oraz wolnizna dla budującego się Augustyna Zbydniowicza",
        "osoby_podmioty": "Fielmanowa [Fielmanowa / Ficmanowa?]; Wojciech Koza [Koza]; Stanisław Kilianek [Kilianek]; Augustyn Zbydniowicz [Zbydniowicz]",
        "kwoty_podatki": "Dług 32 złp 15 gr za miód i trunek (wpłacono 18 złp), kara 2 grzywien i 2 dni więzienia; zwolnienie z podatków miejskich na 1 rok i 6 niedziel",
        "opis_sprawy": "Sesja z 15 I 1731 r. (`Feria 2da post Secundam Dominicam SS. Trium Regum 1731`): (1) sprawa Niewiernej Fielmanowej pierwszego małżeństwa przeciw Wojciechowi Kozie o 32 złp 15 gr z prowizją za miód przaśny i trunek (wpłacono 18 złp, reszta do rozliczenia przy Stanisławie Kilianku); z powodu niestawiennictwa Koza skazany na grzywnę sądowi, drugą stronie i dwa dni więzienia. (2) Zgoda urzędu na udzielenie wolnizny (zwolnienia od składek miejskich na 1 rok i 6 tygodni) dla Augustyna Zbydniowicza budującego się od nowa (`budując się de novo`).",
        "transkrypcja": "116 v\nActum Crasnicy Coram Officio Composito Jurato Crasnicensi Feria 2da post Secundam Dominicam SS. Trium Regum 1731 [15 I 1731 r.].\nW sprawie y Akcyi między Niewierną Fielmanową [Fielmanowa / Ficmanowa?] pierwszego Małżeństwa Aktorką a Pozwanym Uczciwym Wojciechem Kozą [Koza] ratione długu która Aktorka ma długu pieniędzmi gotowemi pożyczanego na miód przaśny [?] y za trunek co sobie Aktorka pretenduje u pozwanego złotych 32 gr 15 y z prowizyą od summy. Na to dał pozwany złp 18 na resztę zaś miał się porachować przy U. Stanisławie Kilianku [Kilianek] któremu aż dał pozwany Wojciech Koza na świadectwo aby stanął na środę blisko przyszłą strony aby stawali bez żadnych pozwów pod temi terminami a że zaś będąc Uczciwy Wojciech Koza [Koza] przypozwanym trzema pozwami a nie stanął który iest za nieposłuszeństwo Contumax za którą contumacyą aby dał grzywien jedną Sądowi a drugą stronie y więzienia dwa dni siedzieć.\n\nSub Eodem Actu.\nPrzed tenże Urząd personaliter stanąwszy Uczciwy Augustyn Zbydniowicz [Zbydniowicz] budując się de novo u którego Urzędu uprosił sobie aby był wolny od podatków skarbowych to jest składek potocznych miejskich do Roku sześciu Niedziel którego wolnym uczynili.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 240,
        "numer_pozycji": "Poz. 240",
        "strona_pagina": "fol. 117r (117)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Sądownictwo łączone (1731 r.) / Sprawa Nowaków z Ćwikową, długi po śp. wójcie u Marszałka i Frankiewicza oraz wyrok Rubinsteyna z Tokarczykiem",
        "osoby_podmioty": "Antoni Nowak [Nowak]; Marcinowa Ćwikowa [Ćwikowa]; Maryana [Maryana]; Stanisław Szymon Marszałek [Marszałek]; Wojciech Frankiewicz [Frankiewicz]; Mosiek Rubinsteyn [Rubinsteyn]; Kazimierz Tokarczyk [Tokarczyk]",
        "kwoty_podatki": "3 złp długu za trunek i owies (zasądzony 1 złp w najbliższą niedzielę)",
        "opis_sprawy": "Sesja z 17 I 1731 r. (`Feria 4ta post Festum SS. Trium Regum intra Dominicam 3tiam 1731`): (1) odroczenie sprawy Antoniego Nowaka i jego żony przeciw Marcinowej Ćwikowej o zwadę na Rynku; (2) odroczenie sprawy Maryany przeciw Stanisławowi Szymonowi Marszałkowi i jego szwagrowi Wojciechowi Frankiewiczowi o dług z rejestru śp. wójta (po śmierci nieboszczyka); (3) wyrok w sprawie Mośka Rubinsteyna przeciw Kazimierzowi Tokarczykowi o 3 złp za trunek i owies (nakaz zapłaty 1 złp w niedzielę bez obrazy boskiej).",
        "transkrypcja": "117\nActum Crasnicy Feria 4ta post Festum SS. Trium Regum intra Dominicam 3tiam 1731 Ano [17 I 1731 r.].\nW sprawie y Akcyi między Uczciwym Antonim Nowakiem [Nowak] y Małżonką Jego Aktorami a Pozwaną Uczciwą Marcinową Ćwikową [Ćwikowa] w tej sprawie daje się dylacyi którzy się powadzili na Rynku aby strony obiedwie stanęły na godzinę po południu [?] y pod temi terminami aby na piątek stawali bez pozwów.\n\nSub Eodem Actu.\nW sprawie y Akcyi między Niewierną Maryanką [Maryana] Aktorką a Pozwanym Stanisławem Szymonem Marszałkiem [Marszałek] y Szwagrem Jego Wojciechem Frankiewiczem [Frankiewicz] ratione długu który dług był wypisany regestrem ręką nieboszczyka Pana Wójta który dług aby Aktorka pokazała regestrem kiedy nieboszczyk przyznał co zaś przyznany dług ten exceptis długu musi być oddany jako to po śmierci nieboszczyka brany któremu stronom do pokazania swoich należytościów daje się dylacyi do piątku blisko przyszłego tak Aktorce do pokazania regestru jako y pozwanym bez winy pod temi terminami aby bez kosztów stawali.\n\nSub Eodem Actu.\nW sprawie y Akcyi między Niewiernym Moskiem Rubinsteynem [Rubinsteyn] Aktorem a Pozwanym Uczciwym Kazimierzem Tokarczykiem [Tokarczyk] ratione długu co sobie Aktor pretenduje u pozwanego złotych trzy za trunek y za owies. Co pozwany neguje y wymawia się że temu Aktorowi nic nie winien Sąd Ninieyszy nakazuje aby pozwany dał Aktorowi złoty jeden na niedzielę blisko przyszłą unikając obrazy Boskiey co Sąd Ninieyszy przykazuje.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 241,
        "numer_pozycji": "Poz. 241",
        "strona_pagina": "fol. 117v (117v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Długi i przysięgi sądowe (1731 r.) / Sprawa Maryany z Jakubem Troycakiem (54 złp) oraz rozłożenie na raty długu Wojciecha Kozy (21 złp)",
        "osoby_podmioty": "Maryana [Maryana]; Jakub Troycak [Troycak]; Wojciech Koza [Koza]",
        "kwoty_podatki": "54 złp (spłacone 29 złp żytem + 5 złp, do przysięgi 20 złp); 21 złp rozłożone na 3 raty + 3 gr 20 (lub 3 złp 20 gr) za trunek",
        "opis_sprawy": "Dokończenie sesji z 17 I 1731 r.: (1) wyrok w sprawie Maryany przeciw Jakubowi Troycakowi o dług 54 złp (spłacono 29 złp żytem i 5 złp gotówką = 34 złp; na pozostałe 20 złp nakazano przysięgę Maryany w bóżnicy na Rodale); (2) wyrok w sprawie Maryany przeciw Wojciechowi Kozie o dług 21 złp rozłożony na 3 raty (Wstępna Niedziela 6 złp 20 gr, Śródpoście 7 złp, Świątki 7 złp) oraz rozliczenie za trunek.",
        "transkrypcja": "117 v\nSub Eodem Actu.\nW sprawie y Akcyi między Niewierną Maryanką [Maryana] Aktorką a Pozwanym Uczciwym Jakubem Troycakiem [Troycak] ratione długu który sobie pretenduje u pozwanego złp 54 co pozwany dał na to żyta złp 29 y złotych 5 sprzedanych co uczyni 34 według zaś rachunku Aktorki to się zostało winien złotych pozwany Aktorce złp 20 na które ma Aktorka wykonać Jurament od dnia dzisiejszego za tydzień w Bóżnicy na Rodale jako prawdziwie y słusznie winien Aktorce przy którym Juramencie aby miał pozwany gotowe pieniądze po uczynionym y wypełnionym Juramencie na co Aktorka przysięże aby jej oddał to złotych 20 którego Juramentu aby pasierb pozwanego słuchał.\n\nSub Eodem Actu.\nW sprawie y Akcyi między Niewierną Maryanką [Maryana] Aktorką a Pozwanym Uczciwym Wojciechem Kozą [Koza] ratione długu przyznanego Aktorce złotych 21 które Sąd zważywszy y widząc ciężkość teraźnieyszą na której by lubo nie potrzeba uważać Sąd przykazuje aby te złotych 21 oddał na rat trzy pierwszą na Wstępną Niedzielę złp 6 gr 20 drugą na Śródpoście złp 7 trzecią na Świątki złp 7 o złotych zaś trzy gr 20 za trunek się porachowali a przed temi ratami za trunek pieniądze oddane były co się zaś tycze złotych trzech za Janka które przyrzekł pozwany aby y te Janeczka w piątek przywoławszy do Urzędu aby Aktorce oddane były prawne terminy y koszta aby oddane były y prowizya ma być porachowana y oddana.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 242,
        "numer_pozycji": "Poz. 242",
        "strona_pagina": "fol. 118r (118)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Długi i procesy (1731 r.) / Dług Kozy u Rubinsteyna po śp. Kilianku, skarga Nowaka na Ćwikową oraz proces Jaskowej z Frankiewiczem",
        "osoby_podmioty": "Mosiek Rubinsteyn [Rubinsteyn]; Wojciech Koza [Koza]; Stanisław Kilianek zmarły [Kilianek]; Antoni Nowak [Nowak]; Marcinowa Ćwikowa [Ćwikowa]; Jaskowa Boruchowa wdowa [Jaskowa]; Wojciech Frankiewicz [Frankiewicz]; Stanisław Frankiewicz [Frankiewicz]",
        "kwoty_podatki": "6 złp długu po śp. Kilianku (zasądzone 2 złp); długi Frankiewiczów: 13 złp po ojcu, 9 złp własny, 4 złp po bracie Stanisławie",
        "opis_sprawy": "(1) Wyrok w sprawie Rubinsteyna przeciw Wojciechowi Kozie o 6 złp długu po nieboszczyku Stanisławie Kilianku (zasądzone 2 złp w najbliższą niedzielę). (2) Sesja z 19 I 1731 r. (`Feria 6ta post Secundam Dominicam post Festum SSS. Trium Regum 1731`): protestacja Antoniego Nowaka przeciw Marcinowej Ćwikowej o obelgi na Rynku przed sprawą. (3) Sprawa Jaskowej Boruchowej wdowy przeciw urodzonemu Wojciechowi Frankiewiczowi o długi po ojcu (13 złp), własny (9 złp) i po bracie Stanisławie (4 złp) oraz o pobicie w głowę.",
        "transkrypcja": "118\nSub Eodem Actu.\nW sprawie y Akcyi między Niewiernym Rubinsteynem [Rubinsteyn] Aktorem a Pozwanym U. Wojciechem Kozą [Koza] ratione długu nieboszczykowskiego Stanisława Wiarza [Kilianek] którego sobie Aktor długu pretenduje złp 6 ale że zaś świadectwem pokazał U. Stanisław Kilianek [Kilianek] jako jego imienia końce zawróciła Rubinsteynowi za ten dług z jej powieści. Więc Sąd przykazuje Uczciwemu Wojciechowi Kozie aby ciężkości nie czynił tak nieboszczykowi jako y swojej Małżonce przeszłego Małżeństwa aby oddał Rubinsteynowi na niedzielę przyszłą złotych dwa unikając obrazy Bożej y ciężkości duszy nie czyniąc bez żadnej egzekucyi ani prawnych terminów.\n\nActum Crasnicy Coram Officio Composito Jurato Crasnicensi Feria 6ta post Secundam Dominicam post Festum SSS. Trium Regum 1731 [19 I 1731 r.].\nPrzed tenże Urząd personaliter stanąwszy Uczciwy Antoni Nowak [Nowak] z małżonką swoją solennie się protestował przeciw Marcinowej Ćwikowej [Ćwikowa] która protestanta nieuczciwie na Rynku obsyłała jeszcze przed sprawą na co ma świadectwo.\n\nSub Eodem Actu.\nW sprawie y Akcyi między Urodzoną Niewierną Jaskową [Jaskowa] Wdową Aktorką a Pozwanym Urodzonym Wojciechem Frankiewiczem [Frankiewicz] ratione naprzód długu za ojca pozwanego pretenduje sobie Aktorka złotych 13 item za pozwanego samego pretenduje złp 9 item u brata pozwanego Stanisława [Frankiewicz] pretenduje złotych 4 które miał pozwany za brata swego płacić. W tej sprawie daje się dylacyi do poniedziałku blisko przyszłego aby pozwany stawił swe dokumenta y regestra czy powinien płacić za ojca swego nieboszczyka tudzież y za brata dla czego do tych czas nie oddał y za siebie ratione zaś Aktorki skaleczenia w głowę ta sprawa będzie...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 243,
        "numer_pozycji": "Poz. 243",
        "strona_pagina": "fol. 118v (118v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Długi i zniewaga sądu (1731 r.) / Długi Frankiewiczów i Marszałka zabezpieczone na ogrodzie za Bramą Krakowską oraz reprotestacja Frankiewicza",
        "osoby_podmioty": "Jaskowa Boruchowa wdowa [Jaskowa]; Szymon Marszałek [Marszałek]; Wojciech Frankiewicz [Frankiewicz]; Kacper Frankiewicz zmarły [Frankiewicz]; Stanisław Frankiewicz [Frankiewicz]; Maryana [Maryana]",
        "kwoty_podatki": "31 złp 24 gr (oraz 13 złp i 18 złp) długu po śp. Kacprze Frankiewiczu zapisane na ogrodzie za Bramą Krakowską",
        "opis_sprawy": "(1) Dokończenie nakazu stawienia świadków w sprawie pobicia Jaskowej. (2) Wyrok w sprawie Maryany przeciw Szymonowi Marszałkowi i jego szwagrowi Wojciechowi Frankiewiczowi o dług po śp. Kacprze Frankiewiczu (31 złp 24 gr, 13 złp i 18 złp z pszenicą) — nakaz zabezpieczenia długu na gruncie, tj. ogrodzie za Bramą Krakowską. (3) Reprotestacja urodzonego Wojciecha Frankiewicza przeciw Jaskowej wdowie o obelgi rzucone przed sądem przy krucyfiksie (*„ty chytrcu coś bożemu tobie psy bić po mieście”*).",
        "transkrypcja": "118 v\n...przy kupie tylko aby świadectwo z obu stron stawili jaka okazya była tego skaleczenia y kto był motorem do tego.\n\nSub Eodem Actu.\nW sprawie y Akcyi między Sławetnym Szymonem Marszałkiem [Marszałek] Niewierną Maryanką [Maryana] Aktorką a Pozwanym Sławetnym Szymonem Marszałkiem y Szwagrem Jego Wojciechem Frankiewiczem [Frankiewicz] ratione długu nieboszczykowskiego Kacpra Frankiewicza [Frankiewicz] tak pozwanego jak y szwagra jego Wojciecha Frankiewicza którego długu było złotych 31/24 na to wzięta pszenica której dwa korce zabrano złotych 13 co Aktorka nie przyznaje tylko korzec to oddał na drugi zaś korzec aby przyświadczył Stanisław Frankiewicz [Frankiewicz] jako z rąk swoich oddał Aktorce co się Aktorce przyznało y żyta korca pszenicy jeszcze nie przyznanym złotych 18 aby ten dług pozwany zapisuje na gruncie to jest na ogrodzie swoim za Bramą Krakowską leżącym jako wolno będzie [?] Aktorce komu zastawić w tej summie y ten ma mocen być do trzymania póki summa oddana nie będzie co zaś mają wzgląd na pozwanego aby się szwagrowie pomiarkowali z długu co nieboszczyk ojciec ich winien został y Wojciech Frankiewicz jako karta [?] ręką nieboszczykowską podpisana.\n\nSub Eodem Actu.\nPrzed tymże Urzędem będąc przypozwanym Urodzony Wojciech Frankiewicz [Frankiewicz] od Niewierney Jaskowey [Jaskowa] Wdowy który do sprawy stanąwszy chcąc się justifikować z jakiej okazyi skaleczył pomienioną Jaskową która naprzód przy stojącym Krucyfiksie na stole y przy Obojnym Urzędzie tak y ławnikach ciężko skonfundowała słowy nieuczciwemi ty chytrcu coś bożemu tobie psy bić po mieście nie tylko słowami ale y córka jej powtóre przyszedłszy do Urzędu te same słowa wołała y inne co jej mogła ślina do gęby przynieść [?] o co się pomieniony Wojciech Frankiewicz solennie z wielkim żalem protestował.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 244,
        "numer_pozycji": "Poz. 244",
        "strona_pagina": "fol. 119r (119)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Długi i zeznania (1731 r.) / Wyrok Maryany z Łukaszem Wójcikiem oraz zeznanie kowala Wojciecha Żakowskiego o zajściu z kożuchem u Jaskowej",
        "osoby_podmioty": "Maryana [Maryana]; Łukasz Wójcik [Wójcik]; Wojciech Żakowski kowal [Żakowski]; Wojciech Frankiewicz [Frankiewicz]; Franek [Franek]; Boruchowa Jaskowa [Jaskowa]",
        "kwoty_podatki": "Dług 29 złp 15 gr (zapłacone 8 złp, do oddania 13 złp 15 gr + 6 złp)",
        "opis_sprawy": "Sesja z 22 I 1731 r. (`Feria 2da post Festum Sanctae Agnetis 1731`): (1) wyrok w sprawie Maryany przeciw Łukaszowi Wójcikowi o 29 złp 15 gr (dał 8 złp, pozostało 13 złp 15 gr oraz 6 złp; sąd nakazuje zapłacić 3 złp 15 gr od razu i odłożyć 3 złp); (2) zeznanie kowala Wojciecha Żakowskiego o tym, jak podpity Wojciech Frankiewicz oddał mu kożuch do trzymania, a gdy Jaskowa odmówiła zwrotu zatrzymanego kożucha za długi, uderzył ją w głowę nogą od stołka.",
        "transkrypcja": "119\nActum Crasnicy Coram Officio Composito Jurato Crasnicy Feria 2da post Festum Sanctae Agnetis 1731 Ano [22 I 1731 r.].\nW sprawie y Akcyi między Niewierną Maryanką [Maryana] Aktorką a Pozwanym Uczciwym Łukaszem Woycikiem [Wójcik] ratione długu złp 29/15 na to Aktorce dał złotych ośm Sąd Ninieyszy sprawy między stronami przesłuchawszy nakazuje aby pozwany swój dług przyznany złp 13/15 oddał na rat dwie pierwszą od Aktu dzisiejszego za tydzień na wstępną Niedzielę, to zaś złotych 6 które nie przyznaje pozwany Sąd na dalsze nakazuje Aktori złotych 18 aby oddał pozwany in instanti złotych trzy gr 15 złotych zaś 3 unikając obrazy Bożej aby odniosła złotych 3 co dekretem naszym przykazujemy aby strona Aktorowa według dekretu kontentowana była.\n\nSub Eodem Actu.\nWojciech Żakowski [Żakowski] Kowal tacto pectore haec formalia recognovit że będąc dużo podpitym Wojciech Frankiewicz [Frankiewicz] dał sobie kożuch trzymać Frankowi [Franek] idąc w taniec co jako y nie tańcował tylko o kożuch upominając się co powiedział że jego Jaskowa [Jaskowa] wzięła do komory upominając się Jaskowey o kożuch mówiąc na co mi kożuch wzięła a ona odpowiedziała że za dług nic tylko [?] ten się rozgniewawszy nogę od stołka w głowę uderzył.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 245,
        "numer_pozycji": "Poz. 245",
        "strona_pagina": "fol. 119v (119v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Zeznania i długi (1731 r.) / Zeznania Franciszka Budnickiego i Mikołaja Szymki o kożuchu oraz ciąg dalszy sprawy Boruchowej z Frankiewiczem",
        "osoby_podmioty": "Wojciech Frankiewicz [Frankiewicz]; Franciszek Budnicki [Budnicki]; Boruchowa Jaskowa [Jaskowa]; Mikołaj Szymko [Szymko]; Kacper Frankiewicz zmarły [Frankiewicz]",
        "kwoty_podatki": "Dług po śp. Kacprze Frankiewiczu z rejestru: 12 złp 23 gr + 11 złp + 1 złp 23 gr + 14 złp (= 25 złp)",
        "opis_sprawy": "Sesja z 24 I 1731 r. (`Feria 4ta ante Festum Conversionis Sancti Pauli Apostoli 1731`): (1) zeznania świadków Franciszka Budnickiego i Mikołaja Szymki z instancji Wojciecha Frankiewicza o oddaniu kożucha do schowania w komorze oraz uderzeniu Boruchowej w głowę podczas kłótni o długi ojca; (2) początek wyroku w sprawie Boruchowej przeciw Wojciechowi Frankiewiczowi i jego szwagrowi o dług 25 złp po śp. Kacprze Frankiewiczu (ciąg dalszy na skanie 246).",
        "transkrypcja": "119 v\nActum Crasnicy Coram Officio Composito Jurato Crasn. Feria 4ta ante Festum Conversionis Sancti Pauli Apostoli 1731 [24 I 1731 r.].\nNa Instancyą Urodzonego Wojciecha Frankiewicza [Frankiewicz] in quantum na wyjściu dana jest Inkwizycya której Inkwizycyi sequitur tenor talis:\n\nTestis Pracowity Franciszek Budnicki [Budnicki] sub Juramento tali recognovit że zabawiając się Wojciech Frankiewicz [Frankiewicz] nieborak będąc podpitym dał mi kożuch do trzymania co ten kożuch trzymając bojąc się aby nie zginął dałem do komory schować po tym jak już miał odchodzić Wojciech Frankiewicz spytał się mnie gdzie kożuch mój y [?] do sieni a córce Jaskowey [Jaskowa] aby kożuch oddała co go schowała to matka powiedziała że nie oddam boście winni za ojca tak y za siebie nie oddam ten rozgniewawszy nie widział czym uderzył w głowę Jaskową.\n\n2dus Testis Uczciwy Mikołaj Szymko [Szymko] ex parte Jaskowey similia recognovit.\n\nSub Eodem Actu.\nW sprawie y Akcyi między Niewierną Boruchową [Jaskowa] a Wojciechem Frankiewiczem [Frankiewicz] y szwagrem jego ratione długu za nieboszczyka ojca śp. Kacpra Frankiewicza [Frankiewicz] na nasz czas kraśnickim który został winien był według regestru złp 12/23 na to oddali sukcessorowie złp 11 resztę długu przyznanego złp 1 gr 23 sprzecznych które sobie Aktorka pretenduje złotych 11 [?] Wojciech Frankiewicz z bratem swym Stanisławem [Frankiewicz] złotych 14 co uczyni złotych 25 Sąd Ninieyszy sprawy między stronami przesłuchawszy nakazuje...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 246,
        "numer_pozycji": "Poz. 246",
        "strona_pagina": "fol. 120r (120)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Wyroki i taksy majątkowe (1731 r.) / Finał sprawy Boruchowej z Frankiewiczem (35 złp i 5 złp 18 gr cyrulikowi) oraz taksa kontuszów i żupana z 25 I 1731 r.",
        "osoby_podmioty": "Boruchowa Jaskowa [Jaskowa]; Wojciech Frankiewicz [Frankiewicz]; Kacper Frankiewicz zmarły [Frankiewicz]; Tomasz Tyrański [Tyrański]; Matyasz Latosłowicz [Latosłowicz]",
        "kwoty_podatki": "25 złp + 1 złp 23 gr + 10 złp nawiązki + 5 złp 18 gr dla cyrulika (łącznie 35 złp na ogrodzie); taksa kontuszów: 22 złp, 19 złp, żupan 16 złp",
        "opis_sprawy": "(1) Dokończenie wyroku w sprawie Boruchowej Jaskowej przeciw Wojciechowi Frankiewiczowi: uznanie 25 złp długu po Kacprze Frankiewiczu, 10 złp nawiązki za skaleczenie w głowę oraz 5 złp 18 gr dla cyrulika — z zabezpieczeniem łącznej kwoty 35 złp na ogrodzie, chałupie i stodole za stodołą. (2) Sesja Sądu Radzieckiego z 25 I 1731 r. (`ipso Festo Conversionis S. Pauli 1731`): urzędowe oszacowanie odzieży — kontusza niebieskiego Tomasza Tyrańskiego na 22 złp, kontusza niebieskiego Matyasza Latosłowicza na 19 złp oraz żupana granatowego tegoż Latosłowicza na 16 złp.",
        "transkrypcja": "120\n...Aktorka dla Boga w kościele przysięże to jest w piątek przyszły przysięgła jako prawdziwie y należycie złp 25 winni są sukcessorowie śp. Kacpra Frankiewicza [Frankiewicz] co zaś złp 1 gr 23 długu przyznanego aby in instanti oddane były Aktorce co zaś na gramach Aktorka przysięże uważając na podupadłość pozwanych zapisuje się na swym własnym ogrodzie za stodołą leżącym jako wolno będzie Aktorce zastawić komu się jej podobało póki summa pomieniona oddana nie będzie. Co Aktorce przysięże jako zaś pobicie Aktorki jako [?] świadomy y iest zapisano którą w głowę skaleczył Wojciech Frankiewicz [Frankiewicz] lubo prawda że y Aktorka będąc winną się podpitemu o dług upominała y kożuch jemu do komory chować kazała Sąd przykazuje lubo będzie winny aby dał Aktorce złotych 10 y z kosztami prawnemi za jej cierpliwość także aby dał cyrulikowi złotych 5 gr 18 które y te mają być na tymże ogrodzie zapisane jednak pozwany aby ten złoty jeden oddał y gr 23 y cyrulikowi za co iest ugodno a reszta summy to jest złp 35 że na ogrodzie, w chałupie y stodole zapisane są y kto będzie chciał mieszkać ten powinien ten dług oddać co się obiecujemy Aktorce przykazuje.\n\nActum Crasnicy Coram Officio Consulari Feria 5ta ipso Festo Conversionis Sancti Pauli 1731 [25 I 1731 r.].\nTaksa kontusza Uczciwego Tomasza Tyrańskiego [Tyrański] niebieskiego tabinowego z potrzebami jedwabnymi mało co przechodzony który był oszacowany złp 22.\nKontusz drugi niebieski kierowy z jedwabnymi potrzebami Uczciwego Matyasza Latosłowicza [Latosłowicz] kontusz oszacowany złp 19.\nItem żupan granatowy tegoż Matyasza Latosłowicza [Latosłowicz] oszacowany złp 16 z potrzebami przedniemi.\nItem kontusz z rycerska niebieski z potrzebami...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 247,
        "numer_pozycji": "Poz. 247",
        "strona_pagina": "fol. 120v (120v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Taksy, obdukcje i protestacje (1731 r.) / Dokończenie taksy garderoby, obdukcja pobicia na weselu u Wilka oraz skarga Judy Kowiena na Jardzyka",
        "osoby_podmioty": "Szymon Jankowski prezydent [Jankowski]; Benedykt Szmatkowski burmistrz [Szmatkowski]; Matyasz Fruga [Fruga / Frug?]; Stanisław Wilk [Wilk]; Jędrzej Skatka [Skatka]; Błasiak [Błasiak]; Łurek [Łurek?]; Juda Kowien [Kowien]; Jan Jardzyk [Jardzyk]",
        "kwoty_podatki": "Taksa kontusza na 18 złp; najem furmanki z solą do Bełżyc",
        "opis_sprawy": "(1) Dokończenie taksy garderoby (kontusz oszacowany na 18 złp przy prezydencie Szymonie Jankowskim, cechmistrzu krawieckim i burmistrzu Benedykcie Szmatkowskim). (2) Sesja z 29 I 1731 r.: protestacja i obdukcja ran Matyasza Frugi i Stanisława Wilka pobitych przez Jędrzeja Skatkę, Błasiaka i Łurka podczas wesela w domu Stanisława Wilka. (3) Podziękowanie burmistrza Benedykta Szmatkowskiego za prezydencję przy wójtach i cechmistrzach. (4) Sesja z 5 II 1731 r. (św. Agaty): protestacja Żyda Judy Kowiena z żoną przeciw Janowi Jardzykowi o porzucenie w Bełżycach z solą i zerwanie czapki na Rynku w Kraśniku.",
        "transkrypcja": "120 v\n...alias potrzebami łokciowemi ten oszacowany złotych 18 przy której taxie byli sławetni mężowie Szymon Jankowski [Jankowski] Prezydent na ten czas Kraśnicki y Cechmistrz Krawiecki y Benedykt Szmatkowski [Szmatkowski] Burmistrz Kraśnicki.\n\nActum Crasnicy Coram Officio Composito Jurato Crasnicensi Feria 2da ante Festum Purificationis Beatissimae Virginis 1731 [29 I 1731 r.].\nPrzed tymże Urzędem personaliter stanąwszy Uczciwy Matyasz Fruga [Fruga / Frug?] y Stanisław Wilk [Wilk] solennie się protestowali przeciw pracowitym Jędrzejowi Skatce [Skatka], Błasiakowi [Błasiak] y Łurkowi [Łurek?] naprzód że podczas weselnego aktu dom naszli u Stanisława Wilka [Wilk] y w tym domu dawszy okazyą Matyaszowi Frugowi [Fruga] jeszcze na dworze będącego [?] rękę potłukli lewą y członki pozbijali, głowę bili y kilka razy w głowę uderzony suchemi razami obduktant iakże y świadkami opowie jako nie winien iest skaleczenia y gdyby na gwałt nie zawołał był obduktant to by był może y zabitym został y na gwałt ludzie wybiegli którzy obduktanta obronili.\n\nSub Eodem Actu.\nUrzędowi dzięki odebrał Sławetny Benedykt Szmatkowski [Szmatkowski] z prezydencyi swojej przy sławetnych burmistrzach y cechmistrzach y wójtach przedmieyskich.\n\nActum Crasnicy Coram Officio Composito Jurato Crasnicensi Feria 2da Ipso Festo Sanctae Agathae 1731 [5 II 1731 r.].\nPrzed tenże Urząd personaliter stanąwszy Niewierny Juda Kowien [Kowien] y z Małżonką swoją solennie się protestowali przeciw Janowi Jardzykowi [Jardzyk] iż będąc najętym od protestanta do Bełżyc z solą którego to protestanta mając jeszcze soli trzy korce w Bełżycach odjechał to protestant musiał płacić za trunek innemu furmanowi po tym w Bożną Niedzielę w Kraśniku...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 248,
        "numer_pozycji": "Poz. 248",
        "strona_pagina": "fol. 121r (121)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Zastawy, taksy i długi (1731 r.) / Taksa zagrabionej jałowicy (18 złp) za dług Pawła Tokarczyka wobec Leybusia oraz sprawa Lachmana z Rępką",
        "osoby_podmioty": "Juda Kowien [Kowien]; Jan Jardzyk [Jardzyk]; Leybuś Ayzykowicz [Ayzykowicz]; Paweł Tokarczyk [Tokarczyk]; Jan Jardzyk wójt Gór i Podlesia [Jardzyk]; Bartosz Zdyb [Zdyb]; Lachman Slomowicz [Lachman]; Grzegorz Rępka [Rępka]",
        "kwoty_podatki": "Dług 24 złp za konia (taksa zagrabionej jałowicy 18 złp); dług za 13,5 garnca gorzałki (16 złp 24 gr) i 1 złp 19 gr 2 szelągi za trunek",
        "opis_sprawy": "(1) Dokończenie skargi Judy Kowiena na Jana Jardzyka o znieważenie na Rynku i zrzucenie czapki. (2) Sesja z 8 II 1731 r. (`Feria 5ta ante Dominicam Cinerum 1731`): Leybuś Ayzykowicz okazuje jałowicę małą graniastą zagrabioną z rozkazu Administratora Pawłowi Tokarczykowi za dług 24 złp za konia; wójt Gór i Podlesia Jan Jardzyk i Bartosz Zdyb szacują jałowicę na 18 złp. (3) Sesja z 14 II 1731 r. (`Feria 4ta post Dominicam Cinerum 1731`): sprawa Lachmana przeciw Grzegorzowi Rępce i jego żonie o niedodanie 13,5 garnca gorzałki (16 złp 24 gr) oraz 1 złp 19 gr 2 szelągi za trunek.",
        "transkrypcja": "121\n...znieważył na Rynku y bić którego chciał y czapkę mu wziął co protestant bez czapki musiał uchodzić y gdzie z okazyi gonił na co protestant ma świadectwo iterum iterum protestatur.\n\nActum Crasnicy Coram Officio Composito Jurato Crasnicensi Feria 5ta ante Dominicam Cinerum 1731 [8 II 1731 r.].\nPrzed tenże Urząd personaliter stanąwszy Niewierny Leybuś Ayzykowicz [Ayzykowicz] będąc mu winnym U. Paweł Tokarczyk [Tokarczyk] za konia złotych 24 któremu się upominając przez długi czas a długu pomienionego oddać nie chciał którego z rozkazu Pana Administratora swojego zagrabił to jest jałowicę niewielką graniastą czarną którą kazawszy przyprowadzić do Urzędu na ten Urząd postawiwszy po taksowych ludzi znających się na tym którzy ją oszacowali złotych 18 która to jałowica będzie upominającego Leybusia pod taksą niż [?] na której taxie byli Uczciwi Jan Jardzyk [Jardzyk] wójt Gór y Podlesia, Bartosz Zdyb [Zdyb] mieszczanin Kraśnicki.\n\nActum Crasnicy Coram Officio Composito Jurato Crasnicensi Feria 4ta post Dominicam Cinerum 1731 [14 II 1731 r.].\nW sprawie y Akcyi między Niewiernym Lachmanem Slomowiczem [Lachman] Aktorem a Pozwanym Uczciwym Grzegorzem Rępką [Rępka] y Małżonką Jego ratione gorzałki niedodania winnemi być Aktorowi garncy 13 y pół za którą uczyni złotych 16/24 za trunek przyznany należy się Aktorowi złp 1 gr 19 szelągów 2 co Aktor pretenduje u pozwanych konwi miodu gorzałczanego...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 249,
        "numer_pozycji": "Poz. 249",
        "strona_pagina": "fol. 121v (121v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Długi i przysięgi (1731 r.) / Wyroki w sprawach Lachmana z Grzegorzem Rępką (gorzałka) oraz z Szymonem Truskawką",
        "osoby_podmioty": "Lachman [Lachman]; Grzegorz Rępka [Rępka]; Eliasz [Eliasz]; Szymon Truskawka [Truskawka]",
        "kwoty_podatki": "13,5 garnca gorzałki (16 złp 24 gr + 1 złp 19 gr 2 szelągi), zwrot worków i konwi; 9 złp 19 gr długu Szymona Truskawki",
        "opis_sprawy": "(1) Dokończenie wyroku w sprawie Lachmana przeciw Grzegorzowi Rępce: nakaz przysięgi „samo wtór” w Bóżnicy na Rodale na 13,5 garnca gorzałki, oddania do sekwestru 16 złp 24 gr i 1 złp 19 gr 2 szelągi oraz rozliczenia worków i konwi pobranych od Żyda Eliasza. (2) Sesja z 16 II 1731 r. (`Feria 6ta post Dominicam Cinerum 1731`): wyrok w sprawie Lachmana i jego żony przeciw Szymonowi Truskawce o 9 złp 19 gr długu (przysięga w Bóżnicy na Rodale).",
        "transkrypcja": "121 v\n...którego pozwani negują worków dwa y konew na tukar sobie Aktor pretenduje co pozwany powiada że od Eliasza [Eliasz] oddał. Pozwany zaś pretenduje u Aktora miodu gorzałczanego ćwiertni 2 y mąki ćwiertni czego Aktor nie przyznał jako nie winien.\nSąd Ninieyszy sprawy między stronami przesłuchawszy nakazuje Aktorowi jako prawdziwie winny iest pozwany gorzałki garncy 13 y pół, miodu ćwiertni 1 gorzałczanego co Aktor ma przysiądz samo wtór w Bóżnicy na Rodale według zwyczaju żydowskiego w sobotę blisko przyszłą oraz o tym miodzie co pozwany pretenduje a Aktor neguje. Pozwany zaś po wykonaniu Juramentu aby oddał do sekwestru za gorzałkę złp 16 gr 24 przyznanych zaś złp 1 gr 19 szel. 2 przed Juramentem o worki zaś aby dokument pokazał iż Eliasz [Eliasz] wziął y na konew a inquantum się nie pokaże aby worki za worki oddał y konew spustną której Jurament ma wykonać od Aktu dzisiejszego za tydzień.\n\nActum Crasnicy Coram Officio Jurato Crasnicensi Feria 6ta post Dominicam Cinerum 1731 Ano [16 II 1731 r.].\nW sprawie y Akcyi między Niewiernym Lachmanem [Lachman] y Małżonką Jego Aktorami a Pozwanym Uczciwym Szymonem Truskawką [Truskawka] ratione długu różnemi czasy nabranego złotych 9 gr 19 których pozwany neguje jako nie winien Aktorom tego długu. Sąd Ninieyszy sprawy między stronami zważywszy z obydwu stron dokładnie przesłuchawszy iż pozwany tego długu neguje jako nie iest winny więc Sąd przykazuje Aktorom aby Jurament wykonali w Bóżnicy na Rodale według Roty ustawnej opisanej jako winny iest który Jurament aby pozwany miał gotową przed Juramentem tę sumę ma wykonać od Aktu dzisiejszego w dzień sądowy.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 250,
        "numer_pozycji": "Poz. 250",
        "strona_pagina": "fol. 122r (122)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1731",
        "kategoria": "Sądownictwo łączone (1731 r.) / Przysięga Stanisława Grasia w sprawie obrazy Leybusia oraz spór o zagubioną bronę (Szostakiewicz v. Ćwiek)",
        "osoby_podmioty": "Leybuś Ayzykowicz [Ayzykowicz]; Stanisław Graś winiarz [Graś]; Jan Szostakiewicz [Szostakiewicz?]; Jan Ćwiek [Ćwiek]; Andrzej Boguta [Boguta]",
        "kwoty_podatki": "Przysięga oczyszczająca Stanisława Grasia; spór o zaginioną bronę",
        "opis_sprawy": "(1) Sesja z 22 II 1731 r. (`Feria 5ta ante Festum Sancti Mathiae Apostoli 1731`): wyrok w sprawie Leybusia Ayzykowicza przeciw winiarzowi Stanisławowi Grasiowi o słowa wymówione w winiarni pod wpływem alkoholu (nakaz przysięgi oczyszczającej dla Grasia). (2) Sesja z 23 II 1731 r. (`in Vigilia Sancti Mathiae 1731`): sprawa Jana Szostakiewicza przeciw Janowi Ćwiekowi o zagubioną bronę pożyczoną do włóczenia, przekazaną dalej Andrzejowi Bogucie.",
        "transkrypcja": "122\nActum Crasnicy Coram Officio Composito Jurato Crasnicensi Feria 5ta ante Festum Sancti Mathiae Apostoli 1731 [22 II 1731 r.].\nW sprawie y Akcyi między Niewiernym Leybusiem Ayzykowiczem [Ayzykowicz] Aktorem a Pozwanym Stanisławem Grasiem [Graś] Winiarzem ratione słów wymówionych jako by miał pozwany słyszeć od Żyda w tymże czasie podpiwszy w winiarni wypadły słowa z tego co się pokazało y z inkwizycyi jako y [?] po tym co pozwany przed sądem wymówił tylko zaś Żydowi się pozwany wymawia że ia tego nie słyszał od nikogo tylko żem to wymówił jedno przed pozwanym kiedy winiarzowi z żalem powiedział jego byt jako go w karczmie spalono y zazdrością że mu Bóg daje kawałek chleba. Sąd Ninieyszy sprawy między stronami przesłuchawszy y z inkwizycyi wyrozumiawszy nakazuje aby pozwany dnia jutrzeyszego przysiągł jako nie słyszał od nikogo tylko sam z płochości y z żalu ani żadnej szkody ani mówienia czynić nie będzie ani nikogo namawiać [?] po wykonaniu tego Juramentu ma być wolny od Aktora.\n\nActum Crasnicy Coram Officio Composito in Vigilia Sancti Mathiae 1731 [23 II 1731 r.].\nW sprawie y Akcyi między Uczciwym Janem Szostakiewiczem [Szostakiewicz?] Aktorem a Pozwanym Uczciwym Janem Ćwiekiem [Ćwiek] ratione brony którey Aktorowi do włóczenia pożyczył pozwanemu a tej brony pożyczył Andrzejowi Bogucie [Boguta] która brona zginęła u pozwanego. W tej sprawie daje się dylacyi Obiema Stronom do środy blisko przyszłey żeby Aktor stawił na świadectwo Uczciwego [?] co obie strony aby bez pozwów stawały pod temi terminami.",
        "link_swa": UNIT_LINK
    }
]

all_data = part9_data + part10_scans
for rec in all_data:
    rec["link_swa"] = UNIT_LINK

assert len(all_data) == 250, f"Oczekiwano 250 rekordów, jest {len(all_data)}"
assert [r["nr_skanu"] for r in all_data] == list(range(1, 251)), "Brak ciągłości nr_skanu 1..250!"

# Weryfikacja braku wewnętrznych wielokropków
for r in all_data[225:250]:
    tr = r["transkrypcja"]
    mid = [i for i in range(len(tr)) if tr[i:i+3] == "..." and i > 10 and i < len(tr)-10]
    assert not mid, f"Wykryto mid_ellipsis na skanie {r['nr_skanu']}: {mid}"

with open('/home/ubuntu/workspace/Gen/main_data_j17_part10.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano pomyślnie main_data_j17_part10.json: {len(all_data)} rekordów (skany 1-250, 0 mid_ellipsis).")
