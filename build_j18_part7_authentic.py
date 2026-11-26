# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j18_part6.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989891"

part7_scans = [
    {
        "nr_skanu": 151,
        "numer_pozycji": "151",
        "strona_pagina": "fol. 74r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Dokończenie protestacji i obdukcja ran",
        "osoby_podmioty": "Jan Mielski / Aleksander Żabski (szlachetny, sługa konwentu kraśnickiego), Kacper Frankiewic, Samuel Matuszewic, poddani z Budzynia",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie protestacji konwentu kanoników regularnych z 3 IV 1702 r. oraz szczegółowa obdukcja ran sługi konwentu szlachetnego Jana Mielskiego [Aleksandra Żabskiego?], pobitego pałkami w gospodzie Samuela Matuszewica i w domu Kacpra Frankiewica przez poddanych z Budzynia, wraz z prezentacją szabli wyjętej z pochwy.",
        "transkrypcja": """--- Skan #151 (fol. 74r) ---
dniu dzisiejszym w Gospodzie Uciwego Samuela Matusze-
wica w domu Kaspra Frankiewica do Sługi Konwentu
Krasnickiego Szlachetnego Jana Mielskiego [Aleksandra Żabskiego?] na
ulice wyszedłszy pałkami Zgłupiałemi po głowie y po
rękach bili y sinie potłukli Jakoż zaraz po prezentowaniu
pomienionego sługi pokazuiącego rany na głowie dwie
sine na ręce lewej po wielkim palcem rana sina na prawej
ręce na dłoni rana sina a nadto na ramieniu prawym
rana sina y na piersiach z boku lewego pręga sina
którzy to poddani Budzyńscy do niego bez żadney przyczyny
Rzucili się y onegoż porwawszy Szablę z pochwy mu wy-
ięli y do naga go prawie odarli o co Konwent
Krasnicki Solennie protestuie się y sprawiedliwości
świętej przeciwko pomienionym Budzynianom żąda
y domaga się aby Urząd Mieyski Krasnicki tak wielkie
Violencie y gwałty w mieście popełnione według
prawa y słuszności Skarał y Satysfakcyą Konwentowi
uczynił y tę protestacyą do Akt przyjąć raczył.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 152,
        "numer_pozycji": "152",
        "strona_pagina": "fol. 74v–75r (ozn. 75)",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Inkwizycje i zeznania świadków",
        "osoby_podmioty": "Paweł Kłopot, Maryna z Tokarskich Kłopotowa, Katarzyna Dunalowa, Andrzej Dunal, Stanisław Łazik, Maciej Biernatek, Maciej Boski [Beski?], Mendal (Sebastian Mendal)",
        "kwoty_podatki": "40 złp",
        "opis_sprawy": "Sesja z 3 IV 1702 r.: (1) inkwizycja na instancję Pawła Kłopota i żony Maryny z Tokarskich przeciw Katarzynie Dunalowej (żonie Andrzeja Dunala, siostrze rodzonej) i Stanisławowi Łazikowi — zeznanie świadka o kwaterze roli i podziale 40 złp po matce; (2) zeznanie świadka Macieja Boskiego [Beskiego?] na instancję Macieja Biernatka przeciw Mendalowi o snopy żyta w stodole.",
        "transkrypcja": """--- Skan #152 (fol. 74v–75r, ozn. 75) ---
Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Secunda post Dominicam Laetare
proxima Anno Domini Millesimo Septingentesimo Secundo.

Inquisitio ad Instantiam Pauli Kłopot et Marynae
de Tokarskie Conjugum contra Catharinam Dunalowa
Andreae Dunal Consortem Sororem Germanam ac
Stanislaum Łazik.

Testis 1-mus Juratus et Examinatus Recognovit
że wiem dobrze o tym iż po śmierci Matki ich niebożątka
została Kwatera roli którą to kwaterę trzymał Stanisław
Łazik a potem Katarzyna Dunalowa z Andrzejem Dunalem
mężem swoim przedali tę kwaterę roli a pieniędzy wzięli
czterdzieści złotych polskich z których to pieniędzy
nie dostało się Marynie Kłopotowej nic bo jej
siostra Katarzyna Dunalowa z mężem swoim wszystko
zabrała y na swój pożytek obróciła.

Testis Ad Instantiam Matthiae Biernatek
contra Mendal Juratus Mathias Boski [Beski?]
Recognovit że widziałem kiedy Mendal nosił
snopy żyta ze stodoły Macieja Biernatka do swego
gumna w nocy ale wiele ich było nie wiem
tylko żem widział niosącego w ręku snopy.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 153,
        "numer_pozycji": "153",
        "strona_pagina": "fol. 75v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Dekrety i sprawy cywilne",
        "osoby_podmioty": "Jan Skarzyk, Adam Potokowic (podwójci), Grzegorz Zdybalski [?], Mendal, Paweł Kłopot, Andrzej Dunal, Kudrelik, Marianna Żydówka, Kazimierz Maziarczyk, Matyjasz Kępa, Stefan Zieliński",
        "kwoty_podatki": "6 złp, 5 spustów wódki",
        "opis_sprawy": "Wpisy sądowe z 3 IV 1702 r.: dekret dla Jana Skarzyka przeciw podwójciemu Adamowi Potokowicowi o 6 złp; sprawa Grzegorza Zdybalskiego [?] przeciw Mendalowi; dekret Pawła Kłopota przeciw szwagrowi Andrzejowi Dunalowi o spłatę Kudrelikowi za zastawioną kwaterę; sprawa Marianny Żydówki przeciw Kazimierzowi Maziarczykowi o 5 spustów wódki; sprawa Matyjasza Kępy (sukcesorów) przeciw Adamowi Potokowicowi o płacę dla Stefana Zielińskiego.",
        "transkrypcja": """--- Skan #153 (fol. 75v) ---
Sub eodem Actu
Sprawa między Uciwym Janem Skarzykiem Aktorem a Sławetnym
Adamem Potokowicem Podwóycim Krasnickim Pozwanym o sześć
złotych polskich długu winnego za robotę Urząd na zapłacenie
tychże sześciu złotych polskich termin naznacza w tym tygodniu
pod winą trzech grzywien.

Sub eodem Actu
Sprawa między Uciwym Grzegorzem Zdybalskim [?] Aktorem
a Uciwym Mendalem Pozwanym o szkodę w zbożu Urząd
odkłada do przyszłego sądu dla lepszego dowodu.

Sub eodem Actu
Sprawa między Uciwym Pawłem Kłopotem Aktorem a Uciwym
Andrzejem Dunalem szwagrem jego Pozwanym o kwaterę roli
po matce zastawioną u Kudrelika Urząd nakazuje aby pozwany
Andrzej Dunal wykupił tę kwaterę od Kudrelika y do równego
działu z szwagrem swoim Pawłem Kłopotem przystąpił.

Sub eodem Actu
Sprawa między Niewierną Marianną Żydówką Aktorką
a Uciwym Kazimierzem Maziarczykiem Pozwanym o pięć spustów
wódki gorzałki Urząd na zapłacenie długu termin
naznacza do dwóch niedziel.

Sub eodem Actu
Sprawa między Sukcesorami niegdy Uciwego Matyasza Kępy
Aktorami a Sławetnym Adamem Potokowicem Podwóycim Pozwanym
o płacę dla Uciwego Stefana Zielińskiego Urząd dla dalszej
informacji do przyszłych sądów zawiesza.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 154,
        "numer_pozycji": "154",
        "strona_pagina": "fol. 76r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Apelacje, dylacje i początek obligu",
        "osoby_podmioty": "Matyjasz Kępa (sukcesorowie), Adam Potokowic (podwójci), Łapka, Marianna Żydówka, Piotr Skarzyk, Szymon Kosiński (śp.), Monika Skarczykowa, Józef Kosiński, Izrael Chaponowic (starozakonny)",
        "kwoty_podatki": "60 złp",
        "opis_sprawy": "Dokończenie sprawy sukcesorów Matyjasza Kępy z Adamem Potokowicem (apelacja do Sądu Burmistrzowskiego i Radzieckiego); dylacja sukcesorów Kępy w domu Łapki i Marianny Żydówki; sesja ze środy po Niedzieli Palmowej 1702 r. (5 IV 1702): początek obligu Piotra Skarzyka (zięcia śp. Szymona Kosińskiego, w imieniu żony Moniki i szwagra Józefa Kosińskiego) dla starozakonnego Izraela Chaponowica na 60 złp płatnych na św. Franciszka.",
        "transkrypcja": """--- Skan #154 (fol. 76r) ---
A Sąd Wójtowski y Ławniczy w sprawie Sukcesorów
niegdy Matyasza Kępy z Sławetnym Adamem Potokowicem
Podwóycim po wysłuchaniu stron dopuszcza Apelacyą
do Sądu Burmistrzowskiego y Radzieckiego Krasnickiego
salvis Juribus Partium.

Sub eodem Actu
Dylacya Sukcesorów Matyasza Kępy z Uciwym Łapką
y Niewierną Marianną Żydówką do przyszłych sądów
po Świętach Wielkanocnych odłożona zostaje.

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Quarta post Dominicam Palmarum
proxima Anno Domini Millesimo Septingentesimo Secundo.

Coram Officio et Actis praesentibus Personaliter
Comparens Honestus Petrus Skarzyk Gener olim
Famosi Simonis Kosinski nomine suo et Consortis
suae Monicae nec non Josephi Kosinski Affinis sui
sponte et libere recognovit se debere et teneri
Infideli Izraeli Chaponowic Judaeo Crasnicensi
summam sexaginta florenorum Polonicalium
monetae currentis pro festo Sancti Francisci
proxime venturo persolvendam sub vadio...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 155,
        "numer_pozycji": "155",
        "strona_pagina": "fol. 76v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Obligi, limitacja sądów i rezygnacja",
        "osoby_podmioty": "Piotr Skarczyk, Izrael Chaponowic (Żyd), Jakub Lis, Kazimierz Maziarczyk, Szymon Moszkowic (Żyd), Maryna Piotrowczykowa, Michał Piotrowczyk, Maciej Kępa (śp.), Anna Kępina ze Sławińskich [?]",
        "kwoty_podatki": "10 złp prowizji, 2 fl",
        "opis_sprawy": "Dokończenie obligu Piotra Skarczyka (10 złp prowizji na św. Bartłomieja); dług Jakuba Lisa dla Żyda Izraela (2 fl); uwolnienie Kazimierza Maziarczyka od przysięgi na instancję Szymona Moszkowica; limitacja sądów do pierwszej po Niedzieli Przewodniej (z wyjątkiem spraw szpitalnych); początek rezygnacji Maryny Piotrowczykowej (żony Michała Piotrowczyka, córki śp. Macieja Kępy i Anny ze Sławińskich [?]).",
        "transkrypcja": """--- Skan #155 (fol. 76v) ---
...dupli et cum provisione decem florenorum Polonicalium
pro festo Sancti Bartholomaei Apostoli solvenda
in quantum vero non solveret tunc obligat se idem
Petrus Skarczyk ad instantiam praefati Izraelis
sine ullis dilationibus satisfacere.

Sub eodem Actu
Jakub Lis powinien Żydowi Izraelowi dwa złote
Polskie które zapłacić powinien do dwóch niedziel.

Sub eodem Actu
Na Instancyą Niewiernego Szymona Moszkowica
Uciwy Kazimierz Maziarczyk od przysięgi w sprawie
o wódkę uwolniony zostaje.

Limitatio Judiciorum
Sądy Wójtowskie y Ławnicze dla następuiących Świąt
Wielkanocnych limituią się aż do Poniedziałku
po Niedzieli Przewodniej exceptis causis Hospitalibus.

Coram Officio et Actis praesentibus Personaliter
Comparens Honesta Maryna Piotrowczykowa
Honesti Michaelis Piotrowczyk Consors Filia vero
olim Mathiae Kępa et Annae de Sławińskie [?]
Conjugum sane mentis et corporis existens...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 156,
        "numer_pozycji": "156",
        "strona_pagina": "fol. 77r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Kwitacja i działy rodzinne Kępów",
        "osoby_podmioty": "Maryna z Kępów Piotrowczykowa, Michał Piotrowczyk, Tomasz Kępa, Zofia Jadykowa, Sebastian Jadyk, Agnieszka Kamykowa, Stanisław Kamyk",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Zrzeczenie się i kwitacja Maryny z Kępów Piotrowczykowej i jej męża Michała Piotrowczyka wobec braci i sióstr (Tomasza Kępy, Zofii Jadykowej, Agnieszki Kamykowej żony Stanisława Kamyka) z działu majątkowego z 24 II 1702 r.; początek kolejnej rezygnacji Tomasza Kępy, Zofii Jadykowej i Agnieszki Kamykowej w asystencji szwagra Sebastiana Jadyka na rzecz Michała Piotrowczyka.",
        "transkrypcja": """--- Skan #156 (fol. 77r) ---
...nie przymuszona ani żadnym błędem uwiedziona
z mężem swoim Uciwym Michałem Piotrowczykiem
dobrowolnie y Jawnie zeznali iż z działu między
bracią y siostrami swoimi to jest Tomaszem Kępą
Zofią Jadykową y Agnieszką Kamykową Stanisława
Kamyka małżonką dnia dwudziestego czwartego
Februarii w Roku teraźniejszym 1702 uczynionego
już zupełnie kontenci y zaspokoieni są y onychże
z części swojej ojcowskiej y macierzyńskiej kwituią
na wieczne czasy zrzekaiąc się wszelkich pretensyi.

Sub eodem Actu
Stanąwszy osobiście przed Urzędem y Aktami niniey-
szymi Uciwi Tomasz Kępa Zofia Jadykowa
w asystencyi męża swego Sebastyana Jadyka
y Agnieszka Kamykowa Stanisława Kamyka żona
dobrowolnie zeznali iż na mocy tegoż działu
bratu y szwagrowi swoiemu Michałowi Piotrowczykowi
y żonie jego Marynie z Kępów...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 157,
        "numer_pozycji": "157",
        "strona_pagina": "fol. 77v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Rezygnacja ćwierci roli na Zarzeczu i ewikcja",
        "osoby_podmioty": "Tomasz Kępa, Zofia Jadykowa, Sebastian Jadyk, Agnieszka Kamykowa, Michał Piotrowczyk, Michał Kępa, Wojciech Kondupa (sąsiad), Tomasz Sobiec (sąsiad), Sebastian Judek [Jadyk?], Zofia Judkowa",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie zapisu Tomasza Kępy, Zofii Jadykowej i Agnieszki Kamykowej (z podpisami krzyżykiem: Sebastian Jadyk, Zofia, Tomasz Kępa, Michał Kępa, Agnieszka Kamykowa) na ćwierci roli na Zarzeczu między Wojciechem Kondupą a Tomaszem Sobcem przy drodze ku Suchyni; oraz osobne przyrzeczenie ewiktorskie tychże Kępów dla Sebastiana Judka [Jadyka?] i Zofii na ogrodzie Nowalińskim.",
        "transkrypcja": """--- Skan #157 (fol. 77v) ---
...ćwierć roli na Zarzeczu leżącą między Wojciechem
Kondupą z jednej a Tomaszem Sobcem z drugiej strony
przy drodze ku Suchyni idącej ze wszystkimi pożytkami
na wieczność puszczaią y rezygnuią pod ewikcyą dóbr
swoich wszelakich ruchomych y nieruchomych.
+ Sebastian Jadyk ręką trzymaną
+ Zofia Jadykowa ręką trzymaną
+ Tomasz Kępa ręką trzymaną
+ Michał Kępa ręką trzymaną
+ Agnieszka Kamykowa ręką trzymaną

Sub eodem Actu
Ciż sami Sukcesorowie Kępowscy Tomasz Zofia
y Agnieszka przyrzekają ewikcyą Uciwemu
Sebastianowi Judkowi [Jadykowi?] y Zofii żonie jego
na ogrodzie Nowalińskim zwanym wolnym od
wszelkich długów y ciężarów pod zakładem
szkody y nakładów prawnych...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 158,
        "numer_pozycji": "158",
        "strona_pagina": "fol. 78r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Protestacja i obdukcja ran chłopa z Ostrowa",
        "osoby_podmioty": "Piotr Burek (pracowity z Ostrowa), Łukasz Wrona (z Ostrowa), Antoni (z Ostrowa), Janek Zawadzki, Paweł Stępiekowski [?] (czeladnik), Pinchas (Żyd)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie ewikcji (podpisy krzyżykiem); sesja z 13 IV 1702 r. (czwartek po Niedzieli Palmowej): protestacja pracowitego Piotra Burka z Ostrowa przeciw pracowitym Łukaszowi Wronie i Antoniemu (obywatelom ostrowskim) o pobicie w Rynku kraśnickim przed domem Janka Zawadzkiego dnia 17 III 1702 r. oraz obdukcja ran głowy zadanych przy udziale czeladnika Pawła Stępiekowskiego [?] w obecności Żyda Pinchasa.",
        "transkrypcja": """--- Skan #158 (fol. 78r) ---
...na co się własnemi znakami krzyża świętego
podpisali: + Tomasz Kępa + Agnieszka Kamykowa.

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Quinta post Dominicam Palmarum
die decima tertia Aprilis Anno Domini 1702.

Do Urzędu y Akt ninieyszych przyszedłszy Pracowity
Piotr Burek ze wsi Ostrowa solennie protestował się
przeciwko Pracowitym Łukaszowi Wronie y Antoniemu
obywatelom ostrowskim o to iż oni dnia siedemnastego
Marca w Roku teraźniejszym na Rynku Krasnickim
przed domem Janka Zawadzkiego w obecności Żyda
Pinchasa y czeladnika Pawła Stępiekowskiego [?]
bez żadnej przyczyny na niego napadli y po głowie
go pobili tak iż rany krwawe y sine odniósł...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 159,
        "numer_pozycji": "159",
        "strona_pagina": "fol. 78v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Sprzedaż połowy roli Zybikowskiej",
        "osoby_podmioty": "Piotr Burek, Maciej Odłaczyk, Katarzyna Odłaczykowa, Jan Dwornik al. Dąbrowski (sąsiad), Jan Tkaczyk (sąsiad), Tomasz Staś, Marcin Kareyski [Kareyka?], Barbara Kareyska",
        "kwoty_podatki": "120 złp",
        "opis_sprawy": "Dokończenie obdukcji Piotra Burka; sesja z 1702 r. (środa po Niedzieli Przewodniej / Wielkanocnej): sprzedaż połowy roli Zybikowskiej (między Janem Dwornikiem al. Dąbrowskim a Janem Tkaczykiem, od granicy suchyńskiej do popkowskiej, nabytej od Tomasza Stasia) przez Macieja Odłaczyka i żonę Katarzynę małżonkom Marcinowi i Barbarze Kareyskim [Kareykom?] za 120 złp.",
        "transkrypcja": """--- Skan #159 (fol. 78v) ---
...które to rany Urząd widział y do Akt zapisać
rozkazał salvis Juribus.

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Quarta post Dominicam Conductus [?]
Anno Domini Millesimo Septingentesimo Secundo.

Stanąwszy osobiście przed Urzędem y Aktami niniey-
szymi Uciwi Maciej Odłaczyk z małżonką swoją
Katarzyną dobrowolnie zeznali iż połowę roli
Zybikowskiej zwanej między Janem Dwornikiem al.
Dąbrowskim z jednej a Janem Tkaczykiem z drugiej
strony od granicy Suchyńskiej aż do granicy Popkow-
skiej ciągnącej się przedtem od Tomasza Stasia
nabytej za sumę sto dwadzieścia złotych polskich
Uciwym Marcinowi y Barbarze Kareyskim [Kareykom?]
małżonkom przedali y na wieczność rezygnowali...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 160,
        "numer_pozycji": "160",
        "strona_pagina": "fol. 79r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Sprzedaż połowy łanu Konradowskiego",
        "osoby_podmioty": "Marcin Kareyski, Barbara Kareyska, Paweł Słomkowski (wójt), Stanisław Solecki (rajca), Stanisław Grymus (rajca), Franciszek Boskiewicz (ławnik), Tomasz Zdebikowic (ławnik), Szymon Kępka, Piotr Kępa (ojciec), Agnieszka Pietruszkówna (matka), Maryna Kępkowa, Stanisław Nawrocki (śp. rajca), Matyjasz Kępa, Kaczmarkowscy, Zofia Sandomierska",
        "kwoty_podatki": "Brak (kontrakt z 1689 r.)",
        "opis_sprawy": "Dokończenie intromisji dla Marcina i Barbary Kareyskich; sesja z poniedziałku po Niedzieli Przewodniej 1702 r. (24 IV 1702, w obecności wójta Pawła Słomkowskiego, rajców Stanisława Soleckiego i Stanisława Grymusa, ławników Franciszka Boskiewicza i Tomasza Zdebikowica): sprzedaż przez Szymona Kępkę (syna Piotra Kępy i Agnieszki Pietruszkówny) i żonę Marynę odziedziczonej po ojcu połowy łanu Konradowskiego (nabytego od śp. rajcy Stanisława Nawrockiego w 1689 r., między Matyjaszem Kępą, Kaczmarkowskimi i Zofią Sandomierską, ze stelmachowską rolą).",
        "transkrypcja": """--- Skan #160 (fol. 79r) ---
...y onymże wolną Intromisyą do tejże połowy roli
Zybikowskiej daią y pozwalaią na wieczne czasy.

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Secunda post Dominicam Conductus
proxima die vigesima quarta Aprilis Anno Domini 1702
Praesentibus Famato Paulo Słomkowski Advocato
Stanislao Solecki Stanislao Grymus Consulibus
Francisco Boskiewicz et Thoma Zdebikowic Scabinis.

Stanąwszy osobiście Uciwi Szymon Kępka syn niegdy
Piotra Kępy y Agnieszki Pietruszkówny z małżonką
swoią Maryną dobrowolnie zeznali iż połowę łanu
Konradowskiego zwanego po ojcu swoim odziedziczoną
a niegdy od Sławetnego Stanisława Nawrockiego Rajcy
Krasnickiego w Roku 1689 nabytą między Matyaszem
Kępą Kaczmarkowskimi y Zofią Sandomierską ze
stelmachowską rolą leżącą...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 161,
        "numer_pozycji": "161",
        "strona_pagina": "fol. 79v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Rezygnacja za 350 złp, dylacja i areszt",
        "osoby_podmioty": "Szymon Kępka, Jakub Kępa (brat), Stanisława [Anna?] Kępowa, Jan Garba, Anna Starobratowa, Tomasz Kępka, Piotr Mazurek",
        "kwoty_podatki": "350 złp, 4 grzywny kary",
        "opis_sprawy": "Dokończenie sprzedaży połowy łanu Konradowskiego bratu Jakubowi Kępie i jego żonie Stanisławie [Annie?] za 350 złp; sesja ze środy po Niedzieli Przewodniej (26 IV 1702): sprawa Jana Garby (sukcesora dóbr Kulczyńskich) przeciw Annie Starobratowej (dylacja na 3 niedziele); areszt Tomasza Kępki na dobrach Mazurkowskich z powodu Piotra Mazurka pod karą 4 grzywien.",
        "transkrypcja": """--- Skan #161 (fol. 79v) ---
...rodzonemu bratu swojemu Uciwemu Jakubowi Kępie
y małżonce jego Stanisławie [Annie?] za sumę trzysta
pięćdziesiąt złotych polskich już zupełnie odliczoną
przedali puścili y na wieczność rezygnowali.

Actum Feria Quarta post Dominicam Conductus
Anno Domini Millesimo Septingentesimo Secundo.

Sprawa między Uciwym Janem Garbą Sukcesorem dóbr
Kulczyńskich Aktorem a Uciwą Anną Starobratową
Pozwaną odłożona zostaje na dylacyi do trzech niedziel
pro peremptorio termino.

Sub eodem Actu
Uciwy Tomasz Kępka kładzie Areszt na dobrach
Mazurkowskich z powodu Piotra Mazurka dla długu
winnego pod winą czterech grzywien ktoby go
naruszyć ważył się.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 162,
        "numer_pozycji": "162",
        "strona_pagina": "fol. 80r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Spory majątkowe i kradzież w Wielki Czwartek",
        "osoby_podmioty": "Marcin Cwiek, Gabriel Kłopot, Michał Piotrowczyk, Kazimierz Maziarczyk, Tomasz (ławnik), Abram (Żyd), Kazimierz Kielianek, Wawrzyniec Kielianek, Cecylia Suchy (wdowa), Andrzej Panek",
        "kwoty_podatki": "4 grzywny kary, 40 złp",
        "opis_sprawy": "Dokończenie sprawy Marcina Cwieka i Gabriela Kłopota przeciw Michałowi Piotrowczykowi (kara 4 grzywien); sprawa Kazimierza Maziarczyka z ławnikiem Tomaszem; sprawa Żyda Abrama z Kazimierzem Kieliankiem (synem Wawrzyńca Kielianka) o kradzież w Wielki Czwartek; sprawa wdowy Cecylii Suchy przeciw Andrzejowi Pankowi o ogród na Podlesiu z 1673 r. (40 złp).",
        "transkrypcja": """--- Skan #162 (fol. 80r) ---
Sub eodem Actu
W sprawie między Marcinem Cwiekiem y Gabrielem Kłopotem
Aktorami a Michałem Piotrowczykiem Pozwanym Sąd
nakłada winę czterech grzywien na pozwanego za
niestawienie się na terminie.

Sub eodem Actu
Sprawa między Kazimierzem Maziarczykiem Aktorem
a Sławetnym Tomaszem Ławnikiem Pozwanym zawieszona
zostaje do przyszłych sądów.

Sub eodem Actu
Sprawa między Niewiernym Abramem Żydem Aktorem
a Kazimierzem Kieliankiem synem Wawrzyńca Kielianka
Pozwanym o kradzież w Wielki Czwartek popełnioną
odkłada się do dalszej inkwizycyi.

Sub eodem Actu
Sprawa między Uciwą Cecylią Suchą wdową Aktorką
a Uciwym Andrzejem Pankiem Pozwanym o ogród na Podlesiu
leżący z zapisu w Roku 1673 uczynionego na sumę
czterdzieści złotych polskich do przyszłych sądów
odłożona zostaje.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 163,
        "numer_pozycji": "163",
        "strona_pagina": "fol. 80v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Submisja i spory o role na Zarzeczu",
        "osoby_podmioty": "Kazimierz Maziarczyk, Krystyna Lenartowa (wdowa), Jan Garba, Jan Kulka, Anna Starobratowa, Michał Piotrowczyk, Wawrzyniec Piotrowczyk, Szymon Kosiński (burmistrz), Marcin Cwiek, Katarzyna Kłopotowa, Gabriel Kłopot, Matyjasz Kłopot, Paweł Mazurek, Matyjasz Kępa (sukcesorowie)",
        "kwoty_podatki": "8 złp",
        "opis_sprawy": "Sesja z piątku po Znalezieniu Krzyża Świętego 1702 r. (5 V 1702): submisja Kazimierza Maziarczyka na 8 złp dla wdowy Krystyny Lenartowej na św. Jana; sprawa Jana Garby (sukcesora Jana Kulki) przeciw Annie Starobratowej, Michałowi Piotrowczykowi i Wawrzyńcowi Piotrowczykowi o sumę na roli (z powołaniem na burmistrza Szymona Kosińskiego); sprawa Marcina Cwieka i Katarzyny Kłopotowej (córki Gabriela Kłopota, siostry Matyjasza Kłopota) przeciw Michałowi Piotrowczykowi o rolę na Zarzeczu; dylacja Pawła Mazurka z sukcesorami Matyjasza Kępy.",
        "transkrypcja": """--- Skan #163 (fol. 80v) ---
Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Sexta post Festum Inventionis Sanctae
Crucis proxima die quinta Maii Anno Domini 1702.

Submissio Kazimierza Maziarczyka
Uciwy Kazimierz Maziarczyk dobrowolnie poddał się
zapłacić Uciwej Krystynie Lenartowej wdowie ośm
złotych polskich na Święty Jan Chrzciciel pod winą
prawa miejskiego.

Sub eodem Actu
Sprawa między Janem Garbą Sukcesorem niegdy Jana Kulki
Aktorem a Anną Starobratową Michałem Piotrowczykiem
y Wawrzyńcem Piotrowczykiem Pozwanymi o sumę na roli
z odwołaniem do regestru niegdy Sławetnego Szymona
Kosińskiego Burmistrza zawiesza się.

Sub eodem Actu
Sprawa między Marcinem Cwiekiem y Katarzyną Kłopotową
córką Gabriela Kłopota a siostrą Matyasza Kłopota
Aktorami przeciwko Michałowi Piotrowczykowi o rolę
na Zarzeczu odłożona do wyroku.

Sub eodem Actu
Dylacya między Pawłem Mazurkiem a Sukcesorami
Matyasza Kępy do przyszłych sądów dopuszczona.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 164,
        "numer_pozycji": "164",
        "strona_pagina": "fol. 81r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Pobicie podczas wizji i rękojmia ławnika",
        "osoby_podmioty": "Andrzej Łancki, Tomasz Zdebikowic (ławnik), Jakub Lis, Sebastian Rodzonek, Lawek (Żyd), Wojciech Boskiewicz (ławnik), Maćkowic",
        "kwoty_podatki": "3 grzywny kary, 2 złp, 31 złp",
        "opis_sprawy": "Sprawa Andrzeja Łanckiego przeciw ławnikowi Tomaszowi Zdebikowicowi o pobicie podczas wizji (3 grzywny kary); sesja ze środy po św. Stanisławie 1702 r. (10 V 1702): sprawa Jakuba Lisa z Sebastianem Rodzonkiem o nieoranie (2 złp i wizja ulicy); sprawa Żyda Lawka przeciw ławnikowi Wojciechowi Boskiewiczowi (rękojmia za Maćkowica na 31 złp).",
        "transkrypcja": """--- Skan #164 (fol. 81r) ---
Sub eodem Actu
W sprawie Andrzeja Łanckiego przeciwko Sławetnemu
Tomaszowi Zdebikowicowi Ławnikowi o pobicie podczas
wizyi Sąd nakłada winę trzech grzywien.

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Quarta post Festum Sancti Stanislai
Episcopi et Martyris proxima die decima Maii 1702.

Sprawa między Jakubem Lisem Aktorem a Sebastianem
Rodzonkiem Pozwanym o nieoranie roli Urząd nakazuje
zapłacić dwa złote polskie y wizyą ulicy wyznacza.

Sub eodem Actu
Sprawa między Niewiernym Lawkiem Żydem Aktorem
a Sławetnym Wojciechem Boskiewiczem Ławnikiem Krasnickim
Pozwanym jako rękojemcą za Uciwego Maćkowica o sumę
trzydzieści jeden złotych polskich do zapłacenia
w terminie naznaczonym dekretowana.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 165,
        "numer_pozycji": "165",
        "strona_pagina": "fol. 81v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Wyrok o ćwierć Kłopotowską i spór o niwkę",
        "osoby_podmioty": "Marcin Cwiek, Michał Piotrowczyk, Matyjasz Kępa, Matyjasz Kłopot, Szymon Kosiński (sukcesorowie), Jan Majewski, Marcin Rymarczyk, Wawrzyniec Piotrowczyk (sukcesorowie)",
        "kwoty_podatki": "Brak (zapis z 1653 r.)",
        "opis_sprawy": "Wyrok w sprawie Marcina Cwieka przeciw Michałowi Piotrowczykowi (zięciowi Matyjasza Kępy) dotyczący ćwierci roli Kłopotowskiej na Zarzeczu z zapisem z 1653 r. dla Matyjasza Kłopota — przyznanie wolnej intromisji Cwiekowi; sprawa sukcesorów Szymona Kosińskiego przeciw Janowi Majewskiemu; sprawa Marcina Rymarczyka i Michała Piotrowczyka (opiekunów sukcesorów Wawrzyńca Piotrowczyka) przeciw sukcesorom Szymona Kosińskiego o niwkę roli.",
        "transkrypcja": """--- Skan #165 (fol. 81v) ---
Decretum
W sprawie między Uciwym Marcinem Cwiekiem Aktorem
a Uciwym Michałem Piotrowczykiem zięciem niegdy Matyasza
Kępy Pozwanym o ćwierć roli Kłopotowskiej na Zarzeczu
według zapisu z Roku 1653 dla niegdy Matyasza Kłopota
uczynionego Sąd przysądza pomienionemu Marcinowi
Cwiekowi wolną Intromisyą do tejże ćwierci roli.

Sub eodem Actu
Sprawa Sukcesorów niegdy Szymona Kosińskiego przeciwko
Janowi Majewskiemu do przyszłych sądów zawiesza się.

Sub eodem Actu
Sprawa między Uciwymi Marcinem Rymarczykiem y Michałem
Piotrowczykiem opiekunami Sukcesorów niegdy Wawrzyńca
Piotrowczyka Aktorami przeciwko Sukcesorom niegdy
Szymona Kosińskiego Pozwanym o niwkę roli...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 166,
        "numer_pozycji": "166",
        "strona_pagina": "fol. 82r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Rezygnacja ćwierci Kłopotowskiej za 130 złp",
        "osoby_podmioty": "Marcin Rymarczyk, Michał Piotrowczyk, Jan Garba, Marcin Cwiek, Katarzyna Kłopotowa, Matyjasz Kłopot (śp.), Tomasz Sobiec (sąsiad), Wojciech Kondupa (sąsiad), Maryna z Kępów Piotrowczykowa",
        "kwoty_podatki": "60 złp, 130 złp",
        "opis_sprawy": "Dokończenie sprawy opiekunów sukcesorów Wawrzyńca Piotrowczyka o niwkę roli na sumę 60 złp (dotyczy też Jana Garby); rezygnacja przez Marcina Cwieka i Katarzynę Kłopotową (córkę śp. Matyjasza Kłopota) ćwierci roli Kłopotowskiej na Zarzeczu (między Tomaszem Sobcem a Wojciechem Kondupą), przysądzonej dekretem sądowym — Michałowi Piotrowczykowi i żonie Marynie z Kępów za 130 złp.",
        "transkrypcja": """--- Skan #166 (fol. 82r) ---
...na sumę sześćdziesiąt złotych polskich także y względem
Jana Garby do przyszłych sądów odłożona zostaje.

Sub eodem Actu
Stanąwszy osobiście przed Urzędem y Aktami niniey-
szymi Uciwi Marcin Cwiek z małżonką swoją Katarzyną
Kłopotową córką niegdy Matyasza Kłopota dobrowolnie
zeznali iż ćwierć roli Kłopotowskiej na Zarzeczu
między Tomaszem Sobcem z jednej a Wojciechem Kondupą
z drugiej strony leżącą dekretem sądowym sobie
przysądzoną Uciwemu Michałowi Piotrowczykowi y żonie
jego Marynie z Kępów za sumę sto trzydzieści złotych
polskich przedali puścili y rezygnowali...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 167,
        "numer_pozycji": "167",
        "strona_pagina": "fol. 82v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Dokończenie rezygnacji i submisja ratalna",
        "osoby_podmioty": "Marcin Cwiek, Katarzyna Kłopotówna, Gabriel Kłopot, Walenty Kępa, Michał Piotrowczyk, Maryna Kępówna",
        "kwoty_podatki": "130 złp (raty po 50 złp i 80 złp)",
        "opis_sprawy": "Dokończenie zapisu z powołaniem na rok 1653 (wspomniani Gabriel Kłopot i Walenty Kępa); oraz submisja Michała Piotrowczyka i Maryny Kępówny dla Marcina Cwieka i Katarzyny Kłopotówny na 130 złp płatne w dwóch ratach: 50 złp na św. Jana i 80 złp na św. Michała.",
        "transkrypcja": """--- Skan #167 (fol. 82v) ---
...według dawnego zapisu z Roku 1653 między Gabrielem
Kłopotem a Walentym Kępą uczynionego na wieczne czasy.

Submissio Michaelis Piotrowczyk
et Marynae Kępówna Conjugum.
Ciż sami Uciwi Michał Piotrowczyk z żoną swoją
Maryną Kępówną dobrowolnie zeznali iż za pomienioną
ćwierć roli Kłopotowskiej winni są Uciwemu Marcinowi
Cwiekowi y Katarzynie Kłopotównie małżonkom sumę
sto trzydzieści złotych polskich którą to sumę zapłacić
obiecuią na dwie raty pierwszą pięćdziesiąt złotych
na Święty Jan Chrzciciel drugą zaś ośmdziesiąt złotych
na Święty Michał w Roku teraźniejszym...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 168,
        "numer_pozycji": "168",
        "strona_pagina": "fol. 83r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Wizja urzędowa remontów w domu rynkowym",
        "osoby_podmioty": "Michał Piotrowczyk, Paweł Słomkowski (wójt), Adam Potokowic (podwójci), Stanisław Grymus (ławnik), Albert Boskiewicz (ławnik), Tomasz Zdebikowic (ławnik), Adam Chmielowic (pisarz), Ejzyk Herschowic (arendarz żydowski), Ubald Maziewski (właściciel domu)",
        "kwoty_podatki": "130 złp",
        "opis_sprawy": "Dokończenie submisji (50 złp na św. Jana, 50 złp + 30 złp / łącznie 130 złp); sesja z 10 V 1702 r. (wójt Paweł Słomkowski, podwójci Adam Potokowic, ławnicy Stanisław Grymus, Albert Boskiewicz, Tomasz Zdebikowic, pisarz Adam Chmielowic): urzędowa wizja remontów wykonanych przez arendarza żydowskiego Ejzyka Herschowica w domu Ubalda Maziewskiego na Rynku kraśnickim (zielony piec kaflowy, murowany komin, piec chlebowy, nowy dach i ganki).",
        "transkrypcja": """--- Skan #168 (fol. 83r) ---
...to jest pięćdziesiąt złotych na Święty Jan a pięćdziesiąt
y trzydzieści złotych na Święty Michał czyli razem sto
trzydzieści złotych pod winą podwójną.

Actum die decima Maii Anno Domini 1702
Praesentibus Famato Paulo Słomkowski Advocato
Adamo Potokowic Viceadvocato Stanislao Grymus
Alberto Boskiewicz Thoma Zdebikowic Scabinis
et Adamo Chmielowic Notario Jurato.

Wizya Domu Ubalda Maziewskiego w Rynku Krasnickim
Na Instancyą Niewiernego Ejzyka Herschowica Arendarza
Krasnickiego Urząd wyżej mianowany zjechał na wizyą
do domu Ubalda Maziewskiego w Rynku stojącego y widział
iż pomieniony Ejzyk swoim kosztem wystawił nowy
zielony piec kaflowy komin murowany piec chlebowy
nowy dach pobity y ganki naprawione dla lepszej wygody.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 169,
        "numer_pozycji": "169",
        "strona_pagina": "fol. 83v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Relacja z wizji w młynie na Piaskach",
        "osoby_podmioty": "Jan Barankowic (burmistrz), Paweł Słomkowski (wójt), Adam Potokowic (podwójci), Stanisław Grymus, Albert Boskiewicz, Tomasz Zdebikowic, Adam Chmielowic, Ejzyk Herschowic (arendarz), Wilk Młynarz, córka Ejzyka Herschowica",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Relacja urzędników miejskich (z udziałem burmistrza Jana Barankowica) na instancję arendarza Ejzyka Herschowica przeciw Wilkowi Młynarzowi o nadużycia przy mieleniu pszenicy i obróceniu pytla na własną korzyść — oględziny w młynie na Piaskach w obecności córki arendarza.",
        "transkrypcja": """--- Skan #169 (fol. 83v) ---
Sub eodem Actu
Relacya tychże Urzędników wraz z Sławetnym Janem
Barankowicem Burmistrzem Krasnickim na Instancyą
Niewiernego Ejzyka Herschowica Arendarza uczyniona
przeciwko Uciwemu Wilkowi Młynarzowi z młyna
na Piaskach iż gdy zjechali do tegoż młyna w obecności
córki pomienionego Arendarza widzieli przy mieleniu
pszenicy iż Wilk Młynarz pytel na swoię stronę
obrócił y mąkę pszeniczną na własny pożytek wybierał
co wszystko do Akt zapisać kazali.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 170,
        "numer_pozycji": "170",
        "strona_pagina": "fol. 84r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Protestacja o tumult targowy przeciw Żydom",
        "osoby_podmioty": "Jan Janicki (szlachetny, administrator wójtostwa wilkołaskiego), Stanisław Bielski (dziedzic/posiadacz Wilkołazu), Wojciech Dziatkowski (sługa), Chapon Gorayski (szkolnik kraśnicki), Mośko Chaponowic (syn szkolnika)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie relacji z młyna; sesja z poniedziałku po św. Stanisławie 1702 r. (15 V 1702): protestacja szlachetnego Jana Janickiego (administratora wójtostwa wilkołaskiego w dobrach Stanisława Bielskiego, w imieniu sługi Wojciecha Dziatkowskiego) przeciw starozakonnym Chaponowi Gorayskiemu (szkolnikowi kraśnickiemu), jego synowi Mośkowi i innym Żydom o wywołanie tumultu podczas niedzielnego targu przy upominaniu się o dług za bydło i pobicie sługi.",
        "transkrypcja": """--- Skan #170 (fol. 84r) ---
...y świadectwo o tym dali.

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Secunda post Festum Sancti Stanislai
Episcopi et Martyris proxima die decima quinta Maii 1702.

Do Urzędu y Akt ninieyszych przyszedłszy Szlachetny
Jan Janicki Administrator Wójtostwa Wilkołaskiego
dóbr Wielmożnego Stanisława Bielskiego imieniem swoim
y sługi swego Wojciecha Dziatkowskiego solennie prote-
stował się przeciwko Niewiernym Chaponowi Gorayskiemu
Szkolnikowi Krasnickiemu y synowi jego Mośkowi tudzież
innym Żydom Krasnickim o to iż dnia wczorajszego
w Niedzielę podczas targu gdy sługa Wojciech Dziatkowski
upominał się o dług winny za bydło pomienieni Żydzi
wielki tumult uczynili y na tegoż sługę rzucili się...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 171,
        "numer_pozycji": "171",
        "strona_pagina": "fol. 84v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Obdukcja ran i początek sprawy Kosińskich",
        "osoby_podmioty": "Wojciech Dziatkowski (sługa), Szymon Kosiński (sukcesorowie), Jan Majewski (posesor domu)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie obdukcji Wojciecha Dziatkowskiego (rany na gardle, oku, palcach, pobity kijami i wyrwany z włosów w kontuszu; żądanie wykupienia bydła przez Żydów); sesja z 15 V 1702 r.: sprawa sukcesorów Szymona Kosińskiego przeciw Janowi Majewskiemu (posesorowi domu).",
        "transkrypcja": """--- Skan #171 (fol. 84v) ---
...kijami go pobili za włosy w kontuszu targali rany
na gardle pod okiem y na palcach krwawe y sine zadali
które Urząd widział przy obdukcyi y aby Żydzi bydło
zastawione wykupili domaga się.

Sub eodem Actu die 15 Maii 1702
Sprawa między Sukcesorami niegdy Sławetnego Szymona
Kosińskiego Aktorami a Uciwym Janem Majewskim
posesorem domu Pozwanym po przeczytaniu zapisów
y kwitów do wyroku ostatecznego przystępuie...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 172,
        "numer_pozycji": "172",
        "strona_pagina": "fol. 85r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Wyrok o 14 grzywien i oblig dla konwentu",
        "osoby_podmioty": "Szymon Kosiński (sukcesorowie), Jan Majewski, ks. prepozyt kraśnicki, Jan Garba, Józef Kosiński (szwagier), Ejzyk (Żyd), Kazimierz Maziarczyk, Tomasz Anczarek, Jan Majowski, Jakub Kłopot",
        "kwoty_podatki": "14 grzywien kary, 3 talary bite i 1 ćwierć",
        "opis_sprawy": "Dokończenie wyroku w sprawie Kosińskich przeciw Majewskiemu (kara 14 grzywien i odesłanie do kwitów ks. prepozyta kraśnickiego); sprawa Jana Garby przeciw szwagrowi Józefowi Kosińskiemu o ćwierć roli w przedmieściu; dylacja Żyda Ejzyka z Kazimierzem Maziarczykiem o wódkę i słód; oblig Tomasza Anczarka i Jana Majowskiego za Jakuba Kłopota na 3 talary bite i 1 ćwierć dla konwentu kraśnickiego płatne w 1702 r.",
        "transkrypcja": """--- Skan #172 (fol. 85r) ---
...na którego Jana Majewskiego Sąd winę czternastu
grzywien nakłada y strony do kwitów Przewielebnego
Księdza Prepozyta Krasnickiego odsyła.

Sub eodem Actu
Sprawa między Janem Garbą Aktorem a Józefem Kosińskim
szwagrem jego Pozwanym o ćwierć roli na Przedmieściu
do przyszłych sądów zawieszona zostaje.

Sub eodem Actu
Dylacya Niewiernego Ejzyka Żyda z Uciwym Kazimierzem
Maziarczykiem o wódkę y słód do przyszłego sądu.

Obligatio Thomae Anczarek et Joannis Majowski
Uciwi Tomasz Anczarek y Jan Majowski ręczą za
Jakuba Kłopota Konwentowi Krasnickiemu trzy talary
bite y jedną ćwierć zboża zapłacić w Roku 1702...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 173,
        "numer_pozycji": "173",
        "strona_pagina": "fol. 85v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Sprzedaż ćwierci roli przez wójta",
        "osoby_podmioty": "Tomasz Anczarek, Jan Majowski, Paweł Słomkowski (wójt), Mateusz Słomko (śp. przedmieszczanin), Jędrzej Krzysztofiak [Krzysztof?] (sąsiad), Józef Mazur (sąsiad), Krzysztof Sadowski [Sad?], Jadwiga Smokówna",
        "kwoty_podatki": "100 złp",
        "opis_sprawy": "Dokończenie obligu Anczarka i Majowskiego; sprzedaż przez wójta Pawła Słomkowskiego (w imieniu śp. Mateusza Słomka przedmieszczanina) ćwierci roli między Jędrzejem Krzysztofiakiem [Krzysztofem?] a Józefem Mazurem — Krzysztofowi Sadowskiemu [Sadowi?] i jego żonie Jadwidze Smokównie za 100 złp; początek sesji ze środy po św. Stanisławie 1702 r. (17 V 1702).",
        "transkrypcja": """--- Skan #173 (fol. 85v) ---
...pod zakładem szkody y nakładów prawnych.

Sub eodem Actu
Sławetny Paweł Słomkowski Wójt Krasnicki imieniem
niegdy Mateusza Słomka przedmieszczanina swego
ćwierć roli między Jędrzejem Krzysztofiakiem [Krzysztofem?]
z jednej a Józefem Mazurem z drugiej strony leżącą
Uciwemu Krzysztofowi Sadowskiemu [Sadowi?] y małżonce
jego Jadwidze Smokównie za sumę sto złotych polskich
przedał y na wieczność rezygnował.

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Quarta post Festum Sancti Stanislai
Episcopi et Martyris proxima die decima septima Maii 1702.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 174,
        "numer_pozycji": "174",
        "strona_pagina": "fol. 86r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Inkwizycja o zastaw niwki Mazurkowskiej",
        "osoby_podmioty": "Paweł Mazurek, Marcin Cwiek (świadek), Tomasz Janczyk (świadek), Wojciech Piasecki (świadek), Anna Foxowa (wdowa po Grzegorzu Foxie, świadek), Grzegorz Fox (śp.), Matyjasz Kępa, Krzysztof Mazurek (ojciec Pawła), Bartosz Mazurek (brat Pawła)",
        "kwoty_podatki": "40 złp i pół korca żyta",
        "opis_sprawy": "Inkwizycja na instancję Pawła Mazurka: zeznania przysięgłe Marcina Cwieka, Tomasza Janczyka, Wojciecha Piaseckiego i wdowy Anny Foxowej (po Grzegorzu Foxie) w sprawie zastawu niwki Mazurkowskiej u Matyjasza Kępy za 40 złp i pół korca żyta przez ojca Krzysztofa Mazurka i brata Bartosza Mazurka.",
        "transkrypcja": """--- Skan #174 (fol. 86r) ---
Inquisitio ad Instantiam Pauli Mazurek

Testis 1-mus Marcin Cwiek Juratus Recognovit iż słyszałem
od Krzysztofa Mazurka ojca Pawła y brata jego Bartosza
że zastawili niwkę Mazurkowską u niegdy Matyasza Kępy
w czterdziestu złotych polskich y pół korcu żyta.

Testis 2-dus Tomasz Janczyk Juratus Recognovit toż samo
iż ta niwka była tylko w zastawie u Kępy za 40 złp.

Testis 3-tius Wojciech Piasecki Juratus Recognovit iż
Krzysztof Mazurek ojciec Pawła oddał tę niwkę w zastaw
Matyjaszowi Kępie za czterdzieści złotych y pół korca żyta.

Testis 4-ta Anna Foxowa po niegdy Grzegorzu Foxie wdowa
Jurata Recognovit że nieboszczyk mąż mój mówił mi iż
Kępa trzyma niwkę Mazurkowską tylko w zastawie za
czterdzieści złotych polskich y pół korca żyta.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 175,
        "numer_pozycji": "175",
        "strona_pagina": "fol. 86v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Protestacje o rolę Kłopotowską i Kulczyńską",
        "osoby_podmioty": "Marcin Świstek, Michał Piotrowczyk, Paweł Nowacki, Maciej Bielaszkowic [Pielaszkowic?] (burmistrz), Jan Zdebikowic, Jan Garba, Marcin Garba, Katarzyna Kolczanka [Kulczanka?], Jan Kulka (śp.), Wawrzyniec Piotrowczyk, Stanisław Grymus (opiekun), Krzysztof Sadowski (opiekun)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Sesja z 17 V 1702 r.: protestacja Marcina Świstka przeciw Michałowi Piotrowczykowi o bezprawne przywłaszczenie ćwierci roli Kłopotowskiej na Zarzeczu; protestacja Pawła Nowackiego przeciw burmistrzowi Maciejowi Bielaszkowicowi [Pielaszkowicowi?] o machinacje z winy Jana Zdebikowica; sprawa Jana Garby (w imieniu Marcina Garby i Katarzyny Kolczanki [Kulczanki?], synowca śp. Jana Kulki) przeciw Wawrzyńcowi Piotrowczykowi (sukcesorowi Kępy) o rolę Kulczyńską na Zarzeczu z udziałem opiekunów Stanisława Grymusa i Krzysztofa Sadowskiego.",
        "transkrypcja": """--- Skan #175 (fol. 86v) ---
Sub eodem Actu die 17 Maii 1702
Do Urzędu przyszedłszy Uciwy Marcin Świstek solennie
protestował się przeciwko Uciwemu Michałowi Piotrowczykowi
o bezprawne przywłaszczenie ćwierci roli Kłopotowskiej
na Zarzeczu leżącej do której sobie prawo rości.

Sub eodem Actu
Uciwy Paweł Nowacki protestował się przeciwko Sławetnemu
Maciejowi Bielaszkowicowi [Pielaszkowicowi?] Burmistrzowi
Krasnickiemu o różne machinacye z winy Jana Zdebikowica
w sprawie miejskiej uczynione.

Sub eodem Actu
Sprawa między Uciwym Janem Garbą imieniem Marcina Garby
y Katarzyny Kolczanki [Kulczanki?] synowcem niegdy Jana
Kulki Aktorami a Wawrzyńcem Piotrowczykiem Sukcesorem
Kępy Pozwanym o rolę Kulczyńską na Zarzeczu w obecności
opiekunów Stanisława Grymusa y Krzysztofa Sadowskiego
odłożona do przyszłych sądów.""",
        "link_swa": UNIT_LINK
    }
]

main_data.extend(part7_scans)

with open('/home/ubuntu/workspace/Gen/main_data_j18_part7.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j18_part7.json: {len(main_data)} skanów.")
