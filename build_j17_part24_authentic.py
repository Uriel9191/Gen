# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j17_part23.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801'

part24_scans = [
    {
        "nr_skanu": 576,
        "numer_pozycji": "Poz. 576",
        "strona_pagina": "fol. 282r (dolna 259)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Inkwizycja i zeznania świadków / Dokończenie inkwizycji Jana Przesławskiego przeciw Piotrowi Potokowiczowi i żonie (zeznania Kazimierza Młynarskiego i Szymona Nowackiego, 1757 r.)",
        "osoby_podmioty": "Jan Przesławski [Przesławski]; Kazimierz Młynarski [Młynarski]; Piotrowa Potokowiczowa [Potokowiczowa]; Szymon Nowacki [Nowacki]; Piotr Potokowicz [Potokowicz]; Siostra Szafrańskiego [Szafrański?]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "Dokończenie inkwizycji z fol. 281v: (1) 2. świadek Kazimierz Młynarski zeznaje o kłótni o paciorki i uderzeniu Przesławskiego łokciem pod brodę przez Potokowiczową; (2) 3. świadek Szymon Nowacki (garbujący skóry u Przesławskiego) zeznaje o kłótni z siostrą Szafrańskiego oraz o napaści syna, córki i żony Piotra Potokowicza na dom Przesławskiego (wybicie okna, szarpanie za włosy, podarcie kożucha).",
        "transkrypcja": (
            "[fol. 282r, dolna numeracja 259]\n"
            "2dus Testis Honesty Casimirus Młynarski sub Iuramento recognovit Jako będącz w swej stancyj "
            "słyszałem kłotnie między Janem Przesławskim y Piotrową Potokowiczową gdzie Piotrowa "
            "Potokowiczowa wołała na Jana Przesławskiego strony paciorkow moich na ty złodzieiu "
            "z swoią Corką wołała na złodzieia a Jan Przesławski mowił nie zadaway mi bo ty sama "
            "złodzieyka boś mie okradła wtym Potokowiczowa poszła do Jana Przesławskiego y uderzyła go "
            "pod brodę łokciem o potym Przesławski kazał iey iść od siebie precz a ona odchodzącz "
            "mowiła mu ty synu albo ia ciebie albo ty mnie zgubisz więcy nie widziałem ani słyszałem\n"
            "3tius Testis Honesty Simon Nowacki sub Iuramento recognovit Jako będąc w domu u Jana "
            "Przesławskiego garbując mu skory przyszła siostra Szafrańskiego w tym kłocąc się z sobą "
            "siostra Szafrańskiego na Przesławskiego zadawała mu złodzieystwo y woytowi iakoby mieli "
            "ukraść kowadło młot y skory potym zaczęli się przeklinać między sobą a kiedy odeszła od "
            "niey przyszedł syn Piotra Potokowicza z Matką swoią y siostrą przychodzącz pod dom Jana "
            "Przesławskiego wołał syn Potokowicza kłoczącz się na Jana Przesławskiego ten mu odpowiedział "
            "idź do diabła ty y twoy ociec kradł konie wtym Potokowiczowa wybiła ręką okno y wparła się "
            "do izby a za nią corka iey przyszedszy z synem zaczęła łapać Przesławskiego za włosy y za "
            "gębę na ostatku wyleciał na dwor y Matka za nim y uderzyła go pięścią w nos z którego "
            "krew poszła y porwała mu łokciem y obaliła go y zadrapnęła go w rękę y kożuch na nim "
            "podarła a na ostatku przychodząc potym na ulicę wołała na Przesławskiego z dziećmi"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 577,
        "numer_pozycji": "Poz. 577",
        "strona_pagina": "fol. 282v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Inkwizycja i dekret / Dokończenie zeznania Nowackiego, inkwizycja Jana Przesławskiego przeciw Haimowi Janklowiczowi oraz początek dekretu Haimowej Janklowiczowej (1757 r.)",
        "osoby_podmioty": "Jan Przesławski [Przesławski]; Haim Janklowicz [Janklowicz]; Szymon Nowacki [Nowacki]; Haimowa Janklowiczowa [Janklowiczowa] niewierna",
        "kwoty_podatki": "7 złp 15 gr (za skórę); 6 złp; 6 złp 20 gr",
        "opis_sprawy": "Zakończenie zeznania Szymona Nowackiego; następnie `Inquisitio ex parte Joannis Przesławski contra Infidelem Haim Janklowicz` (Nowacki zeznaje o skórze wziętej przez żonę od Haima Janklowicza po 7 złp 15 gr i zapłacie 6 złp); poniżej początek dekretu między niewierną Haimową Janklowiczową a Janem Przesławskim o dopłatę za skórę.",
        "transkrypcja": (
            "[fol. 282v]\n"
            "na ty złodzieiu wroc moie paciorki a Jan Przesławski też iey mowił idź ty złodzieyko "
            "więcy nie słyszałem ani widziałem\n"
            "Inquisitio ex parte Joannis Przesławski contra Infidelem Haim Janklowicz\n"
            "Testis Honesty Simon Nowacki sub Iuramento recognovit Jako wziołem od Pana Jana "
            "Przesławskiego skor [dwie? / trzy?] do garbowania a żona moja przyniosła mi trzecią skórę "
            "mowiąc żem ią wzięła od Żyda Haima Janklowicza po złotych 7 gr 15 y w tym z tą żoną "
            "przybyłem do domu mego y oddałem te skory do garbowania ale nie miałem czem zapłacić "
            "y zostałem winien temu Haimowi złotych 7 gr 15 za skórę a gdy przyszedł do mnie Jan "
            "Przesławski z żoną moją y dopominał się o zapłatę za tę skórę y dałem mu za nią złotych 6 "
            "więcy nie widziałem ani słyszałem\n"
            "Między Niewierną Haimową Janklowiczową Aktorką z iedney a Sławetnym Janem Przesławskim "
            "Pozwanym z drugiey strony Sąd Ninieyszy krasnicki wysłuchawszy oboiey strony kontrowersye "
            "y produkowaną przez Aktorkę na Pozwanego inkwizycyą z którego się pokazało iż Pozwany "
            "wzioł od Aktorki skórę jedną za którą powinien był oddać złotych siedm groszy piętnaście "
            "a oddał tylko złotych sześć y groszy dwadzieścia przeto Sąd Ninieyszy uznawa aby "
            "Pozwany Jan Przesławski resztę za tę skórę dopłacił to iest"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 578,
        "numer_pozycji": "Poz. 578",
        "strona_pagina": "fol. 283r (dolna 253)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Dekrety i manifestacje / Zakończenie dekretu Haimowej Janklowiczowej, manifestacja Józefa Gąski przeciw Maciejowi Wilczyńskiemu i Jana Przesławskiego przeciw Piotrowi Potokowiczowi (1757 r.)",
        "osoby_podmioty": "Jan Przesławski [Przesławski]; Haimowa Janklowiczowa [Janklowiczowa]; Józef Gąska [Gąska]; Maciej Wilczyński [Wilczyński]; Piotr Potokowicz [Potokowicz]",
        "kwoty_podatki": "1 złp 25 gr (dopłata); 3 grzywny (stronie, sądowi, na reperację ratusza)",
        "opis_sprawy": "Dokończenie dekretu Haimowej Janklowiczowej z Przesławskim (dopłata 1 złp 25 gr oraz 3 grzywny); manifestacja Józefa Gąski przeciw Maciejowi Wilczyńskiemu o niestawiennictwo w sprawie o dług (`Feria 4ta post Dominicam Exaudi 1757`); początek manifestacji Jana Przesławskiego przeciw Piotrowi Potokowiczowi i jego żonie.",
        "transkrypcja": (
            "[fol. 283r, dolna numeracja 253]\n"
            "złotych ieden groszy dwadzieścia pięć Aktorce zapłacił do tego za koszt sądowy "
            "grzywny trzy stronie Aktorce iednę sądowi drugą a na reperacyą ratusza trzecią "
            "którą sumę z grzywnami instantanee oddać powinien pod exekucyą\n"
            "Sub Eodem Actu\n"
            "Przed Urzędem y Aktami Ninieyszemi stawaiąc personaliter Sł: Jozef Gąska przeciwko "
            "Sławetnemu Macieiowi Wilczyńskiemu solennie manifestował się oto iż pozwany będąc "
            "pozwany na termin ninieyszy Feria 4ta post Dominicam Exaudi 1757 w sprawie o dług "
            "do Sądu nie stanoł ani żadnego plenipotenta nie przysłał przeto manifestant przeciwko "
            "niemu o niestawiennictwo y szkody protestuie się prosząc o zapisanie tey manifestacyi\n"
            "Sub Eodem Actu\n"
            "Przed Urzędem y Aktami Ninieyszemi stawaiąc personaliter Sł: Jan Przesławski przeciwko "
            "Piotrowi Potokowiczowi mieszczaninowi krasnickiemu y żonie iego solennie manifestował się "
            "y protestował oto iż w sprawie swoiey o pobicie y obelgę honoru swego przed Sądem "
            "tutejszym toczącej się pozwany Piotr Potokowicz y żona iego nie tylko na terminie "
            "nie stanęli ale też dalsze kalumnie y pogróżki na zdrowiu iego czynić nie przestaią"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 579,
        "numer_pozycji": "Poz. 579",
        "strona_pagina": "fol. 283v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Dekrety i wizje szkód / Wyrok na Grzegorza Wolaczka dla Habusia oraz wizja szkody w zbożu Michała Matuszkiewicza przez bydło Augustyna Piaseckiego (1757 r.)",
        "osoby_podmioty": "Jan Przesławski [Przesławski]; Piotr Potokowicz [Potokowicz]; Habuś [Habuś] starozakonny; Grzegorz Wolaczek [Wolaczek]; Michał Matuszkiewicz [Matuszkiewicz]; Jan Lubartowski [Lubartowski]; Antoni Pilaszkiewicz [Pilaszkiewicz]; Augustyn Piasecki [Piasecki]",
        "kwoty_podatki": "3 grzywny (stronie, sądowi, na reperację miasta); 2 korce żyta i pół korca jęczmienia",
        "opis_sprawy": "Dokończenie manifestacji Przesławskiego przeciw Potokowiczowi; wyrok nakazujący Grzegorzowi Wolaczkowi uspokojenie starozakonnego Habusia pod grzywnami 3; wizja szkody w życie i jęczmieniu Michała Matuszkiewicza przez bydło rogate Augustyna Piaseckiego (deputowani ławnicy Jan Lubartowski i Antoni Pilaszkiewicz).",
        "transkrypcja": (
            "[fol. 283v]\n"
            "przeciwko którym to bezprawiom manifestant ninieyszą protestacyą swoią zanosi "
            "zapisuiąc ią do akt mieyskich krasnickich\n"
            "Sub Eodem Actu\n"
            "Między Starozakonnym Habusiem Aktorem z iedney a Grzegorzem Wolaczkiem Pozwanym "
            "z drugiey strony Sąd Ninieyszy nakazuie aby Pozwany Grzegorz Wolaczek Starozakonnego "
            "Habusia w pretensyi iego uspokoił y zadosyć uczynił pod winą grzywien trzech "
            "iedney stronie drugiey sądowi trzeciey na reperacyą miasta\n"
            "Sub Eodem Actu\n"
            "Wizyia szkody w zbożu uczynioney na gruncie Michała Matuszkiewicza przez Deputowanych "
            "Sławetnych Jana Lubartowskiego y Antoniego Pilaszkiewicza Ławników Przysięgłych "
            "którzy zeszedszy na grunt wspomnionego Michała Matuszkiewicza widzieli iż w życie "
            "y jęczmieniu szkoda wielka stała się przez bydło rogate Augustyna Piaseckiego "
            "którą to szkodę oszacowali na korcy żyta dwa y jęczmienia pół korca co na sumienie "
            "swoie przed Urzędem zeznali"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 580,
        "numer_pozycji": "Poz. 580",
        "strona_pagina": "fol. 284r (dolna 254)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Manifestacje i kwitacje / Spór wójta Krzywińskiego z burmistrzem Krzeszowskim o karty z protokołów oraz kwitacja burmistrza Bryśkiewicza z Michałem Stachowiczem (1757 r.)",
        "osoby_podmioty": "Michał Krzywiński [Krzywiński] wójt; Łukasz Krzeszowski [Krzeszowski] burmistrz; Marcin Morel [Morel] deputat; Stanisław Bryśkiewicz [Bryśkiewicz] burmistrz; Michał Stachowicz [Stachowicz]; Jerzy Pietrowski [Pietrowski] chorąży lubelski",
        "kwoty_podatki": "brak",
        "opis_sprawy": "Manifestacja wójta Michała Krzywińskiego przeciw burmistrzowi Łukaszowi Krzeszowskiemu o zarzut wyrywania kart z protokołów i sprzedawania ich Marcinowi Morelowi oraz o samowolny cyrograf; następnie (`Sabbatho ante Festum SS. Trinitatis 1757`) kwitacja burmistrza Stanisława Bryśkiewicza z Michałem Stachowiczem, poddanym OO. Franciszkanów w posesji chorążego lubelskiego Jerzego Pietrowskiego.",
        "transkrypcja": (
            "[fol. 284r, dolna numeracja 254]\n"
            "Sub Eodem Actu\n"
            "Przed Urzędem y Aktami Ninieyszemi stawaiąc personaliter Szlachetny Michał Krzywiński "
            "Woyt Krasnicki przeciwko Sławetnemu Łukaszowi Krzeszowskiemu Burmistrzowi Krasnickiemu "
            "solennie manifestował się oto iż pozwany Burmistrz nie tylko publicznie przed ludźmi "
            "zadawał manifestantowi iakoby karty z protokołów mieyskich wyrywał y one Sławetnemu "
            "Marcinowi Morelowi Deputatowi sprzedawał ale też cyrograf pewien bez wiadomości "
            "y woli Urzędu wydał przez co honor y urząd manifestanta ciężko zniesławił\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasnicensi Ipso die Sabathi "
            "ante Festum SS. Trinitatis anno Domini 1757\n"
            "Przed Urzędem y Aktami Ninieyszemi stawaiąc personaliter Sławetny Stanisław Bryśkiewicz "
            "Burmistrz Krasnicki z iedney a Uczciwy Michał Stachowicz poddany OO. Franciszkanów "
            "a w posesyi WJP Chorążego Lubelskiego Jerzego Pietrowskiego z [Karpholu? / Karczmisk?] "
            "z drugiey strony dobrowolnie zeznali iż zadosyćuczynienie między sobą uczynili "
            "o pretensye wszelkie wzaiemnie zaspokoiwszy się y kwituiąc na co się Michał Stachowicz "
            "znakiem Krzyża Świętego podpisał Michał Stachowicz (+)"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 581,
        "numer_pozycji": "Poz. 581",
        "strona_pagina": "fol. 284v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Manifestacje / Protestacja burmistrza i pisarza Stanisława Bryśkiewicza przeciw ławnikowi Janowi Lubartowskiemu i jego żonie o zniesławianie małżonki (1757 r.)",
        "osoby_podmioty": "Stanisław Bryśkiewicz [Bryśkiewicz] burmistrz i pisarz; Jan Lubartowski [Lubartowski] ławnik przysięgły",
        "kwoty_podatki": "brak",
        "opis_sprawy": "Manifestacja Stanisława Bryśkiewicza przeciw ławnikowi Janowi Lubartowskiemu i jego żonie o trzyletnie obelgi wobec żony manifestanta („ma bydź jakąś dragonką”) oraz najście na dom pod nieobecność męża.",
        "transkrypcja": (
            "[fol. 284v]\n"
            "Sub Eodem Actu\n"
            "Przed Urzędem y Aktami Ninieyszemi stawaiąc personaliter Sławetny Stanisław Bryśkiewicz "
            "Burmistrz y Pisarz Przysięgły Krasnicki przeciwko Sławetnemu Janowi Lubartowskiemu "
            "Ławnikowi Przysięgłemu y żonie iego solennie manifestował się y protestował oto iż "
            "ciż małżonkowie od trzech lat żonę manifestanta obelżywemi słowami zniesławiaią "
            "mowiąc iż ma bydź iakąś dragonką a nadto w niebytności manifestanta w domu własnym "
            "na żonę iego naszli y gwałt czynili przeciwko którym to krzywdom y obelgom "
            "manifestant ninieyszą protestacyą swoią zanosi zachowuiąc sobie dalsze prawne dochodzenie"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 582,
        "numer_pozycji": "Poz. 582",
        "strona_pagina": "fol. 285r (dolna 255)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Manifestacje i areszty / Manifestacja wójta Krzywińskiego przeciw Jędrzejowi Kofeckiemu o odmowę przyjęcia sumy oraz areszt na pieniądzach Kofeckiego (1757 r.)",
        "osoby_podmioty": "Michał Krzywiński [Krzywiński] wójt; Jędrzej Kofecki [Kofecki]; Stara Lubkowska [Stara Lubkowska? / Starostkowa?]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "`Feria 3tia ante Festum Sacri Corporis Christi proxima 1757`: manifestacja wójta Michała Krzywińskiego przeciw JP Jędrzejowi Kofeckiemu, który nie chciał przyjąć gotowej sumy położonej na ratuszu; następnie areszt na pieniądzach Kofeckiego u wójta założony przez [Starą Lubkowską? / Starostkową?].",
        "transkrypcja": (
            "[fol. 285r, dolna numeracja 255]\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasnicensi Feria 3tia ante Festum "
            "Sacri Corporis Christi proxima anno Domini 1757\n"
            "Przed Urzędem y Aktami Ninieyszemi stawaiąc personaliter Szlachetny Michał Krzywiński "
            "Woyt Krasnicki przeciwko JP Jędrzeiowi Kofeckiemu solennie manifestował się oto iż "
            "manifestant chcąc dług sprawiedliwy na Ratuszu Krasnickim wypłacić sumę gotową "
            "położył iednak JP Jędrzey Kofecki teyże sumy przyjąć nie chciał y z Ratusza odszedł "
            "przeto manifestant o wszelkie szkody y nakłady przeciwko niemu protestuie się\n"
            "Sub Eodem Actu\n"
            "Areszt na pieniądzach JP Jędrzeia Kofeckiego u Szlachetnego Michała Krzywińskiego "
            "Woyta Krasnickiego będących przez [Starą Lubkowską? / Starostkową?] założony "
            "o pretensyą długu własnego który to areszt Sąd Ninieyszy przyiął y do akt wpisać rozkazał"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 583,
        "numer_pozycji": "Poz. 583",
        "strona_pagina": "fol. 285v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Oblaty i areszty / Oblata skryptu dłużnego Andrzeja Kofeckiego na 158 złp 12 gr dla brata Samuela Kofeckiego oraz areszt na dobrach Tyrawczyzna (1757 r.)",
        "osoby_podmioty": "Samuel Kofecki [Kofecki]; Andrzej Kofecki [Kofecki / Jędrzej Kofecki]; Szymon Marszałkowski [Marszałkowski]",
        "kwoty_podatki": "158 złp 12 gr; 23 gr (za wóz)",
        "opis_sprawy": "`Feryia Tercya ante Festum SS. Corporis Christi proxima 1757`: oblata skryptu dłużnego Andrzeja Kofeckiego z 17 VI 1756 r. na 158 złp 12 gr i 23 gr za wóz dla brata Samuela Kofeckiego; areszt Samuela Kofeckiego na dobrach Tyrawczyzna i niwie od Szymona Marszałkowskiego.",
        "transkrypcja": (
            "[fol. 285v]\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasnicensi Feryia Tercya ante "
            "Festum SS. Corporis Christi proxima anno Domini 1757\n"
            "Przed Urzędem y Aktami Ninieyszemi stawaiąc personaliter Urodzony Samuel Kofecki "
            "do akt ninieyszych podał do oblatowania skrypt dłużny brata swego rodzonego Urodzonego "
            "Andrzeia Kofeckiego w te słowa pisany: Ja niżey na podpisie wyrażony zeznaię tym "
            "skryptem moim iż winien iestem bratu memu rodzonemu Panu Samuelowi Kofeckiemu sumę "
            "złotych polskich sto pięćdziesiąt ośm groszy dwanaście która to suma urosła z różnych "
            "rachunków y za wóz groszy dwadzieścia trzy którą sumę oddać przyrzekam Datt w Kraśniku "
            "die 17 Junii anno 1756 Andrzey Kofecki mp.\n"
            "[na lewym marginesie: Oblatował Urodzony Samuel Kofecki]\n"
            "Sub Eodem Actu\n"
            "Areszt Urodzonego Samuela Kofeckiego na dobrach Tyrawczyzna nazwanych y na niwie "
            "od Szymona Marszałkowskiego trzymanych przez brata swego Urodzonego Jędrzeia Kofeckiego "
            "założony dla pewności sumy złotych 158 groszy 12 z skryptu powyższego wynikający"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 584,
        "numer_pozycji": "Poz. 584",
        "strona_pagina": "fol. 286r (dolna 256)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Areszty i egzekucje / Dokończenie aresztu Samuela Kofeckiego, areszt Gierszona Catowica na 4 złp oraz egzekucja dekretu całej ordynacji (1757 r.)",
        "osoby_podmioty": "Samuel Kofecki [Kofecki]; Jędrzej Kofecki [Kofecki]; Gierszon Catowic [Catowic] starozakonny; JMć Pan Sędzia [brak nazwiska]",
        "kwoty_podatki": "158 złp 12 gr; 4 złp; 14 złp (grzywny) i 14 złp (na kościół)",
        "opis_sprawy": "Zakończenie aresztu Samuela Kofeckiego na 158 złp 12 gr przeciw bratu Jędrzejowi Kofeckiemu; areszt starozakonnego Gierszona Catowica na 4 złp u Pana Kofeckiego; zapiska o egzekucji dekretu Sędziego całej ordynacji (14 złp grzywien i 14 złp na kościół).",
        "transkrypcja": (
            "[fol. 286r, dolna numeracja 256]\n"
            "aż do zupełney satysfakcyi sumy złotych sto pięćdziesiąt ośm groszy dwanaście "
            "przeciwko bratu swemu Urodzonemu Jędrzeiowi Kofeckiemu który to areszt Sąd "
            "Ninieyszy przyiął y do ksiąg wpisać rozkazał\n"
            "Sub Eodem Actu\n"
            "Areszt Starozakonnego Gierszona Catowica na złotych czterech u Pana Kofeckiego "
            "będących założony dla pewności długu swego który Sąd przyiął\n"
            "Sub Eodem Actu\n"
            "Zapiska o exekucyi dekretu JMci Pana Sędziego całey ordynacyi z którego to dekretu "
            "przypadło grzywien złotych czternaście y na kościół złotych czternaście co przez "
            "Urząd Mieyski Krasnicki do exekucyi przywiedzione być ma"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 585,
        "numer_pozycji": "Poz. 585",
        "strona_pagina": "fol. 286v (do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Inkwizycja i manifestacja / Inkwizycja Mikołaja Nowaka przeciw Antoniemu Pawłowskiemu (zeznanie Jana Łypy) oraz manifestacja burmistrza Krzeszowskiego przeciw Ćwiekowi (1757 r., karta odwrócona)",
        "osoby_podmioty": "Mikołaj Nowak [Nowak]; Antoni Pawłowski [Pawłowski]; Jan Łypa [Łypa]; Paweł Fruga [Fruga]; Józef Nowak [Nowak]; Antoni Łypa [Łypa]; Łukasz Krzeszowski [Krzeszowski] burmistrz; Grzegorz Przesławski [Przesławski? / Jędrzejek?]; Wojciech Ćwiek [Ćwiek / Ćwieka?]; Kazimierz Ćwiek [Ćwiek]",
        "kwoty_podatki": "10 złp (pomówienie o pożyczkę na wesele)",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: (1) `Inquisitio ex parte Nicolai Nowak contra Antonium Pawłowski` — zeznanie Jana Łypy o bójce z Pawłem Frugą, Józefem Nowakiem i Antonim Pawłowskim oraz rozdarciu kontusza; (2) `Feria 2da ante Festum SS. Corporis Christi 1757` — manifestacja burmistrza Łukasza Krzeszowskiego przeciw Grzegorzowi [Przesławskiemu?] i Wojciechowi Ćwiekowi o pomówienie o pożyczkę 10 złp od karczmarza Ćwieki na wesele córki.",
        "transkrypcja": (
            "[fol. 286v — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "Inquisitio ex parte Nicolai Nowak contra Antonium Pawłowski\n"
            "Testis Joannes Łypa sub Conscientia recognovit Jako [będąc? / widząc?] "
            "gdy się zdarzyło że Paweł Fruga z Jozefem Nowakiem [szli? / byli?] "
            "zaraz Pawłowski Antoni uderzył na Jozefa Nowaka y porwał za drugi kontusz "
            "ale żaden nie poszedł tylko [z daleka?] krzyczeli Potym porwał y bronił Nowaka Jozefa "
            "który zerwawszy się Paweł Fruga y Pawłowski tak wszyscy razem przewrócili się "
            "na ziemię tylko Antoni Łypa to tylko widział że na końcu Nowak przybiegłszy do siebie "
            "cymbalika mowił Antoniemu Pawłowskiemu zaboty może bić biłbyś porwawszy go za kontusz "
            "rozdarł mu kontusz y żaden żadnego nie bił tylko się szarpali z sobą\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasnicensi Feria Secunda "
            "ante Festum SS. Corporis Christi proxima anno 1757\n"
            "Przed Urzędem y Aktami Ninieyszemi stawaiąc personaliter Sławetny Łukasz Krzeszowski "
            "Burmistrz Krasnicki solennie y iak naysolemniey manifestował się przeciwko "
            "Uczciwym Grzegorzowi [Przesławskiemu? / Jedrzejkowi?] y Woyciechowi Ćwiekowi przedmieszczanom "
            "krasnickim którzy zapomniawszy boiaźni Pana Boga y miłości bliźniego zadali "
            "manifestantowi iakoby od Karczmierza Ćwieki dziesiątka racyego miał pożyczyć "
            "pospolitych pieniędzy złotych 10 na wesele corki swoiey Uczciwy manifestant "
            "urażony nie czuiąc się do tego ażeby miał pożyczać y teni atty ten manifestat et protestatur"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 586,
        "numer_pozycji": "Poz. 586",
        "strona_pagina": "fol. 287r (dolna 257, do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Dekrety / Spór starozakonnego Mośka Lewkowicza z Franciszkiem Czubrowskim i Adamem Posuniakiem o dostawę 3 korcy wapna (1757 r., karta odwrócona)",
        "osoby_podmioty": "Mosiek Lewkowicz [Lewkowicz / Mosiek] starozakonny; Franciszek Czubrowski [Czubrowski]; Adam Posuniak [Posuniak]",
        "kwoty_podatki": "4 złp za korzec wapna (razem 12 złp za 3 korce); 1 grzywna sądowa",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: dokończenie zeznania o sporze o wapno oraz wyrok w sprawie między starozakonnym Mośkiem Lewkowiczem a Franciszkiem Czubrowskim i Adamem Posuniakiem o dostawę 3 korcy wapna niegaszonego po 4 złp (razem 12 złp) oraz 1 grzywnę sądową za brak pisemnego kontraktu.",
        "transkrypcja": (
            "[fol. 287r, dolna numeracja 257 — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "ieden po drugich rozstali y to słyszał osobiście wymawiali mowiąc Mosiek "
            "że mi przywożą niegaszone wapno oni odpowiedzieli że gaszone natychmiast "
            "roziesli co potrzeba wapna\n"
            "Sub Eodem Actu\n"
            "Między Starozakonnym Moskiem Lewkowiczem Aktorem Sprawy z iedney a Pozwanymi "
            "Uczciwymi Franciszkiem Czubrowskim y Adamem Posuniakiem z drugiey strony "
            "Sąd Ninieyszy obydwie strony przychylaiąc się do obydwu stron wysłuchawszy "
            "kontrowersye y dyspozycye zważaiąc ato ratione zgody za wapno zatonione "
            "po złotych 4 zeszli się y zgodzili z Aktorem wszystkiego umawiały sobie strony "
            "Aktor pretendował aby mu Pozwani przywieźli wapno niegaszone a Pozwani zaś "
            "mowili że gaszone mieli przystawić na co żadnego kontraktu między stronami "
            "nie było tylko ustna mowa była przy Urzędniku w czym według zgody korca "
            "po złotych 4 aby dodali Aktorowi z czego wynikło na złotych 12 dotychczas korcy dwa "
            "a trzeci korzec wapna niegaszonego dodać powinni Aktorowi "
            "więcy Aktor ieżeli będzie potrzebował ma się z Pozwanymi zgodzić z Aktorem iakby się "
            "im podobało zaś Pozwani że ostrożności w tym nie mieli y kontraktu czy zgody "
            "między sobą nie opisali maią dać sądowi grzywnę iedną y na dalszy czas "
            "takowych kontrowersyi nie czynić w którey sprawie Pozwani bez pozwu zdali się na Sąd "
            "według dekretu zadosyć uczynić powinni mocą zwierzchności naszey przykazuiemy"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 587,
        "numer_pozycji": "Poz. 587",
        "strona_pagina": "fol. 287v (dolna 258, do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Ugody i inkwizycje / Ugoda Jana Antoniego Marakiewicza z wdową Marcinową Ćwiekową oraz inkwizycja Mośka przeciw Czubrowskiemu i Posuniakowi (1757 r., karta odwrócona)",
        "osoby_podmioty": "Jan Antoni Marakiewicz [Marakiewicz]; Marcinowa Ćwiekowa [Ćwiekowa] wdowa; Mosiek [Mosiek] niewierny; Franciszek Czubrowski [Czubrowski]; Adam Posuniak [Posuniak]; Stanisław Bryśkiewicz [Bryśkiewicz] rajca",
        "kwoty_podatki": "9 złp (odebrał 4 złp, reszta synowcowi); 4 grzywny kary",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: (1) `Feria 6ta ante Festum Pentecostes 1757` — ugoda Jana Antoniego Marakiewicza z wdową Marcinową Ćwiekową o 9 złp za wieprza i kury; (2) `Feria 6ta ante Festum SS. Trinitatis 1757` — inkwizycja Mośka przeciw Czubrowskiemu i Posuniakowi, gdzie zeznaje rajca Stanisław Bryśkiewicz.",
        "transkrypcja": (
            "[fol. 287v, dolna numeracja 258 — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "Actum Coram Officio Advocatiali et Scabinali Jurato Crasnicensi Feria 6ta ante "
            "Festum Pentecostes Proxima anno 1757\n"
            "Stała się zgoda między stronami to iest Sławetnym Antonim Marakiewiczem y Marcinową "
            "Ćwiekową wdową o tamteysze z korzeniami wieprzowe y kury y innych rzeczy w ten "
            "niżey opisany sposób iako maiąc słuszną pretensyą dla miłości Pana Boga wyżey "
            "wyrażony Jan Antoni Marakiewicz darował swoią krzywdę odebrawszy przez zgodę "
            "satysfakcyą to iest złotych 9 y Marcinowa Ćwiekowa wdowa czyni in postensi "
            "ad complementum złotych 9 Marakiewicz odebrał złotych 4 a synowcowi restę "
            "deklarowała się oddać od tey niedzieli za tydzień bez żadney odwłoki y kwasu "
            "w niedotrzymaniu pod grzywnami 4\n"
            "Actum In Officio Consulari Jurato Crasnicensi Feria 6ta ante Festum SS. Trinitatis proxima 1757 ao\n"
            "Inquisitiones Ex Parte Infidelis Mosiek contra Honestos Franciscum Czubrowski et Adamum Posuniak\n"
            "Testis Iuratus Stanislaus Bryśkiewicz Consul Crasnicensis pro munere officii sui "
            "recognovit sub conscientia iako był natenczas przy zgodzie wapna za które zgodzili się za korzec"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 588,
        "numer_pozycji": "Poz. 588",
        "strona_pagina": "fol. 288r (do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Dekrety i inkwizycje / Wyroki w sprawach Antoniego Pawłowskiego z Nowakami (4+2 grzywny) i Szymona Krzeszowskiego o gęś oraz inkwizycja Mikołaja Nowaka (1757 r., karta odwrócona)",
        "osoby_podmioty": "Antoni Pawłowski [Pawłowski]; Mikołaj Nowak [Nowak]; Józef Nowak [Nowak / Nowaczek]; Paweł Fruga [Fruga]; Szymon Krzeszowski [Krzeszowski] ławnik; Wawrzyniec Tokarz [Tokarz]",
        "kwoty_podatki": "4 grzywny (Pawłowskiemu); 2 grzywny (sądowi); gęś",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: (1) wyrok na Mikołaja i Józefa Nowaków za pobicie Antoniego Pawłowskiego i rozdarcie kontusza (4 grzywny aktorowi, 2 sądowi); (2) wyrok w sprawie ławnika Szymona Krzeszowskiego przeciw Pawłowskiemu o gęsię zjedzone przez świnie; (3) `Inquisitio ex parte Mikołay Nowak contra Pawłowski` — zeznanie Wawrzyńca Tokarza.",
        "transkrypcja": (
            "[fol. 288r, dolna numeracja 258 — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "Sub Eodem Actu\n"
            "Między Uczciwym Antonim Pawłowskim Aktorem Sprawy z iedney a Pozwanym Uczciwym "
            "Mikołaiem Nowakiem y synem iego Jozefem z drugiey strony Sąd Ninieyszy obydwóch stron "
            "zważywszy kontrowersye y pretensye ato ratione pobicia Aktora przez Pozwanych "
            "iako świadczy inkwizycyia że Pozwani Aktora bez racyi pobili y kontusz na nim podarli "
            "który to Aktor nieprzyszedł bić Pozwanych tylko bronił Pawła Frugę za co Pozwani "
            "maią dać Aktorowi za pobicie y zdarcie kontusza tudzież prawne koszta grzywien 4 "
            "sądowi grzywien 2 że bez okazyi podrapali Aktora y spolnie Deprekacyą sobie uczynić "
            "w czym ma zakaz poki nie uspokoi mocą zwierzchności naszey przykazuiemy\n"
            "Sub Eodem Actu\n"
            "W sprawie między Sławetnym Szymonem Krzeszowskim Ławnikiem Aktorem a Pozwanym "
            "Uczciwym Antonim Pawłowskim z drugiey strony ato ratione gęsięcia które świnie "
            "zjadły w domu Pozwanego na co żadnego niema świadectwa w którey sprawie y tak "
            "bagatelney pretensyi Sąd nakazuie aby Pozwany zapłacił czyli dał gęś Aktorowi "
            "y przeprosił ponieważ na sądzie nie pokazał świadectwa mocą zwierzchności naszey przykazuiemy\n"
            "Inquisitio Ex parte Mikołay Nowak contra Pawłowski\n"
            "Testis Laurentius Tokarz sub conscientia recognovit Jako widział że gdy się Jozef "
            "Nowaczek porwał za łeb z Pawłem Frugą w tym przybiegłszy Pawłowski porwał z tyłu "
            "Jozefa Nowaczka y obalił na ziemię y obydwa przyciskali go w tym widząc Jędrzey "
            "bronił Nowaczka potym zaś Mikołay Nowak skoczywszy porwał Pawłowskiego y zadrapnął "
            "go po gębie y kontusz rozdarł"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 589,
        "numer_pozycji": "Poz. 589",
        "strona_pagina": "fol. 288v (do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Dekrety / Proces proboszcza ks. Jakuba Maliszewskiego i Konwentu Kanoników Regularnych z Maciejem Frugą o 33 korce żyta (1757 r., karta odwrócona)",
        "osoby_podmioty": "ks. Jakub Maliszewski [Maliszewski] proboszcz; Konwent Kraśnicki Kanoników Regularnych Lateraneńskich; Maciej Fruga [Fruga]",
        "kwoty_podatki": "33 korce żyta po 6 złp = 202 złp 15 gr; potrącenie 26 złp 6 gr; reszta 176 złp 9 gr",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: dokończenie zeznania obyczajowego z góry karty; następnie `Feria 4ta post Dominicam Exaudi 1757` — dekret sądu łączonego w sprawie ks. Jakuba Maliszewskiego i Konwentu przeciw Maciejowi Frudze o 33 korce żyta (202 złp 15 gr minus 26 złp 6 gr = 176 złp 9 gr do spłaty w 4 ratach).",
        "transkrypcja": (
            "[fol. 288v — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "uczynił ponieważ nie była mi powolna y broniła się mi iednak że nie byt było o tym "
            "ani słyszał tylko że mi podała okazyą do tego gdyż sama mi okazyą dała przez różne "
            "sposoby do tego występku któregom lubo nie wypełnił iednak że miałem tę intencyą "
            "nieodmienną wykonać\n"
            "Actum In Officio Composito Jurato Crasnicensi Feria 4ta post Dominicam Exaudi proxima 1757 ao\n"
            "Między Wielebnym X. Jakobem Maliszewskim Proboszczem y całym Konwentem Krasnickim "
            "Kanoników Regularnych Lateraneńskich Aktorem Sprawy z iedney a Pozwanym Uczciwym "
            "Macieiem Frugą Mieszczaninem Krasnickim z drugiey strony Sąd Ninieyszy przełożywszy "
            "sprawiedliwą y słuszną pretensyą Wielebnego X. Proboszcza y całego Konwentu Krasnickiego "
            "Aktora Sprawy iako świadczy skrypt Pozwanego dany na siebie Wielebnemu X. Proboszczowi "
            "że trzydzieści trzy korce żyta wyrobić na folwarku wszystkie które pozwany na własny "
            "obrócił potrzebę deklarował wypłacić w dwóch ratach czyli pieniędzmi rachuiąc korzec "
            "żyta po złotych sześć czyli ziarnem oddać którey asekuracyi do tych zadosyć nie uczynił "
            "y seląga na tę pretensyą nie dał Pozwany w czym okazywał się przed Sądem którey "
            "pretensyi wynosi suma złotych dwieście dwa groszy piętnaście na czym okazywał przed Sądem "
            "Pozwany że nie miał sposobności do wypłacenia tych pretensyi iako się przez skrypt "
            "asekurovał a że zaś na też sumę wyrażoną to iest zł 202 gr 15 ma też swoiey pretensyi "
            "Pozwany zł 26 gr 6 przyznaney którey odciągnąwszy zostanie się sumy zł 176 gr 9 "
            "co Pozwany czterema ratami wypłacić powinien Kon-"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 590,
        "numer_pozycji": "Poz. 590",
        "strona_pagina": "fol. 289r (dolna 260, do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Dekrety / Harmonogram 4 rat spłaty długu Macieja Frugi na rzecz Konwentu Kraśnickiego oraz rozliczenie pracy w winiarni klasztornej (1757–1759 r., karta odwrócona)",
        "osoby_podmioty": "Maciej Fruga [Fruga]; ks. Jakub Maliszewski [Maliszewski] proboszcz; Konwent Kraśnicki",
        "kwoty_podatki": "4 raty po 44 złp 2 gr; ordynaria po 15 gr miesięcznie przez 2 lata; 6 korcy / 3 korce żyta",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: dokończenie dekretu dla Konwentu Kraśnickiego — 4 raty po 44 złp 2 gr (Wniebowzięcie NMP 1757, Trzech Króli 1758, Wniebowzięcie 1758, Trzech Króli 1759) pod rygorem więzienia oraz rozliczenie pracy Macieja Frugi w winiarni Konwentu (15 gr miesięcznie).",
        "transkrypcja": (
            "[fol. 289r, dolna numeracja 260 — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "wentowi Krasnickiemu pierwszą ratę w tydzień post Festum Assumptionis Beatissimae "
            "Virginis Mariae in anno praesenti złotych 44 gr 2 Drugą ratę in crastino Festi "
            "Sanctorum Trium Regum 1758vo anno trzecią ratę post Festum Assumptionis Beatissimae "
            "Virginis Mariae eodem anno currenti zł 44 gr 2 Czwartą ratę in crastino Sanctorum "
            "Trium Regum 1759no anno zł 44 gr 2 Podług rat wyrażonych Pozwany Mieyski "
            "wypłacić Konwentowi Krasnickiemu powinien A gdyby iedney raty Pozwany według pierwszej "
            "raty zadosyć nie uczynił powinien będzie zasiąść więzienie poki nie uczyni satysfakcyi "
            "similiter y za każdą ratę ponieważ dosyć prorogacyi dla Pozwanego widząc iego "
            "niesposobność y wymówkę do satysfakcyi w przyznanych y sprawiedliwych pretensyach "
            "a że zaś Pozwany Maciey Fruga podał do Sądu swoie pretensye iako przez lat dwa "
            "robiąc w winiarni Konwentu Krasnickiego ordynaryi należącey za każdy miesiąc rachuiąc "
            "po groszy 15 nie odbierał y inne rzeczy uczynił korcy sześć która pretensya przy "
            "porachunku z Wielmożnym Imcią X. Proboszczem miała być akceptowana przeciwko "
            "pretensyi korcy trzydziestu trzech y korcy 3 żyta tudzież y innych pretensyi których "
            "Pozwany przy czwartey racie rekwirować powinien będzie gdzie według artykułu szóstego "
            "Magdeburskiego prawa iuramentem comprobare iako iego pretensye nie były przyjęte "
            "y akceptowane do porachunku z Wielmożnym Imcią X. Proboszczem Aktorem Sprawy a lubo "
            "Pozwany pierwszą ratę instantanee oddać y wyliczyć był powinien lecz widząc iego "
            "niesposobność Sąd Ninieyszy prorogował satysfakcyi Konwentowi Krasnickiemu przez Pozwanego "
            "który według dekretu uiścić w czasie powinien będzie mocą zwierzchności naszey przykazuiemy"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 591,
        "numer_pozycji": "Poz. 591",
        "strona_pagina": "fol. 289v (do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Obdukcje, wizje i inkwizycje / Obdukcja Frugów, wizja sadu Jakuba Wojciechowskiego oraz inkwizycja spadkowa Antoniego Trojczaka przeciw Krzysztofowi Rusakowi (1757 r., karta odwrócona)",
        "osoby_podmioty": "Paweł Fruga [Fruga]; Maciej Fruga [Fruga]; Józef Nowak [Nowak]; Wawrzyniec Tokarz [Tokarz]; Mikołaj Nowak [Nowak]; Jakub Wojciechowski [Wojciechowski]; Szymon Krzeszowski [Krzeszowski]; Franciszek Barankiewicz [Barankiewicz]; Szymon Szelichowski [Szelichowski]; Antoni Trojczak [Trojczak / Troyczak]; Jan Ćwiek [Ćwiek / Ćwieka]; Krzysztof Rusak [Rusak]; Tomasz Trojczak [Trojczak]",
        "kwoty_podatki": "4 złp / 8 złp (taksa płotu); 3–5 fur żerdzi",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: (1) obdukcja obrażeń Pawła i Macieja Frugów; (2) wizja szkody w sadzie Jakuba Wojciechowskiego przez świnię Szymona Szelichowskiego (ławnicy Szymon Krzeszowski i Franciszek Barankiewicz); (3) `Ad Instantiam Antonii Troyczak Inquisitio` — zeznanie Jana Ćwieki o spadku po dziadzie Krzysztofa Rusaka i matce Trojczakowej.",
        "transkrypcja": (
            "[fol. 289v — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "Paweł Fruga na kark czyli szyję iako mu ich nadskoczył Jozef Nowak y Wawrzyniec Tokarz "
            "Maciey zaś Fruga prezentował nosie raz siny o [oko?] dalej sinę Mikołaiowi Nowakowi "
            "ręce zadarte z trzech miejscach na lewey ręce na prawey y na łokciu w tych mieyscach "
            "rozdarł na nim przy tey okazyi kożuch y krzyż poniosł zdrapał w szyi długi na pięć "
            "calów od tego Mikołaia Nowaka\n"
            "Sub Eodem Actu\n"
            "Wizya gruntu czyli Jakuba Woyciechowskiego na którey Deputatowie byli Sławetni "
            "Mężowie Szymon Krzeszowski Franciszek Barankiewicz Ławnicy gdzie widzieli y doznali "
            "szkodę w gruncie Woyciechowskiego iak następuie płot z gruntu zruynowany przez Aktorową "
            "szkoda stała się to iest w drzewinie skory w sadzie Woyciechowskiego chmiel powyjadany "
            "przez ogrod Szymona Szelichowskiego tamże w tym sadzie trawa wytłuczona żerdziami z płotu "
            "ktora szkoda stała się z okazyi Szymona Szelichowskiego ponieważ przy tym płocie nie "
            "zagrodził tam świnia wlazła w sadzie y płot przez ruynowanie płotu aż aż Jabłonowski "
            "osten się dali Woyciechowskiemu powiedzieli wyrażeni Mężowie ponieważ tyczek na tym "
            "mieyscu było żerdzi for 3 pięć lub więcy płot zaś taxowany przez połowę "
            "zł 4 że stary aż do Nowy valoris zł 8\n"
            "Sub Eodem Actu\n"
            "Ad Instantiam Antonii Troyczak Inquisitio\n"
            "Testis Honesty Joannes Ćwieka sub Iuramento post exhibitas partes recognovit Jako "
            "Dziad Krzysztofa Rusaka był wstępny do tych dobr do których się sukcessorowie wpraszaią "
            "Antek Troyczak żona y Tomasza Trojczaka matki zaś Troyczakowey którey żadnego posagu "
            "od Oyca y Matki nie wzięli tylko na służbie będąc za mąż pochodziły o sukcesyi więc "
            "który został ociec Krzysztofa Rusaka u którey sukcesyi matka legowała cusem pola na "
            "matkę Troyczakową z którego gruntu ociec Krzysztofa Rusaka partycypował lat kilkanaście "
            "potym Krzysztof po Oycu swoim"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 592,
        "numer_pozycji": "Poz. 592",
        "strona_pagina": "fol. 290r (dolna 261, do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1757",
        "kategoria": "Inkwizycje i interogatoria / Dokończenie sprawy o grunty Rusaka, inkwizycja Macieja Frugi przeciw Józefowi Nowakowi oraz interogatoria Pawła Frugi przeciw żonie Nowaka (1757 r., karta odwrócona)",
        "osoby_podmioty": "Krzysztof Rusak [Rusak]; Maciej Fruga [Fruga]; Józef Nowak [Nowak]; Szymon Worogrodzki [Worogrodzki] z Zamościa; Paweł Fruga [Fruga]",
        "kwoty_podatki": "2 gr (wódka)",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: (1) dokończenie zeznania o gruntach i wołach po ojcu Krzysztofa Rusaka i dziadku Trojczakowej; (2) `Feria 6ta ante Dominicam Exaudi 1757` — inkwizycja Macieja Frugi przeciw Józefowi Nowakowi (zeznaje Szymon Worogrodzki z Zamościa); (3) `Interrogatoria Pauli Fruga contra Uxorem Josephi Nowak`.",
        "transkrypcja": (
            "[fol. 290r, dolna numeracja 261 — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "dotychczas partycypuie podczas zaś inkwizycyi dla zabieżenia w różnych danych "
            "oraz skryptach Urząd był do Xiąg Rewizyi y przystąpiwszy z Pola Zamek y wymieniawszy "
            "co widząc sąsiedztwo skryptu swego ważne asekuracyi dla dobrych względów sąsiedztwa "
            "ociec Krzysztofa po którego pojechawszy ludzie iakowiś nieutowani za bydło przywiedli go "
            "nazad do Kraśnika y parę wołów młodych przygnali na sprowadził y inne daniny o ten "
            "należały od Oyca Krzysztofa którego własne te woły były które za prowiant sprzedano "
            "a starych para wołów było po Dziadku Troyczakowej z teraźniejszą za to wszystko Rusaka "
            "spokoynie zaś pola która była za Jakuba tym ta była mianowana\n"
            "Feria 6ta ante Dominicam Exaudi proxima 1757 anno\n"
            "Ad Instantiam Mathiae Fruga Inquisitio contra Josephum Nowak\n"
            "Testis Honesty Simon Worogrodzki Incola Zamoyscensis Iuratus recognovit Jako będąc "
            "ia z kolegami w gospodzie iedni w karty u stołu grali w tym przyszła iakaś niewiasta "
            "siadła na stołku potym wyszedłszy z dachem Paweł Fruga poszedł w taniec tegom nie uważał "
            "czyli wszedł co przyszedłszy siadła czyli z inną ponieważ tey Matrony nie zna w krótkim "
            "czasie wyszedłszy Paweł Fruga tak zaraz poczęli go bić tego nie wiem z iakiey okazyi\n"
            "Interrogatoria Pauli Fruga contra Uxorem Josephi Nowak\n"
            "Który zeznał przed Sądem że będąc ia z żoną Jozefa Nowaka naprzod wypiliśmy z sobą "
            "za groszy dwa wódki w tym czasie rzekła do mnie żona Jozefa Nowaka mówiła te słowa "
            "do mnie że ia bardziey ciebie kocham iak tego za którego poszła ia iey odpowiedział "
            "to go zaduś potym zabawiła się ze mną do nocy y prowadzi mię y kazała do domu "
            "z którą poszedłem odprowadzając w tym będąc podpity dobrze idąc z nią przez łyski "
            "chciałem z nią wypełnić występek cielesności czego nie"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 593,
        "numer_pozycji": "Poz. 593",
        "strona_pagina": "fol. 290v (do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1752 / 1757",
        "kategoria": "Manifestacje, asekuracje i obdukcje / Spór Marcina Morela z Kazimierzem Młynarskim o wieprza za 24 złp, asekuracja Jana Elbiszowskiego (1757 r.) i obdukcja Pawła Frugi (1752 r., karta odwrócona)",
        "osoby_podmioty": "Marcin Morel [Morel]; Kazimierz Młynarski [Młynarski]; Franciszek Wstruskiowski [Wstruskiowski / Wstruskiowy]; Wojciech Wojciechowski [Wojciechowski / Woyciechowski]; Chłopowa Struska [Struska]; Jan Elbiszowski [Elbiszowski]; Paweł Fruga [Fruga]",
        "kwoty_podatki": "24 złp (za wieprza); czerwony złoty (asekuracya 1757)",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: (1) dokończenie manifestacji Marcina Morela przeciw Kazimierzowi Młynarskiemu o podkupienie wieprza za 24 złp u Franciszka Wstruskiowskiego oraz zeznanie Wojciecha Wojciechowskiego o targu u Chłopowej Struskiej; (2) asekuracja Jana Elbiszowskiego z 1757 r. (czerwony złoty na św. Annę); (3) `Feria 2da ante Dominicam Cantate 1752`: obdukcja obrażeń Pawła Frugi.",
        "transkrypcja": (
            "[fol. 290v — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "wał przeciw Uczciwemu Kazimierzowi Młynarskiemu oto iż on ważył się podkupować "
            "w wieprzu którego iutro stargował był Manifestant za zł 24 u Franciszka "
            "Wstruskiowskiego a że nie wiedział Manifestant będący zazdrością zdjęty z własnego "
            "profitu y zarobku iako swego niedopuszczając własnego iakoby z rąk Manifestantowi "
            "wydarł niego dziw o który postępek niegodziwy y zazdrości pełny wyrażony Manifestant "
            "przeciwko wspomnionemu Kazimierzowi Młynarskiemu protestuie się atque Iterum "
            "Manifestationis Raco Manifestant stawi świadectwo iako tenże stargował tego wieprza\n"
            "Sub Eodem\n"
            "Testis Honesty Adalbertus Woyciechowski sub Iuramento recognovit Jako słyszał że się "
            "Sławetny Marcin Morel zgodził za wieprza z Franciszkiem Wstruskiowym za złotych "
            "dwadzieścia cztery y piniądze nieść miał Marcin Morel który targ stał się między "
            "stronami u Chłopowey Struskiej na podsieniu albo też iakoby żaden go nie płacił "
            "zaś mięsa nikt przed wieczorem nie ważył ani słyszał\n"
            "Ja niżey wyrażony daię tę asekuracyą na siebie iako za moią transakcyą uczynioną "
            "w mieście Kraśniku powinienem odpowiedzieć y uczynić satysfakcyą od dnia czerwonego "
            "złotego na święto świętey Anny w roku teraźnieyszym 1757mo na co dla lepszey wiary "
            "ręką własną podpisuię się Datt ut supra w Kraśniku Jan Elbiszowski\n"
            "Feria 2da ante Dominicam Cantate proxima 1752 anno\n"
            "Obducya Pawła Frugi który prezentował w urzędzie zdrapanie krwawe na stronie lewey "
            "pod okiem prawym zdrapanie ieden w uchu lewym skron tenże obydwie"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 594,
        "numer_pozycji": "Poz. 594",
        "strona_pagina": "fol. 291r (dolna 262, do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1752",
        "kategoria": "Inkwizycje i areszty / Śledztwo z bójki Pawła Frugi z Nowakami oraz areszt deputata Marcina Morela na wieprza za 24 złp u Kazimierza Młynarskiego (1752 r., karta odwrócona)",
        "osoby_podmioty": "Antoni Pawłowski [Pawłowski]; Paweł Fruga [Fruga]; Mikołaj Nowak [Nowak]; Wawrzyniec Tokarz [Tokarz]; Wojciech Bieniawski [Bieniawski]; Krystyna Potokowiczowa [Potokowiczowa] wdowa; Józefowa Nowakowa [Nowakowa]; Marcin Morel [Morel] deputat; Kazimierz Młynarski [Młynarski]",
        "kwoty_podatki": "24 złp (wieprz w areszcie)",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: zeznania w sprawie bójki Pawła Frugi i Pawłowskiego z Nowakami (świadek Wojciech Bieniawski i wdowa Krystyna Potokowiczowa); poniżej (`Feria 6ta ante Dominicam Cantate [1752]`) areszt deputata Marcina Morela na wieprza za 24 złp u Kazimierza Młynarskiego oraz początek manifestacji Morela.",
        "transkrypcja": (
            "[fol. 291r, dolna numeracja 262 — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "dopiero na te słowa Pawłowski wbiegł między ów tumult broniąc Frugi którego "
            "Pawłowskiego uchwyciwszy Mikołay Nowak z tyłu go szarpał y kontusz na nim podarł "
            "z tamtąd rzucili się na Frugi uciekł do Tymcha którego pogonili Nowakowie z oycem "
            "y Wawrzyńcem Tokarzem więcey nie widział ani słyszał\n"
            "2dus Testis Honesty Adalbertus Bieniawski sub Conscientia recognovit Jako widział "
            "że Pawłowskiego Mikołay Nowak szarpał Pawłowskiego y kontusz na nim podarł y za łeb "
            "go chciał dostać tylko nie mógł ieno go po gębie podarł tego nie widział kto bił Frugi "
            "który wyrwawszy się uciekł do Tymcha y tam Nowakowie za nim pogonili\n"
            "Ex parte Pauli Fruga contra Nowakowi\n"
            "Testis Honesta Christina Potokowiczowa Vidua sub Conscientia recognovit Jako widziała "
            "że Paweł Fruga tańcował z żoną Jozefa Nowaka potem gdy się zgasili albo znikli "
            "nie mogła pojąć potem postawiwszy świecę obaczą na łóżku y Fruga pobity y na Nowaków "
            "żonki potyrkali dokąd poszli więcey nie widziała\n"
            "Actum In Officio Consulari et Scabinali Jurato Crasnicensi Feria 6ta ante Dominicam "
            "Cantate proxima [1752]\n"
            "Personaliter Stawający Sławetny Marcin Morel Deputat na Rzeszów Trybunału Zamoyskiego "
            "upraszał o areszt na wieprza którego był stargował za zł 24 w którym wieprzu podkupił "
            "Kazimierz Młynarski którego wieprza aby nie dał Kazimierz Młynarski puki się "
            "nie rozsądzi za Marcinem Morelem który areszt przyjęty y położony na tego wieprza "
            "u Kazimierza Młynarskiego przez urząd\n"
            "Sub Eodem Actu\n"
            "Przed tymże Urzędem y Aktami personaliter stawający Sławetny Marcin Morel Deputat "
            "na Rzeszowskie Trybunał Zamoyski solennie manifestował"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 595,
        "numer_pozycji": "Poz. 595",
        "strona_pagina": "fol. 291v (do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1752",
        "kategoria": "Inkwizycje / Zeznania Małgorzaty Łapiny, Marianny Starobratowej, Franciszka Barankiewicza i Szymona Nowackiego w sprawie bójki Pawła Frugi z Nowakami (1752 r., karta odwrócona)",
        "osoby_podmioty": "Małgorzata Łapina [Łapina]; Marianna Starobratowa [Starobratowa]; Józef Furman [Furman]; Paweł Fruga [Fruga]; Józefowa Nowakowa [Nowakowa]; Franciszek Barankiewicz [Barankiewicz]; Wawrzyniec Tokarz [Tokarz]; Mikołaj Nowak [Nowak]; Wojciech Nowak [Nowak]; Bartek Żołądź [Żołądź]; Maciej Fruga [Fruga]; Antoni Pawłowski [Pawłowski]; Szymon Nowacki [Nowacki]; Józef Nowak [Nowak]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: seria zeznań (Małgorzata Łapina, Marianna Starobratowa, Franciszek Barankiewicz, Szymon Nowacki) dotyczących tańca Pawła Frugi z żoną Józefa Nowaka w gospodzie i późniejszej bójki na dworze i w zaułku z udziałem Wawrzyńca Tokarza, Nowaków i Bartka Żołądzia.",
        "transkrypcja": (
            "[fol. 291v — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "2da Testis Małgorzata Łapina to samo zeznała co y mąż iey więcey nie zeznała "
            "tylko to żeśmy widzieli z mężem swym na dworze ludzi dwóch iedno siedziało "
            "drugi stało ale tego nie wiem kto ponieważ niegodna było nie mogłam uznać kto taki był\n"
            "3tius Testis Maryanna Starobratowa sub Conscientia recognovit Jako będąc u "
            "niedruha na gospodnie gdzie tańcował Drugi syn dwa razy z żoną Jozefa Nowaka "
            "potym prosto mnie na wódkę Jozef Furman potym ia zawoławszy żony Jozefa Nowaka "
            "a bez ten czas ia widziała w tym przybiegł Paweł Fruga ciągnął z izby w taniec "
            "ktorą ia pchnęła a ten do mnie żony Jozefa Nowaka z garścią albo ią bić y wyzywać "
            "na radę albo postaw potym Jozefa Nowaka żona z izby wyrwawszy się z rąk tego "
            "poszła na dwor a ten za nią ciągnął w taniec któremu rzekł inszy młodzieniec "
            "czyś ty głupi daj wódki iest iak drwa a ty ią ciągniesz w taniec więcey nie widziała "
            "ani słyszała\n"
            "Ex parte Pauli Fruga\n"
            "Testis Honesty Franciscus Barankiewicz sub Iuramento officii sui recognovit Jako "
            "widziałem że Paweł Fruga tańcował razy dwa z żoną Jozefa Nowaka potym tenże chciał "
            "ciągnąć ią do tańca ale nie chciała się schroniła się za starosta "
            "a gdy Paweł Fruga z żoną Jozefa Nowaka poszła za tem za stoł "
            "iż nie pił piwa z człowiekiem potym z tańca wyszedłszy rzekł "
            "na dwor dopiero tam stał się hałas pytaiąc się świadka co to za hałas "
            "z któremu powiedział ludzie żebią Frugi dopiero świadek wybiegł który bronił tego "
            "Frugi którego naybardziey bili się sami po zaułku Wawrzyniec Tokarz gdzie był "
            "Mikołay Nowak Woyciech Nowak y Bartek Żołądź y gdy odszedł Fruga Paweł gdzie "
            "postąpiwszy y dowiedziawszy się Maciey Fruga przybiegł broniąc syna którego ludzi "
            "w tym hałasie na karku trzymał słuchać więcey nie widział ani słyszał tamte z domu "
            "swego wyszedł wyganiał Nowaków broniąc Pawła Frugi którego syna Mikołay Nowak "
            "zadrapnął w gębie więcey nie widział ani słyszał\n"
            "Ex parte Antonii Pawłowski contra Nowaków\n"
            "Testis Honesty Simon Nowacki sub Conscientia recognovit Jako widział w gospodzie "
            "tańcował Paweł Fruga potym Pawłowski mowił do Szafrańskiego czego się tu kłócą "
            "Jozef Nowak żebym nie zabił Frugi w tym wyszedłszy Fruga na dwor Jozef zaś Nowak "
            "w nienawiści chcąc wziąć za łeb samego y do sługi swego y go bić z Wawrzyńcem "
            "Tokarzem naybardziey poniewierał Frugi w odzieży żołnierskiej a na Pawłowskiego "
            "go krzycząc żebym go y nie daję bić"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 596,
        "numer_pozycji": "Poz. 596",
        "strona_pagina": "fol. 292r (dolna 263, do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1752 / 1757",
        "kategoria": "Dublet mikrofilmowy / Powtórna karta z manifestacją Marcina Morela przeciw Kazimierzowi Młynarskiemu, asekuracją Jana Elbiszowskiego i obdukcją Pawła Frugi (1752/1757 r., karta odwrócona)",
        "osoby_podmioty": "Marcin Morel [Morel]; Kazimierz Młynarski [Młynarski]; Franciszek Wstruskiowski [Wstruskiowski / Wstruskiowy]; Wojciech Wojciechowski [Wojciechowski / Woyciechowski]; Chłopowa Struska [Struska]; Jan Elbiszowski [Elbiszowski]; Paweł Fruga [Fruga]",
        "kwoty_podatki": "24 złp (wieprz); czerwony złoty",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami (dublet/powtórny wpis karty z fol. 290v / skanu 593): manifestacja Marcina Morela przeciw Kazimierzowi Młynarskiemu o wieprza za 24 złp, zeznanie Wojciecha Wojciechowskiego, asekuracja Jana Elbiszowskiego z 1757 r. oraz obdukcja Pawła Frugi z 1752 r.",
        "transkrypcja": (
            "[fol. 292r, dolna numeracja 263 — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "wat przeciw Uczciwemu Kazimierzowi Młynarskiemu oto iż on ważył się podkupować "
            "w wieprzu którego był stargował Manifestant za zł 24 u Franciszka Wstruskiowskiego "
            "a że nie wiedział Manifestant będący zazdrością zdjęty z własnego profitu y zarobku "
            "niedopuszczając własnego iakoby z rąk Manifestantowi wydarł niego dziw o który "
            "postępek niegodziwy y zazdrości pełny wyrażony Manifestant przeciwko wspomnionemu "
            "Kazimierzowi Młynarskiemu protestuie się atque Iterum Manifestationis Raco Manifestant "
            "stawi świadectwo iako stargował tego wieprza\n"
            "Sub Eodem\n"
            "Testis Honesty Adalbertus Woyciechowski sub Iuramento recognovit Jako słyszał "
            "że się Sławetny Marcin Morel zgodził za wieprza z Franciszkiem Wstruskiowym za złotych "
            "dwadzieścia cztery y pieniądze nieść miał Marcin Morel który targ stał się między "
            "stronami u Chłopowey Struskiej na podsieniu albo też iakoby żaden go nie płacił "
            "zaś mięsa nikt przed wieczorem nie ważył ani słyszał\n"
            "Ja niżey wyrażony daię tę asekuracyą na siebie iako za moią transakcyą uczynioną "
            "w mieście Kraśniku powinienem odpowiedzieć y uczynić satysfakcyą od dnia czerwonego "
            "złotego na święto świętey Anny w roku teraźnieyszym 1757mo na co dla lepszey wiary "
            "ręką własną podpisuię się Datt ut supra w Kraśniku Jan Elbiszowski\n"
            "Feria 2da ante Dominicam Cantate proxima 1752 anno\n"
            "Obducya Pawła Frugi który prezentował w urzędzie zdrapanie krwawe na stronie lewey "
            "pod okiem prawym zdrapanie ieden w uchu lewym skron tenże obydwie"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 597,
        "numer_pozycji": "Poz. 597",
        "strona_pagina": "fol. 292v (do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1752",
        "kategoria": "Inkwizycje / Inkwizycja Macieja Frugi przeciw Nowakom (zeznania Walentego Szafrańskiego i Anny Młynarskiej) oraz Józefa Nowaka przeciw Pawłowi Frudze (zeznanie Mateusza Łapy, 1752 r., karta odwrócona)",
        "osoby_podmioty": "Nieboszczyk Sadowski [Sadowski]; Maciej Fruga [Fruga]; Walenty Szafrański [Szafrański]; Paweł Fruga [Fruga]; Antoni Pawłowski [Pawłowski]; Józef Nowak [Nowak]; Wawrzyniec Tokarz [Tokarz]; Franciszek Barankiewicz [Barankiewicz]; Wojciech Krzeszowski [Krzeszowski]; Anna Młynarska [Młynarska]; Mateusz Łapa [Łapa]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: (1) dokończenie zeznania o górze pustej przez 6 lat i grodzeniu przez Sadowskiego; (2) `Feria 4ta ante Dominicam Cantate 1752`: inkwizycja Macieja Frugi przeciw Nowakom — zeznania Walentego Szafrańskiego i Anny Młynarskiej o pobiciu Pawła Frugi aż pod dom cyrulika; (3) inkwizycja Józefa Nowaka przeciw Pawłowi Frudze — zeznanie Mateusza Łapy.",
        "transkrypcja": (
            "[fol. 292v — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "mieszkał potym Jacek ożeniwszy się pierwszą żoną lecz ią syndyk był z gory y trzymał "
            "tego nie pamiętam roku gdy ta góra pustkami sześć lat leżała tylko dla szkody y sąsiadów "
            "ma grodzić przez kilka lat nieboszczyk Sadowski y panowie inni y dęby y buczyna "
            "czyli korzenie było z dawna albo teraz więcey nie zeznał\n"
            "Actum Feria 4ta ante Dominicam Cantate proxima 1752 ao\n"
            "Inquisitiones ex parte Mathiae Fruga contra Nowaków\n"
            "1mus Testis Honesty Valentinus Szafrański sub Conscientia recognovit Jako widział "
            "że Paweł Fruga tańcował potym z tańca wyszedłszy szedł z Antonim Pawłowskim któremu "
            "zaszedłszy Jozef Nowak uderzył go na przód w gęby tego nie wiem co o siebie mówili "
            "potym z Wawrzyńcem Tokarzem przypadłszy porwał za łeb Frugę w tym ociec Jozefa "
            "y brat tudzież Jędrzey słomiany tulianek przypadłszy poczęli bić tego Frugi "
            "przyszedłszy żaden z nich kija nie miał w tym przybiegłszy świadek Franciszek "
            "Barankiewicz Woyciech Krzeszowski Antoni Pawłowski obronili Frugi który wyrwawszy się "
            "z rąk uciekł do cyrulika gdzie dogoniwszy go Nowak z synem y z Wawrzyńcem Tokarzem "
            "y tuliankiem bili go y słuchał czy umówił\n"
            "2dus Testis Honesta Anna Młynarska sub Conscientia recognovit Jako widziałam że "
            "Paweł Fruga stał z Jozefem Nowakiem y Wawrzyńcem Tokarzem y te słowa mówił Jozef Nowak "
            "mając na sobie kożuch do moiey żony w tym ia poszła na okno patrząc swego męża "
            "obejrzawszy się widziałam że Jozef Nowak uderzył w gęby Pawła Frugi a Wawrzyniec "
            "Tokarz porwał go za łeb y przygiął ku ziemi w tym ia pobiegła daci znać żonie iego "
            "aż na to mieysce syn iego bieży y pobił Macieya Frugi bronić syna więcey nie widziałam "
            "ani słyszałam\n"
            "Ex parte Josephi Nowak contra Paulum Fruga\n"
            "Testis Honesty Mathaeus Łapa sub Iuramento recognovit Jako słyszałem w nocy że "
            "szukali na dworze y krzyk był na podwórzu z żoną moią dwie ludzi widzieliśmy "
            "iedno siedziało drugie stało ludzie poszli drudzy ku stodole potym iedna osoba "
            "weszła śpiewając ale nie mogłem z żoną poznać kto taki ponieważ niewidno było "
            "przed samym końcem więcey nie widział ani słyszał"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 598,
        "numer_pozycji": "Poz. 598",
        "strona_pagina": "fol. 293r (dolna 263, do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1752",
        "kategoria": "Inkwizycje / Sprawa Wawrzyńca Tokarza z Marcinem Budzyńskim oraz inkwizycja Adama Sołoniaka przeciw Antoniemu Dudkowi o górę Sowińską i pożyczony kożuch (1752 r., karta odwrócona)",
        "osoby_podmioty": "Wawrzyniec Tokarz [Tokarz]; Marcin Budzyński [Budzyński]; Dawid Niewiadomy [Niewiadomy]; Adam Sołoniak [Sołoniak]; Antoni Dudek [Dudek]; Bartłomiej Żołądź [Żołądź]; Michał Grzywa [Grzywa]; Michał Sołoniak [Sołoniak]; Jakub Kaliski [Kaliski]; Maciej Fruga [Fruga]",
        "kwoty_podatki": "pół złota, krowa i baran; 3 złp za płot",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami: (1) zeznanie o ugodzie Wawrzyńca Tokarza z Marcinem Budzyńskim; (2) `Feria 6ta ante Dominicam Jubilate 1752` — inkwizycja Adama Sołoniaka przeciw Antoniemu Dudkowi o górę Sowińską i kożuch pożyczony od Jakuba Kaliski do Żabnowa (zeznania Bartłomieja Żołądzia, Michała Grzywy, Michała Sołoniaka i Macieja Frugi).",
        "transkrypcja": (
            "[fol. 293r, dolna numeracja 263 — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "Ex parte Laurentii Tokarz sub Eodem Actu\n"
            "Testis Dawid Niewiadomy zeznał Jako słyszał że się Wawrzyniec Tokarz zgodził "
            "z Marcinem Budzyńskim za śmierć kościelną żony y czworo sam Tokarz prosił świadka "
            "żeby przyszedł przy zgodzie na złote między stronami stanęła zgoda iednak "
            "w drodze gdy szli ubogą dał jeszcze pół złota przydał krowę y barana "
            "ów grzywny za grzybki płot opasał mu Tokarz zł 3\n"
            "Feria 6ta ante Dominicam Jubilate proxima 1752 anno\n"
            "Inquisitio ex parte Honesti Adami Sołoniak contra Antonium Dudek\n"
            "Testis Honesty Bartholomeus Żołądź sub Conscientia recognovit Jako iak mogę "
            "zapamiętać tak górę którą urząd nadał Dudkowi Antoniemu tego nie wiem czyli miał "
            "dług iaki y do tych czas miał Adam Sołoniak to zaś tylko pamiętam teraz miał "
            "tam grządki kilka podobno ieden rok bo ta góra przez lat kilkanaście pusto leżała "
            "kto chciał dla szkody ogrodził był nieboszczyk Sadowski z łany mieyski y czasem "
            "tamo bydło pasze paszano y tego nie wiem z iakiey racyi tam siał tego więcej nie znał\n"
            "2dus Testis Honesty Michael Grzywa sub Conscientia recognovit Jako góra którą "
            "teraz trzyma Antoni Dudek nadaną z urzędu zwała się Sowinska którą potym odebrał był "
            "w swoią opiekę kilka po ciotce swoiey rodzonej sowey nie tego zaś nie wiem czyli "
            "pożyczał kiedy Adam Sołoniak kożucha czyli mowił y iako ma za ten kożuch Adam Sołoniak "
            "do niego pretensyą\n"
            "3tius Testis Honesty Michael Sołoniak sub Conscientia recognovit Jako brat iego "
            "Adam Sołoniak pożyczył był kożucha od Jakuba Kaliski do Żabnowa gdy się tam żenił "
            "potym tenże kożuch przebit był y miał kilka na czynnosci gdy oddawał kożuch Adamowi "
            "mowił młynarz Adam Sołoniak nie chciał przyjąć tego kożucha że był rozdarty "
            "y deklarował ten kożuch zapłacić na niedzielę kwietnią potym iak poszedł z Kraśnika "
            "z żoną tak dotąd nie zapłacił kożuch Adamowi bratowemu\n"
            "Testis ex parte Antonii Dudek Mathaeus Fruga sub Conscientia recognovit Jako "
            "zapamiętam gdy urząd nadał Antoniemu Dudkowi zwała się Sowinska y tam miał"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 599,
        "numer_pozycji": "Poz. 599",
        "strona_pagina": "fol. 293v–294v (do góry nogami)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1752",
        "kategoria": "Raptularz inkwizycyjny z 1752 r. / Inkwizycje Trojczaka z Rusakiem, Budzyńskiego z Tokarzem (62 złp), Jana Lubartowskiego z Morelem (Wyźnica) i Wolfa Jeszkowica o podatek kahalny (1752 r., karta odwrócona)",
        "osoby_podmioty": "Kowalczyk [Kowalczyk]; Kazimierz Kowalski [Kowalski]; Łukasz Dunajski [Dunajski]; Antoni Trojczak [Trojczak / Troyczak]; Krzysztof Rusak [Rusak]; Jan Ćwiek [Ćwiek / Ćwieka]; Marcin Budzyński [Budzyński]; Wawrzyniec Tokarz [Tokarz]; Grzegorz Włoch [Włoch]; Jan Lubartowski [Lubartowski]; Marcin Morel [Morel]; Franciszek Czubrowski [Czubrowski]; Antoni Łazik [Łazik]; Staś Wyźnicki [Wyźnicki]; Mikołaj Orzeł [Orzeł]; Wolf Jeszkowic [Jeszkowic]; Tomasz Herszkowic [Herszkowic / Icko?]; Kryśkowicz [Kryśkowicz]; Stanisław Kowalski [Kowalski]",
        "kwoty_podatki": "62 złp (pole z chałupą); podatek kahalny",
        "opis_sprawy": "Karta zapisana i zmikrofilmowana do góry nogami (na dole strony nagłówek `Sextern tych Raptularz Inkwizycyj Zaczęwszy a d. 26 Martij 1752 Anno`): zeznania o egzekucji u Kowalczyka, inkwizycja o rolę na Podlesiu (Trojczak vs Rusak), zeznanie Grzegorza Włocha o sprzedaży chałupy za 62 złp (Budzyński vs Tokarz), śledztwo Jana Lubartowskiego przeciw Marcinowi Morelowi o wyjazd na Wyźnicę po trzcinę oraz inkwizycja Wolfa Jeszkowica przeciw Herszkowicowi o podatek kahalny.",
        "transkrypcja": (
            "[fol. 293v–294v, skan 599 = kontynuacja z 293v na 294r/294v — karta zapisana i zmikrofilmowana do góry nogami]\n"
            "chałupny gdzie przyszedłszy przynieśliśmy sobie chleba w domu jedząc rzekł "
            "Kowalczyk do nas idźcie do diabła rzekł y pytał nas od kogóż tu na exekucyą "
            "któremu odpowiedzieliśmy że iesteśmy z komissyi od Pana Starosty rzekł do świadków "
            "abym nie był taki złodziey iak on okradnieć piniądze to iak ma nieukraść piniędzy "
            "to iak suma na które słowa na prawdę zeznał Kazmierz Kowalski co samo poświadczył "
            "Żołnierz y Łukasz Dunajski więcey nie słyszeli ani zeznali\n"
            "Inquisitio ex parte Antonii Troyczak contra Christophorum Rusak\n"
            "Testis Joannes Ćwieka sub Iuramento recognovit Jako czworo pola osobno było "
            "babki Antoniowej Troyczakowey y Tomasza Trojczaka która to rola leży na Podlesiu "
            "a zaś ociec Rusaka z dziadem swoim y oyca Rusaka był wstępny do tych gruntów "
            "depenofact Rusaka zostawić tego\n"
            "Inquisitio ex parte Martini Budzyński contra Laurentium Tokarz Feria 4ta ante "
            "Dominicam Jubilate proxima 1752 anno\n"
            "Testis Gregorius Włoch sub Conscientia recognovit Jako słyszał że Wawrzyniec Tokarz "
            "zgodził się z Marcinem Budzyńskim za czworo pola z chałupą za zł 62 y zaraz Marcin "
            "Budzyński kazał swe gorzałki na litkup gdzie Wawrzyniec Tokarz mowił Marcinowi "
            "Budzyńskiemu że przedaię ci za pewne ty się staray o pieniądze może ci potym "
            "pieniądze podać a krowy nie dał a Marcin Budzyński powiedział lubo nie mam gotowych "
            "piniędzy ale krowę sprzedam to ci dam o tym więcej nie słyszał\n"
            "[dół strony — fol. 294v: Sextem tych Raptularz Inkwizycyj Zaczęwszy a d. 26 Martij 1752 Anno "
            "Actum Sabbatho ante Dominicam Laetare proxima]\n"
            "Inquisitio ex parte Joannis Lubartowski contra Martinum Morel\n"
            "1mus Testis Honesty Franciscus Czubrowski sub Iuramento recognovit Jako czasu pewnego "
            "lat temu kilka mieszkając komornym u Jana Lubartowskiego z tym że pojechaliśmy na "
            "Wyźnicę po trzcinę w który czas pojechał z nami Antoni Łazik na ten czas służący "
            "parobek tegoż Jana Lubartowskiego gdzie przyjachawszy my na Wyźnicę nakładliśmy "
            "trzciny na sanie temu parobku Antoniemu Łazikowi któremu Jan Lubartowski kazał "
            "jachać do domu swego a my obydwa zostaliśmy u Stasia Wyźnickiego czekając na inszą "
            "trzciny więcy żeby co brał na sanie tenże Antoni onego nie widziałem ani słyszał\n"
            "2dus Testis Laboriosus Nicolaus Orzeł parobek który za parobka przed tym służył "
            "u Jana Lubartowskiego zeznał pod sumieniem Jako ia będąc u Jana Lubartowskiego "
            "nie widziałem aby kiedy iaki owoc cudzy przywieść albo przynieść pod czas moiey służby "
            "u niego tylko konopnego słyszałem od nieboszczyka Staśka że mieli powiedzieć Janem "
            "Lubartowskim po siano wypis tego nie pamiętam potym za to siano na ten czas kiedy "
            "te słowa powiadał Staśko służyłem za parobka u Jana Lubartowskiego a Janek za "
            "parobka więcey nic nie zeznał ani słyszał\n"
            "Sub Eodem Actu Feria 2da ante Dominicam Quadragesimalis 1752 anno\n"
            "Inquisitio ex parte Infidelis Wolf Jeszkowicz contra [Tomasza? / Icka?] Herszkowica "
            "Testes Kryśkowicz Żołnierz Skarbowy Stanisław Kowalski Łukasz Dunajski qui sub "
            "Conscientia recognoverunt haec verba quae expressa in manifestatione sub eodem "
            "actu his verbis posłał Żyd starszy Kahalny na egzekucyą do Żyda Herszkowica po podatek"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 600,
        "numer_pozycji": "Poz. 600",
        "strona_pagina": "fol. 295r (dolna 264)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1759",
        "kategoria": "Deklaracje i manifestacje / Objęcie ćwierci po Hudrikowskiej przez Benedyka Kawkę oraz manifestacja Antoniego Ławickiego przeciw Matyaszowi Szymarczykowi o pobicie matki (1759 r.)",
        "osoby_podmioty": "Hudrikowska [Hudrikowska]; Benedyk Kawka [Kawka]; Antoni Ławicki [Ławicki]; Matyasz Szymarczyk [Szymarczyk]; Imć Pan Szubartowski [Szubartowski]; Szymon Ławnik [brak nazwiska]",
        "kwoty_podatki": "ćwierć roli bez sukcesora",
        "opis_sprawy": "Powrót do normalnej orientacji i roku 1759 (`Feria Tertia ante Dominicam Paschae Proxima 1759`): (1) deklaracja Benedyka Kawki o objęciu ćwierci po Hudrikowskiej bez sukcesora i ukontentowaniu magistratu; (2) manifestacja Antoniego Ławickiego przeciw Matyaszowi Szymarczykowi o pobicie matki na drodze publicznej; (3) początek zeznania deputowanych Szubartowskiego i Szymona ławnika.",
        "transkrypcja": (
            "[fol. 295r, dolna numeracja 264 — orientacja normalna]\n"
            "Actum Coram Officio Advocatiali Consulari et Scabinali Jurato Crasnicensi "
            "Feria Tertia ante Dominicam Paschae Proxima 1759 anno\n"
            "Uczciwa Hudrikowska którey teraz Uczciwy Benedyk Kawka z tym się odezwał "
            "iako tę ćwierć będzie trzymał y potym Magistrat cały chce ukontentować "
            "według prawa ponieważ ta ćwierć iest bez sukcesora\n"
            "Sub Eodem Actu\n"
            "Przed Urzędem y Aktami Ninieyszemi stawaiąc personaliter Antoni Ławicki "
            "solennie y iak naysolemniey manifestował się y protestował przeciwko Uczciwemu "
            "Matyaszowi Szymarczykowi oto iż nie widząc żadney racyi manifestanta matkę "
            "na drodze publiczney pobił uderzaiąc ią pięścią tak dobrze że prawie na śmierć "
            "iedney poszła ręki y w tym się oświadcza że nie winnie iest pobita w którey "
            "materyi inkwizycyami dowodzić będzie o co iterum atque iterum manifestatur "
            "exprimendo ieżeli by śmierć potkała tę matkę za to Matyasz Szymarczyk odpowie Sądowi\n"
            "Sub Eodem Actu\n"
            "Według skryptu Deputatemu Sławetnemu Imci Panu Szubartowskiemu y Szymonowi "
            "krasnickiego Ławnikowi krasnickiemu którzy zeznali iako według"
        ),
        "link_swa": UNIT_LINK
    }
]

for item in part24_scans:
    t = item["transkrypcja"]
    assert '...' not in t[10:-10], f"Wielokropek w transkrypcji skanu {item['nr_skanu']}!"

main_data.extend(part24_scans)
assert len(main_data) == 600, f"Oczekiwano 600 skanów, jest {len(main_data)}"

with open('/home/ubuntu/workspace/Gen/main_data_j17_part24.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j17_part24.json: {len(main_data)} skanów.")
