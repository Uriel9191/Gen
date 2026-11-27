# -*- coding: utf-8 -*-
import json

LINK_SWA = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989934"
SYGN = "35/40/0/1/21"

raw_scans = [
    (1, "Metryczka początkowa mikrofilmu", "1959",
     "Metryczka początkowa mikrofilmu nr 110402",
     "Wojewódzkie Archiwum Państwowe w Lublinie, Laboratorium Mikrofilmowe ADM",
     "-",
     "Karta tytułowa mikrofilmu nr 110402 (Akta Miasta Kraśnika, nr tomu 10, Laboratorium Mikrofilmowe Archiwum Dokumentacji Mechanicznej, Początek, dn. 3 XI 1959 r.).",
     """[Metryczka początkowa mikrofilmu]
WOJEWÓDZKIE ARCHIWUM PAŃSTWOWE LUBLIN
AKTA MIASTA: KRAŚNIKA
NR TOMU 10
NR MIKROFILMU 110402
LAB. MIKROFILM. ARCH. DOKUM. MECHANICZNEJ
POCZĄTEK
DN. 3 M-C 11 ROK 1959 r."""),

    (2, "Formularz Wzór Nr 1 (Metryczka Akt)", "1959",
     "Metryczka akt archiwalnych (Wzór Nr 1)",
     "Wojewódzkie Archiwum Państwowe w Lublinie",
     "-",
     "Formularz archiwalny Wzór Nr 1: Księga m. Kraśnika różnych czynności cywilnych, sygnatura archiwalna 10, data przygotowania akt do mikrofilmowania 10 IV 1959 r., ilość zdjęć 601, nr książki kontrolnej 110.402.",
     """[Metryczka Akt — Wzór Nr 1]
Wojewódzkie Archiwum Państwowe w Lublinie, ul. Narutowicza 10, tel. 37-18
Wzór Nr 1
METRYCZKA AKT
Wypełnia archiwum:
1. Nazwa Archiwum: [pieczęć WAP Lublin]
2. Nazwa zespołu lub zbioru: Księga m. Kraśnika różnych czynności cywiln.
3. Sygnatura archiwalna: 10
4. Data przygotowania akt do mikrofilmowania: 10. IV. 1959 r.
5. Ilość zdjęć: 601
6. Nr książki kontrolnej: 110.402."""),

    (3, "Karta Informacyjna", "1959",
     "Karta informacyjna jednostki archiwalnej Kraśnik 10",
     "Archiwum Państwowe w Lublinie",
     "-",
     "Karta informacyjna (Kraśnik 10): łączna ilość zdjęć 601, wykaz stron pustych niefilmowanych (67v, 85, 100, 128v, 129, 142v, 157v, 161, 200v, 219v, 306, 306v, 307, 307v), wymiary woluminu 34 x 23 cm.",
     """[Karta Informacyjna]
Kraśnik 10
KARTA INFORMACYJNA
Łączna ilość zdjęć: 601
Wykaz stron pustych niefilmowanych:
67v, 85, 100, 128v, 129, 142v, 157v, 161, 200v, 219v, 306, 306v, 307, 307v.
Wymiary dokumentu, obmiar jednostki archiwalnej w cm. wysokość x szerokość: 34 x 23"""),

    (4, "Okładka / Szyld tytułowy (Nr 10)", "1671–1685",
     "Karta tytułowa rękopisu nr 10 (1671–1685)",
     "Urząd Miejski Kraśnicki",
     "-",
     "Okładka pergaminowa/papierowa księgi nr 10: 'Nr 10. Książka rożnych czynnosci Cywilnych Miasta Krasnika z Lat 1671, 1672, 1673, 1678, 1674, 1679, 1682, 1684, 1683, 1685. Rękopis zawiera kart 391.' (z odbitym tekstem druku łacińsko-polskiego).",
     """[Okładka przednia]
Nr 10.
Książka
rożnych czynnosci Cywilnych
Miasta
Krasnika
z Lat
1671 – 1672 – 1673 – 1678 – 1674.
1679 – 1682. 1684. 1683 –
1685.
Rękopis zawiera kart 391."""),

    (5, "fol. 1r (1)", "1671",
     "Otwarcie Protocollum Advocatiale Crasnicense (1671) — relacje szkodowe Kępki i Maraszka, sprawa K. Szklarza (brulion)",
     "Bartłomiej Kępka, Wojciech Karczewic [?], Paweł Smarowic, Stanisław Nawrocki, Antoni Maraszek [?], Maciej [?] Batusik, Jan Łabędź [?], Kazimierz Szklarz, Jan Stary alias Kowalik, Wdowa Derelikowa, Marcin Przenczkowicz [?]",
     "-",
     "Otwarcie protokołu wójtowskiego kraśnickiego w 1671 r. (pierwotny brulion): relacje ławników Wojciecha Karczewica [?] i Pawła Smarowica o szkodzie w zbożu Bartłomieja Kępki u Stanisława Nawrockiego oraz Antoniego Maraszka [?]; skarga Kazimierza Szklarza przeciw Janowi Staremu alias Kowalikowi (datowana omyłkowo 1670 zamiast 1671); sprawa wdowy Derelikowej z Marcinem Przenczkowiczem [?].",
     """[fol. 1r]
PROTOCOLLUM ADVOCATIALE CRASNICENSE INCEPTUM in Anno Dni 1671: 7bris [Septembris].
Relatio Dominorum Scabinorum ex parte Honesti Bartholomaei Kępka Anteoppidani Crasnicen.
Famati Albertus Karczewic [?] et Paulus Smarowic Scabini Jurati Crasnicenses in vim suae fidei et fidelis relationis recognoverunt: Iż widzieli w polu Uczciwego Bartłomieja Kępki owsa ćwiertnię spasione, także kóp 20 porąbane, w ziemi wdeptane, popasione, winę dał Sławetnemu Stanisławowi Nawrockiemu, na którego się przyjmuie świadectwie Aktor solenniter protestował, że słowa nieuczciwe złodziejskie zwykł nań mówić, które słowa może sprawić, a gotów iest prawie tąż drogą potrzeć, gdzie obwiniony Aktor obiecuie prawnie postąpić, quod est connotatum et solidatum.
Relatio Dnor. Scabinorum ex Instantia Honesti D. Maraszek Anteoppidani Crasn.
Famati Paulus Smarowic et Mathias [?] Batusik Scabini Jurati Crasn. in vim suae verae relationis recognoverunt per requisitionem D. Joannis Łabędź [?] na gruncie Uczciwego Antoniego [?] Maraszka Przedmieszczanina Kraśnickiego o kópę tatarki spasionej, winę dał Urodzonemu [?] [...]
Actum feria sexta ante festum Exaltationis Sanctae Crucis prox[im]a 1670 [recte: 1671].
Przed Urzędem Wóytowskim y Ławniczym oblicznie stawaiący Uczciwy Kazimierz Szklarz Przedmieszczanin Kraśnicki skarżył na Uczciwego Jana Starego alias Kowalika o szkody które iemu przez bydło poczynił w życie, pomieniony Kowalik przyznał aliqua ex parte że konie bywały w szkodzie Aktora [...] Sąd obiedwie strony do ugody odsyła aby szkodę nagrodził y słów nieuczciwych na się nie mówili.
Inter Hon. Viduam Derelikowa actricem et Honest. Martinum Przenczkowicz [?] citatum dilatio."""),

    (6, "fol. 1v (1v)", "1671",
     "Dokończenie sprawy wdowy Derelikowej; proces Stanisława Partyki przeciw Wojciechowi Nogajowi o obelgę (brulion, 16 IX 1671)",
     "Wdowa Derelikowa, Marcinowa Bernatowa [?], Stanisław Partyka, Wojciech Nogai",
     "-",
     "Dokończenie sprawy wdowy Derelikowej z Marcinową Bernatową [?]. Poniżej sesja z środy po Podwyższeniu Krzyża Świętego (16 IX 1671 r.): wyrok w sprawie Stanisława Partyki przeciw Wojciechowi Nogajowi o zniesławienie (nakaz przeprosin w domu w obecności 4 świadków).",
     """[fol. 1v]
[...] tymże Urzędem Wóytowskim y Ławniczym między Uczciwą Wdową Drelikową aktorką a Marcinową Bernatową [...] od Sądu spytane, że nie same miały stanąć w tey sprawie ale z doradą [...] teyże mierze przed tenże Sąd nieodwłocznie ma stanąć, quod est susceptum et solidatum.

Actum feria quarta post festum Exaltationis S. Crucis prox[im]a 1671.
Inter Stanislaum Partyka actorem et Albertum Nogai ciuem Crasn. [?] citatum.
Etsi de iure in causis iniuriarum dilatio dari consueti debet, verum quia actor in recenti crimine silebat [...] nihilominus tamen Officium decernit gratiose, ut citatus cum assistentia virorum quatuor uxorem Actoris in domo ipsius propria reconciliet et de iniuria ratione subornationis salvam actionem partibus utrisque in termino praefixo reservamus, quod ambabus partibus gestum et solidatum est."""),

    (7, "fol. 2r (2)", "1671",
     "Wyroki z 16 IX 1671 r.: S. Partyka vs W. Nogai, żona organisty vs A. Łążkowic [?], Ł. Domitek vs J. Wiatrek, wdowa Drelikowa (brulion)",
     "Stanisław Partyka, Wojciech Nogai, Żona organisty (Łucja Organowa), Augustyn Łążkowic [Łaźkowic?], Wojciech Potocki, Łukasz Domitek [?], Jan Wiatrek [?], Wdowa Drelikowa, Petrykowiczowie [Petrikowscy]",
     "-",
     "Brulion wyroków z 16 IX 1671 r.: 1) Stanisław Partyka przeciw szewcowi Wojciechowi Nogajowi o zamieszanie skór na jarmarku; 2) żona organisty przeciw Augustynowi Łążkowicowi [?] o córkę i zabrane fanty; 3) Stanisław Partyka przeciw Wojciechowi Potockiemu; 4) Łukasz Domitek [?] przeciw Janowi Wiatrowi [Wiatrkowi?] o chorego konia; 5) wdowa Drelikowa przeciw synom Petryka o zabicie świni cepami.",
     """[fol. 2r]
Actum feria quarta post festum Exaltationis S. Crucis prox[im]a 1671.
Inter Stanislaum Partyka actorem et Albertum Nogai citatum.
W sprawie o zadanie niegodziwe przez Aktora pozwanemu, a to iako by miał pozwanemu skórę drugiemu szewcowi na jarmarku zamieszać y wziąć y między swój towar włożyć, iż się pozwany zapiera na świadków, że on tej skóry nie kradł y nie wie iakim sposobem w iego towar się zamieszała, Sąd niniejszy pozwala dylacyi do piątku przyszłego utrique parti cum termino peremptorio, quod est solidatum.
Inter Consortem Organarii actricem et Augustinum Łążkowic [Łaźkowic?] citatum. Sub eodem Actu.
Iż pozwany oddał córkę swoią do Aktorki, która dziewczyna odeszła swowolnie y rzeczy niektóre które fanty pobrała, a pozwany nie przyznawał się aby o tym wiedział, tedy Sąd niniejszy pozwanemu nakazuie na piątek przyszły iuramentem tego poprawić iako nie wie o tey dziewczynie gdzie iest.
Inter Stanislaum Partyka Actorem et Albertum Potocki citatum. Sub eodem Actu.
Decreto praesentis Judicii iniunctum est aby citatus na piątek blisko przyszły stanał y zeznania swego alias iuramentum [...] na przyszłym terminie poprawił, quod est susceptum et solidatum.
Inter Lucam Domitek [?] Actorem et Joannem Wiatrek [?] citatum. Sub eodem Actu.
Vigore praesentis decreti demandatum est: Ponieważ Aktorowi koń za trzy dni przy najmowaniu [...] Ponieważ koń ten iest malikowaty którego Aktor kupił u pozwanego, teraz mu go przywraca a iż go nie oddał zaraz pozwanemu, tedy Sąd niniejszy nakazuie aby konia pozwany nazad wziął, a za to że go nie zaraz oddał pozwanemu ma dać grzywnę ieden.
Inter Viduam Drelikową actricem et Petrikowies [?] citatos.
Skarżyła się Aktorka na pozwaną o zabicie świni iey, Aktorka broniąc się powiedziała że te synowie Petrykowi świnie pozabijali, wegnawszy one na podwórze swoie cepami potłukli, ale nas prosili abyśmy ni przed kim nie powiedali. Sąd niniejszy nakazuie aby w piątek przyszły zeznala to y synów przyprowadziła Petrykowych do tej sprawy."""),

    (8, "fol. 2v (2v)", "1671",
     "Zeznania świadków W. Nogaja z jarmarku urzędowskiego; manifestacja Żyda Wygdora przeciw ślusarzowi A. Pieniążkowi (18 IX 1671)",
     "Wojciech Nogai, Regina Frymuszowa [Grymuzyna] Małbokowa, Jan Frymusz [Grymuza] Małbok, Wojciech Potocki, Stanisław Partyka, Wygdor (Żyd), Andrzej Pieniążek (ślusarz)",
     "14 złp",
     "Sesja z piątku przed św. Mateuszem (18 IX 1671 r.): zeznania świadków Wojciecha Nogaja — 1) Reginy żony Jana Frymusza [Grymuzy] Małboka oraz 2) Wojciecha Potockiego o jarmarku w Urzędowie w poniedziałek po Wielkanocy, sprzedaży skór między Nogajem a szewcem z Opola i kłótni z Partyką. Poniżej manifestacja Żyda Wygdora przeciw ślusarzowi Andrzejowi Pieniążkowi o zastawione rzeczy za 14 złp.",
     """[fol. 2v]
Actum feria 6ta ante festum S. Matthaei Evangel. prox[im]a 1671.
Testimonia ex parte Alberti Nogai citt[ati].
Uczciwa Regina Uczciwego Jana Frymusza [Grymuzy] Małboka przy pozwana z instancyi Uczciwego Wojciecha Nogaia takowe świadectwo pod przysięgą zeznała: Pod czas Jarmarku w Urzędowie na Przewodni poniedziałek po Wielkiej Nocy idąc [...] tamże widziałam pod Ratuszem, gdzie Nogai miał skóry, podle niego przedawał też szewc z Opola skóry także, gdzie Nogai przedawał skóry swoie pijany bardzo ledwie stał na nogach y wziął ze mnie piniądze za swoie roboty y skóry, a szewc z Opola przedawał skóry y poczeli się rozrzucać, a znalazszy tam wóz swój wziął porządkiem bez żadnej winy na Nogaia nie kładąc [...]
2dus Testis: Wojciech Potocki pod przysięgą takowe zeznanie wydał: Pod czas Jarmarku w Urzędowie iako wierny świadek zeznał, żem ia tam natenczas był y widziałem kiedy Nogai szewc przedawał skóry swoie niedaleko Ratusza, a podle niego zaraz przedawał szewc z Opola skóry swoie, y którzy targowali skóry, rzucali tak że się pomieszały z Nogajowemi, a Nogai odszedł y pił gdzieś w gospodzie, a potym pijany przyszedł na to miejsce gdzie skóry swoie przedawał, pijany bardzo, szewc z Opola wziął skórkę swoię z miedzy skór Nogajowych [...] a kiedy przyszedł do wozu, Partyka z Nogajem zaczęli się bić, więcej nie wiem. Super quod iuraverunt.

Manifestatio Perfidi Wigder contra Andream Pieniążek ferri fabrum Civem Crasn.
Do Urzędu y Akt niniejszych przyszedłszy niewierny Wygdor Żyd i obywatel kraśnicki czynił manifestacyą przeciw Andrzejowi Pieniążkowi ślusarzowi kraśnickiemu, iż on zastawiwszy u niego rzeczy niektóre, a mianowicie złoty pierścień [?] y naczynia ślusarskie od lat półtora za czternaście złotych polskich dotąd nie wykupił, prosząc o taxę urzędową tych rzeczy [...]"""),

    (9, "fol. 3r (3)", "1671",
     "Dokończenie manifestacji Wygdora; relacja ławników dla S. Nawrockiego; protestacja przeciw Łeżykowi i Kępce; dług G. Foxa (22–23 IX 1671)",
     "Wygdor (Żyd), Andrzej Pieniążek, Błażej Kołodziejczyk, Paweł Smarowic, Stanisław Nawrocki, Adam Łeżyk [Łężyk?], Piotr Kępka, Łucja Organowa, Augustyn Łążkowic, Grzegorz Fox",
     "30 złp",
     "Dokończenie manifestacji Żyda Wygdora przeciw Andrzejowi Pieniążkowi; sesja z wtorku po św. Mateuszu (22 IX 1671 r.): relacja ławników Błażeja Kołodziejczyka i Pawła Smarowica o szkodzie w zbożu Stanisława Nawrockiego na roli Karczowskiej [Karasowskiej?]; protestacja Stanisława Nawrockiego przeciw Adamowi Łeżykowi [?] i Piotrowi Kępce; sesja z 23 IX 1671 r.: sprawy Augustyna Łążkowica z organistą i Bractwem Różańcowym oraz uznanie długu 30 złp Bractwu Różańcowemu przez Grzegorza Foxa.",
     """[fol. 3r]
[...] a in quantum by nie chciał wykupić tych rzeczy pomieniony Andrzej ślusarz, tedy ma mieć te rzeczy taxowane do Urzędu y przepadać maią według prawa, quod est connotatum et solidatum.

Actum feria tertia post festum S. Matthaei Evangelistae prox[im]a 1671.
Relatio Dnor. Scabinorum ex parte Famosi Dni Stan. Nawrocki.
Famati Blasius Kołodziejczyk et Paulus Smarowic Scabini Jurati in vim suae fidelis relationis recognoverunt: Iż widząc na Roli Karczowskiej [Karasowskiej?] szkodę poczynioną, owsa zagonów trzy spasione, porąbane, także na pszenicy pokopy zdarte y porwane, kóp trzy porzucane, jęczmienia kopinę zposzarpaną, item iedna kopa tatarki nadeptana, winę dał Sławetny P. Nawrocki Adamowi Łeżykowi y Piotrowi Kępce.
Manifestatio Famosi Dni Stan. Nawrocki contra Honestos Adamum Łeżyk [Łężyk?] et Petrum Kępka.
Przed Urzędem Wóytowskim y Ławniczym Sławetny Stanisław Nawrocki protestował się przeciw Adamowi Łeżykowi y Piotrowi Kępce o zajęcie bydła ze szkody y gwałtowne odbicie [...]

Actum feria quarta post festum S. Matthaei Evangelistae prox[im]a 1671.
Inter Organistam actorem et Augustinum Łążkowic [Łaźkowic?] citatum.
Ponieważ między stronami obiema Sąd nakazał aby pozwany na blisko przyszły piątek przysięgę tego poprawił [...]
Inter Promotorem Sacratissimi Rosarii et Aug. Łążkowic citatum. Submissio.
Gregorius Fox recognoscit Debita Confraternitati S. Rosarii.
Coram Officio praesentis Juridicae Gregorius Fox Civis Crasnicensis palam recognovit se debere Confraternitati S. Rosarii florenos 30 computando [...]"""),

    (10, "fol. 3v (3v)", "1671",
     "Ciąg dalszy długu G. Foxa (na rok 1672); S. Wiązkowic vs G. Miecznik; S. Nawrocki vs A. Łeżyk i P. Kępka; zeznanie S. Magierowskiego (brulion)",
     "Grzegorz Fox, Szymon Wiązkowic [Wiaznowicz?], Grzegorz Miecznik [Ensifaber], Stanisław Nawrocki, Adam Łeżyk, Piotr Kępka, Stanisław Magierowski, Stanisław Partyka, Wojciech Nogai, Matyjasz Kępka, Aleksander Strowski [Srowski?], Jan Zamoyski / Zan",
     "-",
     "Dokończenie wpisu długu Grzegorza Foxa (termin spłaty 1672 r.); sprawa burmistrza Szymona Wiązkowica [Wiaznowicza?] przeciw Grzegorzowi Miecznikowi [Ensifaber] o komorne; sprawa Stanisława Nawrockiego przeciw Adamowi Łeżykowi i Piotrowi Kępce o woły; zeznanie Stanisława Magierowskiego ze strony Partyki o jarmarku w Urzędowie; dekret akcesoryjny Matyjasza Kępki vs Adam Łeżyk; manifestacja sługi Aleksandra Strowskiego [Srowskiego?] przeciw poddanym Żatkom [Łatkom] z Budzyna.",
     """[fol. 3v]
[...] in anno proximo venturo millesimo sexcentesimo septuagesimo secundo persolvere ac reponere sub poena [...]
Inter Famatum Simonem Wiaznowicz [Wiązkowic?] Proconsulem Crasn. actorem et Famatum Gregorium Ensifaber [Miecznika] citatum. Dilatio.
Ponieważ pozwany sam przyznaje że za rok nie oddał y że pataraczkami obiecował y teraz czas wziął z gminy [...] Sąd nakazuie aby ludzi wysadził a co piątek blisko przyszły [...] a dorówna za komorne.
Inter Famatum Stan. Nawrocki Actorem et Adamum Łeżyk et Petrum Kępka citatos. Dilatio.
Że pozwany nie przyznaje się aby woły iego na szkodzie były, a Aktor ma świadków stawiać [...]
Testimonia ex parte Honesti Stanislai Partyka.
Uczciwy Stanisław Magierowski będąc przypozwany przed Sąd niniejszy z instancyi Stan. Partyki pod przysięgą zeznał: Będąc na Jarmarku w Urzędowie na Przewodnią niedzielę był też tam y Nogai z swoim towarem, ale nie widziałem podle kogo stał y z kim tylko ze mną pił, zabawił się, przedanie złe mieli, aż teraz Nogai wziął oślą skórę moią y pojechał do Kraśnika [...]
Decretum accessorii inter Mathiam Kępka actorem et Adamum Łeżyk citatum. Dilatio.
Manifestatio Alexandri Srowski [Strowski?] ex parte Żatków [Łatków?].
Do Urzędu i Akt niniejszych Wóytowskich y Ławniczych Kraśnickich przyszedłszy oblicznie Alexander Strowski sługa JW JMP P. Podkomorzego Koronnego Starosty Urzędowskiego oświadczył się, iż poddani ze wsi Budzyna z dzierżawy JMP Zana [Zamoyskiego?] nie stanęli do przysięgi [...]"""),

    (11, "fol. 4r (4)", "1671",
     "Sesja 25 IX 1671 r.: zeznania K. i S. Kozińskich dla S. Nawrockiego; P. Sandomierski; wyrok w sporze S. Partyki z W. Nogajem",
     "Stanisław Nawrocki, Katarzyna Kozińska, Paweł Koziński, Stanisław Koziński, Adam Łeżyk, Piotr Kępka, Paweł Sandomierski (szewc), Stanisław Partyka, Wojciech Nogai",
     "-",
     "Sesja z piątku przed św. Michałem (25 IX 1671 r.): zeznania 1) Katarzyny żony Pawła Kozińskiego i 2) młodzieńca Stanisława Kozińskiego na rzecz Stanisława Nawrockiego o zajęciu wołów ze szkody i oporze Adama Łeżyka z dziewką Piotra Kępki; wyrok w sprawie bractwa różańcowego przeciw szewcowi Pawłowi Sandomierskiemu o bawełnicę bracką; duży wyrok w sprawie Stanisława Partyki przeciw Wojciechowi Nogajowi.",
     """[fol. 4r]
Actum feria 6ta ante festum S. Michaelis Archang. 1671.
Testimonium ex parte Famati Stan. Nawrocki actoris.
Uczciwa Katarzyna Uczciwego Pawła Kozińskiego małżonka przypozwana pod przysięgą zeznała: We wtorek dodnia widzieliśmy że P. Nawrocki zaimował z swego pola woły, a Koziereczka z dziewką Piotra Kępki y z Adamem Łeżykiem bronili mu tego zaięcia [...]
2dus Testis Młodzieniec Stan. Koziński także pod przysięgą zeznał we wtorek z pola o czwartej godzinie przed dniem widziałem kiedy P. Nawrocki zaimował bydło z pola, w tym Adam Łeżyk z kijem nie dał zaimować [...]
Decretum inter Famatum Stan. Nawrocki actorem et Adamum Łeżyk et Petrum Kępka citatos.
Ponieważ Aktor po przysiędze na piersiach rękę położywszy zeznał iż za szkody swoie zawarte pozwane zaiął, Sąd nakazuie na żądanie Aktora aby pozwani szkody nagrodzili y trzy dni w wieży przesiedzieli.
Inter Promotorem SSmi Rosarii actorem et Paulum Sandomierski sutorem citatum.
Decreto Officii praesentis iniunctum est aby pozwany rękodajnie oddał bawełnicę bracką Bractwu Różańca Świętego [...]
Inter Stanislaum Partyka actorem et Albertum Nogai citatum Decretum.
W sprawie między stronami toczącej się o zadanie niegodziwe złodziejstwa skór przez Aktora pozwanemu [...] ponieważ ze świadków przysięgłych pokazuje się iż skóry pomieszały się w zamieszaniu jarmarcznym a nie kradzieżą [...]"""),

    (12, "fol. 4v (4v)", "1671",
     "Dokończenie wyroku Partyka vs Nogai; M. Kępka vs A. Łeżyk; kontumacja G. Miecznika; obdukcja ran żony A. Maraszka (26–28 IX 1671)",
     "Stanisław Partyka, Wojciech Nogai, Matyjasz Kępka, Adam Łeżyk, Grzegorz Miecznik [Ensifaber], Szymon Wiązkowic [Wiaznowicz?], Augustyn Maraszek, Zofia Maraszkowa, Paweł Smarowic, Sebastian Balusik, Rożniatowska, Maryna Drelikowa",
     "-",
     "Dokończenie wyroku dla Partyki i Nogaja (przeprosiny przed 6 osobami wiarygodnymi, wzmianka o Zarzeczu); odłożenie sprawy Matyjasza Kępki vs Adam Łeżyk; kontumacja Grzegorza Miecznika z instancji Szymona Wiązkowica; sobotnia obdukcja (26 IX 1671 r.) ran żony Augustyna Maraszka zadanych przez żonę Rożniatowskiego; poniedziałek 28 IX 1671 r.: sprawa Grzegorza Łeżyka [?] przeciw wdowie Drelikowej.",
     """[fol. 4v]
[...] winy urzędownej grzywien 10 aby oddał, a po wyłożeniu z więzienia ma przeprosić tegoż pozwanego Nogaia w siebie przy Urzędzie przez osób 6 wiarygodnych [...] w Zarzeczu albo przed zamkiem.
Inter Matthiam Kępka actorem et Adamum Łeżyk citatum dilatio.
Na terminie dzisiejszym z dylacyi przypadłym, że Aktor dla krótkości czasu nie mógł się dostatecznie przygotować do pokazania wywodów [...] Sąd niniejszy odsyła sprawę na blisko przyszły poniedziałek.
Manifestatio Gregorius Ensifaber ex parte Simonis Wiązkowic [Wiaznowicz?] contumax.
Culpa P. Stan. Augu. Maraszek et uxoris.
Actum die Sabbatino ante Festum S. Michaelis Archang. prox[im]a 1671.
Famati Paulus Smarowic et Sebast. Balusik Scabini Jurati Crasnicenses coram Officio praesenti fidelis relationis recognoverunt: Że w domu Sławetnego Pawła Gromanowicza [?] widzieli u Zofii Maraszkowej żony Augustyna Maraszka rany na ramieniu od uderzenia sine na trzy palce szerokie [...] które Rożniatowskiego żona wieczór przybiegłszy zadała.
Actum feria secunda ante Festum S. Michaelis Archangeli prox[im]a 1671.
Inter Greg. Łeżyk [?] actorem et Viduam Drelikowa cum filio citatos.
Ponieważ pozwany nie przyznaje się do tego aby żona miała mu szkodę uczynić, Sąd nakazał aby na dzień piątkowy blisko przyszły świadków stawił [...]"""),

    (13, "fol. 5r (5)", "1671",
     "Zeznanie dla A. Maraszka; przysięga poddanych z Budzyna Sz. Łatki i J. Wronki; sesja z 30 IX 1671 r. (G. Łeżyk vs M. Drelikowa)",
     "Augustyn Maraszek, Tomasz Koźmiński [?], Rożniatowska, Aleksander Strowski [Srowski?], Szymon Łatka [Zatka], Jan Wronka, Jan Zan [Zamoyski?], Grzegorz Łeżyk [?], Jakub Wróbel [?], Maryna Drelikowa",
     "-",
     "Zeznanie Tomasza Koźmińskiego [?] ze strony Augustyna Maraszka o najściu Rożniatowskiej z kamieniami. Poniżej akt przysięgi pracowitych Szymona Łatki i Jana Wronki poddanych z Budzyna przeciw słudze Aleksandrowi Strowskiemu z dzierżawy JMP Zana. Na dole sesja z środy po św. Michale (30 IX 1671 r.): zeznanie świadka Jakuba Wróbla [?] i wyrok w sprawie Grzegorza Łeżyka [?] przeciw Marynie Drelikowej z synem.",
     """[fol. 5r]
Testimonium ex parte August. Maraszek.
Uczciwy Tomasz syn Jacka Koźmińskiego [?] zeznał pod przysięgą: Przyszedł do mnie Maraszek z córką i żoną swoią Rożniatowską [?] gonił ią z kamieniem w ręku, aż uciekła do domu mego gdzie Maraszek kazał ią wydać [...]
Terminus Juramenti Laboriosi Simonis Łatka et Joan. Wronka Subditorum de Budzin.
Z dekretu JW Pana Dzierżawcy poddanych swoich z instancyi Szymona Łatki y Jana Wronki z Budzyna, iż nie stanęli na pierwszy termin do wykonania przysięgi [...] stawił się szlachetny Alexander Strowski służący JMP Zana Dzierżawcy Kraśnickiego, a poddani z Budzyna gotowi do wykonania przysięgi [...]
Actum feria quarta post Festum S. Michaelis Archangeli prox[im]a 1671.
Testimonium ex parte Gregorii Łeżyk.
Uczciwy Jakub Wróbel [?] stanąwszy oblicznie przed Sądem Wóytowskim y Ławniczym zeznał iż Grzegorz Łeżyk prosił mię na świadectwo tegoż dnia na oglądanie szkody w zbożu przez bydło poczynionej [...]
Inter Gregorium Łeżyk actorem et Mariannam Drelikowa cum filio citatam Decretum.
W sprawie między Grzegorzem Łeżykiem aktorem a Maryną Drelikową z synem o szkodę w owsie i jęczmieniu [...] Sąd nakazuie aby pozwany szkodę nagrodził y przeprosił, quod est susceptum et solidatum."""),

    (14, "fol. 5v (5v)", "1671",
     "Spory o kradzież zboża i areszty; kwitacja w domu śp. Wójta; taxa srebra guzikowego (2 X 1671)",
     "Kazimierz Stolarz, Tomasz Sztymaszek [?], Stanisław Nawrocki, Adam Łeżyk, Piotr Kępka, Augustyn Maraszek, Rożniatowski, Grzegorz Miecznik, Tomasz Jasiek [?], Wojciech Kurewic [Kuzewic?], Jan Pieniążek, Góralowa [?]",
     "130 złp, 9 próba, 3 łuty po 50 gr",
     "Sprawy z końca września i 2 X 1671 r.: Kazimierz Stolarz vs Tomasz Sztymaszek [?] o kradzież zboża ze stodoły; protestacja Adama Łeżyka przeciw Stanisławowi Nawrockiemu; sprawa Augustyna Maraszka vs żona Rożniatowskiego (kontumacja Grzegorza Miecznika); kwitacja Tomasza Jaśka [?] i Wojciecha Kurewica [?] na 130 złp w domu wójta; sesja z 2 X 1671 r.: urzędowa wycena (taxa) srebra guzikowego próby 9 (3 łuty po 50 gr) zastawionego przez Jana Pieniążka.",
     """[fol. 5v]
Inter Casimirum Stolarz actorem et Thomam Sztymaszek [?] citatum.
Skarżył się Aktor na pozwanego że mu zboże pokradziono z stodoły, pozwany broniąc się powiedział że nie on kradł [...]
Inter Stan. Nawrocki actorem et Adamum Łeżyk et Petrum Kępka Protestantes. Protestatio Adami Łeżyk contra Stan. Nawrocki.
Inter August. Maraszek actorem et Rożniatowski uxorem citatam dilatio (Gregorius Ensifaber contumax).
Inter Hon. Thomam Jasiek [?] Fam. Albertum Kurewic [?] Quietatio.
W domu Sławetnego Pana Wójta Kraśnickiego przyszedłszy do Urzędu Tutejszego Tomasz Jasiek z Wojciechem Kurewicem [?] zeznali iż z sumy 130 złotych polskich z kontraktu między sobą uczynionego kwitują się wzajemnie [...]

Actum feria sexta ante festum S. Francisci Confessoris prox[im]a A. Dni 1671.
Testimonium ex parte Starościk [?].
Taxa Officiosa srebra jednego guzikowego. Próby 9: łotów 3 po gr 50 [...] które srebro przez Jana Pieniążka zastawione od lat półtora u Góralowej [?] taxowane przez złotników i urząd [...]
Inter Hon. Casimirum Stolarz actorem et Thomam Stachyra [?] citatum."""),

    (15, "fol. 6r (6)", "1671",
     "Dekret A. Maraszka; obdukcja ran W. Kurewica, jego żony i furmana (6 X 1671); obdukcja Jakuba Tatara z Kiełczowic (8 X 1671)",
     "Augustyn Maraszek, Rożniatowski, Wojciech Kurewic [Kuzewic?], Paweł Smarowic, Błażej Kołodziejczyk, Wojciech Bartłomiejowic [?], Walenty Prepacki [?], Jan Szarak [?], Jakub Tatar (z Kiełczowic), Tomasz Pałęga, Maciej Bielaszkowic",
     "-",
     "Dekret w sprawie Augustyna Maraszka przeciw żonie Rożniatowskiego (przeprosiny i zwrot kosztów). Poniżej obdukcja z 6 X 1671 r. ran Wojciecha Kurewica [?], jego żony i furmana dokonana przez ławników Pawła Smarowica i Błażeja Kołodziejczyka oraz zeznanie furmana Wojciecha o napaści Walentego Prepackiego [?] i Jana Szaraka [?]. Na dole z 8 X 1671 r.: obdukcja ran pracowitego Jakuba Tatara ze wsi Kiełczowice przez ławników Tomasza Pałęgę i Macieja Bielaszkowica.",
     """[fol. 6r]
Inter August. Maraszek actorem et Rożniatowski uxorem citatos.
Ponieważ Aktor dowiódł świadkami że na dom aktora naszła z kamieniami [...] Sąd nakazuie przeprosić i koszta prawne oddać.

Vulnera Famat. Alberti Kurewic [?] et uxoris eius et aurigae. Actum feria 3tia in crastino S. Francisci 1671.
Przed Urzędem niniejszym oblicznie stawaiący Sławetni Paweł Smarowic y Błażej Kołodziejczyk Ławnicy Przysięgli Kraśniccy zeznali: Iż widzieli u Sławetnego Wojciecha Kurewica [?] na ręce prawej od ramienia aż do łokcia stłuczenie krwawe, u żony iego sine na plecach, a u furmana ich rany na głowie y rękach od kijów zadane [...]
Testimonia ex parte Famati Alberti Kurewic uxoris eius et aurigae.
Uczciwy Wojciech Bartłomiejowic [?] furman zeznał pod przysięgą o napaści na gościniec przez Walentego Prepackiego [?] i towarzyszy [...]

Actum feria quinta ante festum S. Dionisii Episcopi 1671.
Vulnera Jacobi Tatara de Kiełczowice.
Ex Instantia Laboriosi Jacobi Tatara de Kiełczowice Scabini Jurati Crasnicenses Thomas Pałęga et Mathias Bielaszkowic fideliter retulerunt: Iż widzieli rany na głowie y rękach u pomienionego Jakuba Tatara w Kraśniku zadane [...]"""),

    (16, "fol. 6v (6v)", "1671",
     "Obdukcja ran Marianny Nawrockiej (9 X 1671); zeznanie burmistrza M. Dubielowica o sprzedaży domu za 160 złp; protestacja M. Bielaszkowica",
     "Wojciech Kurewic [Kuzewic?], Sebastian Balusik, Marianna Nawrocka, Stanisław Nawrocki, Maciej [Mateusz] Bielaszkowic, Michał Dubielowic (burmistrz), Michał Durgiewicz [?], Szymon Wigozkowic [?], Maciej Dębski [?], Szafrańcowa [?], Tomasz Łążkowic, Andrzej Studiator, Grzegorz Miecznik",
     "160 złp, 20 złp, 40 złp, 48 gr",
     "Sesja z piątku w dzień św. Dionizego (9 X 1671 r., z adnotacją o święcie Wiktorii nad Turkami): obdukcja ran brzemiennej Marianny, żony Stanisława Nawrockiego, zadanych przez Macieja Bielaszkowica. Poniżej zeznanie byłego burmistrza Michała Dubielowica o sprzedaży domu Macieja Dębskiego [?] i Anny dla Szafrańcowej [?] za 160 złp (wzmiankowani Michał Dubiel, Tomasz Łążkowic); sprawa Andrzeja Studiatora vs Grzegorz Miecznik oraz protestacja Macieja Bielaszkowica przeciw Stanisławowi Nawrockiemu.",
     """[fol. 6v]
Actum feria sexta ipso die festi S. Dionisii Episcopi [ante festum S. Victoriae de Turcis reportatae] 1671.
Sławetni Wojciech Kurewic y Sebastian Balusik Ławnicy Przysięgli Kraśniccy zeznali: Iż z ramienia Urzędu na oglądanie ran Sławetnej Stanisława Nawrockiego małżonki Marianny udali się, gdzie widzieli na lewej ręce między łokciem a pięścią raz krwawy, na prawej ręce raz siny na trzy członki, które to rany zadał jej Maciej Bielaszkowic, a ona iest brzemienna [...]
Famatus Michael Dubielowic Mercipotus inter Michaelem Durgiewicz [?] et Simonem Wigozkowic [?].
Przed Urzędem Wóytowskim y Ławniczym oblicznie stawaiący Sławetny Michał Dubielowic Burmistrz Kraśnicki zeznał dobrowolnie iż przedtym byli przy kupnie domu między Maciejem Dębskim [?] y żoną iego Anną a Szafrańcową [?] za summę sto sześćdziesiąt złotych polskich [...]
Scribat Resignatio Thomae Łążkowic in [...]
Inter Andream Studiatorem Actorem et Gregorium gladiatorem [miecznika] citatos dilatio.
Mathias Bielaszkowic protestatur contra Stanislaum Nawrocki.
Przed Urzędem niniejszym stanąwszy oblicznie Maciej Bielaszkowic protestował się przeciw Stanisławowi Nawrockiemu o słowa nieuczciwe y zniewagę [...]"""),

    (17, "fol. 7r (7)", "1671",
     "Dekret S. Nawrocki vs M. Bielaszkowic (14 X 1671); wizja szkód u Łucji Organowej przez świnie sąsiedzkie",
     "Tomasz Pajorowic [?], Stanisław Nawrocki, Maciej Bielaszkowic, Jan Kaczanowski, Paweł Smarowic, Sebastian Balusik, Łucja Organowa, Jan Grymuza, Szymon [sąsiad]",
     "-",
     "Odsyłacz do kwitacji domu Tomasza Pajorowica [?]; sesja z środy przed św. Jadwigą (14 X 1671 r.): dekret w sprawie Stanisława Nawrockiego przeciw Maciejowi Bielaszkowicowi o zniewagi (z dopiskiem o Janie Kaczanowskim); relacja ławników Pawła Smarowica i Sebastiana Balusika z wizji szkód w sadzie i zbożu Łucji Organowej wyrządzonych przez świnie sąsiedzkie (wzmiankowani Jan Grymuza i Szymon).",
     """[fol. 7r]
Quietatio et Resignatio Domus Thomae Paiorowic [?] videatur 7.
Actum feria quarta ante festum S. Hedvigis viduae prox[im]a Anno 1671.
Inter Fam. Stan. Nawrocki actorem et Matthiam Bielaszkowic citatum Decretum.
Na skargę przełożoną przed Sądem Aktora o znieważenie siebie y małżonki swoiej przez pozwanego [...] Sąd nakazuie aby Aktor świadki stawił na piątek przyszły, quod est susceptum et solidatum.
Relat[io] ex Odio Famosi Dni Joannis Kaczanowski [?].
Famati Paulus Smarowic et Sebastianus Balusik deputati ex Officio in vim suae fidelis relationis retulerunt: Iż widzieli w sadzie y na ogrodzie Łucji Organowej szkody przez świnie sąsiedzkie poczynione, przy czym wzmiankowani Jan Grymuza y Szymon [...]"""),

    (18, "fol. 7v (7v)", "1671",
     "Sesja 16 X 1671 r.: obdukcja K. Trojczaka; zeznania dla Ł. Pacanowskiego oraz S. Nawrockiego (Maryna Kotowa, Regina Żydowska)",
     "Krzysztof Trojczak, Ubald Janaszkowicz (wójt), Łukasz Pacanowski, Jan Grymuza, Stanisław Nawrocki, Maryna Kotowa [?], Regina Żydowska [?], Sebastian Balusik",
     "-",
     "Sesja z piątku przed św. Łukaszem (16 X 1671 r.): relacja ławników z ramienia wójta Ubalda o pobiciu Krzysztofa Trojczaka przez Łukasza Pacanowskiego; zeznania świadków ze strony Łukasza Pacanowskiego (o zajściu u Jana Grymuzy); zeznania świadków na rzecz Stanisława Nawrockiego: 1) Maryny Kotowej [?] i 2) Reginy żony Żydowskiego [?].",
     """[fol. 7v]
Actum feria sexta ante festum S. Lucae Apli et Evangel. prox[im]a 1671.
Relatio Dnor. Scabinorum ex parte Cristophori Troiczak.
Na affektacyą Uczciwego Krzysztofa Trojczaka z ramienia Pana Ubalda Wóyta Kraśnickiego oblicznie stawaiący ławnicy [...] et Sebastianus Balusik zeznali: Iż widzieli u niego na głowie y plecach potłuczenie z kijów od Łukasza Pacanowskiego zadane [...]
Testimonia ex parte Lucae Pacanowski.
Ad Instantiam Honesti Lucae Pacanowski Testes iurati: 1mus Testis Joannes [...] zeznał pod przysięgą iż będąc w domu P. Jana Grymuzy przyszedł tamże P. Pacanowski y poczęli się kłócić [...]
Testimonium ex parte Famosi Stanislai Nawrocki.
Ad Instantiam Spectabilis Dni Stanislai Nawrocki testes infrascripti: 1a Testis Honesta Maryna Kotowa [?] sub iuramento praestito zeznała: Gdy szłam koło domu P. Nawrockiego słyszałam słowa nieuczciwe pod adresem P. Nawrockiej [...]
2dus Testis Regina żona Żydowskiego [?] zeznała pod przysięgą takież słowa świadectwa [...]"""),

    (19, "fol. 8r (8)", "1671",
     "Obdukcja ran sługi rajcy G. Foxa (17 X 1671); zeznania w sprawie M. Ratusznego [?]; protestacja A. Łeżyka i Panów Kopców [?] (19 X 1671)",
     "Grzegorz Fox (rajca), Jan (sługa Foxa), Paweł Smarowic, Sebastian Balusik, Piotr Łożycki [?], Matyjasz Ratuszny [?], Wojciech Wnuk, Zofia Kazimierczanka [?], Adam Łeżyk, Matłopka [?], Feliksa [?], Panowie Kopcowie [?], Stanisław Nawrocki",
     "-",
     "Sesja z soboty przed św. Łukaszem (17 X 1671 r.): obdukcja ran Jana, sługi rajcy Grzegorza Foxa, dokonana przez Pawła Smarowica i Sebastiana Balusika (wskazany Piotr Łożycki [?]). Poniżej sesja z poniedziałku po św. Łukaszu (19 X 1671 r.): zeznania Wojciecha Wnuka i Zofii Kazimierczanki [?] w sprawie Matyjasza Ratusznego [?]; protestacja Adama Łeżyka przeciw służącej Matłopce [?]; protestacja Panów Kopców [?] przeciw Stanisławowi Nawrockiemu o dług w Lublinie.",
     """[fol. 8r]
Actum feria Sabbato ante festum S. Lucae Apli et Evang. prox[im]a 1671.
Oblatio vulnerum Joannis famuli Famosi Fox Consulis.
Ad Instantiam Famati Gregorii Fox Consulis Crasnicensis ex brachio officii Famati Paulus Smarowic et Sebastianus Balusik retulerunt: Iż widzieli u Jana sługi pomienionego Pana Foxa rany na głowie y ręce prawej sine spuchłe, które zadał mu Piotr Łożycki [?] [...]

Actum feria 2da post festum S. Lucae Apli et Evangel. prox[im]a 1671.
Testimonia ex parte Matthiae Ratuszny [?].
Wojciech Wnuk będąc przypozwany pod przysięgą zeznał: Słyszałem wielką kłótnię gdy P. Nawrocka wołała na Ratuszną [...]
2da Testis Zofia Kazimierczanka [?] zeznała o temże sporze pod stodołą.
Protestatio Adami Łeżyk.
Przed Urzędem niniejszym stanąwszy Adam Łeżyk protestował się przeciw służącej Matłopce [?] o obmowy y kradzież żyta.
Testes post Matthiam Ratuszny: 3tius Testis Feliksa [?] zeznała o słowach na Ratuszną.
Protestatio Panów Kopców [?] przeciw S. Nawrockiemu o dług lubelski i zaciąg 15 złp."""),

    (20, "fol. 8v (8v)", "1671",
     "Sprawa Żyda Zeldy z Józefem Grotem; T. Łążkowic vs bracia Łążkowicowie z Urzędowa; J. Grymuza vs Ł. Pacanowski; obdukcja A. Giela",
     "Józef Grot, Zelda (Żyd), Wojciech [świadek], Maryna Skórzynka, Grzegorz Stryczkowic [?], Matyjasz Drelik, Bartoszowa Studzińska [?], Tomasz Łążkowic [Łątkowic], Grzegorz Sroka, Jan Grymuza, Łukasz Pacanowski, Paweł Smarowic, Andrzej Giel [?], Sebastian Balusik",
     "-",
     "Zeznania świadków Wojciecha i Maryny Skórzynki w sprawie Józefa Grota przeciw Żydowi Zeldzie; zeznania Matyjasza Drelika i Bartoszowej Studzińskiej [?] dla Grzegorza Stryczkowica [?]; manifestacja Tomasza Łążkowica przeciw braciom Łążkowicom z Urzędowa i Grzegorzowi Sroce; protestacja Jana Grymuzy przeciw Łukaszowi Pacanowskiemu; proces Pawła Smarowica z Tomaszem Łążkowicem; obdukcja ran Andrzeja Giela [?] przez Pawła Smarowica i Sebastiana Balusika.",
     """[fol. 8v]
Testimonia ex parte Josephi Grot contra Zelda Senior[em] Judaeum.
1mus Testis Albertus zeznał pod przysięgą iż widział u Żyda Zeldy zastawione rzeczy od Józefa Grota.
2dus Testis Maryna Skórzynka zeznała iż była w domu u Grota gdy Żyd Zelda przyszedł z sąsiadami.
Protestatio Josephi Grot contra Zelda Judaeum.
Testimonia ex parte Gregorii Stryczkowic [?]. 1mus Testis Matyjasz Drelik zeznał o szkodzie świń P. Pacanowskiego; 2dus Testis Bartoszowa Studzińska [?] zeznała o kopaniu rzepy.
Manifestatio Thomae Łążkowic contra Łążkowicos de Urzędów et con. Gregorium Sroka.
Przed Urzędem niniejszym stanąwszy Tomasz Łążkowic protestował się przeciw braciom swoim z Urzędowa y Grzegorzowi Sroce o podział majątku y pobicie.
Protestatio Joannis Grymuza contra Lucam Pacanowski.
Inrotulatio Pauli Smarowic contra Thomam Łążkowic.
Inter Paulum Smarowic actorem et Thomam Łążkowic citatum.
Vulnera Andreae Giel [?].
Famati Paulus Smarowic et Sebastianus Balusik Scabini Jurati retulerunt: Iż widzieli u Andrzeja Giela [?] rany na głowie y piersiach od kijów zadane."""),

    (21, "fol. 9r (1 / 9)", "1671",
     "Czystopis otwarcia Protokołów (1671): relacje B. Kępki i A. Maraszka; sprawa K. Szklarza z poprawioną datą 1671 (por. #5)",
     "Bartłomiej Kępka, Wojciech Karczewic [?], Paweł Smarowic, Stanisław Nawrocki, Sebastian Balusik, Antoni Maraszek [?], Kazimierz Szklarz, Jan Kowalik, Wdowa Drelikowa, Marcin Rożniatowski [?]",
     "24 kopy",
     "Czystopis akt z fol. 1r (#5) z nową numeracją 1 (fol. 9r): relacja ławników Wojciecha Karczewica [?] i Pawła Smarowica dla Bartłomieja Kępki przeciw Stanisławowi Nawrockiemu; relacja Pawła Smarowica i Sebastiana Balusika dla Antoniego Maraszka; dekret w sprawie Kazimierza Szklarza przeciw Janowi Kowalikowi już pod poprawną datą 1671 r. (na fol. 1r omyłkowo 1670); sprawa wdowy Drelikowej z Marcinem Rożniatowskim [?].",
     """[fol. 9r]
Actum feria 4ta ante festum Exaltat. S. Crucis prox. A. 1671.
Relatio Dnor. Scabinorum ex parte Honesti Bartholomaei Kępka Anteoppidani Crasnicensis.
Famati Albertus Karczewic [?] et Paulus Smarowic Scabini Jurati Crasnicenses in vim suae verae et fidelis relationis recognoverunt: Iż widzieli w polu Uczciwego Bartłomieja Kępki przedmieszczanina kraśnickiego owsa staiko ćwiertni spasione, w ziemię wdeptane, potargane, grochu także kóp nr 24 takie potargane, spasione, winę dał w tey szkodzie Sławetnemu Stanisławowi Nawrockiemu przedmieszczaninowi kraśnickiemu [...]
Relatio Dnor. Scabinorum ex parte Honesti Augustini Maraszek anteoppidani Crasnicensis.
Famati Paulus Smarowic et Sebastianus Balusik Scabini Jurati Crasnicenses retulerunt iż widzieli w ogrodzie Uczciwego Augustyna Maraszka przedmieszczanina kraśnickiego bzu spasionego y potarganego kop nr 6, winę dał P. Sebastianowi Balusikowi [?].

Actum feria sexta ante festum Exaltationis S. Crucis prox[im]a A. 1671.
Inter Honestum Casimirum Stolarz [Szklarz] anteoppidanum Crasnic. actorem et Joannem Kowalik anteoppidanum citatum.
W sprawie o zajęcie i szkodę w owsie zagonów trzydzieści Aktor na pozwanego skarżył się [...] Sąd nakazał aby do piątku miarów dwóch iędrę dwóch zrównali a o więcej szkody się pogodzili.
Inter Hon. Drelikową Viduam actricem et Hon. Martinum Rożniatowski [?] citatum dilatio ad producendos testes concessa."""),

    (22, "fol. 9v (1v / 9v)", "1671",
     "Czystopis wyroków z 16 IX 1671 r.: S. Partyka vs W. Nogai, żona organisty vs A. Łążkowic, Ł. Domitek vs J. Wiatrek, wdowa Drelikowa (por. #7)",
     "Stanisław Partyka, Wojciech Nogai, Łucja Organowa, Augustyn Łążkowic, Wojciech Potocki, Łukasz Domitek [?], Jan Wiatrek [?], Wdowa Drelikowa, Petrykowiczowie",
     "1 grzywna",
     "Czystopis karty fol. 2r (#7): komplet zredagowanych na czysto wyroków sesji z 16 IX 1671 r. (Partyka vs Nogai, żona organisty vs Augustyn Łążkowic, Partyka vs Potocki, Domitek vs Wiatrek o chorego konia, wdowa Drelikowa przeciw synom Petryka o zabicie świni cepami) oraz początek zeznań z 18 IX 1671 r. (Regina Grymuzyna).",
     """[fol. 9v]
[Czystopis wyroków z fol. 2r (#7) pod datą 1671]
[...] pozwany zabiera na świadków że on tej skóry nie brał y nie wie iakim sposobem w iego towar się zamieszała. Sąd niniejszy pozwala dylacyi do piątku przyszłego utrique parti cum termino peremptorio, quod est solidatum.
Inter consortem Organarii actricem et Augustinum Łążkowic citatum dilatio.
Iż pozwany oddał córkę swoią do Aktorki, która dziewczyna odeszła swowolnie y rzeczy niektóre pobrawszy do tąd iey nie widać, a pozwany nie przyznaie się aby o tym wiedział, tedy Sąd niniejszy pozwanemu nakazuie na piątek przyszły iuramentem tego poprawić iako nie wie o tey dziewczynie.
Inter Stanislaum Partyka actorem et Albertum Potocki citatum dilatio ad producendos testes concessa.
Inter Lucam Domitek actorem et Joannem Wiatrek citatum. Sub eodem Actu.
Ponieważ konia tego kupił u pozwanego, a koń iest malikowaty [...] Sąd niniejszy nakazuie aby konia pozwany nazad wziął a za to że nie zaraz oddał pozwanemu ma dać grzywnę ieden.
Inter Actorem partem et Honestam Drelikowa viduam citatam dilatio.
Skarżyła się Aktorka na pozwaną o zabicie świni iey [...]

Actum feria 6ta ante festum S. Matthaei 1671 prox[im]a.
Testimonia ex parte Alberti Nogai anteoppidani Crasnicensis sutoris.
Uczciwa Regina P. Jana Grymuzy Małżonka przypozwana z instancyi W. Nogaia zeznała pod przysięgą o Jarmarku w Urzędowie na Przewodni poniedziałek [...]"""),

    (23, "fol. 10r (2 / 10)", "1671",
     "Czystopis zeznań W. Potockiego dla Nogaja, manifestacji Żyda Wygdora vs A. Pieniążek oraz relacji z 22 IX 1671 r. (por. #8–#9)",
     "Wojciech Nogai, Wojciech Potocki, Stanisław Partyka, Wygdor (Żyd), Andrzej Pieniążek (ślusarz), Błażej Kołodziejczyk, Paweł Smarowic, Stanisław Nawrocki, Adam Łeżyk, Piotr Kępka",
     "14 złp",
     "Czystopis kart fol. 2v–3r (#8–#9): zeznanie Wojciecha Potockiego o kłótni przy wozie z Nogajem i Partyką w Urzędowie; czystopis manifestacji Żyda Wygdora przeciw ślusarzowi Andrzejowi Pieniążkowi; sesja z 22 IX 1671 r. — relacja ławników Błażeja Kołodziejczyka i Pawła Smarowica dla Stanisława Nawrockiego oraz początek protestacji przeciw Adamowi Łeżykowi i Piotrowi Kępce.",
     """[fol. 10r]
[Czystopis z fol. 2v–3r (#8–#9)]
[...] przedał szewc Opolski który wedle niego przedawał skóry swoie y poczęli się rozrzucać [...]
2dus Testis Wojciech Potocki pod przysięgą także zeznał y świadectwo przed Sądem takie wydał mówiąc: Pod czas jarmarku Urzędowskiego byłem ia tam na ten czas y widziałem kiedy Nogai szewc przedawał skóry swoie niedaleko Ratusza, a podle niego zaraz szewc z Opola przedawał skóry swoie [...]
Manifestatio perfidi Wigder contra Andream Pieniążek ferrifaber.
Do Urzędu y Akt niniejszych przyszedłszy niewierny Wygdor Żyd i obywatel kraśnicki czynił manifestacyą przeciw Andrzejowi Pieniążkowi ślusarzowi kraśnickiemu o zastawione rzeczy za czternaście złotych polskich od lat półtora [...]

Actum feria quarta post festum S. Matthaei Evangelistae prox[im]a 1671.
Relatio Dnor. Scabinorum ex parte Stanislai Nawrocki.
Famati Blasius Kołodziejczyk et Paulus Smarowic Scabini Jurati Crasnicenses in vim suae fidelis relationis recognoverunt: Iż widzieli w polu na niwie krakowskiej Sławetnego Stanisława Nawrockiego szkodę poczynioną: owsa zagonów trzy spasione, potargane, jęczmienia kopinę poszarpaną, item iedna kopa tatarki nadeptana, winę dał Adamowi Łeżykowi y Piotrowi Kępce [...]
Protestatio Stanislai Nawrocki contra Adamum Łeżyk et Petrum Kępka."""),

    (24, "fol. 10v (2v / 10v)", "1671",
     "Czystopis protestacji S. Nawrockiego, dekretu dla organisty, wpisu długu 60/65 złp G. Foxa oraz sporu z G. Miecznikiem (por. #9–#10)",
     "Stanisław Nawrocki, Adam Łeżyk, Piotr Kępka, Łucja Organowa, Augustyn Łążkowic, Grzegorz Fox, Szymon Wigozkowic [Wiązkowic], Grzegorz Miecznik [Ensifaber]",
     "60 złp, 65 złp",
     "Czystopis kart fol. 3r–3v (#9–#10): protestacja Stanisława Nawrockiego przeciw Adamowi Łeżykowi i Piotrowi Kępce o odbicie bydła; dekret w sprawie organisty z Augustynem Łążkowicem; rozszerzony wpis długu Grzegorza Foxa na rzecz Bractwa Różańcowego (zapisany na 60 złp / 65 złp w brulionie było 30 złp); sprawa Szymona Wigozkowica przeciw Grzegorzowi Miecznikowi.",
     """[fol. 10v]
[Czystopis z fol. 3r–3v (#9–#10)]
[...] swoim się oświadczył y protestował na przeciwko Uczciwym Adamowi Łeżykowi y Piotrowi Kępce [...]
Actum feria quarta post festum S. Matthaei Evangelistae prox[im]a 1671.
Inter Kresowski [?] Organarium Actorem et Augustinum Łążkowic citatum Decretum.
Sąd niniejszy wysłuchawszy obydwu stron iż się to pokazało że pozwany oddał córkę swoią aktorowi [...]
Gregorius Fox recognoscit debitum suum Confraternitati SSmi Rosarii.
Famatus Gregorius Fox proconsul Crasnicensis coram Officio Advocatiali et Scabinali Crasnicensi sponte et libere recognovit se debere Confraternitati SSmi Rosarii summam florenorum sexaginta [60 złp; poniżej dopisano: summam recensitam fl. 65] in anno proximo venturo 1672 persolvendam et in bonis suis propriis assecuravit.
Inter Simonem Wigozkowic actorem et Gregorium ensifabrum citatum.
Ponieważ pozwany sam przyznaje się aktorowi że mu za rok komornego nie oddał [...]
Inter Stan. Nawrocki actorem et Adamum Łeżyk et Petrum Kępka citatos."""),

    (25, "fol. 11r (3 / 11)", "1671",
     "Czystopis zeznań S. Magierowskiego, dekretu M. Kępki vs A. Łeżyk, manifestacji A. Strowskiego i zeznań Kozińskich (25 IX 1671, por. #10–#11)",
     "Stanisław Magierowski, Stanisław Partyka, Wojciech Nogai, Wojciech Potocki, Matyjasz Kępka, Adam Łeżyk, Aleksander Strowski, Jan Zan, Katarzyna Kozińska, Paweł Koziński, Stanisław Koziński, Stanisław Nawrocki, Piotr Kępka",
     "-",
     "Czystopis kart fol. 3v–4r (#10–#11): zeznanie Stanisława Magierowskiego na rzecz Stanisława Partyki; dekret akcesoryjny Matyjasza Kępki vs Adam Łeżyk; manifestacja Aleksandra Strowskiego w imieniu JMP Podkomorzego Koronnego przeciw poddanym Żatkom z Budzyna (dzierżawa JMP Zana); początek sesji z 25 IX 1671 r. z zeznaniami Katarzyny i Stanisława Kozińskich dla Stanisława Nawrockiego.",
     """[fol. 11r]
[Czystopis z fol. 3v–4r (#10–#11)]
Testimonium ex parte Stanislai Partyka.
Uczciwy Stanisław Magierowski będąc przypozwany przed Sąd niniejszy Wóytowski y Ławniczy na instancyą Stanisława Partyki podniósłszy dwa palce do góry zeznał pod przysięgą o jarmarku w Urzędowie na Przewodnią niedzielę [...]
Decretum accessorium inter Matthiam Kępka actorem et Adamum Łeżyk citatum.
Ex decreto praesentis Officii superlato aby pozwany na piątek blisko przyszły ze wszystką gotowością stanął [...]
Manifestatio Alexandri Strowski ex parte Żatków [Łatków].
Do Urzędu i Akt niniejszych Wóytowskich y Ławniczych stanąwszy oblicznie Alexander Strowski sługa JW JMP Podkomorzego Koronnego Starosty Urzędowskiego opowiedział się iż poddani z Budzyna z dzierżawy JMP Zana nie stanęli do przysięgi [...]

Actum feria 6ta ante festum S. Michaelis Archangeli prox[im]a Ao 1671.
Testimonium ex parte Stanislai Nawrocki.
Uczciwa Katarzyna P. Pawła Kozińskiego małżonka przypozwana przed Urząd niniejszy zeznała pod przysięgą iż we wtorek do dnia widziała że P. Nawrocki zaimował z swego pola woły [...]
2dus Testis Młodzieniec Stan. Koziński także pod przysięgą zeznał [...]""")
]

main_data = []
for nr, pagina, rok, kat, osoby, kwoty, opis, trans in raw_scans:
    main_data.append({
        "nr_skanu": nr,
        "numer_pozycji": str(nr),
        "strona_pagina": pagina,
        "sygnatura": SYGN,
        "data_rok": rok,
        "kategoria": kat,
        "osoby_podmioty": osoby,
        "kwoty_podatki": kwoty,
        "opis_pozycji": opis,
        "kwoty_miary": kwoty,
        "transkrypcja": trans,
        "link_swa": LINK_SWA
    })

with open("main_data_j21_part1.json", "w", encoding="utf-8") as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j21_part1.json: {len(main_data)} skanow.")
