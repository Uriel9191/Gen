# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j20_part7.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
SYGN = "35/40/0/1/20"

part8_scans = [
    {
        "nr_skanu": 176,
        "numer_pozycji": "176",
        "strona_pagina": "fol. 88r (88 / 84)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Obdukcja pobicia, najście domu i kontumacja Wojcikowica",
        "osoby_podmioty": "Jan Więckowicz [Wierckowicz?], Wojciech Wojcikowicz [Woycikowicz?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie obdukcji ran (rana nad uchem od kija na dwa członki wszerz aż do kości, nad czołem na lewej stronie siniak krwią zaszły, prawa ręka stłuczona i obie nogi potłuczone) oraz protestacja o najście domu z bratem, pobicie, zabranie żony, skrzyni i rzeczy według inwentarza; pod datą 1 października 1698 r. (Feria Quarta post Festum S. Michaelis Archangeli) kontumacja Wojciecha Wojcikowica z instancji Jana Więckowicza [?] o niewydanie futra.",
        "transkrypcja": """88. [1698. | u dołu: 84.]
nad uchem od kija przecięta rana wzdłuż na dwa członki wszerz na członkach aż do kości ad aspersionem chirurgi, na lewey stronie nad czołem ułowicy raz na skroni siny krwią zaszły. Item na ręce prawey pięść stłuczona na pięć chromą, Item na nogi obie które potłuczone y sine widziane były za kije. Iż teraży wszyscy w dom jego włazy nasedszy z bratem swoim onegoż zadali, de quibus praemissis idem protestans et obducens querulatur iterum atque iterum offerendo se iuris mediis hasce suas iniurias vindicaturum velle ubi de iure venerit. Ad haec in continenti idem protestans adauget querelam eandem że nie dosyć mu było patratori violentias enferentas że go pobił zabił ale mu żonę jego do siebie wziął, ażeby żadney opatrzności nie miał przeszkadzał by nie starał się, klucz odebrał skrzynię y inne rzeczy inwentarium conscripta zabrali.

Actum Crasnicii Feria Quarta post Festum Sancti Michaelis Archangeli proxima Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [1 X 1698].
Ad Joannes Więckowicz [Wierckowicz?] Crasnicensis ex parte Alberti Wojcikowicz [Woycikowicz?] primum et in finem contumacis decernitur captura post latum decretum ratione futra nie oddania.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 177,
        "numer_pozycji": "177",
        "strona_pagina": "fol. 88v (88v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Spór o dzierżawę roli Tatarskiej (Marcin Rymarczyk vs Jan Stryczak)",
        "osoby_podmioty": "Marcin Rymarczyk, Jan Stryczak [Struczak?], Szymon [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Na terminie wójtowskim i ławniczym kraśnickim sprawa między przedmieszczaninem Marcinem Rymarczykiem a przedmieszczaninem Janem Stryczakiem [Struczakiem?] o niedotrzymanie słowa danego Szymonowi [?] względem arendy roli zwanej Tatarską; sąd nakazuje inkwizycję na piątek. Poniżej protestacja Marcina Rymarczyka przeciw Janowi Stryczakowi o dochodzenie sprawy pod jurysdykcją sądu wójtowskiego.",
        "transkrypcja": """88v.
Na Terminie dzisieyszym Wójtowskim y Ławniczym Kraśnickim stanąwszy oblicznie Uciwy Marcin Rymarczyk w miast skargę na przeciw Uciwemu Janowi Stryczakowi [Struczakowi?] przedmieszczaninowi Kraśnickiemu o to względem niedotrzymania słowa raz Szymonowi [?] danego o rolą alias Tatarską któremu pozwany zaarendował y przy ludziach zgodnych na pierwszą siać pozwolił, a że Aktorea pars żadney niema satisfakcyey od niego owszem zabiera się utraque pars na Inkwizycyą dla którey sąd ninieyszy non denegat. Interea conservando partibus terminum contra se procedendum peremptorie idque pro feria sexta proxime ventura sine ulla adcitatione sub eiusdem iuris vigore quod connotatum.

Sub eodem Actu.
Honestus Martinus Rymarczyk suburbanus Crasnicensis Actor circa agitationem causae suae protestatus est contra Honestum Joannem Stryczak [Struczak?] itidem suburbanum Crasnicensem in hunc modum że on badać na stronie sprawy sub securitate Officii Advocatialis et Scabinalis Crasnicensis sprawiedliwości nie uiścił się protestanti obema prawem dochodzić y do grzywien dowieść prout latius inferetur.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 178,
        "numer_pozycji": "178",
        "strona_pagina": "fol. 89r (89 / 85)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Zeznania o długu wódki prostej (Żyd Wygdor Markowicz vs Szymon Draganek)",
        "osoby_podmioty": "Żyd Wygdor Markowicz, Stanisław Kuzokowicz [Kuzakowicz?], Szymon Draganek, Benedykt Nowak",
        "kwoty_podatki": "półósma spustu wódki prostej",
        "opis_sprawy": "Pod datą 3 października 1698 r. (pridie Festi S. Francisci Confessoris) zeznania świadków z instancji Żyda kraśnickiego Wygdora Markowicza przeciw Szymonowi Dragankowi o nieoddanie półósma spustu wódki prostej: 1. świadek Stanisław Kuzokowicz [?] (zeznaje o ugodzie na 5 spustów w domu starozakonnego Wygdora na św. Jana Chrzciciela) i 2. świadek Benedykt Nowak (o obietnicy oddania długu wódki prostej przez winiarza Szymona Draganka).",
        "transkrypcja": """89. [u dołu: 85.]
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Pridie Festi Sancti Francisci Confessoris Die Videlicet Tertia Octobris Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [3 X 1698].
Ex Instantia Perfidi Wygdor Markowicz Judaei Crasnicensis adcitatus Famatus Stanislaus Kuzokowicz [Kuzakowicz?] ad perhibendum fidele veritatis testimonium in causa inter se inducentem testimonia testium ab una et Simonem Draganek dictum cittatum ab altera ratione debiti certi et liquidi to iest nieoddania wódki prostey półósmu spustów tale recognovit tacto pectore testimonium suum in haec formalia:
1mus Testis. Pamiętam dobrze że Draganek Szymon w domu starozakonnego Wygdora Markowicza Obywatela Kraśnickiego względem nieoddania wódki prostey półósma spustów przez tegoż Draganka winnych między sobą zgodnie zgodzili się na pięć spustów z którey to kwoty spustów miał oddać Draganek pomieniony spustu półtrzecia spustu na dzień Świętego Jana Chrzciciela roku teraźniejszego, drugie półtrzecia spustu znowu o półtrzecia spustu wódki prostey za uproszeniem przyiaciół oraz samey wierzyciele mieli się między sobą uczynić.
2dus Testis. Uciwy Benedykt Nowak taliter recognovit że ia grzejąc u Wygdora Żyda w domu u pieca słyszałem że Szymon Draganek winiarz obiecował mu do długu""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 179,
        "numer_pozycji": "179",
        "strona_pagina": "fol. 89v (89v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Kontumacja Draganka oraz spór Pawła Słomkowskiego z Peronem i Wawrzyłem",
        "osoby_podmioty": "Żyd Wygdor Markowicz, Szymon Draganek, Paweł Słomkowski, Maciej Peron, Wojciech Wawrzyło",
        "kwoty_podatki": "2 grzywny; 3 grzywny",
        "opis_sprawy": "Dokończenie zeznania Benedykta Nowaka i wpis z regestru przeciw Szymonowi Dragankowi o 2 grzywny i 5 spustów wódki dla Wygdora Markowicza; poniżej sprawa Sławetnego Pawła Słomkowskiego przeciw przedmieszczanom Maciejowi Peronowi i Wojciechowi Wawrzyłowi o szkodę w zbożu i nieposłuszeństwo na trzy terminy (kara 3 grzywien oraz dylacja na inkwizycję i przysięgę).",
        "transkrypcja": """89v.
wódki prostey ale nie mógł dosyć uczynić.
Inter Perfidum iuxta Regestri connotationem dictum Wygdor Markowicz et Honestum Simonem Draganek lucrum solutionis Marcarum duarum. O nieoddanie wódki prostey pięć spustów.

Inter Famatum Paulum Słomkowski Actorem et HH. Mathiam Peron et Albertum Wawrzyło Suburbanos Crasnicenses.
W mocy Aktor skarży iż szkodę poszkodowawszy w zbożu jego to iest żyta z synami pozwanych w próżne sprawy wyprowadzili a teraz na terminy po trzy razy dane do Sądu uporczywie stawać nie chcieli y lekce sobie tak Sąd iako y stronę poważali gdzie inter nos obsigno gdzie per Actorem dali na sobie otrzymać lucrum solutionis trzech grzywien irremissibiliter parti et Judicio per medium solvendarum.
Sąd ninieyszy locum standi stronie pozwaney nie dopuszcza póki grzywien trzech zapisanych nie odda dla nawrócenia nakazu parti et Judicio per medium. Et hic in continenti ponieważ strony pozwane przystąpiły do sądu y strony powodowey o expensy na grzywien tedy za ludzką grzywien do poniedziałku przyszłego na marginesie w sprawie expensy mandat Inexperimento... A ponieważ strony tam Actorea quam Citata na sprawę niegotowością compareunt którym tam ad deducendum quam ad expurgandum datur dilatio Inquisicionis.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 180,
        "numer_pozycji": "180",
        "strona_pagina": "fol. 90r (90 / 86)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Wyrok w sporze Rymarczyka ze Stryczakiem o zniewagę i rolę Tatarską oraz kontumacje",
        "osoby_podmioty": "Marcin Rymarczyk, Jan Stryczak [Struczak?], rajca Jan Majowski, Wojciech Piasecki, Kazimierz Maśniarczyk [?], Stanisław Torański [?]",
        "kwoty_podatki": "6 grzywien; 1 zł 10 gr",
        "opis_sprawy": "Dokończenie poprzedniej sprawy (datur dilatio); następnie wyrok Sądu Wójtowskiego i Ławniczego w sprawie Marcina Rymarczyka przeciw Janowi Stryczakowi [?] o zniewagę słowną w sklepie przed ludźmi (skazany na przeproszenie sądu i powoda, tydzień wieży oraz 6 grzywien) i o zasiew roli Tatarskiej (Rymarczyk ma oddać resztę 1 zł 10 gr i zebrać zasiane żyto); na dole dwie kontumacje: szl. Jana Majowskiego rajcy przeciw Wojciechowi Piaseckiemu oraz Kazimierza Maśniarczyka [?] przeciw Stanisławowi Torańskiemu [?] o zatrzymanie sika w ogrodzie.",
        "transkrypcja": """90. [u dołu: 86.]
datur dilatio.
Sub Eodem Actu.
Inter HH. Martinum Rymarczyk suburbanum Crasnicensem Actorem ab una et Joannem Stryczak [Struczak?] Citatum.
Sąd ninieyszy Wójtowski y Ławniczy Kraśnicki uważając na skargę y relacyą Uciwego Marcina Rymarczyka Przedmieszczanina Kraśnickiego przeciwko Uciwemu Janowi Stryczakowi o znieważenie tegoż Aktora przez małżonkę jego przy obejściu ludzi do spraw swych zgromadzonych na sklepie, ponieważ się z Inkwizycyi pokazała zniewaga eluendo poenas exinde demeritas aby in instanti stronie powodowey deprecatio coram Judicio uczynił, wieczór tydzień continuabit a nie wychodzić dziś zapładszy aż odda grzywien sześć per medium parti et Judicio, co zaś tycze pretensyi stron nie dotrzymania słowa o zasiewek roli przez Aktora na roli pozwanego przez syna tegoż Aktora najętey y syna jego Sebastiana, ponieważ się świadectwem pokazało iako tedy prawnego zebrania pożytków z półka Tatarskiego swoje należytości za zagonów ośm z których reszty pretenduie sobie złotych jeden groszy dziesięć którą resztę aby w przyszły poniedziałek a data decreti plenus Rymarczyk z synem oddali także y żyto które wysiał na pomienioney roli tołu odorał w polu jego bo te lata tyle pożytku bo przysięgać mają pozwanemu ad relationem ad Actorem eiusdem adinvenit pro feria secunda proxime ventura incunctanter.

Contumacia Spectabilis Joannis Majowski Consulis Crasnicensis ex parte Honesti Alberti Piasecki ratione contusionis.
HH. Kazimierz Maśniarczyk [?] ex parte Stanislai Torański [?] Citatur contumax 1mo o zatrzymanie sika w ogrodzie.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 181,
        "numer_pozycji": "181",
        "strona_pagina": "fol. 90v (90v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Wizja inwentarza po Zychowiczowej na wniosek Wojciecha Dalmackiego",
        "osoby_podmioty": "Benedykt Nowacki, Wojciech Ornatowski (bedel), Wojciech Dalmacki [?], Zychowiczowa (zm.), Adam Chmielowicz, Stefan Petek [Petkowicz?], Zofia",
        "kwoty_podatki": "1 zł 16 gr (w woreczkach)",
        "opis_sprawy": "Wpis z instancji Benedykta Nowackiego i Chryzostoma [?] przez bedela Wojciecha Ornatowskiego w sprawie inwentarza; poniżej pod datą 6 października 1698 r. (Feria Secunda post Festum S. Francisci Confessoris) w domu zmarłej Uczciwej Zychowiczowej na afektację Wojciecha Dalmackiego [?] rzemieślnika krawieckiego delegowani przez wójta Adam Chmielowicz i Stefan Petek [?] ławnik dokonują spisu rzeczy po zmarłej (ciało zmarłe na ziemi, garnek miodu, kilka snopów drewna, poduszka, koszula śmiertelna i 1 zł 16 gr w dwóch woreczkach).",
        "transkrypcja": """90v.
Ex Instantia H. Benedicti Nowacki Actoris et Chryzostoma [?] Carklina [?] Citt. per Albertum Ornatowski Bedellum iurata relatione ipsius recognovit względem Inwentarza po śmierci... pretensyi na terminie proponowany.

Actum in Casa olim Honestae Zychowiczowa dictum Viduae Feria Secunda Mensis Octobris post Festum S. Francisci Confessoris proxime Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [6 X 1698].
Na affectatią Uciwego Wojciecha Dalmackiego [?] Rzemiosła Krawieckiego Mieszczanina Kraśnickiego z deputacyi Sławetnego Pana Wójta Kraśnickiego w domostwie niegdy Uciwey Zychowiczowey tu w Mieście Kraśniku przed PP. Adama Chmielowica y Stephana Petka [Petkowicza?] Ławników tegoż Miasta takową przed Aktami tegoż Urzędu dla pamięci dzisieyszego y dawnieyszego Kraśnickiego uczynili relacyą:
Iż widzieli ciało zmarłe na ziemi, przy nim na środku izby kamień drobiażgi, podle niektóre mąki, faska y garnek miodu, kilków, kilka snopów trochę drew osobnych, poduszka pospolita na którey leżała, et hic in continenti prezentowała Zofia pisma siedm na koszulę śmiertelną, pieniędzy we dwóch woreczkach złotych jeden groszy szesnaście, więcey nic nie widzieliśmy.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 182,
        "numer_pozycji": "182",
        "strona_pagina": "fol. 91r (91 / 87)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Protestacja rajcy Jana Barankowicza przeciw Błażejowi Stachowiczowi o pobicie w gospodzie",
        "osoby_podmioty": "rajca Jan Barankowicz, Błażej Stachowicz, Jan Żmienda [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Pod datą 6 października 1698 r. (Feria Secunda post Festum S. Francisci) solenna protestacja Sławetnego Pana Jana Barankowicza rajcy kraśnickiego przeciw przedmieszczaninowi Błażejowi Stachowiczowi, który w gospodzie w obecności krewnego Jana Żmiendy [?] bez żadnej okazji zelżył go słowami nieuczciwymi (w tym słowem o baranie), a następnie uderzył w twarz i wyszarpnął za włosy.",
        "transkrypcja": """91. [u dołu: 87.]
Actum Crasnicii Feria Secunda post Festum Sancti Francisci Confessoris proxima die sexta Octobris Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [6 X 1698].
Do Urzędu y Akt niniejszych Wójtowskich y Ławniczych Kraśnickich w osobie swojey przyszedłszy Sławetny Pan Jan Barankowicz Rajca Kraśnicki solennie protestował się przeciwko Uciwemu Błażejowi Stachowiczowi Przedmieszczaninowi Kraśnickiemu o to iż gdy niniejszy protestant o krewnego swego Uciwego Jana Żmiendę [?] na pewne mieysce do posiedzenia y niektórych rzeczy które mieli między sobą mieli rozmawiania, Uciwy pomieniony Błażej Stachowicz bywszy w teyże gospodzie pijany bez żadney daney okazyi zapomniawszy miłości boskiey obserwancyi osoby Urzędowey spokojnie siedzącego protestanta w przód słowy nieuczciwemi zelżył które idem protestans coram iisdem Actis asseruit formalibus indecentibus ty Baranie z trebatze pendentia odpiąć et alia inconvenientia zadał quae ob reverentiam Actorum specificari nequeunt. Verum in termino superius oblato propositum in termino termini insup nie kontentując się tak ciężkim protestanta zelżeniem ważył się na tegoż wzgardzonego milczącego ręką swoją odważną w gębę dać za głowę targać et alia verbe-""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 183,
        "numer_pozycji": "183",
        "strona_pagina": "fol. 91v (91v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Obdukcja ran rajcy Barankowicza oraz protestacja Anny Barankowiczowej przeciw Sitarskiej",
        "osoby_podmioty": "Jan Barankowicz, ławnik Wawrzyniec Bielaszkowic, pisarz Adam Trzelowicz [Chmielowicz?], Anna Barankowiczowa, Franciszek Sitarski, Marcin Sitarski, Zychowiczowa (zm.)",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie protestacji i obdukcja ran Jana Barankowicza przed wójtem, ławnikiem Wawrzyńcem Bielaszkowicem [Pilaszkowicem] i pisarzem Adamem Trzelowiczem [?] (krwawa pręga na lewej stronie twarzy wzdłuż na dwa palce, ból głowy od targania za włosy); poniżej protestacja Sławetnej Pani Anny Barankowiczowej (w asyście męża) przeciw Franciszce żonie Marcina Sitarskiego o publiczne pomówienie na Rynku o pokrewieństwo ze zmarłą Zychowiczową i przywłaszczenie rzeczy po stryju.",
        "transkrypcja": """91v.
bera in obductione expressa.
In cuius protestationis verificationem in Residentia Sławetnego Zaonie Ordynaryjnego Wójta Kraśnickiego przy obecności jego y Sławetnego Pana Wawrzyńca Pilaszkowica [Bielaszkowica] Ławnika Kraśnickiego tudzież Urodzonego Pana Adama Chmielowica [Trzelowica?] Pisarza Urzędu tegoż takowe pokazał rany: naprzód raz krwawy na lewey stronie twarzy wzdłuż na dwa członki, na to linie iż gdy mu impetit colaphum na tęż stronę twarzy napuchła że boleść cierpi tudzież na głowie linie że go za włosy wziąwszy targał inne zaś boleści swoje przez mayorowane supius in termino na sądzie produkowane unasum testimonium obiecując offerens se ratione tanti dishonorationis concussionis prosequi liturum.

Sub Eodem Actu.
Sławetna Pani Anna Barankowiczowa cum assistentia mariti sui protestowała się na przeciwko Uciwey Franciszce żony Marcina Sitarskiego małżonkom o to iż pomieniona Sitarska na Rynku publice zmyśliwszy sobie krewność do niegdy Uciwey Zychowiczowey zakas uczepiła y gdy protestantka poufale odpowiedziała że na tych kłamstwa y nie cierpiąc krewnego wymyśla słowami nieuczciwemi intercessu iako dobr stryia swego ich konserwacyi zabra-""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 184,
        "numer_pozycji": "184",
        "strona_pagina": "fol. 92r (92 / 88)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Poręczenie za Szymona Draganka (5 spustów wódki dla Żyda Wygdora)",
        "osoby_podmioty": "Anna Barankowiczowa, Marcin Boron [?], Wojciech Skakha [?], Szymon Draganek, Żyd Wygdor Markowicz",
        "kwoty_podatki": "5 spustów wódki prostej",
        "opis_sprawy": "Dokończenie protestacji Anny Barankowiczowej; poniżej przed urzędem przedmieszczanie Marcin Boron [?] i Wojciech Skakha [?] stają się rękojemcami (fideiussores) za Szymona Draganka w sprawie długu 5 spustów wódki prostej dla Żyda Wygdora Markowicza (od św. Jana Chrzciciela), zwalniając go z więzienia i rozkładając spłatę ratalną na kolejne niedziele oraz święto Trzech Króli.",
        "transkrypcja": """92. [u dołu: 88.]
lić et alia inconvenientia quae ob reverentiam Actorum Officii exprimi nequeunt jednak obieta sibi cruda in termino termini declaraturam offert se eodem testanti.

Sub Eodem Actu.
Ad Officium et Acta praesentia personaliter venientes HH. Martinus Boron [?] una cum Alberto Skakha [?] suburbani Crasnicenses fideiussores pro H. Simone Draganek ratione ferri et liquidi debiti hoc est non redditionis pięciu spustów wódki prostey quod crematum per ipsum iam a festo S. Joannis Baptistae reddi debuerat Infideli Wygdor Markowicz Judaeo pro tunc Dno suo hi quidem praefati fideiubentes ex amicitia christiana videntes in carceratum prefatum Draganek eundem ex carceribus liberaverunt nihilominus restitutionem plebisi provenientem praefati cremati pięciu spustów sub bonis suis quam et ipsis assecuraverunt et sese per ipsum in casu non restitutionis inscripserunt primo ab Actu praesenti incipiendo pro Dominica incidente et ventura unum vas alias spust, deinde pro sequenti Dominica itidem vas alterum et subsequenti tertia hebdomada medii vasis alias pół spustu wódki, residuitatem vero półtrzecia spusta assecuraverunt że zobowiązali się na trzech ratach oddać pomieniony Draganek na Święto Trzech Królów w roku przyszłym nadchodzące półtora spustu wódki w tydzień zaś po Trzech Królów ostatni spust. Salva tamen actione ratione litis expensarum per Actorem wydanych dla uporu""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 185,
        "numer_pozycji": "185",
        "strona_pagina": "fol. 92v (92v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Spis kontumacji dłużników Bractwa Literackiego (wosk do ołtarza)",
        "osoby_podmioty": "ks. Baltazar Pałuskiewicz (kanonik regularny, promotor Bractwa Literackiego), bedel Wojciech Ornatowski, Szymon Jankowski, Maciej Pielichowicz, Stanisław Jesurkiewicz, Stanisław Rebiński, Maciej Abel (Camax), Tomasz Nowacki, Jakub Dubaj",
        "kwoty_podatki": "1 funt i 0,5 funta wosku (do ołtarza)",
        "opis_sprawy": "Pod datą 8 października 1698 r. (Feria Quarta post Festum S. Francisci) seria kontumacji z instancji ks. Baltazara Pałuskiewicza, kanonika regularnego kraśnickiego i promotora Bractwa Literackiego, za pośrednictwem bedela Wojciecha Ornatowskiego o zaległe czynsze kościelne w wosku na rzecz ołtarza Bractwa Literackiego (Altare Confraternitatis Literatorum): skazani na pół lub cały funt wosku (pociążeni: Szymon Jankowski, Maciej Pielichowicz, Stanisław Jesurkiewicz, Stanisław Rebiński, Maciej Abel Camax, Tomasz Nowacki, Jakub Dubaj).",
        "transkrypcja": """92v.
pomienionego nieoddającego przy wydaniu spustów sobie należytych zachowuie. Quod in forma fideiussionis quam perfectissima et plenissima est connotatum.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quarta post Festum Sancti Francisci Confessoris proxima Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [8 X 1698].
Ex Instantia Venerabilis Baltazaris Pałuskiewicz Promotoris Sacratissimi Rosarii Ecclesiae Canonicorum Regularium Crasnicensis Quoniam citata per Providum Albertum Ornatowski Bedellum Officii praesentis personaliter proventa Contumax ratione non solutionis census retenti ad Ecclesiam suam pertinentis. In cuius contumaciam decernitur restitutio unius pondo Cerae ad Altare Confraternitatis Literatorum.
Item Simon Jankowski ex Instantia eiusdem ut supra personaliter proventus per Bedellum reddito medium pondo Cerae ad idem Altare.
Item Mathias Pielichowicz in simili contumax personaliter proventus.
Item Stanislaus Jesurkiewicz proventus ratione non solutionis census retenti ab ultima quietatione similiter.
Item Stanislaus Rebiński simili ratione non solutionis census ab ultima quietatione in cuius contumaciam decernit medium pondo cerae.
Item Mathias Abel Camax in cuius contumacia decernitur medium pondo cerae personaliter proventus.
Item Tomasz Nowacki contumax medium cerae.
Item Jacobus Dubaj contumax in simili.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 186,
        "numer_pozycji": "186",
        "strona_pagina": "fol. 93r (93 / 89)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Spór Barankowicza ze Stachowiczem oraz zeznanie Tomasza Jardziocha",
        "osoby_podmioty": "Jan Barankowicz, Błażej Stachowicz, Tomasz Jardzioch [?], Paweł Słomkowski, Wojciech Peron, Matyjasz Peron, Jakub Wawrzyło",
        "kwoty_podatki": "-",
        "opis_sprawy": "Odroczenie sprawy rajcy Jana Barankowicza przeciw Błażejowi Stachowiczowi z uwagi na chorobę i złożenie przysięgi (legalitas infirmitatis) pozwanego; poniżej zeznanie świadka Tomasza Jardziocha [?] z instancji Pawła Słomkowskiego o nocnym zwiezieniu snopów z pola w wigilię św. Bartłomieja przez Wojciecha Perona (syna Matyjasza Perona) z bratem Jakubem Wawrzyłem; na dole dekret w sprawie Słomkowskiego przeciw Maciejowi Peronowi i Wojciechowi Wawrzyłowi (3 dni wieży).",
        "transkrypcja": """93. [u dołu: 89.]
Sub Eodem Actu.
Sławetny Pan Barankowicz Radca Kraśnicki wnosi skargę na przeciwko Uciwemu Błażejowi Stachowiczowi iż on w teyże gospodzie będącego Aktora naprzód słowy zelżył pobił przy znaku o czym szerzey de praemissis protestatio una cum obductione opiewa. Ex adverso pars citata per consortem suam intulit legalitatem infirmitatis mariti sui ex occasione zadania ran w domu przez Aktora prosita aby ta w rezydencyi pisała póki rey prawa nie ma którego czego zapłacił potem nie odwłóczy. Ponieważ Actor alligationem legalitatis dictae infirmitatis eandem causam ad convalescentiam citatae decernit postquam convaluerit compareat. Interea temporis partes utraeque inquisitionem pro feria sexta proxime ventura expediant.

Sub eodem Actu.
Testis. Uciwy Tomasz Jardzioch [?] ad instantiam Famati Pauli Słomkowski Viceadvocati ad perhibendum fidele veritatis testimonium per Bedellum Officii citatus haec deposuit iż ia jadąc z żoną y synem swoim z pola między tutejszemi pod lasem w nocy w święto S. Bartłomieja spotkaliśmy Wojciecha Perona syna Uciwego Matyasza Perona my z pola iuż nie rychło jechali z pola a pomieniony Wojciech Peron z rodnym bratem Jakubem Wawrzyłem jechali na wozie drabiniastym y mieli snopki na zadzie tego wozu jechali w pole ku domom.

Sub Eodem Actu.
Inter Famatum Paulum Słomkowski et Mathiam Peron Patrem et Albertum filium ratione suae obiectae decreti quatenus decreto ante non lato satisfaciat doceat de loco standi sub carceris detrusionem per tres dies ratione non observationis Officii.
Item Albertus Wawrzyło adcitatus per Bedellum Officii sui compareat.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 187,
        "numer_pozycji": "187",
        "strona_pagina": "fol. 93v (93v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Kontumacja Nowackich oraz poręczenie za Matyjasza Perona (9 X 1698)",
        "osoby_podmioty": "Katarzyna Nowacka, Wojciech Nowacki, Ubald Janaszkowicz (zm.), Paweł Słomkowski, Wojciech Piasecki, Marcin Świeczka, Matyjasz Peron, Wojciech Peron",
        "kwoty_podatki": "-",
        "opis_sprawy": "Pierwsza kontumacja sukcesorów zmarłego Ubalda Janaszkowica (Katarzyny i Wojciecha Nowackich) z instancji wicewójta Pawła Słomkowskiego o niezapłacony dług; poniżej pod datą 9 października 1698 r. (Feria Quarta post Festum S. Francisci Die Nona Octobris) przedmieszczanie Wojciech Piasecki i Marcin Świeczka stają się rękojemcami za uwięzionego Matyjasza Perona w sprawie z Pawłem Słomkowskim o oskarżenie syna jego Wojciecha Perona o szkodę.",
        "transkrypcja": """93v.
Sub Eodem Actu.
Successores videlicet Spectabilis Catharina Nowacka et Spectabilis Albertus Nowacki coniuges olim Spectabilis Ubaldi Janaszkowicz Advocati Crasnicensis Citati per Bedellum Albertum Ornatowski Ex Instantia Famati Pauli Słomkowski Viceadvocati Crasnicensis ratione non solutionis certi debiti in processu causae introducti et expressi primo contumax.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quarta post Festum Sancti Francisci Confessoris proxima Die Nona Octobris Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [9 X 1698].
Przed Urzędem y Aktami Wójtowskiemi y Ławniczemi Kraśnickiemi w osobach swoich stanąwszy Uciwi Wojciech Piasecki Marcin Świeczka Przedmieszczanie Kraśniccy assekurowali y submittowali się na dobrach swoich ruchomych y nieruchomych w sprawie z Aktorem Sławetnym Panem Pawłem Słomkowskim Podwójcim Kraśnickim Uciwemu Matyaszowi Peronowi o oskarżenie Wojciecha Perona syna jego względem szkody uczynienia inkarcerowanego onegoż eliberować z więzienia onego wyręczyli obiecując iż jeżeliby pomieniony Matyasz Peron nie stawił na przyszłe prawo y zady jego albo sam uciec miał oni za niego odpowiedzą y satisfakcyą czynić w tey sprawie ferowanemu dekretowi. Quod est connotatum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 188,
        "numer_pozycji": "188",
        "strona_pagina": "fol. 94r (94 / 90)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Intromisja Jadwigi Tokarzowej w kwaterę roli Jurkowskiej na Przedmieściu",
        "osoby_podmioty": "Paweł Słomkowski, Adam Trzelowicz [Chmielowicz?], Jadwiga Tokarzowa, Jan Tokarz (zm.), Jan Onufry Kieniewicz [Onupkiewicz?], Paweł Jurek, Wawrzyniec Kowalik, Zofia Jurek [?], Jan Skowronek, Stanisław Jan",
        "kwoty_podatki": "-",
        "opis_sprawy": "Pod datą 9 października 1698 r. (Feria Quinta post Festum S. Francisci) na rekwizycję Jadwigi Tokarzowej wdowy po Janie Tokarzu przedmieszczaninie kraśnickim wicewójt Paweł Słomkowski i pisarz Adam Trzelowicz z rozporządzenia adwokata Jana Onufrego Kieniewicza dokonują pomiaru i intromisji w kwaterę roli zwaną Jurkowską na Przedmieściu Kraśnickim (między kwaterą Pawła Jurka a kwaterą Wawrzyńca Kowalika, aż do granicy Sopowskiej, wraz z sadem i chałupą) kupioną przez Jana Skowronka dla bractwa/kościoła.",
        "transkrypcja": """94. [u dołu: 90.]
Actum Coram Officio Crasnicensi Advocatiali et Scabinali Feria Quinta post Festum Sancti Francisci Confessoris proxima Die Videlicet Nona Octobris Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [9 X 1698].
Famatus Paulus Słomkowski Viceadvocatus Crasnicensis et Honoratus Adamus Trzelowicz [Chmielowicz?] Notarius Actorum praesentium. Na Rekwizycyą Jadwigi Tokarzowey niegdy Uciwego Jana Tokarza Przedmieszczanina Kraśnickiego małżonki pozostałej wdowy ex ordinatione Famati Joannis Onupkiewicz [Kieniewicz?] Advocati Crasnicensis deputati ad metanda bona Jurkowska dicta in Suburbio Crasnicensi między dobrami to iest z iedney strony między kwaterą Uciwego Pawła Jurka z drugiey strony Uciwego Wawrzyńca Kowalika z drugiey strony kwatera także począwszy od granicy Suchowskiej a kończąca się taż kwatera przy granicy Sopowskiej sita et iacentia dobra pierwsza kwaterę y z siedliskiem na którym sadek iest y chałupa ze wszystkiemi okolicznościami ex parte Confraternitatis... Zophia [?] cum olim Honesto Joanne Skowronek procreata venditis emptis intromissionem nemine impugnante et hic subinde H. Stanislaus et Jan""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 189,
        "numer_pozycji": "189",
        "strona_pagina": "fol. 94v (94v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Zeznanie Stanisława Jesurkiewicza o bójce Barankowicza ze Stachowiczem u Żyda Borucha",
        "osoby_podmioty": "Stanisław Jesurkiewicz, Wojciech Ornatowski, Błażej Stachowicz, Żyd Boruch alias Halka, Jan Barankowicz, Jan Żmienda, Chmiel, Baran",
        "kwoty_podatki": "kilkanaście groszy",
        "opis_sprawy": "Dokończenie intromisji z fol. 94r (budynek z trzy lata stojący dla Zofii Regińskiej [?]); poniżej pod datą 10 października 1698 r. (Feria Sexta post Festum S. Francisci) zeznanie starego rajcy Stanisława Jesurkiewicza na żądanie Błażeja Stachowicza szewca i majstra o zajściu w szynku u Żyda Borucha alias Halki: gdy stary rajca i rajca Jan Barankowicz z Janem Żmiendą pili miód, Błażej Stachowicz pił piwo z Chmielem i Baranem i zaczęła się sprzeczka o pieniądze za chmiel i długi.",
        "transkrypcja": """94v.
parobek na pomienioney kwaterze gruncie Jurkowskim nieczynny z budowania budynku od lat trzech satisfactio ut at który to pietnaście z nich kurki [?] w personam pomienioney Regińskiej [?] forbi authet intromissionem dederunt.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Sexta post Festum Sancti Francisci Confessoris proxima Die Decima Mensis Octobris Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [10 X 1698].
Sławetny P. Stanisław Jesurkiewicz Consul antiquus ad perhibendum fidele veritatis testimonium praestito iuramento corporali per Providum Ornatowski Bedellum eiusdem Officii. Ex Instantia Honorati Blasii Stachowicz rzemiosła szewskiego majstra taliter deposuit testimonium: W dzień przeszły poniedziałkowy byłem proszony od Uciwego pomienionego Błażeja Stachowicza na kwater piwa do Żyda Borucha alias Halki względem uspokojenia się z sobą z Janem Stępniem szwagrem jego, tamże w rezerwacji zanami przyszli JP. Jan Barankowicz Radca Kraśnicki z Uciwym Janem Żmiendą kazali sobie dać półgarca miodu, myśmy zaś rezerwacyą piwem swojem mianowicie pomieniony Błażej Stachowicz częstowali się nie tylko obadwa ale że i przybrał Stachowicz aby pił piwo od niego P. Barankowicz rzekł ty Błażnie Chmielu pijesz sam day mi pokój na te słowa tam Chmiel alias Baran małe rzeczy Baranowi zayca uznać a do strony też Żmienda Jan będący z Panem Barankowicem o watkę dużego aby się konował żeby mu Baranowski ustąpił pomieniony Stachowicz rzekł do mnie hamujmy pa-""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 190,
        "numer_pozycji": "190",
        "strona_pagina": "fol. 95r (95 / 91)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dokończenie zeznania o bójce u Borucha oraz skład sądu 10 X 1698 r.",
        "osoby_podmioty": "Stanisław Jesurkiewicz, Jan Barankowicz, Błażej Stachowicz, Jan Żmienda, Jan Onufry Kieniewicz [Onupkiewicz?], Adam Potokowicz [Potocki], Paweł Słomkowski, Stefan Kwasowic, Wojciech Piasecki, Jan Murowski",
        "kwoty_podatki": "kilkanaście groszy",
        "opis_sprawy": "Ciąg dalszy relacji Stanisława Jesurkiewicza: kłótnia w karczmie Borucha o kilkanaście groszy, wyzwiska ('siedź diabli Baranie'), uderzenie Jana Barankowicza w twarz i wyszarpanie za włosy przez Błażeja Stachowicza, którego rozdzielał Jan Żmienda; poniżej skład urzędu z 10 X 1698 r. (adwokat ordynaryjny Jan Onufry Kieniewicz, prokonsul Adam Potokowicz, rajca Jan Barankowicz, wicewójt Paweł Słomkowski, stary rajca Stanisław Jesurkiewicz, rajca Stefan Kwasowic) oraz dylacja w sprawie Wojciecha Piaseckiego przeciw rajcy Janowi Murowskiemu.",
        "transkrypcja": """95. [u dołu: 91.]
chołek nie ma się czym animować bo jednego chłopca zrobił znać krótkie albo długie jeżeli krótkie nad stan mierzyć długie więc P. Barankowicz stanął przy nim ponieważ wziąwszy gorzałkę rzekł y tobie trzeba gęby wziąć boś tu gadał w tym wyszarpnął rękę swoje z gorzałki wypadło mu kilkanaście groszy a za tym rzekł siedź diabli Baranie obymi pieniędzy wytrącił z garści P. Barankowicz rzekł na to nie prawdę mówisz pomalu P. Barankowicz pomusnął mu po gębie, czego on w tym razie w gębę słusznie uderzył pięścią y za głowę porwał pokrzywił się P. Barankowicz y pięścią jego bez słów przytomnego bez rozwodu y Żmienda za tym porozwadzaniu sława nieuczciwe wołał nie tylko na P. Barankowicza ale y na urząd cały które dla poszanowania ksiąg pisać niepodobna za temi słowy powtórne porwał się do niego P. Barankowicz chciał mu w gębę dać on gorzałek broniący go Żmienda trzymał Barankowicza w pół by nie mogąc go dostać za głowę po twarzy go podrapał sięgać więcej nie wiem.

Sub eodem Actu.
Praesentibus Famatis Joanne Onupkiewicz [Kieniewicz?] Advocato Ordinario Crasnicensi, Adamo Potokowicz Proconsule, Joanne Barankowicz Consule, Paulo Słomkowski Viceadvocato, Stanislao Jesurkiewicz Antiquo Consule, Stephano Kwasowic.
Inter Honestum Albertum Piasecki ab una et Joannem Murowski Consulem datur dilatio Inquisitionis pro prima iura expedienda.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 191,
        "numer_pozycji": "191",
        "strona_pagina": "fol. 95v (95v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dekret na inkwizycję w sporze Pawła Słomkowskiego z Nowackimi o 802 złp 15 gr",
        "osoby_podmioty": "Paweł Słomkowski, Wojciech Nowacki, Katarzyna Janaszkowicowa [Nowacka], Ubald Janaszkowicz (zm.), Andrzej Brzozowski [?], Jan Barankowicz, Błażej Stachowicz",
        "kwoty_podatki": "802 złp 15 gr",
        "opis_sprawy": "W sprawie z powództwa podwojciego Pawła Słomkowskiego przeciw Wojciechowi Nowackiemu landwójtowi urzędowskiemu i Katarzynie Janaszkowicowej małżonkom jako dziedzicom i posesorom dóbr po zmarłym wójcie Ubaldzie Janaszkowiczu o 802 złp 15 gr (z udziałem pełnomocnika Andrzeja Brzozowskiego [?]): sąd dopuszcza dowód z zeznań świadków i przysięgi do tygodnia, nakazując pozwanym osobiste stawiennictwo z dokumentami; poniżej dalsza dylacja na inkwizycję w sprawie Jana Barankowicza przeciw Błażejowi Stachowiczowi.",
        "transkrypcja": """95v.
Sub eodem Actu.
W sprawie y Akciey od Sławetnego Pana Pawła Słomkowskiego Podwójciego Urzędu Wójtowskiego y Ławniczego Kraśnickiego praesentibus ut in Actu Sławetnym Panom Wojciechowi Nowackiemu Landwójtowi Urzędowskiemu y Katarzynie Janaszkowicowey małżonkom dóbr niegdy Sł. P. Ubalda Janaszkowica Wójta Kraśnickiego dziedzicom y possessorom intentowaney o dług złotych ośmset y dwa groszy pietnaście [802 zł 15 gr] intentowaney iako propozycya in scripto podana szerzey opiewa. W którey sprawie strony powodowa przez tu pozwaną przez Urodzonego Pana Andrzeja Brzozowskiego [?] plenipotenta stanąwszy. Ponieważ powodowa strona zabiera się na dowód świadkami o długu pomienionym w regestrze podanym świadomemi, sąd mimo własne pozwanych upominanie iż nie broniąc informacyey słuszney sądowi nie chce ale Aktor świadkami y Juramentem dowieść chce sąm iest pozwolony aby dowodził w tygodniu a data praesentis decreti interea aby się stawił osobami swemi stanęli z gotowością munimentów któremi się bronić mogą pod winami prawemi y upadkiem sprawy stronie do dna przyszłego piątkowego za dni tydzień peremptorie citato.

Sub Eodem Actu.
Causae Actionis ex parte Famati Joannis Barankowicz Actorem simul et Citati Blasii Stachowicz citati et Actorum combinatis Actoribus et Reatibus ulterior dilatio Inquisitionis datur quatenus sine ulla adcitatione in termino conservato compareant pro iuramentum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 192,
        "numer_pozycji": "192",
        "strona_pagina": "fol. 96r (96 / 92)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Kontumacje (Sitarski, Bzówka), kradzież snopów u Bartłomieja syna Piwnika i wizja szkody Kondyszka",
        "osoby_podmioty": "Paweł Słomkowski, Matyjasz Peron, Franciszek Sitarski, Bzówka [?], Jan Barankowicz, Jan Pacławkowic [?], Bartłomiej Piwnik [?], Adam Trzelowicz [Chmielowicz?], Wawrzyniec Bielaszkowic, Jan Onufry Kieniewicz [Onupkiewicz?], Krzysztof Tropycak [?], Wojciech Kondyszek [?]",
        "kwoty_podatki": "7 dni wieży",
        "opis_sprawy": "Dalszy ciąg sporu Pawła Słomkowskiego z Matyjaszem Peronem; kontumacja Franciszka Sitarskiego i Bzówki [?] z instancji Jana Barankowicza (7 dni wieży); zeznanie Jana Pacławkowica [?] o kradzieży snopów zboża w nocy z gumna Bartłomieja syna Piwnika [?]; poniżej pod datą 11 października 1698 r. (Sabbatho post Festum S. Francisci) pisarz Adam Trzelowicz i ławnik Wawrzyniec Bielaszkowic z mandatu adwokata Jana Onufrego Kieniewicza składają relację z wizji szkody na gruncie Krzysztofa Tropycaka [?] wywołanej przez bydło Wojciecha Kondyszka [?].",
        "transkrypcja": """96. [u dołu: 92.]
Sub Eodem Actu.
Inter Famatum Paulum Słomkowski Viceadvocatum Crasnicensem et H. Mathiam Peron et filium eius ulterior Inquisitio interea ratione non solutionis marcarum ad elocandum standi ad carceres defereatur ad finem iuris.

Item Franciscus Sitarski y Bzówka [?] ex Instantia Spectabilis Joannis Barankowicz Consulis Contumaces ratione contemptionis prout superius scripto continetur. In cuius contumaciam decernitur lucrum poenarum septem turris per eosdem. Causae limitantur ad feriam secundam proxime venturam.

Sub Eodem Actu.
Honestus Joannes Pacławkowic [?] zeznał że pod kątem w nocy u Bartłomieja syna Piwnika [?] na poprzeczce od dworu stojąc od domu iechał wozem z końmi drabiniastym wiózł na zadzie snopy zboża alem niewiem czyjego.

Actum Crasnicii Sabbatho post Festum Sancti Francisci Confessoris proxima Die Videlicet Undecima Octobris Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [11 X 1698].
Ad Officium et Acta praesentia Officii Crasnicensis personaliter venientes Spectabiles ac Honorati Adamus Trzelowicz Notarius Actorum praesentium iuratus et Laurentius Bielaszkowic Scabinus Juratus in rem suam iuratam fidelis relationis publice libere recognoverunt. Quippe ex Officio regii hominis ex mandato Spectabilis Domini Joannis Onupkiewicz [Kieniewicz?] Advocati Ordinarii ex Instantia H. Christophori Tropycak [?] Suburbano Crasnicensi""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 193,
        "numer_pozycji": "193",
        "strona_pagina": "fol. 96v (96v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dokończenie wizji szkody u Tropycaka oraz protestacja Stanisława Dutkiewicza przeciw Rzepce",
        "osoby_podmioty": "Krzysztof Tropycak [?], Wojciech Kondyszek [?], Stanisław Dutkiewicz, Marcin Rzepka, Adam Petek [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie relacji z wizji na gruncie Krzysztofa Tropycaka [?] (zniszczona trawa i niezagrodzony płot przez sąsiada Wojciecha Kondyszka [?]); poniżej pod datą 13 października 1698 r. (Feria Secunda ante Festum S. Hedvigis) protestacja przedmieszczanina Stanisława Dutkiewicza przeciw Marcinowi Rzepce o napaść przy stole w domu P. Wójta w obecności Adama Petka [?], uderzenie pięścią w twarz i rzucenie pod ławę.",
        "transkrypcja": """96v.
descendentes in et ad domum ipsius... in Actu contenta. Wpisać w Rynku przez z pasioney trawy bydła swego... przez Uciwego Wojciecha Kondyszka [?] sąsiada. Chodziliśmy na wizyą szkody wyżey pomienionego Uciwego Krzysztofa Tropycaka [?] Przedmieszczanina Kraśnickiego, nam na łące przy domu swoim pokazał że mu trawę po kilka razy a mianowicie teyże nocy spasiono bydła wypust Uciwego Wojciecha Kondyszka sąsiada która jest zapłotem... także pokazał nam płot cały od swego domu cały także y od głowy tegoż ogroda bez płotu y od sadyby... pomieniony Kondyszek niema że nie może płota swego nie chce grodzić y przegrodzi się od niego a to czyni na szkodę requirunt. Quae praemissa fideliter recognita Actis praesentibus sunt connotata.

Actum Crasnicii Feria Secunda ante Festum S. Hedvigis Viduae Electae die 13 Octobris Ao 1698 [13 X 1698].
[Na marginesie: Honestus Stanislaus Dutkiewicz Suburbanus Crasnicensis...]
Do Urzędu y Akt niniejszych Wójtowskich y Ławniczych Kraśnickich w osobie swojey przyszedłszy solennie protestował się przeciwko Uciwemu Marcinowi Rzepce iż on bez dania okazyi w dom S. Pana Wójta Kraśnickiego przy stole siedząc spokojnie na przed y konferencyą z Uciwym Adamem Petkiem [?] rozerwał y mowę nie potrzebną wtrącił przeciwko niemu upominając się o dług za półkurca o Tatarce gdy go prosił na piwo mówiąc mu żeby go do stołu na gospodzie nie zachodził y gdy pomieniony foss [?] będący w niniejszym proteście stanął rzekł żeby go zaniechał turbować gdyż nie zbieżny łot, za tym słowami dał mu w gębę y czuprynę w kraty wrzucił pod ławę mówiąc... Obiecuje z nim o to swoje naście ubi de iure venerit.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 194,
        "numer_pozycji": "194",
        "strona_pagina": "fol. 97r (97 / 93)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Protestacja szewca Tomasza Mutkowica przeciw Szymonowi Soleckiemu oraz dekret Słomkowski vs Nowacka",
        "osoby_podmioty": "Tomasz Mutkowic (towarzysz szewski), Szymon Solecki (majster szewski), Paweł Słomkowski, Katarzyna Nowacka, Adam Potokowicz [Potocki], Jan Murowski, Stefan Kwasowic, Wawrzyniec Bielaszkowic, Stefan Wierzbicki [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Pod datą 13 października 1698 r. protestacja Tomasza Mutkowica towarzysza rzemiosła szewskiego przeciw swojemu majstrowi Szymonowi Soleckiemu o obrazę czci i oskarżenia przed gośćmi z rzemiosła i towarzyszami w niedzielę po święcie św. Franciszka; poniżej pod datą 17 października 1698 r. (Feria Sexta pridie Festi S. Lucae) w sprawie Pawła Słomkowskiego przeciw Katarzynie Nowackiej (przy sądzie: Adam Potokowicz, Jan Murowski, Stefan Kwasowic, Wawrzyniec Bielaszkowic) z udziałem pełnomocnika Stefana Wierzbickiego [?].",
        "transkrypcja": """97. [u dołu: 93.]
Actum Crasnicii Feria Secunda ante Festum Sanctae Hedvigis die decima tertia Octobris Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [13 X 1698].
Ad Officium et Acta praesentia Advocatialia et Scabinalia Crasnicensia personaliter veniens Thomas Mutkowic rzemiosła szewskiego towarzysz żałobnie protestował się przeciwko Uciwemu Szymonowi Soleckiemu przeszłemu Majstrowi swemu tegoż rzemiosła szewskiego oto iż on zapomniawszy miłości Boga y bliźniego lekce sobie poważając prawo zadał temuż calumnias winy opisane ważył się w cechowych rzeczach z rzemiosła przy braci wszystkich y towarzyszach dnia wczorajszego bez dania okazyi niniejszego protestanta nie miawszy do niego żadney interesy gdyż się już protestant porachowawszy się z nim w niedzielę przeszłą na tamtej po święcie S. Franciszka w sprawie dobrowolnie odprawił się o rzeczy pewne które się i w rewerentiam Actorum et Officii praesentis wspomnieć nie godzi inne opprobria zadał których ieżeliby się za terminem danym zaprzeć chciał protestant Inkwizycyą dowieść będzie gotów. O beczkę przed nim o tę rzeczy y zniewagi prawem ubi de iure venerit czynić.

Actum Feria Sexta pridie Festi Sancti Lucae Apostoli et Evangelistae Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [17 X 1698].
Inter Słomkowski et Nowackie Citt. In termino conservato.
In iudicio praesente Adamus Potokowicz et Joannes Murowski, Stephanus Kwasowic, Laurentius Bielaszkowic.
Ponieważ strona pozwana przez plenipotenta swojego tan processu acceptowała dekret, a nie stanęła sub succubitione in causa samym przez plenipotenta informowany legalney racji nie ma przez Stephanum Wierzbicki [?] plenipotentem comparentem.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 195,
        "numer_pozycji": "195",
        "strona_pagina": "fol. 97v (97v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dekret w sporze Słomkowskiego z Nowacką oraz zeznanie Jana Barankowicza o wójcie Janaszkowiczu",
        "osoby_podmioty": "Katarzyna Nowacka, Paweł Słomkowski, Jan Barankowicz, Ubald Janaszkowicz (zm.), P. Wojtanowski [?], Piotr Koronny [?]",
        "kwoty_podatki": "2 grzywny; 14 grzywien; 160 złp; 60 złp",
        "opis_sprawy": "Dokończenie dekretu z 17 X 1698 r.: Katarzyna Nowacka zwalczona o zapłatę 2 grzywien, a do piątkowego terminu ma stawić się z dokumentami pod karą 14 grzywien (również Słomkowski pod 14 grzywnami do okazania dokumentów przy dwóch ławnikach); poniżej zeznanie rajcy Jana Barankowicza ze strony Pawła Słomkowskiego w sprawie długu po zmarłym wójcie Ubaldzie Janaszkowiczu: przypomina dług 160 złp za gospodarstwo i 60 złp na budynek, które Słomkowski wypłacał dla wójta, oraz udział P. Wojtanowskiego [?] i Piotra Koronnego [?].",
        "transkrypcja": """97v.
przed sobą opowiadając się że Paniey Nowackiey na sąd zadławił żeby długu albo zaparcia tey sprawy skłonić nie myślę aż w sprawie idzie y nie staje do sądu aby dała grzywien dwie. Interea aby stanęła sub maribus pro feria sexta proxime ventura pod winami videlicet grzywien czternastu parti et Judicio per medium cum paratis monumentis accedat. Famatus Słomkowski sub poena dupli quatuordecim marcarum polonicalium tenetur ad deductionem debiti ante eandem feriam secundam... eundem etiam przy prezencyi dwóch PP. Ławników uproszonych iuramentum.

Sub Eodem Actu.
Testis. Spectabilis Joannes Barankowicz Consul Crasnicensis ex parte Famati Pauli Słomkowski Viceadvocati respectu debiti apud successores olim Spectabilis Ubaldi Janaszkowicz Advocati praetensi taliter recognovit:
Jest temu lat dwie całkiem plus minus jako żywo za nieboszczyka w pewney będąc u P. Słomkowskiego wspominał że przedemną że mi nieboszczyk P. Ubaldy Janaszkowicz winien długu mówiąc że mi po kilkanaście razy pożyczał y nie oddał, także za nieboszczyka Pana Ubaldego Wójta Kraśnickiego uchwalono zł sto sześćdziesiąt y sześćdziesiąt w nagrodę za gospodarstwo śp. chrzestne nieboszczyk sławny i brał za swe pieniądze P. Wojtanowski [?] od P. Piotra Koronnego [?] i chować i brał o bycie i zbycie, a nie chciał oddać tylko o tym nie myślał.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 196,
        "numer_pozycji": "196",
        "strona_pagina": "fol. 98r (98 / 94)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Zeznanie Wojciecha Grzymałowskiego, kontumacja Agnieszki Wereszczyny i zeznanie Tomasza Parciaka",
        "osoby_podmioty": "Wojciech Grzymałowski, Paweł Słomkowski, Ubald Janaszkowicz (zm.), Potokowski [Potocki?], Agnieszka Wereszczyna, Tomasz Jutratek [?], Jan Barankowicz, Błażej Stachowicz, Tomasz Parciak [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Zeznanie ławnika Wojciecha Grzymałowskiego o zleceniu od Pawła Słomkowskiego dla długów zmarłego wójta Ubalda Janaszkowica (z apelacją strony pozwanej dopuszczoną przez sąd); dylacja Słomkowskiego z Peronem; kontumacja Agnieszki Wereszczyny wdowy przeciw Tomaszowi Jutratkowi [?] o nieoddanie lnu i płótna; dylacja w sporze Barankowicza ze Stachowiczem; poniżej pod datą 18 października 1698 r. (Sabbatho ipso die Festi S. Lucae) przysięgłe zeznanie przedmieszczanina Tomasza Parciaka [?] z instancji Pawła Słomkowskiego.",
        "transkrypcja": """98. [u dołu: 94.]
Testis. Famatus Albertus Grzymałowski Scabinus Juratus fide iurata recognovit: Ledwie co pamiętam żem był użyty to od Pana Pawła Słomkowskiego Podwójciego Kraśnickiego który mi zlecił iako zeznał długu nieboszczyka P. Ubalda Janaszkowica Wójta Kraśnickiego odbijąc sobie chata po moim ożenieniu o innych długach niewiem które sobie pretenduie Potokowski [Potocki?]. Od którego dekretu strona pozwana appellowała ad iudicem competentem quod est admissum cum debita reverentia.

Inter F. Słomkowski et Peron ratione damni facti datur ulterior dilatio Inquisitionis.
Ex Instantia H. Agnetis Wereszczyna Vidua H. Thomae Jutratek [?] non comparens ratione nieoddania lnianego płótna contumax.
Inter F. Joannem Barankowicz Consulem et H. Blasium Stachowicz Actores simul et Cittatos... datur ulterior dilatio Inquisitionis sub succubitione in causa.
Causae omnes limitantur ad feriam secundam proxime venturam.

Actum Crasnicii Sabbatho ipso die Festi S. Lucae Apostoli et Evangelistae die 18 8bris Ao 1698 [18 X 1698].
Ex Instantia Famati Pauli Słomkowski Viceadvocati Crasnicensis Honestus Thomas Parciak [?] Suburbanus Crasnicensis praestito iuramento corporali ad imaginem et crucifixum Jesu Dni observata solemnitate iuramentorum tale deposuit testimonium his formalibus:""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 197,
        "numer_pozycji": "197",
        "strona_pagina": "fol. 98v (98v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Zeznania Tomasza Parciaka i Szymona Wójcika o długu po Ubaldzie Janaszkowiczu (20 X 1698)",
        "osoby_podmioty": "Tomasz Parciak [?], Ubald Janaszkowicz (zm.), Paweł Słomkowski, Katarzyna Nowacka, P. Zuławski [?], Szymon Wójcik [Wojcik], P. Stadnicki (stolnik czernihowski)",
        "kwoty_podatki": "1200 wozów/drzewa; 100 kop słomy; talary",
        "opis_sprawy": "Zeznanie Tomasza Parciaka [?] o folwarku wójtowskim przed 30 laty, płatwach i słupach sosnowych (40 sztuk) wziętych od Pawła Słomkowskiego dla nieboszczyka Ubalda Janaszkowica na budowę na folwarku (oraz wyliczenie, że Katarzyna Nowacka supplikowała do P. Zuławskiego [?]); poniżej pod datą 20 października 1698 r. (Feria Secunda post Festum S. Lucae) zeznanie przedmieszczanina Szymona Wójcika [Wojcika] o tym, jak śp. Ubald Janaszkowicz pożyczał od Słomkowskiego niepełną faskę śledzi/gwoździ dla JP. Stadnickiego stolnika czernihowskiego i przyrzekł oddać dług.",
        "transkrypcja": """98v.
Mieszkałem na ten czas iest temu lat plus minus trzydzieści na folwarku gdzie usiadł trzymał z żoną y sukcessorowie jego Nieboszczyk P. Ubaldy Janaszkowic Wójt Kraśnicki użył mnie do roboty z końmi y wozem abym mu płatwy y słupy od Pana Słomkowskiego Podwójciego Kraśnickiego zwiózł na folwark starozakonnemu [?] a potem kiedy mówił nieboszczyk choćby mi po taleru dać za jedną to oddam Panu Słomkowskiemu płatwy wozem sosnowych czterdzieści sztuk krótkich dwadzieścia słupów nie mówiłem tylko że na placu pod murem wiedziałem które wózit nie wiem... Niebożęta Kufara mógł wóz... lepiej nieraz wspominał P. Słomkowski o dług swój a odrzeczwał y nie było przydziału P. Nowacka zorkąca supplikowała do Jejmości Pana Zuławskiego [?] sąm Jana w rzeczy nie wiem.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Secunda post Festum Sancti Lucae Apostoli et Evangelistae proxima die Vigesima 8bris Ao 1698 [20 X 1698].
Ex Instantia Famati Słomkowski Viceadvocati Crasnicensis Honestus Simon Wójcik [Wojcik] Suburbanus Crasnicensis praestito corporali iuramento ad imaginem et crucifixum Christi Dni observata iuramentorum solemnitate:
Wiem dobrze że Nieboszczyk P. Ubaldy Janaszkowicz u Pana Słomkowskiego pożyczył gwoździ gontowych faskę niepełną którą ia swemi rękami od niego przyniosłem na prośbę dla Jegomości Pana Stadnickiego Stolnika Czerniechowskiego y obiecał mu zapłacić a nie zapłacił aż byłem przy śmierci jego że prawie przy zgonie życia kazał spisać długi wszystkie także y gwoździe Panu Słomkowskiemu żeby za nie oddano.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 198,
        "numer_pozycji": "198",
        "strona_pagina": "fol. 99r (99 / 95)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Zeznanie Jana Żmiendy oraz wyrok na Błażeja Stachowicza (7 grzywien i 3 dni wieży)",
        "osoby_podmioty": "Jan Barankowicz, Jan Żmienda, Żyd Boruch, Błażej Stachowicz, Stanisław Jesurkiewicz, Paweł Słomkowski",
        "kwoty_podatki": "7 grzywien; 3 dni wieży",
        "opis_sprawy": "Zeznanie Jana Żmiendy z instancji rajcy Jana Barankowicza potwierdzające relację Stanisława Jesurkiewicza o kłótni i uderzeniu w twarz Barankowicza przez Błażeja Stachowicza u Żyda Borucha; poniżej sąd wójtowski i ławniczy w sprawie z powództwa Pawła Słomkowskiego nakazuje stronie przeciwnej przysiąc na rotę, że nie brali żyta ani nie wiedzą, kto je zabrał; na dole wyrok w sprawie Barankowicza przeciw niestawającemu Błażejowi Stachowiczowi — kara 7 grzywien i 3 dni wieży.",
        "transkrypcja": """99. [u dołu: 95.]
Ex Instantia Famati Joannis Barankowicz Testis taliter recognovit:
H. Joannes Żmienda. Byłem u Żyda Borucha kiedy Uciwy Błażej Stachowicz rzekł do Pana Barankowicza częstując go piwem słowami podane his formalibus: ieżeli długie masz infamora nie dając wziąć iednego chłopca zrobić. W ten czas kiedy za tym słowami pomusnął go po gębie a on wypadłszy ręce zza kręgu dał mu w gębę ut in testimonio Jesurkiewicz approbuje y toż zeznaię.

Sub Eodem Actu.
Na Terminie zażydym z relacyi Inkwizycyi tak powodowey do dowiedzenia toż też expurgowania się przesłuchawszy kontrowersyi praet contra oboey strony przeczytawszy Inkwizycye y niedobrze zrozumiawszy Sąd Wójtowski y Ławniczy Kraśnicki decydował aby obwiniony mąż z żoną y synem odprzysiągł się in eam iuramenti rotham że brali y nie wiedzą kto brał żyto o które obwinioni są od Sławetnego Pana Pawła Słomkowskiego.

In termino conservato ex Instantia Famati Joannis Barankowicz Consulis Crasnicensis Honestus Blasius Stachowicz ratione concussionis contemptionis contumax. In cuius contumaciam ratione postpositionis Officii praesentis ac temporis non comparentionis suo coram Officio decernitur poena septem Marcarum parti et Judicio per medium festo et turris trium dierum pro qua exequenda eadem poena detur familia civilis.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 199,
        "numer_pozycji": "199",
        "strona_pagina": "fol. 99v (99v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Wzajemna protestacja rajcy Jana Majowskiego i szafarza Wojciecha Piaseckiego o najście żołnierskie",
        "osoby_podmioty": "rajca Jan Majowski, przedmieszczanin i szafarz Wojciech Piasecki",
        "kwoty_podatki": "-",
        "opis_sprawy": "Pod datą 21 października 1698 r. (Feria Tertia post Festum S. Lucae) ostra protestacja rajcy Jana Majowskiego przeciw przedmieszczaninowi Wojciechowi Piaseckiemu (Longerowi), który pod pretekstem szafarstwa swego wysłał czeladź żołnierską po sieczkę do domu rajcy na szkodę jego matki i domu; poniżej natychmiastowa reprotestacja Wojciecha Piaseckiego, który wyjaśnia, że z urzędu szafarstwa miejskiego musiał dostarczyć sieczkę dla przejeżdżającej czeladzi żołnierskiej w imię dobra miasta.",
        "transkrypcja": """99v.
idque in instanti.
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Tertia post Festum Sancti Lucae Apostoli et Evangelistae proxima Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [21 X 1698].
Videatur hoc loco Protestatio certa Famati Joannis Majowski Consulis Crasnicensis in et contra H. Albertum Piasecki Suburbanum Longerum Crasnicensem idque in eo iż on nie respektując na winy w prawie przeciwko gwałtownikom pokoju pospolitego opisane będąc w terminach z niniejszym protestantem pod pretekstem szafarstwa swego uformowawszy sobie potrzebę sieczki którą protestant dla siebie rżnąć w domu swoim kazał, mogąc skąd inąd iey dostać subordinował familię mieyską y czeladź żołnierską sam osobą swoją drogę im pokazawszy aby gwałtem wzięli iakoż ledwie umieli ujść przed protestanta Matunka obroniła iednak przecie trzy musiała dać kiełki de quibus praemissis iniuriis protestatur et manifestatur.

Sub Eodem Actu.
Videatur hoc loco reprotestatio certa H. Alberti Piasecki Longeri Suburbano Crasnicensi contra Famatum Joannem Majowski Consulem Crasnicensem idque occasione mulctere indebite forum semphormis sui reprotestantis simul et protestantis, iż pro eo że branie swoje potrzeb ale usługi y funkcyą szafarstwa mieyskiego odprawujący tranom y pretensyi iakoż do pomienionego Sławetnego Pana Jana Majowskiego nie subordinował familię y też czeladź żołnierską znał się tego po sieczkę z domu jego ażeby sam osobą swoją przychodził gwałtem brać ale jako na pomoc całego Miasta trzeba było żołnierzom na drodze tydzień włożyć słysząc gdzie.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 200,
        "numer_pozycji": "200",
        "strona_pagina": "fol. 100r (100)",
        "sygnatura": SYGN,
        "data_rok": "1664",
        "kategoria": "Fascykuł z 1664 r.: dług Marcina Biernata (Szmara vs Szykowic) oraz ugoda Kaspra i Sebastiana Jajczyków",
        "osoby_podmioty": "Paweł Szmara, Maciej Szykowic, Marcin Biernat, Kasper Jajczyk, Sebastian Jajczyk",
        "kwoty_podatki": "3 złote",
        "opis_sprawy": "Karta otwierająca wszyty starszy fascykuł z roku 1664 ('Domini Millesimo Sexcentesimo Sexagesimo Quarto'): sprawa Pawła Szmary występującego w imieniu ojca przeciw Maciejowi Szykowicowi o poręczenie długu 3 zł za Marcina Biernata (sąd nakazuje spłatę 3 zł i kosztów prawnych oraz odroczenie do piątku na przysięgę starego Szmary); poniżej początek wpisu w sprawie ugody między Kasprem Jajczykiem aktorem a Sebastianem Jajczykiem pozwanym.",
        "transkrypcja": """100.
Domini Millesimo Sexcentesimo Sexagesimo Quarto [1664].
Inter Paulum Szmara Actorem et Mathiam Szykowic Citatum.
Proponował y skarżył się Actor imieniem Oyca swego o to iż pozwany ręczył Oycu jego zapłacić za Marcina Biernata złotych trzy. Ex adverso Citatus personaliter comparens negavit his formalibus: iagem ia za niego nie ręczył anim obiecywał płacić. Porro Actor statuit testem który zeznał to zeznawał do tego Szykowica że Szykowic przyobiecał staremu Szmarze ten dług złotych trzy oddać. Sąd iednak ninieyszy Wójtowski y Ławniczy Kraśnicki na kazał ażeby sam stary Szmara jako principalis Actor sua causa w około przyszły piątek stanął a realitatem debiti controversi przy tym świadku w tenże czas żeby poprzysiągł in eam rotham Jako tenże Szykowic przyjął na się ten dług to iest złotych trzy y przyobiecał go za Biernata płacić. Quo praestito tedy pomieniony Mathias Szykowic powinien mu będzie te złote trzy y expensa prawne oddać, salva Szykowicowi do pomienionego Biernata ratione promissorum reservata.

Inter Casparum Jajczyk et Sebastianum Jajczyk.
Na terminie dzisieyszym z przypozwu w sprawie między Kasprem Jajczykiem Aktorem a Sebastianem Jajczykiem Pozwanym do dekretu ferowania przypadającym na którym terminie gdy strony obiedwie personaliter stanęły anticipando tam rigorem iuris jako też ante latam sententiam et promulgatam zgoda między...""",
        "link_swa": UNIT_LINK
    }
]

main_data.extend(part8_scans)
with open('/home/ubuntu/workspace/Gen/main_data_j20_part8.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j20_part8.json: {len(main_data)} skanów")
