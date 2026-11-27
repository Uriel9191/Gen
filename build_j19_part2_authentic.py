# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j19_part1.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989899"

part2_scans = [
    {
        "nr_skanu": 26,
        "numer_pozycji": "26",
        "strona_pagina": "fol. 11v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1657",
        "kategoria": "Sąd Radziecki / Kupno gruntu od Reginy Butowej przez Stanisława Nawrockiego",
        "osoby_podmioty": "Stanisław Nawrocki (rajca), Jadwiga Kupska [?] (żona), Wojciech Nawrocki (syn), Maciej Tharasa (burmistrz), Regina Butowa (wdowa po Gabrielu Bucie), Piotr Tłaczyński [?] (brat), Stanisław Sikor (opiekun)",
        "kwoty_podatki": "120 złp (30 złp gotówką)",
        "opis_sprawy": "Dokończenie kupna za Bramą Lubelską przez rajcę Stanisława Nawrockiego i żonę Jadwigę; poniżej sesja z czwartku w wigilię św. Mateusza Apostoła 1657 r. (20 IX): Mancipatio Famati D. Stanislai Nawrocki — kupno od wdowy Reginy Butowej (w asystencji brata Piotra Tłaczyńskiego [?] i opiekuna Stanisława Sikora) gruntu przy drodze do Ladańska i ogrodu szpitalnego za 120 złp.",
        "transkrypcja": """--- Skan #26 (fol. 11v) ---
11v 1657
...placu będącego Sławetnego Stanisława Nawrockiego y Małżonki jego Jadwigi
także i dziatek ich, to jest Wojciecha nigdy nie mając żadnej...
do Ladańska z drugiej strony Kraśnickiej płacących kupiec wypłaci...
przy tej asekuracyi na błoniu i korzyści...
w liby polskiej w każdy złoty rachując po gr. 30...
dobrego pieniądza, których przedawczyni odebrała i z nich kwituje...
na wieczność...
w formie publicznej oblaty...

Actum Coram Officio Consulari feria quinta in vigilia
Festi S. Matthaei Apostoli 1657.

Mancipatio Famati D. Stanislai Nawrocki.
W domu Sławetnego P. Mathyasza Tharasy Burmistrza natenczas Rezydującego
Krasnickiego przy bytności jego samego y Sławetnych Panów Kolegów przy boku jego siedzących
stał się pewny a nieodmienny kontrakt y wieczne zrzeczenie między
Uczciwą Reginą Buciną wdową pozostałą po niegdy Gabrielu Bucie mieszczaninie
kraśnickim w asystencyi brata swego Piotra Tłaczyńskiego [?]...
y opiekuna swego Sławetnego Stanisława Sikora Pisarza przysięgłego
z jednej a Sławetnym P. Stanisławem Nawrockim Rajcą i małżonką jego
Jadwigą kupcami z drugiej strony...
sprzedała grunt za zgodą opiekunów przy drodze ku Ladańsku i
ogrodzie szpitalnym leżący za summę pewną złotych polskich
sto dwadzieścia monety dobrej polskiej w każdy złoty rachując po gr. 30
gotowych.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 27,
        "numer_pozycji": "27",
        "strona_pagina": "fol. 12r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1657",
        "kategoria": "Sąd Radziecki / Kupno placu przy ul. Lubelskiej przez Wawrzyńca Zętkowica",
        "osoby_podmioty": "Stanisław Nawrocki (rajca), Maciej Tharasa (burmistrz), Regina Butowa (wdowa), Stanisław Sikor (pisarz i opiekun), Wawrzyniec Zętkowic [Żętkowic?], Katarzyna Zętkowicowa, Jan Grzymuszka (sąsiad)",
        "kwoty_podatki": "42 złp (22 złp + 20 złp)",
        "opis_sprawy": "Dokończenie rezygnacji na rzecz Stanisława Nawrockiego; poniżej Mancipatio Laurentii Zętkowic [Żętkowic?]: sprzedaż przez wdowę Reginę Butową (w asystencji opiekuna Stanisława Sikora) placu pustego przy ulicy Lubelskiej między placem Jana Grzymuszki a ulicą pospolitą małżonkom Wawrzyńcowi i Katarzynie Zętkowicom za 42 złp (22 złp gotówką, 20 złp na św. Michała).",
        "transkrypcja": """--- Skan #27 (fol. 12r) ---
1657 12.
...gotowych i odliczonych pieniędzy których przedawczyni...
kupcu swemu i dziatkom jego...
in forma ut supra...
Quod ad affectationem supra dicti Famati Stanislai Nawrocki...

Mancipatio Laurentii Zętkowic [Żętkowic?].
W domu Sławetnego Pana Mathyasza Tharasy Burmistrza natenczas Rezydującego
Krasnickiego przy bytności jego samego y Sławetnych Panów Kolegów przy boku jego siedzących
stał się pewny a nieodmienny kontrakt y wieczne zrzeczenie
między Uczciwą Reginą Buciną wdową pozostałą po niegdy Gabrielu Bucie
mieszczaninie kraśnickim z opiekunem jej Sławetnym Stanisławem Sikorem...
z jednej strony a Uczciwym Wawrzyńcem Zętkowicem [Żętkowicem?] z małżonką jego
Katarzyną mieszczanami kraśnickimi kupcami z drugiej strony...
sprzedała plac pusty przy ulicy Lubelskiej leżący między
placem Jana Grzymuszki z jednej a ulicą pospolitą z drugiej strony...
za summę pewną złotych polskich czterdzieści i dwa po gr. 30 rachując,
z której summy kupiec już oddał złotych 22 a drugą ratę złotych 20
oddać przyrzeka na Święty Michał blisko przyszły...
kosztuje gr. 30, zapisu i pieczęci fl. 2.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 28,
        "numer_pozycji": "28",
        "strona_pagina": "fol. 12v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1657",
        "kategoria": "Sąd Radziecki / Oblig Zętkowica i ugoda z Szymonem Szczygłem",
        "osoby_podmioty": "Wawrzyniec Zętkowic [Żętkowic?], Katarzyna Zętkowicowa, Regina Butowa (Gabrielowa Bucina), Stanisław Sikor (pisarz), Maciej Tharasa (burmistrz), Marcin Sitarski (rajca), Szymon Szczygieł",
        "kwoty_podatki": "10 złp",
        "opis_sprawy": "Oblig Wawrzyńca Zętkowica i żony Katarzyny na 10 złp dla Reginy Gabrielowej Buciny; poniżej Concordia seu amicabilis Compositio (ugoda przyjacielska) między rajcami Maciejem Tharasą i Marcinem Sitarskim a Szymonem Szczygłem w sprawie spadkowej i rozliczeń opiekuńczych.",
        "transkrypcja": """--- Skan #28 (fol. 12v) ---
12v 1657
Laurentius Zętkowic recognovit debitum Hon. Reginae
Viduae Gabrielowa Bucina fl. decem.
Przed Urzędem y Aktami ninieyszemi Radzieckiemi Krasnickiemi
stanąwszy oblicznie Uczciwy Wawrzyniec Zętkowic mieszczanin kraśnicki
z małżonką swoją Katarzyną oboje na ciele i umyśle zdrowi
będąc wyznali iż winni są Uczciwej Reginie Gabrielowej Bucinie
summę złotych polskich dziesięć...
na placu swoim przy ulicy Lubelskiej zabezpieczoną.
Quod ad affectationem supra dictae Actis praesentibus inserta est.

Concordia seu amicabilis Compositio inter Famatos
Dnos Mathiam Tharasa Martinum Sitarski Consules Crasn.
et Hon. Simonem Sczygieł ante Oppidum Crasn.
Stała się ugoda przyjacielska albo raczej Kompromis między Sławetnymi Pany
Mathyaszem Tharasą Burmistrzem natenczas Rezydującym Krasnickim i Marcinem
Sitarskim...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 29,
        "numer_pozycji": "29",
        "strona_pagina": "fol. 13r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1657",
        "kategoria": "Sąd Radziecki / Rozliczenie ugody z Szymonem Szczygłem (118 złp 18 gr)",
        "osoby_podmioty": "Marcin Sitarski (rajca), Szymon Szczygieł, Zofia Szczygłowa, Stanisław Nawrocki (rajca), Jan Dorada [?], Paweł Kłopot, Matyjasz Paluch [?]",
        "kwoty_podatki": "118 złp 18 gr, 30 złp, 22 złp",
        "opis_sprawy": "Dokończenie ugody między rajcami a Szymonem Szczygłem: rozliczenie sumy 118 złp 18 gr z dóbr po śp. rodzicach, wyznaczenie dwóch rat (25 złp i 30 złp na św. Marcina) w obecności Stanisława Nawrockiego, Jana Dorady [?] i Pawła Kłopota.",
        "transkrypcja": """--- Skan #29 (fol. 13r) ---
1657 13.
...Sitarskim Rajcą a Uczciwym Szymonem Sczygłem przedmieszczaninem
kraśnickim z drugiej strony...
ponieważ Sławetni Panowie wyżej pomienieni mieli sprawę dawną...
z Szymonem Sczygłem i z małżonką jego Zofią...
za dekretami powziętymi...
summa złotych sto ośmnaście i gr 18...
po czym Sławetni Panowie Stanisław Nawrocki Rajca, Jan Dorada [?]
i Paweł Kłopot przedmieszczanin kraśnicki jako przyjaciele...
rozsądzili iż Szymon Sczygieł ma oddać ratę pierwszą fl. 25
a drugą ratę fl. 30 na Święty Marcin blisko przyszły...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 30,
        "numer_pozycji": "30",
        "strona_pagina": "fol. 13v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1657",
        "kategoria": "Sąd Radziecki / Translacja prokonsulatu i Laudum Czopowe",
        "osoby_podmioty": "Szymon Szczygieł, Maciej Tharasa (prokonsul ustępujący), Ubald Janaszkowic (nowy prokonsul), Rada Miejska, Sąd Wójtowski, Pospólstwo",
        "kwoty_podatki": "30 złp (zakład), 20 gr (szpital), 9 gr / 1 fl 15 gr / 15 gr (czopowe)",
        "opis_sprawy": "Dokończenie ugody Szymona Szczygła (zakład 30 złp do Trybunału Zamoyskiego i 20 gr do Szpitala); sesja Sądu Łączonego z piątku po św. Franciszku 1657 r. (5 X): Translatio Proconsulatus od Macieja Tharasy do Ubalda Janaszkowica; poniżej Laudum Commune Czopowe w domu burmistrza Ubalda Janaszkowica (ustalające opłaty czopowe od gorzałki po 9 gr, od beczki miodu 1 fl 15 gr, od beczki piwa 15 gr).",
        "transkrypcja": """--- Skan #30 (fol. 13v) ---
13v 1657
...pod zakładem winy trzydzieści złotych do Trybunału Zamoyskiego
i gr. 20 do Szpitala przy oddaniu ostatniej raty...
Actum Coram Officio Composito Consulari Advocatiali
et Scabinali Jurato Crasnicensi feria sexta post Festum S. Francisci 1657.

Translatio Proconsulatus a Famato Dno Mathia Tharasa
ad Famatum Dnum Ubaldum Janaszkowic in patia totius
Magistratus Cechu Sutorum et Scultetorum Suburbii Crasn.
atque totius communitatis iuxta ritum et consuetudinem antiquam.

Laudum Commune Czopowe.
My Rada Miejska zobopolna tak Radziecka jako i Wójtowska z Ławnikami...
zgromadziwszy się do domu Sławetnego Ubalda Janaszkowica Burmistrza
natenczas Rezydującego Krasnickiego...
uchwaliliśmy podatek Czopowy na potrzeby miasta:
od gorzałki po gr. 9, od beczki miodu fl. 1 gr 15, od beczki piwa gr 15...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 31,
        "numer_pozycji": "31",
        "strona_pagina": "fol. 14r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1657",
        "kategoria": "Sąd Radziecki / Wyrok dla Sitarskiego, kwitacja Kapichy i cesja Skroda",
        "osoby_podmioty": "Marcin Sitarski (rajca), Paweł Niedbałka, Adam Kapicha [Kapica?], Regina Butowa (Gabrielowa Bucina), Gabriel But (śp.), Maciej Barkowic [?], Stanisław Skród [?] (z Rzeczycy)",
        "kwoty_podatki": "20 złp",
        "opis_sprawy": "Dokończenie uchwały o czopowym; sesja z piątku po św. Franciszku 1657 r.: wyrok dla Marcina Sitarskiego przeciw Pawłowi Niedbałce o 20 złp; poniżej Adam Kapicha [Kapica?] kwituje wdowę Gabrielową Bucinę (po śp. Gabrielu Bucie) ze wszystkich pretensji spadkowych i sądowych; na dole sesja z wtorku przed św. Barbarą 1657 r.: Maciej Barkowic [?] ceduje grunt pracowitemu Stanisławowi Skrodowi [?] ze wsi Rzeczycy.",
        "transkrypcja": """--- Skan #31 (fol. 14r) ---
1657 14.
...z powołaniem na Ratusz i poborców...

Actum Coram Officio Consulari feria sexta post Festum S. Francisci 1657.
In Causa Famati Martini Sitarski Consulis Crasn. Actoris
contra Hon. Paulum Niedbałka Civem Crasn. Citatum.
Przyznanej długu złotych dwadzieścia pożyczonych pieniędzy winy
Aktorowi Sąd ninieyszy nakazuje aby Citatus zapłacił złotych 20...

Adamus Kapicha [Kapica?] quietat Gabrielową Bucinę.
Przed Urzędem y Aktami ninieyszemi Radzieckiemi Krasnickiemi
stanąwszy oblicznie pracowity Adam Kapicha [Kapica?] zdrowy na ciele i umyśle
będąc dobrowolnie wyznał iż z Gabrielową Buciną wdową pozostałą
po niegdy Gabrielu Bucie z powodu wszelakich pretensyi...
zakończył i oną kwituje na wieczne czasy.

Actum Coram Officio Consulari feria tertia ante Festum
S. Barbarae Virginis et Martyris 1657.
Honestus Mathias Barkowic [?] ante Oppidum Crasnicensis
Laborioso Stanislao Skrod [?] de Villa Rzeczyca fundum cedit.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 32,
        "numer_pozycji": "32",
        "strona_pagina": "fol. 14v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1657",
        "kategoria": "Sąd Radziecki / Cesja na Podlesiu i proces o plac w Rynku",
        "osoby_podmioty": "Maciej Barkowic [?], Stanisław Skród [?] (z Rzeczycy), Ubald Janaszkowic (burmistrz, sąsiad), Paweł Kłopot (sąsiad), Andrzej Pieniążek (kowal), Paweł Różycki, Zofia Dzierżkowa",
        "kwoty_podatki": "200 złp",
        "opis_sprawy": "Dokończenie cesji Macieja Barkowica [?] dla pracowitego Stanisława Skroda [?] z Rzeczycy na Podlesiu (między Ubaldem Janaszkowicem a Pawłem Kłopotem); poniżej sesja z piątku po św. Łukaszu Ewangeliście 1657 r.: sprawa Andrzeja Pieniążka przeciw Pawłowi Różyckiemu o plac w Rynku po matce Zofii Dzierżkowej i dług 200 złp.",
        "transkrypcja": """--- Skan #32 (fol. 14v) ---
14v 1657
Do Urzędu y Akt ninieyszych Radzieckich Krasnickich przyszedłszy oblicznie
Uczciwy Mathyas Barkowic [?] przedmieszczanin kraśnicki...
zeznał iż winien będąc pracowitemu Stanisławowi Skrodowi [?] z Rzeczycy
złotych stodwadzieścia polskich... puszcza mu grunt swój własny na Podlesiu
między rolą Sławetnego Ubalda Janaszkowica Burmistrza natenczas Rezydującego
Krasnickiego z jednej a rolą Uczciwego Pawła Kłopota z drugiej strony leżący
do roku 1658 blisko przyszłego na Św. Wojciecha...

Actum feria sexta post Festum S. Lucae Evangelistae 1657.
In Causa Hon. Andreae Pieniążek Actoris contra Hon. Paulum Różycki Citatum.
Skarży się Aktor na Pozwanego iż od placu w Rynku stojącego
po matce jego należącego nie wie jakim prawem trzyma...
Pozwany odpowiedział że ten plac kupił u Pani Zofii Dzierżkowej
matki jej za sumę złotych 200 i na to ma zapis.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 33,
        "numer_pozycji": "33",
        "strona_pagina": "fol. 15r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1657",
        "kategoria": "Sąd Radziecki / Spór Pawła Różyckiego z Andrzejem Pieniążkiem",
        "osoby_podmioty": "Paweł Różycki, Andrzej Pieniążek, Andrzej Frączek [?], Zofia Dzierżkowa",
        "kwoty_podatki": "30 złp, 80 złp",
        "opis_sprawy": "Sesja ze środy przed śś. Szymonem i Judą 1657 r.: skarga i replika Pawła Różyckiego przeciw Andrzejowi Pieniążkowi o plac po matce i 30 złp oraz 80 złp z testamentu (wzmiankowany Andrzej Frączek [?]).",
        "transkrypcja": """--- Skan #33 (fol. 15r) ---
1657 15.
Actum feria secunda ante Festum SS. Simonis et Judae 1657.
In Causa Hon. Pauli Różycki Actoris contra Andream Pieniążek Citatum.
Uczciwy Paweł Różycki Mieszczanin Krasnicki skarży się na Pozwanego
Andrzeja Pieniążka że mu wziął fl. 30 które dał na plac...
A Pozwany Andrzej Pieniążek odpowiedział że ten plac należał po matce
i testamentem legowany jest na sumę fl. 80...
Sąd ninieyszy Radziecki Krasnicki przychylając się do pierwszego dekretu...
nakazuje aby Pozwany zapłacił lub plac ustąpił.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 34,
        "numer_pozycji": "34",
        "strona_pagina": "fol. 15v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1657",
        "kategoria": "Sąd Radziecki / Przyjęcie prawa miejskiego, sprawa Kłopota i Sitarskiego",
        "osoby_podmioty": "Paweł Różycki al. Dzierżek, Adam Kapica (gorzałcznik), Gabriel Kłopotek, Grzegorz Niedbałka, Marcin Sitarski (rajca i opiekun), Maciej Dzierżek [Sroka?] (śp.), Albert Łopata [?], Błażej Kołodziejczyk",
        "kwoty_podatki": "10 złp, 50 złp",
        "opis_sprawy": "Areszt na rzecz Pawła Różyckiego al. Dzierżka; sesja z soboty przed św. Marcinem 1657 r.: przyjęcie prawa miejskiego magdeburskiego (Jus Civile) przez Adama Kapicę gorzałcznika (Crematarius); sprawa Gabriela Kłopotka przeciw Grzegorzowi Niedbałce o 10 złp; sesja z piątku po św. Mikołaju 1657 r.: sprawa rajcy Marcina Sitarskiego (opiekuna sierot po Macieju Dzierżku [?]) przeciw Albertowi Łopacie [?] o 50 złp długu.",
        "transkrypcja": """--- Skan #34 (fol. 15v) ---
15v 1657
Urząd ninieyszy Radziecki pozwala aresztu na ostatku sumy którą
niedał Paweł Różycki... Michorkowi al. Dzierżkowi...
Decretum ab utraque parte susceptum est.

Actum Sabbato ante Festum S. Martini Episcopi 1657.
Adamus Kapica Crematarius Jus Civile Suscepit
in Jure Civili Magdeburgensi descriptum praestito juramento,
quod Actis cavetur est firmando memoriali.

In Causa Hon. Gabrielis Kłopotek Actoris contra Gregorium Niedbałka Citatum.
O dług złotych dziesięć... Sąd nakazuje zapłacić w terminie dwóch niedziel
pod winą sądową. Decretum ab utraque parte susceptum est.

Actum feria sexta post Festum S. Nicolai Episcopi 1657.
In Causa Famati Martini Sitarski Consulis Crasn. Tutoris Pupillorum olim
Mathiae Dzierżek [?] Actoris et Alberti Łopata [?] Tutoris...
Ponieważ Pozwany opiekun nie chciał płacić długu fl. 50 których winien
jest nieboszczykowi... Sąd pozwala Aktorowi intromisyi...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 35,
        "numer_pozycji": "35",
        "strona_pagina": "fol. 16r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1657",
        "kategoria": "Sąd Radziecki / Sprawa Jędrzeja Karwaczka o klacz",
        "osoby_podmioty": "Marcin Sitarski (opiekun), Albert Łopata [?], Jędrzej Karwaczek (poddany ze Stojeszyna), Stanisław Cwik, Stanisław Błaszczyk (świadek), Wincenty Bucha (świadek), Mikołaj Fortuna",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie dekretu dla opiekunów; sesja z wtorku po Niepokalanym Poczęciu NMP 1657 r. (11 XII): proces pracowitego Jędrzeja Karwaczka poddanego ze Stojeszyna przeciw Stanisławowi Cwikowi o klacz porwaną na szkodzie (świadkowie ze Stojeszyna: Stanisław Błaszczyk i Wincenty Bucha, oraz wzmianka o Mikołaju Fortunie).",
        "transkrypcja": """--- Skan #35 (fol. 16r) ---
1657 16.
...Opiekunowie pomienieni mają dosyć uczynić tak w oddaniu kapitału jako
i interesów zatrzymanych...

Actum feria tertia post Festum Gloriosae Conceptionis B. V. Mariae 1657.
In Causa Laboriosi Andreae Karwaczek Subditi de Villa Stojeszyn Actoris
contra Hon. Stanislaum Cwik ante Oppidum Crasnicensis Citatum.
Pracowity Jędrzej Karwaczek poddany ze wsi Stojeszyna skarżył się
na Pozwanego Stanisława Cwika przedmieszczanina kraśnickiego iż mu
porwał klacz jego własną na szkodzie i nie chce jej wrócić...
stawił dwóch świadków ze wsi Stojeszyna to jest pracowitych
Stanisława Błaszczyka i Wincentego Buchę którzy zeznali iż ta klacz
jest jego własna i ma lat sześć...
na co Urząd pozwolił i nakazał aby klacz przed Urzędem postawiono
w obecności Mikołaja Fortuny...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 36,
        "numer_pozycji": "36",
        "strona_pagina": "fol. 16v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1657",
        "kategoria": "Sąd Radziecki / Wyrok o klacz i zeznania w sprawie spadku Pezików",
        "osoby_podmioty": "Jędrzej Karwaczek, Stanisław Cwik, Sebastian Zarzyka, Maziarczyk, Szymon Kowalik, Józef Sobol (świadek), Wawrzyniec Pezik (śp.), Sebastian Pezik (śp.), Zofia Pezikowa, Sebastian Batusik (opiekun), Michał Zdebik (opiekun), Maciej Giza (opiekun), Paweł Bednarz, Szymon Stolarz",
        "kwoty_podatki": "20 złp (kilkadziesiąt złotych)",
        "opis_sprawy": "Dokończenie wyroku w sprawie klaczy Jędrzeja Karwaczka (wzmiankowany Sebastian Zarzyka i Maziarczyk); sesja z piątku po Niepokalanym Poczęciu NMP 1657 r. (14 XII): zeznanie świadka Józefa Sobola na instancję Szymona Kowalika o sierotach po Wawrzyńcu Peziku, bracie jego Sebastianie Peziku, opiekunach Sebastianie Batusiu, Michale Zdebiku i Macieju Gizie, oraz o długu u Pawła Bednarza (który kupił dom od Szymona Stolarza).",
        "transkrypcja": """--- Skan #36 (fol. 16v) ---
16v 1657
...iż Sebastian Zarzyka i Maziarczyk pod przysięgą przed Urzędem
wyznali że ta klacz jest własnością Karwaczka...
Sąd nakazuje klacz oddać i koszty sądowe zapłacić.

Actum feria sexta post Festum Gloriosae Conceptionis B. M. Virginis 1657.
Testimonium ex parte Hon. Simonis Kowalik ante Oppidum Crasn.
Ad Instantiam Hon. Simonis Kowalik... per Bedellum juratum adhibendus
testis Joseph Sobol ante Oppidum Crasnicensis...
juratus recognovit iż wiem dobrze że zmarły Wawrzyniec Pezik brat
nieboszczyka Sebastiana Pezika zostawił córkę Zofią Pezikównę
którą opiekowali się nieboszczyk Sebastian Batusik, Michał Zdebik
y Maciej Giza przedmieszczanie kraśniccy którzy dobra pozostałe
między dzieci rozdzielili...
a nieboszczyk Sebastian Batusik dał te pieniądze na interes Pawłowi
Bednarzowi od którego kupił dom Szymon Stolarz...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 37,
        "numer_pozycji": "37",
        "strona_pagina": "fol. 17r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1657",
        "kategoria": "Sąd Radziecki / Zeznanie kowala Szymona Dzeka i wyrok dla Zofii Pezikówny",
        "osoby_podmioty": "Szymon Dzek [Dzik?] (kowal, świadek), Paweł Bednarz, Sebastian Batusik (śp.), Jakub Dzek [Dzik?] (brat), Jan Rzepka (śp.), Szymon Kowalik, Zofia Pezikówna (żona Sz. Kowalika), Jan Batusik (pozwany)",
        "kwoty_podatki": "20 złp, 10 złp (razem 30 złp)",
        "opis_sprawy": "Zeznanie drugiego świadka — kowala Szymona Dzeka [Dzika?] o długu Pawła Bednarza i spłacie 20 złp dla Jakuba Dzeka i 10 złp dla Sebastiana Batusia; poniżej sesja ze środy po Niepokalanym Poczęciu NMP 1657 r.: dekret dla Szymona Kowalika i jego żony Zofii Pezikówny przeciw Janowi Batusiowi o spłatę 20 złp i 10 złp po ojcu Sebastianie Peziku.",
        "transkrypcja": """--- Skan #37 (fol. 17r) ---
1657 17.
2dus Testis Hon. Simon Dzek [Dzik?] Serri faber Civis Crasn. post praestitum
juramentum et iuris examinationem recognovit:
Wiadomo mi jest dobrze iż kiedy Paweł Bednarz miał dług u
Pawła... ten dług oddał bratu memu Jakubowi Dzekowi [Dzikowi?]
złotych dwadzieścia a złotych dziesięć oddał Sebastianowi Batusiowi...
co wszystko zeznał na prośbę Szymona Kowalika.

Actum feria quarta post Festum Gloriosae Conceptionis B. M. Virginis 1657.
In Causa Hon. Simonem Kowalik et Zophiam Pezikównę ante Oppidum
Crasnicensis Actores contra Hon. Joannem Batusik ante Oppidum Crasn. Citatum.
Fundując się na relacyi dwóch świadków którzy pod przysięgą
wyznali że nieboszczyk Sebastian Pezik ociec Pozwanej Zofii
zostawił po sobie sumę złotych dwadzieścia i dziesięć u brata swego
nieboszczyka Sebastiana Batusia i Jakuba Dzeka...
Sąd ninieyszy Radziecki nakazuje aby Pozwany Jan Batusik jako
sukcesor brata swego Sebastiana oddał...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 38,
        "numer_pozycji": "38",
        "strona_pagina": "fol. 17v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1658",
        "kategoria": "Sąd Radziecki / Dokończenie dekretu i Elekcja Magistratu 1658 r.",
        "osoby_podmioty": "Sebastian Pezik, Jakub Dzek, Jan Rzepka, Jan Batusik, Ubald Janaszkowic (wójt), Jan z Zamościa (dziedzic), Krzysztof Brzostowski [Brzozowski?] (komisarz), Stanisław Borkowski (komisarz), Stanisław Nawrocki (rajca), Marcin Sitarski (rajca), Albert Kurzący (rajca), Albert Szafraniec (wójt)",
        "kwoty_podatki": "20 złp, 10 złp",
        "opis_sprawy": "Dokończenie wyroku dla Szymona Kowalika i Zofii Pezikówny przeciw Janowi Batusiowi (wzmianka o domu Rzepczyńskim kupionym przez śp. Jana Rzepkę); poniżej uroczysta ELECTIO z wtorku przed Nawróceniem św. Pawła 1658 r. (22 I 1658) w domu Ubalda Janaszkowica z udziałem komisarzy ordynackich Krzysztofa Brzostowskiego [Brzozowskiego?] i Stanisława Borkowskiego: wybór czterech rajców (Ubalda Janaszkowica, Stanisława Nawrockiego, Marcina Sitarskiego i Alberta Kurzącego) oraz wójta Alberta Szafrańca.",
        "transkrypcja": """--- Skan #38 (fol. 17v) ---
17v 1658
...na ojca swego Sebastiana Pezika opiekuna pomienionej Aktorki na tych
złotych dwudziestu z dobrami dochodzić na sukcesorach nieboszczyka
Jakuba Dzeka którzy dobra jego otrzymali osobliwie na domu Rzepczyń-
skim który był kupił nieboszczyk Jan Rzepka po nieboszczyku Peziku...
Decretum ab utraque parte susceptum est.

ELECTIO
Solemni et Laudabilis Magistratus Civilis Crasn. in Domo Famati
Dni Ubaldi Janaszkowic Proconsulis Crasn. in patia totius Magistratus
et Communitatis celebrata feria tertia ante Festum Conversionis S. Pauli Apli
Anno Domini Millesimo Sexcentesimo Quinquagesimo Octavo.

Et in primis ex Brachio Illmi ac Magnifici Dni Dni Joannis de Zamoście
Zamoyski Pocillatoris Regni Dni nostri Haereditarii Clementissimi Generosi ac
Magnifici Dni Christophorus Brzostowski [Brzozowski?] Pocillator Czernichoviensis...
una cum Generoso Dno Stanislao Borkowski Commissariis ad hanc Electionem
ex Brachio supra dicti Illmi Dni demissis elegerunt duos Consules Residentes:
Famatum Dnum Ubaldum Janaszkowic et Famatum Dnum Stanislaum Nawrocki...
qui quidem tres tali modo electi adsciverunt sibi quartum Consulem Residentem
Famatum Dnum Albertum Kurzący.
In Advocatum vero et Judicem Ordinarium Juratum Crasn.
eligunt et constituunt Famatum Dnum Albertum Szafraniec...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 39,
        "numer_pozycji": "39",
        "strona_pagina": "fol. 18r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1658",
        "kategoria": "Sąd Radziecki / Lista ławników i cechmistrzów z Elekcji 1658 r. oraz sprawa Prokopka",
        "osoby_podmioty": "Marcin Skarzyński (ławnik), Błażej Kołodziejczyk (ławnik i cechmistrz), Jan Zdebikowic (ławnik), Jan Szczurkowic (ławnik), Maciej Konięga (ławnik), Augustyn Kwasowic (ławnik), Grzegorz Fox (ławnik), Maciej Tharasa (asesor i cechmistrz), Stanisław Nawrocki (prokonsul), Wawrzyniec Zętkowic (cechmistrz), Bartłomiej Święcicki (cechmistrz), Maciej Różycki (cechmistrz), Jan Potokowic (egzaktor), Bartłomiej Bożęborski (egzaktor), Maciej Jarzębek (egzaktor), Wawrzyniec Prokopek, Andrzej Kowalik, Anna Kowalikowa",
        "kwoty_podatki": "12 złp 5 gr",
        "opis_sprawy": "Dokończenie Elekcji 1658 r. (ławnicy, asesor do Trybunału Zamoyskiego Maciej Tharasa, prokonsul Stanisław Nawrocki, pięciu cechmistrzów oraz egzaktorzy Jan Potokowic, Bartłomiej Bożęborski i Maciej Jarzębek); poniżej sesja z piątku w dzień Nawrócenia św. Pawła 1658 r. (25 I): zeznania i sprawa Wawrzyńca Prokopka przeciw Maciejowi Tharasie (opiekunowi dzieci Andrzeja i Anny Kowalików, m.in. Bartosza, Kaliny i Lidwiny) o 12 złp 5 gr.",
        "transkrypcja": """--- Skan #39 (fol. 18r) ---
1658 18.
...ordinaverunt et approbaverunt.
Scabini antiqui: Martinus Skarzyński, Blasius Kołodziejczyk, Joannes Zdebikowic,
Joannes Szczurkowic, Mathias Konięga, Augustinus Kwasowic et Gregorius Fox.
In Assessorem ad Suprema Judicia Tribunalis Zamoscensis Famatum Dnum
Mathiam Tharasa Consulem antiquum constituerunt.
Absoluta itaque Electione Famatus D. Stanislaus Nawrocki Offm Proconsulatus
una cum Thesauro Reipublicae suscepit.
In Archi Magistros:
Pellionum: Famatum D. Mathiam Tharasa
Sutorum: Famatum Blasium Kołodziejczyk
Sartorum: Hon. Laurentium Zętkowic
Fabrum: Hon. Bartholomaeum Święcicki
Textorum: Hon. Mathiam Różycki.
Exactores ad exactiones publicas: Famatum Joannem Potokowic et
Bartholomaeum Bożęborski constituerunt. Exactor Braseorum: Hon. Mathias Jarzębek.

Actum Coram Officio Consulari feria sexta ipso die Festi Conversionis
S. Pauli proxima Anno Dni 1658.
Testimonium ex parte Hon. Laurentii Prokopek ante Oppidum Crasn.
Pro Hon. Mathia Dzik [?] Tutore Minorum Andreae et Annae
Kowalików ante Oppidum Crasnicensis Actore ac Minorum Bartosza,
Kaliny, Lidwiny Kowalików Tutoribus ipsius Famati Dni Mathiae Tharasa...
o dług złotych dwanaście y gr 5...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 40,
        "numer_pozycji": "40",
        "strona_pagina": "fol. 18v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1658",
        "kategoria": "Sąd Radziecki / Zeznania Prokopka i sprawa Batusia z Bożęborskim",
        "osoby_podmioty": "Wawrzyniec Prokopek, Sebastian Węgorkiewicz (świadek), Marek [?] (krawiec?), Jan Batusik, Bartłomiej Bożęborski, Wawrzyniec Pezik (śp.), Jakub Dzek [Dzik?] (śp.), Zofia Pezikówna",
        "kwoty_podatki": "20 złp",
        "opis_sprawy": "Dokończenie sprawy Wawrzyńca Prokopka oraz zeznanie świadka Sebastiana Węgorkiewicza o rozmowie w sprawie konia z Markiem; poniżej sesja z piątku w wigilię Oczyszczenia NMP 1658 r. (1 II): sprawa Jana Batusika przeciw Bartłomiejowi Bożęborskiemu o 20 złp długu po śp. Jakubie Dzeku [Dziku?] i Wawrzyńcu Peziku na placu Rzepczyńskim.",
        "transkrypcja": """--- Skan #40 (fol. 18v) ---
18v 1658
Radziecki Krasnicki pozwala dylacyi Pozwanemu na zapłacenie tego długu do
dwóch niedziel... Decretum ab utraque parte susceptum est.

Testimonium ex parte Hon. Laurentii Prokopek ante Oppidum Crasn.
Ad Instantiam Hon. Laurentii Prokopek... Hon. Sebastianus Węgorkiewicz
ante Oppidum Crasn. ad Officium per Bedellum juratum adhibitus...
recognovit iż w jesieni nie pamiętam którego dnia przed Świętym Michałem...
posłał mię Wawrzyniec Prokopek do domu Marka...
że mu winien 30 złp za konia...

Actum Coram Officio Consulari feria sexta in vigilia Festi
Purificationis B. M. Virginis proxima 1658.
In Causa Hon. Joannis Batusik ante Oppidum Crasn. Actoris
ac Hon. Bartholomaei Bożęborski Civis Crasnicensis Citati.
Uczciwy Jan Batusik przedmieszczanin kraśnicki skarżył się na Pozwanego
Bartłomieja Bożęborskiego iż nieboszczyk ojciec jego jako opiekun
nieboszczyka Wawrzyńca Pezika pożyczył był złotych dwadzieścia
nieboszczykowi Jakubowi Dzekowi [Dzikowi?] na plac Rzepczyński...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 41,
        "numer_pozycji": "41",
        "strona_pagina": "fol. 19r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1658",
        "kategoria": "Sąd Radziecki / Wyroki: Batusik vs Bożęborski, Nowak vs Olęcki, Młodnicki vs Niedbałka",
        "osoby_podmioty": "Jan Batusik, Bartłomiej Bożęborski, Zofia Pezikówna, Jakub Dzek, Jan Rzepka, Benedykt Nowak, Wojciech Olęcki, Jędrzej Młodnicki, Paweł Niedbałka",
        "kwoty_podatki": "20 złp, 50 złp, 35 złp",
        "opis_sprawy": "Dokończenie wyroku między Janem Batusikiem a Bartłomiejem Bożęborskim (odesłanie do spadkobierców Jakuba Dzeka i Rzepki); wyrok dla Benedykta Nowaka przeciw Wojciechowi Olęckiemu o 35 złp; nakaz zamknięcia Pawła Niedbałki na Bramie Lubelskiej na wniosek Jędrzeja Młodnickiego.",
        "transkrypcja": """--- Skan #41 (fol. 19r) ---
1658 19.
Bożęborskiemu gdzie pomieniony Rzepczyński miał być wszystkie długi spłacać...
A potem pozostała sierotka Zofia Pezikówna przed Sądem dochodziła tych pieniędzy...
Sąd ninieyszy Radziecki Krasnicki nakazuje Aktorowi aby oblig pokazał
nieboszczyka Jakuba Dzeka albo atestacyą... Decretum ab utraque parte susceptum est.

Pro Benedicto Nowak ante Oppidum Crasnicensis Actore
et Hon. Alberto Olęcki Civem Crasnicensis Citato.
Przychylając się do pierwszego dekretu...
nakazuje się Pozwanemu aby zapłacił dług fl. 35 Aktorowi do trzeciego dnia.
Decretum ab utraque parte susceptum est.

In Causa Hon. Andreae Młodnicki Actoris ac Hon. Pauli Niedbałka Citati.
Ponieważ to clare constat ex relatione Bedelli że Citatus do prawa nie stanął...
Sąd skazuje go na więzienie zamknięte na Bramie Lubelskiej...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 42,
        "numer_pozycji": "42",
        "strona_pagina": "fol. 19v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1658",
        "kategoria": "Sąd Radziecki / Sprawa o arszenik, dług Olkowskiego i spór Wroniny z Kotyczem",
        "osoby_podmioty": "Jędrzej Młodnicki, Paweł Niedbałka, Wawrzyniec Prokopek, Jan Olkowski (świadek), Grzegorz Królik, Stanisław Cwik, Jadwiga Wronina (wdowa), Wojciech Kotycz [Kotłyk?], Maciej Tharasa (rajca)",
        "kwoty_podatki": "20 złp, 30 złp",
        "opis_sprawy": "Dokończenie dekretu przeciw Pawłowi Niedbałce (20 złp); sesja z piątku po św. Dorocie 1658 r. (8 II): zeznanie Jana Olkowskiego na instancję Wawrzyńca Prokopka o 30 złp; wyrok dla Grzegorza Królika przeciw Stanisławowi Cwikowi o 20 złp; poniżej początek procesu wdowy Jadwigi Wroniny przeciw Wojciechowi Kotyczowi [Kotłykowi?] o arszenik znaleziony i rzekome otrucie.",
        "transkrypcja": """--- Skan #42 (fol. 19v) ---
19v 1658
...zanim nie zapłaci albo nie zaręczy złotych dwudziestu...
Decretum ab utraque parte susceptum est.

Actum Coram Officio Consulari feria sexta post Festum
S. Dorotheae Virginis et Martyris 1658.
Testimonium ex parte Laurentii Prokopek.
Testis Hon. Joannes Olkowski Juratus sub juramento corporali recognovit
iż słyszałem od Wawrzyńca Prokopka że winien mu fl. 30...

Pro Hon. Gregorio Królik ante Oppidum Crasn. Actore
ac Hon. Stanislao Cwik ante Oppidum Crasn. Citato.
Przychylając się do dekretu z roku 1657...
nakazuje się Pozwanemu aby dług fl. 20 oddał do ósmego dnia.

In Causa Hedvigis Viduae Wronina Actricis ac Albertum Kotycz [Kotłyk?] Citatum.
Iż skoro informacyą pokazała przed Sądem P. Mathyasza Tharasy Rajcy
Krasnickiego że żona Wojciecha Kotycza [?] miała arszenik...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 43,
        "numer_pozycji": "43",
        "strona_pagina": "fol. 20r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1658",
        "kategoria": "Sąd Radziecki / Wyrok o arszenik i sprawa Batusia z Bożęborskim",
        "osoby_podmioty": "Jadwiga Wronina, Wojciech Kotycz [Kotłyk?], żona Wojciecha Kotycza, kramarze żydowscy, Jan Batusik, Bartłomiej Bożęborski, Zofia Pezikowa, Szymon Kowalik, Jan Rzepka (śp.), Stanisław Sikora (świadek)",
        "kwoty_podatki": "20 złp",
        "opis_sprawy": "Dokończenie procesu o arszenik (wyjaśnienie oskarżonej, że znalazła proszek u kramarzy żydowskich i wzięła go za tabakę; nakaz przysięgi oczyszczającej tacto pectore i uwięzienia w baszcie do dnia przysięgi); poniżej sesja ze środy przed św. Maciejem 1658 r. (20 II): sprawa Jana Batusika z Zofią Pezikową (żoną Szymona Kowalika) przeciw Bartłomiejowi Bożęborskiemu o 20 złp po śp. Janie Rzepce (świadek Stanisław Sikora).",
        "transkrypcja": """--- Skan #43 (fol. 20r) ---
1658 20.
Arsenik dalej znalazł tedy jej stary nieborak chłopie gardło wziąć...
Aktorka zaś broniła się iż w kramnicy żydowskiej znalazła
y nie wiedziała że to był arsenik ale mniemała że tabaka...
Urząd ninieyszy Radziecki Krasnicki widząc iż Aktorka nie ma
świadków dostatecznych ale ma na sobie podejrzenie o takowy występek,
nakazuje jej zamknięcie do baszty aż do wykonania przysięgi
tacto pectore że tego arszeniku nikomu na szkodę nie użyła...
Decretum susceptum est a partibus.

Actum Coram Officio Consulari feria quarta ante Festum
S. Mathiae Apostoli proxima 1658.
In Causa Hon. Joannis Batusik ante Oppidum Crasn. Actoris
ac Hon. Bartholomaei Bożęborski Civis Crasnicensis Citati.
Aktor z Zofią Pezikową małżonką Szymona Kowalika...
pokazali atestacyą że nieboszczyk Jan Rzepka podjął się długów
wszystkich spłacić a złotych dwadzieścia pozostałych...
świadek Stanisław Sikora zeznał że u Bartosza Bożęborskiego
zostają pieniądze Jana Rzepki...
Urząd nakazuje aby Bożęborski oddał Aktorowi złotych dwadzieścia.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 44,
        "numer_pozycji": "44",
        "strona_pagina": "fol. 20v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1658",
        "kategoria": "Sąd Radziecki / Inwentarz po Wojciechu Kołodzieju i sprawa Nowaka",
        "osoby_podmioty": "Jan Batusik, Bartłomiej Bożęborski, Wojciech Kołodziej (śp.), Jan Zdebikowic (pisarz), Walenty Sitarczyk, Maciej Tharasa (rajca), Stanisław Nawrocki (burmistrz), Benedykt Nowak, Wojciech Olęcki",
        "kwoty_podatki": "35 złp, 45 złp",
        "opis_sprawy": "Dokończenie dekretu Batusika i Bożęborskiego (35 złp); sesja z soboty w wigilię św. Macieja Apostoła 1658 r. (23 II): Inwentarz rzeczy pozostałych po Wojciechu Kołodzieju spisany przez Jana Zdebikowica i Walentego Sitarczyka na polecenie rajcy Macieja Tharasy i burmistrza Stanisława Nawrockiego (koła małe i wielkie, siekiery, dłuta, świdry, piła ręczna, kapelusz czarny); poniżej sesja z piątku przed św. Kazimierzem 1658 r.: sprawa Benedykta Nowaka przeciw Wojciechowi Olęckiemu o 35 złp.",
        "transkrypcja": """--- Skan #44 (fol. 20v) ---
20v 1658
...od Sukcesorów nieboszczyka Jana Rzepki...
Quod Decretum ab utraque parte susceptum est... fl. 35.

Actum Sabbato in vigilia Festi S. Mathiae Apostoli 1658.
Inwentarz rzeczy pozostałych po Wojciechu Kołodzieju.
Na instancyą Uczciwych Szymona Łycka y Walentego Sitarczyka
mieszczan kraśnickich były zlustrowane i spisane przez
Sławetnego Jana Zdebikowica Rajcę Krasnickiego z ramienia
Sławetnego P. Stanisława Nawrockiego Burmistrza natenczas
Rezydującego i w domu Sławetnego P. Mathyasza Tharasy Rajcy
rzeczy po Wojciechu Kołodzieju które są takie:
Naprzód kół wielkich poślednich 10, kół przednich 4,
kół małych 4, dłuto małe, świdry żelazne, siekiera wielka,
cieślica, osko, berlik, piła ręczna mała, dłuto żelazne,
toporek do cieślicy, kapelusz czarny, sukman stary...
długów fl. 45, kobylica z narzędziami...

Actum Coram Officio Consulari feria sexta ante Festum
S. Casimiri Confessoris 1658.
In Causa Hon. Benedicti Nowak Actoris ac Hon. Alberti Olęcki Citati.
O dług złotych 35... Sąd nakazuje wykonanie przysięgi przez Pozwanego.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 45,
        "numer_pozycji": "45",
        "strona_pagina": "fol. 21r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1658",
        "kategoria": "Sąd Radziecki / Glosa Zwiastowania, translacja i testament Jadwigi Jasińskiej",
        "osoby_podmioty": "Benedykt Nowak, Wojciech Olęcki, Stanisław Nawrocki (prokonsul), Albert Kurzący (prokonsul), Sabina [?], o. Marcin Mrowski (przeor augustianów), Jadwiga Jasińska [Jasinek?] (śp.)",
        "kwoty_podatki": "35 złp, 18 gr",
        "opis_sprawy": "Dokończenie wyroku Nowaka przeciw Olęckiemu (35 złp); sesja z soboty przed Zwiastowaniem NMP 1658 r. (23 III): skarga prokonsula Stanisława Nawrockiego o zniewagę (kara 18 gr); poniżej Translatio Proconsulatus z piątku po Wielkanocy 1658 r. od Stanisława Nawrockiego do Alberta Kurzącego; poniżej zeznanie świadka na instancję o. Marcina Mrowskiego (przeora konwentu św. Augustyna) o testamencie śp. Jadwigi Jasińskiej [Jasinek?].",
        "transkrypcja": """--- Skan #45 (fol. 21r) ---
1658 21.
...dług złotych 35... Decretum ab utraque parte susceptum est.

Actum Coram Officio Consulari Sabbato ante Festum
Gloriosae Annuntiationis B. M. Virginis proxime Anno Dni 1658.
Glosa Annuntiationis.
Famatus Stanislaus Nawrocki Proconsul... skarżył się na Sabinę [?]
że go przed domem znieważyła słowy uszczypliwemi...
skazana na karę gr. 18 do skrzynki miejskiej.

Actum Coram Officio Composito Consulari Advocatiali
et Scabinali Jurato Crasnicensi feria sexta post Festa Solennia Paschae 1658.
Translatio Proconsulatus a Famato D. Stanislao Nawrocki ad Famatum
D. Albertum Kurzący in patia Cechu Sutorum Scultetorumque Suburbii
et totius communitatis cum omnibus Thesauris civilibus iuxta ritum
et consuetudinem antiquam.

Testimonium ex parte Rndi Patris Martini Mrowski Ord. S. Augustini.
Na zadanie J. X. Marcina Mrowskiego Kanonika i Przeora Zakonu S. Augustyna
Konwentu Krasnickiego przed Urzędem y Aktami ninieyszemi Radzieckiemi
zeznał pracowity świadek iż przed śmiercią nieboszczka Jadwiga Jasińska
uczyniła testament i legowała dwadzieścia złotych na kościół...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 46,
        "numer_pozycji": "46",
        "strona_pagina": "fol. 21v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1658",
        "kategoria": "Sąd Radziecki / Legat na kościół św. Ducha i sprzedaż roli na Podlesiu",
        "osoby_podmioty": "Jadwiga Jasińska (śp.), Augustyn Niedźwiadek, Marianna Zofia Kosińska (w Lublinie), o. Marcin Mrowski, Marcin Sitarski (rajca i zbywca/nabywca), Jędrzej Pasio [?] (śp.), Wojciech Kurzący (burmistrz), Jan Piasecki, Regina Płazińska [?] (żona J. Piaseckiego), Regina Szałkowicówna [?] (żona M. Sitarskiego)",
        "kwoty_podatki": "20 złp, 160 złp",
        "opis_sprawy": "Dokończenie zeznań o legacie Jadwigi Jasińskiej (20 złp u Augustyna Niedźwiadka i Marianny Zofii Kosińskiej w Lublinie) oraz wyrok dla o. Marcina Mrowskiego przeciw Marcinowi Sitarskiemu o 20 złp dla kościoła św. Ducha; poniżej sesja z piątku w dzień św. Stanisława 1658 r. (10 V): Mancipatio Famati Martini Sitarski cum Joanne Piasecki — sprzedaż roli na Podlesiu przez Jana Piaseckiego i żonę Reginę Płazińską [?] rajcy Marcinowi Sitarskiemu i jego żonie Reginie Szałkowicównej [?] za 160 złp.",
        "transkrypcja": """--- Skan #46 (fol. 21v) ---
21v 1658
...Jasińska pożyczyła była Augustynowi Niedźwiadkowi y małżonce jego Mariannie
Zofii Kosińskiej w Lublinie mieszkającej... zł 20...

Pro Rndo Patre Martino Mrowski Ord. S. Augustini Actore
ac Famato Dno Martino Sitarski Consule Crasn. Citato.
Ponieważ okazało się że ten dług fl. 20 który nieboszczka Jadwiga
Jasińska legowała przy śmierci swej na pogrzeb ciała swego do kościoła
św. Ducha kraśnickiego zostaje u Augustyna Niedźwiadka...
Sąd Radziecki nakazuje Pozwanemu aby ten dług fl. 20 jako opiekun
oddał... Decretum ab utraque parte susceptum est.

Actum Coram Officio Consulari feria sexta ipso die Festi
S. Stanislai Episcopi et Martyris 1658.
Mancipatio Famati Martini Sitarski cum Joanne Piasecki.
W domu Sławetnego Pana Wojciecha Kurzącego Burmistrza natenczas
Rezydującego Krasnickiego przy bytności jego samego y Panów Kolegów
stał się pewny kontrakt kupna między Uczciwym Janem Piaseckim
y małżonką jego Reginą Płazińską [?] przedawcami z jednej
a Sławetnym Panem Marcinem Sitarskim Rajcą i małżonką jego Reginą
Szałkowicówną [?] kupcami z drugiej strony...
sprzedali rolę swoją własną na Podlesiu leżącą między rolą
Marcina Sitarskiego z jednej a rolą Sławetnego Ubalda...
za summę pewną złotych polskich sto sześćdziesiąt...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 47,
        "numer_pozycji": "47",
        "strona_pagina": "fol. 22r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1658",
        "kategoria": "Sąd Radziecki / Sprawa o składki publiczne i translacja prokonsulatu",
        "osoby_podmioty": "Jan Piasecki, Marcin Sitarski (rajca i prokonsul), Stanisław Jurkowic (egzaktor), Bartłomiej Bożęborski (egzaktor), Jan Skarzyk, Wojciech Kurzący (ustępujący prokonsul)",
        "kwoty_podatki": "160 złp, 16 złp 17 gr",
        "opis_sprawy": "Dokończenie sprzedaży roli na Podlesiu za 160 złp; sesja z czwartku po Zielonych Świątkach 1658 r.: wyrok w sprawie egzaktorów miejskich Stanisława Jurkowica i Bartłomieja Bożęborskiego przeciw Janowi Skarzykowi o 16 złp 17 gr zaległych składek publicznych; poniżej Translatio Proconsulatus z piątku po św. Janie Chrzcicielu 1658 r. (28 VI) od Wojciecha Kurzącego do Marcina Sitarskiego.",
        "transkrypcja": """--- Skan #47 (fol. 22r) ---
1658 22.
...za summę pewną złotych polskich sto sześćdziesiąt w każdy złoty po gr. 30
rachując, które to pieniądze przedawcy od kupca w zupełności odebrali...
Quod Actis praesentibus inserta est.

Actum Coram Officio Consulari in patia Famati D. Advocati
feria quinta post Festa Solennia Pentecostes 1658.
Pro Famatis Stanislao Jurkowic et Bartholomaeo Bożęborski
Exactoribus juratis Actoribus ac Hon. Joanne Skarzyk cive Crasn. Citato.
O zatrzymanie składek publicznych złotych szesnaście i gr 17...
Sąd ninieyszy Radziecki nakazuje Pozwanemu aby zaraz złożył te składki
pod winą sądową. Decretum ab utraque parte susceptum est.

Actum Coram Officio Composito Consulari Advocatiali
et Scabinali Jurato Crasnicensi feria sexta post Festum
S. Joannis Baptistae proxima Anno Dni 1658.
Translatio Proconsulatus a Famato D. Alberto Kurzący ad Famatum
D. Martinum Sitarski in patia totius Magistratus Cechu Sutorum
Scultetorumque Suburbii cum omnibus thesauris civilibus iuxta ritum
et consuetudinem antiquam.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 48,
        "numer_pozycji": "48",
        "strona_pagina": "fol. 22v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1658",
        "kategoria": "Sąd Radziecki / Zeznania Anny Bielikowej o długach w Lublinie i translacja",
        "osoby_podmioty": "Anna Bielikowa [Bielińska?] (wdowa po Macieju Bieliku z Rzeczycy), Maciej Bielik [?] (śp.), Walenty Jarzyk (asystent), Samuel Cirulik, Marcin Sitarski (ustępujący prokonsul), Ubald Janaszkowic (nowy prokonsul)",
        "kwoty_podatki": "24 złp, 7 złp, 8 złp",
        "opis_sprawy": "Sesja ze wtorku przed Wniebowzięciem NMP 1658 r. (13 VIII): zeznania na instancję wdowy Anny Bielikowej [Bielińskiej?] (po śp. Macieju Bieliku z Rzeczycy, w asystencji Walentego Jarzyka z Kraśnika) o długach lubelskich (24 złp u Samuela Cirulika, 7 złp i 8 złp w Lublinie); poniżej Translatio Proconsulatus z poniedziałku przed św. Jadwigą 1658 r. od Marcina Sitarskiego do Ubalda Janaszkowica.",
        "transkrypcja": """--- Skan #48 (fol. 22v) ---
22v 1658
Actum Coram Officio Consulari feria tertia ante Festum
Gloriosae Assumptionis B. M. Virginis proxime 1658.
Testimonium ex parte Annae Bielikowa [Bielińska?].
Ad Instantiam Hon. Annae Bielikowa [?] viduae derelictae post olim Hon.
Mathiam Bielik de Rzeczyca in assistentia Hon. Valentini Jarzyk Civis
Crasnicensis... zeznał świadek iż nieboszczyk Maciej Bielik małżonek
jej pożyczył był w Lublinie u Samuela Cirulika fl. 24 oraz u innych
w Lublinie fl. 7 y fl. 8 które to długi miał przy sobie zapisane...
prosiła aby te zeznania do ksiąg wpisane były dla dochodzenia w Lublinie.

Actum Coram Officio Composito Consulari Advocatiali
et Scabinali Jurato Crasnicensi feria secunda ante Festum S. Hedvigis 1658.
Translatio Proconsulatus a Famato Martino Sitarski ad Famatum
D. Ubaldum Janaszkowic in patia totius Magistratus Cechu Sutorum
et communitatis Scultetorumque Suburbii cum omnibus thesauris civilibus
iuxta ritum et consuetudinem antiquam.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 49,
        "numer_pozycji": "49",
        "strona_pagina": "fol. 23r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Sąd Radziecki / Otwarcie roku 1659 i sprzedaż domu na ul. Lubelskiej",
        "osoby_podmioty": "Ubald Janaszkowic (burmistrz), Wojciech Kurzący (rajca), Maciej Tharasa (rajca), Marcin Sitarski (rajca i zbywca), Regina Sitarska, Michał Cwikielski [Chucholski?], Zofia Biernatówna (żona M. Cwikielskiego), Grabowski (sąsiad), Mikołajewski (sąsiad)",
        "kwoty_podatki": "150 złp",
        "opis_sprawy": "ANNUS INCIPIT NOVUS 1659 (czwartek po Trzech Królach, 9 I 1659 r.) w domu burmistrza Ubalda Janaszkowica (w obecności rajców Wojciecha Kurzącego i Macieja Tharasy): Mancipatio Dni Michaelis Cwikielski cum Famato Martino Sitarski — sprzedaż domu przy ulicy Lubelskiej (między placem Grabowskim a Mikołajewskim) przez Marcina Sitarskiego i żonę Reginę Michałowi Cwikielskiemu [Chucholskiemu?] i jego żonie Zofii Biernatównie za 150 złp.",
        "transkrypcja": """--- Skan #49 (fol. 23r) ---
1659 23.
ANNUS INCIPIT NOVUS
Millesimus Sexcentesimus Quinquagesimus Nonus.
Actum Coram Officio Consulari feria quinta
post Festum Trium Regum proxime 1659.
Mancipatio Dni Michaelis Cwikielski [Chucholski?] cum
Famato Martino Sitarski.
W domu Sławetnego P. Ubalda Janaszkowica Burmistrza
natenczas Rezydującego Krasnickiego przy bytności jego samego
y Sławetnych Panów Wojciecha Kurzącego y Mathyasza Tharasy Radziec
Krasnickich przy boku jego siedzących stał się pewny a nieodmienny
kontrakt y wieczne zrzeczenie między Sławetnym P. Marcinem
Sitarskim Rajcą Krasn. y małżonką jego Reginą przedawcami
z jednej a Uczciwym Michałem Cwikielskim [Chucholskim?]
y małżonką jego Uczciwą Zofią Biernatówną kupcami z drugiej strony...
sprzedali dom swój własny stojący przy ulicy Lubelskiej między
placem Grabowskim z jednej a placem Mikołajewskim z drugiej strony
za summę pewną złotych polskich sto pięćdziesiąt po gr. 30 rachując
którą sumę przedawca od kupca zupełnie odebrał i kwituje...
Zapisu i pieczęci gr. 6.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 50,
        "numer_pozycji": "50",
        "strona_pagina": "fol. 23v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Sąd Radziecki / Elekcja Magistratu Miasta Kraśnika na rok 1659",
        "osoby_podmioty": "Ubald Janaszkowic (wójt), Jan z Zamościa (dziedzic), Krzysztof Brzostowski [Brzozowski?] (komisarz), Marcin Sitarski (rajca), Stanisław Nawrocki (prokonsul), Albert Kurzący (rajca), Maciej Tharasa (rajca i cechmistrz), Marcin Skarzyński (ławnik), Błażej Kołodziejczyk (ławnik), Augustyn Kwasowic (ławnik), Jan Zdebikowic (ławnik), Jan Szczurkowic (ławnik), Maciej Konięga (ławnik), Grzegorz Fox (ławnik i asesor), Paweł Szwed [?] (cechmistrz), Bartłomiej Święcicki (cechmistrz), Maciej Różycki (cechmistrz)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Uroczysta ELECTIO z wtorku przed św. Agnieszką 1659 r. (14 I 1659) w domu Ubalda Janaszkowica z ramienia dziedzica Jana z Zamościa i komisarza Krzysztofa Brzostowskiego [Brzozowskiego?]: wybrano rajców Marcina Sitarskiego, Stanisława Nawrockiego (prokonsula), Alberta Kurzącego i Macieja Tharasę; wójta Ubalda Janaszkowica; 7 ławników; asesora do Trybunału Zamoyskiego Grzegorza Foxa oraz 5 cechmistrzów (Macieja Tharasę, Marcina Sitarskiego, Pawła Szweda [?], Bartłomieja Święcickiego, Macieja Różyckiego).",
        "transkrypcja": """--- Skan #50 (fol. 23v) ---
23v ELECTIO 1659
Solemni et Laudabilis Magistratus Civilis Crasn. in Domo Famati
D. Ubaldi Janaszkowic eo tempore Proconsulis Crasn. in patia totius
Magistratus et Communitatis celebrata feria tertia ante Festum S. Agnetis
Virginis et Martyris proxime Anno Dni 1659.
Et in primis ex Brachio Illmi ac Magnifici Dni D. Joannis de Zamoście
Zamoyski Palatini Kijoviensis Dni Haereditarii Clementissimi Generosi ac
Magnificus Dnus Christophorus Brzostowski [Brzozowski?] Pocillator Czernichoviensis...
elegit duos Consules Residentes Famatum D. Martinum Sitarski et Famatum D. Stanislaum Nawrocki...
adsciverunt sibi tertium Famatum D. Albertum Kurzący et quartum Famatum D. Mathiam Tharasa.
In Advocatum vero et Judicem Ordinarium Juratum Crasn.
elegerunt et constituerunt Famatum D. Ubaldum Janaszkowic.
Scabini antiqui: Martinus Skarzyński, Blasius Kołodziejczyk, Augustinus
Kwasowic, Joannes Zdebikowic, Joannes Szczurkowic, Mathias Konięga et Gregorius Fox.
In Assessorem ad Judicia Suprema Tribunalis Zamoscensis Famatum D. Gregorium Fox.
Absoluta itaque Electione Famatus D. Stanislaus Nawrocki Offm Proconsulatus suscepit.
In Archimagistros:
Pellionum: Famatum D. Mathiam Tharasa
Sutorum: Famatum D. Martinum Sitarski
Sartorum: Hon. Paulum Szwed [?]
Fabrum: Hon. Bartholomaeum Święcicki
Textorum: Hon. Mathiam Różycki
elegerunt et constituerunt.""",
        "link_swa": UNIT_LINK
    }
]

main_data.extend(part2_scans)

with open('/home/ubuntu/workspace/Gen/main_data_j19_part2.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j19_part2.json: {len(main_data)} skanów.")
