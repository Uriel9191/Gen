# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j19_part2.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989899"

part3_scans = [
    {
        "nr_skanu": 51,
        "numer_pozycji": "51",
        "strona_pagina": "fol. 23v (dublet skanu #50)",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Elekcja Magistratu 1659 / Dublet mikrofilmowy skanu #50",
        "osoby_podmioty": "Jan Zamoyski (wojewoda sandomierski), Krzysztof Brzozowski [Brzostowski?] (podczaszy czernihowski, tenutariusz kraśnicki), Maciej Tharasa (rajca i burmistrz), Marcin Sitarski (rajca), Stanisław Nawrocki (rajca), Wojciech Kurowic (rajca), Sebald [Ubald/Albert] Janaszkowic (wójt), Marcin Starzyński (ławnik), Błażej Kołodziejczyk (ławnik), Stanisław Sienkowic (ławnik), Jan Chmielowic (ławnik), Maciej Kozica (ławnik), Grzegorz Fox [Joch?] (ławnik), Jan Cichoń (pisarz)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "[Dublet mikrofilmowy skanu #50 (fol. 23v)] Identyczne ujęcie karty fol. 23v z Elekcją Magistratu Kraśnickiego z 1659 r.: powołanie rajców rezydentów (Macieja Tharasy, Marcina Sitarskiego, Stanisława Nawrockiego, Wojciecha Kurowica), wójta Sebalda [Ubalda] Janaszkowica oraz ławników i pisarza Jana Cichonia.",
        "transkrypcja": """--- Skan #51 (fol. 23v) — [Dublet mikrofilmowy skanu #50] ---
23v
ELECTIO 1659.
Sollennis et Laudabilis Magistratus Civitatis Crasnicensis in praesentia
totius Communitatis et consuetudine antiqua celebrata feria quinta ante Festum
S. Agnetis Virginis et Martyris Anno Domini Millesimo Sexcentesimo Quinquagesimo Nono.

Et inprimis ex Benigna Voluntate et Magnifici Domini D. Joannis de
Zamoście Zamoyski Palatini Sandomiriensis Domini Nostri Illustrissimi Clementissimi
Generosus ac Magnificus D. Christophorus Brzozowski [Brzostowski?] Pocillator Czernichoviensis
Tenutarius pro tunc Crasnicensis elegit duos Consules Residentes
Famatum D. Mathiam Tharasa et Famatum D. Martinum Sitarski.
Advocatus cum Scabinis loci suo assidentes Archi-Magistris Contuberniorum
totaque Communitate confirmaverunt in Consulem Residentem Famatum D.
Stanislaum Nawrocki. Qui quidem Consules more solito electi et confirmati
adsciverunt sibi quartum Consulem Residentem Famatum D. Albertum Kurowic.
In Advocatum vero et Judicem Ordinarium pro tunc Crasnicensem Praeconsul
cum Consulibus Residentibus Archi-Magistris Magistri totius Communitatis elegerunt
et constituerunt Famatum D. Sebaldum [Ubaldum] Janaszkowic. Quem Generosus
ac Magnificus Dominus in tota Communitate Ordinavit, approbavit et confirmavit.
Scabini antiqui: Martinus Starzyński, Blasius Kołodziejczyk, Stanislaus
Sienkowic, Joannes Chmielowic, Mathias Kozica, et Gregorius Fox [Joch?],
ad quos propter plenam rationem Honestus Dominus Joannes Cichoń Notarius
pro tunc Juratus elegerunt et constituerunt, qui quidem supra Officio Scabinali
suo corporale juramentum juxta rotam in jure descriptam praestiterunt.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 52,
        "numer_pozycji": "52",
        "strona_pagina": "fol. 24r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Elekcja 1659 (dok.) / Sąd Radziecki: długi i rozliczenia",
        "osoby_podmioty": "Jan Skarzyk [Skarzyński?], Maciej Jarzębek [?], Szymon Kowalik, Zofia Pezikówna (żona Szymona Kowalika), Jan Batusik [Batuś], Jakub Dzek [Rzepka?], Marcin Sitarski (rajca), Jan Soszyński [Soczyński?]",
        "kwoty_podatki": "30 złp, 6 fl 6 gr",
        "opis_sprawy": "Dokończenie Elekcji 1659 r.: powołanie egzaktorów do składek publicznych (Jan Skarzyk [Skarzyński?] i Maciej Jarzębek [?]); sesja z soboty po Oczyszczeniu NMP 1659 r. (8 II): sprawa Szymona Kowalika i żony Zofii Pezikówny przeciw Janowi Batusiowi o 30 złp po Jakubie Dzeku [Rzepce?] (odesłanie do dekretu z 1658 r.); poniżej sesja z soboty po Popielcu 1659 r. (1 III): sprawa rajcy Marcina Sitarskiego przeciw Janowi Soszyńskiemu [Soczyńskiemu?] o 6 fl 6 gr długu za skóry szewskie.",
        "transkrypcja": """--- Skan #52 (fol. 24r) ---
24. 1659
In Assessorem ad Judicia Civilia Tribus Parochis Famatus Gregorius Fox [Joch?]
et Notarius Joannes Cichoń constituti sunt.
Absoluta Electione Famatus D. Stanislaus Nawrocki Officium
Proconsulatus una cum Thesauris Reipublicae suscepit.
Post in Domo Famati Proconsulis Archi-Magistri una cum Societate taliter
sunt electi:
Pellionum: Famatus Mathias Tharasa Consul Crasnicensis.
Sutorum: Famatus Martinus Sitarski Consul Crasnicensis.
Sartorum: Honestus Paulus Chmara Civis Crasnicensis.
Fabrorum: Honestus Simon Szarek Civis Crasnicensis.
Textorum: Honestus Bartholomaeus Kozicki Civis Crasnicensis.
Exactores ad Exactiones publicas Joannes Skarzyk [Skarzyński?] et Mathias Jarzębek [?] electi et constituti.

Actum Coram Officio Consulari Sabbato post Festum Purificationis
B. M. Virginis proximo Anno Domini 1659.
Inter Honestum Simonem Kowalik et Zophiam Pezikówna consortem ejus Actores
ac Honestum Joannem Batuś Citatum.
Ponieważ się Sąd przychyla do dekretu swego przeszłorocznego w roku 1658
ferowanego względem trzydziestu złotych u Jakuba Dzeka [Rzepki?]...
aby pozwany Jan Batuś dokumenty z Krakowa y Lublina o wkładzie
swoim pokazał pod utraceniem sprawy. Quod Decretum ab utraque parte susceptum est.

Actum Coram Officio Consulari Sabbato post Cineres 1659.
Inter Famatum D. Martinum Sitarski Consulem Crasnicensem Actorem
ac Honestum Joannem Soszyński [Soczyński?] Citatum.
Ponieważ pozwany przyznaje długu złotych sześć y groszy sześć
za skóry szewskie u Powoda wzięte, tedy Sąd nakazuje aby na
przyszłą sobotę pod egzekucyją zapłacił.

Actum Coram Officio Consulari feria sexta ante Dominicam Judica 1659.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 53,
        "numer_pozycji": "53",
        "strona_pagina": "fol. 24v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Sąd Radziecki / Sprawy spadkowe Pezików i długi Batusika",
        "osoby_podmioty": "Szymon Kowalik, Zofia Pezikówna (żona Szymona Kowalika), Jan Batusik [Batuś], Adam Kubak [?], Bartłomiej Kołodziejczyk, Sebastian Pezik, Wawrzyniec Pezik, Anna Pezikówna, Maryna Pezikówna, Katarzyna Pezikówna",
        "kwoty_podatki": "10 złp, 20 złp, 30 złp",
        "opis_sprawy": "Sesja z piątku przed Niedzielą Judica 1659 r. (28 III): (1) dekret dla Szymona Kowalika i żony Zofii Pezikówny przeciw Janowi Batusiowi o zapłatę 10 złp (z 30 złp) w gotówce pod karą więzienia; (2) sprawa Jana Batusika przeciw Adamowi Kubakowi [?] i Bartłomiejowi Kołodziejczykowi, sukcesorom po Sebastianie, Wawrzyńcu, Zofii, Annie, Marynie i Katarzynie Pezikach z 1649 r., o rozliczenie spadku na 20 złp i 10 złp.",
        "transkrypcja": """--- Skan #53 (fol. 24v) ---
24v
Inter Honestum Simonem Kowalik et Zophiam Pezikówna Actores
ac Honestum Joannem Batuś Citatum.
Ponieważ pozwany Jan Batuś nie pokazał dostatecznego dokumentu z Lublina
ani z Krakowa jako obiecał, przeto Sąd nakazuje aby na przyszły piątek
przed Niedzielą Palmową zapłacił Powodom złotych dziesięć z trzydziestu złotych
gotowizną pod karą więzienia y egzekucyją.

Inter Joannem Batusik Actorem ac Adamum Kubak [?] et Bartholomaeum Kołodziejczyk
Citatum successores post olim Sebastianum, Laurentium, Zophiam, Annam,
Marinam et Catharinam Peziki anno 1649.
Sąd nakazuje aby pozwani według dawnego zapisu z roku 1649
uczynili rozliczenie ze spadku po Pezikach, to jest złotych dwadzieścia
y złotych dziesięć na terminie przyszłym pod winą urzędową.
Quod Decretum ab utraque parte susceptum est.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 54,
        "numer_pozycji": "54",
        "strona_pagina": "fol. 25r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Sąd Radziecki i Łączony / Dług z cyrografu i przyjęcia prawa miejskiego",
        "osoby_podmioty": "Jan Batusik, Jan Kulka, Sebastian Jasiński, Bartłomiej Jasiński (śp.), Józef Sobol, Paweł Stockowski [Słomkowski?], Bartłomiej Delygerski [?], Grzegorz Kilian",
        "kwoty_podatki": "18 złp kapitału, 6 fl 20 gr procentu",
        "opis_sprawy": "Dokończenie dekretu Jana Batusika; sprawa opiekunów Jana Kulki i Sebastiana Jasińskiego (brata śp. Bartłomieja Jasińskiego) przeciw Józefowi Sobolowi o 18 złp pożyczonych pieniędzy oraz 6 fl 20 gr procentu wg cyrografu z 19 IX 1655 r. (wyrok na zapłatę procentu na św. Wojciecha); sesja z piątku przed Niedzielą Palmową 1659 r. (4 IV): przyjęcie prawa miejskiego magdeburskiego przez Pawła Stockowskiego [Słomkowskiego?], Bartłomieja Delygerskiego [?] i Grzegorza Kiliana; na dole nagłówek Sądu Łączonego z piątku przed Niedzielą Przewodnią 1659 r. (18 IV).",
        "transkrypcja": """--- Skan #54 (fol. 25r) ---
25. 1659
...Jan Batusik w sprawie przeciw sukcesorom Pezików do wykonania dekretu.

Inter Tutores Joannem Kulka et Sebastianum Jasiński fratrem olim Bartholomaei Jasiński
Actores ac Honestum Josephum Sobol Citatum.
Powodowie pokazali cyrograf z dnia 19 Septembris 1655 roku na złotych ośmnaście
pożyczonych pieniędzy z procentem złotych sześć y groszy dwadzieścia.
Pozwany Józef Sobol dług przyznaje. Sąd nakazuje aby na dzień św. Wojciecha
procent 6 fl 20 gr zapłacił, a kapitał 18 złp na terminie opisanym.

Actum Coram Officio Consulari feria sexta ante Dominicam Palmarum 1659.
Honestus Paulus Stockowski [Słomkowski?], Bartholomaeus Delygerski [?]
et Gregorius Kilian Jus Civile Magdeburgense susceperunt, juramentumque
corporale juxta rotam praestiterunt. Quod Actis inscribi petierunt.

Actum Coram Officio Composito Consulari Advocati et Scabinorum Juratorum
Crasnicensium feria sexta ante Dominicam Conductus Paschae 1659.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 55,
        "numer_pozycji": "55",
        "strona_pagina": "fol. 25v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Przekazanie burmistrzostwa / Długi / Kupno placu przez Żyda Mosia Srulowicza",
        "osoby_podmioty": "Stanisław Nawrocki (ustępujący burmistrz), Maciej Tharasa (nowy burmistrz), Łukasz Dudek (z Piasków), Józef Sobol, Żyd Dawidek, Żyd Lejzor, Żyd Moś Srulowicz [?], Wojciech Batusik, Agnieszka Batusikowa, Jan Pielaszkowic (sąsiad), Żyd Izaak Łobódka (sąsiad)",
        "kwoty_podatki": "7 złp, 3 złp 13 gr",
        "opis_sprawy": "Translatio Proconsulatus z piątku przed Niedzielą Przewodnią 1659 r. (18 IV) od Stanisława Nawrockiego do Macieja Tharasy w obecności cechu szewskiego; sesja z piątku po Niedzieli Rogationum 1659 r.: sprawa pracowitego Łukasza Dudka z Piasków przeciw Józefowi Sobolowi o 7 złp za owies oraz sprawa Żyda Dawidka przeciw Żydowi Lejzorowi o 3 złp 13 gr do zachodu słońca; poniżej ze środy po Rogationum 1659 r.: Mancipatio Infidelis Judaei Mosi Srulowicza [?] cum Alberto Batusik — kupno przez starozakonnego Mosia od Wojciecha Batusika i jego żony Agnieszki placu przy ulicy Lubelskiej między placem Jana Pielaszkowica a domem Żyda Izaaka Łobódki.",
        "transkrypcja": """--- Skan #55 (fol. 25v) ---
25v
Translatio Proconsulatus a Famato D. Stanislao Nawrocki ad Famatum D. Mathiam Tharasa
in praesentia Cechi Sutorum et totius Communitatis juxta ritum et consuetudinem antiquam.

Actum Coram Officio Consulari feria sexta post Dominicam Rogationum 1659.
Inter Laboriosum Lucam Dudek de Piaski Actorem ac Josephum Sobol Citatum.
Powód upomina się złotych siedm za owies. Pozwany przyznaje y na przyszły
piątek zapłacić powinien.

Inter Infidelem Judaeum Dawidek Actorem ac Infidelem Judaeum Lejzor Citatum.
O dług złotych trzy y groszy trzynaście. Sąd nakazuje aby pozwany
do zachodu słońca zapłacił pod egzekucyją.

Actum feria quarta post Dominicam Rogationum 1659.
Mancipatio Infidelis Judaei Mosi Srulowicza [?] cum Alberto Batusik.
Przed Urzędem niniejszym Radzieckim Kraśnickim oblicznie stanąwszy Uczciwy
Wojciech Batusik y Agnieszka małżonkowie z jednej, a Niewierny Moś Srulowicz [?]
Żyd Kraśnicki z drugiej strony zeznali dobrowolnie iż sprzedali plac swój
przy ulicy Lubelskiej między placem Jana Pielaszkowica z jednej a domem
Żyda Izaaka Łobódki z drugiej strony leżący za sumę...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 56,
        "numer_pozycji": "56",
        "strona_pagina": "fol. 26r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Sąd Radziecki / Kupno domu na Przedmieściu przez Wawrzyńca Chudzika",
        "osoby_podmioty": "Żyd Moś Srulowicz [?], Wojciech Batusik, Marcin Serwacy [?], Bartłomiej Świderek, Zofia Rzeczycka [?] (córka Świderka), Wawrzyniec Chudzik, Katarzyna Kępianka (żona Chudzika), Matyjasz Gołąbek (sąsiad), Wojciech Szafraniec (sąsiad)",
        "kwoty_podatki": "100 złp [?], 1 zł wpisu, 30 złp [?]",
        "opis_sprawy": "Dokończenie sprzedaży placu Żydowi Mosiowi (wzmianka o Marcinie Serwacim [?], 100 złp [?] i 1 zł wpisu); sesja z czwartku w dzień Wniebowstąpienia Pańskiego 1659 r. (22 V): Mancipatio Laurentii Chudzik cum Bartholomaeo Świderek — sprzedaż domu z placem na Przedmieściu (na Kurgu Rzeczyckim [?] między Matyjaszem Gołąbkiem a folwarkiem Wojciecha Szafrańca) przez Bartłomieja Świderka i córkę Zofię Rzeczycką [?] Wawrzyńcowi Chudzikowi i jego żonie Katarzynie Kępiance za 30 złp [?].",
        "transkrypcja": """--- Skan #56 (fol. 26r) ---
26. 1659
...sumę złotych sto [?] którą to sumę przedawczyk od Żyda Mosia odebrał
przy bytności Marcina Serwacego [?] y z niej go kwituje, płacąc od wpisu złoty jeden.

Actum Coram Officio Consulari ipso die Festo Ascensionis Domini 1659.
Mancipatio Laurentii Chudzik cum Bartholomaeo Świderek.
Przed Urzędem Radzieckim Kraśnickim stanąwszy oblicznie Uczciwy
Bartłomiej Świderek wraz z córką swoją Zofiją Rzeczycką [?] zeznali
iż sprzedali dom z placem swoim na Przedmieściu na Kurgu Rzeczyckim [?]
między domem Matyjasza Gołąbka z jednej a folwarkiem Wojciecha Szafrańca
z drugiej strony leżący Uczciwemu Wawrzyńcowi Chudzikowi y małżonce jego
Katarzynie Kępiance za sumę złotych trzydzieści [?] monety polskiej...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 57,
        "numer_pozycji": "57",
        "strona_pagina": "fol. 26v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Sąd Radziecki i Łączony / Protestacja burmistrza Tharasy przeciw rajcy Sitarskiemu",
        "osoby_podmioty": "Maciej Tharasa (burmistrz), Marcin Sitarski (rajca), Jan Kłodnicki [Kłodczyński?] (ławnik), Maciej Kozica (ławnik), Wojciech Szafraniec [Szafrankowic], Wawrzyniec Sydkowic",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie transakcji Chudzik–Świderek (opisy granic i uwolnienie od ciężarów); sesja z niedzieli po Wniebowstąpieniu 1659 r. (25 V): protestacja burmistrza Macieja Tharasy przeciw rajcy Marcinowi Sitarskiemu o najście i rękoczyn w domu burmistrza w obecności ławników Jana Kłodnickiego [Kłodczyńskiego?] i Macieja Kozicy (zranienie palca ożogiem bez krwawej rany); poniżej z wtorku po Św. Trójcy 1659 r. (10 VI): protestacje Wojciecha Szafrankowica [Szafrańca] i burmistrza Macieja Tharasy przeciw Wawrzyńcowi Sydkowicowi.",
        "transkrypcja": """--- Skan #57 (fol. 26v) ---
26v
...od wszelakich długów y ciężarów wolnym czyni, które prawo na potomki
y sukcesory swoje wiecznymi czasy przenosi y do Akt niniejszych wpisuje.

Actum die Dominico post Festum Ascensionis Christi Domini 1659.
Famatus D. Mathias Tharasa Proconsul Crasnicensis Prostat contra
Famatum Martinum Sitarski Consulem Crasnicensem.
Sławetny P. Mathias Tharasa Burmistrz natenczas Rezydujący Kraśnicki
zaprowadzony do siebie do domu stawił się przed Pany Ławniki Przysięgłymi
Kraśnickimi Janem Kłodnickim [Kłodczyńskim?] y Macieja Kozicy oświadczając się
przed nimi przeciw Panu Marcinowi Sitarskiemu Rajcy Kraśnickiemu Koledze swemu,
oto iż przyszedłszy ożogiem w ręku będącym w domu moim uderzył mnie w rękę,
palec ożogiem stłukł sine krwawią raną. Oświadczywszy się o to wszystko
zapisuje protestacyją do Akt niniejszych.

Actum Coram Officio Composito Die Martis S. Trinitatis 1659.
Famatus Dominus Albertus Szafrankowic [Szafraniec] Prostat contra
Laurentium Sydkowic quam separata copia porrigere petit.
Eodem die Famatus D. Mathias Tharasa Proconsul cum protestatione
contra eundem Laurentium Sydkowic...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 58,
        "numer_pozycji": "58",
        "strona_pagina": "fol. 27r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Przekazanie burmistrzostwa / Długi / Protestacja pisarza Cichonia",
        "osoby_podmioty": "Wawrzyniec Sydkowic, Maciej Tharasa (ustępujący burmistrz), Wojciech Kurowic (nowy burmistrz), Wojciech Szafraniec [Szafrankowic], Jadwiga Zaciągkowicz [Zaleźbiorz?], Łukasz (śp.), Sebastian, Andrzej Lotwa [Łotwa?], Jan Cichoń (pisarz aktowy), Marcin Kotlarzyk alias Olkowski",
        "kwoty_podatki": "5 fl 10 gr, 2 fl 15 gr, 5 złp",
        "opis_sprawy": "Dokończenie protestacji przeciw Wawrzyńcowi Sydkowicowi; sesja Sądu Łączonego z piątku po św. Janie Chrzcicielu 1659 r. (27 VI): Translatio Proconsulatus od Macieja Tharasy do Wojciecha Kurowica; sesja z piątku przed św. Michałem 1659 r. (26 IX): sprawy Wojciecha Szafrankowica [Szafrańca] przeciw Jadwidze Zaciągkowicz [Zaleźbiorz?] o 5 fl 10 gr długu oraz przeciw Andrzejowi Lotwie [Łotwie?] o 5 złp pożyczki; na dole sesja z poniedziałku w dzień św. Michała (29 IX): protestacja pisarza Jana Cichonia przeciw Marcinowi Kotlarzykowi alias Olkowskiemu.",
        "transkrypcja": """--- Skan #58 (fol. 27r) ---
27.
Laurentius Sydkowic de Sextis... ut supra in protestatione separata copia...

Actum Coram Officio Composito Consulari Advocatiali et Scabinali
feria sexta post Festum Gloriosi S. Joannis Baptistae 1659.
Translatio Proconsulatus a Famato D. Mathia Tharasa ad Famatum D. Albertum Kurowic
in praesentia Cechi Magistrorum Scultetorum [Sutorum?] Suburbii et totius Communitatis
cum omnibus thesauris Civilibus juxta ritum et consuetudinem antiquam.

Actum feria sexta ante Festum S. Michaelis Archangeli 1659.
Inter Famatum D. Albertum Szafrankowic Advocatum antiquum praesentem Actorem
ac Honestam Hedvigim Zaciągkowicz [Zaleźbiorz?] Citatam.
O dług fl 5 gr 10 winy po Łukaszu... Sąd nakazuje aby zapłaciła,
odłożywszy 2 fl 15 gr które Sebastian oddał.

Inter eundem Actorem ac Honestum Andream Lotwa [Łotwa?] Citatum.
O dług złotych pięć winy pożyczanych. Sąd nakazuje aby na przyszły termin zapłacił.

Actum feria secunda ipso die Festo S. Michaelis Archangeli 1659.
Famatus Joannes Cichoń Notarius Actorum praesens personaliter prostat
contra Ingenuum Martinum Kotlarzyk alias Olkowski.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 59,
        "numer_pozycji": "59",
        "strona_pagina": "fol. 27v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Sąd Radziecki / Protestacja pisarza Cichonia przeciw Olkowskiemu i dług Trojaka",
        "osoby_podmioty": "Jan Cichoń (pisarz aktowy), Marcin Olkowski [Kotlarzyk], Wojciech Kiełbic [Kłobucki?], P. Berniszkowicz [Bernyszowicz?], Wojciech Szafraniec [Szafrankowic], Krzysztof Trojak (przedmieszczanin)",
        "kwoty_podatki": "12 gr, 19 fl 18 gr",
        "opis_sprawy": "Ciąg dalszy obszernej polskiej protestacji pisarza aktowego Jana Cichonia przeciw Marcinowi Olkowskiemu (Kotlarzykowi) o spór dotyczący listu i pieniędzy (12 gr) przy udziale P. Wojciecha Kiełbica [Kłobuckiego?] i P. Berniszkowicza [Bernyszowicza?], z cytowanymi dialogami o Lwowie i Kraśniku; poniżej sesja z czwartku po św. Franciszku 1659 r. (9 X): sprawa Wojciecha Szafrankowica [Szafrańca] przeciw przedmieszczaninowi Krzysztofowi Trojakowi o dług 19 fl 18 gr.",
        "transkrypcja": """--- Skan #59 (fol. 27v) ---
27v 1659
Ad Officium Consulare personaliter veniens Famatus Joannes Cichoń Notarius Actorum
protestatur contra Ingenuum Martinum Olkowski idque propter...
P. Wojciecha Kiełbica [Kłobuckiego?] z Urzędowa... przeciwko temu Marcinowi Olkowskiemu,
który gdy przyszedł do mnie pytał się za co 12 gr wziął P. Berniszkowicz [Bernyszowicz?].
A ten odpowiedział że w mieście przy ludziach... i nie chciał dać listu,
a on mu odpowiedział: daleko oko głowy we Lwowie, gdzie idziesz do Krakowa,
ale tu w Kraśniku oświadczę się z prawdą przed P. Burmistrzem...
kiedykolwiek się tu do Kraśnika zatrąci prawnie...

Actum feria quinta post Festum S. Francisci Confessoris 1659.
Inter Famatum D. Albertum Szafrankowic Advocatum antiquum praesentem Actorem
ac Honestum Christophorum Trojak anteoppidanum praesentem Citatum.
Ponieważ się ten Citat poddał Aktorowi dług fl 19 gr 18 winny za cztery...
płacić za niedziel dwie, tedy Urząd przyjmuje submissyję jego.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 60,
        "numer_pozycji": "60",
        "strona_pagina": "fol. 28r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Sąd Radziecki i Łączony / Długi, prawo miejskie i przekazanie burmistrzostwa",
        "osoby_podmioty": "Krzysztof Trojak, Wojciech Szafraniec [Szafrankowic], Marcin Jach [?], Piotr Dzionek, Jan Rzepka (woźny), Wojciech Zaziębek [?], Wojciech Kurowic (ustępujący burmistrz), Marcin Sitarski (nowy burmistrz)",
        "kwoty_podatki": "9 fl, 5 fl",
        "opis_sprawy": "Dokończenie dekretu Krzysztofa Trojaka; sprawa Wojciecha Szafrankowica przeciw przedmieszczaninowi Marcinowi Jachowi [?] o 9 fl; relacja woźnego Jana Rzepki w sprawie Piotra Dzionka przeciw Wojciechowi Szafrankowicowi o dług 5 fl; przyjęcie prawa miejskiego przez Wojciecha Zaziębka [?]; sesja Sądu Łączonego z wtorku w wigilię św. Jadwigi 1659 r. (14 X): Translatio Proconsulatus od Wojciecha Kurowica do Marcina Sitarskiego.",
        "transkrypcja": """--- Skan #60 (fol. 28r) ---
28. 1659
...vigore sui Decreti approbat... za dwie niedzieli pod egzekucyją zapłacić.

Inter eundem Actorem ac Honestum Martinum Jach [?] anteoppidanum Citatum.
O dług fl 9 winny Aktorowi od Pozwanego. Sąd niniejszy nakazuje
aby sumę do rąk Aktora jako się godzi zapłacił sub poena Officii.

Petrus Dzionek Coronatus ad instantiam Famati Alberti Szafrankowic.
Joannes Rzepka Bedellus Officii Juratus fecit relationem ad instantiam
Famati Alberti Szafrankowic Advocati antiqui contra Petrum Dzionek
de debitis fl 5... in poenam condemnationis pronuntiatus est.

Honestus Albertus Zaziębek [?] Jus Civile suscepit, juramentumque
juxta rotam in jure descriptam praestitit.

Actum Coram Officio Composito Consulari Advocati et Scabinorum
simul Crasnicensi feria tertia in Vigilia Festi S. Hedvigis proxima Anno Domini 1659.
Translatio Proconsulatus a Famato D. Alberto Kurowic ad Famatum
D. Martinum Sitarski in praesentia Cechi Magistrorum Scultetorum [Sutorum?] Suburbii
et totius Communitatis cum omnibus thesauris Civilibus juxta ritum et consuetudinem antiquam.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 61,
        "numer_pozycji": "61",
        "strona_pagina": "fol. 28v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Sąd Radziecki / Spór o część gruntu po Katarzynie Kamieńczance",
        "osoby_podmioty": "Wojciech Szafraniec [Szafrankowic], Krzysztof Trojak, Bartłomiej Świderek, Wawrzyniec Świniarz, Katarzyna Kamieńczanka [Kamieńska?], Małgorzata (siostra?), Monika Kościekowska [?] (wdowa), szl. Piotr Świątek [?]",
        "kwoty_podatki": "19 fl 18 gr, 10 złp",
        "opis_sprawy": "Dokończenie sprawy Krzysztofa Trojaka o 19 fl 18 gr (odesłanie do brzegu lubelskiego); sesja z środy przed Ofiarowaniem NMP 1659 r. (19 XI): sprawa Bartłomieja Świderka przeciw Wawrzyńcowi Świniarzowi o spadek i 10 złp po Katarzynie Kamieńczance [Kamieńskiej?] (zeznania dwóch świadków o podziale gruntu); poniżej sesja Sądu Łączonego z wtorku po św. Tomaszu Apostole 1659 r. (23 XII): sprawa wdowy Moniki Kościekowskiej [?] przeciw szl. Piotrowi Świątkowi [?].",
        "transkrypcja": """--- Skan #61 (fol. 28v) ---
28v 1659
Inter Famatum Albertum Szafrankowic Advocatum antiquum Actorem
ac Honestum Christophorum Trojak Citatum.
Ponieważ Citat nie uczynił zadość Dekretowi y Aktorowi nie zapłacił
długu fl 19 gr 18, tedy Sąd nakazuje aby na Brzegu Lubelskim złożył...

Actum Coram Officio Consulari feria quarta ante Festum Presentationis B. M. Virginis 1659.
Inter Honestum Bartholomaeum Świderek Actorem ac Laurentium Świniarz Citatum.
Fundując się na zeznaniu dwóch świadków ex parte Citati produkowanych,
którzy sub juramento zeznali że Katarzyna Kamieńczanka [Kamieńska?] młodszą będąc...
przed śmiercią zapisała tę sumę fl 10 która należy Katarzynie Kamieńczance
a po śmierci bratu lub siostrze Małgorzacie... aby jej powróciła część swej
sumy złotych dziesiątka. Quod Decretum ab utraque parte susceptum est.

Actum Coram Officio Composito Consulari Advocati et Scabinorum
feria tertia post Festum S. Thomae Apostoli proxima Anno Domini 1659.
Inter Viduam Monicam Kościekowską [?] Actricem ac Nobilem Petrum Świątek [?] Citatum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 62,
        "numer_pozycji": "62",
        "strona_pagina": "fol. 29r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Sąd Radziecki / Sprawa o atestację Stanisława Grasia z Borowa",
        "osoby_podmioty": "Monika Kościekowska [?], szl. Piotr Świątek [?], Stanisław Graś (poddany ze wsi Borów), Żyd Jakub Jakubowicz, P. Czerszczyński [Czerwieński?], Tkacz (mieszczanin?)",
        "kwoty_podatki": "60 złp",
        "opis_sprawy": "Dokończenie dekretu wdowy Moniki Kościekowskiej [?] przeciw szl. Piotrowi Świątkowi [?] (sumy 60 złp z dekretu z 1658 r. za zboże, konie i bydło); sesja z 28 XII 1659 r. (święto św. Młodzianków): zeznanie pracowitego Stanisława Grasia poddanego ze wsi Borów przeciw Żydowi Jakubowi Jakubowiczowi o atestację wydaną dwóm chłopom od Tkacza przez P. Czerszczyńskiego [Czerwieńskiego?].",
        "transkrypcja": """--- Skan #62 (fol. 29r) ---
29. 1659
Inhaerendo Decreto Officii Consulari sub Anno 1658...
sumę złotych sześćdziesiąt fl 60 winien oddać według dekretu,
y teraz na dalszym terminie okazuje za zboże, konie y bydło...
Quod Decretum ab utraque parte susceptum est.

Actum Coram Officio Consulari ipso die Festo SS. Innocentum proximo 1659.
Testimonium parte Laboriosi Stanislai Graś de Villa Borów.
Na żądanie Pracowitego Stanisława Grasia poddanego ze wsi Borowa
przed Urzędem niniejszym Radzieckim Kraśnickim oblicznie stanąwszy
niewierny Żyd Jakub Jakubowicz przyrzekł... że za konsensem
żydowskim takowe świadectwo wydał... dwóm chłopom od Tkacza
na atestacyję swojej sprawy... od JMP Czerszczyńskiego [Czerwieńskiego?]
wybierając się do Urzędowa, gdzie dwa chłopi prosili Żyda tego
y dali mu groszy aby im zapisał atestacyję...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 63,
        "numer_pozycji": "63",
        "strona_pagina": "fol. 29v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1659",
        "kategoria": "Sąd Radziecki / Zeznanie z Borowa i zamknięcie roku 1659 (Finis huius anni)",
        "osoby_podmioty": "Stanisław Graś (z Borowa), Żyd Moś Łazarowicz, Wawrzyniec Kowal (ławnik kraśnicki), Andrzej Rak [Rok?], Jan Zamoyski (wojewoda sandomierski, z nagłówka 1660 na sąsiedniej karcie)",
        "kwoty_podatki": "22 i pół gr",
        "opis_sprawy": "Dokończenie zeznania Stanisława Grasia ze wsi Borów (kupno sukna na jarmarku u Żydów, pożyczka u Żyda Mosia Łazarowicza 22 i pół gr w obecności świadków Wawrzyńca Kowala ławnika kraśnickiego i Andrzeja Raka [Roka?]) oraz formuła kończąca rok 1659: Finis huius anni (po prawej stronie widoczna sąsiednia karta Elekcji 1660 r.).",
        "transkrypcja": """--- Skan #63 (fol. 29v) ---
29v 1659
...podczas jarmarku w Kraśniku... Stanisław Graś chcąc kupić sukna
do Żydów do kramu wstąpił... a gdy nie dostawało pieniędzy pożyczył
u Mosia Łazarowicza gr 22 1/2, co Żyd w rejestr zapisał y oddał...
Świadkami tego byli Sławetny Wawrzyniec Kowal Ławnik Kraśnicki y Andrzej Rak [Rok?].
Quod Actis inscribi petiit.

Finis huius anni.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 64,
        "numer_pozycji": "64",
        "strona_pagina": "fol. 30r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1660",
        "kategoria": "Elekcja Magistratu 1660",
        "osoby_podmioty": "Jan Zamoyski (wojewoda sandomierski), Krzysztof Brzozowski (podczaszy czernihowski, tenutariusz kraśnicki), Maciej Tharasa (rajca), Marcin Sitarski (rajca), Stanisław Nawrocki (rajca), Wojciech Kurowic (rajca), Sebald [Ubald/Albert] Janaszkowic (wójt), Marcin Starzyński (ławnik), Błażej Kołodziejczyk (ławnik), Stanisław Sienkowic (ławnik), Jan Chmielowic (ławnik), Maciej Kozica (ławnik), Grzegorz Joch [Fox] (ławnik), Jan Cichoń (pisarz)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Uroczysta Elekcja Magistratu Kraśnickiego z piątku przed św. Agnieszką 1660 r. (16 I): za zgodą wojewody Jana Zamoyskiego i tenutariusza Krzysztofa Brzozowskiego powołano rajców rezydentów Macieja Tharasę, Marcina Sitarskiego, Stanisława Nawrockiego i Wojciecha Kurowica; wójtem obrano Sebalda [Ubalda] Janaszkowica, ławnikami Marcina Starzyńskiego, Błażeja Kołodziejczyka, Stanisława Sienkowica, Jana Chmielowica, Macieja Kozicę i Grzegorza Jocha [Foxa], a pisarzem Jana Cichonia.",
        "transkrypcja": """--- Skan #64 (fol. 30r) ---
ELECTIO 30.
Sollennis et Laudabilis Magistratus Civitatis Crasnicensis in praesentia
totius Communitatis et consuetudine antiqua celebrata feria sexta ante Festum
S. Agnetis Virginis et Martyris Anno Domini Millesimo Sexcentesimo Sexagesimo.

Et inprimis ex Benigna Voluntate Illustrissimi ac Magnifici Domini D. Joannis de
Zamoście Zamoyski Palatini Sandomiriensis Domini Nostri Illustrissimi Clementissimi
Generosus ac Magnificus D. Christophorus Brzozowski Pocillator Czernichoviensis
Tenutarius pro tunc Crasnicensis elegit duos Consules Residentes
Famatum D. Mathiam Tharasa et Famatum D. Martinum Sitarski.
Advocatus cum Scabinis loci suo assidentes Archi-Magistris Contuberniorum
totaque Communitate confirmaverunt in Consulem Residentem Famatum D.
Stanislaum Nawrocki. Qui quidem Consules more solito electi et confirmati
adsciverunt sibi quartum Consulem Residentem Famatum D. Albertum Kurowic.
In Advocatum vero et Judicem Ordinarium pro tunc Crasnicensem Praeconsul
cum Consulibus Residentibus Archi-Magistris Magistri totius Communitatis elegerunt
et constituerunt Famatum D. Sebaldum [Ubaldum] Janaszkowic. Quem Generosus
ac Magnificus Dominus in tota Communitate Ordinavit, approbavit et confirmavit.
Scabini antiqui: Martinus Starzyński, Blasius Kołodziejczyk, Stanislaus
Sienkowic, Joannes Chmielowic, Mathias Kozica et Gregorius Joch [Fox],
ad quos propter plenam rationem Honestus Dominus Joannes Cichoń Notarius
pro tunc Juratus elegerunt et constituerunt, qui quidem supra Officio Scabinali
suo corporale juramentum juxta rotam in jure descriptam praestiterunt.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 65,
        "numer_pozycji": "65",
        "strona_pagina": "fol. 30v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1660",
        "kategoria": "Elekcja 1660 (dok.) / Sąd Radziecki: areszt krowy przez Marinę Serkównę",
        "osoby_podmioty": "Grzegorz Joch [Fox], Jan Cichoń, Stanisław Nawrocki (burmistrz), Maciej Tharasa (cechmistrz kuśnierzy), Marcin Sitarski (cechmistrz szewców), Paweł Chmara (cechmistrz krawców), Szymon Szarek (cechmistrz kowali), Bartłomiej Kozicki (cechmistrz tkaczy), Paweł Stokowski [Stockowski] (egzaktor), Andrzej Piecznik [Pięcznik?] (egzaktor), szl. Marina Serkówna, Bartosz Boryszowski [Boryszkowski?]",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie Elekcji 1660 r.: asesorzy (Grzegorz Joch, Jan Cichoń), objęcie burmistrzostwa przez Stanisława Nawrockiego, wybór cechmistrzów (Maciej Tharasa, Marcin Sitarski, Paweł Chmara, Szymon Szarek, Bartłomiej Kozicki) i egzaktorów (Paweł Stokowski, Andrzej Piecznik [Pięcznik?]); poniżej sesja z poniedziałku przed Popielcem 1660 r. (9 II): szlachetna Marina Serkówna zakłada areszt przeciw Bartoszowi Boryszowskiemu [Boryszkowskiemu?] o skradzioną krowę.",
        "transkrypcja": """--- Skan #65 (fol. 30v) ---
30v
...in jure descriptam praestiterunt.
In Assessorem ad Judicia Civilia Tribus Parochis Famatus Gregorius Joch [Fox]
et Notarius Joannes Cichoń constituti sunt.
Absoluta Electione Famatus D. Stanislaus Nawrocki Officium
Proconsulatus una cum Thesauris Reipublicae suscepit.
Post in Domo Famati Proconsulis Archi-Magistri una cum Societate taliter
sunt electi:
In Archi-Magistrum:
Pellionum: Famatus Mathias Tharasa Consul Crasnicensis.
Sutorum: Famatus Martinus Sitarski Consul Crasnicensis.
Sartorum: Honestus Paulus Chmara Civis Crasnicensis.
Fabrorum: Honestus Simon Szarek Civis Crasnicensis.
Textorum: Honestus Bartholomaeus Kozicki Civis Crasnicensis.
Exactores ad Exactiones publicas Honestus Paulus Stokowski [Stockowski]
et Andreas Piecznik [Pięcznik?] electi et constituti.

Actum Coram Officio Consulari feria secunda ante Cineres proxima Anno Domini 1660.
Nobilis Marina Serkówna Arestum imposuit contra Boryszowski.
Do Urzędu y Akt niniejszych Radzieckich Kraśnickich oblicznie przyszedłszy
Szlachetna Marina Serkówna położyła solenne Arest na krowę, którą kupił
Uczciwy Bartosz Boryszowski [Boryszkowski?] dnia dzisiejszego na targu,
żądając Urzędu niniejszego aby się jej nie ważył nikomu oddawać, aż się
o tę krowę prawem rozprawi, ponieważ ta jej własna krowa jej skradziona.
Który to Arest jest na pisma Sługi Przysięgłego Radzieckiego Kraśnickiego
opowiedziany y za żądaniem jej do Akt niniejszych przyjęty y zapisany.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 66,
        "numer_pozycji": "66",
        "strona_pagina": "fol. 31r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1660",
        "kategoria": "Sąd Radziecki / Spór o skradzioną krowę (Serkówna vs Boryszowski)",
        "osoby_podmioty": "szl. Marina Serkówna, Bartłomiej [Bartosz] Boryszowski [Boryszkowski?], Jan Mączewski [Mączkowski?], Jakub (chłop?)",
        "kwoty_podatki": "20 złp",
        "opis_sprawy": "Sesja popołudniowa z 9 II 1660 r.: rozprawa szl. Mariny Serkówny przeciw Bartłomiejowi Boryszowskiemu o skradzioną krowę; pozwany twierdzi, że kupił ją na jarmarku w Zaklikowie od Jana Mączewskiego [Mączkowskiego?] za 20 złp; sąd po zeznaniu dwóch świadków dopuszcza powódkę do przysięgi z dwoma świadkami i odsyła egzekucję do sądu wójtowskiego.",
        "transkrypcja": """--- Skan #66 (fol. 31r) ---
31. 1660
Eodem die Tempore Pomeridiano.
Inter Nobilem Marinam Serkówna Actricem ac Honestum Bartholomaeum Boryszowski Citatum.
Skarżyła się Aktorka na Pozwanego o krowę którą jej skradziono,
a teraz przedaże ją tutaj w Kraśniku... ale Coram Officio Consulari
tak odpowiedział ten co tę krowę przedawał: iż ją w Zaklikowie na jarmarku
kupił od Jana Mączewskiego [Mączkowskiego?] za złotych dwadzieścia fl 20,
który mi powiedział że ją kupił od chłopa z Woli [?].
Aktorka replikując że ta krowa jej własna jest y z tego stawiła dwóch świadków
jako ta krowa jest jej własna y jej skradziona.
Urząd tedy niniejszy Radziecki Kraśnicki fundując się na zeznaniu dwóch
świadków, którzy pod przysięgą zeznali że ta krowa jest własna Aktorki...
nakazuje aby na przyszły piątek przysięgła z dwoma świadkami jako jej własna
y nieprzedana krowa, a pozwany ma wrócić krowę albo stawić swego
zastępcę, pro executione hujus remittit ad Officium Advocatiale.
Quod Decretum ab utraque parte susceptum est.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 67,
        "numer_pozycji": "67",
        "strona_pagina": "fol. 31v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1660",
        "kategoria": "Sąd Radziecki / Protestacja rajcy bełżyckiego Poniatowskiego przeciw Rudborkowi",
        "osoby_podmioty": "Wojciech Poniatowski (mieszczanin i rajca bełżycki), Rudborek (mieszczanin z Urzędowa), Marcin Lipnicki (mieszczanin z Lublina), Paweł Powroźnik (świadek), Walenty Radachowski (mieszczanin z Lublina)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Sesja z poniedziałku po Niedzieli Palmowej 1660 r. (22 III): protestacja sławetnego Wojciecha Poniatowskiego, mieszczanina i rajcy bełżyckiego, przeciw Rudborkowi mieszczaninowi z Urzędowa o publiczne znieważenie podczas jarmarku w Kraśniku (wyzwiska słowne przy świadkach: Marcinie Lipnickim z Lublina, Pawle Powroźniku i Walentym Radachowskim z Lublina).",
        "transkrypcja": """--- Skan #67 (fol. 31v) ---
31v 1660
Actum Coram Officio Consulari feria secunda post Dominicam Palmarum proxima Anno Domini 1660.
Famatus Albertus Poniatowski Civis et Consul Bełżycensis Prostat contra Rudborek de Urzędów.
Do Urzędu niniejszego Radzieckiego Kraśnickiego przyszedłszy oblicznie Sławetny
Wojciech Poniatowski mieszczanin y Rajca Bełżycki solenną protestacyją uczynił
przeciwko Rudborkowi mieszczaninowi z Urzędowa, iż podczas jarmarku na targu
w Kraśniku stojącego słowami nieuczciwymi znieważył mówiąc: ty szelmo,
skurwysynie, kpie, burmistrzu bełżycki, wyzywając się na rękę. Na co stawił
dwóch świadków którzy się dobrowolnie stawili, aby byli słuchani:
Marcin Lipnicki mieszczanin z Lublina sub juramento corporali zeznał
iż widział gdy Rudborek wywrócił beczkę solną pod konie P. Poniatowskiego
y wyzywał go słowami obelżywymi...
Drugi świadek Walenty Radachowski mieszczanin z Lublina sub juramento zeznał
ut supra, confirmando testimonium primi testis.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 68,
        "numer_pozycji": "68",
        "strona_pagina": "fol. 32r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1660",
        "kategoria": "Przekazanie burmistrzostwa / Laudum Pasienia Trzody (cz. 1)",
        "osoby_podmioty": "Wojciech Poniatowski, Rudborek, Marcin Sitarski (ustępujący burmistrz), Stanisław Nawrocki (nowy burmistrz), Wojciech Kurowic (rajca), Maciej Tharasa (rajca), Sebald [Ubald] Janaszkowic (wójt)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie protestacji Wojciecha Poniatowskiego; sesja Sądu Łączonego z soboty przed Niedzielą Przewodnią 1660 r. (3 IV): Translatio Proconsulatus od Marcina Sitarskiego do Stanisława Nawrockiego; poniżej sesja z Niedzieli Jubilate 1660 r. (18 IV): początek uchwały miejskiej — Laudum Pasienia trzody — podjętej przez burmistrza Stanisława Nawrockiego, rajców, wójta Sebalda Janaszkowica, ławników, cechmistrzów starszych, wójtów przedmiejskich i całe pospólstwo.",
        "transkrypcja": """--- Skan #68 (fol. 32r) ---
32. 1660
...ab utraque parte actis insertum et connotatum est.

Actum Coram Officio Composito Consulari Advocati et Scabinorum Juratorum Crasnicensium
Sabbato ante Dominicam Conductus Paschae 1660.
Translatio Proconsulatus a Famato D. Martino Sitarski ad Famatum D. Stanislaum Nawrocki
in praesentia Cechi Magistrorum Scultetorum [Sutorum?] Suburbii et totius Communitatis
juxta ritum et consuetudinem antiquam. Quod Actis connotatum est.

Actum Coram Officio Composito Consulari Advocati et Scabinorum Juratorum Crasnicensium
Die Dominico quod vocatur Jubilate et haec est Dominica secunda post Pascha proxima Anno Domini 1660.
Laudum Pasienia trzody.
W domu Sławetnego Pana Stanisława Nawrockiego Burmistrza natenczas Rezydującego
Kraśnickiego przy obecności jego samego y Sławetnych PP. Kolegów przy boku jego siedzących,
także przy bytności Sławetnego Pana Sebalda Janaszkowica Wójta Kraśnickiego, PP. Ławników,
Cechmistrzów Starszych y Wójtów Przedmiejskich, sporządziwszy sobie pewne Laudum y postanowienie
o pasieniu świni y trzody, widząc wielkie szkody tak w ogrodach jako też w polach
przez niedbanie pasterzów y puszczanie trzody bez dozoru, wszyscy unanimiter voto consentientes
postanowili...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 69,
        "numer_pozycji": "69",
        "strona_pagina": "fol. 32v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1660",
        "kategoria": "Laudum Pasienia Trzody (cz. 2) / Sprawa Wojciecha Gąski z Polichny o krowę",
        "osoby_podmioty": "Wojciech Gąska (poddany ze wsi Polichna), JMP Brzezicki (ze Słodkowa)",
        "kwoty_podatki": "2 gr (od wołu/krowy), 1 gr (od roczniaka i wieprza), 10 złp winy [?]",
        "opis_sprawy": "Dokończenie Laudum Pasienia trzody (ustalenie taksy dla pastuchów: od wołu i krowy 2 gr, od roczniaka 1 gr, od wieprza 1 gr; zakaz samopasu i prawo zabicia szkody); poniżej sesja z poniedziałku po Niedzieli Jubilate 1660 r. (19 IV): sprawa pracowitego Wojciecha Gąski poddanego z Polichny (za atestacją JMP Brzezickiego ze Słodkowa) o odzyskanie skradzionej krowy wraz ze szczegółowym opisem jej maści i znaków.",
        "transkrypcja": """--- Skan #69 (fol. 32v) ---
32v 1660
...postanowili paść trzodę od świętego Wojciecha blisko przyszłego, któremu pastuchowi
od każdego bydlęcia takowa zapłata należeć będzie: od starego bydlęcia 2 gr,
od roczniaka jeden grosz, od wieprza grosz jeden. A ktoby nie chciał pędzić
swych świń albo bydła na pole przed pastucha, tedy wolno będzie każdemu
szkodę w swoim ogrodzie zająć, a jeśliby świnia albo gęś szkodę uczyniła,
wolno zabić i oddać właścicielowi albo za szkodę zająć. Które to Laudum
na żądanie Cechmistrzów Starszych y Pospólstwa wszystkiego do Akt niniejszych
jest przyjęte y zapisane.

Actum feria secunda post Dominicam Jubilate 1660.
Inter Laboriosum Gąska Albertum subditum de Polichna Actorem ac Instigatorem Officii.
Daje do Akt niniejszych Radzieckich Kraśnickich wiarę atestacyją
JMP Brzezickiego ze Słodkowa, którą pisze za poddanym swoim Wojciechem Gąską
z Polichny, opisując znaki tej krowy która mu zginęła: czarna łysa z białym
podbrzuszem, rogi ma krzywe... na dowód czego stawił dwóch świadków
którzy pod przysięgą zeznali jako ta krowa jest jego własna.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 70,
        "numer_pozycji": "70",
        "strona_pagina": "fol. 33r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1660",
        "kategoria": "Sąd Radziecki / Kradzież zboża w domu ławnika Błażeja Kołodziejczyka",
        "osoby_podmioty": "Wojciech Gąska (z Polichny), Błażej Kołodziejczyk (ławnik przysięgły), Krzysztof Stanisławek (poddany z Wilkołaza), szl. Dorota Lubszycka (ze Starej Wsi)",
        "kwoty_podatki": "5 grzywien",
        "opis_sprawy": "Dokończenie dekretu Wojciecha Gąski z Polichny; sesja z soboty w wigilię Św. Trójcy 1660 r. (22 V): sprawa o kradzież (causa ratione furti) ławnika Błażeja Kołodziejczyka przeciw pracowitemu Krzysztofowi Stanisławkowi z Wilkołaza o kradzież półtora korca żyta i grochu z komory (wyrok nakazujący zwrot lub chłostę pod pręgierzem pod winą 5 grzywien); poniżej sesja z czwartku przed św. Janem Chrzcicielem 1660 r. (17 VI): początek zeznania świadków szl. Doroty Lubszyckiej ze Starej Wsi.",
        "transkrypcja": """--- Skan #70 (fol. 33r) ---
33. 1660
...że sprawiedliwie tę przysięgę Wojciech Gąska odprawił, przeto Urząd
krowę jemu oddać nakazuje, co wpisano do Akt niniejszych.

Actum Sabbato in Vigilia SS. Trinitatis 1660.
Causa ratione furti inter Famatum D. Blasium Kołodziejczyk Scabinum Juratum
Crasnicensem Actorem ac Laboriosum Christophorum Stanisławek de Wilkołaz inculpatum de furto.
Skarżył się Aktor na Obwinionego iż syn jego będąc w służbie u niego w domu
wykradł żyta mąki półtora korca y grochu czwarter... czemu obwiniony Krzysztof
Stanisławek z Wilkołaza zaprzeczyć nie mógł. Urząd niniejszy Radziecki Kraśnicki
skazał Obwinionego do pręgi na rynku miejskim, aby go lud pospolity widział,
a po chłoście przez sługi miejskie pod pręgierzem na pięć grzywien
winy skazany... Quod Decretum per executionem mandatum est.

Actum feria quinta ante Festum S. Joannis Baptistae 1660.
Testimonium parte Nobilis Dorotheae Lubszycka de Starawieś.
Ad instantiam Nobilis Dorotheae Lubszyckiej testes infra inscripti coram Officio...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 71,
        "numer_pozycji": "71",
        "strona_pagina": "fol. 33v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1660",
        "kategoria": "Sąd Radziecki / Świadectwo Doroty Lubszyckiej i spór z Żydem Izaakiem",
        "osoby_podmioty": "szl. Dorota Lubszycka (ze Starej Wsi), szl. Leon Włostek [Włodek?] (mieszczanin kraśnicki), szl. Mikołaj Włodek [?] (ze Starej Wsi), szl. Jakub Kurowski [?] (ze Starej Wsi), Żyd Izaak Grzybek [?] (z Janowa / Sandomierza?)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Zaprzysiężone zeznania świadków szl. Doroty Lubszyckiej ze Starej Wsi (szl. Leona Włostka [Włodka?] mieszczanina kraśnickiego, szl. Mikołaja Włodka [?] i szl. Jakuba Kurowskiego [?] ze Starej Wsi) w sprawie skradzionej krowy z obory Kowalka w Starej Wsi; poniżej sprawa szl. Doroty Lubszyckiej przeciw Żydowi Izaakowi Grzybkowi [?] o tę krowę oddaną przez chłopa poddanego (odesłanie do pana burmistrza).",
        "transkrypcja": """--- Skan #71 (fol. 33v) ---
33v 1660
...praesentes per se examinati quilibet illorum separatim sub juramento corporali
praestito ad fidem duobus digitis recognovit...
Ac inprimis Nobilis Leonis Włostek [Włodek?] Civis Crasnicensis post tortum examen
juratus est sub juramento corporali... że ta krowa z obory Kowalka wzięta ze Starej Wsi
jest własna szlachetnej Doroty Lubszyckiej.
Secundus Testis Nobilis Nicolaus Włodek [?] de Starawieś recognovit ut supra...
Tertius Testis Nobilis Jacobus Kurowski [?] de Starawieś similiter recognovit.

Inter Nobilem Dorotheam Lubszycka de Starawieś Actricem
ac Judaeum Isaacum Grzybek [?] Citatum.
Skarżyła się Aktorka na Pozwanego iż krowę swoją własną u niego znalazła,
którą jej skradziono. Pozwany Żyd stanąwszy przed Sądem odpowiedział że ją
kupił na targu u chłopa nieznajomego, który przedał ją pod panem Burmistrzem...
aby mu Aktorka o tę krowę przed Panem Burmistrzem odpowiedziała.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 72,
        "numer_pozycji": "72",
        "strona_pagina": "fol. 34r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1660",
        "kategoria": "Sąd Radziecki / Kwitacja Żydów lubelskich Chaima i Lewka dla dzierżawcy z Lipy",
        "osoby_podmioty": "szl. Dorota Lubszycka, Żyd Izaak, Stanisław Nawrocki (burmistrz), Wojciech Kurowic (rajca), Maciej Tharasa (rajca), Żyd Chaim Moskowicz (z Lublina), Żyd Lewek Izraelowicz (z Lublina), szl. Tymowski [Zymowski? Łyżkowski?] (dzierżawca z Lipy), Zachariasz Izaakowicz, Stephan Dzieniek [Dzieniecki?]",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie dekretu szl. Doroty Lubszyckiej z Żydem Izaakiem (przysięga powódki na potwierdzenie własności krowy); poniżej sesja z wtorku przed św. Janem Chrzcicielem 1660 r. (22 VI) przed burmistrzem Stanisławem Nawrockim oraz rajcami Wojciechem Kurowicem i Maciejem Tharasą: początek kwitacji Żydów lubelskich Chaima Moskowicza i Lewka Izraelowicza wobec szl. dzierżawcy z Lipy.",
        "transkrypcja": """--- Skan #72 (fol. 34r) ---
34. 1660
...juraverit jako ta krowa jej własna jest. Judicium praesens
exauditis controversiis partium decernit: Ponieważ Żyd
przedał tę krowę pod Burmistrzem, tedy Aktorka na przyszły piątek
z dwoma świadkami przysięże jako ta krowa jest jej własna,
a Żyd ma ją zwrócić bez żadnej zwłoki. Quod Decretum ab utraque parte susceptum est.

Actum Coram Officio Consulari praesente Famato D. Stanislao
Nawrocki Proconsule pro tunc Sedente praesentibus Famatis
Alberto Kurowic et Mathia Tharasa Consulibus Crasnicensibus
feria tertia ante Festum S. Joannis Baptistae 1660.

Perfidi Judaei Chaim et Lewek de Lublin quietant Nobilem Tymowski [Zymowski?] de Lipa.
Przed Urzędem niniejszym Radzieckim Kraśnickim stanąwszy oblicznie
Niewierni Żydzi Chaim Moskowicz y Lewek Izraelowicz z Lublina oba razem
y każdy z nich z osobna, przy obecności Zachariasza Izaakowicza y Stephana Dzieńka [Dzienieckiego?]...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 73,
        "numer_pozycji": "73",
        "strona_pagina": "fol. 34v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1660",
        "kategoria": "Sąd Radziecki / Kwitacja Żydów lubelskich po zabójstwie w Lipie",
        "osoby_podmioty": "Żyd Chaim Moskowicz (z Lublina), Żyd Lewek Izraelowicz (z Lublina), Żyd Heliasz Izaakowicz (starszy zboru kraśnickiego), Żyd Matek Dławski [?] (starszy zboru kraśnickiego), Żyd Mosiek Jarosławski (starszy zboru kraśnickiego), szl. Tymowski [Zymowski?] (dzierżawca z Lipy), Jan Zamoyski (wojewoda sandomierski), Wawrzyniec (poddany z Lipy)",
        "kwoty_podatki": "300 grzywien (vadium)",
        "opis_sprawy": "Dokończenie kwitacji Żydów lubelskich Chaima Moskowicza i Lewka Izraelowicza (w obecności starszych zboru kraśnickiego: Heliasza Izaakowicza, Matka Dławskiego [?] i Moska Jarosławskiego) wobec dzierżawcy wsi Lipa (dóbr wojewody sandomierskiego Jana Zamoyskiego) w związku ze śmiercią Żyda zadaną przez poddanego Wawrzyńca ze wsi Lipa; zrzeczenie się pretensji pod wadium 300 grzywien z wpisem do Trybunału Lubelskiego.",
        "transkrypcja": """--- Skan #73 (fol. 34v) ---
34v 1660
...przy obecności Żydów Heliasza Izaakowicza, Matka Dławskiego [?]
y Moska Jarosławskiego Starszych Zboru Kraśnickiego zeznali y zeznają,
iż przyjechawszy do wsi Lipy dóbr Jaśnie Wielmożnego Pana Wojewody Sandomierskiego
dzierżawy JMP Tymowskiego [Zymowskiego?], gdzie poddany tamtejszy Wawrzyniec
poddany ze wsi Lipy zabił Żyda na drodze w Turzy [?]...
Z której to przyczyny Żydzi lubelscy nic nie mają do JMP Tymowskiego [Zymowskiego?],
kwitując go wiecznie y zrzekając się wszelakich pretensyi tak przed sądem
Trybunału Koronnego Lubelskiego jako y każdym innym urzędem,
pod zakładem wadium grzywien trzysta na stronę przeciwną.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 74,
        "numer_pozycji": "74",
        "strona_pagina": "fol. 35r",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1660",
        "kategoria": "Przekazanie burmistrzostwa / Cesja sadu zagołoborskiego (Dziwkowski vs Pyrek)",
        "osoby_podmioty": "Stanisław Nawrocki (ustępujący burmistrz), Maciej Tharasa (nowy burmistrz), Adam Dziwkowski (mieszczanin lubelski), Szymon Pyrek (ślusarz, mieszczanin i cechmistrz szpitala ubogich), Benedykt Nowak",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Sesja Sądu Łączonego z soboty po Nawiedzeniu NMP 1660 r. (3 VII): Translatio Proconsulatus od Stanisława Nawrockiego do Macieja Tharasy; poniżej sesja z wtorku przed św. Małgorzatą 1660 r. (6 VII): sprawa Adama Dziwkowskiego mieszczanina lubelskiego przeciw Szymonowi Pyrkowi ślusarzowi mieszczaninowi kraśnickiemu i cechmistrzowi szpitala ubogich kościoła farnego kraśnickiego o cesję praw Benedykta Nowaka na sad zagołoborski.",
        "transkrypcja": """--- Skan #74 (fol. 35r) ---
35. 1660
...do Akt niniejszych Radzieckich Kraśnickich jest przyjęto y zapisano.

Actum Coram Officio Composito Consulari Advocati et Scabinorum Juratorum Crasnicensium
Sabbato post Festum Gloriosae Visitationis B. M. Virginis proximo Anno Domini 1660.
Translatio Proconsulatus a Famato D. Stanislao Nawrocki ad Famatum D. Mathiam Tharasa
in praesentia Cechi Magistrorum Scultetorum [Sutorum?] Suburbii et totius Communitatis
cum omnibus thesauris Civilibus juxta ritum et consuetudinem antiquam.

Actum feria tertia ante Festum S. Margarethae Virginis et Martyris proxima Anno Domini 1660.
Inter Honestum Adamum Dziwkowski Civem Lublinensem Actorem ac Honestum
Simonem Pyrek senfabrem [ślusarza] Civem Crasnicensem Citatum.
Pozwany Szymon Pyrek ślusarz mieszczanin kraśnicki y cechmistrz szpitala ubogich
kościoła farnego kraśnickiego... pokazał przed Urzędem cesyją prawa od
Benedykta Nowaka na ten sad zagołoborski, z którego czynsz należy szpitalowi
y Bractwu Różańca Świętego kościoła farnego kraśnickiego...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 75,
        "numer_pozycji": "75",
        "strona_pagina": "fol. 35v",
        "sygnatura": "35/40/0/1/19",
        "data_rok": "1660",
        "kategoria": "Sąd Radziecki / Cesja sadu (dok.) i Laudum o Liquorach (cz. 1)",
        "osoby_podmioty": "Adam Dziwkowski (z Lublina), Szymon Pyrek (ślusarz i cechmistrz szpitala), Benedykt Nowak, Maciej Tharasa (burmistrz), Wojciech Kurowic (rajca), Marcin Sitarski (rajca), Stanisław Nawrocki (rajca), Sebald [Ubald] Janaszkowic (wójt)",
        "kwoty_podatki": "10 złp (szpital), 25 złp (Bractwo Różańca), 10 gr (z marginesu)",
        "opis_sprawy": "Dokończenie dekretu w sprawie Adama Dziwkowskiego i Szymona Pyrka (rozliczenie długów z sadu zagołoborskiego na rzecz szpitala ubogich — 10 złp oraz Bractwa Różańca NMP — 25 złp, z zachowaniem cesji Benedykta Nowaka); poniżej sesja z piątku przed św. Bartłomiejem 1660 r. (20 VIII): początek wielkiego wilkierza miejskiego — Laudum o liquorach — podjętego w domu burmistrza Macieja Tharasy przy udziale rajców Wojciecha Kurowica, Marcina Sitarskiego i Stanisława Nawrockiego, wójta Sebalda Janaszkowica, ławników, cechmistrzów starszych i pospólstwa (z taksami trunków na prawym marginesie).",
        "transkrypcja": """--- Skan #75 (fol. 35v) ---
35v 1660
...na które sady y grunty idą długi różne kościelne: szpitalowi kościoła farnego
kraśnickiego złotych dziesięć fl 10, Bractwu Różańca Najświętszej Panny Maryi
długu złotych dwadzieścia pięć fl 25. Tedy te długi powinien będzie płacić
corocznie wedle sumy swego sadu, a cesyja prawa Benedykta Nowaka w swej
mocy zostaje. Quod Decretum ab utraque parte susceptum est.

Actum Coram Officio Consulari Advocati et Scabinorum Juratorum Crasnicensium
feria sexta ante Festum S. Bartholomaei Apostoli proxima Anno Domini 1660.
Laudum o liquorach.
W domu Sławetnego P. Mathijasza Tharasy Burmistrza natenczas Rezydującego
Kraśnickiego przy bytności jego samego także przy bytności Sławetnych Panów
Wojciecha Kurowica, Marcina Sitarskiego y Stanisława Nawrockiego Radziec Kraśnickich,
tudzież przy bytności Sławetnego P. Sebalda Janaszkowica Wójta Kraśnickiego
y PP. Ławników przy boku jego siedzących, także przy bytności Cechmistrzów
Starszych y Pospólstwa wszystkiego...""",
        "link_swa": UNIT_LINK
    }
]

existing_nums = {r['nr_skanu'] for r in main_data}
for s in part3_scans:
    if s['nr_skanu'] not in existing_nums:
        main_data.append(s)

main_data.sort(key=lambda x: x['nr_skanu'])

with open('/home/ubuntu/workspace/Gen/main_data_j19_part3.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j19_part3.json: {len(main_data)} rekordów.")
