# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j20_part1.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"

part2_scans = [
    {
        "nr_skanu": 26,
        "numer_pozycji": "26",
        "strona_pagina": "fol. 11r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Gajony / Spór A. Marlika z Z. Zielińską o 200 złp (cz. 1)",
        "osoby_podmioty": "Andrzej Marlik [?], Zofia Zielińska [?], Józef Zieliński, Wojciech Zieliński, Maciej Butek, Błażej Kołodziejczyk (ławnik), Augustyn Kurowic (ławnik)",
        "kwoty_podatki": "200 złp",
        "opis_sprawy": "Sesja Sądu Gajonego (Judicium Expositum Bannitum) z 7 XII 1657 r.: proces Andrzeja Marlika [?] przeciw Zofii Zielińskiej [?] i jej mężowi o 200 złp według zapisu z 1650/1652 r. oraz rozliczenie opieki po nieboszczyku Janie (wzmianki o dekretach z 1656 r. i ławnikach).",
        "transkrypcja": """--- Skan #26 (fol. 11r) ---
11.
Actum Sub Judicio Exposito Banno Advocati et Scabinorum Juratorum
Crasnicensium Celebrato feria 6ta post Festum S. Nicolai Episcopi [1657].
Inter Ingenuum Andream Marlik [?] Actorem ac Honestam Sophiam Zielińska [?]
consortem ejus Citatam.
Urodzony Andrzej Marlik skarży się na pozwaną Zofiją Zielińską...
o dług fl 200 według rejestru... z zapisu nieboszczyka...
Ponieważ Zofija Zielińska na taki wielki termin nie stanęła...
zapisana była przed Sądem w roku 1656... a z opieki Jajczyków
z tych 200 fl... Sąd nakazuje aby na przyszły termin stanęła
z dokumentami. Quod Actis connotatum est.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 27,
        "numer_pozycji": "27",
        "strona_pagina": "fol. 11v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Gajony / Spór A. Marlika z Z. Zielińską o 200 złp (cz. 2)",
        "osoby_podmioty": "Andrzej Marlik [?], Zofia Zielińska [?]",
        "kwoty_podatki": "200 złp",
        "opis_sprawy": "Ciąg dalszy procesu Andrzeja Marlika [?] przeciw Zofii Zielińskiej [?]: odwołanie do zapisu z 1652 r. i dekretów z 1656 r., rozliczenie sumy kapitalnej 200 złp i wydatków sądowych (podpis inicjałowy I.S.).",
        "transkrypcja": """--- Skan #27 (fol. 11v) ---
11v
...zapisu w roku 1652 uczynionego... na sumę fl 200...
gdzie po dekretach w roku 1656... od tego terminu nie stanęła...
a teraz przed Sądem niniejszym... w sumie kapitalnej fl 200
ma złożyć rachunek sprawiedliwy. Quod Decretum ab utraque parte susceptum est.
[podpis:] I. S.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 28,
        "numer_pozycji": "28",
        "strona_pagina": "fol. 12r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Gajony / Dokończenie wpisu Zofii Zielińskiej (karta w większości pusta)",
        "osoby_podmioty": "Zofia Zielińska [?]",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie dwuwierszowego wpisu w sprawie Zofii Zielińskiej [?] ('nie chce się z tych pieniędzy... żadnego...'); pozostała część karty fol. 12r czysta.",
        "transkrypcja": """--- Skan #28 (fol. 12r) ---
12.
...Zofija Zielińska [?]... z tejże sumy nie chce się z tych pieniędzy
rozliczyć przed Sądem ani oddać żadnego...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 29,
        "numer_pozycji": "29",
        "strona_pagina": "fol. 12v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Sprawy J. Zielińskiego (Jajczyk, Zaleska, Bybina)",
        "osoby_podmioty": "Józef Zieliński [?], Sebastian Jajczyk, wdowa po Krzysztofie Zaleskim [Zalasku], wdowa Bybina [?]",
        "kwoty_podatki": "4 fl",
        "opis_sprawy": "Sprawa Józefa Zielińskiego [?] przeciw Sebastianowi Jajczykowi o 4 fl z dekretu z Niedzieli Reminiscere; sprawa tegoż przeciw wdowie po Krzysztofie Zaleskim [Zalasku]; poniżej przysięga Zielińskiego przeciw wdowie Bybinej [?] o beczkę i koło.",
        "transkrypcja": """--- Skan #29 (fol. 12v) ---
12v
Inter Josephum Zieliński [?] Actorem ac Sebestianum Jajczyk Citatum.
Sententia est: aby sumę Pozwany Aktorowi położył... według dekretu
sub Actis feria 2da post Dominicam Reminiscere... fl 4.

Inter eundem Actorem ac Viduam Christophori Zaleski [Zalasek?] Citatam.
Pozwana wdowa Krzysztofowa Zaleska... aby bez opiekuna nie stawała...
Sąd nakazuje aby na przyszły termin z opiekunem stanęła.

Juramentum Zieliński contra Bybina [?].
Wykonana przysięga przez Zielińskiego iż o beczkę y koło po Bybie
nie wziął ani nie zatrzymał. Quod juris solidum est.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 30,
        "numer_pozycji": "30",
        "strona_pagina": "fol. 13r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Spory o konia, dług i żyto (Rogalski, Dzierżek, Kosińska)",
        "osoby_podmioty": "Wojciech Rogalski [?], Piotr Dzierżek [?], Józef [?], Wawrzyniec Świątek [?], Kosińska [?], Szymon Jasielski [?], Augustyn Kurowic",
        "kwoty_podatki": "3 grzywny",
        "opis_sprawy": "Sprawa Wojciecha Rogalskiego [?] przeciw Piotrowi Dzierżkowi [?] o konia i 3 grzywny; sprawa Józefa [?] przeciw Wawrzyńcowi Świątkowi [?] o babkę/młyn; sprawa Kosińskiej [?] przeciw Jasielskiemu [?] o półkorca żyta (wzmianka o Augustynie Kurowicu).",
        "transkrypcja": """--- Skan #30 (fol. 13r) ---
13.
Inter Albertum Rogalski [?] Actorem ac Petrum Dzierżek [?] Citatum.
O konia... y trzy grzywny... Sąd nakazuje aby świadka stawił.

Inter Josephum [?] Actorem ac Laurentium Świątek [?] Citatum.
Skarży się Aktor o babkę... Sąd nakazuje aby dług oddał.

Inter Kosińska [?] Actricem ac Jasielski [?] Citatum.
Według dekretu z Augustynem Kurowicem... o półkorca żyta.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 31,
        "numer_pozycji": "31",
        "strona_pagina": "fol. 13v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Sprawy Pyrka, Koska z Tkarzem i przysięga Sydkowica",
        "osoby_podmioty": "Paweł Pyrek, Szymon Jasielski, Adam Kosek [?], Piotr Tkarz [?], Wawrzyniec Sydkowic",
        "kwoty_podatki": "2 fl 15 gr, 18 gr",
        "opis_sprawy": "Sprawa Pawła Pyrka przeciw Szymonowi Jasielskiemu; sprawa Adama Koska [?] przeciw Piotrowi Tkarzowi [?] o 2 fl 15 gr i 18 gr za konia w Bychawie; poniżej przysięga Wawrzyńca Sydkowica przeciw Szymonowi Jasielskiemu w sprawie kłótni na Brzegu Krakowskim.",
        "transkrypcja": """--- Skan #31 (fol. 13v) ---
13v
Inter Paulum Pyrek Actorem ac Simonem Jasielski Citatum.
Dano dylacyję do blisko przyszłego piątku.

Inter Adamum Kosek [?] Actorem ac Petrum Tkarz [?] Citatum.
Skarży się Aktor o dług fl 2 gr 15 za konia w Bychawie... y gr 18...
Sąd nakazuje aby na przyszły termin zapłacił.

Juramentum Laurentii Sydkowic contra Simonem Jasielski.
Wykonał przysięgę Wawrzyniec Sydkowic przeciwko Szymonowi Jasielskiemu
na Brzegu Krakowskim... Quod Actis connotatum est.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 32,
        "numer_pozycji": "32",
        "strona_pagina": "fol. 14r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Gajony / Otwarcie roku 1658 (Zota vs Sydkowic, Dzierżek, Kaniskowic)",
        "osoby_podmioty": "Piotr Dzierżek [?], Żyd Michał, Jan Kaniskowic [?], Zofia Dzierżkowa [?], Andrzej Zota, Krystyna Zotowa, Wawrzyniec Sydkowic",
        "kwoty_podatki": "20 gr, 6 fl, 2 fl 6 gr",
        "opis_sprawy": "Nagłówek roku 1658 (styl Bożego Narodzenia — 28 XII 1657 r.): kontumacja Piotra Dzierżka [?] na żądanie Żyda Michała o 20 gr; sprawa Jana Kaniskowica [?] przeciw Zofii Dzierżkowej [?] o 6 fl; sprawa Andrzeja Zoty i jego żony Krystyny przeciw Wawrzyńcowi Sydkowicowi o 2 fl 6 gr i przysięgę na krucyfiks.",
        "transkrypcja": """--- Skan #32 (fol. 14r) ---
14. 1658.
Honestus Petrus Dzierżek [?] ex instantia Michaelis Judaei Contumax
iż nie oddał gr 20.

Actum Coram Judicio Exposito Banno Advocati et Scabinorum Juratorum
feria sexta post Festum S. Joannis Evangelistae 1658.
Inter Joannem Kaniskowic [?] Actorem ac Zophiam Dzierżkowa [?] Citatam.
Skarży się Aktor o fl 6 z zapisu... Sąd nakazuje aby na przyszły termin zapłaciła.

Inter Honestum Andream Zota et consortem eius Christinam Actores
ac Honestum Laurentium Sydkowic Citatum.
Skarży się Aktor o dług fl 2 gr 6... y o pobicie... Sąd nakazuje aby
przysiągł na krucyfiks na przyszłym terminie.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 33,
        "numer_pozycji": "33",
        "strona_pagina": "fol. 14v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Wójtowski / Przysięga Z. Dzierżkowej i kupno gruntu przez M. Konięgę",
        "osoby_podmioty": "Andrzej Zota, Wawrzyniec Sydkowic, Zofia Dzierżkowa [?], Maciej Konięga (ławnik), Wawrzyniec Kopczyk [?], Zofia Solarska [?], Wojciech Janaszkowic (wójt), Błażej Kołodziejczyk (ławnik), Stefan Dzierżek [?]",
        "kwoty_podatki": "2 fl [?]",
        "opis_sprawy": "Dokończenie dekretu Andrzeja Zoty z Wawrzyńcem Sydkowicem; przysięga Zofii Dzierżkowej [?] przed Maciejem Konięgą; sprawa Wawrzyńca Kopczyka [?] przeciw wdowie Zofii Solarskiej [?]; poniżej Resignatio Famati Mathiae Konięga cum Sophia Dzierżkowa [?] w domu wójta Wojciecha Janaszkowica (przy ławniku Błażeju Kołodziejczyku) o zakup części gruntu po ojcu Stefanie Dzierżku [?].",
        "transkrypcja": """--- Skan #33 (fol. 14v) ---
14v
...według dekretu... Quod Actis connotatum est.

Juramentum Dnae Sophiae Dzierżkowa [?] coram Famato Mathia Konięga.
Wykonała przysięgę Zofija Dzierżkowa [?] według dekretu...

Inter Laurentium Kopczyk [?] Actorem et Sophiam Viduam Solarska [?] Citatam.
O dług z Lublina fl 2 [?]... Sąd odsyła do rozliczenia.

Resignatio Famati Mathiae Konięga cum Sophia Dzierżkowa [?].
W domu Sławetnego P. Wojciecha Janaszkowica Wójta Kraśnickiego przy obecności
Błażeja Kołodziejczyka Ławnika... Zofija Dzierżkowa [?] sprzedała y zrezygnowała
część gruntu swego po niegdy Stefanie Dzierżku [?] ojcu swoim Sławetnemu
Maciejowi Koniędze Ławnikowi Kraśnickiemu wiecznymi czasy.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 34,
        "numer_pozycji": "34",
        "strona_pagina": "fol. 15r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Podstarościego / Protestacja A. Paździecha przeciw J. Rusarkowi",
        "osoby_podmioty": "Augustyn Paździech [?], Jan Rusarek [Rybak?] (przedmieszczanin), Stanisław Cichoń (pisarz)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Sesja Sądu Podstarościego (Officium Subdelegati) i ławników z 9 IX 1658 r. (poniedziałek po Narodzeniu NMP): protestacja Augustyna Paździecha [?] przeciw przedmieszczaninowi Janowi Rusarkowi [Rybakowi?] o najście ogrodu, wyzwiska ('złodzieju, rozbójniku, szelmo') i zniewagę żony (podpis pisarza Stanisława Cichonia).",
        "transkrypcja": """--- Skan #34 (fol. 15r) ---
15.
Actum Crasnicii Coram Officio Subdelegati et Scabinis Juratis Crasnicensibus
feria secunda post Festum Gloriosae Nativitatis B. M. Virginis proxima
Anno Domini Millesimo Sexcentesimo Quinquagesimo Octavo.
Do Urzędu niniejszego Subdelegackiego y Ławników Przysięgłych Kraśnickich
przyszedłszy oblicznie Sławetny Augustyn Paździech [?] mieszczanin kraśnicki
solenną protestacyję uczynił przeciwko Janowi Rusarkowi [Rybakowi?] przedmieszczaninowi
kraśnickiemu iż on zapomniawszy bojaźni Bożej... przyszedłszy do ogrodu mego
słowami obelżywymi nazywając mnie złodziejem, rozbójnikiem, szelmą...
y przez płot przelazłszy małżonkę moją znieważył... Oświadczam się o to prawnie czynić.
[podpis:] Stanislaus Cichoń Notarius.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 35,
        "numer_pozycji": "35",
        "strona_pagina": "fol. 15v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Podstarościego i Wójtowski / Zeznanie K. Wróbla i spór o wóz z Kazimierza",
        "osoby_podmioty": "Krzysztof Wróbel, Augustyn Paździech [?], Jan Szwed [?] (z Kazimierza), Marcin Pączek [?]",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Zeznanie świadka Krzysztofa Wróbla na prośbę Augustyna Paździecha [?] o kłótni przy moście; poniżej sesja Sądu Wójtowskiego z 30 IX 1658 r. (po św. Michale): sprawa Jana Szweda [?] z Kazimierza przeciw Marcinowi Pączkowi [?] mieszczaninowi kraśnickiemu o wóz i konie.",
        "transkrypcja": """--- Skan #35 (fol. 15v) ---
15v
Sub eodem Actu.
Na żądanie Sławetnego Augustyna Paździecha [?] zapozwany będąc Uczciwy
Krzysztof Wróbel sub juramento corporali zeznał iż będąc przy moście
słyszał jak Jan Rusarek [Rybak?] wyzywał Augustyna Paździecha...

Actum Crasnicii Coram Officio Advocati et Scabinorum Juratorum feria secunda
post Festum S. Michaelis Archangeli 1658.
Inter Joannem Szwed [?] de Kazimierz Actorem ac Martinum Pączek [?] Civem Crasnicensem Citatum.
Skarży się Aktor o wóz y konie zatrzymane... Sąd nakazuje aby się na przyszłym
terminie rozprawili. Quod juris solidum est.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 36,
        "numer_pozycji": "36",
        "strona_pagina": "fol. 16r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Wójtowski / Zapis wyderkafowy 100 złp dla Anny Zielińskiej",
        "osoby_podmioty": "Andrzej Marlik [?], Wojciech Szafraniec, Wojciech Jabłoński, Maciej Konięga (ławnik), Krystyna Konięgowa, Anna Zielińska [Dzierżkowa?]",
        "kwoty_podatki": "30 fl, 3 fl, 100 złp kapitału, 7 złp czynszu rocznego",
        "opis_sprawy": "Dokończenie zapisu o sumach 30 fl i 3 fl (wzmianki o Andrzeju Marliku, Wojciechu Szafrańcu i Wojciechu Jabłońskim); poniżej uroczysty zapis wyderkafowy (obligatio) ławnika Macieja Konięgi i żony Krystyny na rzecz Anny Zielińskiej [Dzierżkowej?] na sumę 100 złp kapitału z rocznym czynszem 7 złp zabezpieczonym na kamienicy przy Rynku między placem Andrzeja Marlika a placem P. Wójta.",
        "transkrypcja": """--- Skan #36 (fol. 16r) ---
16.
...Andrzej Marlik... Wojciech Szafraniec... fl 30... fl 3...
Resignatio super hunc Mensuram... Famatus Mathias Konięga...

Coram eodem Judicio Advocati et Scabinorum Juratorum Crasnicensium
comparens Famatus Mathias Konięga et Christina coniuges Cives Crasnicenses...
recognoverunt se debere Honestae Annae Zielińska [Dzierżkowa?] summam
florenorum centum fl 100 monetae currentis in Regno Poloniae, pro qua summa
obligantur cum suis successoribus solvere annuatim alias wyderkaf florenorum
septem fl 7 in die et festo S. Joannis Baptistae incipiendo a festo anni 1658
super domo lapidea in Circulo inter metas ex una Andream Marlik et ex altera
parte Dni Advocati jacente...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 37,
        "numer_pozycji": "37",
        "strona_pagina": "fol. 16v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Wójtowski / Spór M. Dulskiego z M. Kudrelikiem oraz kradzież w Rynku",
        "osoby_podmioty": "Anna Zielińska [Dzierżkowa?], Marcin Dulski [?], Maciej Kudrelik, Augustyn Kurowic [Krogulec?], Błażej Kozłowski [?]",
        "kwoty_podatki": "7 fl, 15 złp, 30 złp",
        "opis_sprawy": "Dokończenie zapisu wyderkafowego Anny Zielińskiej [Dzierżkowej?]; sesja z 19 X 1658 r. (sobota po św. Łukaszu): przedmieszczanin Marcin Dulski [?] przeciw Maciejowi Kudrelikowi o 15 złp z drogi do Lublina; sesja z 27 X 1658 r.: sprawa Augustyna Kurowica [Krogulca?] z Błażejem Kozłowskim [?] o kradzież 30 złp, płótna, srebrnej łyżki i sztyletu z komory na Rynku.",
        "transkrypcja": """--- Skan #37 (fol. 16v) ---
16v
...pro annuo censu fl 7... Quod ad affectationem Dnae Annae Zielińska
Actis praesentibus insertum est.

Actum Coram Officio Advocati et Scabinorum Juratorum Crasnicensium
Sabbato post Festum S. Lucae [1658].
Martinus Dulski [?] anteoppidanus contra Mathiam Kudrelik anteoppidanum.
Skarży się o 15 fl z drogi do Lublina... Sąd nakazuje aby dług oddał.

Actum Coram Officio Advocati et Scabinorum Juratorum die Dominico
ante Festum SS. Apostolorum Simonis et Judae 1658.
Skarżył się Augustyn Kurowic [Krogulec?] przeciwko Błażejowi Kozłowskiemu [?]
iż z komory na Rynku Kraśnickim ukradziono fl 30, płótno, łyżkę srebrną
y sztylet...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 38,
        "numer_pozycji": "38",
        "strona_pagina": "fol. 17r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Łączony / Sukcesja po Adamie Kępskim [Macieju Karczmarzu]",
        "osoby_podmioty": "Augustyn Kurowic, Adam Wojtek [?], Adam Kępski [?], Maciej Karczmarz [?], Stanisław Sikor (pisarz)",
        "kwoty_podatki": "6 fl",
        "opis_sprawy": "Dokończenie dekretu w sprawie kradzieży na Rynku (chłosta lub 6 fl); poniżej sesja Sądu Łączonego z 28 X 1658 r. (przed św. Szymonem i Judą): spór między Adamem Wojtkiem [?] a sukcesorami po niegdy Adamie Kępskim [?] i Macieju Karczmarzu [?] o podział dóbr i długi zapisane w rejestrach pisarza Stanisława Sikora.",
        "transkrypcja": """--- Skan #38 (fol. 17r) ---
17.
...karać chłostą albo fl 6 do skrzynki... Quod juris solidum est.

Actum Crasnicii Coram Officio Composito Consulari Advocati et Scabinorum
Juratorum Crasnicensium feria secunda ante Festum SS. Apostolorum
Simonis et Judae 1658.
W sprawie między P. Adamem Wojtkiem [?] a sukcesorami niegdy Adama Kępskiego [?]
y Macieja Karczmarza [?]... o successyję dóbr pozostałych po nieboszczyku...
Sąd nakazuje aby według rejestrów P. Stanisława Sikora Pisarza Kraśnickiego
uczynili rozliczenie długów y podział dóbr.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 39,
        "numer_pozycji": "39",
        "strona_pagina": "fol. 17v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Łączony / Sukcesja (dok.) i zeznania dla wdowy Koziarowej",
        "osoby_podmioty": "Adam Kępski [?], wdowa Koziarowa [Koniarzowa?], Marcin Dąbek [?] (wójt przedmiejski), Paweł Klisz [Kłoś?], Grzegorz Fox, Wojciech Janaszkowic",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie dekretu w sprawie sukcesji (apelacja jednej ze stron); poniżej Testimonium parte Viduae Koziarowa [Koniarzowa?]: zeznania wójta przedmiejskiego Marcina Dąbka [?] oraz Pawła Klisza [Kłosia?] z wzmianką o Grzegorzu Foxie i Wojciechu Janaszkowicu.",
        "transkrypcja": """--- Skan #39 (fol. 17v) ---
17v
...do dwóch niedziel pod utraceniem sprawy... od którego dekretu
strona apeluje do sądu wyższego.

Testimonium parte Viduae Koziarowa [Koniarzowa?].
Testis Honestus Martinus Dąbek [?] Scultetus Suburbii sub juramento recognovit
iż z Grzegorzem Foxem... o tej sprawie dobrze wiedział...
Secundus Testis Paulus Klisz [Kłoś?] similiter recognovit ut supra, wspominając
P. Wojciecha Janaszkowica.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 40,
        "numer_pozycji": "40",
        "strona_pagina": "fol. 18r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Podstarościego / Sprawy Żywickiego, Olęckiego i Kudrelika",
        "osoby_podmioty": "Marcin Starzyński (ławnik), Maciej Konięga (ławnik), Tomasz Żywicki [Sniechowski?], Wojciech Olęcki, Stanisław Sołtyszczyk [?], Wojciech Kudrelik, Szymon Jasielski",
        "kwoty_podatki": "40 fl, 2 fl, 80 fl",
        "opis_sprawy": "Sesja Sądu Podstarościego z 28 X 1658 r. w obecności ławników Marcina Starzyńskiego i Macieja Konięgi: Tomasz Żywicki [Sniechowski?] przeciw Wojciechowi Olęckiemu o 40 fl arendy; Wojciech Olęcki przeciw Stanisławowi Sołtyszczykowi [?] o 2 fl za robotę; Wojciech Kudrelik przeciw Szymonowi Jasielskiemu o 80 fl z dekretu z 1658 r.",
        "transkrypcja": """--- Skan #40 (fol. 18r) ---
18.
Actum Coram Officio Subdelegati praesente Famato Martino Starzyński
et Mathia Konięga Scabinis Juratis feria secunda ante Festum SS. Apostolorum
Simonis et Judae 1658.
Inter Dnum Thomam Żywicki [Sniechowski?] Actorem ac Albertum Olęcki Citatum.
O dług fl 40 z arendy... Sąd nakazuje aby na św. Marcin zapłacił.

Inter Albertum Olęcki Actorem ac Stanislaum Sołtyszczyk [?] Citatum.
O dług fl 2 za robotę... Sąd nakazuje zapłatę.

Inter Albertum Kudrelik Actorem ac Simonem Jasielski Citatum.
Inhaerendo Decreto sub Actis post Festum S. Mathiae 1658... o sumę fl 80
kapitału. Quod Decretum ab utraque parte susceptum est.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 41,
        "numer_pozycji": "41",
        "strona_pagina": "fol. 18v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Gajony / Rejestr spraw 28 X 1658, Zofia Somkowa i przysięga Sydkowica",
        "osoby_podmioty": "Krystyna Sitarska, Wawrzyniec Sydkowic, Błażej Grygiel, Szymon Łycek, Tomasz Dąbek, Majewski, Dzierżek, Zofia Somkowa, Żyd Zelig, Augustyn Paździech [?], Andrzej Zota",
        "kwoty_podatki": "2 fl",
        "opis_sprawy": "Manifestacja Krystyny Sitarskiej przeciw Wawrzyńcowi Sydkowicowi o potwarz; sesja Sądu Gajonego z 28 X 1658 r. (w święto Szymona i Judy): wywołanie spraw (Błażej Grygiel, Szymon Łycek, Tomasz Dąbek, Majewski, Dzierżek, Zofia Somkowa vs Żyd Zelig o 2 fl); zeznanie Augustyna Paździecha [?] dla Wawrzyńca Sydkowica i jego przysięga przeciw Andrzejowi Zocie.",
        "transkrypcja": """--- Skan #41 (fol. 18v) ---
18v
Christina Sitarska Manifestatur contra Laurentium Sydkowic.
Uczciwa Krystyna Sitarska oświadcza się przeciwko Wawrzyńcowi Sydkowicowi
o niesłuszne słowa i potwarz...

Actum Sub Judicio Banno Advocati et Scabinorum Juratorum in Festo
SS. Apostolorum Simonis et Judae 1658.
Błażej Grygiel... Szymon Łycek z Tomaszem Dąbkiem... Majewski z Dzierżkiem...
Zofija Somkowa ex instantia perfidi Judaei Zelig Contumax o fl 2.

Testimonium pro parte Laurentii Sydkowic.
Testis Augustinus Paździech [?] sub juramento recognovit o kłótni z Zotą.

Juramentum Laurentii Sydkowic contra Andream Zota.
Wykonał przysięgę na krucyfiks Wawrzyniec Sydkowic przeciwko Andrzejowi Zocie.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 42,
        "numer_pozycji": "42",
        "strona_pagina": "fol. 19r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Wójtowski / Spór Konińskiego z Bożęborskim i świadectwa ze Ślinowa",
        "osoby_podmioty": "Wawrzyniec Sydkowic, Andrzej Zota, Andrzej Koniński [Komiński?], Bartłomiej Bożęborski [Świderski?], Bartosz Kępa, Wojciech Rzepka [Rzytka?] (ze Ślinowa), Jan Moskwa [Słotwa?] (ze Ślinowa), Jakub Zajączek [?], Jadwiga",
        "kwoty_podatki": "2 fl",
        "opis_sprawy": "Dokończenie przysięgi W. Sydkowica (2 fl); sprawa Andrzeja Konińskiego [Komińskiego?] przeciw Bartłomiejowi Bożęborskiemu [Świderskiemu?] (wzmianka o Bartoszu Kępie); poniżej początek zeznań ze wsi Ślinów [Słodków?] (Testimonium parte Laboriosi Alberti Rzepka [Rzytka?] de Ślinów): zeznanie Jana Moskwy [Słotwy?] o Jakubie Zajączku [?] i Jadwidze.",
        "transkrypcja": """--- Skan #42 (fol. 19r) ---
19.
...odłożywszy te fl 2 do Sądu... Quod Actis connotatum est.

Inter Honestum Andream Koniński [Komiński?] Actorem ac Dnum Bartholomaeum Bożęborski [Świderski?] Citatum.
Skarży się Aktor o dług z zapisu... od Bartosza Kępy... Sąd nakazuje
aby się na terminie rozliczyli.

Testimonium parte Laboriosi Alberti Rzepka [Rzytka?] de Ślinów [Słodków?].
Testis Laboriosus Joannes Moskwa [Słotwa?] de Villa Ślinów sub juramento recognovit
iż wiedział o Wojciechu Rzepce, Jakubie Zajączku [?] y Jadwidze...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 43,
        "numer_pozycji": "43",
        "strona_pagina": "fol. 19v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Gajony / Zeznania ze Ślinowa i manifestacja W. Olęckiego",
        "osoby_podmioty": "Janek Brożek [?] (ze Ślinowa), Paweł Reszka (ze Ślinowa), Andrzej Gąska (ze Ślinowa), Wojciech Rzepka [Rzytka?], Jakub Zajączek [?], Wojciech Olęcki, Bartłomiej Bożęborski [?], Wojciech Zając [Gros?], Maciej Łycek [?], Katarzyna Sosnowska [?], Wojciech Szafraniec, Maciej Konięga, Grzegorz Fox",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie zeznań poddanych ze wsi Ślinów [Słodków?] (Janek Brożek [?], Paweł Reszka, Andrzej Gąska w sprawie Jakuba Zajączka [?] i Wojciecha Rzepki [Rzytki?]); manifestacja Wojciecha Olęckiego przeciw P. Bożęborskiemu [?]; sesja Sądu Gajonego z 30 X 1658 r. (przed Wszystkimi Świętymi) przed Wojciechem Szafrańcem, Maciejem Konięgą i Grzegorzem Foxem: sprawa Wojciecha Zająca [Gros?] przeciw Maciejowi Łyckowi [?] i Katarzynie Sosnowskiej [?] ze Ślinowa.",
        "transkrypcja": """--- Skan #43 (fol. 19v) ---
19v
...Testis Laboriosus Janek Brożek [?] de Villa Ślinów recognovit ut supra...
Tertius Testis Paulus Reszka de Ślinów... Quartus Testis Andreas Gąska de eadem Villa Ślinów
similiter recognoverunt o Jakubie Zajączku [?] y Wojciechu Rzepce [Rzytce?].

Manifestatio Dni Alberti Olęcki contra Dnum Bożęborski [?].
Oświadcza się Wojciech Olęcki przeciwko P. Bożęborskiemu [?]...

Actum Coram Judicio Exposito Banno Advocati et Scabinorum Juratorum
feria quarta ante Festum SS. Omnium 1658
praesentibus Dno Alberto Szafraniec, Mathia Konięga et Gregorio Fox.
Inter Laboriosum Albertum Zając [Gros?] Actorem ac Laboriosum Mathiam Łycek [?]
et Catherinam Sosnowska [?] de Ślinów Citatos.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 44,
        "numer_pozycji": "44",
        "strona_pagina": "fol. 20r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Wójtowski / Kontumacja Żyda Kopla i spór Foxa oraz Kurowica",
        "osoby_podmioty": "Wojciech Butek, Jakub Zdebik, Żyd Hersz [Herszek] Kopel, Grzegorz Fox, Augustyn Kurowic, Szymon Pyrek [?], Katarzyna Łycka [?], Andrzej Zota, Wawrzyniec Sydkowic",
        "kwoty_podatki": "2 fl",
        "opis_sprawy": "Kontumacja Wojciecha Butka i Jakuba Zdebika na żądanie Żyda Herszka Kopla; proces Grzegorza Foxa i Augustyna Kurowica przeciw Szymonowi Pyrkowi [?] i Katarzynie Łyckiej [?] (odwołanie do Sądu Łączonego z 1657 r.); sprawa Andrzeja Zoty przeciw Wawrzyńcowi Sydkowicowi o 2 fl i wykonanie przysięgi.",
        "transkrypcja": """--- Skan #44 (fol. 20r) ---
20.
Albertus Butek et Jacobus Zdebik ex instantia perfidi Judaei Hersz Kopel
contumaces pronuntiati sunt.

Inter Famatum Gregorium Fox et exploratorem eius Augustinum Kurowic Actores
ac Szymonka [Szymona Pyrka?] et Catherinam Łycka [?] Cives Crasnicenses Citatos.
Skarżą się Aktorowie o rozliczenie dóbr według dekretu Sądu Łączonego z 1657 r...

Inter Honestum Andream Zota Actorem ac Laurentium Sydkowic Citatum.
O dług fl 2... Sąd nakazuje wykonanie przysięgi według prawa.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 45,
        "numer_pozycji": "45",
        "strona_pagina": "fol. 20v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Wójtowski / Spór o kradzież jabłek z sadu ławnika Augustyna Kurowica",
        "osoby_podmioty": "Wojciech Butek, Bartłomiej Bożęborski [?], Jan Koniński [Komiński?], Wojciech Olęcki, Augustyn Kurowic (ławnik), Koniarska [?] (Marina?), Anna (żona/córka), Alberta [?]",
        "kwoty_podatki": "20 fl, 2 grzywny, 30 fl [?]",
        "opis_sprawy": "Sprawa Wojciecha Butka przeciw P. Bożęborskiemu [?] o 20 fl; sprawa Jana Konińskiego [Komińskiego?] przeciw Wojciechowi Olęckiemu o 2 grzywny; poniżej obszerna skarga ławnika Augustyna Kurowica przeciw Koniarskiej [?], Annie i Albercie [?] o kradzież jabłek z sadu i obelgi.",
        "transkrypcja": """--- Skan #45 (fol. 20v) ---
20v
Inter Albertum Butek Actorem ac Dnum Bożęborski [?] Citatum.
O dług fl 20... Sąd nakazuje aby na przyszły termin zapłacił.

Honestus Joannes Koniński [Komiński?] cum Alberto Olęcki... o dwie grzywny.

Inter Famatum Augustinum Kurowic Scabinum Juratum Actorem ac Honestam
Koniarska [?] et consortem eius Annam et filiam eius Albertam [?] Citatas.
Skarży się Aktor iż one do sadu jego zakradłszy się jabłka ukradły,
w sadzie były y słowami obelżywymi go zelżyły... Sąd nakazuje aby
świadkowie na przyszły piątek stanęli pod karą.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 46,
        "numer_pozycji": "46",
        "strona_pagina": "fol. 21r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Wójtowski / Zeznania ze wsi Ślinów dla Katarzyny Sosnowskiej (cz. 1)",
        "osoby_podmioty": "Augustyn Kurowic, Koniarska [?], Katarzyna Sosnowska [Łaśniewska?] (ze Ślinowa), Kacper Rzepka [?] (ze Ślinowa), Jan Karpiński [?] (ze Ślinowa), Stefan Kondlik [Kudrelik?], Jan Kurowski",
        "kwoty_podatki": "4 fl, 12 fl",
        "opis_sprawy": "Dokończenie sprawy Augustyna Kurowica (4 fl winy); poniżej sesja z 4 XI 1658 r. (przed św. Marcinem): zeznanie poddanych ze wsi Ślinów [Słodków?] (Kacper Rzepka [?] oraz Jan Karpiński [?]) na prośbę Katarzyny Sosnowskiej [Łaśniewskiej?] w sprawie Stefana Kondlika [Kudrelika?] i Jana Kurowskiego o 12 fl.",
        "transkrypcja": """--- Skan #46 (fol. 21r) ---
21.
...winy fl 4... Quod Actis connotatum est.

Actum Coram Officio Advocati et Scabinorum Juratorum feria secunda
ante Festum S. Martini Episcopi 1658.
Testimonium pro parte Laboriosae Catherinae Sosnowska [Łaśniewska?] de Ślinów.
Testis Laboriosus Kacper Rzepka [?] de Villa Ślinów sub juramento recognovit:
iż będąc przy Janie Kurowskim y Stefanie Kondliku [Kudreliku?] słyszał o długu
fl 12 y wozie...
Secundus Testis Joannes Karpiński [?] subditus de Villa Ślinów similiter recognovit ut supra.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 47,
        "numer_pozycji": "47",
        "strona_pagina": "fol. 21v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Wójtowski / Zeznania ze wsi Ślinów (cz. 2: Stefan Kondlik)",
        "osoby_podmioty": "Jan Karpiński [?], Stefan Kondlik [Kudrelik?] (ze Ślinowa), Tomasz Rzytka [Rzepka?] (śp.), Andrzej Kondlik [Kudrelik?]",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie zeznań Jana Karpińskiego [?] oraz obszerne zeznanie trzeciego świadka — Stefana Kondlika [Kudrelika?] ze wsi Ślinów [Słodków?] — o testamencie śp. Tomasza Rzytki [Rzepki?], rejestrze długów i rozliczeniach z Andrzejem Kondlikiem [Kudrelikiem?].",
        "transkrypcja": """--- Skan #47 (fol. 21v) ---
21v
...zeznaje drugi świadek Jan Karpiński...
Tertius Testis Stephanus Kondlik [Kudrelik?] de eadem Villa Ślinów sub juramento
erectis ad sydera duobus digitis recognovit:
iż po śmierci nieboszczyka Tomasza Rzytki [Rzepki?] przed śmiercią spisany
był rejestr ręką Jana Karpińskiego... y Andrzej Kondlik [Kudrelik?] zeznał
jako długi z tego rejestru należą...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 48,
        "numer_pozycji": "48",
        "strona_pagina": "fol. 22r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Wójtowski / Zeznania ze Ślinowa (cz. 3: Jan Sobek — 330 złp) i areszt Krawca",
        "osoby_podmioty": "Stefan Kondlik [Kudrelik?], Jan Sobek (ze Ślinowa), pan Sikor [?], Wojciech Kondlik alias Cichowicz, Jędrzej Krawiec, Augustyn Kurowic, Wojciech Szafraniec",
        "kwoty_podatki": "30 fl, 330 fl",
        "opis_sprawy": "Dokończenie zeznania Stefana Kondlika (30 fl długu); czwarty świadek Jan Sobek ze wsi Ślinów (wspomina nieboszczyka pana Sikora [?], Wojciecha Kondlika alias Cichowicza i 330 fl gotowych pieniędzy); na dole sesja Sądu Podstarościego z 6 XI 1658 r.: areszt Jędrzeja Krawca w sprawie P. Kurowica i P. Szafrankowica.",
        "transkrypcja": """--- Skan #48 (fol. 22r) ---
22.
...długu fl 30 z tego rejestru...
Quartus Testis Joannes Sobek de Villa Ślinów sub juramento corporali recognovit:
Nieboszczyk pan Sikor... gdy przyszedł Wojciech Kondlik alias Cichowicz
ze Ślinowa... opowiadając że mu fl 330 gotowych pieniędzy zginęło...

Actum Coram Officio Advocati Subdelegati feria quarta ante Festum S. Martini 1658.
Arestum Jędrzeja Krawca... w sprawie P. Kurowica y P. Szafrankowica.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 49,
        "numer_pozycji": "49",
        "strona_pagina": "fol. 22v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Gajony / Wyroki wójta W. Szafrankowica (Zota, Skrobczyk vs Sosnowska)",
        "osoby_podmioty": "Wojciech Szafraniec [Szafrankowic] (wójt), Maciej Konięga (ławnik), Błażej Kołodziejczyk (ławnik), Grzegorz Fox (ławnik), Andrzej Zota, Tomasz Zielik [?], Jałowiecki [?], Wojciech Skrobczyk [Skrobek?], Jadwiga Skrobczykowa, Wojciech (pasierb), Katarzyna Sosnowska, Maciej Łysak, Jan Pętak [?] (woźny)",
        "kwoty_podatki": "5 fl",
        "opis_sprawy": "Sesja Sądu Gajonego z 8 XI 1658 r. pod przewodnictwem wójta Wojciecha Szafrankowica i ławników Macieja Konięgi, Błażeja Kołodziejczyka oraz Grzegorza Foxa: Andrzej Zota przeciw Tomaszowi Zielikowi [?] o 5 fl z zapisu Jałowieckiego [?]; sprawa poddanych ze Ślinowa — Wojciecha Skrobczyka [Skrobka?], żony Jadwigi i pasierba Wojciecha przeciw Katarzynie Sosnowskiej i Maciejowi Łysakowi; relacja woźnego Jana Pętaka [?].",
        "transkrypcja": """--- Skan #49 (fol. 22v) ---
22v
Judicium Expositum Bannitum per Famatum D. Albertum Szafrankowic Advocatum
et Judicem Ordinarium... et Famatis DD. Mathia Konięga, Blasio Kołodziejczyk
et Gregorio Fox Scabinis Juratis celebratum feria sexta ante Festum S. Martini Episcopi 1658.
Inter Honestum Andream Zota Actorem ac Thomam Zielik [?] Citatum.
O dług fl 5 z zapisu Jałowieckiego [?]... Sąd nakazuje aby zapłacił.

Inter Laboriosos Albertum Skrobczyk [Skrobek?] et consortem eius Hedvigim ac Privignum
eius Albertum Actores ac Laboriosos Catherinam Sosnowska et Mathiam Łysak coniuges
subditos de eadem Villa [Ślinów] Citatos.

Relatio Cechi... Jan Pętak [?] Bedellus Juratus...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 50,
        "numer_pozycji": "50",
        "strona_pagina": "fol. 23r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1658",
        "kategoria": "Sąd Gajony / Zeznanie Łukasza Katonia ze Ślinowa i sprawa Koniarskiej",
        "osoby_podmioty": "Łukasz Katoń [Kaczor?] (ze Ślinowa), pan Pełczyński [?], Augustyn Kurowic, Marina Koniarska [?] (wdowa), Wojciech Koniarski",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Zeznanie świadka Łukasza Katonia [Kaczora?] ze wsi Ślinów (wzmianka o płótnie i panu Pełczyńskim [?]); poniżej sprawa ławnika Augustyna Kurowica przeciw wdowie Marinie Koniarskiej [?] i jej synowi Wojciechowi o rozliczenie i odroczenie przysięgi.",
        "transkrypcja": """--- Skan #50 (fol. 23r) ---
23. 1658.
Replika...
Testis Laboriosus Łukasz Katoń [Kaczor?] de eadem Villa Ślinów sub juramento
recognovit iż o płótnie u nieboszczyka y pana Pełczyńskiego [?]...

Inter Augustinum Kurowic Actorem ac Viduam Marinam Koniarska [?]
et filium eius Albertum Citatos.
Stając oblicznie wdowa Marina Koniarska z synem swoim Wojciechem
przed Sądem niniejszym... w sprawie przysięgi z Augustynem Kurowicem...
dano dylacyję do przyszłego terminu.""",
        "link_swa": UNIT_LINK
    }
]

existing_nums = {r['nr_skanu'] for r in main_data}
for s in part2_scans:
    if s['nr_skanu'] not in existing_nums:
        main_data.append(s)

main_data.sort(key=lambda x: x['nr_skanu'])

with open('/home/ubuntu/workspace/Gen/main_data_j20_part2.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j20_part2.json: {len(main_data)} rekordów.")
