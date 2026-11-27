# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j20_part5.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989914"
SYGN = "35/40/0/1/20"

part6_scans = [
    {
        "nr_skanu": 126,
        "numer_pozycji": "126",
        "strona_pagina": "fol. 62r (62)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Dekrety: dług z cyrografu i apelacja Dziwanowskiego",
        "osoby_podmioty": "Żyd Jakub Jozwowicz, Żyd Jakub Koplowic [?], Wojciech Kochanowski, Tomasz Kochanowski, Maciej Bielaszkowic [Błaszkowicz], Wojciech Dziwanowski [Dzierżanowski], Stanisław Nawrocki, Kobierski",
        "kwoty_podatki": "fl 12; 2 grzywny",
        "opis_sprawy": "Dekret w sprawie Żyda Jakuba Jozwowicza (działającego za Jakuba Koplowica [?]) przeciw Wojciechowi Kochanowskiemu o fl 12 długu z cyrografu za Tomasza Kochanowskiego (kara 2 grzywien i 3 dni więzienia); poniżej wyrok w sprawie Wojciecha Dziwanowskiego [Dzierżanowskiego] przeciw Stanisławowi Nawrockiemu i zięciowi jego Kobierskiemu (odrzucenie apelacji z powodu niezapłacenia salarium).",
        "transkrypcja": """62.
Inter perfidum Jacobum Jozwowicz Actorem et Albertum Kochanowski Citatum.
Decretum.
W sprawie o dług pozostały według Ceregrafu napisanego przez Żyda Jakuba Koplowica [?] a Aktora a Tomasza Kochanowskiego intentowanej, Sąd niniejszy nakazuje aby pozwany Kochanowski porachowawszy się należycie resztę długu złotych dwanaście niektóry czas niepłacone zaptacić powinien. A za nieposłuszeństwo za tydzień pod winą grzywien dwóch y z więzieniem bez żadnego odwłóczenia aby zasiadł y nakłady aby oddał. A z Aktorem Żydem zostawiając sobie zdrowe prawo in foro fori. Który Dekret strony przyjęły y do Akt zapisano iest.

Inter Mathiam Bielaszkowic Actorem [tytuł przerwany].

Inter Albertum Dziwanowski [Dzierżanowski] Actorem et Stanislaum Nawrocki Citatum.
W sprawie na dzisiejszym terminie z przypozwu do Bosu Urzędowego Dekretowej przypadłej przez sław. Stan. Nawrockiego iako Ojca y Plenipotenta zięcia swego Kobierskiego pozwanemu sław. Dziwanowskiemu intentowanej, Sąd niniejszy przesłuchawszy kontrowersji stron... iż Aktor apellował sobie od dekretu, od apelacji nie zapłaciwszy do słońca zachodu należytego salarium, czyni to wszystko in ludibrium Sądu, przeto ta apelacja nullitatis subiacere ma decidi y aby tenże Citatus Dziwanowski w nakładach na wedle strony przysądzonej według Dekretu dosyć uczynił non recedendo sub poena bannitionis in instanti publicandae na karni. Co do Akt iest przyjęto y zapisano.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 127,
        "numer_pozycji": "127",
        "strona_pagina": "fol. 62v (62v)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Spór Nawrockiego z Dziwanowskim i pobicie Mantemberka",
        "osoby_podmioty": "Stanisław Nawrocki, Wojciech Dziwanowski [Dzierżanowski], Aleksander Mantemberk, Wojciech Jurdzik",
        "kwoty_podatki": "-",
        "opis_sprawy": "Sprawa Stanisława Nawrockiego przeciw Wojciechowi Dziwanowskiemu o rzeczy wyszczególnione w rejestrze (dylacja do tygodnia); poniżej sprawa Aleksandra Mantemberka przeciw Wojciechowi Jurdzikowi o zabranie konia i zadanie ran (obdukcja ran, dylacja na świadków).",
        "transkrypcja": """62v.
Inter Stanislaum Nawrocki Actorem et Albertum Dziwanowski [Dzierżanowski] Citatum.
W sprawie z przypozwu na dzisiejszym terminie przypadającej sław. Dziwanowskiemu przez sław. Stan. Nawrockiego o to opisywane wiele rzeczy w Regestrze specyfikowanych intentowanej, Sąd niniejszy przesłuchawszy kontrowersji, ponieważ pozwany nie zna się jako proponował in scriptis nieznając się aby miał od córki z domu jego zabierać rzeczy, a Aktor zaś na wywód idzie niewinności swojej, Sąd niniejszy pozwala im ab actu praesenti do tygodnia. Co obie strony przyjęły y do Akt zapisano.

Inter Alexander Mantemberk Actorem et Albertum Jurdzik Citatum.
Skarżył się Aktor iż w kupiectwie wyjechał, a na pozwanego Citatus nie zna się do tego któremu konia wziął, po który Jurdzik przyszedłszy który niesłusznie zająwszy Mantemberk pozwanemu o to tego prośby Aktorowi rany zadał iako obdukcja iest zapisana. Sąd niniejszy daje Dylację ab actu praesenti za tydzień, dokąd puki się Mantemberk nie powróci z probostwem y z świadectwem aby z gotowością stanęli.

Protestatio Contra Albertum Jurdzik.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 128,
        "numer_pozycji": "128",
        "strona_pagina": "fol. 63r (63)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Spór o czary (Bartoszek, Babarczyk, Zychko vs Wilk) i długi",
        "osoby_podmioty": "Wojciech Bartoszek [Bartłomiej], Stanisław Babarczyk, Wojciech Zychko, młynarz Bartłomiej Wilk, Maciej Bielaszkowic [Błaszkowicz], Grudniowicz, wdowa Anna Kotifera [Kołodziejka], Jan Okoń [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Proces Wojciecha Bartoszka, Stanisława Babarczyka i Wojciecha Zychki przeciw młynarzowi Bartłomiejowi Wilkowi o oszczerstwo o spalenie młyna i złodziejstwo (sąd wyznacza 2 tygodnie dylacji); sprawa Macieja Bielaszkowica przeciw rękojemcom za Grudniowicza; skarga wdowy Anny Kotifery [Kołodziejki] przeciw Janowi Okoniowi [?] o pobicie wieprza i obelgi.",
        "transkrypcja": """63.
Inter Albertum Bartoszek, Babarczyk et Alber. Zychko Actores et Molendinatorem Bartolomeum Wilk Citatum.
Skarżył się Aktor Bartoszek z przytomnością to iest z Stan. Babarczykiem y Wojciechem Zychkiem Przedmieszczanami Kraśnickimi o spalenie młyna, że ich Młynarz niesłusznie turbuje żałując się do tego iż y oni nie znają, poza oni zaś Wilk młynarz iż za gotowi przysięgą y świadectwem pokazać. Sąd niniejszy daje im rekollekcją na odwód y wywód obiema stronami ab Actu praesenti do niedziel dwóch żeby obie strony z gotowością wszelaką stanęli na termin zawity. Co obie strony przyjęły y do Akt zapisano, y przy tym złodziejstwa aby im dowodzili, co Aktorowie gotowi przysięgą deklarowali się gotowi przeciw złodziejstwa.

Inter Mathiam Bielaszkowic Actorem et Fideiussores Grudniowicza.
W sprawie z przypozwu na dzisiejszym terminie przypadającej sławetnych Rękojmiów przez sław. Macieja Bielaszkowica intentowanej, Sąd niniejszy stosując się do pierwszego Dekretu że ci Rękojmiowie za Grudniowicza ręczyli y nie dosyć czynią Dekretowi, Sąd niniejszy Wójtowski daje relację rękojemcom do tygodnia aby za tydzień summę tę którą Aktor Bielaszkowic pozywa zapłacili. Co do Akt iest zapisano.

Inter Annam Kotiferam Viduam Actricem et Joannem Okon [?] Citatum.
Skarżyła się Aktorka Kołodziejka na Okonia pozwanego o pobicie wieprzka y nieuczciwe słowa co na Aktorkę wołał. Iż się pozwany Okoń nie zna do tego, Sąd niniejszy odkłada tę sprawę do poniedziałku na inkwizycję.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 129,
        "numer_pozycji": "129",
        "strona_pagina": "fol. 63v (63v)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Obdukcja sługi miejskiego i dekret z 19 X 1684 r.",
        "osoby_podmioty": "Jan Okoń [?], Anna Kotifera, sługa miejski Marcin Pietruszczak, wójt Ubald Janaszkowicz, ławnicy Paweł Słomkowski, Sebastian Banaszowicz, Marcin Kurc [?], Wojciech Grzymek, Maciej Woluk [Wolski], Stanisław Nawrocki, Wojciech Dziwanowski",
        "kwoty_podatki": "3 grzywny",
        "opis_sprawy": "Dokończenie dekretu z Okoniem; obdukcja krwawych ran na czole sługi miejskiego Marcina Pietruszczaka (w domu wójta Ubalda Janaszkowicza przed ławnikami Pawłem Słomkowskim i Sebastianem Banaszowicem), zadanych przez Marcina Kurca [?]; sesja z 19 X 1684 r. (w dzień św. Jana Kantego): sprawa Wojciecha Grzymka przeciw Maciejowi Wolukowi [Wolskiemu] o świnie i gęsi w rzepie (kara 3 grzywien i 3 dni); dylacja w sprawie Nawrockiego z Dziwanowskim.",
        "transkrypcja": """63v.
... za jego nieposłuszeństwo tedy aby grzywnę zapłacił y do więzienia zasiadł. Co do Akt iest zapisano.

Obductio vulnerum Martini Pietruszczak Bedelli Civitatis.
Do Urzędu Wójtowskiego y Ławniczego Przysięgłego Kraśnickiego oblicznie przyszedłszy do Domu P. Ubaldego Janaszkowicza Wójta y Sędziego Kraśnickiego Uczciwy Marcin Pietruszczak sługa Miejski przy bytności sławetnych Panów Pawła Słomkowskiego y Sebastiana Batuszowica Ławników przysięgłych swój raz takowy prezentował: Naprzód raz krwawy przecięty w członku aż do kości nad lewem okiem, po tymże razem y drugi niewielki krwawy w tych razach winę dał Marcinowi Kurcowi [?]. Co do Akt iest przyjęto y zapisano.

Actum Feria Sexta ipso die S. Joannis Kantii proxima 1684 Die 19 Octobris.
Inter Albertum Grzymek Actorem et Mathiam Woluk [Wolski] Citatum.
W sprawie na dzisiejszym terminie o uczynienie szkody w rzepie Aktora... po woli... przez relację ławników... Sąd nakazuje aby pozwany Woluk szkodę nagrodził y winy grzywien trzy oddał oraz 3 dni więzienia, co obie strony przyjęły.

Inter Stanislaum Nawrocki Actorem et Albertum Dziwanowski Citatum.
Dana iest stronom dylacja na inkwizycję obu stron.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 130,
        "numer_pozycji": "130",
        "strona_pagina": "fol. 64r (64)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Dekrety przeciw Dziwanowskiemu, sprawa Kudrelika i Kotifery",
        "osoby_podmioty": "Stanisław Nawrocki, Wojciech Dziwanowski [Dzierżanowski], Kobierski, Maciej Bielaszkowic [Błaszkowicz], Maciej Kudrelik, Wojciech Biegajczyk [?], Anna Kotifera [Kołodziejka], Jan Okoń [?]",
        "kwoty_podatki": "grzywny 2; fl 15; grzywny 6",
        "opis_sprawy": "Dwa dekrety przeciw Wojciechowi Dziwanowskiemu (w sprawie Stanisława Nawrockiego i Kobierskich — nakaz osadzenia w skarbnicy za grzywny 2 i fl 15; oraz w sprawie Macieja Bielaszkowica o czynsz z gruntów Nawrockiego); sprawa Macieja Kudrelika przeciw Wojciechowi Biegajczykowi [?] o pobicie czeladzi; wyrok nakazujący Annie Kotiferze przeprosić sąsiadów za wyzwiska pod karą 6 grzywien i tygodnia więzienia.",
        "transkrypcja": """64.
... żeby sobie pars Citata prosiła aby do bytności P. Wójta Kraśnickiego... tedy Sąd niniejszy pozwolił Dylacji do poniedziałku.

Sub eodem Actu inter Dziwanowski.
Sąd niniejszy zważywszy sław. Stan. Nawrockiego stanąwszy oblicznie żądał z pozwanego Dziwanowskiego że dosyć nie uczynił Dekretowi żeby z Kobierskimi małżonkami miał był in instanti oddać ziemię y koszty. Sąd niniejszy Wójtowski nakazuje aby w skarbnicy siedział za grzywny 2 y nakłady fl 15 oddał.

Inter Mathiam Bielaszkowic Actorem et Albertum Dziwanowski Citatum.
Sąd niniejszy nakazuje aby czynsz z gruntów P. Nawrockiego należyty zapłacił do dnia trzeciego pod egzekucją.

Inter Mathiam Kudrelik Actorem et Albertum Biegajczyk [?] Citatum.
Skarżył się Aktor na pozwanego o pobicie czeladzi... Sąd daje dylację do poniedziałku na inkwizycję.

Inter Annam Kotiferam Viduam et Joannem Okon [?] Citatum.
Skarżyła się Aktorka Kołodziejka na pozwanego Okonia o nieuczciwe słowa... Sąd nakazuje aby się zaraz przeprosili y za obrazę grzywien 6 oraz tydzień więzienia, ieśli by nie przeprosiła.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 131,
        "numer_pozycji": "131",
        "strona_pagina": "fol. 64v (64v)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Zeznania w sprawie kradzieży drzewa i kupna konia",
        "osoby_podmioty": "Stanisław Magurowski [?], Jan Nowak, Stanisław Decik [?], Szymon [chłop], Szymon Starobrat [?], Babarczyk, wdowa Luthko [?], Wojciech Dziwanowski",
        "kwoty_podatki": "30 złp",
        "opis_sprawy": "Sprawa Stanisława Magurowskiego [?] przeciw Janowi Nowakowi o zabranie drzewa; zeznanie przedmieszczanina Stanisława Decika [?] o chłopie Szymonie wiozącym drzewo; zeznanie Szymona Starobrata [?] na rzecz wdowy Luthko [?] o kupnie konia od Babarczyka za 30 złp; na dole tytuł Publicatio Alberti Dziwanowski.",
        "transkrypcja": """64v.
Inter Stanislaum Magurowski [?] Actorem et Joannem Nowak Citatum.
Skarżył się Magurowski o zabranie drzewa przez pozwanego. Citatus Nowak nie zna się do tego, Aktor świadectwem produkuje.

Testimonium ex Stanislai Magurowski.
Uczciwy Stanisław Decik [?] Przedmieszczanin K[raśnicki] pod przysięgą zeznał temi słowy: Chłop mój iedzie... z lasu... wzięli sobie drzewa na łaskę... do domu swego pojechał, ale nie wiem skąd to drzewo, czy Magurowskiego czy nie więcej nie wiem. Co do Akt iest zapisano.

Testimonium ex parte Luthko [?] Viduae.
Szymon Starobrat [?] pod przysięgą zeznał żem przedał konia za 30 złp, mówiąc że Babarczyk kupił za złotych trzydzieści... więcej nie pamiętam. Co do Akt iest przyjęto.

Publicatio Alberti Dziwanowski.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 132,
        "numer_pozycji": "132",
        "strona_pagina": "fol. 65r (65)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Spór o czary i spalenie młyna (27 X 1684)",
        "osoby_podmioty": "Wojciech Bartoszek, Stanisław Babarczyk, Bartłomiej Wilk (młynarz), żona Bartłomieja Wilka, Szymon Grzebieniowiec [?], córka Bartoszka",
        "kwoty_podatki": "-",
        "opis_sprawy": "Protokół z piątku w wigilię śś. Szymona i Judy 1684 r. (27 X 1684): w sprawie Wojciecha Bartoszka i Stanisława Babarczyka przeciw młynarzowi Bartłomiejowi Wilkowi i jego żonie (którzy pomawiali córkę Bartoszka i Babarczyka o podłożenie ognia i spalenie młyna przez czary) pozwany nie dostawił świadka Szymona Grzebieniowca [?], więc sąd wyznacza termin zawity za tydzień na dostawienie świadków i czeladzi.",
        "transkrypcja": """65.
Actum Feria Sexta in Vigilia SS. Simonis et Judae Apostolorum prox. 1684 A.
Inter Albertum Bartoszek Actorem et...
W sprawie między Aktorem Wojciechem Bartoszkiem y Stan. Babarczykiem Aktorami a Młynarzem Bartłomiejem Wilkiem y żoną jego pozwanym na dzisiejszym terminie przypadającej na którym terminie miał pozwany Szymona Grzebieniowca [?] dowód y świadectwo odprawić na które się zabierało iż Aktorowie mianowicie Babarczyk y córka Bartoszkowa mieli jakby podłożywszy ogień z czarostwem spalić młyn, na co teraz pozwany nie stawił świadków ani żadnego fundamentu ani dowodu, tylko upornie sam twierdzi że oni spalili. Sąd niniejszy pozwala jeszcze pozwanemu Dylacji do tygodnia aby dowody i świadków stawił oraz czeladź wszelaką y żonę na ten termin stawił y niewinność pokazali. Co do Sądu przyjęto y zapisano iest.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 133,
        "numer_pozycji": "133",
        "strona_pagina": "fol. 65v (65v)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Kondemnata na rękojemcach i sprawy Marcina Rymarczyka",
        "osoby_podmioty": "Maciej Bielaszkowic [Błaszkowicz], rękojemcy za Grudniowica (młynarz Jakub Młynarczyk), Marcin Rymarczyk, Wojciech Nogaj, ławnik Sebastian Banaszowicz, Maciej Pełka, Stefan [?] Pełka",
        "kwoty_podatki": "-",
        "opis_sprawy": "Kondemnata w sprawie Macieja Bielaszkowica przeciw rękojemcom za Grudniowica (szczególnie przeciw młynarzowi Jakubowi Młynarczykowi); sprawa Marcina Rymarczyka przeciw Wojciechowi Nogajowi o szkodę w bydle (relacja ławnika Banaszowica, nakaz zwrotu krowy); sprawa Marcina Rymarczyka przeciw Maciejowi Pełce o sukcesję po zmarłej żonie.",
        "transkrypcja": """65v.
Inter Actorem Bielaszkowic Actorem et Fideiussores Grudniowica.
Sąd niniejszy przychylając się do pierwszego Dekretu między sław. Bielaszkowicem Aktorem a Pozwanymi Rękojmiami Grudniowica, iż mimo dekretu nie dosyć uczynili, osobliwie młynarz mianowicie Jakub Młynarczyk, przeto sąd kondemnatę na nich dekretuje z dóbr i osób ich pod egzekucją urzędową.

Inter Martinum Rymarczyk Actorem et Albertum Nogaj Citatum.
W sprawie o szkodę w bydle uczynioną przez Aktora Rymarczyka przeciw Wojciechowi Nogajowi, Sąd niniejszy stosując się do Relacji sław. Batuszowica Ławnika nakazuje aby pozwany Nogaj Aktorowi krowę oddał bez żadnej dylacji pod winą y nakłady.

Inter Martinum Rymarczyk Actorem et Mathiam Pełka Citatum.
W sprawie między Marcinem Rymarczykiem Aktorem a pozwanym Pełką o sukcesję po zmarłej żonie, odesłano do wywodu prawnego z ojczyzny.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 134,
        "numer_pozycji": "134",
        "strona_pagina": "fol. 66r (66)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Moderacja Rymarczyka z Pełką, sprawa ks. Smarzyńskiego i Rodzonka",
        "osoby_podmioty": "Marcin Rymarczyk, Maciej Pełka, Maciej Błaszkowicz, Jan Młodowski [?], Andrzej Nogaj, Jakub Wojtalik, ks. Smarzyński (Kanonicy Regularni), Wojciech Nogaj, Stanisław Sobel [?], Bartłomiej Rodzonek",
        "kwoty_podatki": "-",
        "opis_sprawy": "Odesłanie sprawy Marcina Rymarczyka z Maciejem Pełką do moderacji przyjacielskiej w domu P. Błaszkowica z arbitrem; sprawa Andrzeja Nogaja przeciw Jakubowi Wojtalikowi o tymfy i pobicie czeladzi; sprawa ks. Smarzyńskiego z konwentu Kanoników Regularnych przeciw Wojciechowi Nogajowi o wyderkaf z gruntów; przysięga oczyszczająca Bartłomieja Rodzonka w sprawie Stanisława Sobla [?] o wieprzka.",
        "transkrypcja": """66.
Sąd niniejszy z jednej i drugiej strony kontrowersji wysłuchawszy w tej sprawie na moderacją przyjacielską to iest w domu sław. P. Błaszkowica z arbitrem Janem Młodowskim [?] odesłał, co do Akt jest zapisano.

Inter Andream Nogaj Actorem et Jacobum Wojtalik Citatum.
W sprawie między Aktorem Nogajem a Wojtalikiem o tymfy i pobicie czeladzi, Sąd daje dylację do poniedziałku blisko przyszłego aby się pogodzili.

Inter Reverendum Smarzyński Conventus Crasn. Canonicorum Regularium Actorem et Albertum Nogaj Citatum.
W sprawie o wyderkaf z gruntów kamieńskich aby tenże pozwany Nogaj dokument pokazał dla informacji sądowej do poniedziałku blisko przyszłego.

Inter Stanislaum Sobel [?] Actorem et Bartolomaeum Rodzonek Citatum.
Ponieważ pozwany Rodzonek przysięgą swoją potwierdził iż tego wieprzka nie zabrał, Sąd czyni go wolnym od pozwu.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 135,
        "numer_pozycji": "135",
        "strona_pagina": "fol. 66v (66v)",
        "sygnatura": SYGN,
        "data_rok": "1684",
        "kategoria": "Obdukcja Jakuba Chruścika (28 X 1684) i sesja z 29 X 1684",
        "osoby_podmioty": "Wojciech Kudrelik, Wawrzyniec Brzęk [?], Wojciech Szocik [?], wójt Jan Koryca [?], podwójci Paweł Stankowski, ławnik Sebastian Banaszowicz, Jakub Chruścik [?], Jakub Żyta [?], Maciej Bielaszkowic, rękojemcy za Grudniowica",
        "kwoty_podatki": "-",
        "opis_sprawy": "Uwolnienie Wawrzyńca Brzęka [?] od pozwu Wojciecha Kudrelika; sesja z soboty w święto śś. Szymona i Judy 1684 r. (28 X 1684): obdukcja ran młodzieńca Jakuba Chruścika [?] (na prośbę Wojciecha Szocika [?], przez podwójciego Pawła Stankowskiego i ławnika Sebastiana Banaszowica) — rana cięta na głowie aż do błony mózgowej i na prawej nodze zadane przez Jakuba Żytę [?]; sesja z 29 X 1684 r. w sprawie Bielaszkowica z rękojemcami Grudniowica.",
        "transkrypcja": """66v.
Inter Albertum Kudrelik Actorem et Laurentium Brzęk [?] Cit.
Ponieważ Aktor nie próbował niczym aby miał pozwanego Brzęka o szkodę winić, tedy Sąd uwalnia pozwanego od ekspensów.

Actum Die Sabbatino in Festo SS. Simonis et Judae Apostolorum A. 1684.
Obductio Vulnerum Adolescentis Jacobi Chruścik [?].
Na affektacją Wojciecha Szocika [?] byli deputowani z ramienia sław. P. Jana Korycy [Ubalda Janaszkowicza] Wójta y Sędziego Kraśnickiego do domu pomienionego na oglądanie razów, to iest sław. P. Paweł Stankowski i Sebastian Batuszowicz Ławnicy Przysięgli Kraśniccy taką relacją uczynili: Naprzód na głowie cięta otworzysta rana w kość aż do błonki mózgowej, na prawej nodze rana cięta y siniec, w tych razach winę dali Jakubowi Życie [?].

Actum Feria Secunda ante Festum Omnium Sanctorum prox. 1684 Die 29 Octobris.
Inter Actorem Bielaszkowic Actorem et Fideiussores Grudniowica Citatos.
Przychylając się do pierwszego Dekretu Sąd nakazuje egzekucję na dobrach rękojemców.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 136,
        "numer_pozycji": "136",
        "strona_pagina": "fol. 67r (67)",
        "sygnatura": SYGN,
        "data_rok": "1686",
        "kategoria": "Elekcja władz miejskich na rok 1686 (12 I 1686)",
        "osoby_podmioty": "Maciej Bielaszkowic [Błaszkowicz], Dorota Zamoyska (kasztelanowa kijowska, wdowa), komisarze szl. Jakub Łębowski [?], Kazimierz Toruński [?], rajcy rezydujący Paweł Stankowski, Stanisław Grymuza [Gomuza], starszy cechów Jerzy Gucki",
        "kwoty_podatki": "-",
        "opis_sprawy": "Uroczysta elekcja magistratu kraśnickiego na rok 1686 odbyta w sobotę po Trzech Królach 12 stycznia 1686 r. w domu rajcy Macieja Bielaszkowica: z ramienia pani dożywotniej Doroty Zamoyskiej komisarze szl. Jakub Łębowski [?] i Kazimierz Toruński [?] wyznaczają dwóch rajców rezydujących — Pawła Stankowskiego i Stanisława Grymuzę [Gomuzę], a wójt z ławnikami wybierają starszego cechów Jerzego Guckiego na trzeciego rajcę.",
        "transkrypcja": """67.
ANNUS 1686tus.
Electio Solennis et laudabilis magistratus civilis Crasnicensis in Domo Famati Mathiae Bielaszkowic Consulis Crasnicensis in praesentia totius Magistratus et Communitatis celebrata Die Sabbati post Festum Trium Regum 12da Januarii Anno praesenti.
Et in primis ex Brachio Illustrissimae ac Magnificae Dnae Dorotheae Illustris ac Magnifici Dni olim Stephani [Martini?] Zamoyski Castellanissae Kiioviensis Relictae Viduae Dnae in Crasnik advitalis Generoso Jacobo Łębowski [?] et Casimiro Toruński [?] ad hanc Electionem ex Brachio supradictae Illustrissimae ac Magnificae Dnae demisso elegerunt Duos Consules Residentes Famatum Paulum Stankowski et Stanislaum Grymuza [Gomuza].
Advocatus cum Scabinis Lateri suo assidentibus Elegerunt in Consulem Residentem Famatum Georgium Gucki Archimagistrum Contuberniorum...""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 137,
        "numer_pozycji": "137",
        "strona_pagina": "fol. 67v (67v)",
        "sygnatura": SYGN,
        "data_rok": "1686",
        "kategoria": "Elekcja ławników, egzaktorów i cechmistrzów (12 I 1686)",
        "osoby_podmioty": "Sebastian Batusiowic [Banaszowicz], Szymon Kościński, Wojciech Kanaszkowicz, Marcin Sitarski, Jan Barankowicz, Stanisław Solecki, Stanisław Szczerkowicz, Adam Potocki, Stanisław Reszka, Stanisław Kucharski, Stanisław Grymuza, Beszkowic minor, Tomasz Paśkowic [?], Jan Barankowicz minor, Paweł Stankowski, Maciej Strzyżowski minor",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie elekcji z 12 I 1686 r.: pospólstwo wybiera rajcą Sebastiana Batusiowica [Banaszowica]; zaprzysiężenie ławników (Szymon Kościński, Wojciech Kanaszkowicz, Marcin Sitarski, Jan Barankowicz, Stanisław Solecki, Stanisław Szczerkowicz, Adam Potocki); wybór Szymona Kościńskiego na asesora do Trybunału Zamojskiego; wybór egzaktorów (Stanisław Reszka, Stanisław Kucharski, Jan Barankowicz) oraz cechmistrzów szewców, kuśnierzy, krawców, kowali i tkaczy.",
        "transkrypcja": """67v.
... totaque Communitas Elegerunt in Consulem sibi Sebastianum Batusiowic [Banaszowicz].
Scabini Antiqui: Simon Kościński et Albertus Kanaszkowicz, Martinus Sitarski, Joannes Barankowicz, Stanislaus Solecki, Stanislaus Szczerkowicz et Adamus Potocki Qui supra Officium Scabinatus sui corporale Iuramentum praestiterunt.
In Assessorem ad Iuditia Tribunalitia Zamoscensia Honoratum Simonem Kościński Scabinum et Notarium Civitatis Crasnicensis constituerunt.
Exactores ad Exactiones Publicas: Stanislaum Reszka et Stanislaum Kucharski.
Exactor Proventus Crasnicensis: Joannes Barankowicz.
In Artificii Magistrum:
Sutorum: Stanislaum Grymuza ior, Beszkowic minor.
Pellionum: Tomasz Paśkowic [?] ior, Joannes Barankowicz minor.
Sartorum: [niewypełnione].
Fabrorum: Paulum Stankowski ior, Mathiam Strzyżowski minor.
Textorum: [niewypełnione].""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 138,
        "numer_pozycji": "138",
        "strona_pagina": "fol. 68r (68)",
        "sygnatura": SYGN,
        "data_rok": "1686",
        "kategoria": "Manifestacja Nowaczka i poręczenie za Katarzynę Chmielównę (11 II 1686)",
        "osoby_podmioty": "Paweł Nowaczek, zmarły P. Sitarski, Wojciech Butka, wdowa Jadwiga Więckowa [?], Stefan Nagórny, Katarzyna Chmielówna, Żyd Moszko Berkowicz [Berel?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Manifestacja Pawła Nowaczka o stargowanie ćwierci roli Rodzonkowskiej od zmarłego P. Sitarskiego przed jego śmiercią; protokół z 11 II 1686 r. (poniedziałek przed św. Walentym): poręczenie (fideiussio) Wojciecha Butki, wdowy Jadwigi Więckowej [?] i Stefana Nagórnego za Katarzynę Chmielównę osadzoną w więzieniu o rzekomą ucieczkę do Brzezin z synem Żyda Moszka Berkowicza [Berela?].",
        "transkrypcja": """68.
Manifestatio Pauli Nowaczek.
Paweł Nowaczek przyszedłszy do Urzędu Wójtowskiego oświadczał się iż u nieboszczyka P. Sitarskiego stargował był ćwierć roli Rodzonkowskiej, na którą zadał... co iest Urzędowi wiadomo że affektował y chciał rezygnacją czynić że śmierć świeża nastąpiła aby mu to było na potym przyznano. Quod est Actis praesentibus connotatum.

Actum Crasnicii Coram Officio Advocat. Crasn. Feria Secunda ante Festum S. Valentini Proxima Anno 1686 Die 11 Februarii.
Fideiussio Catharinae Chmielówny.
Do Urzędu Niniejszego W[ójtowskiego] Kraśnickiego oblicznie przyszedłszy Wojciech Butka Mieszczanin Kraśnicki y wdowa niegdy pozostała małżonka Jadwiga Więckowa [?]... iż wyręczeli z więzienia Katarzynę Chmielównę która była wsadzona że się do uciec z synem Moszkiem Berelem Brzezinia miała... obiecując mu tego dowodzić co zadała natenczas kiedy sprawa będzie z pomienionym Żydem Berelem, którzy rękojemcami zapisują się na osobach swoich y dobrach z nią stawić do Sądu. Która rękojmia do Akt niniejszych iest zapisana.
Wojciech Buta
Stefan Nagórny +
Jadwiga Więckowa Córka.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 139,
        "numer_pozycji": "139",
        "strona_pagina": "fol. 69r (69)",
        "sygnatura": SYGN,
        "data_rok": "1694",
        "kategoria": "Protokoły z czerwca 1694 r. (Proskowic, Brzeziński, Kanaszkowicz)",
        "osoby_podmioty": "Jan Proskowic [?], Żyd Herszko, Grzegorz Bednarz, Jan Brzeziński [?], Kanaszkowicz, Pałka [?]",
        "kwoty_podatki": "fl 10",
        "opis_sprawy": "Wpisy z piątku po Zielonych Świątkach 1694 r. (4 VI 1694 — przeskok chronologiczny księgi z 1686 na 1694 r.): pozew Jana Proskowica [?] przeciw Żydowi Herszkowi o konia; skarga Grzegorza Bednarza o fl 10 długu; sprawa Jana Brzezińskiego [?] przeciw Maciejowi o rolę; kontynuacja sprawy Brzezińskiego o pobicie na drodze; sprawa Kanaszkowicza przeciw Pałce [?].",
        "transkrypcja": """69. 1694.
Feria 6ta post Festa Solennia SS. Pentecostes pxa A. 1694.
Videtur propositio per Joannem Proskowicz [?] contra Infidelem Herszko ratione abductionis equi et paritatis sui cum Statutis.

Feria 6ta post Festa Solennia SS. Pentecostes pxa Ao 1694.
Pomiędzy stronami... Grzegorz Bednarz skarżył się o dług fl 10, Sąd nakazał zapłatę z kosztami w terminie tygodniowym.

Między Janem Brzezińskim [?] Aktorem a Maciejem [?] Pozwanym o niedopłacenie roli, Sąd daje dylację do poniedziałku.

Continuatio sprawy między Brzezińskim a Łukaszem o porwanie na dobrowolnej drodze, nakazano złożenie przysięgi przez świadków.

Między Kanaszkowiczem Aktorem a Pałką [?] Pozwanym, Sąd wyznacza termin zawity na środę do przysięgi.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 140,
        "numer_pozycji": "140",
        "strona_pagina": "fol. 69v (69v)",
        "sygnatura": SYGN,
        "data_rok": "1694",
        "kategoria": "Protokoły z 7 VI 1694 r. (Zdebik, Herszko, Rymarczyk, Kościński)",
        "osoby_podmioty": "Kazik [?], Zdebik, Skalisz [?], Żyd Herszko, Kucharski [?], Żyd Moszkowic, Jan Nowaczek [?], Rymarczyk, Świątek [?], Pan Kościński, Proskowic [?]",
        "kwoty_podatki": "fl 50",
        "opis_sprawy": "Protokół z poniedziałku po Trójcy Świętej 1694 r. (7 VI 1694): sprawa Zdebika przeciw Skaliszowi [?] o sąsiedztwo i inkwizycję; wyrok Żyda Herszka przeciw Kucharskiemu [?]; sprawa Żyda Moszkowica przeciw Janowi Nowaczkowi [?] o fl 50 długu z dekretu komisarskiego; sprawa Rymarczyka przeciw Świątkowi [?]; manifestacja P. Kościńskiego przeciw Proskowicowi o niesłuszną kalkulację.",
        "transkrypcja": """69v.
Inter ... Kazik [?] Actorem et ... Citatum: Sąd odłożył do działu sprawę o dług.

Feria 2da post Festum SS. Trinitatis pxa Ao 1694.
Inter H. Zdebik Actorem et H. Skalisz [?] Citatum.
W sprawie o zadanie czarostwa y niektóre szkody przez pozwanego Aktorowi... Sąd odkłada sprawę do środy na inkwizycję świadków.

Inter Infidelem Herszko Actorem et H. Kucharski [?] Citatum.
Dekret nakazuje zapłatę długu w terminie tygodniowym pod egzekucją.

Inter Infidelem Moszkowicz Actorem et Joannem Nowaczek [?] Citatum.
W sprawie o dług fl 50 według dekretu komisarskiego, Sąd nakazuje zapłatę lub rachunek do środy.

Inter H. Rymarczyk Actorem et H. Świątek [?] Citatum: odesłano do poniedziałku.

Ex parte Dni Kościński contra Fam. Proskowicz [?] Manifestatio ratione iniustae per eum factae calculationis.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 141,
        "numer_pozycji": "141",
        "strona_pagina": "fol. 70r (70)",
        "sygnatura": SYGN,
        "data_rok": "1694–1695",
        "kategoria": "Relacja burmistrzów z 12 V 1694, protestacje i Żyd Abel Anzel",
        "osoby_podmioty": "Stanisław Solecki, Stanisław Szymkiewicz [?] (burmistrzowie), Stanisław Broskowic [Proskowic], Jan Broskowic, A. Potocki, Żyd Abel Anzel, Kasper [?], Jakub Janczarek [Janczarok?] (ze wsi Sulów)",
        "kwoty_podatki": "fl 30; fl 2",
        "opis_sprawy": "Protokół ze środy po niedzieli Cantate 1694 r. (12 V 1694): relacja burmistrzów kraśnickich Stanisława Soleckiego i Stanisława Szymkiewicza [?] w sprawie fl 30 wypłaconych P. Broskowicowi; wzajemne protestacje Jana Broskowica i A. Potockiego o najście i zniesławienie; protestacja Żyda Abla Anzela z wigilii Bożego Narodzenia 1694 r. (24 XII 1694) o niezapłacenie soli i fl 2; protestacja Jakuba Janczarka ze wsi Sulów z 7 I 1695 r.",
        "transkrypcja": """70.
Actum Crasnicii Feria 4ta post Dominicam Cantate pxa Ao 1694.
Relacja sław. PP. Burmistrzów Kraśnickich od Urzędu niniejszego deputowanych przeciwko sław. P. Stanisławowi Soleckiemu i Stanisławowi Szymkiewiczowi [?] Burmistrzom, którzy zeznali iż P. Broskowic [Proskowic] długu żadnego nie ma gdyż mu fl 30 wypłacono. Co do Akt zapisano.

Videnda Protestatio ex parte F. Joannis Broskowicz contra F. Potocki ratione invasionis et dishonorationis.
Videnda Protestatio et reprotestatio ex parte F. Potocki contra F. Joannem Broskowicz.

Feria 6ta in Vigilia Nativitatis Christi Dni 1694.
Abel Anzel protestuje się przeciw Kasprowi [?] o niezapłacenie soli y złotych dwóch.

Feria 2da in Crastino SS. Trium Regum Ao 1695 [1694?].
Facta est protestatio per Jacobum Janczarek [Janczarok?] de Villa Sułów.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 142,
        "numer_pozycji": "142",
        "strona_pagina": "fol. 70v (70v)",
        "sygnatura": SYGN,
        "data_rok": "1694",
        "kategoria": "Spory rolne i manifestacja Mateusza Biernatka (9 VI 1694)",
        "osoby_podmioty": "Wojciech Biały [?], Mateusz Bąk, Tomasz [?], Maciej Błaszkowic, Jan Kajmik [?], Konduk [?], Mateusz Biernatek, Marcin Biernatek",
        "kwoty_podatki": "fl 20",
        "opis_sprawy": "Protokół ze środy po Zielonych Świątkach 1694 r. (9 VI 1694): konsens obojga urzędów dla Wojciecha Białego [?]; sprawa Mateusza Bąka o dług z cyrografu (odroczona z powodu nieurodzaju i podatków); spór o wykup roli z udziałem P. Błaszkowica, Jana Kajmika [?] i Konduka [?] (fl 20); manifestacja Mateusza Biernatka przeciw Marcinowi Biernatkowi o bezprawne przedanie ćwierci roli.",
        "transkrypcja": """70v.
Feria 4ta post Festa Solennia SS. Pentecostes pxa Ao 1694.
Consensus dany z Obojga Urzędu tak Radzieckiego iako y Wójtowskiego y Ławniczego Wojciechowi Białemu [?] na gruncie...
Uczciwy Mateusz Bąk stawiwszy się przed Urzędem Kraśnickim... o dług z cyrografu na fl 20, Sąd z uwagi na ciężary pańskie y nieurodzaj rozkłada spłatę.

W sprawie między Tkaczem [?] a Biernatem [?] o wykup roli... Sąd wyznacza do kalkulacji PP. Błaszkowica i innych... a w sprawie o fl 20 do świadków Jana Kajmika [?] y Konduka [?].

Manifestatio: Stanąwszy oblicznie przed Urzędem Wójtowskim Uczciwy Mateusz Biernatek solenniter protestuje przeciw Marcinowi Biernatkowi iż ćwierć roli mimo zakazu przedał.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 143,
        "numer_pozycji": "143",
        "strona_pagina": "fol. 71r (71)",
        "sygnatura": SYGN,
        "data_rok": "1695",
        "kategoria": "Ugoda spadkowa rodziny Piaseckich (25 II 1695) i sprawa Wileżki",
        "osoby_podmioty": "Wojciech Piasecki, Bartłomiej Piasecki, Marianna Piasecka, Zofia Piasecka, Jan Piasecki (zm.), Marianna Piasecka (zm.), Józef Wileżka [Wilczek?], Józef Szyszkowski [?], Bartłomiej Jastrzębski [?], Stanisław Świątek",
        "kwoty_podatki": "-",
        "opis_sprawy": "Akt Sądu Łączonego (Radzieckiego, Wójtowskiego i Ławniczego) z piątku po św. Macieju Apostole 1695 r. (25 II 1695): ugoda spadkowa rodzeństwa Wojciecha, Bartłomieja, Marianny i Zofii Piaseckich, sierot po zmarłym Janie Piaseckim i Mariannie, o podział gruntów zwanych Płazińska [?]; poniżej wpis z 14 III 1695 r. (poniedziałek po Niedzieli Laetare): skarga Józefa Wileżki [Wilczka?] przeciw Józefowi Wilczkowi [?] o pobicie żony Marianny u Stanisława Świątka.",
        "transkrypcja": """71.
Actum Crasnicii coram Iudicio Composito tam Consulari quam Advocatiali et Scabinali Iurato Feria Sexta in Crastino Festi Sancti Mathiae Apostoli Anno Domini Millesimo Sexcentesimo Nonagesimo Quinto 1695.

W sprawie w Akciey Sądowney między Uczciwemi Wojciechem y Bartłomiejem, także Marianną y Zofią Piaseckiemi Bracią między sobą y Siostrami rodzonemi Przedmieszczany Kraśnickiemi niegdy Uczciwego Jana Piaseckiego y Marianny Małżonków Przedmieszczanina Kraśnickiego pozostałemi Sierotami zgadzającemi między sobą ugodą własną uczynili aby każdy według naturalnej sukcesji swoim cieszył się oraz z przydatkiem Płazińskiej [?] antiquitus nazwanej upominających się od starszego brata Wojciecha Piaseckiego.

Feria 2da post Dominicam Laetare pxa Ao 1695to.
Narratio Josephi Wileżka [Wilczek?] ex instantia F. Josephi Szyszkowski [?] et Bartłomieja Jastrzębskiego [?] przeciwko Józefowi Wilczkowi [?], iż on Mariannę żonę u Stanisława Świątka pobił.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 144,
        "numer_pozycji": "144",
        "strona_pagina": "fol. 71v (71v)",
        "sygnatura": SYGN,
        "data_rok": "1695",
        "kategoria": "Poręczenie za Józefa Wilczka i procesy Rożewskiego (22–24 III 1695)",
        "osoby_podmioty": "Józef Madej, Szymon Kuśmierz, Adam Wilczek, Dorota Tutkowa, Józef Wilczek [Wileżka], Stefan Kwasowic, Kazimierz Rożewski [Różewski?], Marcin Wilczek, Madejczyk",
        "kwoty_podatki": "fl 1",
        "opis_sprawy": "Protokół z wtorku po Niedzieli Judica 1695 r. (22 III 1695): poręczenie Józefa Madeja, Szymona Kuśmierza, Adama Wilczka (brata) i Doroty Tutkowej (matki) w obecności Stefana Kwasowica za Józefa Wilczka [Wileżkę] na czas wygojenia rannego sąsiada; sprawa Kazimierza Rożewskiego [?] przeciw Marcinowi Wilczkowi o pobicie w karczmie i fl 1 (oraz sesja z 24 III 1695 r. przeciw Winiarczykowi [?]).",
        "transkrypcja": """71v.
... [dokończenie narracji z k. 71r] ...

Feria 3tia post Dominicam Judica Luctum pxa An. Dni 1695to.
Uczciwi Józef Madej, także Szymon Kuśmierz Przedmieszczanie Kraśn. Uczciwy Adam Wilczek brat y Dorota Tutkowa Matka przed Urzędem y Aktami niniejszemi oblicznie stanąwszy zdrowi na ciele y umyśle nieprzymuszeni prawdziwie dobrowolnie zeznali że oni Józefa Wilczka sąsiada swego na ten czas z więzienia będącego na porękę biorą, obiecując go za tydzień do sprawy stawić, pod zakładem w obecności Stefana Kwasowica Scabini Jurati.

Inter Casimirum Rożewski [Różewski?] Actorem et Martinum Wilczek Citatum fl 1.
W sprawie na terminie dzisiejszym przed Urzędem niniejszym o pobicie w karczmie i fl 1 z udziałem Madejczyka y winiarza, odesłano do inkwizycji.

Feria 5ta post Dominicam Judica Luctum pxa Ao 1695to.
W sprawie między Kazimierzem Rożewskim Aktorem a Winiarczykiem [?] Pozwanym o pobicie, pozwany nie stawił się, więc wpada w kontumację.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 145,
        "numer_pozycji": "145",
        "strona_pagina": "fol. 72r (72)",
        "sygnatura": SYGN,
        "data_rok": "1695",
        "kategoria": "Manifestacja burmistrza Potokowicza i sprawy z 6 V 1695",
        "osoby_podmioty": "Burmistrz Adam Potokowicz, Pan Stankowski, Tomasz Zdebik, Kazimierz Maziarczyk [?], Dębski [?], Kot [?], Jan Majowski, Adam Fox, Wojciech Bębenek [?]",
        "kwoty_podatki": "fl 30",
        "opis_sprawy": "Manifestacja burmistrza i rezydenta kraśnickiego Adama Potokowicza z 29 IV 1695 r. (sobota przed św. Filipem i Jakubem) o niedotrzymaniu warunków kupna roli za fl 30 wobec P. Stankowskiego; sesja z 6 V 1695 r. (piątek po Znalezieniu Krzyża Św.): sprawa Tomasza Zdebika przeciw Kazimierzowi Maziarczykowi [?] oraz sprawa Jana Majowskiego przeciw Adamowi Foxowi (z udziałem Wojciecha Bębenka [?]) o dług pieniężny.",
        "transkrypcja": """72.
In Sabbatho ante Vigiliam Festi SS. Philippi et Jacobi Apostolorum Ao 1695to.
Sław. P. Adam Potokowicz Rezydent y Burmistrz Kraśn. przyszedłszy oblicznie do Akt y Urzędu Radzieckiego... złożył manifestacją względem niedotrzymania terminu kupna roli za fl 30 wobec P. Stankowskiego przy obecności Panów Radziec.

Feria 6ta post Festum Inventionis Sanctae Crucis pxa Anno D. 1695to.
Inter Thomam Zdebik Actorem et Casimirum Maziarczyk [?] Citatum.
Sąd niniejszy kontrowersji wysłuchawszy nakazał aby strony obie w obecności J.J. Dębskiego [?] y P. Kota [?] w poniedziałek stawiły się na świadków.

Inter Joannem Majowski Actorem et H. Adamum Fox Citatum.
W sprawie na terminie dzisiejszym o egzekucję dekretu z Wojciechem Bębenkiem [?] o dług pieniężny, wyznaczono termin zawity na poniedziałek.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 146,
        "numer_pozycji": "146",
        "strona_pagina": "fol. 72v (72v)",
        "sygnatura": SYGN,
        "data_rok": "1695",
        "kategoria": "Procesy z Żydami (Wardęga, Więcko) i sprawa Adama Foxa",
        "osoby_podmioty": "Adam Fox, Jan Majowski, Jakub Wardęga, Żyd Abus [?], Żydówka Itralowa [Izraelowa?], Żydówka Abusiowa, Jan Więcko [Więcek], Wojciech Koza [?], Tomasz Kozik [?], Maciej Kozik [?]",
        "kwoty_podatki": "-",
        "opis_sprawy": "Dokończenie sprawy Adama Foxa z Janem Majowskim (odesłanie na inkwizycję); sprawa Jakuba Wardęgi z Żydem Abusem [?]; sprawa Żydówki Itralowej [Izraelowej?] przeciw Jakubowi Wardędze; sprawa Żydówki Abusiowej przeciw Janowi Więcce o dług zmarłego zięcia; zapis kwitacji Wojciecha Kozy [?] z Tomaszem i Maciejem Kozikami [?].",
        "transkrypcja": """72v.
... [dokończenie sprawy Foxa z Majowskim] ... dlatego na inkwizycję do przyszłego poniedziałku odesłano.

Inter H. Jacobum Wardęga et infidum Abus [?] Citatum.
Mając wygrany dekret Jakub Wardęga z Żydem, Sąd odłożył sprawę do poniedziałku na złożenie dowodu.

Inter Infidam Itralowa [Izraelowa?] Actricem et Jacobum Wardęga Citatum.
Datur Dilatio Parti Citatae ad exsolvendum Parti Actoreae ad Feriam Secundam proxime venturam.

Inter Infidam Abusiowa Actricem et Hon. Joannem Więcko [Więcek] Citatum.
Żydówka Abusiowa pozwała Jana Więckę o dług zmarłego zięcia, sąd wyznaczył dylację do poniedziałku.

Zeznanie Wojciecha Kozy [?] z Tomaszem Kozikiem [?] i bratem jego Maciejem względem kwitacji i kalumnii, zapisano do Akt.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 147,
        "numer_pozycji": "147",
        "strona_pagina": "fol. 73r (73)",
        "sygnatura": SYGN,
        "data_rok": "1697",
        "kategoria": "Protestacja ze wsi Sulów i kondemnaty (1697)",
        "osoby_podmioty": "Wawrzyniec Kąkoła [?] (ze wsi Sulów), Stanisław Kowal [?], Paweł Słomkowski, Jan Trawiński [?], Jan Gomuza, Józef Macal",
        "kwoty_podatki": "fl 5; 6 grzywien",
        "opis_sprawy": "Protokół z roku 1697 (przeskok z 1695 na 1697 r.): 1) Protestacja pracowitego Wawrzyńca Kąkoły [?] ze wsi Sulów przeciw Stanisławowi Kowalowi [?] o pobicie na dobrowolnej drodze i rany krwawe oka i głowy; 2) Sprawa Pawła Słomkowskiego przeciw Janowi Trawińskiemu [?] o fl 5 długu (kara więzienia i 6 grzywien); 3) Kondemnata na Józefie Macalu z instancji Jana Gomuzy.",
        "transkrypcja": """1697. 73.
Actum Coram Iudicio Advocat. et Scab. Iur. Crasnicen. Feria Secunda ante Festum S. Thomae [?] pxa A.D. 1697.
Do Urzędu y Akt niniejszych Wójtowskich Przysięgłych oblicznie przyszedłszy pracowity Wawrzyniec Kąkoła [?] ze Wsi Sulowa protestował się na przeciwko Stanisławowi Kowalowi [?], iż on bez żadnej przyczyny na dobrowolnej drodze pobił go i poranił, pokazując rany krwawe na oku i na głowie.

Sub eodem Actu.
Inter Famatum Paulum Słomkowski post tam multas citationes contra Joannem Trawiński [?] ob contumaciam in non solutione fl 5, poena captivationis et Marcarum 6 decernitur.

Ex Instantia Joannis Gomuzy contra Josephum Macal post tot terminos non comparentem poena contumaciae et executio decernitur.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 148,
        "numer_pozycji": "148",
        "strona_pagina": "fol. 73v (73v)",
        "sygnatura": SYGN,
        "data_rok": "1697",
        "kategoria": "Protestacja Tomasza Nowaka i zeznanie z 18 XII 1697 r.",
        "osoby_podmioty": "Wojciech Dudek [?], Jan Trawiński [?], Maciej Kubik [?], Tomasz Nowak, Franciszek Grątek [?], Maciej Łąka [?], Karol Mrozek [?], Maciej Rzepka [?], Maciej Śliwiński [?]",
        "kwoty_podatki": "7 grzywien",
        "opis_sprawy": "Kondemnata na Janie Trawińskim [?] z instancji Wojciecha Dudka [?] (7 grzywien); sprawa Macieja Kubika [?]; protestacja Tomasza Nowaka przeciw szwagrowi Franciszkowi Grątkowi [?] o zniewagi żony i sióstr oraz groźby obcięcia rąk i podpalenia; sprawa Macieja Łąki [?] przeciw Karolowi Mrozkowi [?]; na dole wpis z 18 XII 1697 r. (środa przed św. Tomaszem Apostołem) w sprawie Macieja Rzepki [?] przeciw Maciejowi Śliwińskiemu [?] o porwanie córki i zabór bydła.",
        "transkrypcja": """73v.
Ex Instantia Alberti Dudek [?] contra Joannem Trawiński [?] poena contumaciae et Marcarum 7 decernitur.

Inter honestum Mathiam Kubik [?] Actorem et ... Citatum: datur dilatio inquisitionis.

Sub eodem Actu: Do Urzędu y Akt niniejszych W[ójtowskich] przyszedłszy oblicznie Uczciwy Tomasz Nowak solenniter protestował się przeciwko Franciszkowi Grątkowi [?] szwagrowi swemu, iż on zapomniawszy Bojaźni Bożey y prawa sąsiedzkiego na żonę swoję własną y siostry jej wielkie przeciwności czynił, grożąc obcięciem rąk y podpaleniem.

Inter Honestum Mathiam Łąka [?] Actorem et Carolum Mrozek [?] Citatum: datur dilatio inquisitionis.

Actum Feria 4ta ante Festum S. Thomae Apostoli proxima A.D. 1697.
Na terminie dzisiejszym stanąwszy Uczciwy Maciej Rzepka [?] wniósł skargę przeciwko Uczciwemu Maciejowi Śliwińskiemu [?], iż on mając za sobą córkę Aktora zabrał mu bezprawnie bydło y inne rzeczy.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 149,
        "numer_pozycji": "149",
        "strona_pagina": "fol. 74r (74)",
        "sygnatura": SYGN,
        "data_rok": "1694–1697",
        "kategoria": "Sprawa ks. Plebana Potockiego oraz proces Macieja Piotrowczyka (25 II 1694)",
        "osoby_podmioty": "Ks. Pleban Potocki, Imć Pan Andrzej (podstarości?), Maciej Łukasz [?], Andrzej Sienko [?], Maciej [Aktor], Maciej Piotrowczyk, Kłosowa",
        "kwoty_podatki": "fl 80; fl 23; fl 3",
        "opis_sprawy": "Dokończenie zeznań o chłopie Macieju Łukaszu [?] i Andrzeju Sienku [?] w sprawie sum fl 80 i fl 23 dla Imci Ks. Plebana Potockiego; poniżej wpis z 25 lutego 1694 r. (środa po Popielcu — cofnięcie do 1694 r.): spór Macieja z Maciejem Piotrowczykiem o zabranie rzeczy po zmarłej żonie (w tym 3 złp u Kłosowej), wyznaczenie terminu zawitego na dowody i przysięgę.",
        "transkrypcja": """74.
... [dokończenie wpisu z k. 73v] ... za subą P. Andrzeja Podstarościego y Imci Xiędza Plebana Potockiego o złotych 23... Testis Szymon Jankowski [?] zeznał iż ten chłop Maciej Łukasz [?] y Andrzej Sienko [?] o fl 80 dla Imci P. Andrzeja y Ks. Plebana Potockiego y złotych 23 zeznali.

Actum Feria 4ta post Dominicam Cinerum proxima A.D. 1694.
W Sprawie między Uczciwym Maciejem Aktorem a Uczciwym Maciejem Piotrowczykiem Pozwanym: skarżył się Aktor iż pozwany zabił i pobrał rzeczy po zmarłej żonie, a zwłaszcza złotych 3 u Kłosowej. Pozwany odpowiedział iż po nieboszczce rzeczy te na pogrzeb przedał według regestru. Sąd wyznaczył stronom termin zawity na dowody i przysięgę.""",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 150,
        "numer_pozycji": "150",
        "strona_pagina": "fol. 74v (74v)",
        "sygnatura": SYGN,
        "data_rok": "1694",
        "kategoria": "Kontumacje żydowskie i sprawa Piotrowczyka z Rodzonkiem (1694)",
        "osoby_podmioty": "Żyd Icko Agrorowy [?], Jan Ryczek [?], Bubayczykowic [?], Sebastian Papuża [?], Wojciech Rusek, Augustyn Pękala [?], Michał Piotrowczyk, Bartłomiej Rodzonek, Paweł Kozak",
        "kwoty_podatki": "7 grzywien",
        "opis_sprawy": "Cztery wyroki zaoczne z sesji z lutego 1694 r.: 1) Jan Ryczek [?] skazany z instancji Żyda Icka Agrorowego [?]; 2) Bubayczykowic [?] skazany z instancji tegoż Żyda; 3) wyrok na 7 grzywien z instancji Sebastiani Papuży [?]; 4) Augustyn Pękala [?] skazany z instancji Wojciecha Ruska; poniżej sprawa Michała Piotrowczyka przeciw Bartłomiejowi Rodzonkowi o kradzież grochu i dług z dekretu (z udziałem Pawła Kozaka).",
        "transkrypcja": """74v.
Sub eodem Actu.
Ad Instantiam Infidelis Icko Agrorowego [?] Joannes Ryczek [?] bina citatione citatus contumax.
Ad Instantiam eiusdem Infidelis Judaei Bubayczykowic [?] prima citatione non comparens contumax.
Ad Instantiam Sebastiani Papuży [?] primo contumax... poena 7 Marcarum parti et Iudicio per medium decernitur.
Ad Instantiam Alberti Rusek Augustinus Pękala [?] prima citatione citatus contumax.

Inter Honestum Michaelem Piotrowczyk Actorem et Honestum Bartlomaeum Rodzonek Citatum: datur dilatio inquisitionis ad feriam sextam venturam. A tymże terminie Bartłomiej Rodzonek według dekretu na inkwizycję mu pozwoloną protestował się względem zadania o kradzież grochu przez Aktora Rodzonkowi zeznał iż Paweł Kozak o tym wie.""",
        "link_swa": UNIT_LINK
    }
]

existing_nums = {r["nr_skanu"] for r in main_data}
for rec in part6_scans:
    assert rec["nr_skanu"] not in existing_nums, f"Duplikat nr_skanu {rec['nr_skanu']}"
    main_data.append(rec)

main_data.sort(key=lambda x: x["nr_skanu"])

with open('/home/ubuntu/workspace/Gen/main_data_j20_part6.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j20_part6.json: {len(main_data)} skanow")
