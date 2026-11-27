# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j20_part3.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
SYGN = "35/40/0/1/20"

part4_scans = [
    {
        "nr_skanu": 76,
        "numer_pozycji": "76",
        "strona_pagina": "fol. 36r (36)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Proces spadkowy poddanych ze wsi Blinów",
        "osoby_podmioty": "Stefan Kondla [Kondlik], Tomasz Rzepka (zm.), Katarzyna Rzepkowa, Agnieszka Rzepkowa (zm.), Jadwiga Staroszkowa, Wojciech Staroszek, Katarzyna Łysakowa, Sebastian Rzepka",
        "kwoty_podatki": "fl 30; fl 200",
        "opis_sprawy": "Dokończenie zeznań i wywodu w procesie spadkowym po zmarłym Tomaszu Rzepce ze wsi Blinów: potwierdzenie długu fl 30 według rejestru oraz rozliczenia między wdową Katarzyną Rzepkową a córkami z pierwszego małżeństwa z Agnieszką — Jadwigą i Katarzyną — oraz synem Sebastianem co do sumy fl 200 i inwentarza.",
        "transkrypcja": """36.
... gdyż datek taki to sam iednak się w tey mierze nie dopuszcza bez wiadomości dawney tylko z Rzepkowie, co tenże dług fl 30 długu oddać według rejestru, jako z Rejestru okazuje y z tego wszystkiego pisać należy. Pozostałość została się po nim która ma iść na dział dla dzieci które pozostały po Tomaszu Rzepce w łaskę wiedzieli panie, gdy między dekret y na objaśnienie przyjdzie Katarzyna Rzepkowa aby wiedziała co ma oddać.
Pierwszy Testament pozostały świadków podpisy... gdy po śmierci tego Tomasza Rzepki została było móc dzieci które z wielkie dzieciem przez lat kilka chował, y pokazał według prawa i sprawiedliwości wszystkie dobra po ojcowskie matki Tomasza Rzepki, a matka dzieci powiedziała że po wielkiey sumie żywiąc dobra nie zostało, bo gdy dana w tey wsi zima została nieporządek, tylko na dziatkach Tomasza Rzepki z małżonką Katarzyną. Co sie tycze prawem tego u której strony jest im surowo do powiedzianych po matce swoiey Agnieszce, których iż pan sędzia nie chce na tak odprawować aby dwoie sie nie rozdzielało... Tomasz Rzepka z małżonką Katarzyną przez lat kilka na tym gruncie, dla którego im surowo aby należy gdyz wiele zostało z ostatku, dobra y dziatki które były spłodzone z Tomaszem Rzepką aby według prawa były szacowane, także bydło, owce y inne dobra, a z działem Katarzyny w domie aby zostało.
Na drugi Rejestrzyk krótko opowiadam że na Blinowie w Rejestrze położyli mnie Sebastiana Rzepkę jako bym przy śmierci był, a tom nie był...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 77,
        "numer_pozycji": "77",
        "strona_pagina": "fol. 36v (36 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Replika i dekret w sprawie wsi Blinów",
        "osoby_podmioty": "J.P. Jan Świderski, Katarzyna Rzepkowa, Wojciech Rzepka, Tomasz Rzepka (zm.), Jan Rzepka, Łukasz Reszka, Stanisław Reszka, Andrzej Rzepka, Paweł Brożek, Jan Karpiński, Stefan Kondla, Mateusz Kłos, Antoni Wacławic [?]",
        "kwoty_podatki": "fl 30",
        "opis_sprawy": "Dokończenie repliki w procesie blinowskim z powołaniem na dekret wydany przed J.P. Janem Świderskim dnia 8 marca 1658 r. (podpis własnoręczny: Jan Świderski mpp), wymieniający świadków z Blinowa: Jana Rzepkę, Łukasza Reszkę, Stanisława Reszkę, Andrzeja Rzepkę, Pawła Brożka, Jana Karpińskiego, Wojciecha Rzepkę, Stefana Kondlę i Mateusza Kłosa; u dołu dopisek Dobra Blinowskie... A. Antoni Wacławic [?] mpp.",
        "transkrypcja": """36 N.
... przeciwko stronie stawać y zeznawać na prawdę... [dokończenie repliki] ... tak iżby ten Dekret nie tylko z powołania Skarbu Polskiego był podniesiony, ale też jako dekret J.P. Świderskiego z dnia 8 Martii Anno Dni 1658 w sobie ma.
Zawołanie J.P. Jana Świderskiego mpp, który w miasteczku Jaśnie Wielmożnego Pana Podkomorzego przed Urzędem naszym zeznał o zgodzie dóbr Blinowskich, iż to wszystko między dziećmi Tomasza Rzepki a żoną Katarzyną Rzepkową było rozdzielone y bez krzywdy ludzkiey się stało, jako świadczą podpisy:
Jan Rzepka wójt Blinowski, Łukasz Reszka, Stanisław Reszka, Andrzej Rzepka, Paweł Brożek, Stanisław Karpiński, Wojciech Rzepka, Stefan Kondla, Mateusz Kłos.
Jan Świderski mpp.

Dobra Blinowskie. Ponieważ sobie nic nie ujmując kazał Rzepka tey sprawie przed J.P. Świderskim stanąć, a tam się bez świadków y innych okoliczności zgodzili, tedy Sąd potwierdza ten dekret y zapisuje do ksiąg.
A. Antoni Wacławic [?] mpp. Kondla z prawa.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 78,
        "numer_pozycji": "78",
        "strona_pagina": "fol. 37r (37)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Replika w procesie spadkowym (Blinów)",
        "osoby_podmioty": "Wojciech Kłos [?], Sebastian Sasek [?], Wojciech Rzepka, Tomasz Rzepka (zm.), Jan Karpiński, Stefan Kondla, Andrzej Kondla, Bartłomiej Janorowski, Stanisław Reszka, Jakub Grątka, Piotr Gieracki",
        "kwoty_podatki": "fl 130; fl 22; fl 20; 7 sztuk bydła",
        "opis_sprawy": "Dalszy ciąg dokumentacji procesu z Blinowa z 1658 r. (daty 12 IV i 14 X 1658 r.): zeznania o majątku po nieboszczyku Tomaszu Rzepce z własnoręcznym podpisem Andrzeja Kondli (Andrzej Kondla mpp), oraz replika powoda przed J.P. Bartłomiejem Janorowskim przeciw dzierżawcy i sukcessorom z wyliczeniem sum fl 130 (w rękach Piotra Gierackiego), fl 22 pszenicy i fl 20.",
        "transkrypcja": """37.
Anno 1658.
Rozliczenie prawne między takiemi iakie było od skarbu Wojciecha Kłosa [?] Blinowskiego w sprawie Tomasza Rzepki, gdzie po śmierci jego pozostał Sebastian Sasek [?], Wojciech Rzepka, a iż po śmierci nieboszczyka Tomasza Rzepki dnia 12 kwietnia z ludźmi świadki liczono... Jakoż gdy przyszli na miejsce Stefan Kondla, Stanisław Reszka y Andrzej Kondla, oświadczyli przed ludźmi o dobrach pozostałych.
Andrzej Kondla mpp.

Replikando pars Actorea podaje iż na niektóre punkta nie dostaje sprawiedliwości w sprawie Blinowskiej przed J.M.P. Janorowskim... po Tomaszu Rzepce gdy przyszło do rozdziału między dziećmi z pierwszey żony y drugą żoną Katarzyną, w której to sprawie Stanisław Reszka, Paweł Brożek, Jakub Grątka, Andrzej Kondla, Stanisław Kondla y inni świadkowie zeznali o tym co zostało:
Blinowskie dobra z dnia 14 octobris 1658:
Pieniędzy gotowych na długu fl 130 u Piotra Gierackiego, żyta korcy 10, pszenice fl 22, tatarki fl 20, bydła sztuk 7 od Kondli, owiec 10.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 79,
        "numer_pozycji": "79",
        "strona_pagina": "fol. 37v (37 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Dekret końcowy w sprawie wsi Blinów",
        "osoby_podmioty": "Tomasz Rzepka (zm.), Agnieszka Rzepkowa (zm.), Jadwiga Staroszkowa, Wojciech Rzepka alias Staroszek, Katarzyna Łysakowa, Maciej Łysak, Katarzyna Rzepkowa, Bartłomiej Janorowski",
        "kwoty_podatki": "fl 30; fl 13; 20 kop zboża; 7 kwart",
        "opis_sprawy": "Początek obszernego dekretu Sądu Wójtowskiego i Ławniczego (Decretum) rozstrzygającego spór o spadek po Tomaszu Rzepce i pierwszej żonie Agnieszce ze wsi Blinów (dawniej z Potoka, przez 48 lat pożycia) na rzecz córek Jadwigi i Katarzyny oraz wdowy Katarzyny Rzepkowej.",
        "transkrypcja": """37 N.
... [dokończenie repliki] ... pieniądze fl 30 w rękach ludzi pozostałe... a wszystko pod wolny rozsądek oddają.

Decretum.
Po długich kontrowersjach przed Sąd niniejszy zeszłych y po pilnym przesłuchaniu stron obu y świadków takowy Dekret między stronami wydany jest:
Ponieważ z zeznań świadków okazuje się iż nieboszczyk Tomasz Rzepka z pierwszą żoną Agnieszką z Potoka do Blinowa przyszedłszy przez lat 48 dorobił się wiela dobra, mając dzieci Jadwigę i Katarzynę, a potym ożenił się powtórnie z Katarzyną, której żadnego zapisu nie uczynił, tylko przed sąsiadami wolę swoją wyznał. Przeto Sąd nakazuje aby z dóbr pozostałych po Tomaszu Rzepce córkom Jadwidze i Katarzynie dział sprawiedliwy oddany był z tego co się po matce Agnieszce należało, a wdowie Katarzynie trzecia część z dorobku nowego przy mężu zasłużonego.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 80,
        "numer_pozycji": "80",
        "strona_pagina": "fol. 38r (38)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Dekret końcowy w sprawie wsi Blinów (c.d.)",
        "osoby_podmioty": "Tomasz Rzepka (zm.), Agnieszka Rzepkowa (zm.), Jadwiga Staroszkowa, Katarzyna Łysakowa, Katarzyna Rzepkowa, Bartłomiej Janorowski",
        "kwoty_podatki": "fl 17; fl 130",
        "opis_sprawy": "Kontynuacja dekretu sądu kraśnickiego w sprawie spadkowej poddanych z Blinowa: szczegółowe rozliczenie kwot fl 17 i fl 130 z testamentu i dorobku Tomasza Rzepki, zasądzenie zwrotu ruchomości i egzekucji przez urząd dworski w Blinowie.",
        "transkrypcja": """38.
... z dóbr tych wszystkich wedle prawa podzielić się mają: po fl 17 każda z córek za pozostałe sprzęty domowe, a z sumy fl 130 na długach będących po połowie między córkami a macochą Katarzyną, z zachowaniem praw J.P. Bartłomieja Janorowskiego dzierżawcy Blinowskiego co do gruntu i inwentarza dworskiego.
A ponieważ niektóre rzeczy przez stronę pozwaną zostały rozproszone, Sąd nakazuje ich zwrot lub zapłatę pod egzekucją urzędu Blinowskiego.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 81,
        "numer_pozycji": "81",
        "strona_pagina": "fol. 38v (38 N.)",
        "sygnatura": SYGN,
        "data_rok": "1658",
        "kategoria": "Dekret i rozliczenie końcowe (Blinów / Zieliński)",
        "osoby_podmioty": "Katarzyna Rzepkowa, Jadwiga Staroszkowa, Katarzyna Łysakowa, Paweł Zieliński [?], Stanisław Reszka, Bartłomiej Janorowski",
        "kwoty_podatki": "fl 12; fl 15; 12 korcy żyta",
        "opis_sprawy": "Zakończenie dekretu w sprawie Blinowa oraz dodatkowy wpis rozliczeniowy z powołaniem na P. Pawła Zielińskiego [?], Stanisława Reszkę i J.P. Bartłomieja Janorowskiego dotyczący 12 korcy żyta i sumy fl 15 oraz fl 12 długu.",
        "transkrypcja": """38 N.
... stronami takowy dekret wydany y przyjęty, z aresztowaniem przez urząd Blinowski do czasu wykonania wszystkich warunków dekretu.

[Wpis dodatkowy na dole karty:]
Oświadczamy się przed Sądem o dług Stanisława Reszki y Pawła Zielińskiego [?], którzy z dekretu winni oddać 12 korcy żyta oraz długu fl 15 y fl 12 pod egzekucją urzędową.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 82,
        "numer_pozycji": "82",
        "strona_pagina": "fol. 39r (39)",
        "sygnatura": SYGN,
        "data_rok": "1668",
        "kategoria": "Protestacja przeciw Żydowi Mamelowi i sprawa szewców",
        "osoby_podmioty": "Andrzej [brat protestującego / Kłopot?], Żyd Marek, Żyd Mamel, szewcy Kanaszek [Kanaszkowic], Jakub Krasnodębski z Urzędowa, Iwan/Jan Kramarz, P. Bombiński [?], Jakub Panownik, Michał Cębalski",
        "kwoty_podatki": "-",
        "opis_sprawy": "Wpisy z roku 1668 (przeskok chronologiczny księgi): 1) Protestacja chrześcijanina (Kłopota) przeciwko niewiernemu Żydowi Mamelowi o pobicie jego i kobiety sprzedającej biały chleb na rynku w jarmark, po tym jak jego brat Andrzej znalazł czerwony rękawik turecki i oddał go Żydowi Markowi; 2) Sprawa szewców Kanaszek przeciw Jakubowi Krasnodębskiemu z Urzędowa o areszt na towary Kramarza stojącego u P. Bombińskiego [?] oraz zeznanie o suknie i kontuszu wuja Michała Cębalskiego.",
        "transkrypcja": """1668. 39.
Przedmieszczanka naprzeciwko Niewiernemu Mameli Żydowi Kraśnickiemu i z żydówkami Kraśnickimi.
Oto iż Brat mój Andrzej znalazłszy rękawik czerwony muchajerowy turecki złoty, y stawił go u Żyda Marka, a nie tego dał go niewiedząc czyi był, w którym ja chodziłem jawnie kilka dni niespodziewając się nic złego. W ten Piątek blisko przeszły to iest w Jarmark pomieniony Żyd Mamel z żydem i z żydówkami na rynek weszli, ten rękawik ja w nie małej gromadzie pokazałem, a żydzi wraz z żydówkami zawoławszy rzucili się na mnie i na białogłowę pszeniczną [sprzedającą chleb biały], bili, szarpali, szamotali, włóczyli, a drudzy chleb pobrali, po ziemi porozrzucali y pieniądze z stołka powywracali y pobrali. W czym ten Mamel był pryncypałem a także pod czas Jarmarku w takim tumulcie mogło się rzucić na kramy y na złoto. Przeto o to pobicie y szamotanie protestuję się przed Sądem W[aszmościów]. Quod est Actis corroboratum.

Inter Hon. Kanaszek Sutores et N. Krasnodębski de Urzędów.
Prosili Actorowie o Areszt Sądowy na rzeczy Iwana Kramarza która stoi u P. Bombińskiego [?] in re et super bonis ipsius. A to dlatego żeby miał wywód z rąk Jakuba Panownika który dał toże sukno na pomienionego Kanaszka prout in anteriori Termino. Insuper statuerunt Jacobum Krasnodębski de Urzędów, który zeznał o suknie i kontuszu od wuja mego P. Michała Cębalskiego które mi w kamienicy darował było.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 83,
        "numer_pozycji": "83",
        "strona_pagina": "fol. 39v (39 N.)",
        "sygnatura": SYGN,
        "data_rok": "1668",
        "kategoria": "Proces Żyda Mamela z Kłopotem i sprawa o kontusz",
        "osoby_podmioty": "Jakub Krasnodębski, krawiec Turobiński, burmistrz Turobiński, krawiec Franciszkowski, Żyd Mamel, Kłopot, brat Kłopota (Andrzej)",
        "kwoty_podatki": "kilka złotych",
        "opis_sprawy": "Dokończenie zeznań Jakuba Krasnodębskiego o szyciu kontusza w Turobinie u krawca Turobińskiego (z dopiskiem o krawcu Franciszkowskim); protokół ze środy po Trzech Królach 1668 r. (11 I 1668): sprawa Żyda Mamela przeciw Kłopotowi o bójkę na jarmarku i chleb biały (nakaz oczyszczenia z 2 świadkami); na dole nagłówek sesji z poniedziałku przed św. Pryską 1668 r. (16 I 1668).",
        "transkrypcja": """39 N.
... [dokończenie zeznań Jakuba Krasnodębskiego] ... szedłem do Turobina kontusz robić z niego krawcowi P. Kłopotowskiemu teraz niegdyś Burmistrzowi Turobińskiemu, a gdy się skąpiło to sukno, niedostało go na podłożenie, y kazał tenże krawiec przykupić pułłokcia u Żyda, ale nie mogłem takiego dostać, więc przydał białe sukno u krawca Franciszkowskiego. Ten kontusz u Kanaszka co iest na nim bo go znam po szwie... Quod est susceptum ad mandatum Famae Dni Advocati.

Feria Quarta post Festum Sanctorum Trium Regum proxima A.D. 1668.
Inter Infidum Mamele et H. Kłopot Cit.
Proponował Actor contra Citatum ze go w piątek blisko przeszły pod czas Jarmarku pobił y poranił, o co to dokładając iż jeśli mu był co winien miał na niego Sąd u Imci P. Podstarościego. Ex adverso Citatus personaliter comparens intulit że ten Żyd na Rynku wten czas bez niego bił i chleb biały jej pobrał y ma szkody na kilka złotych. Sąd nakazał aby się Kłopot dwoma świadkami oczyścił w piątek blisko przyszły.

Actum Feria Secunda ante Festum Sanctae Priscae Virginis et Martyris proxima Anno Dni 1668.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 84,
        "numer_pozycji": "84",
        "strona_pagina": "fol. 40r (40)",
        "sygnatura": SYGN,
        "data_rok": "1666",
        "kategoria": "Kwitacja z sumy 100 złp (Kanonicy Regularni)",
        "osoby_podmioty": "Anna Dubitowa (żona Macieja Dubita), Maciej Dubit, ławnik Wojciech Kurowic, Wojciech Tuszyński (syn Mikołaja), zmarły Mikołaj Tuszyński, Maciej Konięga, Krystyna Konięgowa",
        "kwoty_podatki": "fl 100",
        "opis_sprawy": "Akt z poniedziałku w wigilię św. Tomasza Apostoła 1666 r. (20 XII 1666): Anna (trzecia żona chorego mieszczanina Macieja Dubita, w asyście ławnika Wojciecha Kurowica) wraz z synem z pierwszego małżeństwa Wojciechem (synem zmarłego Mikołaja Tuszyńskiego) kwitują Macieja Konięgę i jego żonę Krystynę z sumy zapisanej w wigilię św. Andrzeja 1666 r.",
        "transkrypcja": """40.
Actum Feria Secunda in Vigilia Festi Sancti Thomae Apostoli proxima Anno Domini Millesimo Sexcentesimo Sexagesimo Sexto.

Coram Actis praesentibus Advocatialibus et Scabinalibus Crasnicensibus Personaliter comparentes Honesta Anna Honesti Mathiae Dubito Civis Crasnicensis iam tertii voti Consors, Una cum assistentia Famati Alberti Kurowicz Scabini Jurati Crasnicensis sibi quo ad hunc Actum praecipue Loco praedicti Mariti tam temporis in Lecto aegritudinis decumbentis assumpti Tutoris, filius vero ipsius nomine Albertus in assistentia eiusdem Tutoris sani mentibus et Corporibus existentes, non compulsi nec coacti ullo levis errore circumventi, Verum animo bene deliberato et praemeditato, palam libere ac per expressum recognoverunt. Quia ipsi et Alberto filio eius ex Marito primi voti suo videlicet olim Nicolao Tuszyński Cive Crasnicensi suscepto, realiter et effectualiter Vigore Inscriptionis certae de Actu et data Feria Secunda in Vigilia Festi Sancti Andreae Apostoli proxima Anno Domini Millesimo Sexcentesimo Sexagesimo Sexto proxime praeterito per Honestum Mathiam Konięga et Christinam Conjuges coram Iudicio Advocatiali et Scabinali Crasnicensi recognitae... plenarie...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 85,
        "numer_pozycji": "85",
        "strona_pagina": "fol. 40v (40 N.)",
        "sygnatura": SYGN,
        "data_rok": "1666",
        "kategoria": "Kwitacja na 100 złp dla Macieja Konięgi (Prepozyt Jastrzębski)",
        "osoby_podmioty": "Anna Dubitowa, Wojciech Tuszyński, Maciej Konięga, Krystyna Konięgowa, ks. Ludwik Jastrzębski [Jastrzęski?] (prepozyt kraśnicki), notariusz Franciszek Antoni Grot",
        "kwoty_podatki": "fl 100",
        "opis_sprawy": "Dokończenie kwitacji z 20 XII 1666 r. potwierdzającej odbiór sumy 100 złp z rąk wielebnego ks. Ludwika Jastrzębskiego [Jastrzęskiego?], doktora teologii, prepozyta kraśnickiego i konwentu Kanoników Regularnych, z uwolnieniem domu Macieja Konięgi i jego żony Krystyny; uwierzytelnione ekstraktem przez notariusza przysięgłego Franciszka Antoniego Grota.",
        "transkrypcja": """40 N.
... plenarie satisfactum est, Videlicet de Summa Florenorum Centum monetae Polonialis sibi recognoscentibus super Domo Famati Mathiae Konięga et Consortis eius obligata et inscripta, idque de manibus Adm. Rndi Domini Ludovici Jastrzenski [Jastrzębski?] Sac. Theol. Doctoris, Praepositi Crasnicensis et totius Conventus Crasnicensis Canonicorum Regularium. De qua quidem summa Florenorum Centum realiter et effectualiter sibi in facie Iudicii praesentis enumerata, levata atque percepta praefatum Adm. Rndum Praepositum, totumque Conventum Crasnicensem eorumque Successores in perpetuum quietant, liberosque ac indemnes faciunt et promittunt. Inscriptionemque supradictam super praedictam summam Florenorum Centum Polonialis per dictum Mathiam Konięga factam cassant, annihilant, nulliusque viris quoad hanc summam sibi servire debere declarant vigore praesentis Quietitionis. Quod est Actis praesentibus inscriptum Memorialibusque firmatum.
Ex Protocollis Actorum Iudicii Advocatialis et Scabinalis Crasnicensis depromptum per me Franciscum Ant. Grot Publicum Sac. Auct. Aplica et Civitatis eiusdem Notarium Iuratum mpp.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 86,
        "numer_pozycji": "86",
        "strona_pagina": "fol. 41r (41)",
        "sygnatura": SYGN,
        "data_rok": "1668",
        "kategoria": "Testament szpitalny i areszt na winiarza proboszcza",
        "osoby_podmioty": "Andrzej Węgorzowic [Węgorzowich], Andrzej Macal, Grzegorz Kilianek, Maryna Kilianka, Maciej Kownicki [?], ks. Proboszcz kraśnicki, Jasiemicki [?]",
        "kwoty_podatki": "fl 50",
        "opis_sprawy": "1) Dyspozycja ostatniej woli Andrzeja Węgorzowica, dawniej mieszczanina kraśnickiego, obecnie przebywającego w szpitalu przy kościele św. Ducha w Kraśniku — przekazuje fl 50 ze swojej ojcowizny u Andrzeja Macala na szpital oraz resztę swoim wnuczętom (dzieciom Grzegorza Kilianka, w tym Marynie, i Macieja Kownickiego [?]); 2) Sesja z piątku przed Niedzielą Palmową 1668 r. (23 III 1668): spór plenipotenta ks. Proboszcza przeciw Jasiemickiemu [?] o wywiezione zboże winiarza.",
        "transkrypcja": """41.
Węgorzowich przedtym Mieszczanin Kraśnicki a teraz w starości swoiey w Szpitalu przy Kościele Kraśnickim S. Ducha zostaiący, acz w latach podeszły, iednak zdrowy moc y władzę maiący tak na ciele iako y na umyśle, zdrowy, nieprzymuszony ani żadnym błędem zawiedziony zeznał dobrowolnie iż mu Ucciwy Andrzej Macal Mieszczanin Kraśnicki winien z oycowizny swoiey, podług zapisu y dekretu fl 50, a że dla starości nie mogąc tego dochodzić, zapisuje po śmierci swoiey na Szpital Kraśnicki na sprawienie potrzeb kościelnych złotych pięćdziesiąt, a co by zostało z teyże summy oddaie wnuczętom swoim, to iest dzieciom Grzegorza Kilianka y Macieia Kownickiego [?], to iest Marynie Grzegorzowey Kilianka wnuczce swoiey. Co iest na affektacyą tegoż Szpitala do Akt wpisano.

Feria Sexta ante Dnicam Palmarum prox. 1668.
Inter Plenipotentem Rndi Praepositi Act[orem] et Jasiemicki [?] Citatum.
Ponieważ zaszedł Areszt Urzędowy na zboże winiarza sługi Imci X. Proboszcza które miał w łące u pozwanego, a pozwany tego zboża pozwolił temuż winiarzowi wymłócić bez wiadomości Imci X. Proboszcza, tedy Sąd nakazuje aby pozwany to zboże lub wartość jego Imci X. Proboszczowi oddał pod egzekucją urzędową.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 87,
        "numer_pozycji": "87",
        "strona_pagina": "fol. 41v (41 N.)",
        "sygnatura": SYGN,
        "data_rok": "1668",
        "kategoria": "Kontumacja rajcy Sitarskiego i limitacja sądów",
        "osoby_podmioty": "Marcin Sitarski, Żyd Andzel, woźny sądowy",
        "kwoty_podatki": "-",
        "opis_sprawy": "Wyrok zaoczny (contumacia) przeciwko sławetnemu Marcinowi Sitarskiemu z powództwa Żyda Andzela o dług oraz rygor banicji/egzekucji na dobrach; poniżej urzędowa limitacja sądów (Limitatio Causarum) z powodu nadchodzących świąt Wielkanocnych do czwartku po Niedzieli Przewodniej, ogłoszona przez woźnego na rynku.",
        "transkrypcja": """41 N.
Famatus Sitarski ex parte Infidelis Judaei Andzel Contumax.
Famatus Martinus Sitarski sua sponte in Termino Legitimo ex decreto prolibito cum Infideli Judaeo Andzel in causa debiti non comparuit, neque per Plenipotentem suum excusavit, idcirco ad instantiam eiusdem Judaei Actoris in poenam contumaciae et in vadiis condemnatur, adiudicatis in eius fortunas compensatione damnorum et expensarum cum rigore iuris usque ad plenam satisfactionem. Quod est ad Acta susceptum.

Limitatio Causarum.
Iudicium Praesens Advocatiale et Scabinale Crasnicense ob imminentiam Festi Solennis Paschae iuxta normam antiquam et Iuris dispositionem limitat causas omnes ad Feriam Quartam proximam post Dnicam Conductus Paschae, et hoc per Bedellum Iuratum in Foro publico denunciatum et proclamatum.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 88,
        "numer_pozycji": "88",
        "strona_pagina": "fol. 42r (42)",
        "sygnatura": SYGN,
        "data_rok": "1681",
        "kategoria": "Spory o konie, trawę i relacja Żyda Gorajskiego",
        "osoby_podmioty": "Maciej Pieliński [Pielinkowicz?], Sebastian Skarżeński [Skarzeński?], Żyd Gorajski, Maciej Puonik [Płonik?], Wojciech Progutka [Pogutka?], Bogutka",
        "kwoty_podatki": "fl 2; fl 10; fl 15",
        "opis_sprawy": "Wpisy z roku 1681: 1) Spór Macieja Pielińskiego [?] przeciw Sebastianowi Skarżeńskiemu [?] o areszt na konia i zwrot kosztów; 2) Sesja z poniedziałku przed św. Kazimierzem 1681 r. (3 III 1681): relacja pod przysięgą Żyda Gorajskiego, obywatela kraśnickiego, w sprawie wyceny trawy i siana; 3) Spór Macieja Puonika [?] przeciw Wojciechowi Progutce [?] o trawę wartości fl 10 i szkody fl 15.",
        "transkrypcja": """1681. 42.
Inter Hon. Mathiam Pieliński [Pielinkowicz?] Actorem et Hon. Sebastianum Skarżeński [Skarzeński?] Citatum.
Protestował się Actor na Pozwanego iż osobę jego i konia aresztował bez prawa, a pozwany odpowiadał iż mu konia na szkodzie zajął. Sąd wysłuchawszy stron nakazał wydanie konia i rozliczenie szkód pod aresztem.

Actum Feria Secunda ante Festum S. Casimiri Anno Dni 1681.
Relatio Infidi Judaei Gorayski.
Stanąwszy przed Sądem Radzieckim Niewierny Żyd Gorajski Obywatel Kraśnicki pod przysięgą zeznał iż na szkodzie znalezioną trawę wycenił na fl 2 i siano na fl 10, które rzetelnie zapisał.

Inter Mathiam Puonik [Płonik?] Actorem et Albertum Progutka [Pogutka?] Citatum.
Ponieważ się okazuje z relacji Żyda iż Pozwany trawę skosił i zabrał, Sąd nakazuje aby fl 10 za trawę i fl 15 za szkody oddał pod egzekucją urzędową.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 89,
        "numer_pozycji": "89",
        "strona_pagina": "fol. 42v (42 N.)",
        "sygnatura": SYGN,
        "data_rok": "1681",
        "kategoria": "Przysięgi sądowe i areszt na Żydówkę Moszkową",
        "osoby_podmioty": "Mikołaj Sienka [?], Paweł Kłopotek [Kłopot], Jan Kłopotek [?], Grzegorz Wojtek, Mikołaj Kołodziej [?], Tomasz Kochanowski, Michał Piotrowski, Andrzej Kantorek, Żydówka Moszkowa, Mikołaj Zbrończyk, Sebastian Masłowski, Sebastian Furman",
        "kwoty_podatki": "-",
        "opis_sprawy": "Protokół z 1681 r. (11 III, 18 III oraz po Niedzieli Przewodniej): przysięgi świadków Mikołaja Sienki [?], Pawła Kłopotka, Jana Kłopotka i Grzegorza Wojtka; sprawa Mikołaja Kołodzieja [?] przeciw Tomaszowi Kochanowskiemu o potwarz; przysięgi Michała Piotrowskiego, Andrzeja Kantorka i Mikołaja Zbrończyka; areszt na Żydówkę Moszkową; zeznanie Sebastiana Masłowskiego w sprawie Sebastiana Furmana.",
        "transkrypcja": """42 N.
Actum Feria Tertia ante Festum S. Gregorii Anno Dni 1681.
Nicolaus Sienka [?] Ius Civile Suscepit Iuramentumque dedit.
Paulus Kłopotek Ius Civile Suscepit Iuramentum fecit.
Joannes Kłopotek Ius Civile Suscepit Iuramentum fecit.
Gregorius Wojtek Ius Civile Suscepit Iuramentum fecit.

Inter Hon. Nicolaum Kołodziej [?] Actorem et Hon. Thomam Kochanowski Citatum.
W sprawie o potwarz między Actorem a Pozwanym Sąd nakazał aby Pozwany za obrazę słowną przeprosił y koszty prawne powrócił pod rygorem więzienia.

Actum Feria Tertia ante Festum S. Josephi Sponsi B. V. Anno Dni 1681.
Michael Piotrowski Ius Civile Suscepit Iuramentum fecit.
Andreas Kantorek Ius Civile Suscepit Iuramentum fecit.
Sub eodem Actu: Położyła Niewierna Żydówka Moszkowa Areszt aby się obcy kupiec nie ważył wyprzedawać do rozprawy.
Nicolaus Zbrończyk Ius Civile Suscepit Iuramentum fecit.

Actum Feria 5ta post Dnicam Conductus [?] Anno Dni 1681.
Testis ex parte Sebastiani: Sebastianus Masłowski zeznał pod przysięgą w sprawie Sebastiana Furmana z Zagórza.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 90,
        "numer_pozycji": "90",
        "strona_pagina": "fol. 43r (43)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Karta tytułowa wewnętrzna (1683)",
        "osoby_podmioty": "-",
        "kwoty_podatki": "-",
        "opis_sprawy": "Karta rozdzielcza (okładka wewnętrzna) nowej części księgi wójtowsko-ławniczej z wyraźnym napisem rocznym 1683.",
        "transkrypcja": """43.
1683.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 91,
        "numer_pozycji": "91",
        "strona_pagina": "fol. 44r (44)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Strona tytułowa księgi wójtowskiej z 1683 r.",
        "osoby_podmioty": "Marcin Zamoyski (wojewoda lubelski i bełski, ordynat), Dorota z Leszczkowa Zamoyska (kasztelanowa kijowska), notariusz Jan Rogalowski, wójt Ubald Florian Janaszkowicz",
        "kwoty_podatki": "-",
        "opis_sprawy": "Uroczysta kaligrafowana karta tytułowa księgi Sądu Wójtowskiego i Ławniczego miasta Kraśnika z 1683 r., dedykowana ordynatowi Marcinowi Zamoyskiemu (wojewodzie lubelskiemu i bełskiemu) oraz jego żonie Dorocie z Leszczkowa Zamoyskiej (kasztelanowej kijowskiej), spisana przez patrycjusza i notariusza przysięgłego Jana Rogalowskiego za wójtostwa Ubalda Floriana Janaszkowicza.",
        "transkrypcja": """44.
ACTA
Officii Advocatialis & Scabinalis Crasnicensis
Contractus & Obligationes, tum alias Inscriptiones Officiose recognitas, nec non Causas & Actiones cum Controversiis et Decretis in se
CONTINENTIA
SUB
Felicissimis Illustrissimi & Magnifici Domini Dni MARTINI IN ZAMOSCIE ZAMOYSKI Palatini Lublinensis, Belzensis, Ploskrezoviensis &c. &c. Capitanei Primi Ordinati Haeredis Dni Clementissimi
&
Illustrissima ac Magnifica Domina Dna DOROTHEA DE LESCZKOW ZAMOYSKA Castellanissa Kiioviensis Domina Advitalis & Possestricis Civitatis istius Domina Clementissima
Auspiciis.
Per me Joannem Rogalowski Patritium et Notarium Crasnicensem Juratum sub Honorato ac Spectabili Dno Ubaldo Floriano Janaszkowicz Advocato Crasnicensi Anno Domini 1683tio CONSCRIPTA.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 92,
        "numer_pozycji": "92",
        "strona_pagina": "fol. 45r (45)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Elekcja pisarza miejskiego i skład władz (1683)",
        "osoby_podmioty": "Administrator Jakub Skrzeszowski, wójt Ubald Florian Janaszkowicz, burmistrz Stanisław Gomuza, rajcy Paweł Chmarowicz, Jakub Chmielanowski, Maciej Błaszkowicz, starzy rajcy Marcin Sitarski, Jan Barankowicz, podwójci Paweł Stankowski, ławnicy Sebastian Banaszowicz, Jan Gomuza, Wojciech Kanaszkowicz, kahał żydowski (Dawid Mucda, Lejzor Achiaszowicz, syndyk Mojżesz Majer Jozwowicz), notariusz Jan Rogalowski, Dorota Zamoyska",
        "kwoty_podatki": "-",
        "opis_sprawy": "Uroczysty akt elekcji patrycjusza Jana Rogalowskiego na aktualnego pisarza miejskiego (23 IV 1683) w domu wójta Ubalda Floriana Janaszkowicza z udziałem administratora dóbr kraśnickich Jakuba Skrzeszowskiego, pełnej Rady i Ławy miejskiej oraz reprezentacji kahału żydowskiego (Dawid Mucda, Lejzor Achiaszowicz, szkolnik Mojżesz Majer Jozwowicz), za zezwoleniem kasztelanowej kijowskiej Doroty Zamoyskiej.",
        "transkrypcja": """45.
In Nomine Domini Amen.
Actum Feria Sexta ante Dominicam Conductus Paschae proxima Die Vicesima tertia Aprilis A.D. 1683tio.

Elegitur Joannes Rogalowski pro Notario Civitatis istius Actualis.
Generosus Dominus Jacobus Skrzeszowski Bonorum Crasnicensium Administrator Honoratus ac Spectabilis Dominus Ubaldus Florianus Janaszkowicz Advocatus; Famati Stanislaus Gomuza Proconsul, Paulus Chmarowicz, Jacobus Chmielanowski, Mathias Błaszkowicz Anni Currentis Praesidentes; Martinus Sitarski, Joannes Barankowicz Antiqui Consules; Paulus Stankowski Viceadvocatus, Sebastianus Banaszowicz, Joannes Gomuza, Albertus Kanaszkowicz Scabini Jurati; David Mucda, Leyzor Achiaszowicz Judaei Seniores, Moyzes Maior Jozwowicz Syndicus alias Szkolnik Synagogae Judaeorum Civitatis Crasnicensis, in Negotio infrascripto in Domum Honorati et Spectabilis Dni Ubaldi Floriani Janaszkowicz Advocati Crasnicensis convocati et legitime congregati existentes, consulendo Bono istius Civitatis publico, praecisa Honorati Joannis Rogalowski Patritii... Iuris experientia et Morum probitate eundem pro Notario Civitatis huius de expresso Illustrissimae et Magnificae Dominae Dnae Dorotheae Zamoyska Castellanissae Kiioviensis Dominae Clementissimae consensu unanimi Votis et Sententiis suis elegerunt. Qui quidem Honoratus Joannes Rogalowski sic electus super Officio suo Notariatus...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 93,
        "numer_pozycji": "93",
        "strona_pagina": "fol. 45v (45v)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Przysięga notariusza i proces Stanisława Nawrockiego z Wardęgą",
        "osoby_podmioty": "Jan Rogalowski, Dorota Zamoyska, Stanisław Nawrocki (stary rajca), Jakub Wardęga (z Dzierzkowic), ordynat Jan Zamoyski (zm.)",
        "kwoty_podatki": "-",
        "opis_sprawy": "Złożenie przysięgi przez nowego pisarza Jana Rogalowskiego; następnie protokół ze środy po Niedzieli Przewodniej 1683 r. (28 IV 1683): początek obszernej skargi byłego burmistrza i starego rajcy Stanisława Nawrockiego przeciwko Jakubowi Wardędze z Dzierzkowic (z odesłania kasztelanowej Doroty Zamoyskiej z Miłosnej) o zaległe składki podatkowe jeszcze z czasów ordynata Jana Zamoyskiego i ucieczkę z miasta.",
        "transkrypcja": """45v.
Notariatus de Rutara Iuris Praxi et more solitis Iuramentum praestitit. Quod Actis praesentibus connotatum est.

Actum Feria Quarta post Dominicam Conductus Paschae proxima Die Vicesima octava Aprilis A.D. 1683.
Inter Fam. Stanislaum Nawrocki Actorem et Hon. Jacobum Wardęga Cit.

In Termino hodierno ex Remissione ab Illustrissima Domina Dorothea Zamoyska Castellanissa Kiioviensi Dna Clementissima et Citatione legitime ad praesens inaudiente, Famatus Stanislaus Nawrocki consul antiquus Crasnicensis auctore praesentis Actor proposuit et contra Honestum Jacobum Wardęga Anteoppidanum Crasnicensem Citatus in eum qui sequitur modum:
Za odesłaniem od Jaśnie Wielmożney Iey Mości Paniey Kasztelanowey Kiiowskiey Paniey Miłościwey do Urzędu Wójtowskiego dałem przypozwać Jakuba Wardęgę, z którego świętej sprawiedliwości przez czas długi żebrzę w takowej sprawie. Pod czas ciężki za Ordynata Jaśnie Wielmożnego J.M. Pana Ordynata do Kraśnika na ten czas wielkie były ciężary na to ubogie Miasto, gdzie ubodzy ludzie musieli wielkie kontrybucye y składki dawać y wydawać. Między inszymi Jakub Wardęga teraźniejszy Pozwany przedtym był mieszczaninem, a potym przed składkami do Dzierzkowic ze wszystkim zabrawszy się y tam mieszkał a został...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 94,
        "numer_pozycji": "94",
        "strona_pagina": "fol. 46r (46)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Skarga Stanisława Nawrockiego przeciw Wardędze (c.d.)",
        "osoby_podmioty": "Stanisław Nawrocki, Jakub Wardęga, Pan Młodowski (podstarości), Dzierzgowski [?]",
        "kwoty_podatki": "fl 15",
        "opis_sprawy": "Kontynuacja skargi Stanisława Nawrockiego: zajęcie 6 świń Jakuba Wardęgi przez egzaktorów miejskich na poczet zaległych składek (oszacowanych przez gospodarzy na fl 15), ucieczka Wardęgi do Dzierzkowic i oddanie się w poddaństwo podstarościemu Panu Młodowskiemu na Budzyniu.",
        "transkrypcja": """46.
... został był składki Exaktorom przez nie mały czas w swey sesji. Trafunkiem świnie iego z Dzierzkowic powróciwszy sobie przyszły nazad do gniazda, których było sześcioro. Dzierzgowski [?] dał znać Exaktorom; Exaktorowie wziąwszy sługę mieyskiego zaieli pomienione świnie w Sekwestr na ten czas kadencya Urzędu mego przypadała. Ja zniósłszy się z Pany Collegami swemi nakazałem aby go Exaktorowie albo Oyca iego obesłali aby o swoich dobrach wiedział a składki zapłacił; który nam hardzie odpowiedział: niech iedzą świnie za nic y wiedzieć o nich y po nie nie chciał. Exaktorom zaś pieniędzy pilna potrzeba była za polską ratę Urzędu, przez uczciwych dobrych gospodarzów oszacowane te świnie były za złotych piętnaście tylko, bo to były chude y małe, które Exaktorowie przedali y pieniądze odebrali na potrzebę Mieyską obrócili, a sam się tego nie tykał. Wardęga także w Dzierzkowicach po staremu mieszkał y przez lat kilka blisko dziesięciu nic o to nie mówił. A gdy potym odebrał w posesję swoją Kraśnik Jaśnie Wielmożny J.P. Koniuszy Pan nasz Miłościwy a Pan Młodowski został tutecznym Podstarościm, ten Wardęga przykrywszy sobie poddaństwo w Dzierzkowicach poddał się pod Pana Młodowskiego na ten czas Podstarościego, obiecując się być poddanym na Budzyniu y z osobna go udarował iako bogatym...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 95,
        "numer_pozycji": "95",
        "strona_pagina": "fol. 46v (46v)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Skarga Stanisława Nawrockiego przeciw Wardędze i Młodowskiemu",
        "osoby_podmioty": "Stanisław Nawrocki, Jakub Wardęga, Pan Młodowski",
        "kwoty_podatki": "fl 12; fl 6; fl 15; fl 60",
        "opis_sprawy": "Dalszy ciąg skargi Stanisława Nawrockiego: bezprawne wymuszenie przez podstarościego Młodowskiego zapłaty fl 12 za świnie, fl 6 za karmienie i fl 15 za konia na Nawrockim mimo pełnienia przezeń urzędu burmistrza; najazd Wardęgi na pole Nawrockiego i gwałtowne zabranie pary młodych koni w zaprzęgu.",
        "transkrypcja": """46v.
... się potym przechwalał aby tylko swego dokazał żebym mu ia świnie zabrane y iakiegoś konia o których nigdy nie wiedział zapłacił. Pan Młodowski furiozo nie wiedząc nastawszy uwierzywszy złemu Wardędze zdania nie wysłuchawszy ani wyrozumiawszy sprawy zjechawszy niespodzianie do Kraśnika bez sądu żadnego Mieyskiego zawoławszy mię za poduszczeniem niektórych osób mnie zawistnych, którym pod czas Urzędu mego musiałem się naprzykrzyć w podatkach, zaraz mię surowo nie iako mieszczanina y Raycę sądził, ale odpowiadać mię przymusił... przymusił że mi za świnie musiałem dać złotych dwanaście y z osobna za paszę swoię dwie z przychowkiem pokarmione za któremi pomienionemu za paszę musiałem dać złotych sześć; tenże Wardęga gwałtownie wziął y z osobna za konia o którym ia iako żywo nie wiem musiałem dać złotych piętnaście. A że tenże Wardęga pretendował sobie nakładów iakichś złotych sześćdziesiąt a podobno to co Panu Młodowskiemu za tey sprawy dał, a iam ich nie miał skąd płacić ani był powinien; tenże Wardęga naiechawszy na pole moie z pomocnikami dwemi końmi parę młodych z brony włoiczę swowolnie y gwałtownie wziął bez żadnego...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 96,
        "numer_pozycji": "96",
        "strona_pagina": "fol. 47r (47)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Skarga Stanisława Nawrockiego (suplika i przeniesienie na Budzyn)",
        "osoby_podmioty": "Stanisław Nawrocki, Pan Młodowski, Jakub Wardęga",
        "kwoty_podatki": "kilkanaście złotych; fl 26; fl 15; fl 100",
        "opis_sprawy": "Dokończenie relacji Nawrockiego: wręczenie podarunku kilkunastu złotych Panu Młodowskiemu w suplice o zwrot koni, poniżenie przez podstarościego, spalenie chaty Wardęgi na Budzyniu i powrót na Przedmieście, oraz dochodzenie przez Nawrockiego zwrotu fl 26 (za świnie), fl 15 (za konia) i fl 100 za zabrane w zaprzęgu konie.",
        "transkrypcja": """47.
... żadnego sądu y te konie przepadły. Ja ubogi y strapiony człowiek widząc się tak być uciśniony y nie wiedząc co sobie dalej radzić poszedłem z suppliką do Pana Młodowskiego, dałem mu podarunek na złotych kilkanaście żebrząc aby mi przynajmniej konie przywrócił kazał y te sprawę chciał wyrozumieć y przesłuchać; że ia tylko Burmistrzem był żadnych Exakcyi nie tykałem się; y tak wiele tu bydła y tak innych rzeczy za Panów Collegów szacowano y przedawano, a żaden takiego długu ma nie miał, iako ia ubogi człowiek niewinnie. Pan Młodowski y to wziął com ofiarował y mnie pokonfundował mówiąc że mię samego do gąsiora za szyję każe włożyć. I tak ubogi człowiek z hańbą odejść musiałem; a z Wardęgą że na Budzyniu obowiązał się być poddanym sprawiedliwości dojść nie mogłem. A że tenże Wardęga dlatego na Budzyniu został był poddanym aby swego nademną dokazał, szukał potym iakoby z poddaństwa Budzyńskiego wykręcił się. I zapaliwszy prawie własną chatę na Budzyniu wyniósł się znowu na Przedmieście gdzie y zostaie. Upoważony tedy czas swoy i tak ciężkiey krzywdy moiey szukam do Sądów W[aszmościów] żebrząc sprawiedliwości aby mi to com ia mu niesłusznie za świnie wracał musiał złotych dwadzieścia y sześć oddać y złotych piętnaście za konia. Za konie które mi gwałtownie z bron wziął na polu które mnie kosztowały złotych sto, ponieważ memi kilka lat robiąc one wniwecz obrócił y stracił...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 97,
        "numer_pozycji": "97",
        "strona_pagina": "fol. 47v (47v)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Skarga Nawrockiego (ciężary wojenne i kontrybucje miejskie)",
        "osoby_podmioty": "Stanisław Nawrocki, Jakub Wardęga, Pan Młodowski, Jan Szarowski [?], Bębenek [?]",
        "kwoty_podatki": "fl 100; fl 60",
        "opis_sprawy": "Dalszy ciąg skargi Nawrockiego: dochodzenie fl 100 za konie i szkody na mocy dekretu Ordynata, przypomnienie ciężkich czasów wojennych i kontrybucji na żołnierzy (co tydzień płaca, branie wołów, krów, kożuchów i fantów mieszczanom i przedmieszczanom, m.in. Janowi Szarowskiemu [?] i Bębenkowi [?]).",
        "transkrypcja": """47v.
... szkody y omieszkania moie y insze nakłady bez te czasy wszystkie iako mi konie wziął których sobie rachuję na mniey na złotych sto nagrodzić. A nie uporczywie się tego dopominam bo mam w sobie Dekret J.W. Jaśnie Wielmożnego J.M. Pana Dobrodzieia Naszego między tymże Wardęgą a mną przy wszystkim Urzędzie y niektórych z Pospólstwa Kraśnickiego publicznie ferowany. Gdzie J. Mość P. Dobrodziey uważając pilnie te sprawę y widząc Sąd niesłuszny y przegrany Pana Młodowskiego wszystkie Dekreta y kompromisy któremi się na ten czas Wardęga bronił iako niesłuszne pokasował, y nakazał aby Wardęga za świnie zabrane płacił y płacić musiał. Zaraz przypominał że y Nawrockiemu konie y świnie płacić będzie powinien któremu bez byt nie miał brać. Podaję y to pod wysoki rozsądek Sądu W[aszmościów] co wszystkim W[aszmościom] y całemu Miastu jawno, że pod tenże czas bardzo ciężki woyny mieszne były kontrybucye, żołnierzom co tydzień płacić było potrzeba, na co składki ciężkie być musiały. Zaczynym tym którzy składek oddawać nie chcieli brano woły, krowy, kożuchy y inne fanty iako to Panu Janowi Szarowskiemu, Bębenkowi y innym kilkunastom mieszczanom y przedmieszczanom które za różnych Panów Rezydentów których teraz nie wymieniam szacowano y przedawano, a żadnego Pana Rezydenta...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 98,
        "numer_pozycji": "98",
        "strona_pagina": "fol. 48r (48)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Zakończenie skargi Stanisława Nawrockiego",
        "osoby_podmioty": "Stanisław Nawrocki, Jakub Wardęga, Jan Ordynat Zamoyski (zm.), Łyś [?], Pyzik",
        "kwoty_podatki": "fl 15",
        "opis_sprawy": "Zakończenie skargi Stanisława Nawrockiego: obrona uczciwości urzędowania (fanty szacowali egzaktorzy i starsi z pospólstwa na potrzeby miasta), wspomnienie konia zabranego w drodze do Lublina przez żołnierzy ordynata Jana Zamoyskiego (jak i Łysiowi [?] oraz Pyzikowi), wniosek o zwrot majątku i ukaranie Wardęgi więzieniem.",
        "transkrypcja": """48.
... o to ani turbowano ani do płacenia przymuszano. Czemuż ia tedy ieden z pośrodka Panów Rajców mam być takowy żebym tego na żaden swój pożytek nie obracał ale Exaktorowie brali a starsi z Pospólstwa szacowali y na potrzeby Miasta na ten czas gwałtowne obracali. Podaję y to pod wysoki rozsądek: tego konia Wardężynego czyli kradzież za którego mię przymuszono złotych piętnaście płacić nie sam brał ani z mego rozkazania ale wzięli mi go żołnierze Jaśnie Wielmożnego J.M. Pana Jana Ordynata na ten czas kiedyśmy odjechali byli u dworu za J.M.P. Koniuszym pod Broną do Lublina; a nie tylko iemu wzięto ale wzięto Łysiowi [?] y Pyzikowi y innym którym potym Pospólstwo za radą Panów Rajców aby sami na tym szkodowali składkę złożyć y wynagrodzić kazało... A ponieważ tedy pokazałem iaśnie niewinność moię a upór y złość zuchwałą na mnie nienawistnego tego człowieka przeciwko mnie co y Exaktorowie y Starsi z Pospólstwa przyznać muszą, tedy powtórnie upraszam mego dzisiejszego Sprawiedliwości aby mi nie tylko to co odemnie za konia y świnie wziął, ale y to co mi gwałtownie na polu wziął nagrodził, ale też aby za takowe kłótnie winami y więzieniem karany był. Co wszystko do wysokiego rozsądku W[aszmościów] podaię, nieodwłoczney z niego żebrząc świętej sprawiedliwości.
Zarzucenie... 45.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 99,
        "numer_pozycji": "99",
        "strona_pagina": "fol. 48v (48v)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Dekret dylacji (Wardęga) i sprawa Szpitala Św. Ducha (Turek)",
        "osoby_podmioty": "Jakub Wardęga, Stanisław Nawrocki, Prowizorowie Szpitala Św. Ducha, Stanisław Turek (zm.), sukcesorowie Turkowianie [Turek]",
        "kwoty_podatki": "fl 100 (czynsz fl 5)",
        "opis_sprawy": "Dylacja na odpowiedź (7 dni) dla Jakuba Wardęgi w sprawie ze Stanisławem Nawrockim; poniżej protokół z 28 kwietnia 1683 r. (Feria Quarta post Dominicam Conductus Paschae 28 Aprilis A.D. 1683): pozew prowizorów Szpitala Świętego Ducha przeciwko sukcesorom zmarłego przedmieszczanina Stanisława Turka (Turkowianom) o czynsz wyderkafowy fl 5 rocznie od sumy głównej fl 100 zapisanej na półłanku zwanym Popielczanka [?].",
        "transkrypcja": """48v.
Z rzeczonej strony Pozwany Jakub Wardęga stanąwszy osobiście przed Sądem na skargę Aktora nie odpowiadając żądał sobie Dylacyey na odpowiedź do tygodnia.
Urząd tedy Woytowski y Ławniczy Kraśnicki Pozwanego affektacyi dosyć czyniąc takowej mu Dylacyey pozwolił, a oraz tak Aktora aby dowody do tey sprawy dobrze służące iako y Pozwanego aby na swą obronę miał gotowe napomniał. Stronom obiema zawity naznaczając Termin.

Actum Feria Quarta post Dominicam Conductus Paschae proxima 28 Aprilis Anno Dni 1683.
Provisores Hospitalis Sancti Spiritus Actt. contra Successores Turkowianos Citatos.
In Termino hodierno ex Citatione Verbali legitime ad praesens inaudiente, Famati Provisores Hospitalis Sancti Spiritus suos Actores proposuerunt in et contra Successores Honesti olim Stanislai Turek Suburbiani Crasnicensis citatos eo nomine: Aby Pozwani Czynsz Wyderkafowy od Summy pryncypalney złotych sto na półłanku roli zwanym Popielczanka [?] złotego co rocznie szpitalowi Świętego Ducha należący, a od ośmiu lat alias ab ultima Quietitione zatrzymany una cum damnis et litis expensis zapłacili. Decernentes...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 100,
        "numer_pozycji": "100",
        "strona_pagina": "fol. 49r (49)",
        "sygnatura": SYGN,
        "data_rok": "1683",
        "kategoria": "Sprawa Szpitala Św. Ducha z Turkowianami",
        "osoby_podmioty": "Sukcesorowie Turkowianie (Tomasz Turek, Marcin Turek), wicewójt Paweł Stankowski, Prowizorowie Szpitala Św. Ducha",
        "kwoty_podatki": "fl 5 czynszu rocznie",
        "opis_sprawy": "Odpowiedź pozwanych sukcesorów Stanisława Turka (Turkowianów), którzy twierdzą, że czynsz wyderkafowy dla Szpitala Św. Ducha przypada także na innych posiadaczy półłanka; Urząd Wójtowski (z udziałem podwójciego Pawła Stankowskiego) wyznacza 2 tygodnie na rachunek (calculum). U dołu początek kolejnego wpisu przedmieszczan Tomasza i Marcina Turków.",
        "transkrypcja": """49.
Ex adverso Citati personaliter comparentes intulerunt iż nie za tak wiele lat siało się to czynszowe powieda takowe wyderkafowe czynsze z tego półłanku w całku zatrzymane są. A druga że ten półłanek omnes citatos sive Successores za równo concernit a nie wszyscy go iednakowo zażywają, prosząc przed wszystkiem o pozwolenie Dylacyey ażeby się z sobą porachowali kto z nich takowy czynsz zatrzymany płacić powinien.
Officium itaque Advocatiale et Scabinale Crasnicense partium... Actorea per Famatum Paulum Stankowski Viceadvocatum Crasnicensem et eiusdem Provisorem dicti Hospitalis Sancti Spiritus, partibus vero personaliter coram se comparentium controversiis auditis et intellectis, eoque in consideratione habito, quandoquidem Actores eiusmodi censum reemptionalem pro Anno quinto per Citatos ex allegato ipsorum medio anno retentum esse asserunt, id autem Citati negant, deinde rationem ad calculum inter se ineundum quisnam illorum eiusmodi censum retentum de dicto medio laneo Hospitali praefato solvere debeat exspectant. Proinde Acta huius ad probandam assertionem suam, Citatis vero ad expediendum inter se calculum ad duas Septimanas ab Actu hodierno computando Dilationem concedit...

In Termino hodierno ex Citatione Verbali legitime ad praesens inaudiente Honesti Thomas et Martinus Turekowie Anteoppidani Crasnicenses sua et... 46.""",
        "link_swa": UNIT_LINK
    }
]

existing_nums = {r["nr_skanu"] for r in main_data}
for rec in part4_scans:
    assert rec["nr_skanu"] not in existing_nums, f"Duplikat nr_skanu {rec['nr_skanu']}"
    main_data.append(rec)

main_data.sort(key=lambda x: x["nr_skanu"])

with open('/home/ubuntu/workspace/Gen/main_data_j20_part4.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j20_part4.json: {len(main_data)} skanow")
