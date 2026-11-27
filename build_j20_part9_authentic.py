# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j20_part8.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
SYGN = "35/40/0/1/20"

part9_scans = [
    {
        "nr_skanu": 201,
        "numer_pozycji": "201",
        "strona_pagina": "fol. 100v (100v)",
        "sygnatura": SYGN,
        "data_rok": "1664",
        "kategoria": "Ugoda Kaspra i Sebastiana Jajczyków (220 złp) oraz dekret Łosików",
        "osoby_podmioty": "Kasper Jajczyk, Sebastian Jajczyk, Katarzyna Łosika [Łożyka?], Agnieszka (córka Katarzyny Łosiki), Magdalena Piotra Łowna",
        "kwoty_podatki": "220 złp (200 + 20 złp); 3 zł 15 gr",
        "opis_sprawy": "Dokończenie ugody między Kasprem Jajczykiem a Sebastianem Jajczykiem z 1664 r.: pozwany zobowiązuje się spłacić 220 złp długu po zmarłym ojcu Kaspra (2 zł na koszty prawne w najbliższą niedzielę, 120 zł nazajutrz po jarmarku kraśnickim po niedzieli Laetare i resztę 100 zł na św. Michała); poniżej początek dekretu w sprawie Katarzyny Łosiki [?] z córką Agnieszką przeciw Magdalenie Piotra Łownej.",
        "transkrypcja": """100v.
między sobą in facie Judicii praesentis taką uczynili: Wy płaca z pozwaney dług Aktorowi przez Nieboszczyka Ojca swego u Opiekunów Aktora Kaspra Jajczyka na ten czas jeszcze małoletniego zaciągniony, tedy pozwolił pozwany Aktorowi oddać nie czekając dalszego zawodu prawnego summę złotych Dwieście Dwadzieścia Polskich wraz z nakładami prawnemi. Na co Kasper Jajczyk Aktor przystał y pozwolił. Które to złote dwieście dwadzieścia takim sposobem wypłacać pozwany Aktorowi submittował się bez żadney turbacyi prawney: Naprzód złotych dwa ma mu oddać względem nakładów prawnych da Pan Bóg w przyszłą Niedzielę, a na summę złotych sto dwadzieścia nazajutrz po Jarmarku Kraśnickim po Niedzieli Laetare w tym teraźniejszym roku tu przypadającym, ostatek zaś to iest sto złotych submittował się oddać na S. Michała blisko przyszły w roku także teraźniejszym bez żadney turbacyi prawney. Na czym Aktor pomieniony Kasper Jajczyk przystał. In continenti Dekretem stronie pozwaney in ten sprawie cassuiąc i anni sibi iąc, ale się tą złotych dwieście do zapłacenia assekurowanych kontentuie obligując się swoimi y Sukcessorów swoich imieniem pomienionego pozwanego przy oddaniu ostatniej raty totaliter quitować wiecznymi czasy in forma Quitationis quam plenissima atque perfectissima. Co strony obiedwie prosili żeby było pamięciom zapisano. Co otrzymali. Quod est Actis connotatum.

Inter Catharinam Łosika [Łożyka?] et filiam eius Agnetem Actrices et Magdalenam Piotra Łowna.
Na terminie dzisieyszym zawitym stronom przez Dekret na...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 202,
        "numer_pozycji": "202",
        "strona_pagina": "fol. 101r (101 / 97)",
        "sygnatura": SYGN,
        "data_rok": "1664",
        "kategoria": "Sprawa Katarzyny Łosiki o 3 zł 15 gr oraz proces Piotra Muszki z Tomaszem Jajczykiem o włamanie do komory",
        "osoby_podmioty": "Katarzyna Łosika [Łożyka?], Magdalena Piotra Łowna, Piotr Muszka, Tomasz Jajczyk, Jakub Smazanowski",
        "kwoty_podatki": "3 zł 15 gr",
        "opis_sprawy": "Dokończenie dekretu w sprawie Katarzyny Łosiki (wydzielenie śnieży/roli za 3 zł 15 gr); poniżej sprawa Piotra Muszki przeciw Tomaszowi Jajczykowi (mieszkającemu u sławetnego Jakuba Smazanowskiego) o nocne włamanie do komory przez poszycie, kradzież zboża, gorsetu/garnka, dwóch worków i siekierki oraz późniejsze pobicie powoda wracającego z kościoła (zadane 7 razów); pozwany wypiera się kradzieży i powołuje świadka Jakuba Smazanowskiego, lecz przyznaje się do pobicia.",
        "transkrypcja": """101. [u dołu: 97.]
trzech złotych groszy piętnastu Sąd ninieyszy przy podawaniu Intromissyi ex integro onego role Aktorowi ma wydzielić śnieży która na tym polu zostaie tym nakładom correspondens którą wydzieloną wolno będzie Aktorowi ujmując po naszey postęp obrócić y tym sobie nakłady zapłacić. Quod ab utraque parte susceptum.

Inter Petrum Muszka Actorem et Thomam Jajczyk Citatum.
Proponował y skarżył się Aktor według propozycyi swey in parata Copia podanej na Tomasza Jajczyka to iest o to że Citatus w onej komorze jego dobywszy się nocnym sposobem do komory jego przez poszycie y iuskę byst zboża nabrał, ale tego przez czas postrzegł y usłyszał kołat w komorze uchyłił się tego Jajczyka znając go dobrze a drugi uciekł iednak mu się wydart z garści a worów dwóch y siekierki odbiegł które Sądowi prezentował. Owo gdy się przed ludźmi onego znemi oskarżał Tomasz Jajczyk pewnego czasu idącego z kościoła na dobrowolnej drodze pobił y razy pozadawał iemu Aktorowi iako obductia szerzey świadczy żądając z niego sprawiedliwości y biorąc się na świadki o to pobicie.
Citatus odpowiedział nie znając się do dobycia komory obmawiając niewinność swoią że nigdy tego nie uczynił y nawet ani iest niczym podejrzany ani to wory są jego ani siekierka stawiając Sławetnego Jakuba Smazanowskiego u którego mieszka ten zeznał że nigdy podejrzany nie iest y nie widział u niego, do pobicia przyznał się dając racią że go szkalował y przed ludźmi złodziejem czynił o co się z nim ująwszy pobił go.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 203,
        "numer_pozycji": "203",
        "strona_pagina": "fol. 101v (101v)",
        "sygnatura": SYGN,
        "data_rok": "1664",
        "kategoria": "Wyrok w sporze Muszki z Jajczykiem oraz sprawa Macieja Lisika z Andrzejem Macalem o jęczmień",
        "osoby_podmioty": "Piotr Muszka, Tomasz Jajczyk, Maciej Lisik, Andrzej Macal, Gabriel Bąk [?] (zm.)",
        "kwoty_podatki": "-",
        "opis_sprawy": "Wyrok w sprawie Piotra Muszki przeciw Tomaszowi Jajczykowi: ponieważ powód nie ma świadków na włamanie do komory, a jedynie poszlaki (wory i siekierkę), sąd nakazuje pozwanemu oczyścić się przysięgą w piątek, zaś na pobicie powód ma stawić świadków; poniżej sprawa Macieja Lisika przeciw Andrzejowi Macalowi i jego małżonce o dziesięcinę jęczmienia po zmarłym pierwszym mężu pozwanej Gabrielu Bąku [?].",
        "transkrypcja": """101v.
Sąd ninieyszy wysłuchawszy pilno stron obydwu kontrowersye to iest zważywszy lubo Aktor żadnych świadków przeciwko pozwanemu nie ma aby on miał w komorze jego być y zboże kraść y nie iest notatus pozwany żadną suspycyą, iednakże Aktor prezentował zaraz przed sądem wory odjęte y siekierkę co mu ją wydarł y w oczy mu mówi że jego własne w komorze uciekł... a w kościele to się działo przez co nieiaka coniectura iest według Prawa iako w wątpliwey sprawie propior uznawszy Citatum ad evadendum nakazuie aby pozwany w Piątek blisko przyszły przysiągł in eam Juramenti Rotam iako on nie iest uczynią tego o co mu Aktor winę dał y wory to nie są jego ani siekierka y nie wie czyie. Quo praestito liber in hoc puncto zostawać ma y nie ma to Aktorowi szkodzić ani jego imieniu, co zaś tycze pobicia ma Aktor stawić świadków na których się zabiera dla lepszego wyrozumienia z jakiej okazyi to się pobicie stało na Piątek blisko przyszły termin stronom zawity naznaczając. Quod est Actis connotatum.

Inter Mathiam Lisik Actorem et Andream Macal atque suam Consortem eius Citatos.
Skarżył się Aktor na pozwanych małżonków o Dziesięcinę Jęczmienia jeszcze przez nieboszczyka Gabriela Bąka [?] małżonka pierwszego pozwaney kupnym sposobem wziętą żądając aby pozwana strona pomieniony jęczmień onemu zapłaciła za który lubo przez tak długi czas czekał zapłaty tedy to uczynił za uproszeniem pozwaney strony którey go prosiła żeby na nich o to przed Urzędem nie skarżył. In oppositis pozwani personaliter comparentes...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 204,
        "numer_pozycji": "204",
        "strona_pagina": "fol. 102r (102 / 98)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dekret dla cechu kuśnierskiego (Stanisław Luterski) oraz kontumacje Bartoszka i Mutkowica",
        "osoby_podmioty": "Stanisław Luterski (brat cechu kuśnierskiego), Stanisław Jesurkiewicz, Wawrzyniec Bielaszkowic, Adam Michał Chmielowicz (pisarz), Stanisław Solecki, Jan Barankowicz, Grzegorz Bartoszek, Jan Smorzik [?], Tomasz Mutkowic, Szymon Solecki",
        "kwoty_podatki": "3 grzywny",
        "opis_sprawy": "Powrót do roku 1698 (22 października 1698 r., Feria Quarta post Festum S. Lucae): dekret w sprawie Stanisława Luterskiego przedmieszczanina i brata cechu kuśnierskiego kraśnickiego przeciw cechowi kuśnierskiemu (wobec Stanisława Jesurkiewicza, Wawrzyńca Bielaszkowica i cechu kuśnierskiego) — sąd nakazuje rewizję ksiąg i przywilejów przez deputowanych (pisarza Adama Michała Chmielowica, Stanisława Soleckiego, Jana Barankowicza rajców i starszych cechowych); poniżej kontumacja Jana Smorzika [?] z instancji Grzegorza Bartoszka oraz kara 3 grzywien dla Szymona Soleckiego majstra szewskiego z instancji towarzysza Tomasza Mutkowica.",
        "transkrypcja": """102. [u dołu: 98.]
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quarta post Festum Sancti Lucae Apostoli et Evangelistae proxima die 22 8bris Ao 1698 [22 X 1698].
W sprawie y Akcyey między Uciwym Stanisławem Luterskim Przedmieszczaninem Bratem Cechu Kuśnierskiego Kraśnickiego Aktorem ad contenta propositionis jego z iedney y Cechu Kuśnierskiego przez Sławetnych P. Stanisława Jesurkiewicza, Wawrzyńca Bielaszkowica Cechmistrzów et aliorum confratrum... exauditis et debite intellectis Decernuie Sąd Wójtowski y Ławniczy Kraśnicki aby dnia jutrzeyszego mutuo partium sumptu cognitio stanęła aequitatis et iustitiae circa productionem iurium privilegiorum ad quam peragendam deputowani PP. Adam Michał Chmielowic Pisarz Kraśnicki, Stanisława Soleckiego, Jana Barankowicza Radców y innych z bedelem contubernii cechmistrzów delegat postquam peractam... terminus sine ulla adcitatione suo coram Officio comparendi conservatur.

Ex Instantia H. Gregorii Bartoszek Actoris H. Joannes Smorzik [?] contumax ratione suspitionis furti obiectionis. In cuius contumaciam decernitur solutio poenae trium Marcarum parti et Officio luenda...

Ex Instantia H. Thomae Mutkowic artis sutoriae socii H. Simon Solecki Magister eiusdem artis denuntiatione consorti ipsius denuntiando luendae solutionis Marcarum trium parti et Officio per medium solvenda una cum litis expensis.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 205,
        "numer_pozycji": "205",
        "strona_pagina": "fol. 102v (102v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Protestacje Grzegorza Bartoszka przeciw Smorzikowi i Pawła Kozaka przeciw Rdzonkom",
        "osoby_podmioty": "Grzegorz Bartoszek, Jan Smorzik [?], Paweł Kozak, Wojciech Rdzonek [Rozdzeń?], Bartłomiej Rdzonek [Rozdzeń?], Zofia Rdzonkowa [Rozdzeniowa?], Paweł Słomkowski, Wojciech Dzymanowski [Dzimanowski?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie poprzedniego wpisu; protestacja Grzegorza Bartoszka przeciw Janowi Smorzikowi [?] o niesłuszne posądzenie o kradzież bydlęcia w ogrodzie; poniżej pod datą 22 października 1698 r. protestacja i obdukcja ran przedmieszczanina Pawła Kozaka przeciw Wojciechowi Rdzonkowi [?], jego ojcu Bartłomiejowi i Zofii Rdzonkowej o pobicie na drodze publicznej (podrapania na lewej ręce i łopatce), oglądanych przez wicewójta Pawła Słomkowskiego i ławnika Wojciecha Dzymanowskiego [?].",
        "transkrypcja": """102v.
kożusznika nuzko pili y prosili Panie albo nam ustąpić swoiey dolegliwości które osobnym processem tłumaczyć vindicowac declarant de quibus praemissis iterum atque iterum testatur et manifestatur.

Sub eodem Actu.
Videatur protestatio facta H. Gregorii Bartoszek contra H. Joannem Smorzik [?] idque in eo że on lubo z szkody swojej którą słusznie niesłusznie pretenduie sobie za tę kłaczę protestanta w sobotę niedawno przeszłą bez szkody... iednak na kunę protestanta nagle zezłościł gwałtownie aż porozbijał, tandem kiedy około tey kłaczy obsyłał protestant odpowiedział his formalibus niech mi wrych wróci krowami w ogrodzie ukradł do szkody przydał detractionem sławy y reputacyi ludzi złodziejstwo zadać poważył się o co iterum atque iterum protestatur.

Actum coram Officio Advocatiali et Scabinali Crasnicensi Feria Quarta post Festum Sancti Lucae Apostoli et Evangelistae die 22 8bris [1698].
Videatur hoc loco Protestatio facta una cum Obductione Vulnerum infrascripti H. Pauli Kozak suburbani Crasnicensis adversus HH. Albertum Bartolomeum Rdzonek [Rozdzeń?] patrem et filium atque Sophiam eiusdem Bartholomei Rdzonek consortem... violentiam ratione per eosdem graminis in primario kadnikow... eundemque protestantem in via publica et libera... praesentavit vulnera sibi indita coram eisdem praesentibus FF. Paulo Słomkowski Viceadvocato, Alberto Dzymanowski [Dzimanowski?] Scabino Jurato Judicii seu Officii Advocatialis et Scabinalis Crasnicensis: na lewey ręce zdrapany na paznogcie Item linie na plecy zego wrzodami po łopatkach y... czterech palców bili widzieliśmy.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 206,
        "numer_pozycji": "206",
        "strona_pagina": "fol. 103r (103 / 99)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Skarga Matyjasza Skarza na wójta gromadzkiego Wojciecha oraz zeznanie o Marcina Rymarczyka",
        "osoby_podmioty": "Matyjasz Skarz [?], Wojciech [wójt gromadzki], Marcin Rymarczyk, Jan Stryczak [Struczak?], Matyjasz Skowronek [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Skarga Matyjasza Skarza [?] przeciw wójtowi gromadzkiemu Wojciechowi o pobicie laską i znieważenie ubóstwa przy składce gromadzkiej ('tyś bogaty, żonę bogatą pojąłeś'); poniżej odroczenie sprawy przez sąd do dnia następnego z wyznaczeniem delegatów; na dole zeznanie świadka Matyjasza Skowronka [?] z instancji Marcina Rymarczyka o żonie Jana Stryczaka [Struczaka?].",
        "transkrypcja": """103. [u dołu: 99.]
pomieniony Matyasz Skarz [?] powtórnie requirowany na folwark poszedł y okrutnie znieważył wójta gromadzkiego w te słowa: żona uboga iest człowiek a tyś bogaty żeś żonę bogatą pojął na żonę a mnie trzeba na składkę zaraz bieżeć... Matyasz Skarz mówił przeciwko pomienionemu Wójtowi Gromadzkiemu Wojciechowi z Karczówki: jużeście dawno folwark byli kończyć gdybyś był drugim sąsiadom nie folgował y na swoje strony roboty ich nie folgował... w tym młody się pomieniony Wójt Gromadzki za temi słowami uderzył go laską iako obductia opiewa szerzey.

Sub Eodem Actu.
Ponieważ strony pomienione in litigium między sobą zaszły libere Sądu upraszają aby się między sobą pogodzili dnia dzisieyszego którey affectacyey dosyć czyniąc pozwolili y nakazali aby w inszenty uproszonych Panów przyjaciół ex Officio assidentów wysadzili pod winami przed sąd opatrzonymi poszukuje... terminus conservatur peremptorius.

Sub Eodem Actu.
Ex Instantia Honesti Martini Rymarczyk Suburbani Crasnicensis H. Mathias Skowronek [?] tacto pectore recognovit że in via Judiciali circa agitationem causarum zabita Stryczakowa Janowa pomienionego Marcina Rymarczyka w te słowa nazwała...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 207,
        "numer_pozycji": "207",
        "strona_pagina": "fol. 103v (103v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Kontumacje (Jakub Kłopot, Tomasz Nowacki, Adam Kowalczyk, Maciej Peron i Wojciech Wawrzyło)",
        "osoby_podmioty": "Jakub Kłopot, Tomasz Nowacki, Wojciech Bożkowic, Adam Kowalczyk [?], Maciej Peron, Wojciech Wawrzyło, Wojciech Peron, Jakub Wawrzyło, Paweł Słomkowski",
        "kwoty_podatki": "3 grzywny",
        "opis_sprawy": "Dokończenie zeznania o żonie Stryczaka i ćwierci roli wiatrakowej; druga kontumacja Jakuba Kłopota z instancji Tomasza Nowackiego o wypasioną potrawę; pierwsza kontumacja Adama Kowalczyka [?] z instancji ławnika Wojciecha Bożkowica o dług; kontumacja Macieja Perona z bratem Wojciechem Wawrzyłem i synami Wojciechem Peronem i Jakubem Wawrzyłem z instancji wicewójta Pawła Słomkowskiego o szkodę w sześćdziesiątkach żyta (kara 3 grzywien).",
        "transkrypcja": """103v.
chcąc alberową ćwierć roli za kosą wyfałdować od Wiatraka bo iey nic nie mówił tylko oświadczysz.
Super Jacobo Kłopot Suburbano Crasnicensi ex Instantia H. Thomae Nowacki itidem Crasnicensis ratione damni illationis o wypasioną potrawę 2do contumax.
[Na marginesie: Honestus Jacobus Kłopot citatus contumax.]
In contumaciam na affectatią strony powodowey przez familię do sądu swego captivandam ex Officio calligari fecit.

Sub Eodem Actu.
Na Instantią Sławetnego Pana Wojciecha Bożkowica Ławnika Kraśnickiego przeciwko Uciwemu Adamowi Kowalczykowi [?] annotata contuma na primo względem długu pewnego z tąż stroną.

Sub Eodem Actu.
Super Honesto Mathia Peron Suburbano Crasnicensi et fratre Alberto Wawrzyło dicto itidem itidem Crasnicensi nec non statutionis filiorum suorum unius Alberti Peron Jacobi Wawrzyło respectu damnorum illationis siliginis ex sexagenis interceptionis tam ipsi Actori quam famulo ipsius ex parte Famati Pauli Słomkowski Viceadvocati Crasnicensis ex termino praeservato decernitur Contumax. In quorum contumacia decernit poena tam super persona patrum quam et filiorum per ipsos statuendorum trium Marcarum exolvenda solutio.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 208,
        "numer_pozycji": "208",
        "strona_pagina": "fol. 104r (104 / 100)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dekret w sporze dziesiętnika Pawła Kłopota z Matyjaszem Skarzem o składkę i pobicie",
        "osoby_podmioty": "Matyjasz Skarz [?], Paweł Kłopot (dziesiętnik przedmiejski)",
        "kwoty_podatki": "2 złp (składka); 2 grzywny; 3 dni wieży",
        "opis_sprawy": "Skarga przedmieszczanina Matyjasza Skarza [?] przeciw przedmieszczaninowi Pawłowi Kłopotowi, pełniącemu wówczas funkcję dziesiętnika przedmiejskiego, że przy zbieraniu składki 2 złp zabił/pobił powoda; Paweł Kłopot przysięga, iż żadnych dwóch złotych dla siebie nie brał ani pierwszy nie uderzył; sąd nakazuje Kłopotowi 3 dni wieży i 2 grzywny kary oraz zwrot kosztów prawnych.",
        "transkrypcja": """104. [u dołu: 100.]
Sub Eodem Actu.
Na Terminie dzisieyszym stanąwszy Uciwy Matyasz Skarz [?] przedmieszczanin Kraśnicki wniósł skargę naprzeciw Uciwemu Pawłowi Kłopotowi przedmieszczaninowi na ten czas Dziesiętnikowi Przedmieścia tegoż Miasta Kraśnika iż on zupełnie wybrawszy składkę... od Aktora iako protestacyą obducia świadczy gdy dwóch złotych dany a z drugi raz Aktora pobił. Ex adverso pars citata przyznała że wprawdzie... ale dla przyczyn danie my domówieniem stawanie nienależytym. Sąd ninieyszy Kraśnicki Wójtowski y Ławniczy zabiegając dalszym niesnaskom między sąsiadami nakazał aby pomieniony Uciwy Paweł Kłopot przysiągł się w pierwszym zaprzysiężeniu po sumieniem zeznał iż tych dwóch złotych o które rzecz w sprawie y świadka stała się nie brał ani na rękę żadną sedł na Aktora pobić Aktora do którego się przyznał pozwany. Uważając Sąd pomieniony y powinien być pozwany za prawem... zeznał y dekretem ninieyszym nakazuie pozwanemu aby w więzieniu siedział in instanti y one kontynuował bez dni trzy grzywien dwie parti et Judicio per medium oddał y nakłady zastąpił koszta prawne.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 209,
        "numer_pozycji": "209",
        "strona_pagina": "fol. 104r (104 / 100 — dublet mikrofilmu)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dublet mikrofilmu karty fol. 104r (powtórzony skan #208)",
        "osoby_podmioty": "Matyjasz Skarz [?], Paweł Kłopot (dziesiętnik przedmiejski)",
        "kwoty_podatki": "2 złp; 2 grzywny; 3 dni wieży",
        "opis_sprawy": "Powtórna klatka mikrofilmowa strony fol. 104r (104 / 100) — treść identyczna ze skanem #208 (sprawa Matyjasza Skarza [?] przeciw dziesiętnikowi Pawłowi Kłopotowi).",
        "transkrypcja": """[Dublet mikrofilmu karty fol. 104r (104 / 100) — pełny odczyt tekstu jak na skanie #208.]
104. [u dołu: 100.]
Sub Eodem Actu.
Na Terminie dzisieyszym stanąwszy Uciwy Matyasz Skarz [?] przedmieszczanin Kraśnicki wniósł skargę naprzeciw Uciwemu Pawłowi Kłopotowi przedmieszczaninowi na ten czas Dziesiętnikowi Przedmieścia tegoż Miasta Kraśnika... [treść identyczna ze skanem #208].""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 210,
        "numer_pozycji": "210",
        "strona_pagina": "fol. 104v (104v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Spór Matyjasza Skarza z Wojciechem Tokarczykiem i zeznanie dziesiętnika Pawła Kłopota",
        "osoby_podmioty": "Matyjasz Skarz [?], Wojciech Tokarczyk, Paweł Kłopot (dziesiętnik), żona Matyjasza Skarza",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie dekretu z 104r; sprawa między Matyjaszem Skarzem [?] a Wojciechem Tokarczykiem o pobicie (dylacja na inkwizycję); zeznanie 1. świadka Pawła Kłopota, iż z urzędu dziesiętnika miejskiego poszedł z urzędem do Matyjasza Skarza po należną składkę na folwark, a żona Skarza wygnała ich z kijem z domu; na dole odwrócony (do góry nogami) dopisek kancelaryjny o Agnieszce żonie Matyjasza.",
        "transkrypcja": """104v.
przywrócił idque non recedendo sub poena grzywny... per Officium adinveniendae... ad exequendum feria sexta proxime ventura sine ulla adcitatione peremptorie.

Inter Honestos Mathiam Skarz [?] Actorem et Albertum Tokarczyk Citatum idque ratione contusionis per Citatum Actori factae datur dilatio Inquisitionis quatenus in instanti cum testibus compareat eorundemque testimonia de verbo ad verbum descripta in praesentia suprascriptorum Dnorum assidentium Judicii exaudiant et connotentur.

1mus Testis. Honestus Paulus Kłopot suburbanus Crasnicensis recognovit fideliter in haec formalia: Chodziłem po składkę o folwark z urzędu mieyskiego y poszliśmy do Uciwego Matyasza Skarza [?] więc w tym tamże kiedyśmy requirowali od niego aby oddał składkę należytą na folwark przyszedł gdy żona jego w tym czasie z kijem na nas z domu wygnała... znowu że nie chciał oddać...
[Na dole karty dopisek odwrócony do góry nogami o Agnieszce żonie aktora i terminie poniedziałkowym.]""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 211,
        "numer_pozycji": "211",
        "strona_pagina": "fol. 105r (105 / 101)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Obdukcja pobicia Jędrzeja Berkowskiego oraz skarga Piotra Tokarczyka na opiekunów o dom w Rynku",
        "osoby_podmioty": "Jędrzej Berkowski [?], Stefan Kwasowic, Wojciech Grzymałowski, Matyjasz Skarz [?], Piotr Tokarczyk, Szymon Kościński, rajca Jan Majowski",
        "kwoty_podatki": "-",
        "opis_sprawy": "Obdukcja ran pobitego (Jędrzeja Berkowskiego [?]) przed ławnikami Stefanem Kwasowicem i Wojciechem Grzymałowskim (włóczenie za włosy, guzy na boku i ręce, zapowiedź dochodzenia na Matyaszu Skarzu [?] / Maruszewskim [?]); poniżej pod datą 23 lipca 1698 r. (Feria Quarta in Crastino Festi S. Mariae Magdalenae) skarga przedmieszczanina Piotra Tokarczyka przeciw opiekunom Wojciechowi Grzymałowskiemu i Szymonowi Kościńskiemu o sprzedanie domu w Rynku po ojcu rajcy Janowi Majowskiemu bez wydzielenia pieniędzy sukcesorom.",
        "transkrypcja": """105. [1698. | u dołu: 101.]
Sub eodem Actu. Videatur Protestatio una cum obductione vulnerum Laboriosi Andrae Berkowski [?]... praesentavit przed PP. Wojciechem Grzymałowskim y Stephanem Kwasowicem... iż bez dania żadney okazyi... za włosy porwawszy nie tylko włóczył... na boku prawym guz wielki, na lewey ręce na łokciu sine... o co iterum protestatur przeciwko Sławetnemu P. Maruszewskiemu [Skarzowi?].

Actum Feria Quarta in Crastino Festi Sctae Mariae Magdalenae Anno 1698vo [23 VII 1698].
Na terminie dzisieyszym stanąwszy Uciwy Piotr Tokarczyk Przedmieszczanin Kraśnicki wniósł skargę na przeciw Sławetnemu P. Wojciechowi Grzymałowskiemu Mieszczaninowi Kraśnickiemu tudzież... opiekunom uproszonym do SS. Pana Szymona Kościńskiego a oyca Aktora do dźwigowania dóbr które po nim zostały. Dom w mieście leżący w Rynku przedał P. Janowi Majowskiemu Rajcy Kraśnickiemu pieniądze zaś niewiemy gdzie podział naymnieyszego grosza nam sukcessorom do używania niedał ani dać chce. Ex adverso pars citata odpowiedziała nie dając tego... iż ia miał jakie czynsze brać... ale że mi P. Majowski iuż nie oddał, prosił przynajmniej do środy blisko przyszłey dylacyi aby go obesłać co mi na to odpowie. Któremu pozwolona iest. Quod connotatum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 212,
        "numer_pozycji": "212",
        "strona_pagina": "fol. 105v (105v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Sprawy z 21 VII 1698 r.: Kłopot, Tokarczyk, Michalski vs Biegajczyk i skarga Borona",
        "osoby_podmioty": "Wojciech Kłopot, Piotr Tokarczyk, Szymon Kościński, Wojciech Grzymałowski, Adam Potokowicz [Potocki], Kazimierz Michalski, Stanisław Biegajczyk [?], Jan Wierzuk [?], Matyjasz Boron [?]",
        "kwoty_podatki": "3 grzywny; 2 grzywny",
        "opis_sprawy": "Pod datą 21 lipca 1698 r. (Feria Secunda pridie Festi S. Mariae Magdalenae): kara 3 grzywien i 3 dni wieży na Wojciecha Kłopota; dylacja w sprawie Piotra Tokarczyka przeciw opiekunom Szymonowi Kościńskiemu, Wojciechowi Grzymałowskiemu i Adamowi Potokowiczowi; sprawa Kazimierza Michalskiego przeciw Stanisławowi Biegajczykowi [?]; kontumacja Jana Wierzuka [?] z instancji Wojciecha Grzymałowskiego (2 grzywny); skarga Matyasza Borona [?] o pobicie w sobotę na drodze do kościoła.",
        "transkrypcja": """105v.
Actum Feria Secunda pridie Festi S. Mariae Magdalenae proxima Anno 1698vo [21 VII 1698].
Super Albertus Kłopot ratione contumaciae... decernitur poena trium Marcarum et sessio trium dierum.
Inter Honestum Petrum Tokarczyk Actorem et Tutores Famati olim Simonis Kościński, scilicet Albertum Grzymałowski, F. Adamum Potokowicz Dilatio.

Sub eodem Actu.
Inter Famatum Casimirum Michalski Actorem et Stanislaum Biegajczyk [?] Citatum datur dilatio Inquisitionis ad feriam quartam proxime venturam.
Sub eodem Actu. Prima citatio Honesta Cechlina [?] citata contumax.
Ad Instantiam Famati Alberti Grzymałowski Honestus Joannes Wierzuk [?] contumax in cuius contumaciam decernitur poena duarum Marcarum parti et Judicio per medium.

Sub eodem Actu.
Do Urzędu y Akt ninieyszych w osobie swojey przyszedłszy Uciwy Matyasz Boron [?]... zaniósł skargę o pobicie w sobotę... kiedy szedł do kościoła... o co protestatur.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 213,
        "numer_pozycji": "213",
        "strona_pagina": "fol. 106r (106 / 102)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Intromisja Jana i Ewy Grotowskich oraz ugoda Jakuba Józefkowica z kowalem Janem Rygarem",
        "osoby_podmioty": "Jan Grotowski [?], Ewa Grotowska [?], Paweł Słomkowski, Wojciech Grzymałowski, Wawrzyniec Bielaszkowic, Jakub Józefkowic [Josepkowic], kowal Jan Rygar [?]",
        "kwoty_podatki": "14 grzywien (vadium)",
        "opis_sprawy": "Dokończenie poprzedniego wpisu; pod datą 23 marca 1698 r. (Feria Quarta ante Dominicam Palmarum) intromisja Jana i Ewy Grotowskich [?] w grunt i dobra nabyte za zgodą sukcesorów przy delegowanych z urzędu: Pawle Słomkowskim podwojcim, Wojciechu Grzymałowskim i Wawrzyńcu Bielaszkowicu ławnikach; poniżej pod tą samą datą przeprosiny i zgoda między pracowitym Jakubem Józefkowicem a Janem Rygarem [?] kowalem kraśnickim z vadium 14 grzywien przeciw dalszym kalumniom.",
        "transkrypcja": """106. [1698 | u dołu: 102.]
gospodarzom y mieszkać iako należy rząd y obronić, co się tylko skarga stała naydaley czterech niedziel po świętach Wielkonocnych quod Actis praesentibus connotatum et ab utraque parte susceptum.

Actum Feria Quarta ante Dominicam Palmarum Ao 1698 [23 III 1698].
[Na marginesie: Intromissio.] Do Urzędu y Akt niniejszych oblicznie stanąwszy Uciwy Jan y Ewa Grotowscy [?] potrzebę y myśl swoię publice uznali i koncessyą swoię... od ojców swoich nabyli y... sukcessorom jego za summę złotowych... dla lepszego stwierdzenia kupna tego prosili sławetnego Urzędu iuxta morem aby dana była Intromissia przy ludziach obecnych, do którey z Urzędu deputowani Sławetni Panowie Paweł Słomkowski Podwójci, Wojciech Grzymałowski, Wawrzyniec Bielaszkowic Ławnicy.

Actum Feria Quarta ante Dominicam Palmarum proxima Ao 1698 [23 III 1698].
Do Urzędu y Akt niniejszych Wójtowskich y Ławniczych przyszedłszy pracowity Jakub Josepkowic [Józefkowic] zeznał iż miał sprawę z Uciwym Janem Rygarem [?] Kowalem Kraśnickim którego publice przy zgodzie przeprosił y to co mu zadał odwołał, aby na potem takowych kalumnii żaden z nich nie wznawiał pod winą grzywien czternastu na co obie strony pozwoliły y przyjęły quod connotatum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 214,
        "numer_pozycji": "214",
        "strona_pagina": "fol. 106v (106v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Sprawy żydowskie (Moszek Koplowic, kantor synagogi Izaak vs Grymuza) i protestacja Chmielków",
        "osoby_podmioty": "Żyd Moszek Koplowic, Matyjasz Pilaskiewicz [Bielaszkowic?], kantor Izaak (Isaac Cantor Sinagogae), bedel Wojciech Ornatowski, Jan Grymuza, Żyd Jakub Moszek, Sebastian Chmielek, Anna Chmielkowa, Błażej Chmielek, Katarzyna Chmielkowa",
        "kwoty_podatki": "3 grzywny",
        "opis_sprawy": "Sprawa Żyda Moszka Koplowica przeciw Matyjaszowi Pilaskiewiczowi [?] (dylacja); pierwsza kontumacja Jana Grymuzy z instancji kantora synagogi kraśnickiej Izaaka (Isaac Cantoris Sinagogae Crasnicensis) przez bedela Wojciecha Ornatowskiego (kara 3 grzywien); sprawa Jakuba Moszka; poniżej pod datą 4 kwietnia 1698 r. (Feria Sexta ante Dominicam Conductus Paschae) protestacja Sebastiana i Anny Chmielków przeciw Błażejowi i Katarzynie Chmielkom o wstrzymywanie działu dóbr po zmarłych rodzicach i zelżenie żony protestanta w gospodzie.",
        "transkrypcja": """106v.
W sprawie między Niewiernym Moszkiem Koplowicem Aktorem a Sławetnym Panem Matyaszem Pilaskiewiczem [Bielaszkowicem?] Pozwanym o nie oddanie słowa do pozwanego... ponieważ z obydwu stron do zgody nie stanęli do lepszej informacyi sąd dylacyi pozwala.

Ex Instantia Infidelis Isaac Cantoris Sinagogae Crasnicensis ex relatione providi Alberti Ornatowski Bedelli prima citatio Citati Joannis Grymuza ratione non comparitionis decernitur poena trium Marcarum parti et Judicio per medium.

Jakub Moszek przypozwany będzie od...

Actum Feria Sexta ante Dominicam Conductus Paschae proxima 1698 [4 IV 1698].
Do Urzędu y Akt niniejszych W. Ł. K. oblicznie przyszedłszy Uciwi Sebastian y Anna Chmielkowie Sukcessorowie dóbr po nieboszczykach rodzicach swoich solennie protestowali się przeciw Uciwym Błażejowi y Katarzynie Chmielkom którzy nie dość że kilkanaście lat za żywota matki trzymali teraz po śmierci nie tylko dzielić ziemię chcą iako im część należy ale y na gospodzie Błażej Chmielek żonę protestanta zelżył słowy nieuczciwemi, o co przed sądem ofiarują się dochodzić de quo iterum atque iterum protestatur.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 215,
        "numer_pozycji": "215",
        "strona_pagina": "fol. 107r (107 / 103)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Wizje szkód polnych (Pradkowski, Koszykowic vs Abel) oraz skarga wdowy Elżbiety z Janem Okoniem na Adama Wilka",
        "osoby_podmioty": "Stanisław Pradkowski [?], Kazimierz (parobek Wojciecha Dubaja), Wojciech Dubaj, Kazimierz Oszmarowic [?], Wawrzyniec Bielaszkowic, Kazimierz Koszykowic [?], Paweł Abel, Stefan Bożkowic [?], Wawrzyniec Bożkowic [?], wdowa Elżbieta Okoniowa, Jan Okoń, Adam Wilk, Bakałowski, Sitarski",
        "kwoty_podatki": "110 złp; 85 złp; 25 złp",
        "opis_sprawy": "Pod datą 9 kwietnia 1698 r. (Feria Quarta post Dominicam Conductus Paschae) wizja szkody Stanisława Pradkowskiego [?] przeciw parobkowi Kazimierzowi od Wojciecha Dubaja; pod datą 11 kwietnia 1698 r. (Feria Sexta ante Dominicam Misericordiae) wizja Kazimierza Koszykowica [?] z Pawłem Ablem o niegrodzenie płotu (ławnicy Stefan i Wawrzyniec Bożkowicowie); na dole skarga wdowy Elżbiety z synem Janem Okoniem przeciw Adamowi Wilkowi o 110 złp za budynek/karczmę między mieszczanami Bakałowskim i Sitarskim (z czego oddał tylko 25 złp, a 85 złp zalega od św. Marcina 1697 r.).",
        "transkrypcja": """107. [u dołu: 103.]
Actum Feria Quarta post Dominicam Conductus Paschae proxima 1698 [9 IV 1698].
Na affectacyą Stanisława Pradkowskiego [?] do obejrzenia szkody uczynioney przez Kazimierza parobka Wojciecha Dubaja deputowani Panowie Kazimierz Oszmarowic [?] y Wawrzyniec Pilaszkowic z Urzędu Wójtowskiego Ławnicy przed tym że Urzędem zeznali iż tam tegoż czasu pusto pole... tylko iak może szkody co iest widziano.

Actum Feria Sexta ante Dominicam Misericordiae proxima 1698 [11 IV 1698].
Na affectacyą Uciwego Kazimierza Koszykowica [?] do obejrzenia szkody od Pawła Abla względem niegrodzenia ogrody który powinni zaraz oba grodzić deputowani Panowie Stephan Bożkowic Wawrzyniec Bożkowic Ławnicy przysięgli Kraśniccy takową przed Urzędem uczynili relacyą iż zeszedszy na grunt gdzie y P. Abel był uznali aby Paweł połowę grodził... szkody zaś żadney Panowie na ten czas nie widzieli tylko aby połowę płotu P. Abel postawił.

Sub eodem Actu.
Na terminie dzisieyszym oblicznie stanąwszy Uciwa Elżbieta niegdy Uciwego Matyasza [?] pozostała małżonka wespół z synem swoim Janem Okoniem wnieśli przed Urzędem niniejszym skargę przeciwko Adamowi Wilkowi iż on stargowawszy u Aktorki... między mieszczanami Bakałowskim i Sitarskim za złotych polskich sto dziesięć które summę miał wypłacać ratami trzema: pierwszą ratę przy stargowaniu tey karczmy, drugą ratę na Świątki, trzecią ratę na Święty Marcin w roku 1697, a teraz oddawszy tylko złotych dwadzieścia y pięć złotych reszty oddać nie chce.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 216,
        "numer_pozycji": "216",
        "strona_pagina": "fol. 107v (107v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dekret w sporze Elżbiety Okoniowej z Adamem Wilkiem (85 złp) oraz sprawa Koszykowica z Ablem",
        "osoby_podmioty": "Adam Wilk, Elżbieta Okoniowa, Jan Okoń, Kazimierz Koszykowic [?], Paweł Abel",
        "kwoty_podatki": "85 złp (30 + 55 złp); 25 złp",
        "opis_sprawy": "Ciąg dalszy i dekret w sprawie wdowy Elżbiety Okoniowej z synem przeciw Adamowi Wilkowi: pozwany zasłania się ciężkimi czasami (calamitas temporum), sąd nakazuje spłatę 30 złp na najbliższą niedzielę oraz reszty 55 złp nazajutrz po św. Wojciechu (z prawem zwrotu 25 złp w razie niedotrzymania przez powódkę); poniżej dylacja do poniedziałku w sprawie o ogród między Kazimierzem Koszykowicem a Pawłem Ablem.",
        "transkrypcja": """107v.
że bydła do tego żem winien jeszcze złotych ośmdziesiąt y pięć ale calamitas temporum sprawiła żem nie mógł oddać y teraz nie mogę ale proszę aby była mi strona powodowa cierpliwa. Iterum Pars Actorea prosiła sądu aby przynajmniej na tak potrzebny czas dała mi złotych trzydzieści reszty zaś summy złotych pięćdziesiąt y pięć będę mu czekała nazajutrz po świętym Wojciechu.

Sąd ninieyszy widząc pozwanego osobliwy żal z ubogiej sieroty gdzie iuż po tak dawnym czasie y słowie przy przyjęciu osiadłości miał wypłacić danym a nie ma dosyć nie uczynił decernuie aby pozwany na Niedzielę blisko przyszłą złotych trzydzieści, na kończącym zaś złotych pięćdziesiąt y pięć aby oddał nazajutrz po S. Wojciechu, w czym ieżeliby miał contrariari Aktorowi niniejszemu pod przepadkiem y utratą specyfikowanych złotych dwadzieścia pięć. Quod Decretum utraque pars suscepit.

Sub eodem Actu.
W sprawie o ogród między Uciwym Kazimierzem Koszykowicem Aktorem a Uciwym Pawłem Ablem Pozwanym toczącey się. Ponieważ pozwany odwoływa się że to nie jego grunt dziedziczny ale zastawą trzyma, Sąd ninieyszy daie dylacyi stronom do poniedziałku aby się dowiedziało kto ten grunt trzyma.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 217,
        "numer_pozycji": "217",
        "strona_pagina": "fol. 108r (108 / 104)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Spór Sebastiana Studzickiego ze szwagrem Błażejem Stachowicem oraz kontumacje",
        "osoby_podmioty": "Sebastian Studzicki, Błażej Stachowicz, Stanisław Tomkowic [?], Jan Trawiński, Wojciech Kurcel [?], Jakub Piserek [?], Stanisław Latosek [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Sprawa Sebastiana Studzickiego przeciw szwagrowi swojemu Błażejowi Stachowicowi o dobra po zmarłej matce trzymane zastawem (dylacja do poniedziałku na przedstawienie dokumentów); poniżej trzy pierwsze kontumacje: Jan Trawiński z instancji Stanisława Tomkowica [?], Jakub Piserek [?] z instancji Wojciecha Kurcela [?] oraz Jan Trawiński z instancji Stanisława Latoska [?].",
        "transkrypcja": """108. [u dołu: 104.]
Sub eodem Actu.
Uciwy Sebastian Studzicki Aktor proposuit przeciwko Uciwemu Błażejowi Stachowicowi Szwagrowi swemu iż on nie winnie matkę o którey y Aktor coraz by należy po winien przez tak niemały czas trzyma pożywnie y stoi za zastawią przez co krzywdę Aktor ma od niego. Citatus na propozycyą Aktora nie mogąc zaraz odpowiedzieć prosił sądu dylacyey do przygotowania się y pokazania dokumentów jak go nie winnie turbuie. Sąd ninieyszy widząc tak powodową stronę iako y pozwaną niegotową tedy Aktorowi do dowiedzenia tak też Citato do odpowiedzi daie dylacyey do poniedziałku blisko przyszłego aby obie strony z gotowością stanęły conservando partibus terminum peremptorium.

Ex Instantia Famati Stanislai Tomkowic [?] Honestus Joannes Trawiński primo citatus contumax.
Ex Instantia Honesti Alberti Kurcel [?] Honestus Jacobus Piserek [?] prima citatione citatus contumax.
Ex Instantia Honesti Stanislai Latosek [?] Joannes Trawiński prima citatione citatus contumax.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 218,
        "numer_pozycji": "218",
        "strona_pagina": "fol. 108v (108v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Sprzedaż ćwierci roli z ogrodem przez Jakuba Dubaja Stanisławowi Rakowskiemu za 180 złp",
        "osoby_podmioty": "Jakub Dubaj, Anna Zdębiówna [?], Wojciech Dubaj, Stanisław Rakowski, Marianna Piotrowczykówna [Piotrowczykowa], Paweł Słomkowski, Stefan Kwasowic, Wojciech Grzymałowski, Wawrzyniec Bielaszkowic",
        "kwoty_podatki": "180 złp (po 30 gr za złoty)",
        "opis_sprawy": "Uroczysty zapis sprzedaży: Jakub Dubaj wraz z żoną Anną Zdębiówną [?] i w obecności brata rodzonego Wojciecha Dubaja sprzedają ćwierć roli ojcowskiej z ogrodem małżonkom Stanisławowi Rakowskiemu i Mariannie Piotrowczykównie za 180 złp (z prawem odkupu przez sprzedawców lub ich dzieci); do wprowadzenia w posesję delegowano wicewójta Pawła Słomkowskiego oraz ławników Stefana Kwasowica, Wojciecha Grzymałowskiego i Wawrzyńca Bielaszkowica.",
        "transkrypcja": """108v.
Sub eodem Actu.
Do Urzędu y Akt ninieyszych Wójtowskich Ławniczych Przysięgłych Kraśnickich oblicznie przyszedłszy Uciwy Jakub Dubaj wespół z małżonką swoją Anną Zdębiówną [?] z przytomnością brata swego Wojciecha Dubaja Przedmieszczanie Kraśniccy zdrowi na ciele y umyśle nieprzymuszeniem ani żadnym błędem uwiedzeni jaśnie jawnie zeznali iż oni ćwierć roli ojcowskiey y z ogrodem mostem przedającym swoją własnością będącą Uciwemu Stanisławowi Rakowskiemu y Maryannie Piotrowczykównie małżonkom przedali dali darowali za summę złotych polskich Sto Ośmdziesiąt monety w koronie idącey to iest każdy złoty rachując po groszy Nro 30. Między imieniem Uciwego kupca ninieyszego z iedney strony a ninieyszego przedawcy z drugiey to iest Jakuba Dubaja. Przedawca zaś wespół z małżonką swoją Maryanną [Anną] Zdębiówną warują sobie iż gdy ich P. Bóg lub ich samych lubo dziatki iako dziedziców na tę summę wspomoże wolno tey ćwierci odkupienie... A teraz pomienieni kupcy mają sobie tey ćwierci dla pożytku jak najlepiej używać y fructificować do uspokojenia przedawców... Teraz zaś w tę ćwierć pomienioną przedawcy kupcom wyż specyfikowanym wolną dają intromissyą do którey z Urzędu deputowani Sławetni Panowie P. Paweł Słomkowski Podwójci Kraśnicki, Stefan Kwasowic, Wojciech Grzymałowski, Wawrzyniec Bielaszkowic Ławnicy przysięgli zeznali z gruntu wpisz.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 219,
        "numer_pozycji": "219",
        "strona_pagina": "fol. 109r (109 / 105)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Sesja 16 IV 1698 r.: Studzicki vs Stachowicz, Szymon Kępa, Wojciech z Agnieszką vs Woszek i Dubaj",
        "osoby_podmioty": "Sebastian Studzicki, Błażej Stachowicz, Katarzyna Nogajowa (zm.), Szymon Kępa, Józef Rabak [?], Wojciech, Agnieszka, Jakub Woszek [?], Andrzej Skowroński [?], Jan Tokarczyk, Matka Tokarczykowa, Maciej Araczniak [?], Wojciech Dubaj",
        "kwoty_podatki": "22 złp; 40 złp",
        "opis_sprawy": "Pod datą 16 kwietnia 1698 r. (Feria Quarta post Dominicam Misericordiae): dylacja w sprawie Sebastiana Studzickiego przeciw Błażejowi Stachowicowi o sukcesję po zmarłej Katarzynie Nogajowej; sprawa Szymona Kępy przez Józefa Rabaka [?]; sprawa Wojciecha z Agnieszką przeciw Jakubowi Woszkowi [?] o majątek po matce; sprawa Andrzeja Skowrońskiego [?] przeciw Janowi i Matce Tokarczykowej o egzekucję; sprawa Macieja Araczniaka [?] przeciw Wojciechowi Dubajowi o 22 złp i owies na zastawionej roli.",
        "transkrypcja": """109. [u dołu: 105.]
Actum Feria Quarta post Dominicam Misericordiae Anno 1698 [16 IV 1698].
Inter Honestum Sebastianum Studzicki Actorem et Blasius Stachowicz datur dilatio ad feriam sextam proxime venturam ratione successionis bonorum piae memoriae Catharinae Nogajowa.

Honestus Kempa Szymon citatus per Josephum Rabak [?] quoniam pars Actorea non comparuit ad respondendum paratus liber.

Inter Honestum Albertum una cum uxore Agneta Actores et Jacobum Woszek [?] citatum ratione illationis matris eius in bona... Jacobus Woszek vocatus per matrem eius... petit ad expurgandum sibi dilationem conceditur ad feriam quartam proxime venturam.

Inter Honestum Andream Skowroński [?] Actorem et Joannem et Matrem Tokarczykowa citatos ratione poenae executionis...

Inter Mathiam Araczniak [?] Actorem et Albertum Dubaj citatum ratione porrectionis opignorationis sibi agri in summa 22 florenorum et avenae...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 220,
        "numer_pozycji": "220",
        "strona_pagina": "fol. 109v (109v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Ugoda ślusarza Grzegorza Kaczorkowica z rajcą Stefanem Kwasowicem po procesie w Trybunale Zamojskim",
        "osoby_podmioty": "Jan Grymuza, Paweł Abel, Kazimierz Koszykowic [?], ślusarz Grzegorz Kaczorkowic, Jan Onufry Kieniewicz [Onupkiewicz?], Paweł Słomkowski, Stefan Kwasowic, Wojciech Bożkowic, Wawrzyniec Bielaszkowic",
        "kwoty_podatki": "14 grzywien (vadium)",
        "opis_sprawy": "Dokończenie sprawy Dubaja (40 złp); areszt Jana Grymuzy na Tękupowskiej [?]; kontumacja Pawła Abla z instancji Kazimierza Koszykowica [?]; poniżej ugoda i kompromis przyjacielski przed wójtem Janem Onufrym Kieniewiczem, podwojcim Pawłem Słomkowskim i ławnikami Stefanem Kwasowicem, Wojciechem Bożkowicem i Wawrzyńcem Bielaszkowicem, w której ślusarz Grzegorz Kaczorkowic kwituje dawnego rajcę Stefana Kwasowica z procesu w Najwyższym Trybunale Zamojskim i kondemnaty pod vadium 14 grzywien.",
        "transkrypcja": """109v.
dari dilationem ad Judicium pro feria sexta proxime ventura... super quod agrum... 40 florenorum etc.
Honesti Joanni Grymuza datur arestum super... dictam Tękupowska [?].
Ex termino conservato quoniam non comparuit Honestus Abel contumax ex Instantia Casimiri Koszykowic [?] in cuius contumaciam decernitur poena unius Marca parti et Judicio per medium.

Do Urzędu y Akt niniejszych oblicznie przyszedłszy Sławetny Grzegorz Kaczorkowic Ślosarz Mieszczanin Kraśnicki przy bytności Sławetnych Panów Jana Onupkiewicza [Kieniewicza?] Wójta y sędziego, P. Pawła Słomkowskiego Podwójciego, Stephana Kwasowica, Wojciecha Bożkowica, Wawrzyńca Bielaszkowica Ławników przysięgłych Kraśnickich oblicznie przyszedłszy jawnie jaśnie dobrowolnie zeznał iż Sławetnego Stephana Kwasowica Rajcy dawnego Kraśnickiego o zadanie sobie pewnych a niesłusznych rzeczy o co sprawa w Trybunale Naywyższym Zamoyskim toczyła się y tam kondemnatę na nim otrzymał, że przez kompromis przyjacielski iest ukontentowany y uroszony onego sądownie quitował y nie ma więcej sprawy tey wzniecać ani tak strona powodowa iako pozwana... pod winą grzywien czternastu sądowi y stronie per medium. Quod connotatum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 221,
        "numer_pozycji": "221",
        "strona_pagina": "fol. 110r (110 / 106)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Sprawa Rabaka ze ślusarzem Kaczorkowicem o kulbakę (8 złp) oraz proces Studzickich ze Stachowicami",
        "osoby_podmioty": "Józef Rabak [?], ślusarz Grzegorz Kaczorkowic, Kazimierz Koszykowic [?], Paweł Abel, Jan Grymuza, Sebastian Studzicki, Anna Studzicka, Błażej Stachowicz, Katarzyna Stachowicowa, Balcer, Tomasz, Jan, Sebastian",
        "kwoty_podatki": "8 złp; 30 złp (na każde dziecko)",
        "opis_sprawy": "Pod datą 18 kwietnia 1698 r. (Feria Sexta ante Festum Sancti Alberti) sprawa pracowitego Józefa Rabaka [?] przeciw ślusarzowi Grzegorzowi Kaczorkowicowi o 8 złp za kulbakę; sprawa Kazimierza Koszykowica [?] przeciw Pawłowi Ablowi o ogród; zapis o niwie Kondupowskiej przypadającej Janowi Grymuzie; poniżej skarga Sebastiana i Anny Studzickich przeciw Błażejowi i Katarzynie Stachowicom o dobra po matce i testament przewidujący udział dzieci: Balcera, Tomasza, Jana i Sebastiana.",
        "transkrypcja": """110. [u dołu: 106.]
Actum Coram Judicio Advocatiali et Scabinali Jurato Crasnicensi Feria Sexta ante Festum Sancti Alberti proxima 1698 [18 IV 1698].
Na Terminie dzisieyszym stanąwszy pracowity Józef Rabak [?] wniósł skargę naprzeciw Uciwemu Grzegorzowi Kaczorkowicowi ślosarzowi mieszczaninowi Kraśnickiemu który pożyczywszy u Aktora kulbaki... iż miał ją temuż jeszcze pożyczyć, w tym prosił pozwany do komplanacyi przyjaciół... zeznał iż mu miał pozwany oddać fl 8 y dosyć zrobił, a teraz fortelemi zarabia...

Między Uciwym Koszykowicem Aktorem a Pawłem Ablem pozwanym o ogród względem zastawionego przez Sławetną Panią Jorkową [?] ogroda dawnemu Ablowi który per consensum... dziedzica grodzić nie chciał...

Względem niwki Kondupowskiej [?] naturali iure Janowi Grymuzie po rodzicu jego należy... teraz w possessyi alias zastawie...

Przed Urzędem ninieyszym stanąwszy Uciwy Sebastian Studzicki wniósł skargę przeciw Uciwemu Błażejowi y Katarzynie Stachowicom iż oni będący tak długo w dobrach po zmarłej matce... bronią się testamentem w którym stanęły na affectacyą... Sebastianowi y Annie Studzickim małżonkom... a Katarzynie Stachowicowej nic nie pieniędzy... na dziatki Balcera, Tomasza, Jana, Sebastiana...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 222,
        "numer_pozycji": "222",
        "strona_pagina": "fol. 110v (110v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dokończenie sprawy Studzickich (po 30 złp) oraz dekret w sporze Wojciecha i Doroty z Jakubem Woszkiem",
        "osoby_podmioty": "Sebastian Studzicki, Anna Studzicka, Wojciech, Dorota, Jakub Woszek [?]",
        "kwoty_podatki": "30 złp; 8 złp (albo wieprz)",
        "opis_sprawy": "Dokończenie wpisu o dzieciach Sebastiana i Anny Studzickich (po 30 złp na każde z nich do wzrostu); poniżej pod datą 25 kwietnia 1698 r. (Feria Sexta ante Festum S. Philippi Jacobi) dekret w sprawie małżonków Wojciecha i Doroty przeciw Jakubowi Woszkowi [?] o sukcesję po rodzicach — sąd nakazuje wydać wieprza albo 8 złp według zapisu matki oraz złożyć oświadczenie w sprawie krowy i panny służebnej.",
        "transkrypcja": """110v.
Sebastiana y Anny Studzickich synów a ma być złożone na tym gruncie do wszystkich dokąd na każdego do wzrostu ich po zł 30 to iest złotych trzydzieści które pomieniony ma ich onym dotrzymać.

Actum Feria Sexta ante Festum Sancti Philippi Jacobi Apostolorum proxima 1698 [25 IV 1698].
Na terminie dzisieyszym między Uciwemi Wojciechem y Dorotą małżonkami w tey sprawie Aktorami a Uciwym Jakubem Woszkiem [?] pozwanym z dylacyi sub conservato termino... tak Aktorowie quam Citatus o sukcesyą po rodzicach daney... Sąd dobrze wyrozumiawszy nakazuie pozwanemu aby wieprza lub złotych ośm Aktorom oddał... także pod przysięgą pozwany przy sobie miał aby Aktorom oddał... którą matka Aktorów odkazała iako iest aby się nią kontentowali. Quod Actis praesentibus connotatum. A quo Decreto pars...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 223,
        "numer_pozycji": "223",
        "strona_pagina": "fol. 111r (111 / 107)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Spory: Franciszek i Agnieszka Michałowicowie vs Grzegorz Kaczorkowic oraz Jan Grymuza vs Gucka",
        "osoby_podmioty": "Franciszek Michałowic, Agnieszka Michałowicowa, Grzegorz Kaczorkowic, Jan Grymuza (syn Jana Grymuzy), Gucka (żona zmarłego Grzegorza Guckiego), Grzegorz Gucki (zm.)",
        "kwoty_podatki": "-",
        "opis_sprawy": "Sprawa Sławnych Franciszka i Agnieszki Michałowiców przeciw Sławnemu Grzegorzowi Kaczorkowicowi o wzajemną zwadę i poswarek słowny na Rynku (odroczenie do poniedziałku na informację świadkami); poniżej sprawa Sławnego Jana Grymuzy (syna zmarłego Jana Grymuzy) przeciw Sławetnej Pani Guckiej (żonie zmarłego Grzegorza Guckiego) o wydanie dóbr przypadających mu jako naturalnemu sukcesorowi (dylacja do środy na opiekunów).",
        "transkrypcja": """111. [u dołu: 107.]
W sprawie między Sławnym Franciszkiem y Agnieszką Michałowicami Aktorami a Sławnym Grzegorzem Kaczorkowicem pozwanym wniósł Aktor że mu pozwany żonę na Rynku... słowy nieuczciwemi zelżył na co pozwany odpowiedział że z wadą żem musiał się do niey odezwać ale nie tak iako wnosi gdyż ona mię po oczu lży... dlatego Sąd niema z kąd informować strzelby do poswarku z nikąd okazyi do poniedziałku blisko przyszłego termin im się naznacza.

Sub eodem Actu.
Wniósł sprawę Sławny Jan Grymuza niegdy Sławetnego Jana Grymuzy z dany przychodzoney syn przeciw Sławetney Paniey Guckiey niegdy Sławetnego P. Grzegorza Guckiego pozostałey małżonce iż on iako naturalny będąc Sukcessor dóbr mu iure należytych nie oddaie y w swoiey trzyma possessyey. Ex adverso pars citata ponieważ zabiera się na Opiekunów prosząc dylacyey Sąd ninieyszy determinuie do środy blisko przyszłey aby wraz z nimi stanęła pod upadkiem sprawy conservando partibus terminum peremptorium. Quod Actis praesentibus est Connotatum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 224,
        "numer_pozycji": "224",
        "strona_pagina": "fol. 111v (111v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Kompromis przyjacielski Studzickich i Stachowiców o sukcesję po Wojciechu i Katarzynie Nogajach",
        "osoby_podmioty": "Sebastian Studzicki, Anna Studzicka, Jan Onufry Kieniewicz [Onupkiewicz?], Stanisław Solecki, Stanisław Jesurkiewicz, Wojciech Bożkowic, Wawrzyniec Bielaszkowic, Błażej Stachowicz, Anna Stachowicowa, Wojciech Nogaj (zm.), Katarzyna Nogajowa (zm.)",
        "kwoty_podatki": "14 grzywien (vadium)",
        "opis_sprawy": "Pod datą 29 kwietnia 1698 r. (Feria Tertia ante Festum SS. Philippi et Jacobi) ugoda i kompromis w sprawie sukcesji po zmarłych Wojciechu i Katarzynie Nogajach zawarty przez Sebastiana i Annę Studzickich oraz Błażeja i Annę Stachowiców w obecności wójta Jana Onufrego Kieniewicza, burmistrza Stanisława Soleckiego, dawnego rajcy Stanisława Jesurkiewicza oraz ławników Wojciecha Bożkowica i Wawrzyńca Bielaszkowica (z podziałem roli i zagonów oraz zakładem 14 grzywien vadium).",
        "transkrypcja": """111v.
Actum Feria Tertia ante Festum Sanctorum Philippi et Jacobi Apostolorum proxima Anno Millesimo Sexcentesimo Nonagesimo Octavo [29 IV 1698].
Do Urzędu y Akt ninieyszych Wójtowskich Ławniczych oblicznie przyszedłszy Uciwi Sebastian y Anna małżonkowie swoi Studziccy zdrowi na umyśle... jaśnie jawnie nie przymuszeni ani żadnym błędem uwiedzeni przy bytności Sławetnych Panów samego Sławetnego Pana Onupkiewicza [Kieniewicza?] Wójta Kraśnickiego za uproszeniem także Sławetnego P. Stanisława Soleckiego Burmistrza y Sławetnego Pana Stanisława Jesurkiewicza Rajcy dawnego... Pana Wojciecha Bożkowica, Pana Wawrzyńca Bielaszkowica Ławników... zeznali iż oni mają z Uciwymi Błażejem y Anną Stachowicami ratione Sukcessyey po nieboszczyku Wojciechu y Katarzynie Nogajom im należytey o którą lubo sprawa przed sądem ninieyszym agitowała się y Appellacia do Sądu Radzieckiego im dana była y pozwolona, na przyjacielskich affectacyą nie wchodząc w prawne terminy dobrowolnie uproszonych Panów Compromissum... w swey opiece specyfikowanych Panów. Kontentuią się na którym to... Panowie uznali aby Uciwy Błażej Stachowic przy podziale miał zagonów... co Sebastian Studzicki... utrzymał, in quantum by zaś między sobą iaką zwadkę o ten grunt czynili przyjaciel nakazał z którey strony do rozterku okazyą była na obie stronie po grzywien czternastu...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 225,
        "numer_pozycji": "225",
        "strona_pagina": "fol. 112r (112 / 108)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Łaciński hymn maryjny oraz protestacje Benedykta Nowackiego i Tomasza Nowackiego przeciw Carklinom",
        "osoby_podmioty": "Benedykt Nowacki, Krystyna Carklina [?], Kazimierz Michalski, Biegaj [Biegajczyk?], Tomasz Nowacki, Carklin [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "U góry karty wpisany łaciński rymowany hymn-modlitwa maryjna ('Reparatrix Consolatrix Desperantis Animae...'); poniżej pod datą 21 lipca 1698 r. (Feria Secunda ante Festum S. Mariae Magdalenae) protestacja Benedykta Nowackiego przeciw Krystynie Carklinie [?] o napaść w sklepie i zadanie trzech krwawych ran; poniżej diligentia Kazimierza Michalskiego przeciw Biegajowi [Biegajczykowi?] oraz protestacja Tomasza Nowackiego przeciw Carklinowi [?] o napaść w niedzielę na posiedzeniu i spotkaniu.",
        "transkrypcja": """112. [u dołu: 108.]
Reparatrix Consolatrix Desperantis Animae
Et pressura quae ventura malis est nos redime
Pro me pete ut quiete sempiterna perfruar
Ne tormentis comburentis stagnis miser obruar
Quod requiro quod suspiro mea sana vulnera
Et damenti te poscenti gratiarum munera
Ut sim castus et modestus dulcis blandus sobrius
Pius rectus circumspectus simultatis nescius.

Actum Feria Secunda ante Festum S. Mariae Magdalenae proxima Anno 1698 [21 VII 1698].
Do Urzędu y Akt niniejszych W. Ł. K. oblicznie przyszedłszy Uciwy Benedykt Nowacki z innymi wielkim żalem protestował się na przeciw Uciwey Krystynie Carklinie [?], iż ona bez żadney daney okazyi w sklepie... gdzie w mieście... przyszedłszy z nią... w tym sklepie... pokazał razy trzy krwawe, trzy pręgi krwawe... i rękę prawą... której krzywdy obiecuje dochodzić ubi de iure venerit.

Sub eodem Actu.
Diligentia simul cum protestatione Famati Casimiri Michalski contra Biegaj [Biegajczyk?] ratione...

Sub eodem Actu.
Videatur Protestatio H. Thomae Nowacki contra H. Carklin [?] et eius consortem... w niedzielę tak na posiedzeniu tak też y na spotkaniu etc.""",
        "link_swa": UNIT_LINK
    }
]

main_data.extend(part9_scans)
with open('/home/ubuntu/workspace/Gen/main_data_j20_part9.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j20_part9.json: {len(main_data)} skanów")
