import json

nowe_profile = [
    {
        "lp": 831,
        "nazwisko": "Krajewski",
        "wariant_nazwiska": "Krajewski / Krayewski / Grzegorz Krayewski / Grzegorz Krajewski",
        "imie": "Grzegorz",
        "przydomek": "",
        "funkcja": "Szewc / Mieszkaniec (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#180",
        "skany_list": [180],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Krajewski", "imie": "Grzegorz", "miejsce": "Śródmieście", "rola": "Szewc upomniany karnie", "skan": 180, "rok": "1779", "zapis_oryginalny": "Grzegorz Krayewski", "kwota_ctx": "Dekret karny"}
        ],
        "uwagi": "Szewc kraśnicki ukarany dyscyplinarnie przez sędziego Wyszyńskiego 26 XI 1779 r. za pijaństwo i pobicie żony, pod rygorem dyb i 50 plag."
    },
    {
        "lp": 832,
        "nazwisko": "Krajewska",
        "wariant_nazwiska": "Krajewska / Żona Grzegorza Krajewskiego / Żonie swoiey",
        "imie": "[N.]",
        "przydomek": "",
        "funkcja": "Mieszkanka (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#180",
        "skany_list": [180],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Krajewska", "imie": "[N.]", "miejsce": "Śródmieście", "rola": "Ofiara pobicia domowego", "skan": 180, "rok": "1779", "zapis_oryginalny": "Grzegorz Kraiewski Żonie swoiey Rękę skaleczył", "kwota_ctx": "Sprawa karna"}
        ],
        "uwagi": "Żona szewca Grzegorza Krajewskiego, ofiara pobicia (skaleczenie ręki) odnotowana w dekrecie sądowym sędziego Wyszyńskiego 26 XI 1779 r."
    },
    {
        "lp": 833,
        "nazwisko": "Bora",
        "wariant_nazwiska": "Bora / Jędrzejowa Bora / Jędrzeyowey Borze / Bora Wdowa",
        "imie": "Jędrzejowa [Wdowa]",
        "przydomek": "",
        "funkcja": "Mieszkanka (wdowa) (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#174",
        "skany_list": [174],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Bora", "imie": "Jędrzejowa [Wdowa]", "miejsce": "Śródmieście", "rola": "Wierzycielka kasy miejskiej", "skan": 174, "rok": "1779", "zapis_oryginalny": "Jędrzeyowey Borze wdowie", "kwota_ctx": "12 zł długu"}
        ],
        "uwagi": "Wdowa po Jędrzeju Borze, wierzycielka kasy miejskiej Kraśnika na sumę 12 zł za żupan i wyprawę do Kielc po kamień."
    },
    {
        "lp": 834,
        "nazwisko": "Trojanowicz",
        "wariant_nazwiska": "Trojanowicz / Wolew Trojanowicz / Wolew Troianowicz / Troymowicz / Trojanowicz starozakonny",
        "imie": "Wolew",
        "przydomek": "",
        "funkcja": "Podstarszy cechmistrz kuśnierski (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#182",
        "skany_list": [182],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Trojanowicz", "imie": "Wolew", "miejsce": "Śródmieście", "rola": "Podstarszy cechu kuśnierskiego", "skan": 182, "rok": "1779", "zapis_oryginalny": "Wolew Troianowicz", "kwota_ctx": "Cech kuśnierski"}
        ],
        "uwagi": "Kuśnierz starozakonny wybrany 27 XI 1779 r. na podstarszego cechu kuśnierskiego w Kraśniku u boku Grzegorza Zdyba."
    },
    {
        "lp": 835,
        "nazwisko": "Rosicki",
        "wariant_nazwiska": "Rosicki / Jakob Rosicki / Jakub Rosicki",
        "imie": "Jakub",
        "przydomek": "",
        "funkcja": "Mieszkaniec centrum (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#176",
        "skany_list": [176],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Rosicki", "imie": "Jakub", "miejsce": "Śródmieście", "rola": "Płatnik sympli", "skan": 176, "rok": "1779", "zapis_oryginalny": "Jakob Rosicki", "kwota_ctx": "5 gr"}
        ],
        "uwagi": "Posesjonat w Śródmieściu Kraśnika płacący symplę 5 gr w rejestrze z 26 XI 1779 r."
    },
    {
        "lp": 836,
        "nazwisko": "Pachciarz",
        "wariant_nazwiska": "Pachciarz / Pachciarzowa Wdowa / Pachciarz Wdowa",
        "imie": "[Wdowa]",
        "przydomek": "",
        "funkcja": "Mieszkanka centrum (wdowa) (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#176",
        "skany_list": [176],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Pachciarz", "imie": "[Wdowa]", "miejsce": "Śródmieście", "rola": "Płatniczka sympli", "skan": 176, "rok": "1779", "zapis_oryginalny": "Pachciarzowa Wdowa", "kwota_ctx": "1 gr"}
        ],
        "uwagi": "Wdowa po pachciarzu miejskim ujęta w rejestrze sympli z 1779 r. ze stawką 1 gr."
    },
    {
        "lp": 837,
        "nazwisko": "Podstolski",
        "wariant_nazwiska": "Podstolski / Piotr Podstolski",
        "imie": "Piotr",
        "przydomek": "",
        "funkcja": "Mieszkaniec centrum (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#176",
        "skany_list": [176],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Podstolski", "imie": "Piotr", "miejsce": "Śródmieście", "rola": "Płatnik sympli", "skan": 176, "rok": "1779", "zapis_oryginalny": "Piotr Podstolski", "kwota_ctx": "6 gr"}
        ],
        "uwagi": "Posesjonat w centrum Kraśnika opodatkowany kwotą 6 gr w taryfie sympli z 1779 r."
    },
    {
        "lp": 838,
        "nazwisko": "Stanisz",
        "wariant_nazwiska": "Stanisz / Wawrzyniec Stanisz",
        "imie": "Wawrzyniec",
        "przydomek": "",
        "funkcja": "Posesjonat / Kupiec centrum (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#176",
        "skany_list": [176],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Stanisz", "imie": "Wawrzyniec", "miejsce": "Śródmieście", "rola": "Posesjonat opodatkowany", "skan": 176, "rok": "1779", "zapis_oryginalny": "Wawrzyniec Stanisz", "kwota_ctx": "7 zł 1½ gr"}
        ],
        "uwagi": "Znaczniejszy posesjonat w Rynku kraśnickim płacący najwyższą stawkę sympli 7 zł 1½ gr w 1779 r."
    },
    {
        "lp": 839,
        "nazwisko": "Rzęcimorski",
        "wariant_nazwiska": "Rzęcimorski / Mikołay Rzęcimorski / Mikołaj Rzęcimorski",
        "imie": "Mikołaj",
        "przydomek": "",
        "funkcja": "Mieszkaniec centrum (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#177",
        "skany_list": [177],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Rzęcimorski", "imie": "Mikołaj", "miejsce": "Śródmieście", "rola": "Płatnik sympli", "skan": 177, "rok": "1779", "zapis_oryginalny": "Mikołay Rzęcimorski", "kwota_ctx": "1 zł"}
        ],
        "uwagi": "Mieszkaniec Kraśnika płacący 1 zł sympli miejskiej w 1779 r."
    },
    {
        "lp": 840,
        "nazwisko": "Piątkowski",
        "wariant_nazwiska": "Piątkowski / Piatkowski / Woyciech Piatkowski / Wojciech Piątkowski",
        "imie": "Wojciech",
        "przydomek": "",
        "funkcja": "Mieszkaniec centrum (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#177",
        "skany_list": [177],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Piątkowski", "imie": "Wojciech", "miejsce": "Śródmieście", "rola": "Płatnik sympli", "skan": 177, "rok": "1779", "zapis_oryginalny": "Woyciech Piatkowski", "kwota_ctx": "2 gr"}
        ],
        "uwagi": "Mieszkaniec Śródmieścia ujęty w rejestrze sympli z 1779 r. ze stawką 2 gr."
    },
    {
        "lp": 841,
        "nazwisko": "Królicka",
        "wariant_nazwiska": "Królicka / Krulicka / Jakubowa Krulicka / Królicka Wdowa",
        "imie": "Jakubowa [Wdowa]",
        "przydomek": "",
        "funkcja": "Mieszkanka przedmiejska (wdowa) (1779)",
        "miejsce": "Przedmieście Piasek",
        "skany_roboczo": "#177",
        "skany_list": [177],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Królicka", "imie": "Jakubowa [Wdowa]", "miejsce": "Przedmieście Piasek", "rola": "Płatniczka sympli", "skan": 177, "rok": "1779", "zapis_oryginalny": "Jakubowa Krulicka", "kwota_ctx": "7½ gr"}
        ],
        "uwagi": "Wdowa po Jakubie Królickim na Przedmieściu Piasek płacąca 7½ gr sympli w 1779 r."
    },
    {
        "lp": 842,
        "nazwisko": "Ciurka",
        "wariant_nazwiska": "Ciurka / Ciurkowa Wdowa / Ciurkowa / Ciurka Wdowa",
        "imie": "[Wdowa]",
        "przydomek": "",
        "funkcja": "Mieszkanka przedmiejska (wdowa) (1779)",
        "miejsce": "Przedmieście Piasek",
        "skany_roboczo": "#178",
        "skany_list": [178],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Ciurka", "imie": "[Wdowa]", "miejsce": "Przedmieście Piasek", "rola": "Płatniczka sympli", "skan": 178, "rok": "1779", "zapis_oryginalny": "Ciurkowa Wdowa", "kwota_ctx": "12 gr"}
        ],
        "uwagi": "Wdowa po Ciurce na Przedmieściu Piasek notowana w sympli 1779 r. ze składką 12 gr."
    },
    {
        "lp": 843,
        "nazwisko": "Jęczorek",
        "wariant_nazwiska": "Jęczorek / Wawrzyniec Jęczorek",
        "imie": "Wawrzyniec",
        "przydomek": "",
        "funkcja": "Gospodarz przedmiejski (1779)",
        "miejsce": "Przedmieście Piasek",
        "skany_roboczo": "#178",
        "skany_list": [178],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Jęczorek", "imie": "Wawrzyniec", "miejsce": "Przedmieście Piasek", "rola": "Płatnik sympli", "skan": 178, "rok": "1779", "zapis_oryginalny": "Wawrzyniec Jęczorek", "kwota_ctx": "12 gr"}
        ],
        "uwagi": "Gospodarz na Przedmieściu Piasek płacący 12 gr sympli w 1779 r."
    },
    {
        "lp": 844,
        "nazwisko": "Rądrab",
        "wariant_nazwiska": "Rądrab / Tomasz Rądrab / Rondrab / Rądrąb",
        "imie": "Tomasz",
        "przydomek": "",
        "funkcja": "Gospodarz przedmiejski (1779)",
        "miejsce": "Przedmieście Góry i Podlesie",
        "skany_roboczo": "#179",
        "skany_list": [179],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Rądrab", "imie": "Tomasz", "miejsce": "Przedmieście Góry i Podlesie", "rola": "Płatnik sympli", "skan": 179, "rok": "1779", "zapis_oryginalny": "Tomasz Rądrab", "kwota_ctx": "15 gr"}
        ],
        "uwagi": "Gospodarz na Górach i Podlesiu opodatkowany symplą 15 gr w rejestrze z 26 XI 1779 r."
    },
    {
        "lp": 845,
        "nazwisko": "Cukierka",
        "wariant_nazwiska": "Cukierka / Szymon Cukierka",
        "imie": "Szymon",
        "przydomek": "",
        "funkcja": "Gospodarz przedmiejski (1779)",
        "miejsce": "Przedmieście Góry i Podlesie",
        "skany_roboczo": "#179",
        "skany_list": [179],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Cukierka", "imie": "Szymon", "miejsce": "Przedmieście Góry i Podlesie", "rola": "Płatnik sympli", "skan": 179, "rok": "1779", "zapis_oryginalny": "Szymon Cukierka", "kwota_ctx": "14 gr"}
        ],
        "uwagi": "Posesjonat w dzielnicy Góry i Podlesie płacący 14 gr sympli w 1779 r."
    },
    {
        "lp": 846,
        "nazwisko": "Bułka",
        "wariant_nazwiska": "Bułka / Tomasz Bułka / Tomek Bułka",
        "imie": "Tomasz",
        "przydomek": "",
        "funkcja": "Gospodarz przedmiejski (1779)",
        "miejsce": "Przedmieście Góry i Podlesie",
        "skany_roboczo": "#179",
        "skany_list": [179],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Bułka", "imie": "Tomasz", "miejsce": "Przedmieście Góry i Podlesie", "rola": "Płatnik sympli", "skan": 179, "rok": "1779", "zapis_oryginalny": "Tomek Bułka", "kwota_ctx": "13 gr"}
        ],
        "uwagi": "Gospodarz na Górach i Podlesiu płacący 13 gr sympli w 1779 r."
    },
    {
        "lp": 847,
        "nazwisko": "Gąska",
        "wariant_nazwiska": "Gąska / Franciszek Gąska / Franek Gąska",
        "imie": "Franciszek",
        "przydomek": "",
        "funkcja": "Gospodarz przedmiejski (1779)",
        "miejsce": "Przedmieście Góry i Podlesie",
        "skany_roboczo": "#179",
        "skany_list": [179],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Gąska", "imie": "Franciszek", "miejsce": "Przedmieście Góry i Podlesie", "rola": "Płatnik sympli", "skan": 179, "rok": "1779", "zapis_oryginalny": "Franek Gąska", "kwota_ctx": "10 gr"}
        ],
        "uwagi": "Mieszkaniec dzielnicy Góry i Podlesie ujęty w rejestrze sympli z 1779 r."
    },
    {
        "lp": 848,
        "nazwisko": "Zięba",
        "wariant_nazwiska": "Zięba / Walenty Zięba / Walwet Ziębica / Ziębica",
        "imie": "Walenty",
        "przydomek": "",
        "funkcja": "Gospodarz przedmiejski (1779)",
        "miejsce": "Przedmieście Góry i Podlesie",
        "skany_roboczo": "#179",
        "skany_list": [179],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Zięba", "imie": "Walenty", "miejsce": "Przedmieście Góry i Podlesie", "rola": "Płatnik sympli", "skan": 179, "rok": "1779", "zapis_oryginalny": "Walwet Ziębica", "kwota_ctx": "9 gr"}
        ],
        "uwagi": "Gospodarz na Górach i Podlesiu notowany w rejestrze symplowym z 1779 r."
    },
    {
        "lp": 849,
        "nazwisko": "Dejka",
        "wariant_nazwiska": "Dejka / Kazimierz Dejka / Kazimierz Deyka / Deyka",
        "imie": "Kazimierz",
        "przydomek": "",
        "funkcja": "Gospodarz przedmiejski (1779)",
        "miejsce": "Przedmieście Piasek",
        "skany_roboczo": "#178",
        "skany_list": [178],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Dejka", "imie": "Kazimierz", "miejsce": "Przedmieście Piasek", "rola": "Płatnik sympli", "skan": 178, "rok": "1779", "zapis_oryginalny": "Kazimierz Deyka", "kwota_ctx": "7½ gr"}
        ],
        "uwagi": "Gospodarz na Przedmieściu Piasek opodatkowany kwotą 7½ gr sympli w 1779 r."
    },
    {
        "lp": 850,
        "nazwisko": "Laszczyk",
        "wariant_nazwiska": "Laszczyk / Laszczykowa Wdowa / Laszczyka Wdowa",
        "imie": "[Wdowa]",
        "przydomek": "",
        "funkcja": "Mieszkanka przedmiejska (wdowa) (1779)",
        "miejsce": "Przedmieście Piasek",
        "skany_roboczo": "#178",
        "skany_list": [178],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Laszczyk", "imie": "[Wdowa]", "miejsce": "Przedmieście Piasek", "rola": "Płatniczka sympli", "skan": 178, "rok": "1779", "zapis_oryginalny": "Laszczyka Wdowa", "kwota_ctx": "7½ gr"}
        ],
        "uwagi": "Wdowa na Przedmieściu Piasek płacąca 7½ gr sympli w 1779 r."
    },
    {
        "lp": 851,
        "nazwisko": "Zarzycka",
        "wariant_nazwiska": "Zarzycka / Zarzycka Wdowa / Michałowa Zariska",
        "imie": "Michałowa [Wdowa]",
        "przydomek": "",
        "funkcja": "Mieszkanka centrum (wdowa) (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#177",
        "skany_list": [177],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Zarzycka", "imie": "Michałowa [Wdowa]", "miejsce": "Śródmieście", "rola": "Płatniczka sympli", "skan": 177, "rok": "1779", "zapis_oryginalny": "Michałowa Zariska", "kwota_ctx": "6 gr"}
        ],
        "uwagi": "Wdowa po Michale Zarzyckim w Śródmieściu Kraśnika notowana w sympli 1779 r."
    },
    {
        "lp": 852,
        "nazwisko": "Stachera",
        "wariant_nazwiska": "Stachera / Stachera Wdowa / Stacherwa Wdowa",
        "imie": "[Wdowa]",
        "przydomek": "",
        "funkcja": "Mieszkanka przedmiejska (wdowa) (1779)",
        "miejsce": "Przedmieście Piasek",
        "skany_roboczo": "#178",
        "skany_list": [178],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Stachera", "imie": "[Wdowa]", "miejsce": "Przedmieście Piasek", "rola": "Płatniczka sympli", "skan": 178, "rok": "1779", "zapis_oryginalny": "Stacherwa Wdowa", "kwota_ctx": "12 gr"}
        ],
        "uwagi": "Wdowa po Stacherze na Przedmieściu Piasek ujęta w sympli z 1779 r."
    },
    {
        "lp": 853,
        "nazwisko": "Tarnawska",
        "wariant_nazwiska": "Tarnawska / Antoniowa Tarnawska / Tarnawska Wdowa",
        "imie": "Antoniowa [Wdowa]",
        "przydomek": "",
        "funkcja": "Mieszkanka centrum (wdowa) (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#176",
        "skany_list": [176],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Tarnawska", "imie": "Antoniowa [Wdowa]", "miejsce": "Śródmieście", "rola": "Płatniczka sympli", "skan": 176, "rok": "1779", "zapis_oryginalny": "Antoniowa Tarnawska", "kwota_ctx": "2 gr"}
        ],
        "uwagi": "Wdowa w centrum Kraśnika płacąca 2 gr sympli miejskiej w 1779 r."
    }
]

with open('/home/ubuntu/workspace/Gen/part10_new_profiles.json', 'w', encoding='utf-8') as f:
    json.dump(nowe_profile, f, ensure_ascii=False, indent=2)

print(f"Zapisano part10_new_profiles.json z {len(nowe_profile)} profilami (lp {nowe_profile[0]['lp']}-{nowe_profile[-1]['lp']})!")
