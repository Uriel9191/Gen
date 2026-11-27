# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j19_part4.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989899"

part5_scans = [
    {
        "nr_skanu": 101,
        "numer_pozycji": "101",
        "strona_pagina": "fol. 48v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Spór M. Sitarskiego z opiekunami Kłopotem i Reszką (rozgraniczenie roli)",
        "osoby_podmioty": "Marcin Sitarski (rajca), Maciej Reszka (opiekun), Gabriel Kłopot (opiekun), Maciej Konięga (rajca), Maciej Tharasa (rajca), Wojciech Kurowic (burmistrz), Jan Łukasik [?] (sąsiad)",
        "kwoty_podatki": "50 złp kapitału, 20 złp interesu",
        "opis_sprawy": "Sesja z 10 II 1661 r.: ciąg dalszy sporu rajcy Marcina Sitarskiego z opiekunami Maciejem Reszką i Gabrielem Kłopotem o 50 złp kapitału i 20 złp procentu na roli Decowskiej; poniżej sesja z 23 II 1661 r. (wigilia św. Macieja): relacja rajców Macieja Konięgi i Macieja Tharasy z rozgraniczenia roli Decowskiej na Górach Podleskich przez burmistrza Wojciecha Kurowica.",
        "transkrypcja": """--- Skan #101 (fol. 48v) ---
48v 1661
Inter Famatum Martinum Sitarski Consulem Crasnicensem Actorem
ac Honestos Mathiam Reszka et Gabrielem Kłopot Tutores bonorum
Decretalium anteoppidanos Crasnicenses Citatos.
Iż Pozwani Opiekunowie jako na przeszłych terminach tak y na dzisiejszym
terminie stając wymawiają się y pokazują Regestr rachunku anni 1658 sub
Actis feria 6ta post Festum Circumcisionis Christi Domini ad instantiam Actoris...
Urząd niniejszy Radziecki Kraśnicki nakazuje aby Citati feria 6ta proxima Decretum
wypłacili... tak w Summie Capitali fl 50 jako y interesie fl 20...
Quod Decretum ab utraque parte susceptum est.

Actum Coram Officio Consulari feria quinta in Vigilia Festi S. Mathiae Apostoli proxima Anno Dni 1661.
Przed Urzędem y Aktami niniejszymi Radzieckimi Kraśnickimi stanąwszy
oblicznie Sławetni Panowie Maciej Konięga y Mathias Tharasa Rajce Kraśniccy
wnoszą prawdziwą relacyję swojej że gdy z rozkazania Sławetnego
Pana Wojciecha Kurowica Burmistrza natenczas Rezydującego Kraśnickiego
byli zesłani y deputowani na pokazanie y rozgraniczenie roli Decowskiej
leżącej na Górach Podleskich między miedzami... z jednej strony Jana Łukasika [?]
a z drugiej strony uczciwego Gabriela Kłopota przedmieszczanina kraśnickiego
Sławetnemu P. Marcinowi Sitarskiemu Rajcy Kraśnickiemu z Dekretu Urzędu...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 102,
        "numer_pozycji": "102",
        "strona_pagina": "fol. 49r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Intromisja M. Sitarskiego na przedmieściu Piasek",
        "osoby_podmioty": "Marcin Sitarski (rajca), Maciej Reszka, Gabriel Kłopot, Maciej Konięga (rajca), Maciej Tharasa (rajca), Wojciech Żartowski [Zętkowic?]",
        "kwoty_podatki": "50 złp kapitału, 20 złp interesu, 50 fl (zapis na gruncie)",
        "opis_sprawy": "Dokończenie relacji M. Reszki i G. Kłopota dla M. Sitarskiego (50 złp kapitału i 20 złp procentu); poniżej: Intromissio na ćwierć roli Rutkowskiej [?] na przedmieściu Piasek (między gruntami Sadkowskimi) w sumie 50 fl dla rajcy Marcina Sitarskiego przez rajców Macieja Konięgę i Macieja Tharasę; na dole sprawa M. Sitarskiego przeciw Wojciechowi Żartowskiemu [Zętkowicowi?] o 50 fl.",
        "transkrypcja": """--- Skan #102 (fol. 49r) ---
49. 1661
...Radzieckiego sub Actis feria quinta ante Festum S. Valentini 1661...
byli także relacyją czynili że Maciej Reszka y Gabriel Kłopot opiekunowie
dóbr Decowskich dali y puścili rolę używaną według opisu...
do odebrania Summy Capitalis fl 50 y interesu fl 20...
Quae quidem Intromissio ad affectationem supradicti Famati Martini Sitarski Actis
praesentibus inserta et connotata est.

Eidem Famato Martino Sitarski Consuli Crasnicensi Intromissio datur in bona Rutkowskiego [?].
Auctoritate Officii et Vigore Juris data et assignata est realis et actualis
Intromissio cum pacifica possessione et libero usufructu in quartam Agri dicta
Rutkowskie [?] jacentem in Suburbio dicto Piasek inter metas ex una Sadkowskie...
in summa florenorum quinquaginta certi et liquidi debiti, absque tamen interesse...
per Famatum Mathiam Konięga et Mathiam Tharasa Consules Crasnicenses...

Inter eundem Famatum Martinum Sitarski Consulem Crasnicensem Tutorem bonorum Sołtyszowski [?] Actorem
ac Albertum Żartowski [Zętkowic?] Citatum.
O dług fl 50... Urząd niniejszy Radziecki Kraśnicki nakazuje aby sąsiedzi...
wyszli y wydzielili sztukę roli... odpowiadającej sumie fl 50.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 103,
        "numer_pozycji": "103",
        "strona_pagina": "fol. 49v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Łączony / Spór K. Łopkowskiego [Bystrowskiego] z M. Sitarskim o 150 złp",
        "osoby_podmioty": "Kazimierz Łopkowski [Bystrowski?], Marcin Sitarski (rajca), Wojciech Budek [Bucki?]",
        "kwoty_podatki": "150 złp",
        "opis_sprawy": "Dokończenie dekretu Marcina Sitarskiego; poniżej sesja Sądu Łączonego z 26 II 1661 r.: sprawa Kazimierza Łopkowskiego [Bystrowskiego?] przeciw rajcy Marcinowi Sitarskiemu o 150 złp wraz z procentami (z odwołaniem do dekretu przed św. Katarzyną 1660 r. i wzmianką o Wojciechu Budku [Buckim?]).",
        "transkrypcja": """--- Skan #103 (fol. 49v) ---
49v 1661
...do S. Szymona y Judy... Quod Actis connotatum est.

Actum Coram Officio Composito Consulari Advocati et Scabinorum Juratorum
Crasnicensium Sabbato post Festum S. Mathiae Apostoli proximo Anno Dni 1661.
Inter Honestum Casimirum Łopkowski [Bystrowski?] Actorem ac Famatum Martinum Sitarski Consulem Crasnicensem Citatum.
Uczciwy Kazimierz Łopkowski [Bystrowski?] starosta [?] dziedzic przypozwał Sławetnego
Marcina Sitarskiego Rajcę Kraśnickiego, skarżył się na niego że mu według dekretu
który mu ten rzetelnie otrzymał... oddać nie chce...
o summę fl 150 wespół z interesem...
Decretum:
Judicium praesens Compositum Consularis Advocati Scabinorumque Juratorum Crasnicensium
Inhaerendo priori Decreto Coram Officio Composito Consulari Advocati et Scabinorum Juratorum
Crasnicensium sub Actis feria 2da ante Festum S. Catharinae Virginis et Martyris
Anno 1660... nakazuje Pozwanemu aby dług powyżej mianowany...
w dekrecie pierwszym specyfikowany do rąk Aktora ad occasum solis oddał...
z zapisu od Wojciecha Budka [Buckiego?]...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 104,
        "numer_pozycji": "104",
        "strona_pagina": "fol. 50r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Łączony i Radziecki / Odrzucenie apelacji i submisja M. Sitarskiego",
        "osoby_podmioty": "Kazimierz Łopkowski [Bystrowski?], Marcin Sitarski (rajca)",
        "kwoty_podatki": "50 złp, 15 złp procentu",
        "opis_sprawy": "Dokończenie dekretu Kazimierza Łopkowskiego [Bystrowskiego?] przeciw Marcinowi Sitarskiemu (odrzucenie apelacji Sitarskiego do Trybunału Koronnego Lubelskiego); poniżej sesja z 28 II 1661 r.: Submissio Famati Martini Sitarski — rajca Marcin Sitarski uznaje dług i poddaje się zapłacić Kazimierzowi Łopkowskiemu [Bystrowskiemu?] 50 złp z procentem bez dalszych apelacji.",
        "transkrypcja": """--- Skan #104 (fol. 50r) ---
50. 1661
...od sumy złotych pięćdziesiąt po złotych piętnaście na każdy rok...
a w tym długu i interesie niema żadnej zwłoki...
Od którego dekretu Pozwany Marcin Sitarski chciał apelować do Trybunału
Koronnego Lubelskiego, lecz Sąd Łączony apelacyi nie dopuścił,
gdyż po submisyi apelacyja nie idzie... Quod Actis hisce connotatum est.

Actum Coram Officio Consulari feria secunda ante Dominicam Cinerum proxima 1661.
Submissio Famati Martini Sitarski.
Przed zupełnym Radzieckim Urzędem Kraśnickim stojący oblicznie
Sławetny Marcin Sitarski Rajca Kraśnicki... submittował się dobrowolnie
Uczciwemu Kazimierzowi Łopkowskiemu [Bystrowskiemu?] oddać długu fl 50
wespół z interesem... bez żadnej dalszej zwłoki.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 105,
        "numer_pozycji": "105",
        "strona_pagina": "fol. 50v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Opieka nad małoletnimi Jasińskimi (Piotrowczyk i Grudzień)",
        "osoby_podmioty": "Marcin Sitarski, Sebastian Jasiński (opiekun), Jan Kulka (opiekun), Jan Jasiński [Jasieniec] (śp.), Adam Piotrowczyk (przedmieszczanin), Bartłomiej Grudzień [?]",
        "kwoty_podatki": "8 złp (arenda z chałupy)",
        "opis_sprawy": "Dokończenie submisji M. Sitarskiego; sesja z 8 III 1661 r. (przed św. Grzegorzem): opiekunowie małoletnich po śp. Janie Jasińskim [Jasieńcu] — Sebastian Jasiński i Jan Kulka — przeciw przedmieszczaninowi Adamowi Piotrowczykowi o dług i czynsz ojcowski; poniżej sprawa tychże opiekunów przeciw Bartłomiejowi Grudniowi [?] o 8 złp arendy z chałupy po śp. Janie Jasińskim.",
        "transkrypcja": """--- Skan #105 (fol. 50v) ---
50v 1661
...bez wszelakich dalszych wymówek y trudności... Quod Actis connotatum est.

Actum Coram Officio Consulari feria tertia ante Festum S. Gregorii Papae proxima Anno Dni 1661.
Inter Honestos Sebastianum Jasiński et Joannem Kulka Tutores bonorum
minorum Joannis Jasieniec [Jasińskiego] anteoppidani Crasnicensis Actores
ac Honestum Adamum Piotrowczyk anteoppidanum Crasnicensem Citatum.
Skarżyli się Aktorowie jako Opiekunowie sieroty małoletniego Jana Jasieńca
na Pozwanego Adama Piotrowczyka o dług... według zapisu ojcowskiego...
Sąd nakazuje aby na przyszłą sobotę rachunek uczynili y dług oddali.

Inter eosdem Actores ac Honestum Bartholomaeum Grudzień [?] Citatum.
Skarżyli się Aktorowie na Pozwanego o dług fl 8 winny arendy z chałupy
niegdy Jana Jasińskiego, wzięty na przyszły rok...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 106,
        "numer_pozycji": "106",
        "strona_pagina": "fol. 51r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Przysięga S. Jasińskiego i umowa małżeńska Wojtorkowica z Grzymuszką",
        "osoby_podmioty": "Sebastian Jasiński, Jan Kulka, Bartłomiej Grudzień [?], Sebestjan Wojtorkowic [?], Jan Grzymuszka (przedmieszczanin), Zofia (córka Wojtorkowica), Wojciech Kozakowicz alias Rogalowski (śp.)",
        "kwoty_podatki": "8 złp (arenda)",
        "opis_sprawy": "Dokończenie sprawy opiekunów przeciw Bartłomiejowi Grudniowi [?] (nakaz przysięgi Sebastiana Jasińskiego na 8 złp arendy); poniżej: ugoda przed Urzędem Radzieckim między Sebestjanem Wojtorkowicem [?] a przedmieszczaninem Janem Grzymuszką w sprawie posagu i działów po śp. Wojciechu Kozakowiczu alias Rogalowskim (mężu córki Zofii).",
        "transkrypcja": """--- Skan #106 (fol. 51r) ---
51. 1661
...wziął na wychowanie dziecięcia...
Judicium praesens decernit: Ponieważ Aktorowie zeznają że Pozwany nie płacił
arendy... tedy Sebastian Jasiński ma wykonać przysięgę na 8 fl arendy
w sobotę blisko przyszłą. Quod Decretum ab utraque parte susceptum est.

Sebestianus Wojtorkowic [?] cum Joanne Grzymuszka.
Przed Urzędem y Aktami niniejszymi Radzieckimi Kraśnickimi stanąwszy
oblicznie Uczciwy Sebestjan Wojtorkowic [?] z jednej, a Uczciwy Jan Grzymuszka
przedmieszczanin kraśnicki z drugiej strony... oświadczają się o posag
córki swej Zofii, która była za Wojciechem Kozakowiczem alias Rogalowskim
na gruncie leżącym... aby między nimi zgoda była względem działów...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 107,
        "numer_pozycji": "107",
        "strona_pagina": "fol. 51v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Wielki proces o opiekę: Stanisław Pyrek vs Szymon Pyrek ślusarz",
        "osoby_podmioty": "Sebestjan Wojtorkowic [?], Jan Grzymuszka, szl. Stanisław Pyrek (brat/synowiec), Tomasz Pyrek (śp.), Szymon Pyrek (ślusarz i opiekun), Dubik (wójt kraśnicki)",
        "kwoty_podatki": "400 złp (sad), 60 złp (ogród), 80 złp (drugi ogród za furtką), 40 złp (gotówka od Dubika)",
        "opis_sprawy": "Dokończenie zgody Sebestjana Wojtorkowica [?] i Jana Grzymuszki; poniżej obszerny pozew urodzonego Stanisława Pyrka (po śp. Tomaszu Pyrku mieszczaninie kraśnickim) przeciw opiekunowi Szymonowi Pyrkowi ślusarzowi o 10 lat bezprawnego użytkowania dóbr sierocych (sad na 400 złp, ogród na 60 złp, drugi ogród za furtką na 80 złp oraz 40 złp gotówki pobranej od wójta Dubika).",
        "transkrypcja": """--- Skan #107 (fol. 51v) ---
51v 1661
...sprawiedliwie działają, przeto zgoda między nimi stanęła...
Judicium praesens Consulare nakazuje aby Jan Grzymuszka y Sebestjan
Wojtorkowic [?] zachowali sobie na wieczne czasy działy tych gruntów.
Quod ab utraque parte susceptum est.

Inter Ingenuum Stanislaum Pyrek Actorem ac Honestum Simonem Pyrek senfabrem Citatum.
Urodzony Stanisław Pyrek... po śmierci niegdy Tomasza Pyrka mieszczanina
kraśnickiego takową skargę przed Urzędem Radzieckim podał na Szymona Pyrka
ślusarza opiekuna swego: iż on przez lat dziesięć opiekunem dóbr moich
będąc zażywał dóbr moich: naprzód sadu z którego na każdy rok przedawał
po złotych czterdzieści co czyni za lat dziesięć fl 400; do tego ogrodu
z którego na każdy rok brał po złotych sześć co czyni fl 60; drugi ogród
za furtką z którego brał na każdy rok po złotych ośm co czyni fl 80;
od Dubika wójta z Kraśnika gotowych pieniędzy fl 40 zabrał...
żądając rachunku z opieki y oddania rejestrów przed sądem.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 108,
        "numer_pozycji": "108",
        "strona_pagina": "fol. 52r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Kalkulacja Pyrków, dług Cząstkowicowej i wizja dóbr Łęckowica",
        "osoby_podmioty": "Stanisław Pyrek, Szymon Pyrek (ślusarz), Marina Cząstkowicowa [Czastkowicowa?], Mateusz (śp. mąż), Jan Łyczek [Łyczko?] (z Borowa), Stanisław Łęckowic [Lęckowic?]",
        "kwoty_podatki": "6 złp",
        "opis_sprawy": "Dokończenie dekretu Stanisława Pyrka przeciw Szymonowi Pyrkowi (nakaz kalkulacji we wtorek przed Niedzielą Reminiscere); sesja z 11 III 1661 r.: Marina Cząstkowicowa [Czastkowicowa?] mieszczanka kraśnicka zeznaje dług 6 złp Janowi Łyczkowi [Łyckowi?] z Borowa na ogrodzie przy Bramie Krakowskiej; sesja z 12 III 1661 r.: początek wizji ogrodów i budynków urodzonego Stanisława Łęckowica [Lęckowica?].",
        "transkrypcja": """--- Skan #108 (fol. 52r) ---
52. 1661
...ad faciendum calculum de Tutela... we wtorek przed Niedzielą Reminiscere. Quod Actis connotatum est.

Actum Coram Officio Consulari feria sexta in Vigilia Festi S. Gregorii Papae proxima 1661.
Honesta Marina Cząstkowicowa [Czastkowicowa?] Civis Crasnicensis recognovit debitum
florenorum sex Laborioso Joanni Łyczkowi [Łyckowi?] subdito de Villa Borów.
Przed Urzędem zupełnym Radzieckim Kraśnickim stanąwszy oblicznie
Uczciwa Marina Cząstkowicowa wdowa pozostała po niegdy Mateuszu
Cząstkowicu mieszczaninie kraśnickim zeznała długu złotych sześć
pracowitemu Janowi Łyczkowi poddanemu ze wsi Borowa... zapisany na ogrodzie
przy Bramie Krakowskiej blisko ogrodu Łyczkowego [Sętkowego?]...

Actum Coram Officio Consulari Sabbato ante Dominicam Reminiscere proxima 1661.
Visio Depositionis Hortorum et Aedium Ingenui Stanislai Łęckowic [Lęckowica?]
Relatio facta per DD. Consules.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 109,
        "numer_pozycji": "109",
        "strona_pagina": "fol. 52v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Wizja sądowa / Spustoszenia ogrodów Stanisława Łęckowica",
        "osoby_podmioty": "Stanisław Łęckowic [Lęckowic?], Wojciech Kurowic (burmistrz), Wojciech Szafraniec [Szafrankowic] (rajca), Maciej Konięga (rajca), Jan Rysak (sąsiad), Maruszka (sąsiadka), Gabriel But (śp. sąsiad), Andrzej Rak (sąsiad), Jan Olchawa [?] (opiekun)",
        "kwoty_podatki": "200 złp (szkody w ogrodach)",
        "opis_sprawy": "Szczegółowa wizja sądowa ogrodów i budynków urodzonego Stanisława Łęckowica przeprowadzona przez burmistrza Wojciecha Kurowica i rajców Wojciecha Szafrankowica oraz Macieja Konięgę: opis zniszczonych płotów (12 przęseł) między sąsiadami (Jan Rysak, Maruszka, Gabriel But, Andrzej Rak) i skarga na opiekuna Jana Olchawę [?] o 200 złp szkody.",
        "transkrypcja": """--- Skan #109 (fol. 52v) ---
52v 1661
Na żądanie Urodzonego Stanisława Łęckowica mieszczanina kraśnickiego
wyjechali Sławetni Panowie Wojciech Kurowic Burmistrz natenczas Rezydujący
Kraśnicki wespół z Sławetnymi Pany Wojciechem Szafrankowicem y Maciejem
Konięgą Rajcami Kraśnickimi na obejrzenie spustoszenia ogrodów...
od ogrodu Jana Rysaka y Maruszki... dwanaście przęseł płotu z jednej strony...
od ogrodu niegdy Gabriela Buta ad praesens Andrzeja Raka...
stanął tedy Stanisław Łęckowic przeciwko opiekunowi swemu Janowi Olchawie [?]
żądając inwentarza z dóbr y rachunku z opieki, gdzie na obydwu ogrodach
szkody przez niepłacenie y zaniedbanie na fl 200 szacuje...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 110,
        "numer_pozycji": "110",
        "strona_pagina": "fol. 53r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Cesja Łęckowica na Szafrankowica i areszt srebra Augustyna",
        "osoby_podmioty": "Stanisław Łęckowic, Wojciech Szafraniec [Szafrankowic] (rajca), Augustyn (śp.), wdowa Foxowska [?], Mateusz (śp.), Błażej Rzepka (sługa przysięgły)",
        "kwoty_podatki": "61 złp",
        "opis_sprawy": "Dokończenie wizji Stanisława Łęckowica i uroczysta cesja jego praw do ogrodów i sadów na rzecz rajcy Wojciecha Szafrankowica [Szafrańca]; poniżej sesja z 29 III 1661 r.: rajca Wojciech Szafrankowic zakłada areszt na srebro po śp. Augustynie u wdowy Foxowskiej [?] na poczet długu 61 złp po nieboszczyku Mateuszu (opowiedziane przez sługę przysięgłego Błażeja Rzepkę).",
        "transkrypcja": """--- Skan #110 (fol. 53r) ---
53. 1661
...oświadczając się o to prawnie czynić. Quod Actis connotatum est.

Idem Supradictus Stanislaus Łęckowic Jus suum supra Famatum D. Albertum
Szafrankowic Consulem Crasnicensem transfundit et plenariam potestatem dat.
Stanąwszy oblicznie Stanisław Łęckowic przed Urzędem Radzieckim...
prawa swoje na ogrodach y sadach na Sławetnego Pana Wojciecha
Szafrankowica Rajcę Kraśnickiego przenosi y ceduje wiecznymi czasy.

Actum feria tertia post Dominicam Laetare 1661.
Famatus D. Albertus Szafrankowic Consul Crasnicensis Arestum imposuit
super Argentum Augustini Crasnicensis.
Do Urzędu y Akt niniejszych Radzieckich Kraśnickich przyszedłszy oblicznie
Sławetny P. Wojciech Szafrankowic Rajca Kraśnicki położył solenne Arest
na srebro u wdowy Foxowskiej [?] po niegdy Augustynie kraśnickim leżące...
za dług fl 61 po nieboszczyku Mateuszu... przez sługę przysięgłego
Błażeja Rzepkę opowiedziane y zapisane.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 111,
        "numer_pozycji": "111",
        "strona_pagina": "fol. 53v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Przekazanie burmistrzostwa / Atestacja kradzieży u Tomasza Podchorodeńskiego",
        "osoby_podmioty": "Wojciech Kurowic (ustępujący burmistrz), Maciej Konięga (nowy burmistrz), Tomasz Podchorodeński [Podchorodzieński], Kazimierz Łyszkowski [Łysik?] (czeladnik), Jerzy Potocki [?], Wojciech (mieszczanin kraśnicki), Józef Butecki [Botecki?], Jurg Naumowicz",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Sesja Sądu Łączonego z 29 IV 1661 r.: Translatio Proconsulatus od Wojciecha Kurowica do Macieja Konięgi; poniżej polska atestacja z podpisami własnoręcznymi Józefa Buteckiego [Boteckiego?] i Jurga Naumowicza w imieniu JMP Tomasza Podchorodeńskiego o czeladniku Kazimierzu Łyszkowskim [Łysiku?], który w Wielki Piątek okradł pana z kulbaki tureckiej haftowanej srebrem, szabli i sukni i zbiegł do Kraśnika.",
        "transkrypcja": """--- Skan #111 (fol. 53v) ---
53v 1661
Actum Coram Officio Composito Consulari Advocati et Scabinorum Juratorum
Crasnicensium feria sexta post Dominicam Conductus Paschae 1661.
Translatio Proconsulatus a Famato D. Alberto Kurowic ad Famatum
D. Mathiam Konięga in praesentia totius Magistratus et Communitatis...
cum omnibus thesauris civilibus juxta ritum et consuetudinem antiquam.

Actum Die Dominico ante Festum S. Adalberti Episcopi et Martyris proximo 1661.
My niżej podpisani zeznawamy tym pismem naszym y listem świadectwa
od JMP Tomasza Podchorodeńskiego [Podchorodzieńskiego] iż czeladnik jego niejaki
Kazimierz Łyszkowski [Łysik?] w Wielki Piątek przeszły... ukradł...
kulbakę turecką srebrem haftowaną, szablę y suknię y zbiegł do Kraśnika,
gdzie go przy P. Wojciechu złapano y odebrano wszystko...
Podpisy własnoręczne:
Józef Butecki [Botecki?], Jurg Naumowicz sługa JMP Tomasza Podchorodeńskiego.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 112,
        "numer_pozycji": "112",
        "strona_pagina": "fol. 54r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Protestacja K. Bystrowskiego przeciw rajcy M. Sitarskiemu",
        "osoby_podmioty": "Kazimierz Bystrowski [Łopkowski?], Marcin Sitarski (rajca), Błażej Rzepka (sługa przysięgły), Wojciech Kurowic (burmistrz)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Sesja z 27 IV 1661 r.: gwałtowna protestacja Kazimierza Bystrowskiego [Łopkowskiego?] przeciw rajcy Marcinowi Sitarskiemu o najście domu z sługą przysięgłym Błażejem Rzepką, pobicie i zdeptanie żony oraz zięcia; na dole natychmiastowa reprotestacja Marcina Sitarskiego przeciw Kazimierzowi Bystrowskiemu o obrazę sądu i burmistrza.",
        "transkrypcja": """--- Skan #112 (fol. 54r) ---
54. 1661
Actum Coram Officio Consulari feria quarta post Dominicam Conductus Paschae proxima Anno Dni 1661.
Honestus Casimirus Bystrowski [Łopkowski?] Protestatur contra Famatum
D. Martinum Sitarski Consulem Crasnicensem.
Ad Officium praesens Consulare Crasnicense personaliter veniens Honestus Casimirus
Bystrowski protestatus est contra Famatum D. Martinum Sitarski Consulem
Crasnicensem idque pro eo iż sługę radzieckiego Błażeja Rzepkę przysięgłego
nasłał... pobił Bystrowską y zięcia przysypał y nogami podeptał...
wszystko w domu w obecności sługi Błażeja Rzepki... oświadczam się o to prawnie czynić.

Et incontinenti Famatus D. Martinus Sitarski Consul Crasnicensis coram Officio
praesente solenniter reprotestatus est contra Honestum Casimirum Bystrowski
iż on inordinate dwa razy przyszedłszy do domu Pana Burmistrza...
słowy nieuczciwemi zelżył Urząd y sługę przysięgłego...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 113,
        "numer_pozycji": "113",
        "strona_pagina": "fol. 54r (dublet skanu #112)",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Dublet mikrofilmowy skanu #112",
        "osoby_podmioty": "Kazimierz Bystrowski [Łopkowski?], Marcin Sitarski (rajca), Błażej Rzepka (sługa przysięgły)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "[Dublet mikrofilmowy skanu #112 (fol. 54r)] Identyczne ujęcie karty fol. 54r z protestacją Kazimierza Bystrowskiego [Łopkowskiego?] przeciw rajcy Marcinowi Sitarskiemu o najście z sługą Błażejem Rzepką oraz reprotestacją Marcina Sitarskiego z 27 IV 1661 r.",
        "transkrypcja": """--- Skan #113 (fol. 54r) — [Dublet mikrofilmowy skanu #112] ---
54. 1661
Actum Coram Officio Consulari feria quarta post Dominicam Conductus Paschae proxima Anno Dni 1661.
Honestus Casimirus Bystrowski [Łopkowski?] Protestatur contra Famatum
D. Martinum Sitarski Consulem Crasnicensem.
Ad Officium praesens Consulare Crasnicense personaliter veniens Honestus Casimirus
Bystrowski protestatus est contra Famatum D. Martinum Sitarski Consulem
Crasnicensem idque pro eo iż sługę radzieckiego Błażeja Rzepkę przysięgłego
nasłał... pobił Bystrowską y zięcia przysypał y nogami podeptał...

Et incontinenti Famatus D. Martinus Sitarski Consul Crasnicensis coram Officio
praesente solenniter reprotestatus est contra Honestum Casimirum Bystrowski
iż on inordinate dwa razy przyszedłszy do domu Pana Burmistrza...
słowy nieuczciwemi zelżył Urząd y sługę przysięgłego...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 114,
        "numer_pozycji": "114",
        "strona_pagina": "fol. 54v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Spory egzaktorskie (Pyrek i Jeżykowic vs Różycki) i spór o ogród",
        "osoby_podmioty": "Marcin Sitarski, Szymon Pyrek (ślusarz), Paweł Różycki (egzaktor), Wojciech Szafraniec [Szafrankowic], Maciej Jeżykowic (egzaktor), Wojciech Oleski [Bielik?], Wojciech Kurowic (rajca)",
        "kwoty_podatki": "50 złp, 10 fl 9 1/2 gr, 12 fl 21 gr",
        "opis_sprawy": "Dokończenie reprotestacji M. Sitarskiego (50 złp); sesja z 30 IV 1661 r.: (1) Szymon Pyrek przeciw Pawłowi Różyckiemu o 10 fl 9 1/2 gr dla P. Szafrańca; (2) egzaktor Maciej Jeżykowic przeciw Pawłowi Różyckiemu o 12 fl 21 gr z rachunków egzaktorskich; sesja z 2 V 1661 r.: Maciej Jeżykowic przeciw Wojciechowi Oleskiemu [Bielikowi?] o zagon ogrodu przy Bramie Krakowskiej (zeznanie rajcy Wojciecha Kurowica).",
        "transkrypcja": """--- Skan #114 (fol. 54v) ---
54v 1661
...oddania długu fl 50... Quod Actis connotatum est.

Actum Coram Officio Consulari Sabbato in Vigilia Festi SS. Philippi et Jacobi Apostolorum proximo A.D. 1661.
Inter Honestum Simonem Pyrek Actorem ac Honestum Paulum Różycki Citatum.
Przyznany dług fl 10 gr 9 1/2 które Citatus za Szafrańcem...
Urząd niniejszy nakazuje Pozwanemu aby ten dług oddał sub poena Officii
et Carceris. Quod Decretum ab utraque parte susceptum est.

Inter Famatum Mathiam Jeżykowic Exactorem Actorem ac Paulum Różycki Citatum.
Inhaerendo priori Decreto sub Acto Sabbato ab Officio Composito...
o dług fl 12 gr 21 które z rachunku winien był oddać...
Urząd niniejszy nakazuje aby pomieniony dług sub poena Officii et Carceris oddał.

Actum Coram Officio Consulari feria secunda post Festum SS. Philippi et Jacobi Apostolorum proxima A.D. 1661.
Inter Honestum Mathiam Jeżykowic Actorem ac Albertum Oleski [Bielik?] Citatum.
Świadectwo pokazane z obydwu stron... rajcy Wojciecha Kurowica...
o zagon ogrodu przy bramie Krakowskiej...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 115,
        "numer_pozycji": "115",
        "strona_pagina": "fol. 55r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Przekazanie burmistrzostwa / Dług 41 fl i sprawa Ledwona z Rogalem",
        "osoby_podmioty": "Maciej Jeżykowic, Wojciech Oleski [Bielik?], Maciej Konięga (ustępujący burmistrz), Wojciech Szafraniec [Szafrankowic] (nowy burmistrz), Maciej Zielik [?], Wawrzyniec Sączek [Zajączek?], Bartłomiej Ledwon [Łętowski?], Jan Rogal [Kowal?] (przedmieszczanin)",
        "kwoty_podatki": "41 fl",
        "opis_sprawy": "Dokończenie dekretu M. Jeżykowica z W. Oleskim [Bielikiem?] o ogród przy Bramie Krakowskiej; sesja Sądu Łączonego z 16 VII 1661 r.: Translatio Proconsulatus od Macieja Konięgi do Wojciecha Szafrankowica; tegoż dnia: Maciej Zielik [?] przeciw Wawrzyńcowi Sączkowi [?] o 41 fl; sesja z 25 VIII 1661 r.: Bartłomiej Ledwon [Łętowski?] przeciw przedmieszczaninowi Janowi Rogalowi [Kowalowi?].",
        "transkrypcja": """--- Skan #115 (fol. 55r) ---
55. 1661
...nakazuje Sąd pod zawiedzeniem przed Bramą Krakowską... aby zagon
ogrodu według świadectw pozostał. Quod Actis connotatum est.

Actum Coram Officio Composito Consulari Advocati et Scabinorum Juratorum
Crasnicensium Sabbato post Festum S. Margarethae Virginis et Martyris 1661.
Translatio Proconsulatus a Famato D. Mathia Konięga ad Famatum
D. Albertum Szafrankowic in praesentia totius Magistratus et Communitatis...
cum omnibus thesauris civilibus juxta ritum et consuetudinem antiquam.

Sub eodem Actu:
Inter Ingenuum Mathiam Zielik [?] Actorem ac Laurentium Sączek [?] Citatum.
O dług fl 41... Sąd nakazuje aby w dwóch tygodniach oddał.
Quod Decretum ab utraque parte susceptum est.

Actum feria quinta post Festum S. Bartholomaei Apostoli 1661.
Inter Ingenuum Bartholomaeum Ledwon [Łętowski?] Actorem
ac Honestum Joannem Rogal [Kowal?] anteoppidanum Crasnicensem Citatum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 116,
        "numer_pozycji": "116",
        "strona_pagina": "fol. 55v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Przekazanie burmistrzostwa / Sprawa obyczajowa Szeredasza i córek",
        "osoby_podmioty": "Bartłomiej Ledwon [Łętowski?], Jan Rogal [Kowal?], Wojciech Szafraniec [Szafrankowic] (ustępujący burmistrz), Marcin Sitarski (nowy burmistrz), Maciej Jeżykowic (instygator urzędu), Tomasz Szeredasz [Sieradz?], Jadwiga Szeredaszówna, Anna Szeredaszówna, Dorota (matka)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie sprawy B. Ledwona [Łętowskiego?] z J. Rogalem [Kowalem?]; sesja Sądu Łączonego z 11 X 1661 r.: Translatio Proconsulatus od Wojciecha Szafrankowica do Marcina Sitarskiego; sesja z listopada 1661 r. (po Wszystkich Świętych): sprawa instygatora Macieja Jeżykowica przeciw Tomaszowi Szeredaszowi [Sieradzowi?] i jego córkom Jadwidze oraz Annie o przestępstwo obyczajowe (nomine stupri) — wyrok uwięzienia w domu burmistrza i ukarania matki.",
        "transkrypcja": """--- Skan #116 (fol. 55v) ---
55v 1661
...Urząd niniejszy Radziecki Kraśnicki... nakazuje aby z inwentarza
dóbr opiekę rozliczył... Quod Actis hisce connotatum est.

Actum Coram Officio Composito Consulari Advocati et Scabinorum Juratorum
Crasnicensium feria tertia ante Festum S. Hedvigis proxima 1661.
Translatio Proconsulatus a Famato D. Alberto Szafrankowic ad Famatum
D. Martinum Sitarski in praesentia totius Magistratus et Communitatis...
cum omnibus thesauris civilibus juxta ritum et consuetudinem antiquam.

Actum Coram Officio Consulari post Festum SS. Omnium 1661.
Inter Honestum Mathiam Jeżykowic Instigatorem Officii Actorem
ac Thomam Szeredasz [Sieradz?] et filias ejus Hedvigim et Annam nomine stupri inculpatos Decreta.
Że obwinione Szeredaszówny... w sprawie obyczajowej na przedmieściu...
Urząd niniejszy nakazuje aby obwinione w domu P. Burmistrza były
trzymane pod kłódką, a pokarana ma być także matka ich Dorota...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 117,
        "numer_pozycji": "117",
        "strona_pagina": "fol. 56r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki i Łączony / Opieka Zajączków i dekret przeciw opornym podatnikom",
        "osoby_podmioty": "Tomasz Szeredasz [Sieradz?], Maciej Zajączek [Zawada?], Łukasz Zajączek [Zawada?], Wawrzyniec Sączek [Zajączek?], Stanisław Szczurkowic [Sienkowic?] (egzaktor), Maciej Jeżykowic (egzaktor)",
        "kwoty_podatki": "41 fl",
        "opis_sprawy": "Dokończenie egzekucji dekretu Szeredaszów; sesja z 20 XI 1661 r.: Maciej i Łukasz Zajączkowie [Zawadowie?] przeciw Wawrzyńcowi Sączkowi [Zajączkowi?] o 41 fl z rachunku opieki; sesja Sądu Łączonego z 29 XI 1661 r.: Decretum contra renitentes Exactionum publicarum — egzaktorzy Stanisław Szczurkowic [Sienkowic?] i Maciej Jeżykowic przeciw opornym mieszkańcom uchylającym się od płacenia uchwalonych składek.",
        "transkrypcja": """--- Skan #117 (fol. 56r) ---
56. 1661
...do więzienia... executio per Bedellos Juratos facta est. Quod Actis hisce connotatum est.

Actum Sabbato in Vigilia Festi Praesentationis B. M. Virginis 1661.
Inter Ingenuum Mathiam Zajączek [Zawada?] et Honestum Lucam Zajączek [Zawada?]...
Actores ac Honestum Laurentium Sączek [Zajączek?] Citatum.
O dług fl 41 z rachunku opieki... Urząd niniejszy nakazuje aby na przyszły
termin dług oddał albo z dóbr pokazał. Quod Decretum ab utraque parte susceptum est.

Actum Coram Officio Composito Consulari Advocati et Scabinorum Juratorum
Crasnicensium feria sexta in Vigilia Festi S. Andreae Apostoli proxima 1661.
Decretum contra renitentes Exactionum publicarum.
Sławetni Stanisław Szczurkowic [Sienkowic?] y Maciej Jeżykowic Exactorowie
skarżą się na to iż pospólstwo tak miejskie jako y przedmiejskie składek
uchwalonych oddawać nie chce... przeto Sąd niniejszy nakazuje aby
Exactorowie fanty y bydło brali y na rynku publicznym sprzedawali...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 118,
        "numer_pozycji": "118",
        "strona_pagina": "fol. 56v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Proclamatio Novi Thelonei (nowa taryfa cła generalnego, 29 XII 1661)",
        "osoby_podmioty": "Marcin Sitarski (burmistrz), Wojciech Szafraniec [Szafrankowic] (rajca), Wojciech Kurowic (rajca), Maciej Konięga (rajca), Jakub Kozieł (woźny przysięgły)",
        "kwoty_podatki": "Nowe cło generalne (konie, woły, jałowice, wieprze, zboża)",
        "opis_sprawy": "Dokończenie dekretu egzaktorskiego; poniżej z 29 XII 1661 r.: Proclamatio Novi Thelonei — ogłoszenie na rynku przez woźnego Jakuba Kozła (z rozkazu burmistrza Marcina Sitarskiego oraz rajców Wojciecha Szafrankowica, Wojciecha Kurowica i Macieja Konięgi) nowej taryfy cła generalnego uchwalonej na sejmie warszawskim od towarów, bydła i zbóż na targach (ostatnia karta oryginalna z 1661 r.).",
        "transkrypcja": """--- Skan #118 (fol. 56v) ---
56v 1661
...y one wykupować nie będą do trzeciego dnia, tedy bydło przez cechmistrzów
y rzeźników ma być taksowane y według taksy sprzedawane, a Exactorowie
wedle Regestru co kto winien dług swój odbiorą. Quod Actis connotatum est.

Actum Coram Officio Consulari feria quinta in Crastino Festi SS. Innocentium proxima
Anno Domini Millesimo Sexcentesimo Sexagesimo Primo.
Proclamatio Novi Thelonei.
Ad Mandatum Famati D. Martini Sitarski Proconsulis pro tunc Residentis
et aliorum Famatorum Alberti Szafrankowic, Alberti Kurowic et Mathiae Konięga
Consulum pro tunc Residentium facta est proclamatio in foro publico Novi Thelonei
per Providum Jacobum Kozieł Bedellum Juratum Officii Consularis,
cujus proclamationis talis sequitur tenor:
Panowie Obywatele Miasta Kraśnika y inni wszyscy różnej kondycyi ludzie...
iż na teraźniejszym Sejmie blisko przeszłym Warszawskim stanęła za zgodą
stanów Rzeczypospolitej Konstytucyja aby od wszelakich towarów tak zagranicznych
jako y koronnych... Generalne Nowe Cło płacone było... tak stanu duchownego
jako y szlacheckiego od koni, stad, wołów, jałowic, wieprzów... także od zboża
na targi do miasta y miasteczek przez poddanych przywożonego... do Skarbu Koronnego.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 119,
        "numer_pozycji": "119",
        "strona_pagina": "fol. 57r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1827",
        "kategoria": "Kodykologia / Atestacja Sądu Pokoju Powiatu Kraśnickiego z 10 X 1827 r.",
        "osoby_podmioty": "Sąd Pokoju Powiatu Kraśnickiego, Trybunał Cywilny Województwa Lubelskiego, J. Doliński [?] (sędzia/podsędek)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Urzędowa atestacja z 10 X 1827 r. zamykająca księgę Nr 9 (obejmującą karty 1–56 z lat 1657–1661), odnotowująca uszkodzenia przez mole (zwłaszcza od karty nr 39 do końca) oraz nową oprawę introligatorską wykonaną na zlecenie Trybunału Cywilnego Województwa Lubelskiego z 14 VII 1827 r. (nr 3076), z podpisem i okrągłą pieczęcią Sądu Pokoju Powiatu Kraśnickiego.",
        "transkrypcja": """--- Skan #119 (fol. 57r) ---
57
Niniejsza Księga Nro 9. Miasta Kraśnika
Dekreta, Manifesta, Wizye, Intromissye, Testamenta etc.
od Roku 1657. do 1661. w sobie obejmująca od Karty 1. do 56.
liczbą łącznie oznaczoną, z nadmienieniem iż jest nadbutwiała
przez mole po rogach a nawet y same karty od Nro 39. do końca nadpsute.
Nowo wyintroligowana oprawna. Co wskutek zalecenia Wys. Trybunału
Cywil: Województwa Lubelskiego z dnia 14. Lipca 1827 Nro 3076
przy podpisaniu y przyłożeniu pieczęci Sądu pokoju powiatu Kraśnickiego dopełniono.
Dan na Posiedzeniu Sądu dnia 10. Paźdź. 1827.
[podpis:] J. Doliński [?]
[Okrągła pieczęć tuszowa Sądu Pokoju Powiatu Kraśnickiego]""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 120,
        "numer_pozycji": "120",
        "strona_pagina": "klatka końcowa",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1959",
        "kategoria": "Metryka Archiwalna / Koniec mikrofilmu nr 110358 (11 IX 1959)",
        "osoby_podmioty": "Wojewódzkie Archiwum Państwowe w Lublinie",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Klatka końcowa mikrofilmu nr 110358 (Tom 9, Akta Miasta Kraśnika), wykonana przez Laboratorium Mikrofilmowe Archiwum Dokumentacji Mechanicznej dnia 11 września 1959 r.",
        "transkrypcja": """--- Skan #120 (klatka końcowa) ---
WOJEWÓDZKIE
ARCHIWUM PAŃSTWOWE
LUBLIN

AKTA MIASTA: KRAŚNIKA
NR TOMU 9
NR MIKROFILMU 110358
LAB. MIKROFILM. ARCH. DOKUM. MECHANICZNEJ
KONIEC
DN. 11 M-C 9 ROK 1959 r.""",
        "link_swa": UNIT_LINK
    }
]

existing_nums = {r['nr_skanu'] for r in main_data}
for s in part5_scans:
    if s['nr_skanu'] not in existing_nums:
        main_data.append(s)

main_data.sort(key=lambda x: x['nr_skanu'])

with open('/home/ubuntu/workspace/Gen/main_data_j19_part5.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j19_part5.json: {len(main_data)} rekordów.")
