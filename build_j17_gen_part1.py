# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/main_data_j17_part1.json', encoding='utf-8') as f:
    main_data = json.load(f)

# Słownik genealogiczny osób z Partii 1 (skany 1-25)
# Rygor Wariantu 2: 1 fizyczna osoba = 1 rekord, pole wariant_nazwiska, brak podmiotów nieosobowych
raw_persons = [
    {
        "nazwisko": "Niewiadomski",
        "imie": "Bartłomiej",
        "miejsce": "Kraśnik",
        "funkcja": "Mieszczanin kraśnicki, powód w sporze o sukno",
        "wariant_nazwiska": "Kruszelniczek? / Kruszelnicki? / Niewiadomski",
        "wystapienia": [
            {"skan": 5, "rok": "1700", "zapis_oryginalny": "Bartłomiej Niewiadomski Kruszelniczek", "rola": "Aktor w procesie o suknię przeciw Tkaczykowi"}
        ]
    },
    {
        "nazwisko": "Tkaczyk",
        "imie": "Andrzej",
        "miejsce": "Kraśnik",
        "funkcja": "Tkacz / rzemieślnik kraśnicki, pozwany o sukno",
        "wariant_nazwiska": "Tkaczyk [Kaczyk?]",
        "wystapienia": [
            {"skan": 5, "rok": "1700", "zapis_oryginalny": "Andrzej Tkaczyk", "rola": "Pozwany przez Niewiadomskiego o suknię u żyda Herszka"}
        ]
    },
    {
        "nazwisko": "Tokarski",
        "imie": "Herszek",
        "miejsce": "Kraśnik",
        "funkcja": "Żyd kupiec kraśnicki, właściciel składu sukna",
        "wariant_nazwiska": "Herszko Tokarski [Vokarszangego? / Tokarskiego?]",
        "wystapienia": [
            {"skan": 5, "rok": "1700", "zapis_oryginalny": "Żyd Herszek Vokarszangi w składzie Sukna", "rola": "Posiadacz składu sukna w Kraśniku"}
        ]
    },
    {
        "nazwisko": "Hardysz",
        "imie": "Wojciech",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki, brat Jakuba",
        "wariant_nazwiska": "Hardycz [Hardysz? / Hardycz?]",
        "wystapienia": [
            {"skan": 5, "rok": "1700", "zapis_oryginalny": "Wojciech Hardycz Aktor Przedmieszczanin", "rola": "Powód w gwałtownym sporze rodzinnym o pobicie i wtrącenie brata"},
            {"skan": 8, "rok": "1700", "zapis_oryginalny": "Wojciech Hardysz Brat protestanta", "rola": "Pozwany o lekkomyślne zerwanie przysięgi i dekretu, skazany do aresztu"}
        ]
    },
    {
        "nazwisko": "Hardysz",
        "imie": "Jakub",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki, ojciec Adama, brat Wojciecha",
        "wariant_nazwiska": "Hardyza [Hardysz? / Hardyza / Sentygielski?]",
        "wystapienia": [
            {"skan": 5, "rok": "1700", "zapis_oryginalny": "Jakub Hardyza Oyciec", "rola": "Pozwany przez brata Wojciecha o pobicie i zniewagi"},
            {"skan": 8, "rok": "1700", "zapis_oryginalny": "Jakub Hardyza Ociec", "rola": "Protestujący przeciw bratu Wojciechowi o uwięzienie"},
            {"skan": 14, "rok": "1700", "zapis_oryginalny": "Jakub Hardysz", "rola": "Pozwany przez Tokarczyka o rąbanie drzewa w lesie miejskim"}
        ]
    },
    {
        "nazwisko": "Hardysz",
        "imie": "Adam",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki, syn Jakuba",
        "wariant_nazwiska": "Hardyza [Hardysz? / Hardyza syn]",
        "wystapienia": [
            {"skan": 5, "rok": "1700", "zapis_oryginalny": "Adam Hardyza Syn", "rola": "Pozwany wraz z ojcem przez stryja Wojciecha"},
            {"skan": 8, "rok": "1700", "zapis_oryginalny": "Adam Syn", "rola": "Protestujący wraz z ojcem przeciwko stryjowi"}
        ]
    },
    {
        "nazwisko": "Hardysz",
        "imie": "Andrzej",
        "miejsce": "Kraśnik",
        "funkcja": "Mieszkaniec kraśnicki, uczestnik bójki karczemnej",
        "wariant_nazwiska": "Hardysz [Andrzej Hardysz]",
        "wystapienia": [
            {"skan": 12, "rok": "1700", "zapis_oryginalny": "Andrzej Hardysz", "rola": "Uczestnik krwawej bójki w szynku Lejby Markowicza z Tomaszem Kępką"}
        ]
    },
    {
        "nazwisko": "Berek",
        "imie": "Berek",
        "miejsce": "Kraśnik",
        "funkcja": "Żyd młynarz kraśnicki, obywatel miejski",
        "wariant_nazwiska": "Berek molitor [Berek młynarz]",
        "wystapienia": [
            {"skan": 6, "rok": "1700", "zapis_oryginalny": "Infidelis Berek molitor", "rola": "Powód o pretensje piwne przeciw Olchowskiemu"},
            {"skan": 7, "rok": "1700", "zapis_oryginalny": "Berek żyd Obywatel Kraśnicki", "rola": "Powód o koła i rzeczy przeciw Stawińskiemu"}
        ]
    },
    {
        "nazwisko": "Olchowski",
        "imie": "Szymon",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki, dłużnik i posesjonat",
        "wariant_nazwiska": "Olchowski [Simon Olchowski]",
        "wystapienia": [
            {"skan": 6, "rok": "1700", "zapis_oryginalny": "Simon Olchowski", "rola": "Pozwany o długi piwne przez Berka młynarza"},
            {"skan": 21, "rok": "1700", "zapis_oryginalny": "Szymon Olchowski Przedmieszczanin", "rola": "Powód przeciw szafarzowi Piaseckiemu o zajęcie konia za podatek"}
        ]
    },
    {
        "nazwisko": "Stawiński",
        "imie": "Jan",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki, szelwiorz",
        "wariant_nazwiska": "Stawiński [Joannes Stawiński]",
        "wystapienia": [
            {"skan": 6, "rok": "1700", "zapis_oryginalny": "Joannes Stawiński", "rola": "Pozwany o długi, ukarany kontumacją"},
            {"skan": 7, "rok": "1700", "zapis_oryginalny": "Jan Stawiński przedmieszczanin", "rola": "Pozwany przez Berka żyda o koła wozowe"},
            {"skan": 8, "rok": "1700", "zapis_oryginalny": "Jan Stawiński szelwiorz", "rola": "Aresztowanie jego dóbr na ratuszu przez bedela Kleina"},
            {"skan": 13, "rok": "1700", "zapis_oryginalny": "Jan Stawiński", "rola": "Skazany dekretem do spłaty 80 zł długu krawcowi"}
        ]
    },
    {
        "nazwisko": "Zysmanowa",
        "imie": "[Wdowa]",
        "miejsce": "Kraśnik",
        "funkcja": "Żydówka kraśnicka, wierzycielka miejska",
        "wariant_nazwiska": "Zysmanowa Judea [Zysmanowa wdowa]",
        "wystapienia": [
            {"skan": 6, "rok": "1700", "zapis_oryginalny": "Zysmanowa Judea", "rola": "Powódka w procesie o długi przeciw Idzieńskiemu"}
        ]
    },
    {
        "nazwisko": "Idzieński",
        "imie": "Stanisław",
        "miejsce": "Kraśnik",
        "funkcja": "Mieszczanin kraśnicki, dłużnik",
        "wariant_nazwiska": "Idzieński [Stanisław Idzienski]",
        "wystapienia": [
            {"skan": 6, "rok": "1700", "zapis_oryginalny": "Stanisław Idzienski", "rola": "Pozwany przez Zysmanową żydówkę, skazany na kontumację"}
        ]
    },
    {
        "nazwisko": "Trafica",
        "imie": "Kazimierz",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki",
        "wariant_nazwiska": "Trafica [Frafica? / Trasica? / Trafica]",
        "wystapienia": [
            {"skan": 6, "rok": "1700", "zapis_oryginalny": "Kazimierz Frafica Przedmieszczanin", "rola": "Protestujący solennie przeciw Wawrzyńcowi Zielińskiemu o szynkownice"}
        ]
    },
    {
        "nazwisko": "Trafica",
        "imie": "Wawrzyniec",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki, sługa dworski",
        "wariant_nazwiska": "Trafica [Wawrzyniec Trafica / Trasica]",
        "wystapienia": [
            {"skan": 23, "rok": "1700", "zapis_oryginalny": "Wawrzyniec Trafica Przedmieszczanin", "rola": "Powód o 12 zł zaległego myta za służbę u Szymona Krasuskiego"}
        ]
    },
    {
        "nazwisko": "Zieliński",
        "imie": "Wawrzyniec",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki",
        "wariant_nazwiska": "Zieliński [Wawrzyniec Zieliński / Dieliński?]",
        "wystapienia": [
            {"skan": 6, "rok": "1700", "zapis_oryginalny": "Wawrzyniec Zieliński Przedmieszczanin", "rola": "Pozwany przez Traficę o zatajenie szynkownic kradzionych"},
            {"skan": 18, "rok": "1700", "zapis_oryginalny": "Wawrzyniec Zieliński Przedmieszczanin", "rola": "Pozwany przez wójta Rymarczyka o obelgi i zniesławienie"}
        ]
    },
    {
        "nazwisko": "Pławnik",
        "imie": "Matyasz",
        "miejsce": "Kraśnik",
        "funkcja": "Mieszczanin kraśnicki",
        "wariant_nazwiska": "Pławnik [Matyasz Pławnik / Pławnik]",
        "wystapienia": [
            {"skan": 6, "rok": "1700", "zapis_oryginalny": "Matyasz Pławnik Aktor", "rola": "Powód o nową suknię samodziałową 12 zł przeciw Skałce"},
            {"skan": 14, "rok": "1700", "zapis_oryginalny": "Matyasz Pławnik", "rola": "Otrzymanie 8 zł zadośćuczynienia i zgoda ze Skałką"}
        ]
    },
    {
        "nazwisko": "Skałka",
        "imie": "Wojciech",
        "miejsce": "Przedmieście Góry i Podlesie",
        "funkcja": "Przedmieszczanin kraśnicki, piwowar [Piwar]",
        "wariant_nazwiska": "Skałka [Skałka Piwar / Wojciech Skałka]",
        "wystapienia": [
            {"skan": 6, "rok": "1700", "zapis_oryginalny": "Wojciech Skałka Piwar", "rola": "Pozwany o suknię sequestrowaną przez szafarzy"},
            {"skan": 7, "rok": "1700", "zapis_oryginalny": "Wojciech Skałka Przedmieszczanin Podleski", "rola": "Pozwany przez Ignacego Pawlika o uwięzienie"},
            {"skan": 9, "rok": "1700", "zapis_oryginalny": "Wojciech Skałka", "rola": "Sąsiad roli szpitalnej na Górach"},
            {"skan": 11, "rok": "1700", "zapis_oryginalny": "Wojciech Skałka Przedmieszczanin", "rola": "Powód o subordynację po pogrzebie przeciw Lutrowi"},
            {"skan": 14, "rok": "1700", "zapis_oryginalny": "Wojciech Skałka", "rola": "Wypłata 8 zł ugody Pławnikowi za suknię"}
        ]
    },
    {
        "nazwisko": "Skałka",
        "imie": "Albert",
        "miejsce": "Kraśnik",
        "funkcja": "Mieszczanin kraśnicki",
        "wariant_nazwiska": "Skałka [Albertus Skałka / Wojciech?]",
        "wystapienia": [
            {"skan": 14, "rok": "1700", "zapis_oryginalny": "Albert Skałka", "rola": "Powód przeciw Piaseckiemu i Zdebionkowi"}
        ]
    },
    {
        "nazwisko": "Kotowicz",
        "imie": "Adam",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Burmistrz kraśnicki, prowizor szpitala Św. Ducha",
        "wariant_nazwiska": "Kotowicz [Adam Kotowicz Burmistrz / Letokowicz?]",
        "wystapienia": [
            {"skan": 6, "rok": "1700", "zapis_oryginalny": "Pan Letokowicz rezydent", "rola": "Właściciel kwatery, w której złożono suknię"},
            {"skan": 9, "rok": "1700", "zapis_oryginalny": "Adam Kotowicz Burmistrz y Prowizor Szpitala", "rola": "Urzędowe kwitowanie Katarzyny Bartoszkowej z sumy 90 złp"},
            {"skan": 10, "rok": "1700", "zapis_oryginalny": "JM Adam Kotowicz Burmistrz", "rola": "Właściciel roli sąsiedzkiej na Podlesiu"}
        ]
    },
    {
        "nazwisko": "Kruszelnicki",
        "imie": "Jan",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Prowizor szpitala Św. Ducha, radny miejski",
        "wariant_nazwiska": "Kruszelnicki [Jan Kruszelnicki]",
        "wystapienia": [
            {"skan": 9, "rok": "1700", "zapis_oryginalny": "Jan Kruszelnicki Prowizor Szpitala", "rola": "Kwitowanie sumy 90 złp dla szpitala Św. Ducha"}
        ]
    },
    {
        "nazwisko": "Bartoszek",
        "imie": "Katarzyna",
        "miejsce": "Przedmieście Góry i Podlesie",
        "funkcja": "Wdowa przedmieszczańska po Matyaszu Wiatrze / Wolaku",
        "wariant_nazwiska": "Bartoszkowa [Katarzyna Bartoszkowa wdowa / Wolakowa]",
        "wystapienia": [
            {"skan": 9, "rok": "1700", "zapis_oryginalny": "Katarzyna Bartoszkowa wdowa", "rola": "Spłata 90 złp długu szpitalnego z roli na Górach"},
            {"skan": 10, "rok": "1700", "zapis_oryginalny": "Katarzyna Bartoszkowa", "rola": "Zabezpieczenie prowizji rocznej 6 złp dla szpitala"}
        ]
    },
    {
        "nazwisko": "Wolak",
        "imie": "Matyasz",
        "miejsce": "Przedmieście Góry i Podlesie",
        "funkcja": "Zmarły gospodarz przedmieszczański [Wiatr vel Wolak]",
        "wariant_nazwiska": "Wolak [Matyasz Wolak / Wiatr]",
        "wystapienia": [
            {"skan": 9, "rok": "1700", "zapis_oryginalny": "niegdy Uczciwy Matyasz Wolak Ojciec", "rola": "Zmarły mąż Katarzyny Bartoszkowej"}
        ]
    },
    {
        "nazwisko": "Wolak",
        "imie": "Maciej",
        "miejsce": "Przedmieście Góry i Podlesie",
        "funkcja": "Przedmieszczanin, sąsiad roli szpitalnej",
        "wariant_nazwiska": "Wolak [Maciej Wolak]",
        "wystapienia": [
            {"skan": 9, "rok": "1700", "zapis_oryginalny": "Maciej Wolak Przedmieszczanin", "rola": "Właściciel sąsiedniej roli na Górach"}
        ]
    },
    {
        "nazwisko": "Pawlik",
        "imie": "Ignacy",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki",
        "wariant_nazwiska": "Pawlik [Ignacy Pawlik / Panlik?]",
        "wystapienia": [
            {"skan": 7, "rok": "1700", "zapis_oryginalny": "Ignacy Pawlik Przedmieszczanin", "rola": "Powód przeciwko Skałce o uwięzienie w bramie"}
        ]
    },
    {
        "nazwisko": "Śmieszkowic",
        "imie": "Stanisław",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Podwójci kraśnicki",
        "wariant_nazwiska": "Śmieszkowic [Śmieszek / Śmieszkowic]",
        "wystapienia": [
            {"skan": 7, "rok": "1700", "zapis_oryginalny": "Stanisław Śmieszkowic Podwójci", "rola": "Sędzia podwójci w sprawach podatkowych"},
            {"skan": 18, "rok": "1700", "zapis_oryginalny": "Stanisław Śmieszkowic Podwójci", "rola": "Sędzia w sporze wójta Piasków Rymarczyka"}
        ]
    },
    {
        "nazwisko": "Puklina",
        "imie": "Krystyna",
        "miejsce": "Kraśnik (ogólne)",
        "funkcja": "Wdowa miejska kraśnicka, teściowa Tomasza Kępki",
        "wariant_nazwiska": "Puklina [Krystyna Puklina wdowa / Joanna Krystyna]",
        "wystapienia": [
            {"skan": 7, "rok": "1700", "zapis_oryginalny": "Krystyna Puklina wdowa", "rola": "Pozwana przez parobka Stasia o myto"},
            {"skan": 11, "rok": "1700", "zapis_oryginalny": "Krystyna Puklina Przedmieszczanka", "rola": "Powódka przeciw zięciowi Kępce o zniewagi i bicie córki"},
            {"skan": 16, "rok": "1700", "zapis_oryginalny": "Krystyna Puklina Mieyska Wdowa", "rola": "Protest przeciw zięciowi o obelgi"},
            {"skan": 24, "rok": "1700", "zapis_oryginalny": "Krystyna Puklina wdowa", "rola": "Nakaz sądu pojednania małżeńskiego córki Katarzyny"}
        ]
    },
    {
        "nazwisko": "Kępka",
        "imie": "Tomasz",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki, zięć Krystyny Pukliny",
        "wariant_nazwiska": "Kępka [Thomas Kępka / Kępka]",
        "wystapienia": [
            {"skan": 11, "rok": "1700", "zapis_oryginalny": "Tomasz Kępka zięć", "rola": "Pozwany o pobicie żony i znieważenie teściowej"},
            {"skan": 12, "rok": "1700", "zapis_oryginalny": "Tomasz Kępka", "rola": "Uczestnik bójki w szynku Lejby Markowicza"},
            {"skan": 19, "rok": "1700", "zapis_oryginalny": "Tomasz Kępka", "rola": "Oskarżony o pobicie kosturem Hardysza"},
            {"skan": 24, "rok": "1700", "zapis_oryginalny": "Tomasz Kępka", "rola": "Nakaz sądu przyjęcia żony Katarzyny do domu pod karą więzienia"}
        ]
    },
    {
        "nazwisko": "Kępka",
        "imie": "Katarzyna",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Córka Krystyny Pukliny, żona Tomasza Kępki",
        "wariant_nazwiska": "Kępczyna [Katarzyna Kępczyna / Puklanka]",
        "wystapienia": [
            {"skan": 11, "rok": "1700", "zapis_oryginalny": "Małżonka Katarzyna", "rola": "Bita i wyrzucona z domu przez męża Tomasza"},
            {"skan": 24, "rok": "1700", "zapis_oryginalny": "Katarzyna córka małżonka", "rola": "Powrót do pożycia małżeńskiego nakazem sądu"}
        ]
    },
    {
        "nazwisko": "Klein",
        "imie": "Paweł",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Bedel / sługa miejski ratusza kraśnickiego",
        "wariant_nazwiska": "Klein [Paulus Kleynek / Kleynek]",
        "wystapienia": [
            {"skan": 8, "rok": "1700", "zapis_oryginalny": "Paweł Kleynek sługa mieyski", "rola": "Aresztowanie ruchomości Stawińskiego na ratuszu"}
        ]
    },
    {
        "nazwisko": "Luter",
        "imie": "Stanisław",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki",
        "wariant_nazwiska": "Luter [Stanisław Luterek / Lutrek? / Luter]",
        "wystapienia": [
            {"skan": 11, "rok": "1700", "zapis_oryginalny": "Stanisław Lutrek", "rola": "Pozwany przez Skałkę o awanturę po pogrzebie"}
        ]
    },
    {
        "nazwisko": "Kamiński",
        "imie": "Franciszek",
        "miejsce": "Kraśnik",
        "funkcja": "Mieszkaniec kraśnicki",
        "wariant_nazwiska": "Kamiński [Franciszek Kamiński]",
        "wystapienia": [
            {"skan": 11, "rok": "1700", "zapis_oryginalny": "Franciszek Kamiński", "rola": "Pozwany przez Stanisława Dudka o krwawe rany"}
        ]
    },
    {
        "nazwisko": "Dudek",
        "imie": "Stanisław",
        "miejsce": "Kraśnik",
        "funkcja": "Mieszkaniec kraśnicki, poszkodowany pobiciem",
        "wariant_nazwiska": "Dudek [Stanisław Dudek]",
        "wystapienia": [
            {"skan": 11, "rok": "1700", "zapis_oryginalny": "Stanisław Dudek Aktor", "rola": "Powód o krwawe pobicie przeciw Kamińskiemu"}
        ]
    },
    {
        "nazwisko": "Karbielan",
        "imie": "Wojciech",
        "miejsce": "Kraśnik",
        "funkcja": "Mieszkaniec kraśnicki [pan Urodzony]",
        "wariant_nazwiska": "Karbielan [Wojciech Karbielan]",
        "wystapienia": [
            {"skan": 12, "rok": "1700", "zapis_oryginalny": "Wojciech Karbielan Aktor", "rola": "Powód o kradzież 24 talarów bitych w szynku u żyda Joska"}
        ]
    },
    {
        "nazwisko": "Markowicz",
        "imie": "Lejba",
        "miejsce": "Kraśnik",
        "funkcja": "Żyd szynkarz i karczmarz kraśnicki",
        "wariant_nazwiska": "Markowicz [Leybus Markowicz]",
        "wystapienia": [
            {"skan": 12, "rok": "1700", "zapis_oryginalny": "Leybus Markowicz gospodarz", "rola": "Zeznania o bójce Kępki z Hardyszem w szynku"}
        ]
    },
    {
        "nazwisko": "Kowalik",
        "imie": "Paweł",
        "miejsce": "Kraśnik",
        "funkcja": "Świadek bójki karczemnej",
        "wariant_nazwiska": "Kowalik [Paulus Kowalik]",
        "wystapienia": [
            {"skan": 12, "rok": "1700", "zapis_oryginalny": "Paulus Kowalik", "rola": "Zeznania pod przysięgą o uderzeniu w gębę Kępki"}
        ]
    },
    {
        "nazwisko": "Rycerz",
        "imie": "Jan",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Kowal mieszczanin kraśnicki",
        "wariant_nazwiska": "Rycerz [Joannes Rycerz Kowal / Jan Rycerz]",
        "wystapienia": [
            {"skan": 13, "rok": "1700", "zapis_oryginalny": "Joannes Rycerz Kowal", "rola": "Świadek w sprawie jarmarcznej Rodzonka"},
            {"skan": 22, "rok": "1700", "zapis_oryginalny": "Jan Rycerz Kowal", "rola": "Protest przeciw szewcowi Koziołowi o pobicie w szynku"},
            {"skan": 23, "rok": "1700", "zapis_oryginalny": "Jan Rycerz Kowal", "rola": "Skarga o zamach siekierą przeciw Koziołowi"},
            {"skan": 24, "rok": "1700", "zapis_oryginalny": "Jan Rycerz Kowal", "rola": "Pozwany przez Kozioła o pijaństwo"}
        ]
    },
    {
        "nazwisko": "Rodzonek",
        "imie": "Sobestian",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki, handlarz skórami",
        "wariant_nazwiska": "Rodzonek [Sobestian Rodzonek / Sebastian]",
        "wystapienia": [
            {"skan": 13, "rok": "1700", "zapis_oryginalny": "Sobestian Rodzonek Przedmieszczanin", "rola": "Oskarżony przez Abrama rzeźnika o kradzież konia"},
            {"skan": 19, "rok": "1700", "zapis_oryginalny": "Sobestian Rodzonek", "rola": "Pozwany o kradzież skór wołowych za 70 zł"},
            {"skan": 25, "rok": "1700", "zapis_oryginalny": "Sobestian Rodzonek", "rola": "Prawomocnie uniewinniony od zarzutów żyda Abrama rzeźnika"}
        ]
    },
    {
        "nazwisko": "Abram",
        "imie": "Abram",
        "miejsce": "Kraśnik",
        "funkcja": "Żyd rzeźnik kraśnicki [Abram Lamio]",
        "wariant_nazwiska": "Abram Lamio [Abram Rzeźnik / Abram Michał krupka?]",
        "wystapienia": [
            {"skan": 13, "rok": "1700", "zapis_oryginalny": "Niewierny Abram Rzeźnik", "rola": "Oskarżyciel Rodzonka o kradzież konia"},
            {"skan": 19, "rok": "1700", "zapis_oryginalny": "Abram Lamio Kraśnicensis", "rola": "Pozew o 70 zł za skóry wołowe"},
            {"skan": 25, "rok": "1700", "zapis_oryginalny": "Abram żyd Rzeźnik", "rola": "Przegrana w procesie z Rodzonkiem z braku przysięgi"}
        ]
    },
    {
        "nazwisko": "Tokarczyk",
        "imie": "Andrzej",
        "miejsce": "Kraśnik",
        "funkcja": "Mieszkaniec kraśnicki",
        "wariant_nazwiska": "Tokarczyk [Andrzej Tokarczyk]",
        "wystapienia": [
            {"skan": 14, "rok": "1700", "zapis_oryginalny": "Andrzej Tokarczyk", "rola": "Powód o rąbanie drzewa przeciw Hardyszowi"}
        ]
    },
    {
        "nazwisko": "Tokarczyk",
        "imie": "Piotr",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin, sukcesor Szymona Krasuskiego",
        "wariant_nazwiska": "Tokarczyk [Piotr Tokarczyk]",
        "wystapienia": [
            {"skan": 23, "rok": "1700", "zapis_oryginalny": "Piotr Tokarczyk Przedmieszczanin", "rola": "Pozwany o 12 zł zaległego myta przez Traficę"}
        ]
    },
    {
        "nazwisko": "Onuszkiewicz",
        "imie": "Jan",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Burmistrz kraśnicki",
        "wariant_nazwiska": "Onuszkiewicz [Jan Onuszkiewicz Burmistrz]",
        "wystapienia": [
            {"skan": 10, "rok": "1700", "zapis_oryginalny": "JM Jan Onuszkiewicz Burmistrz", "rola": "Sąsiad roli na Podlesiu"},
            {"skan": 14, "rok": "1700", "zapis_oryginalny": "Jan Onuszkiewicz Burmistrz", "rola": "Rozliczenia młyńskie"},
            {"skan": 15, "rok": "1700", "zapis_oryginalny": "Jan Onuszkiewicz Burmistrz", "rola": "Protest o wypas owiec na folwarku Dzierzkowskim"},
            {"skan": 20, "rok": "1700", "zapis_oryginalny": "Jan Onuszkiewicz Burmistrz", "rola": "Kierowanie urzędową wizją na Podlesiu"}
        ]
    },
    {
        "nazwisko": "Wojtyk",
        "imie": "Jakub",
        "miejsce": "Kraśnik",
        "funkcja": "Obywatel kraśnicki, pasterz owiec",
        "wariant_nazwiska": "Wojtyk [Jakub Woytyk]",
        "wystapienia": [
            {"skan": 15, "rok": "1700", "zapis_oryginalny": "Jakub Woytyk Obywatel", "rola": "Pozwany przez burmistrza o szkodę 6 zł w owcach"}
        ]
    },
    {
        "nazwisko": "Macał",
        "imie": "Józef",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Rzeźnik mieszczanin kraśnicki",
        "wariant_nazwiska": "Macał [Józef Macał Rzeźnik]",
        "wystapienia": [
            {"skan": 15, "rok": "1700", "zapis_oryginalny": "Józef Macał Mieszczanin Rzeźnik", "rola": "Protest przeciw arendarzowi Dawidowiczowi o najście nocne z siekierami"},
            {"skan": 16, "rok": "1700", "zapis_oryginalny": "Józef Macał", "rola": "Dalsze dochodzenie odszkodowania za najście"}
        ]
    },
    {
        "nazwisko": "Macałowa",
        "imie": "Anna",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Mieszczanka kraśnicka, żona rzeźnika Józefa",
        "wariant_nazwiska": "Macałowa [Anna Macałowa / Macał]",
        "wystapienia": [
            {"skan": 15, "rok": "1700", "zapis_oryginalny": "Anna Małżonka", "rola": "Pobita podczas nocnego napadu arendarza"},
            {"skan": 16, "rok": "1700", "zapis_oryginalny": "Anna Małżonka", "rola": "Świadectwo ran i zaboru mienia"}
        ]
    },
    {
        "nazwisko": "Dawidowicz",
        "imie": "Pinchas",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Żyd arendarz kraśnicki, dzierżawca szynków",
        "wariant_nazwiska": "Dawidowicz [Pinchas Dawidowicz Arendarz / Moszko?]",
        "wystapienia": [
            {"skan": 15, "rok": "1700", "zapis_oryginalny": "Dawidowic Arendarz", "rola": "Oskarżony o nocne najście na dom Macałów"},
            {"skan": 17, "rok": "1700", "zapis_oryginalny": "Pinchas Dawidowicz Arendator", "rola": "Proces o potajemny przewóz słodu do Dzierzkowic"},
            {"skan": 22, "rok": "1700", "zapis_oryginalny": "Pinchas Dawidowicz szynkarz", "rola": "Właściciel szynku, w którym pobito kowala Rycerza"}
        ]
    },
    {
        "nazwisko": "Barankiewicz",
        "imie": "Jan",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Burmistrz i radny kraśnicki",
        "wariant_nazwiska": "Barankiewicz [Jan Barankiewicz Burmistrz]",
        "wystapienia": [
            {"skan": 14, "rok": "1700", "zapis_oryginalny": "Jan Barankiewicz Burmistrz", "rola": "Sędzia sesji sądu wójtowskiego"},
            {"skan": 17, "rok": "1700", "zapis_oryginalny": "Joannes Barankiewicz", "rola": "Zarządca funduszy brackich"},
            {"skan": 18, "rok": "1700", "zapis_oryginalny": "Jan Barankiewicz Burmistrz", "rola": "Sędzia w połączonym sądzie wielkim"}
        ]
    },
    {
        "nazwisko": "Peleszkowic",
        "imie": "Jan",
        "miejsce": "Przedmieście Góry i Podlesie",
        "funkcja": "Przedmieszczanin z Podlesia, furman",
        "wariant_nazwiska": "Peleszkowic [Joannes Peleszkowic / Pielaszkowic?]",
        "wystapienia": [
            {"skan": 17, "rok": "1700", "zapis_oryginalny": "Joannes Peleszkowic z Podlesia", "rola": "Zeznania o nocnym przewozie słodu do młyna Dzierzkowskiego"}
        ]
    },
    {
        "nazwisko": "Majowski",
        "imie": "Jan",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Wójt kraśnicki",
        "wariant_nazwiska": "Majowski [Jan Majowski Wójt]",
        "wystapienia": [
            {"skan": 14, "rok": "1700", "zapis_oryginalny": "Jan Majowski Wójt", "rola": "Przewodniczący sądu wójtowskiego"},
            {"skan": 18, "rok": "1700", "zapis_oryginalny": "Jan Majowski Wójt Kraśnicki", "rola": "Przewodniczący Sądu Wielkiego Połączonego"},
            {"skan": 20, "rok": "1700", "zapis_oryginalny": "Jan Majowski Wójt", "rola": "Zarządzenie urzędowej wizji granic na Podlesiu"},
            {"skan": 22, "rok": "1700", "zapis_oryginalny": "Pan Jan Majowski Wójt", "rola": "Obecny przy znieważeniu kuśnierza"}
        ]
    },
    {
        "nazwisko": "Płechowicz",
        "imie": "Stanisław",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Ławnik i deputat Ordynacji Zamojskiej",
        "wariant_nazwiska": "Płechowicz [Stanisław Płechowicz Radny / Płechowicz]",
        "wystapienia": [
            {"skan": 18, "rok": "1700", "zapis_oryginalny": "Stanisław Płechowicz Radny y Deputat", "rola": "Deputat do Sądu Połączonego z Ordynacji Zamojskiej"}
        ]
    },
    {
        "nazwisko": "Piasecki",
        "imie": "Janusz",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Radny i deputat kraśnicki",
        "wariant_nazwiska": "Piasecki [Janusz Piasecki]",
        "wystapienia": [
            {"skan": 18, "rok": "1700", "zapis_oryginalny": "Janusz Piasecki", "rola": "Sędzia sądu połączonego"}
        ]
    },
    {
        "nazwisko": "Piasecki",
        "imie": "Wojciech",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Szafarz miejski kraśnicki",
        "wariant_nazwiska": "Piasecki [Wojciech Piasecki Szafarz]",
        "wystapienia": [
            {"skan": 21, "rok": "1700", "zapis_oryginalny": "Wojciech Piasecki Szafarz Meyjski", "rola": "Pozwany o zajęcie konia i pościeli za podatki"}
        ]
    },
    {
        "nazwisko": "Piasecki",
        "imie": "Franciszek",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Rajca kraśnicki",
        "wariant_nazwiska": "Piasecki [Franciszek Piasecki]",
        "wystapienia": [
            {"skan": 20, "rok": "1700", "zapis_oryginalny": "Franciszek Piasecki", "rola": "Uczestnik urzędowej wizji lokalnej na Podlesiu"}
        ]
    },
    {
        "nazwisko": "Borowiecki",
        "imie": "Wojciech",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Ławnik kraśnicki",
        "wariant_nazwiska": "Borowiecki [Wojciech Borowiecki Ławnik]",
        "wystapienia": [
            {"skan": 20, "rok": "1700", "zapis_oryginalny": "Wojciech Borowiecki Ławnik", "rola": "Uczestnik urzędowej wizji granic na Podlesiu"}
        ]
    },
    {
        "nazwisko": "Rymarczyk",
        "imie": "Marcin",
        "miejsce": "Przedmieście Piaski",
        "funkcja": "Wójt przedmieścia Piaski, rymarz",
        "wariant_nazwiska": "Rymarczyk [Marcin Rymarczyk Wójt Piasków]",
        "wystapienia": [
            {"skan": 18, "rok": "1700", "zapis_oryginalny": "Marcin Rymarczyk Wójt Przedmieścia Piasek", "rola": "Powód o zniewagi przeciw Zielińskiemu"},
            {"skan": 24, "rok": "1700", "zapis_oryginalny": "Marcin Rymarczyk", "rola": "Pozwany przez żyda Borucha o suknię ze straganu"},
            {"skan": 25, "rok": "1700", "zapis_oryginalny": "Marcin Rymarczyk", "rola": "Nakaz zwrotu sukni 13 złp lub pieniędzy"}
        ]
    },
    {
        "nazwisko": "Dudonek",
        "imie": "Szymon",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin, świadek pobicia",
        "wariant_nazwiska": "Dudonek [Simon Dudonek]",
        "wystapienia": [
            {"skan": 19, "rok": "1700", "zapis_oryginalny": "Simon Dudonek", "rola": "Zeznania pod przysięgą o uderzeniu kosturem w plecy"}
        ]
    },
    {
        "nazwisko": "Stary",
        "imie": "Marcin",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki [bratek]",
        "wariant_nazwiska": "Stary bratek [Martinus Stary bratek / Marcin Stary]",
        "wystapienia": [
            {"skan": 19, "rok": "1700", "zapis_oryginalny": "Martinus Stary bratek", "rola": "Świadek krwawej bójki pod karczmą"}
        ]
    },
    {
        "nazwisko": "Dymarek",
        "imie": "Marcin",
        "miejsce": "Kraśnik",
        "funkcja": "Gospodarz kraśnicki, poszkodowany kradzieżą",
        "wariant_nazwiska": "Dymarek [Marcin Dymarek]",
        "wystapienia": [
            {"skan": 21, "rok": "1700", "zapis_oryginalny": "Marcin Dymarek", "rola": "Kradzież wozów na szkodę gospodarza"}
        ]
    },
    {
        "nazwisko": "Lenkiewicz",
        "imie": "Jakub",
        "miejsce": "Kraśnik",
        "funkcja": "Mieszkaniec kraśnicki",
        "wariant_nazwiska": "Lenkiewicz [Jakubus Lenkiewicz]",
        "wystapienia": [
            {"skan": 21, "rok": "1700", "zapis_oryginalny": "Jakubus Lenkiewicz", "rola": "Świadek kradzieży wozów u Dymarka"}
        ]
    },
    {
        "nazwisko": "Józefowa",
        "imie": "Anna",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Wdowa po zmarłym burmistrzu Józefie kraśnickim",
        "wariant_nazwiska": "Józefowa [Anna Józefowa wdowa]",
        "wystapienia": [
            {"skan": 21, "rok": "1700", "zapis_oryginalny": "Anna Józefowa onegdys Burmistrza Małżonka wdowa", "rola": "Protest o prawo do kamienicy po bracie matki"}
        ]
    },
    {
        "nazwisko": "Szymałowski",
        "imie": "Wojciech",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Burmistrz kraśnicki",
        "wariant_nazwiska": "Szymałowski [Wojciech Szymałowski Burmistrz]",
        "wystapienia": [
            {"skan": 21, "rok": "1700", "zapis_oryginalny": "JM Pan Wojciech Szymałowski Burmistrz", "rola": "Zajęcie placu kamienicznego"}
        ]
    },
    {
        "nazwisko": "Kozioł",
        "imie": "Kazimierz",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Szewc przedmieszczanin kraśnicki",
        "wariant_nazwiska": "Kozioł [Kazimierz Kozieł / Koźlak / Szewc]",
        "wystapienia": [
            {"skan": 22, "rok": "1700", "zapis_oryginalny": "Kazimierz Kozioł Szewc", "rola": "Oskarżony o pobicie kowala Rycerza i kuśnierza"},
            {"skan": 23, "rok": "1700", "zapis_oryginalny": "Kazimierz Kozioł szewc", "rola": "Pozwany o zamach siekierą"},
            {"skan": 24, "rok": "1700", "zapis_oryginalny": "Jan Kaźmirz Kozieł Szewc", "rola": "Wzajemna protestacja o pijaństwo w szynku"}
        ]
    },
    {
        "nazwisko": "Matysikowic",
        "imie": "Tomasz",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Krawiec mieszczanin kraśnicki",
        "wariant_nazwiska": "Matysikowic [Tomasz Matysikowic Krawiec]",
        "wystapienia": [
            {"skan": 22, "rok": "1700", "zapis_oryginalny": "Tomasz Matysikowic Krawiec", "rola": "Protest przeciw podstarościemu o pobicie kijem na pogrzebie"}
        ]
    },
    {
        "nazwisko": "Krasuski",
        "imie": "Kazimierz",
        "miejsce": "Kraśnik (zamek / dwór)",
        "funkcja": "Podstarości kraśnicki",
        "wariant_nazwiska": "Krasuski [Kazimierz Krasuski Podstarości]",
        "wystapienia": [
            {"skan": 22, "rok": "1700", "zapis_oryginalny": "Kazimierz Krasuski Podstarości", "rola": "Uderzenie kijem krawca na kondukcie pogrzebowym"}
        ]
    },
    {
        "nazwisko": "Kuśnierz",
        "imie": "Wojciech",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Kuśnierz mieszczanin kraśnicki",
        "wariant_nazwiska": "Kuśnierz [Wojciech Kuśnierz]",
        "wystapienia": [
            {"skan": 22, "rok": "1700", "zapis_oryginalny": "Wojciech Kuśnierz Mieszczanin", "rola": "Znieważony w obecności wójta przez szewca Kozioła"}
        ]
    },
    {
        "nazwisko": "Kłopot",
        "imie": "Jakub",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki, brat Wojciecha",
        "wariant_nazwiska": "Kłopot [Jakub Kłopot]",
        "wystapienia": [
            {"skan": 23, "rok": "1700", "zapis_oryginalny": "Jakub Kłopot", "rola": "Oskarżony o kradzież tuczonego wieprza za 7 zł"}
        ]
    },
    {
        "nazwisko": "Kłopot",
        "imie": "Wojciech",
        "miejsce": "Przedmieście Kraśnickie",
        "funkcja": "Przedmieszczanin kraśnicki, brat Jakuba",
        "wariant_nazwiska": "Kłopot [Wojciech Kłopot]",
        "wystapienia": [
            {"skan": 23, "rok": "1700", "zapis_oryginalny": "Wojciech Kłopot", "rola": "Oskarżony wraz z bratem o kradzież wieprza"}
        ]
    },
    {
        "nazwisko": "Boruch",
        "imie": "Boruch",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Żyd kupiec kramarz kraśnicki",
        "wariant_nazwiska": "Boruch żyd [Boruch żyd Kraśnicki]",
        "wystapienia": [
            {"skan": 24, "rok": "1700", "zapis_oryginalny": "Niewierny Boruch żyd", "rola": "Powód o kradzież sukni targowej ze straganu"},
            {"skan": 25, "rok": "1700", "zapis_oryginalny": "Niewierny żyd Boruch Obywatel", "rola": "Wyrok nakazujący zwrot sukni 13 złp przez Rymarczyka"}
        ]
    },
    {
        "nazwisko": "Borek",
        "imie": "Matyasz",
        "miejsce": "Miasto Kraśnik",
        "funkcja": "Mieszczanin kraśnicki",
        "wariant_nazwiska": "Borek [Matyasz Borek Mieszczanin]",
        "wystapienia": [
            {"skan": 25, "rok": "1700", "zapis_oryginalny": "Matyasz Borek Mieszczanin", "rola": "Urzędowy zapis w księdze wójtowskiej"}
        ]
    }
]

# Normalizacja i przypisanie pól zgodnie z J40
gen_data = []
for idx, p in enumerate(raw_persons, 1):
    p["lp"] = idx
    p["skany_list"] = [int(w["skan"]) for w in p["wystapienia"]]
    p["skany_roboczo"] = ", ".join([f"#{s}" for s in p["skany_list"]])
    years = [w["rok"] for w in p["wystapienia"]]
    p["zakres_lat"] = f"{min(years)}–{max(years)}" if len(set(years)) > 1 else years[0]
    p["liczba_wystapien"] = len(p["wystapienia"])
    gen_data.append(p)

print(f"Extracted {len(gen_data)} unique persons for Partia 1 (Variant 2).")

# Zapis do JSON
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part1.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

# Eksport do CSV (UTF-8-SIG, 9 kolumn, separator ;)
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
headers = ["Lp", "Nazwisko", "Imię", "Miejsce", "Funkcja społeczna / zawód", "Skany źródłowe", "Zakres lat", "Liczba wzmianek", "Warianty nazwiska"]

with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(headers)
    for p in gen_data:
        writer.writerow([
            p["lp"],
            p["nazwisko"],
            p["imie"],
            p["miejsce"],
            p["funkcja"],
            p["skany_roboczo"],
            p["zakres_lat"],
            p["liczba_wystapien"],
            p["wariant_nazwiska"]
        ])

print(f"Exported CSV successfully to {csv_path}")
