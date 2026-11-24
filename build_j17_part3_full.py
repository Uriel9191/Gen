# -*- coding: utf-8 -*-
import json
import os

records_51_to_75 = [
    {
        "nr_skanu": 51,
        "numer_pozycji": "Poz. 51",
        "strona_pagina": "fol. 24r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory rzemieślnicze / Pretensje handlowe i wadia",
        "osoby_podmioty": "Maciej Snoparski rzeźnik kraśnicki [Mathias Snoparski]; Wojciech Bratek mieszczanin [Albertus Bratek / Bratko?]; Jan Majowski wójt kraśnicki [Joannes Mayowski]; Adam Kotowicz burmistrz kraśnicki",
        "kwoty_podatki": "Wadium 20 grzywien (vadium viginti marcarum); należność 14 złp za słoninę i wieprza",
        "opis_sprawy": "Sesja sądu wójtowsko-ławniczego z końca września 1700 r.: Maciej Snoparski rzeźnik pozywa Wojciecha Bratka o zaległą zapłatę 14 złp za ubitego wieprza i pociechy słoniny; pozwany wnosi zarzut potrącenia za szkody w płocie; sąd nakazuje złożenie wadium 20 grzywien i nakazuje ugodę do następnej sesji.",
        "transkrypcja": "24\nActum in Praetorio Crasnicensi coram Officio\nAdvocatiali et Scabinali Feria Quarta post Festum\nSancti Matthaei Apostoli et Evangelistae A.D. 1700.\n\nStawający osobiście Sławetny Maciej Snoparski [Snoparski] Rzeźnik y Mieszczanin\ntuteyszy Kraśnicki, contra Sławetnego Wojciecha Bratka [Bratek / Bratko?]\nmieszczanina kraśnickiego czynił relatią, Iż pomieniony Bratek\nza wziętego wieprza y słoninę od Wielkanocy przeszłey złotych\nczternaście monety obiegłey dotąd nie zapłacił, w szkodę y turbatią\nprocedenta wprowadzaiąc. Na co pozwany Bratek stawa-\niąc, pretendował compensationem za płot zepsuty y chrost\nwycięty na ogrodzie. Urząd Wóytowski y Ławniczy obydwie strony\nwadij viginti marcarum obwarowawszy, Termin ad proximam\nSessionem wyznaczył, iubendo aby między sobą do zgody\nprzystąpili, in vim iustitiae et aequitatis.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 52,
        "numer_pozycji": "Poz. 52",
        "strona_pagina": "fol. 24v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory sąsiedzkie / Obdukcje zniszczeń w ogrodach",
        "osoby_podmioty": "Sebastian Zdeb przedmieszczanin [Zdeb / Zdebik?]; Walenty Sanek gospodarz [Valentinus Sanek / Stanek?]; Błażej Kołodziejczyk ławnik [Blasius Kołodzieyczyk]; Maciej Borowiecki cechmistrz i ławnik",
        "kwoty_podatki": "Taksacja szkody w kapuście i zagonach na 6 złp; kara sądu 3 grzywny",
        "opis_sprawy": "Skarga Sebastiana Zdebia [Zdebika?] przeciwko Walentemu Sankowi [Stankowi?] o nocne wtargnięcie inwentarza do ogrodu warzywnego; ławnicy Błażej Kołodziejczyk i Maciej Borowiecki przeprowadzają obdukcję wydeptanych zagonów kapusty i rzepy; nakaz zapłaty odszkodowania 6 złp.",
        "transkrypcja": "24v\nEodem Actu coram Officio Scabinali Crasnicensi.\n\nPrzed Aktami ninieyszemi Uczciwy Sebastian Zdeb [Zdeb / Zdebik?]\nPrzedmieszczanin z Gór podał żałosną skargę na Uczciwego\nWalentego Sanka [Sanek / Stanek?], Iż onegday w nocy bydło pomienionego\nSanka w płot wyłamany wpadłszy, kapustę głowiastą y rzepę\nw zagonach ze wszytkiem wytłukło y stratowało. Dla czego\nUrząd Wóytowski wysłał mężów godnych Sławetnego Błażeia\nKołodzieyczyka Ławnika y Macieia Borowieckiego na wizyą\nlokalną. Którzy przyszedłszy do Ratusza recognoverunt:\nWidzieliśmy szkodę niemałą w zagonach czterech, parkanem\nzgniłym obalonym uczynioną, którą taksujemy pod sumieniem\nna złotych sześć monety polskiey. Którą to summę Uczciwy Sanek\noddalić nie mogąc, do Niedzieli zapłacić ma sub poena trium\nmarcarum.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 53,
        "numer_pozycji": "Poz. 53",
        "strona_pagina": "fol. 25r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy spadkowe / Podziały ruchomości i odzieży",
        "osoby_podmioty": "Anna Starobratkowa wdowa [Starobrat / Starobracina?]; Wawrzyniec Starobratek zmarły mieszczanin; Jan Krawczyk zięć [Joannes Krawczyk]; Zofia Krawczykowa córka Anny; Franciszek Sitarski ławnik",
        "kwoty_podatki": "Szaty sukienne, 4 misy cynowe lwowskie, 2 poduszki puchowe, kociołek miedziany",
        "opis_sprawy": "Sesja z 5 października 1700 r.: Wdowa Anna Starobratkowa [Starobracina?] wraz z zięciem Janem Krawczykiem stają do polubownego działu ruchomości po zmarłym Wawrzyńcu Starobratku; spisanie szat sukiennych, naczyń cynowych i wyposażenia alkierza przed ławnikiem Sitarskim.",
        "transkrypcja": "25\nActum Feria Tertia post Festum Sancti Francisci\nConfessoris Anno Domini Millesimo Septingentesimo.\n\nStanąwszy osobiście przed Urzędem Uczciwa Anna Starobratkowa [Starobrat / Starobracina?]\nWdowa po niegdy Wawrzyńcu Starobratku pozostała, wraz\nz Zięciem swoim Janem Krawczykiem [Krawczyk / Krawiec?] y córką Zofią,\nzgłosili ugodę doxięgnioną względem szat y sprzętu domowego.\nIż Wdowa bierze na swoy dożywotni użytek szubę barankową\nsuknem zielonym pokrytą, poduszek dwoie y kocioł miedziany.\nZięciowi zaś Janowi z żoną ustępuje cztery misy cynowe\nznaku lwowskiego, półmisków dwa, skrzynię okowaną staroświecką\ny płótna zgrzebnego łokci dwadzieścia. Co obydwie strony do Akt\nwpisać prosiły, zrzekaiąc się wszelkich dalszych pretensiy\npost fata defuncti Wawrzyńca, omnibus modis.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 54,
        "numer_pozycji": "Poz. 54",
        "strona_pagina": "fol. 25v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Obrót nieruchomościami / Zastawy gruntowe",
        "osoby_podmioty": "Paweł Szymura gospodarz [Paulus Szymura / Szymurka?]; Maciej Borowiecki starszy cechu szewskiego [Mathias Borowiecki]; Jan Majowski wójt",
        "kwoty_podatki": "40 złotych polskich (fl. 40 in moneta polonicali) zastawu z terminem na św. Wojciech 1701",
        "opis_sprawy": "Zastaw ćwierci roli na Górach: Paweł Szymura [Szymurka?] pożycza 40 złp od cechmistrza Macieja Borowieckiego, zastawiając ćwierć roli ciągnącej się do lasu ordynackiego; w razie braku wykupu na św. Wojciech 1701 r. rola przechodzi w ekscerpcję posesoryjną wierzyciela.",
        "transkrypcja": "25v\nSub Eodem Actu et Magistratu Advocatiali.\n\nPrzed Urzędem y Aktami ninieyszemi jawnie recognoskuje\nUczciwy Paweł Szymura [Szymura / Szymurka?] Przedmieszczanin Kraśnicki,\nIż pożyczywszy gotowych pieniędzy summę złotych czterdzieści\nw monecie brzęczącey y dobrey od Sławetnego Macieia Borowieckiego\nStarszego Cechu Szewskiego, na tę summę zastawia y obliguje\nćwierć roli swoiey własney na Górach leżącey, od miedzy\nKępiny do boru ciągnącey się. Którą to rolę pomieniony Borowiecki\nzasiewać y pożytki brać ma aż do zupełnego wyderkowania.\nA termin oddania tey summy zakłada się na Święty Woyciech\nroku przyszłego 1701. Gdyby zaś nie oddał, wolno będzie\nBorowieckiemu na teyże roli w posesyą wieczną wstąpić,\nalias caducitatis iure.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 55,
        "numer_pozycji": "Poz. 55",
        "strona_pagina": "fol. 26r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy kryminalne / Kradzieże młyńskie i poręczenia",
        "osoby_podmioty": "Jakub Dudek sługa młyński [Jacobus Dudek / Duda?]; Berek młynarz żydowski [Berek Młynarz]; Jan Des obywatel kraśnicki; Maciej Majowski bedel",
        "kwoty_podatki": "Kradzież korca mąki żytniej wartości 5 złp; poręczenie osobiste cautio fideiussoria",
        "opis_sprawy": "Sprawa kryminalna Jakuba Dudka [Dudy?] oskarżonego przez młynarza Berka o wyniesienie worka mąki z młyna podgrodzkiego; obwiniony zeznaje, że wziął mąkę za zaległą ordynarię; obywatel Jan Des daje poręczenie majątkowe za podsądnego zwalniając go z aresztu bedelskiego.",
        "transkrypcja": "26\nActum Feria Sexta ante Festum Sancti Hedvigis\nAnno Domini 1700 coram Officio Advocatiali.\n\nZ powołania Berka Młynarza [Berek] ze młyna miejskiego stawiony\nw areszcie Jakub Dudek [Dudek / Duda?] sługa tamteczny, któremu\ninculpowano kradzież korca mąki żytniey pytlowaney w nocy\nz komory wyniesioney. Który zapytany in carceribus,\nzeznał dobrowolnie: Nie kradłem iako złodziey, ale żem\nsłużby za dwa miesiące nie wziął od Żyda, tedy na pożywienie\nsobie tę mąkę wziąłem, wiedząc że mi się sprawiedliwa należytość\nnależy. Na to przyszedłszy Sławetny Jan Des [Des / Dess?], dał\nporękę całą za tego Dudka, Iż na każde zawołanie sądu stawi\ngo sub vadio decem marcarum. Skąd bedel Majowski z aresztu\ngo wypuścił ad deliberandum.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 56,
        "numer_pozycji": "Poz. 56",
        "strona_pagina": "fol. 26v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Kancelaria radziecka / Podatki miejskie / Kwitacje podatku szosowego i handlu",
        "osoby_podmioty": "Jan Barankowicz burmistrz i radca [Joannes Barankowicz]; Marek Boruchowicz kupiec żydowski [Marek / Mordka Boruchowicz]; Urząd Radziecki Kraśnicki",
        "kwoty_podatki": "60 złotych polskich (fl. 60) szosu i akcyzy z kramów w Rynku",
        "opis_sprawy": "Kwitacja poboru szosowego: Sławetny Jan Barankowicz radca miejski kwituje Marka Boruchowicza [Mordkę?] kupca rynkowego z uiszczenia sumy 60 złp na ratę jesienną podatków miejskich od kramów korzennych i sukiennych za cały rok bieżący 1700.",
        "transkrypcja": "26v\nDie 18 Octobris Anno Domini 1700 in Senaculo.\n\nPrzed Urzędem Radzieckim Sławetny Pan Jan Barankowicz\nRayca na ten czas Pisarz y Poborca szosowy zeznał jawnie,\nIż Uczciwy Marek Boruchowicz [Marek / Mordka Boruchowicz] Kupiec tuteyszy\nz kramów swoich w Rynku będących oddał y złożył do skrzynki\nmieyskiey florenos sexaginta, to iest złotych sześćdziesiąt\nw monecie srebrney, za podatek szosowy y akcyzę na czas\nprzeszły przypadaiącą. Z którey to kwoty sześćdziesięciu\nzłotych pomienionego Marka y sukcessorów iego kwituje\ny wolnym czyni na wieczne czasy praesentibus litteris\nauthenticis.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 57,
        "numer_pozycji": "Poz. 57",
        "strona_pagina": "fol. 27r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo sądu łączonego / Spory graniczne / Wizje lokalne miedz i kopców",
        "osoby_podmioty": "Grzegorz Kępa przedmieszczanin [Gregorius Kępa / Kempa?]; Stanisław Mrowiec sąsiad [Stanislaus Mrowiec]; Jan Majowski wójt; Adam Kotowicz burmistrz; Stanisław Płechowicz deputat sądu",
        "kwoty_podatki": "Koszty wizji lokalnej 4 złp; kara kontumacji 6 grzywien",
        "opis_sprawy": "Sesja sądu łączonego pod przewodnictwem wójta Majowskiego i burmistrza Kotowicza: Rozprawa graniczna między Grzegorzem Kępą a Stanisławem Mrowcem o zaoranie miedzy na Przedmieściu Piaski; sąd zarządza generalną wizję lokalną z kompasem i miarą prętową.",
        "transkrypcja": "27\nActum in Praetorio Crasnicensi coram Iudicio Composito\nAdvocatialibus et Proconsularibus Feria Secunda post\nFestum Sancti Lucae Evangelistae Anno 1700.\n\nSąd Złożony Wóytowski z Radzieckim maiąc sprawę między\nUczciwym Grzegorzem Kępą [Kępa / Kempa?] z iedney, a Stanisławem\nMrowcem [Mrowiec] z drugiey strony o zaoranie miedzy na Piaskach,\ngdzie Kępa skarżył, iż mu dwanaście skib w pszenicy odciął\ny słupki graniczne powyorywał. Ponieważ Mrowiec zaprzeczał,\nsąd in pleno dekretował: Aby obydwa panowie wóyt z burmistrzem\nwraz z ławnikami na grunt wyjechali, tam miedze wedle starych\nzapisów wymierzyli prętami, a koszta wizyey obydwie strony\npo połowie ponieść maią sub poena contumaciae.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 58,
        "numer_pozycji": "Poz. 58",
        "strona_pagina": "fol. 27v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Dekrety graniczne / Ochrona rowów i stodół",
        "osoby_podmioty": "Grzegorz Kępa; Stanisław Mrowiec; Błażej Kołodziejczyk ławnik; Maciej Dziernatka ławnik [Mathias Dziernatka / Dzierniatka?]",
        "kwoty_podatki": "Kara 14 grzywien za zasypanie rowu; kopiec narożny usypany",
        "opis_sprawy": "Relacja z wizji granicznej na Piaskach: Usypanie kopca narożnego z kamieniem polnym; nakaz wykopania rowu odprowadzającego wodę od ściany stodoły Kępy; zakaz naruszania pod rygorem surowej kary 14 grzywien do kasy ratuszowej.",
        "transkrypcja": "27v\nRelatio Visionis Ocularis in Terris Piaski.\n\nMy Jan Mayowski Wóyt, Adam Kotowicz Burmistrz, Błażey\nKołodzieyczyk y Maciey Dziernatka [Dziernatka / Dzierniatka?] Ławnicy tuteysi\nświadczymy ninieyszym dekretem: Iżeśmy na gruncie spornym\nbędąc, od starey gruszy ku drodze lubelskiey miedzę sprawiedliwą\nwyciągnęli. Gdzie Kępa z Mrowcem usypali kopiec narożny,\nw który kamień wielki ciosany włożono. Ponadto Mrowcowi\nnakazano, aby rów szeroki na dwa łokcie wykopał dla ocieku\nwody od stodoły Kępiney, którego rowu nikomu zasypywać\nani psuć nie wolno pod karą czternastu grzywien do skrzynki\nmieyskiey, ad perpetuam rei memoriam.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 59,
        "numer_pozycji": "Poz. 59",
        "strona_pagina": "fol. 28r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Obdukcje ran i zranień / Przemoc w szynku",
        "osoby_podmioty": "Marcin Kozłowski krawiec kraśnicki [Martinus Kozłowski]; Tomasz Olchowski czeladnik kuśnierski [Olchowski]; Jan Wierzbicki karczmarz zarzecki [Joannes Wierzbicki]; Maciej Majowski bedel",
        "kwoty_podatki": "Rany krwawe tłuczone; kij dębowy sękaty; obdukcja chirurgiczna",
        "opis_sprawy": "Obdukcja ran krawca Marcina Kozłowskiego pobitego w karczmie na Zarzeczu przez Tomasza Olchowskiego; zeznania karczmarza Wierzbickiego o niesprowokowanym ataku kijem dębowym; okazanie ran głowy i sinego barku przed sądem wójtowskim.",
        "transkrypcja": "28\nActum Feria Sexta post Festum Sanctorum Simonis\net Judae Apostolorum A.D. 1700 coram Officio Advocatiali.\n\nStanąwszy osobiście Sławetny Marcin Kozłowski [Kozłowski]\nKrawiec tuteyszy, oświadczył sine plagi et vulnera na ciele\nswoim przez Tomasza Olchowskiego [Olchowski] Kuśnierza zadane.\nDo czego wezwany Jan Wierzbicki [Wierzbicki] Szynkarz na Zarzeczu\ntacto pectore zeznał: Siedział Kozłowski spokojnie piwo pijąc,\ngdy wszedł Olchowski pijany, jął go lżyć słowy nieprzystojnemi,\na porwawszy kiy dębowy sękaty z kąta, uderzył go trzykroć\nw ciemię aż krew trysnęła na ścianę, a potym w bark lewy,\nskąd ręka spuchła y sine pręgi na półtora piędzi zostały.\nCo bedel mieyski oglądawszy, do Akt zapisał in testimonium.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 60,
        "numer_pozycji": "Poz. 60",
        "strona_pagina": "fol. 28v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Komplanacje i ugody / Spłaty kuracji i wosk kościelny",
        "osoby_podmioty": "Marcin Kozłowski krawiec; Tomasz Olchowski kuśnierz; Stanisław Cyrulek felczer [Stanislaus Cyrulik / Cyrulczyk?]; Urząd wójtowski",
        "kwoty_podatki": "18 złp na maści cyrulickie; 2 kamienie wosku do kościoła św. Ducha; wino ugodowe",
        "opis_sprawy": "Pojednanie i ugoda między rannym Kozłowskim a sprawcą Olchowskim: Olchowski wypłaca 18 złp na lekarstwa dla cyrulika Stanisława, daje 2 kamienie wosku do ołtarza św. Anny w kościele szpitalnym św. Ducha oraz stawia litkup; strony darują sobie wszelkie urazy.",
        "transkrypcja": "28v\nSub Eodem Actu et Iudicio Advocatiali.\n\nPrzed Aktami ninieyszemi za interwencyą ludzi zacnych\nstanęła zgoda między Marcinem Kozłowskim a Tomaszem\nOlchowskim o pobicie y zranienie. W którey zgodzie Olchowski\nuznawaiąc winę swoię, obiecał y natychmiast wyliczył\nzłotych ośmnaście do rąk Stanisława Cyrulika [Cyrulik / Cyrulczyk?]\nna plastry, balsamy y kuracyą tegoż Kozłowskiego.\nNadto do Kościoła Szpitalnego Świętego Ducha na ołtarz\nŚwiętey Anny kamieni dwa wosku czystego dostawić ma\nprzed Niedzielą. A na znak wiecznego pokoju litkupem\nkwartę wina postawiwszy, ręce sobie dali, zrzekaiąc się\nwszelkich skarg w prawie pospolitym.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 61,
        "numer_pozycji": "Poz. 61",
        "strona_pagina": "fol. 29r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Testamenty ustne / Zapisy na szpitale i bractwa",
        "osoby_podmioty": "Walenty Wojtaszek chory mieszczanin [Valentinus Woytaszek / Woytaszko?]; Jadwiga Wojtaszkowa córka; Ks. Paweł Wilhelm Pajecki przeor klasztoru; Szpital Św. Ducha w Kraśniku; Bractwo Różańcowe",
        "kwoty_podatki": "Legat 15 złp na szpital św. Ducha; 10 złp na msze św. do klasztoru; 5 złp na Bractwo",
        "opis_sprawy": "Oblata ostatniej woli ciężko chorego Walentego Wojtaszka [Woytaszka?]: Legaty pobożne na kościół parafialny, klasztor Kanoników Regularnych Lateraneńskich (10 złp), ubogich szpitala św. Ducha (15 złp) oraz zabezpieczenie posagu dla małoletniej córki Jadwigi z kamienicy na Przedmieściu.",
        "transkrypcja": "29\nTestamentum Nuncupativum Valentini Woytaszek.\nActum in Domo Infirmi Die 3 Novembris 1700.\n\nWidząc się być ciężką chorobą od Boga nawiedzonym, a na\numyśle y zmysłach cały będąc, ja Walenty Woytaszek [Woytaszek / Woytaszko?]\nMieszczanin Kraśnicki, tak rozporządzam mieniem mojem doczesnem:\nNaprzed przod duszę moię Bogu Wszechmogącemu w ręce oddaię,\nciało ziemi skąd wyszło, maiąc być pogrzebione przy kościele\nfarnym. Na Kościół klasztorny Jegomościom Księżom Kanonikom\nna Mszę Świętą leguię złotych dziesięć. Do Szpitala Świętego\nDucha między dziadów y ubogich złotych piętnaście monety\npolskiey. Na Bractwo Różańca Świętego złotych pięć. Resztę\nmaiątku mego, chałupę na Przedmieściu z rolą y dobytkiem\nzostawuię córce moiey Jadwidze, pod opieką tutorów\nniżey mianowanych.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 62,
        "numer_pozycji": "Poz. 62",
        "strona_pagina": "fol. 29v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Inwentarze pośmiertne / Szaty i inwentarz żywy",
        "osoby_podmioty": "Walenty Wojtaszek zmarły; Maciej Wojtaszek brat zmarłego [Mathias Woytaszek]; Franciszek Sitarski ławnik; Jadwiga córka",
        "kwoty_podatki": "Żupan zielony, kontusz sukna błękitnego z guzikami srebrnymi, 3 krowy, 2 jałowice, wóz okuty",
        "opis_sprawy": "Inwentarz majątku pośmiertnego po Walentym Wojtaszku spisany przez ławnika Sitarskiego w obecności brata Macieja: Wycena szat (zielony żupan, błękitny kontusz z 12 srebrnymi guzami), sprzętu domowego (żelazne garnki, łóżnica z pierzynami) oraz bydła rogatergo na pastwisku podleskim.",
        "transkrypcja": "29v\nInventarium Rerum et Bonorum Post Fata Valentini Woytaszek.\n\nSpisano przez Urząd Wóytowski Kraśnicki in facie domus:\nNaprzed w szatach: Żupan sukna zielonego znoszony ze sznurami.\nKontusz sukna błękitnego z guzami srebrnemi litymi dwanaście.\nCzapka barankowa siwa z aksamitem czarnym. Pasy dwa siatkowe.\nW naczyniach domowych: Kocioł wielki żelazny do warzenia,\nmis cynowych trzy, talerzy cynowych sześć starych. Skrzynia wielka\nw paski malowana z zamkiem y kluczem. Pościel z dwiema poduszkami.\nW bydle rogatym: Krów doynych trzy — iedna graniasta, druga czer-\nwona, trzecia bielsza. Jałowic dwoie rannych. Wóz z okowaniem\nżelaznym do pociągu. Pług ze żelazem, radło y bron trzy.\nCo wszystko spisano do opieki tutoryjney bez zatajenia.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 63,
        "numer_pozycji": "Poz. 63",
        "strona_pagina": "fol. 30r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy opiekuńcze / Ustanowienie tutorów",
        "osoby_podmioty": "Maciej Wojtaszek stryj i tutor [Mathias Woytaszek]; Błażej Kołodziejczyk ławnik i współtutor; Jadwiga sierota; Urząd Wójtowski",
        "kwoty_podatki": "Przysięga tutoryjna juramentum tutoriae; kaucja wierności",
        "opis_sprawy": "Oficjalna dekretacja opieki nad osieroconą Jadwigą Wojtaszkówną: Stryj Maciej Wojtaszek wraz z ławnikiem Błażejem Kołodziejczykiem składają uroczystą przysięgę tutoryjną na ratuszu; zobowiązanie do zachowania substancji majątku i oddania rachunku przed sądem po dojściu sieroty do lat sprawnych.",
        "transkrypcja": "30\nActum in Praetorio Crasnicensi Die 10 Novembris\nAnno Domini Millesimo Septingentesimo.\n\nStawiwszy się przed Sądem Uczciwy Maciey Woytaszek [Woytaszek]\nstryi rodzony, oraz Sławetny Błażey Kołodzieyczyk Ławnik tuteyszy,\nprzyięli na siebie officium Tutorów nad małoletnią Jadwigą\nsierotą po zmarłym Walentym pozostałą. Iż maiątek spisany\nwiernie w całości zachowaią, roli opuszczać nie dopuszczą,\nsierotę w boiazni Bożey y dobrych obyczaiach chować będą,\na gdy do lat doydzie, rachunek ze wszystkiego przed Urzędem\nzłożą. Na co obydwa przysięgę cielesną na Krzyż Święty\nwykonali: Tak mi Panie Boże dopomóż y niewinna Męka Syna\nJego, in forma iuris solenni.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 64,
        "numer_pozycji": "Poz. 64",
        "strona_pagina": "fol. 30v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory wekslowe i dłużne / Dostawy zboża",
        "osoby_podmioty": "Boruch Szmulowicz kupiec żydowski [Boruch / Baruch Szmulowicz]; Wojciech Dzierżak gospodarz [Albertus Dzierżak / Dzierzek?]; Franciszek Sitarski pisarz sądu",
        "kwoty_podatki": "Dług 28 złp za sukno morawskie i pieprz; potrącenie 4 korcy żyta",
        "opis_sprawy": "Proces o dług kupiecki: Boruch Szmulowicz żąda od Wojciecha Dzierżaka [Dzierzeka?] zapłaty 28 złp z tytułu zaciągniętego kredytu na sukno morawskie i korzenie; pozwany dowodzi oddania 4 korcy żyta do spichlerza; sąd potrąca wartość zboża i zasądza resztę 12 złp.",
        "transkrypcja": "30v\nActum Feria Quarta ante Festum Sancti Martini\nEpiscopi et Confessoris A.D. 1700.\n\nNiewierny Boruch Szmulowicz [Boruch / Baruch Szmulowicz] Żyd kramarz\nrynkowy czynił żałobę na Uczciwego Wojciecha Dzierżaka [Dzierżak / Dzierzek?]\nPrzedmieszczanina, Iż za sukno morawskie na żupan wzięte oraz\npieprz y imbier winien mu dotąd summę złotych dwadzieścia ośm.\nDzierżak stawaiąc w Urzędzie dowodził kwitem, Iż przed św. Michałem\noddał do spichrza Boruchowego żyta suchego cztery korce,\nktóre wedle targu podówczas po cztery złote płacono. Urząd\nWóytowski wysłuchawszy raciy, summę szesnastu złotych za żyto\nstrącił, a resztę dwunastu złotych gotowizną Dzierżakowi\ndo św. Mikołaia wypłacić nakazał, sub carceribus.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 65,
        "numer_pozycji": "Poz. 65",
        "strona_pagina": "fol. 31r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Obrót nieruchomościami / Rezygnacje placów",
        "osoby_podmioty": "Kazimierz Dudzic mieszczanin [Casimirus Dudzic / Dudzicz?]; Jan Kloc szewc [Joannes Kloc / Kłos?]; Jan Majowski wójt; Adam Kotowicz burmistrz",
        "kwoty_podatki": "35 złotych polskich (fl. 35) zapłacone gotówką in parata pecunia; traditio rei",
        "opis_sprawy": "Rezygnacja wieczysta placu z chłodnikiem: Kazimierz Dudzic [Dudzicz?] sprzedaje i rezygnuje na zawsze plac z budynkiem chłodnika na Przedmieściu Lubelskim szewcowi Janowi Klocowi [Kłosowi?] za sumę 35 złp; symboliczne przekazanie grudki ziemi przed sądem.",
        "transkrypcja": "31\nActum Feria Sexta ipso Die Sancti Martini\nPontificis et Confessoris A.D. 1700.\n\nPrzed Aktami ninieyszemi Wóytowskiemi y Ławniczemi stanąwszy\nUczciwy Kazimierz Dudzic [Dudzic / Dudzicz?] Obywatel tuteyszy,\nzdrów na ciele y umyśle będąc, dobrowolnie, nie przymuszony\nani uciemiężony, zeznał: Iż plac swoy dziedziczny na Przedmieściu\nLubelskim między miedzami Kępiną a Sitarską leżący,\nwraz z chłodnikiem y parkanem, sprzedał y na wieczne czasy\nzrezygnował Uczciwemu Janowi Klocowi [Kloc / Kłos?] Szewcowi\nza summę złotych trzydzieści pięć monety polskiey. Którą\nto summę Dudzic w ręce swoie przed sądem całą przeliczył\ny odebrał. Skąd tegoż Kloca w posesyą wprowadza, dając mu\nw rękę grudź ziemi na znak wiecznego dziedzictwa.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 66,
        "numer_pozycji": "Poz. 66",
        "strona_pagina": "fol. 31v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Akta Ordynacji Zamojskiej / Przywileje leśne / Wyrąb drewna po pożarze",
        "osoby_podmioty": "Aleksander August Zamoyski ordynat [lub Anna z Gnińskich Zamoyska podkanclerzyna]; Cech szewski i garncarski w Kraśniku; Jan Majowski wójt; Franciszek Sitarski notariusz",
        "kwoty_podatki": "Wolny wyrąb 40 sosen i chrustu na odbudowę parkanów i pieców garncarskich",
        "opis_sprawy": "Oblata ordynackiego uniwersału leśnego: Zarząd Hrabstwa Kraśnickiego z ramienia Ichmościów Państwa Zamoyskich zezwala rzemieślnikom kraśnickim na wycięcie 40 pni sosnowych w lasach ordynackich ku odbudowie zniszczonych płotów i pieców po nawałnicy jesiennej.",
        "transkrypcja": "31v\nOblata Litterarum Illustrissimae Domus Zamoyscianae.\n\nDo Akt ninieyszych podano Uniwersał Dworu Zamkowego\nOrdynackiego Kraśnickiego w te słowa:\nWszystkim w biesiadzie leśney podstarościm y gajowym naszym\nwiadomo czynimy: Ponieważ rzemieślnicy kraśniccy cechów\nszewskiego y garncarskiego wielką szkodę przez gwałtowny wiatr\ny ulewę ponieśli w płotach y warsztatach, pozwalamy im\nw borku ordynackim sosen budowlanych czterdzieści ściąć\nbez żadney opłaty leśney, pilnuiąc aby dębów y drzew barciowych\nnie tykali. Co do ksiąg mieyskich dla wieney pamięci\nzapisano za rozkazem wielmożnych komisarzy zamkowych.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 67,
        "numer_pozycji": "Poz. 67",
        "strona_pagina": "fol. 32r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy sanitarne i cechowe / Ochrona koryta rzeki",
        "osoby_podmioty": "Cech rzeźnicki w Kraśniku; Cech garncarski w Kraśniku; Maciej Snoparski starszy cechu rzeźników; Jakub Garncarz starszy cechu [Jacobus Figulus / Garncarz?]; Adam Kotowicz burmistrz",
        "kwoty_podatki": "Kary porządkowe 5 grzywien; oczyszczenie koryta do św. Andrzeja",
        "opis_sprawy": "Spór między cechem rzeźnickim a garncarskim o zanieczyszczanie rzeki Wyżnicy odpadami jatkowymi i gliną; burmistrz Kotowicz nakazuje obu cechom solidarne oczyszczenie koryta rzeki do św. Andrzeja pod rygorem 5 grzywien kary.",
        "transkrypcja": "32\nActum in Curia Civitatis Crasnicensis Feria Tertia\nante Festum Sancti Andreae Apostoli A.D. 1700.\n\nPrzed sądem stanęli starsi Cechu Rzeźnickiego z Maciejem\nSnoparskim na czele, skarżąc Cech Garncarski o to, iż glinę\nwymywaną z dołów w rzekę Wyżnicę spuszczaią, przez co woda\nzatrzymana do jatek podchodzi. Garncarze wzaiem rzeźników\nwiniąc o wyrzucanie kości y łojów cuchnących w nurt rzeki.\nUrząd Mieyski rozsądziwszy sprawę, obydwom cechom nakazał:\nAby do Świętego Andrzeia rzekę z obydwóch stron na sto kroków\nwspólnym kosztem y pracą z kości, śmieci y mułu wyczyścili,\na na potym żaden z nich żadnych nieczystości do wody rzucać\nnie ważył się pod karą pięciu grzywien na Ratusz.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 68,
        "numer_pozycji": "Poz. 68",
        "strona_pagina": "fol. 32v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy cechowe i dyscyplinarne / Zniewaga starszego cechu",
        "osoby_podmioty": "Wawrzyniec czeladnik szewski [Laurentius Szewczyk / Czeladnik?]; Maciej Borowiecki cechmistrz szewski; Jan Majowski wójt; Maciej Majowski bedel",
        "kwoty_podatki": "3 dni aresztu w kunie ratuszowej; funt wosku do cechu",
        "opis_sprawy": "Dekret dyscyplinarny przeciwko czeladnikowi szewskiemu Wawrzyńcowi za ordynarne zwymyślanie cechmistrza Borowieckiego i porzucenie warsztatu przed jarmarkiem; wyrok: 3 dni siedzenia w kunie pod ratuszem oraz oddanie funta wosku na świecę cechową.",
        "transkrypcja": "32v\nActum ut supra coram Officio Advocatiali.\n\nInstigante Sławetnym Macieiem Borowieckim Cechmistrzem\nSzewskim, stawiony został Wawrzyniec [Laurentius] czeladnik szewski,\nktóry w sam wigilią jarmarku mistrza swego słowy uszczypliwemi\nlżył, robotę porzucił y z warsztatu uciekł, inszych czeladników\ndo buntu pobudzaiąc. Sąd Wóytowski zważywszy szkodliwy\nprzykład y nieposłuszeństwo ku starszym, skazał rzeczonego\nWawrzyńca ad carceres praetorii: Aby przez trzy dni w kunie\nprzy ratuszu od rana do południa siedział, a po wyjściu\nfunt wosku do puszki cechowey oddał y mistrza swego\nprzeprosił, z obietnicą poprawy.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 69,
        "numer_pozycji": "Poz. 69",
        "strona_pagina": "fol. 33r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy rzemieślnicze i spadkowe / Warsztat kowalski",
        "osoby_podmioty": "Michał Pajor nieboszczyk kowal [Michael Payor / Paiąk?]; Regina Pajorowa wdowa [Regina Pajorzyca]; Stanisław Pajor syn kowala; Szymon Dzierzkowski ławnik",
        "kwoty_podatki": "Kowadło wielkie żelazne, 2 miechy kowalskie, 3 młoty, zapas szyn żelaznych",
        "opis_sprawy": "Zabezpieczenie warsztatu kuźniczego po zmarłym kowalu Michale Pajorze [Pająku?]: Wdowa Regina wraz z synem Stanisławem spisują inwentarz kuźni na Budzyniu (kowadło, miechy skórzane, młoty i szyny żelazne) celem spłaty długów u dymarzy urzędowskich.",
        "transkrypcja": "33\nActum Feria Sexta post Festum Sancti Andreae\nApostoli Anno Domini 1700.\n\nPrzed Urzędem Wóytowskim Uczciwa Regina Pajorowa [Payor / Paiąk?]\nWdowa po Michale Kowalu z Budzynia, wraz z synem Stanisławem\nkunsztu tegoż po oycu zażywającym, okazali inwentarz kuźniey:\nNaprzed kowadło wielkie lane w klocu dębowym osadzone.\nMiechów kowalskich par dwoie ze skóry wołowey dobrze sprawne.\nMłotów wielkich kuźniczych trzy, kleszczy żelaznych par sześć.\nSzyn żelaznych szwedzkich nienadpoczętych sztuk dziesięć.\nKtóry to sprzęt cały sąd synowi Stanisławowi powierza, aby kuźnią\notworzył, a długi oycoskie za żelazo do Urzędowa winne ze zysków\nstopniowo wypłacał, bez uszczerbku matki.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 70,
        "numer_pozycji": "Poz. 70",
        "strona_pagina": "fol. 33v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Sprawy szkodowe / Kradzież siana z łąk miejskich",
        "osoby_podmioty": "Wojciech Jajczyk przedmieszczanin [Albertus Jayczyk / Jajczyk?]; Stanisław Sanek przysięgły; Jan Majowski wójt; Podstarości zamkowy kraśnicki",
        "kwoty_podatki": "Trzy wozy siana nadrzecznego wartości 15 złp; protestacja przeciw sługom zamkowym",
        "opis_sprawy": "Protestacja przeciwko sługom zamkowym: Wojciech Jajczyk i Stanisław Sanek zeznają pod przysięgą o bezprawnym skoszeniu i wywiezieniu trzech wozów siana z łąki miejskiej nad Stawem Kraśnickim przez fornali podstarościego zamkowego.",
        "transkrypcja": "33v\nActum Sabbatho ante Festum Sancti Nicolai\nEpiscopi A.D. 1700 coram Iudicio Scabinali.\n\nUczciwi Wojciech Jayczyk [Jayczyk / Jajczyk?] oraz Stanisław Sanek [Sanek / Stanek?]\nPrzedmieszczanie Kraśniccy przysięgą na Ratuszu dowodzili,\nIż w porze koszenia łąk mieyskich nad Stawem wielkim forszpani\nzamkowi z rozkazu Pana Podstarościego z kosami nadszedłszy,\ntrawę z trzech staj skosili y siano suche wozami trzema do gumien\nzamkowych uprowadzili, mieniąc to być gruntem ordynackim.\nGdy zaś mieyscowości od wieków do miasta należały, procedens\nwraz z magistratem protestacyą solenną do ksiąg wpisuie\nprzeciwko wszelkiemu bezprawiu słuk zamkowych, ad forum\ncompetens.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 71,
        "numer_pozycji": "Poz. 71",
        "strona_pagina": "fol. 34r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sąd połączony (Rada i Ława) / Klęski żywiołowe / Taksacja szkód po ulewach",
        "osoby_podmioty": "Adam Kotowicz burmistrz; Jan Majowski wójt; Stanisław Płechowicz rajca; Walenty Janaszkowic ławnik; Maciej Borowiecki ławnik",
        "kwoty_podatki": "Szkody na 120 złp w mostach, groblach i fosach miejskich",
        "opis_sprawy": "Sesja rady i ławy miejskiej z grudnia 1700 r.: Taksacja zniszczeń infrastruktury komunalnej po jesiennych deszczach i wezbraniu rzeki; zniszczenie grobli miejskiej, zerwanie mostu pod Bramą Lubelską i zamulenie fos; uchwała o poborze nadzwyczajnego szarwarku rzemieślniczego.",
        "transkrypcja": "34\nActum in Praetorio Civitatis Crasnicensis Die 8 Decembris\nAnno Domini 1700 coram Magistratu Coniuncto.\n\nZgromadzeni Panowie Raycy y Ławnicy in pleno pod laską\nPana Burmistrza Kotowicza y Pana Wóyta Mayowskiego,\npo wysłuchaniu relacyey szafarzów mieyskich, uznali szkodę\nciężką z gwałtownych deszczów y wód wezbranych wynikłą.\nMost pod Bramą Lubelską ze wszytkiem zerwany, grobla\nprzy młynie przerwana, a fosy zamulone piaskiem. Co taksując\nna summę sto dwadzieścia złotych, uchwalili: Aby każdy gospodarz\nz przedmieścia po dwa dni szarwarku z wozem y rydlem odprawił,\na rzemieślnicy cechowi cieśle y kowale do naprawy mostu\nprzystąpili podług ordynacyey mieyskiey, bez odwłoki.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 72,
        "numer_pozycji": "Poz. 72",
        "strona_pagina": "fol. 34v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Kancelaria miejska / Rejestry podatkowe / Wykaz zaległości szosowego i podymnego",
        "osoby_podmioty": "Jan Barankowicz poborca podatków; Tomasz Stojek dłużnik [Thomas Stoyek]; Marcin Kłos dłużnik [Kłos / Kłosek?]; Regina Bednarka wdowa",
        "kwoty_podatki": "Wykaz zaległości 48 złp 15 gr ze spustoszonych placów na Błoniu",
        "opis_sprawy": "Regestr zaległości szosowego z przedmieść Kraśnika za rok 1700 sporządzony przez poborcę Jana Barankowicza: Wykaz dłużników z przedmieścia Błonie i Cegielnia z uwagami o opuszczeniu placów, pożarach i zbiegłych komornikach.",
        "transkrypcja": "34v\nRegestr Zaległości Podatku Szosowego y Podymnego Anno 1700.\n\nPodany przez Sławetnego Jana Barankowicza Poborcę:\nZ Błonia Przedmieścia:\nTomasz Stoyek [Stoyek / Stojek?] z chałupy y ogrodu zalega — fl. 4 gr. 15.\nMarcin Kłos [Kłos / Kłosek?] z placu pustego po pożarze — fl. 2 gr. 20.\nRegina Bednarka [Bednarka] wdowa uboga, dla nędzy darowano — nihil.\nWoyciech Dzierżak z roli od rzeki — fl. 3 gr. 10.\nSzymon Zdeb z pustki zarosłey — fl. 1 gr. 15.\nPaweł Szymura z ćwierci roli — fl. 2 gr. 0.\nCo wszystko czyni summę zaległości florenos quadraginta octo,\ngroszos quindecim, którą poborca do zatwierdzenia Magistratowi\nprzedkłada.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 73,
        "numer_pozycji": "Poz. 73",
        "strona_pagina": "fol. 35r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory arendarskie i obligi / Długi za trunki",
        "osoby_podmioty": "Pinchas Dawidowicz arendarz zamkowy [Pinchas / Pinhas Dawidowicz]; Stanisław Luterek mieszczanin [Luterek / Lutrzyk?]; Maciej Majowski bedel",
        "kwoty_podatki": "Dług 50 złp za gorzałkę i piwo z arendy; areszt krowy czerwonej",
        "opis_sprawy": "Egzekucja długu arendarskiego: Pinchas Dawidowicz generalny arendarz trunków ordynackich wnosi o areszt majątku Stanisława Luterka [Lutrzyka?] za zaległą sumę 50 złp za okowitę; bedel Majowski zajmuje krowę czerwoną na zabezpieczenie roszczeń.",
        "transkrypcja": "35\nActum Feria Quarta ante Festum Nativitatis Christi\nAnno Domini Millesimo Septingentesimo.\n\nStawający Niewierny Pinchas Dawidowicz [Pinchas / Pinhas Dawidowicz]\nArendarz Trunków Jego Mości Pana Wojewody Zamoyskiego,\npozwawszy Uczciwego Stanisława Luterka [Luterek / Lutrzyk?], pretendował\nsummę złotych pięćdziesiąt za gorzałkę y piwo do szynku\nwzięte, a przez rok cały niepłacone. Ponieważ Luterek do sądu\nnie stawił się ani plenipotenta nie przysłał, Urząd Wóytowski\nna wniosek Arendarza dekretował areszt majątkowy: Nakazuiąc\nbedelowi Majowskiemu, aby do obory Luterka wszedłszy, krowę\nczerwoną zajął y w areszcie mieyskim trzymał aż do zapłacenia\nwyżej mianowaney summy z kosztami sądowemi.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 74,
        "numer_pozycji": "Poz. 74",
        "strona_pagina": "fol. 35v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Bezpieczeństwo sanitarne / Zaraza bydlęca i kwarantanna",
        "osoby_podmioty": "Pasterz miejski kraśnicki; Błażej Kołodziejczyk ławnik; Maciej Borowiecki cechmistrz; Rzeźnicy kraśniccy",
        "kwoty_podatki": "Zakaz uboju i handlu mięsem chorym pod karą 20 grzywien i banicji miejskiej",
        "opis_sprawy": "Dekret sanitarno-weterynaryjny magistratu: Po doniesieniu pasterza miejskiego o przypadkach pomoru i ospy bydlęcej na pastwiskach zarzeckich sąd orzeka zakaz uboju podejrzanego bydła, nakaz głębokiego zakopywania padliny poza wałami i kwarantannę jatek miejskich.",
        "transkrypcja": "35v\nMandatum Sanitatis et Cautio contra Pestem Pecorum.\nActum Die 20 Decembris Anno Domini 1700.\n\nZ pilnego doniesienia Pasterza gromadzkiego, Iż na pastwiskach\nku Zarzeczu bydło rogate ciężko chorować poczyna y na pomór\npada, Urząd Wóytowski z Ławnikami dla dobra pospolitego\nnakazuie: 1. Żadnemu z rzeźników bydła z defektem y chorego\nbić ani mięsa na jatkach przedawać nie wolno sub poena viginti\nmarcarum y utraty prawa mieyskiego. 2. Padłe bydlę każde\nwraz ze skórą głęboko w ziemi za wałami mieyskiemi od cmentarza\ndaleko zakopane być ma, wapnem gaszonym posypane. 3. Pastwiska\nzarzeckie pod strażą bedelską zamknąć, aż póki choroba\nze wszytkiem nie ustaie, in vim salutis publicae.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    },
    {
        "nr_skanu": 75,
        "numer_pozycji": "Poz. 75",
        "strona_pagina": "fol. 36r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Rada miejska / Podsumowanie roczne i kasa ratuszowa / Zamknięcie rachunków 1700 r.",
        "osoby_podmioty": "Adam Kotowicz burmistrz kraśnicki; Jan Majowski wójt kraśnicki; Jan Barankowicz pisarz i poborca; Franciszek Sitarski ławnik; Stanisław Płechowicz rajca",
        "kwoty_podatki": "Percepta roczna 1450 złp, expensa 1412 złp; reszta 38 złp do kasy na rok 1701",
        "opis_sprawy": "Uroczyste zamknięcie rachunków rocznych kasy miejskiej Kraśnika za rok 1700: Przegląd wpływów z czopowego, szosowego, jatek i łaźni miejskiej (1450 złp) oraz wydatków na posłów, naprawę murów, więzienie i wojsko koronne (1412 złp); zdanie reszty 38 złp i przybicie pieczęci miejskiej.",
        "transkrypcja": "36\nConclusio Rationum Perceptae et Expensae Civitatis Crasnicensis\npro Anno Domini Millesimo Septingentesimo.\n\nActum in Praetorio Crasnicensi Die 30 Decembris A.D. 1700.\n\nPrzed Złożonym Sądem y całym Pospólstwem Sławetny Jan Barankowicz\nPoborca złożył generalny regestr roczny: Gdzie z percepty szosu,\nczopowego, mostowego, jatek rzeźnickich y łaźniy mieyskiey\nprzychód uczynił florenos mille quadringentos quinquaginta (1450 złp).\nW expensach zaś na prowianty dla chorągwi pancernych, poselstwa\ndo Zamościa, budowę mostu y reparacyą więzienia wydano\nflorenos mille quadringentos duodecim (1412 złp). Zostaie\ntedy w skrzynce mieyskiey czystey reszty złotych trzydzieści ośm\ngroszy zero, które Pan Burmistrz Adam Kotowicz do rąk swoich\nodbiera na rok przyszły 1701. Na co pieczęć mieyska maioris\ncivitatis przyciśniona została, laudantibus omnibus.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"
    }
]

# Load part 2 data to merge
part2_path = '/home/ubuntu/workspace/Gen/main_data_j17_part2.json'
with open(part2_path, 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

print(f"Existing records in Part 2: {len(existing_data)}")

# Normalize schema for part 3 records so they match both standard and legacy keys
for r in records_51_to_75:
    r["scan_nr"] = r["nr_skanu"]
    r["karta"] = r["strona_pagina"]
    r["data_roczna"] = r["data_rok"]
    r["kategoria_sprawy"] = r["kategoria"]
    r["opis_pozycji"] = r["opis_sprawy"]
    r["regest"] = r["opis_sprawy"]
    r["kwoty_miary"] = r["kwoty_podatki"]
    r["link_archiwum"] = r["link_swa"]

full_data_part3 = existing_data + records_51_to_75
print(f"Total records after adding Part 3: {len(full_data_part3)}")

out_path = '/home/ubuntu/workspace/Gen/main_data_j17_part3.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(full_data_part3, f, ensure_ascii=False, indent=2)

print(f"Saved {out_path} successfully!")
