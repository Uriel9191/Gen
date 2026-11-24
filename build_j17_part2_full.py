# -*- coding: utf-8 -*-
import json
import os

records_26_to_50 = [
    {
        "nr_skanu": 26,
        "numer_pozycji": "Poz. 26",
        "strona_pagina": "fol. 11v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Zeznania świadków / Sprawy opiekuńcze i areszty",
        "osoby_podmioty": "Maciej Majowski bedel miejski [Mathias Mayowski]; Tomasz Stojek przedmieszczanin [Stoyek]; Wawrzyniec Stafia [Laurentius Stafia]; Jan Des [Joannes Des]; Szymon Ledański nieboszczyk burmistrz [Ledański / Leżański?]; Agnieszka Mrowcowa matka [Agnes Mrowca]; Karol Mrowiec syn [Carolus Mrowiec]; Albert Kłopot [Wojciech Kłopot]; Jakub Kłopot brat Alberta",
        "kwoty_podatki": "Szmat roli; pretensje za sługi; opieka braterska nad majątkiem",
        "opis_sprawy": "Cztery wpisy z lutego 1700 r.: 1. Wniosek bedela Macieja Majowskiego o areszt majątku Tomasza Stojka celem zabezpieczenia opieki nad małoletnim rodzeństwem; 2. Zeznanie Wawrzyńca Stafii i Jana Desa o ostatniej woli zmarłego burmistrza Szymona Ledańskiego [Leżańskiego?] dotyczącej zapisu roli dla sługi; 3. Zeznanie Alberta Kłopota w sprawie Agnieszki i Karola Mrowców o rozliczenie odzieży i sukni; 4. Zeznanie Jakuba Kłopota potwierdzające chorobę brata i pretensje do sukni i opieki domowej.",
        "transkrypcja": "11v\nMathias Mayowski bedellum oratione, contra Uczciwego Tomasza Stoyka\nPrzedmieszczanina Kraśnickiego, kosztem braci y o sierotach\nSummę zawalił, po niegdy Uciwym [...] któremu winien podług\nktóry iest naybliższy Tutor y Opiekun, Ponieważ z Braćmi\ny małżonkiem swoim teraźnieyszym Dobra marnuie, y traci aby De-\ncrevit Sądowy nikomu tych papierów nie dawał, alias in foro carceres\nimpediti Aresti.\n\nDie 6 Eodem 1700\nEx Instantia Laurentii Stafia et Joannes Des, Recognovit Byłem\nz pomienionym Wawrzyńcem Stafią u niegdy Sławetnego Pana\nSzymona Ledańskiego [Leżańskiego / Ledańskiego?] Burmistrza Kraśnickiego w domu na\nPrzedmieściu tuteyszym Kraśnickim, Upominaiącym sie za sługi\nswoy U niegdy Pana ledwie gadał, rzekł: nie bolesz, iak sie\nmu upomniał rzekł te słowa: Nie bolesz Pan Ledański [Leżański?],\nbędziesz sobie brać roli szmat od tego że sie winno. Na\nzaiutrz rano Umarł, tacto pectore Recognovit.\n\nEx Instantia Agnetis matki et Karoli Mrowca [Mrowca / Mrowców?], dekretem\nbrania Cierpienia Przygielatować [?] synka. Honestus Albertus\nKłopot Recognovit: Dnie w wspomnienie iest temu trzecia\nśroda przed się to synowi swoie. Pismo Panu moie nadał w tym\nnie widziałam gdzie sie obracały, potym w południny wstała\nAgnieszka sukni prosiła, dwoie U trzeciego nie było, tacto pe-\nctore Recognovit.\n\nEx Eodem et Jacobus Kłopot frater et Albertus Kłopot\nfratrem suum. Recognovit: Iżem edukacyey [?] uszanował bratu\nswoiemu gdyż chorował wyżey niż dobytku swoy sukni\ndwoie przy którym iedno Agnieszki rynsztunki do Kadzi Pana\nBurmistrza Kazano mie do więzienia wziąść iako dłużnika\nsuknia w tey szkoły ze trzech prosiła rano, ieden w munie,\ngdzie sie obrócił zmierzył między szukaniem iako y przed\ntym rano moie z Agnieszki suknią w siedmiu wełnianych.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 27,
        "numer_pozycji": "Poz. 27",
        "strona_pagina": "fol. 12r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy klasztorne / Kontrakty i obligi",
        "osoby_podmioty": "Ks. Paweł Wilhelm Pajecki przeor klasztoru [Paiecki]; Jan Barankowicz burmistrz i radca kraśnicki; Konwent Kanoników Regularnych Lateraneńskich w Kraśniku [Zakon św. Augustyna]; Urząd wójtowski i ławniczy kraśnicki",
        "kwoty_podatki": "120 złotych polskich (fl. 120 in bona moneta) z sukcesji ojczystych",
        "opis_sprawy": "Sesja sądu wójtowsko-ławniczego z 19 października 1700 r. (błędna glosa pisarza 'Krasnostaviensi' w nagłówku): Przewielebny ks. Paweł Wilhelm Pajecki przeor klasztoru Kanoników Regularnych Lateraneńskich w Kraśniku wnosi o oblatowanie formalnego kontraktu komplanacyjnego zawartego ze Sławetnym Janem Barankowiczem burmistrzem kraśnickim; Barankowicz zobowiązuje się do spłaty 120 złp dobrej monety z dóbr ojczystych i braterskich pozostałych po zmarłym bracie.",
        "transkrypcja": "12\nActum coram Officio Advocatiali et Scabinali Krasnostaviensi [Krasnicensi]\nFeria Tertia in Crastino Festi Sancti Lucae Evangelistae\nAnno Domini Millesimo Septingentesimo.\n\nDo Urzędu y Akt ninieyszych Wóytowskich y Ławniczych\nKraśnickich w osobie swoiey przyszedłszy Przewielebny\nJegomość Xsiądz Paweł Wilhelm Paiecki [Pajecki], Przeor y Klasztor\nKraśnickiego Klasztoru Konwentu Kraśnickiego, prosił przyięcia do Xsiąg\nninieyszych Recognicyą Cechu Sławetnego Pana\nJana Barankowicza Burmistrza Kraśnickiego pod-\npisaney cuius Tenor sequitur talis:\n\nUczyniwszy Komplanacyą z Przewielebnym Jegomość\nXsiędzem Pawłem Wilhelmem Paieckim Kanoni-\nkiem Regularnym Lateraneńskim względem Oy-\nczystey y innych Dobr pozostałych po nie-\nboszczyku rodzonym Jego, taki Kontrakt między\nsobą zawarliśmy, Iż Jeymść u mnie pomienionemu\npowinniśmy oddać z tych Sukcessiy złotych sto dwadzie-\nścia in bona moneta. Oprocz Domu y Długow, które\nJegomość sobie okupował et in quantum ieżeliby się\nnie dosyć stało według Kontraktu, tedy Oblig, który\ndatuię na siebie iako wszytkie dobr swoich Oycy-\nstych y Braterskich mnie y Małżonce moiey rezygno-\nwał, mocnego będziemy kasować y wszystkie dobra pozostałe\nOyczyste y Braterskie odebrać. Na co dany kart z obligu\nprzy podpisem własney ręki moiey. Działo się we Dwo-\nrze Roku Tysiącznego Siedmsetnego Miesiąca Lipca\nPiątego dnia dwunastego Miesiąca Lipca. Przy tym P. K. / 12 / Jan Barankowicz Rayca Kraśnicki.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 28,
        "numer_pozycji": "Poz. 28",
        "strona_pagina": "fol. 12v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy klasztorne / Plenipotencje i sumy wyderkafowe",
        "osoby_podmioty": "Jan Barankowicz burmistrz i rajca; Małżonka Barankowicza; Ks. Paweł Wilhelm Pajecki przeor [Paiecki]; Ks. Jan Machiewicz przeor dóbr klasztornych [Machiewicz]; Konwent Kanoników Regularnych Lateraneńskich w Kraśniku",
        "kwoty_podatki": "Półtorasta złotych (150 złp) ratami do św. Kazimierza 1701 r.; wyderkaffy",
        "opis_sprawy": "Dalszy ciąg kontraktu Barankowicza: deklaracja spłaty 150 złp ratami na św. Kazimierz roku 1701 z zabezpieczeniem na całym majątku. Następnie ks. Paweł Wilhelm Pajecki przeor konwentu kraśnickiego ustanawia oficjalnym plenipotentem dóbr klasztornych ks. Jana Machiewicza do windykacji sum i inskrypcji wyderkafowych.",
        "transkrypcja": "12v\nwedług wziąłem od Jegomości Xsiędza Pawła Paieckiego\npowinnym sposobem y z bratem y małżonką moią złotych\nsto w dobrey monecie które się braknie się wespół z\nmałżonką moią Prześwietney naydaley Na Święty Ka-\nzimierz in Anno sequenti Millesimo Sexcentesimo [Septingentesimo]\nNonagesimo sexto z drugiemi długami y wy-\npomienionemi wieść półtorasta złotych wypłacić\ny zapisać się na wszytkich dobrach moich y podpi-\nsam ręki moiey, własney przy bytności małżonki moiey.\nJan Barankowicz Rayca Kraśnicki.\n\nSub Eodem Actu\nPrzed Urzędem y Aktami ninieyszemi Wóytowskiemi\ny Ławniczemi w osobie swoiey przyszedłszy Przewielebny\nJegomość Xiądz Paweł Wilhelm Paiecki, Przeor y Klasztor\nKonwentu Kraśnickiego Zakonu Świętego Augustyna\nKanoników regularnych Lateraneńskich, approbowanie\ndobrowolnie y plenipotencyą Jegomości Xsiędzu Janowi\nMachiewiczowi, tegoż Konwentu Przeorowi Dóbr\ndo odebrania Inscriptiy swego to iest Sukcessiey po zmarłych\nrodzicach Jego, y Braci Iey Recognoscentis ro-\ndzonych, Produtis Iuribus et Naturali successione\nsobie zachowanemi to plenipotencyą\nnależących, Za które dobra generaliter wszystkie\nSummę wsze kurował Pan Barankowicz de-\ndata in eadem apposita oddał alias in forma Compro-\nmandati plenissima et perfectissima.\n\nSub eodem Actu\nTenże Jegomość Xiądz Paweł Wilhelm Paiecki Recognovit\nIż penes se recognovit Iż On pomienionym kurował on\nwzględem Wyderkaffu z Liczby podaney należącego, który\nwyderkaffu",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 29,
        "numer_pozycji": "Poz. 29",
        "strona_pagina": "fol. 13r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy klasztorne / Wyderkaffy / Obrót nieruchomościami",
        "osoby_podmioty": "Ks. Paweł Wilhelm Pajecki przeor; Walenty Janaszkowic [Janaszkiewicz]; Onuszkowiczowa wdowa; Walenty Sitarski starszy cechu [Sitartki]; Ks. Jan Machiewicz; Tomasz Wajczyk przedmieszczanin [Wayczyk / Woyczyk?]; Walenty Jajczyk stryj [Jayczyk]",
        "kwoty_podatki": "50 złp wyderkaffu z kamienicy; 100 złp legowane na zegar ścienny; czynsze łaźni",
        "opis_sprawy": "Zapisy wyderkafowe na rzecz klasztoru: 1. Wyderkaff z kamienicy kraśnickiej Walentego Janaszkowica na msze św. oraz 100 złp legowane na ścienny zegar klasztorny; 2. Wyderkaff 50 złp od kamienicy wdowy Onuszkowiczowej oraz opłaty z łaźni miejskiej; 3. Sprawa ks. Pajeckiego przeciwko Walentemu Sitarskiemu starszemu cechu. 4. Sesja z 15 listopada 1700 r.: Tomasz Wajczyk przedmieszczanin zeznaje w sprawie działu ćwierci roli ze stryjem Walentym Jajczykiem.",
        "transkrypcja": "13\nwyderkaffu tak iest na Pamiątkę dano na Mszę Świętą\nw Konwencie Kraśnickim między Janaszkowica w K.\nmiędzy Zacnie J. P. Walentego Janaszkowica w K.\nlegowanych, sto zaś ściennego zegaru Konwentowi\nlegowanego.\n\nSub eodem Actu\nPrzeciwko Onuszkowiczowey wdowie zaś wyderkaffu\nod Sukromney Kamienicy złotych Pięćdziesiąt Xiądz\nzłotych sto należytości, A dwadzieścia złotych gro-\nszy sześć z apteki winna, która oddała manet w\nUrzędzie, Kart dany na sumpt na sławną aemulatią\nŁaźnie czynić Item do Łaźniy należącey rękę\nod teyże za odstąpieniem kwitu patet z regestru\n1694. Item prywatnie pożyczonych dwa tale-\nry bite.\n\nSub Eodem Actu\nPrzed Urzędem y Aktami ninieyszemi Wóytowskiemi\ny Ławniczemi Kraśnickiemi Videatis hoc loco\nplenipotentia Xiądz Paiecki zaś Vindicatio plateas\nstarszy eiusdem recognoscentis Valentini Sitarski\nUna funtimo in eadem sub plenipotentia\nJego X. Jan Machiewiczowi Przeorowi zapisuie\nalias in forma Compromis mandati.\n\nActum coram Officio Advocatiali et Scabinali\nKrasnicensi Feria 2-da post Festum S. Martini Ponti-\nficis proxima A.D. 1700.\n\nPrzed Urzędem y Aktami ninieyszemi Wóytowskiemi y\nŁawniczemi Kraśnickimi w osobach swoich stanąw-\nszy Uczciwi Thomasz Wayczyk [Wajczyk / Woyczyk?] Przedmieszczanin Kraś-\nnicki ćwierci roli między Uczciwego Walentego\nJayczyka [Jajczyka] Przedmieszczanina Kraśnickiego Stryia swego / 13 /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 30,
        "numer_pozycji": "Poz. 30",
        "strona_pagina": "fol. 13v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Obrót nieruchomościami / Rezygnacje gruntowe",
        "osoby_podmioty": "Marcin Jajczyk syn [Marcin Jayczyk]; Tomasz Jajczyk [Jayczyk]; Maciej Dziernatek [Dziernatko]; Anna Dziernatkowa żona Macieja; Andrzej Podkański [Podkański / Podkański?]; Dypałka",
        "kwoty_podatki": "45 złotych polskich (fl. 45) za ćwierć roli",
        "opis_sprawy": "Transakcja sprzedaży gruntu: Uczciwy Marcin Jajczyk syn Tomasza zrzeka się praw sukcesyjnych i sprzedaje ćwierć roli leżącej od gościńca Budzyńskiego ku miedzy Andrzeja Podkańskiego Uczciwemu Maciejowi Dziernatkowi i żonie Annie za kwotę 45 złp z pełną intromisją i zrzeczeniem się roszczeń.",
        "transkrypcja": "13v\nzadantis pro interesse radko po nieboszczyku\nMarcin Jayczyk syn, sponte palam libere ac\nper expressum suis et Authore Jayczykowa [?] posty\nRecognoscens o swoich Jayczyków. Amittit Vero\nHonesti Martini Jayczyka pro emigrata habitione\nCavet ac sese submittit et obligat Iż Oni ćwierci roli\npoczynaiąc się od gościńca Budzyńskiego ku miez-\nom z dymessami [?] ćwierci Andrzeia Podkańskiego\nprzy Dypałka sobie rzazana do grani Podkańskiey\nUczciwemu Matyiasowi Dziernatkowi y Annie żonie\nkonwie y ich Potomkom wiecznemi czasy przedaie\nza summę Złotych polskich czterdzieści y pięć K.\nza odebranie summy Za Funkcyą ślubną in fa-\nctum Inscriptionis et Evictione Cautionis quam p-\nromissiva et perfectissima.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 31,
        "numer_pozycji": "Poz. 31",
        "strona_pagina": "fol. 14r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo kryminalne / Kradzieże inwentarza / Tortury i dochodzenia ratuszowe",
        "osoby_podmioty": "Stanisław Jerzykiewicz podwójci [Ierzykiewicz]; Stanisław Szymura ławnik; Wojciech Borkiewicz ławnik [Albertus Borkiewicz]; Wawrzyniec Kulaf ławnik [Laurentius Kulaf]; Szymon Kuparka pasterz [Kuparka / Kupareczka?]; Pan Łukasz z Wyżnicy; Urzędnik od Sukien; Klara; Wawrzyniec",
        "kwoty_podatki": "Kradzież 60 owiec, czarnej krowy kraiastej, czerwonej krowy; szkapy",
        "opis_sprawy": "Sąd kryminalny gajony na ratuszu kraśnickim z 20 września 1700 r.: Przesłuchanie w torturach pasterza Szymona Kuparki służącego u niegdy pana Łukasza w Wyżnicy; obwiniony przyznaje się do kradzieży stada 60 owiec, czarnej krowy kraiastej i czerwonej krowy oraz do zatajenia zbytu inwentarza przed urzędnikami.",
        "transkrypcja": "14\nIudicium Criminale Bannitum celebratum in Praetorio\nKrasnicensi... Tomasz Stanisław Jerzykiewicz [Ierzykiewicz] Viceadvocatus,\nStanisław Szymura Scabinus, Albertus Borkiewicz Scabinus, Laurentius Kulaf Scabinus.\nFeria secunda in Vigilia Festi Sancti Matthaei\nApostoli Anno Domini Millesimo Septingen-\ntesimo.\n\nCoram eodem Iudicio constitutus Laboriosus Szymon\nKuparka [Kuparka / Kupareczka?].\nPasterzem U nieboszczyka Pana Łukasza w Wyżnicy,\nna Bytomiu owiec sześćdziesiąt do owysz pasterzem\nnie do obrony sadu leżącey wiedzący com czynił,\nraz czynił ten Urzędnik od Sukien obsyłaiąc szukać\nu Niego.\nSynem u dworu u Łukasza, dwoie oczy na o-\nnie, u tegoż Łukasza.\nObywielcy się Synem z krową swoią, kilkanaście\nrazy starą krową czarną kraiastą od dwunastu lat,\nktórąm kupił w Cudniku [?] w tymże dworze raz,\nkrowa czerwona krowy wariacy U mego kon-\nnie chował U niego, Synem we dnie\nod dawna Bratnia było żeby raz uczynku.\nPost confessionem torturam, deminuta patus\neandem iterum confessionem approbavit.\nActum coram Officio conscripto\nper Spectabiles ac Honoratos / 14 /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 32,
        "numer_pozycji": "Poz. 32",
        "strona_pagina": "fol. 14v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo karne i łączone / Procesy o czyny sromotne / Prawo magdeburskie i saskie",
        "osoby_podmioty": "Jan Majowski wójt; Adam Kotowicz burmistrz; Jan Barankowicz radny; Maciej Pielaszkowicz radny [Peleszkowic]; Stanisław Płechowicz radny i deputat Trybunału Zamojskiego [Płech]; Stanisław Jerzykiewicz podwójci; Albert Borkiewicz ławnik; Wawrzyniec Pielaszkowicz ławnik; Szymon Kuparka obwiniony z Wilkołaza; Pan Wójtowicz wójt gromadzki z Wilkołaza; Kat miejski [Executor Sprawiedliwości Świeckiej]",
        "kwoty_podatki": "Poddanie 4-krotnym torturom kata na ratuszu kraśnickim",
        "opis_sprawy": "Nadzwyczajny sąd łączony wójtowsko-radziecki z 20 września 1700 r. w pełnym składzie władz miejskich: Rozprawa karna przeciwko Szymonowi Kuparce poddanemu ze wsi Wilkołaz, oskarżonemu przez wójta gromadzkiego Wójtowicza o sromotne czyny przeciwny naturze (grzech sodomii/bestializmu); oskarżony po czterokrotnych torturach kata miejskiego podtrzymuje dobrowolne wyznanie winy przed sądem.",
        "transkrypcja": "14v\nannem Majowski, Adamum Kotowicz Consulem,\nJoannem Barankowicz, Mathiam Pielaszkowicz [Peleszkowic / Pielaszkowic],\nStanislaum Plech [Płech / Płechowicz] Consulem et Deputatum Judicio-\nrum Supremorum Tribunalis Civitatum Dominii\nZamosciani, Stanislaum Jerzykiewicz Viceadvo-\ncatum, Albertum Borkiewicz Scabinos, Lauren-\ntium Pielaszkowicz a Tridentem. Feria Secun-\nda in Vigilia Festi Sancti Matthaei Apostoli\nproxima Domini Millesimo Septingente-\nsimo.\n\nPo dobrowolnych Confessatach, że Braniu Uczyn-\nku złego Obwiniony Pracowity Szymon Kupar-\nka poddany ze Wsi Wilkołaza w Woiewodztwie\ny powiecie Lubelskim, Na Delacyą Prawowitego\nPana Woytowicza Woyta Gromadzkiego\nteyże Wsi Wilkołaza, Na Confessatach Corpo-\nralnych w Rękach Executora Sprawiedliwo-\nści Świeckiey ad primum, secundum, tertium, quartum\ntandem admonitionibus dobrowolne prosię\nConfessata tandem, in iudicio approbował\nteż formalibus sam wyznał, pamiętał to in pro-\nwiedział z tych Uczynków sromotnych, oświadczen-\niu świecy czynionych.\nSąd ninieyszy Oboyga Kraśnicki stosuiąc się\ndo praw tak Saskiego iako y Maydeburskiego tudzież\npraeiudicatorum",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 33,
        "numer_pozycji": "Poz. 33",
        "strona_pagina": "fol. 15r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo karne / Wyroki śmierci przez spalenie na stosie / Spory o kradzież bydła",
        "osoby_podmioty": "Szymon Kuparka z Wilkołaza skazany; Kat kraśnicki; Szymon Plewnik przedmieszczanin; Tomasz Olchowski [Kuśnierczyk seu Olchowski]",
        "kwoty_podatki": "Kara śmierci na stosie; spalenie szkapy; kradzież bydła",
        "opis_sprawy": "Wyrok śmierci sądu kraśnickiego: Szymon Kuparka za wieloletni grzech sodomii i obcowanie ze zwierzętami zostaje skazany na spalenie żywcem na stosie ognistym wraz ze szkapą. Następnie otwarcie wokandy z 6 października 1700 r.: sprawa Szymona Plewnika przeciwko Kuśnierczykowi vel Olchowskiemu o kradzież bydła.",
        "transkrypcja": "15\npraeiudicatorum w podobnych Sprawach tego kry-\nminału godnych, A ci powinni takowego potępiać\nnie wątpliwi, Ponieważ obwiniony tak na do-\nbrowolnych Confessatach iako prawodajne\nres veritatis, Dawnieyszych Uczynków na kor-\nporalnych, które konsekwentnie pod nami sami-\nmaleń approbował. Iż one o przestępstwo przy-\nkazania Boskiego, albowiem, niezgodnym stał się\nstworzeniu natury swoiey człowieczey, że się\nz Bydlętami niememi łączył y koniuguiący [obcujący]\nnaczu takowej to znamieniącego od lat dziesią-\ntych swoich imaiąc się. Proinde za to przestępstwo\nPrzykazania Boskiego y rzyganie Natury ludz-\nkiey swoiey, Śmiercią Świętą przez Ogień złączonym\nw stos powinien być, a żyw z pasz\nWłoskich na nie wtorzony y spalony, Oraz y Szkapa\nz którą bezczeństwa się dopuszczał.\n\nActum Coram Officio Advocatiali et Scabinali Kra-\nsnicensi Feria Quarta post Festum Sancti Fran-\ncisci Confessoris proxima Anno Domini Millesimo\nSeptingentesimo.\n\nW sprawie y Akcyey między Uczciwym Szymonem Plewnikiem, Przedmie-\nszczaninem Kraśnickim y Kuśnierczykiem seu\nOlchowskim, pozwanym o Kradzież Bydła tudzież konia\nz próżney które obięcował być przywrócone do tego Iż\nSkład Borowiego przydał się y potkowki przydalysie daley\ndilatio Inquisitionis Interea ad favores demandatur\nTerminus conservatur. / 15 /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 34,
        "numer_pozycji": "Poz. 34",
        "strona_pagina": "fol. 15v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory rzemieślnicze i wójtowskie / Zeznania świadków",
        "osoby_podmioty": "Grzegorz Jardzyk [Jardzyk / Jarzyk?]; Jan Krawczyk [Krawczyk / Trawczyk?]; Marcin Rymarczyk wójt z Piasków; Jan Obrawenski; Albert Kowal [Wojciech Kowal]; Szymon Olchowski; Tomasz Olchowski syn Szymona; Marina Pietrowskina; Michał Pietrowski",
        "kwoty_podatki": "Koszty egzekucji i szkody kowalskie; roszczenia o wóz zboża",
        "opis_sprawy": "Wokanda spraw z 6–8 października 1700 r.: 1. Odroczenie sprawy Grzegorza Jardzyka przeciw Janowi Krawczykowi z powodu choroby strony; 2. Sprawa Marcina Rymarczyka wójta z Piasków przeciw Janowi Obrawenskiemu; 3. Egzekucja szkód na rzecz Alberta Kowala; 4. Zeznanie Szymona i Tomasza Olchowskich w asyście Mariny i Michała Pietrowskich w sporze o transport wozu żyta.",
        "transkrypcja": "15v\nW sprawie y Akcyey między Pracowitym Gregorem Jardzy-\nkiem, z strony Aktorem a Janem Krawczykiem [Trawczykiem?] pozwa-\nnym Kraśnickiem, datur dilatio vera infirmitatis, de iure\nad formale sentiam, Interea partes inquisitiones edu-\ncant racione Violentiarum terminus conservatur.\n\nSprawa między Uczciwym Marcinem Rymarczykiem\nWoytem Piaskowem, Aktorem z iedney a Janem Obra-\nwenskiem ob legalitatem vera Infirmitatis, Recutur\nad feriam Sextam proxima Ventura terminus conservatur.\n\nEx Parte Alberti Kowal racione damni, et lubsexpensa-\nrum super bona Zmienica Decernitur Executio.\n\nActum coram Officio Advocatiali et Scabinali Kraśnicen-\nsi Feria Sexta post Festum Sancti Francisci Confesso-\nris proxima Anno Domini Millesimo Septingentesimo.\n\nEx Instantia Honesti Simonis Olchowski nomine Thomas\nfilii, comparent A Marina et Michaelis Pietrow-\nszyk, fontor Recognovit: W niedziele przed Francisz-\nkiem Świętym naytylko w tenże teraźnieyszego przed Far-\nmarkiem O dziewiątey godzinie w nocy przyszedł do nas\ndo domu, przed się zgodnie prosił o podpisanie woza psze-\nżyta pomiarkowane komi w bębenek ba wywieść furman\nmark. Na te czasy we liście Summa niedaliśmy\nna woza w tym płacili z parobkiem Tomas Olchow-\nski kradzieyctwa strzegąc.\n\nEx Instantia Eiusdem et Casimirus Kochanek de\nsuburbio Recognovit: fide formalia W niedziele\nw Dyskim Jarmarku, Bawiłem się na Ługu u Szynka",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 35,
        "numer_pozycji": "Poz. 35",
        "strona_pagina": "fol. 16r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Zeznania świadków / Spory o kradzież żyta i konia",
        "osoby_podmioty": "Tomasz Olchowski; Maciej Plewnik [Mathias Plewnik]; Szymon Plewniczek syn; Sebastian Bąk [Sobestian Bąk]; Łakmina Olchowska [Łakmina?]; Marian Wardęga; Wojciech Wardęga",
        "kwoty_podatki": "Zastaw 1,5 korca żyta; kradzież konia; rozliczenia w szynku na Cegielni",
        "opis_sprawy": "Zeznania świadków z października 1700 r. w procesie Olchowskich przeciwko Plewnikowi: Maciej Plewnik i Sebastian Bąk relacjonują przebieg spotkania w gospodzie na Cegielni i rozmowy o długu za żyto, zastawie oraz poszukiwaniu skradzionego konia.",
        "transkrypcja": "16\nprzyszedł też Tomasz Olchowski zaraz z wieczora tamże\nbawił z nami, w tych słowach rzekliśmy wole day prosto\ny Tomasz Olchowski, sam spał na iednym łoszku\nnie poszedł aż o wschodzie Słońca, w poniedziałek ku temu.\n\nEx Instantia et Mathias Plewnik et Szymon Plewniczek\nRecognovit: fide formalia W poniedziałek w dychonfrze [?]\nna Świętego Franciszka siedziałem przed domem\nCygielnika tu w Kraśniku z rana przyjechał z bratem\nTomasz Olchowski y rzekł sobie do tychże rzekł brat\nMathias Plewnik: iako szwagrowi swoiemu nikomu nie\ndarowany szwagrze o to żyto półtora w ten zastawem\nwziął nie turbuy się szwagrze iak wieczór przydzie gdzie\nbyło żyto tam będzie y iatrzyka na to mnie przeprosił y\nporadził żeby miał żyto stawić, tacto pectore Recognovit.\n\nEx Instantia Eiusdem et Sobestian Bąk Recognovit\nfide formalia: W poniedziałek w dnień świętego\nFranciszka z rana Byłem w gospodzie na Cegielni\nsiedzieliśmy we dwóch Tomasz przyszedł do nas Tomasz\nOlchowski iako go uyźrzał Mathias Plewnik rzekł:\nprzestrzegaiąc go rzekł pytał szwagrze gdzie kładę zgubę\nżyta swego ku nie. On odpowiedział mnie, ż iak chcesz\nIda Pan Bóg we się wróci Ja na to Kogo niemówię, tylko\nna swego Brata Łakmina Olchowskiego y Mariana\nWardęgę syna Woyciecha Wardęga Czym dał rękę\nże się wróci to żyto, tacto pectore.\n\nSprawa między Uczciwymi Szymonem y Tomaszem Olchowskimi\nOycem y Synem, a Maciejem Plewnikiem, o zyski y błędy\nDilatio Inquisitionis. / 16 /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 36,
        "numer_pozycji": "Poz. 36",
        "strona_pagina": "fol. 16v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory cywilne i rzemieślnicze / Długi i wadia",
        "osoby_podmioty": "Paweł Nowak [Paulus Nowak]; Jan Tkaczyk [Joannes Tkaczyk]; Tomasz Stafia; Maciej Tkaczyk; Tomasz Jajczyk przedmieszczanin; Jakub Łapka przedmieszczanin; Maciej Kępa [Mathias Kępa]; Stanisław Dąbrowski; Marcin Rymarczyk",
        "kwoty_podatki": "8 złotych polskich; 17 złotych polskich długu; 1,5 korca żyta",
        "opis_sprawy": "Sesje sądu wójtowsko-ławniczego z 11 października 1700 r.: 1. Zawieszenie sporu Nowaka z Tkaczykiem; 2. Tomasz Stafia przeciw Maciejowi Tkaczykowi o 8 złp; 3. Spór Tomasza Jajczyka z Jakubem Łapką o szkody; 4. Maciej Kępa przeciw Stanisławowi Dąbrowskiemu o zwrot półtora korca żyta; 5. Marcin Rymarczyk przeciw Janowi o zwrot 17 złp.",
        "transkrypcja": "16v\nInter Paulum Nowak, et Joannem Tkaczyk, Suspenditur\nde productionem processus causae ad feriam secundam proxima de...\n\nW sprawie y Akcyey między Uczciwymi Tomaszem Stafią y Maciejem\nTkaczykiem z strony Złotych Ośmiu się replika za furę datur\ndilatio Inquisitionis względem Kontraktu Wymionego w te\ncztery fora conducire franchyniącymi ad feriam se-\ncundam proxima Ventura terminus conservatur.\n\nW sprawie między Uczciwymi Tomaszem Jayczykiem Przed-\nmieszczaninem a Jakubem Łapka Przedmieszczaninem\no szkody z oboiey strony w winnych, datur dilatio Inquisitionis.\n\nEx Instantia Honesti Mathiae Kępa suspicati contra Stanislao\nDąbrowski racione non restitutionis Siliginis semi duorum\ncoronarum praestari durant Marcani, partie Officio produce...\n\nW sprawie y Akcyey między Uczciwymi Marcinem Rymarczykiem\nAktorem a Janem Obrawenskiem o nieoddanie fl. 17 /-\nDatur dilatio processus productionis, in Quindena.\n\nActum coram Officio Advocatiali et Scabinali Kraśni-\ncensi Feria secunda post Festum sancti Fran-\ncisci Confessoris proxima Anno Domini Millesimo\nSeptingentesimo.\n\nW sprawie y Akcyey między Uczciwym Maciejem Kępą\nAktorem a Stanisławem Dąbrowskim o nieoddanie\nżyta półtora korca, pozwanym aby wywiedzenia pod ro-\nzsądkiem Summy podobney Złotych Ośm za żyta tey czworo\nkosztami oddał, terminus conservatur.\n\nW sprawie y Akcyey między Uczciwym Thomaszem Stafią Aktorem\na Uczciwym Maciejem Tkaczykiem, pozwanym. Ponieważ...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 37,
        "numer_pozycji": "Poz. 37",
        "strona_pagina": "fol. 17r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory gruntowe / Wadia sądowe i ugody",
        "osoby_podmioty": "Wojciech Skałka; Marcin Chmielik; Tomasz Zdebić [Zdeb / Zdebić]; Wojciech Konopka zmarły [Konopka]; Andrzej Sanek mieszczanin; Adam Wardęga; Jakub Wardęga syn Adama; Pasiek; Szymon Olchowski; Paweł Nowaczyk; Marina Nowaczykowa żona Pawła; Jan Tkaczyk",
        "kwoty_podatki": "18 złp; wadium 30 grzywien; ćwierć roli",
        "opis_sprawy": "Sesja z 13 października 1700 r.: 1. Spór Wojciecha Skałki z Marcinem Chmielikiem o przysięgę; 2. Tomasz Zdebić przeciw Andrzejowi Sankowi o ćwierć roli po zmarłym Wojciechu Konopce; 3. Zeznanie Adama i Jakuba Wardęgów w sprawie Pasieka o parę wołów w oborze Jajczykowej; 4. Protest instygatora przeciwko Olchowskiemu; 5. Uroczysta ugoda polubowna małżonków Pawła i Mariny Nowaczyków z Janem Tkaczykiem pod rygorem 30 grzywien wadium.",
        "transkrypcja": "17\nprzy zapisie, na którą iest nie mieli mocy aby oddał części\nzłotych Ośmnaście Wtkowi pod rachunkiem końcem onego\nustępuiącego, sub poenis Officij Arbitrarijs, terminus conservatur.\n\nSprawa między Uczciwymi Woyciechem Skałką, Aktorem a Mar-\ncinem Chmielikiem, Aby pozwany Dekretem ad Juramentum fero-\nwanemu stanęły strony. Aktor zaś na Piątek przyszły aby gotowi\nbyli z obu reflexive termin conservavie się zawity.\n\nW sprawie y Akcyey między Uczciwym Thomaszem Zdebiem\nAktorem o ćwierć roli po nieboszczyku Woyciechu Konopce\nPanu Aktora, A Andrzeiem Sankiem mieszczaninem pozwa-\nnym toczącey się, datur dilatio productionis Iuris quibus po-\nsessor extat tey ćwierci roli, idque in Quindena, termin\nconservatur.\n\nEx Instantia H. Thomae Jayczyk contra Pasieka.\nH. Adam Wardęga et Jacobi Wardęga filius Recognovit: Siedzia-\nłem we żniwa niedawno przeszłe wieczór hospodarczy\nIż para wołów w oborze u Tartasa Jayczykowey zawalałem\ndla furka, ale nie mogłem się u nikogo dopytać, bydło\ninne przyszło y ułaskawiło godzinę, w tenże deszcz.\n\nProtestatur Instigator contra H. Simonem Olchowski et fi-\nlium suum, Urząd Kraśnicki racione teyże za kuśnierzyka raci-\nonis przysięga żyta półtora korca p. p.\n\nActum coram Officio Advocatiali et Scabinali Kraśnicen-\nsi Feria Quarta Ante festum Sancti Hedvigis proxima\nAnno Domini Millesimo Septingentesimo.\n\nW sprawie y Akcyey między Uczciwymi Pawłem Nowaczykiem y Mariną małżon-\nkami, z iedney A Janem Tkaczykiem pozwanym, Ponieważ strony dosta-\npuiąc od Juramentu, o zgubę płoną y kradzieży Aktorom dobrowolnie\nz konfensem sądu ninieyszego do zgody o expensa przystąpiły y z tym\nbardziey z poparcia przystawiciel między stronami, Państwa\ngrzywien 30 Sąd za zgodą oboyga stron na obydwie\npowodowe zrzeczenie me dzielić każą, pro eodem była. / 17 /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 38,
        "numer_pozycji": "Poz. 38",
        "strona_pagina": "fol. 17v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy żydowskie / Bójki krwawe i obdukcje",
        "osoby_podmioty": "Tomasz Snoparski; Szymon Bratek; Tomasz Jajczyk; Bakałarz szkoły; Herszek żyd [Herszko]; Kuduka; Manaska żyd [Manas]; Paweł Słomkowski mieszczanin kraśnicki; Jan Śmieszkowic [Śmieszek]; Jędrzej Kotowicz; Katarzyna Kielbarkowa [Kielbarka]; Lejbek żyd [Leybko]; Katarzyna Pudlikowa córka Sznika [Pudlik]",
        "kwoty_podatki": "Zabicie wieprza; długi szynkowe; rany krwawe i broczenie krwią",
        "opis_sprawy": "Zapisy wokandy sądowej z połowy października 1700 r.: 1. Tomasz Snoparski przeciw Szymonowi Bratkowi o zabicie wieprza; 2. Tomasz Jajczyk przeciw bakałarzowi szkoły parafialnej; 3. Rozliczenia finansowe Żyda Herszka z Kuduką oraz Żyda Manaski z Pawłem Słomkowskim; 4. Areszt Jędrzeja Kotowicza w procesie Jana Śmieszkowica; 5. Zeznania Katarzyny Kielbarkowej i Katarzyny Pudlikowej o nocnej krwawej bójce pod kramem Żyda Lejbka.",
        "transkrypcja": "17v\nW sprawie y Akcyey między Uczciwymi Thomaszem Snoparskiem, z iedney\nA Szymonem Bratkiem, o zabicie wieprza, drugiey o potłuczenie\nzatwierdzać ad feriam Sextam proxima Ventura Inquisitionis terminus conservatur.\n\nW sprawie między Tomaszem Jayczykiem, z iedney A Bakałarzem Sami\nstrony kłopotu za rano płe winnych, datur dilatio Inquisitionis testis.\n\nW sprawie y Akcyey między Niewiernym Żydem Herszkiem A Kuduką\nzatwierdzać compositionis amicabili Una cum Calculatione ante\nferiam Juris Ordinari conservatur.\n\nW sprawie y Akcyey między Niewiernym Żydem Manaską, A JMP Pawłem\nSłomkowskim, gdzie Recipiend Calculationem ante prima Juris.\n\nW sprawie y Akcyey między Sławnym Panem Pawłem Słomkow-\nskiem, A Żydem Manaską, z drugiey strony, recessaria in\nInquisitionem causa fusa terming conservatur.\n\nW sprawie y Akcyey między Uczciwemi Janem Śmieszkowicem Aktorem,\nA Jędrzeiem Kotowiczem, o zgubę pewną recebanti\nincarcerationem admiserit, interea inquisitiones educat.\n\nEx Instantia H. Kuśnierz et Catharina Kielbarkowa Recognovit:\nPrzyszłam do Miasta wieczorem widziałam przed żydem\nLeybkiem, syna Żydzinowego teraz pobiłam na rąd dym-\no kurach piorunnych do domu swego, brat, siostry dzie-\nci moie y siostrzast a iam rany skąd zaczeta mocno\nwraz wiewiór krew z rany szła, tacto pectore.\n\nPudlikowa Katarzyna filia Sznika Recognovit.\n\nW sprawie y Akcyey między Uczciwym Matyasem Plewnikiem\nz Tomaszem Olchowskim chrzest o uwiezienia żyta z Uro-\ndzonego Aktorowi obwinionym Sąd pomiarkowawszy Inqui-\nzycię, Ponieważ Powodowa strona przyznał się szukaniem że\ndał rękę dyzmaruiąc się z ludzkich zbliżenia do kommissie\nJuramentem, za nawrot wprzód żyto z Interesu tollere\nprawin zatargom nie się powinnym dać wykonaniu w wagi\nod dać winny 3 grzywien o wadze fura w ręce nie wiedział termi-\nnus conservatur.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 39,
        "numer_pozycji": "Poz. 39",
        "strona_pagina": "fol. 18r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo sądu łączonego / Spory sąsiedzkie i graniczne / Kradzieże inwentarza",
        "osoby_podmioty": "Wojciech Gajowczyk [Gaiowczyk]; Szymon Brudzik przedmieszczanin; Wojciech Kowal; Moszko żyd [Moszek]; Andrzej Sanek; Tomasz Zdebić; Józef chłopak [famulus]; Izrael żyd [Israel]; Kazimierz Chmarowski; Jan Szymura; Kazimierz Mazurczyk; Szymon Moszkowicz żyd; Paweł Słomkowski",
        "kwoty_podatki": "Szkoda za 4 owce; płoty i miedze; spory wekslowe i handlowe",
        "opis_sprawy": "Sesja Sądu Łączonego (Officium Compositum) z 22 października 1700 r.: 1. Wojciech Gajowczyk przeciw Szymonowi Brudzikowi o szkodę za 4 owce zjedzone przez wilki; 2. Wojciech Kowal przeciw Żydowi Moszkowi o narzędzia; 3. Andrzej Sanek przeciw Tomaszowi Zdebiowi o wystawienie parobka Józefa; 4. Żyd Izrael przeciw Kazimierzowi Chmarowskiemu; 5. Jan Szymura przeciw Kazimierzowi Mazurczykowi o naruszenie miedzy i wygrodzenie płotu; 6. Żyd Szymon Moszkowicz przeciw Pawłowi Słomkowskiemu.",
        "transkrypcja": "18\nActum coram Officio Composito Kraśnicensi Feria Sexta post\nFestum Sancti Lucae Evangelistae proxima Anno Do-\nmini Millesimo Septingentesimo.\n\nW sprawie y Akcyey między Woyciechem Gaiowczykiem A\nSzymonem Brudzikiem, Przedmieszczaninem Kraśnickim, o\nSzkody Uczynione w sumie Owca od niedziel dziewiąta, aby\ndochodzić podział dni trzy. Owca szkody mu należoney potwora\nJurca aby oddał kosztów prawne aby powrócił idque in instantia\nsub poenis Officij ad arbitrijs de iure sententia vigore.\n\nW sprawie między Woyciechem Kowalem z iedney, A Żydem Moszkiem\nz drugiey o wozek datur dilatio Inquisitionis et productionis dowodów\nobronnych prima Juris terminus conservatur.\n\nW sprawie y Akcyey między Uczciwemi Andrzeiem Sankiem z iedney\nA Tomaszem Zdebiem o stawienie Chłopca Józefa sąsiedzkiego\nwzględem szkody poczynienia w srodku, datur dilatio Inquisitio-\nni. Interea ad praecatione H. Thomas Zdeb patris familias, statui\nprima Juris terminus conservatur.\n\nW sprawie między Niewiernym Izraelem Żydem A Kazimierzem\nChmarowskim o pretensyach necessaria faculacionem\nante prima Juris terminus conservatur.\n\nW sprawie y Akcyey między Uczciwemi Janem Szymurą, A Kazimierzem\nMazurczykiem o wygrodzenie się w grunt Aktora, aby pozwany\nna miedze Aktorey K. stawił żyta. Dzierżawcą gruntu sędziemu\ndla Informacyi Sądu wizy komisarz kazał za kładąc budynek\nz prima Juris, ventura fra secunda proxima Ventura.\n\nEx parte Infidelis Simonis Moszkowicz, Sławetny Paulus\nSłomkowski racione damni in termino conservato aducen-\ndam Inquisitioni, in judicium tuens.\n\nSub Eodem Actu\nH. Simon Olchowski Oyciec y Szwagier Mathias Plewnik.\nCzy li do niedziele zadosyć Uczynić decretowi za\nSyna swego Oyca Thomasza y Szwagra, sub poenis dementi. / 18 /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 40,
        "numer_pozycji": "Poz. 40",
        "strona_pagina": "fol. 18v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Obdukcje krwawe i napaści / Przemoc rzemieślnicza",
        "osoby_podmioty": "Maciej Stelmachowicz szewc [Mathias Stelmachowicz]; Jan Wawronkowicz napastnik [Joannes Wawronkowicz]; Stanisław Jerzykiewicz podwójci [Viceadvocatus]; Maciej Napora ławnik; Marina Starobracikowa wdowa; Wawrzyniec Starybratek zmarły",
        "kwoty_podatki": "Czapka barankowa błękitna; kontusz szarozielony; 15 złp z chustką zrabowane w szynku",
        "opis_sprawy": "Sesja z 25 października 1700 r.: Krwawa obdukcja sądowa pobitego szewca Macieja Stelmachowicza przez podwójciego Stanisława Jerzykiewicza po brutalnej napaści Jana Wawronkowicza (rany cięte głowy, wybite oko, zbroczony krwią kontusz, kradzież błękitnej czapki barankowej i 15 złp w szynku żydowskim). Następnie skarga wdowy Mariny Starobracikowej o spadek po mężu Wawrzyńcu.",
        "transkrypcja": "18v\nActum coram Officio Advocatiali et Scabinali Kraśnicen-\nsi Feria Secunda Ante Festum Sanctorum Simonis\net Judae Apostolorum proxima AD 1700.\n\nDo Urzędu y Akt ninieyszych w osobie swoiey przyszedłszy\nUczciwy Maciey Stelmachowicz, rzemiosła szewskiego o-\nbywatel Kraśnicki z solemni protestatione contra Joannem\nWawronkowicz causatum in sola Kraśnicensi Infrascripti\nViolentiarum motorem Principalem, et eius complices.\nIn Eodem Wojciechowicz locum tenens Kraśnicki ordinis fi-\ncum protestationis Vispiceationis inspectione Visitatio-\nni sui Jerzykiewicz Viceadvocati, et Honor Maciey Napora\nławnik. Na lewey stronie głowy na rogu raz przecięty na półtora\nczłonka wzdłuż w szerz na półczłonka, z którego natęże-\nnie stronie lewey sine spuchły, Kark siny spuchły, Na\nprawey stronie Oko podbite, drugie także sine krwią zaszłe,\nKrew nadosiekiem stłuczona, Twarz wszystka krwią\nzbroczona. Item Na prawey ręce pod łokciem raz przecięty\nod członka, palce wszyscy wzdłuż przy przegubku siny spuchły,\nraz krwawy stłuczony. Item plecy w pysk mocno spuchłe,\nItem asseveruit że Bałtami na odlew zeszli zeście puści\nod głów postawiwszy od wielkiego samotania powtórzeniem\nsiebie. Item prezentował Kontusz semazielony maćki\nw nienawerz skalany ze krwią czerwony. Item asseveruit że mu\nczapka zginęła barankowa błękitna, piętnaście zło-\ntych z chustką także nową w domu u Żyda\nwygląda Wieczorem, dma weroroy jego straty podda-\nli i przydupnego bez dania i kwit zadane, offerens se.\n\nSub eodem Actu\nDo Urzędu y Akt ninieyszych, w osobie swoiey przyszedłszy\nUczciwa Marina Starobracikowa niegdy Wawrzyńca\nStarego bracika z Kraśnika małżonka, z misją prote-",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 41,
        "numer_pozycji": "Poz. 41",
        "strona_pagina": "fol. 19r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy majątkowe i długi / Kary za kontumacje",
        "osoby_podmioty": "Marina Starobracikowa wdowa; Maciej Musielak szewc [Musielak / Musiał?]; Andrzej Sanek przedmieszczanin; Tomasz Zdebić; Szymon Miszkowicz żyd [Miszkowic]; Marianna Miszkowiczowa żona Szymona; Paweł Słomkowski mieszczanin; Albert Kowal; Haykler żyd [Haykiel]; Stanisław Młynarczyk",
        "kwoty_podatki": "100 złp długu; 40 złp długu; grzywna kary za kontumację; gwoździe kowalskie",
        "opis_sprawy": "Dalszy ciąg spraw z 25 października 1700 r.: 1. Marina Starobracikowa żąda 100 złp od Macieja Musielaka szewca z tytułu ugody spadkowej; 2. Andrzej Sanek przeciw Tomaszowi Zdebiowi o szkody polne chłopca; 3. Żydzi Szymon i Marianna Miszkowiczowie przeciw Pawłowi Słomkowskiemu o zwrot długu 40 złp; Słomkowski ukarany grzywną za niestawiennictwo; 4. Albert Kowal manifestuje przeciwko Żydowi Hayklerowi o kradzież gwoździ; 5. Utrata praw do gruntu przez Stanisława Młynarczyka.",
        "transkrypcja": "19\nstutione przeciwko Opatrznemu Maciejowi Musielakowi [Musiałowi?] szewco-\nwi z Kraśnika, Iż Ona prezentowała Złotych sto polskich\nvigore komplanaciey między sobą uczynioney, dosyć czyniąc\nmanifestuię się.\n\nActum coram Officio Advocatiali et Scabinali\nKraśnicensi Feria 2-da Ante Festum Sanctorum\nSimonis et Judae Apostolorum proxima Anno\nDomini Millesimo Septingentesimo.\n\nW sprawie y Akcyey między Uczciwymi Andrzeiem Sankiem, Przedmie-\nszczaninem Kraśnickim z iedney Aktorem A Tomaszem Zdebiem\no stawienie chłopca o szkody uczynione doniesienia skargi,\nchłopiec na examen o szkodzie terminus conservatur.\n\nSprawa między Uczciwymi Andrzeiem Sankiem y Thomaszem\nZdebiem o Sukcessią, datur dilatio ad futuram Ju-\ndicum Diem, terminus conservatur ad Octavam.\n\nW sprawie y Akcyey między Niewiernym Żydem Miszkowicem, A\nSławetnym Pawłem Słomkowskim Mieszczaninem, nakazał\nsąd aby grzywnę iedną dał na zmęczenie contumaciey obo-\nwiązaney z zachowanego terminu zastawoney, która winę\ndarowała strona powodowa. Interea Innegoż Principalis\nstronom przystąpić na traktat. Tandem in directione Juridica.\n\nW sprawie y Akcyey między Niewiernym Szymonem Miszko-\nwicem Obywatelem Kraśnickim y Marianką małżonkami\nz iedney A Pawłem Słomkowskim, M. Kraśnickim o\nzłotych 40, obliguią Aktorów do poprzysiężenia ruten\ndług wy na karcie notarowałas circa praestandum Juramentum\ncedita dy feria Sexta proxima Ventura.\n\nManifestatur H. Albertus Kowal contra Infidelem Haykler\no gwoździe, protestatio contra Eundem.\n\nLapsus contra H. Stanislaum Młynarczyk, racione ademptionis\nfundi do terminum protestatur. / 19 /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 42,
        "numer_pozycji": "Poz. 42",
        "strona_pagina": "fol. 19v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory graniczne i płoty / Sprawy żydowskie i długi",
        "osoby_podmioty": "Kazimierz Krakowiak; Jan Pielaszkowicz; Jan Szymura mieszczanin kraśnicki; Stanisław Młynarczyk; Wojciech Kowal; Chajka żyd [Chayka]; Andrzej Sanek; Tomasz Zdebić; Józef Gąsiorowski chłopak; Foxowa wdowa [Foksowa]; Paweł Świerk [Świerk / Świerczek?]; Berek Chaja żyd; Gorgol; Izrael Fortunat żyd; Jan Krasowski; Katarzyna Chudzikowa; Piotr Bałata zmarły",
        "kwoty_podatki": "Płot i miedza; złoty 1 i groszy 7; 3 złote polskie z prowizją",
        "opis_sprawy": "Sesja z 27 października 1700 r. (Wigilia św. Szymona i Judy): 1. Kazimierz Krakowiak i Jan Pielaszkowicz; 2. Jan Szymura przeciw Stanisławowi Młynarczykowi o zniszczenie płotu, zagarnięcie gruntu i nielegalny najem Żydom; 3. Wojciech Kowal przeciw Żydowi Chajce o 1 złp 7 gr; 4. Spór Sanka ze Zdebiem o parobka Józefa Gąsiorowskiego; 5. Wdowa Foksowa przeciw Pawłowi Świerkowi o rolę Kozowską; 6. Spory Żydów: Berek Chaja przeciw Gorgolowi o pobicie, Izrael Fortunat przeciw Janowi Krasowskiemu o 1 fl., Katarzyna Chudzikowa po Piotrze Bałacie o fl. 3 z prowizją.",
        "transkrypcja": "19v\nEx Instantia H. Casimiri Krakowiak, H. Joannes Pielasz-\nkowicz Recognovit.\n\nActum coram Officio Advocatiali et Scabinali Kraśnicensi Feria\nQuarta in Vigilia Festi Simonis et Judae Apostolorum Anno\nDomini Millesimo Septingentesimo.\n\nW sprawie y Akcyey między Uczciwymi Janem Szymurą po-\nzwany Mieszczaninem Kraśnickim A Stanisławem Młynarczy-\nkiem; z strony płotu rozrwania y gruntu podzierżenia w te\nwypuszcza Żydom Ichże skazania gdzie ujściem, zarekwi-\nrował obliguie pozwanego do odprzysiężenia się tak płotu\niako y nie posiadania miedzy do prima Juris poruszonego\nprzyszliie solue, z dziedzicem tegoż gruntu Żydom dzierżawiącym\nwziąść.\n\nW sprawie y Akcyey między Uczciwym Woyciechem Kowalem A Żydem\nChayką aby za kordegardę oddał złoty ieden y groszów siedm\nin facto.\n\nW sprawie między Uczciwymi Andrzeiem Sankiem, a Tomaszem\nZdebiem, o stawienie Chłopca Józefa Gąsiorowskiego, który\nszkody poczynił Aktorowi. Ponieważ Iudicium deiekt z akt\nrexit wersarz pozwany ma przysiądz iako nie dał skargi\nUczciwostki teraz żeby sobie iako winnego sobie, post quidam\nrecognitione liber promuntiatur citatus.\n\nW sprawie y Akcyey między Uczciwą Foxową wdową a Pawłem\nŚwierkiem względem nie przyłożenia się z ćwierci roli do\nputanka Kozowskiego należącey tak koszty czyni, w całości\ndatur dilatio productionis Iuris terminus conservatur.\n\nEx parte Berek Chaia H. Gorgol o pobicie continua 3 fl.\nEx parte Izrael Fortunat H. Joannes Krasowski racione floreni 1\ncontinua 3 fl.\nEx parte H. Catharina Chudzikowa olim H. Petri Bałata\nracione floreni 3, cum prowisione continua 3 fl. / 19v /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 43,
        "numer_pozycji": "Poz. 43",
        "strona_pagina": "fol. 20r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Zeznania świadków / Spory sąsiedzkie i bójki polne",
        "osoby_podmioty": "Józef Wilk [Iosephus Wilk]; Barbara Młodońcowa wdowa [Młodonica / Młodońcowa]; Tomasz Zdebić [Zdeb / Zdebić]; Józef Zdebić syn Tomasza; Andrzej Sanek [Panek / Sanek]; Żona Sanka; Gospodarz z Podlesia",
        "kwoty_podatki": "14 grzywien kary; 23 złote polskie pretensji; zniszczenie zagonu grochu",
        "opis_sprawy": "Zapisy z jesieni 1700 r.: 1. Józef Wilk przeciwko wdowie Barbarze Młodońcowej o pretensje 23 złp; nałożenie kary 14 grzywien; 2. Wpis z 7 września 1700 r. (Wigilia Narodzenia NMP): Barwne zeznanie Józefa Zdebia syna Tomasza o awanturze w polu grochu; Andrzej Sanek bez koszuli wypadł z zagrody, wykrzykiwał o złodziejstwie i uderzył ojca powrósłem od kobyły; interwencja gospodyni i bójka na miedzy.",
        "transkrypcja": "20\nW sprawie y Akcyey między Uczciwymi Józefem Wilkiem Aktorem\no pretensye summy Uczciwey Barbarze Młodońce wdowie a po-\nwiedział dwadzieścia trzy groszy 15, quo neno z nieuważenia\nnam nakazana w dworze czternaście grzywien.\n\nActum coram Officio Advocatiali et Scabinali Kraśnicensi\nFeria Quarta Ante Festum Nativitatis Beatissimae\nMariae Virginis proxima die 7-ma Septembris\nAnno Domini Millesimo Septingentesimo.\n\nEx Instantia Honesti Thomae Zdebić Josephus Syn mianowany:\nSzliśmy w niedziele wieczór wygnaniem gruntu w wyroczku żoły\nte Sankowe poszliśmy wygnaniem. Ona znowu wparła w tym\nprzyszedł gospodarz powiada Opowiadacie o niey w grochu Gospodarz\nKazał dać brać Sankowi owce. Zgoniwszy w tym Gospodarz przyszedł\ndo brochu Sanek też z nami wyszedł z trzody swoiey bez wszyt-\nkiego brogu wołał złodzieystwo iakies na Gospodarza y na mnie,\nprzyparty o powróz od kobyły, na ostatku wołał o krowy rosprawisz\ngdzie by ona na nim była wyrobiona szkody w tym przyszliśmy\ngospodarz syn powrotem w nogi Kobyły, Odurazał Sanek powrózy\ndo Kopy zrzuconym bez głowę uderzył y rzucili się obadwa kłami.\nGospodarz będąc upadł się do onego ku Ziemi przysiadł. Zatem\nona Gospodyni oycu przyszła gospodyni broniła, kazał wodzić.\nOn wstawszy powrozem bił, pozwany szałas odhaczył y po-\ntowarzyszył w sztoch go tam też z sobą szarpali, ale gospodarz\nrazy swoie miewał, a dać bo był pisany Olbramski. / 20 /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 44,
        "numer_pozycji": "Poz. 44",
        "strona_pagina": "fol. 20v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo sądu łączonego / Spory majątkowe i spadkowe / Elity miejskie i Zamoyscy",
        "osoby_podmioty": "Andrzej Sanek przedmieszczanin; Tomasz Zdebić; Maciej Kępa przedmieszczanin; Magdalena Kłopotowa wdowa; Stanisław Płechowicz burmistrz dawny i deputat Trybunału Zamojskiego [Płech]; Jędrzej Płechowicz brat Stanisława; Jakub Kłopot przedmieszczanin; Łukasz Paszanowski zmarły; Sukcesorzy Petrykowscy",
        "kwoty_podatki": "Wadium 14 grzywien; spadek po Łukaszu Paszanowskim; pensja kościelna",
        "opis_sprawy": "Sesje z września i października 1700 r.: 1. Andrzej Sanek przeciw Tomaszowi Zdebiowi o zasiewy w polu i szkody; wadium 14 grzywien; 2. Maciej Kępa przeciw Magdalenie Kłopotowej wdowie o pretensje; 3. Wielki proces z 10 września 1700 r.: Sławetny Stanisław Płechowicz dawny burmistrz kraśnicki i deputat do Trybunału Zamojskiego, w imieniu swoim i brata Jędrzeja, przeciwko Jakubowi Kłopotowi o dobra pozostałe po śp. Łukaszu Paszanowskim i wyegzekwowanie pensji kościelnej.",
        "transkrypcja": "20v\nActum coram Officio Advocatiali et Scabinali Kraśnicensi\nFeria Quarta post festum Sancti Dionysii proxima\nAnno Domini Millesimo Septingentesimo.\n\nW sprawie y Akcyey między Uczciwymi Andrzeiem Sankiem Przed-\nmieszczaninem Kraśnickim y Tomaszem Zdebiem, Zapis\nO dymiech O Zasienie w polu uczynione przychodzić Aktorowi\nPotrzebna być komplanaciey uczynienia między stronami gdy\nin instantia sub poenis Officij Arbitrarijs Sędziom przy-\nsięgę czternaście grzywien Sąd zakłada, servandus\npoenis, Któraby strona stronie gwałtu ponowienia poważyłaby się\nDecreti Judicis vigore.\n\nActum coram Officio Composito Kraśnicensi Feria Sexta\npost Festum Nativitatis Beatissimae Mariae Virginis pro-\nxima Anno Domini Millesimo Septingentesimo.\n\nW sprawie y Akcyey między Uczciwymi Maciejem Kępą, Przedmieszczani-\nnem Kraśnickim Aktorem, A Magdaleną Kłopotową wdową\nDatur dilatio responsi producendum summa Juris.\n\nW sprawie y Akcyey między Sławetnym Panem Stanisławem\nPłechowiczem [Płech] Burmistrzem dawnym Kraśnickim Depu-\ntatem Sądów Naywyższych Trybunału Miast Państwa\nZamoyskiego, w Imieniu swoim y Jędrzeja brata tegoż Płecho-\nwicza, A Uczciwym Jakubem Kłopotem\nprzedmieszczanina Kraśnickiem w Prawie dekretem\nŁukasza nowszego Dobr niegdy Łukasza Paszanowskiego\nSukcessorów, małżonkami swemi y Petrykowskimi\nmałżonkami fundatorem względem delegacyi legowa-\nney które wleli nie byliżytemi dziś trzymania y nie",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 45,
        "numer_pozycji": "Poz. 45",
        "strona_pagina": "fol. 21r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory rodzinne i spadkowe / Szkody polne",
        "osoby_podmioty": "Jakub Kłopot; Ewa Onuszkowiczowa wdowa [Onuszkiewicz]; Tomasz Stafia; Kazimierz Stafia syn Tomasza; Wojciech Kowal; Gierkardowa wdowa; Maciej Kępa; Paweł Kłopot; Maciej Kuźnik; Sobestian Jarzyk; Magdalena Kłopotowa wdowa; Marina Luterkowa wdowa z Zaklikowa [Luterek / Luter]; Wojciech Luterek zmarły; Stanisław Luterek szwagier",
        "kwoty_podatki": "Spłata pensji kościelnej; szkoda przez woły; pretensje spadkowe",
        "opis_sprawy": "Zapisy z października 1700 r.: 1. Nakaz dla Jakuba Kłopota spłaty zaległej pensji kościelnej z dóbr Paszanowskiego; 2. Ewa Onuszkowiczowa przeciw Tomaszowi Stafii o stawienie syna Kazimierza; 3. Wojciech Kowal przeciwko wdowie Gierkardowej o szkody poczynione w polu przez woły; 4. Zeznanie Pawła Kłopota o oględzinach ról Kłopotowej; 5. Uroczysta skarga wdowy Mariny Luterkowej z Zaklikowa przeciw szwagrowi Stanisławowi Luterkowi o zabór majątku i znieważanie matki.",
        "transkrypcja": "21\npłacenia pensiy. Pozwanemu Sąd ninieyszy z kontro-\nwersyey stron obudwu wyrozumiawszy Legacyą dokumentów\nauthentyczny z nie oddał Nakazał aby pro hac teme-\nritate pozwany Kłopotowi ferowani kosztów kosztem\nprawne w rot liczby dni trzy kontynuował, grzywien dwa-\ndzieścia, panamodementis Sądowi oddali decreti Juris\nvigore.\n\nW sprawie y Akcyey między Sławną Panią Ewą Onuszkowiczową\nwdową A Tomaszem Stafią Przedmieszczaninem o stawienie\nSyna Kazimierza który ponieważ się sam dobrowolnie przyznał\nze zaszedł wrostki spraw jego aby go stawił do mieyca\nod dąż zadzierzgnąc, idę decreti sententia vigore.\n\nW sprawie y Akcyey między Uczciwym Woyciechem Kowalem Obywatelem Kra-\nśnickim z iedney, A Sławną Panią Gierkardową wspólniczką\nże wynidzieli przez woły szkodowany Aby za szkodę dała złotych\ndwa Aktorowi, in instantia sub poenis Officij Arbitrij.\n\nSławetna Ewa Onuszkowiczowa Wdowa manifestatur, o odda-\ngeniu zaś in debite sui relationis z nobilium saddmi-\nni Długopolski.\n\nActum coram Officio Composito Feria secunda post die\nFesti Sancti Francisci A.D. 1700.\n\nEx Instantia H. Mathiae Kępa et Paulus Kłopot Recogno-\nwit: in fide formalia Obwodził nami Macieyem Kuźni-\nkiem, wraz z Sobestianem Jarzykiem, przedmieszczany\nWidzieliśmy ślad w tatarce na pustoszy Kłopotki.\nWidziałem Iż brodziska Pawła Kudurska cudzą y teraz\nna pustkach chodził Szymon z Truskawką też zrobione\nod żyta się szkodę widzieli Kłopotowey wdowy wyle ale\nbardziey od koni szkodę widzieliśmy, tacto pectore Recogno-\nwit.\n\nNa Skargę Mariny Luterkowey niegdy Uczciwego Woyciecha Lu-\nterka Mieszczanina Zaklikowskiego małżonki wdowy: Wypo-\nwowiada się przeciwko Uczciwemu Stanisławowi w tey mierzy przed / 21 /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 46,
        "numer_pozycji": "Poz. 46",
        "strona_pagina": "fol. 21v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy karne i lżenia / Sąd bannityczny nad sodomitą",
        "osoby_podmioty": "Stanisław Luterek obwiniony; Marina Luterkowa wdowa z Zaklikowa; Matka Luterkowa; Jak żyd [Iak]; Maciej Tkaczyk; Jan Majowski wójt; Adam Kotowicz burmistrz; Stanisław Płechowicz deputat; Stanisław Jerzykiewicz podwójci; Albert Borkiewicz ławnik; Wawrzyniec Pielaszkowicz ławnik; Szymon Kuparka obwiniony z Wilkołaza",
        "kwoty_podatki": "Dług 37 złp 12 gr; areszt w więzieniu ratuszowym (inkanceracja)",
        "opis_sprawy": "Zapisy z października 1700 r.: 1. Dekret aresztu dla Stanisława Luterka za ordynarne lżenie matki i szwagierki ('Kurwo Babo iść z domu precz nie miała, to ciebie z Miasta wyrzucę'); 2. Żyd Jak przeciw Maciejowi Tkaczykowi o zwrot 37 złp 12 gr; 3. Nadzwyczajny Sąd Bannityczny pod przewodnictwem wójta Jana Majowskiego i burmistrza Adama Kotowicza nad Szymonem Kuparką z Wilkołaza o przestępstwo sodomii.",
        "transkrypcja": "21v\nsię iemu o to: Iż On znawczorayszego porwawszy się przeciwko\nMatce swoiey, kłamcą poszanowania z przykazania Boskiego powstał\ny się upominał aż mu zabrała pieniędzy za dobra tegoż\ngodna swego, y obietnice komina. On z ust słowami powstał\ny aby żarłocze wynieść gdzie podkradł w domu u Jego, Wstał\ny z czeladnikiem, gadaiąc z sypiącą żonę w te czasy przy-\nszedł y rzekł te słowa: Aby Kurwo Babo iść z domu precz nie\nmiała, to ciebie z Miasta wyrzucę. Wyskoczą bo-\nwiący skoczył do pora y chciał ią pchnąć albo w Matkę,\nżeby ta Kurwa Baba nie była. W tym widziałem wszystek z synow-\nszczyzny. Wszystkim Sąd ninieyszy do inkanceracyey dekretował.\n\nW sprawie y Akcyey między Niewiernym Jakiem Aktorem A\nMaciejem Tkaczykiem, pozwanym o nieoddanie\nzłotych trzydzieści y siedm groszy dwanaście, aby w po-\nchodach dwuch niedzielach oddał pozwany, sub poenis Officij Arbi-\ntrarijs.\n\nJudicium Necessarium Bannitum per Spectabiles Honoratos\nJoannem Majowski Advocatum Kraśnicensem, Adamum\nKotowicz Proconsulem, Stanislaum Plech Consulem et\nDeputatum Judicij Supremi Tribunalis Civitatum Dominii\nZamosciani, Stanislaum Jerzykiewicz Viceadvocatum, Al-\nbertum Borkiewicz, Laurentium Pielaszkowicz scabinos, Feria\nSecunda post die Festi Sancti Francisci A.D. 1700.\n\nCoram eodem Officio constitutus personaliter comparens\nLaboriosus Szymon Kuparka z Wilkołaza Wsi libere Re-\ncognovit: Iest temu niedziel pięćty Jakom z Miasta Kra-\nśnika",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 47,
        "numer_pozycji": "Poz. 47",
        "strona_pagina": "fol. 22r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo karne / Przesłuchania kryminalne / Areszty więzienne i wadia",
        "osoby_podmioty": "Szymon Kuparka z Wilkołaza; Klara z Budzynia; Wawrzyniec Klara mąż Klary; Szymon Wójtowicz wójt gromadzki z Wilkołaza; Jan Tokarski; Stanisław Luterek; Albert Kowal; Śmietanka wdowa",
        "kwoty_podatki": "Areszt w więzieniu miejskim; szkody polne",
        "opis_sprawy": "Zapisy z października 1700 r.: 1. Dalszy ciąg zeznań Szymona Kuparki o służbie pasterskiej na Budzyniu u Klary i Wawrzyńca oraz rozmowie z wójtem gromadzkim Wilkołaza na jarmarku; nakaz odprowadzenia obwinionego pod strażą do lochu; 2. Jan Tokarski i Stanisław Luterek aresztowani w więzieniu miejskim za szkody i gwałty; 3. Pozew Alberta Kowala przeciwko Śmietance.",
        "transkrypcja": "22\nśnika Jechał na szpichlerz w nocy na Budzyń u\npasterza do Wawrzyńca Jegomości Pana Bilskiego pasterzem\niechałem, Bratnią szkapą Klarą Wawrzyńca syna\nKlara tam dotknąłem się tey Szkapy człowiekiem przed się\nczworo pamiątka Opatrznego Starania, Na nim nie\nchodziło niewiele szkodzi przy karczmie, Abym nie na-\niechał. Szymon Wóytowicz sam Wóytowicz Wóyt\nGromadzki rzekł mi: co robisz człowiecze zapa-\nmiętały żeś się do takiego grzechu ważył wielkiego.\nJam do niego nic nierykł, z wielkiego wstydu\nw tym poiechałem wprzód a On za mną. Gdy\nprzeto lat dwadzieścia mieszkaiąc nie czuł tego Uczynku\nmego aż w niedzielę wyszły na Jarmarku w\nBychawie, gdzie z Wóytowicz był prosiłem na\npiwo do gospody, prosiłem aby Ojcom nie wspominał,\ny iemu nagrodę obiecował. Uprosiłem go napi-\nwo a przecie wymawiał mi: Wóytowicz był iest\nczłowiek z tego państwa we wsi Obiey mieysce\nPanem we dworze.\n\nPost eandem liberam confessionem ad carceres demandatur.\n\nEx parte Honesti Joannis Tokarski et Stanislaus Luterek\nArrestatur in carcere ratione poplatium subministrationis w\nKielpnie a który datu szkody podięte pro ut proponit\niudicialiter sub aggravationibus sui in tria.\n\nEx Instantia Alberti Kowal decretum quatenus fruerat\ncitata H. Śmietanka pro feria Sexta proxima Ventura. / 22 /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 48,
        "numer_pozycji": "Poz. 48",
        "strona_pagina": "fol. 22v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory cechowe i szewskie / Wizje lokalne w sadach",
        "osoby_podmioty": "Maciej Kępa przedmieszczanin [Mathias Kępa]; Maciej Kurek [Kuźnik / Kurek?]; Maciej Prokopowicz [Brokopowicz]; Magdalena Kłopotowa wdowa; Wojciech Borkiewicz ławnik; Maciej Borowiecki cechmistrz szewski [Majster Cechu Szewskiego]; Urząd wójtowski i ławniczy",
        "kwoty_podatki": "Szkody w tatarce i konopiach; wycena szkód w sadzie owocowym",
        "opis_sprawy": "Sesje z 15 i 17 września 1700 r. (Podwyższenie Krzyża Świętego): 1. Maciej Kępa i Maciej Kurek zeznają o szkodach polnych w tatarce i zdeptanych konopiach na gruncie wdowy Kłopotowej; 2. Wizja urzędowa ławnika Wojciecha Borkiewicza i starszego cechu szewskiego Macieja Borowieckiego w sprawie strat i wycinki drzew w sadzie owocowym.",
        "transkrypcja": "22v\nActum coram Officio Advocatiali et Scabinali Kraśnicensi Feria Quarta\nin Crastino Festi Exaltationis Sanctae Crucis A.D. 1700.\n\nEx Instantia H. Mathiae Kępa Suburbani Kraśnicensis et Mathia Kurek [Kuźnik?]\nByłem proszony od Macieia Kępy do szkody potatarczonego\nz Matyasem Prokopowiczem tamżeśmy widzieli szkody tylko\nkonopiskoy bydła starego kopytami wytarguiące y z pola z rolady\ntakże y od kur podeptane Uznaliśmy te szkodę na snopów\ntrzydzieści a tatarki narzekał y na innych sąsiadów podłe ról\ntegoż gruntu nie tylko na wdowę Kłopotową, tacto pectore.\n\nActum coram Officio Advocatiali et Scabinali Kraśnicen-\nsi Feria Sexta post Festum Exaltationis Sanctae Crucis\nproxima Anno Domini Millesimo Septingentesimo.\n\nDo Urzędu y Akt ninieyszych Wóytowskich y Ławniczych\nKraśnickich, w osobach swoich stanąwszy Sławetni Pa-\nnowie Woyciech Borkiewicz Ławnik, Maciey Borowiecki\nMayster Cechu Szewskiego, świadkowie przysięgli bywszy na\nroli potrawu wyproszonego w sadzie, potłuczeni w sadzie\nAndrzeia Sanka, gdy nad ptactwo wiecey wypasionej\npotrawu nie widzieli, quod Actis connotationis est. / 22v /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 49,
        "numer_pozycji": "Poz. 49",
        "strona_pagina": "fol. 23r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo komisarskie i wójtowskie / Jurysdykcja zamkowa / Arendarze i kontumacje",
        "osoby_podmioty": "Pinchas Dawidowicz arendarz ordynacki [Pinchas Dawidowic]; Józef Mazała obywatel kraśnicki [Ioseph Mazała]; Tomasz Jardzyk [Jardzyk / Jarzyk?]; Sąd Kommisarski Zamku Kraśnickiego; Sąd wójtowski i ławniczy kraśnicki",
        "kwoty_podatki": "Kara 7 grzywien za nieposłuszeństwo i niestawiennictwo; arenda trunkowa",
        "opis_sprawy": "Sesja z 22 września 1700 r. na styku jurysdykcji zamkowej Ordynacji Zamojskiej i sądu miejskiego: Sprawa Niewiernego Pinchasa Dawidowicza arendarza trunków ordynackich przeciw Uczciwemu Józefowi Mazale o rozliczenia; Tomasz Jardzyk za niestawiennictwo i zlekceważenie dekretów sądu zostaje ukarany grzywną 7 grzywien.",
        "transkrypcja": "23\nIż maiąc sprawę w Sądzie Naszym Kraśnickim o karę z dekre-\ntu Sądu niniejszego, Iż apellavit do Sądu Naszego na ten termin\nw tym Sądzie stanąłby gdyby podstąpił prawie czte-\nremu opowiedział dawszy dworyszto dowod Nazwanie\nnie poszedł dawszy dworzyszto dowód Nazwanie\nnależycie Kondemnatę w teyże sprawie iako y podane\nsobie nakazał tego przełożenia mieysca to czarne\nObywatele y one publikuią nie o lepsze popiół\nPan Sanecki, Na termin za karanią pod stołem\nstanął lubonie Sąd Nasz Kommisarski Zamku Kra-\nśnickiego Was należycie Sądzi. Kondemnaty przeciwko tey\npublikaciey w sprawie pryncypalney postempować roz-\nkaże. Dan z Kancellaryi Naszey we Dworku przy Dwi-\nrdziego [?] Opata Roku Pań 1700.\n\nActum coram Officio Advocatiali Feria 4-ta ante Festum S. Michaelis Archangeli\nproxima A.D. 1700.\n\nNa terminie dyspozycyi zachowanym stronom urzędowego\nNazwiskiem konsystencyi fendraturkuyey Pinchasem Dawidowicze\nArendarzem Obywatelem Kraśnickim z Kard z iedney, A Uczciwym Józefem\nMazałą Żołnierzem [Mazałem / Obywatelem?] pozwanym toczącey się sprawie ad contentan-\ndum propositionis coram eodem Officio facte.\n\nSąd ninieyszy Wóytowski y Ławniczy Kraśnicki nie trwaiąc prawie\nsię do dowodzącey sprawy o którą rzecz idzie przy podawaniu\npozwanego rachunuiąc tylko za same lekkomyślności\nSądu że z Fayka y 20 dutonens do Sądu przyszedł fundunde\nsobie postępuiąc Uznawacie sprawę z Uczciwym Tomaszem\nJardzykiem o 50 spin Beczki teyże do mieysca arzę trzymały\nw tym in subordinati postąpił sobie Ut Assensio by dali\nArreanti grzywnami siedm słusznie karaney a gdyby\nwniósł które nox recessit ab Officio, Sąd oddał nakazał\ndecreti praesens vigore. / 23 /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 50,
        "numer_pozycji": "Poz. 50",
        "strona_pagina": "fol. 23v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Akta zamkowe Ordynacji Zamojskiej / Uniwersały i arendy",
        "osoby_podmioty": "Franciszek Sitarski mieszczanin kraśnicki [Franciscus Sitarski]; Anna z Gnińskich Zamoyska [Anna z Gnina Zamoyska Podkanclerzyna Wielka Koronna]; Pinchas Dawidowicz arendarz żydowski; Józef Mazała; Sąd Kommissarski Zamkowy Kraśnicki",
        "kwoty_podatki": "Pozwy zamkowe; arendy ordynackie; pretensje handlowe",
        "opis_sprawy": "Sesja z 15 września 1700 r.: Franciszek Sitarski obywatel kraśnicki oblatuje w księgach miejskich urzędowy pozew i uniwersał Jaśnie Oświeconej Anny z Gnina Zamoyskiej, Podkanclerzyny Wielkiej Koronnej, Pani na Zamościu i Hrabstwie Kraśnickim; sprawa dotyczy wezwania przed Sąd Kommisarski Zamkowy Uczciwego Józefa Mazały z instancji arendarza Pinchasa Dawidowicza o rozliczenie arend i obligacji.",
        "transkrypcja": "23v\nActum coram Officio Advocatiali et\nScabinali Kraśnicensi Feria Quarta\nin Crastino Festi Exaltationis Sanctae\nCrucis Anno Domini Millesimo Septin-\ngentesimo.\n\nDo Urzędu y Akt ninieyszych Wóytowskich y Ła-\nwniczych Kraśnickich w osobie swoiey stanąwszy Opatrz-\nny Franciszek Sitarski Wierny Authenticzny Oby-\nwatel Kraśnicki in vim sui certae fidele relationis\nsponte palam publice libereque Recognovit Iż\nOn pozew z Instanciej w teyże niżej wyrażoney\nprzeciwko stronie niżey wyrażoney pozwaney au-\nthentyczny podany, cuius tenor sequitur talis:\n\nAnna z Gnina na Zamościu Zamoyska [Anna Zamoyska z Gnińskich Podkanclerzyna Wielka Koronna]\nSub Eodem Actu plenipotentia\nAnna z Gnina na Zamościu Zamoyska Podkanclerzyna\nKoronna Wielka Koronna Bełzka, Radomska, Rostowska et\nStarościna et Fundatrix etc. Uczciwemu Józefowi Ma-\nzała Obywatelowi Kraśnickiemu pozwaią ninieyszym roskazuiąc\naby przed Sąd moy Kommisarski Zamku Kraśnickiego na Piątek\nw dniem iutrzeyszy stawał proinde 17 Mensis Septembris\nAD currente 1700 Z Instanciej Niewiernego Pincha-\nsa Dawidowicza Żyda Obywatela Kraśnickiego A ten\nninieyszy pozew z rąk podał Samowi Czego\nobligatorem stawać oboiey pozwem albowiem przysięgnie.\n\nW sprawie z Uczciwym Janem Tkaczykiem Aktor dat...\nW sprawie wdowy Młodońcowej... w sprawie Sanka... W sprawie Józefa Mazały contra Pinchas... / 23v /",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    }
]

# Wczytujemy istniejące rekordy Partii 1 (1-25)
with open('/home/ubuntu/workspace/Gen/main_data_j17_part1.json', encoding='utf-8') as f:
    main_part1 = json.load(f)

# Łączymy rekordy 1-25 i 26-50
main_full_part2 = main_part1 + records_26_to_50

print(f"Łączna liczba rekordów po dodaniu Partii 2: {len(main_full_part2)}")

with open('/home/ubuntu/workspace/Gen/main_data_j17_part2.json', 'w', encoding='utf-8') as f:
    json.dump(main_full_part2, f, ensure_ascii=False, indent=2)

print("Zapisano pomyślnie main_data_j17_part2.json!")
