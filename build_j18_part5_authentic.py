# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j18_part4.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989891"

part5_scans = [
    {
        "nr_skanu": 101,
        "numer_pozycji": "101",
        "strona_pagina": "fol. 49r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Oblig i zeznania świadków",
        "osoby_podmioty": "Jan Grymus (mieszczanin), Tomasz Konny (obywatel kraśnicki), Marianna Przemieniecka (panna), Kazimierz Koszykowic, Paweł Nowacki (świadek), Wojciech Piasecki, Pielaszkowic (prokonsul), Anna Kępina (żona Jana Kępy, świadek), Maryna (chłopianka, świadek)",
        "kwoty_podatki": "150 złp (submisja Jana Grymusa)",
        "opis_sprawy": "Sesja z 23 I 1702 r.: submisja Jana Grymusa na 150 złp dla Tomasza Konnego z dóbr panny Marianny Przemienieckiej oraz zeznania świadków na instancję Kazimierza Koszykowica (Paweł Nowacki, Anna żona Jana Kępy, Maryna chłopianka Piaseckiego) w sprawie bójki i gróźb ze strony Wojciecha Piaseckiego.",
        "transkrypcja": """--- Skan #101 (fol. 49r) ---
Actum Coram Officio Advocatiali et Scabinali Crasnicensi
Feria Secunda postridie Festi Sanctae Agnetis Virginis
et Martyris Anno Domini Millesimo Septingentesimo Secundo.

Przed Urzędem y Aktami niniejszemi w osobie swojej stanąwszy
Uciwy Jan Grymusa Mieszczanin tuteczny Krasnicki Submittował
się Tomaszowi Konnemu Postroznemu[?] Kuncowi Obywatelowi Krasnickiemu
złożyć złotych sto pięćdziesiąt polskich za sukces które pod wolną execucją
na siebie bez żadnego prawa przewodu oddać na czas y święto Panny
Maryey Gromnicznej Roku teraźniejszego, na sobie podpisuie
Jan Grymusa.

Testes ex Parte H. Casimiri Koszykowic
1us Testis H. Paulus Nowacki Recognovit haec formalia
W niedzielę przedtem skoczyło przed sobą y Wojciech Pia-
secki, zszedł się z żoną swoją przed Panem Pielaszkowi-
ca starego radce domem rzekła do niego żona tegoż
nie wiedzieć czemu zabieł nam Koszykowic prosię z ub-
mistowy rzekł to zabieł zabieł od rydzy dalej z żoną ku
drzwiom rzekł to na śmierć zabieł re proce rzekła żona
jeżeli tam żyje A on potym zeszła wobec przed tym zabieł
mi jedno zabieżeć mu dwoje w tym słowa weszły między
we ten pisu brat po żonki syn, dawno On komu bieda za bre
czynione.

2dus Testis Honesta Anna H. Joannis Kempa Consors Reco-
gnovit haec formalia Jadąc z Urzędowa z Jarmarku gadał
do ludzi Wojciech Piasecki komu to mówię zabiełem do
Szymona prośbę to słyszałam słyszała, Ultra nihil.

3tius Testis Marinus[?] Chłopiec z chaty syna Piaseckiego mówi
w izbie do Jana Kępy po słomie uźreliśmy zeza na dwór
płot ułożyliśmy tyż razem ku niemu a gospodarza""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 102,
        "numer_pozycji": "102",
        "strona_pagina": "fol. 49v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Inkwizycja świadków",
        "osoby_podmioty": "Jan Bieleszkowic [Bielaszkowic?], Kazimierz Koszykowic, Wojciech Piasecki, Marcin Cwikła [Cwieka?] (świadek), Szymon Olchowski (świadek), Maciek Szynkwas",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie inkwizycji w sprawie Kazimierza Koszykowica i Wojciecha Piaseckiego: zeznania Jana Bieleszkowica (świadka Koszykowica) oraz świadków ze strony Piaseckiego — Marcina Cwikły i Szymona Olchowskiego — opisujących kłótnię i uderzenie kuflem w szynku.",
        "transkrypcja": """--- Skan #102 (fol. 49v) ---
Drugi
4tus Testis H. Joannes Bieleszkowic Recognovit haec formalia
Podczas Nieszporu przedtem z Kościoła Koszykowicowa spytała
mnie i rzekłem nie widziałem w cale odpowiedziałem tam nie wi-
dział w kroć rano w zmowieniu się ku temu domowi na wro-
cie niego zamosobnoszedł Piasecki y dał mu w łeb towa-
rzysz wszystkich braciom śmiała p. tego onego a on
jest w domu y prosił mi zabieł wzdy goniła mego swego
y opowiedziałam o tym zabiciu Prostewatego On rzekł tak
idź sobie chcie zabieł mnie jedno w domu iutro dwoje zabieł będę
czego nie słyszałem.

Ex Utraque
1us H. Martinus Cwikła[?] Recognovit Wleźliśmy naprzód
z Zagojskim na piwo y siedzieliśmy U jednego końca
stołu taż też U drugiego stołu siedział Koszykowic z okna
U Szynkwasu Piasecki z Kuśnierzem siedzieli od drzwi koło
węgła, wstał w tym Koszykowic rzekł przeciwko Piaseckie-
mu porwawszy butów podał ku mnie a tak leciała szklanica
nie mam takiego grontu tak On nie mogąc po mnie iak się
stało dalej między niemi to tylko pamiętam że Koszyko-
wic zmierzał do Piaseckiego y dał mu od lew w łeb Chciał
się porwać Piasecki ale my bronili się bić w tym się było
nas poł to zmierzawszy ludźmi Piasecki pochwyciwszy
Koszykowica Uderzył się o ziemię My go też zasiedzi rze-
waliśmy Piaseckiego z Koszykowica tak go w czepisku
Szymon mówi Piasecki ponieważ tego chcesz o toć mo-
wa zabiełeś mi prosię a toś najpierwej się porwał
Koszykowic tak dostał iako y do bicia Ultra nihil.

2dus H. Simon Olchowski Ex Utraque Vi et Cwikła
to tylko przydał że Koszykowic wspominał o Ferdynandzie
y prosięciu Piasecki rzekł ponieważ tego chcesz to toś
mi zabieł, iedno ia tobie dwoje zabieł upił.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 103,
        "numer_pozycji": "103",
        "strona_pagina": "fol. 50r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Zeznania świadków i limitacja",
        "osoby_podmioty": "Józef Kosiński [?] (świadek), Kazimierz Koszykowic, Maciek Szynkwas, Wojciech Piasecki, Szymon Olchowski, Andrzej [?] (świadek)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie inkwizycji w sprawie Wojciecha Piaseckiego i Kazimierza Koszykowica (zeznania 3. i 4. świadka opisujących zajście w karczmie za Bramą na Przedmieściu). Na dole limitacja spraw oraz początek nowej sesji z 25 I 1702 r. (środa po św. Agnieszce).",
        "transkrypcja": """--- Skan #103 (fol. 50r) ---
3tius Testis Josephus Kosiński[?] ex parte Piasecki Recognovit
z Kamieńca Karczemki w przeszły tydzień siedział Koszy-
kowic z Macieiem u Szynkwasu My też zasiedli siedzieliśmy
w tym przyszedł Piasecki z Olchowskim poaresztowaliśmy
w tym Koszykowic Obaczywszy go zaczął mowę i tacy
wysłuchcie chcą słuchać od Macieja ale nie dam w poru
wszy upadł na Piaseckiego Słowy ten mówi przestań
taki że mu zabieł prosię dopiero Piasecki rzekł pone-
waż się odzywasz oto ia tobie dwoje zabieł w tym przyszedł
z stołu a Piasecki się umykał od niego iedno razą od lew
dał mu w łeb słowa nie dziwne rzekł na niego bo On okrutnie
y uchwaliliśmy żeby uderzenie złożyć ale szmych
byli a on przecie zgrzytał zębami palec grożąc na nie-
go Ultra nihil to powiedział że naprzód Maciek
dał Koszykowicowi okazję Piaseckiemu.

4tus Testis ex parte H. Piasecki siedzący przy piecu
na Ziółkiem[?] piliśmy piwo siedział Koszykowic
z Macieiem u szynkwasu już piwo poszedł mówić o ko-
tosztach dalej rzekł do Piaseckiego mówisz na
mnie żem ci wieprzaka zabieł rzekł Piasecki Boże nie
daj rzeczy nie mówiłem On przecie byś nie kurwiu
mać mówiąc zniechęcisz zabił dalej rzekł daj mi
opysk rzekł Piasecki Ależ w tym dał mu w łeb oba dwu
nie poczuć i to uderzenie o ziemię w tym ich rozwa-
dzili sąsiedzi Ultra nihil.

Limitatio Intercessit Causarum.
Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Quarta post Festum Sanctae
Agnetis Virginis et Martyris proxima Anno Domini""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 104,
        "numer_pozycji": "104",
        "strona_pagina": "fol. 50v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Protestacje i dekrety",
        "osoby_podmioty": "Kazimierz Koszykowic, Wojciech Piasecki, Marcin Cwikła, Jan Bieleszkowic, Kazimierz Zagojski, Matyjasz Dudarczyk, Pan Zieliński [?], Lawko Dawidowic (starozakonny), Andrzej Łancki, Szmul (starozakonny), Marcin Maziarczyk",
        "kwoty_podatki": "1 złp (spór Szmula z M. Maziarczykiem)",
        "opis_sprawy": "Sesja z 25 I 1702 r.: protestacja Kazimierza Koszykowica przeciw Wojciechowi Piaseckiemu o groźbę z fuzją; protestacja Marcina Cwikły, Jana Bieleszkowica i Kazimierza Zagojskiego przeciw Matyjaszowi Dudarczykowi; dekret w sprawie Lawka Dawidowica z Andrzejem Łanckiem o gliniany dzbanek; dekret w sprawie Szmula przeciw Marcinowi Maziarczykowi o 1 złp.",
        "transkrypcja": """--- Skan #104 (fol. 50v) ---
Millesimo Septingentesimo Secundo. Do Urzędu y Akt niniejszych
w osobie swoiej przyszedłszy Uciwy Kazimierz Koszykowic so-
lennie z wielkim żalem protestował się przeciwko Uciwemu
Woyciechowi Piaseckiemu Oto Iż On zapomniawszy Boiaźni
Bożey y miłości bliźniego także Ustaw na protestanta co
zawsze rujnować usiłuje nie respektując na to sprawę
z protestantem będący w potyczkach stawać powinien Chodnik
dnia wczorajszego świni dworze na ogrodzie swoim ze śru-
tową strzelbą próżno chodził jako się groził to wykonał
co iterum et iterum protestuie się.

Videatur hoc loco Protestatio facta Honestorum Martini
Cwikła, Joannis Bieleszkowic, Casimiri Zagoyski Contra H.
Mathiam Dudarczyk Suburbanum et eius Consortem, Iż Oni
z domu swego zakaz osobę nieznajomą osobę poważyli się
subordinować na zdradę protestantów jakoż de facto subordi-
nowali którę po odjeździe Jego Mci Pana Zielińskiego który
niebo chciał strzelać do protestantów gdy się mu odezwali
być sąsiadami On mieszkał spokojnie iednak inne takie
osoby wypadły z domu ich bili o co się protestują et abhinc
wolną drogą, offerendo se iniurias easdem Vindicaturum velle.

W sprawie y Akciej między Niewiernym Lawkiem Dawidowi-
cem Obywatelem Krasnickim Aktorem a Uciwym Andrze-
iem Łanckiem pozwanym o oddanie rzeczy ukradzionej dzbanek
miał gliniany który podczas pożaru zginął w którym przy-
bytym zginęło y płótno rzeczy Sąd niniejszy Necessa-
riam inquisitionem huius causae statuendo na dzień po-
zwanego y Trzecią prima Juris adinvenit officium.

W sprawie y Akciej między Niewiernym Szmulem Żydem Obywa-
telem Krasnickim Aktorem z jednej a Marcinem Maziarczykiem
pozwanym aby pozwany oddał złotych 1mo Aktorowi do Łatwienia
stanąć pod Zakładami takowej kwoty Karta pokazana nullitatis
powinna bydz decreti praesentis vigore.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 105,
        "numer_pozycji": "105",
        "strona_pagina": "fol. 51r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Ugoda o wolną ulicę na Górach",
        "osoby_podmioty": "Andrzej Łancki, Michał Kepka, Jakub Młynarczyk (przedmieszczanin), Wojciech Szabla (przedmieszczanin), Jakub Lis (przedmieszczanin z Gór), Sebastian Rodzonek",
        "kwoty_podatki": "12 złp (opłata za ulicę na Górach)",
        "opis_sprawy": "Sesja z piątku po Oczyszczeniu NMP 1702 r. (3 II 1702): dekret między Andrzejem Łanckim a Michałem Kepką o zasługi; oraz ugoda między Jakubem Lisem z Gór a Sebastianem Rodzonkiem w obecności rozjemców Jakuba Młynarczyka i Wojciecha Szabli o wytyczenie i utrzymanie wolnej ulicy do chałupy za 12 złp.",
        "transkrypcja": """--- Skan #105 (fol. 51r) ---
Actum Coram Officio Advocatiali et Scabinali Cra-
snicensi Feria Sexta post Festum Purificationis Bea-
tissimae Mariae Virginis proxima Anno Domini Millesimo
Septingentesimo Secundo.

W sprawie y Akciej między Uciwym Andrzeiem Łanckim Aktorem
z jednej a Michałem Kepką o zasługi nie zapłacone forest
Aktora Pozwanym Sąd niniejszy Ponieważ strony sobie zapie-
rają w niektórych punktach mianowicie że Uiednania sobie
mać być przydane aby się przed przyjacielskiem między sobą
zdawszy dwóch ludzi zgodziły & Termin conservando zachowany.

Sub eodem Actu
Przed Urzędem y Aktami niniejszemi Woytowskiemi y
Ławniczemi Krasnickiemi w osobach swoich stanąwszy
Uciwi Jakub Młynarczyk, Woyciech Szabla przed-
mieszczanie Krasniccy dobrowolnie zeznali praesentibus
że znaią Iż Oni Na Affektacią Uciwego Jakuba Lisa
Przedmieszczanina Krasnickiego w domu jego na przed-
mieściu Góry nazwanym około święta świętego Mi-
chała Archanioła Roku niedawno przeszłego tysiącznego
siedmsetnego pierwszego upraszani zeszli tamże między
requirującym z jednej a Sobestianem Rodzonkiem są-
siadem jego o pretensiej około Ulicy wolnej requiru-
jącemu który do chałupy swojej bydła y wszystko do-
bytek gonienia pomieniony Sobestian Rodzonek przedaie mu
dlatego że musi płoty na ich podjąć około ku-
rom y gruszki bo trzeba wyciąć y skopać na swoię
stronę do chałupy swojej fundować nową ulicę za którą
moderacją y rozporządzeniem między niemi uczyniliśmy
Naprzód za to że bez lat siedmnaście pretendował""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 106,
        "numer_pozycji": "106",
        "strona_pagina": "fol. 51v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Zeznania w sprawie burmistrza Barankowica",
        "osoby_podmioty": "Jakub Lis, Sebastian Rodzonek, Wojciech Grzymek (pisarz?), Jan Barankowic (burmistrz kraśnicki), Jan Barankowic (syn burmistrza), Matyjasz Stalmachowic (rzeźnik / świadek), Maryna Żydówka, Kazimierz Zagojski",
        "kwoty_podatki": "12 złp",
        "opis_sprawy": "Dokończenie ugody Jakuba Lisa z Sebastianem Rodzonkiem (12 złp i obowiązek grodzenia płotów). Następnie inkwizycja na instancję burmistrza Jana Barankowica i jego syna Jana: zeznanie rzeźnika Matyjasza Stalmachowica o bójce i obelgach Kazimierza Zagojskiego wobec syna burmistrza w sieni u Maryny Żydówki.",
        "transkrypcja": """--- Skan #106 (fol. 51v) ---
sobie requirujący nas pomieniony Jakub Lis za każdy rok
po złotych trzy za Używanie tejże ulicy w tym punkcie na
złotych dwanaście strony zgodziliśmy którą summę razem
obligował się oddać pomieniony Sobestian Rodzonek bez
turbowania y kosztów zaraz w tydzień po tej ugodzie bo
sierota idzie od teraźniejszego Gód po tej ugodzie
w Używania jej puko nie ufunduje swojej ulicy
ale będzie używał tejże którą na dwie obligował się
stare jedno podnieść, płotem drugie na ukośne za
pierwszą rekwizycją requirującego bez omieszkania
żadnego przy tej ugodzie Rękami Woyciecha
Grzymka de quo praesens ipsorum relatio.

W sprawie y Akciej między Sławetnym Panem Janem
Barankowicem Burmistrzem Krasnickim Ojcem y Synem
iego Janem Barankowicem ex delatione Inquisitionis
1mus Testis Honestus Matthias Stalmachowic rzemio-
sła rzeźnickiego Towarzysz Recognovit haec formalia
W niedzielę niedawno przeszłą byłem U Maryny Żydówki
tutejszej Krasnickiej z drugimi kolegami swoiemi staliśmy
sobie w sieni przypatrując się ludziom tańcującym w izbie
Wyszedł Kazimierz Zagojski do sieni y rzekł te słowa czego
wy tu stoicie Podsie co żeby kazał sobie piwa dać
w poniewieracie sobie w zórki a nas Wy pędzicie
z zamiarem przy sobie dalej rzekł nie dziwuję się nikomu
tylko tobie Barankowic Burmistrzowski synku do żyd-
ów chodzisz, On odpowiedział Kpiesz sam w tymże do
siebie porwali y szarpali się z sobą rzekł w tym Zagojski
abym przytykał do Marowickiego wybił Barankowicowi
szyję albo by chciał Bassarunku damy go na ostatku""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 107,
        "numer_pozycji": "107",
        "strona_pagina": "fol. 52r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Wyrok przeciw Wojciechowi Piaseckiemu",
        "osoby_podmioty": "Kazimierz Koszykowic (aktor), Wojciech Piasecki (pozwany)",
        "kwoty_podatki": "Brak (kara 2 tygodni wieży i przeprosiny)",
        "opis_sprawy": "Obszerny dekret Sądu Wójtowsko-Ławniczego Kraśnickiego w sprawie Kazimierza Koszykowica z Wojciechem Piaseckim: po rozpatrzeniu zeznań świadków sąd uznał winę Piaseckiego za rzucenie się z nożem/kufilem i groźby zabicia, skazując go na dwa tygodnie wieży i uroczyste przeprosiny z dwiema godnymi osobami.",
        "transkrypcja": """--- Skan #107 (fol. 52r) ---
W sprawie y Akciej między Uciwym Kazimierzem Koszyko-
wicem Aktorem a Woyciechem Piaseckim pozwanym o
z Aktorem Sąd niniejszy Woytowski y Ławniczy Krasnicki
przeczytawszy Inkwizycie z obojej strony wywiedzione
y one dobrze zrozumiawszy z których gdyż obiedwie
wysłuchawszy Ponieważ się to dowodnie pokazało Iż Uci-
wy Woyciech Piasecki idąc z Kuśnierzem poważył się
słów obelżywych przeciwko Uciwego Kazimierza Koszykowica
ma żonę publicznie używać mianowicie iżby był pierwej
małżonkiem miasto pohamowania gdyż słów zadziałała
sama zabieżała grompą po śmierci gdy pod stołem y groził się
mu z jednego dwoje zabić za niesprawiedliwie też
że winy swej aby dał winę winy na dwie strony dwie
sądowe, Woyciech o to że się nań rzucił in instanti oddał
po pierwszem Juramenta aby sądownie Deprecacją tak
samego Aktora jako y Żony iego wypełnił dwoma
godnemi osobami że bez niegodne o zabicie prosięta
gdyż pozwany Piasecki perswazyi na biedę użył y mówił
że mógł nieść na grunt Aktora tego prosięta aby
się Aktor sumieniem pozbywszy na piersiach ręce
prawą dowiódł jako Ani sam ani nikt z domu
jego nie zabił y mówił żeby go zabił iść in instanti
Ponieważ zaś pomieniony Aktor Koszykowic niere-
spektnie na winy przeciwko niesłusznym się krzywdy
swoiej w szynku pokazał się w gospodzie na skargę
wolną wtedy żeby nie uciśnić i okazji do kłótni
dać nadto że błogosławieństwem by winy większe
zasłużył jednak One na łaskę obrońcę sąd
został aby za to śmiałość lekkomyślną dał winy
grzywien dwie stronie y Sądowi dwie Więzienie
w gospodzie kontynuował po wyjściu aby także
Deprecacją wypełnił sądową Publicznie y żeby
w tej sprawie między dwiema stronami dobrotliwie""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 108,
        "numer_pozycji": "108",
        "strona_pagina": "fol. 52v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Protestacja Kępków i inkwizycja o dzbanek",
        "osoby_podmioty": "Tomasz Kępka, Matyjasz Kępa, Lawko Dawidowic (starozakonny), Jan Sycz [?] (świadek), Sebastian Strusek, Andrzej Łancki, Katarzyna Chudzikowa (wdowa, świadek)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie dekretu Koszykowica z Piaseckim; protestacja Tomasza Kępki i Matyjasza Kępy. Następnie sesja z piątku po Nawróceniu św. Pawła 1702 r. (27 I 1702): zeznania świadków na instancję Lawka Dawidowica — Jana Sycza i wdowy Katarzyny Chudzikowej — o zniknięciu glinianego dzbanka z wódką podczas pożaru u Andrzeja Łanckiego.",
        "transkrypcja": """--- Skan #108 (fol. 52v) ---
na przyszły czas nie ma się więcej nie czynić y czasu powiedź-
niałych y innych kłótni zachować Sąd nakazał
by strona stronę asekurovała w tej sprawie.

Sub eodem Actu
Videatur hoc loco Protestatio facta H. Thomae Kepka
et Mathiae Kepa Suburbano Crasnicensi de nullitate nos
Brata y Żony między Consuccessorami protestanta dnia
wczorajszego uczynionej in praeiudicium protestanta
et restitutio zakładu na wszystkie Sieradzkie y z tejże
nieprawej przedaży do którego prawnie windikować
krzywdy swojej.

Actum Coram Officio Advocatiali et Scabinali Cra-
snicensi Feria Sexta post Festum Conversionis
Sancti Pauli Apostoli proxima A. D. 1702.

Ex Instantia Infidelis Lawko Dawidowic incolae Cra-
snicensis 1us Testis H. Joannes Sycz[?] Recognovit we śro-
dę niedawno przeszłą byłem posłany do Lawka
żydowskiego do Sebastiana Struska z żoną Andrzeia
Łanckiego pytającego skąd by dzbanek miał iego w którym
i wódka y inne rzeczy podczas pożaru było w tymże
miejscu gdziem gospodynia odpowiadała że to wszystko kupi-
ła u tegoż Chłopca gdy rozpytałem tejże żony to
kto mówił skąd ten dzbanek ma z rąk a idzie do
tego być może że ten dzbanek to było przepadło teraz
gdy się patrzył Najświętszy y Męka Ultra nihil.

2dus Testis H. Katarzyna Chudzikowa wdowa Recognovit
Summe memento że na ten czas między inszemi jest dzbanek tego
żydowskiego żyda w którym było 4 garncy wódki na szyję
podczas jarmarku bom mu 3 garnce wlała y to jest.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 109,
        "numer_pozycji": "109",
        "strona_pagina": "fol. 53r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Zeznania i manifestacja",
        "osoby_podmioty": "Katarzyna Chudzikowa, Tomasz Łancki, Andrzej Łancki, Sebastian Strusek, Stanisław Żelazny (mieszczanin), Pinchas Dawidowic (arendarz kraśnicki), Matyjasz Głuchowski",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie zeznań Katarzyny Chudzikowej i Sebastiana Struska w sprawie dzbanka u Łanckich. Następnie oświadczenie Stanisława Żelaznego na rekwizycję arendarza Pinchasa Dawidowica w domu Matyjasza Głuchowskiego (termin do poniedziałku). Na dole początek sesji z 30 I 1702 r. (poniedziałek przed Oczyszczeniem NMP).",
        "transkrypcja": """--- Skan #109 (fol. 53r) ---
zdało się że do Kłodzianki wstało u Łanckiego jest ten
dzbanek który miał jeden skopiec jego drugi nosił do tej
wsi Tomasz Łancki widziałem też kiedy między niemi
on syn jego z tego dzbanka powstał y w ten sposób
tom widziała, A kiedy sama Łancka niosła piwo w nim
do domu swego to go zakrywała chustką że nim wie-
le się nie śmiano tak więc to też rzekła że jej per-
swadowała Łancka aby nie gadała mówiąc lepiej że
Katolikiem być niż żydem sam rzekła ia wyznam że nie
czyj inszy dzbanek tylko żydowskiego.

3tius Testis Sebastianus Strusek Recognovit że od tego samego
jest ten dzbanek który odebrano do mnie zowiąc go moim
przez most oddał Ojcu.

Sub eodem Actu
Przed Urzędem y Aktami niniejszemi w osobie swojej
stanąwszy Uciwy Stanisław Żelazny Mieszczanin
Krasnicki Na rekwizycję Starozakonnego Pinchasa Da-
widowica Arendarza Krasnickiego zeznał Będąc U
Starozakonnego Pinchasa Dawidowica w domu w piątek
niedawno przeszły słyszałem z ust Matiasza Głuchowskiego
Przedmieszczanina Krasnickiego który mówił te słowa Pa-
nie Arendarzu mnie wystarczą że komu powiedział u was nie
dajecie mnie do poniedziałku to ia będę wiedział
co z tym czynić najdalej w poniedziałek to ja jeżeli nie
będzie u Spokojem według swojej woli na sąd od
urody dowód na mnie wydacie, jeżeli ich nie od-
prowadzę to ia u tego będę.

Actum Coram Officio Advocatiali et Scabinali Cra-
snicensi Feria Secunda ante Festum Purificationis
Beatissimae Mariae Virginis proxima Anno Domini Mille-""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 110,
        "numer_pozycji": "110",
        "strona_pagina": "fol. 53v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Długi i proces o dzbanek",
        "osoby_podmioty": "Lawko Dawidowic (starozakonny), Andrzej Łancki, Szymon Jartek, Wigdor (starozakonny)",
        "kwoty_podatki": "18 fl (dług Szymona Jartka dla Wigdora: półsłódka, 25 korcy owsa po 18 gr, 18 gr za pszenicę)",
        "opis_sprawy": "Dokończenie sesji z 30 I 1702 r.: dylacja w sprawie Lawka Dawidowica z Andrzejem Łanckiem; uznanie długu 18 fl Szymona Jartka dla Wigdora za słód i owies. Następnie sesja ze środy w wigilię Oczyszczenia NMP 1702 r. (1 II 1702): kontynuacja procesu Lawka Dawidowica przeciw Andrzejowi Łanckiemu o dzbanek i płótno warte 77 gr.",
        "transkrypcja": """--- Skan #110 (fol. 53v) ---
simo Septingentesimo Secundo. W sprawie y Akciej między Nie-
wiernym Lawkiem Dawidowicem Obywatelem Krasnickim a
Andrzeiem Łanckiem datur dilatio Inquisitionis, cuius poenam
et Unius parvet Officio per medium.

Sub eodem Actu
Winien Szymon Jartek hanc Wigdorowi złotych osmnascie
y groszy 18 powinien wypłacić na Niedzielę Przewodnią
żyto przyprawić do każdego półsłodka po korcy przy tym
półdziesięty dwu kwart dwadzieścia za korcy 18 y groszy dwadzieścia
item pszenica spustowa za korce 18 y groszy piętnaście przy
chudobie złożyć których pieniędzy abysmy Juramentem
odwrócił za tysiąc a z Aktu Decreti.

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Quarta in Vigilia Festi Purifi-
cationis Beatissimae Mariae Virginis Anno Domini
Millesimo Septingentesimo Secundo.

W sprawie y Akciej między Niewiernym Lawkiem Dawido-
wicem Obywatelem Krasnickim Aktorem a Uciwym An-
drzeiem Łanckiem Przedmieszczaninem Krasnickim pozwanym
Sąd niniejszy Woytowski y Ławniczy Krasnicki przeczytawszy
Inkwizycie w tej sprawie wywiedzione Na dowód licząc zezna-
nego dzbanka z wódką dobry podczas pożaru w Mie-
ście Krasniku ukradzionego przy którym y rzeczy
różne wartości siedmdziesiąt ieden groszy synackiey[?]
stracone ukradziono, Ponieważ potwierdza oczywista lisza
weryfikacja tego tu pokazała że się do niego nie ma Jury
zachować, evidenter pokazało y in formie że ukradł
o tym dzbanku Oficie Proinde Aktora przychylnym bliżej""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 111,
        "numer_pozycji": "111",
        "strona_pagina": "fol. 54r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Przysięga w bożnicy i dekrety",
        "osoby_podmioty": "Lawko Dawidowic, Andrzej Łancki, Szmul Moszkowic, Anna Kotłubajka [?], Matyjasz (szwagier)",
        "kwoty_podatki": "71 gr 8 szel (wartość skradzionych rzeczy), 24 grzywny (kara dla Łanckiego), 22 gr (spór Szmula z Matyjaszem)",
        "opis_sprawy": "Rota przysięgi Lawka Dawidowica w bożnicy na rodał i surowy wyrok na Andrzeja Łanckiego (24 grzywny kary i groźba fustigacji). Następnie sesja z 3 II 1702 r. (nazajutrz po Oczyszczeniu NMP): sprawa Szmula Moszkowica przeciw Annie Kotłubajce oraz dekret przeciw Matyjaszowi o 22 gr.",
        "transkrypcja": """--- Skan #111 (fol. 54r) ---
do poprzysiężenia szkód wszystkich w piątek przyszły
w Bożnicy Krasnickiej na rodale bosemi nogami stojąc na ziemi
ubrawszy się w krakowski płaszcz w szabas chodzić w te rothę
Ja przysięgam P. B. Iż za przybyciem słusznie wino daje każde
winy Łanckiemu szkód swoich rzeczy ukradzionych wartości
Siedmdziesiąt y jeden groszy polskich i groszy ośm na to winien jestem
i nie kto inny tylko że rzekł obwiniony, Owszem lubo
nie kto by to uwierzył Po którym Juramencie odprowadzić
powinien pozwany winy złodziejskiej popadać do Miasta
ratunku z tej kąty w razie jeżeli słusznej umowy powrotu
z dzbanka które wino mając respekt na niedostatek
jego ułaskawiąc obrócił aby dał grzywien Dwadzieścia
stronie y Sądowi per medium, Koszta Aktorowi prawne go
wrócić Inquantum zaś ta kaucja konsekwencji nie będzie
się kontentował y zadosyć nie uczyni do grzywien powinien
będzie fustigacji być karany publicznie, Decreti
praesentis vigore.

Actum Coram Officio Advocatiali et Scabinali
Crasnicensi in Crastino Festi Purificationis
Beatissimae Mariae Virginis Anno Dni 1702.

W sprawie y Akciej między Niewiernym Szmulem Moszko-
wicem a Anną Kotłubajką aby świadki strony wezwa-
den złożyć przed sądem pod terminem prima Juris
Terminum Conservando.

W sprawie między Szmulem y Matiaszem aby złotych
groszy dwadzieścia oddał pozwany, tym instanti.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 112,
        "numer_pozycji": "112",
        "strona_pagina": "fol. 54v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Kalkulacja, manifestacja i protestacja",
        "osoby_podmioty": "Szymon Moszkowic, Kazimierz Maziarczyk, Szmul (starozakonny), Jakub Kłopot, Jan Srawski (przedmieszczanin), Walenty Gozdał, Marianna Gozdałowa",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie sesji z 3 II 1702 r.: sprawa Szymona Moszkowica przeciw Kazimierzowi Maziarczykowi o kalkulację oraz manifestacja Żyda Szmula przeciw Jakubowi Kłopotowi. Następnie sesja z soboty po Oczyszczeniu NMP 1702 r. (4 II 1702): protestacja przedmieszczanina Jana Srawskiego przeciw Walentemu Gozdałowi i jego żonie Mariannie o pobicie i obelgi.",
        "transkrypcja": """--- Skan #112 (fol. 54v) ---
W sprawie y Akciej między Starozakonnym Szymonem Mosz-
kowicem Obywatelem Krasnickim a Kazimierzem Maziar-
czykiem o kalkulację aby nie włożył do ksiąg z Feria Secunda
ante Festum Sanctae Mariae Magdalenae proxima Anno
Domini Millesimo Septingentesimo Primo copy tej
wody aby oddał według dekretu względem różnych
pretensji Calculationem czyni tej strony Całej nieba War-
tium cum probatione amicali & Terminum Conservando perem-
ptorium.

Manifestuje się od impetycji tego Szmula aby Kłopot
Jakub nie szedł z więzienia pod aresztem a Aktorowi za
decyzję.

Actum Coram Officio Advocatiali et Scabinali Cra-
snicensi Sabbato post Festum Purificationis Beatis-
simae Mariae Virginis proxima Anno Domini Millesi-
mo Septingentesimo Secundo.

Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
Krasnickich w osobie swoiej przyszedłszy Uciwy Jan
Srawski Przedmieszczanin Krasnicki solennie
z wielkim żalem protestował się przeciwko Uci-
wemu Walentemu Gozdałowi y Mariannie małżonkom
Iż Oni zapomniawszy Boiaźni Bożej y miłości
bliźniego poważyli się na kłamstwo protestanta w drodze
złodziejstwem zadawać iako by z tego prosię
Nadto w rezydencji mieszkania biegąc płacząc się
w kłótnię z którym despektowali, Iterum atque iterum pro-
testuie się.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 113,
        "numer_pozycji": "113",
        "strona_pagina": "fol. 55r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Wyrok, areszt i dekret",
        "osoby_podmioty": "Jan Srawski (przedmieszczanin), Walenty Gozdał, Marianna Gozdałowa, Józef Wilk, Andrzej Wilk (brat), Wojciech Piasecki, Izrael Chaponowic (starozakonny), Kazimierz Maziarczyk",
        "kwoty_podatki": "12 grzywien (kara Gozdała), 5 złp (areszt na płótno i owies), 5 złp (dług K. Maziarczyka), 24 gr (dwa spusty wódki)",
        "opis_sprawy": "Sesja z poniedziałku po Oczyszczeniu NMP 1702 r. (6 II 1702): (1) dekret w sprawie Jana Srawskiego przeciw Walentemu i Mariannie Gozdałom (kara 12 grzywien); (2) areszt Józefa i Andrzeja Wilków na rzeczach Wojciecha Piaseckiego (płótno i 5 złp); (3) dekret dla Izraela Chaponowica przeciw Kazimierzowi Maziarczykowi o 5 złp oraz 24 gr za wódkę.",
        "transkrypcja": """--- Skan #113 (fol. 55r) ---
Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Secunda post Festum Puri-
ficationis Beatissimae Mariae Virginis proxima Anno
Domini Millesimo Septingentesimo Secundo.

W sprawie y Akciej między Uciwym Janem Srawskim
Przedmieszczaninem Krasnickim z jednej a Walentym
Gozdałem y Marianną małżonkami względem zadania
krzywdy i złodziejstwa grzywien dwanaście parti et officio
per medium powinno być żądania z poprawą Kto by
miał skargę infestować się pod karą decreti praesentis
Vigore.

Areszt założony od Uciwych Józefa Wilka y Andrze-
ia Brata iego Obywatelów Krasnickich areszt założony
przeciwko Woyciechowi Piaseckiemu względem długu
złotych pięciu y płótna miar sześci od środy przyszłej
aż do drugiej środy Terminum Conservando peremptorium.

W sprawie y Akciej między Niewiernym Izraelem Chapo-
nowicem Obywatelem Krasnickim Aktorem a Kazimierzem
Maziarczykiem o dług pewny złotych pięćdziesiąt pięć
polskich aby za te pieniądze na święto Bożego
Narodzenia w komplanacji wyrażone do rąk
Święta Świętego Macieja Apostoła wypełnił
A że ony nie stawał w przeszły poniedziałek areszt
czyni na złotych dwudziestu pięciu aby oddał
trzecia na Kwiecień niedzielę Czwartą na święto
św. Wojciecha Roku teraźniejszego oddał decreti
praesentis vigore Quo vero spectat o długu na koniu
od Karczmarza ulica jest Szmul et suspensa decyzja.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 114,
        "numer_pozycji": "114",
        "strona_pagina": "fol. 55v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Protestacje i obdukcja ran",
        "osoby_podmioty": "Walenty Gozdał, Anna Gozdałowa (żona), Jan Srawski, Marcin Kanapkowic, Wojciech Kanapkowic (ławnik), Matyjasz Dederowski, Wawrzyniec (towarzysz tkacki)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie dekretu z 6 II 1702 r. oraz dwie protestacje pod tym samym aktem: (1) Walenty Gozdał z żoną Anną przeciw Janowi Srawskiemu o bezprawne najście izby; (2) Marcin Kanapkowic w asystencji ławnika Wojciecha Kanapkowica przeciw Matyjaszowi Dederowskiemu i tkaczowi Wawrzyńcowi o pobicie na drodze i uszkodzenie sukni.",
        "transkrypcja": """--- Skan #114 (fol. 55v) ---
po wysprawiedliwieniu złotych pięć groszy sześć złotych y sześć
groszy dwadzieścia za miód z rzeczami takiemi na
calculationis Terminum Conservando peremptorium prima Juris.

Sub eodem Actu
Do Urzędu y Akt niniejszych w osobie swoiej przyszedłszy
Uciwy Walenty Gozdał Przedmieszczanin Krasnicki y z An-
ną małżonką solennie z wielkim żalem protestowali
się przeciwko Uciwemu Janowi Srawskiemu Oto
Iż On na Uczynienie przy sprawie szkody protestantów
dnie bywa wedle dekretu trzymać nie ma w pokoju
nie między sobą nie wspominać w jednej szkodzie pomie-
nionego jednak On słów złodziejskich użył, kłótnie wniósł
kłócąc się.

Sub eodem Actu
Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
Krasnickich w osobie swojej przyszedłszy Uciwy Mar-
cin Kanapkowic Sławetnego Pana Woyciecha Kanapko-
wica Ławnika Krasnickiego w przytomności tegoż
szwagra swego solennie z wielkim żalem protestował
przeciwko Uciwemu Matiaszowi Dederowskiemu Przed-
mieszczaninowi Krasnickiemu y Wawrzyńcowi Człotko-
wi tegoż rzemiosła Tkackiego towarzyszowi Iż Oni bez
miłości Bożej y bliźniego na dobrowolnej drodze
z miasta idącego bez dania okazij powazyli się protestanta
ogródek lewy zbić we mnie zabić z tejże woli lecz
in emias[?] protestationis verificationem pokazał
Na lewej stronie raz krwawy w twarzy na dwa członki
palca w szerz wzdłuż także pokazał krwią zbryzganą
suknią od ramienia uszkodził to tak wiele""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 115,
        "numer_pozycji": "115",
        "strona_pagina": "fol. 56r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Manifestacja i dekret",
        "osoby_podmioty": "Marcin Kanapkowic, Stanisław Sprawski (obywatel kraśnicki), Tomasz Anczarek (przedmieszczanin), Izrael (starozakonny), Stanisław Luterek (mieszczanin)",
        "kwoty_podatki": "43 złp 12 gr (dług S. Luterka dla Izraela)",
        "opis_sprawy": "Dokończenie protestacji M. Kanapkowica. Następnie sesja ze środy po Oczyszczeniu NMP 1702 r. (8 II 1702): uroczysta manifestacja Stanisława Sprawskiego przeciw Tomaszowi Anczarkowi o zniewagę honoru i naruszenie zapisu o wykupie dóbr oraz dekret w sprawie Izraela przeciw Stanisławowi Luterkowi o 43 złp 12 gr.",
        "transkrypcja": """--- Skan #115 (fol. 56r) ---
w sieni nie wyprasza bez dania okazij przed domem Sławet-
nej Pani Suchiej wdowy strzela się za darmo y prosi o
dojście poważnie obiecując prawnie Violenciej dochodzić.

Actum Coram Officio Advocatiali et Scabinali Crasni-
censi Feria Quarta post Festum Purificationis Be-
atissimae Mariae Virginis proxima Anno Domini Millesimo
Septingentesimo Secundo.

Do Urzędu y Akt niniejszych Woytowskich y Ławniczych Kra-
snickich w osobie swoiej przyszedłszy Zacnie Sławetny Pan
Stanisław Sprawski Obywatel Krasnicki solennie manife-
stował się przeciwko Uciwemu Tomaszowi Anczarkowi Przed-
mieszczaninowi Krasnickiemu Oto Iż On luboby mu podług
niepotrzeby y kosztów trzymania z okazji wyprowadzenia się
trefnego zadania słów honorowi y urodzeniu manifestanta szko-
dzących podczas Sprawy o dobra pewne które od niego ma-
nifestant windikował y oznaczono Jakoż o tym protesta-
cja do woli opiewa w Aktach tutecznych Burmistrzow-
skich y Radzieckich Krasnickich Wspomniane opiewają
że ma w tej o honor y prawo Violenciej dochodzić
ma w takie koszta włożył y pod rygor podał o które z tego
iterum atque iterum manifestuie się iudicio renovando
protestationem suam de prosequenda tali protestatione.

W sprawie y Akciej między Niewiernym Chaponowicem
Izraelem Obywatelem Krasnickim Aktorem z jednej a
Uciwym Stanisławem Luterkiem Mieszczaninem Kra-
snickim pozwanym o złotych czterdzieści y trzy dziesięć
oddać aby oddał z niedziel dwie Aktorowi sub poenis
officii arbitrariis executione in bona et personam facien-
da fone tym złotych trzech groszy dwanaście do""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 116,
        "numer_pozycji": "116",
        "strona_pagina": "fol. 56v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Dekret i zeznanie świadka",
        "osoby_podmioty": "Stanisław Luterek, Szmul (starozakonny), Kołodziejka (wdowa), Tomasz Barankowic, Matyjasz Stalmachowic (świadek), Kazimierz Zagojski, Jan Barankowic, Wojciech Zagojski, Marcin Kłak [?], Stanisław Krokoszowski [?]",
        "kwoty_podatki": "2 złp (dług Kołodziejki dla Szmula)",
        "opis_sprawy": "Dokończenie dekretu Izraela z Luterkiem; dekret dla Szmula przeciw Kołodziejce wdowie o 2 złp. Następnie inkwizycja na instancję Tomasza Barankowica: zeznanie Matyjasza Stalmachowica o niedzielnym incydencie przy muzyce żydowskiej w domu Żydówki między Kazimierzem i Wojciechem Zagojskimi a Janem Barankowicem.",
        "transkrypcja": """--- Skan #116 (fol. 56v) ---
miodu y piwa aby oddał przed zachodem Słońca decretum
praesentis vigore.

W sprawie y Akciej między Niewiernym Szmulem Aktorem
a Kołodziejką wdową aby złotych dwie na następny
wtorek oddała decrevit.

Videatur sub Actu Feria 6ta post Purificat.
Ex Instantia Thomae Barankowic 1us Testis
Honestus Matthias Stalmachowic Recognovit haec
formalia W niedzielę niedawno przeszłą byłem u
Muzyki Żydowskiej tutejszej Krasnickiej z drugiemi
kollegami staliśmy sobie w sieni przypatrując się lu-
dziom tańcującym w Izbie Wyszedł Kazimierz Zagojski
bo iem y rzekł te słowa czego wy tu stoicie Podcie
do Izby każcie sobie piwa dać Wy Krowie wybiera-
cie sobie w zórki a nas iak my się nie żenimy we
źlemy że piwo pijemy y wódkę dalej rzekł w niedzi-
elę nie nikomu iak tobie Panie Barankowic Bur-
mistrzowski synku Pójdźże do Izby każ sobie piwa
dać On odpowiedział Kpię sam w tymże do
siebie porwali y szarpali się w tym Zagojski
do Barankowica aż w to przepłynął za mną
niego wybił On rzekł albo y ty chcesz Bassarunku
sam o to masz brata u której mowa mi między poparł
aż Barankowic musiał ustąpić na stołka Brata iego
Woyciech Zagojski w obronę słowa o ten skarżył się
na ped nam po złości ale miałby bitwę chciał coby był
miał zabić, obaczył Marcin Kłak y Krokowski słysząc
rzekł donieść z tejże za Barankowicem trzymał
nie raz a nikt go nie bił, chcieli go bić y zabić
ale uciekł.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 117,
        "numer_pozycji": "117",
        "strona_pagina": "fol. 57r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Zeznania świadków i dekret",
        "osoby_podmioty": "Andrzej Bębenkowski (świadek, szewc), Kazimierz Zagojski, Jan Barankowic, Wawrzyniec Kuczanowski (świadek), Marowski, Izrael Chaponowic (starozakonny), Kazimierz Maziarczyk",
        "kwoty_podatki": "18 złp (dekret dla Izraela Chaponowica: 9 złp od razu + 9 złp na św. Dorotę)",
        "opis_sprawy": "Dalsze zeznania świadków w sprawie Tomasza i Jana Barankowiców z Kazimierzem Zagojskim: szewca Andrzeja Bębenkowskiego i Wawrzyńca Kuczanowskiego (pijany Zagojski ciągnący Barankowica za włosy i grożący basarunkiem pod drzwiami Marowskiego). Następnie dekret dla Izraela Chaponowica przeciw Kazimierzowi Maziarczykowi na 18 złp.",
        "transkrypcja": """--- Skan #117 (fol. 57r) ---
2dus Testis Andreas Bębenkowski rzemiosła szewskiego
Recognovit haec W niedzielę niedawno przeszłą wieczór
z muzyki stałem w sieni z drugiemi ludźmi Wyszedł
Zagojski Kazimierz rzekł te słowa czego tu stoicie Każcie
sobie Kuwada albo wódki nie wybierajcie w zórki z ludzi
w tym wziął za barki Barankowica Jana y ciągnął go
do Izby Barankowic rzekł do niego nie ciągnij mnie sto-
imy sobie kiedy ia tobie miał gość to pójdę w tym
poszli z sobą na Izbę y dalej bo mi się zdaje Barankowic
rzekł te słowa jeżeliś dał majstrowi nie mu Bassarunek
dalszym nie dalej nie wiem bo się między niemi stało
od tych wyszli na dwór z sobą z drugiemi nie wiem
nic more tacto pectore.

3tius Testis Wawrzyniec Kuczanowski similiter to
tylko dołożył, że Pijany był Kazimierz Zagojski
y z tym wyszedł że z pełnemi słowami pobiegł do
Marowskiego y kołatał we drzwi do niego tacto
pectore.

W sprawie y Akciej między Starozakonnym Izraelem
Chaponowicem Obywatelem Krasnickim Aktorem a
Kazimierzem Maziarczykiem o dług pewny z likwidacji
regestru jego pokazanej Należności przybywających
Ośm Oprócz kosztów prawnych wynoszących Sąd ni-
niejszy przejrzawszy Upartości stron wyrokem swym
wynalazł aby złotych Osmnaście polskich oddał
pozwany Aktorowi złotych dziewięć polskich in instanti
złotych zaś dziewięć na środek postu do teraźniej-
szego Inquantum nie odda pozwany bliżej Aktor
przy regestrze sumować do Comprobacji w przyszły""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 118,
        "numer_pozycji": "118",
        "strona_pagina": "fol. 57v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Reprotestacja i manifestacja",
        "osoby_podmioty": "Tomasz Anczarek (przedmieszczanin), Stanisław Sprawski (obywatel kraśnicki), Michał Kepka, Andrzej Łancki",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie dekretu dla Izraela; reprotestacja Tomasza Anczarka przeciw Stanisławowi Sprawskiemu o niesłuszną kalumnię i ujmę na honorze z okazji wykupu dóbr przed sądem burmistrzowskim. Na dole sesja z poniedziałku przed św. Walentym 1702 r. (13 II 1702): manifestacja Michała Kepki przeciw Andrzejowi Łanckiemu.",
        "transkrypcja": """--- Skan #118 (fol. 57v) ---
piątek & Terminum partibus Conservando peremptorium.

Sub eodem Actu
Do Urzędu y Akt niniejszych w osobie swoiej przyszedł-
szy Uciwy Tomasz Anczarek Przedmieszczanin Krasnicki
solennie z wielkim żalem reprotestował się przeciwko
Panu Stanisławowi Sprawskiemu Obywatelowi Kra-
snickiemu Oto Iż On niewinną Calumnią iako by Uięcia
honoru y Urodzenia iego poważył się zadać niesłusznie po-
bieżeć siebie podczas Sumacji z dóbr protestanta na ten
czas służących A potym przez pomienionego Tomasza Anczar-
ka Windikowanych, y one zapisane którey rzeczy
przeciwko niemu protestant nigdy nie zażył tyle
gmocie pokaże Po drugiej jego że On nie zastaw
ny terminu z protestantem w nosze jedzie na
pokazanie dokumentów honoru swego y inne
potrzeby znać ma a na szkodę protestanta waży
się protestować o krzywdę o której nieważności pro-
testacyi solennissime reprotestuie się protestant
Obrawszy czas zniewagi y sądów podczas sumacji
z dóbr sobie obligowany Jako procesa sprawy opie-
wania reprotestuie się.

Actum Coram Officio Advocatiali et Scabinali Crasni-
censi Feria Secunda Ante Festum Sancti Valentini
proxima Anno Dni Millesimo Septingentesimo Secundo.
Videatur protestatio Una cum manifestatione H. Michaelis
Kepka Contra H. Andream Łancki ratione tenere sui le-
xatonis in damna inductionis.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 119,
        "numer_pozycji": "119",
        "strona_pagina": "fol. 58r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Dekrety i kontumacja",
        "osoby_podmioty": "Jakub Lis (przedmieszczanin), Sebastian Rodzonek (przedmieszczanin), Albert Szabliński [?], Jan (syn?), Dorota Wilkowa (matka), Józef Wilk, Andrzej Wilk (bracia), Jan Lis, Tomasz Nowak (mieszczanin)",
        "kwoty_podatki": "12 złp + 3 złp (S. Rodzonek), 4 grzywny (kontumacja Wilków)",
        "opis_sprawy": "Sesja ze środy w oktawie św. Walentego 1702 r. (15 II 1702?): (1) nakaz w sprawie Jakuba Lisa przeciw Sebastianowi Rodzonkowi (zapłata 12 złp, 3 złp kosztów oraz 2 dni orki na wiosnę); (2) kontumacja Doroty Wilkowej i jej synów Józefa i Andrzeja Wilków na instancję Alberta Szablińskiego (zysk 4 grzywien); (3) sprawa Jana Lisa przeciw Tomaszowi Nowakowi o intromisję.",
        "transkrypcja": """--- Skan #119 (fol. 58r) ---
Actum Coram Officio Advocatiali et Scabinali
Crasnicensi Feria Quarta in Octava Festi Sancti
Valentini proxima Anno Domini 1702.

W sprawie y Akciej między Uciwymi Jakubem Li-
sem Aktorem z jednej a Sobestianem Rodzonkiem
Przedmieszczanami Krasnickiemi Aby pozwany według kom-
planacji zawartej Uczynił do złotych dwunastu złotych
trzy dodać kosztów prawnych ponieważ Aktorowi zało-
żono pod Kosztem aby dwa dni na Wiosnę orał
Aktorowi, póty powinien brać póki nie będzie miał
swoiej Ulicy Vadium grzywien dwoje & Terminum
pro iure servando paris interposuit.

Ex Instantia H. Alberti Szabliński[?] suo et Joan-
nis filij H. Dorothea Wilkowa Mater atque filij
Josephus Wilk, Andreas fratres Contumaces
in Causa względem niesłusznego Aresztu tatitij
in lucrum solvendi Maream quatuor parti
et officio per medium solvenda.

Sub eodem Actu
W sprawie y Akciej między Uciwymi Janem Li-
sem Przedmieszczaninem Krasnickim Aktorem a
Tomaszem Nowakiem Mieszczaninem Krasnickim
aby za ten dług który Juramentem wykonanem
wygnał Złotych raz czterdzieści y cztery za
oznaczeniem się sumieniem w tydzień jako nie
ma przygotowania płacić tedy wolna Intromissia
w dobra pozwanego będąc podana Decreti praesentis
Vigore.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 120,
        "numer_pozycji": "120",
        "strona_pagina": "fol. 58v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Dekrety i relacja kontrybucyjna",
        "osoby_podmioty": "Stanisław Dudkowski, Tomasz Zdebikowic (ławnik), Stanisław Dudek, Stalmach (aktor), Dorota Wilkowa, Andrzej Wilk, Wojciech Piasecki, Kazimierz Koszykowic, Kazimierz Chmielowic (ławnik), Franciszek Rymarczyk, Wawrzyniec Brzostowski [?], Pinchas Dawidowic (arendarz)",
        "kwoty_podatki": "15 grzywien (kara Dudka), 4 grzywny (kara Wilka), 42 grzywny (kontrybucja u Pinchasa Dawidowica)",
        "opis_sprawy": "Sesja z czwartku przed św. Maciejem Apostołem 1702 r. (16 II 1702): przysięga Stanisława Dudkowskiego z siostrą; dekret dla ławnika Tomasza Zdebikowica przeciw Stanisławowi Dudkowi (15 grzywien); sprawa Stalmacha przeciw Dorocie i Andrzejowi Wilkom (4 grzywny); sprawa Piaseckiego z Koszykowicem; oraz relacja ławników Kazimierza Chmielowica, Tomasza Zdebikowica i Franciszka Rymarczyka o złożeniu 42 grzywien u arendarza Pinchasa Dawidowica.",
        "transkrypcja": """--- Skan #120 (fol. 58v) ---
Actum Coram Officio Advocatiali et Scabinali Cra-
snicensi Feria Quinta ante Festum Sancti Mathiae Apostoli proxima
Anno Domini Millesimo Septingentesimo Secundo.

Juramentum praestitum H. Stanislai Dudkowski cum sorore sua
filiis olim Jakuba syna de Papretka[?] respectu pecuniarum
subrepta liberi a praestando.

W sprawie y Akciej między Sławetnym Panem Thomaszem Zdebi-
kowicem Ławnikiem Krasnickim Aktorem z jednej a Stanisła-
wem Dudkiem o niedotrzymanie słowa aby złoty czech yan
sy Piętnaście in instanti oddał grzywien dwie parti et offi-
cio per medium.

Sub eodem Actu
W sprawie między Stalmachem Aktorem Dorotą Wilkową
Matką y Synem Andrzeiem Wilkiem in obiectione loci
standi aby grzywien cztery Samopasowe oddał rzekł
nie zasłużył aby oddał y dowiedzie Aktorowi o wszystko
co w żądaniu zapisie prawo & Termin zachowano.

Sub eodem Actu
W sprawie y Akciej między Uciwymi Wojciechem Piaseckim
Aktorem a Kazimierzem Koszykowicem datur dilatio Inquisi-
tionis respectu dowodu Jakuba Proszka na którego się po-
zwał Decretum dowiedzie Aktor declaravit & probat.

Sub eodem Actu
Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
przyszedłszy Sławetni Kazimierz Chmielowic y Tomasz
Zdebikowic Ławnicy Krasniccy w osobach swoich y Franci-
szek Rymarczyk Przedmieszczanin Krasnicki zeznali że złożyli
42 Grz. na rekwizycję Pana Wawrzyńca Brzostowskiego[?]
y multa tu iego przyszli włożyli do Niewiernego Żyda
Pinchasa Dawidowica Arendarza Krasnickiego w sklepie""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 121,
        "numer_pozycji": "121",
        "strona_pagina": "fol. 59r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Komisja i protestacja o pobicie",
        "osoby_podmioty": "Stanisław Antoni Morelowski (komisarz), Pinchas Dawidowic (arendarz), Bartłomiej Walerak, Marek Jadyk, Franciszek Jadyk (poddani z Olbięcina), Bielski (skarbnik bełski), Ajzyk (starozakonny), Wigdor (starozakonny), Berek (starozakonny)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie relacji ławników o komisji podstolego Stanisława Antoniego Morelowskiego z 12 I 1702 r. i arendarzu Pinchasie Dawidowicu. Następnie sesja z poniedziałku przed św. Maciejem 1702 r. (20 II 1702): protestacja pracowitych braci Bartłomieja Waleraka, Marka i Franciszka Jadyków z Olbięcina (poddanych skarbnika bełskiego Bielskiego) przeciw Żydowi Ajzykowi o pobicie przy przechodzeniu od Wigdora do Berka.",
        "transkrypcja": """--- Skan #121 (fol. 59r) ---
zachowania swoich na ten czas do którego złożenia na tej
należytości tak do Skarbu J. M. Pana Tutaj onego ma
stać u Sądu Lubelskiego Kommissarskim Dekretem Jego Mci
Pana Antoniego Morelowskiego na ten czas będącego
de Actu et data 12. Januarij 1702 na ten czas będącego
towarzyszów sobie rekwirujący wolne prawa y wódki
oddać ma takiemu trzymając ad praementionem arendarza
y utrzymali relacją Niechaj pyta się Starosty
Panie Burmistrzu dlaczego nie pozwalają piwa
y wódkę robią de quo praesens relatio.

Actum Coram Officio Advocatiali et Scabinali Crasni-
censi Feria Secunda Ante Festum Sancti Mathiae Apo-
stoli proxima Anno Domini Millesimo Septingentesimo
Secundo.

Do Urzędu y Akt niniejszych Woytowskich y Ławniczych
Krasnickich w osobach swoich przyszedłszy Pracowici Bar-
tłomiej Walerak Marek y Franciszek [?] Stanisław
Jadyk Bracia z Olbięcina Wielmożnego Jego Mci Pana
Wybranowskiego Skarbnika Bełskiego poddani solennie
protestowali się przeciwko Niewiernemu Aizykowi Żydowi
Krasnickiemu Iż On poważył się Naprzód Bartłomieja
Waleraka pobitego z Franciszka Jadyka dnia wczo-
rajszego gdy na przechod od Wigdora Żyda przechodzili
do Berka Żyda sąsiada zabał yenia musieli szali
bez żadnej przyczyny Które kłótnie na księgę w sromocie
In cuius Protestationis Verificationem pokazał pomieniony
Bartłomiej Walerak pokazał W Ubiorach swoich
od rany przedniory znak.
Pracowity zaś Franciszek Jadyk pokazał w ubiorach swoich
sukiennych znaków prostych na Zewnętrznym Kuśmierzu""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 122,
        "numer_pozycji": "122",
        "strona_pagina": "fol. 59v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Reprotestacja żydowska i bójka",
        "osoby_podmioty": "Bartłomiej Walerak, Franciszek Jadyk, Ajzyk Muszkowic (starozakonny, obywatel kraśnicki), Lewek (starozakonny), Stanisław Judyk",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie protestacji poddanych z Olbięcina; następnie pod tym samym aktem reprotestacja starozakonnego Ajzyka Muszkowica przeciw poddanym o napad i bójkę przy ucieczce do domu Żyda Gersona; oraz protestacja Lewka przeciw Stanisławowi Judykowi z obdukcją ran z bójki na drodze.",
        "transkrypcja": """--- Skan #122 (fol. 59v) ---
siny, rzeki u dwóch palców od bitwy jakiej chciały dni
tej krzywdy dojść gdy uciekał pomieniony Ayzyk Żyd do domu
Gersona Żyda ciężko zbiłem słysząc się polskim rzu-
cał krzycząc synowie Matka kłótni aby się nie wdali
w tumult kłócąc się w żydami uczynił o co się protestuie y
bije nie prawie, o te violencję czynić item Franciszek Jadyk.

Sub eodem Actu
Videatur hoc loco Reprotestatio facta Infidelis Aizyk
Muszkowicz incolae Crasnicensis Contra subditos supra
specificatos ratione sinistra traductionis aliorum
oni na skargę protestanta na skargę kary do diece-
zyi tutejszej gdzie nie szanując skóry swojej tylko
w sianie ostatni kąt odstąpili albo nie mniej prote-
stantowi zastąpili w drodze katolicy z bronią rękami
przyszli y zabić chcieli o koszt kraśnicki o co war-
waną tę violencję pryncypał Franciszek z Jadyk
Lewek zaś kupiec protestował się przeciwko Stanisła-
wowi Judykowi Iż On poważył się nie mając o sło-
wa czego sobie kłótni a bić którym był nie termin
z Izby karczemnej protestował się przeciwko Braci
omienionemu Franciszkowi y Jadykowi na dobrowolnej
drodze przeciwko Jadykom poważył się protestant
kamieniem do tamtego rzucać czemu za Biedą
Uchybił przypadłszy Bartosz Walerak przeciwko te-
mu tumult eskurował Pokazał rany na lewej stronie
w ręku rany ad instar dwóch plaga z tejże strony
sukni przedartej na lewej stronie o pół łokcia i ten na
dwóch członkach palców dwóch lewej ręki zdrapane.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 123,
        "numer_pozycji": "123",
        "strona_pagina": "fol. 60r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Zeznania o płótnie i arendzie",
        "osoby_podmioty": "Lewek (kupiec, obywatel kraśnicki), Szymon Karczmarczyk (z Przedmieścia, świadek), Michał Piotrowczyk, Marcin Błażejczyk (stary poddany z arendy Kwasa, świadek), Kwas (arendarz)",
        "kwoty_podatki": "12 złp 20 gr (szacunek szkody Lewka)",
        "opis_sprawy": "Dokończenie obdukcji ran Lewka. Następnie zeznania świadków na instancję kupca Lewka: Szymona Karczmarczyka z Przedmieścia oraz starego Marcina Błażejczyka z arendy pana Kwasa o zajściu w piątek przy wozie z parobkiem Michała Piotrowczyka o płótno i zgrzebne worki.",
        "transkrypcja": """--- Skan #123 (fol. 60r) ---
oznajmując że ma w tym tłumaku złotych dwanaście z chustą
zgrzebną z worka za groszy dwadzieścia okradzioną
zrobienie szwady iterum przeżegnawszy się pokazał chustę
z krwią.

Sub eodem Actu
Ex Instantia Infidelis Lewko Mercatoris incolae Crasnicensis
1us Testis Simon Karczmarczyk de Suburbio Crasnicensi
dicto Zalesie Recognovit w Piątek niedawno przeszły
stojąc na gościńcu przed Bractwem widziałem że Parobka
Michała Piotrowczyka pomieniony Lewek wziął za miarę pa-
trząc żeby co nie kradł tylko poznał płótna z worka nie po-
znawał w tymże wziął jego rozpędował y w kieszeni
szukał Nic nie naleźli y też widziałem że konia
chcieli wyprzęgać y turbowali go u wozu On nie ucie-
kał z wozu ale po spłodzeniu dobrowolnie wyje-
chał y mówił to że mój Parobek do tegoż Lewka
drugi pytał co masz w worku iaki by rzekł futro
nie słyszałem Ultra nihil Recognovit tacto pectore
Recognovit sub Juramento.

2dus Testis Pracowity Marcin Błażejczyk stary poddany
do Arendy P. Kwasa przydany zeznał in haec formalia
zabrałem się z rana u P. Kwasa w sieni w Piątek w południe
w tym Lewek z drugiemi Żydami byli też po płótnie
Żydzi przeszli wóz Michała Piotrowczyka y Barankowi-
ca co przyjechał z Jarmarku nic nie naleźli w mieszku
obojga przeszli bom słyszał między jeżeli nie ma płótna
czy jeżeli nie przeszli rzeczy na Jarmarku albo w drodze
nie widziałem żeby z worka albo skąd płótno wyjęto było
tylko mówi sprawiedliwie y pokazał sam rzekł.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 124,
        "numer_pozycji": "124",
        "strona_pagina": "fol. 60v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Zeznania, dylacja i ugoda",
        "osoby_podmioty": "Michał Piotrowczyk, Grzegorz Maciej (świadek?), Adam Szołtys [?], Tomasz Kępa (świadek), Jan Kępka (przedmieszczanin), Matyjasz Kępa, Jakub Lis, Sebastian Rodzonek",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dalsze zeznania na instancję Michała Piotrowczyka i Grzegorza Macieja oraz Tomasza Kępy w sprawie sporu o płótno z Żydem. Następnie dylacja w sprawie Jana Kępki przeciw Michałowi Piotrowczykowi o grunt po Matyjaszu Kępie oraz ugoda Jakuba Lisa z Sebastianem Rodzonkiem o ulicę.",
        "transkrypcja": """--- Skan #124 (fol. 60v) ---
z dzwonkiem nie pomniemy przy sprzedaży iak rzekł nie
brałem mu nic ani siłą w płótnie sub Juramento.

Ex Instantia H. Michaelis Piotrowczyk et H. Gregori Macieja
1us Recognovit staliśmy sobie na przedmieściu przed p.
Ferdynanda przyszedł do mnie Żyd Krawiec rzekł
że skradziono mi z grosza że płótno wyjęto z pod wor-
ka y z chusty odebrano z nim parobek a on z nami
żebraka za kradzież pytał Jam odpowiedział nie miałem
tu żadnej z płótna o co mię pytasz tacto pectore Ultra
nihil scit.

2dus Testis H. Thomas Kępa Recognovit Byli
H. z Wantuchen[?] y z innymi na stoły przy pa-
howatensie z markaczynem zacięto mnie za kuśnierza
pościć obaczyć płótno w rozbiatek Kupionego syna
płótno rzekł że kawałek płótna ale nie wiem skąd
pożyczyć wyprzedał parobek z sieni dobrowolnie.

W sprawie y Akciej między Uciwym Janem Kępką Przedmie-
szczaninem Krasnickim Aktorem a Michałem Piotrow-
czykiem Przedmieszczaninem także o miasto z approbacji
na gront od nieboszczyka Matyasza Kępy nabytego nie do-
syć uczynienia dekretowi datur dilatio ad Quindenam
producant Jura ad metet status Consuccessores pro
eadem prima Juris & Terminus Conservatur.

Przed Urzędem y Aktami niniejszemi w osobach swoich
stanąwszy Uciwy Jakub Lis y Sobestian Rodzonek Przed-
mieszczanie Krasniccy Sąsiedzi w zgodzie iednajcie się
o różnicy personaliter Comparentes zeznali praesentibus że
mają być według zgody między sobą około Ulicy na""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 125,
        "numer_pozycji": "125",
        "strona_pagina": "fol. 61r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1702",
        "kategoria": "Sąd Wójtowsko-Ławniczy / Protestacja żydowska o pobicie syna",
        "osoby_podmioty": "Jakub Lis, Sebastian Rodzonek, Dawidowa (obywatelka kraśnicka, wdowa po Dawidzie Germanie), Dawid German (zmarły), Józef Macal (mieszczanin), Anna Macalowa, Wojciech Kłos (syn), Dawid (syn Dawidowej)",
        "kwoty_podatki": "Brak",
        "opis_sprawy": "Dokończenie komplanacji Jakuba Lisa z Sebastianem Rodzonkiem. Następnie sesja z 23 II 1702 r. (w wigilię św. Macieja Apostoła): protestacja starozakonnej Dawidowej (wdowy po Dawidzie Germanie) przeciw mieszczaninowi Józefowi Macalowi, jego żonie Annie i synowi Wojciechowi Kłosowi o pobicie jej syna Dawida i wepchnięcie go w błoto. Na dole początek sesji z 25 II 1702 r.",
        "transkrypcja": """--- Skan #125 (fol. 61r) ---
Górach przedmieściu Krasnickim zadasz sobie uczynili wejty
zgody sąsiadami osiadłemi Vadium grzywien dwoje z aktor
na złe z tendencjami w Komplanacji wyrażonemi trzymać
powinni successores swoich.

Actum Coram Officio Advocatiali et Scabinali Crasni-
censi Feria Quinta in Vigilia Festi Sancti Mathiae
Apostoli Anno Domini Millesimo Septingentesimo Secundo.

Do Urzędu y Akt niniejszych w osobie swoiej przyszedłszy Nie-
wierna Dawidowa Obywatelka Krasnicka Niewiernego
Dawida Germana Obywatela Krasnickiego małżonka solen-
nie protestowała się przeciwko Uciwym Józefowi Macalo-
wi Mieszczaninowi Krasnickiemu y Annie małżonkom Oto Iż
Oni synowi swemu Wojciechowi Kłosowi pozwalali do pisma
który lubo w młodym wieku swawoli dopuszczenia onego nie ma
w czym zmartwionego Dawida syna pomienionej protestantki
syna dającego sobie po potrzebie od tejże Matki do Lichowskiej
na dobrowolnej drodze na Przedmieściu Krasnickim Bże
w dzień z rany w błoto wepchnąć gdzie nóż lewy
wywinął sobie czyli też rana fractum z statusie
jak się po tym pokaże stłuczonej tym się nie kontentuiąc
w błocie topił go nogami bił gdzie Matka zbiegała
Matka żałosna obroniła szwank syna swego y protestowa-
ła się przeciwko Rodzicom o damę przywoli temuż synowi
oraz synowi swawolnemu obiecując prawnie dochodzić
In Cuius Verificationem protestationis praesentis poka-
zała syna swego skalanego w błocie zbitą Offerens eandem
Violentias Jure Vindicaturam Velle.

Actum Coram Officio Sabbato in Crastino Festi Sancti
Matthiae Apostoli Anno Millesimo Septin-
gentesimo Secundo.""",
        "link_swa": UNIT_LINK
    }
]

main_data.extend(part5_scans)
assert len(main_data) == 125, f"Expected 125 scans, got {len(main_data)}"

with open('/home/ubuntu/workspace/Gen/main_data_j18_part5.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j18_part5.json: {len(main_data)} skanów.")
