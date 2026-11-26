# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j17_part30.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801'

part31_scans = [
    {
        "nr_skanu": 751,
        "numer_pozycji": "Poz. 751",
        "strona_pagina": "fol. 368r (dolna 345)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Dekrety i inkwizycje / Dylacja Kazimierza Młynarskiego przeciw Marcinowi Morelowi i Antoniemu Okoniowi oraz interogatoria z zeznaniem Jadwigi Potokowiczowej (1758 r.)",
        "osoby_podmioty": "Kazimierz Młynarski [Młynarski]; Marcin Morel [Morel] asesor kraśnicki; Antoni Okoń [Okoń]; Jadwiga Potokowiczowa [Potokowiczowa]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "(1) Dylacja w sprawie Kazimierza Młynarskiego przeciw Marcinowi Morelowi i Antoniemu Okoniowi z powodu niestawiennictwa pozwanego Okonia; (2) `Interrogatoryia` z powództwa Kazimierza Młynarskiego przeciw asesorowi Marcinowi Morelowi i Antoniemu Okoniowi — zeznaje uczciwa Jadwiga Potokowiczowa mężatka o kłótni o niwkę w gospodzie i przyjściu gniewnego Okonia.",
        "transkrypcja": (
            "[fol. 368r, dolna numeracja 345]\n"
            "kompartyi tak obducti wyprowadzoney iako y jnkwizycyi de moschowanych [?] "
            "ponieważ Sławetny Antoni Okoń był pozwany od aktora do finalnego dekretu "
            "nie stanoł przetoż strona aktorska sprawę zawiesza dla absencyi pozwanego "
            "który się nie opowiedział w czym Sąd nasz dylacyią z urzędu do następuiącey "
            "prawney kadencyi daie.\n"
            "Sub eodem actu\n"
            "Interrogatoryia ex Parte Honesti Casimieri Młynarski Civ. Cras. Contra "
            "Famatum Martinum Morel Assessorem Cras. et Famatum Antonium Okoń Civ. Cras.\n"
            "Testis 1ma Honesta Hedvigis Potokowiczowa Mężatka Jurata zeznała "
            "jako będąc w gospodzie słyszała iak Sławet. Marcin Morel z Kazimierzem "
            "Młynarskim kłócili się o niwkę w tym przyszedłszy Sławet. Antoni Okoń "
            "gniewny y mowił do Młynarskiego..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 752,
        "numer_pozycji": "Poz. 752",
        "strona_pagina": "fol. 368v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Inkwizycje i dekrety / Dokończenie zeznań Jadwigi Potokowiczowej o bójce z udziałem Morelowej i psa oraz dekret zaoczny Matyasza Deuki przeciw Matyaszowi Łyżikowi (1758 r.)",
        "osoby_podmioty": "Jadwiga Potokowiczowa [Potokowiczowa]; Antoni Okoń [Okoń]; Kazimierz Młynarski [Młynarski]; Marcin Morel [Morel]; Marcinowa Morelowa [Morelowa]; Matyasz Deuka [Deuka]; Matyasz Łyżik [Łyżik]",
        "kwoty_podatki": "grzywny sądowi per medium",
        "opis_sprawy": "(1) Dokończenie zeznań Jadwigi Potokowiczowej: Antoni Okoń trzymał pieniądze w garści i wyzywał Młynarskiego, po czym Marcinowa Morelowa pchnęła Młynarskiego i sama upadła aż jej czepiec spadł, Morel z żoną bili Młynarskiego, a pies go gryzł, podczas gdy Okoń stał z boku i nie bił; (2) dekret zaoczny w sprawie Matyasza Deuki przeciw Matyaszowi Łyżikowi (grzywny sądowi per medium i więzienie).",
        "transkrypcja": (
            "[fol. 368v]\n"
            "y trzymaiąc w garści pieniądze mowił mam pieniądze psie a zatym Sławetna "
            "Marcinowa Morelowa pchnęła Młynarskiego y sama upadła aż iey czepiec "
            "spadł w tym oboie Morel z żoną bili tegoż Młynarskiego y pies ieszcze "
            "gryzł Młynarskiego a Antoni Okoń stoiąc na boku nie bił tylko mowił "
            "jako wyżey.\n"
            "Sub eodem actu\n"
            "W sprawie przez uciwego Matyasza Deuki aktora sprawy rzędney a pozwanego "
            "uciwego Matyasza Łyżika o pobicie y kalumnią ponieważ pozwany Matyasz "
            "Łyżik na terminie dzisieyszym nie stanoł ani przyczyny niestania swego "
            "nie opowiedział przetoż Sąd nasz zaocznie skazuie ażeby pozwany za "
            "niestawienie się dał grzywien sądowi per medium y do więzienia..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 753,
        "numer_pozycji": "Poz. 753",
        "strona_pagina": "fol. 369r (dolna 346)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Dekrety, dylacje i manifestacje / Dokończenie dekretu Deuki z Łyżikiem, wyrok Sebestyana Grzętki przeciw Marcinowi Kotłunowi, dylacja Tomasza Bednarza z Lewkiem oraz manifestacja Sebestyana Pawlickiego przeciw Ciurkom (1758 r.)",
        "osoby_podmioty": "Matyasz Deuka [Deuka]; Matyasz Łyżik [Łyżik]; Sebestyan Grzętka [Grzętka]; Marcin Kotłun [Kotłun]; Tomasz Bednarz [Bednarz]; Lewek [Lewek / Lawka?]; Sebestyan Pawlicki [Pawlicki]; Jan Ciurka [Ciurka]; Grzegorz Ciurka [Ciurka]; Wojciech Ciurka [Ciurka]",
        "kwoty_podatki": "grzywien 2 sądowi per medium",
        "opis_sprawy": "(1) Dokończenie dekretu Matyasza Deuki z Matyaszem Łyżikiem; (2) wyrok zaoczny w sprawie Sebestyana Grzętki przeciw Marcinowi Kotłunowi (2 grzywny sądowi per medium); (3) dylacja w sprawie Tomasza Bednarza mieszczanina kraśnickiego przeciw Lewkowi [Lawce?] o dekret; (4) `Feryia Secunda ante Festum Sancti Martini Pontificis Proxima 1758 anno`: początek manifestacji Sebestyana Pawlickiego przeciw Janowi Ciurce i synom jego Grzegorzowi i Wojciechowi.",
        "transkrypcja": (
            "[fol. 369r, dolna numeracja 346]\n"
            "poszedł aż do zaspokoienia strony aktorskiey y sądu.\n"
            "Sub eodem actu\n"
            "W sprawie przez uciwego Sebestyana Grzętki aktora sprawy rzędney a pozwanego "
            "uciwego Marcina Kotłuna o niesłuszne pobicie ponieważ pozwany nie stanoł "
            "przetoż Sąd nasz zaocznie skazuie na grzywien dwie sądowi per medium.\n"
            "Sub eodem actu\n"
            "W sprawie przez uciwego Tomasza Bednarza mieszczanina krasnickiego aktora "
            "a pozwanego niewiernego Lewka [Lawki?] o dekret Sąd nasz dylacyią daie "
            "do następuiącego terminu.\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasn: Feryia Secunda "
            "ante Festum Sancti Martini Pontificis Proxima 1758 anno\n"
            "Przed urzędem y aktami ninieyszemi WŁ. stanowszy Personaliter uciwy "
            "Sebestyan Pawlicki mieszczanin krasnicki solennie manifestował się przeciw "
            "uciwego Jana Ciurki y synów iego Grzegorza [?] y Woyciecha..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 754,
        "numer_pozycji": "Poz. 754",
        "strona_pagina": "fol. 369v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Manifestacje i areszty / Dokończenie manifestacji Sebestyana Pawlickiego przeciw Ciurkom o sprzedaż kwatery pola za Grzegorzką, areszt Chaima Markowicza na żonę oraz początek wizji Piurkowskiego i Kotłuna (dublet 754–755, 1758 r.)",
        "osoby_podmioty": "Sebestyan Pawlicki [Pawlicki]; Jan Ciurka [Ciurka]; Grzegorz Ciurka [Ciurka]; Wojciech Ciurka [Ciurka]; Chaim Markowicz [Markowicz]; Marszałek [JW Imć Pan Marszałek]; Sebestyan Piurkowski [Piurkowski]; Antoni Kotłun [Kotłun]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "Skan #754 (pierwsza kopia dubletu mikrofilmowego 754–755, fol. 369v): (1) dokończenie manifestacji Sebestyana Pawlickiego przeciw Janowi, Grzegorzowi i Wojciechowi Ciurkom przedmieszczanom kraśnickim o potajemną sprzedaż kwatery pola za Grzegorzką bez wiedzy manifestanta, zięcia i dzieci, z położeniem aresztu na pieniądze u szwagra; (2) areszt położony przez starozakonnego Chaima Markowicza, aby jego żona nie wyjeżdżała przed rozprawą z mężem przed JW Imć Panem Marszałkiem; (3) `Feryia Secunda ante Festum Sancti Martini Pontificis Proxima 1758 Anno`: początek zeznania wizji Sebestyana Piurkowskiego i Antoniego Kotłuna.",
        "transkrypcja": (
            "[fol. 369v — dublet mikrofilmowy skanów 754 i 755]\n"
            "przedmieszczanów krasnickich oto iż oni bez wiadomości manifestanta, zięcia "
            "y dzieci kwaterę pola za Grzegorzką leżącą sprzedali y pieniądze wzięli "
            "przetoż manifestant kładzie areszt na te pieniądze u szwagra swego aby "
            "nikomu nie były wydane aż do rozsądzenia sprawy.\n"
            "Sub eodem actu\n"
            "Areszt położony przez starozakonnego Chaima Markowicza ażeby żona iego "
            "z miasta nie wyieżdżała przed rozprawą z mężem swoim od JW Imć Pana Marszałka.\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasn: Feryia Secunda "
            "ante Festum Sancti Martini Pontificis Proxima 1758 Anno\n"
            "Zeznanie wizyi przez uciwego Sebestyana Piurkowskiego y Antoniego Kotłuna..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 755,
        "numer_pozycji": "Poz. 755",
        "strona_pagina": "fol. 369v (dublet)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Manifestacje i areszty / Druga kopia mikrofilmowa karty fol. 369v: manifestacja Pawlickiego przeciw Ciurkom, areszt Chaima Markowicza oraz wizja Piurkowskiego i Kotłuna (dublet 754–755, 1758 r.)",
        "osoby_podmioty": "Sebestyan Pawlicki [Pawlicki]; Jan Ciurka [Ciurka]; Grzegorz Ciurka [Ciurka]; Wojciech Ciurka [Ciurka]; Chaim Markowicz [Markowicz]; Marszałek [JW Imć Pan Marszałek]; Sebestyan Piurkowski [Piurkowski]; Antoni Kotłun [Kotłun]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "Skan #755 (druga kopia dubletu mikrofilmowego 754–755, ta sama karta fol. 369v): (1) dokończenie manifestacji Sebestyana Pawlickiego przeciw Janowi, Grzegorzowi i Wojciechowi Ciurkom o sprzedaż kwatery pola za Grzegorzką; (2) areszt Chaima Markowicza przeciw żonie przed rozprawą u JW Imć Pana Marszałka; (3) początek zeznania wizji Sebestyana Piurkowskiego i Antoniego Kotłuna.",
        "transkrypcja": (
            "[fol. 369v — druga kopia dubletu mikrofilmowego skanów 754 i 755]\n"
            "przedmieszczanów krasnickich oto iż oni bez wiadomości manifestanta, zięcia "
            "y dzieci kwaterę pola za Grzegorzką leżącą sprzedali y pieniądze wzięli "
            "przetoż manifestant kładzie areszt na te pieniądze u szwagra swego aby "
            "nikomu nie były wydane aż do rozsądzenia sprawy.\n"
            "Sub eodem actu\n"
            "Areszt położony przez starozakonnego Chaima Markowicza ażeby żona iego "
            "z miasta nie wyieżdżała przed rozprawą z mężem swoim od JW Imć Pana Marszałka.\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasn: Feryia Secunda "
            "ante Festum Sancti Martini Pontificis Proxima 1758 Anno\n"
            "Zeznanie wizyi przez uciwego Sebestyana Piurkowskiego y Antoniego Kotłuna..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 756,
        "numer_pozycji": "Poz. 756",
        "strona_pagina": "fol. 370r (dolna 347)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Wizje, inkwizycje i dekrety / Dokończenie wizji szkody w tatarce przez Andrzeja Kratkowskiego i Antoniego Potokowicza, zeznanie Józefa Laski w sprawie Grzętki przeciw Kotłunowi oraz początek dekretu (1758 r.)",
        "osoby_podmioty": "Andrzej Kratkowski [Kratkowski] exaktor miejski; Antoni Potokowicz [Potokowicz]; Sebestyan Piurkowski [Piurkowski]; Antoni Kotłun [Kotłun]; Sebestyan Grzętka [Grzętka]; Marcin Kotłun [Kotłun]; Józef Laska [Laska]",
        "kwoty_podatki": "15 snopów tatarki (u Piurkowskiego); 15 snopów tatarki (u Kotłuna)",
        "opis_sprawy": "(1) Dokończenie zeznania wizji przez Andrzeja Kratkowskiego exaktora miejskiego i Antoniego Potokowicza mieszczanina kraśnickiego o szkodzie w tatarce po 15 snopów u Sebestyana Piurkowskiego i Antoniego Kotłuna; (2) `Interrogatoryia` z powództwa Sebestyana Grzętki przeciw Marcinowi Kotłunowi przedmieszczaninowi kraśnickiemu — zeznaje Józef Laska o wykopaniu kopaniny i zaoraniu jej przez dwa lata; (3) początek dekretu Grzętki przeciw Kotłunowi (odesłanie do przyjaciół).",
        "transkrypcja": (
            "[fol. 370r, dolna numeracja 347]\n"
            "przez Sławetnego Andrzeia Kratkowskiego Exaktora Mieyskiego Krasn. y "
            "Antoniego Potokowicza Mieszczanina Krasn. zeznali iż szkody w tatarce "
            "u Sebestyana Piurkowskiego snopów piętnaście y u Antoniego Kotłuna także "
            "snopów piętnaście znależli.\n"
            "Sub eodem actu\n"
            "Interrogatoryia ex Parte Honesti Sobestyani Grzętka Contra Honestum "
            "Martinum Kotłun anteopidanum Cras.\n"
            "Testis Józef Laska przedmieszczanin zeznał iż widział kopaninę wykopaną "
            "ktorą Marcin Kotłun przez lat dwie zaorywał y użytkował.\n"
            "Sub eodem actu\n"
            "W sprawie przez uciwego Sebestyana Grzętki przeciw Marcinowi Kotłunowi "
            "Sąd nasz odsyła strony do przyjaciół na ugodę..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 757,
        "numer_pozycji": "Poz. 757",
        "strona_pagina": "fol. 370v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Dekrety i dylacje / Dokończenie dylacji Grzętki z Kotłunem, wyrok żydowskiego rzeźnika Ahla przeciw kowalowi Jędrzejowi Małeckiemu o topór oraz dylacja ławnika Szymona Krzeszowskiego przeciw Antoniemu Kaweckiemu (1758 r.)",
        "osoby_podmioty": "Sebestyan Grzętka [Grzętka]; Marcin Kotłun [Kotłun]; Ahel [Ahel / Aron? / Anzelm?] rzeźnik; Jędrzej Małecki [Małecki / Maiecki?] kowal; Szymon Krzeszowski [Krzeszowski] ławnik kraśnicki; Antoni Kawecki [Kawecki]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "(1) Dokończenie dylacji w sprawie Grzętki przeciw Kotłunowi; (2) wyrok w sprawie niewiernego Ahla [Arona? / Anzelma?] rzeźnika obywatela kraśnickiego przeciw Jędrzejowi Małeckiemu [Maieckiemu?] kunsztu kowalskiego o topór oddany do reparacji — pozwany ma topór naprawić i oddać bez zapłaty za robotę, a strony mają stawić świadków o pobicie i kalumnię; (3) dylacja ławnika Szymona Krzeszowskiego przeciw Antoniemu Kaweckiemu o potrącenie żony w młynie.",
        "transkrypcja": (
            "[fol. 370v]\n"
            "na terminie następuiącym.\n"
            "Sub eodem actu\n"
            "W sprawie przez niewiernego Ahla [Arona? / Anzelma?] Rzeźnika obywatela "
            "krasnickiego aktora a pozwanego uciwego Jędrzeia Małeckiego [Maieckiego?] "
            "kunsztu kowalskiego o topór dany do reparacyi y o pobicie tudzież kalumnią "
            "Sąd nasz nakazuie ażeby pozwany topór zreparował y oddał aktorowi bez "
            "zapłaty za robotę zaś względem pobicia y kalumnii obie strony maią stawić "
            "świadków na następuiącym terminie.\n"
            "Sub eodem actu\n"
            "W sprawie przez Sławetnego Szymona Krzeszowskiego Ławnika krasnickiego "
            "przeciw Antoniemu Kaweckiemu mieszczaninowi krasnickiemu o potrącenie "
            "żony w młynie Sąd nasz dylacyią daie..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 758,
        "numer_pozycji": "Poz. 758",
        "strona_pagina": "fol. 371r (dolna 348)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Dylacje i inkwizycje / Dokończenie dylacji Krzeszowskiego z Kaweckim oraz zeznania Kazimierza Młynarskiego i rajcy Łukasza Krzeszowskiego w sprawie ławnika Antoniego Pilińskiego przeciw Marcinowi Morelowi (1758 r.)",
        "osoby_podmioty": "Szymon Krzeszowski [Krzeszowski]; Antoni Kawecki [Kawecki]; Antoni Piliński [Piliński] ławnik kraśnicki; Marcin Morel [Morel] asesor; Kazimierz Młynarski [Młynarski]; Antoni Pilaszkiewicz [Pilaszkiewicz]; Łukasz Krzeszowski [Krzeszowski] rajca; Frankiewiczowa [Frankiewiczowa]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "(1) Dokończenie dylacji Szymona Krzeszowskiego z Antonim Kaweckim; (2) `Interrogatoryia` z powództwa ławnika Antoniego Pilińskiego przeciw Marcinowi Morelowi — zeznaje Sławetny Kazimierz Młynarski o kłótni Morela z Pilińskim („żebyś siedział pod ławą z tym pismem i kartem z Antonim Pilaszkiewiczem”); (3) dylacja Pilińskiego przeciw Morelowi i Młynarskiemu; (4) `Interrogatoryia` Antoniego Pilińskiego przeciw Morelowi — zeznaje rajca Łukasz Krzeszowski o słowach Morela o koniarzu i hipińskiej niwce P. Frankiewiczowej.",
        "transkrypcja": (
            "[fol. 371r, dolna numeracja 348]\n"
            "do dalszey rozprawy.\n"
            "Sub eodem actu\n"
            "Interrogatoryia ex Parte Famati Antonii Piliński Scab. Cras. Contra Famatum "
            "Martinum Morel Civ. Cras. et Assessorem\n"
            "Testis Famatus Casimirus Młynarski zeznał iż słyszał iak Morel mowił do "
            "Pilińskiego żebyś siedział pod ławą z tym pismem y kartem z Antonim "
            "Pilaszkiewiczem.\n"
            "Sub eodem actu\n"
            "Dylacyia w sprawie Antoniego Pilińskiego przeciw Marcinowi Morelowi y "
            "Kazimierzowi Młynarskiemu.\n"
            "Sub eodem actu\n"
            "Interrogatoryia ex Parte Famati Antonii Piliński Scab. Crasn. Contra "
            "Famatum Martinum Morel\n"
            "Testis Famatus Lucas Krzeszowski Consul Cras. zeznał iż słyszał iak "
            "Morel mowił ty koniarzu lepszy byś hipińską niwkę odebrał P. Frankiewiczowey "
            "iakiey który nie dostaniesz..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 759,
        "numer_pozycji": "Poz. 759",
        "strona_pagina": "fol. 371v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Inkwizycje / Dokończenie zeznań rajcy Łukasza Krzeszowskiego oraz zeznanie ławnika Jana Szubertowskiego w sprawie Antoniego Pilińskiego przeciw Marcinowi Morelowi (1758 r.)",
        "osoby_podmioty": "Łukasz Krzeszowski [Krzeszowski] rajca; Marcin Morel [Morel]; Marcinowa Morelowa [Morelowa]; Antoni Piliński [Piliński] ławnik; Kazimierz Młynarski [Młynarski]; Jan Szubertowski [Szubertowski] ławnik kraśnicki",
        "kwoty_podatki": "brak",
        "opis_sprawy": "(1) Dokończenie zeznań rajcy Łukasza Krzeszowskiego: Morel wyzywał („psie bracie”), Piliński bronił Młynarskiego, Morel i Młynarski skakali do siebie, a żona Morela pchnęła Młynarskiego; (2) zeznanie drugiego świadka, ławnika kraśnickiego Jana Szubertowskiego, potwierdzające wymawianie niwki Młynarskiemu i ratowanie go przez Pilińskiego.",
        "transkrypcja": (
            "[fol. 371v]\n"
            "y mowił do tegoż psie bracie a Piliński ratował Młynarskiego y bronił "
            "żeby się nie bili kiedy Morel y Młynarski skakali do siebie zaś żona "
            "Morela pchnęła Młynarskiego.\n"
            "Testis 2dus Famatus Joannes Szubertowski Scabinus Crasn: zeznał iako "
            "słyszał gdy Morel wymawiał Młynarskiemu niwkę y mowił niegodziwe słowa "
            "a Piliński ratował Młynarskiego y bronił go razem..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 760,
        "numer_pozycji": "Poz. 760",
        "strona_pagina": "fol. 372r (dolna 349)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Inkwizycje i dekrety / Dokończenie zeznań Jana Szubertowskiego oraz dekret w sprawie ławnika Antoniego Pilińskiego przeciw deputatowi Marcinowi Morelowi o zadanie kradzieży na jarmarku (1758 r.)",
        "osoby_podmioty": "Jan Szubertowski [Szubertowski] ławnik; Łukasz Krzeszowski [Krzeszowski] rajca; Antoni Piliński [Piliński] ławnik kraśnicki; Marcin Morel [Morel] deputat",
        "kwoty_podatki": "grzywien 2 aktorowi, sądowi per medium",
        "opis_sprawy": "(1) Dokończenie zeznań ławnika Jana Szubertowskiego (bronił razem z Łukaszem Krzeszowskim); (2) dekret w sprawie ławnika Antoniego Pilińskiego przeciw deputatowi Marcinowi Morelowi o zadanie kradzieży na jarmarku — pozwany ma dać aktorowi 2 grzywny, sądowi per medium, przeprosić i iść na dobrowolne więzienie.",
        "transkrypcja": (
            "[fol. 372r, dolna numeracja 349]\n"
            "z Sławetnym Łukaszem Krzeszowskim aby do większego zgorszenia nie przyszło.\n"
            "Sub eodem actu\n"
            "W sprawie przez Sławetnego Antoniego Pilińskiego Ławnika krasnickiego "
            "aktora a pozwanego Sławetnego Marcina Morela Deputata o zadanie kradzieży "
            "na jarmarku y o zniewagę urzędu Sąd nasz nakazuie ażeby pozwany dał "
            "aktorowi grzywien dwie, sądowi per medium, aktora przeprosił y na "
            "dobrowolne więzienie..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 761,
        "numer_pozycji": "Poz. 761",
        "strona_pagina": "fol. 372v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Dekrety, apelacje i manifestacje / Apelacja Antoniego Pilińskiego od dekretu z Morelem, manifestacja Kazimierza Młynarskiego, areszt apelacji przez Pilińskiego oraz manifestacja ławników Szubertowskiego i Krzeszowskiego (dublet 761–762, 1758 r.)",
        "osoby_podmioty": "Antoni Piliński [Piliński] ławnik; Marcin Morel [Morel]; Kazimierz Młynarski [Młynarski] cechmistrz szewski; Jan Szubertowski [Szubertowski] ławnik; Szymon Krzeszowski [Krzeszowski] ławnik",
        "kwoty_podatki": "brak",
        "opis_sprawy": "Skan #761 (pierwsza kopia dubletu mikrofilmowego 761–762, fol. 372v): (1) dokończenie dekretu Pilińskiego z Morelem — aktor nie kontentował się i apelował do Najwyższego Sądu, pozwany kontentował się; (2) manifestacja cechmistrza szewskiego Kazimierza Młynarskiego przeciw Marcinowi Morelowi o obelgę („ty koniarzu, tyś siedem wieprzków skrzywdził”); (3) areszt apelacji Marcina Morela przez Antoniego Pilińskiego; (4) manifestacja ławników Jana Szubertowskiego i Szymona Krzeszowskiego przeciw Morelowi o zarzut niesłuszności przy obdukcji Młynarskiego.",
        "transkrypcja": (
            "[fol. 372v — dublet mikrofilmowy skanów 761 i 762]\n"
            "poszedł, którym to dekretem strona aktorska nie kontentowała się y "
            "apelowała do naywyższego Sądu zaś pozwany kontentował się.\n"
            "Sub eodem actu\n"
            "Manifestacyia Sławetnego Kazimierza Młynarskiego Cechmistrza Szewskiego "
            "przeciw Sławetnemu Marcinowi Morelowi o zadanie mu obelgi słowy ty koniarzu "
            "tyś siedem wieprzków skrzywdził.\n"
            "Sub eodem actu\n"
            "Areszt apelacyi Marcina Morela położony przez Antoniego Pilińskiego.\n"
            "Sub eodem actu\n"
            "Manifestacyia Sławetnych Jana Szubertowskiego y Szymona Krzeszowskiego "
            "Ławników krasnickich przeciw Marcinowi Morelowi iż tenże zarzucał im "
            "niesłuszność przy obdukcyi Kazimierza Młynarskiego..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 762,
        "numer_pozycji": "Poz. 762",
        "strona_pagina": "fol. 372v (dublet)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Dekrety, apelacje i manifestacje / Druga kopia mikrofilmowa karty fol. 372v: apelacja Pilińskiego, manifestacja Młynarskiego, areszt apelacji Morela oraz manifestacja Szubertowskiego i Krzeszowskiego (dublet 761–762, 1758 r.)",
        "osoby_podmioty": "Antoni Piliński [Piliński] ławnik; Marcin Morel [Morel]; Kazimierz Młynarski [Młynarski] cechmistrz szewski; Jan Szubertowski [Szubertowski] ławnik; Szymon Krzeszowski [Krzeszowski] ławnik",
        "kwoty_podatki": "brak",
        "opis_sprawy": "Skan #762 (druga kopia dubletu mikrofilmowego 761–762, ta sama karta fol. 372v): (1) apelacja Antoniego Pilińskiego do Najwyższego Sądu od dekretu z Marcinem Morelem; (2) manifestacja Kazimierza Młynarskiego przeciw Morelowi; (3) areszt apelacji Morela; (4) manifestacja ławników Jana Szubertowskiego i Szymona Krzeszowskiego przeciw Morelowi.",
        "transkrypcja": (
            "[fol. 372v — druga kopia dubletu mikrofilmowego skanów 761 i 762]\n"
            "poszedł, którym to dekretem strona aktorska nie kontentowała się y "
            "apelowała do naywyższego Sądu zaś pozwany kontentował się.\n"
            "Sub eodem actu\n"
            "Manifestacyia Sławetnego Kazimierza Młynarskiego Cechmistrza Szewskiego "
            "przeciw Sławetnemu Marcinowi Morelowi o zadanie mu obelgi słowy ty koniarzu "
            "tyś siedem wieprzków skrzywdził.\n"
            "Sub eodem actu\n"
            "Areszt apelacyi Marcina Morela położony przez Antoniego Pilińskiego.\n"
            "Sub eodem actu\n"
            "Manifestacyia Sławetnych Jana Szubertowskiego y Szymona Krzeszowskiego "
            "Ławników krasnickich przeciw Marcinowi Morelowi iż tenże zarzucał im "
            "niesłuszność przy obdukcyi Kazimierza Młynarskiego..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 763,
        "numer_pozycji": "Poz. 763",
        "strona_pagina": "fol. 373r (dolna 350)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Areszty, wizje i dekrety / Dokończenie manifestacji ławników, areszt na Jana Ciurkę w stodole Bartłomieja Zdybła, wizja 50 snopów tatarki, zeznanie Mikołaja Milewskiego przeciw Bednarzowi i początek dekretu Młynarskiego z Morelem (1758 r.)",
        "osoby_podmioty": "Jan Szubertowski [Szubertowski]; Szymon Krzeszowski [Krzeszowski]; Sebastian Pawlicki [Pawlicki]; Józef Nowak [Nowak]; Jan Ciurka [Ciurka]; Bartłomiej Zdybeł [Zdybeł]; Antoni Piliński [Piliński]; Matyasz Łapka [Łapka]; Kazimierz Tomkowski [Tomkowski]; Sebestyan Piurkowski [Piurkowski]; Mikołaj Milewski [Milewski / Miliski?]; Tomasz Bednarz [Bednarz]; Kazimierz Młynarski [Młynarski]; Marcin Morel [Morel]; Antoni Okoń [Okoń]",
        "kwoty_podatki": "50 snopów tatarki",
        "opis_sprawy": "(1) Dokończenie manifestacji Szubertowskiego i Krzeszowskiego; (2) areszt Sebestyana Pawlickiego i Józefa Nowaka na Jana Ciurkę w stodole Bartłomieja Zdybła; (3) zeznanie wizji Antoniego Pilińskiego i Matyasza Łapki w sprawie Kazimierza Tomkowskiego i Sebestyana Piurkowskiego (50 snopów tatarki szkody); (4) zeznanie Mikołaja Milewskiego [Miliskiego?] przeciw Tomaszowi Bednarzowi o kwartę okowity, spódnicę czarną i wypędzenie z Piątkowizny; (5) początek dekretu Kazimierza Młynarskiego przeciw Marcinowi Morelowi i Antoniemu Okoniowi.",
        "transkrypcja": (
            "[fol. 373r, dolna numeracja 350]\n"
            "przed urzędem naszym o co iterum manifestantur.\n"
            "Sub eodem actu\n"
            "Areszt położony przez uciwych Sebestyana Pawlickiego y Józefa Nowaka na "
            "Jana Ciurkę w stodole u Bartłomieia Zdybła.\n"
            "Sub eodem actu\n"
            "Zeznanie wizyi przez Sławetnego Antoniego Pilińskiego y Matyasza Łapkę "
            "w sprawie Kazimierza Tomkowskiego y Sebestyana Piurkowskiego iż szkody "
            "w tatarce snopów pięćdziesiąt znaleziono.\n"
            "Sub eodem actu\n"
            "Zeznanie uciwego Mikołaia Milewskiego [Miliskiego?] przeciw Tomaszowi "
            "Bednarzowi o kwartę okowity, spódnicę czarną y wypędzenie z Piątkowizny.\n"
            "Sub eodem actu\n"
            "W sprawie przez uciwego Kazimierza Młynarskiego aktora przeciwko "
            "Sławetnym Marcinowi Morelowi y Antoniemu Okoniowi..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 764,
        "numer_pozycji": "Poz. 764",
        "strona_pagina": "fol. 373v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Dekrety i dylacje / Dokończenie dekretu Kazimierza Młynarskiego przeciw Morelowi i Okoniowi oraz dylacja w sprawie Pawlickiego i Nowaka przeciw Ciurkom i Grzętce o pole za Grzegorzką (1758 r.)",
        "osoby_podmioty": "Marcin Morel [Morel] deputat kraśnicki; Antoni Okoń [Okoń]; Kazimierz Młynarski [Młynarski]; Sebastian Pawlicki [Pawlicki]; Józef Nowak [Nowak]; Jan Ciurka [Ciurka]; Wojciech Ciurka [Ciurka]; Grzegorz Grzętka [Grzętka]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "(1) Dokończenie dekretu w sprawie Kazimierza Młynarskiego przeciw deputatowi Marcinowi Morelowi i Antoniemu Okoniowi (ponieważ Okoń nie stanął na termin do przysięgi i nie okazał dowodów, sąd daje dylację na dzień jutrzejszy bez przymuszania stron do ekspensów prawnych); (2) dylacja w sprawie uczciwych Sebestyana Pawlickiego i Józefa Nowaka przeciw Janowi Ciurce oraz jego synowi Wojciechowi i Grzegorzowi Grzętce o kwaterę pola za Grzegorzką z budynkami.",
        "transkrypcja": (
            "[fol. 373v]\n"
            "Sławet. Marcina Morela Deputt. krasn: a że obwiniony Antoni Okoń iest "
            "w komparyi tak obducyi wyprowadzoney iako y w jnkwizycyi de moschowanych [?], "
            "ponieważ był pozwany od aktora do finalnego dekretu nie stanoł przeto "
            "tego sprawa zaczęta skutku otrzymać nie może tudzież ktorzy na jnkwizycyie "
            "byli pozwani lubo zeznali, lecz dnia dzisieyszego na termin nie stanęli "
            "do przysięgi nie stanęli. W ktorey racji sąd nasz obopulny dla rożnych "
            "circumstancyj daie Dylacyią na dzień jutrzeyszy ażeby obie strony ze "
            "wszelkiemi stawali dokumentami tak na dowod iako na odwod y oczyście bez "
            "porusza wali na termin następuiący ażeby sąd nasz więcey nad to spraw "
            "nie mitrężył y strony do ekspensow prawnych nie przyprowadzalisz.\n"
            "Sub eodem actu\n"
            "W sprawie przez uciwych Sebestyana Pawlickiego Józefa Nowaka aktorow "
            "sprawy rzędney a pozwanych Jana Ciurki Woyciecha syna iego Grzegorza "
            "Grzętki z racyi różnych pretensyi aktorow tudzież że aktor miał od pozwanego "
            "Jana Ciurki że nie komu jnszemu tylko temu Sobestyanowi obiecał spuścić "
            "kwaterę pola z pobudynkami, w ktory materyi Jan Ciurka [nadpisane: z rąde "
            "Grzętki złożył?] torowi, y do niesłusznych przyprowadził terminow. Sąd "
            "nasz ninieyszy obopulny zwazywszy między stronami kontrowersyie nakazuie "
            "ażeby pozwany Grzegorz Grzętka y Woyciech syn iego sądowi naszemu byca "
            "stawili a aktor patrzył bydź pokiey w possessyi pokiey między..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 765,
        "numer_pozycji": "Poz. 765",
        "strona_pagina": "fol. 374r (dolna 351)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Dylacje i dekrety / Dokończenie dylacji Pawlickiego i Nowaka, dylacja Krystyny Potokowiczowej przeciw Antoniemu Fryczakowi o masło i skrzynkę oraz dekret Sebestyana Piurkowskiego przeciw Antoniemu Kotłunowi o spasienie tatarki (dublet 765–766, 1758 r.)",
        "osoby_podmioty": "Sebastian Pawlicki [Pawlicki]; Józef Nowak [Nowak]; Krystyna Potokowiczowa [Potokowiczowa]; Antoni Fryczak [Fryczak / Frycrak?]; Sebestyan Piurkowski [Piurkowski]; Antoni Kotłun [Kotłun]",
        "kwoty_podatki": "złotych 15 groszy 8; tatarki snopów 20; grzywny 2 aktorowi, sądowi per medium",
        "opis_sprawy": "Skan #765 (pierwsza kopia dubletu mikrofilmowego 765–766, fol. 374r): (1) dokończenie dylacji w sprawie Pawlickiego i Nowaka na dzień jutrzejszy; (2) dylacja w sprawie uczciwej Krystyny Potokowiczowej przeciw uczciwemu Antoniemu Fryczakowi [Frycrakowi?] o masło, krochmal, konopie i zaginioną skrzynkę siostry z zegarinkiem wartości 15 złp 8 gr; (3) wyrok w sprawie uczciwego Sebestyana Piurkowskiego przeciw Antoniemu Kotłunowi mieszczaninowi kraśnickiemu o spasienie tatarki — pozwany ma oddać 20 snopów tatarki, zapłacić koszta i 2 grzywny, sądowi per medium i iść na dobrowolne więzienie.",
        "transkrypcja": (
            "[fol. 374r, dolna numeracja 351 — dublet mikrofilmowy skanów 765 i 766]\n"
            "tymiż stronami Sąd nasz nie uczyni statek y do tey akcyi nie przyprowadzi, "
            "y dlatego Dylacyia staneła na dzień jutrzeyszy ażeby obie strony bez "
            "pozwu stawały na termin następuiący.\n"
            "Sub eodem actu\n"
            "W sprawie przez uciwey Krystyny Potokowiczowey mężatki aktorki sprawy "
            "rzędney a pozwanego uciwego Antoniego Frycraka [Fryczaka?] Ph: z drugą "
            "strony z racji masła maku krochmalu konopi ktorzy ze zginęła skrzynki "
            "aktorki siostry iako się aktorka skarżyła przed sądem naszym zegarinuch [?] "
            "masła valoris byt złotych 15 groszy 8. Sąd nasz ninieyszy obopulny zwazywszy "
            "między stronami kontrowersyie a że aktorka publicco zadała że pozwanego "
            "żona zadała że miała schowanie masła y jnne rzeczy nakazuie ażeby "
            "pozwanego żona odwiodła się dokumentami lepsnemi y dlatego na dzień "
            "jutrzeyszy daie Dylacyią, y obie strony bez pozwu stawali na terminie "
            "następuiącym.\n"
            "Sub eodem actu\n"
            "W sprawie przez uciwego Sebestyana Piurkowskiego aktora sprawy rzędney "
            "a pozwanego uciwego Antoniego Kotłuna Mieszcz. krasn: z drugiey strony "
            "racyionem spasienia tatarki aktorowey o ktorą się skarżył aktor na "
            "pozwanego. Sąd nasz ninieyszy obopulny zwazywszy wszelkie circumstancyie "
            "nakazuie ażeby pozwany jnstantanea oddał aktorowi tatarki snopow 20 "
            "y zaprawione koszta grzywien dwie, sądowi per medium po przeczytaniu "
            "dekretu pozwany ma puiść na dobrowolne więzienie y posiedzieć tyle poki "
            "strony y sąd nie uspokoy."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 766,
        "numer_pozycji": "Poz. 766",
        "strona_pagina": "fol. 374r (dublet)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Dylacje i dekrety / Druga kopia mikrofilmowa karty fol. 374r: dylacja Pawlickiego i Nowaka, sprawa Potokowiczowej z Fryczakiem oraz dekret Piurkowskiego przeciw Kotłunowi o 20 snopów tatarki (dublet 765–766, 1758 r.)",
        "osoby_podmioty": "Sebastian Pawlicki [Pawlicki]; Józef Nowak [Nowak]; Krystyna Potokowiczowa [Potokowiczowa]; Antoni Fryczak [Fryczak / Frycrak?]; Sebestyan Piurkowski [Piurkowski]; Antoni Kotłun [Kotłun]",
        "kwoty_podatki": "złotych 15 groszy 8; tatarki snopów 20; grzywny 2 aktorowi, sądowi per medium",
        "opis_sprawy": "Skan #766 (druga kopia dubletu mikrofilmowego 765–766, ta sama karta fol. 374r): (1) dokończenie dylacji Pawlickiego i Nowaka; (2) dylacja w sprawie Krystyny Potokowiczowej przeciw Antoniemu Fryczakowi [Frycrakowi?] o masło i skrzynkę; (3) dekret Sebestyana Piurkowskiego przeciw Antoniemu Kotłunowi o spasienie 20 snopów tatarki.",
        "transkrypcja": (
            "[fol. 374r — druga kopia dubletu mikrofilmowego skanów 765 i 766]\n"
            "tymiż stronami Sąd nasz nie uczyni statek y do tey akcyi nie przyprowadzi, "
            "y dlatego Dylacyia staneła na dzień jutrzeyszy ażeby obie strony bez "
            "pozwu stawały na termin następuiący.\n"
            "Sub eodem actu\n"
            "W sprawie przez uciwey Krystyny Potokowiczowey mężatki aktorki sprawy "
            "rzędney a pozwanego uciwego Antoniego Frycraka [Fryczaka?] Ph: z drugą "
            "strony z racji masła maku krochmalu konopi ktorzy ze zginęła skrzynki "
            "aktorki siostry iako się aktorka skarżyła przed sądem naszym zegarinuch [?] "
            "masła valoris byt złotych 15 groszy 8. Sąd nasz ninieyszy obopulny zwazywszy "
            "między stronami kontrowersyie a że aktorka publicco zadała że pozwanego "
            "żona zadała że miała schowanie masła y jnne rzeczy nakazuie ażeby "
            "pozwanego żona odwiodła się dokumentami lepsnemi y dlatego na dzień "
            "jutrzeyszy daie Dylacyią, y obie strony bez pozwu stawali na terminie "
            "następuiącym.\n"
            "Sub eodem actu\n"
            "W sprawie przez uciwego Sebestyana Piurkowskiego aktora sprawy rzędney "
            "a pozwanego uciwego Antoniego Kotłuna Mieszcz. krasn: z drugiey strony "
            "racyionem spasienia tatarki aktorowey o ktorą się skarżył aktor na "
            "pozwanego. Sąd nasz ninieyszy obopulny zwazywszy wszelkie circumstancyie "
            "nakazuie ażeby pozwany jnstantanea oddał aktorowi tatarki snopow 20 "
            "y zaprawione koszta grzywien dwie, sądowi per medium po przeczytaniu "
            "dekretu pozwany ma puiść na dobrowolne więzienie y posiedzieć tyle poki "
            "strony y sąd nie uspokoy."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 767,
        "numer_pozycji": "Poz. 767",
        "strona_pagina": "fol. 374v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Donacje i rezygnacje / Wieczysta donacja Wojciecha Ciurki na kwaterę pola Ciurkowską dla szwagra Józefa Nowaka i żony jego Agnieszki z Ciurków za 15 złotych (1758 r.)",
        "osoby_podmioty": "Wojciech Ciurka [Ciurka]; Jan Ciurka [Ciurka]; Józef Nowak [Nowak]; Agnieszka Nowakowa z Ciurków [Nowakowa / Ciurkówna]; Grzegorz Piliński [Piliński] burmistrz kraśnicki; Michał Ignacy Krzywicki [Krzywicki] pisarz przysięgły",
        "kwoty_podatki": "złotych 14 (wzięte), złotych 15 (cena umówiona)",
        "opis_sprawy": "`Sub eodem actu`: Wojciech Ciurka, syn zmarłego Jana Ciurki, zeznaje wieczystą donację na kwaterę pola zwaną Ciurkowską na rzecz szwagra Józefa Nowaka i jego małżonki Agnieszki z domu Ciurków za umówioną sumę 15 złotych (z czego wziął 14 złotych), podpisując się znakiem krzyża w obecności burmistrza Grzegorza Pilińskiego i pisarza przysięgłego Michała Ignacego Krzywickiego.",
        "transkrypcja": (
            "[fol. 374v]\n"
            "Sub eodem actu\n"
            "Przed urzędem y aktami ninieyszemi WŁ. stanowszy Personaliter uciwy "
            "Woyciech Ciurka syn uciwego Jana Ciurki Ph: a szwagier uciwego Józefa "
            "Nowaka szwagier ktory ma za sobą w małżeństwie Agnieszkę de Gente "
            "Ciurkowey ktory to wyżey wyrażony Woyciech Ciurka uczynił wieczną Donacyią "
            "na kwaterę pola nazwaniem Ciurkowską y temuż uciwemu Józefowi Nowakowi "
            "y żonie iego Agnieszce w własność y w posiadanie quovis modo y na tę "
            "kwaterę wziął złotych 14 y tym się zgodził za złotych 15 na co dla "
            "lepszey wiary y wagi iako nie umieiący pisać znak krzyża świętego kładzie.\n"
            "+ Woyciech Ciurka\n"
            "Przy tey Donacyi byli Sławet. Grzegorz Piliński Bur. y Ławn. krasn.\n"
            "Dla lepszey wiary przy tym będący y piszący iako prawdziwą uczynił Donacyią "
            "ręką własną podpisuię się Michał Ignacy Krzywicki Oboyga Miasta Krasn: "
            "Prawnego Pisarz Przysięgły mp."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 768,
        "numer_pozycji": "Poz. 768",
        "strona_pagina": "fol. 375r (dolna 352)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Manifestacje i ugody / Manifestacja wdowy Katarzyny Dobrowiczowej przeciw Jakubowi Śliżewskiemu oraz początek ugody Adama Łada z Mikołajem Kawką o zasiew na kopaninie (25 VIII 1758 r.)",
        "osoby_podmioty": "Katarzyna Dobrowiczowa [Dobrowiczowa / Dobrowicowa?] wdowa; Jakub Śliżewski [Śliżewski / Śliwiński?]; Adam Ład [Ład / Łada?]; Mikołaj Kawka [Kawka]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "(1) `Feryia 6ta post Festum Sancti Bartholomaei Apostoli 1758 Anno` (25 VIII 1758 r.): manifestacja uczciwej Katarzyny Dobrowiczowej wdowy przeciw Jakubowi Śliżewskiemu i jego żonie o zelżenie niegodziwymi słowami („ty kurwo złodzieiko”) i wzywanie do sądu; (2) początek ugody nieodmiennej między Sławetnym Adamem Ładem i żoną a przedmieszczaninem Mikołajem Kawką o zasiew żyta na kopaninie bez wiedzy Adama.",
        "transkrypcja": (
            "[fol. 375r, dolna numeracja 352]\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasn: Feryia 6ta "
            "post Festum Sancti Bartholomaei Apostoli 1758 Anno\n"
            "Przed urzędem y aktami ninieyszemi WŁ. stanowszy Personaliter uciwa "
            "Katarzyna Dobrowicowa wdowa solennie y iak naysolenniey manifestowała "
            "się y protestowała przeciw uciwego Jakuba Śliżewskiego [Śliwińskiego?] "
            "y żony iego bez daney racyi manifestantki niegodziwemi słowy żona iego "
            "zelżyła mowiąc ty kurwo złodzieiko w tuteyszym mieście co się podobało "
            "tak wołała o czym manifestantka jnkwizycyiami dowodzić będzie. W czym "
            "manifestantka maiąc tak wielką krzywdę y nie czuiąc się do tego iterum "
            "atque iterum manifestatur et protestatur.\n"
            "Sub eodem actu\n"
            "Staneła zgoda nieodmienna między Sławet. Adamem Ładem Ph: z żoną "
            "y Mikołaiem Kawką przed. kras. ktorzy maiąc do siebie pretensyie z strony "
            "zasiewu żyta na kopaninie uciwego Mikołaia Kawki ktorą to zasiał Sławet: "
            "Adamowi żona jego bez wiedzy Mikołaia Kawki, a Sławet: Adama żona "
            "kazała kopaninę zasiać bez wiedzy iego, ktorzy to byli upraszeni uprosiwszy "
            "sobie przyjacioł takową między temi uczynili zgodę y rozporządzenie "
            "z uczynionemi czasy ażeby z tey kopaniny obie strony zbierali żyto pługi "
            "raz y uprawiać z zasiewu przykazali..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 769,
        "numer_pozycji": "Poz. 769",
        "strona_pagina": "fol. 375v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Ugody i dylacje / Dokończenie ugody Adama Łada z Mikołajem Kawką pod wadium 14 grzywien (świadkowie Wojciech Potokowicz i Bartłomiej Kratkowski), dylacja Katarzyny Dobrowiczowej z Jakubem Wojciechowskim oraz otwarcie sesji 28 VIII 1758 r.",
        "osoby_podmioty": "Adam Ład [Ład / Łada?]; Mikołaj Kawka [Kawka]; Wojciech Potokowicz [Potokowicz]; Bartłomiej Kratkowski [Kratkowski]; Katarzyna Dobrowiczowa [Dobrowiczowa / Dobrowicowa?]; Jakub Wojciechowski [Wojciechowski]",
        "kwoty_podatki": "wadium grzywien 14 i 3 dni więzienia",
        "opis_sprawy": "(1) Dokończenie ugody Adama Łada z Mikołajem Kawką pod wadium 14 grzywien i 3 dni więzienia, z wyznaczeniem terminu do św. Judy i zwrotu zasiewu (podpisy krzyżykiem `+ Adam Ład`, `+ Mikołaj Kawka`, świadkowie Wojciech Potokowicz i Bartłomiej Kratkowski); (2) dylacja w sprawie wdowy Katarzyny Dobrowiczowej przeciw Jakubowi Wojciechowskiemu o kalumnię przez żonę pozwanego; (3) `Feryia Secunda ante Festum Decollationis Sancti Joannis Baptistae 1758 Anno` (28 VIII 1758 r.): otwarcie protokołu.",
        "transkrypcja": (
            "[fol. 375v]\n"
            "przypadłoby oniechować alias umorzyć zaszłą z niemi żadna strona do "
            "siebie żadney nie ma pretensyi ani kłótni żadney między sobą sub vadio "
            "grzywien 14 y więzienia dni trzy na co dla lepszey wiary y uwagii iako "
            "nie umieiący pisać znak krzyża świętego kładą. Czas zaś tego pola "
            "powinien oddać Mikołay Kawka y żyta czarnego miarowi a zaś oddać "
            "powinien.\n"
            "+ Adam Ład gołombowe [?] z podpisem + Mikołay Kawka.\n"
            "Przy tey ugodzie byli Sławet. Woyciech Potokowicz y uciwy Bartłomiey "
            "Kratkowski.\n"
            "Sub eodem actu\n"
            "W sprawie przez uciwey Katarzyny Dobrowicowey wdowy aktorki a pozwanego "
            "uciwego Jakuba Woyciechowskiego z drugiey strony o kalumnią przez "
            "pozwanego żonę. Sąd ninieyszy Ph: zwazywszy między stronami kontrowersyie "
            "daie Dylacyią po niedzieli następuiącey na środę przybyć obie strony "
            "z lepsnemi stawali dokumentami tak na dowod iako y na odwod y bez pozwu "
            "stawali na terminie następuiącym.\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasn: Feryia "
            "Secunda ante Festum Decollationis Sancti Joannis Baptistae 1758 Anno\n"
            "Przed urzędem y aktami ninieyszemi WŁ."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 770,
        "numer_pozycji": "Poz. 770",
        "strona_pagina": "fol. 376r (dolna 353)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Manifestacje i obdukcje / Manifestacja szlachetnego Jana Domaniewicza przeciw Antoniemu Kotłunowi o zniewagę na gospodzie oraz początek obdukcji Wojciecha Patki (28–29 VIII 1758 r.)",
        "osoby_podmioty": "Jan Domaniewicz [Domaniewicz] szlachetnie urodzony; Antoni Kotłun [Kotłun]; Wojciech Patka [Patka / Pałka?]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "(1) Dokończenie protokołu z 28 VIII 1758 r.: manifestacja szlachetnie urodzonego Jana Domaniewicza przeciw Antoniemu Kotłunowi mieszczaninowi kraśnickiemu o zniewagę na gospodzie („witam grabarza”, „pisarz… ty śpie dam ci pięścią w pysk”) i przymuszenie do ustąpienia z gospody; (2) `Feryia 3tia post Festum Sancti Augustini Episcopi in crastino 1758 Anno` (29 VIII 1758 r.): początek obdukcji uczciwego Wojciecha Patki [Pałki?].",
        "transkrypcja": (
            "[fol. 376r, dolna numeracja 353]\n"
            "stanowszy Personaliter Szlachetnie urodzony Jan Domaniewicz solennie "
            "y iak naysolenniey manifestował się y protestował przeciw uciwego Antoniego "
            "Kotłuna miesz. kras: oto iako nie maiąc żadney racyi manifestanta na "
            "gospodzie niesłusznie konfundował y szkalował niegodziwemi słowy mowiąc "
            "testowa manifestantowi owitam grabarza, na co manifestant odpowiedział "
            "grabarze a grabarki pisarze a kałamarze a na gospodzie twardy sąd za "
            "swóy grosz co powtórnie wyżey wyrażony Kotłun mowił testowa alboś nie "
            "grabarz y testowa mowił tenże ty śpie dam ci pięścią w pysk mowiąc "
            "widziałem zydłem y powtórnie y trzeci przystępował z pięścią manifestantowi "
            "do gęby także szkaluiąc niegodziwemi słowy aż nareszcie manifestant "
            "musiał z gospody ustąpić o co powtórnie manifestant iterum atque iterum "
            "manifestatur et protestatur.\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Cras: Feryia 3tia "
            "post Festum Sancti Augustini Episcopi in crastino 1758 Anno\n"
            "Obdukcyia uciwego Woyciecha Patki [Pałki?] Ph: który przyszedłszy do "
            "urzędu naszego..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 771,
        "numer_pozycji": "Poz. 771",
        "strona_pagina": "fol. 376v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Obdukcje i manifestacje / Dokończenie obdukcji Wojciecha Patki i jego żony Marianny (pobitych przez Antoniego Tokarza/Kobiarza i Andrzeja Kratkowskiego) oraz manifestacja Patki przeciw Joachimowi Karabaszowi (30 VIII 1758 r.)",
        "osoby_podmioty": "Wojciech Patka [Patka / Pałka?]; Marianna Patkowa [Patkowa]; Antoni Tokarz [Tokarz / Kobiarz?]; Andrzej Kratkowski [Kratkowski]; Joachim Karabasz [Karabasz / Harabasz?]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "(1) Dokończenie obdukcji Wojciecha Patki i jego żony Marianny (rany, pięści na głowie i grzbiecie, pobicie motyczką od kozy) — obwiniają Antoniego Tokarza [Kobiarza?] i Andrzeja Kratkowskiego, a także relacjonują pościg i uderzenie starozakonnego Joachima Karabasza [Harabasza?]; (2) `Feryia 4ta Post Festum Sancti Augustini Proxima 1758` (30 VIII 1758 r.): manifestacja Wojciecha Patki przeciw Joachimowi Karabaszowi o niestawienie się na termin i odmowę posłuszeństwa miejskiego.",
        "transkrypcja": (
            "[fol. 376v]\n"
            "pokazał żonę na imię Mariannę z której rany ukazał zęby pięścią... "
            "jeden drugi y trzeci granat [?] y pięścią po głowie wszystkie rany sine "
            "krew zaszłe y zapuchłe ten zaś zaczynał od ramienia gdzie ku łopatce "
            "a kończył na połopiek [?] ten zaś uderzony motyczką od kozy a to z tey "
            "przyczyny to iest złości Sławetnych Antoniego Tokarza [Kobiarza?] y "
            "Andrzeia Kratkowskiego y tenże wyżey opisany gonił y dogonił na uciwego "
            "Patki łukasza [?] gdzie pies z nasieki uderzył tego pobicia daie winę "
            "niektoremu Joachimowi Karabaszowi [Harabaszowi?] Ph:\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasn: Feryia 4ta "
            "Post Festum Sancti Augustini Proxima 1758\n"
            "Przed urzędem y aktami ninieyszemi WŁ. stanowszy Personaliter uciwy "
            "Woyciech Patka Ph: solennie y iak naysolenniey manifestował się y "
            "protestował przeciw uciwego Joachima Karabasza [Harabasza?] oto iż ten "
            "maiąc pozwem upodobnie [?] winy manifestanta nie stanoł na termin "
            "naznaczony ale przez położonego odpowiedział że nie stanę nie mam "
            "czasu idąc do Krężnicy na posłuszeństwo mieyskie przysiągł y nie był "
            "posłusznym ale zhardział w czym manifestant maiąc krzywdę iterum atque "
            "iterum manifestatur et protestatur."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 772,
        "numer_pozycji": "Poz. 772",
        "strona_pagina": "fol. 377r (dolna 354)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Wizje i manifestacje / Wizja ławników Jana Szubertowskiego i Szymona Krzeszowskiego w sprawie zaginionych gęsi Antoniego Kotłuna u gospodyni Sołeckiej (14 XI 1758 r.) oraz początek manifestacji Bartłomieja Kilianka (15 XI 1758 r.)",
        "osoby_podmioty": "Jan Szubertowski [Szubertowski] ławnik; Szymon Krzeszowski [Krzeszowski] ławnik; Antoni Kotłun [Kotłun]; Antoniowa Kotłunowa [Kotłunowa]; Sołecka [Sołecka / Kazimierzowa Sołecka?]; Antoni Zdybeł [Zdybeł]; Bartłomiej Kilianek [Kilianek]",
        "kwoty_podatki": "6 gęsi + 4 gęsi = 10 gęsi (8 wypuszczonych, 2 zostawione)",
        "opis_sprawy": "(1) `Feryia 3tia post Festum Sancti Martini Pontificis Proxima anno Domini 1758` (14 XI 1758 r.): zeznanie deputowanych ławników Jana Szubertowskiego i Szymona Krzeszowskiego na żądanie Antoniego Kotłuna w sprawie zaginionych gęsi u gospodyni Sołeckiej (było 6 gęsi i 4 przyszły z pola, gospodyni 8 wypuściła, a 2 zostawiła i jedno zabiła na obiad — potwierdza trzeci świadek Antoni Zdybeł); (2) `Feryia 4ta Post Festum Sancti Martini Pontificis Proxima 1758 anno` (15 XI 1758 r.): początek manifestacji uczciwego Bartłomieja Kilianka.",
        "transkrypcja": (
            "[fol. 377r, dolna numeracja 354]\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasn: Feryia 3tia "
            "post Festum Sancti Martini Pontificis Proxima anno Domini 1758\n"
            "Będąc Deputowani z urzędu Woytowskiego Sławetni Mężowie Jan Szubertowski "
            "y Szymon Krzeszowski Ławnicy krasn: na jnstancyią uciwego Antoniego "
            "Kotłuna Mieszczanina krasn: strony gęsi zginionych do uciwey Kazimierzowey "
            "Sołeckiej która to Sołecka zeznała przed tymiż wyżey wyrażonemi "
            "urzędnikami że tylko było gęsi u mego gospodarza 6, a zaś z pola przyszło "
            "10 z tych dziesięciorga taż gospodyni wypuściła 8 a dwoie zostawiła w domu, "
            "z tych dwoyga zabiła iedno y gotowała a w tym razie przyszła Antoniowa "
            "Kotłunowa pytaiąc się o gęsi, ale ta gospodyni zaparła się mowiąc testowa "
            "że u mnie nie masz cudzych gęsi tylko moie własne, potym y drugie zabiła "
            "y biada [?] ale tego nie widziła iakie były lecz ta gospodyni nie sobie "
            "zabiła tylko kuchnię y trzeci uciwy Antoni Zdybeł toż samo zeznał.\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasnice Feryia 4ta "
            "Post Festum Sancti Martini Pontificis Proxima 1758 anno\n"
            "Przed urzędem y aktami ninieyszemi WŁ. stanowszy Personaliter uciwy "
            "Bartłomiey Kilianek Ph: solennie y iak naysolenniey manifestował się..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 773,
        "numer_pozycji": "Poz. 773",
        "strona_pagina": "fol. 377v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Manifestacje i zapisy długów / Dokończenie manifestacji Bartłomieja Kilianka przeciw młynarzowi grobelnemu Jakubowi Bieleckiemu oraz zapis długu Jakuba Tarnawskiego na rzecz Grzegorza Rycerza przez sprzedaż futra rzeźnikowi Anklowi (1758 r.)",
        "osoby_podmioty": "Bartłomiej Kilianek [Kilianek]; Jakub Bielecki [Bielecki] młynarz grobelny; Jakub Tarnawski [Tarnawski]; Grzegorz Rycerz [Rycerz]; Ankel Rzeźnik [Ankel / Anzelm?] obywatel kraśnicki",
        "kwoty_podatki": "złotych 17 (dług główny), wadium złotych 7, złotych 20 (za futro), złotych 17 (dla Rycerza)",
        "opis_sprawy": "(1) Dokończenie manifestacji Bartłomieja Kilianka przeciw Jakubowi Bieleckiemu młynarzowi grobelnemu o uderzenie na gospodzie w oko (Bielecki pozwany nie stanął, twierdząc, że należy do jurysdykcji dworskiej); (2) zapis długu uczciwego Jakuba Tarnawskiego mieszczanina kraśnickiego na rzecz Grzegorza Rycerza mieszczanina kraśnickiego na 17 złp (z wadium 7 złp) — chcąc zaspokoić wierzyciela, Tarnawski sprzedał niewiernemu Anklowi rzeźnikowi futro [?] za sumę 20 złp, z czego 17 złp ma oddać Rycerzowi, a resztę magistratowi.",
        "transkrypcja": (
            "[fol. 377v]\n"
            "tował się y protestował przeciw uciwego Jakuba Bieleckiego przed: y "
            "młynarza Grobelnego oto iż tenże manifestanta bez dania racyi na gospodzie "
            "uderzył tak dobrze że przyszedłszy manifestant do urzędu naszego prezentował "
            "że oko całe prawie było skrwawione y zapuchłe, przytym pozwawszy manifestant "
            "Jakuba Bieleckiego nie stanoł y na to odpowiedział że ja nie należę do "
            "mieyskiey jurysdykcyi tylko do Dworskiey lecz będąc przysięgłym miastu "
            "y grunta trzymaiąc między pospulstwem z hardością narabia w ktorey "
            "materyi manifestant maiąc krzywdę iterum atque iterum manifestatur et "
            "protestatur.\n"
            "Sub eodem actu\n"
            "Jako opisawszy się uciwy Jakub Tarnawski mieszczanin krasnicki będąc "
            "winien uciwemu Grzegorzowi Rycerzowi mieszczaninowi krasnickiemu według "
            "opisu swego złot: 17 y wadium siedem złotych sądom per medium więc chcąc "
            "uspokoić toż wyżey wyrażonego Grzegorza Rycerza mieszczanina krasnickiego "
            "umyślnie przedał niewiernemu Anklowi Rzeźnikowi obyw: krasn: za sumę "
            "złotych 20 sarnie futro przedany y stargowany y pierwszą ratę złotych 17 "
            "powinien oddać za niedziel dwie od aktu dzisieyszego reszta zaś pieniędzy "
            "oddać powinien magistratowi a przychyliwszy by..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 774,
        "numer_pozycji": "Poz. 774",
        "strona_pagina": "fol. 378r (dolna 355)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Zapisy długów, kwitacje i areszty / Dokończenie zapisu Tarnawskiego i Rycerza (podpis Junkla Słamowicza), kwitacja starozakonnego Nautyla u Sebestyana Pawlickiego za dług Jana Ciurki oraz areszt na niwkę Techo (20 XI 1758 r.)",
        "osoby_podmioty": "Ankel Rzeźnik [Ankel / Anzelm?]; Junkiel Słamowicz [Słamowicz] obywatel kraśnicki; Nautyl [Nautyl / Nawtul?] starozakonny; Jan Ciurka [Ciurka] zmarły; Sebestyan Pawlicki [Pawlicki]; Wojciech Buś [Buś]; Matyasz Grzętka [Grzętka]",
        "kwoty_podatki": "wadium złotych 3 (sądowi per medium); 2 korce żyta i 1 ćwierć [?]",
        "opis_sprawy": "(1) Dokończenie zapisu Jakuba Tarnawskiego (gdyby Ankel nie oddał na termin, wadium 3 złp sądowi per medium i 1 dzień więzienia; podpis własnoręczny `Junkiel Słamowicz obyw. krasnicki`); (2) `Sub eodem actu`: kwitacja starozakonnego Nautyla z długu zmarłego Jana Ciurki opisanego w testamencie — zięć Sebestyan Pawlicki zaspokoił dług (korcy 2 żyta i ćwierć 1) za co Nautyl kwituje (`+ Sobestyan Pawlicki`); (3) `Feryia Secunda ante Festum Stae Catharinae 1758 anno` (20 XI 1758 r.): areszt położony na niwkę zwaną Techo przeciw każdemu, kto by chciał ją kupić lub w zastaw brać (z wzmianką o Wojciechu Busiu i Matyaszu Grzętce).",
        "transkrypcja": (
            "[fol. 378r, dolna numeracja 355]\n"
            "by Ankel nie oddał na termin naznaczony zapisuie wadium sobie słusznie "
            "złotych 3 sądowi per medium y więzienia dzień ieden w kłodzie siedzieć "
            "powinien bez żadney odwłoki na co dla lepszey wiary podpisuie się a czas "
            "zaś powinien uspokoić na niedziel trzy gdy będzie wydane oddanie [?].\n"
            "Junkiel Słamowicz obyw. krasnicki\n"
            "Sub eodem actu et Advocatiali et Scabinali Jurato Cras: 1758 anno\n"
            "Według starozakonnego Nautyla długu który wyniósł uciwy Jan Ciurka jako "
            "w testamencie opisał się więc uciwy Sobestyan Pawlicki zięć iego co miał "
            "zboża po oycu swoim oddał na ten dług wyżey wyrażonemu Nautylowi żyta "
            "korcy 2 y ćwierć 1 na co dla lepszey wiary y wagi podpisuie się y nato "
            "dał że jako odebrał według zapisu naszego uwalnia nie umieiącemu pisać "
            "znak krzyża swego kładzie.\n"
            "+ Sobestyan Pawlicki\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasn: Feryia Secunda "
            "ante Festum Stae Catharinae 1758 anno\n"
            "Areszt położony na niwkę co Techo nazwaną iż kto chciał kupić lub na "
            "zastaw dawać Sławet. Woyciech Buś y Matyasz Grzętka areszt..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 775,
        "numer_pozycji": "Poz. 775",
        "strona_pagina": "fol. 378v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1758",
        "kategoria": "Manifestacje i egzekucje / Dokończenie aresztu na niwkę Techo, manifestacja ławnika Adama Zadela przeciw Marcinowi Morelowi o krwawe pobicie, manifestacja burmistrza Łukasza Krzeszowskiego przeciw Wojciechowi Busiowi oraz wpis o karze słupa z rozkazu Dzierżawskiego (1758 r.)",
        "osoby_podmioty": "Adam Zadel [Zadel / Żadło?] ławnik kraśnicki; Marcin Morel [Morel]; Łukasz Krzeszowski [Krzeszowski] burmistrz kraśnicki; Wojciech Buś [Buś]; Sołecka [Sołecka] nieboszczka; Dzierżawski [Dzierżawski] Wielmożny Imć Pan",
        "kwoty_podatki": "dni 3 przy słupie",
        "opis_sprawy": "(1) Dokończenie aresztu na niwkę Techo (póki JW Imć Pan Sędzia tej sprawy nie rozsądzi); (2) manifestacja ławnika kraśnickiego Adama Zadela [Zadla?] przeciw Marcinowi Morelowi o bezpodstawne pobicie na gospodzie, aż go krew oblała; (3) manifestacja burmistrza kraśnickiego Łukasza Krzeszowskiego przeciw Wojciechowi Busiowi mieszczaninowi kraśnickiemu o targnięcie się na podkupienie niwki u nieboszczki Sołeckiej; (4) ostatnia notatka księgi: z rozkazu Wielmożnego Imć Pana Dzierżawskiego [?] wystawienie pod słup na 3 dni.",
        "transkrypcja": (
            "[fol. 378v]\n"
            "poki Jaśnie Wielmożny Imć Pan Sędzia tey sprawy nie rozsądzi.\n"
            "Sub eodem actu\n"
            "Przed urzędem y aktami ninieyszemi WŁ. stanowszy Personaliter Sławetny "
            "Adam Zadel Ławnik krasn. solennie y iak naysoleńniey manifestował się "
            "y protestował przeciw Sławet. Marcina Morela mies. krasn. ktory zapomniawszy "
            "Boiaźni Pana Boga y miłości Bliźniego tu dziś o sprawie zapomniawszy "
            "ktory wielkiemi iest zaostrzone karaniami bez dania racyi manifestanta "
            "na gospodzie w gęby uderzył tak dobrze że go krew oblała tę krew "
            "manifestant prezentował przed urzędem naszym w ktory materyi manifestant "
            "iako naysoleniey manifestatur et protestatur.\n"
            "Sub eodem actu\n"
            "Przed urzędem y aktami ninieyszemi WŁ. stanowszy Personaliter Sławet. "
            "Łukasz Krzeszowski Bur. krasn. solennie y iak naysolenniey manifestował "
            "się y protestował przeciw uciwego Woyciecha Busia miesz. krasn. oto iż "
            "ten manifestanta podkupić w niwie Sołeckiej ktora manifestant ztargował "
            "u nieboszczki Sołeckiej w ktory materyi manifestant iterum atque iterum "
            "manifestatur et protestatur.\n"
            "Sub eodem actu\n"
            "Z rozkazu Wiel. Imć Pana Dzierżawskiego [?] sługo pod słupem zaiste do "
            "słupa wystawić... dni 3 na mieyscu..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 776,
        "numer_pozycji": "Poz. 776",
        "strona_pagina": "karta końcowa mikrofilmu",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1959",
        "kategoria": "Metryka archiwalna mikrofilmu / Karta końcowa mikrofilmu nr 110404 (Wojewódzkie Archiwum Państwowe Lublin, 31 X 1959 r.)",
        "osoby_podmioty": "Wojewódzkie Archiwum Państwowe Lublin; Laboratorium Mikrofilmowe Archiwum Dokumentacji Mechanicznej",
        "kwoty_podatki": "brak",
        "opis_sprawy": "Końcowa karta techniczna mikrofilmu nr 110404 z dnia 31 października 1959 r., zamykająca reprodukcję cyfrową Tomu 12 Akt Miasta Kraśnika (sygn. 35/40/0/1/17).",
        "transkrypcja": (
            "[Karta końcowa mikrofilmu]\n"
            "WOJEWÓDZKIE\n"
            "ARCHIWUM PAŃSTWOWE\n"
            "LUBLIN\n\n"
            "AKTA MIASTA: KRAŚNIKA\n"
            "NR TOMU 12\n"
            "NR MIKROFILMU 110404\n"
            "LAB. MIKROFILM. ARCH. DOKUM. MECHANICZNEJ\n"
            "Koniec\n"
            "DN. 31 M-C 10 ROK 1959 r."
        ),
        "link_swa": UNIT_LINK
    }
]

main_data.extend(part31_scans)
with open('/home/ubuntu/workspace/Gen/main_data_j17_part31.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"SUCCESS: main_data_j17_part31.json saved with {len(main_data)} scans.")
