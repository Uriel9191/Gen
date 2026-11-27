# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j20_part6.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
SYGN = "35/40/0/1/20"

part7_scans = [
    {
        "nr_skanu": 151,
        "numer_pozycji": "151",
        "strona_pagina": "fol. 75r (75)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Protestacje i obdukcja pobicia (Rękuta/Łaziński, Szmul Ichowic)",
        "osoby_podmioty": "Stanisław Rękuta [Pękuta?], Jan Żydek [?], Wojciech Żydek [?], Jan Łaciński [Łaziński?], ławnik Stefan Kwasowic, ławnik Wojciech Grzymałowski, ławnik Wawrzyniec Bielaszkowic, Żyd Szmul Ichowic [?], Andrzej Pełk [?], Jakub Lis, Jakub Młynarczyk [?]",
        "kwoty_podatki": "1 zł na dzień (szkoda)",
        "opis_sprawy": "Protestacja Stanisława Rękuty [Pękuty?] przeciw Janowi i Wojciechowi Żydkom [?] o pobicie na drodze Jana Łacińskiego [Łazińskiego?] oraz obdukcja jego ran (na prawej skroni na półtora członka w głąb i od cięcia na karku) w obecności ławników Stefana Kwasowica, Wojciecha Grzymałowskiego i Wawrzyńca Bielaszkowica; poniżej protestacja Żyda Szmula Ichowica [?] przeciw Andrzejowi Pełkowi [?], Jakubowi Lisowi i Jakubowi Młynarczykowi [?] o krowę i szkodę po złotemu na dzień.",
        "transkrypcja": """75.
Sub eodem Actu.
Protestatio Stanisława Rękuty [Pękuty?] na przeciw Janowi y Wojciechowi Żydkom [?].
Stanąwszy oblicznie przed Urzędem y Aktami niniejszemi Wójtowskiemi Kraśnickiemi Uczciwy Stanisław Rękuta [Pękuta?] Protestował się solennie na przeciw Pracowitym Janowi y Wojciechowi Żydkom [?] o to iż oni bez żadney okazyi na drodze idącego Uczciwego Jana Łacińskiego [Łazińskiego?] napadłszy, onegoż pobili y rany srogie zadali, które to rany przed Urzędem y Ławnikami Przysięgłemi Sławnymi Stefanem Kwasowicem, Wojciechem Grzymałowskim y Wawrzyńcem Bielaszkowicem prezentował: naprzód na prawey skroni rana cięta na półtora członka w głąb, druga od cięcia na karku sinizna y spuchlina wielka, o co iterum atque iterum protestatur.

Sub eodem Actu.
Protestował się Niewierny Szmul Ichowic [?] na przeciw Uczciwemu Andrzejowi Pełkowi [?], Jakubowi Lisowi y Jakubowi Młynarczykowi [?] o to iż oni krowę jego zająwszy y nie oddając szkodę mu po złotemu na dzień czynią, o co protestatur.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 152,
        "numer_pozycji": "152",
        "strona_pagina": "fol. 75v (75v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Obdukcje ran oraz wizja szkody w życie Katarzyny Nowackiej",
        "osoby_podmioty": "Jan Łaziński [Łaciński?], ławnik Stefan Kwasowic, ławnik Wojciech Grzymałowski, ławnik Wawrzyniec Bielaszkowic, Piotr [?], Paweł Stabrawic [?], Katarzyna Nowacka, parobek Stasiek, Paweł Jędrzejowski [?]",
        "kwoty_podatki": "40 snopów żyta (szkoda)",
        "opis_sprawy": "Dokończenie obdukcji ran Jana Łazińskiego [?] oraz obdukcja rany Piotra [?] na łopatce w obecności ławników kraśnickich; poniżej pod datą 30 maja 1698 r. (Feria Sexta in Crastino Festi Corporis Christi) na afektację Pawła Stabrawica [?] wizja szkody w życie Pani Katarzyny Nowackiej, gdzie parobek Stasiek z Pawłem Jędrzejowskim [?] zeznali o 8 wołach i 40 snopach szkody.",
        "transkrypcja": """75v.
Obductio vulnerum Joannis Łaziński [Łaciński?].
Prezentował rany swoje przed Urzędem y Ławnikami Przysięgłemi Sławnymi Stefanem Kwasowicem, Wojciechem Grzymałowskim y Wawrzyńcem Bielaszkowicem Uczciwy Jan Łaziński [?] na prawey stronie y na głowie zadane.
Item prezentował ranę Uczciwy Piotr [?] na łopatce prawym bokiem zadane siną y spuchłą.

Actum Feria Sexta in Crastino Festi Corporis Christi proxima Anno 1698 [30 V 1698].
Na affectatią Uczciwego Pawła Stabrawica [?] zeszli Ławnicy Przysięgli Kraśniccy na wizyą szkody w życie Paniey Katarzyny Nowackiey, gdzie zastawszy ośm wołów w życie y oszacowawszy szkodę na czterdzieści snopów, o czym parobek teyże Paniey Nowackiey Stasiek z Pawłem Jędrzejowskim [?] świadectwo dali y do Akt zapisano.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 153,
        "numer_pozycji": "153",
        "strona_pagina": "fol. 76r (76)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Protestacje o szkodę w łące i obdukcja ran Janczewskiego i Kamińskiego",
        "osoby_podmioty": "Jędrzej Panek, Żyd Feliks [?], Paweł Słomkowski, Michał Janczewski [?], Stanisław Kamiński, woźny Wojciech [?], Jakub Musik [?], Wojciech Grzymek [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Protestacja Jędrzeja Panka przeciw Żydowi Feliksowi [?] o spasioną łąkę/zboże przez krowę (świadomy Paweł Słomkowski) oraz przerwana protestacja Feliksa; pod datą 31 maja 1698 r. (Sabbatho post Festum S. Corporis Christi) obdukcja ran Michała Janczewskiego [?] i Stanisława Kamińskiego (rany na głowie, wzdłuż lewej skroni, dwóch palcach i małym palcu prawej ręki) wraz z relacją woźnego Wojciecha [?] i Jakuba Musika [?].",
        "transkrypcja": """76.
Stanąwszy oblicznie przed Urzędem Uczciwy Jędrzej Panek Protestował się na przeciw Niewiernemu Feliksowi [?] Żydowi Kraśnickiemu o spasioną łąkę y zboże przez krowę jego, czego iest świadom Sławny Paweł Słomkowski.
Niewierny Feliks [?] Protestował się [zapis przerwany].

Actum et Sabbatho post Festum S. Corporis Christi Anno 1698 [31 V 1698].
Prezentowali rany swoje przed Urzędem Uczciwy Michał Janczewski [?] y Stanisław Kamiński, to iest na głowie wzdłuż lewey skroni rana cięta, na dwóch palcach y małym palcu u prawey ręki rany cięte y sine spuchłe. Relacya Woźnego Wojciecha [?] y Jakuba Musika [?], świadczy Wojciech Grzymek [?].""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 154,
        "numer_pozycji": "154",
        "strona_pagina": "fol. 76v (76v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Relacja woźnego o pozwie do Trybunału i spory o szkody polne",
        "osoby_podmioty": "woźny Franciszek Starski [?], Stanisław Solecki, Jan Barankowicz, Wojciech Wardęga, Andrzej Panek, Żyd Feliks [?], ławnik Stefan Kwasowic, ławnik Wawrzyniec Bielaszkowic, Kazimierz Łyszkowic [?], Marcin Paszek [?], P. Kłoskowic [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Relacja woźnego Franciszka Starskiego [?] z oddania pozwu od Stanisława Soleckiego i Jana Barankowicza przeciw Wojciechowi Wardędze do Trybunału; pod datą 2 czerwca 1698 r. (Feria Secunda post Festum SS. Corporis Christi) protestacja Andrzeja Panka przeciw Żydowi Feliksowi [?] o szkodę w życie (przy ławnikach Stefanie Kwasowicu i Wawrzyńcu Bielaszkowicu) oraz sprawa Kazimierza Łyszkowica [?] przeciw Marcinowi Paszkowi [?] o snopy żyta i P. Kłoskowica [?].",
        "transkrypcja": """76v.
Relacya Woźnego Franciszka Starskiego [?] iż oddał pozew od Sławnych Stanisława Soleckiego y Jana Barankowicza na przeciw Pracowitemu Wojciechowi Wardędze na Trybunał.

Actum Feria Secunda post Festum SS. Corporis Christi proxima Anno 1698 [2 VI 1698].
Protestował się Uczciwy Andrzej Panek na przeciw Niewiernemu Feliksowi [?] Żydowi o szkodę w życie uczynioną, którą wizyowali Ławnicy Stefan Kwasowic y Wawrzyniec Bielaszkowic.
W sprawie między Kazimierzem Łyszkowicem [?] Aktorem a Marcinem Paszkiem [?] Pozwanym o snopy żyta y P. Kłoskowica [?], Sąd nakazał do tygodnia się rozliczyć.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 155,
        "numer_pozycji": "155",
        "strona_pagina": "fol. 77r (77)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Kontumacje i manifestacje w sporze o sukcesję po wójcie Ubaldzie Janaszkowiczu",
        "osoby_podmioty": "Jan Proskowic [?], Wojciech Kłopot, Stasik [?], Jan Murowski [?], Stanisław Solecki, Jan Barankowicz, Wojciech Wardęga, Katarzyna Nowacka, P. Wojciech Grzymałowski, wójt Ubald Janaszkowicz (zm.)",
        "kwoty_podatki": "-",
        "opis_sprawy": "Kontumacja Jana Proskowica [?] z instancji Wojciecha Kłopota oraz Stasika [?] z instancji Jana Murowskiego [?]; poniżej manifestacja Stanisława Soleckiego i Jana Barankowicza przeciw Wojciechowi Wardędze oraz relacja o Katarzynie Nowackiej landwójtowej urzędowskiej w sprawie wykonania dekretu Trybunału Zamojskiego i wydania wołów oraz krowy po zmarłym wójcie kraśnickim Ubaldzie Janaszkowiczu przeciw P. Grzymałowskiemu; na dole protestacja Katarzyny Nowackiej przeciw Wojciechowi Grzymałowskiemu.",
        "transkrypcja": """77.
Contumacia Joannis Proskowic [?] ad instantiam Alberti Kłopot.
Contumacia Stasik [?] ad instantiam Joannis Murowski [?].

Manifestatio Stanislai Solecki et Joannis Barankowicz contra Albertum Wardęga.
Relacya o Sławney Paniey Katarzynie Nowackiey Landwójtowey Urzędowskiey exekucyą Dekretu Trybunału Zamojskiego czyniącey na przeciw Sławnemu Panu Wojciechowi Grzymałowskiemu o oddanie wołów y krowy po zmarłym Sławetnym Panu Ubaldzie Janaszkowiczu Wójcie Kraśnickim y oycu żony jego pozostałych.

Protestatio Catharinae Nowacka contra Albertum Grzymałowski.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 156,
        "numer_pozycji": "156",
        "strona_pagina": "fol. 77v (77v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Wpis niedokończony: skarga przedmieszczanina Jędrzeja Panka",
        "osoby_podmioty": "Jędrzej Panek",
        "kwoty_podatki": "-",
        "opis_sprawy": "Karta w większości pusta z widocznym przebiciem atramentu z sąsiednich kart; u góry data 4 czerwca 1698 r. (Feria Quarta post Dominicam Infra Octavam Sacratissimi Corporis Christi) i początek skargi przedmieszczanina Jędrzeja Panka.",
        "transkrypcja": """77v.
Actum Feria Quarta post Dominicam Infra Octavam Sacratissimi Corporis Christi Anno 1698 [4 VI 1698].
Skarżył się Uczciwy Jędrzej Panek przedmieszczanin Kraśnicki [dalsza część karty niezapisana / wyblakła].""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 157,
        "numer_pozycji": "157",
        "strona_pagina": "fol. 78r (78)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dekret w sprawie Berka Moszkowicza z Kłopotem i kontumacje",
        "osoby_podmioty": "Żyd Berek Moszkowicz, Paweł Kłopot, Burmistrz, Tomasz Kołkowic [?], Sebastian Sowiński [?], Adam Wilk, Maciej Kłopotek [?], Tomasz Trawiński [?], Bartłomiej Piasecki",
        "kwoty_podatki": "4 grzywny; 2 grzywny",
        "opis_sprawy": "Pod datą 16 czerwca 1698 r. (Feria Secunda post Festum S. Antoni) sprawa Żyda Berka Moszkowicza przeciw Pawłowi Kłopotowi o woły i 4 grzywny (z czego 2 grzywny dla P. Burmistrza); sprawa Tomasza Kołkowica [?] przeciw Sebastianowi Sowińskiemu [?]; kontumacja Adama Wilka z instancji Macieja Kłopotka [?] oraz kontumacja Tomasza Trawińskiego [?] z instancji Bartłomieja Piaseckiego.",
        "transkrypcja": """78.
Actum Feria Secunda post Festum S. Antoni proxima Anno 1698 [16 VI 1698].
W sprawie między Niewiernym Berkiem Moszkowiczem Żydem Aktorem a Uczciwym Pawłem Kłopotem Pozwanym o woły y grzywien cztery, z których dwie grzywny P. Burmistrzowi przysądzono.
W sprawie między Tomaszem Kołkowicem [?] a Sebastianem Sowińskim [?].
Contumacia Adami Wilk ad instantiam Mathiae Kłopotek [?].
Contumacia Thomae Trawiński [?] ad instantiam Bartholomei Piasecki.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 158,
        "numer_pozycji": "158",
        "strona_pagina": "fol. 78v (78v)",
        "sygnatura": SYGN,
        "data_rok": "1698 (wzm. 1694)",
        "kategoria": "Intromisja Kobierskiej (1694) oraz manifestacje Berka Moszkowicza i Łopatki",
        "osoby_podmioty": "Żyd Berek Moszkowicz, wdowa Szymonowa Kobierska, Katarzyna Nowacka, Paweł Słomkowski, Paweł Kłopot, Sebastian Łopatka [?], Karol Mrozowski [Mroziński?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Wpis Żyda Berka Moszkowicza dotyczący intromisji wdowy Szymonowej Kobierskiej z datą 15 stycznia 1694 r.; kontumacja Katarzyny Nowackiej z instancji Pawła Słomkowskiego; manifestacja Berka Moszkowicza przeciw Pawłowi Kłopotowi o rzekome ukradzenie koni z wozu oraz manifestacja Sebastiana Łopatki [?] w sprawie z Karolem Mrozińskim [Mrozowskim?].",
        "transkrypcja": """78v.
Wpis Niewiernego Berka Moszkowicza o intromisyi wdowy Szymonowey Kobierskiey z datą 15 Januarii Ao 1694.
Contumacia Catharinae Nowacka ad instantiam Pauli Słomkowski.
Manifestatio Berka Moszkowicza contra Paulum Kłopot o rzekome ukradzenie koni z wozu.
Manifestatio Sebastiana Łopatki [?] w sprawie z Karolem Mrozińskim [Mrozowskim?].""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 159,
        "numer_pozycji": "159",
        "strona_pagina": "fol. 79r (79)",
        "sygnatura": SYGN,
        "data_rok": "1698 / 1695",
        "kategoria": "Kontumacja Pietrzaka, protestacja przeciw Majowskiemu i wpis z 1695 r. (Olchowski vs Icek)",
        "osoby_podmioty": "Tomasz Pietrzak [?], Bartłomiej Piasecki, rajca Jan Majowski, Stefan Zasadzowic [?], Szymon Olchowski [?], Żyd Icek [?], Biernas [?]",
        "kwoty_podatki": "3 grzywny",
        "opis_sprawy": "Pod datą 19 czerwca 1698 r. (Feria Quinta ante Festum S. Joannis Baptistae) kontumacja Tomasza Pietrzaka [?] z instancji Bartłomieja Piaseckiego (kara 3 grzywien i 3 dni wieży) oraz protestacja przeciw rajcy Janowi Majowskiemu z instancji Stefana Zasadzowica [?]; poniżej wpis z datą 23 czerwca 1695 r. (Feria Secunda pridie Festi S. Joannis Baptistae 1695): Szymon Olchowski [?] przedmieszczanin z Piasków protestuje przeciw Żydowi Ickowi [?] synowi Biernasia [?] o zniewagę i próbę pobicia córki.",
        "transkrypcja": """79.
Actum Feria Quinta ante Festum S. Joannis Baptistae proxima 1698vo [19 VI 1698].
Contumacia Thomae Pietrzak [?] ad instantiam Bartholomei Piasecki pod winą grzywien trzech y trzema dniami wieży.
Protestatio contra Fam. Joannem Majowski Consulem ad instantiam Stephani Zasadzowic [?].

Actum Feria Secunda pridie Festi S. Joannis Baptistae proxima 1695 [23 VI 1695].
Stanąwszy oblicznie przed Urzędem Uczciwy Szymon Olchowski [?] Przedmieszczanin Kraśnicki z Piasków Protestował się na przeciw Niewiernemu Ickowi [?] Żydowi synowi Biernasia [?], iż on go znieważył y córkę jego chciał pobić, o co protestatur.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 160,
        "numer_pozycji": "160",
        "strona_pagina": "fol. 79v (79v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Obdukcja ran Stanisława Soleckiego i Pawła Dąbrowskiego",
        "osoby_podmioty": "Stanisław Solecki, Matyjasz Borucki [?], Paweł Dąbrowski, Jakub Złotnicki [?], Szczepan Złotnicki [?], ławnik Wojciech Bożkowic, ławnik Wawrzyniec Pisarzowic [Bielaszkowic?], Wolanowski [?], cyrulik Mojżesz Abramowic, Krzysztof Dutkowic [?], Lipczyński [?], Wysocki, Walenty Bosacki [Bożkowic?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Obdukcja ran P. Stanisława Soleckiego, Matyasza Boruckiego [?] i Pawła Dąbrowskiego zadanych przez Jakuba Złotnickiego [?] bez żadnej okazji; rany oglądali ławnicy PP. Wojciech Bożkowic, Wawrzyniec Pisarzowic [?] i Wolanowski [?] z cyrulikiem Mojżeszem Abramowicem (rana na lewej stronie rogu głowy o palec wzdłuż do kości, prawe oko podbite sine, na lewej ręce raz cięty i tłuczony, na prawej ręce sina na członku, pocięta czapka i suknia); obwiniani także Krzysztof Dutkowic [?], Lipczyński [?], Wysocki i Walenty Bosacki [?] (dolna lewa część karty zalana kleksem atramentowym).",
        "transkrypcja": """79v.
Sub eodem Actu.
Do Urzędu y Akt niniejszych oblicznie przyszedłszy Sławetni Panowie P. Stanisław Solecki y Matyasz Borucki [?] tegoż rzemiosła prosili Urzędu aby raz przez Uciwego Jakuba Złotnickiego [?] bez żadney okazyey iemu dany [popr. na: przez Szczepana Złotnickiego?] mógł być widziany do którego deputowani Sławetni PP. Wojciech Bożkowic, Wawrzyniec Pisarzowic [?] Ławnicy przysięgli teraz w Kraśniku do tego z Mojżeszem Abramowicem cyrulikiem takowy raz opowiedzieli: Naprzód u P. Stanisława Soleckiego na lewey stronie rogu głowy ciemienia o palec wzdłuż do kości którey y krew zacieka, Oko prawe podbite sine spuchłe, Na lewey ręce raz cięty o członku od którego rana sina spuchła, Na teyże stronie raz tłuczony siny spuchły od kija o palec wszerz o palcy trzy wzdłuż, oprócz łokieć prezentował tłuczony, na prawey ręce wszerz y wzdłuż na członku siną krwią zaszłą, czapkę y suknię prezentował pociętą, na osobliwie żalił się na wszystkie rany gdy go sobie pokrzywdzony raz obliczyli do szkoły swojey.
Y Uciwego Pawła Dąbrowskiego na samym środku głowy na ciemieniu raz cięty na łokciu na członku poniżej ramienia na prawey ręce raz siny na [nieczyt. — kleks] wszerz y wzdłuż od którego ręka spuchła. W tym wszystkim winę dają Lipczyńskiemu [?] y Krzysztofowi Dutkowi [Dutkowicowi?], [nieczyt. — kleks] tego obłazu y tak częstych [nieczyt. — kleks] ofiarują się tego u prawa dochodzić. Ad finem: Lipczyńskimy y innych przybyłych P. Wysocki y Walenty Bosacki [Bożkowic?] ofiarują się dochodzić.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 161,
        "numer_pozycji": "161",
        "strona_pagina": "fol. 80r (80)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Protestacja Katarzyny Wysockiej oraz inkwizycja o rolę Tudorkowską na Piaskach",
        "osoby_podmioty": "Katarzyna Wysocka, Zofia Pyrzkowna [?], Zofia Piasecka, Aleksander Wysocki, Anna Tudorkowa, Matyjasz Leś [?], Kuczyński [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Protestacja Sławnej Pani Katarzyny Wysockiej przeciw Zofii Pyrzkownej [?] i Zofii Piaseckiej o pomówienie jej męża Aleksandra Wysockiego o niecnotę i złodziejstwo; pod datą 26 czerwca 1698 r. (Feria Quinta ante Festum SS. Petri et Pauli) inkwizycja ze strony Uczciwej Anny Tudorkowej o kwaterę roli nazwanej Tudorkowskiej na Piaskach oraz zeznanie pierwszego świadka Matyjasza Lesia [?] o bójce w domu i przy płocie z udziałem Kuczyńskiego [?].",
        "transkrypcja": """80.
Sub eodem Actu.
Protestowała się Sławna Pani Katarzyna Wysocka na przeciw Zofiey Pyrzkowney [?] y Zofiey Piaseckiey o niecnotę złodziejstwa z Mężem iey Alexandrem Wysockim, o co szerzey z dalszych dowodów proponować na Terminie przyszłym ofiaruje się.

Actum Feria Quinta ante Festum Sanctorum Petri et Pauli Apostolorum proxima Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [26 VI 1698].
Inquisitia z strony Uciwey Anny Tudorkowey o kwaterę roli nazwaney Tudorkowskiey na Piaskach podług Matyasza Lesia [?] z iedney a z drugiey B. R. N. Panny.

Sub eodem Actu Testimonium ex Parte [zapis nadpisany].
1mus testis Uczciwy Matyasz Leś [?] zeznał, iż on nie raz bywał w domu [tekst silnie poprawiany] przy płocie, gdzie Kuczyński [?] z drugiemi przyszedłszy [dalsze wiersze z licznymi skreśleniami i poprawkami o bójce przy stodole].""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 162,
        "numer_pozycji": "162",
        "strona_pagina": "fol. 80v (80v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dekret o rolę Tudorkowską oraz zeznania w sprawie podwodnej Sebastiana Brząsa",
        "osoby_podmioty": "Anna Tudorek, Stanisław Tudorek (zm.), Stanisław Pastuszka Łołkowic [?], Jadwiga Gąskowicowa [?], Sebastian Brząs [?], Rymarczyk, P. Deputat",
        "kwoty_podatki": "7 grzywien (vadium); 2 pary trzewików",
        "opis_sprawy": "Pod datą 26 czerwca 1698 r. dekret w sprawie Anny córki zmarłego Stanisława Tudorka (w obecności ojca jej męża Stanisława Pastuszki Łołkowica [?]) przeciw Jadwidze Gąskowicowej [?] o kwaterę roli Tudorkowskiej — sąd nakazuje przedstawić dowody i zakłada 7 grzywien vadium, dopuszczając zeznania w sprawie trzewików danych przez matkę aktorki; poniżej pod datą 30 czerwca 1698 r. (Feria Secunda ante Festum Visitationis BVM) zeznanie Rymarczyka ze strony Sebastiana Brząsa [?] o jeździe z podwodą do Zamościa pod P. Deputata, spotkaniu z żołnierzami i pozostawieniu wozu z obrokiem u parobka.",
        "transkrypcja": """80v.
Actum Feria Quinta ante Festum Scti Petri et Pauli Apostolorum proxima 1698 [26 VI 1698].
W sprawie między Uciwą Anną córką niegdy Stanisława Tudorka pozostałą małżonką z przytomnością oyca swojego Stanisława Pastuszki Łołkowica [?], a między Uciwą Jadwigą Gąskowicową [?] o kwaterę roli Tudorkowską nazwaną na terminie dzisiejszym agitującej się, ponieważ się z Inkwizycyi jawnie pokazało iż ta ćwierć od Matki Actorki dana iest a ona lubo to iaką do niey niema nic, dla czego y częste poswarki kalumnie przez pozwaną cierpi Actorka, Sąd niniejszy nakazuje widzieć słuszne dowody aby Actorki więcey nie turbowały y żadney sobie nie uzurpowały do tey kwatery possessyey. Co zaś koło poswarków zabiegając im z któreyby strony między niemi pokazały się dowodnie, zakłada się wina grzywien siedmiu ad partem et Judicio medium y więzieniem trzy dniowe. Actorka iednakże ma pozwanej ponieważ świadectwo zeznaje że przy ostateczney woli mówiła Matka męża Actorki kiedy tę ćwierć iemu darowała aby iey z miłości iako siostrze trzewiki kupiła dwie parze, aby Actorka in triduum kupiła Decreti praesentis vigore.

Actum Feria Secunda ante Festum Visitationis Beatissimae Virginis Mariae proxima Anno 1698 [30 VI 1698].
Testimonium tam ex parte Sebastiani Brząs [?].
1mus Uczciwy Rymarczyk. Zeznał iż gdy mi nakazano iechać do Zamościa na podwodę pod P. Deputata, tam przyjechał a ze sześciu żołnierzów szedł y kazali mi się nazad do domu wrócić, ia nieufając w domu wozowi ze wszystkiem com do wiozła nagotował w drodze u karczmy zaprowadziłem a gdy gorszych tam jadów wozów były, kazałem parobkowi aby obrok wozowi tego do domu przyniósł który przyniósł, na za jutro zaś kazałem mu iak się żołnierstwo uspokoi po wóz spodziewając się że trzeba P. Deputatowi.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 163,
        "numer_pozycji": "163",
        "strona_pagina": "fol. 81r (81 / 78)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dalsze zeznania o zaginionym wozie w stodole Szymona Olchowskiego",
        "osoby_podmioty": "Rymarczyk, Szymon Olchowski, Brząs [?], Katarzyna Kozakowa, Kozakowicz (syn Kozaka), Kuśmierz alias Olchowski",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie zeznania o szukaniu zaginionego wozu na polu, rozmowie z Brząsem [?] i odnalezieniu wozu zamkniętego w stodole Szymona Olchowskiego; poniżej zeznanie 2. świadka Katarzyny Kozakowej oraz 3. świadka syna Kozakowego (Kozakowicza) o tym, jak wóz zaprowadzono do stodoły Kuśmierza alias Olchowskiego i jak spotkał ich Rymarczyk.",
        "transkrypcja": """81. [u dołu: 78.]
iednako iechać. Przyszedł parobek z pola opowiedział że wozu naszego niemas. W tym ia wziąwszy się samo piąty bez niedzieli szukaliśmy y napadszy stróżka który pasł bydło pytaliśmy ieżeli wozu niewidział żeby kto wziął. Odpowiedział że nie zginie wasz wóz, iam go powtórnie mówił powiadaj mi gdy mi niechciał powiedzieć samym nim oświadczyłem się że mi szkody należyć będzie odpowiedzieć. Więc niedzieli iuż ku wieczorowi idąc syn móy spotkał się z Brząsem gdzie Brząs pytał się go abo to wam wóz zginął odpowiedział że zginął szukaliśmy go cały dzień Brząs rzekł ba niewidział ia takiego wozu u Szymona Olchowskiego iaki iest teraz u niego w stodole zamknięty. W tym syn wrócił się do domu to usłyszawszy powrócił y to mi powiedział iam go zaraz widząc na sam ślad nagle pośpieszyć sobie posłałem tegoż syna aby z wolna przyszedłszy do pomienionego Olchowskiego pytał się ieżeliby wozu niewidzieli na co w niebytności męża iey żona jego odpowiedziała że ia o tym niewiem, a z pochwili w nocy odesłał mi przez dziecię odesłał mi Olchowski wóz bez wiadomości moiey.

2dus Uczciwa Katarzyna Kozakowa zeznała iż ia idąc poszedłszy do koni nadybałam wóz słomą przykryty y powiedziałam pastuchom o tym wozie gdzie y czyi mógł być z mięśniami po tym z pola odchodząc móy mąż z synem Kuśmierza alias Olchowskiego wziąwszy zaprowadzili do stodoły Kuśmierza do stodoły na cmentarz gdy ten brat Rymarczyk wozu spotkał się móy mąż z nim y gdy go Rymarczyk on pytał powiedział mu iż ieżeli to wasz wóz to iest w stodole u Kuśmierza bośmy niewiedzieli czyi tameśmy go zaprowadzili.

3tius Testis Syn Kozak [Kozakowicz] haec formalia recognovit iem iak mi dali oni znać żem go zaprowadził do stodoły Olchowskiego y nie widzę go, a lubo go zechcesz zarazem Rymarczyku spytać nie.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 164,
        "numer_pozycji": "164",
        "strona_pagina": "fol. 81v (81v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dylacja na Wisłę, protestacja Olchowskiego na Rymarczyka i zeznanie Tomasza Starego Kmiecia",
        "osoby_podmioty": "Kozakowicz, Szymon Olchowski, Sebastian Brząs [?], Jakub Boguta, Marcin Rymarczyk, Tomasz Stary Kmieć, Kozakowa",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie zeznania syna Kozaka; decyzja w sprawie Szymona Olchowskiego przeciw Sebastianowi Brząsowi [?] o dylację do piątku z uwagi na wyjazd aktora na Wisłę; diligentia Jakuba Boguty; solenna protestacja Szymona Olchowskiego przeciw Marcinowi Rymarczykowi o odejście od sądu i zabranie rzeczy (zrzepy); pod datą 4 lipca 1698 r. (Feria Sexta post Festum Visitationis BMV) początek zeznania Tomasza Starego Kmiecia ze strony Szymona Olchowskiego o spotkaniu z Kozakową przy bydle i wozie.",
        "transkrypcja": """81v.
ustaw wozu tego nieukradłeś ale nie wiem czy byśmy go pierwey zaprowadzili do stodoły Olchowskiego niżli to go poznać, on mi za to podziękował.

Sub eodem Actu.
W sprawie między Uciwym Szymonem Olchowskim Aktorem a Uciwym Sebastianem Brzązem [?] ponieważ Actor zabiera się na Wisłę ze świadectwem pozwala im się dilacyey do Piątku blisko przyszłego Conservando partibus terminum peremptorium.

Diligentia Instanti et Honesti Jacobi Boguta [nadpisane: Diligentia Uciwego Jakuba Boguty względem...].

Uciwy Szymon Olchowski solennie protestował się na Uciwego Marcina Rymarczyka iż on odszedłszy od Sądu protestanta słowa w domu gdzie sprawy nie ma [?] o zadanie mu rzepy gdy mu z gwałta woda iako by mu protestant miał znalazłszy nie oddać, o co iuż z prawa za S. P. Wójta agitowała się y umorzono iest, ino in praeiudicium protestanta teraz iterum atque iterum protestuje się offerens se cum eo Judicialiter Actum.

Actum Feria Sexta post Festum Visitationis Beatissimae Mariae Virginis Anno 1698 [4 VII 1698].
Testimonium ex Parte Simonis Olchowski.
1mus Testis Thomas Stary Kmieć zeznał żem na ten czas bydło pasł u matki swojey gdzie pasąc bydło z dróżkami chłopcy dali znać że Kozakowa za zamieść wóz przykryty słomą, my też poszli y napadliśmy na to iak ona powiadała y przy tym wozie bawiliśmy się y rzekliśmy do siebie abyśmy się tym wozem podzielili: Kozakowa na to rzekła lepiey go wcale zawieść do domu spytacie o niego kto tedy ma się oddać w tym na zajutrz szukał Rymarczyk wozu, my też powiedzieliśmy bierz u Kuśmierza wóz po który.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 165,
        "numer_pozycji": "165",
        "strona_pagina": "fol. 82r (82 — wklejka)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Ugoda Jadwigi Taborówny z pasierbami o pretensje spadkowe",
        "osoby_podmioty": "Jadwiga Taborówna (płócienniczka, żona tokarza), Małgorzata (pasierbica), Jędrzej (pasierb), Jan, Piotr [?], Matka",
        "kwoty_podatki": "-",
        "opis_sprawy": "Luźna karta wklejona do księgi, datowana 26 września 1698 r. (Feria Sexta ante Festum Scti Michaelis Archangeli): Uczciwa Jadwiga Taborówna płócienniczka żona tokarza zawiera przez przyjaciół ugodę z pasierbami (Małgorzatą, Jędrzejem, Janem i Piotrem [?]) względem pretensji przed sądem wójtowskim kraśnickim, kwitując ich z wszelkich dalszych roszczeń.",
        "transkrypcja": """82. [wklejka]
Actum Feria Sexta ante Festum Scti Michaelis Archangeli Proxima Anno 1698vo [26 IX 1698].
Uciwa Jadwiga Taborówna Płócienniczka żona Tokarza pozostała Małżonka względem pretensyey które przed Sądem Wójtowskim Kraśnickim agitowały się po kilkakroć z Pasierbami Małgorzatą y z synami, ponieważ iuż dobrowolnie więcey nie trudniąc Sądu przez przyjaciół zgoda stanęła o czym iuż niema nic ani żadney pretensyey zeznała że we wszystkim ukontentowana to iest od PP. Matki także y Jędrzeja Pasierbów a Mieszczańców [?] Jana, Piotra [?] synów od których przy Urzędzie za dość się stało.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 166,
        "numer_pozycji": "166",
        "strona_pagina": "fol. 83r (83 / 79)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Ciąg dalszy zeznań (Rutkowic, Ruchowski) oraz spory Żyda Arela i Olchowskiego",
        "osoby_podmioty": "Stanisław Rutkowic [?], Jan Ruchowski [?], Żyd Arel [Aron?], Józef Macal, Szymon Olchowski, Marcin Rymarczyk, Sebastian Brząs [?], Wójt",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie inkwizycji ze skanu 164: zeznania 2. świadka Stanisława Rutkowica [?] i 3. świadka Jana Ruchowskiego [?] potwierdzające odebranie wozu ze stodoły; poniżej sprawa między niewiernym Arelem [?] a Józefem Macalem o kamienicę/szynk (dylacja do poniedziałku) oraz sprawa Szymona Olchowskiego przeciw Marcinowi Rymarczykowi i Sebastianowi Brząsowi [?] odesłana do P. Wójta i urzędu.",
        "transkrypcja": """83. [u dołu: 79.]
on zaraz poszedł y on zaraz odebrał.
2dus Testis Stanisław Rutkowic [?] hoc similia recognovit de verbo ad verbum.
3tius Testis Jan Ruchowski [?] zeznał iż temu iest lat cztery iak to się stało, ale na ten czas pamiętno było.

Sub eodem Actu.
Inter Infidelem Arel [Aron?] Actorem et Josephum Macal Christianum Citatum.
Actio ze go niewinnie Macal na szynku pogotowała co za dworzec [?] atata odpowiedniała, iż onegoż niełaciła y owszem namawiała aby mu zadać. Dawno nie lat cień. Data dilatio utrique parti ad deducendum ad feriam secundam proximam venturam. Conservatur partibus terminus peremptorius.

Sub eodem Actu.
Inter Simonem Olchowski Actorem et Martinum Rymarczyk Sebastianum Brząz [?].
Sprawa między niemi. A że skora poważa [?] mocą patrzy się sprawy od deserta do S. Wójta y Urzędu. Strony obie dwie każą się posłać przed P. Wójta y Ławników na ostatek [?].""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 167,
        "numer_pozycji": "167",
        "strona_pagina": "fol. 83v (83v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Ugoda i vadium 50 grzywien w sprawie Szymona Olchowskiego",
        "osoby_podmioty": "Paweł Słomkowski, Stefan Kwasowic, Wojciech Grzymałowski, Wawrzyniec Bielaszkowic, Szymon Olchowski",
        "kwoty_podatki": "50 grzywien (vadium)",
        "opis_sprawy": "Wpis pojednawczy przed urzędem (PP. Paweł Słomkowski, Stefan Kwasowic, Wojciech Grzymałowski, Wawrzyniec Bielaszkowic) w sprawie Szymona Olchowskiego o rany i przeprosiny za kalumnię; nałożono vadium pięćdziesiąt grzywien (na rzecz ołtarza/bractwa Najświętszej Panny Różańca Świętego oraz sądu) dla zachowania wiecznego pokoju.",
        "transkrypcja": """83v.
PP. Pawła Słomkowskiego, Stephana Kwasowica, Wojciecha Grzymałowskiego, Wawrzyńca Bielaszkowica Ławników Przysięgłych Urzędu Kraśnickiego [przedstawicieli?].
Przedmieszczanina y sąsiada ich tokarza między niemi czynili, a potem za naprzód iż kaseta weyście które negował. Więc w tymże z bez żadnego... Szymonowi Olchowskiemu o rany in instanti uczynił onego solennie przeprosił. A in quantum by która strona przeciwko takiemu kalumnię zadawać vadium między niemi przywiedzionej za to u pod teorem trzecia część grzywien pięćdziesiąt dochodziła do Różańca Panny Maryi Świętego Różańca, trzecia część et Judicio per medium nieopuszczając inne zaś oddania dalszego pretensye które by były y miały strony do siebie salvis Actis między niemi y wolno się będzie rozpisać. Potem ale wszystkie dawne opisane są, utwierdzono przez przyjaciół et perpetuum silentium między niemi przyrzekli.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 168,
        "numer_pozycji": "168",
        "strona_pagina": "fol. 84r (84 / 80)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Manifestacja Karola Mrozowskiego (200/300 zł) i tumult w jego domu",
        "osoby_podmioty": "Karol Mrozowski, Stanisław Solecki, Adam Potokowicz [Potocki], Rajcy, Stasio (parobek), Pani Mundajna [?] z Izdebna [?], Matyjasz, Kazimierz, P. Panek [?]",
        "kwoty_podatki": "200 zł; 300 zł; grzywny",
        "opis_sprawy": "Otwarcie roku 1698 ('Annus 1698. Cum Dei Auxilio Sit Felix') pod datą 23 stycznia 1698 r. (Feria Quinta ante Festum Conversionis S. Pauli): Sławetny Karol Mrozowski mieszczanin kraśnicki składa sumę 200 zł i grzywny z dekretu w sprawie przeciw Stanisławowi Soleckiemu i Adamowi Potokowiczowi (wyciągając do 300 zł przy rajcach), na co Solecki nie chce przystać i wychodzi; poniżej relacja na uproszenie Karola Mrozowskiego o nocnym tumultcie w jego domu z udziałem parobka Stasia od Pani Mundajnej [?] z Izdebna [?], czeladzi, Matyjasza i Kazimierza.",
        "transkrypcja": """84. [u dołu: 80.]
Annus 1698. Cum Dei Auxilio Sit Felix.
Actum Coram Officio Advocatiali et Scabinali Jurato Crasnicensi Feria Quinta ante Festum Conversionis Sancti Pauli proxima Anno Millesimo Sexcentesimo Nonagesimo Octavo [23 I 1698].
Do Urzędu y Akt niniejszych Wójtowskich Ławniczych Przysięgłych Kraśnickich oblicznie przyszedłszy Sławetny Karol Mrozowski Mieszczanin Kraśnicki chcąc zadość uczynić dekretowi przez Obóz Wójtowski y Radziecki w sprawie P. Stanisława Soleckiego y Adama Potokowica ferowanemu, grzywny dwie opisane oddawał, który że będąc przytem Pan Solecki odbierać niechciał, większey nad to w dekrecie opisanej z pomienionego Karola Mrozowskiego wyciągał sumy to iest złotych dwuset y trzydziestu [nadpisane: złotych 300], jeszcze niekontentował się y zaraz wyszedł ani sobie dał persuadować. Wrócić się niechciał. Przeto Sławetny P. Karol Mrozowski zabiegając tak wielkiemu sporowi przed niniejszym Urzędem manifestował się zabiegając aby takich win pro ratione contraventionis Decretorum nie popadł, omnem facilitatem wypełnienia według Dekretu przed PP. Rajcami specyfikowanych dawał y oświadczał się że zadość chciał czynić, a gdyby niechciał [nieczyt. — dopiski] manifestacya do Akt przyjęta.

Na uproszenie Sławetnego Karola Mrozowskiego przed Urzędem niniejszym oblicznie stanąwszy względem sprawy między nim a Uczciwym Stasiem parobkiem Pani Mundajny [?] z Izdebna [?] przepraszając o takowy hałas w domu jego, relacyą uczynili że idąc z Podgórza z domu do bitwy stanęli u Sławetnego P. Karola Mrozowskiego gdzie słysząc krzyk ludzi z powiedzi ludzi siedzącego P. Mrozowskiego, tam zastali Matyasza y Kazimierza... naprzód sami jako atakowani y bili się, gdzie y dziewka z P. Pankową [?] wyszli w tumulcie pobili y żonę Sławetnego P. Mrozowskiego która gdy chciała rozwadzać poszanowali nie mogąc cierpieć.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 169,
        "numer_pozycji": "169",
        "strona_pagina": "fol. 84v (84v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dokończenie relacji o tumultcie i rejestr spadkowy po Annie Kempionce",
        "osoby_podmioty": "Karol Mrozowski, parobek Stasio, Anna Kempionka [?] (zm.), Matyjasz Piotrowczyk, Babiarczyk [?] (syn Anny Kempionki)",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie relacji o tumultcie w domu Karola Mrozowskiego (gospodarz obudzony ze snu, pobicie kijami); poniżej pod datą 22 kwietnia 1698 r. (Feria Tertia ante Festum S. Adalberti) 'Regestr rzeczy pozostałych po Annie Kempionce co była za Matyjaszem Piotrowczykiem': klacza ze źrebięciem dla syna Babiarczyka [?], krowa dla dziecka z pierwszego ojca, krowa dla dziecka z teraźniejszym mężem (lat półtrzecia), a reszta ruchomości na pogrzeb.",
        "transkrypcja": """84v.
tak wielkiego hałasu Sławetnego P. Karola Mrozowskiego iako Gospodarza ze śpiącego obudzili, który gdy przyszedłszy do izby naprzód im począł odmawiać gdzie indziey posilili się a u mnie żadney o pobytu nie usłyszawszy, że widzieliście ale się zbić byś dał mi pobili. W tym się poszamotali na leżącego Stasia, odpowiedział mu proszę was to nie iest żaden pan u nas, on tedy z rankorem widząc go idącym na dwór z domu wygnał y potem wszyscy tam bili bom w izbie siedział, niewiem. Quod est Connotatum. Ta Inquisitia iest przyjęta sub Actu hoc.

Actum Coram Officio Advocatiali et Scabinali Jurato Crasnicensi Feria Tertia ante Festum Sancti Adalberti Confessoris et Martyris proxima Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [22 IV 1698].
Regestr rzeczy pozostałych po Annie Kempionce [?] co była za Matyjaszem Piotrowczykiem.
1mo. Klacza ze źrebięciem którą sama Nieboszczka odkazała Babiarczykowi [?] synowi swemu która iest własna była.
2do. Także krowa która za własne oyca dziecięcia tegoż z nim spłodzonego iemu należy.
Item krowa dziecięciu z teraźniejszym mężem spłodzonemu któremu lat półtrzecia ma się dostać, ostatek ruchomości na pogrzeb aby ciało grzesznie pogrzebione było.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 170,
        "numer_pozycji": "170",
        "strona_pagina": "fol. 85r (85 / 81)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Spory o kulbakę (Koczorowski vs Białek, Opaskiewicz vs Chuctry)",
        "osoby_podmioty": "Grzegorz Koczorowski [?], Bartek Białek [?], P. Opaskiewicz [?], A. Chuctry [Huctry?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Pod datą 2 maja 1698 r. (Feria Sexta post Festum S. Apostolorum Philippi et Jacobi) sprawa Grzegorza Koczorowskiego [?] przeciw Bartkowi Białkowi [?] o kulbakę; poniżej sprawa Sławetnego P. Opaskiewicza [?] przeciw A. Chuctremu [Huctremu?] o kulbakę z dylacją do najbliższego poniedziałku; na dole sam nagłówek daty 5 maja 1698 r. (Feria Secunda post Festum Inventionis S. Crucis) bez wpisu.",
        "transkrypcja": """85. [u dołu: 81.]
Actum Coram Judicio Advocatiali et Scabinali Jurato Feria Sexta post Festum S. Apostolorum Philipi Jacobi Anno 1698 [2 V 1698].
Na dzisiejszym terminie agituje się sprawa między Uciwym Grzegorzem Koczorowskim [?] Aktorem a Uciwym Bartkiem Białkiem [?] pozwanym iż aktor skargę zaniósł przeciwko o kulbakę którą do tych czas mu nie oddaje, aktor chce przysiądz samego siebie upominając się y przed sądem niechce oddać gdyby nie dopotrzebny. Sąd z tym na prośbę przy pozwanym pod winą vadium aby za kulbakę onego zapłacił y szkodę onemu nagrodził, a co małych gdzie Actis protestatur...

Sub eodem Actu.
Między Sławetnym P. Opaskiewiczem [?] Aktorem a Aktorem A. Chuctrym [Huctrym?] P. Kaniskim [?] data dilatio ad feriam secundam proximam a stary o kulbakę zgodową...

Actum Feria Secunda post Festum Inventionis Sanctae Crucis proxima Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [5 V 1698].
[reszta strony niezapisana].""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 171,
        "numer_pozycji": "171",
        "strona_pagina": "fol. 85v (85v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Pozew przez brewe od Katarzyny Nowackiej oraz obdukcja ran Jana Łazińskiego",
        "osoby_podmioty": "Franciszek Sitarczyk [?], Rajcy kraśniccy, Katarzyna Nowacka, Jan Łaziński (młynarz stoki), Jan Żydek [?], Wojciech Żydek [?], ławnik Stefan Kwasowic, ławnik Wojciech Grzymałowski, ławnik Wawrzyniec Bielaszkowic",
        "kwoty_podatki": "-",
        "opis_sprawy": "Pod datą 15 maja 1698 r. (Feria Quinta ante Festum Pentecostes) zeznanie Franciszka Sitarczyka [?] o oddaniu pozwu Panom Rajcom przez brewe od Katarzyny Nowackiej landwójtowej urzędowskiej; poniżej pod datą 30 maja 1698 r. (Feria Sexta post Festum SS. Corporis Christi) solenna protestacja Jana Łazińskiego młynarza przeciw pracowitym Janowi i Wojciechowi Żydkom [?] o pobicie na gospodzie wraz z obdukcją ran (nad prawym rogiem głowy do kości, zęby/głowa nabrzmiała, pręgi na plecach i rękach od kijów) przy ławnikach Stefanie Kwasowicu, Wojciechu Grzymałowskim i Wawrzyńcu Bielaszkowicu.",
        "transkrypcja": """85v.
Actum Feria Quinta ante Festum Pentecostes proxima 1698 [15 V 1698].
Stanąwszy Uciwy Franciszek Sitarczyk [?] zeznał przed Urzędem iż on dał pozew Sławetnym Panom Rajcom przez brewe od Sławetney Paniey Katarzyny Nowackiey Landwójtowey Urzędowskiey etc.

Actum Feria Sexta post Festum Sacratissimi Corporis Christi proxima 1698 [30 V 1698].
Do Urzędu y Akt niniejszych oblicznie przyszedłszy Uciwy Jan Łaziński młynarz stoki [?] solenniter protestował się na przeciw Pracowitym Janowi y Wojciechowi Żydkom czeladzi w sprawie iż on nie dawszy żadney onym okazyey na gospodzie cichutko z ludźmi zabawiającego się onemu okazyą dali y zaraz ranili bezbronnego de quo iterum atque iterum protestatur offerens se cum iis in foro fori de tanto excessu facturum in cuius protestationis verificationem pokazał w prezencyey Sławetnych Panów Stephana Kwasowica, Wojciecha Grzymałowskiego, Wawrzyńca Bielaszkowica Ławników y przy cyruliku ranę wyżej na prawey stronie nad rogiem głowy przeciętą aż do kości, na lewym boku dwie rany sine aż do kości, zęby nabrzmiałe na członku, rany na plecach y na ręku siny y pręgi bite go przez łóżko przełamali, quod Actis praesentibus connotatum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 172,
        "numer_pozycji": "172",
        "strona_pagina": "fol. 86r (86 / 82)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dekret sądu złożonego w sporze o rachunki po Ubaldzie Janaszkowiczu oraz protestacja Słomkowskiego",
        "osoby_podmioty": "Jan Onufry Kieniewicz [Onupkiewicz?], Adam Karol Mrozowski, Jan Majowski, Wojciech Nowacki, Katarzyna Nowacka, Paweł Słomkowski",
        "kwoty_podatki": "14 grzywien polskich; 4 grzywny",
        "opis_sprawy": "Dekret sądu złożonego (radziecko-wójtowsko-ławniczego) w sprawie spornej o przysięgłe rejestry i kalkulację majątkową między stronami reprezentowanymi przez adwokata ordynaryjnego Jana Onufrego Kieniewicza [?] i mistrza sztuk wyzwolonych Adama Karola Mrozowskiego; nakazano komplanację w domu rajcy Jana Majowskiego wobec Wojciecha i Katarzyny Nowackich pod winą 14 grzywien polskich (oraz 4 grzywien za pierwszą kondemnatę) z wyznaczeniem terminu na piątek po św. Marcinie; poniżej pod datą 13 listopada 1698 r. (Feria Quinta post Festum S. Martini) protestacja podwojciego Pawła Słomkowskiego przeciw Wojciechowi Nowackiemu landwójtowi urzędowskiemu i Katarzynie małżonkom.",
        "transkrypcja": """86. [1698. | u dołu: 82.]
Officium praesens compositum Consulare cum Advocatiali et Scabinali Crasnicense in controversiis partium utrarumque Actoreae personaliter citatae per Famatum Joannem Onuphrium Kieniewicz [Onupkiewicz?] Advocatum Ordinarium Crasnicensem et Adamum Carolum Mrozowski artis liberalis Pictorea Magistrum itidem praesentem suo coram Judicio Plenipotentem... ad comprobationem Juratorum Regestri per Actorem conscripti et producti cuius de lege scripta simpliciter negante citata parte, propior ad comprobandum esse deberet ex rationibus Judicium suum permoventibus necessariam complanationem una cum calculatione in praesentia amicorum ab utraque mutuo sumptorum in domo Famati Joannis Majowski Consulis Crasnicensis sub poena quatuordecim Marcarum Polonicalium parti et officio per medium in casu contraventionis Decreti solvenda... Famati Albertus Nowacki et Catharina coniuges... Terminum partibus ad ulterius contra se procedendum coram Judicio feria sexta post festum Sancti Martini Episcopi proxima Anno ad praesens currenti comparendi. Quod Decretum partes utraeque acceptaverunt et gratias egerunt.

Actum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quinta post Festum Sancti Martini Episcopi proxima Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [13 XI 1698].
Do Urzędu y Akt niniejszych Wójtowskich y Ławniczych Kraśnickich w osobie swojey stanąwszy Sławetny Pan Paweł Słomkowski Podwójci Kraśnicki Actor solennie manifestował się y protestował przeciwko Sławetnemu Panu Wojciechowi Nowackiemu Landwójtowi Urzędowskiemu y Katarzynie małżonkom.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 173,
        "numer_pozycji": "173",
        "strona_pagina": "fol. 86v (86v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Manifestacja Słomkowskiego o niestawieniu się Nowackiej oraz plenipotencja dla Wojciecha Słomkowskiego",
        "osoby_podmioty": "Paweł Słomkowski, Wojciech Nowacki, Katarzyna Nowacka, Ubald Janaszkowicz (zm.), Stanisław Solecki, Jan Barankowicz, Stefan Kwasowic, Wojciech Słomkowski (pasierb)",
        "kwoty_podatki": "14 grzywien (wina)",
        "opis_sprawy": "Ciąg dalszy protestacji Pawła Słomkowskiego przeciw Wojciechowi i Katarzynie Nowackim jako dziedzicom i posesorom dóbr po zmarłym wójcie Ubaldzie Janaszkowiczu o niezrealizowanie dekretu komplanacji i kalkulacji długu mimo sprowadzenia przyjaciół (Stanisława Soleckiego subdelegata, Jana Barankowicza, Stefana Kwasowica ławnika i rajców) oraz niestawienie się Katarzyny Nowackiej do wieczora; poniżej pod datą 24 listopada 1698 r. (Feria Secunda in Vigilia Festi S. Catharinae) wpis przed urzędem radzieckim, w którym Paweł Słomkowski wicewójt kraśnicki ustanawia swojego pasierba Wojciecha Słomkowskiego pełnomocnikiem w sprawie przed Trybunałem Zamojskim.",
        "transkrypcja": """86v.
dóbr tak ruchomych iako y nieruchomych generaliter wszystkich po śmierci niegdy Sławetnego Pana Ubalda Janaszkowica Wójta Kraśnickiego dziedzicom possessorom y dyspozytorom. Oto że oni wiedząc o dekrecie Sądu Obojnego Kraśnickiego który od tygodnia iest ferowany między Actorem a sobą pozwanemi abyśmy przystąpili do kalkulacyi która się oraz y z kompozycyą przyjacielską nie skwapiąc się do przysięgi według Inkwizycyj mnie Actorowi należącey około długu mego, któremu ia dosyć czyniąc abym nie popadł w winę grzywien czternastu y kosztów sprowadziłem z swojey strony przyjaciół Sławetnych Panów Stanisława Soleckiego Subdelegata Urzędu Radzieckiego y Burmistrzowskiego, Jana Barankowica, Stephana Kwasowica Ławnika y Rajców na mieysce naznaczone, a zaś Sławetna Pani Nowacka bywszy obecną w Kraśniku nie przyszła aż wieczór kiedy do niczego niechciała przystąpić, owszem Actora chciała... o to wszystko tak o nie dosyć czynienie Dekretowi iako y o szkody koszta y nie oddanie długu iterum atque iterum in forma Manifestationum solita manifestatur et protestatur.

Actum Coram Officio Consulari Crasnicensi Feria Secunda in Vigilia Festi Sanctae Catharinae Virginis et Martyris Die Videlicet Vigesima quarta Novembris Anno Domini Millesimo Sexcentesimo Nonagesimo Octavo [24 XI 1698].
Ad Officium et Acta praesentia Consularia Crasnicensia personaliter veniens Famatus Paulus Słomkowski Viceadvocatus Crasnicensis sponte palam libere et per expressum recognovit praesenti plenipotentem Honoratum Albertum Słomkowski filiastrum suum in causis omnibus specialiter inter se recognoscentem ab una et Famatos Nowackie coniuges legitimos ad Suppremum Judicium Tribunalitium Dominii Zamoscani parte ab altera scilicet ex Appellatione a Sententia gravaminosa devoluta...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 174,
        "numer_pozycji": "174",
        "strona_pagina": "fol. 87r (87 / 83)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Dekret sądu złożonego na 802 złp 15 gr w sporze Słomkowskiego z Nowackimi",
        "osoby_podmioty": "Paweł Słomkowski, Wojciech Słomkowski, Adam Potokowicz [Potocki], Stanisław Solecki, Jan Barankowicz, Jan Majowski, Wojciech Bożkowic, Stefan Kwasowic, Wawrzyniec Bielaszkowic, Wojciech Nowacki, Katarzyna Janaszkowicowa [Nowacka], Ubald Janaszkowicz (zm.)",
        "kwoty_podatki": "802 złp 15 gr; 4 grzywny; 14 grzywien polskich",
        "opis_sprawy": "Dokończenie pełnomocnictwa z 24 XI 1698 r.; poniżej akt Sądu Złożonego Radziecko-Wójtowsko-Ławniczego z dnia Ofiarowania NMP 21 listopada 1698 r. (w składzie: Adam Potokowicz prokonsul, Stanisław Solecki subdelegat, Jan Barankowicz, Jan Majowski rajcowie, Wojciech Bożkowic, Stefan Kwasowic, Wawrzyniec Bielaszkowic ławnicy): Paweł Słomkowski domaga się od Wojciecha Nowackiego i Katarzyny Janaszkowicowej zapłaty 802 złp 15 gr z dóbr po zmarłym Ubaldzie Janaszkowiczu; sąd zasądza grzywny (4 i 14 grzywien polskich) i nakazuje egzekucję.",
        "transkrypcja": """87. [u dołu: 83.]
quam Consularibus composito Judicio ipso die Festi Praesentationis Beatissimae Virginis Mariae ad praesens currenti elegit constituit et praesentem offerens se omne totum per ipsum gestum pro rato et grato acceptaturum velle alias in forma commissi mandati de iure solita plenissima et perfectissima.

Judicium Compositum Consulare cum Advocatiali et Scabinali Crasnicense celebratum per Famatos Adamum Potokowicz Proconsulem, Stanislaum Solecki Subdelegatum, Joannem Barankowicz, Joannem Majowski Consules, eidem Judicio Assidentes Albertum Bożkowic, Stephanum Kwasowic, Laurentium Bielaszkowic Scabinos Juratos ipso die Festi Praesentationis Beatae Mariae Virginis Anno Millesimo Sexcentesimo Nonagesimo Octavo [21 XI 1698].
In Termino hodierno post translapsum Terminum per partes infrascriptas libere agnito Famatus Paulus Słomkowski Viceadvocatus Crasnicensis Actor petiit ut ante habemus Famati Albertus Nowacki Viceadvocatus Urzędoviensis et Catharina Janaszkowicowa Coniuges Summam florenorum Octingentorum duorum florenorum et grossorum quindecim sibi Actori ex bonis mobilibus et immobilibus generaliter omnibus morte olim spectabilis Ubaldi Janaszkowicz derelictis ad eandem partem possessis hucusque non persolutam una cum refusione damnorum et litis expensarum in instanti exolvant... tum quoque poenam quatuordecim Marcarum Polonicalium...

Officium Consulare compositum cum Advocatiali et Scabinali Crasnicense duo ad condemnationem obiectam atque poenam quatuor Marcarum Polonicalium parti et officio per medium luendam quatenus pars citata in instanti solvat...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 175,
        "numer_pozycji": "175",
        "strona_pagina": "fol. 87v (87v)",
        "sygnatura": SYGN,
        "data_rok": "1698",
        "kategoria": "Apelacja Słomkowskiego do Trybunału Zamojskiego i protestacja o kalumnię",
        "osoby_podmioty": "Paweł Słomkowski, Katarzyna Nowacka, Wojciech Nowacki",
        "kwoty_podatki": "14 grzywien polskich; 4 złp (gwoździe); 1 złp 23 gr (kremat); 15 grzywien",
        "opis_sprawy": "Dokończenie dekretu z 21 listopada 1698 r.: sąd zwalnia Katarzynę Nowacką z kary 14 grzywien (wobec manifestacji o niemożności komplanacji), zasądza na rzecz Słomkowskiego jedynie 4 złp za gortowe gwoździe i 1 złp 23 gr za kremat, lecz na powoda nakłada 15 grzywien kary, 15 dni wieży na ratuszu i obowiązek przeprosin; Paweł Słomkowski składa apelację do Najwyższego Trybunału Zamojskiego, którą sąd dopuszcza, a następnie protestuje przeciw pozwanej o znieważające słowa wypowiedziane przed sądem ('Wolno ci było ojcu memu obwiesić kazać').",
        "transkrypcja": """87v.
Decreto quo iniunctum fuerat quatenus personaliter eadem Citata pars cum paratis monimentis causam perimentibus comparuisset. Quantum vero attinet poenae quatuordecim Marcarum Polonicalium Parti et Officio per medium solvendae respectu omissionis ad complanationem una cum calculatione inter se Actore et Citata iniunctam, siquidem personaliter comparens prefata Catharina Nowacka sola per se in expiratione temporis peragendae eiusdem compositionis amicabilis una cum calculatione expedienda manifestata est de impossibili acceptatione eiusdem Decreti... liberam a solutione eiusdem poenae esse debere censet. Quo vero spectat rationem praetensionis debiti in propositione sua verbotenus facta referendo se ad productionem Regestri Actorem praescripsisse decernit excepta Summa florenorum quatuor za gortowe gwoździe proveniente atque pro kremato floreni unius et grossorum viginti trium solidi unius libere per partem Citatam agnita quatenus in instanti solvat. Ratione vero temerariae vexae tenetur eadem pars Actorea Citatae Parti Marcas Quindecim Officio totidem luere et reponere idque in instanti sessionem Turris quindecimalem ab Actu praesentis Decreti subire et continuare partem Citatam in Residentia ipsius deprecari idque per quatuor viros dignos, damna et litis expensas per Citatam erogatas restituere Decreti praesentis vigore.

A quo Decreto pro iure non suscepto movit et appellavit ad Suprema Judicia Tribunalitia Civitatis Dominii Zamoscani Actor cuius affectationi annuendo debita cum reverentia eandem Appellationem admisit Officium.

Protestatur Actor contra eandem partem Citatam ratione calumniationis sui furti obiectionis in haec formalia: Wolno ci było oycu memu obwiesić kazać et aliorum inconvenientium idque in facie Officii praesentis.""",
        "link_swa": UNIT_LINK
    }
]

main_data.extend(part7_scans)
with open('/home/ubuntu/workspace/Gen/main_data_j20_part7.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j20_part7.json: {len(main_data)} skanów")
