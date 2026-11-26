# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j18_part3.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989891"

part4_scans = [
    {
        "nr_skanu": 76,
        "numer_pozycji": "76",
        "strona_pagina": "fol. 36r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Protestacje",
        "osoby_podmioty": "Maryna Wardeczyna (wdowa po Jakubie Wardecy), Marcin Rymarczyk (przedmieszczanin), Brakowie (starostowie/sąsiedzi), Stanisław Nawrocki (mieszczanin), Grzegorz Krawiec, Maciej Duda [?], Wojciech Duda [?], Mosiek, Lewek Chapon [?], Lewek Kraśmarz, Witko",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dwie protestacje: (1) wdowy Maryny po Jakubie Wardecy przeciw Marcinowi Rymarczykowi o przechowanie i przywód syna; (2) uroczysta protestacja mieszczan kraśnickich Stanisława Nawrockiego, Grzegorza Krawca, Macieja i Wojciecha Dudów przeciw starozakonnym arendarzom Mośkowi, Lewkowi Chaponowi, Lewkowi Kraśmarzowi i Witkowi o fałszywe regestry, zabór wódki i krzywoprzysięstwo w bożnicy.",
        "transkrypcja": """--- Skan #76 (fol. 36r) ---
Przed Urzędem y Aktami niniejszemi Uciwa Maryna Uciwego
Jakuba Wardecy Przedmieszczanina Krasnickiego małżonka
solennie protestowała się przeciwko Uciwemu Marcinowi
Rymarczykowi Przedmieszczaninowi względem zadania zło-
dziejstwa iako by przechowanie y przywód z synem iego
miało nastąpić przypozwać gotowa Offerens se Vindicare
Velle.

Sub eodem Actu
Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
Krasnickich w osobach swoich przyszedłszy Pracowici Sta-
nisław Nawrocki mieszczanin Miejski, Grzegorz Krawiec,
Wojciech Maciej Dudowie z swoim y brata
specifikowanych sąsiad imieniem solennie z wielkim żalem
protestowali się przeciwko Niewiernym Moskowi, Lew-
kowi Markow[i], Chaponowi Lewkowi Kraśmarzowi Witko-
wskim tutejszym Żydom Arendarzom Oto Iż Oni nie
słusznie swoim wymysłem żydowskim sposobem wykrętarskim
aż z Katolików byli powazyli się niewinnie protestantów
z innemi sąsiadami potwarzyć odłożywszy regestra spe-
cifikowane y który do nich niegi nie zabrali, ale
że niewedług prawa y zwyczaiu przysiądz chcieli y
także młoda w suknach poszli do Bożnicy gdzie
protestantowie Upominali żeby w koszuli śmiertelnej
iako na sądny dzień chodzą na stołki na świni skóre
przysięgali Oniż ponieważ w le mianowicie pomie-
niony Żydów kradzież Sumy cudzej y inne słowa
Uszczypliwe zadawali nad to i przed sądem by pozwalali
coko nieprowincy podano było przed sądem oskarżone
waży y szkody stąd pochodzące, ieżeli takim sposobem
aggrawować powazyli się ludzi niewinnych.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 77,
        "numer_pozycji": "77",
        "strona_pagina": "fol. 36v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Przysięga żydowska w bożnicy",
        "osoby_podmioty": "Mośko, Lewek Marek, Chapon Lewek, Kraśmarz Witko (starozakonni), Andrzej Rzędecki (administrator klucza), Jan Wojtowic (wójt gromadzki wilkołaski), Piotr Debik (ławnik przysięgły), Dudras Wojciech, Wójcik Maciej, Grzegorz Krawiec, Błażej Nowicki",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Sesja z czwartku przed św. Katarzyną 1701 r. (24 XI 1701): manifestacja starozakonnych Mośka, Lewka Marka, Chapona Lewka i Kraśmarza Witka, którzy z rozkazu administratora Rzędeckiego złożyli w bożnicy kraśnickiej przysięgę na rodał przeciw gromadzie wilkołaskiej w obecności wójta wilkołaskiego Jana Wojtowica i ławnika Piotra Debika.",
        "transkrypcja": """--- Skan #77 (fol. 36v) ---
Actum Coram Officio Advocatiali et Scabinali Cra-
snicensi Feria Quinta ante Festum Sanctae Catharinae
Virginis et Martyris proxima Anno Domini Millesimo
Septingentesimo Primo.

Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
Krasnickich w osobach swoich przyszedłszy Starozakon-
ni Lewek Marek, Chapon Lewek, Kraśmarz Witko
Sami Gui manifestati sunt et protestati są według
woli z skryptem Jego Mci Pana Mikołaia[?] Admi-
nistratora Klucza Krasnickiego na ten czas będącego
Jurament w Bożnicy Krasnickiej na rodale in cu[ius]
Juramenti rotham. Ja Mosko, Lewek Marek,
Chapon Lewek przysięgamy Panu Bogu wszech-
mogącemu Iż ten Regestr dłużny U Groma-
dy Wilkołaskiej sprawiedliwie opisaliśmy od tych
ludzi Którzy są w regestrze specifikowani dłużni
należy y do aresztu w statucie de scriptam
praesentes przy tym byli Jan Wojtowic Woyt
gromadzki Wilkołaski Piotr Debik Ławnik
przysięgły Dudras Wojciech Wójcik Maciej, Grzegorz
Krawiec y Błażej Nowicki. Jurament ten był
na rodale.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 78,
        "numer_pozycji": "78",
        "strona_pagina": "fol. 37r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Wykup owoców i dekret",
        "osoby_podmioty": "Stanisław Solecki (burmistrz dzienny kraśnicki), Wojciech Beski (ławnik), Stefan Ciesielski (ławnik), Jan Onuszkowic (wójt kraśnicki), ks. Serafin Jarzynka (pleban dzierzkowicki), Jadwiga Butczyna (wdowa), Sobestian Jarzyk (przedmieszczanin), Jan Skiba, Józef Madejczyk",
        "kwoty_podatki": "30 złp (taksa owoców na Podlesiu)",
        "opis_sprawy": "Zeznanie burmistrza Stanisława Soleckiego oraz ławników Wojciecha Beskiego i Stefana Ciesielskiego w sprawie dekretu wójta Jana Onuszkowica między plebanem dzierzkowickim ks. Serafinem Jarzynką a Jadwigą Butczyną i Sobestianem Jarzykiem o wykup owoców i ogrodu na Podlesiu (taksa owoców 30 złp).",
        "transkrypcja": """--- Skan #78 (fol. 37r) ---
Actum Coram Officio Advocatiali et Scabinali Crasni-
censi Feria Quinta Pridie Festi Sanctae Catharinae
Virginis et Martyris Anno Domini Millesimo Se-
ptingentesimo Primo.

Przed Urzędem y Aktami niniejszemi Woytowskiemi y Ław-
niczemi Krasnickiemi w osobach swoich stanąwszy
Sławetni Panowie Stanisław Solecki Burmistrz dzienny
Krasnicki, Woyciech Beski y Stefan Ciesielski
Ławnicy Jasnie iawnie dobrowolnie zdrowi na u-
mysłach Zeznali praesentibus że znaią Iż Oni wia-
domi y tamże będący dekretu za wójtostwa nie-
gdy Sławetnego Pana Jana Onuszkowica Woyta Krasni-
ckiego, między Wielebnym Jegomością Księdzem Sera-
finem Jarzynką Plebanem Dzierzkowskim Dziadem
Successorem między Uciwą Jadwigą Butczyną o-
piekunem naturalnym z jednej strony a Uciwym
Sobestianem Jarzykiem Przedmieszczaninem Krasni-
ckim Jana Skiby alias Butczyna na dziedzic-
twie na Przedmieściu Krasnickim Podlesie nazwanym
leżącym prawem pozwanym ferowanego gdzie
Oni z tymi natenczas ławnikami z drugimi kolegami
zgodziwszy się na sentencją przysądzili pozwane-
mu odbierać od Summy w karcie wyrażonej o
woce zaś z dzierżawy aby pozwany w sumie ręce
póki nie wytrzyma summy aż na owoce złoży
którą mu iest Chodziliśmy na otaxowanie Owocu
y otaxowaliśmy go złotych trzydzieści który owoc
na Owoce zebrał Miał nieuczyni żadnem prawem
o tymże pomienionym dekrecie dołożono tego
że ieżeliby potrzebował iednego sadu komu
innemu chciał przedać za pomieniony, aby""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 79,
        "numer_pozycji": "79",
        "strona_pagina": "fol. 37v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Apelacja do Trybunału Zamoyskiego i protestacja",
        "osoby_podmioty": "Sobestian Jarzyk, ks. Serafin Jarzynka (pleban dzierzkowicki), Jan Skiba, Józef Madejczyk, Paweł Kłopot (przedmieszczanin), Marcin Ząbek, Żyd (arendarz)",
        "kwoty_podatki": "112 złp, 20 złp",
        "opis_sprawy": "Dokończenie zeznania o dekrecie ks. Jarzynki z Sobestianem Jarzykiem (rozliczenie na 112 złp i 20 złp) oraz apelacja Sobestiana Jarzyka do Trybunału Zamoyskiego. Następnie sesja z piątku w oktawie Niepokalanego Poczęcia NMP 1701 r. (9 XII 1701): protestacja Pawła Kłopota przeciw Marcinowi Ząbkowi o pobicie w domu Żyda.",
        "transkrypcja": """--- Skan #79 (fol. 37v) ---
mimo nich do przedaży pomienionych [dóbr] nie szedł
ponieważ iest na dożywociu Małżonki swojej
o tym świadectwo stanęło że onych ludzi wiary godne to
lepszego tylko pomienionego Jarzyka taksowanie
całe y Karta Skibska do Kupna y Wyzwania postano-
wiona na one y swoje zdrowie podpisali y to wszystko
pomieniony Wielebny J.M. Ksiądz Pleban Dzierzkowski
pozwolił z którym się porachował Jarzyk, który mu zło-
żych dwanaście z Awoiem potrąceni w sumę a złotych
sto dziesięć y sześć na gruncie do dalszego Używania
zostały potym złotych dwadzieścia Successorowie
przybrali to wszystko zeznali iak Decretu
praesens relatio. Sub eodem Actu pro parte Sobestiana Jarzyka
chcącego Velle in ausum iść Jarzyk z Opatrznym Made-
iem Mogielskim[?] Uciwego Józefa Madejczyka
Ukarać według apellacyi zdeklarował Termin stanąć do
Sądu Najwyższego Trybunału Państwa Za-
moyskiego Na poniedziałek po pierwszej niedzieli
przyszłej Adwentowej.

Actum Coram Officio Advocatiali et Scabinali Cra-
snicensi Feria Sexta in Octava Festi Immaculatae
Conceptionis Beatissimae Mariae Virginis Anno Domini
Millesimo Septingentesimo Primo.

Do Urzędu y Akt niniejszych Woytowskich y Ławniczych Kra-
snickich w osobie swoiej przyszedłszy Uciwy Paweł Kłopot
Przedmieszczanin Krasnicki solennie z wielkim żalem pro-
testował się przeciwko Uciwemu Marcinowi Ząbkowi
Oto Iż On protestanta dnia wczorajszego gdy nie się
protestant rozumiejąc za długi upominał się łagodnemi
słowy Sędziwymi w domu Niewiernego Żyda Arendarza""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 80,
        "numer_pozycji": "80",
        "strona_pagina": "fol. 38r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Obdukcja i dekrety",
        "osoby_podmioty": "Paweł Kłopot, Marcin Ząbek, Szmul (starozakonny), Michał Piotrowczyk, Sobek Krowa [?], Matyjasz Koza [?], Marcin Rymarczyk, Wawrzyniec Kępka, Jan [?], Matyjasz Kępa",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie obdukcji ran Pawła Kłopota po pobiciu przez Marcina Ząbka; wpis o protestacji przeciw Żydowi Szmulowi (Feria Secunda post S. Andreae 1701); oraz dekrety z poniedziałku po Niepokalanym Poczęciu NMP 1701 r. (12 XII 1701) w sprawach: Michała Piotrowczyka, Marcina Rymarczyka przeciw Wawrzyńcowi oraz Matyjasza Kępy.",
        "transkrypcja": """--- Skan #80 (fol. 38r) ---
tłukł tegoż o to że potym Powierchnie na którym naszliśmy
przynieść budzieli się nie podobało In praesentia Praeceptoris Verifi-
cationem pokazał Pod prawą ręką na boku spuchły
siny o dwóch piędzach w szerz wzdłuż od którego
się zaciążył tak na ranę we obecności prawnej by
mię z nim oto Violencia.

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Secunda post Festum San-
cti Andreae Apostoli proxima Anno 1701mo.
Videatur hoc loco protestatio facta Contra
Infidelem Szmol incolam Crasnicensem
ratione infrascriptae Violentiarum.

Actum Coram Officio Advocatiali et Scabinali Crasni-
censi Feria Secunda post Festum Immaculatae Con-
ceptionis proxima Anno Domini Millesimo Septingen-
tesimo Primo.

W sprawie y Akciej między Uciwym Michałem Piotrowczykiem A-
ktorem z jednej a Koziakową wdową pozwaną o pra-
wicę w tej mieszczącej się nieboszczyka tego zdawny świadek
tymże powodem nie odrzuciła Necessarium Institutionem
probatio probari praemissorum Informatione Officij facto
pro Feria Quarta proxime ventura.

W sprawie y Akciej między Uciwym Marcinem Rymarczy-
kiem Aktorem a Wawrzyńcem pozwanym tak o niewolny
swój iako y stosowanie syna ad contenta protestationis
Obwinionego sprawozdanie świadki z Dzierzkowic
Inquisitiones pro interesse tam ab eorum Stanisla-
wi pozwoleniu na środę przyszłą.

W sprawie y Akciej między Uciwym Matiaszem Kępą Przed-
mieszczaninem Krasnickim Aktorem z jednej a Janem""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 81,
        "numer_pozycji": "81",
        "strona_pagina": "fol. 38v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Spór o niwkę i obdukcja ran",
        "osoby_podmioty": "Matyjasz Kępa, Jan Bratkowski [?], Michał Stadnicki [?], Maciej Stachnik, Andrzej Stachnik, Jan Ławonowicz [?], Kazimierz Zagojski (żołnierz / oskarżony)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie dekretu w sprawie Matyjasza Kępy z Janem Bratkowskim o gwałtowne odebranie roli i niwki (dylacja do Trzech Króli 1702 r.). Następnie sesja z wtorku po Niepokalanym Poczęciu NMP 1701 r. (13 XII 1701): protestacja i obdukcja ran Macieja Stachnika w swoim i brata Andrzeja imieniu przeciw Janowi Ławonowiczowi oraz nota o protestacji przeciw Kazimierzowi Zagojskiemu.",
        "transkrypcja": """--- Skan #81 (fol. 38v) ---
Kępką Bratkowicem względem Niwki pewnej zoraney y zasia-
ney na tymże miejscu Pozwanym z drugiej strony Actor
na rządy Michał Stadnicki alias Stadniczuk czyni o
gwałtowne odebranie roli bez prawa przewodu danego mu
rzeczą Sądową nakazuje trzydniówkę kontynuować Prawa
zaś zapisy testament i jakiekolwiek dokumenta mają prze-
kładać na pierwszą po święcie Trzech Królów w Ro-
ku przyszłym 1702 przypadającą judicii termin peremptorium.

Actum Coram Officio Advocatiali et Scabinali Cra-
snicensi Feria Tertia post Festum Immaculatae Con-
ceptionis Beatissimae Mariae Virginis proxima A. 1701.
Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
Krasnickich w osobie swoiej przyszedłszy Uciwy
Maciej Stachnik z swoim y Andrzeiem Stachnikiem
Brata swego imieniem solennie Iniuria cum dolo
protestował się przeciwko Uciwemu Janowi Ławonowi-
czowi Mieszczaninowi Krasnickiemu Oto Iż On
bez dania okazji poważył się Protestanta y z bratem
skrzywdzić y pomienionych obu tak na propozycjam
o prawa Insumi[?] praesentis verificationem pokazał
raz stłuczony na lewej stronie głowy od ucha
prawego i lewego Item na piersiach od bicia bez
słuszności za sobą będących kije na głowie
nadto brata iego pokazał nad okiem o bolem na ręku
krwi wylew z tego protestantis Offerens se pro iure
Vindicare Velle.

Videatur hoc loco Protestatio Contra D. Casimirum
Zagojski extranei ad Violenciam in praesentis
die hodie in Actis facta et posita est.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 82,
        "numer_pozycji": "82",
        "strona_pagina": "fol. 39r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Dekrety sądowe",
        "osoby_podmioty": "Szymon Moszkowic (starozakonny, obywatel kraśnicki), Paweł [?], Marcin Rymarczyk (przedmieszczanin), Maciej Nadzieja, Matyjasz (syn M. Nadziei), Michał Piotrowczyk, Paweł Powtórny [?]",
        "kwoty_podatki": "3 grzywny (kara sądowa, dwukrotnie), 1 złp 22 gr (szeląg), 20 gr",
        "opis_sprawy": "Sesja z piątku po św. Łucji 1701 r. (16 XII 1701): (1) dylacja w sprawie Szymona Moszkowica do Trzech Króli 1702; (2) dekret w sprawie Marcina Rymarczyka przeciw Maciejowi Nadziei i jego synowi Matyjaszowi (kara po 3 grzywny za nieusprawiedliwione odejście i bluźnierstwo w sądzie); (3) sprawa Michała Piotrowczyka z bratem i Pawłem o dług 1 złp 22 gr i siekierę.",
        "transkrypcja": """--- Skan #82 (fol. 39r) ---
Actum Coram Officio Advocatiali et Scabinali Cra-
snicensi Feria Sexta post Festum Sanctae Luciae pro-
xima Anno Domini Millesimo Septingentesimo
Primo.

W sprawie y Akciej między Starozakonnym Szymonem Moszko-
wicem Obywatelem Krasnickim Aktorem z jednej a Pawłem
[nieczytelne] w tymże długu pewnym Datur dilatio Verae Infirmitatis
ad futuras Judicia post Trium Regum 1702.

W sprawie y Akciej między Uciwym Marcinem Rymarczykiem
Przedmieszczaninem Krasnickim Aktorem a Uciwymi
Maciejem Nadzieią synem y Matyiaszem Jadnieyszym
aby pozwani ponieważ nie dołożyli oddali konew owsa
złotych kilka y wóz do kopania dany względem zaś innych
punktów w protestacji podanych aby coacią z obojej
strony wysadzili przed jedynem Sądów naypierwszą
A że za tyle odeszli nieposłusznego aby w obronie
Sądowej kontynuowali winy trzy grzywny per mediam
Sądowi y stronie oddał deprecando Maestatem Ponieważ
także Matka tegoż aby za zniewagę Aktora y mego
błogosławieństwo sądu dni trzy kontynuowała y grzywien trzy
oddała Sądowi, Sąd zaś w więzieniu zostać powinien
póki się nie zachowa iak ma stanąć do Upodobania pretensjej
w protestacji wyrażonych oprócz długu Stanek & Termin
zachowując prima Juris po Święcie Świętych Trzech
Królów Roku przyszłego 1702.

W sprawie y Akciej między Michałem Piotrowczykiem
Aktorem a Pawłową Matką y Bratem jej a Akto-
rom za sprawę wzięty Który sobie przyznały strony aby złotych
groszy dwadzieścia y dwa szeląg teraz przed sądem przynieśli
Oddał brat posłanej bez żelazną hakę groszy dwadzieścia""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 83,
        "numer_pozycji": "83",
        "strona_pagina": "fol. 39v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Kontumacje, limitacja i protestacja",
        "osoby_podmioty": "Matyjasz Stachnik [Stadnik?], Stanisław Lubelski, Kazimierz Maziarczyk, Jurek (Żyd), Jan Kaimian [?], Józef Wilk, Marcin Rymarczyk, Stanisław Luterek (mieszczanin), Jan Ołtarzyk [?]",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie sprawy Piotrowczyka; sprawa Matyjasza Stachnika ze Stanisławem Lubelskim o zniewagę; seria kontumacji (Kazimierz Maziarczyk vs Żyd Jurek, Jan Kaimian, Józef Wilk); protestacja Marcina Rymarczyka przeciw Wawrzyńcowi; limitacja sądów do Trzech Króli 1702 r. oraz protestacja Stanisława Luterka przeciw Janowi Ołtarzykowi o pobicie w domu Żyda.",
        "transkrypcja": """--- Skan #83 (fol. 39v) ---
położoną [nieczytelne] nie chciał zapłacić byle za bramą
trzymał o niedostatecznego długu skończonego Aby sądownie
Aktor okazał o Termin zachowując na pierwsze po
Trzech Królów 1702.

W sprawie między Uciwym Matiaszem Stadnikiem z ko-
legami Aktorem a Stanisławem Lubelskim o zniewagę
pozwanym datur dilatio Inquisitionis & Termin zachowują prima
post Trium Regum.

Super H. Casimirum Maziarczyk ex Parte Judaei Israela Contu-
max ad Instantiam Infidelis Marianka ibidem Contumax.
Ex Instantia H. Joannis Kamiana Obiektora 3tio Contu-
max decernit executio super bonis et persona.
Super H. Josepho Wilk rai debita ad Octo et oro pro
quingentis 2do contumax lucrum Marec Unius.

Videatur hoc loco Protestatio facta H. Martini Rymarczyk
Contra Wawrzyńca Daco et Wardęga Consortem ratione fa-
miliarum.

Limitatio Intercessit authoram
ad primam Juris post Festum Sancto-
rum Trium Regum proxima Anno Do-
mini Millesimo Septingentesimo Secundo.

Sub eodem Actu
Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
Krasnickich w osobie swoiej przyszedłszy Uciwy Stani-
sław Luterek Mieszczanin Krasnicki solennie protestował
się przeciwko Uciwemu Janowi Ołtarzykowi Tyca macze""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 84,
        "numer_pozycji": "84",
        "strona_pagina": "fol. 40r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Obdukcja i relacja woźnego z Wilkołaza",
        "osoby_podmioty": "Stanisław Luterek, Jan Ołtarzyk, Franciszek Tatarski (woźny przysięgły), Moszko Lewkowic (karczmarz ze wsi Wilkołaza), Aleksander Chapon (arendarz z Wilkołaza), Jan (poddany/chłop z Wilkołaza)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie obdukcji ran Stanisława Luterka. Następnie sesja z poniedziałku przed św. Tomaszem Apostołem 1701 r. (19 XII 1701): relacja woźnego Franciszka Tatarskiego na instancję Moszka Lewkowica, karczmarza ze wsi Wilkołaza, przeciw arendarzowi tejże wsi Aleksandrowi Chaponowi o gwałtowne odebranie wołów i krowy oraz wygnanie z arendy.",
        "transkrypcja": """--- Skan #84 (fol. 40r) ---
mu końcowi mniemania Ołtarzykom bijąc się na dzień
ostatni w domu Izraela Żyda Uczynionych protestował się
że mu protestant pokazał na prawej nodze raz od kij-
ka sinym odwapiony nad piszczelkiem Na teyże nodze
blizny nie wielkie od łomu Item na prawej ręce
łokcie w środek stłuczony krwią zaszły Item za uchem
na głowie tegoż poniżej pieczątką bili Na tenże ręce
ma głowę siną zdrapaną które razy bez dania okazji
we środę niedawno przeszłą zadane są Offerens se
Confessas Violencias Vindicare Velle.

Actum Coram Officio Advocatiali et Scabinali Crasni-
censi Feria Secunda ante Festum Sancti Thomae
Apostoli proxima Die Vero Decima Nona Decembris An-
no Domini Millesimo Septingentesimo Primo.

Videatur hoc loco relatio facta Providi Francisci Ta-
tarski Ministralis Regni Generalis incolae Crasnicensis ex
parte Infidelis Moskonis Lewkowicz Tabernatoris Villae
Wilkołaz Actoris Contra Infidelem Alexandrum Cha-
ponem Arendatorem eiusdem Villae per Indiciis Comissio-
nalibus Annis Jamokienis ad sententiam litis ad copiam
porrectis ratione Violentiae factae Subinde Recognovit
że dnia dzisiejszego oddał dozak Pozwanego w własnej
w Arendzie gdzie rezyduie Recognovit że w południu będą-
cy wyniosłszy żonę Aktora Karczmarkę od tego czasu wygna-
niem siebie chom nie brał także Recognovit żeby na wieczór
chciał kazać powary wziąć y do Komorowego chłopa Woy-
ciecha kramy odnieść Który chłop nie chciał wziąć Akta
de quo praesens relatio.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 85,
        "numer_pozycji": "85",
        "strona_pagina": "fol. 40v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Protestacja wdowy Boguckiej",
        "osoby_podmioty": "Maryna Bogucka (wdowa po Jakubie Boguckim, przedmieszczaninie), Kazimierz Bogucki (syn), Piotr Bogucki (syn), Gabriel Szpot [?] (krawiec kraśnicki)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Sesja z czwartku przed Bożym Narodzeniem 1701 r. (22 XII 1701): protestacja i obdukcja ran wdowy Maryny Boguckiej (po Jakubie Boguckim) oraz jej synów Kazimierza i Piotra przeciw krawcowi kraśnickiemu Gabrielowi Szpotowi [?] o napaść i pobicie z okazji rozliczania czeladnika.",
        "transkrypcja": """--- Skan #85 (fol. 40v) ---
Actum Coram Officio Advocatiali et Scabinali Crasni-
censi Feria Quinta Ante Festum Nativitatis Jesu Chri-
sti Domini proxima Anno Domini Millesimo Se-
ptingentesimo Primo.

Do Urzędu y Akt niniejszych Woytowskich y Ławniczych przy-
szedłszy Wdowa Maryna Bogucka Uciwego Jakuba
Boguckiego Przedmieszczanina Krasnickiego małżonka z
synami Kazimierzem y Piotrem Boguckiemi
bratem rodzonym solennie z wielkim bólem pro-
testowała się przeciwko Niewiernym Gabrielowi
Szpotowi[?] Abatia Żyda Krasnickiego krawca Oto
Iż On nie respektuiąc na wiary w prawie opisane po-
ważył się Protestantkę na drodze przed kościołem
wielkiej maści bez dania okazji z łokciem brzeżnym za
tarzę z rąk jego przed kościołem gdy protestantka brata
wybierała y o drążeniu go z łokciem załubrał
y publicznie w przedrządku przez całą wiarę dał
In factum protestantis verificavit pokazała na prawej
policzku raz krwawy zbity na palec łokcia w szerz wzdłuż
Item Raz na drugiej stronie pod nosem takowyż Item
krwi z tegoż bicia mocno ciekących Które rany
żadną miarą na zdrowiu budzić nie mogące z nie-
bicia obiecując prawnie takichże Violen-
tiarum do sądu dochodzić.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 86,
        "numer_pozycji": "86",
        "strona_pagina": "fol. 41r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Obdukcja ran po szabli",
        "osoby_podmioty": "Marcin Stachnik (przedmieszczanin kraśnicki), Tomasz Stachnik, Michał Stachnik, Matyjasz Stachnik",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Sesja z czwartku po św. Janie Ewangeliście 1701 r. (29 XII 1701): protestacja i szczegółowa obdukcja ran zadanych szablą przez Tomasza Stachnika przedmieszczaninowi Marcinowi Stachnikowi oraz jego bratu Matyjaszowi Stachnikowi.",
        "transkrypcja": """--- Skan #86 (fol. 41r) ---
Actum Coram Officio Advocatiali et Scabinali Crasnicensi
Feria Quinta post Festum Sancti Joannis Evangelistae
proxima A. D. 1701.

Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
Krasnickich przyszedłszy Uciwy Marcin Stachnik Przedmieszczanin
Krasnicki solennie z wielkim żalem protestował
się przeciwko Uciwemu Tomaszowi Stachnikowi o to
Iż On dnia wczorajszego Akt tej protestacji uprzedza-
jący poważył się zastać z szablą wszystkie okazie
przeciwne peragendo In Cuius Protestationis Verificat-
ionem pokazał raz Marcin Stachnik przez michata
Tomasza Stachnika zadane Naprzód na lewej
ręce począwszy od łokcia raz szablą cięty o piędzi
wzdłuż w szerz o trzy słomki spuchły krwią za-
bity Item od boku począwszy ku pierśi ręki
wszystkiej spuchłą siną in medietate ramię
aż ad instar plaga Item na tejże ręce pięć
lewą pokazał siną krwią zaszłą Item na piersiach z tego
względu michał stachnik bez dania okaziej bity Offerens se
iure Vindicare Velle.

Subinde
A Matthia Stachnik obducit Vulnera infrascripta Naprzód
na lewej strony głowy raz cięty do kości wzdłuż do
członka w szerz o pół łokcia płuco krwią zaszłe
Item po ramieniu zdarte we wszystkich stronach Offerens
se pro iure Vindicare Item na lewej ręce począwszy
od pięści aż do ramienia samego stłuczone i debile
nadwyrężone krew z tego ciekąca.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 87,
        "numer_pozycji": "87",
        "strona_pagina": "fol. 41v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Areszt arendarza wilkołaskiego",
        "osoby_podmioty": "Matyjasz Stachnik, Matyjasz Petka (woźny przysięgły), Matyjasz Stosiek [?], Chaim Chajmowic (syn Marka arendarza w Wilkołazie), Kucharski (pan z Ostrowa), Giebułtowski (administrator w Ostrowie), Zamoyski (pan)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie obdukcji ran Matyjasza Stachnika oraz relacja woźnego Matyjasza Petki. Następnie sesja z piątku po św. Młodziankach 1701 r. (30 XII 1701): uroczysta protestacja Chaima Chajmowica, syna Marka arendarza w Wilkołazie, przeciw panu Kucharskiemu z Ostrowa i jego administratorowi Giebułtowskiemu o najazd i porwanie dawnego arendarza Dawida.",
        "transkrypcja": """--- Skan #87 (fol. 41v) ---
Item na tejże ręce prawej od wielkiego palca idąc na dół
ręki spuchłej raz stłuczony Offerens Violencias iure Vin-
dicare Velle.

Sub eodem Actu
Videatur relatio facta Providi Mathiae Petka
będącego super filum Honesti Mathiae Stoska [?] prout sui
exhibuit de quo praesens relatio.

Actum Coram Officio Advocatiali et Scabinali Cra-
snicensi Feria Sexta post Festum Sanctorum In-
nocentum proxima Anno Domini Millesimo Septin-
gentesimo Primo.

Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
Krasnickich w osobie swoiej przyszedłszy Niewierny Chaim
Chaymowic Syn Niewiernego Marka Żyda Arendarza
na Wilkołazie w Woiewództwie Lubelskim dobra Jaśnie
Wielmożnego Jaśka Podskarbiego Wielkiego Koronnego solennie
z wielkim żalem Cavendo indemnitati ac integritati sa-
lutis suae gdyż ieżeli by nie nastąpiła prędkiego ratunku
w Grodzie Lubelskim protestacją czynić y razy leśne
swoie obwieścić protestował się przeciwko Panu
Kucharskiemu dóbr części Ostrowa w Wo-
iewództwie y powiecie Lubelskim leżących y Panu iego
Administratorowi Panu Giebułtowskiemu w te słowa
który z rozkazania tegoż Pana swego dnia wczorajszego
wieczorem po zachodzie słońca z przydanemi ludźmi
zbrojnymi przysłali że 2gi poddany nieiakoto przy tym
do sprawy pokazał się Iż Oni powazyli się najechać
dwór w tejże wsi wzwyż pomienionej Wilkołazie rzeczonej""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 88,
        "numer_pozycji": "88",
        "strona_pagina": "fol. 42r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Najazd na dwór i zamknięcie akt 1701 r.",
        "osoby_podmioty": "Chaim Chajmowic, Dawid Chajmowic (arendarz w Sulowie), Zamoyski (pan), Pomiatowski (administrator), Chaim Aleksandrowic, Franciszek Tatarski (woźny przysięgły), Albert Boskiewicz (świadek), Albert Kanapka (świadek), Stanisław Maziewski (wójt kraśnicki)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie protestacji Chaima Chajmowica o najazd na dwór w Wilkołazie, porwanie brata Dawida Chajmowica z browaru w Sulowie i obdukcja ran Chaima Aleksandrowica w obecności woźnego Franciszka Tatarskiego oraz świadków Alberta Boskiewicza i Alberta Kanapki. Na dole strony uroczysta klauzula zamknięcia akt roku 1701 do elekcji magistratu, podpisana przez wójta Stanisława Maziewskiego.",
        "transkrypcja": """--- Skan #88 (fol. 42r) ---
pod pretekstem długu od Niewiernego Dawida Chaymowica
brata mego rodzonego Arendarza Browaru we wsi Sudo-
wek nazwanej w tymże powiecie y województwie Lubelskim
leżącej dóbr Jaśnie Pana Zamoyskiego przywłaszczonego długu
pretendowanego przez zgodę przyjacielską przybyłych
Jego Mci Pana Zamoyskiego y innych braterstwa przybyli
obie strony do dworu w Aktu wyrażonego nieczekając
pieniędzy z długu swego dla którego Dokumenty nalazł
dwór pomienionego Dawida gdzie przyszli do dworu w Wilkołazu
nie zastali Jego Mci P. Pomiatowskiego Administratora
który na ten czas odjechał był po pańskiej potrzebie do Rzeczy
z lasów gdzie zastali samey Jego Mci Panią Administratorową
prosząc aby był wydany pomieniony Dawid Chaymowic
Kramczykowie przy Pani swej wymówki to czynić brać nie
pozwalali aby się gwałt dworowi w dobrach pańskich
nie dział Oni mało nie respektując gwałtem weszli
w dwór gdzie arendarza gwałtem na szablę wzięli
wzięli do więzienia y do komornego dali było gdzie
nie mogli bez przyczyny inne Violencie na ten czas
obszernie doniesione popełnili.
In Cuius Protestationis Verificationem pokazał pomienio-
ny Chaim Alexandrowic cięty do kości szablą na
rogu głowy wzdłuż na palec średni w szerz na pół
palca także w obecności Providi Francisci
Tatarski Ministralis Generalis atque Famatorum Alberti Bos-
kiewicz Alberti Kanapka Scabinorum Juratorum de
horum Actu contenta Obecnie.

Acta skończone do Elekcyjej Panów Expediowanej odda-
ne przez P. Maziewskiego Woyta na ten czas będącego y pod-
pisane ręką własną zostawuię.
Stanisław Maziewski Woyt mpp.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 89,
        "numer_pozycji": "89",
        "strona_pagina": "fol. 43r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Elekcja Magistratu i Kalkulacja Skarbowa",
        "osoby_podmioty": "Jan Chocimowski (gospodarz domu), Anna z Gmina Zamoyska Potocka (opiekunka Ordynacji Zamoyskiej), Wawrzyniec Grzymałowski, Jan Potokowic (rezydent), Strzelecki (podstarości klucza kraśnickiego)",
        "kwoty_podatki": "16 fl (Grzymałowski), 14 fl 5 gr (Potokowic), 160 fl (składka), 190 fl 5 gr (suma pierwsza), 705 fl, 64 fl, 87 fl 12 gr, 28 fl, 769 fl 8 gr, 51 fl, 6 fl (synagoga na paszkartów), 94 fl 22 gr, 921 fl (percepta J. Potokowica)",
        "opis_sprawy": "Początek księgi roku 1702: zjazd w domu Jana Chocimowskiego nazajutrz po Święcie Trzech Króli (7 I 1702 r.) z woli Anny z Gmina Zamoyskiej Potockiej przed elekcją magistratu. Szczegółowe rozliczenie remanentów i percept poborcy Jana Potokowica (suma percepty 921 fl).",
        "transkrypcja": """--- Skan #89 (fol. 43r) ---
Działosię w Krasniku w domu P. Jana
Chocimowskiego woyta na ten czas nazaiutrz po
Święcie Trzech Królów Roku Pańskiego
Tysiącznego Siedmsetnego Wtórego.

Z wyraźnej woli Jaśnie Wielmożnej Imci Paniey Anny z Gmina Zamoyskiey
Potockiey Starościney & Ogromnej Pierwszej y Naturalnej Opiekunki Ordy-
nacyey Zamoyskiey Paniey y Dobrodziejki mojej, zjechawszy tu pro ter-
mino electionis magistratu, iuxta eloquentiam praw Ordynackich, ante
omnia ad faciendam calculationem z powinności po przeszłej Elekcyey
Sum pieniędzy z majątków pro oculis y Remanentu Regestra w przeszłej
kalkulacyey wyrażonej przystąpiłem in praesentia totius Communi-
tatis ad hunc Actum congregatae.
Tenor calculationis sequitur talis.
U Sławetnego Grzymałowskiego restabat . . . . . fl 16 —
U P. Jana Potokowica . . . . . . . . . . . . . . fl 14 — 5
Uchwalona była składka przed elekcją przeszłoroczną
na fl 160 która że tylko rozpoczęta była rezerwowana
tędy została dotąd więc w Perceptę includitur . . . fl 160 —
Summa Facit ex Restis fl 190 — 5 —
Po Elekcyey zaś przeszłorocznej Pan Jan Potokowic
Rezydens wybierał ex Laudo na fl 100 y pokazał Per-
cepty fl 705. Więc ex retentis regestr exakcyey wywiodł
P. Strzelecki Podstarości na ten czas Klucza Krasnickie-
go pewnych do wybrania fl 64. 8. a niepewnych fl 87
gr 12. iednak iniunctum podczas Kommissyey d. 28
Maij Anno 1701mo expedjowanej aby te pewne
wybrał Sławetny Potokowic Więc iuncta summa
pro percepta posita . . . . . . . . . . . . . . . Facit fl 769. 8.
Osobno potym dobrali y dali P. Grzymałowskiemu . . . fl 51. —
Od Synagogi na Paszkartów wzięte . . . . . . . . . . fl 6. —
Zaciągnionych z długami apparet . . . . . . . . . . fl 94. 22
Summa przez Pana Potokowica percepta fl 921 —""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 90,
        "numer_pozycji": "90",
        "strona_pagina": "fol. 43v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Kalkulacja Skarbowa Miasta Kraśnika",
        "osoby_podmioty": "Wawrzyniec Grzymałowski, Wawrzyniec Pielaszkowic (rezydent), Anna Zamoyska Potocka, Jan Potokowic, Wójt Zarzecki, Wójt Podleski, Wójt Piaskowy, Szafarze miejscy (Jan i koledzy), Synagoga Kraśnicka, Komisja Lutowskiego",
        "kwoty_podatki": "533 fl 15 gr (percepta Grzymałowskiego), 1004 fl 12 gr (percepta Pielaszkowica), 205 fl 18 gr (talary od Zamoyskiej), 360 fl 15 gr (Zarzecze), 363 fl 15 gr (Podlesie), 360 fl 6 gr (Piaski), 136 fl 15 gr 6 szel (szafarze), 300 fl (synagoga), 1536 fl 21 gr 6 szel (suma taryf), 371 fl 25 gr (suma z synagogi)",
        "opis_sprawy": "Dalszy ciąg kalkulacji skarbowej miasta Kraśnika przed elekcją 1702 r.: rachunki percepty Wawrzyńca Grzymałowskiego (533 fl 15 gr), Wawrzyńca Pielaszkowica (1004 fl 12 gr), pożyczka w talarach od Zamoyskiej (205 fl 18 gr) oraz zestawienie taryf składki na 1500 fl rozpisanej na wójtów Zarzeckiego, Podleskiego, Piaskowego, szafarzy i synagogę (1536 fl 21 gr 6 szel).",
        "transkrypcja": """--- Skan #90 (fol. 43v) ---
Tenże Grzymałowski zaciągnął długiem u Żyda . . . . . fl 16 —
U Berka Żyda . . . . . . . . . . . . . . . . . . . fl 129 —
Przez ręce Pana Podleskiego pożyczany y temuz
oddany u patet w Rachunku Pana Pielaszkowica . . . . fl 300 —
Insuper Zaciągnionych u różnych apparent . . . . . . fl 88. 15
Summa przez Pana Grzymałowskiego percepta. fl 533. 15 —

Sławetny Pielaszkowic miał sobie oddane Laudum na fl 1500.
Na tę summę nie wybrali Dziesiętnicy iako się pokazało
z weryfikacyey tylko . . . . . . . . . . . . . . . fl 907. 12
Residuum in retentis et defectibus ut infra patebit exhi-
bitio to iest złotych fl 212. 16. u Synagogi fl 300. ratione
piątego grosza od nich do tego laudum należącego.
Tenże Pielaszkowic potrącił ad rationem długu fl 129 —
który dorobił ut supra in calculo Grzymałowskiego patet
należących z piątego grosza . . . . . . . . . . . . fl 91 —
Tenże na Paszkartów wziął u tychże . . . . . . . . fl 6 —
Summa przez Pana Pielaszkowica percepta fl 1004. 12 —

Od Wielebnej Imci Panny Zamoyskiej zaciągnione na po-
trzebę miasta y długów zapłacenie Talarów bitych No 49 —
rachując po fl 4 gr 24 uczyni Summa . . . . . . . . . fl 205. 18.
Dziesiętnikow y Szafarzów exakcya z składki na fl 1500
dobra wyrażonej za rezydencyey Pana Potokowica
na ów czas uchwalonej:
Woytowi Zarzyckiemu wydana Taryffa na Summę . . . . fl 360. 15
Woytowi Podleskiemu . . . . . . . . na Summę . . . fl 363. 15
Woytowi Piaskowemu . . . . . . . . na Summę . . . fl 360. 6
Szafarzom to iest Janowi z Collegg . . na Summę . . . fl 136. 15. 6
Od Synagogi z Piątego grosza miało się dostać . . . fl 300 —
Summa efficit wydanych z Taryff fl 1536. 21. 6.
Synagoga do Summy przez Potokowica wybranej to iest
fl 828 powinni byli wnieść Piątym groszem jako wzwyż
wyprowadzili od Kommissyey Imci Lutowskiego . . . . . fl 164
Z osobna Składki na fl 1500 uchwalonej należałoby od
nich fl 300 lecz iż Mieszczanie nie wydali tylko fl 1039. 5. więc
iuxta proportionem należy od nich in vim piątego grosza fl 207. 25 —
Summa Facit fl 371. 25 —""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 91,
        "numer_pozycji": "91",
        "strona_pagina": "fol. 44r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Bilans Skarbowy Miasta (Percepta i Expensa)",
        "osoby_podmioty": "Jan Potokowic, Wawrzyniec Grzymałowski, Wawrzyniec Pielaszkowic, Piasecki (rezydent), Synagoga Kraśnicka",
        "kwoty_podatki": "4922 fl 6 gr 6 szel (Summa Perceptarum), 190 fl 5 gr (Suma Pierwsza), 921 fl (Suma Powtórna), 533 fl 15 gr (Suma Trzecia), 967 fl 3 gr (expensa Pielaszkowica)",
        "opis_sprawy": "Podsumowanie całkowitej Percepty Miasta Kraśnika (Summa Perceptarum 4922 fl 6 gr 6 szel) oraz rozliczenie Expensy podzielonej na Sumę Pierwszą (190 fl 5 gr), Sumę Powtórną Potokowica (921 fl), Sumę Trzecią Grzymałowskiego (533 fl 15 gr) i początek rozliczenia Pielaszkowica.",
        "transkrypcja": """--- Skan #91 (fol. 44r) ---
Summariusz Percepty pro Każdego
Specifice wyrażoney.
Ad Exactionem Woytów y Szafarzów według Taryff . . . . fl 1536. 21. 6
Ex Remanentu y Reszty ex Ao 1701 . . . . . . . . . . fl 190. 5 —
Z Exakcyey Sławetnego Potokowica . . . . . . . . . . fl 921 — —
Z Exakcyey Sławetnego Grzymałowskiego . . . . . . . . fl 533. 15 —
Z Exakcyey Sławetnego Pielaszkowica . . . . . . . . . fl 1004. 12 —
Wzięte u Wielebnej Imci Panny Zamoyskiej przez
Sławetnego Grzymałowskiego y Piaseckiego Tal. 42 . . . . fl 205. 18 —
Od Synagogi Piątego grosza . . . . . . . . . . . . . fl 371. 25 —
Summa Perceptarum fl 4922. 6. 6.

Expensa z tey Summy Takowa.
Naprzód z remanentu y reszty Supra wyrażoney Summy fl 190.
pokazali expensy . . . . . . . . . . . . . . . . . fl 71
Z osobna niedobranej ad complementum fl 160 in defectibus fl 88. 14
Item remanent in integro u P. Grzymałowskiego . . . . fl 16 —
Z osobna u P. Potokowica zostało . . . . . . . . . . fl 14. 5 —
Summy pierwszey elucidatio facit fl 190. 5.

Z Exakcyey P. Potokowica składki na fl 1000 uchwa-
lonej y z innych percept supra wyrażonych In Sum-
ma fl 921 . . . . . . . . . . . . . . . . . . . . fl 870 — —
Z osobna Grzymałowskiemu na expens Żołnierskie danego fl 51 — —
Summa Powtorna fl 921 — —

Sławetny Grzymałowski z powziętey Summy fl 533. 15
modo quo Supra wyrażoney pokazał regestrem jednym expensy fl 233. 15
Na drugim regestrze pokazał expensy ze fl 300 — . . . fl 288. 15
Restat przy nim . . . . . . . . . . . . . . . . . . fl 11. 15.
Summa Trzecia fl 533. 15 —

Sławetny Pielaszkowic z exakcyey składki na fl 1500 y in-
nych Supra wyrażonych prowentów in Summą fl 1004. 12
pokazał expensy jednym regestrem fl 119. drugim
fl 848. 3. Facit . . . . . . . . . . . . . . . . . fl 967. 3 —""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 92,
        "numer_pozycji": "92",
        "strona_pagina": "fol. 44v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Bilans Skarbowy Miasta (Sumy Czwarta–Siódma)",
        "osoby_podmioty": "Wawrzyniec Pielaszkowic, Wawrzyniec Grzymałowski, Jan Potokowic, Piasecki, Wójt Zarzecki, Wójt Podleski, Wójt Piaskowy, Szafarze, Synagoga Kraśnicka, Puszkarze",
        "kwoty_podatki": "91 fl, 26 fl 9 gr, 1004 fl 12 gr (Suma Czwarta), 256 fl 14 gr, 29 fl 4 gr, 285 fl 18 gr (Suma Piąta), 360 fl 20 gr (Zarzecki), 363 fl 15 gr (Podleski), 360 fl 6 gr (Piaskowy), 136 fl 15 gr 6 szel (Szafarze), 300 fl (Synagoga), 1536 fl 21 gr 6 szel (Suma Szósta), 371 fl (Suma Siódma)",
        "opis_sprawy": "Dokończenie rozliczenia Expensy Miasta Kraśnika: Suma Czwarta (1004 fl 12 gr), Suma Piąta z talarów od Zamoyskiej (285 fl 18 gr), Suma Szósta — rozliczenie wójtów Zarzeckiego, Podleskiego, Piaskowego, szafarzy i synagogi (1536 fl 21 gr 6 szel) oraz Suma Siódma — wydatki synagogi w tym 12 fl puszkarzom za dwa kwartały (371 fl).",
        "transkrypcja": """--- Skan #92 (fol. 44v) ---
Z osobna do niego na zapłacenie długu iemu należącego fl 91 —
Zostaje przy nim z tey exakcyey oprócz Złotych którey
niżej a iemu per partes dedit . . . . . . . . . . . fl 26. 9
Summa Czwarta fl 1004. 12

Item Sławetny Grzymałowski, Potokowic y Piasecki z wzię-
tego u Wielmożnej J. Panny Zamoyskiej popłacili długi nadto
z Rachunku P. Potokowica fl 94. 22. z Rachunku P. Grzy-
małowskiego długu zaciągnionego fl 88. 15. Piasecki poka-
zał regestrem wydanych fl 73. 7. Summa Facit . . . . fl 256. 14
Restant u Potokowica y Grzymałowskiego . . . . . . . fl 29. 4
Summa Piąta fl 285. 18.

Woyt Zarzycki wydał Pielaszkowicowi fl 311. 20. Expensy fl 5.
remanentu u niegoż fl 5. 15. na retentach pewnych fl 8. 25.
na defektach dla ubóstwa iusz niepewnych fl 22. 20 Facit fl 360. 20
Woyt Podleski wydał Pielaszkowicowi fl 298. Expensy fl 2. 5.
remanet u niego fl 7. 26. in retentis u ludzi fl 34. 17. In defe-
ctibus dla ubóstwa 21. 15 . . . . . . . . . . . . . fl 363. 15 —
Woyt Piaskowy oddał Pielaszkowicowi fl 307. remanentu u
niego fl 1. 18. in retentis u ludzi fl 25. 13. in defectibus
dla Ubostwa fl 34 . . . . . . . . . . . . . . . . fl 368. 6 —
Szafarze wydali Pielaszkowicowi fl 72. na expensa fl 5. 20.
In retentis u ludzi w Mieście pewnych do wybrania fl 59 — fl 136. 15. 6
Synagoga wydała temuz Pielaszkowicowi fl 97. Restat
dać paratis ad complementum fl 300 — fl 203. Facit fl 300 —
Summa Szósta Facit fl 1536. 21. 6

Synagoga z pochodzącej od nich Summy ut Supra wyrażonej
fl 371. 25. wydali iako patet w Rachunku Pielaszkowica . . fl 97.
Puszkarzom za dwa kwartały exceptis wyżej wyrażonych
fl 12 dali fl 12 . . . . . . . . . . . . . . . . . fl 12.
Reszta u nich fl 262. które twierdzą że na expensa rozpuścili
Summa Siódma fl 371.
To iednak additur ponieważ żydzi żadnego nie
produkowali expens swoich regestru to w przy-
szłym czasie z reszty u nich pozostałej powinni dać
rationem.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 93,
        "numer_pozycji": "93",
        "strona_pagina": "fol. 45r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Bilans Skarbowy Miasta (Reszty i Długi Synagogi)",
        "osoby_podmioty": "Wawrzyniec Grzymałowski, Jan Potokowic, Wawrzyniec Pielaszkowic, Stanisław Rzadkowski (wójt zarzecki), Marcin Cwiek (wójt podleski), Matyjasz Bernat (wójt piaskowy), Bernat (wójt z Piasku), Jarzyk, Wigdor (Żyd), Jeżyk (Żyd), Sbrich [?] (Żyd)",
        "kwoty_podatki": "100 fl 12 gr (reszty u wójtów i rezydentów), 119 fl 25 gr (retenta pewne), 220 fl 7 gr (suma obu pozycji), 71 fl 28 gr (długi miasta: 38 fl Wigdorowi, 16 fl Jeżykowi, 17 fl 28 gr Sbrichowi)",
        "opis_sprawy": "Zestawienie reszt pozostałych u urzędników (Grzymałowskiego, Potokowica, Pielaszkowica, wójta zarzeckiego Stanisława Rzadkowskiego, podleskiego Marcina Cwieka, piaskowego Matyjasza Bernata — 100 fl 12 gr) oraz retent pewnych do wybrania (119 fl 25 gr), łącznie 220 fl 7 gr. Wykaz długów miasta wobec Żydów Wigdora (38 fl), Jeżyka (16 fl) i Sbricha (17 fl 28 gr) przekazanych do spłaty synagodze.",
        "transkrypcja": """--- Skan #93 (fol. 45r) ---
Reszty u rożnych pozostałe
Dawny remanent u Grzymałowskiego . . . . . . . . . fl 16 —
U P. Potokowica . . . . . . . . . . . . . . . . . fl 14. 5 —
Z teraźniejszej percepy przy P. Pielaszkowicu . . . fl 26. 9 —
Z Summy od Imci Zamoyskiej wziętej zostało
przy Sławetnych Grzymałowskim y Potokowicu . . . . fl 29. 4 —
Przy Stanisławie Rzadkowskim Woycie Zarzyckim . . . fl 5. 15 —
Przy Marcinie Cwieku Woycie Podleskim . . . . . . . fl 7. 26 —
Przy Matyaszu Bernatku Woycie Piaskowym . . . . . . fl 1. 18
Summa Facit fl 100. 12

Retenta do wybrania pewne
Z exakcyey Woyta Zarzyckiego wzwyż mianowanego . . fl 25. 25 —
Z exakcyey Cwieka Woyta Podleskiego . . . . . . . . fl 34. 17 —
Z exakcyey Bernatka Woyta z Piasku . . . . . . . . fl 25. 13 —
Z exakcyey Jarzyka z Collegg Szafarzów . . . . . . fl 34 — —
Summa Facit fl 119. 25 —
Z osobna reszty ut supra fl 100. 12. In unum fl 220. 7 —
Te Summy obiedwie najdalej Niedziel trzech wybrane być powinny
Zalecam Serio Sławetnemu Magistratowi, na zapłacenie dłu-
gów, y potrzeb następujących Całego Miasta.

Długi zaś takowe Znajduią się
Wigdorowi Żydowi reszty Na dwadzieścia dwie
Oświęcim złotych należy . . . . . . . . . . . . . fl 38 —
Jeżykowi Żydowi . . . . . . . . . . . . . . . . . fl 16 —
Sbrichowi . . . . . . . . . . . . . . . . . . . . fl 17. 28
Summa Facit fl 71. 28. Ktora to Summa
z reszty u Synagogi Znajduiącej się Assignatur.
Na ten czas długi iusz więcej nikt sobie nie pretendo-
wał, lubo pytani publice byli, więc in futurum jeśliby się
kto odzywał, żadnego waloru mieć nie powinien, ponie-
waż w regestrach podanych długi Znajduiące się po-
płacone.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 94,
        "numer_pozycji": "94",
        "strona_pagina": "fol. 45v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Dekret Komisarza Ordynacji Zamoyskiej",
        "osoby_podmioty": "Komisarz Ordynacji Zamoyskiej, Katolicy mieszczanie i przedmieszczanie, Żydzi kraśniccy, Lutowski (komisarz), Instytor Sądu Trybunalskiego Zamoyskiego",
        "kwoty_podatki": "507 fl 29 gr (katolicy), 93 fl 6 gr (Żydzi)",
        "opis_sprawy": "Postanowienie komisarza ordynackiego po kalkulacji z 1700 r. (komisja z 13 V 1701 r.): nakaz przedłożenia oryginalnych regestrów przez katolików (507 fl 29 gr) i Żydów (93 fl 6 gr) w ciągu 3 dni oraz przestrzegania ordynacji z 1698 r. pod rygorem pozwu przed Trybunał Zamoyski.",
        "transkrypcja": """--- Skan #94 (fol. 45v) ---
Chociaż przy tym informuję z Calculacyey in Anno Septin-
gentesimo ipso expedyowanej, iż tak Katolicy Mieszczanie
y Przedmieszczanie Summy Złotych Pięćset Siedmiu
groszy dziewięci, jako też y Żydzi Summy Złotych
Dziewięćdziesiąt trzech y groszy sześciu dico fl 93. 6.
nie dali rationem pod czas przeszłorocznej calculacyey Anni
Millesimi Septingentesimi primi, w której ulla mentio o tym
nie znajduje się, co musi bydz errore factum. Więc kiedy
się zabierają wzwyż pomienieni ad probationem Regestra-
mi Oryginalnemi, których ad praesens wynaleść nie mogli, su-
benduc tedy decyzją do czterech Niedziel ab Actu
praesenti, na który czas powinni będą comportare pomie-
nione regestra Sub onere exolutionis Summ wzwyż
wyrażonych. Similiter y Kommissyey decima tertia
Maij Anno praeterito expedjowanej aby in toto satisfa-
ciant sub eodem rigore przykazuie. Quantum attinet
melioracyey regiminis w tym Mieście w wielu rzeczach
widzę bydz potrzebną. A ponieważ dla krótkości cza-
su nie mogła bydz ad praesens postanowiona Więc potrze-
bną bydz uznaię Kommissyą, której w czasie wzwyż wy-
rażonym, Sive etiam captato tempore deklaruję, na ten
czas tedy, y w innych sprawach y pretensyach tak
Katolików jako też y Synagogi finalna będzie decyzja
Interea quo ad regimen miasta tego spectat referując
się do przeszłych z Anno 1698vo Dyspozycyj, reasu-
muię one y przykazuię Sławetnemu Magistratowi
aby one in integro zachowali, Salvam actionem in casu
contraventionis Instigatori Judicij Tribunalicij Zamosc.
reservando.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 95,
        "numer_pozycji": "95",
        "strona_pagina": "fol. 46r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Elekcja Magistratu Kraśnickiego na rok 1702",
        "osoby_podmioty": "Paweł Słomkowski (wójt), Adam Potokowic (podwójci), Wawrzyniec Pielaszkowic (rajca 1.), Stanisław Solecki (rajca 2.), Stanisław Szczurkowic (rajca 3.), Jan Barankowic (rajca 4.), Wojciech Grzymałowski (deputat na Trybunał), Paweł Nowacki (faktor), Jan Jarzyk (faktor), Stanisław Morelowski (komisarz ordynacki)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Uroczysta elekcja Magistratu Miasta Kraśnika na rok 1702: wójt Paweł Słomkowski, podwójci Adam Potokowic, czterej rajcowie (Wawrzyniec Pielaszkowic, Stanisław Solecki, Stanisław Szczurkowic, Jan Barankowic), deputat na Trybunał Wojciech Grzymałowski oraz faktorzy Paweł Nowacki i Jan Jarzyk. Przysięga według prawa magdeburskiego oraz zarządzenie komisarza Stanisława Antoniego Morelowskiego w sprawie porządku w archiwum miejskim.",
        "transkrypcja": """--- Skan #95 (fol. 46r) ---
Sequitur electio Magistratus
Pro Anno Millesimo Septingentesimo Secundo.

Na Urząd Woytowski:
Sławetny Paweł Słomkowski Woyt.
Sławetny Adam Potokowic Podwoyt.

Na Urząd Radziecki:
Sławetni 1. Wawrzyniec Pielaszkowic
2. Stanisław Solecki
3. Stanisław Szczurkowic
4. Jan Barankowic

Deputatus na Trybunał Sław. Woyciech Grzymałowski.
Faktorowie: Paweł Nowacki, Jan Jarzyk.

Nowo tedy obrani Sławetni Słomkowski, Potokowic Podwóyci
y Raycy wzwyż pomienieni Juramenta według Prawa
Maydeburskiego in facie Communitatis praestiterunt, in instanti.

Postanowienie Komputu według Sumienia y Słuszności sine iniu-
ria ubogich ludzi naznaczam na przyszłe Składki pro necessi-
tate totius Civitatis które powinno bydz in praesentia Pana
Administratora Klucza Krasnickiego. & Serio iakonajsil-
niej zalecam, ponieważ o przeszły Komput wielkie Po-
spólstwa były aklamacye dla przeładowania ich.

Conscriptionem Inwentarij Archivi w którym wielki nieporzą-
dek zastałem, w ten czas gdy na postanowienie Komputu zie-
dzie Imci Pan Administrator oraz comportacyą y ingrossacyą
wszystkich do tego czasu expedyowanych Kommissyi Miastu
Całemu potrzebnych Serio przykazuię, ponieważ w teraźniej-
szym czasie niektórych nie mogłem widzieć drugie zaś po ró-
żnych rękach poznajdowały się chociaż była dawniejsza
o tym dyspozycya aby in Archivo wszelkie Acta pod Inwen-
tarzem zostawały. Oryginały zaś wszelkich Kommissyj
Pisarz miejski w księgę aby indukował upominam.
Stanisław Ant. Morelowski
Podstoli [podpis]""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 96,
        "numer_pozycji": "96",
        "strona_pagina": "fol. 46v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Inwentarz Papierów i Regestrów Archiwalnych",
        "osoby_podmioty": "Wawrzyniec Pielaszkowic, Pan Wittan, Pan Jasiecki, Pan Podczaszego Winnickiego, Pan Lutowski, Pan Jan Potokowic, Pan Grzymałowski, Anna Zamoyska, Pan Leszczynowski",
        "kwoty_podatki": "1078 fl 18 gr, 102 fl 29 gr, 34 fl 10 gr, 849 fl 3 gr, 30 fl, 1067 fl 26 gr, 300 fl, 160 fl, 990 fl 10 gr, 2007 fl 29 gr, 1281 fl 15 gr",
        "opis_sprawy": "Szczegółowy spis 17 pozycji dokumentów i regestrów skarbowych z lat 1690–1702 przedłożonych podczas elekcji 1702 r. ('Inwentarz Papierów pro Actu Electionis in Anno 1702'): taryfy z 6 X 1701 r., regestry Pielaszkowica, Potokowica, Grzymałowskiego, pisma z komisji z lat 1690, 1693, 1697 i 1701 oraz regestry długów na 990 fl 10 gr i 2007 fl 29 gr.",
        "transkrypcja": """--- Skan #96 (fol. 46v) ---
Inwentarz Papierów pro Actu Electionis in Anno
1702 produkowanych y znowu nazad który komu
należał in praesentia Magistratus oddanych.
1mo Taryff cztery sub data 6. 8bris Anni 1701. Woytom Zarzyckiemu
Podleskiemu, Piaskowemu y Szafarzom pro exactione składki
wydanych, na których są connotowane percepty, expensa rema-
nenta y defecta.
2do Percepta P. Wawrzyńca Pielaszkowica Rezydenta wynosząca
Summę fl 1078. 18.
3tio Regestr expens przez Szafarzów wydanych wynoszący fl 102. 29.
4to Regestr remanentów Szafarskich wynoszący fl 34. 10.
5to Regestr expensy przez Pielaszkowica wynoszący fl 849. 3.
6to Karta Imci Wittana na fl 30.
7mo Regestr wydatków P. Pielaszkowica ręką Imci P. Jasieckiego
podpisany fl 1067. 26. wynoszący.
8vo Regestr P. Potokowica rękami ImPP. Podczaszego Winnic. y Stolni-
ka Różanskiego podpisany 18. Maij Ao 1701.
9no Regestr P. Grzymałowskiego przez tychże Imci podpisany.
10mo Regestr tegoż z Zł 300. wziętych od Imci Panny Zamoyskiey.
11mo Regestr wydatku z Talerów 40. od teyże Imci wziętych przy
którym remanent wybranych ad rationem fl 160. Składki ex
Ao 1701mo pozostałej.
12o Kommissya rękami ImPP. Wittana y Leszczynowskiego podpisana.
13o Regestr długów na fl 990. 10. 5 Febr. 1693 ręką Imci Podczaszego Winni-
ckiego podpisany.
14o Regestr długów fl 2007. 29. Anno 1690 przez tegoż Imci podpisany.
15o Kommissya Imci Pana Lutowskiego 22. Maij 1697 odprawiona.
16o Regestr percepty Szafarskiej in Ao 1701. z składki na fl 1281. 15 uchwalonej.
17o Kommissya Imci Pana Podczaszego Winnickiego in Ao 1690
expedyowana d. 17. Januarij.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 97,
        "numer_pozycji": "97",
        "strona_pagina": "fol. 47r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Elekcja Cechmistrzów i Ławników na rok 1702",
        "osoby_podmioty": "Wawrzyniec Pielaszkowic (prokonsul), Paweł Słomkowski (wójt), Stanisław Solecki (rajca), Stanisław Szczurkowic (rajca), Jan Barankowic (rajca), Adam Potokowic (podwójci), Stanisław Grymus, Wojciech Janaszkowic (stary rajca), Wojciech Beskiewicz (ławnik), Stanisław Solecki (cechmistrz kuśnierski i krawiecki?), Matyjasz Loreński (cechmistrz tkacki), Wojciech Kanapkowic (ławnik), Tomasz Zdebikowic (ławnik)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Sesja z czwartku przed św. Fabianem i Sebastianem 1702 r. (19 I 1702) w rezydencji prokonsula Wawrzyńca Pielaszkowica w obecności wójta Pawła Słomkowskiego i rajców: elekcja cechmistrzów (kuśnierzy — Stanisław Solecki, tkaczy — Matyjasz Loreński, kuśnierzy/szewców — Stanisław Solecki) oraz wybór ławników miejskich z bram (Wojciech Kanapkowic, Wojciech Beskiewicz, Tomasz Zdebikowic, Stanisław Grymus).",
        "transkrypcja": """--- Skan #97 (fol. 47r) ---
Actum In Residentia Spectabilis ac Honorati Laurentii
Pielaszkowic Proconsulis, ad quem Officium Pro-
consulatus translatio extitit, In praesentia Spectabilium
ac Honoratorum Pauli Słomkowski Advocati, Stani-
slai Solecki, Stanislai Szczurkowic, Joannis
Barankowic Consulum, Adami Potokowic
Viceadvocati, Stanislai Grymus, Antiqui Con-
sulis Alberti Janaszkowic, Alberti Beskiewicz
Scabinis et aliis circa eandem Translationem con-
gregatis Feria Quinta pridie Festi Sanctorum
Fabiani et Sebastiani Anno Millesimo Sep-
tingentesimo Secundo.

Et Inprimis Officium hoc ad Electionem
Cechmagistrorum accessit.
1. In Eodem Contubernij Sutorum Cechmagister
   Famatus Stanislaus Solecki electus.
2. Contubernij Fabrorum [brak wpisu]
3. Contubernij Textorum Honestus Matthias
   Lorenski approbatur.
4. Pellionum Cechmagister Famatus Stanislaus
   Solecki electus.
Sartorum Cechmagister [brak wpisu].
Ad Scabinatum przy Bramie St. Woyciech Ka-
napkowic, St. Woyciech Beskiewicz, approbantur
St. Thomas Zdebikowic, Stanislaus Grymus.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 98,
        "numer_pozycji": "98",
        "strona_pagina": "fol. 47v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Elekcja Wójtów Przedmiejskich i Sąd Wójtowsko-Ławniczy",
        "osoby_podmioty": "Wojciech Sokół (wójt na Górach), Stanisław Rzadkowski (wójt na Zarzeczu), Jan Smok (przedmieszczanin, aktor), Tomasz Nowacki (mieszczanin, pozwany), Stanisław Leszczyński [?], Sobestian Frasiek [?], Dorota Młynarka (z Grebiennej), Jakub Krawiec",
        "kwoty_podatki": "49 złp (dług T. Nowackiego: 22 złp w 3 dni, 27 złp na św. Macieja), 3 złp (S. Leszczyński), 4 złp (Dorota Młynarka)",
        "opis_sprawy": "Dokończenie elekcji wójtów przedmiejskich (Góry: Wojciech Sokół, Zarzecze: Stanisław Rzadkowski, Piaski i Podlesie bez wpisów imion). Następnie pierwsza sesja sądowa 1702 r. w dzień św. Fabiana i Sebastiana (20 I 1702): dekret w sprawie Jana Smoka przeciw Tomaszowi Nowackiemu o 49 złp, dekret dla Sobestiana Fraśka (3 złp) oraz nakaz dla Doroty Młynarki z Grebiennej zwrotu 4 złp.",
        "transkrypcja": """--- Skan #98 (fol. 47v) ---
Woytów Gromadzkich:
1. Z Gór Uciwy Woyciech Sokół.
2. Z Przedmieścia Piaski [brak wpisu].
3. Z Zarzecza Stanisław Rzadkowski approbatur.
4. Z Podlesia [brak wpisu].

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Sexta ipso Die Festi Sancto-
rum Fabiani et Sebastiani Anno Domini Millesi-
mo Septingentesimo Secundo.

W sprawie y Akciej między Uciwym Janem Smokiem
Przedmieszczaninem Krasnickim Aktorem, a Uciwym
Tomaszem Nowackim Mieszczaninem Krasnickim wzglę-
dem nieoddania długu złotych czterdziestu y dziewięci
polskich za spisanie aby dłużnikowi luboby pozwany
zasługi winy za niesłuszne uczynienie dekretem
ferowanym jednak habito respectu dyspozycji pozwa-
nego In Concurrencia zachodzi Creditorum których musi
pozwany pacyfikować tak może aby złotych dwadzieścia
polskich we trzech dniach Aktorowi oddał Resztę zaś
złotych dwadzieścia y dziewięć aby na czas y święto świę-
tego Macieja Apostoła do rąk rzetelnego pod wolną
exekucyą lub na dobra lub na osobę decreta praesentis vigore.

Z Dekretu powinien Stanisław Leszczyński[?] Uciwemu
Sobestianowi Fraśkowi za karmienie świni brawor[?]
oddać złotych trzy in instanti non recedendo.

Z Dekretu Dorota Młynarka Grebienna powinna
Szkolnikowi oddać złotych cztery we trzech dniach chust
parę albo płótno rzemieślnik wykupić od Krawca.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 99,
        "numer_pozycji": "99",
        "strona_pagina": "fol. 48r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Dekrety sądowe",
        "osoby_podmioty": "Jędrzej Markowic (obywatel kraśnicki), Szymon Świstek [?], Kazimierz Koszykowiec, Wojciech Piasecki, Jakub Kłopot, Szmul (starozakonny, obywatel kraśnicki), Szymon Jartek [?]",
        "kwoty_podatki": "28 fl (pół trzeciej grzywny? / 2 fl 15 gr), 2 fl 12 gr (2 złp 2 gr za 3 spusty wódki)",
        "opis_sprawy": "Cztery dekrety z sesji 20 I 1702 r.: (1) sprawa Jędrzeja Markowica przeciw Szymonowi Świstkowi o 28 złp i kwartę; (2) sprawa Kazimierza Koszykowica z Wojciechem Piaseckim o inkwizycję świadków; (3) dekret dla Jędrzeja Markowica przeciw Jakubowi Kłopotowi o 2 fury nawozu; (4) sprawa starozakonnego Szmula przeciw Szymonowi Jartkowi i Jakubowi Kłopotowi o 3 spusty wódki z żyta.",
        "transkrypcja": """--- Skan #99 (fol. 48r) ---
W sprawie między Starozakonnym, Jędrzejem Markowicem Oby-
watelem Krasnickim Aktorem na moc zł trzydziestu bez dwóch
spory o zadatki y kwart dwadzieścia y pięć miodu pół trzecia
garca za gęsi y indyka złotych dwa groszy piętnaście długu
na długach z Szymonem Świstkiem[?] Necessariam Calculatio-
nem ante primam Juris adinvenit & Terminum Conservando
peremptorium.

W sprawie y Akciej między Uciwym Kazimierzem Koszyko-
wicem z jednej a Wojciechem Piaseckim o zniewagę
obojey strony Necessariam Inquisitionem testium decrevit
& Terminum Conservando peremptorium.

W sprawie y Akciej między Jędrzejem Markowicem Obywa-
telem Krasnickim Aktorem z jednej a Jakubem Kłopotem
pozwanym pół talara nawozu wrócić i oddać in instanti dwie
razy wóz odnieść inaczej odprzysiądz się w poniedziałek
używać per medium stronie y Sądowi.

W sprawie y Akciej między Starozakonnym Szmulem
Żydem Obywatelem Krasnickim z jednej a Szymonem
Jartkiem y Jakubem Kłopotem pozwanemi o niezapła-
cenie spustów trzech wódki proszą Sąd niniejszy
potrawiwszy trzy ćwierci żyta facere pośmiewiska aby
w dwóch niedzielach ab Actu praesenti złotych dwa
na swej groszy bez piątek oddał drugie złotych dwa
na swej groszy bez Jakub Kłopot że się raz bycie
przeczącej spustu wódki przy karczmie pod P. Paney
bliższego Aktora w przyszły piątek Wypadł ad Jura-
mentum & Terminum Conservando peremptorium.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 100,
        "numer_pozycji": "100",
        "strona_pagina": "fol. 48v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Intytulacja sesji i próby pióra",
        "osoby_podmioty": "Sąd Wójtowsko-Ławniczy Kraśnicki",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Niedokończony nagłówek sesji Sądu Wójtowsko-Ławniczego z piątku przed św. Maciejem Apostołem 1702 r. (17 II 1702 r.); poniżej wolna przestrzeń karty pokryta kaligraficznymi próbami pióra (esami-floresami).",
        "transkrypcja": """--- Skan #100 (fol. 48v) ---
Actum Coram Officio Advocatiali et Scabinali Crasnicen-
si Feria Sexta Ante Festum Sancti Mathiae Apostoli
proxima Anno Domini Millesimo Septingentesimo
Secundo.

[Poniżej wolna strona z kaligraficznymi próbami pióra]""",
        "link_swa": UNIT_LINK
    }
]

main_data.extend(part4_scans)
assert len(main_data) == 100, f"Expected 100 scans, got {len(main_data)}"

with open('/home/ubuntu/workspace/Gen/main_data_j18_part4.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j18_part4.json: {len(main_data)} skanów.")
