# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j17_part8.json', 'r', encoding='utf-8') as f:
    part8_data = json.load(f)

UNIT_LINK = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2065801"

part9_scans = [
    {
        "nr_skanu": 201,
        "numer_pozycji": "Poz. 201",
        "strona_pagina": "fol. 97r (97)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Zeznania o kradzieży i chmielu oraz spór Lenartki z Pukliną",
        "osoby_podmioty": "Matyasz Tkaczyk [Tkaczyk]; Regina Krawcowa [Krawcowa / Żabowska?]; Marcin Hapak [Hapak]; Krystyna Lenartka [Lenartka]; Jan Lenart [Lenart]; Krystyna Puklina [Puklina]; Matyasz Kępa [Kępa]; Zofia Katarzynowa [Katarzynowa]; Szymon Kępka [Kępa]",
        "kwoty_podatki": "15 złp i 6 łyżek w sporze Lenartki z Pukliną; 1 korzec chmielu w sporze braci Kępów",
        "opis_sprawy": "Sesja z 1 XII 1700 r.: (1) zeznanie Reginy Krawcowej z instancji Matyasza Tkaczyka o pobycie w domu Tkaczyka, młóceniu przez Marcina Hapaka i rozmowach o mące, torbie, serze i soli; (2) odroczenie sprawy Krystyny Lenartkowej z wdową Krystyną Pukliną o zniewagę, 15 złp, 6 łyżek, porwanie syna i skoszenie ziela; (3) zeznanie Zofii Katarzynowej z instancji Matyasza Kępy o chmielu brata Szymona Kępki; (4) odroczenie procesu braci Kępów o korzec chmielu.",
        "transkrypcja": "97\nSub eodem Actu\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quarta in Crastino festi Sancti Andreae Apostoli Anno Domini Millesimo Septingentesimo [1 XII 1700 r.].\n\nEx Instantia Honesti Mathiae Tkaczyk [Tkaczyk] Laboriosa Regina Krawcowa [Krawcowa / Żabowska?] vagabunda persona Recognovit Bywszy u Matyasza Tkaczyka przedmieyscie Jesieni trzech dni dwie pościele ułacz w domu iego, Marcina Hapaka [Hapak] razem zastała robiącego w stodole młócącego w tym [?] przyszła surka z Marcina mówił Kino nie tam mnie Gospodyni kazała do izdebki niema siemia nie tam poszedłszy mówił żony z Hapakiem że iednego więcey niż korce Hapak rzekł to dostanie bo to miał na kasisnie w stało go nad koniec czwarteck. On rzekł meystam skąd wzdywał torby skądnie to ubiał rzekł miłalegiko nie wiedzące o tym rzekłam o to mniey po rzekł że w domnie Tkaczyka [Tkawaka?] szł wszedł niebyć więcey do ta dał by mi sera sam rzekł poszła do sieni, rzekłam No niech żeś przygarnie soli y dałam mu ale mi sera nie dał.\n\nW sprawie y Akcyi miedzy Uczciwą Krystyną Lenartką [Lenartka] Uczciwego Jana Lenarta [Lenart] małżonką Aktorką o zniewagę tudzież o niedanie złotych piętnastu A Krystyną Pukliną [Puklina] wdową pozwaną o sześć łyżek długu także o porwanie syna y skoszenie ziela iż się strony o rąki przypozwały z strony zniewagi datur dilatio Inquisitionis prima Juris expedienda terminus conservatur.\n\nEx Instantia H[onesti] Mathiae Kępa [Kępa] H[onesta] Sophia Katarzynowa [Katarzynowa] zeznała Jest tymi niebożęciak Szymon Kępka [Kępa] nie płut u mnie miał nasienie chmielu że świecie nie wiem skąd bo przy swoy ogrod one.\n\nSprawa y Akcya z strony Chmielu Uszkodowania miedzy Uczciwym Matyaszem Kępką [Kępa] Aktorem a Szymonem Kępką [Kępa] ad feriam sextam datur dilatio inquisitionis po czym na twierdzenie chmielu korzec połowone terminus conservatur.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 202,
        "numer_pozycji": "Poz. 202",
        "strona_pagina": "fol. 97v (97v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Kontumacje, skarga na Maciarzyka i spory Kępów z Tkaczykiem",
        "osoby_podmioty": "Jan Barankowicz [Barankowicz]; Wojciech Dalmaczyk [Dalmaczyk]; Wojciech Dubaj [Dubaj]; Tomasz Kopeć [Kopeć]; Andrzej Panek [Panek]; Berek Moszkowic [Moszkowic]; Bartłomiej ze Zbonka [Zbonek / Zbąnek?]; Kazimierz Maciarzyk [Maciarz]; Anna Maciakowa [Maciakowa / Maciarzykowa?]; Matyasz Kępa [Kępa]; Szymon Kępka [Kępa]; Matyasz Tkaczyk [Tkaczyk]; Marcin Hapak [Hapak]",
        "kwoty_podatki": "Trzecia kontumacja Dubaja; spór o dług i wyzwiska u Berka",
        "opis_sprawy": "Dokończenie sesji z 1 XII 1700 r. (kontumacje: Dalmaczyk wobec Barankowicza, 3. kontumacja z instancji Dubaja, protestacja Tomasza Kopcia przeciw Andrzejowi Pankowi). Sesja z 3 XII 1700 r.: (1) zeznanie Bartłomieja ze Zbonka z instancji Żyda Berka o kłótni Berka z Kazimierzem Maciarzykiem o kamienie i wyzwisko od złodzieja; (2) zeznanie Anny Maciakowej na rzecz Maciarzyka; (3) dekret w sprawie Matyasza Kępy z bratem Szymonem o koszty sądowe; (4) sprawa Matyasza Tkaczyka z Hapakem.",
        "transkrypcja": "97 v\nEx Instantia F[amati] Barankowic [Barankowicz] H[onestus] Dalmaczyki [Dalmaczyk] Contumax in termino conservato ratione deductionis Obiectorum.\n\nEx Instantia Dubay [Dubaj] Mosanka [?] 3tio Contumax.\n\nSub eodem Actu.\nH[onestus] Thomas Kobiec [Kopeć] Contra Andrea Panek [Panek] ratione non satisfactionis decreto per litas protestatur.\n\nActum feria sexta post festum Sancti Andreae Apostoli Anno Dni 1700 [3 XII 1700 r.].\n\nEx Instantia Infidelis Berek [Moszkowic] Bartholomeus de Sbonek [Zbonek / Zbąnek?] recognovit Judtem u mnie kamienie z onym Żyd Berek z Maciarzykiem [Maciarz] przemawiali się słyszałem to że Maciarzyk [w tym?] rzekł zastawa złodzieiem Sic na wozie drayanowe nawrócił y rzekł wniwecz obrócił sam od nich poszedł w inną stronę a oni w drugą stronę poszli swarzeyąc się.\n\nEx parte H[onesti] Casimiri Maciarzyk [Maciarz] H[onesta] Anna Maciakowa [Maciakowa / Maciarzykowa?] Recognovit Widziałam przed zimą że Kamień Maciarzyk [Maciarz] robił onut po drodze z targu więcey nie widziałam tacto pectore Recognovit.\n\nW sprawie y Akcyi miedzy Uczciwymi Matyaszem Kępą [Kępa] Przedmieszczaninem Kraśnickim z iedney A Szymonem Kępką [Kępa] pozwanym sad ninieyszy nakazał Aby Aktor za honory rerum ad [?] w tymże dwie stronie koszty postawił honorifice się prosit Pozwanego.\n\nW sprawie y Akcyi miedzy Matyaszem Tkaczykiem [Tkaczyk] Przedmieszczaninem Kraśnickim z iedney A Hapakiem [Hapak] pozwanym in terminis ad Carceres demandatur.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 203,
        "numer_pozycji": "Poz. 203",
        "strona_pagina": "fol. 98r (98)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Wyroki przeciw Makaremu, sprawa Dalmaczyka i spłata Zdeba",
        "osoby_podmioty": "Krystyna Lenartka [Lenartka]; Krystyna Puklina [Puklina]; Wojciech Borkiewicz burmistrz [Borkiewicz]; Berek Moszkowic arendarz [Moszkowic]; Makary [Makary]; Wojciech Dalmaczyk [Dalmaczyk]; Jan Barankowicz [Barankowicz]; Stanisław Luterek [Luterek]; Bądkowski [Bądkowski / Żadkowski?]; Piotr Jagiełko [Jagiełko?]; Tomasz Zdeb [Zdeb]",
        "kwoty_podatki": "15 złp w sprawie Lenartkowej; 3 złp i 2+3 grzywny kary dla Makarego oraz przysięga na 6 złp od 15 wieprzów; złożenie 100 złp przez Zdeba",
        "opis_sprawy": "Ciąg dalszy sesji z 3 XII 1700 r.: (1) odesłanie sprawy Krystyny Lenartkowej z Pukliną o 15 złp do sądu burmistrza Borkowicza; (2) dwa dekrety dla arendarza Berka przeciw Makaremu (zapłata 3 złp w 3 dni, grzywny po 2 i 3 grzywny oraz przysięga o zatrzymanie 6 złp od 15 wieprzów); (3) sprawa Wojciecha Dalmaczyka z Janem Barankowiczem; (4) uwolnienie Stanisława Luterka od żydowskiego pozwu; (5) nakaz wydania ćwierci przez Bądkowskiego; (6) ponowne złożenie sumy 100 złp przez Tomasza Zdeba według dekretu.",
        "transkrypcja": "98\nW sprawie y Akcyi miedzy Uczciwą Lenartką [Lenartka] Aktorką a Pukliną [Puklina] wdową Ponieważ zł 15 zachodzi Sąd Borkowica [Borkiewicz] Burmistrza Kraśnickiego &c.\n\nW sprawie y Akcyi miedzy Starozakonnym Berkiem [Moszkowic] Arendarzem Kontraktu Juteiszego Aktorem o zniewagę y zatrzymanie [pieniędzy?] od wieprzów biła aby do rąk zł trzy oddał w niedziel dni trzy a kontynuować grzywien dwie stronie y sądowi oddał Makary [Makary] &c.\n\nSub Eodem Actu.\nAby Makary [Makary] dał grzywien trzy, parti et officio per medium iuxta eadem poenam in negotio principali będący [?] ad praestandum Juramentum względem zatrzymania złotych sześciu od wieprzów 15 ab ultima quietatione koszta prawne.\n\nSub Eodem Actu.\nW sprawie y Akcyi miedzy Uczciwym Wojciechem Dalmaczykiem [Dalmaczyk] Aktorem A Sławetnym Panem Janem Barankowicem [Barankowicz] Rezydentem o pewne pretensye aby dał Aktor in Constitutione loci standi grzywny i interea na ruszenie powinien być względem sumy [złożoney?] oddać ma za tydzień aby stanęli gotowi.\n\nH[onestus] Stanislaus Luterek [Luterek] ex Instantia Certi Judaei liber pronuntiatur.\n\nPonieważ Uczciwy Bądkowski [Bądkowski / Żadkowski?] Submittował się oddać Jagiełkowi [Jagiełko?] Piotrowi ćwierć aby oddał przed zachodem słońca in instanti sub poenis Officii arbitrariis.\n\nSub eodem Actu.\nHonestus Thomas Zdeb [Zdeb] stosując się do dekretu [ferowanego?] summę złotych sto prezentował [ad?] wyrok prezentacyi et depositi sum mu odda...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 204,
        "numer_pozycji": "Poz. 204",
        "strona_pagina": "fol. 98v (98v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Akty własności i intromisja / Rękojmia za Hapaka oraz uroczysta intromisja Tomasza Zdeba w grunty po Kondupie",
        "osoby_podmioty": "Tomasz Zdeb [Zdeb]; Andrzej Panek [Panek]; Piotr Sokołowic [Sokołowic?]; Szymon Grodzik [Grodzik]; Marcin Hapak [Hapak]; Matyasz Tkaczyk [Tkaczyk]; Adam Sokołowicz burmistrz [Sokołowicz]; Wojciech Borkiewicz ławnik [Borkiewicz]; Wawrzyniec Pielaszkowicz ławnik [Pielaszkowicz]; Adam Michał Chmielowicz pisarz [Chmielowicz]; Tomasz Kopeć [Kopeć]; Tomasz Anczerek [Anczerek]; Józef Wilk [Wilk]; Jakub Wójcik [Wójcik]; Michał Rępka [Rępka]; Matyasz Młynarz [Młynarz]; Jan Kłopot [Kłopot]; Paweł Kłopot [Kłopot]; Marcin Paweł parobek [Paweł]; Jan Majowski wójt [Majowski]; Wojciech Kondup zmarły [Kondup]",
        "kwoty_podatki": "Złożenie 100 złp w depozycie i urzędowa intromisja w ćwierć roli po Kondupie na Zarzeczu Podlesiu",
        "opis_sprawy": "Dokończenie protestacji Zdeba o odmowę przyjęcia 100 złp przez stronę przeciwną i wniosek o intromisję. Sesja z 4 XII 1700 r. (św. Barbary): (1) rękojmia Piotra Sokołowica i Szymona Grodzika za Marcina Hapaka w procesie z Matyaszem Tkaczykiem; (2) zjazd urzędowy burmistrza Adama Sokołowicza, ławników Wojciecha Borkiewicza i Wawrzyńca Pielaszkowica oraz pisarza Adama Michała Chmielowicza z mandatu wójta Jana Majowskiego przy licznych sąsiadach (Kopeć, Anczerek, Wilk, Wójcik, Rępka, Kłopotowie) w celu dokonania intromisji Tomasza Zdeba w ćwierć roli po wuju Wojciechu Kondupie przeciw Andrzejowi Pankowi.",
        "transkrypcja": "98 v\n...A ponieważ zadość czyni dekretowi strona przeciwna na to ze strony powodowey oney brać niechce więc się odesłał [do?] appellacyi y oney prosekucyi nie czyni Intromissią w dobra Udzielić która własnie w urzędzie nie zafastowała.\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Sabbato ipso die festi Sanctae Barbarae Anno Dni 1700 [4 XII 1700 r.].\n\nPrzed Urzędem y Aktami w osobach swoich stanąwszy Uczciwi Piotr Sokołowic [Sokołowic?], Szymon Grodzik [Grodzik] Przedmieszczanie Kraśniccy za przyszcie na obrank [?] swoy Hapaka [Hapak] stanąć na przyszłe prawo do sądów w sprawie Uczciwego Matyasza Tkaczyka [Tkaczyk] z Rzeczyckim [?] w recesie in forma fideiussionis solita.\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Sabbato ipso die festi Sanctae Barbarae Virginis et Martyris Anno Dni 1700 [4 XII 1700 r.].\n\nDo Urzędu y Akt ninieyszych w osobach swoich przybywszy Zacnie Sławetni Panowie Adam Sokołowicz [Sokołowicz] Burmistrz, Wojciech Borkiewicz [Borkiewicz], Wawrzyniec Pielaszkowicz [Pielaszkowicz] Ławnicy przysięgli, Adam Michał Chmielowicz [Chmielowicz] Pisarz Miasta Kraśnika, przy obecności Sąsiadów Uczciwych Thomasa Kopcia [Kopeć], Thomasa Anczerka [Anczerek], Józefa Wilka [Wilk], Jakuba Woycika [Wójcik], Michała Rępki [Rępka], Matyasza Młynarza [Młynarz], Jana Jasińskiego [?], Jana Kłopota [Kłopot], syna Pawła Kłopota [Kłopot], Marcina Pawła Parobka [Paweł] dnia dzisieyszego exequując munus deputationis suae ex Mandato Zacnie Sławetnego Pana Jana Majowskiego [Majowski] Wójta Kraśnickiego ex Officiosa requisitione stosując się do dekretu miedzy Uczciwymi Thomasem Zdebem [Zdeb] po niegdy Uczciwym Wojciechu Kondupie [Kondup] wuju swoim [rodzonym?] w dobrach na Zarzeczu Podlesiu w posesyi niegdy [Kondupa?] w którey obywatel Uczciwy Andrzej Panek [Panek] Przedmieszczanin Kraśnicki [?] wydany dekretowi ponieważ Aktor zadość uczynił [a?] pozwany...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 205,
        "numer_pozycji": "Poz. 205",
        "strona_pagina": "fol. 99r (99)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Akty własności i obdukcje / Zakończenie intromisji Zdeba oraz obdukcja krwawych ran chłopów ze Słodkowa",
        "osoby_podmioty": "Tomasz Zdeb [Zdeb]; Wojciech Kondup zmarły [Kondup]; Wojciech Skatka [Skatka]; Matyasz Mozielak woźny [Mozielak / Mordelak?]; Wawrzyniec Syś [Syś / Łyś?]; Stanisław Syś [Syś / Łyś?]; Jan Pezik [Pezik / Perzyk?]; Grzegorz Jardzyk [Jardzyk / Jazdyk?]",
        "kwoty_podatki": "Prawne wprowadzenie w posiadanie (`nemine impugnante`); obdukcja licznych ran krwawych na głowie, rękach i twarzy",
        "opis_sprawy": "Dokończenie relacji z intromisji Tomasza Zdeba w ćwierć roli Kondupowską przy świadku Wojciechu Skatce oraz publiczne wywołanie w czterech rogach gruntu przez woźnego Matyasza Mozielaka (`nemine impugnante`). Sesja z 7 XII 1700 r.: protestacja i obdukcja ciężkich ran krwawych ojca Wawrzyńca i syna Stanisława Sysiów (Łysiów?), poddanych ze wsi Słodków, pobitych przez Jana Pezika i Grzegorza Jardzyka (Jazdyka?).",
        "transkrypcja": "99\n...nie założył appellacyi y oney prosekucyi nie zadał w Trybunał [Koronny?] wyżey wspomnianych żadney przeszkody niebyło. Tedy wyżey specyfikowani do oddania Intromissyi w ćwierć roli Kondupowska nazwaney miedzy miedzami z iedney strony teyże pomienionego Aktora z drugiey Wojciecha Skatki [Skatka] ze wszystkimi należytościami y dawnymi granicami należącymi drzewiny sadowey podośley [?] Intromissią realną cum pacifica possessione publicznie in Quatuor partibus tegoż gruntu alta et intelligibili voce sonora przez opatrnego Matyasza Mozielaka [Mozielak / Mordelak?] sługę mieyskiego aby kto w posessyą lub pieniędzy za pretensye tegoż po zmienionemu Aktorowi należące [?] Jurisdictioni Crasnicensi fundowali In quorum fidem conscripserunt nemine impugnante.\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Sexta in Crastino festi Sancti Nicolai Episcopi Anno Domini Millesimo Septingentesimo [7 XII 1700 r.].\n\nDo Urzędu y Akt ninieyszych w osobach swoich przybywszy Pracowici Wawrzyniec Ociec [Syś / Łyś?], Stanisław Syn Sysiowie [Syś / Łyś?] Obywatele Poddani ze wsi Słodkowa, Gruszki [?] Protestatione Contra Laboriosos Jan Pezika [Pezik / Perzyk?] y Grzegorz Jardzyka [Jardzyk / Jazdyk?] et alios Complices ratione Conculcationis suorum Adducentes [?] pokazał ociec na prawey stronie boku siny krwawy Item na prawey ręce z pryskiem stłuczony siny także na lewey stronie od łupania Item Syn pokazał na prawem uchu krwawy na drugiey stronie napuchniony pod okiem [prawym?] Item na lewey stronie warga przecięta druga spuchła stłuczona Item na lewey stronie głowy raz przecięty na półtora palca powierzchowny Item [?] z targania za włosy bolenie bardzo żebranie [?]",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 206,
        "numer_pozycji": "Poz. 206",
        "strona_pagina": "fol. 99v (99v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Akty własności / Dokończenie obdukcji ze Słodkowa oraz sprzedaż ról przez Katarzynę Kukiełkową, babę szpitalną, na rzecz Kopciów (200 złp)",
        "osoby_podmioty": "Wawrzyniec Syś [Syś / Łyś?]; Stanisław Syś [Syś / Łyś?]; Jan Pezik [Pezik / Perzyk?]; Grzegorz Jardzyk [Jardzyk / Jazdyk?]; Herszek Żyd [Herszek]; Katarzyna Kukiełkowa [Kukiełkowa]; Wawrzyniec Kukiełka zmarły [Kukiełka]; Stanisław Jerzykiewicz podwójci [Jerzykiewicz]; Tomasz Kopeć [Kopeć]; Marianna Kopciowa [Kopciowa]",
        "kwoty_podatki": "200 złp (dwie kwatery roli po 100 złp) za chałupę, stodołę i ogród po Wawrzyńcu Kukiełce",
        "opis_sprawy": "Dokończenie obdukcji ran ze Słodkowa przed domem Żyda Herszka. Sesja z 7 XII 1700 r. (wigilia Niepokalanego Poczęcia NMP): Katarzyna, wdowa po zmarłym Wawrzyńcu Kukiełce, mieszkająca obecnie jako „Baba Szpitalna” w Szpitalu św. Ducha na Przedmieściu Kraśnickim, w asyście opiekuna podwójciego Stanisława Jerzykiewicza sprzedaje i ceduje dwie kwatery roli z chałupą, stodołą i ogrodem za łączną sumę 200 złp Tomaszowi Kopcowi i Mariannie z Jasieńskich (ciąg dalszy na skanie 207).",
        "transkrypcja": "99 v\n...łopatce prawey raz krwawy [?] rany bierze Janowi Pezikowi [Pezik / Perzyk?] y przytomnemu Grzegorzowi Jardzykowi [Jardzyk / Jazdyk?] Przełożonemu y Bratu tegoż Grzegorza Smarowicza [?] że na Słodkowie przed domem Żyda Herszka [Herszek] vi et violenter zadane [?] Item opuścił syn ze rękawa y pieniędzy złotych trzy chustkę z szyi Oycu rękawicę [?] Item zł 20 [?]\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Tertia in Vigilia festi Immaculatae Conceptionis BMV Anno Domini 1700 [7 XII 1700 r.].\n\nPrzed Urzędem y Aktami Ninieyszemi Woytowskiemi y Ławniczemi Kraśnickiemi w osobie swoiey stanąwszy Uczciwa Katarzyna niegdy Uczciwego Wawrzenca Kukiełki [Kukiełka] Przedmieszczanina Kraśnickiego małżonka pozostała wdowa ad praesens w Szpitalu Świętego Ducha tu na Przedmieściu Kraśnickim Baba Szpitalna [Kukiełkowa] Mieszkająca w przytomności Sławetnego Stanisława Jerurkiewicza [Jerzykiewicz] Podwóyciego Kraśnickiego Opiekuna ad hunc Actum Uproszonego y [?] Approbowanego zdrowa na Ciele y Umyśle będąc Jawnie dobrowolnie zeznawa praesentibus y [?] modis de Jure firmissimis obligat ac resignat dobra stosując się do zapisu [?] Anno Domini 1690 [?] pomienionym Uczciwym Wawrzencem Kukiełką [Kukiełka] Przedmieszczaninem Kraśnickim za summę zł 200 w którey sprzedały kwatery roli z chałupą stodołą ogrodem tudzież [?] drugiej kwatery pustey Vigore libertacyi od Miasta...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 207,
        "numer_pozycji": "Poz. 207",
        "strona_pagina": "fol. 100r (100)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Akty własności i protestacje / Dokończenie cesji na rzecz Kopciów oraz protestacja burmistrza Szymatowskiego przeciw Starszym Synagogi",
        "osoby_podmioty": "Katarzyna Kukiełkowa [Kukiełkowa]; Tomasz Kopeć [Kopeć]; Marianna z Jasieńskich Kopciowa [Kopciowa]; Wojciech Szymatowski burmistrz [Szymatowski]; Teresa z Janaszkowiców Szymatowska [Szymatowska]; Pinchas Dawidowicz starszy synagogi [Dawidowicz]; Wigdor Markowicz starszy synagogi [Markowicz]; Abuś krawiec żydowski [Abuś]",
        "kwoty_podatki": "Dwie raty po 100 złp (łącznie 200 złp) na rzecz Kopciów; spór burmistrza ze Starszymi Synagogi",
        "opis_sprawy": "Dokończenie zapisu Katarzyny Kukiełkowej, baby szpitalnej, na rzecz Tomasza Kopcia i Marianny z Jasieńskich Kopciowej (odniesienie do zapisu z 13 II 1693 r. i dwóch rat po 100 złp). Następnie uroczysta protestacja burmistrza Wojciecha Szymatowskiego i jego żony Teresy z Janaszkowiców przeciw Starszym Synagogi Kraśnickiej: Pinchasowi Dawidowiczowi i Wigdorowi Markowiczowi oraz krawcowi Abusiowi o oszukanie i zniewagę w domu protestanta.",
        "transkrypcja": "100\n...które dobra wszystkich potrzeb swoich przy [?] na zł 200 przez [?] w [?] Anno 1690 Uczynioney między [?] wszystkich [?] sobie y nieboszczykowi mężowi swemu y sukcessorom swoim zadość uczyniła [?] wszystkich Ostatniey kwitacyi Roku 1693 die 13 Februarii uczynioney która tak z pierwszej jako y z drugiey Summy za 100 zł kwitowana w [?] między [?] obrócone odebrania Uczciwych Thomasa Kopeyka [Kopeć] Przedmieszczanina Kraśnickiego y Marianny Jasiewicowey [Kopciowa] małżonków sukcessorów własnych wiecznych prawa [?] nieprzystępne na osoby [?] y posesorów dobra pomienione [?] w lewo, testamentem żadney legacyi [?] sobie nie rezerwując Ani żadnych legatów między dobra specyfikowanych w posesyą y [?] kupców otrzymać obiecuje. Alias in forma Juris talionis quam plenissima et perfectissima ad praemissa mediante.\n\nSub eodem Actu.\nDo Urzędu y Akt ninieyszych w osobie swoiey przyszedłszy Zacnie Sławetny Pan Wojciech Szymatowski [Szymatowski] Burmistrz Kraśnicki Swoim y Zacney Pani Teresy de gente Janaszkowicowey [Szymatowska] małżonki imieniem solennie suae iterum salve protestował się przeciwko Starozakonnym Pinchasowi Dawidowiczowi [Dawidowicz], Wigdorowi Markowicowi [Markowicz] Starszym Synagogi Kraśnickiey, y Abusiowi [Abuś] Żydowi Kraśnickiemu Krawcowi, Oto iż wspomnieni Starsi Synagogi Kraśnickiey sprawiedliwości ex tunc swego deklarując protestanowi lubo by prawnie oszukaniem z protestantem postąpili dla [?] Bożnicy swojej w kłótnie tandem deprecacyą [?] w domu protestanta [?] nie zostawszy którzy [?] protestantowi ale jako [?] protestantowi, na jakieś rekowanie...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 208,
        "numer_pozycji": "Poz. 208",
        "strona_pagina": "fol. 100v (100v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo wójtowsko-ławnicze / Zeznania Luterka i Puklińskiego w sprawie Dalmaczyka oraz skarga na Tkaczyka",
        "osoby_podmioty": "Wojciech Szymatowski burmistrz [Szymatowski]; Wojciech Dalmaczyk [Dalmaczyk]; Stanisław Luterek kuśnierz [Luterek]; Jan z Podlesia [Podleski]; Kidanowa [Kidanowa / Ridanowa?]; Franciszek Pukliński [Pukliński]; Augustynowa Pielaszkowicowa [Pielaszkowicowa]; Tomasz Tkaczyk [Tkaczyk]",
        "kwoty_podatki": "Zeznania o talarach i kradzieży u Dalmaczyka; skarga o miedze i ogród",
        "opis_sprawy": "Dokończenie protestacji burmistrza Szymatowskiego. Sesja z 10 XII 1700 r.: (1) zeznanie kuśnierza Stanisława Luterka z instancji Wojciecha Dalmaczyka o słowach Jana z Podlesia na Kidanową (Ridanową?); (2) zeznanie drugiego świadka Franciszka Puklińskiego o Augustynowej Pielaszkowicowej, Kidanowej i chorobie męża pytającego o sługę; (3) protestacja Franciszka Puklińskiego przeciw Tomaszowi Tkaczykowi i jego żonie o naruszenie miedz, niewygradzanie i niszczenie płotu.",
        "transkrypcja": "100 v\n...tego bez wiadomości Protestanta czyście nie powinni radzić [?] nad aby ten [?] protestanta [?] velle.\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi feria sexta post octavam Conceptionis BMV proxima AD 1700 [10 XII 1700 r.].\n\nEx Instantia H[onesti] Alberti Dalmaczyki [Dalmaczyk] H[onestus] Stanislaus Luterek [Luterek] Pellio Civis Crasnicensis Recognovit To tylko słyszałem od Jana z Podlesia [Podleski] że wołał na Kidanową [Kidanowa / Ridanowa?] małżonką albo co by talary nie oddała pieniądze od Dalmaczyckiego [Dalmaczyk] córki. Ultra nihil.\n\n2dus testis. Franciscus Pukliński [Pukliński] Recognovit Słyszałem od Augustynowey Pielaszkowicowey [Pielaszkowicowa] iakoby Kidanowa [Kidanowa / Ridanowa?] mówiła że kiedy ksiądz z Panem Bogiem był u niey chory miała się pytać o tych pieniądzach gdy dziad odszedł marnować narzekała Na nic chłopcami woły zrać a ia o niczym nie wiem [?] słyszałem że kiedy Kidanowa [Kidanowa] kupiła tatarki że chory mąż o tym nie wiedział pytał się skąd by była powiedziała z borgowano nikt nie powiedział kto.\n\nActum coram Officio [?] H[onestus] Franciscus Pukliński [Pukliński] przeciwko Thomasowi Tkaczykowi [Tkaczyk] y iego żonie [?] o miedze między ogrodami [?] protestatur iż [?] w ogrodzie [?] ani wygradzał ale niszczył [?] przeciw płotowi [?] przed sądem [?] in hoc loco.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 209,
        "numer_pozycji": "Poz. 209",
        "strona_pagina": "fol. 101r (101)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Sesja z 13 XII 1700 r. (św. Łucji): procesy Puklińskiego, Jardzyka i Smoka",
        "osoby_podmioty": "Stanisław Dudkowicz [Dudkowicz / Dąbkowicz?]; Józef Kozak [Kozak / Rajak?]; Berek Moszkowic [Moszkowic]; Franciszek Pukliński [Pukliński]; Tomasz Nowacki [Nowacki]; Tomasz Feler [Feler?]; Wojciech Jardzyk [Jardzyk / Jazdyk?]; Jan Smok [Smok]; Grzegorz Rzeczywolek [Rzeczywolek / Rzęciewolik?]",
        "kwoty_podatki": "1 zł 10 gr do zapłaty i wadium w sprawie o płot; 1 grzywna sądowi, 2 stronie oraz zwrot sukni w sprawie Smoka",
        "opis_sprawy": "Sesja Sądu Obojnego z 13 XII 1700 r. (św. Łucji): (1) zeznanie Józefa Kozaka z instancji Stanisława Dudkowicza o wyzwiskach parobka Wojtowicza i Żyda Berka; (2) odroczenie sprawy Franciszka Puklińskiego z Tomaszem Nowackim o pobicie chłopa; (3) dekret w sprawie Tomasza Felera z Wojciechem Jardzykiem o zapłatę 1 zł 10 gr do zachodu słońca i ogrodzenie sadu; (4) skazanie Grzegorza Rzeczywolika w sprawie z Janem Smokiem o zatrzymanie sukni chłopca pastucha (1 grzywna sądowi, 2 stronie i zwrot sukni).",
        "transkrypcja": "101\nActum Coram Officio Composito Crasnicensi Feria Secunda ipso die festi Sanctae Luciae Virginis et Martyris Anno Domini Millesimo Septingentesimo [13 XII 1700 r.].\n\nEx Instantia H[onesti] Stanislai Dudkowicz [Dudkowicz / Dąbkowicz?] H[onestus] Josephus Kozak [Kozak / Rajak?] Recognovit słyszałem uradim że iednego [?] z tądzieyszy parobek od Wojtowicza [Wojtowicz] o [?] z [?] od [?] biały [?] mówiąc jakoś Berek [Moszkowic] bez złodzieja tak y tyś jesteś niecnotko.\n\nW sprawie y Akcyi miedzy Uczciwymi Franciszkiem Puklińskim [Pukliński] Aktorem z iedney A Thomasem Nowackiem [Nowacki] pozwanym o szkodę y pobicie chłopa z konia aby [?] jako się zgodziły strony miedzy sobą [?] terminus conservatur in feria 4ta proxime ventura.\n\nW sprawie y Akcyi miedzy Uczciwym Thomasem Felerem [Feler?] a Wojciechem Jardzykiem [Jardzyk / Jazdyk?] przedmieszczany aby złoty ieden y groszy dziesięć [?] do trzeciego dnia oddał ad occasum solis Vadium grzywien [?] ad servandam pacem [?] płot około sadu aby ogrodzony był terminus conservatur.\n\nW sprawie y Akcyi miedzy Uczciwymi Janem Smokiem [Smok] Aktorem A Grzegorzem Rzeczywolikiem [Rzeczywolek / Rzęciewolik?] pozwanym o zatrzymanie sukni chłopca Pastora w postawniku wziętey aby oddał grzywnę sądowi grzywny dwie stronie y suknię od [?] dwie...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 210,
        "numer_pozycji": "Poz. 210",
        "strona_pagina": "fol. 101v (101v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Sprawy Jana Smoka, rękojmia za Hapaka oraz zeznanie parobka Wojciecha z Borowa",
        "osoby_podmioty": "Jan Smok [Smok]; Matyasz Biernatek [Biernatek]; Dorota Podeszła [Podeszła?]; Kazimierz Podeszły [Podeszły?]; Matyasz Tkaczyk [Tkaczyk]; Piotr Tokarczyk [Tokarczyk]; Szymon Grodzik [Grodzik / Broddzik?]; Marcin Hapak [Hapak]; Wojciech Dalmaczyk [Dalmaczyk]; Koszykowicz [Koszykowicz]; Wojciech z Borowa [Borowski]; Brzezina [Brzezina]; Józef Wilk młynarz [Wilk]; Tomasz Wojtowicz [Wojtowicz]; Stanisław [Stanisław]",
        "kwoty_podatki": "Rękojmia za Hapaka; zeznanie parobka o półćwiartkach mąki we młynie",
        "opis_sprawy": "Dokończenie sesji z 13 XII 1700 r.: (1) nakaz dla Matyasza Biernatka stawienia chłopca w sprawie z Janem Smokiem; (2) odroczenie sprawy Smoka z Dorotą żoną Kazimierza Podeszłego o zniewagę; (3) rękojmia Piotra Tokarczyka i Szymona Grodzika za Marcina Hapaka z instancji Matyasza Tkaczyka; (4) kontumacja Koszykowicza w sprawie Dalmaczyka; (5) zeznanie 20-letniego parobka Wojciecha z Borowa o służbie u Brzeziny, u młynarza Józefa Wilka oraz u Tomasza Wojtowicza i o wynoszeniu mąki ze młyna; (6) początek protestacji Stanisława przeciw Tomaszowi Wojtowiczowi.",
        "transkrypcja": "101 v\nW sprawie y Akcyi miedzy Uczciwymi Janem Smokiem [Smok] y Matyaszem Biernatkiem [Biernatek] aby chłopca Biernatek stawił na środę przyszłą albo pieniądze oddał, sprawę [?] terminus conservatur.\n\nW sprawie y Akcyi miedzy Uczciwym Janem Smokiem [Smok] A Dorotą Uczciwego Kazimierza Podeszłego [Podeszły?] małżonką o zniewagę datur dilatio Inquisitionis.\n\nEx Instantia H[onesti] Mathiae Tkaczyk [Tkaczyk] H[onestus] Petrus Tokarczyk [Tokarczyk], Szymon Broddzik [Grodzik / Broddzik?] stali za rękojmią za Hapaka [Hapak] Sub poena marcarum duarum in eodem terminis.\n\nEx Instantia H[onesti] Dalmaczyki [Dalmaczyk] H[onestus] Koszykowicz [Koszykowicz] Contumax Aktor ratione plenariae [?]\n\nSub Eodem Actu.\nPrzed tymże Sądem Wojciech ze wsi Borowa [Borowski] lat plus minus 20 libere zeznał iż mię na zimę taką nastat do Kraśnika naprzód u Brzeziny [Brzezina] służyłem u Pawła Józefa Wilka [Wilk] młynarza służyłem półtora roku u X. Zandrowicza na folwarku od niego odszedłem więcey niż cztery niedziele [?] u Thomasa Woytowica [Wojtowicz] brałem mąkę we młynie [?] A po tym [?] kiedy [?] brałem bez drwinki od wody [?] wyjmowałem przed tymi dwoma niedzielami [?] za parobka młynarza [?] osypkę mąki nosiłem potem sam Woytowicz albo [?] jego potrzebnemu [?] którzy groch [?] dochodzili drugiego brali.\n\nSub Eodem Actu.\n[?] in hoc loco protestato [?] Honesti Stanislai [Stanisław] przeciwko [?] Thomas Woytowic [Wojtowicz]...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 211,
        "numer_pozycji": "Poz. 211",
        "strona_pagina": "fol. 102r (102)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Protestacje i skargi / Protestacje Berka przeciw Janowi Szwedowi oraz Abusia Jakubowicza o napad podczas jarmarku w Urzędowie",
        "osoby_podmioty": "Stanisław [Stanisław]; Tomasz Wojtowicz [Wojtowicz]; Berek Moszkowic [Moszkowic]; Jan Szwed [Szwed]; Abus Jakubowicz [Abuś]; Jan Rysiewicz z Wilkołaza [Rysiewicz / Krysiewicz?]",
        "kwoty_podatki": "Sprawa długu z Modliborzyc; skarga o napad podczas jarmarku w Urzędowie",
        "opis_sprawy": "Dokończenie protestacji przeciw Tomaszowi Wojtowiczowi. Protestacja Żyda Berka przeciw Janowi Szwedowi o zniewagi na targu w związku ze sprawą długu w Modliborzycach. Sesja z 16 XII 1700 r.: początek uroczystej protestacji Żyda Abusia Jakubowicza przeciw Janowi Rysiewiczowi (Krysiewiczowi?) z Wilkołaza i jego kompanom o napad i pobicie po drodze z jarmarku w Urzędowie.",
        "transkrypcja": "102\n...Wojtowicz [Wojtowicz], w piech pięć w złości swey zadane [?] które niechcąc się poddać [?] na takowe [?] tak i w tych sprawach protestatur de damnis et expensis de praesenti facto.\n\nSub eodem Actu.\nNiewierny Żyd Berek [Moszkowic] obywatel Kraśnicki protestował się przeciwko Uczciwemu Janowi Szwedowi [Szwed] iż przed [?] przyszedłszy na targę przeciwko protestującemu rzekł te słowa haniebne słowa [?] o sprawie długu u Berka Żyda Kraśnickiego który siedział w Modliborzycach [?] odebrał [?] y te słowa iemu zadane protestuje się tak o zniewagę iak y koszta praesentes.\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quinta in Crastino festi Sanctae Luciae Virginis et Martyris Anno Domini Millesimo Septingentesimo [16 XII 1700 r.].\n\nDo Urzędu y Akt ninieyszych w osobie swoiey przyszedłszy Niewierny Abus Jakubowicz [Abuś] Żyd Obywatel Kraśnicki Solennie z wielkim żalem protestował się przeciwko Pracowitym Janowi Rysiewiczowi [Rysiewicz / Krysiewicz?] Obywatelowi Wilkołaskiemu Principatowi i nieprzyjacielowi wolności [?] na koń nazwanym [?] w czwartek niedawno przeszły [?] Najświętszej Panny Maryi podczas Jarmarku w Urzędowie...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 212,
        "numer_pozycji": "Poz. 212",
        "strona_pagina": "fol. 102v (102v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Obdukcje i protestacje / Obdukcja pobicia i rabunku 15 złp na Abusiu Jakubowiczu oraz protestacja Tokarczyków przeciw Janowi Smokowi",
        "osoby_podmioty": "Abus Jakubowicz [Abuś]; Jan Rysiewicz [Rysiewicz / Krysiewicz?]; Wojciech Tokarczyk [Tokarczyk]; Katarzyna ze Smonanowskich Tokarczykowa [Tokarczykowa]; Jan Smok [Smok]",
        "kwoty_podatki": "Rabunek 15 złp i krwawe rany na głowie, rękach i plecach Abusia Jakubowicza",
        "opis_sprawy": "Dokończenie protestacji i obdukcji Abusia Jakubowicza o napaść na Rynku po jarmarku w Urzędowie przez Jana Rysiewicza i towarzyszy, zrabowanie 15 złp oraz zadanie ciężkich ran na głowie, obu rękach i plecach. Sesja z 14 XII 1700 r. (wtorek po św. Łucji): początek protestacji Wojciecha Tokarczyka i jego żony Katarzyny przeciw Janowi Smokowi.",
        "transkrypcja": "102 v\n...napadłszy Protestanta na Rynku kiedy Protestant szedł z chłopcem [?] dla zmienienia szeląga [?] za który złotych piętnaście pochwyciwszy zaraz na pasie [?] z kieszeni od [?] złotych [?] podanego [?] bił y gwałtem [?] szablą violentiam Iniurias protestationis verificatione Pokazał raz na środku głowy ocięty [?] pałką [?] Item [?] wszystkie [?] Item u Prawey ręki na palcu [?] Item na lewey ręce na łokciu raz siny spuchły Na ręce [?] skóra zdarta od szamotania siebie [?] na plecach [?] kijami bili y tłukli we wszystko tak o zadanie razów jako też y szkodę złotych piętnaście z któremi chłopcem oraz [?] protestanta trzymali y bił tak peremptorie do dołu przechał [?] Offerens de praemissa vindicatur Velle.\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Tertia post festum Sanctae Luciae Virginis et Martyris Anno Domini Millesimo Septingentesimo [14 XII 1700 r.].\n\nDo Urzędu y Akt ninieyszych Woytowskich y Ławniczych Kraśnickich w osobach swoich przyszedłszy Uczciwy Wojciech Tokarczyk [Tokarczyk] Przedmieszczanin Kraśnicki y Katarzyna de gente Smonanowska [Tokarczykowa / Szymanowska?] małżonkowie solennie z wielkim żalem protestowali się przeciwko Uczciwemu Janowi Smokowi [Smok] Przedmieszczaninowi...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 213,
        "numer_pozycji": "Poz. 213",
        "strona_pagina": "fol. 103r (103)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Protestacje i delegacje sądowe / Dokończenie skargi Tokarczyków na Jana Smoka oraz delegacja ławnika i pisarza do chorego",
        "osoby_podmioty": "Wojciech Tokarczyk [Tokarczyk]; Katarzyna Tokarczykowa [Tokarczykowa]; Jan Smok [Smok]; Jan Majowski wójt [Majowski]; Wojciech Borkiewicz ławnik [Borkiewicz]; Adam Michał Chmielowicz pisarz [Chmielowicz]",
        "kwoty_podatki": "Zatarg o pieniądze zabrane od matki i ojca oraz wyzwiska przed domem wójta",
        "opis_sprawy": "Dokończenie protestacji Wojciecha i Katarzyny Tokarczyków przeciw Janowi Smokowi o prześladowanie w domu wójta Jana Majowskiego, rzucanie obelg o pieniądze zabrane matce i ojcu oraz targanie za włosy i groźby. Początek relacji ławnika Wojciecha Borkowicza i pisarza Adama Michała Chmielowicza z urzędowej wizji u chorego świadka (ciąg dalszy na skanie 214).",
        "transkrypcja": "103\n...Przedmieszczaninowi Kraśnickiemu Oto iż on niepomnąc na Boga y miłość bliźniego mając przeciwko protestantom taką nienawiść y zazdrość chciał by [?] że rożnie tradukuje y szkaluje protestantów mianowicie dnia wczorayszego Aktey Protestacyi przeciwnego samego Protestanta w domu Zacnie Sławetnego Pana Jana Majowskiego [Majowski] Wójta Kraśnickiego po swoich potrzebach będącego, Umyślnie pod pretextem przepraszania onego zaczepia [?] zatrzymania mowy zelżywemi, poważył się Angariować [?] nefanda słowa [?] ty Ałdynu rozgadywacie pieniądze coś je w czwartek zarzucił poniebożęciu coś zabrał od Matki od Oyca żądając z tym się nie kontentował jako y dawnymi tradukcyami szkalowaniem przed ludźmi [?] do bicia się porywać do głowy protestanta za które by był de facto złości swey dokonał [?] przed protestantem gdyby go było nie pohamowano [?] mało [?] tako o wróżenie sobie [?] na zdrowie szkodzić tem słowy nie wydziesz ty z moich rąk [?] zabrzękając [?] którędy by jakie protestanta spotkać miał [?] tylko z odpowiedzi pomienionego Jana Smoka [Smok] za [?] swego nienawistnego [?] aby ten protestacya salvam [?]\n\nDo Urzędu y Akt ninieyszych w osobie swoiey przyszedłszy Sławetny Pan Wojciech Borkowicz [Borkiewicz] Ławnik, Adam Michał Chmielowicz [Chmielowicz]...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 214,
        "numer_pozycji": "Poz. 214",
        "strona_pagina": "fol. 103v (103v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo i relacje urzędowe / Przesłuchanie chorego Matyasza Kidania w sprawie Dalmaczyka oraz sesje z 15 i 17 XII 1700 r.",
        "osoby_podmioty": "Wojciech Borkiewicz ławnik [Borkiewicz]; Adam Michał Chmielowicz pisarz [Chmielowicz]; Matyasz Kidań [Kidań / Ridań?]; Wojciech Dalmaczyk [Dalmaczyk]; Agnieszka Barankowicowa [Barankowicowa]; Stanisław Dudkowicz [Dudkowicz]; Wawrzyniec Tokarczyk [Tokarczyk]; Tomasz Wojtowicz [Wojtowicz]; Matyasz Tkaczyk [Tkaczyk]",
        "kwoty_podatki": "Zeznanie chorego świadka o tatarkach, pieczywie i pieniądzach w procesie Dalmaczyka",
        "opis_sprawy": "Relacja ławnika Wojciecha Borkowicza i pisarza Adama Michała Chmielowicza z przesłuchania chorego Matyasza Kidania (Ridania?) w sprawie zgubionych pieniędzy Wojciecha Dalmaczyka i Agnieszki Barankowicowej (chory potwierdził, że kupowała tatarkę i pieczywo, ale nie wiedział skąd miała pieniądze). Sesja z 15 XII 1700 r.: zeznanie Wawrzyńca Tokarczyka z instancji Stanisława Dudkowicza przeciw Tomaszowi Wojtowiczowi. Sesja z 17 XII 1700 r.: początek dekretu w sprawie Matyasza Tkaczyka z Marcinem Hapakem.",
        "transkrypcja": "103 v\n...Pisarz ex Officio Deputowani takową uczynili relacyą Iż pomienionego Aktora stronie swey upominającego chodzili w dom Uczciwego Matyasza Kidania [Kidań / Ridań?] Przedmieszczanina do onego na ciężką chorobę złożonego aby zeznał o której jest wiadomość z strony zguby pieniędzy Uczciwego Wojciecha Dalmaczyka [Dalmaczyk] która tylko zeznawała że kupowała [?] różnymi czasy Panna Agnieszka Barankowiczowa [Barankowicowa] tatarkę y sama wysprzedawała sama u niey pieczywo sprzedawała y za swoje pieniądze nie wiem u mnie jest córka Pana Dalmaczyka niech to tylko [?] służy że ociec pobit był. O niczym więcey nie wiem.\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quarta post festum Sanctae Luciae Virginis proxima AD 1700 [15 XII 1700 r.].\n\nEx Instantia Stanislai Dudkowicz [Dudkowicz] H[onestus] Wawrzyniec Tokarczyk [Tokarczyk] od Woytowicza [Wojtowicz] Thomasa Recognovit Przyszedłszy we czwartek iutro będzie byłem po potrzebie u Pani Barankowicowey [Barankowicowa], był też tam y pomieniony Stanisław Dudkowicz [Dudkowicz] w sieni tam [?] będąc na podsieniu [?] wołał słowa nieuczciwe twój ociec [?] za złodziejem chciałeś mię nawieść o to [?] nie powiedział o to [?] cierpliwie znosił Dudkowicz [?] do kamienia się porwał ale go nie uderzył, sam rzekł [?] iary wyprowadził za boż drewno tacto pectore.\n\nActum Coram Officio Composito Crasnicensi Feria Sexta post festum Sanctae Luciae Virginis et Martyris proxima AD 1700 [17 XII 1700 r.].\n\nW sprawie y Akcyi miedzy Uczciwym Matyaszem Tkaczykiem [Tkaczyk]...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 215,
        "numer_pozycji": "Poz. 215",
        "strona_pagina": "fol. 104r (104)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Wyrok chłosty na Marcina Hapaka oraz wyrok na wójta pastewnego Biernatka i chłopca pastucha",
        "osoby_podmioty": "Matyasz Tkaczyk [Tkaczyk]; Marcin Hapak [Hapak]; Jan Smok [Smok]; Matyasz Biernatek wójt pastewny [Biernatek / Rzadko?]; Szymon Broddzik [Grodzik / Broddzik?]",
        "kwoty_podatki": "Skazanie Hapaka na publiczne plagi; 3 grzywny oraz 7 grzywien dla sądu w sprawie Biernatka i publiczna chłosta pastucha",
        "opis_sprawy": "Sesja z 17 XII 1700 r.: (1) dokończenie dekretu w sprawie Matyasza Tkaczyka przeciw Marcinowi Hapakowi, który złamał rękojmię i zbiegł przed wyrokiem — skazany zaocznie na publiczną chłostę (`publicae plagis`); (2) wyrok w sprawie Jana Smoka przeciw wójtowi pastewnemu Matyaszowi Biernatkowi (Rzadkowi?) o szkodę i pobicie: nakaz zapłaty 3 grzywien sądowi i stronie, ponadto 7 grzywien sądowi za niestawienie zgody oraz publiczna kara rózg dla chłopca pastucha.",
        "transkrypcja": "104\n...Przedmieszczaninem Aktorem a Marcinem Hapakiem [Hapak] który odstąpiwszy od rękojmi sam za sobą [?] stanąć [?] Uważając że [?] przystąpili przed [?] zeznania [?] Hapak rzeczy aż na [?] sobie [?] jako za ten swar [?] grzech powinien publicae plagis karanego być [?] interea do ucieczki skazany dekret praesenti vigore.\n\nSub eodem Actu.\nW sprawie y Akcyi miedzy Uczciwymi Janem Smokiem [Smok] Przedmieszczaninem Kraśnickim Aktorem A Matyaszem Rzadkiem alias Biernatkiem [Biernatek / Rzadko?] Woytem Pastewnym [?] oddanie [?] przez [?] od chłopca Matyasza Biernatka [Biernatek] służącego Wyznanie [?] chłopiec zeznał tudzież [?] Aktorowi skazany Matyaszowi Biernatkowi o nieoddanie [?] któremu zakazawszy [?] Chłopiec też się sam nie przyznał [?] byłby się y pytał ią od Szymona Broddzika [Grodzik / Broddzik?] oddać sam [?] znać nie dał o tym Aktorowi [?] w ucieczce wpadł z obydwu stronami [?] Jednak do łaskawszego Sąd przystąpiwszy Nakazał aby Matyasz Biernatek [Biernatek] oddał grzywien trzy per medium stronie y sądowi [?] za szkodę [?] chłopca tegoż z ratowaniem [?] także aby dał grzywien siedm do sądu [?] kontynuować. Ponieważ oddać [?] z [?] i deprecacyą bez [?] Aktorowi wypełnić dekret [?] Chłopiec publiczną karą pod pręgą karany być powinien.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 216,
        "numer_pozycji": "Poz. 216",
        "strona_pagina": "fol. 104v (104v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Przysięga w sprawie młynarza Wilka o mąkę i dalsze śledztwo w procesie Dalmaczyka",
        "osoby_podmioty": "Jan Smok [Smok]; Katarzyna Podeszła [Podeszła?]; Boguta [Boguta?]; Józef Wilk młynarz [Wilk]; Wojciech z Borowa [Borowski]; Wojciech Dalmaczyk krawiec [Dalmaczyk]; Anna Dalmaczykówna [Dalmaczykówna]; Jan Barankowicz [Barankowicz]; Agnieszka Barankowicowa [Barankowicowa]; Jan Posowalk [Posowalk?]; Matyasz Kidań [Kidań]; Maryna Pielaszkowicowa [Pielaszkowicowa]",
        "kwoty_podatki": "Przysięga o półćwiartki mąki we młynie; wezwanie świadków po Trzech Królach 1701 r.",
        "opis_sprawy": "Ciąg dalszy sesji z 17 XII 1700 r.: (1) odroczenie sprawy Jana Smoka z Katarzyną Podeszłą na świadka Bogutę; (2) rota przysięgi w sprawie młynarza Józefa Wilka przeciw parobkowi Wojciechowi z Borowa o branie mąki we młynie; (3) dekret w sprawie krawca Wojciecha Dalmaczyka (z córką Anną) przeciw Janowi i Agnieszce Barankowicom o stawienie świadków (Jana Posowalka, Matyasza Kidania i Maryny Augustynowej Pielaszkowicowej).",
        "transkrypcja": "104 v\nSprawa miedzy Uczciwym Janem Smokiem [Smok] Przedmieszczaninem Kraśnickim Aktorem o zniewagę A Katarzyną Podeszłą [Podeszła?] [?] ponieważ Aktor zabiera na świadka Bogutę [Boguta?] [?] reicitur ad feriam post Trium Regum prima Juridica terminus conservatur.\n\nW sprawie y Akcyi miedzy Uczciwym Józefem Wilkiem [Wilk] młynarzem Kraśnickim Aktorem z iedney A Wojciechem [Borowski] o przechowanie chłopca Wojciecha który mąki we młynie brał [?] bliższego do odprzysiężenia się, Pozwanego in eam Juramenti Rotam iż nie namawiałem Chłopca Wojciecha na szkodę żadną we młynie uczynioną tylko że mąki po półćwiartku brał ten chłopiec [?] na swoie stronę nie obracałem Tak mi Panie Boże dopomóż y męka Jego Święta. Ad prima Juris post festum Trium Regum.\n\nW sprawie y Akcyi miedzy Uczciwym Wojciechem Dalmaczykiem [Dalmaczyk] Krawcem Kraśnickim z żoną y córką Anną [Dalmaczykówna] Aktorem z iedney A Zacnie Sławetnym Panem Janem Barankowicem [Barankowicz] Rezydentem Kraśnickim z małżonką iego [Barankowicowa] o stawienie córki Agnieszki, Na propozycyą Aktora y replikę pozwanych Sąd ninieyszy nie skłaniając się do finalney decyzyi w tey sprawie dla lepszey auskultacyi y zrozumienia, świadków słyszących [?] do przyszłych [?] stawienia Jana Posowalka [Posowalk?], Matyasza Kidania [Kidań], y Maryny Augustynowey Pielaszkowicowey [Pielaszkowicowa] y dalszych do czego...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 217,
        "numer_pozycji": "Poz. 217",
        "strona_pagina": "fol. 105r (105)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Akty szlachecko-żydowskie / Kwitacja szlachcianki Konstancji z Zamiechowskich Wolanowskiej i Jakuba Wolanowskiego dla Starszych Synagogi",
        "osoby_podmioty": "Wojciech Dalmaczyk [Dalmaczyk]; Jan Barankowicz [Barankowicz]; Franciszek Dudkowicz [Dudkowicz]; Andrzej Mucha [Mucha]; Konstancja z Zamiechowskich Wolanowska [Wolanowska]; Franciszek Wolanowski zmarły [Wolanowski]; Jakub Wolanowski [Wolanowski]; Pinchas Dawidowicz starszy synagogi [Dawidowicz]; Wigdor Markowicz starszy synagogi [Markowicz]",
        "kwoty_podatki": "Zwrot pełnej sumy kapitałowej z prowizjami powierzonymi na Bożnicę Kraśnicką przez śp. Franciszka Wolanowskiego",
        "opis_sprawy": "Dokończenie dekretu w sprawie Dalmaczyka z Barankowiczem (termin po Trzech Królach 1701 r.). Wzmianka o Franciszku Dudkowiczu i Andrzeju Musze. Sesja z 20 XII 1700 r. (wigilia św. Tomasza Apostoła): szlachcianka Konstancja z Zamiechowskich Wolanowska, wdowa po Franciszku Wolanowskim, wraz z synem Jakubem Wolanowskim stają przed sądem miejskim kraśnickim i kwitują Starszych Synagogi Kraśnickiej (Pinchasa Dawidowicza i Wigdora Markowicza) ze spłaty kapitału wraz z prowizjami powierzonego dawniej na Bożnicę Kraśnicką.",
        "transkrypcja": "105\n...dalszego suspensę pro cognitione realitatis proferencyi y dalszey defensy pozwanych do przyszłey pełney po Trzech Królach Roku przyszłego 1701 terminum peremptorie conservando.\n\nFranckek Dudkowicz [Dudkowicz] od Gyry Łapkiewicz [Łapkiewicz?] od Muchy Andrzeia [Mucha] o stawę [?]\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Secunda in Vigilia festi Sancti Thomae Apostoli [20 XII 1700 r.].\n\nPrzed Urzędem y Aktami ninieyszemi Woytowskiemi y Ławniczemi Kraśnickiemi w osobach swoich stanąwszy Jchmość Konstancia de gente Zamiechowska [Wolanowska] niegdy świętej pamięci Jego Mci Pana Franciszka Wolanowskiego [Wolanowski] małżonka pozostała wdowa Matka y Jego Mć Pan Jakub Wolanowski [Wolanowski] z pomienioney Jey Mci Zofii [Konstancji] Zamiechowskiey spłodzony Syn zdrowi na Umyśle y Ciele swoich będąc odstępując od forum y jurysdykcyi sobie należytey do teraźnieyszego Aktu należney mnieyszey podlegając y zapisując się iawnie dobrowolnie zeznali praesentibus zeznają Iż Oni z rąk Starozakonnych Pinchasa Dawidowicza [Dawidowicz], Wygdora Markowicza [Markowicz] Starszych Synagogi Kraśnickiey summę na prowizyą przez niegdy Jego Mci Pana Franciszka Wolanowskiego [Wolanowski] na Boźnicę Kraśnicką powierzoną rzetelnie ze wszystkiemi pretensyami prowizyami do teraznieyszego czasu [?] w całości odebrali z którey Summy odebrania Jako sukcessorowie własni [?] Synagogę Kraśnicką kwitują y wolną od płacenia czynią wiecznymi czasy...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 218,
        "numer_pozycji": "Poz. 218",
        "strona_pagina": "fol. 105v (105v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Akty szlachecko-żydowskie i protestacje / Podpisy Wolanowskich oraz protestacja Berka Moszkowica o kradzież jupy w Modliborzycach",
        "osoby_podmioty": "Konstancja Wolanowska [Wolanowska]; Jakub Wolanowski [Wolanowski]; Berek Moszkowic [Moszkowic]; Jan Zmienosic [Zmienosic / Zmieroszic?]",
        "kwoty_podatki": "Skarga o kradzież jupy na jarmarku w Modliborzycach",
        "opis_sprawy": "Dokończenie kwitacji szlacheckiej dla Synagogi Kraśnickiej z własnoręcznymi podpisami Konstancji Wolanowskiej i Jakuba Wolanowskiego z 20 XII 1700 r. Sesja z 23 XII 1700 r.: protestacja Żyda Berka Moszkowica przeciw Janowi Zmienosicowi (Zmieroszicowi?) o posądzenie i kradzież jupy podczas jarmarku w Modliborzycach.",
        "transkrypcja": "105 v\n...brony od tychże Żydów y ich antecessorów dane [?] aby tak oryginały jako y kopie waloru nie miały Ponieważ się im satysfakcya od Synagogi pomienioney stała [?] od wszelkich impetycyi prawnych y nieprawnych teyże Synagodze Kraśnickiey asekurują że in quantum by się z boku chciało upominać o jakie interesa bronić powinni. Na co się dla lepszey wiary y pewności rękami swemi własnemi podpisali Działo się w Aktach Kraśnickich Woytowskich dnia 20 Miesiąca Grudnia Roku Pańskiego 1700.\nKonstancyia Wolanowska [Wolanowska]\nJakob Wolanoský [Wolanowski]\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quinta post festum Sancti Thomae Apostoli Anno Domini Millesimo Septingentesimo [23 XII 1700 r.].\n\nDo Urzędu y Akt Ninieyszych W. Niewierny Żyd Berek Moskowic [Moszkowic] Obywatel Kraśnicki z wielkim żalem protestował się przeciwko Uczciwemu Janowi Zmienosic [Zmienosic / Zmieroszic?] iż on nie słusznie do prawa pociągnął względem zadania złodziejstwa względem rzeczy pewnych temuż Zmienosicowi ukradzionych który się to pokazało do starszych Żydów Kraśnickich protestanta w koszta prawne pociąga, którego ukradzenia niecnie nieświadom [?] tylko że z przypadku podczas Jarmarku widziany w Modliborzycach na Jarmarku Jupę poszytą której [?] po tym dowiedział przyjechawszy z Jarmarku [?] obmawiać że widział podobną Jupę u tymże niecnotliwym [?] o żydowskie nie [?] nie potrzeba mu było [?] kiedy nie był [?] protestował się de damnis et litis expensis causa subsecutis et subsequendis.",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 219,
        "numer_pozycji": "Poz. 219",
        "strona_pagina": "fol. 106r (106)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone (Kodykologia: przestawiona składka) / Pierwotna propozycja Tomasza Zdeba przeciw Andrzejowi Pankowi o rolę Kondupowską",
        "osoby_podmioty": "Tomasz Zdeb [Zdeb]; Andrzej Panek [Panek]; Zofia z Wójcików Pankowa [Pankowa]; Wojciech Kondup zmarły [Kondup]",
        "kwoty_podatki": "Spór o posiadanie ćwierci roli Kondupowskiej",
        "opis_sprawy": "Kodykologicznie przestawiona składka z wcześniejszej fazy procesu (1700 r.): na terminie zawitym przed Sądem Obojnym staje Tomasz Zdeb jako powód przeciw Andrzejowi Pankowi i jego żonie Zofii z Wójcików o niesłuszną posesję ćwierci roli Kondupowskiej po zmarłym wuju Zdeba, Wojciechu Kondupie.",
        "transkrypcja": "106\nActum Coram Officio Composito Crasnicensi Feria Quarta post festum Sancti [Stanislai / Matthaei?] proxima Anno Domini Millesimo Septingentesimo [1700 r.].\n\nNa Terminie dzisieyszym zawitym stronom niżey wyrażonym ad comparendum naznaczonym.\nStawa Uczciwy Thomas Zdeb [Zdeb] Przedmieszczanin Kraśnicki Aktor przeciwko Uczciwemu Andrzejowi Pankowi [Panek] Przedmieszczaninowi sąsiadowi swemu y Zofiey de gente Woycikowey [Pankowa] małżonkom pozwanym o niesłuszną possessią dobr pewnych videlicet ćwierci roley in suo esse Kondupowska nazwaney Aktorowi po niegdy Uczciwym Wojciechu Kondupie [Kondup] Przedmieszczaninie Kraśnickim wuiju rodzonym naturalnym prawem należącey nescietur quo Jure dotąd trzymanie y używanie o którą ćwierć roli cum omnibus attinentiis et pertinentiis [?] Aktor iuxta processum eo nomine [?] pozwanego [?] propter [?]",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 220,
        "numer_pozycji": "Poz. 220",
        "strona_pagina": "fol. 106v (106v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Dokończenie pozwu Tomasza Zdeba przeciw Andrzejowi Pankowi o grunty po Wojciechu Kondupie",
        "osoby_podmioty": "Tomasz Zdeb [Zdeb]; Andrzej Panek [Panek]; Zofia z Wójcików Pankowa [Pankowa]; Wojciech Kondup zmarły [Kondup]",
        "kwoty_podatki": "Żądanie ustąpienia z roli i zwrotu pożytków oraz kosztów prawnych",
        "opis_sprawy": "Dokończenie ustnej propozycji Tomasza Zdeba przed Sądem Obojnym: opis praw spadkowych po wuju Wojciechu Kondupie (bracie matki Zdeba), skarga na rujnowanie gospodarstwa przez Andrzeja Panka i żądanie pokazania tytułu prawnego do roli oraz zwrotu pożytków i kosztów.",
        "transkrypcja": "106 v\n...cową małżonków sąsiadów [?] nieprawnie [?] nie wiem jakim prawem ćwierci roley po nieboszczyku Wojciechu Kondupie [Kondup] Bracie Matki moiey rodzonym iemu moim prawem przyrodzonym mnie Aktorowi należącey dotąd używa pożytki z niey bierze [?] mnie zaś ruinuie co widząc [?] czyni iako y wszystkich dolegliwościach moich [?] a na Ratusz Mieyskie Kraśnickie opieczętował gdzież ubogi człowiek prawie sobie z nim postępować nie mało podziałem A przecie dotąd pokoju od nich mieć nie mogę Chociaż Vadia zachodzą Oni tym wszystkim zadość nie czynili Ani mi kosztów prawnych a najbardziej za szkody uczynione nie wracali y onych nie nagradzali. Upraszam tedy pokornie Sądu ninieyszego Aby wedle dylacyi dawnych w procesie [?] za [?] sprawy [?] iakąm mógł iuż w latach będąc [?] gospodarzom upominać pokazali jakim prawem przywłaszczają sobie te dobra wyżey specyfikowane A in quantum nie pokażą prawa Aby mi z nich ustąpili y z pożytku wziętego rachunek uczynili [?] gdyż ia nie żadną napaścią ale samą...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 221,
        "numer_pozycji": "Poz. 221",
        "strona_pagina": "fol. 107r (107)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Replika Andrzeja Panka (prawo po Szymonie Wójciku) i początek wyroku Sądu Obojnego",
        "osoby_podmioty": "Tomasz Zdeb [Zdeb]; Andrzej Panek [Panek]; Zofia z Wójcików Pankowa [Pankowa]; Szymon Wójcik zmarły [Wójcik]; Wojciech Kondup zmarły [Kondup]",
        "kwoty_podatki": "Nakłady na uprawę roli i podatki rolne ponoszone przez Andrzeja Panka",
        "opis_sprawy": "Dokończenie wywodu Zdeba (gotowość zrekompensowania nakładów na zasiewy). Replika pozwanego Andrzeja Panka: wszedł w dobra po zmarłym Szymonie Wójciku, ojcu swojej żony Zofii, trzymał rolę przez wiele lat, uprawiał ją i płacił podatki rolne, podczas gdy powód dawniej się nie upominał. Początek wyroku Sądu Obojnego Kraśnickiego.",
        "transkrypcja": "107\n...ale samą słusznością prawa przyrodzonego y iakom dawno upominał swoiey ojcowizny tak y teraz upominam. A ieśliby co rzetelności do miedzy ubyło po mienionego wuja mego rodzonego pokazało dla tego korzenia samego siebie gotowem recompensować. Onym prawa swego nie odstępując prosił przysądzenia dóbr o które rzecz idzie Propositione oretenus facta de praemissis latius existente.\n\nPozwana zaś strona nic trudniejszego nie wnosząca przeciwko Aktorowi tylko Alleguie że wstąpił iest w dobra o które rzecz idzie po nieboszczyku Szymonie Woyciku [Wójcik] Przedmieszczaninie tuteyszym Kraśnickim Oycu Żony swoiey iakim prawem pomieniony miedzy wyżey specyfikowany rodzic pozwanego tę ćwierć roli trzymał nie wie było się tym dziwić czemu się Aktor dawniey nie upominał. Stąd kosztów nie mało tak na uprawienie roli jako też płacenia podatków rolnych podejmować musiał replicatione de praemissis oretenus facta de praemissis latius existente.\n\nSąd ninieyszy Oboyny Kraśnicki po obszernych y długich dylacyach w sprawie miedzy Uczciwym Tomaszem Zdebikiem [Zdeb] Aktorem a Andrzeiem...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 222,
        "numer_pozycji": "Poz. 222",
        "strona_pagina": "fol. 107v (107v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Wyrok Sądu Obojnego w sprawie roli Kondupowskiej (odwołanie do akt z 1690 r.)",
        "osoby_podmioty": "Andrzej Panek [Panek]; Zofia z Wójcików Pankowa [Pankowa]; Tomasz Zdeb [Zdeb]; Wojciech Kondup zmarły [Kondup]",
        "kwoty_podatki": "Analiza dokumentów i zaniedbań od 1690 r.",
        "opis_sprawy": "Kontynuacja wyroku Sądu Obojnego: sąd przywołuje dylacje i akta sprawy z 1690 r., analizuje posiadanie roli od 40 lat oraz brak formalnej rezygnacji po stronie poprzedników, darując Zdebowi dawne zaniedbanie.",
        "transkrypcja": "107 v\n...Pankiem [Panek] y Zofią Woycikową [Pankowa] małżonkami przedmieszczany Kraśnickimi pozwanymi O niesłuszną przywłaszczenie sobie ćwierci roley tu na przedmieściu Gory nazwanym Aktorowi po niegdy Uczciwym Wojciechu Kondupie [Kondup] Przedmieszczaninie Kraśnickim wuiju rodzonym prawem naturalnym należącey Kontrowersyi stron obudwu wysłuchawszy Inkwizycie o nieczystych dóbr zachodzące dylacie w tey sprawie sub potiori Anno Millesimo Sexcentesimo Nonagesimo [1690 r.] ad Affectationem pozwanych stron uważając ponieważ Jura proueniunt non retrocedunt do teraźnieyszego czasu ponowienia sprawy pozwany za obięcie uczynił [?] iuris abusi sunt któremi negligentia, de clementia Officii praesentis darowano iest [?] a dokumentów authentycznych pierwej iakim prawem niegdy Antecessor ich nabył tey ćwierci roley z rezygnacyi nie pokazali ale jako z dawna na [?] że Aktorowi koszta nie iurydycznego nie pokazali tak y teraz zaniedbywają tylko się o swoich konsukcessorów swoich którzy nie wiedzieć gdzie się obracają czy żyją czy nie [?] od lat czterdziestu...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 223,
        "numer_pozycji": "Poz. 223",
        "strona_pagina": "fol. 108r (108)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Dalszy ciąg wyroku: długi Wojciecha Kondupa (50 złp i 10 złp) oraz cesja na rzecz Szymona Wójcika (60 złp)",
        "osoby_podmioty": "Tomasz Zdeb [Zdeb]; Andrzej Panek [Panek]; Zofia z Wójcików Pankowa [Pankowa]; Wojciech Kondup zmarły [Kondup]; Brabant [Brabant?]; Szymon Wójcik zmarły [Wójcik]",
        "kwoty_podatki": "50 złp długu Kondupa u Brabanta, 10 złp kosztów oraz 60 złp dla Szymona Wójcika",
        "opis_sprawy": "Dalszy ciąg uzasadnienia wyroku Sądu Obojnego: stwierdzenie braku pisemnej rezygnacji po stronie Szymona Wójcika (ojca Zofii Pankowej) oraz wykazanie, że zmarły Wojciech Kondup zaciągnął na tej roli dług 50 złp u Brabanta, 10 złp kosztów i odstąpił ją Szymonowi Wójcikowi za 60 złp.",
        "transkrypcja": "108\n...dwóch bronią się że bez nich nic czynić nie mogą która trudność evidentissima [?] patet [?] cierpi krzywdy swoiey że pozwani in solutionem Aktora oddać mogą Aktorowi złote wysądzone o czym proces sprawy [?] wyięte de dato et Actu [?] obloquentes opiewają Aktorowi w przeszłości czasu upominania się nie iest podległy [?] sobie strony verbaliter przyznały że się z dawna o te dobra wadzą między sobą [?] in defectu pokazania resignacyi od Antecessora Aktora przez niegdy Uczciwego Szymona Woycika [Wójcik] pozwanego Żony Oyca mego mamy [?] żadną miarą pokazali pozwani nie mogą tak też y ich sukcessorowie z konsukcessorami nie mogą się tym bronić [?] z zawiścią y gniewem przeciwko Aktorowi [?] się evidenter pokazuje że złotych polskich pięćdziesiąt niegdy Wojciech Kondup [Kondup] Przedmieszczanin Kraśnicki wuj rodzony Aktora na imię jego Brabant [Brabant?] nazwany zaciągnął po tym zaś o ten dług prawem pociągniony będąc złotych dziesięć polskich za koszta powinien był wrócić między Szymonowi Woycikowi [Wójcik] pozwanego żony Oycu co kosztuje złotych sześćdziesiąt jednak mając wzgląd na pracę poniesioną [?] używanie dóbr mogło by...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 224,
        "numer_pozycji": "Poz. 224",
        "strona_pagina": "fol. 108v (108v)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Sentencja finansowa wyroku: zasądzenie 100 złp (50 + 50 złp) dla Andrzeja Panka i intromisja Zdeba",
        "osoby_podmioty": "Tomasz Zdeb [Zdeb]; Andrzej Panek [Panek]; Zofia z Wójcików Pankowa [Pankowa]",
        "kwoty_podatki": "100 złp (50 złp płatne od razu, 50 złp w depozycie do czasu rękojmi); podatki skarbowe od św. Jana 1701 r.",
        "opis_sprawy": "Sentencja finansowa wyroku Sądu Obojnego: Tomasz Zdeb ma wypłacić Andrzejowi Pankowi za wszystkie nakłady i pretensje 100 złp (50 złp po dekrecie, a drugie 50 złp do złożenia po zapisaniu się Panka od impetycji sukcesorów), po czym otrzyma urzędową intromisję w ćwierć roli z drzewami i płotami, a od św. Jana Chrzciciela 1701 r. przejmie obowiązki podatkowe.",
        "transkrypcja": "108 v\n...chcący do ukontentowania strony przyjąć aby się pozwani nie opierali z tych dóbr o które rzecz idzie ustąpić gdyż bliższemu Aktorowi należą Nakazał Aby Aktor pozwanym za wszystkie pretensye wyliczył złotych sto polskich którą summę tak wypłacić powinien summy złotych pięćdziesiąt zanieść die ab Actu praesentis Decreti drugie zaś złotych pięćdziesiąt przy Aktorze [?] aż do zapisania się za rękojmią od impetycyi prawnych y nieprawnych pozwani nie zapiszą iak prędko się zapiszą dobra oddać wolne zarazem summę odebrać [?] którą summę do sekwestru Urzędowego złożyć powinien Aktor interea Intromissia per Officium praesens Compositum w te dobra o które rzecz idzie [?] aby tak przyszli Interesantowie pokazać się mogli gdyż obstante receptione summae po ucieczce [?] w te dobra in suis metis et limitibus ab antiquo existentibus drzewina stodołka na tey ćwierci będąca płotami grodzona. Aktor nowy posesor dopiero od święta świętego Jana Chrzciciela blisko przyszłego w przyszłym roku przypadającego Onera skarbowe...",
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 225,
        "numer_pozycji": "Poz. 225",
        "strona_pagina": "fol. 109r (109)",
        "sygnatura": "35/40/0/1/17",
        "data_rok": "1700",
        "kategoria": "Sądownictwo łączone / Koniec wyroku (wadium 100 złp) oraz wykonanie dekretu przez Tomasza Zdeba z 24 XI 1700 r.",
        "osoby_podmioty": "Tomasz Zdeb [Zdeb]; Andrzej Panek [Panek]; Zofia z Wójcików Pankowa [Pankowa]; Wojciech Kondup zmarły [Kondup]",
        "kwoty_podatki": "Wadium 100 złp `parti et officio per medium`; wykonanie dekretu 24 XI 1700 r.",
        "opis_sprawy": "Zakończenie wyroku Sądu Obojnego: zasiewy żyta ozimego należą do pozwanych, a stodoła Kondupowska ma zostać opróżniona do św. Wojciecha 1701 r.; nałożono wadium 100 złp na wypadek wznowienia sporu. Poniżej wpis z 24 XI 1700 r.: Tomasz Zdeb staje przed sądem i wykonuje dekret przeciw Andrzejowi Pankowi i Zofii z Wójcików o ćwierć roli i stodołę.",
        "transkrypcja": "109\n...bowe iakiekolwiek przechodzące żołnierskie płacić powinien, Osobno zaś na tym teraźnieyszym roku pole ozime żyto w stay troie półćwiartek jako swoie własne swoim kosztem zebrać powinien z stodołki zaś Kondupowska nazwaney na teyże ćwierci roley będącey do czasu święta Świętego Wojciecha Roku przyszłego 1701 pozwanym należącey [?] koszta prawne y nieprawne ab utrinque między stronami pretendowane umorzył [?] servando pacem sub summą pewnego wadium złotych sto parti et officio per medium [?] strona okazała [?] ponowienia [?] sub poena Banitionis et Vadio simili summae citati ad exolvendum perveniet [?] sub poena Intromissionis in bona [?] terminis Partibus in Qurando ab Actu praesentis Decreti post mediante satisfactione [?] in praesentiarum peremptorie decreti praesentis Vigore.\n\nActum Coram Officio Advocatiali et Scabinali Crasnicensi Feria Quarta Ante festum Sanctae Catharinae Virginis et Martyris die 24 9bris Anno Dni 1700 [24 XI 1700 r.].\n\nUczciwy Thomas Zdeb [Zdeb] Przedmieszczanin Kraśnicki zadość czyniąc decretowi miedzy sobą Aktorem a Andrzeiem Pankiem [Panek] przedmieszczaninem Kraśnickim y Zofią de gente Woycikową [Pankowa] małżonkami dobra ćwierć roley drzewiny y stodoły...",
        "link_swa": UNIT_LINK
    }
]

all_data = part8_data + part9_scans
for rec in all_data:
    rec["link_swa"] = UNIT_LINK

assert len(all_data) == 225, f"Oczekiwano 225 rekordów, jest {len(all_data)}"
assert [r["nr_skanu"] for r in all_data] == list(range(1, 226)), "Brak ciągłości nr_skanu 1..225!"

# Weryfikacja braku wewnętrznych wielokropków
for r in all_data[200:225]:
    tr = r["transkrypcja"]
    mid = [i for i in range(len(tr)) if tr[i:i+3] == "..." and i > 10 and i < len(tr)-10]
    assert not mid, f"Wykryto mid_ellipsis na skanie {r['nr_skanu']}: {mid}"

with open('/home/ubuntu/workspace/Gen/main_data_j17_part9.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano pomyślnie main_data_j17_part9.json: {len(all_data)} rekordów (skany 1-225, 0 mid_ellipsis).")
