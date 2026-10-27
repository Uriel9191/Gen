import json

nowe_profile = [
    {
        "lp": 816,
        "nazwisko": "Wilczyński",
        "wariant_nazwiska": "Wilczynski / Franciszek Wilczyński / Franciszek Wileński / Wileński / Exaktor",
        "imie": "Franciszek",
        "przydomek": "",
        "funkcja": "Egzaktor miejski (1778–1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#147, #160, #161, #162, #165",
        "skany_list": [147, 160, 161, 162, 165],
        "zakres_lat": "1778–1779",
        "min_rok": 1778,
        "max_rok": 1779,
        "liczba_wystapien": 5,
        "wystapienia": [
            {"nazwisko": "Wilczyński", "imie": "Franciszek", "miejsce": "Śródmieście", "rola": "Egzaktor miejski zaprzysiężony", "skan": 147, "rok": "1778", "zapis_oryginalny": "Franciszek Wilczynski Juravit", "kwota_ctx": "Urząd"},
            {"nazwisko": "Wilczyński", "imie": "Franciszek", "miejsce": "Śródmieście", "rola": "Egzaktor zdający rachunki", "skan": 160, "rok": "1779", "zapis_oryginalny": "Franciszek Wilczyński", "kwota_ctx": "Sesja"},
            {"nazwisko": "Wilczyński", "imie": "Franciszek", "miejsce": "Śródmieście", "rola": "Egzaktor podający Perceptę", "skan": 161, "rok": "1779", "zapis_oryginalny": "Franciszek Wilczyński", "kwota_ctx": "5088 zł 17 gr"},
            {"nazwisko": "Wilczyński", "imie": "Franciszek", "miejsce": "Śródmieście", "rola": "Egzaktor podający Expensę", "skan": 162, "rok": "1779", "zapis_oryginalny": "Franciszek Wilczyński", "kwota_ctx": "369 zł 15 gr"},
            {"nazwisko": "Wilczyński", "imie": "Franciszek", "miejsce": "Śródmieście", "rola": "Egzaktor kwitowany z urzędu", "skan": 165, "rok": "1779", "zapis_oryginalny": "Franciszek Wilczyński", "kwota_ctx": "100 zł pensji"}
        ],
        "uwagi": "Nowy egzaktor miejski wybrany i zaprzysiężony 3 IV 1778 r. wspólnie z Kazimierzem Rycerzem pod komisarzem Karolem Lipskim; prowadził kasę miejską do 26 XI 1779 r."
    },
    {
        "lp": 817,
        "nazwisko": "Wilczyński",
        "wariant_nazwiska": "Wilczynski / Jan Wilczyński",
        "imie": "Jan",
        "przydomek": "",
        "funkcja": "Mieszczanin / Kandydat na burmistrza (1778)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#146",
        "skany_list": [146],
        "zakres_lat": "1778",
        "min_rok": 1778,
        "max_rok": 1778,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Wilczyński", "imie": "Jan", "miejsce": "Śródmieście", "rola": "Kandydat na urząd burmistrza", "skan": 146, "rok": "1778", "zapis_oryginalny": "Jan Wilczynski", "kwota_ctx": "Elekcja"}
        ],
        "uwagi": "Jeden z czterech kandydatów wysuniętych przez pospólstwo kraśnickie na urząd burmistrza 3 IV 1778 r."
    },
    {
        "lp": 818,
        "nazwisko": "Wadowicz",
        "wariant_nazwiska": "Eliasz Wadowicz / Eli Wadowicz / Eli / Wadowicz niewierny",
        "imie": "Eliasz",
        "przydomek": "Eli",
        "funkcja": "Cechmistrz podstarszy kuśnierski (1778)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#159",
        "skany_list": [159],
        "zakres_lat": "1778",
        "min_rok": 1778,
        "max_rok": 1778,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Wadowicz", "imie": "Eliasz", "miejsce": "Śródmieście", "rola": "Podstarszy cechu kuśnierskiego", "skan": 159, "rok": "1778", "zapis_oryginalny": "Eli Wadowicz", "kwota_ctx": "Cech kuśnierski"}
        ],
        "uwagi": "Kuśnierz starozakonny obrany podstarszym (młodszym) cechmistrzem cechu kuśnierskiego 28 X 1778 r. u boku Grzegorza Zdybickiego."
    },
    {
        "lp": 819,
        "nazwisko": "Lewkowicz",
        "wariant_nazwiska": "Herszek Lewkowicz / Herszek / Lewkowicz starozakonny",
        "imie": "Herszek",
        "przydomek": "",
        "funkcja": "Cechmistrz starszy krawiecki żydowski (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#159",
        "skany_list": [159],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Lewkowicz", "imie": "Herszek", "miejsce": "Śródmieście", "rola": "Starszy krawców żydowskich", "skan": 159, "rok": "1779", "zapis_oryginalny": "Herszek Lewkowicz", "kwota_ctx": "Cech krawiecki"}
        ],
        "uwagi": "Cechmistrz krawiecki wybrany 12 IV 1779 r. ze strony krawców żydowskich do wspólnego chrześcijańsko-żydowskiego zarządu cechu krawieckiego w Kraśniku u boku Jakuba Grzymka."
    },
    {
        "lp": 820,
        "nazwisko": "Ciutkowski",
        "wariant_nazwiska": "Ciutkowski / Dawny Dyrektor Szkoły / Ciutkowskiego",
        "imie": "[N.]",
        "przydomek": "",
        "funkcja": "Dyrektor Szkoły Miejskiej (1778)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#164",
        "skany_list": [164],
        "zakres_lat": "1778–1779",
        "min_rok": 1778,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Ciutkowski", "imie": "[N.]", "miejsce": "Śródmieście", "rola": "Zbiegły dyrektor szkoły miejskiej", "skan": 164, "rok": "1779", "zapis_oryginalny": "Dyrektora dawnego Ciutkowskiego", "kwota_ctx": "8 zł reszty"}
        ],
        "uwagi": "Pierwszy nauczyciel nowo erygowanej Szkoły Miejskiej na Bramie Murowanej, który zbiegł ze służby; resztę jego pensji 8 zł wypłacono sukcesorom."
    },
    {
        "lp": 821,
        "nazwisko": "Ciałkowski",
        "wariant_nazwiska": "Ciałkowski / P. Ciałkowski / Ciałkowskiego",
        "imie": "[N.]",
        "przydomek": "",
        "funkcja": "Obywatel / Pośrednik (1779)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#164",
        "skany_list": [164],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Ciałkowski", "imie": "[N.]", "miejsce": "Śródmieście", "rola": "Pośrednik przy wypłacie pensji szkolnej", "skan": 164, "rok": "1779", "zapis_oryginalny": "P. Ciałkowski", "kwota_ctx": "8 zł"}
        ],
        "uwagi": "Mieszkaniec Kraśnika lub urzędnik, za pośrednictwem którego uregulowano należność po zbiegłym dyrektorze szkoły Ciutkowskim."
    },
    {
        "lp": 822,
        "nazwisko": "Grodzicki",
        "wariant_nazwiska": "Grodzicki / Jan Grodzicki / Pisarz Prowentowy Zamoyski",
        "imie": "Jan",
        "przydomek": "",
        "funkcja": "Pisarz prowentowy Ordynacji Zamojskiej (1778–1779)",
        "miejsce": "Zamość",
        "skany_roboczo": "#164",
        "skany_list": [164],
        "zakres_lat": "1778–1779",
        "min_rok": 1778,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Grodzicki", "imie": "Jan", "miejsce": "Zamość", "rola": "Pisarz prowentowy zamojski", "skan": 164, "rok": "1779", "zapis_oryginalny": "Jan Grodzicki Pisarz Prowentowy", "kwota_ctx": "200 zł parkanowego"}
        ],
        "uwagi": "Urzędnik skarbowy Ordynacji Zamojskiej w Zamościu, odbierający od władz Kraśnika roczny podatek parkanowy na sumę 200 zł."
    },
    {
        "lp": 823,
        "nazwisko": "Skrzelowski",
        "wariant_nazwiska": "Skrzelowski / Ekonom Zamkowy / Skrzelowskiego",
        "imie": "[N.]",
        "przydomek": "",
        "funkcja": "Ekonom zamkowy kraśnicki (1779)",
        "miejsce": "Zamek Kraśnicki",
        "skany_roboczo": "#164",
        "skany_list": [164],
        "zakres_lat": "1779",
        "min_rok": 1779,
        "max_rok": 1779,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Skrzelowski", "imie": "[N.]", "miejsce": "Zamek Kraśnicki", "rola": "Ekonom zamkowy ordynacki", "skan": 164, "rok": "1779", "zapis_oryginalny": "Pan Ekonom Skrzelowski", "kwota_ctx": "25 zł kolędy"}
        ],
        "uwagi": "Ekonom ordynacki na zamku kraśnickim, obdarowany świąteczną kolędą z kasy miejskiej Kraśnika w 1779 r."
    },
    {
        "lp": 824,
        "nazwisko": "Bęgas",
        "wariant_nazwiska": "Bęgasina / Aleksandrowa Bęgasina / Aleksandrowa Wdowa / Alexanrowa Bęgasina",
        "imie": "Aleksandrowa",
        "przydomek": "",
        "funkcja": "Mieszkanka centrum (wdowa) (1778)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#154",
        "skany_list": [154],
        "zakres_lat": "1778",
        "min_rok": 1778,
        "max_rok": 1778,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Bęgas", "imie": "Aleksandrowa", "miejsce": "Śródmieście", "rola": "Płatniczka sympli", "skan": 154, "rok": "1778", "zapis_oryginalny": "Aleksandrowa Bęgasina", "kwota_ctx": "4 gr"}
        ],
        "uwagi": "Wdowa po Aleksandrze Bęgasie w Śródmieściu Kraśnika płacąca symplę miejską w 1778 r."
    },
    {
        "lp": 825,
        "nazwisko": "Zdyb",
        "wariant_nazwiska": "Zdybowa Adamowa / Adamowa Zdybowa / Adamowa",
        "imie": "Adamowa",
        "przydomek": "",
        "funkcja": "Mieszkanka centrum (wdowa) (1778)",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#154",
        "skany_list": [154],
        "zakres_lat": "1778",
        "min_rok": 1778,
        "max_rok": 1778,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Zdyb", "imie": "Adamowa", "miejsce": "Śródmieście", "rola": "Płatniczka sympli", "skan": 154, "rok": "1778", "zapis_oryginalny": "Zdybowa Adamowa", "kwota_ctx": "3 gr"}
        ],
        "uwagi": "Wdowa po Adamie Zdybie w centrum Kraśnika odnotowana w taryfie sympli miejskiej z 3 IV 1778 r."
    },
    {
        "lp": 826,
        "nazwisko": "Łukawski",
        "wariant_nazwiska": "Łukawski / Jędrzey Łukawski / Jędrzej Łukawski",
        "imie": "Jędrzej",
        "przydomek": "",
        "funkcja": "Gospodarz przedmiejski (1778)",
        "miejsce": "Przedmieście Piasek",
        "skany_roboczo": "#155",
        "skany_list": [155],
        "zakres_lat": "1778",
        "min_rok": 1778,
        "max_rok": 1778,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Łukawski", "imie": "Jędrzej", "miejsce": "Przedmieście Piasek", "rola": "Płatnik sympli", "skan": 155, "rok": "1778", "zapis_oryginalny": "Jędrzey Łukawski", "kwota_ctx": "2 gr"}
        ],
        "uwagi": "Gospodarz na Przedmieściu Piasek ujęty w taryfie sympli z 1778 r."
    },
    {
        "lp": 827,
        "nazwisko": "Ciepły",
        "wariant_nazwiska": "Ciepłowa / Ciepłowa Wdowa / Ciepła Wdowa",
        "imie": "[Wdowa]",
        "przydomek": "",
        "funkcja": "Mieszkanka przedmiejska (wdowa) (1778)",
        "miejsce": "Przedmieście Piasek",
        "skany_roboczo": "#155",
        "skany_list": [155],
        "zakres_lat": "1778",
        "min_rok": 1778,
        "max_rok": 1778,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Ciepły", "imie": "[Wdowa]", "miejsce": "Przedmieście Piasek", "rola": "Płatniczka sympli", "skan": 155, "rok": "1778", "zapis_oryginalny": "Ciepłowa Wdowa", "kwota_ctx": "2 gr"}
        ],
        "uwagi": "Wdowa na Przedmieściu Piasek opodatkowana w rejestrze sympli z 1778 r."
    },
    {
        "lp": 828,
        "nazwisko": "Podgórski",
        "wariant_nazwiska": "Podgórski / Grzegorz Podgórski / Podgorski",
        "imie": "Grzegorz",
        "przydomek": "",
        "funkcja": "Gospodarz przedmiejski (1778)",
        "miejsce": "Przedmieście Zarzyce",
        "skany_roboczo": "#155",
        "skany_list": [155],
        "zakres_lat": "1778",
        "min_rok": 1778,
        "max_rok": 1778,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Podgórski", "imie": "Grzegorz", "miejsce": "Przedmieście Zarzyce", "rola": "Płatnik sympli", "skan": 155, "rok": "1778", "zapis_oryginalny": "Gregor Podgorski", "kwota_ctx": "2 gr"}
        ],
        "uwagi": "Gospodarz na Przedmieściu Zarzyce notowany w sympli z 1778 r."
    },
    {
        "lp": 829,
        "nazwisko": "Łazarz",
        "wariant_nazwiska": "Łazarz / Andrzey Łazarz / Andrzej Łazarz",
        "imie": "Andrzej",
        "przydomek": "",
        "funkcja": "Gospodarz przedmiejski (1778)",
        "miejsce": "Przedmieście Piasek",
        "skany_roboczo": "#155",
        "skany_list": [155],
        "zakres_lat": "1778",
        "min_rok": 1778,
        "max_rok": 1778,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Łazarz", "imie": "Andrzej", "miejsce": "Przedmieście Piasek", "rola": "Płatnik sympli", "skan": 155, "rok": "1778", "zapis_oryginalny": "Andrzey Łazarz", "kwota_ctx": "2 gr"}
        ],
        "uwagi": "Mieszkaniec Przedmieścia Piasek ujęty w rejestrze symplowym z 3 IV 1778 r."
    },
    {
        "lp": 830,
        "nazwisko": "Tokarz",
        "wariant_nazwiska": "Tokarz / Andrzey Tokarz / Andrzej Tokarz",
        "imie": "Andrzej",
        "przydomek": "",
        "funkcja": "Rzemieślnik / Gospodarz przedmiejski (1778)",
        "miejsce": "Przedmieście Piasek",
        "skany_roboczo": "#155",
        "skany_list": [155],
        "zakres_lat": "1778",
        "min_rok": 1778,
        "max_rok": 1778,
        "liczba_wystapien": 1,
        "wystapienia": [
            {"nazwisko": "Tokarz", "imie": "Andrzej", "miejsce": "Przedmieście Piasek", "rola": "Płatnik sympli", "skan": 155, "rok": "1778", "zapis_oryginalny": "Andrzey Tokarz", "kwota_ctx": "3 gr"}
        ],
        "uwagi": "Rzemieślnik (tokarz) lub posesjonat na Przedmieściu Piasek notowany w sympli z 1778 r."
    }
]

with open('/home/ubuntu/workspace/Gen/part9_new_profiles.json', 'w', encoding='utf-8') as f:
    json.dump(nowe_profile, f, ensure_ascii=False, indent=2)

print(f"Utworzono part9_new_profiles.json z {len(nowe_profile)} profilami (lp {nowe_profile[0]['lp']}-{nowe_profile[-1]['lp']})!")
