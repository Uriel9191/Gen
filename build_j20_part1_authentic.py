# -*- coding: utf-8 -*-
import json

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"

part1_scans = [
    {
        "nr_skanu": 1,
        "numer_pozycji": "1",
        "strona_pagina": "klatka początkowa",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1959",
        "kategoria": "Metryka Archiwalna / Początek mikrofilmu nr 110399 (30 X 1959)",
        "osoby_podmioty": "Wojewódzkie Archiwum Państwowe w Lublinie",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Klatka tytułowa początku mikrofilmu nr 110399 (Akta Miasta Kraśnika), wykonana przez Laboratorium Mikrofilmowe Archiwum Dokumentacji Mechanicznej dnia 30 października 1959 r.",
        "transkrypcja": """--- Skan #1 (klatka początkowa) ---
WOJEWÓDZKIE
ARCHIWUM PAŃSTWOWE
LUBLIN

AKTA MIASTA: KRAŚNIKA
NR TOMU
NR MIKROFILMU 110399
LAB. MIKROFILM. ARCH. DOKUM. MECHANICZNEJ
Początek
DN. 30 M-C 10 ROK 1959 r.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 2,
        "numer_pozycji": "2",
        "strona_pagina": "metryczka Wzór Nr 1",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1959",
        "kategoria": "Metryka Archiwalna / Formularz Wzór Nr 1",
        "osoby_podmioty": "Wojewódzkie Archiwum Państwowe w Lublinie",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Metryczka akt (Wzór Nr 1) dla jednostki o dawnej sygnaturze archiwalnej 7: 'Księga m. Kraśnika różnych czynności cywiln.', data przygotowania do mikrofilmowania 9 IV 1959 r., ilość zdjęć 274, nr książki kontrolnej 110399.",
        "transkrypcja": """--- Skan #2 (metryczka Wzór Nr 1) ---
Wojewódzkie Archiwum Państwowe w Lublinie
ul. Narutowicza 10, tel. 37-19
Wzór Nr 1
METRYCZKA AKT

Wypełnia archiwum
1. Nazwa archiwum: [WAP Lublin]
2. Nazwa zespołu lub zbioru: Księga m. Kraśnika różnych czynności cywiln.
3. Sygnatura archiwalna: 7
4. Data przygotowania akt do mikrofilmowania: 9. IV. 1959 r.
5. Ilość zdjęć: 274
6. Nr książki kontrolnej: 110.399""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 3,
        "numer_pozycji": "3",
        "strona_pagina": "karta informacyjna",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1959",
        "kategoria": "Metryka Archiwalna / Karta informacyjna (Kraśnik 7)",
        "osoby_podmioty": "Wojewódzkie Archiwum Państwowe w Lublinie",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Karta informacyjna mikrofilmowania (Kraśnik 7): łączna ilość zdjęć 274, wykaz stron pustych niefotografowanych (43, 43v, 44v, 68v, 82v, 112v) oraz wymiary jednostki archiwalnej 33 x 21 cm.",
        "transkrypcja": """--- Skan #3 (karta informacyjna) ---
Kraśnik 7
KARTA INFORMACYJNA

Łączna ilość zdjęć: 274
Wykaz stron pustych niefilmowanych:
43, 43v, 44v, 68v, 82v, 112v.

Wymiary dokumentu, obmiar jednostki archiwalnej
w cm. wysokość x szerokość 33 x 21""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 4,
        "numer_pozycji": "4",
        "strona_pagina": "okładka tytułowa",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657–1700",
        "kategoria": "Kodykologia / Okładka i szyld tytułowy (Nr 7 / Nr 465)",
        "osoby_podmioty": "Kancelaria Miasta Kraśnika",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Okładka i XIX/XX-wieczny szyld tytułowy księgi (Nr 7, Nr 465): 'Książka różnych czynności cywilnych miasta Kraśnika z lat 1657, 1658, 1664, 1668, 1683, 1686, 1695, 1697, 1698, 1699. Rękopis zawiera 135 kart'.",
        "transkrypcja": """--- Skan #4 (okładka tytułowa) ---
Nr 7. По описи
Nr 465
Książka różnych czynności cywilnych
miasta Kraśnika
z lat
1657 - 1658 - 1664 - 1668
1683 - 1686 - 1695 - 1697 -
1698 - 1699.

Rękopis zawiera 135 kart.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 5,
        "numer_pozycji": "5",
        "strona_pagina": "karta ochronna (XIX w.)",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "XIX w.",
        "kategoria": "Kodykologia / Wtórna karta ochronna (fragment formularza XIX w.)",
        "osoby_podmioty": "Introligatornia / Kancelaria XIX w.",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Wtórna karta ochronna oprawy zawierająca odwrócony fragment drukowanego formularza przesłuchania świadka z XIX w. w sprawie popisu wojskowego ('Religii jestem Katolickiej', 'w szczególności ad 2. Odpowiedź na 2.').",
        "transkrypcja": """--- Skan #5 (karta ochronna XIX w., tekst odwrócony) ---
...lat mam / Religii jestem Katolickiej
rodem / Mieszkam w / Utrzymuję się
Pod Sądem nie byłem nigdy.—
w SZCZEGÓLNOŚCI
ad 2. Odpowiedź na 2.
Familię znam bardzo dobrze i jest mi wiadomo
dostatecznie, że niemają żadnego Syna
który by dla jakiego kolwiek powodu wolnym był od popisu Woyskowego, albowiem...
Item Świadkowie obydwa upomnieni o ważności przysięgi i skutkach
krzywoprzysięstwa wykonali przysięgę w rothę 'że wszystko zeznałem rzetelnie
sumiennie.' Czego protokół spisany po przeczytaniu gdy stawający oświadczyli...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 6,
        "numer_pozycji": "6",
        "strona_pagina": "fol. 1r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Relacje, najście i długi (Nr 1)",
        "osoby_podmioty": "Stanisław Kołodziejczyk, Maciej Konięga, Wojciech Jataniec [Jatańczyk?], Błażej Dzierżek, Błażej Kołodziejczyk, Maciej Dąbek [Bęben?], Katarzyna Baltazarowa [Balcerzykowa?], Marcin Paplenik [?], wdowa Frysiowa [?]",
        "kwoty_podatki": "Półkorca żyta",
        "opis_sprawy": "Pierwsza karta księgi (Nr 1, 1657 r.): relacja Stanisława Kołodziejczyka i Macieja Konięgi o słowach Wojciecha Jatańca [Jatańczyka?] i Błażeja Dzierżka; sesja z 23 XI 1657 r. (przed św. Katarzyną): Błażej Kołodziejczyk przeciw Maciejowi Dąbkowi [Bębnowi?] o najście domu; sprawa Katarzyny Baltazarowej [Balcerzykowej?]; sprawa Marcina Paplenika [?] przeciw wdowie Frysiowej [?] o półkorca żyta.",
        "transkrypcja": """--- Skan #6 (fol. 1r) ---
1657 Nr 1.
Relatio DD. Scabinorum pro D. Advocato.
Przed Aktami sławetny Błażej Kołodziejczyk y Maciej Konięga Ławnicy przysięgli...
zeznali że słyszeli od Wojciecha Jatańca [Jatańczyka?]... o Błażeju Dzierżku...
gdy w domu rozprawy czynili... o czym świadectwo dają...

Actum feria sexta ante Festum S. Catharinae Virginis et Martyris 1657.
Inter Famatum Blasium Kołodziejczyk Actorem ac Mathiam Dąbek [Bęben?] Citatum.
Sprawa z Lublina o najście domu... przed Sądem niniejszym...
odesłana do dalszej rozprawy prawnej.

Ad instantiam Catharinae Baltazarowa [Balcerzykowa?]...
o niedbałość w sprawie spadkowej...

Inter Martinum Paplenik [?] Actorem ac Viduam Frysiowa [?] Citatam.
Skarży się Aktor na pozwaną wdowę o półkorca żyta... Sąd nakazuje
aby na przyszły termin oddała.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 7,
        "numer_pozycji": "7",
        "strona_pagina": "fol. 1v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Długi i sprawa kołodziejska (Skwarek vs Batusik)",
        "osoby_podmioty": "Piotr [?] (z Urzędowa), wdowa Anna Pękowa [?], Walenty Lasek [Łączek?], Jan Kender [?] Żyłówka [?], Wojciech Potocki, Świdnicki [?], Marlik [?], Walenty Skwarek [?], Wojciech Batusik",
        "kwoty_podatki": "15 fl, 8 fl",
        "opis_sprawy": "Sprawy przed Sądem Wójtowskim w listopadzie 1657 r.: Piotr [?] z Urzędowa przeciw wdowie Annie Pękowej [?] o dług nieboszczyka; kontumacja Walentego Laska [Łączka?]; sprawa Jana Żyłówki [?] przeciw Wojciechowi Potockiemu o 15 fl i 8 fl; sprawa Świdnickiego [?] z Marlikiem [?]; sesja z 26 XI 1657 r. (poniedziałek po św. Katarzynie): Walenty Skwarek [?] przeciw Wojciechowi Batusikowi o robotę kołodziejską.",
        "transkrypcja": """--- Skan #7 (fol. 1v) ---
Inter Famatum Petrum [?] de Urzędów Actorem ac Viduam Annam Pękowa [?] Citatam.
Skarży się Aktor na dług uszły po nieboszczyku... świadectwo składa...

Contumax Beatus [?] Valentini Lasek [Łączek?] ex relatione Bedelli
qui tertio citatus in Contumaciam pronuntiatus est.

Ex Remissione... Joannes Kender [?] Żyłówka [?] Actorem ac Albertum Potocki Citatum.
Skarży się Aktor na dług fl 15 za krowę... czego tylko fl 8 oddał...

Inter Świdnicki [?] et Marlik [?].
Sprawa o zagon roli... Quod juris solidum est.

Actum Coram Officio Advocati et Scabinorum Juratorum feria secunda post
Festum S. Catharinae Virginis 1657.
Inter Valentinum Skwarek [?] Actorem ac Albertum Batusik Citatum.
Skarży się Aktor na Pozwanego iż mu nie oddał kół y roboty kołodziejskiej
którą mu dał zrobić, czego się teraz przed Sądem domaga.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 8,
        "numer_pozycji": "8",
        "strona_pagina": "fol. 2r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Przysięgi, świadectwa i zeznanie M. Łycka",
        "osoby_podmioty": "Walenty Skwarek [?], Wojciech Batusik, Żyd Benedykt Babińczyk [?], Błażej Kołodziejczyk (ławnik), Sebastian Dąbrowicz [?] (z Bielic?), Stanisław Bendralik, Andrzej Marlik [?], Mielchik [?], Paweł Łycek, Mikołaj Łycek (brat)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie dekretu Walentego Skwarka [?] przeciw Wojciechowi Batusikowi; dopuszczenie Żyda Benedykta Babińczyka [?] do przysięgi; zeznanie świadka Sebastiana Dąbrowicza [?] na prośbę Błażeja Kołodziejczyka (wzmianka o Stanisławie Bendraliku); sprawa Andrzeja Marlika [?] przeciw Mielchikowi [?]; zeznanie Mikołaja Łycka dla brata Pawła Łycka w sprawie obligu.",
        "transkrypcja": """--- Skan #8 (fol. 2r) ---
...Uważa Pozwany że nie jest winien... Aktor replicando wnosi do zeznania
świadków... Urząd nakazuje aby Pozwany w sobotę robotę oddał albo
pieniądze złożył. Quod Decretum ab utraque parte susceptum est.

Indulsit Juramentum perfido Judaeo Benedicto Babińczyk [?]
feria quarta proxima.

Testimonium parte Famati Blasii Kołodziejczyk.
Testis Laboriosus Sebastianus Dąbrowicz [?] de Bielice [?] sub juramento...
zeznaje iż będąc na drodze widział gdy Błażej Kołodziejczyk y Stanisław
Bendralik... o czym świadectwo czyni.

Inter Andream Marlik [?] Actorem ac Mielchik [?] Citatum.
Inhaerendo Decreto Coram Officio Advocati... o rozliczenie sumy według rejestru.

Testimonium pro parte Pauli Łycek de Obligatione.
Testis Mikołaj Łycek brat rodzony Pawła Łycka świadczy iż o tym długu
dobrze wiedział jako brat mój dał pieniędzy...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 9,
        "numer_pozycji": "9",
        "strona_pagina": "fol. 2v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Obdukcja ran (Mikołaj Pisak alias Rusek) / Dług Treli",
        "osoby_podmioty": "Paweł Łycek, Anna Łyckowa (wdowa), Mikołaj Pisak [?] alias Rusek [?], Augustyn Kurowic (ławnik), Grzegorz Fox (ławnik), Jakub Rogalowski [?], Jan Lech, Stanisław Trela, Anna Łapczyńska [?]",
        "kwoty_podatki": "6 fl 20 gr",
        "opis_sprawy": "Sprawa Pawła Łycka przeciw wdowie Annie Łyckowej o opiekę; poniżej szczegółowa obdukcja ran (Obductio Nicolai Pisak [?] alias Rusek [?]) dokonana przez ławników Augustyna Kurowica i Grzegorza Foxa w domu Jakuba Rogalowskiego [?] (rany krwawe na skroniach i siniaki zadane w domu Jana Lecha); sesja z 28 XI 1657 r.: Stanisław Trela przeciw Annie Łapczyńskiej [?] o dług 6 fl 20 gr.",
        "transkrypcja": """--- Skan #9 (fol. 2v) ---
Inter Paulum Łycek de Obligatione Actorem ac Viduam Annam Łyckowa Citatam.
Dano dylacyję do soboty... do sprawy opiekunów... Quod juris solidum est.

Obductio Nicolai Pisak [?] alias Rusek [?].
Przed Mężami Augustynem Kurowicem y Grzegorzem Foxem Ławnikami Przysięgłymi
Kraśnickimi stanąwszy w domu Jakuba Rogalowskiego [?] ukazał rany swoje
Mikołaj Pisak alias Rusek: naprzód na skroni dwie rany krwawe, na prawej
skroni jedna rana krwawa, na lewej jedna rana krwawa, siniaki na boku...
których to ran nabawił się w domu Jana Lecha podczas pijatyki...
Quod ad affectationem partis insertum est.

Actum Coram Officio Advocatiali feria quarta ante Festum S. Andreae 1657.
Inter Stanislaum Trela Actorem ac Annam Łapczyńska [?] Citatam.
Skarży się Aktor na Pozwaną o fl 6 gr 20 winnych długu...
który to dług na przyszłą sobotę oddać powinna.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 10,
        "numer_pozycji": "10",
        "strona_pagina": "fol. 3r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Spór o opiekę Łycków (30 złp) i długi",
        "osoby_podmioty": "Stanisław Trela, Anna Łapczyńska [?], Paweł Łycek, Anna Łyckowa (wdowa), Anna Żyłówka [?], Wojciech Kulka, Wojciech Mazur, Jan Sienka [?]",
        "kwoty_podatki": "6 fl 20 gr, 30 złp, 7 fl, 2 fl",
        "opis_sprawy": "Dokończenie sprawy Stanisława Treli z Anną Łapczyńską [?] (6 fl 20 gr); proces Pawła Łycka przeciw wdowie Annie Łyckowej o 30 złp i rozliczenie 11 lat opieki (nakaz przysięgi z dwoma świadkami); sprawa wdowy Anny Żyłówki [?] przeciw Wojciechowi Kulce o 7 fl odsetek z kotliny; sprawa urzędowa przeciw Wojciechowi Mazurowi i Janowi Sience [?] o 2 fl.",
        "transkrypcja": """--- Skan #10 (fol. 3r) ---
...a z tych pieniędzy... które kończy... 6 fl 20 gr
ad satisfactionem... Quod juris solidum est.

Inter Paulum Łycek Actorem ac Annam Viduam Łyckowa Citatam.
Skarży się Aktor na Pozwaną o dług fl 30 który nieboszczyk zostawił...
po której przez lat 11 jako sierota dbała... a teraz trzydzieści złotych
oddać nie chce. Sąd niniejszy nakazuje aby Aktor przysiągł z dwoma
świadkami na krucyfiks jako nic nie otrzymał, a wtedy Pozwana 30 fl odda.

Inter Viduam Annam Żyłówka [?] Actricem ac Albertum Kulka Citatum.
O dług fl 7 z procentem od kotliny... Sąd nakazuje aby na przyszły tydzień
zapłacił pod egzekucyją.

Inter eundem Officium ac Albertum Mazur et Joannem Sienka [?] Citatos.
Skarży się na nich o dług fl 2... na rzecz kościoła i miasta.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 11,
        "numer_pozycji": "11",
        "strona_pagina": "fol. 3v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Zeznanie W. Olęckiego i procesy W. Sydkowica",
        "osoby_podmioty": "Wojciech Mazur, Jan Sienka [?], Wojciech Olęcki (mieszczanin i szewc), Wawrzyniec Sydkowic, Koniarska [?], Zuzanna Jasińska [?], Szymon Jasielski, Augustyn Lasek [Łycek?]",
        "kwoty_podatki": "1 fl 15 gr, 5 fl, 25 fl, 6 gr",
        "opis_sprawy": "Dokończenie sprawy Wojciecha Mazura i Jana Sienki [?]; zeznanie szewca Wojciecha Olęckiego na prośbę Wawrzyńca Sydkowica o bójce na jarmarku w Łęcznej; sprawa Koniarskiej [?] przeciw Zuzannie Jasińskiej [?] o 1 fl 15 gr (wzmianka o 5 fl); sprawa Wawrzyńca Sydkowica przeciw Szymonowi Jasielskiemu (dylacja na świadków) oraz przeciw Augustynowi Laskowi [Łyckowi?] o 25 fl.",
        "transkrypcja": """--- Skan #11 (fol. 3v) ---
...których za fl 2 a siódmy grosz... na rzecz ubogich... Quod Decretum ab utraque parte susceptum est.

Testimonium parte Laurentii Sydkowic.
Testis Honestus Albertus Olęcki Civis et Sutor Crasnicensis recognovit:
Po jarmarku w Łęcznej kiedyśmy się zeszli w domu u Jana...
przyszedł Sydkowic y porwał się za włosy z Batusiem...
a ludzie rozebrali ich. Quod ad affectationem partis insertum est.

Inter Koniarska [?] Actricem ac Zuzannam Jasińska [?] Citatam.
Skarży się Aktorka na fl 1 gr 15 długu... z czego już tylko 5 fl
oddać powinna... Quod Decretum ab utraque parte susceptum est.

Inter Laurentium Sydkowic Actorem ac Simonem Jasielski Citatum.
Dana y pozwolona jest Dylacyja do przedstawienia świadków na dwa tygodnie.

Inter eundem Actorem ac Augustinum Lasek [Łycek?] Citatum.
Skarży się Aktor o dług fl 25 y gr 6 z zapisu...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 12,
        "numer_pozycji": "12",
        "strona_pagina": "fol. 4r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Sprawy Koniarskiej i Barbary Kuśnierz (43 złp)",
        "osoby_podmioty": "Maciej Konięga, Koniarska [?], Zuzanna Jasińska [?], Barbara Kuśnierz [?], Kudła [?]",
        "kwoty_podatki": "43 złp",
        "opis_sprawy": "Dokończenie sprawy o dług z Łęcznej/Kraśnika (wzmianka o Macieju Koniędze); dalszy ciąg procesu Koniarskiej [?] z Zuzanną Jasińską [?] (odesłanie na Brzeg Krakowski?); poniżej sesja z 1 XII 1657 r. (sobota po św. Andrzeju): Barbara Kuśnierz [?] przeciw Kudle [?] o zapis 43 złp na gruncie.",
        "transkrypcja": """--- Skan #12 (fol. 4r) ---
...sądzić się do Lublina / do dalszego rozstrzygnięcia...
Maciej Konięga świadczy iż tak było... Quod Decretum ab utraque parte susceptum est.

Inter Koniarska [?] Actricem ac Zuzannam Jasińska [?] Citatam.
Sąd niniejszy nakazuje aby na Brzeg Krakowski stawiła się z dokumentami...
Quod Decretum ab utraque parte susceptum est.

Actum Coram Officio Advocati et Scabinorum Juratorum Sabbato post Festum S. Andreae Apostoli 1657.
Inter Barbaram Kuśnierz [?] Actricem ac Kudła [?] Citatam.
Skarży się Aktorka na Pozwaną o dług zapisany na gruncie za fl 43...
z którego gruntu po dziś dzień nic nie oddaje... Sąd nakazuje aby
w czterech tygodniach dług zapłaciła albo grunt puściła.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 13,
        "numer_pozycji": "13",
        "strona_pagina": "fol. 4v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Długi Treli, Domiłka i Błażejowskiej",
        "osoby_podmioty": "Stanisław Trela, Anna Łapczyńska [?], Andrzej Domiłek [?], Zofia Zielińska [?], szl. Błażejowska [?], Żyłówka [?], Adam Szafraniec [?], Świniarka [?]",
        "kwoty_podatki": "6 fl 20 gr",
        "opis_sprawy": "Dekret w sprawie Stanisława Treli przeciw Annie Łapczyńskiej [?] o 6 fl 20 gr; sesja z 4 XII 1657 r. (wtorek przed św. Mikołajem): Andrzej Domiłek [?] przeciw Zofii Zielińskiej [?] i jej mężowi o dług z rejestru; sprawa szl. Błażejowskiej [?] przeciw Żyłówce [?] o grzywny na Brzegu Krakowskim; sprawa Adama Szafrańca [?] przeciw Świniarce [?].",
        "transkrypcja": """--- Skan #13 (fol. 4v) ---
Inter Stanislaum Trela Actorem ac Annam Łapczyńska [?] Citatam.
Ponieważ Citat nie okazał żadnego kwitu z zapłaty fl 6 gr 20...
Sąd nakazuje aby dług oddał w przyszły piątek. Quod Decretum ab utraque parte susceptum est.

Actum Coram Officio Advocati et Scabinorum Juratorum feria tertia ante Festum S. Nicolai Episcopi 1657.
Inter Andream Domiłek [?] Actorem ac Sophiam Zielińska [?] et Maritum ejus Citatos.
O dług z rejestru... Sąd nakazuje aby zapłacili na przyszły tydzień.

Inter Nobilem Błażejowska [?] Actricem ac Żyłówka [?] Citatam.
Z dekretu Sądu niniejszego nakazano jest aby się stawiła na Brzegu Krakowskim...

Inter Adamum Szafraniec [?] Actorem ac Świniarka [?] Citatam.
Dano dylacyję do przyszłego piątku.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 14,
        "numer_pozycji": "14",
        "strona_pagina": "fol. 5r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Spór o krowę, przysięga Jajczykówny i długi Kurowica",
        "osoby_podmioty": "Jan Buła [?], Walenty Olesek [?], Stanisław Kosek, Zuzanna Jajczykówna [?], Katarzyna Śliżanka [?], Walenty Sitarski, Augustyn Kurowic (ławnik), Augustyn Paździech [?], Jan Batusik, Grzegorz Łapka [Rzepka?], Koniarska [?]",
        "kwoty_podatki": "8 fl, 23 fl, 11 fl",
        "opis_sprawy": "Sprawa Jana Buły [?] przeciw Walentemu Oleskowi [?] o 8 fl za krowę (wzmianka o Stanisławie Kosku); przysięga Zuzanny Jajczykówny [?] z udziałem Katarzyny Śliżanki [?] i Walentego Sitarskiego; zeznanie Augustyna Paździecha [?] dla ławnika Augustyna Kurowica; sprawa Jana Batusika przeciw Grzegorzowi Łapce [Rzepce?] o dwie kopy żyta; sprawa Augustyna Kurowica przeciw Koniarskiej [?] o 23 fl i 11 fl.",
        "transkrypcja": """--- Skan #14 (fol. 5r) ---
Inter Joannem Buła [?] Actorem ac Valentinum Olesek [?] Citatum.
Skarży się Aktor na Pozwanego o krowę sprzedaną po fl 8, a Stanisław Kosek
świadczy iż zapłata miała być na terminie...

Juramentum Zuzannae Jajczykówna [?].
Katarzyna Śliżanka [?] zeznała... przy Walentym Sitarskim o krowie...

Testimonium pro parte Famati Augustini Kurowic.
Testis Augustinus Paździech [?] sub juramento recognovit iż słyszał
w domu u Krawca o tej sumie...

Inter Joannem Batusik Actorem ac Gregorium Łapka [Rzepka?] Citatum.
Skarży się Aktor o dwie kopy żyta... Sąd nakazuje aby na przyszły termin oddał.

Inter Famatum Augustinum Kurowic Actorem ac Koniarska [?] Citatam.
Skarży się Aktor o dług fl 23 i interes fl 11 z zapisu...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 15,
        "numer_pozycji": "15",
        "strona_pagina": "fol. 5v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Relacja ławników dla Wojciecha Butka (45 i 55 złp)",
        "osoby_podmioty": "Augustyn Kurowic (ławnik), wdowa Bogucka [Bugajowa?], szl. Sulski [?], Wojciech Butek [?], Grzegorz Fox (ławnik), Marcin Dolski (brat zięcia)",
        "kwoty_podatki": "23 fl, 27 fl, 45 fl, 55 fl",
        "opis_sprawy": "Dokończenie sprawy Augustyna Kurowica (27 fl i 23 fl); sprawa A. Kurowica przeciw wdowie Boguckiej [Bugajowej?]; sprawa szl. Sulskiego [?] przeciw Wojciechowi Butkowi [?]; poniżej relacja ławników Augustyna Kurowica i Grzegorza Foxa z wizji i rozmowy z Wojciechem Butkiem oraz Marcinem Dolskim w sprawie długów 45 fl i 55 fl.",
        "transkrypcja": """--- Skan #15 (fol. 5v) ---
...sumę fl 27... y drugie fl 23... Quod susceptum est ab utraque parte.

Inter Famatum Augustinum Kurowic Actorem ac Viduam Bogucka [Bugajowa?] Citatam.
Sąd nakazuje aby zeznanie złożyła co do zagonu roli...

Inter Nobilem Sulski [?] Actorem ac Albertum Butka [?] Citatum.
Nakazano jest aby Pozwany na przyszły termin pieniądze złożył.

Relatio DD. Scabinorum ex parte Alberti Butka [?].
Przed Mężami Augustynem Kurowicem y Grzegorzem Foxem Ławnikami
Kraśnickimi stanąwszy Marcin Dolski brat rodzonego zięcia Wojciecha Butka
zeznał w obecności ławników względem sum fl 45 i fl 55...
jako te pieniądze należą Wojciechowi Butkowi z zapisu...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 16,
        "numer_pozycji": "16",
        "strona_pagina": "fol. 6r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1656",
        "kategoria": "Sąd Łączony i Wójtowski / Sprawy z grudnia 1656 r. (Koniński, Madejski)",
        "osoby_podmioty": "Stochański [?], Grzegorz Zieliński, Jan Kotlarek, Andrzej Kotlarek, Jadwiga Kotlarka, Augustyn Kurowic, Koniński [Komiński?], Elżbieta Konińska, Bochan [?], Andrzej Szpakowski, Stanisław Madejski [Madeick?], Wawrzyniec Rzepka, Jakub Rogalka [Rogala?]",
        "kwoty_podatki": "15 gr",
        "opis_sprawy": "Sprawa Stochańskiego [?] przeciw Grzegorzowi Zielińskiemu o 15 gr; sesja Sądu Łączonego z soboty po Niepokalanym Poczęciu NMP 1656 r. (9 XII 1656): Jan, Andrzej i Jadwiga Kotlarkowie (z opiekunem Augustynem Kurowicem) przeciw Konińskiemu [Komińskiemu?] i jego żonie Elżbiecie o dobra po Bochanie [?] i Andrzeju Szpakowskim; sesja Sądu Wójtowskiego z 13 XII 1656 r. (św. Łucja): Stanisław Madejski [Madeick?] przeciw Wawrzyńcowi Rzepce (relacja woźnego Jakuba Rogalki).",
        "transkrypcja": """--- Skan #16 (fol. 6r) ---
Inter Famatum Stochański [?] Actorem ac Honestum Gregorium Zieliński Citatum.
O dług gr 15... Sąd nakazuje aby Aktor dowiódł świadkami na terminie.

Actum Crasnicii Coram Officio Composito Consulari Advocati et Scabinorum
Juratorum Crasnicensium Sabbato post Festum Conceptionis B. M. Virginis Anno 1656.
Inter Honestos Joannem et Andream ac Hedvigim Kotlarka Famati Augustini
Kurowic Tutelam gerentem Actores ac Honestum Koniński [Komiński?] et
Consortem ejus Elisabetham Citatos.
Sąd tedy niniejszy Wójtowski y Ławniczy Przysięgły Kraśnicki przesłuchawszy
kontrowersyi stron obydwu... nakazuje aby dobra po niegdy Bochanie [?]
y Andrzeju Szpakowskim podzielone zostały według prawa.

Actum Coram Officio Advocati et Scabinorum Juratorum Crasnicensium
feria quarta ipso festo S. Luciae Virginis 1656.
Stanislaus Madejski [Madeick?] contra eximium Laurentium Rzepka.
Providus Jacobus Rogalka Bedellus Officii Advocatialis Juratus fecit relationem
iż pozwał Wawrzyńca Rzepkę na żądanie Stanisława Madejskiego.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 17,
        "numer_pozycji": "17",
        "strona_pagina": "fol. 6v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1656",
        "kategoria": "Sąd Wójtowski / Sprawy z grudnia 1656 r. (Młodnicka vs Pieniążek, Cwik vs Łycek)",
        "osoby_podmioty": "Augustyn Morawek [?] (z Rudek), Wojciech Łysak [?], Maryna Młodnicka (wdowa), Andrzej Pieniążek (ślusarz), Andrzej Cwik [?], Wojciech Łycek [?], Marcin Starzyński (ławnik), Błażej Kołodziejczyk (ławnik)",
        "kwoty_podatki": "54 fl, 60 fl",
        "opis_sprawy": "Sesja z 15 XII 1656 r. (piątek przed św. Tomaszem): Augustyn Morawek [?] z Rudek przeciw Wojciechowi Łysakowi [?] o 54 fl za żyto; protestacja wdowy Maryny Młodnickiej przeciw ślusarzowi Andrzejowi Pieniążkowi; sprawa Andrzeja Cwika [?] przeciw Wojciechowi Łyckowi [?] o 60 fl; na dole nagłówek sesji z 18 XII 1656 r. z ławnikami Marcinem Starzyńskim i Błażejem Kołodziejczykiem.",
        "transkrypcja": """--- Skan #17 (fol. 6v) ---
Actum Coram Officio Advocati et Scabinorum Juratorum feria sexta ante Festum S. Thomae Apostoli 1656.
Inter Augustinum Morawek [?] Tutorem de Rudki Subditum Actorem ac Albertum Łysak [?] Citatum.
Skarży się Aktor o fl 54 za żyto sprzedane... Sąd nakazuje aby
świadków stawił na przyszły termin.

Diligentia Honestae Mariae Młodnicka contra Andream Pieniążek senfabrum.
Honesta Maria Młodnicka vidua derelicta... solenniter manifestata est
contra Andream Pieniążek senfabrum o zwrot długu i narzędzi.

Inter Honestum Andream Cwik [?] Actorem ac Albertum Łycek [?] Citatum.
Skarży się Aktor na Pozwanego o dług fl 60... Sąd nakazuje aby na
przyszły termin zapłacił albo rękojmię stawił.

Actum Coram Officio Advocati et Scabinorum Juratorum Crasnicensium
praesente ipso D. Advocato aliisque Famatis Martino Starzyński et Blasio Kołodziejczyk
feria secunda ante Festum S. Thomae Apostoli [1656].""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 18,
        "numer_pozycji": "18",
        "strona_pagina": "fol. 7r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1656",
        "kategoria": "Sąd Wójtowski / Protestacja sługi Jerzego Espena przeciw rajcy M. Sitarskiemu",
        "osoby_podmioty": "Jerzy Espen [?] (sługa J. Deserta z Lublina), Jakub Desert (mieszczanin lubelski), Marcin Sitarski (rajca kraśnicki), Stanisław Nawrocki (rajca kraśnicki), Marcin Starzyński (ławnik), Błażej Kołodziejczyk (ławnik)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Sesja z 18 XII 1656 r.: głośna protestacja Jerzego Espena [?], sługi mieszczanina lubelskiego Jakuba Deserta, przeciw rajcy kraśnickiemu Marcinowi Sitarskiemu o pobicie w domu rajcy Stanisława Nawrockiego podczas rozmowy w języku niemieckim, z obdukcją ran (podbite lewe oko, zakrwawiona lewa ręka, guzy na głowie) przez ławników Marcina Starzyńskiego i Błażeja Kołodziejczyka.",
        "transkrypcja": """--- Skan #18 (fol. 7r) ---
7. 1656
Protestatio Georgii Espen [?] contra Martinum Sitarski Consulem Crasnicensem.
Ad Officium praesens Advocatiale Crasnicense personaliter veniens Honestus
Georgius Espen [?] Famulus Famati Jacobi Deserti Civis Lublinensis...
contra Dominum Martinum Sitarski Consulem Crasnicensem querela exposuit:
Dnia wczorajszego wieczorem przyszedłem do P. Stanisława Nawrockiego Rajcy
Kraśnickiego... gdzie gdy ja po niemiecku mówił, naraził się P. Sitarski
czego po niemiecku gadam... y na dworze albo na izbie rzucił się na mnie...
z tego uderzenia krew z nosa y ręki poszła...
Na co ławnicy przysięgli Marcin Starzyński y Błażej Kołodziejczyk oglądali:
oko lewe podbite sine krwią zaszło, rękę lewą krwawioną, w głowę kilka
guzów... Oświadczam się o to prawnie czynić. Quod Actis connotatum est.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 19,
        "numer_pozycji": "19",
        "strona_pagina": "fol. 7v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Opieka po Pawle Jajczyku i areszt dóbr u T. Larkowskiego",
        "osoby_podmioty": "Jan Kulka (opiekun), Szymon Jajczyk (opiekun), Paweł Jajczyk (śp.), Tomasz Larkowski, Wojciech Tokarzyk [?], Jan Tatarczuk (szewc), Szymon, Jakub Jajczyk (śp.)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Sprawa opiekunów Jana Kulki i Szymona Jajczyka (dóbr po śp. Pawle Jajczyku) przeciw Tomaszowi Larkowskiemu; sprawa Wojciecha Tokarzyka [?] przeciw Larkowskiemu; areszt założony przez szewca Jana Tatarczuka przeciw Szymonowi; poniżej areszt Jana Kulki i Szymona Jajczyka na dobrach po śp. Jakubie Jajczyku znajdujących się w domu Tomasza Larkowskiego.",
        "transkrypcja": """--- Skan #19 (fol. 7v) ---
Inter Honestos Joannem Kulka et Simonem Jajczyk Tutores bonorum olim
Honesti Pauli Jajczyk Actores ac Honestum Thomam Larkowski Citatum.
Dana y pozwolona jest Dylacyja do blisko przyszłego piątku...

Inter Albertum Tokarzyk [?] Actorem ac Honestum Larkowski Citatum.
Zapisana jest dylacyja do drugiego terminu. Quod juris solidum est.

Joannes Tatarczuk Sutor Arestum imposuit super personam Simonis [?].

Item Joannes Kulka et Simon Jajczyk Tutores bonorum Honesti Pauli Jajczyk
Arestum imposuerunt super bona Honesti Thomae Larkowski.
Do Urzędu y Akt niniejszych Wójtowskich Kraśnickich przyszedłszy oblicznie
Jan Kulka y Szymon Jajczyk Opiekunowie dóbr pozostałych po niegdy Jakubie
Jajczyku położyli solenne Arest na dobrach wszystkich w domu Tomasza
Larkowskiego będących, żądając aby ich nikomu nie wydawał.
Quod Arestum per Bedellum Juratum connotatum est.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 20,
        "numer_pozycji": "20",
        "strona_pagina": "fol. 8r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Sprawy z grudnia 1657 r. (Olęcki, Konięga, Zieliński)",
        "osoby_podmioty": "Andrzej Pieniążek [?], Wojciech Olęcki, Paweł Tarnowczyk [?], Maciej Konięga (ławnik), Jan Skura [Skóra?], Zieliński [?], wdowa Bybina [?], Paweł Gabriel",
        "kwoty_podatki": "4 fl, 1 fl 15 gr, 3 fl 15 gr, 12 gr",
        "opis_sprawy": "Dokończenie aresztu (wzmianka o Andrzeju Pieniążku i 4 fl); sesja z 5 XII 1657 r. (wigilia św. Mikołaja): Wojciech Olęcki przeciw Pawłowi Tarnowczykowi [?] o 1 fl 15 gr i 3 fl 15 gr za robotę; ławnik Maciej Konięga przeciw Janowi Skurze [Skórze?] o najście domu; Zieliński [?] przeciw wdowie Bybinej [?] o 12 gr za beczkę i koło od Pawła Gabriela.",
        "transkrypcja": """--- Skan #20 (fol. 8r) ---
...Andrzej Pieniążek zeznał iż fl 4 powinien oddać... Quod Actis connotatum est.

Actum Coram Officio Advocati et Scabinorum Juratorum Crasnicensium
feria quarta in Vigilia S. Nicolai Episcopi 1657.
Inter Albertum Olęcki Actorem ac Paulum Tarnowczyk [?] Citatum.
Skarży się Aktor na Pozwanego iż mu winien za robotę fl 1 gr 15 y drugie
fl 3 gr 15... Sąd nakazuje aby zapłacił bez dalszej zwłoki.

Inter Famatum Mathiam Konięga Actorem ac Joannem Skura [Skóra?] Citatum.
O najście domu y zelżenie... Sąd nakazuje aby na przyszły termin stawił się.

Inter Zieliński [?] Actorem ac Viduam Bybina [?] Citatam.
O beczkę y koło od Pawła Gabriela wzięte za gr 12... Sąd nakazuje zapłatę.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 21,
        "numer_pozycji": "21",
        "strona_pagina": "fol. 8v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Spory z udziałem Konięgi, Kapicy i bójka u Paździechy",
        "osoby_podmioty": "Zieliński [?], Sebastian Jajczyk, Krzysztof Zalasek [Zaleski?], Andrzej Cuda [Ruda?], Maciej Konięga, Szymon Jasielski, Michał Brzostek [?], Adam Kapica, Augustyn Paździech [?], Wawrzyniec Sydkowic",
        "kwoty_podatki": "15 fl",
        "opis_sprawy": "Sprawa Zielińskiego [?] przeciw Sebastianowi Jajczykowi; sprawa przeciw Krzysztofowi Zalaskowi [Zaleskiemu?] i Andrzejowi Cudzie [Rudzie?] o 15 fl długu z 1653 r. (poręczenie Macieja Konięgi); poniżej zeznania świadków Szymona Jasielskiego — Michała Brzostka [?] oraz Adama Kapicy — o bójce i wyzwiskach w domu P. Paździechy [?] z udziałem Wawrzyńca Sydkowica.",
        "transkrypcja": """--- Skan #21 (fol. 8v) ---
Inter Zieliński [?] Actorem ac Sebestianum Jajczyk Citatum.
Zapisana jest dylacyja do drugiego terminu.

Inter eundem Actorem ac Christophorum Zalasek [Zaleski?] et Andream Cuda [Ruda?] Citatos.
Skarży się Aktor na Pozwanych o dług fl 15 z roku 1653, za który Maciej
Konięga poręczył... Sąd nakazuje aby obydwaj do sprawy stanęli.

Testimonium pro parte Simonis Jasielski.
Testis Michael Brzostek [?] post praevium examen sub juramento recognovit:
iż będąc w domu u P. Paździechy [?] słyszał gdy się Szymon Jasielski
z Wawrzyńcem Sydkowicem poswarzyli...
Secundus Testis Adam Kapica similiter sub juramento recognovit ut supra
iż widział gdy się bili y popychali.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 22,
        "numer_pozycji": "22",
        "strona_pagina": "fol. 9r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Spory Sydkowica z Jasielskim, Kołodziejczyka i Łycka",
        "osoby_podmioty": "Wawrzyniec Sydkowic, Szymon Jasielski, Błażej Kołodziejczyk (ławnik), Marcin Siedlecki [Sieradzki?], Adam Szafraniec, Maciej Rzepka [?], Jan Łycek, Grzegorz Kupka [Rzepka?]",
        "kwoty_podatki": "5 fl, 10 fl",
        "opis_sprawy": "Wzajemne skargi Wawrzyńca Sydkowica i Szymona Jasielskiego o pobicie i obelgi; sprawa ławnika Błażeja Kołodziejczyka przeciw Marcinowi Siedleckiemu [Sieradzkiemu?] o skórę butową; sprawa Adama Szafrańca przeciw Maciejowi Rzepce [?] o 5 fl; sprawa Jana Łycka przeciw Grzegorzowi Kupce [Rzepce?] o dwie kopy żyta i 10 fl.",
        "transkrypcja": """--- Skan #22 (fol. 9r) ---
Obligatio Laurentii Sydkowic contra Simonem Jasielski.
Skarży się o krwawe bicie y kradzież...

Simon Jasielski Reproduxit contra Sydkowic.
Że w obronie swojej bronił się... Quod Actis connotatum est.

Inter Famatum Blasium Kołodziejczyk Actorem ac Martinum Siedlecki [Sieradzki?] Citatum.
Skarży się na niego o skórę butową zabraną z roboty... Sąd nakazuje
aby ją oddał albo zapłacił.

Inter Adamum Szafraniec Actorem ac Mathiam Rzepka [?] Citatum.
O dług fl 5 za Józefa... Sąd nakazuje aby na przyszły termin zapłacił.

Inter Joannem Łycek Actorem ac Gregorium Kupka [Rzepka?] Citatum.
O dług fl 10 y dwie kopy żyta... Sąd nakazuje aby się rozliczył.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 23,
        "numer_pozycji": "23",
        "strona_pagina": "fol. 9v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Sprawa o żyto, Delik vs Olesek i świadkowie Sydkowica",
        "osoby_podmioty": "Jan Łycek, Grzegorz Kupka [Rzepka?], Jan Delik, Olesek [Olęcki?], Kos [?], Satomski [Słomkowski?], Wawrzyniec Sydkowic, Wojciech Rogalowski [?], Maciej Rzepka [?], Szymon Jasielski",
        "kwoty_podatki": "9 fl, 6 gr za korzec",
        "opis_sprawy": "Dokończenie dekretu Jana Łycka; sprawa Jana Delika przeciw Oleskowi [Olęckiemu?] i Kosowi [?] o żyto po 6 gr za korzec i 9 fl; sprawa przeciw P. Satomskiemu [Słomkowskiemu?]; poniżej zeznania świadków Wawrzyńca Sydkowica — Wojciecha Rogalowskiego [?] i Macieja Rzepki [?] — o wyzwiskach rzucanych przez Szymona Jasielskiego.",
        "transkrypcja": """--- Skan #23 (fol. 9v) ---
...a z tego długu fl 3... Sąd nakazuje aby na przyszły termin złożył.

Inter Joannem Delik Actorem ac Olesek [Olęcki?] et Kos [?] Citatos.
Skarży się Aktor o żyto zabrane po gr 6 za korzec y sumę fl 9...
Sąd nakazuje aby mu na przyszły tydzień zapłacili.

Inter Hiacinthum [?] Actorem ac Dnum Satomski [Słomkowski?] Citatum.
Ex decreto praesentis Officii... odesłano do dalszego terminu.

Testimonium pro parte Laurentii Sydkowic.
Testis Honestus Albertus Rogalowski [?] recognovit iż słyszał gdy Szymon
Jasielski wyzywał Wawrzyńca Sydkowica słowami obelżywymi 'jako pies'.
Secundus Testis Mathias Rzepka [?] similiter recognovit ut supra.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 24,
        "numer_pozycji": "24",
        "strona_pagina": "fol. 10r",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski / Proces Sydkowic vs Jasielski oraz spór wójta o konia",
        "osoby_podmioty": "Wawrzyniec Sydkowic, Szymon Jasielski, Wójt Kraśnicki, Józef Zieliński [?], Bujak [?]",
        "kwoty_podatki": "12 fl, 2 fl 15 gr",
        "opis_sprawy": "Kontynuacja procesu Wawrzyńca Sydkowica przeciw Szymonowi Jasielskiemu (dopuszczenie do przysięgi z sześcioma świadkami); poniżej sprawa Wójta Kraśnickiego przeciw Józefowi Zielińskiemu [?] o konia kupionego na jarmarku od Bujaka [?] za 12 fl i dopłatę 2 fl 15 gr.",
        "transkrypcja": """--- Skan #24 (fol. 10r) ---
Inter Laurentium Sydkowic Actorem ac Simonem Jasielski Citatum.
Skarży się Aktor na Pozwanego o zniewagę słowną y obelgę...
Sąd niniejszy nakazuje aby Aktor wykonał przysięgę z sześcioma świadkami
na potwierdzenie swojej niewinności. Quod Decretum ab utraque parte susceptum est.

Inter Famatum D. Advocatum Actorem ac Josephum Zieliński [?] Citatum.
O konia kupionego na jarmarku od Bujaka [?] za fl 12... gdzie tylko
fl 2 gr 15 brakuje... Sąd nakazuje aby na przyszły termin dopłacił
albo konia oddał.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 25,
        "numer_pozycji": "25",
        "strona_pagina": "fol. 10v",
        "sygnatura": "35/40/0/1/20",
        "data_rok": "1657",
        "kategoria": "Sąd Wójtowski i Wielki Gajony / Manifestacja Łyszkowej i najem izby (Konięga)",
        "osoby_podmioty": "Józef Zieliński [?], Zofia Łyszkowa [?] (wdowa), Szymon Jasielski, Paweł Łycek, Maciej Konięga (ławnik), Jan Kępa [?], Andrzej Marlik [?], Anna Zielińska",
        "kwoty_podatki": "2 fl 15 gr, 2 fl (najem izby)",
        "opis_sprawy": "Dokończenie dekretu wójta przeciw Józefowi Zielińskiemu [?] (2 fl 15 gr); manifestacja wdowy Zofii Łyszkowej [?] przed Szymonem Jasielskim przeciw Pawłowi Łyckowi; poniżej Judicium Magnum Bannitum z 7 XII 1657 r. (piątek po św. Mikołaju): sprawa ławnika Macieja Konięgi przeciw Janowi Kępie [?] o 2 fl za najęcie izby i komory oraz sprawa Andrzeja Marlika [?] przeciw Józefowi i Annie Zielińskim.",
        "transkrypcja": """--- Skan #25 (fol. 10v) ---
...fl 2 gr 15... na terminie przyszłym bez zwłoki oddać powinien.

Manifestatio Viduae Łyszkowa [?] contra Paulum Łycek.
Przed Szymonem Jasielskim manifestowała się wdowa Łyszkowa [?] przeciwko
Pawłowi Łyckowi o niesłuszne pozywanie y zatrzymanie długu.

Judicium Magnum Bannitum expositum per Famatum D. Advocatum
feria sexta post Festum S. Nicolai Episcopi 1657.
Inter Famatum Mathiam Konięga Actorem ac Joannem Kępa [?] Citatum.
Skarży się Aktor na Pozwanego iż miał najętą izbę z komorą za fl 2
y do dziś dnia nie zapłacił... Sąd nakazuje aby na przyszły termin
czynsz oddał.

Inter Andream Marlik [?] Actorem ac Josephum Zieliński et consortem ejus Annam Zielińska Citatos.
Zapisana jest dylacyja do dalszego rozpatrzenia.""",
        "link_swa": UNIT_LINK
    }
]

with open('/home/ubuntu/workspace/Gen/main_data_j20_part1.json', 'w', encoding='utf-8') as f:
    json.dump(part1_scans, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j20_part1.json: {len(part1_scans)} rekordów.")
