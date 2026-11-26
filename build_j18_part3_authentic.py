# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j18_part2.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989891"

part3_scans = [
    {
        "nr_skanu": 51,
        "numer_pozycji": "51",
        "strona_pagina": "fol. 23v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki i Łączony / Rachunek opiekuńczy",
        "osoby_podmioty": "Wawrzyniec Łysak (opiekun), Mateusz Żmięda, Marianna Żmiędzianka, Łukasz Śnieżek [?], Jakub Zając [Zaięczy?], Grzygiel Kowal, P. P. Rajcy",
        "kwoty_podatki": "20 gr, 8 złp, 2 gr/tydzień, 1 fl, 1 fl 10 gr, 12 gr, 1 fl 15 gr, 4 gr, 3 gr, 6 gr, 1 fl 17 gr, 3 gr, 9 gr, 2 fl 25 gr, 3 fl 10 gr, 3 fl 28 gr, 2 fl 20 gr, 51 fl 22 gr (expensa), 5 fl 7 gr, 74 złp",
        "opis_sprawy": "Dalszy ciąg rachunku opiekuna Wawrzyńca Łysaka za lata 1649–1651 nad Marianną i Mateuszem Żmiędami: wydatki na utrzymanie, odzież (suknie, płótno knapskie i zgrzebne), leczenie, umieszczenie Marianny w Szpitalu św. Ducha, pogrzeb Marianny oraz spłata długów Grzygielowi Kowalowi (suma expensy 51 fl 22 gr).",
        "transkrypcja": """--- Skan #51 (fol. 23v) ---
Maryey do Szpitala udawszy daliszmj dla Ubostwa pafrygare połetki zakupy
gr 20, w tymze roku czwartem chłopca Matusa niedziel ośm zacheiz jeko[?]
po którech aezydzięga czyni zł 8 W drugem roku 1650 temuz Matusowi
którego chował począwszy od Bożego Narodzenia az do Przewodniej Niedzieli
przez niedziel piętnaście dawałem na rastrawę po gr 2 na tydzień czyni to
fl 1 temuz za brój gr 20 Siostrze iego Marynie za brój fl 1/10 od prania chust
gr 12 od zrobienia sukni z płótna fl 1/15 temuz za zgrzebie gr 4 od płocenia i[e]go
płótna gr 12 Młockowi za zgrzebie gr 2 co przędziono to płótno gr 3 Od naprawy
skrzynki Siostrze iego gr 20 od szycia dwóch koszul temuz Matysowi gr 6 Na
prawę pogrzebną Łukaszowi Śnieżkowi[?] gdyz ją sami pochowali a szynarze za
chust wydał fl 1/17 Od wpisania Decretu gr 3 Od pisania Regestru gr 9 Jaka
byli dziecięcie to chłopca chował z siostrą iego Maryną gr 20 za obiad temu
Matysowi na strawę fl 1/15. W trzeciem roku 1651 począwszy od Bożego
Narodzenia az do Świątek przez niedziel dwadzieścia temuz Matysowi dawałem
na strawę co dzień po gr 2 uczyni fl 8 temuz za brój fl 1 nie chciałem a by
w nędze nie dać ale P. P. Rajcy przykazali Sierotem z tego bogu nie chcieć
tylko w długi za służbę, Na pogrzeb Siostry iego Maryny daliśmy fl 2/25 Od
wjechowania to było z siostrą z Jakuba Zaięczego[?] od Gód az do Przewodniej Niedzieli
dałem fl 3/10 za papier na Regestr gr 1 za suknią Matusowi fl 3/28 temuz
kiedy poszedł do Łukasza Zaięczego[?] dałem fl 2/20 Płótna knapskie łokci
12 a zgrzebnego było miar 10 to na miękkich i zgrzebnych płócien na dwie pary
zrobić dać, czyni tedy Expensy Suma fl 51/22 reię potrąciwszy
od wydatku tego co nadto wydał fl 5/7 z których zas Siedmdziesiąt y czte-
rych złotych siedm dziesiąt zasłużą przepadały w Paktowi atrawiwszy bo
Grzyglowi Kowalowi kto wedle decreta [nieczytelne], odpłaciło się ich nie mało""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 52,
        "numer_pozycji": "52",
        "strona_pagina": "fol. 24r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Dekret opiekuńczy",
        "osoby_podmioty": "Wawrzyniec Łysak (pozwany), Mateusz Żmięda (aktor), Jakub Zając [Zaięcki], Bartosz Kulka, Wojciech Byk, Sąd Radziecki Kraśnicki",
        "kwoty_podatki": "20 fl, 30 fl, 2 fl (Bartosz Kulka)",
        "opis_sprawy": "Zakończenie odpowiedzi Wawrzyńca Łysaka (kwestia długu lubelskiego, krowy skradzionej i sumy na obligu) oraz początek dekretu Sądu Radzieckiego Kraśnickiego w sprawie Żmięda przeciw Łysakowi (wzmianka o sumie w Lublinie z 8 X oraz 2 fl od Bartosza Kulki).",
        "transkrypcja": """--- Skan #52 (fol. 24r) ---
co do Skargi Pana nie dobrze świadczy. A że Skargę zadaie
o fl 20 i konia że od Nieboszczyka Zaięckiego szeląg nie wziął żadnego
ani mi ich odsyłał ani miał odbierać, ani żadnego długu w Lublinie
nie brał ani płótna ieno com wziął w Regestrze położył. Co się zas tycze
zatrzymania którem się dopominał nigdy nie tusząc (bo i sam za sobą oświadczam
to potrzeba), wypytać się komu w pole pasą, kto brał zboża a krów od tych ktorym
nie skradziono a ta krowa do spoznachania fl 20 wedle konia zynstai[?] za
fl 30 co ia sobie sam w sumie iak zachowaię, A że rzekomo przez zaniedbanie
tey sumy z rąk swych nie wydawał położył przecież liberos ab inpetitione Aktorowi
niech iey sobie raczej na gruntach zastawnych na obligu do zwiedzenia z który na in-
tercesją pokład. Nadto też krowę Bartosz Kulka ukradł fl 2 co wszystko
na Uważny rozsądek Sądowy podaię.

Decretum.
Urząd tedy niniejszy Radziecki Krasnicki pilnie przesłuchawszy controwersyą
stron obudwu y one dobrze uważywszy widząc w regestrach Pozwanego dobrze
pokazuiących się tak iż Dobrze miedzy stronami denderował Nagradzając iże
złożyli z Dokumenty Sumy Capitalnej Skarżącym Aktorom Pozwanego Skargę
płytko, a na wywód intercesyą zalał i od grafu należytą oddał, wezmą Prowizor
do skutku pokazać claro iak Sędzia to iest Sumy Capitalnej dać obojgu dzieciom
za siostrą iego Maryną zbytkami, temu Aktor przydał z zapisu dług ich sąsied
libero sto, a takowych się dziś skapatować może i dać na nie rachunek z tej części
pokładztwem Regestru z tychże póżnych lat, a zwłaszcza o Nieboszczyka Pana
Wojciecha Byka, po tych siedm setek i czterech lat niezapłaconych Nieboszczykowi
Bartosz Kulka fl 2 sobie iako Jest Opiekunem Zbiernego dawał, o które
resy biletu widzą z danej Sumy Capitalnej w Lublinie ad praesens d. 8 Octobris
na krakowskie zakłady, które wedle Decretu Sądu Radzieckiego Krasni-
ckiego""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 53,
        "numer_pozycji": "53",
        "strona_pagina": "fol. 24v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1661",
        "kategoria": "Sąd Radziecki / Dekret i intytulacja taksy",
        "osoby_podmioty": "Mateusz Żmięda, Wawrzyniec Łysak, Wawrzyniec Kordek, Jakub Zając [Zaięcki], Bartosz Kulka, Wojciech Byk, sukcesorowie Rogalowscy",
        "kwoty_podatki": "25 złp, 71 złp, 15 złp, 42 złp, 7 złp 10 gr",
        "opis_sprawy": "Dokończenie dekretu w sprawie Żmiędy z Łysakiem (zasądzenie 42 złp do rąk aktora w 6 niedziel oraz 7 złp 10 gr na dzieci Bartosza Kulki, oddalenie pretensji o krowę; obie strony wyrok przyjęły) oraz nagłówek ingrosacji taksy i działu dóbr po Wojciechu Rogalowskim (piątek przed Obrzezaniem Pańskim 1662, tj. 30 XII 1661 r.).",
        "transkrypcja": """--- Skan #53 (fol. 24v) ---
tego tamtego od przysięgi tej Sumy Aktor y na naszem naznacza granicę po
Nieboszczyku Wawrzyńcu Kordku pozostałą w któreym się Inwentarz do kładu Aktor
chciał regimować albo bardziej przenosić, Co się tycze złotych dwudziestu pięciu albo
ze Aktor wiarę daie Lubelskiemu że ie odebrał od Nieboszczyka Jakuba Zaięckiego, tak
że głowna część tych dwoch, czego się Sąd nie może dowiedzieć o tych pieniądzach nie
słychał ani ich widział, na Sąd w wątpliwości tego iuramentu incam iuramenti votum
iako tych pieniędzy deficite nie odebrał tak że iako głowna dochodzą poświadcza niech
to ale tylko każdemu ma być dowiedzenie a żeby tego miał by to skłonić, komu
przysięgać Aktor Pozwanemu iest in facie eiusdem Offi libere odpuścił i deo iurat libe-
ra z przypadku alioquin Aktorowi zostanie, a cokolwiek idzie na Aktor albo tych
ośm dwudziestu pięciu zapłaci Zaięckim wedle Ratusza Lubelskiego takowego
dochodzi, A z owych regestrach które Sąd przed sobą pokładał wielkie zakła-
mania dzieią się, w których po części niektóre rzeczy Sąd nie uważa by iść do int-
resje na łaskę P. Pozwanego długi złotych siedmdziesiąt ieden oprócz Skarżących piętnastu
który Sąd widzi na oczach potrzebę Aktora kończyć na Aktor spójrzeć, tedy ten dług
złotych czterdziestu i dwa Sąd niniejszy nakazuje aby Sądowi do rąk Aktora do
niedziel sześci oddał, złotych siedm i groszy dziesięć Nieboszczyka Bartosza Kulki dzieci-
bie dawał ma b. z. kładź to swoich dwa zaś oba za pnie i odkupi od nich tym
Nieboszczyka Bartosza Kulki, Zaś wszystkie pretensje osobliwie co się Aktor do Po-
zwanego za zastawę Sądowej dopominał, tak że co Sąd z Aktorem obnaża y krowę
żadną dostawać Sąd niniejszy z obadwu stron one kasuie, Salva praesente Aktor
reservato z okoliczności Nieboszczyka Wawrzyńca Byka wedle się zeznań
który brat, tedy wobec przez Aktora ma nieść o krzywdy i straty one. Quod
Decretum ab utraque parte susceptum est.

Actum Coram Offo Consulari Feria Sexta
ante Festum Circumcisionis Christi Dni proxia 1662
Ingrossatio Taxae fundorum simul et divisionis bonorum
inter Succores Rogalowskios.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 54,
        "numer_pozycji": "54",
        "strona_pagina": "fol. 25r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1661–1662",
        "kategoria": "Sąd Radziecki / Taksa i dział dóbr",
        "osoby_podmioty": "Jan Grzętka (opiekun), Sebastian Batusik [Batuś] (opiekun), Wojciech Rogalowski al. Sosnowski (zmarły), Wojciech Kwasowic (burmistrz), Wojciech Szafrankowic (rajca), Maciej Koniega (rajca), Maryna, Zofia i Ewa Rogalowskie (starsze córki), Gabriel Kłopot, Matyjasz Jeżykowic (exactor przysięgły)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Prezentacja przed Sądem Radzieckim przez opiekunów Jana Grzętkę i Sebastiana Batusia taksy gruntów oraz działu majątkowego po zmarłym tkaczu Wojciechu Rogalowskim al. Sosnowskim z udziałem rajców oraz taksatorów Gabriela Kłopota i Matyjasza Jeżykowica.",
        "transkrypcja": """--- Skan #54 (fol. 25r) ---
Do Urzędu y Akt niniejszych Radzieckich Krasnickich przy-
szedłszy oblicznie Uczciwi Mężowie Jan Grzętka y Sebastian
Batuś Mieszczanie Krasniccy Opiekunowie Sierot pozostałych po Niegdy
Uczciwem Wojciechu Rogalowskim przedmieszczaninie Krasnickim przy-
nieśli Taxę gruntów separata copia spisaną wespół z Podziałem
między ich opisanemi sierotami dobrowolnie uczynionym prosząc
Urzędu niniejszego aby to było do Akt niniejszych przyjęto y zapisa-
no, Której prośbie ich Urząd niniejszy chcąc dosyć uczynić ex
quo Aeta iustis deneganda, Supred Pisarzowi Przysięgłemu przed
sobą głośno rozkazał, a potym do Akt niniejszych wpisać pozwolił
cuius series de Verbo ad Verbum talis sequitur tenor.

Z Rozkazania Sławetnego Pana Wojciecha Kwasowica Bur-
mistrza na ten czas rezyduiącego Krasnickiego także Sławetnych
Panów Wojciecha Szafrankowica y Macieja Koniegi Radziec Krasni-
ckich Collegów przy boku iego siedzących z instanciej Uczciwych Ja-
na Grzętki y Sebastiana Batusika Opiekunów Sierot pozostałych po
niegdy poćciwym Wojciechu Rogalowskim al[ia]s Sosnowskim Rzemiosła
Tkackiego Przedmieszczaninie Krasnickim byli zaproszeni na taxę Dworne
Uczciwi Mężowie, to iest z strony Uczciwego Jana Grzętki Opiekuna
starszych Dzieciów Marynie Zophiei y Ewie pozostałych Sierot po
wzyż pomienionym Wojciechu Rogalowskim z pierwszej żony Rogalo-
wskiej Małżonki pierwszej przerzeczonego Wojciecha Rogalowskiego
spłodzonych (Tefanes albo y Dróżdż żonie obwarowanych) był Uczciwy
Gabryel Kłopot przedmieszczanin Krasnicki y Matyiasz Jeżykowic Exactor""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 55,
        "numer_pozycji": "55",
        "strona_pagina": "fol. 25v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1661–1662",
        "kategoria": "Taksa nieruchomości",
        "osoby_podmioty": "Matyjasz Jeżykowic, Sebastian Batusik, Katarzyna, Agnieszka, Ignacy [Jan?] i Kazimierz Rogalowscy (młodsze dzieci), Katarzyna Węgorkiewiczówna (żona ostatnia), Sebastian Węgorkiewicz (dziad i opiekun), Stanisław Szwankowic (ławnik), Stanisław Celica [?] (ławnik), Cynda Młynarowski, Cyroń Madejowski, Dworzański, Stanisław Krokoszowski, Matyjasz Kowalik, Wojciech Czaia",
        "kwoty_podatki": "200 fl (dom z ogrodem i stodołą za Bramą Lubelską), 30 fl (półłanek na Zarzeczu), 16 fl (ogród na Stawiskach), 150 złp (rola za Podlesiem)",
        "opis_sprawy": "Szczegółowa wycena nieruchomości po Wojciechu Rogalowskim dokonana przez ławników Stanisława Szwankowica i Stanisława Celicę: dom za Bramą Murowaną Lubelską z ogrodem i stodołą (200 fl), rola na Zarzeczu (30 fl), ogród na Stawiskach (16 fl) i rola za Podlesiem (150 złp).",
        "transkrypcja": """--- Skan #55 (fol. 25v) ---
Mieszczanin y Exactor na ten czas Przysięgły Krasnicki, a z strony Uczciwe-
go Sebastiana Batusika Młodszey Sieroty Katarzyny Agnieszki Ignacego
y Kazimierza spłodzonych z Uczciwej Katarzyny Węgorkiewiczowny Żony o-
statniej Uczciwego Sebastiana Węgorkiewicza Dziada tych Sierot Opiekuna
Testamentalnego y z Urzędu approbowanego, gdzie tak napisali pomienio-
nego Węgorkiewicza jako też y Sebastiana Batusika byli proszeni Sławetni Mę-
żowie Stanisław Szwankowic y Stanisław Celica[?] Ławnicy Przysię-
gli Krasniccy. Którzy wyszedłszy na przedmieście za Bramą Murowaną
Lubelską do domu Rogalowskiego Sławney pamięci o dwóch wierzchnich naprzeciw-
ko Ogroda Szpitalnego z Ogrodca także Stodoły y Spichlerza niżey
miedzy miedzą Cynda Młynarowskiego, z drugiej strony Ulica co
spolnie ktora się ciągnie od Młyna Miejskiego do Miasta, Czeladź wew-
nęcznie Nazwiskiem Dwornego iest dom cały opustoszały niema dachu ani
drzwi okiennic garc budynku iako komory z szlęz[?] porobione ale ze
wszystko szczęki w nich słabe y powały powybiiane płoty do koła złe
Ogród opalone, Lecz iżby to tedy iż tak czasy dały y grunty różne mięsza-
ne albo dalekowiersze są dokładniejsze y budowniejsze y niektóre pusto stoją
wziąwszy P. Boga na pomoc otaxowali pomieniony dom ze wszystkiem co
to iest z ogrodem y ze stodołą za fl 200 (miary borgu raczkowięć dzień
Zarzeczu miedzy miedzami miedzą Cyroni Madeiowskiej, a z drugiej
strony Dworzanskiego Półłanka tą szacowali za fl 30, Ogród na Sta-
wiskach leżący między miedzami miedzą Stanisława Krokoszowskiego
z jednej strony Matyjasza Kowalika ten szacowali za fl 16 tamże iest
y za przednią częścią Podlesia między miedzami miedzą Wojciecha Czaia
z drugiej strony Księżego Ogroda ten szacowali za złotych Półtorasta ktory
za to tej strony obiedwie Contentowały się y oną pro rato et grato przyjęły.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 56,
        "numer_pozycji": "56",
        "strona_pagina": "fol. 26r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1661–1662",
        "kategoria": "Dział majątkowy między sukcesorami",
        "osoby_podmioty": "Sebastian Węgorkiewicz, Sebastian Batusik, Katarzyna, Agnieszka, Jan i Kazimierz Rogalowscy (młodsze dzieci), Katarzyna Węgorkiewiczówna (matka), Paweł Temliński [?], Jan Olkowski, Gabriel Kłopot, Jan Grzętka, Maryna, Zofia i Ewa Rogalowskie (starsze dzieci), Anna Rogalowska (1. żona), Jan Baty, Kacper Jeżykowic Skarnik",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Popołudniowy dział dóbr (Divisio inter eosdem Succores Tempore Pomeridiano): czworo młodszych dzieci z Katarzyny Węgorkiewiczówny otrzymało ogród z sadem na Podlesiu, ćwierć roli za Lasem i ogród na Stawiskach, natomiast starsze dzieci z 1. żony Anny przejęły dom z ogrodem i stodołą wraz z obowiązkiem spłaty długów po ojcu.",
        "transkrypcja": """--- Skan #56 (fol. 26r) ---
ty zadaiąc aby to do Ksiąg dla pamięci było przyjęto y zapisano.
Quod Actum est firmando memorati.

Divisio inter eosdem Succores
Tempore Pomeridiano.
Na żądanie Uczciwych Sebastiana Węgorkiewicza y Sebastiana Batusika
Opiekunów sierot młodszych Katarzyny Agnieszki Jana y Kazimie-
rza po niegdy Uczciwem Wojciechu Sosnowskim al[ia]s Rogalowskim pośled-
niej żony Katarzyny pozostałych a wtórej Matki Katarzyny by-
li postronnych osób wziętych były zaproszeni na ten dział Uczciwi Mężowie
Paweł Temliński[?], Jan Olkowski y Gabryel Kłopot, a z strony Giermów[?]
a Ławnik zaś Uczciwego Jana Grzętki Opiekuna Starszych Dzieci
to iest Maryny Zophiei y Ewy pierwszej Małżonki Anny Rogalowskie
było wziętych spomnionych Mężów Rogalowskich byli zaproszeni
Uczciwi Jan Baty przedmieszczanin Krasnicki, Kacper Jeżykowic Skar-
nik y Ciesielski Mieszczanie Krasniccy, Którzy wziąwszy Pana Bo-
ga na pomoc onychże podział między stronami uczynili, Naprzód
Ogród z Sadem leżący na Podlesiu także ćwierć roli leżącej za Lasem
y Ogród na Stawiskach to przysądzili dzieciom Czworgu to iest Katarzynie
Agnieszce Janowi y Kazimierzowi z wtórego Małżeństwa z Katarzyną
Węgorkiewiczowną spłodzonym, A zaś ze wszystkim budynkiem tak z do-
mem ogrodem y stodołą przysądzili starszym dzieciom pierwszego Małżeństwa
z Anną Rogalowską spłodzonych, które powinne będą długi pośled-
nieboszczyka zaciągnione na wszelką osobę którego się znaydzie do
tych wzglądów pełnić długów spłacić do którego spłacenia długów dzieci
starsze wtórego Małżeństwa nie powinny będą należeć, Ale tylko
Starsze dzieci,""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 57,
        "numer_pozycji": "57",
        "strona_pagina": "fol. 26v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1661–1662",
        "kategoria": "Sąd Radziecki / Koniec roku 1661 i otwarcie 1662 r.",
        "osoby_podmioty": "Wojciech Kwasowic (burmistrz), Jan Grzętka, Sebastian Węgorkiewicz (dziad i aktor), Sebastian Batusik (pozwany), Wojciech Rogalowski (zmarły)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Konfirmacja działu w domu burmistrza Wojciecha Kwasowica (wtorek przed św. Grzegorzem 1661 r.) i zamknięcie księgi za rok pierwszy ('Finis huius anni primi'). Następnie otwarcie sesji roku 1662 (wtorek przed Zwiastowaniem NMP 1662 r.) ze skargą Sebastiana Węgorkiewicza przeciw opiekunowi Sebastianowi Batusikowi o brak inwentarza, rozdziału, rachunku i testamentu.",
        "transkrypcja": """--- Skan #57 (fol. 26v) ---
starsze dzieci, wszelki raczey także co do wyprawy należy onym podług
wspomnionych Ksiąg opisano iest zarówno strony obiedwie podda-
li się końcem w Księgach strony obiedwie konfirmowały, nie z czego w
przyszłych latach więc opisanych było iako wszystkim zezwalają Dział
ten w domu Sławetnego P. Wojciecha Kwasowica Burmistrza na ten czas
Będącego dnia we wtorek przed S. Grzegorzem Papieżem Anno Dni
Millo Sexcento Sexagesimo Primo. Ad Actis hisce adscriptum
supradictum erat.

Finis huius anni primi.

Actum Coram Offo Consulari fra 3tia
ante Festum Glosae Anuntiationis B M Virginis
proxa Anno Dni Millmo Sexcentmo
Sexagmo Secundo.
Ratio Tutorum de bonis Rogalowski.
W sprawie y Akciej Sądowej między Uczciwymi Janem Grzętką y Se-
bastianem Węgorkiewiczem Aktorem z jednej, a Uczciwym Janem Grzętką y Se-
bastianem Batusikiem mieszczanami Krasnickiemi Opiekunami dzieci po-
zostałych po Nieboszczyku Wojciechu Rogalowskim Przedmieszczaninie
Krasnickim Pozwanemi z drugiej strony, przeciw którym Aktor oskarżając
inparata copia spisaną podał cuius series talis sequitur tenor. Moi Łaskawi
P. Burmistrzu y Pany Collegami W.M., proszę W.M. zacni Sędziowie
wobec po Nieboszczyku Rogalowskim za jako dziad tych sierot, iż P. Opie-
kun mianowicie Batusik nie wie ani o dzieciach ani o gruntach za czyją
prośbę W.M. niech inwentarz pokaże y rozdział, przy tym rachunek ze
wszystkiego żeby uczynił, a kto nie dbały tedy na swe miejsce inszego Opie-
kuna niech stawi, także y Testament Nieboszczykowski niech pokaże.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 58,
        "numer_pozycji": "58",
        "strona_pagina": "fol. 27r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1662",
        "kategoria": "Rachunek opiekuńczy (percepta i expensa)",
        "osoby_podmioty": "Wojciech Rogalowski al. Sosnowski (zmarły), Wawrzyniec Zięba, Sebastian Węgorkiewicz, Bractwo Różańca Świętego, Pisarz miejski, Panowie Rajcy",
        "kwoty_podatki": "20 złp (percepta: 5 złp, 12 złp od W. Zięby, 2 złp za kaftan); Expensa: 2 fl dzwonne, 12 gr niedzielnica, 18 gr bakałarz, 21 gr piwo dla bractwa, 5 gr dół, 1 fl 18 gr zakosteła, 14 gr piwo, 17 gr spisanie inwentarza, 23 gr obiad rybny, 6 gr flaki, 4 gr kiszki, 1 gr ocet, 17 gr garnki, 1 fl 5 gr piwo, 24 gr chleb, 18 gr wpis inwentarza, 1 fl czynsz zamkowy, 15 gr msza, 7 gr Węgorkiewiczowi, 21 gr piwo na szacunek, 20 gr pozew, 5 gr dekret, 13 gr statut",
        "opis_sprawy": "Kompletny regestr dochodów (20 złp, w tym 12 złp od Wawrzyńca Zięby) i wydatków pogrzebowych oraz sądowych po Wojciechu Rogalowskim al. Sosnowskim, obejmujący m.in. dzwonne, posługę bakałarza, stypę (obiad rybny, flaki, chleb, piwo), czynsz zamkowy z chałupy oraz taksy za spisanie inwentarza, szacunek i dekrety.",
        "transkrypcja": """--- Skan #58 (fol. 27r) ---
za drogi frasunek niczego nie mieć moja Pani gdyż niczego tak wielkie-
go kłopotku darmo ma słabą niedługo nigdziey do tego chodzić proszę z
pokorą o miłosierdzie gdyż to P. Bóg u W.M. będzie widział kiedy W.M. będzie-
cie mieli wzgląd nad temi sierotami.
Pozwany stanąwszy oblicznie przed Sądem onymże Regestr tak Percepty
iako też y Expensy pokładali cuius talis sequitur tenor. Regestr dochodu
dobrego Nieboszczyka Wojciecha Rogalowskiego al[ia]s Sosnowskiego.
Naprzód odebraliśmy złotych pięć, od Wawrzyńca Zięby złotych
dwanaście, za kaftan płócienny wzięliśmy złotych dwie, Suma to
czyni złotych Dwadzieścia. Expensy z tego pokładali takowy.
Naprzód gdy Nieboszczyk Wojciech Rogalowski Umarł daliśmy od dzwon-
nego w dzień razy dzwonili fl 2 Niedzielnica wyświęcili gr 12 Bakała-
rzowi gr 18 Bractwu Różańca S. piwa konwi dwie gr 21 od dołu kopania gr 5
Zapłono zakościela fl 1/18 od uszycia gr 2 płótna, Zbadalec[?] u rata
przygłówek za posładkę gr 2 temuz za piwo gr 2, Curowi[?] ze miasta
płóciennego dwie konwi piwa gr 14 od spisowania Inwentarza gr 17
Obiad było Rybny zacięto gr 23 za flaki gr 6 za kiszki[?]
gr 4 za Ocet gr 1 od garków za gubiękę gr 17 za piwo konwi dwie fl 1/5
za chleb groszy 24 Kalitkiewy przedaie kiepsko na posładkę gr 5
Od wpisania Inwentarza gr 18 Czynszu zamkowego z chałupy fl 1
Na panek[?] piwa gr 4 Na Mszę S. gr 15 P. Węgorkiewiczowi od odbie-
rania bramy gr 7 za dwie miscie gr 3 Na syta[?] Barana gr 18 Ludzie
którzy przychodzili na szacunek y na rozdział piwa konwi dwie gr 21 Dla
tychże posładki półkwarty gr 5 P. Pisarzowi od zapisowania w Księ-
gi gr 6 temuz od czytania gr 1 od pisania pozwu gr 20 od Decretu
gr 5 od czytania gr 1 gdy Panowie Rajcy byli przy szacunku dałem
na piwo gr 7 na kładki gr 10 za piwo dla ludzi gdy mieli tę sumę
gr 15 Od starych ludzi na posładkę gr 25 od zapisowania Statutu gr 13.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 59,
        "numer_pozycji": "59",
        "strona_pagina": "fol. 27v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1662",
        "kategoria": "Sąd Radziecki / Zatwierdzenie rachunku",
        "osoby_podmioty": "Sąd Radziecki Kraśnicki, opiekunowie sierot po Wojciechu Rogalowskim",
        "kwoty_podatki": "13 gr, 20 gr, 2 gr, 19 fl 20 gr (suma expensy)",
        "opis_sprawy": "Zamknięcie rachunku opiekuńczego po Wojciechu Rogalowskim (suma expensy 19 fl 20 gr) i dekret Sądu Radzieckiego Kraśnickiego zatwierdzający rachunek oraz nakazujący opiekunom pilną troskę o sieroty na rok przyszły. Ostatnia karta XVII-wiecznej części księgi (Acta Pupillorum).",
        "transkrypcja": """--- Skan #59 (fol. 27v) ---
gr 13 pan dla ludzi co rozdział między sierotami czynili gr 20 od jadła
posładki za gr 2 to wszystkiego in summa czyni fl 19/20.
Urząd tedy niniejszy Radziecki Krasnicki przesłuchawszy Rachunku
pomienionych Opiekunów któremu rachunkowi iż Aktor wiarę daie wobec
niż Późniejszych Opiekunów z Opieki ratyfikować nakazuje ofierę Opie-
kunom aby na przyszły rok koło tych sierot pilne staranie mieli Decretum est
onychże approbuje. Quod Decretum ab utraque parte susceptum est.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 60,
        "numer_pozycji": "60",
        "strona_pagina": "fol. 28r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Zapis długu i wykup nieruchomości",
        "osoby_podmioty": "Stanisław Sprawski, Anna Sprawska (małżonkowie), Tomasz Anczarek (przedmieszczanin), Baltazar Safranek [Safrankowiec] (zmarły), Andrzej Rzędecki (administrator klucza kraśnickiego)",
        "kwoty_podatki": "300 złp (po 30 gr w złoty)",
        "opis_sprawy": "Początek II części księgi — czystopisu akt wójtowsko-ławniczych z lat 1701–1702 (sobota po św. Łukaszu 1701 r., tj. 22 X 1701). Stanisław i Anna Sprawscy zeznają oblig na 300 złp płatny do rąk administratora klucza kraśnickiego Andrzeja Rzędeckiego na św. Wojciecha 1702 r. z tytułu wykupu prawem bliższości półłanka Rędzinskiego z budą i placami na Przedmieściu po zmarłym Baltazarze Safrankowcu z rąk Tomasza Anczarka.",
        "transkrypcja": """--- Skan #60 (fol. 28r) ---
[Dopisek u góry po prawej: o krowę skrzywdz(oną)]
Actum Coram Officio Advocatiali et Scabinali Crasnicensi
Sabbato post Festum Sancti Lucae Evangelistae proximo
Anno Domini Millesimo Septingentesimo Primo.

Przed Urzędem y Aktami niniejszemi Woytowskimi y Ławni-
czemi Krasnickiemi w osobach swoich stanąwszy Panowie
Stanisław Sprawski y Anna małżonkowie Obywatele
Krasniccy Zdrowi na umysłach y ciałach swoich bę-
dący iasnie iawnie dobrowolnie zeznali praesentibusque
znaią Iż Oni Na Windikowanie y Wykupno dobr pe-
wnych specifice Pułanka roli z Budą z Placami tu na
Przedmieściu Krasnickim ze wszystkiemi należytościa-
mi Rędzinskie rzeczonej z dawna w Posesiey na
ten czas Uciwego Tomasza Anczarka Przedmieszczani-
na Krasnickiego będących sobie zeznawaiącym po
niegdy Uciwym Baltazarze Safrankowcu Obywate-
lu Krasnickim Viuo suo et proprium prawem natural-
nym bliskoscią odkupienia należących, Summę złotych
polskich trzysta monety w koronie idącey w każdy zło-
ty po groszy trzydzieści rachuiąc zóstali Wdzięczni
zaś obliguiemy się y zapisuiemy sub onere Juridictis
protestibus do rąk Jegomości Pana Andrzeia Rzęde-
ckiego Administratora Klucza Krasnickiego na
czas y święto Świętego Woyciecha Roku przyszłego
tysiącznego siedmsetnego drugiego przy-
padaiącey bez żadney zwłoki y wymowki oddać Inquan-
tum by nie oddali Wolney Exekucyi w też dobra spe-
cifikowane od pomienionego Anczarka wykupione""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 61,
        "numer_pozycji": "61",
        "strona_pagina": "fol. 28v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Oblig i protestacja cechowa",
        "osoby_podmioty": "Stanisław Sprawski, Anna Sprawska, Sebastian Jędryszek (majster szewski), Jan Grymus, Jamiel [?] Grymus, Wojciech Beski (ławnik)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie i podpisy pod obligiem Stanisława i Anny Sprawskich. Następnie wpis z 24 X 1701 r.: uroczysta protestacja majstra rzemiosła szewskiego Sebastiana Jędryszka przeciw braciom Grymusom (Janowi i jego bratu) o znieważenie praw cechowych i obelgę w obecności ławnika Wojciecha Beskiego.",
        "transkrypcja": """--- Skan #61 (fol. 28v) ---
wpuszczaią [póki?] sobie w tym czasie zaciągnionemi tera
wszystkich zeznawaiący w tychże dobrach Wykupować,
bez exekucyi Dworskiey prywatney czego sobie zawoła-
nie mieć nie powinni Zeznawaiący, a komu innemu
w tey summie puścić lubo poddanego Na tymże gron-
cie osadzić alias in forma cogniti debiti in for-
ma solita quam plenissima et perfectissima.
Stanisław Sprawsky Anna Sprawska

Actum Coram Officio Advocatiali et Scabinali Crasnicensi
Feria Secunda post Festum Sancti Lucae Evangelistae
proxima Anno Domini Millesimo Septingentesimo Primo

Do Urzędu y Akt niniejszych Woytowskich y Ławniczych Krasnickich
w osobie swoiey przyszedłszy Uciwy Sebastian Jędryszek mieszczanin
Krasnicki rzemiosła szewskiego Majster Solennie Jurec-
kim razem protestował się przeciwko Sławetnemu Ja-
mielowi[?] y Janowi Grymusom Mieszczanom Krasnickim
Słyszowi y Bratu swoiemu Iż oni zapomniawszy boiaźni
Bożej y miłości bliźniego bez dania okaziey do tego Sławetnego
Woyciecha Beskiego Ławnika Krasnickiego siedzącego przy tym
stole poważyli się usiadłszy mówić że protestant [ty?] na
swego M. M. Warstatu nie komu nie mieć tylko naturalnym
sposobem a mianowicie według praw Cechu nadanych że
wypłaciwszy Majstrowi wolno obcemu między stołem zecho-
wać takie upstrzone a po tym Bączkowi na poważenie
bezczesności iako defacto pomieniony Jan Grymus z
zeformany [wspólnik?] swoiemi z tego się przyczyńca wyżej
odwazył stłuczeniem nieuszanowawszy szacunku ludzkiego przez
cośiny[?] słuszne zasłużył mianowicie pomieniony Jan
Grymus o które złocenie dna w tenże czas skarżącemu""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 62,
        "numer_pozycji": "62",
        "strona_pagina": "fol. 29r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Protestacja przeciw burmistrzowi",
        "osoby_podmioty": "Tomasz Sobiec (przedmieszczanin), Jan Sokołowicz [Sokołowski?] (burmistrz kraśnicki), Stanisław Janny (mieszczanin), Konwent Kanoników Regularnych i Bractwo",
        "kwoty_podatki": "100 złp (koszty), 70 złp (reszta sumy)",
        "opis_sprawy": "Zakończenie protestacji Sebastiana Jędryszka oraz nowa protestacja z piątku przed św. Szymonem i Judą 1701 r. (21 X 1701) wniesiona przez przedmieszczanina Tomasza Sobca przeciw burmistrzowi Janowi Sokołowiczowi [Sokołowskiemu?] o niedotrzymanie kontraktu i konsensu konwentu kanoników przy kupnie pustek Kuchniowskich z ogrodem Liderlińskim.",
        "transkrypcja": """--- Skan #62 (fol. 29r) ---
szkodę w tem grozi się Obwieszcza przemiana ta krowa skrzywdzona
Contemptos mieszczan dochodzić in foro fori.

Actum Coram Officio Advocatiali et Scabinali Crasni-
censi Feria Sexta Ante Festum Simonis et Judae
Apostolorum proxima Anno Domini Millesimo Septin-
gentesimo Primo.

Do Urzędu y Akt niniejszych w osobie swoiey przyszedłszy
Uciwy Tomasz Sobiec Przedmieszczanin Krasnicki solennie
z wielkim żalem protestował się przeciwko Sławetnemu
Panu Janowi Sokołowiczowi[?] Burmistrzowi Krasnickiemu
oto Iż On zapomniawszy Boiaźni Bożej y miłości bliźniego
poważył się nie respektuiąc na Urząd Swój na ktory przysiągł
lekkie sobie prawa trzymając onegoż nie dotrzymuiącym Słowa
Kontraktu obecnego powarzać lubo nie chciał, bo gdy
Stanisław Janny mieszczanin sobie okazał kupna dał pustki
Kuchniowskie rzeczonej przy którey Ogród Liderliński quon-
dam nazwany iest tu przy Krasniku leżący przedał za na
przedaż dane słowo z podanym y wiarą Urzędu y Burmistrzem
będąc assekurował że dotrzymać przeciw każdemu do-
br, na sumie że nie znacznego przywrócił z tego że mu
funkcyę złożyć kazał oprócz kosztów pochodnych na
złotych sto wyprowadził wydał która osobać iedna kiedy
dał ten zapis Intromissią gruntu przedanego a odużo
czyść y dalszy summę złotych siedmdziesiąt pulkruk[?]
którą część gruntu na swoje dobra ad offensa na wz-
mianę pieniędzy się assekurował Consensus przenies-
ienia od zwierzchności Konwentu tutejszego Ka-
noników od Bractwa otrzymać obiecał na one na
dobrach swoich zapisał przed Aktami Burmistrzowskiemi
y Radzieckiemi Krasnickiemi czego odmówił
na wielką szkodę protestanta Gloriose""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 63,
        "numer_pozycji": "63",
        "strona_pagina": "fol. 29v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Zeznanie świadka",
        "osoby_podmioty": "Tomasz Sobiec, Stanisław Maziarczyk, Andrzej Stachowski (świadek), Aucek (Żyd), Berek (Żyd)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie protestacji Tomasza Sobca oraz zeznanie świadka Andrzeja Stachowskiego z 26 X 1701 r. na instancję Stanisława Maziarczyka w sprawie zakupu żyta na pierwszym targu przez Żydów Aucka i Berka oraz sporu o zalewanie słodu i wódkę.",
        "transkrypcja": """--- Skan #63 (fol. 29v) ---
czyniąc Dnia wczorajszego. Akt tey Protestacyi Uprzedza-
iącego Uczyniwszy Nad to dzisieyszy w kłótney Bur-
mistrz nie przedawa dobr Uczynił tylko protestan-
towi iż nie fundowanie prawa iego potrzebna iest nie było by
myślnie się schronić miałem z tąd y z teyże wota
prawa Owszem to za kościelne pełne iako z winy
przeciwko sobie mianym Słowa danego w sposobie
Kupieckiego przez przedawcę zachowane za to że przy
dy choćby u kupca zapisu rzecznego poczęte było
spisanie od sąsiedztwa gdyż z weczarstwa danego
za mną w tenże zapis y rezygnacyą otrzymać miał
y tym men protestat me quoad Omnia Juris in eo
sua prosequendo tempore alio iterum protestando się.

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Quarta Ante Festum Sanctorum
Simonis et Judae Apostolorum proxima Anno
Domini Millesimo Septingentesimo Primo.

Ad Instantiam H. Stanislai Maziarczyk Testis
H. Andreas Stachowski Obywatel Bebravs[?] Krasnicki
Recognovit We czwartek roku terazniejszego iak nay-
pierwsze żyto na targu nastało przybywszy do miasta dwie
Żyda różnych przykładki dawać naprawuiący w tymże
onychże oba tych żydów Aucka y Berka w sieni do mar-
ni rzekli te słowa zalewał słód Stanisław Maziar-
czyk odpowiedział nie będę zalewał żydzi rzekli dyć
my na pew kupiliśmy żyto w tym udziało się za łat
to żyto przy pomienionych Żydach o żadnej dalszej mowie
nie wiem jaką między sobą zmowę mieli. Ultra nihil.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 64,
        "numer_pozycji": "64",
        "strona_pagina": "fol. 30r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Dekrety i roty przysiąg",
        "osoby_podmioty": "Huczek Dawidowicz (kupiec, aktor), Stanisław Maziarczyk (pozwany), Kazimierz Maziarczyk, Wawrzyniec Radzik, Kazimierz Koza, Matyjasz (szwagier), Marcin Pielka [?], Bartłomiej [Mierzwa?], Matyjasz Biernat",
        "kwoty_podatki": "8 garncy wódki, 9 spustów wódki; 33 gr, 4 gr 8 szel., siekiera",
        "opis_sprawy": "Cztery dekrety Sądu Wójtowsko-Ławniczego z 26 X 1701 r.: (1) rota przysięgi Stanisława Maziarczyka w sporze z kupcem Huczkiem Dawidowiczem o wyrób wódki i oddanie 9 spustów; (2) dylacja w sprawie Kazimierza Maziarczyka z Wawrzyńcem Radzikiem o grunt; (3) nakaz oddania siekiery i groszy w sprawie Kazimierza Kozy przeciw szwagrowi Matyjaszowi; (4) sprawa Bartłomieja przeciw Matyjaszowi Biernatowi o żyto z brogu i szkodę w słomie.",
        "transkrypcja": """--- Skan #64 (fol. 30r) ---
W sprawie y Akciej między Uciwym Huczkiem Dawido-
wiczem Kupcem Obywatelem Krasnickim z iedney Aktorowie a
Uciwym Stanisławem Maziarczykiem Mieszczaninem Krasnickim
z drugiej strony względem pretensiej pewnych które w protes-
tacyi specyfikowane są. Na skargę y odpowiedź Sąd niniejszy
Bliżej pozwanego do Odprzysiężenia w te rothę.
Ja przysięgam Panu Bogu Wszechmogącemu w Troycy
Jedynej że ia z tego Kondwinu świadomsie wyrobić nie by-
łoby ośm garniec z nowego naypierwszego targu tylko mi
Huczek Dawidowicz dobrowolnie pozwolił zalać y tey wódki
którey wyniść mogło w dobre kontentować obiecał Na którą
oddałem mu Spustów dziewięć wódki y nie więcey prze[s]tem
całym, ale zaś to co żyto na ten czas wydało z siebie byłem
oddał Tak mi Panie Boże dopomóż męka iego święta
Którą przysięgę w poniedziałek przyszły zgodnym mnia
y sąsiadem odprawić powinien o staraniu tego Jura-
mentu eadem prima Juris zachowując obwiniony.

W sprawie y Akciej między Uciwym Kazimierzem Maziarzy-
kiem z iedney a Wawrzyńcem Radzikiem względem gruntu pew-
nego na przedmieściu z jednej stawać do poniedziałku termin zacho-
wany.

W sprawie y Akciej między Uciwym Kazimierzem Kozą Kraśniczaninem Aktorem
a Matyiaszem Szwagrem o starych Rzeczy gr 33 na sile siły
oddać pozwany winien cztery groszy ośm wydzielił po śmierci
Marcina Pielku[?] terazniejszego siekierę in instanti aby oddał.

W sprawie y Akciej między Uciwym Bartłomiejem [Mierzwa?] a Matyiaszem Biernatem [pozwanym?], aby Aktor żyto
wyszedł z brogu i siedmdziesiąt tegoż starego mu wyłożył swoją szkodę
w kradzieży obcy słomę powinien czego niedostanie
miedzy pozwanego powinien dosyć uczynić, Aktor zaś w trzeciey
miedzy [zaprowadzony?] aby ludzi wysadzili na umówie postulat ad
jurandum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 65,
        "numer_pozycji": "65",
        "strona_pagina": "fol. 30v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Sprawy sporne i zapis nieruchomości",
        "osoby_podmioty": "Jakub Lis (przedmieszczanin), Sobestian Sąsadek, Wojciech Suchek [?], Maciej Sokołowicz [?], Wojciech Misowicz [?], Wawrzyniec Kraśnicki, Jan Brawowski, Stefan Ciesielski (ławnik), Jadwiga Ciesielska, Maciej Nowacki, Ewa Nowacka",
        "kwoty_podatki": "Brak (kwota na fol. 31r)",
        "opis_sprawy": "Sesja z 4 XI 1701 r. (sprawa Jakuba Lisa z Sobestianem Sąsadkiem o zagrodę, manifestacja Macieja Sokołowicza, kontumacja Jana Brawowskiego na instancję Wawrzyńca Kraśnickiego) oraz sesja z 7 XI 1701 r.: początek zapisu sprzedaży placu i budynku przez ławnika Stefana Ciesielskiego z żoną Jadwigą małżonkom Maciejowi i Ewie Nowackim.",
        "transkrypcja": """--- Skan #65 (fol. 30v) ---
Actum Coram Officio Advocatiali et Scabinali Crasnicensi
Feria Sexta post Festum Omnium Sanctorum proximo
Anno Domini Millesimo Septingentesimo Primo.

W sprawie y Akciej między Uciwymi Jakubem Lisiem Przedmieszczani-
nem Krasnickim Aktorem a Sobestianem Sąsadkiem zenie
Woyciechem Suchkiem[?] Ojcem o zagrodę Uczyniony zgody
z towarzysza Sąd nakazał aby ludzi wysadzić strony jako się zgo-
dziły idque prima Juris termin zachowany Actorom comparend.

Uciwy Maciej Sokołowicz[?] contra Woyciecha Misowicza[?] suum
protestatur de Calumniatione sui Manifestatur de diligen-
tia. Za attentować terminu sobie danego.

Na Instanciu Uciwego Wawrzyńca Krasnickiego Uciwy Jan
Brawowski 3tio Contumax respectu długu pewnego nie wydał.

Actum Coram Officio Advocatiali et Scabinali Cra-
snicensi Feria Secunda Ante Festum Sancti Mar-
tini Pontificis proxima Anno Domini millesimo se-
ptingentesimo Primo.

Przed Urzędem y Aktami niniejszemi Woytowskimi y Ławni-
czemi Krasnickiemi w osobach swoich stanąwszy Uciwi
Stefan Ciesielski Ławnik Krasnicki y Jadwiga mał-
żonkowie Jasnie iawnie dobrowolnie zdrowi na umysłach
zeznali praesentibus że zdawna z żoną swoią własną
nikomu nie zadłużoną na sobie obliguiąc y nadobno
swoią własną y teraz na potomki mający dziedzicznym
tytułem przepisuią Uciwemu Maciejowi Nowackiemu mieszczaninowi
y Obywatelowi Krasnickiemu y Ewie małżonkom ich
sukcessorom specyfikowane dobra Plac y""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 66,
        "numer_pozycji": "66",
        "strona_pagina": "fol. 31r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Sprzedaż nieruchomości i oblata testamentu",
        "osoby_podmioty": "Stefan Ciesielski (ławnik), Maciej Nowacki, Anna Jarzykowa, Wojciech Jarzyk (przedmieszczanin), Stanisław Jeżewicz [?] (burmistrz), Józef Madejczyk (ławnik)",
        "kwoty_podatki": "45 złp (cena sprzedaży budynku i placu)",
        "opis_sprawy": "Dokończenie rezygnacji budynku i placu przez Stefana Ciesielskiego dla Macieja Nowackiego za 45 złp. Następnie pod tym samym aktem (7 XI 1701 r.) Anna, małżonka Wojciecha Jarzyka, w asystencji burmistrza Stanisława Jeżewicza i ławnika Józefa Madejczyka oblatuje testament Wojciecha Jarzyka.",
        "transkrypcja": """--- Skan #66 (fol. 31r) ---
domostwie wedle przedpomienionego Pana Stefana
Ciesielskiego Ławnika Krasnickiego utrzymany na którym
gruncie swoim kosztem Budynek in suo esse zbudowali
przeciwko Kupcom sprzedaią Za Summę złotych
czterdzieści y pięć polskich z których odebrania prze-
d Urzędem kwituią y z nichże Intromissię w też
dobra dopuszczaią ad resignandum zaś tychże dobr
specyfikowanych e gremio Officii eiusdem Advo-
catialis seniorem vel eius proxime assidentem
natychmiast nie sobie prawa według używania
nie zostawuiąc ani excepuiąc wszelkie prawo
sworne rezygnuią i kładą do własności uczciwości
vinculando alias in forma iuris inferioris quam
plenissima et perfectissima.

Sub eodem Actu
Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
Krasnickich w osobach swoich stanąwszy Uciwi
Anna Uciwego Woyciecha Jarzyka Przedmieszcza-
nina Krasnickiego małżonkowie in assistentia
Sławetnego Pana Stanisława Jeżewicza[?] Burmistrza
Krasnickiego ad praesens rezydującego Józef
Madejczyk Przedmieszczanin Krasnicki ad
hunc Actum oblatował testament Uciwego
Woyciecha Jarzyka Przedmieszczanina Krasnickiego
primo voto żony iego oblatuiący testament w""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 67,
        "numer_pozycji": "67",
        "strona_pagina": "fol. 31v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Testament (oblata)",
        "osoby_podmioty": "Wojciech Jarzyk (testator), Anna Jarzykowa (żona), Mateusz Anisarek [?] (wierzyciel), Marcin Chleb (poprzedni właściciel gruntu), Zofia (pierwsza żona)",
        "kwoty_podatki": "32 złp (dług Mateuszowi Anisarkowi), 436 złp (kupno gruntu od Marcina Chleba przed 40 laty)",
        "opis_sprawy": "Pierwsza część testamentu Wojciecha Jarzyka: dyspozycja pogrzebu na cmentarzu kościoła kraśnickiego (3 msze żałobne, jałmużna dla ubogich), wyznanie długu 32 złp Mateuszowi Anisarkowi oraz historia kupna gruntu przed 40 laty od Marcina Chleba za 436 złp i wzniesienia na nim domu ze stodołą.",
        "transkrypcja": """--- Skan #67 (fol. 31v) ---
woli którego tenor ma się tak. W Imię Pańskie Amen.
będąc ja na zdrowym umyśle będąc Uciwy
Wojciech Jarzyk Przedmieszczanin Krasnicki
Lubo na ciele słaby na umyśle iednak zdrowy bę-
dąc choroby w starości swoiej od Boga Nawiedzony nie chcąc
dobrze y według należytości świata swego z ziemią Boga
wszechmogącego a na śmierć na krótkie ślepiący niczego
się nie spodziewaiąc tymże skoro do tego się nie przygotuie
pójdzie za czym duszę swoię w rąk Bożych oddaię
Ciało swoie pospolitej Ziemi które aby na Cmentarzu koś-
cioła Kościoła Krasnickiego pochowane było Na którego pochowa-
nie duszę swoię przy ciele trzech Mszy Świętych żałobnych y o-
fiary dla Ubogich na Ubogą Majestatu Boskiego za
grzechy swoie zlecam, te fundusze w ręce żony swoiey An-
nie na pochowanie ciała swego i dziadów dla Ubogich według
przepomożenia. 6to te że Zeznawam żem Winien Mateuszowi
Anisarkowi[?] złotych trzydzieści dwie aby mu oddana była
przez żonę obliguię się że Żadney swoiej więcey długów nie wi-
nienem nikomu też także nie winien 7mo Zeznawam
wolą moią Ostatnią Iżem gront ten z pierwsze kupił
U Marcina Chleba przedmieszczanina Krasnickiego
pusty za który dałem czterysta złotych trzydzieści y sześć
których iest temu lat Czterdzieści. Na tym gruncie swoim ko-
sztem budowałem tak mieszkanie iako y stodołę z żoną
swoią spłodzoną z pierwszą żoną która dzieci nie miała iednego
syna z domu Zofia z gront pomieniony że w żadnej wyro-
bie nie mam Żeki dziewiętnaście lubom był niepomny
żem to dom kupił wszystek Uchodzę precz do żony""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 68,
        "numer_pozycji": "68",
        "strona_pagina": "fol. 32r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Testament (oblata)",
        "osoby_podmioty": "Wojciech Jarzyk, Anna Jarzykowa (żona), Jadwiga (córka z 1. żony), Matyjasz Kudrel, Józef i Andrzej Jarzykowie (synowie z Anny), Adam Sobek (sąsiad), Stanisław Jeżewicz (burmistrz), Józef Madejczyk (ławnik)",
        "kwoty_podatki": "12 złp",
        "opis_sprawy": "Zakończenie testamentu Wojciecha Jarzyka: zapis dożywocia żonie Annie, sukcesja synów Józefa i Andrzeja (oraz wzmianka o córce Jadwidze i Matyjaszu Kudrelu), opis ćwierci roli w ulicy przy Adamie Sobku oraz powierzenie egzekucji testamentu burmistrzowi Stanisławowi Jeżewiczowi i ławnikowi Józefowi Madejczykowi.",
        "transkrypcja": """--- Skan #68 (fol. 32r) ---
Żeby po śmierci na ten czas były to podług tego
Które się dzieci żoną pierwszą z żoną Anną na Imię
Jadwigą między Uciwego Matyasza Kudrela sako[?] z pierwszą
gront w gront ma być grunty z tejże że zeznawam iż mi dał
żona suknia pomieniony Nieboszczyk y onychże żona Anna
która kupowała na ten czas złotych dwanaście y to od tego
gruntu pochodzi pieniędzy żadnych nie mam, dobra wszystkie
które mi Pan Bóg dał mianowicie pomienionej żonie swej
w dożywociu Żonie swoiey Wdowie niechay po śmierci
Na synów Józefa y Andrzeia moich z nią spłodzonych
spadać powinny ieżeli się zgadzać z nią będą między sobą
wolne im używanie z tych dóbr ieśliby zaś woleli ieżeli
zaś nie będą się zgadzać to wolno tejże żonie a matce ich
tem dobrem dysponować iako chce z Bożą y dobrą
także że dziatek Bóg nam dał przy chałupie żonie
całej O wymiernym kupnie Czwierci rolej w ulicy
iest Adam Sobek z tejże ziemi miedzy pomienionego
mała rola przedawnego Zakopie[?] lunow[?] tej woli
ostatniej moiej żonie y dziatkom na znacznym Sławetnym
Panu Stanisławie Jeżewiczu Burmistrzu Krasni-
ckiego Ławnika Józefa Madejczyka Proszę ich dla
miłości Boskiej aby we wszystkim po śmierci mojej roz-
porządzili tak pochowanie ciała mego iako y dóbr
przestrzegali krzywdy żonie mojej y dzieciom mo-
im nie dopuszczali na to aby naywyżej według
możności pochowane było, oświadczam dla Boga sprawiony
wiarą ich niebiańską. J.J.K.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 69,
        "numer_pozycji": "69",
        "strona_pagina": "fol. 32v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Areszt na domu żydowskim i dekret",
        "osoby_podmioty": "Franciszek Sosnowski (woźny przysięgły), Lewek Moszkowic (szkolnik synagogi kraśnickiej), Andrzej Rzędecki (administrator klucza), Doktor (Żyd), Josek Moszkowic (obywatel kraśnicki), Sebastian Krawiec (dworzanin kasztelana lubelskiego), Katarzyna Chudzikowa (wdowa, winiarka)",
        "kwoty_podatki": "400 złp (areszt na domu Joska Moszkowica)",
        "opis_sprawy": "Sesja z 9 XI 1701 r.: (1) relacja woźnego Franciszka Sosnowskiego i szkolnika Lewka Moszkowica z aresztu sumy 400 złp na domu Joska Moszkowica na rzecz Sebastiana Krawca (z dworu kasztelana lubelskiego) oraz Doktora Żyda; (2) początek procesu winiarki Katarzyny Chudzikowej z Joskiem Moszkowicem o dzierżawę wódki i komplanację z 1700 r.",
        "transkrypcja": """--- Skan #69 (fol. 32v) ---
Actum Coram Officio Advocatiali et Scabinali Crasnicensi
Feria Quarta Ante Festum Sancti Martini Pontificis
proxima Anno Domini Millesimo Septingentesimo Primo.

Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
Krasnickich w osobie swoiey przyszedłszy Opatrzny Franciszek
Sosnowski Woźny authentyczny Obywatel Krasnicki i z Nie-
wiernym Lewkiem Moszkowicem Obywatelem Szkolnikiem synagogi
Krasnickiey, in Vim suae verae ac fidei relationis sponte
palam publice libereque Recognoverunt Iż Oni ex Officio
za requizycją od Imci Pana Andrzeja Rzędeckiego Admi-
nistratora Klucza Krasnickiego, względem Doctora Żyda tu-
teyszego Synagogi Krasnickiey y z sumy złotych polskich
czterysta Jidelskich monety w koronie idącey na pewny dom
Niewiernego Żyda Joska Moszkowica w Kraśniku in
tuito długu pewnego Panu Sobestianowi Krawcowi na
dworze u Jaśnie Wielmożnego Jegomości Pana Kasztelana Lubelskiego
przychodzącego aby tey summy aresztowanej sąd kazał
pieniądze grunt z widłami z resztą opisanemi nie wydawał
do decyzyi dalszej de quo praesens relatio.

W sprawie y Akciej między Uciwą Katarzyną Chudzikową
wdową winiarką Krasnicką Aktorką a Niewiernym Jos-
kiem Moszkowicem Obywatelem Krasnickim przed Sąd
Jegomości Pana Andrzeja Rzędeckiego Administratora
Klucza Krasnickiego przypozwanym, na skargę iest
podaną y odpowiedź daną Pomieniony JegoM. Pan
Administrator Panowie Urzędnicy Wysłuchawszy y one zro-
zumiawszy decydował Quantum attinet Komplanacyi
między stronami nabytej de Actu Feria Quarta Ante
Festum S. Hedvigis AD 1700 względem preten-
siey w tę Komplanacyą wyrażonych poniewaz
kontrowersya nie zachodzi, onę ani żadney probie""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 70,
        "numer_pozycji": "70",
        "strona_pagina": "fol. 33r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Wyrok i rezygnacja nieruchomości",
        "osoby_podmioty": "Katarzyna Chudzikowa, Josek Moszkowic, Jadwiga, Zuzanna, Franciszek Tatarski (woźny przysięgły), Adam Michał Chmielowic (pisarz miejski przysięgły), Andrzej Rzędecki (administrator klucza), Jan Sokołowicz [?]",
        "kwoty_podatki": "3 grzywny (kara), 4 złp 20 gr",
        "opis_sprawy": "Zakończenie wyroku w sprawie Chudzikowej z Joskiem Moszkowicem (przysięga, kary po 3 grzywny, 4 złp 20 gr dla Zuzanny). Następnie relacja woźnego Franciszka Tatarskiego i pisarza miejskiego Adama Michała Chmielowica o rezygnacji i intromisji domu z budynkami obok posesji Jana Sokołowicza.",
        "transkrypcja": """--- Skan #70 (fol. 33r) ---
stąpić nie może Sądem swoim approbować domagają się w tym
obiedwie strony Quo vero spectat Dzierżawy wódki od tej
wdowy nie oddanej nad tę Komplanacyę ponieważ do-
kumentu nie ma y o szkodzie od przysięgi ma się Aktor
wynaleźć inquantum iuramentum Który w poniedziałek
przyszły być ma powinna Iż niewinna tey Wódki y nie iest
dziedzic y przyczyny nie oddania Quo vero spectat spuściła
Gospodynia, Ponieważ Prawo przypisane za porycie ogroda
śmierci zaś dla mierzenia Stodół oddać nie mogła y meno
że od tey Uwłoki Sądem swoim Atestem przydany ważyć
prywatnie sobie Aktorkę aby zaś o inną szkodę dać przymus
z tey każdej stronie trzy grzywny trzy, Który przysięgać atto-
nować powinien Jadwiga podania sądowego Zuzanna
wskazanej przysięgi Różnych powinien podany oddać złotych
cztery groszy dwadzieścia z obydwu stron oświadczyć może od tych pita-
niami oskarzony wolny został decreta praesentis vigore.

Sub eodem Actu
Do Urzędu y Akt niniejszych Woytowskich y Ławniczych Kra-
snickich w osobach swoich przyszedłszy Opatrzny Franciszek
Tatarski Woźny authentyczny Obywatel Krasnicki, Adam Michał
Chmielowic Pisarz Miejski Krasnicki przysięgły sponte palam
et publice libere Recognoverunt Iż Oni z Consensu Jegomości
Pana Andrzeja Rzędeckiego Administratora Klucza Krasnickiego
z tradycji Urzędu Oboyga Krasnickiego Dom Ciudobiet[?] /
Plac quondam nazwany z budynkami na tymże
placu będącemi Sławetnymi, iako Inwentarz opiewa rezygnacyą
opisaną rezygnowali kupiony y sprzedany tych dóbr kuwrys[?] pomie-
nionych między miedzami siedzącymi P. Jana Sokołowicza
z drugiej strony Obywatelów Krasnickich, leżąc w obu stronach""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 71,
        "numer_pozycji": "71",
        "strona_pagina": "fol. 33v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Intromisja i zapis na dobrach",
        "osoby_podmioty": "Jachym Chapon [?], Josek Moszkowic (nabywca), Stanisław Dudek (syn), Wawrzyniec Dudek (ojciec, zmarły), Zofia z Jantunów [?] Dudkowa (matka), Ewa (wdowa), Szymon Struski (sąsiad), Wojciech Kuropka",
        "kwoty_podatki": "1000 złp (cena zakupu domu przez Joska Moszkowica)",
        "opis_sprawy": "Dokończenie wwiązania (intromisji) Żyda Joska Moszkowica w dom zakupiony za 1000 złp po publicznym trzykrotnym wywołaniu. Następnie sesja z 14 XI 1701 r.: początek zapisu Stanisława Dudka (syna Wawrzyńca i Zofii Jantunówny) dotyczącego roli na polach podleskich przy Szymonie Struskim, obciążonej zastawem u Wojciecha Kuropki.",
        "transkrypcja": """--- Skan #71 (fol. 33v) ---
Miejscowych Brata Jachymów Chaponiów Drawidowych y
przez Niewiernego Joska Moszkowica Obywatela Krasnickiego
z winnymi długi sprzedanych Za Summę Złotych Tysiąc Pol-
skich Monety w Koronie idącey, przedanym z ratyfikacją
plenis fontibus Voce sonora et intelligibili per spatium
horae trium horarum generatum, wezwał aby każdey stronie
którą ieżeli się nayduie do pomienionych dóbr lubo summy
wyłożoney Nunc et instanti odzywali się Którzy że się nie
odzywali libere w też dobra ad palmam eiusdem eatenus
Officii Intromissia w też dobra condescenduiąc Kupcowi confero-
wać nie deneguią alias in forma publicatae resignationis
de Intromissione facta quam plenissima et perfectissima.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi
Feria Secunda post Festum Sancti Martini Pontificis proxima
Anno Domini Millesimo Septingentesimo Primo.

Przed Urzędem y Aktami niniejszemi Woytowskiemi y Ławniczemi
Krasnickiemi w osobie swoiey stanąwszy Stanowisty Uczciwy Stanisław Du-
dek niegdy Uczciwego Wawrzyńca Dudka przedmieszczanina
Krasnickiego z Zofią z domu Jantunówną[?] wiecznemi mał-
żonkami spłodzony Syn swoiem y Consuccessorów swoich
Imieniem iasnie iawnie dobrowolnie zeznaiąc praesentibus zeznaie
Iż On Naturalnym Successorem będąc chleba i z długu żon
pewny mianowicie Ręką roli między miedzami siedzący Uci-
wey Ewy wdowy z drugiej strony Szymona Struskiego
Przedmieszczan Krasnickich na podleskich polach po długiej
ciąży od gościnca podleskiego do Jereszkowej granicy iako
y inne niwki znayduiące się sobie y Consuccessorom swoim prawem
naturalnym dziedzicznym należących Uciwemu Wojciechowi Ku-""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 72,
        "numer_pozycji": "72",
        "strona_pagina": "fol. 34r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Umowa sprzedaży roli i fundacja zakonna",
        "osoby_podmioty": "Wojciech Kuropka, Stanisław Dudek, Ludwika Salomea Zamoyska (księżna), Konwent Panien Zakonnych w Kraśniku, Tomasz Anczarek (nabywca), Górski",
        "kwoty_podatki": "120 złp (zastaw u W. Kuropki), 120 złp (dług konwentowi), 240 złp (cena sprzedaży: 70 złp zaliczki + 170 złp reszty)",
        "opis_sprawy": "Dokończenie zapisu Stanisława Dudka: rola obciążona 120 złp u Wojciecha Kuropki oraz 120 złp długu na rzecz fundacji księżnej Ludwiki Salomei Zamoyskiej w Kraśniku zostaje sprzedana Tomaszowi Anczarkowi za 240 złp (70 złp wypłacono od razu, 170 złp pozostaje na gruncie do św. Wojciecha 1702 r.).",
        "transkrypcja": """--- Skan #72 (fol. 34r) ---
ropkowi mieszczaninowi Krasnickiemu przed kościołem zasta-
wionego summy złotych sto dwadzieścia polskich rodnego zacią-
gnionego Na którego z niesieniem tenże zeznawaiący zacią-
gał długu pierwszego z Kaypczynie[?] obecnym w Bogu Dziecię
Panny Ludwiki Salomei Zamoyskiey Xiężney fundacyi przy
tutejszym Mieście Krasniku leżącey Summy złotych polskich
sto dwadzieścia Którey summy nie mogąc oddać Na czas na
znaczony we długu zaciągi swoiey Jasnie Jawnie dobrowolnie
zeznał praesentibus zeznaie Iż On Ułatwiaiąc trudności wspis
tłoczącego pomienionego grontu na którym y chałupka
stoi Uczciwemu Tomaszowi Anczarkowi Przedmieszczaninowi
Krasnickiemu y małżonce iego Kupno wieczne tychże
dóbr wzwysz specyfikowanych iako to obyczaiów wszystkich
Submittuie się przedać za Summę złotych polskich dwie-
ście czterdzieści polskich Na którą summę ad rationem bie-
rze złotych siedmdziesiąt polskich, summam złotych
sto siedmdziesiąt polskich na tymże gruncie przy
pomienionych Anczarkach małżonkach zostawać będzie
do doskonalszego Urzędu na zapisie przed Successorów
wszystkich principaliter Dobra iednak wszystkie successores
do Czasu święta świętego Woyciecha Roku przyszłego
1702 przypadaiący inquantum zapisu nie zeznaią
na też dobra wzwysz pomienione mocni będą Ci Anczar-
kowie za tym obligiem Intromissią w dobra referować y w nich
następować ponieważ tamciem Otrzymałe One tylko
na Gorskim około tegoż domu summę przysposobić zostawili
Waruią sobie pomienieni Anczarkowie małżonkowie
ieżeliby im zapisu zeznać nie chcieli pomienieni syn""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 73,
        "numer_pozycji": "73",
        "strona_pagina": "fol. 34v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Sekwestr, jurament i sprawy sporne",
        "osoby_podmioty": "Stanisław Dudek, Tomasz Anczarek, Berek (Żyd, aktor), Maciej i Jan Skarczykowicowie [Skarżykowie?] Dąbrowscy, Katarzyna Rudzikowa (wdowa), Jan Snopek, Tomasz Nowak, Józef Jędrych",
        "kwoty_podatki": "50 złp",
        "opis_sprawy": "Zakończenie umowy Dudka z Anczarkiem, sekwestr sądowy przeciw Maciejowi i Janowi Skarczykowicom Dąbrowskim na instancję Żyda Berka oraz uwolnienie wdowy Katarzyny Rudzikowej od przysięgi. Następnie sesja z 16 XI 1701 r.: termin między Janem Snopkiem a Tomaszem Nowakiem oraz początek sprawy Józefa Jędrycha.",
        "transkrypcja": """--- Skan #73 (fol. 34v) ---
y synowie na czas naznaczony aby summy teraz wyłożoney
nie odbierał aż po trzech latach may zabrać z czego
ciey gdyżby tę summę złotych pięćdziesiąt przytaczyszy
do nich nie mogli sobie gdzieindziej kupić a nie dobra
lubo tę summę iako chcieli za bożą pomocą fortuny
zażyć czynsz tego wierny zatrzymany successorowie spła-
cić y oddać powinni złotych polskich dla której bardziej wiaro-
gładności podpisuią.

Sub eodem Actu
Ad Instantiam Infidelis Berek H. H. Mathia et Joannes Skar-
czykowie Dąbrowski citati 2do quarto Vice Conti-
maciae debiti decrevit sequestratio.

Sub eodem Actu
Uciwa Katarzyna Rudzikowa Wdowa Jurament Na na-
czony wyż komuś u libera a praestando Juramento.

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Quarta post Festum Sancti
Martini Pontificis proxima die decima sexta
Novembris Anno Domini Millesimo Septingen-
tesimo Primo.

W sprawie y Akciej między Uciwym Janem Snopkiem Przed-
mieszczaninem Krasnickim Aktorem z iedney a Tomaszem
Nowakiem od tej strony za sprawą przychodzący Aktorom
aby załataną krzywdę sobie uczynili z obowiązku na
przyszły Piątek stanęli ieżeli się nie pojednaią nie
będąc sobie należyto sądu Obywateli termin zawity
stronom.

W sprawie y Akciej między Uciwymi Józefem Jędrychiem
synem matki iego Aktorem z iedney a Uciwym Grzegorzem""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 74,
        "numer_pozycji": "74",
        "strona_pagina": "fol. 35r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Dekret i aprobacja zapisu",
        "osoby_podmioty": "Józef Jędrych, Grzegorz (brat), Jakub Wójcikowic, Zofia (wdowa po Adamie Ziębie), Bractwo Różańca Świętego, Zofia z Jantunów Dudkowa (matka), Wawrzyniec Dudek (zmarły), Franciszek Dudek (syn), Stanisław Dudek (syn), Tomasz Anczarek",
        "kwoty_podatki": "3 talary (zastaw krzyża do Bractwa Różańca Świętego)",
        "opis_sprawy": "Dokończenie dekretu w sprawie Józefa Jędrycha z bratem Grzegorzem oraz dekret w sprawie Jakuba Wójcikowica przeciw wdowie po Adamie Ziębie Zofii o zwrot zbroi miejskiej i 3 talarów dla Bractwa Różańca Świętego. Następnie aprobacja umowy Stanisława Dudka z Tomaszem Anczarkiem przez matkę Zofię Dudkową i brata Franciszka Dudka (podpisy krzyżykami).",
        "transkrypcja": """--- Skan #74 (fol. 35r) ---
swym bratem o starych kopcem rękoma zaniesioną iżby
mu oddali suknia boża pukiera[?] ostatnie nakazał aby
prawnie posłali aby oddali Aktorowi, o rzeczy ze zbóż y
niech zawsze przegra ponieważ nienależnie pożwań wolne
pozwanie filia Aktorom decrevit każdemu piątek.

W sprawie y Akciej między Uciwym Jakubem Wójcikowicem Oby-
watelem Krasnickim Aktorem a Uciwą Zofią wdową Adama
Zięby małżonką, Za prośbą iednak z obu stron ostawaią
na pierwszem reiestrze strony przy którym sporze stoi z wdową
żona. Aktor o Żołnierki nie może się iakim sposobem prawo
na ubycie ogólnie mieć także z urzędu ma do sekwensu oddać
za pożyczenia zbroi miejskiego przedtem trzy talarów do
Bractwa Różańca Świętego którego krzyż założyła aby
im stało.

Sub eodem Actu
Przed Urzędem y Aktami niniejszemi w osobach swoich
stanąwszy Uciwa Zofia z domu Jantunówna niegdy
Uciwego Wawrzyńca Dudka przedmieszczanina Krasnickiego
małżonka pozostała wdowa Matka y Franciszek
Dudek syn spłodzony iasnie iawnie dobrowolnie ze-
znali Iż Oni submissią zapisu Uciwego Stanisława
Dudka Matki syna Brata bratu na stronę Uciwego
Tomasza Anczarka Przedmieszczanina Krasnickiego
małżonki y successorów de Acto w poniedziałek
po św. Marcina Biskupa Roku teraźniejszego
uczynioną approbuią we wszystkim za dobrze i oną czynią
gotową Obliguiąc się alias in forma approbationis
Inseronis Ipsis quam plenissima et perfectissima
nie umiejący pisać znakiem krzyża świętego podpisali
się Zofia Jantunówna + + Franciszek Syn.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 75,
        "numer_pozycji": "75",
        "strona_pagina": "fol. 35v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1701",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Obdukcja ran i protestacja",
        "osoby_podmioty": "Tomasz Zięba (przedmieszczanin), Maryna Ziębina (żona), Walenty Chrzanowski (poddany ze wsi Rudnika), Pan Bielski (dziedzic Rudnika)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Protestacja i obdukcja ran przedmieszczanina Tomasza Zięby oraz jego żony Maryny przeciw pracowitemu Walentemu Chrzanowskiemu z Rudnika (poddanemu p. Bielskiego), który 11 XI 1701 r. na drodze do Sadkowiska ciężko pobił Ziębę brzeszczotem (szablą) i kijem po upomnieniu się o dług. Na dole strony początek kolejnej sesji z 23 XI 1701 r. (środa przed św. Katarzyną).",
        "transkrypcja": """--- Skan #75 (fol. 35v) ---
Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
Krasnickich w osobie swoiey przyszedłszy Uciwy Tomasz Zięba
Przedmieszczanin Krasnicki swoim y Uciwej Maryny małżon-
ki imieniem solennie z wielkim żalem protestował się prze-
ciwko Pracowitemu Walentemu Chrzanowskiemu ze wsi
Rudnika Poddanego Jegomości Pana Bielskiego Oto Iż On za-
pomniawszy boiaźni Bożey y miłości bliźniego lekkie sobie
ważywszy prawo przeciwko gwałtownikom pokoju
pospolitego mianowicie garmańskiego poważył się prote-
stanta na drodze dobrowolnej idącego do Sadkowiska
że mu się upomniał w dobry sposób o dług swoy którego
bez mała czas oddać nie chciał y owszem za przyznanie
iego dóbr tymi słowy onego bił y szturkował osobliwie
o Dzień Piątkowy święta Świętego Marcina Roku teraźniej-
szego nie tylko żonę protestanta która z wielkiego szamotania
chora leży ale y samego do Ustronia piechotą idącego z tey
tylko okazyi bronią Brzeszczanta mieszka swego zbił y stukł
Ktorych że ran y sinizn protestans ostensionem pokazał Naprzód
na lewe ramię prawe wszystko stłuczone spuchłe sino
zarosłe Item Pod łokciem na prawey ręce spuchły
od dłoni w szerz y wzdłuż Item po wierzchu teyże ręki prawej
wszystkiej spuchłą Item palec ręki prawej stłuczony także
wszystkie potłuczone sine spuchłe Item z tejże strony na
bok prawy liche od Uderzenia Item Na lewej ręce na
łokciu za skrócony stłuczony spuchły cały y na prawey od dłoni
Item nad brwią głaz nad okiem prabionem Krwawy o słonku
pasa wzdłuż wzier o półtora łokcia Item a przedtemże bity
na plecy od suchych kijów Offerens se praesentibus ad jurandum
Velle Volentas.

Actum Coram Officio Advocatiali et Scabinali Cra-
snicensi Feria Quarta Ante Festum Sanctae Catha-
rinae V et M proxima Anno Dni 1701.""",
        "link_swa": UNIT_LINK
    }
]

main_data.extend(part3_scans)
assert len(main_data) == 75, f"Expected 75 scans, got {len(main_data)}"

with open('/home/ubuntu/workspace/Gen/main_data_j18_part3.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j18_part3.json: {len(main_data)} skanów.")
