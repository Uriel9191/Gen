# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/main_data_j18_part1.json', 'r', encoding='utf-8') as f:
    main_data = json.load(f)

UNIT_LINK = 'https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989891'

part2_scans = [
    {
        "nr_skanu": 26,
        "numer_pozycji": "Poz. 26",
        "strona_pagina": "fol. 11r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1655–1657 [23 VI 1657 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Zakończenie zapisu z 1655 r., adnotacja o braku rachunków w 1656 r. oraz ustanowienie opiekunów w 1657 r. (23 VI 1657 r.)",
        "osoby_podmioty": "Regina Miarowiczówna [Miarowiczówna]; Regina Butowa [Butowa] wdowa po Gabrielu Bucie; Maciej Koniega [Koniega]; Stanisław Cichoń [Cichoń / Cichon?]; Wojciech Szafrański [Szafrański] sierota; Paweł Szafrański [Szafrański] zmarły; Wojciech Olęcki [Olęcki]",
        "kwoty_podatki": "złotych 50 (czynsz z obligu)",
        "opis_sprawy": "(1) Dokończenie wpisu obligu Reginy Miarowiczówny z 1655 r.; (2) `ANNUS INCIPIT NOVUS 1656` z adnotacją `Huius anni nulla Ratio de Tutoria facta est` (brak rozliczeń opiekuńczych w roku potopu szwedzkiego); (3) `ANNUS 1657` (`Sabbato ante Festum S. Joannis Baptistae` = 23 VI 1657 r.): wyznaczenie Macieja Koniegi i Stanisława Cichonia [?] opiekunami Reginy wdowy po Gabrielu Bucie oraz Wojciecha Olęckiego opiekunem małoletniego Wojciecha Szafrańskiego, syna śp. Pawła Szafrańskiego.",
        "transkrypcja": (
            "[fol. 11r]\n"
            "wek za wyźey... do tych czasow od złotych 50... do oddania sumy capitalney... "
            "a data Obligatio ad affectationem dictorum Tutorum Actis praesentibus "
            "infertur et connotata usque ad resolutionem.\n"
            "ANNUS INCIPIT NOVUS 1656\n"
            "Huius anni nulla Ratio de Tutoria facta est.\n"
            "ANNUS MILLESIMUS SEXCENTESIMUS QUINQUAGESIMUS SEPTIMUS\n"
            "Actum Coram Officio Consulari Sabbato ante Festum S. Joannis Baptistae 1657\n"
            "Tutores dantur Viduae Gabrielowa Butowa.\n"
            "Ad postulationem Hon. Reginae Viduae Gabrielowa Butowa Civis Crasnicensis "
            "dati et assignati sunt ab Officio praesenti eidem Tutores Famatus Mathias "
            "Koniega Decanus [?] et Stanislaus Cichoń [?] Notarius...\n"
            "Famati Domini Proconsul et Consules providentes indemnitati Pupillo minorennis "
            "Alberti Szafrański post olim Paulum Szafrański Civem Crasnicensem filio "
            "derelicto in bonis ac locum Tutorem assignaverunt et constituerunt Hon. "
            "Albertum Olęcki Civem Crasnicensem..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 27,
        "numer_pozycji": "Poz. 27",
        "strona_pagina": "fol. 11v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1657–1658 [21 VII 1657 – 8 I 1658 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Opiekunowie wdów Zofii Gąskowej (21 VII 1657 r.) i Maryny Kudrelikowej (3 X 1657 r.) oraz otwarcie roku 1658 z rachunkiem po Sebastianie Decu",
        "osoby_podmioty": "Zofia Gąskowa [Gąskowa] wdowa; Augustyn Kwasowic [Kwasowic] ławnik; Jan Kasza [Kasza / Kaza?]; Maryna Kudrelikowa [Kudrelikowa] wdowa; Stanisław Rymarczyk [Rymarczyk]; Gabriel Kłopotek [Kłopotek] opiekun; Matyasz Reszka [Reszka] opiekun; Sebastian Dec [Dec] zmarły",
        "kwoty_podatki": "brak",
        "opis_sprawy": "(1) `Sabbato in Vigilia Festi S. Mariae Magdalenae 1657` (21 VII 1657 r.): wyznaczenie ławnika Augustyna Kwasowica i Jana Kaszy [Kazy?] opiekunami wdowy Zofii Gąskowej; (2) `Feria 4ta in Vigilia Festi Sancti Francisci 1657` (3 X 1657 r.): wyznaczenie przedmieszczanina Stanisława Rymarczyka opiekunem wdowy Maryny Kudrelikowej; (3) `ANNUS INCIPIT NOVUS 1658` (`sub Actu Feria 3tia post Festum Circumcisionis` = 8 I 1658 r.): otwarcie rachunku opiekunów Gabriela Kłopotka i Matyasza Reszki z dóbr zmarłego Sebastiana Deca.",
        "transkrypcja": (
            "[fol. 11v]\n"
            "Actum Coram Officio Consulari Sabbato in Vigilia Festi S. Mariae Magdalenae 1657\n"
            "Tutores dantur Viduae Gąskowa.\n"
            "Ad instantiam Hon. Viduae Zophiae Gąskowa dati et assignati sunt ab Officio "
            "Consulari Tutores Famatus Augustinus Kwasowic Scabinus Juratus Crasnicensis "
            "et Joannes Kasza [Kaza?] Curator...\n"
            "Actum Coram Officio Consulari Feria 4ta in Vigilia Festi Sancti Francisci 1657\n"
            "Tutor datus est Marinae Kudrelikowa.\n"
            "Ad postulationem Hon. Viduae Marinae Kudrelikowa anteoppidanae Crasnicensis "
            "datus et assignatus est ab Officio Consulari Tutor Hon. Stanislaus Rymarczyk "
            "anteoppidanus Crasnicensis...\n"
            "ANNUS INCIPIT NOVUS Millesimus Sexcentesimus Quinquagesimus Octavus\n"
            "Sub Actu Feria 3tia post Festum Circumcisionis\n"
            "Ratio Tutorum Hon. Gabrielis Kłopotek et Mathiae Reszka anteoppidanorum "
            "Crasnicensium de bonis olim Hon. Sebastiani Dec..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 28,
        "numer_pozycji": "Poz. 28",
        "strona_pagina": "fol. 12r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1658 [8 Stycznia 1658 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Regestr percepty z dóbr zmarłego Sebastiana Deca złożony przez Gabriela Kłopotka i Matyasza Reszkę za burmistrza Marcina Sitarskiego (1658 r.)",
        "osoby_podmioty": "Marcin Sitarski [Sitarski] burmistrz kraśnicki; Gabriel Kłopotek [Kłopotek] opiekun; Matyasz Reszka [Reszka] opiekun; Sebastian Dec [Dec] zmarły; Maria Siwia [Siwia / Siwa?]; Paweł Kłopotek [Kłopotek]; Kazimierz [Kazimierz]",
        "kwoty_podatki": "złotych 18 (żyto); złotych 50 groszy 28 (tatarka); złotych 4 (owies); złotych 7 groszy 26 (jęczmień); złotych 7 groszy 16 (pszenica); złotych 22 (krowa); złotych 2; złotych 26 groszy 20 (żyto z pola)",
        "opis_sprawy": "Regestr przychodów (percepty) z majątku zmarłego Sebastiana Deca przedłożony przed burmistrzem Marcinem Sitarskim przez opiekunów Gabriela Kłopotka i Matyasza Reszkę: sprzedaż żyta (`18 złp`), tatarki (`50 złp 28 gr`), owsa (`4 złp`), jęczmienia (`7 złp 26 gr`), grochu, pszenicy (`7 złp 16 gr`), krowy od Marii Siwiej i Pawła Kłopotka (`22 złp`), długu od Kazimierza (`2 złp`), żyta z pola (14 kop / 16 korcy za `26 złp 20 gr`), chust, kapusty i konopi.",
        "transkrypcja": (
            "[fol. 12r]\n"
            "Na zadaniu Sławetnego Pana Marcina Sitarskiego Burmistrza krasnickiego "
            "stanowszy obecnie w Urzędzie Gabriel Kłopotek y Matiasz Reszka przedmieszczanie "
            "krasniccy Opiekunowie dóbr pozostałych po nieboszczyku Sebastianie Decu "
            "przedmieszczaninie krasnickim rachunek z pomienionych dóbr przed Urzędem "
            "Radzieckim czynili.\n"
            "Naprzód pokazali Regestr Percepty takowy:\n"
            "Żyta ozimego kop 4 snopów 20 namłócili z tego korcy półsiódma, z tego "
            "przedali korcy półpięta wzięli za nie zł 18... a dwa korca oddali Żydowi "
            "krasnickiemu według Dekretu Sądu Wójtowskiego któremu był nieboszczyk Dec "
            "zadłużył. Tatarki namłócili korcy półczwarta sprzedali po gr 50 wzięli "
            "zł 50/28 [?]. Owsa kop dwie namłócili korcy półtrzecia wzięli zań zł 4. "
            "Jęczmienia kop dwie namłócili z tego korcy półtrzecia wzięli zań zł 7/26. "
            "Grochu kop 4... Pszenice kop dwie namłócili z tego korcy półtora wzięli "
            "za nię zł 7/16. Krowę przedali wzięli zł 22 którą przedała Maria Siwia "
            "y Paweł Kłopotek... od Kazimierza wzięli zł 2 które był winien... Żyta "
            "z pola wzięli kop 14 namłócili korcy 16... uczyni zł 26/20. Item w domu "
            "chusty... kapusta w bółu, konopi kilka dziesiątek..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 29,
        "numer_pozycji": "Poz. 29",
        "strona_pagina": "fol. 12v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1658",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Suma percepty (114 złp 6,5 gr) oraz regestr wydatków z majątku po Sebastianie Decu (1658 r.)",
        "osoby_podmioty": "Gabriel Kłopotek [Kłopotek] opiekun; Matyasz Reszka [Reszka] opiekun; Sebastian Dec [Dec] zmarły; Kotlarzowa [Kotlarzowa] wdowa; Nakiel [Nakiel / Nakło?] żyd; Marcin Sitarski [Sitarski]; Paczanowski [Paczanowski]; Sebastian Młynarczyk [Młynarczyk]; Szafraniec [Szafraniec / Szafrański?]; Matyasz Gierada [Gierada]",
        "kwoty_podatki": "złotych 114 groszy 6,5 (suma percepty); złotych 20 (za woły); złotych 7 (Sitarskiemu); złotych 30 (Paczanowskiemu); złotych 11 groszy 15 (Młynarczykowi); złotych 27 (podatki); złotych 20 (czynsz); złotych 4 (Gieradzie)",
        "opis_sprawy": "(1) Dokończenie percepty po Sebastianie Decu (sprzęty, siekiera, żelaza płużne, spalone w dachu rzeczy, woły sprzedane za `20 złp`, z zastrzeżeniem Kotlarzowej wdowy) — łączna suma percepty **`114 złp 6,5 gr`**; (2) regestr wydatków (`Expensa`): Żydowi Nakłowi (`12 gr`), Marcinowi Sitarskiemu długu (`7 złp`), Paczanowskiemu (`30 złp`), Sebastianowi Młynarczykowi (`11 złp 15 gr`), podatki (`27 złp`), koszenie i zwózka (`3 złp`, `1 złp 6 gr`, `2 złp 28 gr`), czynsz (`20 złp`), Szafraniowi (`80 gr` / `15 gr`), Matyaszowi Gieradzie z dekretu (`4 złp`).",
        "transkrypcja": (
            "[fol. 12v]\n"
            "przedali żelaza... siekiera... w dachu... spaliły... skrzynka spłonęła... "
            "żelaza płużne... beczka zgorzała... przy Gabryelu Kłopotku... zł 3... "
            "stodoła zgorzała... Opiekunowie... wołów parę przedali za zł 20... "
            "Kotlarzowa wdowa wzięła... iż iey winien był...\n"
            "Summa Percepti wszystkiej zł 114/6½.\n"
            "Expensę z tego pokazali takową:\n"
            "Nakłowi [Nakiel?] Żydowi krasnickiemu co ich pozywał o żyto dali gr 12. "
            "Panu Sitarskiemu długu iego który winien był nieboszczyk oddali zł 7. "
            "Item na... Paczanowskiemu zł 30 dali. Sebestyanowi Młynarczykowi długu "
            "który winien był nieboszczyk oddali zł 11/15. Podatków wszystkich wydali "
            "przez lat dwie z chałupy... zł 27. Na koszenie... oddali zł 3... od "
            "kopy... uczyni zł 1/6... na młócenie... wydali zł 2/28... za czynsz "
            "dali zł 20... na dwie lata wydali zł 1/4... za... Szafrańcowi gr 15, "
            "za kobier... Szafraniowi dali gr 80... Matyaszowi Gieradzie przez "
            "Dekret oddali długu zł 4..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 30,
        "numer_pozycji": "Poz. 30",
        "strona_pagina": "fol. 13r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1658",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Dokończenie wydatków (120 złp 17 gr) i zamknięcie rachunku po Sebastianie Decu za burmistrza Sitarskiego (1658 r.)",
        "osoby_podmioty": "Gabriel Kłopotek [Kłopotek] opiekun; Matyasz Reszka [Reszka] opiekun; Sebastian Dec [Dec] zmarły; Marcin Sitarski [Sitarski] burmistrz",
        "kwoty_podatki": "złotych 120 groszy 17 (suma expensy); złotych 6 groszy 10,5 (przewyżka wydatków); złotych 50 (kapitał długu)",
        "opis_sprawy": "Dokończenie wydatków opiekunów po Sebastianie Decu (opłaty sądowe `18 gr`, `12 gr`, pisarzowi `5 gr`, `3 złp 20 gr`) z łączną sumą expensy **`120 złp 17 gr`**, przewyżką wydatków nad dochodem **`6 złp 10,5 gr`**, zaprzysiężeniem rachunku przez opiekunów przed Sądem Radzieckim i nakazem spłaty `50 złp` kapitału burmistrzowi Marcinowi Sitarskiemu.",
        "transkrypcja": (
            "[fol. 13r]\n"
            "dali gr 13/20... od kopy... dali zł 4 ostatek długu który winien był "
            "nieboszczyk... zł 3/20 od Janczarka... pisarzowi dali gr 18... od "
            "extraktu delicyi gr 12.\n"
            "Summa Expensi facit zł 120/17.\n"
            "Gdzie nad Perceptę wydali zł 6/10½. Którego to rachunku Urząd ninieyszy "
            "Radziecki krasnicki... Opiekunowie... na tychże rzeczach... wnieśli "
            "Juramentum corporale... na summę capitalną zł 50 z interesem... Panu "
            "Sitarskiemu płacić... Opiekunowie powinni będą zaradzić y o... części "
            "okupić się postarać y dług zapłacić..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 31,
        "numer_pozycji": "Poz. 31",
        "strona_pagina": "fol. 13v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1658 [25 I – 17 VI 1658 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Wyznaczenie opiekunów dla Agnieszki Królikówny (25 I 1658 r.) oraz dla Wojciecha Buta (17 VI 1658 r.)",
        "osoby_podmioty": "Stanisław Nawrocki [Nawrocki] burmistrz; Wojciech Jerzykiewicz [Jerzykiewicz] rajca; Marcin Sitarski [Sitarski] rajca; Wojciech Kwasowic [Kwasowic] rajca; Agnieszka Królikówna [Królikówna] sierota; Jan Szczerbowic [Szczerbowic / Szczurkowic?] ławnik; Tomasz Szwajbrowic [Szwajbrowic?]; Wojciech But [But] sierota; Gabriel But [But] zmarły",
        "kwoty_podatki": "brak",
        "opis_sprawy": "(1) Zakończenie rachunku opiekunów Deca; (2) `Feria Sexta ipso die Festo Conversionis S. Pauli Apostoli 1658` (25 I 1658 r.): przed burmistrzem Stanisławem Nawrockim oraz rajcami Wojciechem Jerzykiewiczem, Marcinem Sitarskim i Wojciechem Kwasowicem wyznaczono ławnika Jana Szczerbowica [Szczurkowica?] opiekunem sieroty Agnieszki Królikówny (córki Tomasza Szwajbrowica [?]); (3) `Feria 2da ante Festum SS. Corporis Christi 1658` (17 VI 1658 r.): otwarcie wpisu opiekuńczego dla małoletniego Wojciecha Buta, syna zmarłego Gabriela Buta.",
        "transkrypcja": (
            "[fol. 13v]\n"
            "do wolny ludzkich... Panu Sitarskiemu... Ratio ad affectationem "
            "supradictorum Tutorum Actis praesentibus inserta et connotata usque ad "
            "resolutionem.\n"
            "Actum Coram Officio Consulari Feria Sexta ipso die Festo Conversionis "
            "S. Pauli Apostoli proxima Anno Domini 1658\n"
            "Tutores assignati sunt Hon. Agnetis Krolikowna.\n"
            "Famati Domini Stanislaus Nawrocki Proconsul una cum Famatis Dominis "
            "Alberto Jerzykiewicz, Martino Sitarski et Alberto Kwasowic Consulibus "
            "Residentibus providentes indemnitati Pupillae Hon. Agnetis Krolikowna... "
            "in veros ac bonos Tutores assignaverunt et constituerunt Famatum "
            "Joannem Szczurkowic [Szczerbowic?] Scabinum Juratum Crasnicensem una "
            "cum Hon. Thoma Szwajbrowic anteoppidano Crasnicensi...\n"
            "Actum Coram Officio Composito Consulari Advocati et Scabinali Jurato "
            "Crasnicensi Feria 2da ante Festum SS. Corporis Christi proxima Anno Domini "
            "Millesimo Sexcentesimo Octavo [1658]\n"
            "Tutores dati sunt minorenni Alberto But filio derelicto post olim Hon. "
            "Gabrielem But Civem Crasnicensem."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 32,
        "numer_pozycji": "Poz. 32",
        "strona_pagina": "fol. 14r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1658 [17 Czerwca 1658 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Ustanowienie Macieja Koniegi i Szymona Stolarza opiekunami Wojciecha Buta przeciw macosze Reginie Markowej (1658 r.)",
        "osoby_podmioty": "Stanisław Nawrocki [Nawrocki] burmistrz; Maciej Tarasa [Tarasa] rajca; Wojciech Kwasowic [Kwasowic] rajca; Marcin Sitarski [Sitarski] rajca; Ubald Janaszkowic [Janaszkowic] wójt; Wojciech But [But] sierota; Gabriel But [But] zmarły; Regina Markowa [Markowa] macocha; Maciej Koniega [Koniega] ławnik; Szymon Stolarz [Stolarz / Słomka?] kowal?; Agnieszka Butówna [Butówna] sierota",
        "kwoty_podatki": "brak",
        "opis_sprawy": "Przed Sądem Łączonym (burmistrz Stanisław Nawrocki, rajcy Maciej Tarasa, Wojciech Kwasowic, Marcin Sitarski, wójt Ubald Janaszkowic) z powodu pokrzywdzenia sieroty Wojciecha Buta przez macochę Reginę Markową (po śmierci ojca Gabriela Buta) wyznaczono ławnika Macieja Koniegę oraz Szymona Stolarza [Słomkę?] opiekunami obojga sierot (Wojciecha i Agnieszki Butów), z zakazem zbywania gruntów przez Reginę Markową.",
        "transkrypcja": (
            "[fol. 14r]\n"
            "Famati Domini Stanislaus Nawrocki eo tempore Proconsul Crasnicensis, "
            "Mathias Tarasa, Albertus Kwasowic et Martinus Sitarski Consules "
            "Crasnicenses una cum Famato Domino Ubaldo Janaszkowic Advocato et Judice "
            "Ordinario Jurato Crasnicensi et in praesentia Scabinorum Juratorum "
            "Crasnicensium... z powodu wielkiego pokrzywdzenia między Dziecięciem "
            "Gabryela Buta... iż Regina Markowa Matka sieroty... nie rządzi się "
            "dobra tego sieroty po oycowskim zgonie po Gabrielu Bucie... Sąd ninieyszy "
            "obopólny tak Radziecki iako y Wójtowski... z urzędu swego... nad "
            "Sławetnym Maciejem Koniegą Ławnikiem Przysięgłym krasnickim y Uczciwym "
            "Szymonem Stolarzem [Słomką?] Kowalskim przedmieszczaninem krasnickim "
            "ad tuenda et conservanda bona tam mobilia quam immobilia po nieboszczyku "
            "sieroty Agnieszki Butki... Reginae Markowa Matka tego sieroty nie "
            "chciała żadney szkody uczynić albo gruntu zbyć..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 33,
        "numer_pozycji": "Poz. 33",
        "strona_pagina": "fol. 14v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660 [22 Listopada 1660 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Otwarcie roku 1660 i początek procesu Kazimierza Baśkowskiego przeciw rajcy Marcinowi Sitarskiemu o rozliczenie opieki (22 XI 1660 r.)",
        "osoby_podmioty": "Wojciech Kwasowic [Kwasowic] burmistrz; Ubald Janaszkowic [Janaszkowic] wójt; Stanisław Nawrocki [Nawrocki] rajca; Maciej Tarasa [Tarasa] rajca; Jan Kwasowic [Kwasowic] ławnik; Błażej Kołodziejczyk [Kołodziejczyk] ławnik; Maciej Koniega [Koniega] ławnik; Grzegorz Fox [Fox] ławnik; Stanisław Pilin [Pilin] ławnik; Kazimierz Baśkowski [Baśkowski / Bąskowski?]; Marcin Sitarski [Sitarski] rajca i opiekun",
        "kwoty_podatki": "złotych 100 (prowizja)",
        "opis_sprawy": "`Feria 2da ante Festum S. Catharinae 1660` (22 XI 1660 r.): przed pełnym Sądem Łączonym (burmistrz Wojciech Kwasowic, wójt Ubald Janaszkowic, rajcy Stanisław Nawrocki i Maciej Tarasa, ławnicy Jan Kwasowic, Błażej Kołodziejczyk, Maciej Koniega, Grzegorz Fox i Stanisław Pilin) rozpoczyna się wielki proces Kazimierza Baśkowskiego przeciw rajcy Marcinowi Sitarskiemu, jego dawnemu opiekunowi, o rozliczenie majątku po zmarłych rodzicach i prowizji od sum opiekuńczych.",
        "transkrypcja": (
            "[fol. 14v]\n"
            "Actum Coram Officio Composito Consulari praesidente Famato D. Alberto "
            "Kwasowic Proconsule, Ubaldo Janaszkowic Advocato et Judice Ordinario "
            "Jurato Crasnicensi, Stanislao Nawrocki et Mathia Tarasa Consulibus, "
            "praesentibus Famatis Joanne Kwasowic, Blasio Kołodziejczyk, Mathia "
            "Koniega, Gregorio Fox et Stanislao Pilin Scabinis Juratis Crasnicensibus "
            "Feria 2da ante Festum S. Catharinae Virginis et Martyris proxima Anno "
            "Domini Millesimo Sexcentesimo Sexagesimo [1660].\n"
            "Inter Ingenuum Casimirum Baśkowski Actorem ac Famatum Martinum Sitarski "
            "Consulem Crasnicensem Tutorem bonorum Actoris actio mota et agitata.\n"
            "Swobodny Kazimierz Baśkowski dawny podopieczny przypozwawszy Sławetnego "
            "Marcina Sitarskiego Raycę krasnickiego Opiekuna swego takową skargę "
            "w piśmie podaną spisaną za pozwoleniem Sądu ninieyszego podał...\n"
            "Łaskawy Panie Burmistrzu spolnie z Pany Raycami y Ławnikami... z łaski "
            "Pana Sitarskiego Opiekuna mego... iż po śmierci rodziców moich... dobra "
            "moie w zawiadywaniu iego będące..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 34,
        "numer_pozycji": "Poz. 34",
        "strona_pagina": "fol. 15r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660 [22 Listopada 1660 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Dokończenie skargi Kazimierza Baśkowskiego przeciw Marcinowi Sitarskiemu o 400 złp u wójta Ubalda Janaszkowica (1660 r.)",
        "osoby_podmioty": "Kazimierz Baśkowski [Baśkowski]; Marcin Sitarski [Sitarski] opiekun; Ubald Janaszkowic [Janaszkowic] wójt",
        "kwoty_podatki": "złotych 100; złotych 30; złotych 400 (u Ubalda Janaszkowica); złotych 400 (u Kładkiego?)",
        "opis_sprawy": "Dokończenie skargi Kazimierza Baśkowskiego: zarzuty wobec opiekuna Marcina Sitarskiego o niedokładne rachunki, wydatki na wychowanie i ucieczkę brata do Krakowa, oraz upomnienie się o sumy opiekuńcze (`100 złp`, `30 złp` prowizji, `400 złp` odebrane przez wójta Ubalda Janaszkowica i `400 złp` na dobrach).",
        "transkrypcja": (
            "[fol. 15r]\n"
            "ko Sąd łaskawy Panów Radziec y przysięgłych... z rachunków Starych "
            "P. Opiekuna... okazało się niektóre wydatki... po śmierci brata mego "
            "do Krakowa... na wychowanie... Sąd tedy ninieyszy nakazuie ażeby... "
            "rachunek pod wysoki rozsądek Sądu podał. Naprzód... P. Opiekun trzymał "
            "przez lat kilka złotych pięćdziesiąt y jnteresu... pożyczałem na "
            "wychowanie... złotych 100 przyznaie się bydź... złotych 30... Pokazuje "
            "P. Opiekun... dobra moie oyczyste złotych trzysta, z których to złotych "
            "czterysta które P. Ubald Janaszkowic Wójt krasnicki odebrał... a drugie "
            "złotych czterysta które kładki..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 35,
        "numer_pozycji": "Poz. 35",
        "strona_pagina": "fol. 15v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660 [22 Listopada 1660 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Replika Marcina Sitarskiego w sprawie Baśkowskiego i przedłożenie regestrów z 1649 r. (1660 r.)",
        "osoby_podmioty": "Marcin Sitarski [Sitarski] opiekun; Kazimierz Baśkowski [Baśkowski]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "Odpowiedź opiekuna Marcina Sitarskiego na skargę Kazimierza Baśkowskiego: tłumaczy spustoszenia wojenne, opiekę nad dziećmi w czasie wyjazdu do Lublina i przedkłada oryginalne regestry rachunkowe z roku 1649.",
        "transkrypcja": (
            "[fol. 15v]\n"
            "będzie P. Opiekun... prosząc aby mu z interesem oddał... gdyż w takim "
            "stanie do Pana swego odjechał... gdyż P. Opiekun sam nie żył... "
            "zaś co się tycze tych złotych... a co się tycze interesu gdyż P. Opiekun "
            "wówczas kiedy było w Lublinie... a teraz kiedy sieroty... Regestra "
            "tylko oddaie... iako z tych wszystkich dóbr rodziców moich... "
            "Inwentarz opisanych... z podniesionym niedbalstwem P. Opiekuna... "
            "pisał na te sieroty... prosił o sprawiedliwe rozsądzenie... P. Opiekun "
            "odstąpił... do sprawiedliwego rozsądku Sądu...\n"
            "Ingenuus vero citatus filius comparens. Naprzód Regestr Rachunków..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 36,
        "numer_pozycji": "Poz. 36",
        "strona_pagina": "fol. 16r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660 [regestr z 6 III 1649 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Oblatowany Regestr dóbr Wawrzyńca i Marianny Baśkowskich z 1649 r.: sprzedaż ogrodu na Podlesiu (180 złp) i domu w Rynku (200 złp)",
        "osoby_podmioty": "Wawrzyniec Baśkowski [Baśkowski] zmarły; Marianna Baśkowska [Baśkowska] zmarła; Maciej Koniega [Koniega] opiekun?; Marcin Sitarski [Sitarski] opiekun; Mikołaj Konicki [Konicki / Koń?]; Stanisław Nawrocki [Nawrocki]; Matyasz Dudka [Dudka]; Jędrzej Dudorek [Dudorek / Rudorek?]",
        "kwoty_podatki": "złotych 180 (ogród na Podlesiu); złotych 200 (dom w Rynku); złotych 1 groszy 18 (kapusta); groszy 9 (farba malarska); groszy 18 (dzieża); groszy 4 (aręda); złotych 20 (prowizja Nawrockiego); złotych 10 (prowizja Dudki); złotych 15 (prowizja Dudorka)",
        "opis_sprawy": "Oblata oryginalnego rejestru majątkowego z `Sabbato ante Dominicam Oculi quadragesimae 1649` (6 III 1649 r.) po zmarłych Wawrzyńcu i Mariannie Baśkowskich, prowadzonego przez opiekunów Macieja Koniegę i Marcina Sitarskiego: sprzedaż ogrodu na Podlesiu (`180 złp`), sprzedaż domu w Rynku Stanisławowi Nawrockiemu (`200 złp`), wpływy za kapustę (`1 złp 18 gr`), farbę malarską (`9 gr`), dzieżę (`18 gr`), arędę (`4 gr`), oraz prowizje od Stanisława Nawrockiego (`20 złp`), Matyasza Dudki (`10 złp`) i Jędrzeja Dudorka (`15 złp`).",
        "transkrypcja": (
            "[fol. 16r]\n"
            "dóbr pozostałego... iest wpisany Regestr rachowania dóbr małoletnich "
            "sierot Wawrzyńca y Maryanny Baśkowskich po nieboszczykach Rodzicach ich "
            "pozostałych za Opiekunów Sławetnych Macieia Koniegi [?] y Marcina "
            "Sitarskiego Ławników przysięgłych krasnickich.\n"
            "Sabbato ante Dominicam Oculi quadragesimae Anno 1649\n"
            "Naprzód przedaliśmy Ogród na przedmieściu Podlesiu a to na zapłacenie "
            "długu Kościelnego... za sumę — zł 180\n"
            "Eodem Anno przedaliśmy Dom w Rynku stojący P. Stanisławowi Nawrockiemu "
            "za sumę pewną złotych dwieście — zł 200\n"
            "Residuum sumę 200 za rok obiecnie oddać albo od tych pieniędzy "
            "interesować.\n"
            "Za Kapustę wzięliśmy — zł 1 gr 18\n"
            "Za farbę malarską — gr 9\n"
            "Za kolebkę y dzieżę wzięliśmy — gr 18\n"
            "Arędy stęki zamek wzięliśmy — gr 4\n"
            "Od P. Stanisława Nawrockiego wzięliśmy interesu od sta złotych za lat "
            "dwie — zł 20\n"
            "Od Matyasza Dudki wzięliśmy interesu od zł 50 za lat dwie — zł 10\n"
            "Od Jędrzeia Dudorka [Rudorka?] wzięliśmy interesu od zł 50 za lat trzy — zł 15"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 37,
        "numer_pozycji": "Poz. 37",
        "strona_pagina": "fol. 16v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1649–1653 [oblata 1660 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Suma percepty Baśkowskich (544 złp) oraz początek regestru expensy z lat 1649–1653",
        "osoby_podmioty": "Sebastian Dec [Dec]; Sederz [Sederz?]; Stanisław Nawrocki [Nawrocki]; Matyasz But [But]; Andrzej Rodzonek [Rodzonek]; Marcin Sitarski [Sitarski]; Ubald Janaszkowic [Janaszkowic]",
        "kwoty_podatki": "złotych 10; złotych 15; złotych 2; złotych 100; złotych 544 (suma percepty); złotych 50 (Rodzonkowi); złotych 50 (Decowi); złotych 50 (Sitarskiemu); złotych 150 (Janaszkowicowi); złotych 100 (kościelny dług); złotych 20 (szpitalowi); złotych 2 groszy 10 (wyderkaf)",
        "opis_sprawy": "(1) Dokończenie percepty z rejestru Baśkowskich: od Sebastiana Deca (`10 złp`), za dwie skrzynie sprzedane Sederzowi (`15 złp`), spichrz (`2 złp`), od Stanisława Nawrockiego w 1653 r. (`100 złp`) — łączna suma percepty: **`544 złp`**; (2) początek expensy z lat 1649–1653: wypłaty po `50 złp` dla Andrzeja Rodzonka, Sebastiana Deca i Marcina Sitarskiego, `150 złp` dane Ubaldowi Janaszkowicowi (18 V 1653 r.), spłata długu kościelnego (`100 złp`), szpitalowi (`20 złp`) i wyderkaf (`2 złp 10 gr`).",
        "transkrypcja": (
            "[fol. 16v]\n"
            "Od Sebestyana Deca od zł 50 za lat dwie — zł 10\n"
            "Skrzynek dwie które były popsowane w kramie przedaliśmy Sederzowi — zł 15\n"
            "Spichlerz zły popsowany przedaliśmy — zł 2\n"
            "Anno 1653 die 13 Maii od P. Stanisława Nawrockiego odebraliśmy "
            "residuum sumę — zł 100\n"
            "Suma Percepti czyni złotych 544\n"
            "Regestr Expensy y Sumy dispositia in Anno 1649\n"
            "Die 15 Maii Nieboszczykowi Matyaszowi Butowi przedmieszczaninowi "
            "krasnickiemu daliśmy na grunt pewny — zł 50\n"
            "Andrzeiowi Rodzonkowi — zł 50\n"
            "Sebestyanowi Decowi — zł 50\n"
            "Do Pana Marcina Sitarskiego — zł 50\n"
            "Anno Dni 1653 die 18 Maii Panu Ubaldowi Janaszkowicowi dana na interes "
            "— zł 150 (to iest zł 100 którą odebrał od P. Stanisława Nawrockiego "
            "a od siebie samego Marcina Sitarskiego zł 50).\n"
            "Płacenie Długów\n"
            "Naprzód Kościelnego długu oddaliśmy — zł 100\n"
            "Szpitalowi grzywna — zł 20\n"
            "Od interesu albo raczey wyderkafu — zł 2 gr 10"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 38,
        "numer_pozycji": "Poz. 38",
        "strona_pagina": "fol. 17r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1649–1653 [oblata 1660 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Drobiazgowy rachunek wydatków na sieroty Baśkowskich: pogrzeby, szkło w oknach, odzież, szkoła i kwartalne (1660 r.)",
        "osoby_podmioty": "Łobodzina [Łobodzina]; Złotnik [Złotnik]; Wiklina [Wiklina]; Krakowski [Krakowski]; Bakałarz [Bakałarz]; Zofia [Zofia]",
        "kwoty_podatki": "złotych 15 (pogrzeby); złotych 3 groszy 5 (okna); groszy 7, 10, 25, 9; złotych 1 groszy 6 (Łobodzina); złotych 2 (Wiklina); groszy 14, 24; złotych 1 groszy 10 (Krakowski); złotych 1 (bakałarz, kocioł, ławy); złotych 1 groszy 6 (kwartał bakałarzowi)",
        "opis_sprawy": "Szczegółowa lista drobnych wydatków opiekuńczych na wychowanie sierot Baśkowskich: dwa pogrzeby (`15 złp`), okna w izbie wielkiej (`3 złp 5 gr`), kłódka (`7 gr`), naprawa drzwi do sklepu (`10 gr`), odzież dla chłopców (`25 gr`, `9 gr`, `1 złp`, `3 złp`, `1 złp 4 gr`), dla Łobodziny na mszę za nieboszczkę matkę (`1 złp 6 gr`), Wiklinie (`2 złp`), Krakowskiemu (`1 złp 10 gr`), bakałarzowi na kwartał (`1 złp 6 gr`), rekreacje jarmarczne i świątkowe (`12 gr`, `12 gr`), papier i okładki do szkoły (`6 gr`) oraz koszulka (`12 gr`).",
        "transkrypcja": (
            "[fol. 17r]\n"
            "Od pogrzebów dwóch daliśmy — zł 15\n"
            "Od naprawy okna w izbie wielkiey — zł 3 gr 5\n"
            "Na kłódkę — gr 7\n"
            "Od naprawy drzwi do sklepu — gr 10\n"
            "Chłopiętom w chorobie na piwo — gr 25\n"
            "Od okucia dziecięcia chłopięcia tufek y czapki — gr 9\n"
            "Od siodła tegoż chłopca — zł 1\n"
            "Za sukno na suknię chłopięciu — zł 3\n"
            "Za czapkę nową y drobney sukni — zł 1 gr 4\n"
            "Na piwo dla dziecięcia — gr 15\n"
            "Za missę Łobodziney za nieboszkę Matkę... wzięła dla Złotników — zł 1 gr 6\n"
            "Wiklinie Zwirzchowi długu pożyczonego — zł 2\n"
            "Chłopiętom na piwo y za pracę — gr 14\n"
            "Misieykowi długu pożyczonego — gr 24\n"
            "Krakowskiemu oddaliśmy — zł 1 gr 10\n"
            "Bakałarzowi / Kotlarzowi / Ławkom / za sól y za ubiór — po zł 1\n"
            "Za trzy kwartały Bakałarzowi — zł 1 gr 6\n"
            "Na rekreacyią jarmarczną i świątkową — gr 12 i gr 12\n"
            "Papier y okładki do szkoły — gr 6\n"
            "Na koszulkę najtową chłopięciu — gr 12"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 39,
        "numer_pozycji": "Poz. 39",
        "strona_pagina": "fol. 17v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1649–1660",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Dalszy ciąg wydatków Baśkowskich: wykup łyżki srebrnej od Jackowskiego oraz pogrzeb małoletniego Wawrzyńca",
        "osoby_podmioty": "Stanisław Jackowski [Jackowski]; Chrostowski [Chrostowski]; Kazimierz Baśkowski [Baśkowski]; Wawrzyniec Baśkowski [Baśkowski] małoletni zmarły; ks. Zakrystian [ks. Zakrystian]",
        "kwoty_podatki": "złotych 1 groszy 15; groszy 18; złotych 22 groszy 1,5; złotych 2 groszy 10 (łyżka srebrna); złotych 1 groszy 6; groszy 3; złotych 3 groszy 15; złotych 1 groszy 4; złotych 1 groszy 10; złotych 5; złotych 80 (wychowanie); złotych 20; złotych 1 groszy 18 (trumna); groszy 9 (grób); złotych 4 groszy 15 (dzwonny i zakrystian); złotych 2 groszy 15 (muzyka i szkoła); złotych 1 groszy 15 (cech szewski)",
        "opis_sprawy": "Kontynuacja regestru wydatków na sieroty Baśkowskich: wykupienie srebrnej łyżki pana Chrostowskiego od Stanisława Jackowskiego (`2 złp 10 gr`), zakup kordów (`3 złp 15 gr`), wychowanie dwojga sierot Kazimierza i Wawrzyńca przez cały rok (`80 złp` i `20 złp`), oraz szczegółowy kosztorys pogrzebu małoletniego Wawrzyńca (trumna `1 złp 18 gr`, wykopanie grobu `9 gr`, dzwonny i ks. zakrystian `4 złp 15 gr`, muzyka i szkoła `2 złp 15 gr`, cech szewski `1 złp 15 gr`, świece `18 gr`, `8 gr`).",
        "transkrypcja": (
            "[fol. 17v]\n"
            "Na kłódkę przedniego domu daliśmy za półgarnca miodu — zł 1 gr 15\n"
            "Na dwie krowy siana — gr 18\n"
            "Ogród przedni daliśmy na kwaśne wino — gr 22½\n"
            "U Stanisława Jackowskiego wykupiłem łyżkę srebrną Pana Chrostowskiego "
            "którą była nieboszka matka tych sierot zastawiła — zł 2 gr 10\n"
            "Czapek dwie nowych dałem — zł 1 gr 6\n"
            "Spisarzowi — gr 3\n"
            "Kordów rzemieślnikowi kupiłem... korda po gr 3 — zł 3 gr 15\n"
            "Za dwa noże kotkowe — zł 1 gr 4\n"
            "Chłopu co cztery dni grodził — zł 1 gr 10\n"
            "Od wychowania dwojga sierot Kazimierza y Wawrzyńca których chowałem "
            "rok cały — zł 80\n"
            "Z osobna od wychowania małego chłopięcia za pół roka — zł 20\n"
            "Wydatek na pogrzeb Małoletniego Wawrzyńca:\n"
            "Naprzód na trumnę — zł 1 gr 18\n"
            "Od wykopania grobu — gr 9\n"
            "Od dzwonów y kapłanom... Dzwonnemu y X. Zakrystianowi — zł 4 gr 15\n"
            "Muzykom y szkole — zł 2 gr 15\n"
            "Cechowi Szewskiemu — zł 1 gr 15\n"
            "Kapłanom w święto... świeca — gr 18\n"
            "Ubogim... — gr 8"
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 40,
        "numer_pozycji": "Poz. 40",
        "strona_pagina": "fol. 18r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Dokończenie wydatków z 1660 r. (wdowa Janaszkowicowa, Gabriel But) i replika Kazimierza Baśkowskiego przeciw Marcinowi Sitarskiemu (1660 r.)",
        "osoby_podmioty": "Gabriel But [But]; Pani Janaszkowicowa [Janaszkowicowa] wdowa; Kazimierz Baśkowski [Baśkowski]; Marcin Sitarski [Sitarski] opiekun",
        "kwoty_podatki": "groszy 7, 8, 4, 8, 3½, 18; złotych 10 i groszy 22 (dla Kazimierza Baśkowskiego); złotych 50",
        "opis_sprawy": "(1) Końcowe pozycje rachunku z 1660 r. (w tym dla Gabriela Buta za kozła, wydatki na okowitę u Pani wdowy Janaszkowicowej oraz przekazanie Kazimierzowi Baśkowskiemu `10 złp` i `22 gr`); (2) replika ustna i pisemna Kazimierza Baśkowskiego przed Sądem Radzieckim i Łączonym na przedstawiony inwentarz i rachunek Marcina Sitarskiego (kwestionowanie wyliczenia `50 złp` i procentów po rodzicach).",
        "transkrypcja": (
            "[fol. 18r]\n"
            "Boże miłościwy — gr 7; Od wybrania dołu — gr 8; Od zbierania... w kościele — gr 4; "
            "Od zrobienia trumny — gr 8; Tym w lesie do kopania daliśmy parę piwa — gr 3½; "
            "Gabryelowi Butowi do kozła... — gr 18; Pani wdowa Janaszkowicowa odebrała "
            "od nas z rachunku okowitą niektórą za służebne bydło...\n"
            "Anno Dni 1660\n"
            "Panu Kazimierzowi Baśkowskiemu dałem — zł 10\n"
            "Tymże czasem grosze z rąk oddałem — gr 22\n"
            "Po tey mowie citatus pokazał Inwentarz dóbr Baśkowskich... gdzie takową "
            "replikę aktor Kazimierz Baśkowski uczynił:\n"
            "Łaskawy Panie Burmistrzu spolnie z Pany Ławnikami... Stawiając przed "
            "Sądem ninieyszym ten to pozew przeciwko P. Marcinowi Sitarskiemu tak "
            "krótko na żałobę jego... przed ramią kładzie odpowiedź... na przykład "
            "sumę tę zł 50 o które się z nich zaskarżył..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 41,
        "numer_pozycji": "Poz. 41",
        "strona_pagina": "fol. 18v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Dalsza replika Kazimierza Baśkowskiego o sumy 300 złp i 150 złp u Jana Skowronka i straty w czasie opieki (1660 r.)",
        "osoby_podmioty": "Kazimierz Baśkowski [Baśkowski]; Marcin Sitarski [Sitarski] opiekun; Jan Skowronek [Skowronek / Skotnica?]",
        "kwoty_podatki": "złotych 34 groszy 24; złotych 50; złotych 33 groszy 15; złotych 40; złotych 300 (suma główna); złotych 150 (u Jana Skowronka); złotych 400 (na wyderkaf)",
        "opis_sprawy": "Kontynuacja repliki Kazimierza Baśkowskiego przeciw opiekunowi Marcinowi Sitarskiemu: wyliczenie procentów (`34 złp 24 gr`, `33 złp 15 gr`), zarzut niepłacenia za naukę w szkole i na służbie w Krakowie, oraz zestawienie kapitałów opiekuńczych (`300 złp`, `150 złp` u Jana Skowronka i `400 złp` danych na wyderkaf).",
        "transkrypcja": (
            "[fol. 18v]\n"
            "względem prac moich które podejmowałem... ażeby prowizya na rok od "
            "sta złotych a w swey było złotych 300... uczyniło po niej groszy "
            "rocznie zł 34/24 y na ten interes nie starczało bo od zł 50 przychodzi "
            "zł 3/15... do tego... zł 40 oświadczono... a co się tycze tej sumy "
            "którą... na edukacyę... P. Opiekunowie nie chcieli wypłacić... gdyż "
            "do Krakowa... na służbę... w sumie principalney zł 300 albo na "
            "P. Jana Skowronka [Skotnicę?] zł 150 które przyjąłem a złotych czterysta "
            "dane między ludzi na wyderkaf za własnych rodziców..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 42,
        "numer_pozycji": "Poz. 42",
        "strona_pagina": "fol. 19r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Powołanie na Jus Municipale (art. XIV) w sprawie Baśkowskiego przeciw Sitarskiemu o zarząd dobrami w czasie wojny i zarazy (1660 r.)",
        "osoby_podmioty": "Marcin Sitarski [Sitarski] opiekun; Kazimierz Baśkowski [Baśkowski]",
        "kwoty_podatki": "złotych 50",
        "opis_sprawy": "Kontynuacja wywodu prawnego w sprawie Baśkowskiego przeciw Sitarskiemu: omówienie trudności egzekucyjnych w czasach wojennych (Zamoyskiego), śmierci dłużników w czasie pomoru oraz cytat z prawa miejskiego magdeburskiego (*Jus Municipale*, art. XIV *O Opiekunach*) o odpowiedzialności opiekunów za przypadki losowe.",
        "transkrypcja": (
            "[fol. 19r]\n"
            "raczey nieboszczyka P. Janaszkowica krewnego tych sierot... nie umiem "
            "rozdzielić w pieniądzach między ludzi... na gruntach położonych... "
            "kiedy pod Zamoyskiego przyszło y miasto Kraśnik ograbiono y żadnego "
            "pokoju nie było... obligatores w pieniądzach pożyczanych pomarli... "
            "wielkie zamieszanie... prawo mieyskie uczy iako iest w prawie *Jure "
            "Municipali* Art. XIV *O Opiekunach*, kto według prawa pospolitego "
            "przypadek którego się strzec nie może nie może opiekunowi szkodzić... "
            "owe zł 50 na które obligacyią... przez nieprzyjaciela popsuwane..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 43,
        "numer_pozycji": "Poz. 43",
        "strona_pagina": "fol. 19v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Dekret Sądu Łączonego w sprawie Kazimierza Baśkowskiego przeciw Marcinowi Sitarskiemu (60 złp procentów i 73 złp kapitału, 1660 r.)",
        "osoby_podmioty": "Kazimierz Baśkowski [Baśkowski]; Marcin Sitarski [Sitarski] opiekun; Wojciech Dudka [Dudka]?",
        "kwoty_podatki": "złotych 50; złotych 60 (procentów); złotych 73 (kapitału)",
        "opis_sprawy": "(1) Dokończenie repliki opiekuna Marcina Sitarskiego (wspomnienie Wojciecha Dudki i strat wojennych); (2) `Decretum`: Sąd Łączony Radziecki i Wójtowski w sprawie Kazimierza Baśkowskiego przeciw Marcinowi Sitarskiemu nakazuje pozwanemu wypłacić `60 złp` z tytułu procentów za 3 lata oraz przygotować zwrot kapitału (`73 złp` i sumy z obligacji).",
        "transkrypcja": (
            "[fol. 19v]\n"
            "poprawie... Woyciecha Dudki przy ktorych ten dług iest... Szpitalowi, "
            "Kościołowi Różańcowi... przez lat kilkanaście prosząc Sądu o "
            "rozsądek...\n"
            "Decretum\n"
            "Urząd tedy ninieyszy zobopolny tak Radziecki iako y Wójtowski y "
            "Ławnicy Przysięgli krasniccy pilnie przesłuchawszy kontrowersyi stron "
            "obudwu y one dobrze uważywszy takowy Dekret między stronami ferował: "
            "Co się tycze złotych pięćdziesiąt które... przez lat trzy przy sobie "
            "miał... nakazuie pozwanemu aby procentów za lat trzy zatrzymanych "
            "od tych złotych pięćdziesiąt złotych... oraz z kapitałem oddał... "
            "a na ostatek złotych sześćdziesiąt które sobie strona... odebrać ma..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 44,
        "numer_pozycji": "Poz. 44",
        "strona_pagina": "fol. 20r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660 [31 XII 1659 / 1660 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Wykonanie dekretu Baśkowskiego z Sitarskim (73 złp) oraz ustanowienie opiekunów sierot po Wojciechu Rogalowskim (1660 r.)",
        "osoby_podmioty": "Marcin Sitarski [Sitarski] opiekun; Kazimierz Baśkowski [Baśkowski]; Ubald Janaszkowic [Janaszkowic] wójt; Wojciech Rogalowski [Rogalowski] zmarły",
        "kwoty_podatki": "złotych 50; złotych 73 (wypłacone Baśkowskiemu); złotych 200",
        "opis_sprawy": "(1) Dokończenie dekretu i pokwitowanie wykonania wyroku między Marcinem Sitarskim a Kazimierzem Baśkowskim (wypłata `73 złp` gotówką w obecności wójta Ubalda Janaszkowica oraz rozliczenie `200 złp`, z zastrzeżeniem przysięgi na brakujące ruchomości); (2) `Feria Sexta in Vigilia Festi Circumcisionis Christi 1660` (31 XII 1659 / 1660 r.): otwarcie wpisu ustanowienia opiekunów dla sierot po zmarłym przedmieszczaninie Wojciechu Rogalowskim.",
        "transkrypcja": (
            "[fol. 20r]\n"
            "reszcie przy pozwanym... z procentem złotych pięćdziesiąt... złotych "
            "73 oddał gotowych złotych patronowi P. Ubaldowi Janaszkowicowi... "
            "co się zaś tycze złotych dwustu... na gruncie... a to pod karą "
            "iuramenti... iż nie zataił ani przy sobie nic nie zatrzymał... "
            "Quod Decretum ab utraque parte susceptum est.\n"
            "Actum Coram Officio Advocati et Scabinali Jurato Crasnicensi.\n"
            "Actum Coram Officio Consulari Feria Sexta in Vigilia Festi Circumcisionis "
            "Christi Domini proxima Anno Domini 1660\n"
            "Tutores dantur Pupillis olim Hon. Alberti Rogalowski anteoppidani Crasnicensis."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 45,
        "numer_pozycji": "Poz. 45",
        "strona_pagina": "fol. 20v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660 [1660 r.]",
        "kategoria": "Sprawy opiekuńcze i inwentarze / Ustanowienie Jana Grzętki i Sebastiana Batusika opiekunami sierot po Wojciechu Rogalowskim oraz początek inwentarza (1660 r.)",
        "osoby_podmioty": "Wojciech Rogalowski [Rogalowski] zmarły; Jan Grzętka [Grzętka] opiekun; Sebastian Batusik [Batusik] opiekun; Maciej Koniega [Koniega]",
        "kwoty_podatki": "brak",
        "opis_sprawy": "(1) Wobec ucieczki/nieobecności wójta i konieczności ochrony sierot po zmarłym jałmużniku szpitala św. Ducha Wojciechu Rogalowskim, Sąd Radziecki na wniosek obecnego Macieja Koniegi ustanawia Jana Grzętkę i Sebastiana Batusika opiekunami dzieci Rogalowskiego, zobowiązując ich do sporządzenia inwentarza; (2) `Eodem die Tempore Pomeridiano`: początek *Inventarium bonorum post olim Alberti Rogalowski*.",
        "transkrypcja": (
            "[fol. 20v]\n"
            "Przed Urzędem y Aktami ninieyszemi Radzieckiemi krasnickiemi... "
            "stanowszy... jałmużnik szpitala Ś. Ducha wyznał że nieboszczyk Woyciech "
            "Rogalowski z tego świata zszedł... nie zostawiwszy opiekuna... w obecności "
            "Macieia Koniegi... Urząd tedy ninieyszy Radziecki krasnicki... "
            "przychylając się do prośby... po śmierci nieboszczyka Woyciecha "
            "Rogalowskiego naznacza opiekunami Sebestyana Batusika y Jana Grzętkę "
            "którzy to powinni będą inwentarz wszystkich dóbr pozostałych do Urzędu "
            "oddać...\n"
            "Eodem die Tempore Pomeridiano\n"
            "Inventarium bonorum post olim Hon. Alberti Rogalowski anteoppidani "
            "Crasnicensis derelictorum.\n"
            "Ex instantia Hon. Joannis Grzętka et Sebastiani Batusik Tutorum "
            "filiorum et filiarum minorennium olim Hon. Alberti Rogalowski..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 46,
        "numer_pozycji": "Poz. 46",
        "strona_pagina": "fol. 21r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660",
        "kategoria": "Inwentarze pośmiertne / Inwentarz domu i warsztatu po Wojciechu Rogalowskim spisany przez Błażeja Kołodziejczyka i pisarza Stanisława Sikora (1660 r.)",
        "osoby_podmioty": "Ubald Janaszkowic [Janaszkowic] wójt; Błażej Kołodziejczyk [Kołodziejczyk] ławnik; Stanisław Sikor [Sikor / Sikora?] pisarz przysięgły; Miarowicki [Miarowicki] sąsiad; Wojciech Rogalowski [Rogalowski] zmarły",
        "kwoty_podatki": "opis budynku (okna, piec zielony kaflowy, komin z blachy, kłódki)",
        "opis_sprawy": "Komisja wyznaczona przez wójta Ubalda Janaszkowica (ławnik Błażej Kołodziejczyk i pisarz przysięgły Stanisław Sikor) spisuje inwentarz nieruchomości po Wojciechu Rogalowskim: dom za Bramą Staromiejską obok ogrodu szpitalnego św. Ducha (między Miarowickim a ulicą pospolitą do młyna miejskiego), szczegółowy opis drzwi na zawiasach żelaznych, klamek, wrzeciądzów, skobli, okien szklanych w ołów i drewno, zielonego pieca kaflowego, komina z blachy, stołów i szafy w komorze.",
        "transkrypcja": (
            "[fol. 21r]\n"
            "Ex Mandato Famati Dni Ubaldi Janaszkowic Advocati et Judicis Ordinarii "
            "Crasnicensis missi et deputati fuerunt Famati Blasius Kołodziejczyk "
            "Scabinus et Stanislaus Sikor Scriba et Notarius Juratus Crasnicensis "
            "ad inventanda bona tam mobilia quam immobilia...\n"
            "Naprzód Dom stoiecy na Przedmieściu za Bramą Staromieyską podług ogroda "
            "szpitalnego z iedney strony Miarowickiego a z drugiey strony Ulicy "
            "pospolitey która się ciągnie od Młyna Mieyskiego do Miasta... do którego "
            "drzwi dębowe na zawiasach żelaznych z wrzeciądzem y klamką... w sieni "
            "drzwi... bez skobli... wedle tego chlewa komora... w izbie po prawey "
            "ręce okna trzy z których iedno cale w ołów, drugie okno w drewno "
            "robione... piec zielony kaflowy dobry, ławki dwie koło pieca... stoł "
            "wielki dębowy... w drugiej izbie... drzwi na zawiasach żelaznych do "
            "komory..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 47,
        "numer_pozycji": "Poz. 47",
        "strona_pagina": "fol. 21v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660",
        "kategoria": "Inwentarze pośmiertne / Dokończenie inwentarza Wojciecha Rogalowskiego: piekarnia, sad (39 drzew), stodoła i warsztaty tkackie (1660 r.)",
        "osoby_podmioty": "Wojciech Rogalowski [Rogalowski] zmarły; Młynarzewski [Młynarzewski?] sąsiad; Jan Krawczyk [Krawczyk]",
        "kwoty_podatki": "39 drzew owocowych; 2 warsztaty tkackie; beczki, siekiery, koryta",
        "opis_sprawy": "Dalszy ciąg inwentarza po Wojciechu Rogalowskim: opis komory na ogród, piekarni z piecem chlebowym i sadu przy ogrodzie Młynarzewskiego [?] (39 drzew śliwowych, gruszkowych i jabłoni), nowej stodoły z drzewa na słupy stawianej, dwóch warsztatów tkackich („warsztatów dwa do płóciennictwa ze wszystkimi narzędziami”), beczek kapustnych, sieci, siekier i dzieży chlebowej (wzmiankowany Jan Krawczyk).",
        "transkrypcja": (
            "[fol. 21v]\n"
            "komory na ogród są drzwi na zawiasach żelaznych... do kuchni... do "
            "piekarni drzwi na zawiasach żelaznych... piec chlebowy zły... podług "
            "ogroda płot od miedzy ogroda Młynarzewskiego... w tym ogrodzie drzewa "
            "rodzajnego gruszkowego czworo, jabłoni pięć, śliwowego drzewa 39... "
            "nowa stodoła z drzewa zbudowana na słupach... w którey stodołe... "
            "warsztatów dwa do płóciennego rzemiosła z których dwóch na jednym nie "
            "dostaje... beczek trzy kapustnych... sieci... poduszki cztery, siekier "
            "dwie, dzieża, niecek chlebowych dwie... od Krawczyka tok... od tego "
            "roku na dwie żyta..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 48,
        "numer_pozycji": "Poz. 48",
        "strona_pagina": "fol. 22r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1660–1661 [5 IV 1661 r.]",
        "kategoria": "Inwentarze pośmiertne i sprawy opiekuńcze / Zakończenie inwentarza Rogalowskiego (długi u Węgorka i Świadonia) oraz sprawa Mateusza Żmiędy z opiekunem Wawrzyńcem Łysakiem (5 IV 1661 r.)",
        "osoby_podmioty": "Wojciech Rogalowski [Rogalowski] zmarły; Jan Grzętka [Grzętka] opiekun; Sebastian Batusik [Batusik] opiekun; Sebastian Węgorek [Węgorek]; Borecki [Borecki]; Piotr Świadoń [Świadoń] z Dzierzkowic; Mateusz Żmięda [Żmięda / Żmigrodzki?]; Anna Żmiędzina [Żmiędzina]; Łukasz Żmięda [Żmięda]; Wawrzyniec Łysak [Łysak / Łysy?]; Ubald Janaszkowic [Janaszkowic] wójt",
        "kwoty_podatki": "złotych 10 (do Boreckiego); złotych 19 (do Węgorka); złotych 6 (od Piotra Świadonia)",
        "opis_sprawy": "(1) Zakończenie inwentarza Wojciecha Rogalowskiego: długi należne od Sebastiana Węgorka (`10 złp` do Boreckiego i `19 złp` na Węgorkowym obligu), od Piotra Świadonia z Dzierzkowic (`6 złp`) oraz fasa wielka w szpitalu; (2) `Feria 3tia post Dominicam Passionis 1661` (5 IV 1661 r.): szlachetny Mateusz Żmięda z żoną Anną (oraz opiekunem Łukaszem Żmiędą) wnosi sprawę z remisji wójta Ubalda Janaszkowica przeciw opiekunowi Wawrzyńcowi Łysemu [Łysakowi?] przed Sądem Łączonym.",
        "transkrypcja": (
            "[fol. 22r]\n"
            "półkorca... z skrzynią... w kuchni na kominie... długi które nieboszczyk "
            "Woyciech Rogalowski przed ludźmi zeznał: naprzód Sebestyanowi Węgorkowi "
            "winien zł 10 do Boreckiego, na Węgorkowym obligu zł 19 które obligował "
            "na domu swoim, Piotrowi Świadoniowi z Dzierzkowic zł 6, fasa wielka "
            "w szpitalu w której się wsypie... Quod quidem Inventarium... ad "
            "affectationem Tutorum Actis praesentibus inserta et connotata...\n"
            "Actum Coram Officio Consulari Feria 3tia post Dominicam Passionis proxima "
            "Anno Domini Millesimo Sexcentesimo Sexagesimo Primo [1661]\n"
            "Inter Ingenuum Matheum Żmięda [Żmigrodzki?] et Hon. Annam eiusdem "
            "coniugem ac Tutorem Actores, ac Hon. Laurentium Łysy [Łysak?] Civem "
            "Crasnicensem Tutorem bonorum Mathaei Szmięda [?] citatum.\n"
            "Ex Remissione Famati Dni Ubaldi Janaszkowic Advocati Judicii Ordinarii "
            "Jurati Crasnicensis... między szlachetnym Mateuszem Żmiędą... a "
            "Wawrzyńcem Łysakiem mieszczaninem krasnickim..."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 49,
        "numer_pozycji": "Poz. 49",
        "strona_pagina": "fol. 22v",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1661 [5 Kwietnia 1661 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Skarga Mateusza Żmiędy przeciw opiekunowi Wawrzyńcowi Łysakowi o majątek po babce (z odwołaniem do roku 1649)",
        "osoby_podmioty": "Mateusz Żmięda [Żmięda]; Wawrzyniec Łysak [Łysak / Łysy?]; Jakub [Jakub] zięć?; Ewa [Ewa] matka",
        "kwoty_podatki": "złotych 200; złotych 20; złotych 15 (wypłacone)",
        "opis_sprawy": "Obszerna skarga Mateusza Żmiędy przeciw opiekunowi Wawrzyńcowi Łysakowi o majątek i spadek po rodzicach oraz babce od roku 1649 (`anno 1649`): zarzut o brak inwentarza, przetrzymywanie `200 złp` kapitału i prowizji z kilkunastu lat, wykup `20 złp` od Jakuba oraz żądanie zwrotu dokumentów i rozliczenia przed sądem (wypłacone jedynie `15 złp`).",
        "transkrypcja": (
            "[fol. 22v]\n"
            "copia spisana przed Urzędem... Łaskawy Panie Burmistrzu spolnie z Pany "
            "Ławnikami... skarży się przed Sądem na Pana Wawrzyńca Łysaka Opiekuna "
            "mego... iż według Dekretu... inwentarz dóbr moich wszystkich... z "
            "których się opiekował... przy tym też... w sumie złotych 200... od "
            "których procent... od Jakuba... złotych 20... a do brata mego... po "
            "nieboszczce matce mey Ewie... prosząc Sądu aby... podał ofiarując "
            "sobie... za wszystko... złotych 15... na co wszystko poddaję pod "
            "łaskawy rozsądek Sądu...\n"
            "Który to pozew przed Sądem podał wespół z inwentarzem Anno Dni 1649."
        ),
        "link_swa": UNIT_LINK
    },
    {
        "nr_skanu": 50,
        "numer_pozycji": "Poz. 50",
        "strona_pagina": "fol. 23r",
        "sygnatura": "35/40/0/1/18",
        "data_rok": "1661 [5 Kwietnia 1661 r.]",
        "kategoria": "Sprawy opiekuńcze (Acta Pupillorum) / Odpowiedź opiekuna Wawrzyńca Łysaka i rachunek opieki nad siostrą Marianną w Szpitalu św. Ducha (1661 r.)",
        "osoby_podmioty": "Mateusz Żmięda [Żmięda]; Marianna Żmiędzianka [Żmiędzianka] siostra; Barbara Saienkowa [Saienkowa] babka zmarła; Wawrzyniec Łysak [Łysak / Łysy?]; Bartosz Kulka [Kulka]; Jakub Saienek [Saienka]; Marianna Saienkówna [Saienkówna]",
        "kwoty_podatki": "złotych 7; złotych 36 (prowizja); złotych 3 (od Jakuba); złotych 2 groszy 10; złotych 3 groszy 10; groszy 18; złotych 46 (suma percepty); złotych 1 groszy 24 (expensa); groszy 18 (pisarzowi)",
        "opis_sprawy": "Odpowiedź opiekuna Wawrzyńca Łysaka przed Sądem Wójtowsko-Ławniczym i Radzieckim w sprawie opieki nad dwojgiem sierot (Mateuszem i jego siostrą Marianną) powierzonej mu przez zmarłą babkę Barbarę Saienkową: opis choroby siostry Marianny, umieszczenia jej w Szpitalu św. Ducha za staraniem prowizorów szpitalnych, rozliczenie percepty (`46 złp` z prowizji od Bartosza Kulki `7 złp`, Jakuba Saienka `3 złp`, `2 złp 10 gr`, `3 złp 10 gr`, `18 gr`) i expensy z roku 1649 (`1 złp 24 gr`, `18 gr` pisarzowi).",
        "transkrypcja": (
            "[fol. 23r]\n"
            "Officio Advocati et Scabinorum Juratorum Crasnicensium praesentibus...\n"
            "percepta uczyniona była za dwoje sierot to iest Mateusza Żmiędę y "
            "Siostrę iego Mariannę... których nieboszczka Barbara Saienkowa Baba "
            "pamięci swoiey... poruczyła była nieboszczykowi Wawrzyńcowi Babi [?], "
            "a po śmierci Barbary... Bartoszowi Kulce z Urzędu Radzieckiego... "
            "wielka choroba przyszła iż się nikt chować w sieni nie chciał... tedy "
            "za wielkim uproszeniem Panów Prowizorów Szpitalnych uprosiwszy się do "
            "szpitala y daliśmy na szpital złotych 40... od sumy złotych... "
            "Bartosza Kulki odebrał był interesu złotych 7... suma interesu tego "
            "do siebie... złotych 36 od Jakuba Saienka złotych 3... za korzec żyta "
            "zł 3/10... suma percepty złotych 46.\n"
            "Expensę z tego pokazali takową:\n"
            "Anno Dni 1649 Urzędowi co wychodzili na wizyę... gr 18... na sukno... "
            "zł 1/24... Pisarzowi wpisania Rozdziału gr 18. Item dla siostry iego "
            "Maryanny..."
        ),
        "link_swa": UNIT_LINK
    }
]

main_data.extend(part2_scans)
with open('/home/ubuntu/workspace/Gen/main_data_j18_part2.json', 'w', encoding='utf-8') as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"SUCCESS: main_data_j18_part2.json saved with {len(main_data)} scans.")
