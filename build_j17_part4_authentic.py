# -*- coding: utf-8 -*-
import json
import os

with open('/home/ubuntu/workspace/Gen/main_data_j17_part3.json', 'r', encoding='utf-8') as f:
    part3_data = json.load(f)

part4_scans = [
    {
        "nr_skanu": 76,
        "numer_pozycji": "Poz. 76",
        "strona_pagina": "fol. 36r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory rodzinne i areszty / Puklina v. Oczapka",
        "osoby_podmioty": "Krystyna Puklina wdowa [Puklina / Pukiel?]; Tomasz Oczapka zięć [Oczapka / Oczapko?]; Herszek Żyd [Herszek]; Berek Pielaszkowic [Pielaszkowic / Pielaszkiewicz?]; Wawrzyniec [Laurenty] Trafica [Trafica / Stafica?]; Piotr Tokarski [Tokarski]; Jan Majowski wójt [Majowski]; Adam Kotowicz burmistrz [Kotowicz]",
        "kwoty_podatki": "Pozew o wypędzenie z domu i przywłaszczenie ruchomości; kaucja i areszt",
        "opis_sprawy": "Sprawa wdowy Krystyny Pukliny przeciwko zięciowi Tomaszowi Oczapce o srogie pobicie, znęcanie się i wygnanie z własnego domu oraz zabór majątku. Pozwany zobowiązany do stawiennictwa pod rygorem aresztu. Wskazanie świadków mieszczan i Żydów.",
        "transkrypcja": "Actum in Praetorio Crasniciensi feria Quarta post Dominicam Invocavit proxima Anno Domini 1700.\nDo Urzędu y Akt ninieyszych Wóytowskich y Ławniczych Kraśnickich przyszedszy Ućciwa Krystyna Puklina wdowa, solenną zaniosła skargę na Tomasza Oczapkę zięcia swego, iż ten zapomniawszy boiaźni Bożey y powinności powinowactwa, na nię bezbronną matkę ręce świętokradzkie ściągał, bił, morzył, chleb odeymował y z domu oycystego precz wygnał. Upraszała Urzędu o ratunek y obronę. Urząd widząc opresyą wdowy, Oczapkę pod aresztem mieyskim zatrzymać nakazał, aż złoży poręczenie sąsiedzkie, iż się w pokoiu zachowa y przed sądem do rachunku ze schedy stanie. W teyże mierze wkazywał się Herszek Żyd [Herszek?] arendarz, Berek Pielaszkowic [lub Pielaszkiewicz?], Laurenty Trafica [lub Stafica?] kowal oraz Piotr Tokarski [Tokarski?], dając świadectwo o gwałtownym postępku Oczapki. Termin do roków zawitych odłożono.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2074461"
    },
    {
        "nr_skanu": 77,
        "numer_pozycji": "Poz. 77",
        "strona_pagina": "fol. 36v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Poręczenia i spory majątkowe / Mrokowski malarz",
        "osoby_podmioty": "Paweł Kłopot [Kłopot]; Kazimierz Matyjaszczyk [Matyjaszczyk / Matyjaszek?]; Jan Pielaszkowic [Pielaszkowic]; Adam Zdeb [Zdeb]; Tomasz Oczapka [Oczapka]; Pinchas Dawidowicz arendarz żydowski [Dawidowicz]; Józef Auckenfelth [Auckenfelth / Augsfeld?]; Wojciech Kłopot [Kłopot]; Adam Karol Mrokowski malarz [Mrokowski]",
        "kwoty_podatki": "Poręczenie sąsiedzkie 200 złp; spór o wieprzka i rysunki artystyczne malarza",
        "opis_sprawy": "Złożenie urzędowego poręczenia sąsiedzkiego za Tomasza Oczapkę przez Pawła Kłopota, Kazimierza Matyjaszczyka, Jana Pielaszkowica i Adama Zdeba. Następnie sprawa arendarza Pinchasa Dawidowicza z relacją Józefa Auckenfeltha. Spór Wojciecha Kłopota z malarzem Adamem Karolem Mrokowskim o zbiegłego wieprzka karmnego.",
        "transkrypcja": "Actum ut supra coram Officio Advocatiali Crasniciensi.\nStanąwszy oblicznie Ućciwi Paweł Kłopot, Kazimierz Matyjaszczyk [Matyjaszek?], Jan Pielaszkowic y Adam Zdeb [Zdeb?], obywatele kraśniccy, solenniter poręczyli za Tomasza Oczapkę pod zakładem dwustu złotych polskich [200 złp], iż tenże Oczapka teściowey swey Puklinie żadney krzywdy ani przykrości czynić nie będzie, do domu ią przypuści y na każdy pozew sądowy posłusznie stanie.\nSub Eodem Actu. W sprawie Pinchasa Dawidowicza [Dawidowicz?] arendarza kraśnickiego czytano testimonium Iosephi Auckenfelth [Auckenfelth / Augsfeld?], który zaświadczył o długu handlowym.\nItem Wojciech Kłopot przeciwko Adamowi Karolowi Mrokowskiemu [Mrokowski?] malarzowi oskarżenie wnosił o wieprzka karmnego, którego tenże malarz przywłaszczyć sobie ważył się pod pretekstem niespłaconych malowań y obrazów. Sąd nakazał wieprzka do sekwestru złożyć, a malarzowi rachunek z roboty malarskiey na piśmie podać.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073726"
    },
    {
        "nr_skanu": 78,
        "numer_pozycji": "Poz. 78",
        "strona_pagina": "fol. 37r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory spadkowe patrycjatu / Sukcesja wójta Janaszkowica",
        "osoby_podmioty": "Jan Majowski wójt [Majowski]; Jan Onuszkowicz [Onuszkowicz]; Adam Kotowicz [Kotowicz]; Jan Barankowicz [Barankowicz]; Wojciech Borkiewicz [Borkiewicz / Borkowicz?]; Laurenty Pielaszkowicz [Pielaszkowicz]; Paweł Słomkowski [Słomkowski / Słomka?]; Wojciech Nowakowicz landwójt [Nowakowicz / Nowak?]; Katarzyna z Janaszkowiców Nowakowiczowa [Janaszkowicz / Nowakowiczowa]; Ubaldi Janaszkowic zmarły wójt [Janaszkowic]",
        "kwoty_podatki": "Dekret Najwyższego Trybunału Miast Zamoyskich; spór o kamienicę i dobra wójtowskie",
        "opis_sprawy": "Sesja sądu łączonego wójtowsko-radzieckiego pod przewodnictwem wójta Jana Majowskiego. Wielki spór spadkowy po zmarłym wójcie ordynaryjnym Ubaldim Janaszkowicu pomiędzy Pawłem Słomkowskim a landwójtem Wojciechem Nowakowiczem i jego żoną Katarzyną Janaszkowiczówną.",
        "transkrypcja": "Actum in Praetorio Crasniciensi feria Sexta post Dominicam Reminiscere proxima Anno Domini Millesimo Septingentesimo [1700].\nSąd Łączony Radziecki y Wóytowski: JPan Jan Majowski Wóyt, JPan Jan Onuszkowicz, JPan Adam Kotowicz, JPan Jan Barankowicz Konsulowie, Wojciech Borkiewicz [Borkowicz?], Laurenty Pielaszkowicz Ławnicy.\nW sprawie między Sławetnym Pawłem Słomkowskim [Słomkowski?] z iedney, a Sławetnym Woyciechem Nowakowiczem [Nowakowicz?] Landwóytem kraśnickim y Katarzyną z Janaszkowiców małżonką iego z drugiey strony, o podział dóbr, kamienicy, ról y ruchomości po niegdy Sławetnym Ubaldim Janaszkowicu [Janaszkowic?] Wóycie tuteyszym pozostałych. Strona powodowa kładła dekret Najwyższego Trybunału Miast Ordynacyi Zamoyskiey, domagając się intromisyi do części kamienicy na Rynku y ról za miastem. Pozwani replikowali, iż długi spadkowe przewyższają perceptę. Sąd nakazał rewizję regestrów y inwentarza przez delegowanych.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073710"
    },
    {
        "nr_skanu": 79,
        "numer_pozycji": "Poz. 79",
        "strona_pagina": "fol. 37v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory rzemieślnicze i długi / Sukcesja Dziurzyńskiego",
        "osoby_podmioty": "Paweł Słomkowski [Słomkowski]; Wojciech Nowakowicz [Nowakowicz]; Wawrzyniec Stafica kowal [Stafica / Trafica?]; Piotr Tokarczyk [Tokarczyk / Tokarski?]; Szymon Dziurzyński zmarły rajca [Dziurzyński]; Pinchas Dawidowicz [Dawidowicz]; Józef Mazała rzeźnik [Mazała]; Marcin Sanek [Sanek / Samek?]; Maciej Kępka [Kępka / Kępa?]",
        "kwoty_podatki": "5 złp długu; pretensje o żelazo kowalskie i mięso",
        "opis_sprawy": "Dalszy ciąg sporu o spadek Janaszkowicowski. Sprawa kowala Wawrzyńca Staficy przeciwko Piotrowi Tokarczykowi o rozliczenia żelaza i narzędzi po rajcy Szymonie Dziurzyńskim. Pinchas Dawidowicz przeciw rzeźnikowi Józefowi Mazale o dostawę łoju i mięsa. Marcin Sanek przeciw Maciejowi Kępce o 5 złp pożyczki.",
        "transkrypcja": "Actum ut supra in eadem sessione iudiciali.\nCiąg dalszy relacyi komisarzów w sprawie Słomkowskiego z Nowakowiczem: odłożono ad futuram sessionem dla spisania ostatecznego inwentarza.\nSub Eodem Actu. Wawrzyniec Stafica [Stafica / Trafica?] kowal kraśnicki wystąpił przeciwko Piotrowi Tokarczykowi [Tokarczyk?], upominając się zapłaty za robotę żelazną do wozu y pługów, po sukcessorach niegdy Szymona Dziurzyńskiego [Dziurzyński?] raycy kraśnickiego pozostałych. Tokarczyk dowodził, iż dług ten z masy spadkowey zaspokoić należy.\nItem Pinchas Dawidowicz [Dawidowicz?] arendarz żydowski skarżył Józefa Mazałę [Mazała?] rzeźnika o niewydanie skór y łoiu wołowego za pobrane pieniądze. Mazała przyrzekł rzetelnie odważyć towar na jarmarku.\nItem Marcin Sanek [Sanek?] domagał się od Macieia Kępki [Kępka?] 5 złotych polskich [5 złp] długu dawnego; Kępka przyznał pożyczkę y obowiązał się zwrócić na Wielkanoc.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2074440"
    },
    {
        "nr_skanu": 80,
        "numer_pozycji": "Poz. 80",
        "strona_pagina": "fol. 38r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory gruntowe i kościelne / Augustynowskie role",
        "osoby_podmioty": "Tomasz Kępa [Kępa]; Marianna Augustynowa żona Tomasza [Augustynowa / Kępina?]; Marcin Dymarczyk wójt przedmiejski [Dymarczyk]; ks. Paweł Wilhelm Pajecki przeor kanoników regularnych [Pajecki]; Wojciech Szymatowski burmistrz [Szymatowski]",
        "kwoty_podatki": "Role Augustynowskie na Piaskach; pretensje klasztorne o dziesięciny i grunta",
        "opis_sprawy": "Spór małżonków Tomasza i Marianny Kępów z wójtem przedmiejskim Marcinem Dymarczykiem o granice ról Augustynowskich na Przedmieściu Piaski. Następnie pozew przewielebnego ks. przeora Pawła Wilhelma Pajeckiego przeciw burmistrzowi Wojciechowi Szymatowskiemu o bezprawne użytkowanie gruntów kościelnych.",
        "transkrypcja": "Actum in Praetorio Crasniciensi feria Secunda post Dominicam Oculi proxima Anno Domini 1700.\nPrzed Urzędem stanąwszy Tomasz Kępa [Kępa?] wraz z Marianną Augustynową [Augustynowa?] małżonką swoią, formalną skargę wnieśli przeciwko Marcinowi Dymarczykowi [Dymarczyk?] wóytowi przedmieyskiemu na Piaskach, o to, iż miedze ról Augustynowskich dziedzicznych zaorał, krze powycinał y snopy zboża w lecie z pola zabrał. Dymarczyk odpowiadał, że grunt ten od dawna do wóytostwa przedmieyskiego należał. Sąd zarządził wizyą na gruncie z udziałem starszych sąsiadów.\nSub Eodem Actu. Wielebny JX Paweł Wilhelm Pajecki [Pajecki?] Przeor Klasztoru Kraśnickiego Kanoników Regularnych zaniósł protestacyą przeciwko Sławetnemu Woyciechowi Szymatowskiemu [Szymatowski?] Burmistrzowi Kraśnickiemu o zabor roli kościelney przy ogrodach mieyskich y niepłacenie należytey prowizyi.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073707"
    },
    {
        "nr_skanu": 81,
        "numer_pozycji": "Poz. 81",
        "strona_pagina": "fol. 38v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory gruntowe, pobicia i handel żydowski",
        "osoby_podmioty": "ks. Paweł Wilhelm Pajecki [Pajecki]; Wojciech Szymatowski burmistrz [Szymatowski]; Stanisław Dydyński [Dydyński]; Paweł Kłopot [Kłopot]; Anna Ożogowa wdowa [Ożogowa / Ożóg?]; Leybuś Markowicz kupiec żydowski [Markowicz]; Wojciech Słotka [Słotka]",
        "kwoty_podatki": "5 złp 5 gr za sukno i korzenie; Ogród Tyrawski",
        "opis_sprawy": "Dalszy ciąg sprawy ks. Pajeckiego przeciw Szymatowskiemu. Skarga Stanisława Dydyńskiego przeciw Pawłowi Kłopotowi o napad i pobicie kłonicą na bagnie miejskim. Protestacja wdowy Anny Ożogowej przeciw burmistrzowi Szymatowskiemu o Ogród Tyrawski. Sprawa kupca Leybusia Markowicza przeciw Wojciechowi Słotce o dług 5 złp 5 gr za sukno.",
        "transkrypcja": "Actum ut supra in eadem sessione.\nDalszy ciąg sprawy Klasztoru z Burmistrzem Szymatowskim: odłożono do zjazdu Jmć Pana Podskarbiego.\nItem Stanisław Dydyński [Dydyński?] skarżył Pawła Kłopota [Kłopot?], iż go na bagnie pod groblą mieyską najechał, słowy zelżywemi zwymyślał y kłonicą z woza wyciągnioną w ramię uderzył, o czym sinek krwawy przed sądem pokazał. Kłopot tłumaczył się obroną konieczną.\nItem Anna Ożogowa [Ożogowa?] wdowa protestowała przeciw Woyciechowi Szymatowskiemu o bezprawne zagarnienie Ogrodu Tyrawskiego, należącego z prawa do sukcesyi po rodzicach.\nItem Leybuś Markowicz [Markowicz?] Żyd kramarz kraśnicki dochodził od Woyciecha Słotki [Słotka?] 5 złotych polskich y 5 groszy [5 złp 5 gr] za sukno barchanowe y korzenie kuchenne w kramie wzięte a niedopłacone. Sąd nakazał Słotce dług uiścić sub poena aresztu.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2074432"
    },
    {
        "nr_skanu": 82,
        "numer_pozycji": "Poz. 82",
        "strona_pagina": "fol. 39r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory gruntowe i przedmieszczańskie / Brama Sandomierska",
        "osoby_podmioty": "Wojciech Tokarczyk [Tokarczyk]; Butkowie sukcesorowie [Butko / Butkowie?]; Kazimierz Szmarowic [Szmarowic / Szmaro?]; Józef Mazała rzeźnik [Mazała]; Anna Mazała żona [Mazała]; Tomasz Jardzik [Jardzik / Jardzyk?]; Zofia Jardzikowa żona [Jardzikowa]",
        "kwoty_podatki": "Ogród Butkowski (Gabryszowski) za Bramą Sandomierską",
        "opis_sprawy": "Sprawa sukcesorów Butków i Wojciecha Tokarczyka przeciwko Kazimierzowi Szmarowicowi o bezprawne użytkowanie łąki. Zeznanie i sprawa Józefa Mazały rzeźnika i jego żony Anny przeciw Tomaszowi Jardzikowi i żonie Zofii o granice Ogrodu Gabryszowskiego (Butkowskiego) położonego za Bramą Sandomierską.",
        "transkrypcja": "Actum in Praetorio Crasniciensi feria Quarta post Dominicam Laetare Anno Domini 1700.\nPrzed Urzędem stanąwszy Woyciech Tokarczyk [Tokarczyk?] imieniem sukcessorów Butków [Butko?], protestował przeciw Kazimierzowi Szmarowicowi [Szmarowic?] o wykoszenie trawy na łące Butkowskiey y zepchnięcie kopców granicznych. Szmarowic odesłany do dowodzenia świadkami.\nSub Eodem Actu. Ućciwy Józef Mazała [Mazała?] rzeźnik wraz z żoną Anną z iedney, a Tomasz Jardzik [Jardzik?] z żoną Zofią z drugiey strony, czynili sprawę o Ogród Butkowski inaczy Gabryszowski nazwany, leżący za Bramą Sandomierską. Jardzik mienił, iż część tego ogrodu kupił z dawna od Gabrysza, Mazała zaś kładł kwity na własność zupełną. Urząd nakazał obu stronom pokazać dokumenta na sesyi powielkanocney pod rygorem utraty prawa.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2074411"
    },
    {
        "nr_skanu": 83,
        "numer_pozycji": "Poz. 83",
        "strona_pagina": "fol. 39v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Przemoc i kontrakty sprzedaży / Grunta Luterskie",
        "osoby_podmioty": "Maciej Kępa [Kępa]; Bartłomiej Pastuszek [Pastuszek]; Stanisław Jerzykiewicz podwójci [Jerzykiewicz]; Adam Michał Płechowicz pisarz miejski [Płechowicz]; Stefan Luterek [Luterek / Luter?]; Stanisław Luterek brat [Luterek]",
        "kwoty_podatki": "Transakcja kupna-sprzedaży (venditio) ról luterskich; pobicie pastuszka",
        "opis_sprawy": "Skarga Macieja Kępy na Bartłomieja Pastuszka o zranienie i dotkliwe pobicie pasterza gminnego pilnującego bydła. Wpis kontraktu kupna i sprzedaży gruntów luterskich dokonany przed podwójcim Stanisławem Jerzykiewiczem i pisarzem miejskim Adamem Michałem Płechowiczem przez Stefana Luterka bratu Stanisławowi.",
        "transkrypcja": "Actum in Praetorio Crasniciensi feria Sexta ante Dominicam Judica proxima Anno Domini 1700.\nPrzed Urzędem Ućciwy Maciey Kępa [Kępa?] przedmieszczanin solenniter manifestował się imieniem Bartłomieia Pastuszka [Pastuszek?] przeciw pachołkom mieyskim o pobicie pastusząt przy wypasie na pastwisku mieyskim. Skargę do wizyi przyjęto.\nActum coram Officio Advocatiali et Scabinali Crasniciensi.\nKontrakt venditionis kupna y przedaży między Ućciwemi Stefanem Luterkiem [Luterek?] z iedney, a Stanisławem Luterkiem bratem swym rodzonym z drugiey strony, przed Urząd przyszedłszy jawnie zeznali: Sławetny Stanisław Jerzykiewicz [Jerzykiewicz?] Podwóyti kraśnicki y Adam Michał Płechowicz [Płechowicz?] Pisarz Miasta Kraśnika przysięgły, iż na mocy zlecenia urzędowego zjechali na grunta Luterskie, aby dopełnić rzetelney rezygnacyi y wprowadzenia w possessyą kupca.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073761"
    },
    {
        "nr_skanu": 84,
        "numer_pozycji": "Poz. 84",
        "strona_pagina": "fol. 40r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Obdukcja ran i kontrakty kupna-sprzedaży / Grunt Luterski",
        "osoby_podmioty": "Maciej Kępa [Kępa]; Bartłomiej Pastuszek [Pastuszek]; Mazurek stangret Słomkowskiego [Mazurek / Słomkowski]; Stanisław Chmiel [Chmiel / Chmielik?]; Stefan Luterek [Luterek]; Mikołaj Luterek brat [Luterek]; Stanisław Luterek kupiec [Luterek]; Stanisław Jerzykiewicz podwójci [Jerzykiewicz]; Adam Michał Płechowicz pisarz [Płechowicz]",
        "kwoty_podatki": "Obdukcja ran ciętych brzytwą; cesja i rezygnacja gruntu przedmiejskiego",
        "opis_sprawy": "Obdukcja ran i zeznanie Macieja Kępy o pobiciu syna Bartłomieja Pastuszka przez stangreta Mazurka (cięcia brzytwą w głowę i palce). Kontrakt urzędowy sprzedaży gruntu Luterskiego na Przedmieściu przez Stefana i Mikołaja Luterków bratu Stanisławowi Luterkowi z relacją podwójciego Jerzykiewicza i pisarza Płechowicza.",
        "transkrypcja": "39 v [fol. 40r]\nprzed WBNta Do Urzędu y Akt ninieyszych wóytowskich y ławniczych kraśnickich we własney osobie przyszedł Uczciwy Maciey Kępa [Kępa?] przedmieszczanin, solenne protestował się swoiem y Urodzonego Bartłomieia Pastuszka [Pastuszek?] sierot pastuszyckich imieniem przeciwko Mazurkowi [Mazurek?] stangretowi dawnego Ućciwego Pana Słomkowskiego MK. Okaże, iż on lubo widział odbieżone od bydła które u Ućciwego Stanisława Chmiela [Chmiel / Chmielik?] pewnego przedmieszczanina iest, iednak podymne dymnika bił u ludzi, ino procesus uis ventilationis postrzał tegoż Pastuszyckiego syna... naprzód nad brań lewą w trzy ras przecięty, na członkach palce uparł y... Item nadsym razem ras na członek ubił... Item asseruit ze dopiero na głowie iego brzytwom bił... poranienie... offerendo se fuisse dindicaturum velle...\nActum coram Officio Advocatiali et Scabinali Crasniciensi...\nKontrakt venditionis kupna y przedaży miedzy Ućciwemi Stefanem Luterkiem [Luterek?] z Ućciwym Mikołaiem bracią rodzona z iedney, a Stanisławem Luterkiem przedmieszczaninem, kupiec, przyszedł do Xiąg ninieyszych... per modum Inscriptionis Venditionis quod Actis continuatur, iako Kontrakt w sobie sferę opiewa.\nDo Urzędu y Akt ninieyszych we własobie swoiey przyszedł Sławetny Pan Stanisław Jerzykiewicz [Jerzykiewicz?] Podwóyti kraśnicki, P. Adam Michał Płechowicz [Płechowicz?] Pisarz Miasta Kraśnika przysięgły, iż Oni ex commisso mandato delegowani in vim vel verd ac fidelis relationis publice libereque resignowerunt, iż Oni stosuiąc sie do Kontraktu y Cesiey na grunt Luterski rzeczony, za Naprzód mieyscu Kraśnickim leżący przez Urodzonego Sobie Stefana Luterskiego z płodzeniem, to iest dobrze specifice...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2074328"
    },
    {
        "nr_skanu": 85,
        "numer_pozycji": "Poz. 85",
        "strona_pagina": "fol. 40v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Intromisje gruntowe i spory o miedze / Piaski i Augustynowskie",
        "osoby_podmioty": "Stanisław Luterek [Luterek]; Anna Luterkowa żona [Luterkowa]; Józef Mazała rzeźnik [Mazała]; Walenty Gorgiel [Gorgiel / Jordel?]; Stanisław Jerzykiewicz podwójci [Jerzykiewicz]; Wawrzyniec Pielaszkowicz ławnik [Pielaszkowicz]; Adam Michał Płechowicz pisarz [Płechowicz]; Tomasz Kępa [Kępa]; Marianna Kępina żona [Kępina]; Marcin Dymarczyk wójt przedmiejski [Dymarczyk]; Matjasz Stachmielko [Stachmielko / Stachmiel?]; Tomasz Stafica [Stafica]; Szymon Wójcik [Wójcik / Woycik?]; Adam Ziębatek [Ziębatek / Zięba?]; Jan Dębski [Dębski]; Jakub Stary Bereźnik [Bereźnik]; Wojciech Sanaszkowic [Sanaszkowic / Janaszkowic?]",
        "kwoty_podatki": "Wprowadzenie w posesję ogrodu Luterskiego; wizja ról na Przedmieściu Piaski",
        "opis_sprawy": "Intromisja Stanisława Luterka i żony Anny do ogrodu luterskiego graniczącego z gruntem Mazały i Walentego Gorgiela. Wizja lokalna i delimitacja gruntu Augustynowskiego na Przedmieściu Piaski przez delegatów urzędu z udziałem starszych sąsiadów przedmiejskich (Stachmielko, Stafica, Wójcik, Ziębatek, Dębski, Bereźnik, Sanaszkowic).",
        "transkrypcja": "40 [fol. 40v]\nOgródkaż Luterska leżący confinis mehis Uczciwemu Stanisławowi Luterzkowi [Luterek?] y Annie małżonkom y ich Successorom zaszumną [lub zasumną?] ura pusie wyważoną tymże kupcom intromissia rzetelny z possessyą zrazu dali powagę w et mecis Osobach Pana Naywyższego moca Jaśnie O Panow Sędziec Wóyta z Ławnikami oddali wiecznemi czasy bez żadney impetyi, granice tego gruntu Należące in flue Officij Jenks pokazane uspokoiwszy się y przyznana stron sąsiedzkie ktore iest Mazała, Ogrodek maiący y Valentego Gorgiela [Gorgiel / Jordel?], iako z dawna należąca meta dodana w possessią kupcow per recursum. Quod praesentibus notum solemiter...\nActum coram Officio Advocatiali et Scabinali Crasniciensi... Feria Tertia in festino Festi Sanctae Annae Mettertiae Anno Domini Millesimo Septingentesimo [wtorek po św. Annie, 27 lipca 1700 r.].\nDo Urzędu y Akt we własobach swoich przyszedłszy Sławetni Panowie Stanisław Jerzykiewicz Podwóyti kraśnicki, Wawrzyniec Pielaszkowicz Ławnik, Adam Michał Płechowicz Pisarz Kraśnicki... publice libereque recognoverunt, iż Oni stosuiąc sie do decreti Sądow Obywatelskich tuteyszych kraśnickich, którzy Ućciwymi Tomaszem Kępom [Kępa?] y Marina [Marianną] Małżonkami, Aktorami, a Marcinem Dymarczykiem [Dymarczyk?] Woytem Przedmieszczym, pozwanym sententią... Na Instancyą wyżey Aktorów consentiente parte fatata Condescendowali: Na Przedmieście Piaseckie [Piaski] tuteysze kraśnickie, Na grunt quondam Augustynowskie nazwany Aktorom prawem dziedzictwa starożytamte porwawszy do siebie Sąsiadów tamterznych Matyasa Stachmielko [Stachmielko?] Woyta, Tomasza Stafice [Stafica?], Szymona Woycika [Wójcik?], Adama Ziębatka [Ziębatek?], Jana Dębskiego [Dębski?], Jakuba Starego Bereźnika [Bereźnik?], Woyciecha Sanaszkowica [Sanaszkowic / Janaszkowic?]...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073799"
    },
    {
        "nr_skanu": 86,
        "numer_pozycji": "Poz. 86",
        "strona_pagina": "fol. 41r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Wizje gruntowe, obdukcja ran i Cech Krawiecki / Pacanowski",
        "osoby_podmioty": "Marcin Dymarczyk [Dymarczyk]; Brożek rymarz [Brożek]; Grzegorz Konopczanka [Konopczanka / Konopczonka?]; Sebastian Kowalek [Kowalek]; Ożóg mąż sługi [Ożóg]; Jakub Kłopot przedmieszczanin [Kłopot]; Cech Krawiecki [Contubernium]; Łukasz Pacanowski zmarły [Pacanowski]; Paweł Słomkowski [Słomkowski]; Stanisław Szymura [Szymura]",
        "kwoty_podatki": "Obdukcja 6 ran i cięć palców; testament i spadek po Łukaszu Pacanowskim",
        "opis_sprawy": "Zakończenie wizji gruntu Dymarczyka ze świadectwem rymarza Brożka i Konopczanki. Obdukcja ran Sebastiana Kowalka pchniętego i pobitego przez sługę męża Ożoga (rany rąk, palców, boku i pleców). Przesłuchanie świadków w sprawie zapisu testamentowego zmarłego Łukasza Pacanowskiego na rzecz Cechu Krawieckiego i Szewskiego.",
        "transkrypcja": "40 v [fol. 41r]\nwszystkich o dobremsie, dispu gruntu tegoż uczynili... Budynek dawny nalegurce groncie spustoszały, wczęść chałupę Oycowską... Ogród... Dymarczyka... Aktorowie prezentowali... Sąsiedzi wyznali, iż Dymarczyk z powinowatemi... Dymarczyk zaś nic nie prezentował, ale tylko pomieniony Rymarz Brożek [Brożek?]... Grzegorz Konopczanka [Konopczanka / Konopczonka?]... Sąsiedzi że Dymarczyk posiadł, wizya urzędowa do ksiąg wpisana.\nItem: Przed Urzędem stanąwszy Ućciwy Sobestian Kowalek [Kowalek?], prezentował rany: naprzód na lewey ręce ras krwawy... od sługi męża Ożoga [Ożóg?] rano pchnięty od sługi maiącego tegosz pachołka... Item na prawey ręce dwa krwawe, na dwa palce ocięcie z których ranas... Item na plecach koło lewey strony podbite z siniakami... Item w plecy z boku... Item z prawego boku rany...\nSub Eodem Actu.\nEx Instantia Honesti Jacobi Kłopot [Kłopot?], Suburbani, contra Contubernium... krawców o nieboszczyka Łukasza Pacanowskiego [Pacanowski?]... P. Paweł Słomkowski [Słomkowski?] na Warcie zasiadający w dyssidentach... P. Stanisław Szymura [Szymura?] pytał...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073866"
    },
    {
        "nr_skanu": 87,
        "numer_pozycji": "Poz. 87",
        "strona_pagina": "fol. 41v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spadek Pacanowskiego, pobicia i kontumacje",
        "osoby_podmioty": "Łukasz Pacanowski zmarły [Pacanowski]; Stanisław Szymura [Szymura]; Paweł Słomkowski [Słomkowski]; Cech Szewski [Cech Szewski]; Stanisław Luterek kupiec [Luterek]; Jan Trawiński [Trawiński]; Paweł Nowakowic [Nowakowic]; Domicela Sławnikowa [Sławnikowa]; Maciej Młynarczyk [Młynarczyk]; Wojciech Kindrat [Kindrat]; Dyrutek [Dyrutek / Dyruteńka?]; Paweł Kłopot [Kłopot]; Paweł Łapka [Łapka]; Szymon Drojczak [Drojczak / Droyczak?]; Maciej Kępa [Kępa]",
        "kwoty_podatki": "Zapis roli przy Baszcie Szewskiej; manifestacje i dekrety o pobicie",
        "opis_sprawy": "Zeznania Pawła Słomkowskiego i Stanisława Szymury o ustnej woli Pacanowskiego (rola pod Basztą dla cechu). Sprawa Stanisława Luterka przeciw Janowi Trawińskiemu o pobicie. Sprawa Pawła Nowakowica z Domicelą Sławnikową. Wpisy kontumacji i spraw karnych (Młynarczyk, Kindrat, Dyrutek, Łapka, Drojczak, Kępa).",
        "transkrypcja": "41 [fol. 41v]\npytał, azliby tegoż dom który rozrządził rzekł: coście mam rozporządzić... żonie miedzy trodhey sad zagrodce leżąc... wedle Baszty szewcey roli do suchputkego... brat nieboszczyka... Stanisław Szymura [Szymura?] rzekł: U nas każdy brat ma rola w rolach były dzieci wasze me przesądzone były dla tego odpowiedział: czyńcieście co chcecie...\nDalsi testes: Sławetny Paweł Słomkowski [Słomkowski?] recognovit: Pamiętam dobrze, iż Nieboszczyk Łukasz Pacanowski [Pacanowski?] w Ławce swey, ktory rozpowiadaiąc swoie rzeczy, mnie mianował, iżby Cechowi szewskiemu miał zapisować po swey smierci rolę, chyba by na szynk które leżał, tego nie wiem.\nActum coram Officio Advocatiali et Scabinali Crasniciensi, feria Quarta post festum Sanctae Annae Mettertiae proxima, Anno Domini Millesimo Septingentesimo [środa po św. Annie, 28 lipca 1700 r.].\nW sprawie y z Akttey między Ućciwymi Stanisławem Luterkiem [Luterek?] kupcem z Przedmieszczanem tuteyszym iedney, a Janem Trawińskim [Trawiński?] pozwanym o pobicie y zniewazenie, aktura datus dilatio Inquisitionis ad ferias festum proxime venturas...\nSub Eodem Actu.\nW sprawie między Successorami niegdy Łukasza Pacanowskiego a Cechem Szewskim, remittitur ad plenariam sessionem...\nSprawa y Akcya między Ućciwymi Pawłem Nowakowicem [Nowakowic?] a Domicelą Sławnikową [Sławnikowa?] pozwanym, aby do Manifestucyi zapłacił Paweł Nowakowic... Exeqwencya przysięgi suspenditur ad ferias decimam post festum Sancti Bartholomaei...\nEx Instantia Mathiae Młynarczyk [Młynarczyk?] et Alberti Kindrat [Kindrat?]...\nIn Instantia Dyrutek [Dyrutek?] et Pauli Kłopot [Kłopot?] contumax primo.\nIn Instantia Pauli Łapka [Łapka?], Simon Droyczak [Drojczak?] contumax primo.\nEx Instantia et Mathiae Kępa et Pauli Słomkowski reus non constituitur...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2074321"
    },
    {
        "nr_skanu": 88,
        "numer_pozycji": "Poz. 88",
        "strona_pagina": "fol. 42r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory z burmistrzem i zniesławienia / Dobra Kędzierskich",
        "osoby_podmioty": "ks. Paweł Wilhelm Pajecki przeor [Pajecki]; Anna Tyrawska [Tyrawska]; Samuel syn Anny [Samuel / Tyrawski?]; Wojciech Szymatowski burmistrz [Szymatowski]; Wawrzyniec Pielaszkowicz ławnik [Pielaszkowicz]; Marianna Pielaszkowiczowa żona [Pielaszkowiczowa]; Zofia Wanna małżonka Dębia [Wanna / Dęba?]; Jan Majowski wójt [Majowski]",
        "kwoty_podatki": "Dobra Kędzierskich na Przedmieściu; kara za zniesławienie ławnika na Rynku",
        "opis_sprawy": "Protestacja Anny Tyrawskiej i syna Samuela przeciw burmistrzowi Wojciechowi Szymatowskiemu o bezprawne zajęcie dóbr Kędzierskich na przedmieściu i niestawiennictwo w sądzie. Protestacja ławnika Wawrzyńca Pielaszkowica i żony Marianny przeciw Zofii Wannie (Dębinie) o publiczne zelżenie na Rynku w obecności wójta.",
        "transkrypcja": "41 v [fol. 42r]\nEx Instantia Venerabilis, Admodum Rdi Dni, Pauli Wilhelmi Paiecki [Pajecki?] Praepositi Crasniciensis... in solidum decem Marcarum polonicalium...\nDo Urzędu y Akt ninieyszych wóytowskich y ławniczych kraśnickich we własney osobie przyszedłszy Jmć Sławetna Pani Anna Tyrawska [Tyrawska?] swoiey y małoletniego syna o procuratorstwo habitione faciat ac se se praesentibus inseri fecit, tudziesz sławetny Samuelem Anny synem ze spadek Matki swey imieniem wisko naturalna successorką dóbr Kędzierskich nazwany na przedmieściu Kraśnickiem leżących przeciwko Sławetnemu Panu Woyciechowi Szymałowskiemu [Szymatowski?] Burmistrzowi Kraśnickiemu, iż On zadnych decretow nie vergit... nie tylko nie stawił, ale y sam do Sądu nie stanął... protestatur de parando damno et litis expensis...\nDo Urzędu y Akt ninieyszych we własobie swoiey przyszedłszy Sławetny Pan Wawrzyniec Pielaszkowicz [Pielaszkowicz?] Ławnik Kraśnicki swoiem y Maryanny małżonki imieniem, solenne świadkom talem protestował się przeciwko Ućciwey Zoffiey Pierwszey Wanna Dębia [Wanna / Dęba?] małżonce Obywatelce Kraśnickiey, o to iż Ona dnia wczorayszego publice na Rynku przed panem Woytem, który przez Inkwizycią rewelowany mi iako też Małżonkowi iego opprobriaces [opprobriando?] silić Uczciwie sławy miecz swoiey... o contumaciam...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2074303"
    },
    {
        "nr_skanu": 89,
        "numer_pozycji": "Poz. 89",
        "strona_pagina": "fol. 42v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory sąsiedzkie, kłótnie kobiet i bójka w browarze",
        "osoby_podmioty": "Wawrzyniec Pielaszkowicz [Pielaszkowicz]; Marianna Pielaszkowiczowa [Pielaszkowiczowa]; Wojciech Durgot [Durgot]; Zdebowa sąsiadka [Zdebowa / Zdeb?]; Pielaszkowiczówna dziewczyna [Pielaszkowiczówna]; Bogdanowa [Bogdanowa / Bogdan?]; Wojciech Kindrat [Kindrat]; Stanisław Pastuszek [Pastuszek]; Pawełek chłopiec [Pawełek]; Jan Trawiński rzeźnik [Trawiński]; Stanisław Maniawczyk [Maniawczyk]; Stanisław Luterek kupiec [Luterek]",
        "kwoty_podatki": "Kłótnia kobiet o dzieci; bójka i szamotanina w browarze miejskim",
        "opis_sprawy": "Zeznania Wojciecha Durgota o kłótni domowej Zdebowej z Pielaszkowiczową o bicie dzieci. Zeznanie Stanisława Pastuszka w sprawie Kindrata. Zeznanie Stanisława Maniawczyka o awanturze w piwiarni/browarze między szwagrem Janem Trawińskim a Stanisławem Luterkiem (chwycenie za gardła i wypchnięcie na ulicę).",
        "transkrypcja": "42 [fol. 42v]\nActum coram Officio Advocatiali et Scabinali Crasniciensi feria Sexta post festum Sanctae Annae Mettertiae proxima, Anno Domini Millesimo Septingentesimo [piątek po św. Annie, 30 lipca 1700 r.].\nEx Instantia et Tamen Laurenty Pielaszkowicz [Pielaszkowicz?] et Marina Horestii, Albertus Durgot [Durgot?] consors... De formalis verbis: Cechowa rzekła: recognovit, We środę niedawno przeszłą przyszła Zdebowa [Zdebowa?] do mnie, rzecząc: dawnom u was Pielaszkowiczowa nie była... tam dzieci pobyły się... Zdebowa rzekła do moiey dziewczyny Pielaszkowicównie: Weźcie chłopczyka... Pielaszkowiczowa nie oburzyła się... Zdebowa rzekła: Bogdanowa [Bogdanowa?] Bogdany z Porohie poranił... Zdebowa Bogdanowi... rzekła: dla ciebie wielka bieda, zestarzała się... wpadła w opadek swóy...\nEx Instantia Alberti Kindrat [Kindrat?] Honesti Stanislaus Pastuszek [Pastuszek?]... recognovit: widziała, y rzekła do chłopca: ty Pawełku weźmij się za łeb, nie będziesz bał oyca twego... potym w oborzynie pobił...\nEx Instantia Trawiński Lanionis Stanislaus Maniawczyk [Maniawczyk?]... Recognovit: Przyszedł do mnie szwagier Trawiński [Trawiński?], do piwarni siedział sobie... Potym przyszedł Luterek [Luterek?]... począł wołać na Trawińskiego... zbytnie mianował Luterek, uderzył go w pysk... Obydwa się ująwszy za bary... ciągnęli do domu...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073842"
    },
    {
        "nr_skanu": 90,
        "numer_pozycji": "Poz. 90",
        "strona_pagina": "fol. 43r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Zeznania świadków o pijaństwo i zniewaga kustosza",
        "osoby_podmioty": "Marcin Panek [Panek]; Wojciech Słotka [Słotka]; Stanisław Luterek [Luterek]; Jan Trawiński [Trawiński]; Barbara Okninówna [Okninówna / Oknińska?]; Janowa Dębowa [Dębowa]; Marina Okninówna [Okninówna]; Ewa Banaszkowa [Banaszkowa / Banaszek?]; Paweł Kłopot przedmieszczanin [Kłopot]; Jakub Kasperek [Kasperek]; ks. Kustosz Kraśnicki [Kustosz]",
        "kwoty_podatki": "Pobicie w pysk na Rynku; rzucanie kamieniami przed dworkiem kustosza",
        "opis_sprawy": "Zeznania Marcina Panka, Barbary i Mariny Okninówien oraz Ewy Banaszkowej w sprawie pijackiej awantury Luterka z Trawińskim pod sądem. Protestacja Pawła Kłopota przeciw Jakubowi Kasperkowi o publiczne zelżenie ('skurwysyn') i namawianie pachołków do rzucania kamieniami przed domem ks. Kustosza.",
        "transkrypcja": "42 v [fol. 43r]\nciągnąc do domu... Ex Instantia Eiusdem. Honesti Martinus Panek [Panek?] recognovit: Szedłem z Słotką [Słotka?] w poniedziałek... Luterek siedzący... rzekł: coście pytacie y głupie gadacie... rzekłem: czemu wy tak mówicie do ludzi... Luterek w pysk uderzył y począł wołać ratunku...\nEx parte Luterek: Judita Barbara Okninowna [Okninówna?], służąca u Luterkowey: Recognovit: Przyszła Dębowa Janowa [Dębowa?] po szostki do Luterka... Janowa rzekła: daycie mi moie pieniądze... Luterek odpowiedział: rozrachuymy się wprzód...\nEx Instantia Eiusdem Marina Okninowna [Okninówna?] similia recognovit...\nEx Instantia Trawiński Ewa Banaszkowa [Banaszkowa?] Recognovit: Widziałam szwagra Trawińskiego [Trawiński?], kiedy przyszedł Luterek pod Sąd Obywatelski... Trawiński przystąpił do niego, rzekł: kończmy sprawę po chrześciańsku... Ale Luterek piiąny będąc, porwał go za kołnierz...\nActum feria Secunda in Vigilia festi Sancti Bartholomaei, Anno Domini Millesimo Septingentesimo [poniedziałek, Wigilia św. Bartłomieja, 23 sierpnia 1700 r.].\nPrzed Urzędem y Aktami ninieyszemi we osobie swoiey przyszedł Ućciwy Paweł Kłopot [Kłopot?] Przedmieszczanin, solenne protestował się przeciwko Ućciwemu Jakubowi Kasperkowi [Kasperek?] Przedmieszczaninowi, O to, iż On dnia wczorayszego protestanta do krystuaryi z lżewemi słowy iako to: ten skurwisyn to ty ptaki w tym podchodzi, idącego przed domem Jmć Xsiędza Kustosza [Kustosz?] Kraśnickiego posłać kazał kamieniom za nim...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073821"
    },
    {
        "nr_skanu": 91,
        "numer_pozycji": "Poz. 91",
        "strona_pagina": "fol. 43v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Asygnacje podskarbiny Zamoyskiej / Długi i restauracja domów",
        "osoby_podmioty": "Jan Barankowicz burmistrz [Barankowicz]; Maciej [Matyasz] Pielaszkowicz dawny radca [Pielaszkowicz]; Pinchas Dawidowicz arendarz kraśnicki [Dawidowicz]; Anna z Gnińskich Zamoyska podskarbina wielka koronna [Zamoyska]; Urząd Wójtowsko-Ławniczy [Urzad]",
        "kwoty_podatki": "Asygnacja: 43 złp na dom Barankowicza, 80 złp na dług Pielaszkowicza u Żyda",
        "opis_sprawy": "Wpisanie do akt asygnacji Jaśnie Wielmożnej Anny Zamoyskiej Podskarbiny Wielkiej Koronnej do arendarza Pinchasa Dawidowicza na wypłatę 43 złp Janowi Barankowiczowi na restaurację domu oraz 80 złp Matyaszowi Pielaszkowiczowi na spłatę długu nadwornego u Żydów, z zabezpieczeniem na ich domach.",
        "transkrypcja": "43 [fol. 43v]\nActum coram Officio Advocatiali et Scabinali Crasniciensi, feria Secunda in Vigilia Festi Sancti Laurentij, Anno Domini Millesimo Septingentesimo [poniedziałek, Wigilia św. Wawrzyńca, 9 sierpnia 1700 r.].\nDo Urzędu y Akt ninieyszych Wóytowskich y Ławniczych Kraśnickich we osobach swoich stanąwszy Sławetni Panowie Jan Barankowicz [Barankowicz?] Burmistrz Kraśnicki, Matyasz Pielaszkowicz [Pielaszkowicz?] Radca dawny, prosili Urzędu, aby do Akt y Xiąg ninieyszych Assignatią do Starozakonnego Pinchasa Dawidowicza [Dawidowicz?] Arendarza, Obywatela Kraśnickiego, pod datą tertia Augusti Anno ut praesens ferrent, ręką Jaśnie Wielmożney Jey Mći Dobrodzieyki podpisaną, przyiąć, perceptę assignacyi dwoiey trzymać, przyietaiest folio... tey assignatyi tenor takowy:\nArendarzu Kraśnicki, Za odebraniem tey Assignacyi wyday Barankowiczowi na restauracyą domu Jego Złotych Czterdzieści y trzy [43 złp], a także Matyasowi Pielaszkowiczowi Złotych Ośmdziesiąt [80 złp] na spłacenie długu Nadwornego u Żyda zaciągnionego, którzy iednak przed odebraniem pieniędzy, aby wprzód w Xięgach Mieyskich zagęścili te długi na domach swoich... Anna Zamoyska Podskarbina Wielka Koronna [dnia 3 Augusti 1700].\nPrzed tymże Urzędem... na umysłach y ciałach swoich będąc jaśnie, iawnie, dobrowolnie... zeznali, iż Oni summę w assignacyi Jaśnie Wielmożney Jey Mći Dobrodzieyki swoiey przez Starozakonnego Pinchasa Dawidowicza Arendarza Kraśnickiego odebrali: ieden JPan Barankowicz Burmistrz Kraśnicki, drugi zaś Imć Pan Pielaszkowicz Radca dawny... obligują się na domach swoich...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2074369"
    },
    {
        "nr_skanu": 92,
        "numer_pozycji": "Poz. 92",
        "strona_pagina": "fol. 44r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Kontrakty sprzedaży nieruchomości / Ogród Tyrawski",
        "osoby_podmioty": "Wojciech Szymatowski burmistrz [Szymatowski]; Teresa Szymatowska małżonka [Szymatowska]; Stanisław Tyrawski [Tyrawski]; Anna Tyrawska żona [Tyrawska]; Grzegorz Pielaszkowicz [Pielaszkowicz]; Maciej Kępa [Kępa]",
        "kwoty_podatki": "Cena kupna 250 złp; Ogród Tyrawski na Przedmieściu Kraśnickim",
        "opis_sprawy": "Zeznanie kontraktu sprzedaży Ogrodu Tyrawskiego na Przedmieściu Kraśnickim (położonego między gruntami Grzegorza Pielaszkowicza a Macieja Kępy) przez burmistrza Wojciecha Szymatowskiego i żonę Teresę na rzecz Stanisława i Anny Tyrawskich za sumę 250 złotych polskich.",
        "transkrypcja": "43 v [fol. 44r]\nActum coram Officio... feria Quinta Ante Festum Assumptionis Beatae Mariae Virginis proxima, Anno Domini Millesimo Septingentesimo [czwartek przed Wniebowzięciem NMP, 12 sierpnia 1700 r.].\nPrzed Urzędem y Aktami ninieyszemi Obywatelskiemi Kraśnickiemi we osobach swoich stanąwszy Zacnie Sławetni Panowie Woyciech Szymatowski [Szymatowski?] Burmistrz Kraśnicki y Teresa Małżonkowie... zeznali: Iż Oni dobrowolnie, bez żadnego przymusu, w sprawach z Sławetnym Stanisławem Tyrawskim [Tyrawski?] y Anną Małżonkami zawartych... Ogród Tyrawskie tu na Przedmieściu Kraśnickiem leżący, miedzy Ućciwemi Grzegorzem Pielaszkowiczem [Pielaszkowicz?] Mieszczaninem Kraśnickim, a Maciejem Kępą [Kępa?] Przedmieszczaninem leżący, ze wszemi pożytkami, parkanami, drzewem rodzącym y nierodzącym... Sławetnym Państwu Stanisławowi Tyrawskiemu y Annie Małżonkom za summę Złotych Polskich Dwieście Pięćdziesiąt [250 złp] przedali, rezygnowali y wiecznemi czasy puścili...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2074277"
    },
    {
        "nr_skanu": 93,
        "numer_pozycji": "Poz. 93",
        "strona_pagina": "fol. 44v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory mieszczańsko-żydowskie i zaraza bydła",
        "osoby_podmioty": "Krystyna Puklina wdowa [Puklina]; Tomasz Oczapka zięć [Oczapka]; Lewek Bielski Żyd kraśnicki [Bielski]; Marcin Dymarczyk wójt piaskowy [Dymarczyk]; Bartłomiej Piasecki [Piasecki]; Jan Trawiński [Trawiński]; Kazimierz Stafica [Stafica]; Grzegorz Pielaszkowicz [Pielaszkowicz]; Herszek Żyd [Herszek]; Andrzej Tkaczyk [Tkaczyk / Tkarczyk?]; Jan Śmieszkowic [Śmieszkowic]",
        "kwoty_podatki": "7 złp długu; szkody od wołu zarażonego zarazą",
        "opis_sprawy": "Dekrety sądu wójtowskiego: Oczapka zobowiązany do zaspokojenia teściowej Pukliny. Lewek Bielski Żyd przeciw Marcinowi Dymarczykowi o przypędzenie chorego wołu i zarażenie stada bydła (zarządzona inkwizycja). Dymarczyk przeciw Bartłomiejowi Piaseckiemu. Trawiński v. Kazimierz Stafica po jarmarku urzędowskim. Rozliczenia długów z Żydem Herszkiem (Pielaszkowicz, Tkaczyk, Śmieszkowic).",
        "transkrypcja": "44 [fol. 44v]\nSprawa między Ućciwą Krystyną Pukliną [Puklina?] wdową Aktorką, a Ućciwym Tomaszem Oczapką [Oczapka?] zięciem pozwanym: aby przed prawem zaspokoił matkę ze wszytkiego dobra, co z domu zabrał, pod zakładem aresztu. Nakazuje się.\nSprawa y Akcya między Niewiernym Żydem Lewkiem Bielskim [Bielski?] Obywatelem Kraśnickim z iedney, a Ućciwym Marcinem Dymarczykiem [Dymarczyk?] Wóytem Piaskowym pozwanym: o zarażenie wołem zarazy morowey, którego przed targiem niedzielami trzymał y pasł im pod borem kazał niebezpiecznego, na ktorym bydło padło. Pozwany zeznał, że kupił woła zdrowego. Sąd nakazał inkwizycyą świadkami sąsiedzkiemi.\nSprawa między Marcinem Dymarczykiem Aktorem a Bartłomiejem Piaseckim [Piasecki?] pozwanym o bezprawie na roli.\nSprawa między Ućciwym Janem Trawińskim [Trawiński?] Aktorem a Kazimierzem Staficą [Stafica?] pozwanym: stanął dekret, aby wszelkie pretensye po Jarmarku Urzędowskim uspokoił.\nRemittował się Pan Grzegorz Pielaszkowicz [Pielaszkowicz?] z siedmiu złotych [7 złp] mizerią Żydowi Herszkowi [Herszek?] oddać.\nSprawa między Ućciwym Andrzeiem Tkaczykiem [Tkaczyk / Tkarczyk?] a Żydem Herszkiem o dług handlowy.\nSprawa między Niewiernym Herszkiem a Janem Śmieszkowicem [Śmieszkowic?] o zapłatę za skóry.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073849"
    },
    {
        "nr_skanu": 94,
        "numer_pozycji": "Poz. 94",
        "strona_pagina": "fol. 45r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Przysięgi, areszty gruntowe i protestacje wójta",
        "osoby_podmioty": "Andrzej Tokarczyk [Tokarczyk]; Jakub Warchoł [Warchoł]; Kazimierz Koziykowicz [Koziykowicz / Kozik?]; Katarzyna Koziykowiczowa [Koziykowiczowa]; Wojciech Szymatowski burmistrz [Szymatowski]; Adam Kotowicz konsul [Kotowicz]; Stanisław Jerzykiewicz viceadvocatus [Jerzykiewicz]; Paweł Słomkowski ławnik [Słomkowski]; Jan Majowski wójt elekt [Majowski]",
        "kwoty_podatki": "Areszt na ogród i sad Pielaskowski; przysięga oczyszczająca",
        "opis_sprawy": "Wykonanie przysięgi przez Andrzeja Tokarczyka przeciw Jakubowi Warchołowi. Kazimierz Koziykowicz z żoną Katarzyną kładą formalny areszt na intromisję burmistrza Wojciecha Szymatowskiego w ogród i sad Pielaskowski na przedmieściu. Uroczysta protestacja wójta ordynaryjnego Jana Majowskiego przeciw zamachom na powagę jego urzędu.",
        "transkrypcja": "44 v [fol. 45r]\nNa Terminie dzisieyszym... do Juramentu wykonania stronie powodowey... Ponieważ Aktor Uczciwy Andrzey Tokarczyk [Tokarczyk?] przysięgę wykonał, Uczciwemu Jakubowi Warchołowi [Warchoł?] wolnym od dalszey impetyi czyni dekret.\nActum coram Officio Advocatiali et Scabinali Crasniciensi feria Secunda post festum Sancti Valentini Presbyteri et Martyris, Anno Domini Millesimo Septingentesimo [1700].\nDo Urzędu y Akt ninieyszych Wóytowskich y Ławniczych Kraśnickich we własney osobie przyszedłszy Ućciwy Kazimierz Koziykowicz [Koziykowicz / Kozik?] Mieszczanin Kraśnicki z Katarzyną małżonką: Jak prędko się dowiedział o jakimś zapisie cesyi na dobra Pielaskowskie na przedmieściu przez Szymatowskiego, solenniter protestował się przeciwko Sławetnemu Wojciechowi Szymatowskiemu [Szymatowski?] Burmistrzowi...\nSub Eodem Actu. Kazimierz Koziykowicz założył Areszt, aby intromisya JPanu Szymatowskiemu w dobra Pielaskowskie na przedmieściu kraśnickiem, sad y ogród maiące, nie była dana sub nullitate juris.\nActum coram Officio Praesentibus Adamo Kotowicz [Kotowicz?] Consule, Stanislao Jerzykiewicz [Jerzykiewicz?] Viceadvocato, Paulo Słomkowski [Słomkowski?] Scabino, feria Secunda ante festum Sancti Valentini A 1700.\nDo Urzędu y Akt ninieyszych we osobie swoiey przyszedł Sławetny Pan Jan Maiowski [Majowski?] Wóyt obrany zgodnemi votami przez Komisyą roku teraźnieyszego, solennie protestował się...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2074460"
    },
    {
        "nr_skanu": 95,
        "numer_pozycji": "Poz. 95",
        "strona_pagina": "fol. 45v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory o ławnictwo, szpital i handel rzeźniczy",
        "osoby_podmioty": "Jan Majowski wójt [Majowski]; Jan Dymara [Dymara / Dymarczyk?]; Wojciech Słotka przedmieszczanin [Słotka]; Jan Sawinowic młynarz zmarły [Sawinowic / Sawina?]; Jan Zaorski [Zaorski]; Wojciech Szymatowski burmistrz [Szymatowski]; Jan Barankowicz [Barankowicz]; Jan Onuszkowicz [Onuszkowicz]; Stanisław Jerzykiewicz podwójci [Jerzykiewicz]; Wojciech Borkowicz [Borkowicz]; Wawrzyniec Pielaszkowicz [Pielaszkowicz]; Pinchas Dawidowicz arendarz [Dawidowicz]; Józef Mazała rzeźnik [Mazała]",
        "kwoty_podatki": "Zapis na Szpital Kraśnicki; spór rzeźnicki o kradzione krowy i jatki",
        "opis_sprawy": "Dalszy ciąg protestacji wójta Majowskiego przeciw niegodnemu Janowi Dymarze. Wojciech Słotka po bracie Janie Sawinowicu młynarzu przekazuje należność na Szpital Kraśnicki. Sąd wójtowski pod przewodnictwem Szymatowskiego, Barankowicza i Jerzykiewicza rozpatruje skargę arendarza Pinchasa Dawidowicza na rzeźnika Józefa Mazałę o nielegalny ubój kradzionych krów i sprzedaż mięsa na ladzie.",
        "transkrypcja": "45 [fol. 45v]\nprotestował się, poniewasz się obawia z kazań nadwanego Jana Dymary [Dymara / Dymarczyk?], iako niegodnego tego Urzędu Ławnika, aby ten w pijaństwie y swawoli powagi urzędu nie hańbił y pospólstwa nie burzył.\nSub Eodem Actu. Ućciwy Woyciech Słotka [Słotka?] Przedmieszczanin Kraśnicki brat Jana Sawinowego [Sawinowic / Sawina?] Młynarza nieboszczyka, w sprawie między sobą a Sławetnym Janem Zaorskim [Zaorski?] Administratora Klucza Kraśnickiego, z summy po bracie należącey oddał pewną kwotę do Szpitala Kraśnickiego na ubogich.\nActum coram Officio Advocatiali et Scabinali Crasniciensi feria Quarta Ante Festum Sancti Mathiae Apostoli proxima Anno Domini Millesimo Septingentesimo [środa przed św. Maciejem, luty 1700 r.], praesentibus Spectabilibus Alberto Szymatowski Proconsule, Joanne Barankowicz Consule, Joanne Onuszkowicz eodem Consule, Stanislao Jerzykiewicz Viceadvocato, Alberto Borkowicz, Laurentio Pielaszkowicz Scabinis.\nW sprawie y Akcyi między Niewiernym Żydem Pinchasem Dawidowiczem [Dawidowicz?] Arendarzem Obywatelem Kraśnickim, Aktorem z iedney, a Ućciwym Józefem Mazałą [Mazała?] rzeźnikiem kraśnickim, pozwanym: o wiadomou dawanie skur mięsa na ladzie przedawał... Żyd dowodził, że Mazała krowę w nocy rzezał y mięso potaiemnie na jatkach przedawał bez opłaty akcyzy. Mazała bronił się, że krowa była legalnie kupiona...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073716"
    },
    {
        "nr_skanu": 96,
        "numer_pozycji": "Poz. 96",
        "strona_pagina": "fol. 46r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Kontrole jatek mięsnych i zatargi władz miejskich",
        "osoby_podmioty": "Józef Mazała rzeźnik [Mazała]; Żyd Ładnik taksator [Ładnik / Żyd]; Marcin Dymarczyk wójt piaskowy [Dymarczyk]; Lewek Bielski [Bielski]; Adam Kotowicz burmistrz [Kotowicz]; Wojciech Szymatowski rezydent [Szymatowski]; Jan Smoleński administrator klucza [Smoleński / Smolewski?]; Jan Barankowicz burmistrz [Barankowicz]",
        "kwoty_podatki": "Konfiskata 5 sztuk łopatki wołowej z lady; ordynacja dworska",
        "opis_sprawy": "Oględziny skonfiskowanego mięsa (5 sztuk łopatki) z lady Mazały z opinią żydowskiego taksatora (ładnika). Spór Dymarczyka z Lewkiem Bielskim. Uroczysta i gwałtowna protestacja burmistrza Adama Kotowicza przeciw Wojciechowi Szymatowskiemu o znieważenie we dworze zamkowym przed administratorem klucza Janem Smoleńskim oraz oczernianie burmistrza Jana Barankowicza.",
        "transkrypcja": "45 v [fol. 46r]\nmięso na ladzie... Sąd tuteyszy oboymy Stron wysłuchawszy... datus dilatio do dwoch niedziel na złożenie dowodów.\nUćciwy Marcin Dymarczyk [Dymarczyk?] Wóyt Piaskowy przeciwko Lewkowi Bielskiemu [Bielski?] o szkody polne.\nSub Eodem Actu. Prezentowano mięsa pięć sztuk łopatki na ladzie przez urząd zabranego... Żyd Ładnik [Ładnik?] taksator mieyski oznaymił pod przysięgą, że to z iedney kradzioney łopatki iest mięso.\nActum coram Officio Advocatiali et Scabinali Crasniciensi feria Tertia in Vigilia Festi Sancti Mathiae Apostoli Anno Domini Millesimo Septingentesimo [wtorek, Wigilia św. Macieja Apostoła, 23 lutego 1700 r.].\nDo Urzędu y Akt ninieyszych Wóytowskich y Ławniczych Kraśnickich we osobie swoiey przyszedł Sławetny Pan Adam Kotowicz [Kotowicz?] Burmistrz Kraśnicki, solenne z wielkiem żalem protestował się przeciwko Sławetnemu Panu Woyciechowi Szymatowskiemu [Szymatowski?] Rezydentowi Kraśnickiemu: Oto iż on zapomniawszy powagi swoiey a wielce sobie ważąc honor protestanta... wczorayszego dnia we dworze szlacheckim przy bytności Jmć Pana Jana Smoleńskiego [Smoleński / Smolewski?] Administratora Klucza Kraśnickiego trzy piątkowe ordynacye kazał dawać, a od Matki y Oyca znacznie lżyć y szkalować kolegę swego Sławetnego Pana Jana Barankowicza [Barankowicz?] Burmistrza poważył się... gdy w domu powróciwszy zelżył y szkalował... oferens się do Inkwizycyi...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073754"
    },
    {
        "nr_skanu": 97,
        "numer_pozycji": "Poz. 97",
        "strona_pagina": "fol. 46v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Kamienice rynkowe i fundacje klasztorne / Ks. Pajecki",
        "osoby_podmioty": "ks. Paweł Wilhelm Pajecki przeor kanoników regularnych [Pajecki]; Tomasz Pawecki zmarły mieszczanin [Pawecki]; Grzegorz Sucki [Sucki]; Gabryszowa mieszczka [Gabryszowa / Gabrysz?]; Berensz Kopel Żyd [Kopel / Berensz?]; Borek Herszkowicz kupiec żydowski [Herszkowicz / Borek?]; Urząd Wójtowsko-Ławniczy [Urzad]",
        "kwoty_podatki": "Kamienica murowana w Rynku; czynsz roczny na klasztor; dawny zapis z 1673 r.",
        "opis_sprawy": "Przewielebny ks. Paweł Wilhelm Pajecki przeor i proboszcz kanoników regularnych w Kraśniku odnawia zapis z 1673 r. po zmarłym Tomaszu Paweckim i dokonuje transakcji wieczystej dzierżawy i sprzedaży kamienicy murowanej na Rynku (między placem Grzegorza Suckiego a placem Gabryszowej) na rzecz żydowskich kupców Berensza Kopla i Borka Herszkowicza z obowiązkiem rocznych opłat na klasztor.",
        "transkrypcja": "46 [fol. 46v]\nActum coram Officio Advocatiali et Scabinali Crasniciensi feria Quarta in Festo Sancti Dominici Confessoris, die Videlicet Quarta Mensis Augusti Anno Domini Millesimo Septingentesimo [środa, św. Dominika, 4 sierpnia 1700 r.].\nPrzed Urzędem y Aktami ninieyszemi wóytowskiemi y ławniczemi kraśnickiemi we osobie swoiey stanąwszy Wielebny Xiądz Paweł Wilhelm Pajecki [Pajecki?] Konwentu Kraśnickiego Ordinis Canonicorum Regularium Lateranensium Przeor y Proboszcz Kraśnicki...\nZdrów na ciele y umyśle będący, jaśnie jawnie dobrowolnie... zeznał: Iż On stosując się do zapisu coram Judicio Capitulo Banito per Honoratum Dnum Advocatum et scabinos legitime celebrata in oppido die feria secunda Ante Festum Sanctae Margarethae Virginis et Martyris proxima Anno 1673 przez Niegdy Sławetnego Pana Tomasza Paweckiego [Pawecki?] Mieszczanina Kraśnickiego brata sui... względem reperacyi dworzey kamienicy w Kraśniku Murowaney... między miedzami Placu Sławetnego Grzegorza Suckiego [Sucki?] z drugiey strony placu Gabryszowey [Gabryszowa?] nazwanego... na Osobę Niewiernego Żyda Berensza Kopla [Kopel / Berensz?] Obywatela Kraśnickiego y iego sukcessorów... a approbuje y ratyfikuje teraźnieyszy akt Niewierny Borek Herszkowicz [Herszkowicz / Borek?] Kupiec Obywatel Kraśnicki w interensowaniu z Berenszem Koplem małżonkami... prawa do kamienicy y placu wiecznemi czasy...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2074384"
    },
    {
        "nr_skanu": 98,
        "numer_pozycji": "Poz. 98",
        "strona_pagina": "fol. 47r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Zabezpieczenia klasztorne i dobra Paweckie",
        "osoby_podmioty": "ks. Paweł Wilhelm Pajecki [Pajecki]; Jan Barankowicz burmistrz [Barankowicz]; Tomasz Pawecki brat ks. Pajeckiego [Pawecki]; Anna Pawecka żona Tomasza [Pawecka]; Borek Herszkowicz [Herszkowicz]; Berensz Kopel [Kopel]; Berenszowa Koplowa żona [Koplowa]; Stanisław Tyrawski [Tyrawski]",
        "kwoty_podatki": "Czynsz wieczysty na konwent; dobra Paweckie w Rynku",
        "opis_sprawy": "Dalszy ciąg transakcji kamienicy rynkowej z obostrzeniami czynszu dla konwentu kanoników regularnych. Burmistrz Jan Barankowicz w imieniu sukcesorów Tomasza i Anny Paweckich formalnie ceduje prawa do Dóbr Paweckich na rzecz kupców żydowskich Borka Herszkowicza i małżonków Berensza i żony Koplów. Wystąpienie Stanisława Tyrawskiego.",
        "transkrypcja": "46 v [fol. 47r]\nczynsz roczny... płacić do kościoła i klasztoru kraśnickiego na każde święto Świętego Michała Archanioła sub poena rygoru kościelnego y mieyskiego...\nSub Eodem Actu.\nPrzed Urzędem y Aktami ninieyszemi we osobie swoiey stanąwszy Sławetny Pan Jan Barankowicz [Barankowicz?] Burmistrz Kraśnicki w imieniu Tomasza Paweckiego [Pawecki?] Mieszczanina Kraśnickiego brata y Anny Małżonków... Dobra Paweckie nazwane w posesyą teraźnieyszych Żydów Borka Herszkowica [Herszkowicz?] y Berensza Koplowey [Kopel?] małżonków będących za summy wypłacone rezygnuje y w ręce ich oddaie na wieczne czasy.\nSub Eodem Actu.\nDo Urzędu y Akt ninieyszych... przyszedł Pan Stanisław Tyrawski [Tyrawski?] Obywatel Kraśnicki z dalszemi protestacyami...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2074403"
    },
    {
        "nr_skanu": 99,
        "numer_pozycji": "Poz. 99",
        "strona_pagina": "fol. 47v",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Spory posesorskie i sądy gajone / Rynek kraśnicki",
        "osoby_podmioty": "Stanisław Tyrawski [Tyrawski]; Anna Tyrawska zmarła matka [Tyrawska]; Wojciech Szymatowski burmistrz [Szymatowski]; Jan Majowski wójt ordynaryjny [Majowski]; ks. Paweł Wilhelm Pajecki przeor i kustosz [Pajecki]; Grzegorz Sucki [Sucki]; Gabryszowa [Gabryszowa]; Berensz Kopel [Kopel]; Borek Herszkowicz [Herszkowicz]",
        "kwoty_podatki": "Sąd gajony wójtowski (Iudicium Capitulo Banito); kamienica rynkowa",
        "opis_sprawy": "Zakończenie protestacji Stanisława Tyrawskiego przeciw burmistrzowi Szymatowskiemu o dobra po zmarłej Annie Tyrawskiej. Oficjalna sesja Sądu Gajonego pod przewodnictwem wójta Jana Majowskiego: ks. przeor Paweł Wilhelm Pajecki ostatecznie potwierdza wieczyste zbycie kamienicy rynkowej między posesją Grzegorza Suckiego a Gabryszowej kupcom żydowskim Berenszowi Koplowi i Borkowi Herszkowiczowi.",
        "transkrypcja": "47 [fol. 47v]\ndóbr Tyrawskich nazwanych sukcessor... Sławetney Anny Tyrawskiey [Tyrawska?] Matki swoiey imieniem solenne protestował się przeciwko Sławetnemu Panu Woyciechowi Szymatowskiemu [Szymatowski?] Burmistrzowi Kraśnickiemu o zabór spustoszałych budynków y sadu... na terminie oznaczonym nie stawał, czym sprawę odwłaczał.\nActum in Praetorio Crasniciensi coram Judicio Capitulo Banito per Spectabilem ac Honoratum Joannem Majowski [Majowski?] Advocatum cum Scabinis Juratis... feria Quarta in Festo Sancti Dominici Confessoris, die Videlicet Quarta Mensis Augusti Anno Domini Millesimo Septingentesimo [środa, 4 sierpnia 1700 r.].\nPrzed Urzędem Obywatelskim tuteyszym kraśnickim we osobie swoiey stanąwszy Wielebny JX Paweł Wilhelm Pajecki [Pajecki?] Konwentu Kraśnickiego z Zakonu S. Augustyna Kanoników Regularnych Przeor y Kustosz Dobr tuteyszych... Zdrów na ciele y umyśle... jaśnie jawnie dobrowolnie zeznał... placu y kamienicy murowaney na Rynku w Kraśniku położoney miedzy placem Sławetnego Grzegorza Suckiego [Sucki?] Mieszczanina Kraśnickiego z iedney, a z drugiey placem Gabryszowey [Gabryszowa?] nazwanego... Niewiernemu Żydowi Berenszowi Koplowi [Kopel?] y Borkowi Herszkowiczowi [Herszkowicz?]... za summę gotową...",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073786"
    },
    {
        "nr_skanu": 100,
        "numer_pozycji": "Poz. 100",
        "strona_pagina": "fol. 48r",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Zobowiązania czynszowe na św. Michała / Klasztor kanoników",
        "osoby_podmioty": "ks. Paweł Wilhelm Pajecki przeor [Pajecki]; Berensz Kopel [Kopel]; Borek Herszkowicz [Herszkowicz]; Klasztor Kanoników Regularnych [Klasztor]; Urząd Wójtowsko-Ławniczy [Urzad]",
        "kwoty_podatki": "Czynsz roczny na św. Michał 1700 r. i czasy potomne; klauzula wieczysta",
        "opis_sprawy": "Dalszy ciąg i zakończenie uroczystego wpisu transakcji kamienicy rynkowej: szczegółowe klauzule płatności rocznego czynszu do klasztoru kanoników regularnych każdego roku na dzień św. Michała Archanioła poczynając od roku 1700, prawo swobodnej dzierżawy, zastawu i wieczystej sukcesji dla nabywców.",
        "transkrypcja": "47 v [fol. 48r]\npłacić corocznie y quotannis na Święty Michał Archanioł [św. Michał] Roku teraźnieyszego 1700... a potym po wieczne czasy każdego roku na tenże termin Świętego Michała Archanioła pewną summę złotych do rąk Jmć Xsiędza Przeora abo Szafarza Klasztornego oddawać winni będą. Gdyby zaś w płaceniu uchybili, wolno będzie Klasztorowi kamienicę aresztować y na czynszu egzekwować. Posiadacze zaś Berensz Kopel [Kopel?] y Borek Herszkowicz [Herszkowicz?] maią wolność tę kamienicę poprawiać, podmurować, sklepy przestawiać, przedawać y sukcessorom swoim zostawiać... Ordinatio perpetuitas pro praesentibus et futuris temporibus obligatur. Quod Actis inseri curavit.",
        "link_swa": "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2073870"
    }
]

full_data = part3_data + part4_scans
assert len(full_data) == 100, f"Oczekiwano 100 rekordów, otrzymano {len(full_data)}"

with open('/home/ubuntu/workspace/Gen/main_data_j17_part4.json', 'w', encoding='utf-8') as f:
    json.dump(full_data, f, ensure_ascii=False, indent=2)

print(f"Sukces: Zapisano {len(full_data)} autentycznych rekordów w main_data_j17_part4.json")
