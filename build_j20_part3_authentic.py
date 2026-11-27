# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j20_part2.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
SYGN = "35/40/0/1/20"

part3_scans = [
    {
        "nr_skanu": 51,
        "numer_pozycji": "51",
        "strona_pagina": "fol. 23v (23 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Sprawy sporne, pobicia i relacje woźnego",
        "osoby_podmioty": "Stanisław Soszłygarczyk [Poszłygarczyk?], Wojciech [Albert] Oleszek [Oleszkowicz?], Grzegorz Fox, Jadwiga Zdanowa [Zdanianka?], woźny Jan Kłębski [?], Marcin Sulik [?], Wojciech Siedlatka [Siedlatko?], Maciej Dudzik [?], Jan Klatkowski [?], Jan Łatka [?], Marcin Słodzarski [?], Grzegorz Łotka [?]",
        "kwoty_podatki": "fl 25 / gr 15; fl 4",
        "opis_sprawy": "Protokół Sądu Wójtowskiego i Ławniczego (feria 4ta post festum S. Martini Episcopi 1658): sprawa Stanisława Soszłygarczyka [Poszłygarczyka?] przeciw Wojciechowi Oleszkowi [Oleszkowiczowi?] o pobicie i najście; sprawa Grzegorza Foxa przeciw Jadwidze Zdanowej [Zdanianki?] o dług fl 25 gr 15; relacje woźnego sądowego w sprawach Marcina Sulika [?], Wojciecha Siedlatki [?], Macieja Dudzika [?], Jana Klatkowskiego [?], Jana Łatki [?] oraz Marcina Słodzarskiego [?] przeciw Grzegorzowi Łotce [?] o fl 4.",
        "transkrypcja": """23 N.
Actum coram Off[ici]o Advocati et Scab. Iur. f[e]ria 4ta post f[e]s[tum] S. Martini Episcopi 1658.

Innot. Fam. Stanislai Soszlygarczyk [Poszłygarczyk?] Act[oris] ac Alberti Oleszek [Oleszkowic?] Cit.
Skarżył sie Actor na Pozwanego iz mu w Sochniu [Sokowem?] zbił i poranił rękę y głowę krwawo, aż na ziemię upadł, a żona iego zbiła y obelżyła słowy nieuczciwemi, na co świadki ma y okazował przed Urzędem. A Pozwany odpowiedział ze ia nie bił ani żona moia, ale on sam napastował w domu moim y bił, a przysięgę na to ofiarował. Sąd dekretował aby przysiągł Pozwany jako nie bił ani żona iego, a po przysiędze wolny będzie, co iuris est.

Innot. Famatus Gregorius Fox Act[or] ac Hedvigis Zdanianka [Zdanowa?] Cit.
Tandem sie nie zgadzali strony przed Urzędem o dług fl 25 gr 15, o który Pozwana zeznała że winna, ale prosiła o termin do oddania z komory y rzeczy swoich. Sąd nakazał aby w 15 dniach oddała pod egzekucją urzędową.

Relatio Nobilis Bedelli existen[tis] Martini Sulik [Sulik?] Act. ac Albertum Siedlatka [Siedlatko?] et Mathiam Dudzik [Dudzik?] Cit.
Stawając przed Urzędem woźny przysięgły zeznał jako pozwał tychże obwinionych na dzień dzisiejszy.

Diligentia Fam. Joannis Klatkowski [?] et Joannis Łatka [?] contra Soszlygarczyk [?].
Stawili się przed Sądem, a strona przeciwna nie stanęła, więc zapisano diligentiam.

Relatio Bedelli existen[tis] Fam. Martini Słodzarski [Słodzarski?].
Coram Off[ici]o Advocati et Scab. Iur. f[e]ria 4ta ut supra stawił sie woźny Joannes Kłębski [Kłębski?] y zeznał jako pozwał Fam. Martinum Słodzarski ad inst[antiam] Fam. Gregorii Łotka [Lotka?] o dług fl 4 z zapisu, a iż strona nie stanęła, Sąd uznał kontumację y nakazał zapłatę pod egzekucją urzędową.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 52,
        "numer_pozycji": "52",
        "strona_pagina": "fol. 24r (24)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Sprawy sporne i inkwizycje świadków",
        "osoby_podmioty": "Mikołaj Kurowek [Kurowicz?], Marcin Ptaszek [?], Marcin Gębalka [Gębałka?], Wojciech Gębalski [?], Grzegorz Fox, Wojciech Maruszkowic [Maruszka?], 8 świadków (Stefan Dębski [?], Maciej Kozak [Kozłowski?], Szymon Kuśmierz [?], Daniel Łysik [?], Marcin Kowal [?])",
        "kwoty_podatki": "fl 200; fl 30",
        "opis_sprawy": "Dokończenie dekretu z poprzedniej karty; skarga Mikołaja Kurowka [Kurowicza?] i Marcina Ptaszka [?] przeciw Marcinowi Gębalce [?] o dług i szkody; protokół z piątku po św. Marcinie 1658 r. zawierający relację 8 mężów z inkwizycji w sprawie sławetnego Grzegorza Foxa przeciwko dobrom po nieboszczyku Wojciechu Maruszkowicu [Maruszce?] (zeznania m.in. Stefana Dębskiego [?], Macieja Kozaka [?], Szymona Kuśmierza [?], Daniela Łysika [?]).",
        "transkrypcja": """24.
In Off[ici]o ut iuris relatio... [dokończenie klauzuli dekretu z k. 23v] ... ad Offm. Adalbertus Gębalski [Gębala?] zeznał jako czynił zadość dekretowi, a Sąd termin naznaczył na przyszłą sesję.

Sub eodem Actu Fam. Nicolaus Kurowek [Kurowicz?] et Martinus Ptaszek [?] contra Martinum Gębalka [Gębałka?].
Ad Off[ici]um p[rae]s[ens] Advocati et Scab. Iur. stanąwszy przed Urzędem Mikołaj Kurowek y Marcin Ptaszek skarżyli sie na Marcina Gębalkę iż im winien długu z zapisu y szkody poczynił, a płacić nie chce. Pozwany prosił o dylację do przyszłego Sądu, na co Sąd przyzwolił pod rygorem egzekucji.

Actum coram Off[ici]o Advocati et Scab. Iud. Iur. f[e]ria 6ta post Festum S. Martini Episcopi 1658.

Relatio 8 Virorum ex inquisitione Famati Gregorii Fox Act[oris].
Inkwizycja 8 mężów przysięgłych w sprawie sławetnego Grzegorza Foxa przeciwko dobrom po nieboszczyku Wojciechu Maruszkowicu [Maruszce?] pozostałym, z których zeznali:
1. Stefan Dębski [Dębowski?], 2. Maciej Kozak [Kozłowski?], 3. Szymon Kuśmierz [Kuszmir?], 4. Daniel Łysik [?], 5. Marcin Kowal [?], którzy pod przysięgą zeznali o stanie dóbr po nieboszczyku Wojciechu Maruszkowicu, o długach jego do fl 200 i o sumie fl 30 należnej Grzegorzowi Foxowi, jako po śmierci tegoż Maruszkowica rzeczy zostały zabrane y rozebrane bez zaspokojenia wierzycieli.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 53,
        "numer_pozycji": "53",
        "strona_pagina": "fol. 24v",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Zeznania świadków, długi i wyderkafy",
        "osoby_podmioty": "Kazimierski [Rębiński?], Sebastian Zięba [Zgęba?], Jan Dąbrowski [Bąkowski?], Grzegorz Fox, Andrzej Głodzik [Gładysz?], Szymon [?] Sułkowicz [?], Wojciech Krupiński [?], Michał Miazga [Maslik?], Wawrzyniec Świątek [Świątkowicz?]",
        "kwoty_podatki": "fl 8; fl 3; fl 10 gr 15; fl 100 (czynsz fl 7); fl 2; fl 50",
        "opis_sprawy": "Zeznania świadków Sebastiana Zięby [?] i Jana Dąbrowskiego [?] w sprawie sławetnego Kazimierskiego [?]; seria pozwów Grzegorza Foxa przeciw Andrzejowi Głodzikowi [?] o fl 10 gr 15, Szymonowi Sułkowiczowi [?], Wojciechowi Krupińskiemu [?] o wyderkaf fl 100 (czynsz fl 7), Michałowi Miazdze [?] o fl 2 oraz Wawrzyńcowi Świątkowi [?] o wyderkaf z fl 10 gr 15 na sumie fl 50.",
        "transkrypcja": """Testes pro parte Fam. Kazimierski [Rębiński?] 24v.
1mus Testis Sebestianus Zięba [Zgęba?] zeznał pod przysięgą jako słyszał od Pana Kazimierskiego iż mu drzewo i granice naruszono na gruncie jego.
2dus Testis Joannes Dąbrowski [Bąkowski?] zeznał pod przysięgą iż widział jako szkodę uczyniono na fl 8, a na drugie szacowano fl 3 y nawiązki fl 3.

Innot. Fam. Gregorii Fox Act[oris] ac Andream Głodzik [Gładysz?] Cit.
Skarżył sie Actor o dług z zapisu fl 10 gr 15, który Pozwany oddać powinien w terminie dwuniedzielnym pod egzekucją.

Innot. eiusdem Act[oris] ac Simonem [?] Sułkowicz [Sulik?] Cit.
O niezapłacenie długu z terminu przeszłego.

Innot. eiusdem Act[oris] ac Albertum Krupiński [?] et Sebestianum [?] Cit.
Skarżył sie Actor o wyderkaf na ogrodzie Łaskowskie [?] z sumy fl 100 po fl 7 rocznego czynszu, którego Pozwany nie oddaje, przeto Sąd nakazał zapłatę zaległości pod rygorem egzekucji na gruncie.

Innot. eiusdem Act[oris] ac Michaelem Miazga [Maslik?] Cit.
Skarżył sie o dług fl 2 z zaciągu.

Item eiusdem Act[oris] ac Laurentium Świątek [Świątkowicz?] Cit.
O czynsz fl 10 gr 15 wyderkafu należnego od fl 50 sumy głównej na gruncie zapisanej, który Sąd nakazał oddać pod egzekucją.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 54,
        "numer_pozycji": "54",
        "strona_pagina": "fol. 25r (wklejka)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Suplika / Pismo procesowe (wklejka oryginalna)",
        "osoby_podmioty": "Wawrzyniec Prokopek, Grzegorz Fox, Wojciech Maruszkowic [Maruszka?], Wójt i Ławnicy Kraśniccy",
        "kwoty_podatki": "fl 30",
        "opis_sprawy": "Oryginalna wklejona suplika napisana i podpisana własnoręcznie przez Wawrzyńca Prokopka do Pana Wójta i Ławników w sprawie przeciwko Grzegorzowi Foxowi, który po nieboszczyku Wojciechu Maruszkowicu zajął dobra za dług fl 30, z pominięciem innych wierzycieli i z odesłaniem sprawy do Trybunału.",
        "transkrypcja": """Łaskawy Panie Woycie z pełnym Pany Collegami. Skarżę sie przed Sądem W[aszmościów] na Pana Grzegorza Foxa iż on dobra pobrawszy po Nieboszczyku Woyciechu Maruszkowicu niże długu fl 30 winien był któryż ten był Nieboszczyk, żenie położył inwentarza którego z nas nie wychodził, a dawszy na siebie a iż on sprawiedliwie nieboszczyk został na długu winien płacić to świadkami i per Extractum regestru, któryż ten zajął z osobna do Nieboszczyka domu tego licząc bez długu. Przetoż proszę Waszmościów Panów o sprawiedliwy wyrok, a iż sie cytowała przed Sąd W[aszmościów] sub Actu fer. 6ta ante Viti [?] w sprawie z Panem Foxem ad respondendum, a gdy termin przyszedł, toż nie stanął y nie stawił sie, czekam sprawiedliwości, jednak teraz sprawę pokornie przed W[aszmościami] stawiam, Łaskawych Panów o sprawiedliwość prosząc aby W[aszmościowie] raczyli wysłuchać P. Foxa z tej strony a nie z inszej, a wszystko pod dalszy rozsądek W[aszmościów] poddaję.
Wawrzyniec Prokopek""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 55,
        "numer_pozycji": "55",
        "strona_pagina": "fol. 25v (25 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Zapiska dorsalna na wklejce",
        "osoby_podmioty": "Wawrzyniec Prokopek, Grzegorz Fox",
        "kwoty_podatki": "-",
        "opis_sprawy": "Odwrocie (verso) wklejonej supliki Wawrzyńca Prokopka z notatką kancelaryjną ad replicam oraz śladem odwróconego zapisu daty 1658 na dolnej krawędzi.",
        "transkrypcja": """25 N.
[Notatka dorsalna w poprzek karty:]
Ad replicam... [tekst wyblakły/kancelaryjny: ad replicam partis Actoreae protestatio obligatoria in causa praesenti ad futura...].
[U dołu do góry nogami fragment tytułu sesji z datą 1658:]
... 1658 ... coram Officio Advocatiali et Scabinali ...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 56,
        "numer_pozycji": "56",
        "strona_pagina": "fol. 26r (26)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Sprawy majątkowe, długi i wyderkafy",
        "osoby_podmioty": "Jan Gębecki [Gołecki?], Wdowa Krawcowa [Kwiecina?], Wawrzyniec Prokopek, Jan Gębski [Grząbka?], Stanisław Łysik [?], Jan Marlik [Manlik?]",
        "kwoty_podatki": "fl 1 gr 15; fl 20; fl 140; fl 200; fl 56",
        "opis_sprawy": "Trzy wpisy sporne przed Sądem Wójtowskim: Jan Gębecki [Gołecki?] przeciw Wdowie Krawcowej [?] o fl 1 gr 15 za robotę i towar; Wawrzyniec Prokopek przeciw Janowi Gębskiemu [?] o grunt/plac oraz dług fl 20 i fl 140 z interesem za kilka lat; Stanisław Łysik [?] przeciw Janowi Marlikowi [Manlikowi?] o zapis wyderkafowy na fl 200 i zaległy czynsz fl 56.",
        "transkrypcja": """26.
Innot. Joannes Gębecki [Gołecki?] Act[or] ac Viduam Krawcową [Kwiecinę?] Cit.
Skarżył sie Actor na Pozwaną o fl 1 gr 15, które jej dał na robotę y towar, a ona nie oddała ani roboty nie uczyniła, przeto Sąd nakazał zapłatę w dwóch niedzielach pod egzekucją.

Innot. Laurentius Prokopek Act[or] ac Joannem Gębski [Grząbka?] Cit.
Skarżył sie Actor na Pozwanego iż na gruncie jego trzyma długu fl 20 z zapisu dawnego, a nadto fl 140 z interesem za kilka lat niedopłaconych, o które upominał sie wielokrotnie, a Pozwany nie oddał. Sąd wysłuchawszy stron nakazał obrachunek y zapłatę długu pod rygorem egzekucji na gruncie.

Innot. Stanislai Łysik [?] Act[oris] ac Joannem Marlik [Manlik?] Cit.
Skarżył sie Actor na Pozwanego o wyderkaf z fl 200 kapitału, od których zaległego czynszu fl 56 nie oddał, przeto Marlik odpowiedział że nie powinien płacić bez okazania zapisu, na co Sąd nakazał złożenie dokumentów.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 57,
        "numer_pozycji": "57",
        "strona_pagina": "fol. 26v (26 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Sprawy o długi, komorne i pobicie",
        "osoby_podmioty": "Jan Marlik [Manlik?], Maciej Konięga, Wawrzyniec Paszek [Bąk?], Jan Poszłygarczyk, Jadwiga Łopionka [Łopianka?], Żyd Izaak [?], Wdowa Lalka [Falka?]",
        "kwoty_podatki": "fl 30; fl 2; fl 5; fl 7; fl 3",
        "opis_sprawy": "Dokończenie dekretu w sprawie Jana Marlika; sprawa ławnika Macieja Konięgi przeciw Wawrzyńcowi Paszkowi [?] o fl 30 długu z komory i fl 2 podatku (Anno 1658 2da die post S. Martini); sprawa Jana Poszłygarczyka przeciw Jadwidze Łopionce [?] o fl 5 z komornego i obelgi; pozew Żyda Izaaka [?] przeciw Wdowie Lalce [?] o fl 7 i fl 3 długu.",
        "transkrypcja": """26 N.
... [dokończenie dekretu w sprawie Jana Marlika] ... aby zapisy z ksiąg okazał y do Sądów Podstarościego odesłał, co iuris est.

Innot. Fam. Mathiae Konięga Act[oris] ac Laurentium Paszek [Bąk?] Cit.
Skarżył sie Actor na Pozwanego iż mu winien długu fl 30, a nie oddaje komornego ani podatków fl 2, które za niego założył w roku 1658 2da die post S. Martini. Sąd nakazał zapłatę w dwóch niedzielach pod egzekucją.

Innot. Joannes Poszłygarczyk Act[or] ac Hedvigim Łopionka [Łopianka?] Cit.
Skarżył sie Actor na Pozwaną iż mu winna fl 5 z komornego y nie chce ustąpić z izby, a nadto go znieważyła y pobiła na sąsiedztwie. Sąd po wysłuchaniu nakazał jej ustąpić y dług zapłacić.

Innot. Judeus Izaak [?] Act[or] ac Viduam Lalkę [Falkę?] Cit.
Skarżył sie Żyd o fl 7 z zaciągu y fl 3 na zastawę danych, o co Pozwana przyznała się, a Sąd termin zapłaty wyznaczył.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 58,
        "numer_pozycji": "58",
        "strona_pagina": "fol. 27r (27)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Sprawy szlacheckie i mieszczańskie o szkody",
        "osoby_podmioty": "Żyd Izaak [?], Wdowa Lalka [?], Marcin Borowiec [Konięga?], szlachetny Piotr Słodzarski [Zadzarski?], Skrzypkowski [?], Wężyk [?]",
        "kwoty_podatki": "fl 1 gr 15; fl 3; fl 200",
        "opis_sprawy": "Dokończenie dekretu w sprawie długu Żyda (fl 1 gr 15 i fl 3); obszerna sprawa Marcina Borowca [?] przeciwko szlachetnemu Piotrowi Słodzarskiemu [Zadzarskiemu?] o konia, szkodę, najazd i obelgi z udziałem p. Skrzypkowskiego [?] i p. Wężyka [?] oraz sumę fl 200.",
        "transkrypcja": """27.
... [dokończenie sprawy żydowskiej] ... opisze z tego fl 1 gr 15 na płótno y fl 3 na zastawę, za które Pozwana ma oddać w terminie wyznaczonym pod egzekucją.

Innot. Martini Borowiec [Konięga?] Act[oris] ac Nobilem Petrum Słodzarski [Zadzarski?] Cit.
Zawołani obaj przed Urząd, gdzie szlachetny Piotr Słodzarski odpowiadał iż o konia szkodę nie uczynił, ani ludzi nie nasyłał, lecz sam Actor krzywdę mu wyrządził. Actor zaś replikował powołując sie na świadków p. Skrzypkowskiego [?] y p. Wężyka [?], iż szkody poniósł na fl 200. Sąd wyznaczył termin inkwizycji i dalszego rozsądku.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 59,
        "numer_pozycji": "59",
        "strona_pagina": "fol. 27v (27 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Spory graniczne i pozwy żydowskie",
        "osoby_podmioty": "Jan Babiński [Zabiński?], Jakub Soroka [Sroka?], Wiatrak [Wiatrek?], woźny Jan Kłębski [?], Żyd Iczek Łoboda [Łabędź?]",
        "kwoty_podatki": "fl 2 gr 20",
        "opis_sprawy": "Dokończenie sprawy szlacheckiej z k. 27r; spór Jana Babińskiego [Zabińskiego?] przeciw Jakubowi Sorokce [Sroce?] o granicę, płot i drzewo przy gruncie Wiatraka [Wiatrka?]; relacja woźnego Jana Kłębskiego [?] o pozwanie Żyda Iczka Łobody [Łabędzia?] o dług fl 2 gr 20.",
        "transkrypcja": """27 N.
... [dokończenie wpisu z k. 27r] ... w terminie do 2da decembris [?], gdzie Sąd dalszy wyrok wyda.

Innot. Joannis Babiński [Zabiński?] Act[oris] ac Jacobum Soroka [Sroka?] Cit.
Skarżył sie Actor na Pozwanego iż mu grunt zabiera, drzewo wycina y płot przestawił na granicy przy Wiatraku [Wiatrku?]. Pozwany zaprzeczał temu, przeto Sąd nakazał inkwizycję y wizję lokalną gruntu z przydaniem świadków.

Relatio Bedelli contra Iczek Łoboda [Łabędź?] perfid[um] Jud[aeum].
Stawając przed Sądem woźny Jan Kłębski [?] zeznał jako pozwał Iczka Łobodę Żyda o dług fl 2 gr 20 należny z wyroku, a iż Pozwany nie stanął, Sąd uznał kontumację y nakazał zapłatę pod egzekucją.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 60,
        "numer_pozycji": "60",
        "strona_pagina": "fol. 28r (28)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Sprawy sporne, zeznania świadków i dekrety",
        "osoby_podmioty": "Szlachetny Wojciech Zarzycki [Zakrzewski?], Jan Klatkowski [?], Jan Zieliński, Ewa Marcinowa Jędrzejczyk [Jędrzejowa?], Wawrzyniec Żydkowic [Sydkowic?], Mikołaj Kurowek [Kurowicz?], Andrzej Łota",
        "kwoty_podatki": "fl 6; gr 20",
        "opis_sprawy": "Protokół Sądu Wójtowskiego i Ławniczego z poniedziałku przed Ofiarowaniem NMP 1658 r. (18 XI 1658): sprawa szl. Wojciecha Zarzyckiego [?] przeciw Janowi Klatkowskiemu [?] o dług; sprawa Jana Zielińskiego przeciw Ewie Marcinowej Jędrzejczyk [?] o fl 6; zeznanie świadka Mikołaja Kurowka [?] w sprawie Wawrzyńca Żydkowica [Sydkowica?] przeciw Andrzejowi Łocie o klepki dębowe i pobicie żony w lesie (nawiązka gr 20).",
        "transkrypcja": """28.
Actum coram Off[ici]o Advocati et Scab. Iur. Iud. f[e]ria 2da ante Festum Praesentationis B. Mariae Virg. 1658.

Innot. Nob. Alberti Zarzycki [Zakrzewski?] Act[oris] ac Joannem Klatkowski [?] Cit.
Skarżył sie Actor o niezapłacenie długu z terminu przeszłego y o szkody, na co Sąd zapisał niestawiennictwo Pozwanego.

Innot. Fam. Joannis Zieliński Act[oris] ac Evam Martini Jędrzejczyk [Jędrzejowa?] Cit.
Pozwana przyznała się do długu fl 6, który Sąd nakazał jej oddać w terminie 2da [feria] pod egzekucją.

Testis pro parte Laurentii Żydkowic [Sydkowic?].
Testis Nicolaus Kurowek [Kurowicz?] Civis Crasn. zeznał pod przysięgą iż widział jako Andrzej Łota z lasu klepki dębowe brał y żonę Żydkowica pobił.

Laurentius Żydkowic [Sydkowic?] Act[or] ac Andream Łota Cit.
Sąd wysłuchawszy zeznań skazał Andrzeja Łotę na nawiązkę gr 20 y zwrot szkody za zabrane klepki dębowe, pod rygorem więzienia.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 61,
        "numer_pozycji": "61",
        "strona_pagina": "fol. 28v (28 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Zeznania świadków, spory sąsiedzkie i wyderkafy",
        "osoby_podmioty": "Andrzej Łota, Wawrzyniec Żydkowic [Sydkowic?], Stanisław Poszłygarczyk, Kasper Bęben [?], Sebastian Zięba, Andrzej Sadownik, Jadwiga Kopianka [Kępianka?] alias Jachima Kępka [?], Ewa z Łopacina [?], Maciej Gębalski [?]",
        "kwoty_podatki": "fl 50",
        "opis_sprawy": "Dokończenie sprawy Łoty z Żydkowicem; zeznania świadków Kaspra Bębna [?], Sebastiana Zięby i Andrzeja Sadownika w sprawie Stanisława Poszłygarczyka o kradzież z kramu i bójkę; pozew Stanisława Poszłygarczyka przeciw Jadwidze Kopiance [?] alias Jachimie Kępce [?] o siedlisko; zapis wyderkafu fl 50 przeciw Maciejowi Gębalskiemu [?].",
        "transkrypcja": """28 N.
... [dokończenie dekretu z k. 28r] ... przyłożywszy do tego nawiązkę y koszta prawne, które Andrzej Łota oddać powinien.

Testis pro parte Stanislai Poszłygarczyk.
Testis Caspar Bęben [?] zeznał pod przysięgą jako widział kradzież z budki y bójkę przy kramie, a strony sie wzajemnie szarpały.

Testis pro parte eiusdem.
Testis Sebestianus Zięba zeznał podobnie jako poszkodowany Poszłygarczyk krzyczał o kradzież z kramu; 3tius Testis Andreas Sadownik potwierdził zeznania poprzednich.

Innot. Fam. Stanislai Poszłygarczyk Act[oris] ac Hedvigim Kopianka [Kępianka?] alias Jachima Kępka [?] Cit.
Spór o siedlisko y długi po nieboszczyku, odesłano do dalszego rozsądku Sądu.

Innot. Fam. Evae de Łopacina [?] Act[ricis] ac Mathiam Gębalski [?] Cit.
O wyderkaf z sumy fl 50 należący z domu i ogrodu, który Pozwany zapłacić powinien.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 62,
        "numer_pozycji": "62",
        "strona_pagina": "fol. 29r (29)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Wyderkafy, manifestacje i sprawy o długi",
        "osoby_podmioty": "Ewa z Łopacina [?], Tomasz Pełka, Wawrzyniec Prokopek, Wojciech Maruszkowic [?], Jan Gołecki, Maciej Kurowek [?], Wdowa Daliborka [Zabielska?], Marcin Gębalka [?], Augustyn Kurowic, Jan Grząbka, Bartłomiej Grudzień",
        "kwoty_podatki": "fl 50; fl 1; fl 28 gr 20; fl 5",
        "opis_sprawy": "Pozew przeciw Tomaszowi Pełce o wyderkaf fl 50; manifestacja Wawrzyńca Prokopka w sprawie dóbr po Wojciechu Maruszkowicu; zeznanie świadka Macieja Kurowka [?] w sprawie Jana Gołeckiego; manifestacja Jana Gołeckiego przeciw Wdowie Daliborce [?]; relacja woźnego przeciw Marcinowi Gębalce [?] o fl 28 gr 20; protokół z wigilii Ofiarowania NMP 1658 r. (20 XI 1658): sprawa Jana Grząbki przeciw Bartłomiejowi Grudniowi o fl 5 długu z komornego.",
        "transkrypcja": """29.
Innot. eiusdem Act[ricis] ac Thomam Pełka Cit.
Sprawa o wyderkaf z sumy fl 50 na placu y domu zapisanej, który Sąd nakazał zapłacić.

Manifestatio Fam. Laurentii Prokopek in causa contra Fox [?].
Manifestacja względem bezprawnego zajęcia dóbr po nieboszczyku Wojciechu Maruszkowicu y niewydania inwentarza.

Testis pro parte Joannis Gołecki.
Testis Mathias Kurowek [?] zeznał pod przysięgą w sprawie Gołeckiego o obelgi y szkodę sąsiedzką.

Manifestatio Joannis Gołecki contra Daliborkę [Zabielską?] Viduam.
Manifestuje sie przed Urzędem iż mu zabrała ruchomości y winna fl 1 długu, o co protestuje.

Relatio Bedelli.
Marcin Gębalka [?] pozwany przez Augustyna Kurowica ex acto o fl 28 gr 20 z dekretu.

Actum coram Off[ici]o Advocati et Scab. Iur. Iud. f[e]ria 4ta in Vigilia Praesentationis B. M. V. 1658.
Innot. Fam. Joannis Grząbka Act[oris] ac Bartholomaeum Grudzień Cit. (fl 28).
Skarżył sie Actor o fl 5 z komornego y o izbę, na co Pozwany odpowiedział prosząc o termin do obrachunku.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 63,
        "numer_pozycji": "63",
        "strona_pagina": "fol. 29v (29 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Sprawy o długi, handel jabłkami z Lublinem",
        "osoby_podmioty": "Jan Grząbka, Bartłomiej Grudzień, Wojciech Dubaj [Dubański?], Jan Klatkowski, Walenty Słodki [Skutka?], Grzegorz Orlak [Orlik?]",
        "kwoty_podatki": "fl 24; fl 3; fl 6; fl 4; fl 1",
        "opis_sprawy": "Dokończenie sprawy Grząbki z Grudniem; obszerny proces Wojciecha Dubaja [?] przeciw Janowi Klatkowskiemu o dług fl 24 z zapisu na Podwyższenie Krzyża Św. 1658 r.; sprawa Walentego Słodkiego [?] przeciw Grzegorzowi Orlakowi [?] o fl 3 i fl 6 za jabłka wiezione do Lublina (z potrąceniem fl 4 i nakazem zapłaty fl 1).",
        "transkrypcja": """29 N.
... [dokończenie sprawy Grząbki z Grudniem] ... powinien będzie oddać do terminu naznaczonego.

Innot. Alberti Dubaj [Dubański?] Act[oris] ac Joannem Klatkowski Cit.
Na którą skargę Pozwany odpowiedział że nie winien fl 24, ale tylko z zapisu na Exaltatio S. Crucis anno praesenti 1658 uczynionego, a Jan Klatkowski ręczył za niego. Sąd wysłuchawszy stron nakazał zapłatę długu fl 24 w dwóch ratach pod rygorem egzekucji na dobrach Pozwanego.

Innot. Valentini Słodki [Skutka?] Act[oris] ac Gregorium Orlak [Orlik?] Cit.
Skarżył sie Actor na Pozwanego o fl 3 winne za jabłka, które stanęły na fl 6, gdyż mu wiózł do Lublina te jabłka, a Pozwany odparł że na nie wydał fl 4 y potrącił sobie. Sąd nakazał aby fl 1 pożyczane oddał, a o resztę przysięgą oczyścił sie w terminie.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 64,
        "numer_pozycji": "64",
        "strona_pagina": "fol. 30r (30)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Sprawy o zboże, pobicie i wyderkafy",
        "osoby_podmioty": "Wojciech Noster [Kostka?], Jadwiga [?] Rudnicka, Felicjan Konięga [Koniński?], szlachetny Szymon Szarek, Jakub Zięba [Zgęba?], Maciej Konięga, Jan Lisek [Cichy?]",
        "kwoty_podatki": "7 korcy żyta; fl 7; fl 2; fl 50 (czynsz fl 3 gr 15)",
        "opis_sprawy": "Protokół Sądu Wójtowskiego i Ławniczego z piątku przed św. Katarzyną 1658 r. (22 XI 1658): sprawa prac. Wojciecha Nostera [?] z Rudnika przeciw Felicjanowi Koniędze [?] o 7 korcy zboża i pobicie; sprawa szl. Szymona Szarka przeciw Jakubowi Ziębie [?] o fl 7 i fl 2 na ogrodzie; sprawa ławnika Macieja Konięgi przeciw Janowi Liskowi [?] o wyderkaf fl 50 z czynszem fl 3 gr 15.",
        "transkrypcja": """30.
Actum Iudicii coram Off[ici]o Advocati et Scab. Iur. f[e]ria 6ta ante Festum S. Catharinae Virg. et Mart. 1658.

Innot. Lab. Alberti Noster [Kostka?] et Hedvigis [?] Rudnicki de Rudnik Act[orum] ac Felicianum Konięga [Koniński?] Cit.
Skarżyli sie Powodowie o 7 korcy żyta zabranego y o pobicie w drodze, na co Pozwany zaprzeczył, przeto Sąd odesłał sprawę do inkwizycji świadków.

Innot. Nob. Simonis Szarek Act[oris] ac Jacobum Zięba [Zgęba?] Cit.
Skarżył sie Actor o fl 7 z ogrodu y o fl 2 z zastawu, prosząc aby mu ogród wrócono po wykupie. Sąd nakazał obrachunek y zwrot po złożeniu sumy.

Innot. Fam. Mathiae Konięga Scab. Iur. Act[oris] ac Joannem Lisek [Cichy?] Cit.
Skarżył sie o wyderkaf na sumę fl 50, od której zaległego czynszu fl 3 gr 15 nie oddał, przeto Sąd nakazał zapłatę pod rygorem egzekucji.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 65,
        "numer_pozycji": "65",
        "strona_pagina": "fol. 30v (30 N.)",
        "sygnatura": SYGN,
        "data_rok": "1657–1658",
        "kategoria": "Przysięgi sądowe (Iuramenta) i ugoda",
        "osoby_podmioty": "Szymon Szutka [Sutka?], Żyd Icek, Jan Tomaszczyk, Maciej Kępka, Jadwiga Tomaszczykowa [?], szlachetny Piotr Słodzarski, Maciej Prus [Ptaszek?], Jakub Serba [Sroka?], Zofia Rębińska [Łębińska?], Łukasz Kaczorowski [?], Krzysztof Zieliński [?]",
        "kwoty_podatki": "fl 5",
        "opis_sprawy": "Cztery przysięgi sądowe (Iuramentum): Szymona Szutki [?] przeciw Żydowi Ickowi na fl 5; sprawa Jana Tomaszczyka przeciw Maciejowi Kępce; przysięga szl. Piotra Słodzarskiego przeciw Maciejowi Prusowi [?]; przysięga Jakuba Serby [?] na krucyfiks przeciw Zofii Rębińskiej [?]; na dole ugoda mieszczan kraśnickich z soboty przed św. Katarzyną 1657 [popr. na 1658?].",
        "transkrypcja": """30 N.
Iuramentum Simonis Szutka [Sutka?] contra Judeum Ickum.
Stanąwszy przed Urzędem Szymon Szutka wykonał przysięgę według dekretu przeciw Żydowi Ickowi na sumę fl 5, po której wolnym od dalszej pretensji uznany został.

Innot. Fam. Joannis Tomaszczyk contra Mathiam Kępka.
O zapłatę według dekretu y wydanie fantu zajętego z udziałem Jadwigi żony.

Iuramentum Nob. Petri Słodzarski contra Mathiam Prus [Ptaszek?].
Stanąwszy szlachetny Piotr Słodzarski wykonał przysięgę przeciw Maciejowi Prusowi na sumę z dekretu.

Iuramentum Jacobi Serba [Sroka?] contra Sophiam Rębińska [Łębińska?].
Stanąwszy Jakub Serba wykonał przysięgę na krucyfiks według dekretu iż zboża nie zabrał ani sługi nie namawiał przeciw Zofii Rębińskiej.

Actum Sabbato ante Festum S. Catharinae Virg. et Mart. 1657 [popr. na 1658?].
Przed Urzędem stanęli dobrowolnie mieszczanie kraśniccy [Łukasz Kaczorowski? i Krzysztof Zieliński?], którzy o wszelkie krzywdy i zajścia pomiędzy sobą dobrowolną zgodę uczynili i onej dotrzymać przyrzekli.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 66,
        "numer_pozycji": "66",
        "strona_pagina": "fol. 31r (31, wklejka)",
        "sygnatura": SYGN,
        "data_rok": "1657",
        "kategoria": "Plenipotencja sądowa (wklejka oryginalna)",
        "osoby_podmioty": "Ewa Koźmianowa, Grzegorz Fox, nieboszczka Zofia Kowalowa, Maciej Saraczkowic [Saraczkowicz?], Wójt i Ławnicy Kraśniccy",
        "kwoty_podatki": "-",
        "opis_sprawy": "Oryginalna wklejona plenipotencja podpisana własnoręcznie przez Ewę Koźmianową (datowana na dole: piątek przed św. Marcinem 1657 r. = 9 XI 1657), ustanawiająca jej krewnego sławetnego Macieja Saraczkowica [?] plenipotentem w sprawie przed Trybunałem Zamojskim przeciwko Grzegorzowi Foxowi o dobra po nieboszczce Zofii Kowalowej.",
        "transkrypcja": """31.
Łaskawy Panie Woycie na społu z Pany Collegami.
Przekładam tu przed Urzędem W[aszmościów] iżem przez starość swoię barzo słaba y blizsze starości iest onego świata niż tego, a iż ta sprawa P. Foxa wytoczona iest na Trybunał, którą świadczę mi P. Bóg żem nie z żadney chciwości pragnie pożyczywszy zakładać, ale wiedząc dobrze że te dobra pozostałe po Nieboszczce Zofii Kowalowey w ręce nasze nie wyszły nigdy z domu Pana Foxa, ale od Rodziców moich, a siostra moia z Duzelika [?] pierwszą ręką miała na to samey Boga na świadectwo biorę, złożyła sobie tego, a iż Pan Bóg mesiaszny raz przyidał, aby długi te które Nieboszczka z łaski swey pozaciągała popłacone były y ieśliby co zostało za dusze iey dobrze uczynić, a że P. Fox pomienione dobra nienależące do siebie swowolnie pobrał, więc poprawiać drugiey wzywa przeciwko Compromissowi, krzywdy czyniąc ani na Vadium w nim założone dbając, długów nikomu płacić nie chce. Miłosierdziem poruszona w tey sprawie a w ciężkim niedostatku zostając, oświadczam się Sławetnego P. Macieia Saraczkowica [Saraczkowicz?] krewnego mego aby sprawe pomienioną w Trybunale Zamoyskim promowował, daiąc mu wszelaką moc w teyże iako naylepiey postępować według prawa y za Plenipotenta mego postanawiam z mocą woli teyże imieniem moim, inszego Plenipotenta na mieyscu swoim postanowić y to wszystko czynić coby zdało być potrzebnieyszego y sprawnego do sprawy tey. Obiecuiąc wszystko cokolwiek postanowi za wdzięczne przyiać. Czyniąc tę Plenipotencyą moią tak ważną iakoby była według Prawa przed Urzędem zapisana. Która aby była do Akt Waszych przyjęta proszę.
Ewa Koźmianowa
Susceptum coram Iudicio Exposito Banna Advocati et Scabinorum feria 6ta ante Festum S. Martini Episcopi 1657.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 67,
        "numer_pozycji": "67",
        "strona_pagina": "fol. 31v (31v)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Dekret sądowy i zapiska dorsalna",
        "osoby_podmioty": "Ewa Koźmianowa, Jan Gębski [?], Iarocki [?]",
        "kwoty_podatki": "fl 30",
        "opis_sprawy": "Odwrocie (verso) wklejonej plenipotencji Ewy Koźmianowej: u góry dekret sądowy w sprawie Jana Gębskiego [?] o fl 30 długu, pośrodku glosa dorsalna z nazwiskiem Ewy Koźmianowej oraz przebijające pismo z karty 31r.",
        "transkrypcja": """31v.
Audito... [dekret sądowy u góry karty] ... Joannes Gębski [?] contra Viduam ... de fl 30, na którą sumę dekret wyroku wydany został pod egzekucją urzędową.
[Na środku karty notatka dorsalna:]
Ewa Koźmianowa płaciła ... [Iarockiego?].
[Pozostała część karty zawiera przebijający tekst z karty 31r.]""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 68,
        "numer_pozycji": "68",
        "strona_pagina": "fol. 32r (32)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Obdukcja ran i sprawy sporne",
        "osoby_podmioty": "Albrecht Dubaj [?], Jan Klatkowski, Wawrzyniec Żydkowic, Baltazar Żydkowic, Maciej Konięga, Stanisław Poszłygarczyk, Maciej Zieliński, Wawrzyniec Cichowicz [Cieśliński?]",
        "kwoty_podatki": "fl 24; fl 2",
        "opis_sprawy": "Dokończenie dekretu w sprawie Jana Klatkowskiego o fl 24 długu; protokół z czwartku przed św. Andrzejem 1658 r. (28 XI 1658): obdukcja ran Wawrzyńca Żydkowica pobitego przez Baltazara Żydkowica i Macieja Konięgę (rany cięte głowy, lewej ręki i palców); sesja z 29 XI 1658 r.: pozew Macieja Konięgi przeciw Wawrzyńcowi Cichowiczowi [?] o fl 2 oraz diligentia Stanisława Poszłygarczyka przeciw Maciejowi Zielińskiemu.",
        "transkrypcja": """32.
... [dokończenie sprawy Jana Klatkowskiego] ... iż jako dług fl 24 winien Albrechtowi Dubajowi według dekretu, z których w 3 ratach spłacić powinien pod egzekucją.

Actum f[e]ria 5ta ante Festum S. Andreae Apostoli 1658.
Obductio Laurentii Żydkowic.
Sławetny Wawrzyniec Żydkowic mieszczanin kraśnicki będąc zeszły z Kazimierza przed Urzędem okazował pobicia swego rany od Baltazara Żydkowica y Macieja Konięgi zadane: ranę ciętą na głowie z wierzchu, na ręce lewey ciętą wielką, palec wskazujący zbity, na prawey ręce siniec y na boku rana. Które rany Urząd obejrzał y do ksiąg zapisał.

Iudicium Expositum ... Sub eodem Actu f[e]ria 6ta ante Festum S. Andreae Apostoli 1658.
Innot. Fam. Mathiae Konięga Act[oris] ac Laurentium Cichowicz [Cieśliński?] Cit.
Pozwany dług fl 2 winny Actorowi zapłacić powinien w dwóch niedzielach pod egzekucją.

Diligentia Fam. Stanislai Poszłygarczyk przeciw Maciejowi Zielińskiemu, który nie stanął na terminie, przeto zapisano diligentiam.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 69,
        "numer_pozycji": "69",
        "strona_pagina": "fol. 32v (32 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Dekrety, przysięgi i zeznania Żyda",
        "osoby_podmioty": "Wawrzyniec Kępa [Kępka?], Maciej Ptaszek [Pępek?], Wawrzyniec Żydkowic, Andrzej Łota, Walenty Skutka [Słodki?], Jakub Bobak [Dubak?], Rębiński [?], Andrzej Marlik [Manlik?], Żyd Dawid Łazarz [?], Maciej Zieliński, Jan Kurza [Kurzawa?], Żyd Lejzor [Zelman?], Marcin Kępa [?]",
        "kwoty_podatki": "gr 21; gr 12; fl 28",
        "opis_sprawy": "Sześć wpisów: pozew Wawrzyńca Kępy [?] przeciw Maciejowi Ptaszkowi [?]; dekret w sprawie Wawrzyńca Żydkowica przeciw Andrzejowi Łocie (gr 21 nawiązki); przysięga Walentego Skutki [?] przeciw Jakubowi Bobakowi [?] na gr 12; sprawa o wyderkaf przeciw Andrzejowi Marlikowi; zeznania Żyda Dawida Łazarza [?] i Jana Kurzy [?] w sprawie Macieja Zielińskiego o skóry; pozew Żyda Lejzora [?] przeciw Marcinowi Kępie [?] o fl 28.",
        "transkrypcja": """32 N.
Innot. Laur. Kępa [Kępka?] Act[oris] ac Mathiam Ptaszek [Pępek?] Cit.
O dług z zapisu y wydanie fantu przed Sądem.

Innot. Fam. Laurentii Żydkowic Act[oris] ac Andream Łota Cit.
Sąd nakazał Andrzejowi Łocie zapłacić gr 21 nawiązki y zwrot szkody pod rygorem więzienia.

Iuramentum Valentini Skutka [Słodki?] contra Jacobum Bobak [Dubak?].
Walenty Skutka wykonał przysięgę przeciw Jakubowi Bobakowi na gr 12 według dekretu.

Innot. Fam. ... Rębiński [?] Act[oris] ac Andream Marlik [Manlik?] Cit.
Sprawa o zapis wyderkafowy, odesłana do okazania dokumentów.

Testis in causa Mathiae Zieliński.
Testis Judaeus Dawid Łazarz [?] zeznał pod przysięgą w sprawie Macieja Zielińskiego o kupno skór; 2dus Testis Joannes Kurza [Kurzawa?] zeznał o koniach y skórach przed Sądem.

Innot. Judaei Lejzor [Zelman?] Act[oris] ac Martinum Kępa [?] Cit.
Skarżył sie Żyd o dług fl 28 z dekretu, który Sąd nakazał oddać pod egzekucją.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 70,
        "numer_pozycji": "70",
        "strona_pagina": "fol. 33r (33)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Proces spadkowy poddanych ze wsi Blinów",
        "osoby_podmioty": "Wójt Wojciech Szafrankowic, ławnicy Marek Kępski [?], Augustyn Kurowic, Maciej Konięga, Grzegorz Fox, dzierżawca Blinowa Bartłomiej Janorowski, Wojciech Staroszek [Staszek?], Jadwiga Staroszkowa (z Rzepków), Maciej Łysak, Katarzyna Łysakowa (z Rzepków), Stanisław Kozieł [?], zmarły Tomasz Rzepka, Agnieszka Rzepkowa, Sebastian Rzepka, Jakub Rzepka",
        "kwoty_podatki": "30 kop; 40 lat pożycia",
        "opis_sprawy": "Sąd Wielki Gajony z końca 1658 r. (za zezwoleniem dzierżawcy Blinowa Bartłomieja Janorowskiego): początek wielkiego procesu spadkowego poddanych ze wsi Blinów (dawniej z Potoka). Córki zmarłego Tomasza Rzepki i Agnieszki — Jadwiga (żona Wojciecha Staroszka) i Katarzyna (żona Macieja Łysaka) — dochodzą spadku po ojcu Tomaszu Rzepce przeciwko Stanisławowi Koziełowi [?] i macosze/wdowie, wyliczając dorobek i grunty.",
        "transkrypcja": """1658. 33.
Iudicium Magnum Expositum Banna per Fam. D. Albertum Szafrankowic Advocatum et Iudicem Ordinarium Iuratum, nec non Fam. Viros Marcum Kępski [Kępski?], Augustinum Kurowic, Mathiam Konięga et Gregorium Fox Scabinos Iuratos.
Actum sub eodem loco celebratum f[e]ria 6ta ante Festum N. D. N. Jesu Christi prox. Anno Dni 1658.

Za dozwoleniem Imci P. Bartłomieja Janorowskiego Dzierżawcy na ten czas Blinowskiego przytoczyła sie sprawa niżej wyrażona poddanych ze Wsi Blinowa, to iest między Wojciechem Staroszkiem y Małżonką iego Jadwigą, także Maciejem Łysakiem y Małżonką iego Katarzyną, córkami nieboszczyka Tomasza Rzepki z jednej, a Stanisławem Koziełem [?] y Katarzyną [?] z drugiej strony.
Powodowie skarżyli sie iż nieboszczyk Tomasz Rzepka z pierwszą żoną Agnieszką ze Wsi Potoka dorobił sie wiela dobra przez lat 40, mając bydła rogatego, koni, owiec y zbóż, a po śmierci jego macocha/wdowa z synem Sebastianem i Jakubem Rzepką dobra te zatrzymała y nie wydała działu córkom Jadwidze i Katarzynie.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 71,
        "numer_pozycji": "71",
        "strona_pagina": "fol. 33v (33 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Inwentarz dobytku i proces ze wsi Blinów",
        "osoby_podmioty": "Tomasz Rzepka (zm.), Wojciech Rzepka alias Staroszek, Jadwiga Staroszkowa, Maciej Łysak, Katarzyna Łysakowa, Sebastian Rzepka, Agnieszka Rzepkowa (zm.)",
        "kwoty_podatki": "kor. 15 żyta; kop 30 jęczmienia; kop 17 owsa; kop 10 tatarki; kop 5 grochu; kop 10 pszenicy; 14 bydła; 8 koni; 36 owiec; fl 200; fl 130; kop 30",
        "opis_sprawy": "Szczegółowy inwentarz zasiewów, zboża i inwentarza żywego po zmarłym Tomaszu Rzepce we wsi Blinów (1658 r.), obejmujący m.in. żyto, jęczmień, owies, tatarkę, groch, pszenicę, 14 sztuk bydła, 8 koni, 36 owiec oraz długi fl 200 i fl 130. U dołu sesja z piątku przed św. Tomaszem Apostołem 1658 r. (20 XII 1658) na instancję pracowitego Wojciecha Rzepki alias Staroszka ze wsi Blinowa.",
        "transkrypcja": """33 N.
Żyta zasiano na Blinowskich gruntach kor. 15. Jara żyta kop 8, Jęczmienia kop 30, Owsa kop 17, Tatarki kop 10, Grochu kop 5, Pszenice kop 10. Bydła rogatego 14, Koni 8, Owiec 36, kłer iedna, wóz z rykowiem, pługów półtora, siekiery, rydle, kobyle, gąsiorów parę, kocioł miedziany, długu na fl 200, a po śmierci przybyło jeszcze na fl 130.
Rejestr drugi Dobra pozostałego po nieboszczyku Tomaszu Rzepce 1658: Ozimego kop 22, Jarego żyta kop 8, Jęczmienia kop 30, Pszenice kop 10, Tatarki kop 7, Owsa kop 21, Grochu mierzonego korzec 5, Konopi kop 6, Maku kopa 1, wóz ieden, kosa siekiera, rydel, sanie...
A iż strona powództwa domaga sie działu po matce swojej Agnieszce y ojcu Tomaszu Rzepce dla córek Jadwigi y Katarzyny, które miały wydane po kop 30, Sąd nakazał wysłuchanie świadków z obu stron.

Actum coram Off[ici]o Advocati et Scab. Iud. Iur. f[e]ria 6ta ante Festum S. Thomae Apostoli prox. Anno Dni 1658.
Na instancyą Pracowitego Wojciecha Rzepki alias Staroszka poddanego ze Wsi Blinowa zapisani są świadkowie do Sądu, aby zeznali na okoliczność majątku i testamentu po Tomaszu Rzepce.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 72,
        "numer_pozycji": "72",
        "strona_pagina": "fol. 34r (34)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Zeznania świadków ze wsi Blinów",
        "osoby_podmioty": "Jan Skórka [Storka?], Paweł Rzepka, Jan Rzepka, Andrzej Grątka [Gręta?], Tomasz Rzepka (zm.), Agnieszka Rzepkowa (zm.), Jadwiga Staroszkowa, Wojciech Staroszek, Jakub Rzepka, Sebastian Rzepka",
        "kwoty_podatki": "-",
        "opis_sprawy": "Zeznania czterech zaprzysiężonych świadków ze wsi Blinów (Jan Skórka [Storka?], Paweł Rzepka, Jan Rzepka, Andrzej Grątka [?]) w sprawie spadkowej po zmarłym Tomaszu Rzepce i pierwszej żonie Agnieszce, wyjaśniające pokrewieństwo Wojciecha Rzepki (syna Jakuba) oraz podział majątku na rzecz córek Jadwigi i Katarzyny.",
        "transkrypcja": """34.
Inquisitio testium... Jan Skórka [Storka?] poddany ze Wsi Blinowa oświadczony pod przysięgą zeznał jako nieboszczka Agnieszka pierwsza żona Tomasza Rzepki dorobiła sie z nim wiela dobra, mając dzieci Jadwigę y Katarzynę, a potym Tomasz Rzepka ożenił sie z drugą żoną. Wojciech zaś Rzepka alias Staroszek iest synem Jakuba Rzepki, brata Tomasza.

2dus Testis Laboriosus Paulus Rzepka subditus de Villa Blinow similiter sub iuramento corporali zeznał jako słyszał od Tomasza Rzepki iż testamentu nie uczynił, tylko córkom Jadwidze y Katarzynie po części dobra zapisał.

3tius Testis Lab. Joannes Rzepka subditus de Villa Blinow zeznał pod przysięgą jako wie dobrze iż Wojciech Rzepka iest synem Jakuba Rzepki, a nie rodzonym synem Tomasza.

4tus Testis Lab. Andreas Grątka [Gręta?] subditus de eadem Villa zeznał potwierdzając słowa poprzednich świadków. Sąd wysłuchawszy zeznań nakazał rzetelny dział majątku po Tomaszu Rzepce między sukcessorami pod opieką Sądu.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 73,
        "numer_pozycji": "73",
        "strona_pagina": "fol. 34v (34 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Manifestacja dzierżawcy i replika w sprawie Blinowa",
        "osoby_podmioty": "Wójt Wojciech Szafrankowic, ławnicy Marek Kępski [?], Augustyn Kurowic, Stanisław Szwedowicz [?], Maciej Konięga, Grzegorz Fox, Bartłomiej Janorowski (dzierżawca Blinowa), Piotr Gieracki [?], Wojciech Staroszek, Maciej Łysak, Katarzyna Rzepkowa, Wielmożny Pan Zakrzewski [?]",
        "kwoty_podatki": "fl 200; fl 500; 7 sztuk bydła",
        "opis_sprawy": "Sąd Gajony z końca 1658 r. z udziałem ławników (w tym Stanisława Szwedowica [?]); manifestacja dzierżawcy Blinowa Bartłomieja Janorowskiego (z odwołaniem do daty 19 X 1658 r., własnoręczny podpis B. Janorowski mpp) w sprawie dóbr po Tomaszu Rzepce; replika Wojciecha Staroszka i Macieja Łysaka przeciw Katarzynie Rzepkowej z wyliczeniem bydła (7 sztuk), sum fl 200 i fl 500 oraz powołaniem się na dekret przed J.W. Panem Zakrzewskim [?].",
        "transkrypcja": """34 N.
Iudicium Expositum Banna per Fam. D. Albertum Szafrankowic Advocatum et Iudicem Ordinarium Iuratum, nec non Fam. Viros Marcum Kępski [?], Augustinum Kurowic, Stanislaum Szwedowicz [?], Mathiam Konięga et Gregorium Fox Scabinos Iuratos ... f[e]ria 6ta ante Festum S. Thomae [?] 1658.

Innot. Nob. D. Bartholomaeus Janorowski dzierżawca Blinowski, który wniósł manifestację o dobra pozostałe po nieboszczyku Tomaszu Rzepce z Blinowa dnia 19 8bris 1658 r., że żadnych szkód w dobrach nie dopuścił, podpisując ręką własną:
B. Janorowski mpp.

Replika strony powodowej (Wojciecha Staroszka y Macieja Łysaka) przeciw Katarzynie Rzepkowej: dowodzą iż po śmierci pierwszej żony Agnieszki zostało bydła sztuk 7, pieniędzy fl 200 y na drugie fl 500, co także potwierdził dekret wydany przed J.W. Panem Zakrzewskim [?], a macocha poślubiona bez słusznego zapisu dobra roztrwoniła.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 74,
        "numer_pozycji": "74",
        "strona_pagina": "fol. 35r (35)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Rejestr dóbr i zeznania świadków z Blinowa",
        "osoby_podmioty": "Katarzyna Rzepkowa, Tomasz Rzepka (zm.), Stefan Kondla, Andrzej Kondla, Stanisław Rzepka, Jan Karpiński [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie repliki oraz Regestr Uznania Katarzyny Rzepkowej z wyliczeniem majątku w Blinowie (srebrna łyżka/kubek, bydło, sprzęty) z powołaniem na świadków Stefana i Andrzeja Kondlów z karczmy; u dołu protokół z poniedziałku przed św. Marcinem/Tomaszem 1658 r. i początek zeznań pierwszego świadka Stanisława Rzepki na instancję pracowitej Katarzyny Rzepkowej ze wsi Blinów.",
        "transkrypcja": """35.
... [dokończenie repliki] ... gdyż wszystko to należało do gospodarstwa w Blinowie.

Regestr Uznania Katarzyny Rzepkowej.
Naprzód przyznała do siebie iż po Tomaszu Rzepce została krowa iedna, jałowice dwie, cieląt dwoie, łyżka srebrna, pieniędzy gotowych trochę, pościel y sprzęty domowe. A co mąż jej pożyczył y na długi wydał, to wszystko poświadczyli sąsiedzi ze wsi Blinowa, to iest Stefan Kondla y Andrzej Kondla z karczmy, którzy przy śmierci jego byli y ostatnią wolę słyszeli.

Actum coram Off[ici]o Advocati et Scab. Iur. f[e]ria 2da ante Festum S. Martini Episcopi [lub S. Thomae?] prox. Anno 1658.
Ad instantiam Laboriosae Catharinae Rzepkowa subditae de Villa Blinow.
Testes infra scripti ad Offm. p[rae]s[ens] ad phibendum fidele testimonium citati...
1mus Testis Lab. Stanisław Rzepka subditus de Villa Blinow zeznał pod przysięgą jako dobrze pamięta iż gdy Tomasz Rzepka chorował, przyszedł tam Jan Karpiński [?] y Stefan Kondla z bratem swoim Andrzejem Kondlą, przy których nieboszczyk Tomasz rozporządzał swoim majątkiem y prosił o opiekę nad żoną y dziećmi.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 75,
        "numer_pozycji": "75",
        "strona_pagina": "fol. 35v (35 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Zeznania świadków ze wsi Blinów",
        "osoby_podmioty": "Stanisław Rzepka, Jan Karpiński, Stefan Kondla, Andrzej Kondla, Tomasz Rzepka (zm.), Katarzyna Rzepkowa",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie zeznań Stanisława Rzepki oraz zeznania drugiego i trzeciego świadka ze wsi Blinów — Jana Karpińskiego i Stefana Kondli — o spotkaniu w drodze do Budzynia, rozmowach z Tomaszem Rzepką w obecności Andrzeja Kondli oraz o rejestrach i opiece nad dobrami w Blinowie.",
        "transkrypcja": """35 N.
... [dokończenie zeznań 1. świadka Stanisława Rzepki] ... iż ostatnią wolę swoią przed sąsiadami wyznał, prosząc aby żona Katarzyna przy swoim pozostała y krzywdy nie miała.

2dus Testis Laboriosus Joannes Karpiński subditus de eadem Villa Blinow absolutis omnibus iuramentis zeznał jako wiedział o bytności Tomasza Rzepki, gdy szedł do lasu do Budzynia, gdzie rozmowę miał z nim Stefan Kondla y Andrzej Kondla względem rejestrów y pieniędzy po zmarłym, a nieboszczyk prosił aby w zgodzie żyli y sieroty z żoną opatrzyli, nie czyniąc im krzywdy.

3tius Testis Lab. Stephanus Kondla subditus de eadem Villa Blinow absolutis omnibus iuramentis zeznał jako był przy śmierci Tomasza Rzepki wraz z Janem Karpińskim, Stanisławem Rzepką y bratem swoim Andrzejem Kondlą, słysząc wszystkie słowa zmarłego o rozporządzeniu dobrami y regestrem, które wiernie potwierdza.""",
        "link_swa": UNIT_LINK
    }
]

# Weryfikacja i podmiana/dopisanie
existing_nums = {r["nr_skanu"] for r in main_data}
for rec in part3_scans:
    assert rec["nr_skanu"] not in existing_nums, f"Duplikat nr_skanu {rec['nr_skanu']}"
    main_data.append(rec)

main_data.sort(key=lambda x: x["nr_skanu"])

with open('/home/ubuntu/workspace/Gen/main_data_j20_part3.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j20_part3.json: {len(main_data)} skanow")
