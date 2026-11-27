# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j20_part9.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
SYGN = "35/40/0/1/20"

part10_scans = [
    {
        "nr_skanu": 226,
        "numer_pozycji": "226",
        "strona_pagina": "fol. 113r (113)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Kwitacja Wojciecha Bożkowica na 20 złp i obdukcja pobicia Jana Smoka",
        "osoby_podmioty": "Wojciech Bożkowic, Jakub Lis, Jan Smok, Bartłomiej Wilk, Jan Wilk, Tomasz Wójcik",
        "kwoty_podatki": "20 złp",
        "opis_sprawy": "Pod datą 10 marca 1698 r. (Feria Secunda ante Festum S. Gregorii) ławnik przysięgły Wojciech Bożkowic kwituje Jakuba Lisa ze spłacenia 20 złp z dekretu; poniżej protestacja i obdukcja ran przedmieszczanina Jana Smoka przeciw Bartłomiejowi Wilkowi, jego synowi Janowi i parobkowi Tomaszowi Wójcikowi o pobicie na grobli (stłuczona lewa ręka, rany nad łokciem i na prawej łopatce).",
        "transkrypcja": """113.
Actum Coram Judicio Advocatiali et Scabinali Jurato Crasnicensi Feria Secunda ante Festum Sancti Gregorii proxima Anno 1698 [10 III 1698].
Do Urzędu y Akt niniejszych oblicznie przyszedłszy Sławetny Pan Wojciech Bożkowic mieszczanin Ławnik przysięgły Kraśnicki zeznał przed tym Urzędem dobrowolnie iż według dekretu w Acta eodem ferowanego w zapłaceniu fl 20 zadość mu się stało y nie ma iuż więcey pozwanego to iest Jakuba Lisa nie trudnić y pole które w długu Sławetny P. Bożkowic trzymał ponieważ iuż uspokojony przed... więcey interessować się niema na co dla lepszej wiary wagi iako do siebie nic nie mają to przed Sądem niniejszym zeznali y prosili aby to zapisano było. Quod est connotatum.

Sub Eodem Actu.
Uciwy Jan Smok przedmieszczanin Kraśnicki przyszedłszy do Sądu niniejszego protestował się na przeciw Bartłomiejowi Wilkowi który z żoną y synem Janem y onegoż nieumieiące uśmierzyć parobku na imię Tomasz Wójcik z miasta także z parobkiem y synami niewiedziedząc żadnej okazyi na grobli zastąpiwszy pobili. In cuius protestationis verificationem obduxit na lewej ręce od młodzieży piszczeli ręka tłuczona do pięści sina na łokciu na ręce się nie może nic... Item nad łokciem na prawey ręce raz nad łokciem spuchły siny wszerz y wzdłuż nadto na plecach na prawey łopatce wzdłuż y wszerz siny spuchły. W czym wszystkim dają winę tak ojcu wyżej specyfikowanemu iak synom tego bicia w którym o co iterum idem protestans protestuje się ofiaruje się z nimi prawnie tego dochodzić. Quod connotatum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 227,
        "numer_pozycji": "227",
        "strona_pagina": "fol. 113v (113v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Sprawa Rabaka z Kaczorkowicem i ugoda Majowskiego z Mrozowskim (14 III 1698)",
        "osoby_podmioty": "Jan Majowski, Karol Mrozowski, Józef Rabak [?], Grzegorz Kaczorkowic, Józef Tulcuk [?], Andrzej Łękowski [?], Jan Smok",
        "kwoty_podatki": "4 grzywny",
        "opis_sprawy": "Pod datą 12 marca 1698 r. (Feria Quarta post Dominicam Laetare): dylacja w sprawie Jana Majowskiego przeciw Karolowi Mrozowskiemu; wyrok 4 grzywien dla Grzegorza Kaczorkowica w sprawie z Józefem Rabakiem [?]; diligentia Józefa Tulcuka [?] i Andrzeja Łękowskiego [?]; poniżej pod datą 14 marca 1698 r. (Feria Sexta post Festum S. Gregorii) ugoda Jana Majowskiego z Karolem Mrozowskim za mediacją sądu.",
        "transkrypcja": """113v.
Actum Coram Judicio Advocatiali et Scabinali Feria Quarta post Dominicam Laetare Anno 1698 [12 III 1698].
Inter Famatum Joannem Majowski Actorem et Famatum Carolum Mrozowski datur dilatio sub termino peremptorio...
Sub eodem Actu.
Na dzisieyszym terminie toczący się sprawa między Józefem Rabakiem [?] Aktorem a Grzegorzem Kaczorkowicem pozwanym wnosi Aktor skargę iż po tak wielu sobie danych pozwach do sądu nie stawa za co z tym czasem na nim kondemnatę prosił a więc aby winy na znaczenie wypetnił. Sąd niniejszy na niego y nakazuie aby Grzegorz Kaczorkowic dał grzywien cztery parti et Judicio per medium.
Diligentia Honestorum Josephi Tulcuk [?] et Andreae Łękowski [?] że gotowi byli za pierwszym terminem do sądu ze skargą Aktora...

Actum Feria Sexta post Festum Scti Gregorii proxima 1698 [14 III 1698].
W sprawie między Sławetnym P. Janem Majowskim Aktorem a Sławetnym P. Karolem Mrozowskim pozwanym ponieważ pozwany nie chciał dopuścić względem małej racji przez niego Aktorowi publice zadaney do sądu... aby sami byli mediatorami co słusznie effecerunt y do zgody ich przyprowadzili żeby jednak zaszłych...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 228,
        "numer_pozycji": "228",
        "strona_pagina": "fol. 114r (114 / 110)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Kwitacja Wojciecha Grzymałowskiego i Teresy Janaszkowicowej dla Nowackich z sukcesji po wójcie (16 VI 1699)",
        "osoby_podmioty": "Jan Onufry Kieniewicz [Onupkiewicz?], Adam Potokowicz [Potocki], Jan Barankowicz, Jan Majowski, Stefan Kwasowic, Stanisław Solecki, Wawrzyniec Bielaszkowic, Wojciech Grzymałowski, Teresa Janaszkowicowa [Grzymałowska], Ubald Janaszkowicz (zm.), Marianna Janaszkowicowa (zm.), Wojciech Nowacki, Katarzyna Janaszkowicowa [Nowacka]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Pod datą 16 czerwca 1699 r. (Feria Tertia post Festum SS. Trinitatis) przed Sądem Złożonym Kraśnickim (Jan Onupkiewicz wójt, Adam Potokowicz prokonsul, Jan Barankowicz, Jan Majowski, Stefan Kwasowic, Stanisław Solecki rajcowie, Wawrzyniec Bielaszkowic ławnik): Wojciech Grzymałowski ławnik kraśnicki i deputat Trybunału Zamojskiego oraz jego żona Teresa Janaszkowicowa (córka zmarłego wójta Ubalda Janaszkowicza i Marianny) kwitują Wojciecha Nowackiego landwójta urzędowskiego i Katarzynę Janaszkowicową (siostrę rodzoną Teresy) ze spisanego inwentarza dóbr ruchomych i nieruchomych po rodzicach.",
        "transkrypcja": """114. [1699 | u dołu: 110.]
Actum Coram Officio Composito Crasnicensi Praesentibus Famatis ac Honorato Joanne Onupkiewicz [Kieniewicz?] Advocato, Adamo Potokowicz Proconsule, Joanne Barankowicz, Joanne Majowski, Stephano Kwasowic, Stanislao Solecki Consulibus, Laurentio Bielaszkowic Scabino Feria Tertia post Festum Sanctissimae Trinitatis proxima Anno Domini Millesimo Sexcentesimo Nonagesimo Nono [16 VI 1699].
Przed tymże Urzędem Oboynym Kraśnickim w osobach swoich stanąwszy Sławetni Wojciech Grzymałowski Ławnik tegoż Miasta Kraśnika y Deputat Sądów Naywyższych Trybunału Miast Państwa Zamoyskiego y Teresa Janaszkowicowa de gente niegdy Sławetnego Ubaldego Janaszkowica Wójta Ordynaryjnego Kraśnickiego y Maryanny małżonków spłodzona córka małżonkowie zdrowi na umysłach y ciałach swoich będący jaśnie jawnie dobrowolnie żadnym błędem nie skrypti zeznali praesentibus rebus iż oni Sławetnych Wojciecha Nowackiego Landwójta Urzędowskiego y Katarzynę Janaszkowicową siostrę rodzoną wyżej wymienioney małżonki oboje małżonków y ich następców od spisania Inwentarza dóbr generaliter wszystkich ruchomych y nieruchomych po niegdy pomienionych...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 229,
        "numer_pozycji": "229",
        "strona_pagina": "fol. 114v (114v)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Dokończenie kwitacji Grzymałowskich dla Nowackich — spłata 500 złp długów po wójcie Janaszkowiczu",
        "osoby_podmioty": "Wojciech Grzymałowski, Teresa Janaszkowicowa [Grzymałowska], Wojciech Nowacki, Katarzyna Janaszkowicowa [Nowacka]",
        "kwoty_podatki": "500 złp",
        "opis_sprawy": "Dokończenie aktu z 16 VI 1699 r.: Grzymałowscy aprobują spisany inwentarz bez przysięgi, zrzekają się dalszych roszczeń w urzędach kraśnickich i przed Trybunałem Zamojskim, poświadczając jednocześnie, że z inwentarza po zapłaceniu długów prawie nic nie zostało, a małżonkowie Nowaccy wydali z własnych pieniędzy pięćset złotych polskich (500 złp) na zaspokojenie wierzycieli.",
        "transkrypcja": """114v.
zmarłych Rodzicach swoich tak oyczystych iako y macierzystych wolnych czynią y spisany Inwentarz wolą wyraźną swoią approbuią comprobacyi iuramentem nie requiruią ani sobie sukcesyey partycypowania pro sorte sua przypadającey nie uzurpuią. Ani sukcessorom swoim nie zostawuią z domu narożnego którego dotąd possessorem... a widzimy realitatem spisanego Inwentarza z którey evidenter patet że więcej długów zapłaconych nayduie się aniżeli substancyi massa dobrowolnie zostaje gdzie pomienieni Sławetni Panowie Nowaccy małżonkowie de proprio peculio summę Pięćset złotych polskich wydali przyznali których od impetycyi creditorum przeszłych prawnych nieprawnych gdyż się po zaspokojeniu tych którzy się zmieścić mogli iure nie trzymają teraz nie mogą trwać y zaste powadę declaruią... na wieczne czasy robur.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 230,
        "numer_pozycji": "230",
        "strona_pagina": "fol. 115r (115)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Zapis placu zatylnego w Rynku przez starego rajcę Macieja Bielaszkowica (19 VI 1699)",
        "osoby_podmioty": "Jan Onufry Kieniewicz [Onupkiewicz?], Adam Potokowicz [Potocki], Jan Majowski, Stanisław Solecki, Paweł Słomkowski, Wojciech Grzymałowski, Wawrzyniec Bielaszkowic, Maciej Bielaszkowic [Błaszkowicz], Jan Kinny [?], Regina",
        "kwoty_podatki": "grzywny królewskie i długi",
        "opis_sprawy": "Pod datą 19 czerwca 1699 r. (Feria Sexta post Festum SS. Trinitatis) przed Sądem Złożonym (Jan Onupkiewicz wójt, Adam Potokowicz prokonsul, Jan Majowski, Stanisław Solecki rajcowie, Paweł Słomkowski wicewójt, Wojciech Grzymałowski, Wawrzyniec Bielaszkowic ławnicy): Maciej Bielaszkowic stary rajca kraśnicki zapisuje swój plac zatylny w Rynku wraz z budynkiem i z prawem wolnego przejazdu do ulicy Sławetnemu Janowi Kinnemu [?] i Reginie małżonkom obywatelom kraśnickim na zaspokojenie długów.",
        "transkrypcja": """115.
Actum Coram Officio Composito Crasnicensi Feria Sexta post Festum Sanctissimi et Individuae Trinitatis proxima Anno Dni 1699 [19 VI 1699]. Praesentibus Joanne Onupkiewicz Advocato, Adamo Potokowicz Proconsule, Joanne Majowski, Stanislao Solecki Consulibus, Paulo Słomkowski Viceadvocato, Alberto Grzymałowski, Laurentio Bielaszkowic Scabinis Juratis.
Przed Urzędem y Aktami ninieyszemi Wójtowskiemi y Ławniczemi Kraśnickiemi w osobie swojey stanąwszy Sławetny Maciej Bielaszkowic Radca stary Kraśnicki y obywatel mieszczanin zdrowy na umyśle y ciele będąc publice jaśnie jawnie dobrowolnie żadnym błędem nie uwiedziony zeznał iż plac zatylny... przy budynku moim... wydzieliwszy na pełne widzenie y ustępowanie siebie Sławetnym Janowi Kinnemu [?] i Reginie obywatelom Kraśnickim y sobie małżonkom y ich sukcessorom własnym wolno nie zawiedzioną ani zadłużoną... ażeby na osobliwe inne dobra w possessyi... bez turbacyi y przykładania się z... wydzieloney...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 231,
        "numer_pozycji": "231",
        "strona_pagina": "fol. 115v (115v — uszkodzona)",
        "sygnatura": SYGN,
        "data_rok": "1697",
        "kategoria": "Intromisja w ćwierć roli Augustynowskiej z 1697 r. (fragment górny karty)",
        "osoby_podmioty": "Adam Potokowicz [Potocki], Wojciech Grzymałowski, Wawrzyniec Bielaszkowic, Adam Michał Chmielowicz (pisarz), Tomasz Anczarek [?], Jan Sikorczyk [?], Stanisław Bakałowski, Jan Karapek [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Karta uszkodzona (dolna połowa odcięta/brakująca), na zachowanej górnej części wpis z roku 1697 (Feria Secunda post Festum S. Martini, 18 XI 1697) w obecności Adama Potokowicza, Wojciecha Grzymałowskiego, Wawrzyńca Bielaszkowica, pisarza Adama Michała Chmielowica oraz mieszczan Tomasza Anczarka [?], Jana Sikorczyka [?], Stanisława Bakałowskiego i Jana Karapka [?] — intromisja w ćwierć roli zwanej Augustynowską z ogrodem i łąką.",
        "transkrypcja": """115v.
Actum Coram Officio praesentibus Famatis Adamo Potokowicz, Alberto Grzymałowski, Laurentio Bielaszkowic, Adamo Michaele Chmielowicz Notario et aliis... Thomam Anczarek [?], Joannem Sikorczyk [?], Stanislaum Bakałowski, Jan... Karapek [?]... Feria Secunda post Festum Sancti Martini proxima Anno Dni 1697 [18 XI 1697].
W dobra videlicet ćwierć Augustynowską nazwaną z ogrodem y łąką et aliis pertinentiis observata solemnitate Intromissionis nemine impugnante.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 232,
        "numer_pozycji": "232",
        "strona_pagina": "fol. 116r (116 / 112)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Kontumacje czynszowe na rzecz Konwentu Kanoników Regularnych (Majowski, Bielaszkowic, Solecki)",
        "osoby_podmioty": "Jan Onufry Kieniewicz [Onupkiewicz?], Adam Potokowicz [Potocki], Jan Barankowicz, Paweł Słomkowski, Stanisław Jesurkiewicz, przeor ks. Paweł [?], Jan Majowski, Szymon Rosiński (zm.), Maciej Bielaszkowic [Błaszkowicz], Stanisław Solecki",
        "kwoty_podatki": "100 złp; 50 złp; 10 złp; 500 złp (kapitały); 4 grzywny; 2 grzywny",
        "opis_sprawy": "Pod datą 18 września 1699 r. (Feria Sexta post Festum Exaltationis S. Crucis) przed Sądem Złożonym (Jan Onupkiewicz wójt, Adam Potokowicz, Jan Barankowicz rajcowie, Paweł Słomkowski wicewójt, Stanisław Jesurkiewicz stary rajca): kontumacje z instancji przeora ks. Pawła [?] i konwentu kanoników regularnych kraśnickich o zaległe czynsze wyderkafowe: rajca Jan Majowski (od 100 złp z dóbr Popielów za 8 lat, 50 złp po zmarłym Szymonie Rosińskim i 10 złp z dóbr Gabryszowskich — kara 4 grzywny), Maciej Bielaszkowic (od 500 złp za 4 lata — 2 grzywny) oraz rajca Stanisław Solecki.",
        "transkrypcja": """116. [1699 | u dołu: 112.]
Actum Coram Officio Composito Crasnicensi Feria Sexta post Festum Exaltationis Sanctae Crucis proxima praesentibus Famatis Joanne Onupkiewicz Advocato, Adamo Potokowicz, Joanne Barankowicz Consulibus, Paulo Słomkowski Viceadvocato, Stanislao Jesurkiewicz Consule antiquo Anno Domini Millesimo Sexcentesimo Nonagesimo Nono [18 IX 1699].

Famatus Joannes Majowski Consul Crasnicensis ex Instantia Admodum Reverendi Venerabilis Patris Pauli... Prioris Ecclesiae Crasnicensis et totius Conventus Canonicorum Regularium... ratione census a summa principali centum florenorum polonicalium in bonis Popielowskie assecuratorum retenti... pro annis octo retenti... atque florenorum quinquaginta florenorum polonicalium pro funere olim Simonis Rosiński debitorum atque florenorum decem ex bonis Gabryszowskie contumax. In cuius contumaciam decernitur lucrum solutionis Marcarum quatuor...

Famatus Mathias Bielaszkowic pro annis quatuor ad summa quingentorum florenorum polonicalium a ultima quietatione solutionis contumax. In cuius contumaciam decernitur lucrum solutionis census retenti iuxta poena duarum Marcarum parti et Officio per medium.

Famatus Stanislaus Solecki Consul similiter ratione non solutionis census ab ultima quietatione...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 233,
        "numer_pozycji": "233",
        "strona_pagina": "fol. 116v (116v)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Kontumacja Adama Karola Mrozowskiego (14 grzywien) oraz spory o tatarkę (Kowalik vs Zając, Słomkowski vs Bielaszkowic)",
        "osoby_podmioty": "Stanisław Solecki, Adam Karol Mrozowski, Stanisław Jesurkiewicz, Józef Macal, Sebastian Kowalik, Jakub Zając [Zajączek?], Paweł Słomkowski, Augustyn Bielaszkowic",
        "kwoty_podatki": "4 grzywny; 200 złp (kapitał); 14 grzywien",
        "opis_sprawy": "Dokończenie kontumacji Stanisława Soleckiego (4 grzywny); kontumacja mieszczanina Adama Karola Mrozowskiego o zaległy czynsz od 200 złp za 5 lat (kara 14 grzywien za lekceważenie sądu); odesłanie sprawy dawnego rajcy Stanisława Jesurkiewicza przeciw Józefowi Macalowi do oktawy; pierwsza kontumacja Jakuba Zająca [?] z instancji Sebastiana Kowalika o zabranie tatarki; sprawa podwojciego Pawła Słomkowskiego przeciw Augustynowi Bielaszkowicowi o zabranie tatarki.",
        "transkrypcja": """116v.
contumax decernitur lucrum solutionis census iuxta poena Marcarum quatuor.

Honestus Adamus Carolus Mrozowski Civis Crasnicensis ratione non solutionis a summa principali ducentorum florenorum polonicalium ab ultima quietatione pro annis quinque contumax, ex cuius contumacia ratione postpositionis Officii et elusionis Actorum... decernitur poena Marcarum quatuordecim parti et Officio per medium solvenda.

Między Sławetnym Panem Stanisławem Jesurkiewiczem Radcą dawnym Kraśnickim Aktorem a Uciwym Józefem Macalem Mieszczaninem pozwanym ob non plenam sessionem odsyła się ad octavam, conservando partibus terminum peremptorium.

Ex Instantia H. Sebastiani Kowalik Actoris H. Jacobus Zajączek [Zając?] contumax primo względem zabrania tatarki wespół sianey na roli Aktora...

W sprawie y Akcyey między Sławetnym Panem Pawłem Słomkowskim Podwójcim Kraśnickim Aktorem z iedney a Uciwym Augustynem Bielaszkowicem pozwanym o zabranie tatarki sianey na gruncie Aktora iż mu z gruntu zoranego wykopanego... zasianey tatarki wniósł aby ukarany...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 234,
        "numer_pozycji": "234",
        "strona_pagina": "fol. 117r (117 / 113)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Zeznania Pawła Mazurka i Józefa Kudbałki o kopaniu stawu Augustyna Bielaszkowica (18 IX 1699)",
        "osoby_podmioty": "Augustyn Bielaszkowic, Paweł Słomkowski, Paweł Mazurek, Józef Kudbałka [?], Jan Brodecki [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Obrona Augustyna Bielaszkowica w sprawie o kopanie i sianie tatarki przy gruncie Pawła Słomkowskiego (sąd zarządza inkwizycję i wizję granic); poniżej pod datą 18 września 1699 r. (Feria Sexta ante Festum S. Mathei) zeznania świadków: 1. Paweł Mazurek i 2. Józef Kudbałka [?] zeznają, jak w 1699 r. i przed laty kopali staw przy stawie P. Słomkowskiego z Augustynem Bielaszkowicem i Janem Brodeckim [?].",
        "transkrypcja": """117. [u dołu: 113.]
Pozwany odpowiedział że od lat pięciu... na tym gruncie y wykopał y na brzeg nakładł... podług gruntu Sławetnego Pana Aktora... Haec inter negantem et affirmantem vertitur causa necessaria expiscatio finis controversiae una cum inquisitione per partes expedienda.

Actum Feria Sexta ante Festum Sancti Mathei Apostoli Anno 1699 [18 IX 1699].
Testimonium ex Parte Pauli Słomkowski:
1mus Testis. Uciwy Paweł Mazurek tacto pectore zeznał iż za dwa dni brat nasz... u chłopa co u Pana Słomkowskiego był... tego roku tych kopaliśmy... staw z Augustynem Bielaszkowicem.
2dus Testis. Józef Kudbałka [?] tacto pectore zeznał iż dokładnie z każdym też kiedy kopał podle tego stawka u P. Słomkowskiego... z Augustynem Bielaszkowicem kopałem z Janem Brodeckim [?] też to sam o ten staw kopałem.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 235,
        "numer_pozycji": "235",
        "strona_pagina": "fol. 117v (117v)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Spór Agnieszki Guckiej z Bartoszem Wilkiem o 5 złp oraz Kowalika z Zajączkiem o tatarkę",
        "osoby_podmioty": "Paweł Słomkowski, Augustyn Bielaszkowic, Agnieszka Gucka, Bartosz Wilk, Michał Szymczak [?], Sebastian Kowalik, Jakub Zajączek [Zając?]",
        "kwoty_podatki": "5 złp; półtora korca zboża",
        "opis_sprawy": "Dokończenie zeznań o kopaniu stawu z 1699 r. i dekret na wizję granic; sprawa Agnieszki Guckiej przeciw Bartoszowi Wilkowi o pożyczone 5 złp i półtora korca zboża (wymieniony brat Michał Szymczak [?], dylacja do środy); na dole sprawa Sebastiana Kowalika przeciw Jakubowi Zajączkowi [?] o zabranie tatarki.",
        "transkrypcja": """117v.
u P. Słomkowskiego... w roku 1699...
3tius Testis [z lewej: P. Słomkowskiego]. Tacto pectore zeznał iż za dwa dni... z Mazurkiem iuż temu lat circiter... staw w pełne palenowe... do kopania tego stawu.
Po wywiedzeniu Inkwizycyey Judicium Relacyą na wizyą adinvenit.

W sprawie między Sławetną P. Agnieszką Gucką Aktorką a Uciwym Bartoszem Wilkiem pozwanym o dług pożyczony złotych pięciu, sąd dał dylacyi do środy blisko przyszłej... gdyż P. Gucka świadków przy których to dawała... Bartoszowi Wilkowi y przedtem... za sumę u P. Guckiej ma na ten czas dług za półtora korca zboża które może Michał Szymczak [?] za które pięć złotych zabierając Aktor... Zająć...

W sprawie między Uciwym Sebastianem Kowalikiem Aktorem a Uciwym Jakubem Zajączkiem pozwanym względem zabrania...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 236,
        "numer_pozycji": "236",
        "strona_pagina": "fol. 118r (118 / 114)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Spór Kowalika z Zajączkiem o 80 snopów tatarki i zeznanie Marianny Piotrowczykowej (23 IX 1699)",
        "osoby_podmioty": "Sebastian Kowalik, Jakub Zajączek [Zając?], Jakub Raganek, Sebastian Diracek [Dziadek?], Marianna Piotrowczykowa",
        "kwoty_podatki": "1 kopa i 40 snopów tatarki (lub 20 snopów)",
        "opis_sprawy": "Dokończenie skargi Sebastiana Kowalika przeciw Jakubowi Zajączkowi o samowolne zabranie kopy i 40 snopów tatarki z roli (sąd nakazuje zwrot na środę); poniżej pod datą 23 września 1699 r. (Feria Quarta post Festum S. Mathiae) zeznanie Marianny Piotrowczykowej ze strony przedmieszczanina Jakuba Raganka przeciw Sebastianowi Dirackowi [Dziadkowi?] o szkodę w życie i rozmowę z Michałowicową.",
        "transkrypcja": """118. [u dołu: 114.]
sianey sobie tatarki... Aktor skarży iż nie swoią tatarkę tylko... sobie... tak swawolnie postąpił pozwany tatarkę zabrał gdzie Aktor powiada że miał... kopę y snopów 40... aby teraz w snopów... na środę blisko przyszłą...

Actum Feria Quarta post Festum Scti Mathiae Evangelistae Anno 1699 [23 IX 1699].
Testimonium ex Parte Jacobi Raganek Suburbani Crasnicensis Contra Sebastianum Diracek [Dziadek?].
Uciwa Marianna Piotrowczykowa przypozwana od Uciwego Jakuba Raganka względem wiedzenia iako Sebastian Diracek [Dziadek?] szkodował jego pod sumieniem zeznała w te słowa: Przed nowem przyszedł do mnie Diracek mówiąc mi: Moia Michałowa potwarza mię siostra, iakobym iey skrzywdzić miał żyta, iam do niego rzekła ieśliś skrzywdził to choć nie teraz to wrócić potrzeba, rzekł mi gdzie ona tu u was powiedziała żem ia u was kupił a ia znowego nagrodzę. Gdy po tym przyszła raganowa y pytała się o żona powiedziała kupci swoiście swoi nagrodzicie sobie. Dnia wczorajszego przyszedł do mnie proszący abym go poratowała na kim słowie, przed Sądem więcey niewiedząc się powiedziała. Quod connotatum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 237,
        "numer_pozycji": "237",
        "strona_pagina": "fol. 118v (118v)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Sesja 25 IX 1699 r.: Jesurkiewicz vs Macal (60 złp), Grzymałowski vs Żmienda, Kowalik vs Zajączek",
        "osoby_podmioty": "Stanisław Jesurkiewicz, Józef Macal, Wojciech Grzymałowski, Jan Żmienda, Sebastian Kowalik, Jakub Zajączek [Zając?]",
        "kwoty_podatki": "60 złp; 7 grzywien",
        "opis_sprawy": "Pod datą 25 września 1699 r. (Feria Sexta post Festum S. Mathei): sprawa dawnego rajcy Stanisława Jesurkiewicza przeciw Józefowi Macalowi o niezapłacony dług 60 złp po rodzicach i ogród (kara 7 grzywien); sprawa ławnika Wojciecha Grzymałowskiego przeciw Janowi Żmiendze o zabranie siana (dylacja na inkwizycję); początek wyroku w sprawie Sebastiana Kowalika przeciw Jakubowi Zajączkowi.",
        "transkrypcja": """118v.
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Sexta post Festum Sancti Mathei Apostoli proxima Anno Domini Millesimo Sexcentesimo Nonagesimo Nono [25 IX 1699].
W sprawie y Akcyey między Sławetnym Panem Stanisławem Jesurkiewiczem Radcą dawnym Kraśnickim Aktorem z iedney swoiey y małżonki swey imieniem, a Uciwym Józefem Macalem z strony niezapłacenia długu niegdy rodzica Aktora zapisanego, dotąd niezapłaconego y z dóbr jego nie rekuperowanego... zapisany dług złotych sześćdziesiąt [60 złp]... pod winą grzywien siedmiu parti et Officio per medium... et terminus conservatur partibus.

W sprawie y Akcyey między Sławetnym Panem Wojciechem Grzymałowskim Aktorem a Uciwym Janem Żmiendą pozwanym aby pozwany siana zabrać oddał in instanti Aktorowi... datur dilatio Inquisitionis.

W sprawie y Akcyey między Uciwym Sebastianem Kowalikiem Aktorem z iedney a Jakubem Zajączkiem, ponieważ pozwany Jakub Zajączek dosyć dekretowi nie uczynił...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 238,
        "numer_pozycji": "238",
        "strona_pagina": "fol. 119r (119 / 115)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Wyrok w sprawie tatarki (Kowalik vs Zajączek) i 2. kontumacje Mendalki oraz Augustyna Bielaszkowica",
        "osoby_podmioty": "Sebastian Kowalik, Jakub Zajączek [Zając?], Piotr Tokarczyk, Bartłomiej Mendalka [?], Paweł Słomkowski, Augustyn Bielaszkowic",
        "kwoty_podatki": "2 grzywny",
        "opis_sprawy": "Dokończenie wyroku w sprawie Sebastiana Kowalika przeciw Jakubowi Zajączkowi (przysięga o 20 snopów tatarki); 2. kontumacja Bartłomieja Mendalki [?] z instancji przedmieszczanina Piotra Tokarczyka (kara 2 grzywien); 2. kontumacja Augustyna Bielaszkowica z instancji podwojciego Pawła Słomkowskiego (kara 2 grzywien); na dole nagłówek sesji z 5 października 1699 r. (Feria Secunda post Festum S. Michaelis Archangeli).",
        "transkrypcja": """119. [u dołu: 115.]
nie wyniosło wiele tatarki na roli Aktora... zastrzeżony Aktorowi przysięga... że więcey nad 20 snopów nie zabrali. Terminus conservatur.

Ex Instantia Honesti Petri Tokarczyk Suburbani Crasnicensis H. Bartholomeus Mendalka [?] 2do contumax ratione po użyczonym słownym kontrakcie... in cuius contumaciam decernitur lucrum abiudicationis... luita poena Marcarum duarum una cum litis expensis.

Ex Instantia Famati Pauli Słomkowski Viceadvocati Crasnicensis H. Augustinus Bielaszkowic ratione zabrania tatarki z gruntu orania Aktora contumax 2do... luita poena duarum Marcarum una cum litis expensis.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Secunda post Festum Sancti Michaelis Archangeli proxima Anno Domini Millesimo Sexcentesimo Nonagesimo Nono [5 X 1699].""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 239,
        "numer_pozycji": "239",
        "strona_pagina": "fol. 119v (119v)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Sesja 5 X 1699 r.: Skarz vs Mutkowic, Tokarczyk vs Mendalka, Grzymałowski vs Witkowski, Majowski vs Biegajczyk",
        "osoby_podmioty": "Matyjasz Skarz [Skarzyk?], Szymon Mutkowic [?], Piotr Tokarczyk, Bartłomiej Mendalka [?], Kowalik, Jakub Zajączek [Zając?], Wojciech Grzymałowski, Andrzej Witkowski [?], Jan Majowski, Matyjasz Jurecki [?], Biegajczyk, Józef Rabak [?], Tomasz Kopeć [Kopień?]",
        "kwoty_podatki": "1 grzywna",
        "opis_sprawy": "Wpis spraw z sesji sądowej: Matyjasz Skarzyk [Skarz] przeciw Szymonowi Mutkowicowi [?] (dylacja); Piotr Tokarczyk przeciw Bartłomiejowi Mendalce [?] (kara 1 grzywny); Kowalik przeciw Jakubowi Zajączkowi o kalumnię; Wojciech Grzymałowski przeciw Andrzejowi Witkowskiemu [?] o kalumnię; rajca Jan Majowski przeciw Matyjaszowi Jureckiemu [?] i Biegajczykowi o gwałty (kontumacja); początek sprawy Józefa Rabaka [?] przeciw Tomaszowi Kopciowi [Kopieniowi?].",
        "transkrypcja": """119v.
W sprawie między Uciwym Matyaszem Skarzykiem [Skarzem?]... a Uciwym Szymonem Mutkowicem [?]... datur dilatio...
Inter H. Petrum Tokarczyk Actorem et H. Bartholomeum Mendalka quatenus Marcam unam Judicio...
Inter HH. Kowalik et H. Jacobum Zajączek Citt. datur dilatio Inquisitionis ratione calumniae ad feriam quartam proxime venturam.
W sprawie y Akcyey między Sławetnym Panem Wojciechem Grzymałowskim Aktorem a Andrzejem Witkowskim [?] ratione calumniae... datur dilatio Inquisitionis.
Inter Famatum Joannem Majowski Consulem Actorem et HH. Mathiam Jurecki [?]... ratione violentiarum et H. Biegajczyk... Biegajczyk contumax...
W sprawie między Uciwym Józefem Rabakiem z iedney a Tomaszem Kopciem [Kopieniem?] z drugiey...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 240,
        "numer_pozycji": "240",
        "strona_pagina": "fol. 120r (120 / 116)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Zeznanie Agnieszki Kondupkowej, kontumacje i protestacja wicecechmistrza tkackiego Jana Dumańskiego (30 IX 1699)",
        "osoby_podmioty": "Józef Rabak [?], Agnieszka Kondupkowa [?], Jan Kondupek [?], Tomasz Kopeć [Kopień?], Jan Majowski, Jakub Kłopot, Paweł Słomkowski, Augustyn Bielaszkowic, Jan Dumański (wicecechmistrz tkacki), Tomasz Celej",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie sprawy Rabaka z Kopciem i zeznanie Agnieszki żony Jana Kondupka [?] z instancji Józefa Rabaka; 1. kontumacja Jakuba Kłopota z instancji rajcy Jana Majowskiego; 2. kontumacja Augustyna Bielaszkowica z instancji Pawła Słomkowskiego; poniżej pod datą 30 września 1699 r. (Feria Secunda in Crastino Festi S. Michaelis) protestacja przedmieszczanina Jana Dumańskiego, wicecechmistrza cechu tkackiego kraśnickiego, przeciw Tomaszowi Celejowi.",
        "transkrypcja": """120. [u dołu: 116.]
strony pozwanej... Sądowego... datur dilatio...
Ex Instantia H. Josephi Rabak H. Agnes Joannis Kondupek [?] consors legitima adcitata na Instantią Uciwego Józefa Rabaka... przez Uciwego Tomasza Kopcia [Kopienia?] przedmieszczanina Kraśnickiego...

Ex Instantia Famati Joannis Majowski Consulis Crasnicensis H. Jacobus Kłopot ratione... contumax primo.
Ex Instantia Famati Pauli Słomkowski Viceadvocati H. Augustinus Bielaszkowic contumax 2do... approbatur processus.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Secunda in Crastino Festi Sancti Michaelis Archangeli proxima Ao 1699 [30 IX 1699].
Do Urzędu y Akt ninieyszych Wójtowskich y Ławniczych Kraśnickich w osobie swojey przyszedłszy Uciwy Jan Dumański Przedmieszczanin Vicecechmistrz Cechu Tkackiego Kraśnickiego solennie z wielkim żalem protestował przeciwko Uciwemu Tomaszowi...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 241,
        "numer_pozycji": "241",
        "strona_pagina": "fol. 120v (120v)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Dokończenie protestacji wicecechmistrza Dumańskiego przeciw Celejowi oraz zeznania Szarpy i Piotrowczyka",
        "osoby_podmioty": "Jan Dumański, Tomasz Celej, Jan Szarpa [?], Matyjasz Piotrowczyk, Michał Płóciennik [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie protestacji Jana Dumańskiego przeciw Tomaszowi Celejowi o obrazę słowną i posądzenie o złodziejstwo w gospodzie karczemnej oraz wyprowadzenie świadków: 1. Jan Szarpa [?] (zeznaje, iż Celej mówił na Dumańskiego jako na złodzieja i chciał go wyświecić z miasta) oraz 2. Matyjasz Piotrowczyk przedmieszczanin (o zajściu w domu Michała Płóciennika [?] i groźbach przy bramie).",
        "transkrypcja": """120v.
zalem protestował przeciwko Uciwemu Tomaszowi Celejowi szwagrowi swemu oto iż tenże protestant przyszedłszy bez dania żadney przyczyny w gospodzie karczemnej... y kalumnie przed Urzędem Miasta tegoż zadawał formalibus superius expressis... Et in verificationem praemissorum protestans testes quos in reliquia per... produxit.
1mus Testis. Honestus Joannes Szarpa [?] incola Crasnicensis Causa rei gestae recognovit idque per haec verba: Słyszałem że Tomasz Celej słowa te mówił przeciwko Janowi Dumańskiemu że ty iesteś złodziey wyświecić z Miasta a tam nie iest taki...
2dus Testis. H. Mathias Piotrowczyk przedmieszczanin ex parte et Joannis Dumański recognovit in haec verba: W dzień święta św. Michała w domu Michała Płóciennika [?] słyszałem że Tomasz Celej dał okazją Dumańskiemu... do bramy szli wraz na dwa dni potem Celej a Dumański nie kontentował się z tego...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 242,
        "numer_pozycji": "242",
        "strona_pagina": "fol. 121r (121 / 117)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Obdukcja ran Jana Dumańskiego i reprotestacja Tomasza Celeja",
        "osoby_podmioty": "Jan Dumański, Tomasz Celej, Maciej [dziad], Matyjasz [brat]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie zeznania o wywołaniu na podwórze; obdukcja ran Jana Dumańskiego (krwawa rana na lewej skroni, stłuczenia na ciele); poniżej reprotestacja przedmieszczanina Tomasza Celeja przeciw Janowi Dumańskiemu, który w domu u dziada Macieja i brata Matyjasza miał go bić i targać za nogi w gospodzie.",
        "transkrypcja": """121. [u dołu: 117.]
dał w gębę Dumańskiemu y zabił go... na podwórzu wołał złodzieju...
Et in verificationem praemissorum pokazał rany et quidem raz na skroni lewey a dalej... rany krwawej y siniej...

Do Urzędu y Akt ninieyszych Wójtowskich y Ławniczych Kraśnickich w osobie swojey przyszedłszy Uciwy Tomasz Celej przedmieszczanin Kraśnicki solennie z wielkim żalem reprotestował się przeciwko Uciwemu Janowi Dumańskiemu Przedmieszczaninowi Kraśnickiemu o to iż on z młodości jego poważył się w domu na niego nastąpić protestanta bez dania okazyi bić wziąwszy go za nogi do góry nogami w teyże gospodzie postawił któregoż nie powinien być znieważać... z bratem jego Matyaszem...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 243,
        "numer_pozycji": "243",
        "strona_pagina": "fol. 121v (121v)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Zeznania Wilczka i Jajczyka przeciw ławnikowi Grzymałowskiemu oraz wizja roli Franciszka Dąbrowskiego (30 IX 1699)",
        "osoby_podmioty": "Andrzej Wilczek, Tomasz Jajczyk, Wojciech Grzymałowski, Matyjasz Skarzyk [Skarz], Maciej Krawczyk, Adam Wilk, P. Jabłoński, Paweł Słomkowski, Adam Trzelowicz, Jan Onufry Kieniewicz [Onupkiewicz?], Franciszek Dąbrowski",
        "kwoty_podatki": "-",
        "opis_sprawy": "Pod datą 30 września 1699 r. (Feria Quarta in Crastino Festi S. Michaelis): zeznania świadków Andrzeja Wilczka i Tomasza Jajczyka oraz Macieja Krawczyka w sporze z ławnikiem Wojciechem Grzymałowskim o uderzenie w twarz i kijem koło płotu; poniżej relacja podwojciego Pawła Słomkowskiego i pisarza Adama Trzelowica z ramienia wójta Jana Onufrego Kieniewicza z wizji gruntu i roli przedmieszczanina Franciszka Dąbrowskiego.",
        "transkrypcja": """121v.
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quarta in Crastino Festi Sancti Michaelis Archangeli AD 1699 [30 IX 1699].
Ex Instantia Honesti Andreae Wilczek suburbani Crasnicensis Testis H. Thomas Jajczyk recognovit libere: Byłem w sobotę przy studzienkach... gdy P. Grzymałowski... w tym Andrzej Wilczek przyszedł... P. Grzymałowski... dał temuż Andrzejowi Wilczkowi w gębę...
H. Mathias Krawczyk: Najał mię Adam Wilk... P. Jabłoński... P. Grzymałowski przyszedł także mię pytał... Andrzej Wilczek y rzekł ale cały półtorak brat móy... on odpowiedział y zaraz P. Grzymałowski dał mu w gębę...

Sub Eodem Actu.
My Paweł Słomkowski Podwójci Kraśnicki y Adam Trzelowicz Pisarz Miasta Kraśnika ex brachio Sławetnego Pana Jana Onupkiewicza Wójta Kraśnickiego exequendo munus deputationis suae na Instantią Uciwego Franciszka Dąbrowskiego Przedmieszczanina Kraśnickiego zeszliśmy na grunt pewny scilicet kwaterę roli...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 244,
        "numer_pozycji": "244",
        "strona_pagina": "fol. 122r (122 / 118)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Dokończenie wizji roli Franciszka Dąbrowskiego i zeznanie Szymona Piotrowczyka w sprawie Dumańskiego (2 X 1699)",
        "osoby_podmioty": "Franciszek Dąbrowski, Jan Piwota [?], Matyjasz Skarzyk [Skarz], Michał Piotrowczyk, Tomasz Jajczyk, Szymon Różyc [?], Wojciech Piekarczyk [?], Marina Strużyna [?], Wojciech Piotrowczyk, Sebastian Piotrowczyk, Szymon Piotrowczyk, Jan Dumański, Tomasz Celej",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie wizji roli nabytej przez Franciszka Dąbrowskiego od Jana Piwoty [?] (przy udziale sąsiadów Tomasza Jajczyka, Szymona Różyca [?] i Wojciecha Piekarczyka [?], wzmiankowani Michał, Wojciech i Sebastian Piotrowczykowie oraz Marina Strużyna [?]); poniżej pod datą 2 października 1699 r. (Feria Sexta post Festum S. Michaelis) zeznanie Szymona Piotrowczyka ze strony Jana Dumańskiego przeciw Tomaszowi Celejowi o bójkę i obelgi.",
        "transkrypcja": """122. [u dołu: 118.]
Fruszyńską wedle Instanta kwatery kupnem... od Uciwego Jana Piwoty [?] Przedmieszczanina Kraśnickiego... na zwaney Łąką... kwaterę zoraną przez Uciwego Matyasza Skarzyka będziemy... na tey kwaterze... Dąbrowski... za urazą śp. Uciwego Michała Piotrowczyka przedmieszczanina Kraśnickiego... To hic subinde Uciwy Tomasz Jajczyk, Szymon Różyc [?], Wojciech Piekarczyk [?] sąsiedzi personaliter stanąwszy zeznali iż pamiętają y wiedzą dobrze że ta kwatera... do tey dopiero kiedy Marina Strużyna [?] przedała tey kwatery Dąbrowskiemu... z Wojciechem Piotrowczykiem y Sebastianem Piotrowczykiem...

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Sexta post Festum Sancti Michaelis Archangeli proxima Anno Domini Millesimo Sexcentesimo Nonagesimo Nono [2 X 1699].
H. Szymon Piotrowczyk ex Instantia H. Dumański recognovit będąc na żywym... widziałem że za ten wziął w gębę Tomasza Celeja y podniósł go on go w gębę y zabił...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 245,
        "numer_pozycji": "245",
        "strona_pagina": "fol. 122v (122v)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Wyrok w sporze cechmistrza Dumańskiego z Celejem oraz sprawy Grzymałowskiego, Kowalika i Słomkowskiego",
        "osoby_podmioty": "Matyjasz Piotrowczyk, Jan Dumański, Tomasz Celej, Wojciech Grzymałowski, Andrzej Witkowski [?], Kowalik, Jakub Zajączek [Zając?], Wojciech Słomkowski [Skowroński?], Augustyn Bielaszkowic",
        "kwoty_podatki": "3 dni wieży; 2 grzywny; 14 grzywien (vadium)",
        "opis_sprawy": "Zeznanie 2. świadka Matyjasza Piotrowczyka o bójce i obelgach na Rynku między Dumańskim a Celejem; poniżej wyrok w sprawie wicecechmistrza tkackiego Jana Dumańskiego przeciw Tomaszowi Celejowi — pozwany skazany na 3 dni wieży, przeprosiny oraz 2 grzywny kary (z vadium 14 grzywien na przyszłość); na dole sprawy Wojciecha Grzymałowskiego przeciw Andrzejowi Witkowskiemu [?], Kowalika przeciw Jakubowi Zajączkowi oraz Wojciecha Słomkowskiego [?] przeciw Augustynowi Bielaszkowicowi.",
        "transkrypcja": """122v.
Celej y po tym obadwa się szamotali... na Dumańskiego, nadwórze powiedział...
2dus Testis recognovit H. Mathias Piotrowczyk żartowali z sobą pierwey Dumański z Celejem, sprzeczali się o kitowitow... a potem rozwodziliśmy ich... wyszedłszy Celej na Rynek wołał z Dumańskim z miasta złodzieju...

W sprawie y Akcyey między Uciwym Janem Dumańskim Cechmistrzem młodszym Cechu Tkackiego Aktorem z iedney a Tomaszem Celejem... ponieważ się z Inkwizycyey pokazało iż Aktor... w domu leżąc... mimo to pozwany... uderzył Aktora w gębę y zakrwawił... Sąd skazuie aby dał winy grzywien cztery... na trzy dni w wieży kontynuował deprecatio... pod winą grzywien czternaście...

Sprawa między Sławetnym Panem Wojciechem Grzymałowskim Aktorem a Andrzejem Witkowskim [?]...
H. Kowalik contra Zajączek manifestatur de diligentia.
Sprawa między Sławetnym Panem Wojciechem Słomkowskim [Skowrońskim?] Aktorem a Augustynem Bielaszkowicem względem kopania...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 246,
        "numer_pozycji": "246",
        "strona_pagina": "fol. 123r (123 / 119)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Bójka jarmarczna na św. Franciszka (Maciej Skarzyk vs Grzegorz Wosik z Wilkołaza, 5 X 1699)",
        "osoby_podmioty": "Jakub Kłopot, Jan Majowski, Maciej Skarzyk [Skarz], Grzegorz Michalik alias Wosik [?]",
        "kwoty_podatki": "2 grzywny",
        "opis_sprawy": "Kontumacja Jakuba Kłopota z instancji rajcy Jana Majowskiego (kara 2 grzywien); poniżej pod datą 5 października 1699 r. (Feria Secunda in Crastino Festi S. Francisci) wzajemne protestacje i obdukcje ran z bójki na jarmarku w dzień św. Franciszka: przedmieszczanin Maciej Skarzyk [Skarz] przeciw pracowitemu Grzegorzowi Michalikowi alias Wosikowi [?] ze wsi Wilkołaza (rany na dłoni, głowie i obu rękach) oraz kontraprotestacja Grzegorza Wosika [?] (rana na wierzchu głowy i palcach).",
        "transkrypcja": """123. [u dołu: 119.]
Honestus Jacobus Kłopot względem nie dorównania... Famati Joannis Majowski Actoris tertio contumax. In cuius contumaciam decernitur solutio Marcarum duarum parti et Officio per medium.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Secunda in Crastino Festi Sancti Francisci Confessoris Anno Domini Millesimo Sexcentesimo Nonagesimo Nono [5 X 1699].
Do Urzędu y Akt niniejszych Wójtowskich y Ławniczych Kraśnickich w osobie swojey przyszedłszy Uciwy Maciej Skarzyk [Skarz] Przedmieszczanin Kraśnicki z żalem wielkim solennie protestował się przeciwko Pracowitemu Grzegorzowi Michalikowi alias Wosikowi [?] ze Wsi Wilkołaza o to iż on wczorajszego dnia w dzień święta świętego Franciszka podczas jarmarku tu w Kraśniku... bez dania żadney przyczyny kijem dębowym graniastym... zadał raz na dłoni krwawy na trzy członki wzdłuż... Item na lewej stronie głowy zdrapany krwawy o członku Item na obu rękach tłuczony...

Sub eodem Actu.
Gregorius Wosik [?]... contra personam... obduxit raz na prawey na wierzchu głowy krwawy, raz na palcu... na lewej ręce od łokcia raz spuchły zdrapany krwawy o dwa członki...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 247,
        "numer_pozycji": "247",
        "strona_pagina": "fol. 123v (123v)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Wizja szkody Jakuba Wojcika przeciw Kępie oraz posiedzenie w sprawie najścia na dworzanina Pawłowskiego",
        "osoby_podmioty": "Jakub Wojcik [?], Matyjasz Kępa, Wawrzyniec Bielaszkowic, Adam Michał Chmielowicz, Jan Onufry Kieniewicz [Onupkiewicz?], Adam Potokowicz [Potocki], Jan Majowski, Wojciech Grzymałowski, Michał Pawłowski, Jan Wawrzyniec Chmielowski",
        "kwoty_podatki": "5 gr (szkoda w rzepie)",
        "opis_sprawy": "Pod datą 9 października 1699 r. (Feria Sexta in Crastino Festi S. Francisci proxima): protestacja Jakuba Wojcika [?] przedmieszczanina kraśnickiego przeciw Matyjaszowi Kępie o wyjedzenie żyta i rzepy przez krowy (wizja Wawrzyńca Bielaszkowica i pisarza Adama Michała Chmielowica oszacowała szkodę na 5 groszy); poniżej posiedzenie Sądu Złożonego (Jan Onupkiewicz, Adam Potokowicz, Jan Majowski, Wawrzyniec Bielaszkowic, Wojciech Grzymałowski) w sprawie szl. Michała Pawłowskiego z domu szl. Jana Wawrzyńca Chmielowskiego.",
        "transkrypcja": """123v.
Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Sexta in Crastino Festi Sancti Francisci Confessoris proxima A.D. 1699 [9 X 1699].
Do Urzędu y Akt niniejszych Wójtowskich y Ławniczych Kraśnickich w osobie swojey przyszedłszy Uciwy Jakub Wojcik [?] Przedmieszczanin Kraśnicki solennie protestował się przeciwko Matyaszowi Kępie Przedmieszczaninowi o to iż on sam y z krowami... na pole pomienionego Matyasza Kępy... In cuius protestationis verificationem Wawrzyniec Bielaszkowic y Adam Michał Chmielowic ex Officio deputowani... na pole za sadem swoim groszy 5 w rzepie które nie dozwolone były...

Actum Coram Officio Composito Crasnicensi Praesentibus Famatis Joanne Onupkiewicz Advocato, Adamo Potokowicz in loco Proconsulis constituto, Joanne Majowski Consule, Laurentio Bielaszkowic Scabino iurato. In praesentia Nobilis Alberti Grzymałowski Scabini et Deputati Judicii Supremi... ad Domum Nobilis... in causa Nobilis Michaelis Pawłowski Generosi Domini Laurentii Chmielowski...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 248,
        "numer_pozycji": "248",
        "strona_pagina": "fol. 124r (124 / 120)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Obdukcje ciężkich ran szl. Michała Pawłowskiego i Jana Dumańskiego po tumulcie na jarmarku",
        "osoby_podmioty": "Michał Pawłowski, Jan Wawrzyniec Chmielowski, cyrulik Jakub, Dominik Pawłowski [?], Jan Dumański, Podskarbi / Skarbnik bełski",
        "kwoty_podatki": "-",
        "opis_sprawy": "Obdukcja ciężkich ran szlachetnego Michała Pawłowskiego w rezydencji szl. Jana Wawrzyńca Chmielowskiego sługi JW. Pana Marszałka Wielkiego Koronnego przy cyruliku kraśnickim Jakubie (rany cięte pod łopatką, na prawej skroni, w tyle głowy, na lewej ręce i palcach) podczas tumultu szlachty z porąbaniem drzwi i okien; poniżej obdukcja ran mieszczanina Jana Dumańskiego (rana cięta powyżej łopatki, pod lewą ręką, na trzech palcach) odniesionych przed domem Skarbnika Bełskiego.",
        "transkrypcja": """124. [u dołu: 120.]
Praevendo indemnitati salutis suae non valens Actu praesenti adire Obducit vulnera infrascripta:
Naprzód w Rezydencyey Jegomości Pana Jana Wawrzyńca Chmielowskiego sługi Jaśnie Wielmożnego Jegomości Pana Marszałka Wielkiego Koronnego przy bytności urzędu z cyrulikiem Kraśnickim Jakubem...
Raz pod łopatką na prawey stronie cięty wzdłuż na dwa palce wszerz na trzy palce Item w tyle głowy na lewey stronie raz cięty na członku wzdłuż... Item raz na lewey ręce pod wielkim palcem cięty na pulsach wzdłuż na dwa członki wszerz na jeden członek...
Przy tymże tumulcie pomieniona szlachta okna wycięte drzwi porąbane... contra violentiam Dominika Pawłowskiego [?].

Sub Eodem Actu.
Honestus Joannes Dumański Civis Crasnicensis obduxit: Raz cięty wyżey łopatki pod lewą ręką na trzy członki wzdłuż na trzy palce wszerz... z małym średnim palcem... przed domem P. Skarbnika Bełskiego.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 249,
        "numer_pozycji": "249",
        "strona_pagina": "fol. 124v (124v)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Obdukcja ran Jakuba Świątka oraz pobicia Stanisława Franikowicza ze Stróży przez czeladź Żyda Borucha",
        "osoby_podmioty": "Jakub Świątek, Stanisław Franikowicz [Francyk?] ze Stróży, Żyd Boruch",
        "kwoty_podatki": "-",
        "opis_sprawy": "Obdukcja rany Jakuba Świątka przedmieszczanina kraśnickiego (rana na ramieniu prawej ręki i palcu średnim) odniesionej przed kamienicą Wójta Kraśnickiego; poniżej szczegółowa obdukcja ran pracowitego Stanisława Franikowicza [Francyka?] ze wsi Stróży (de Villa Stróża), napadniętego i pobitego na wolnej drodze przez trzech czeladników Żyda Borucha (dwie rany cięte na głowie, podbite lewe oko, stłuczone obie ręce i palce, podeptany nogami).",
        "transkrypcja": """124v.
Sub Eodem Actu.
H. Jacobus Świątek Suburbanus Crasnicensis obduxit vulnera infrascripta: Raz na ramieniu prawey ręki cały wzdłuż na palcu średnim... które bez dania okazyi otrzymał raz przed Kamienicą Sławetnego Pana Wójta Kraśnickiego.

Sub Eodem Actu.
Laboriosus Stanislaus Franikowicz [Francyk?] de Villa Stróża... idąc na wolnej drodze bez dania żadney przyczyny od trzech czeladzi Żyda Borucha... zadane razy dwie jedna fakturowa druga w rąbek... Item na ręce lewey na łokciu... Item na lewej stronie oko sine spuchłe podbite krwią zaszłe Item na teyże ręce lewey zakrwawionej... na prawey ręce palec od wielkiego... Item pod małym palcem na prawey ręce... oraz nogami deptano.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 250,
        "numer_pozycji": "250",
        "strona_pagina": "fol. 125r (125 / 121)",
        "sygnatura": SYGN,
        "data_rok": "1699",
        "kategoria": "Protestacja dworzanina Wawrzyńca Chmielowskiego o tumult na jarmarku w Kraśniku i śmiertelne pobicie sługi (5 X 1699)",
        "osoby_podmioty": "Jan Onufry Kieniewicz [Onupkiewicz?], Adam Potokowicz [Potocki], Jan Majowski, Wojciech Grzymałowski, Wawrzyniec Bielaszkowic, Wawrzyniec Chmielowski, Anna z Gnińskich Zamoyska (Podskarbina Wielka Koronna), Michał Pawłowski, Dominik Pawłowski [?], Stanisław Węgliński [?] (Skarbnik Bełski)",
        "kwoty_podatki": "-",
        "opis_sprawy": "Pod datą 5 października 1699 r. (Feria Secunda in Crastino Festi S. Francisci) przed Sądem Złożonym Kraśnickim (Jan Onupkiewicz wójt, Adam Potokowicz, Jan Majowski rajcowie, Wojciech Grzymałowski i Wawrzyniec Bielaszkowic ławnicy): uroczysta protestacja szl. Pana Wawrzyńca Chmielowskiego, sługi JW. Marszałka Wielkiego Koronnego i komisarza dóbr klucza kraśnickiego JW. Pani Anny z Gnińskich [?] Zamoyskiej Podskarbiny Wielkiej Koronnej i Ordynatowej Zamoyskiej, o krwawy tumult podczas jarmarku w Kraśniku przeciw PP. Pawłowskim i Stanisławowi Węglińskiemu [?] Skarbnikowi Bełskiemu za śmiertelne pobicie sługi szl. Michała Pawłowskiego, który nie może być nawet przewieziony do grodu lubelskiego.",
        "transkrypcja": """125. [u dołu: 121.]
Actum Coram Officio Composito Crasnicensi tam Advocatiali Scabinali quam Consulari Praesentibus Spectabilibus ac Famatis Joanne Onupkiewicz Advocato Ordinario, Adamo Potokowicz in loco Proconsulis constituto, Joanne Majowski Consule, Alberto Grzymałowski Scabino et Judicii Supremi Civitatum Dominii Zamoscani Deputato, Laurentio Bielaszkowic Scabino Feria Secunda in Crastino Festi Sancti Francisci Confessoris Ao 1699 [5 X 1699].
Do Urzędu y Akt ninieyszych Obojnych Kraśnickich w osobie swojey przyszedłszy Szlachetny Pan Wawrzyniec Chmielowski Jaśnie Wielmożnego Jegomości Pana Marszałka Wielkiego Koronnego sługa y dworzanin dla potrzebniejszego uwagi do dóbr klucza Kraśnickiego dóbr JW. Pani Anny z Gnińskich [?] Zamoyskiej Podskarbiny Wielkiej Koronney Ordynatowej Zamoyskiej... z żalem na Szlachetnego Urodzonego Pana Michała Pawłowskiego sługę swego... bez daney żadney okazyi przy naszym domu w Mieście Kraśniku tumultem podczas Jarmarku przez Panów Pawłowskich y Jegomości Pana Stanisława Węglińskiego [?] Skarbnika Bełskiego... w obductione memorati instantis facti specyfikowanego... na śmierć leżącego y nie jest w stanie do Grodu Lubelskiego zawieziony być...""",
        "link_swa": UNIT_LINK
    }
]

main_data.extend(part10_scans)
with open('/home/ubuntu/workspace/Gen/main_data_j20_part10.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j20_part10.json: {len(main_data)} skanów")
