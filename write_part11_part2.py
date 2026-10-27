import json

part2_trans = {
    "191": {
        "tytul": "Rejestr Sympli Miejskiej z 23 Września 1780 r. – Centrum Miasta i Ulica Lubelska (Latus 1 i Latus 2)",
        "data_rok": "1780-09-23",
        "kategoria": "Rejestr podatkowy / Sympla miejska (Centrum i Lubelska)",
        "osoby_podmioty": "Jacenty Fiszer, Rzepcicka (wdowa), Paweł Latosiewicz, Jędrzej Barankiewicz, Józef Słotka, Gołębiowska (wdowa), Grzegorz Leonorowski, Piotr Tokarczyk (plac), Mikołaj Łapczyński, Sebastian Szubartowski, Jakub Gąska, Michał Chrzanowski, Józef Paszkiewicz, Kazimierz Rycerz, Paweł Kuziński, Kasprowa (wdowa), Grzegorz Dzyba, Wojciech Potocki, Sebastian Prządka, Franciszek Frankiewicz, Petronela Olechowska, Katarzyna Zaniewska, Zofia Kłusowska (wdowa), Józef Korzepski, Jakub Przymka, Antoni Pstrykowski, Maciej Rycerz, Katarzyna Rzeszowska, Antoni Sadowski, Baltazar Latosiewicz, Mateusz Rycerz, Michał Jędrencarz, Jan Tokarski, Marcin Dzyba, Stanisław Bosoniak, Teresa Stachowiczowa, Jan Mutowski, Szymon Niewiadzski, Wojciech Brzezicki, Ignacy Szalenczyński, Marcin Wilk, Piotr Szydłowski, Wojciech Leszczyński, Wojciech Brzeszowski, Krzysztof Szuliczyński, Piotr Małczyński, Walenty Łukasik, Antoni Olejnik, Wojciech Rzeszowski, Sebastian Latoszewicz, Wdowa Potokowa, Jan Potocki, Ewa Pilaszkiewiczowa, Marianna Tokarska (wdowa), Józef Tokarski, Piotr Potocki, Franciszek Barankiewicz, Wawrzyniec Pilaszkiewicz, Petronela Szadowska, Franciszek Matuszkiewicz, Adam Rępa, Anna Rępina (wdowa), Tomasz Pilaszkiewicz, Krzysztof Ruszel, Franciszek Wilczyński",
        "opis_pozycji": "Kompletna taksa sympli miejskiej z 23 września 1780 r. ułożona publicznie na gruncie. Obejmuje 33 posesje w Rynku i Centrum Miasta (Primum Latus: 9 zł 3 gr, w tym najwyższa składka wójta Szubartowskiego – 1 zł 1 gr), 10 pozycji drugiej kolumny rynkowej oraz 25 posesji przy ulicy Lubelskiej (Secundum Latus: 8 zł 0 gr). Zarejestrowano puste place po pożarach (plac Tokarczyka i pustka miejska) oraz parcelę Kanapkowszczyzna w Podlesiu.",
        "kwoty_miary": "Primum Latus (Miasto): 9 zł 3 gr; Secundum Latus (Ulica Lubelska): 8 zł 0 gr. Łącznie z karty: 17 zł 3 gr.",
        "uwagi": "Bezcenny rejestr topograficzno-własnościowy Kraśnika doby stanisławowskiej. Znakomity materiał do badań nad strukturą zamożności patrycjatu i pospólstwa rynkowego.",
        "transkrypcja": """[PAGINA 92v]
[Rejestr Sympli Miejskiej z 23 Września 1780 r. – Centrum Miasta i Ulica Lubelska]

*Regestr Symplowy z Regestru Symplowego Generalnego R[oku] 23 7bris 1780 na gruncie publicznie ułożony.*

### Miasto (Rynek i Centrum):

| Nr | Posesjonat / Podatnik | Złote | Grosze | Kategoria / Uwagi paleograficzne |
| :---: | :--- | :---: | :---: | :--- |
| 1 | Jacenty Fiszer | — | 5 | Posesjonat rynkowy |
| 2 | Rzepcicka Wdowa | — | 2 | Wdowa |
| 3 | Paweł Latosiewicz | — | 2 | Mieszczanin |
| 4 | Jędrzey Barankiewicz | — | 12 | Cechmistrz kowalski |
| 5 | Józef Słotka | — | 5 | Mieszczanin |
| 6 | Gołębiowska Wdowa | — | 2 | Wdowa |
| 7 | Grzegorz Leonorowski | — | 10 | Mieszczanin |
| 8 | Pustka pusto leżąca | — | 9 | Plac opuszczony / pogorzelisko |
| 9 | Plac pusty Piotra Tokarczyka | — | 5 | Plac miejski |
| 10 | Mikołay Łapczyński | — | 14 | Mieszczanin |
| 11 | Sebestyan Szubartowski | 1 | 1 | Wójt kraśnicki |
| 12 | Jakób Gąska | — | 2 | Posesjonat |
| 13 | Michał Chrzanowski | — | 20 | Mieszczanin |
| 14 | Józef Paszkiewicz | — | 10 | Mistrz tkacki, przyszły wójt |
| 15 | Kazimierz Rycerz | — | 23 | Były exaktor |
| 16 | Paweł Kuziński | — | 17 | Mieszczanin |
| 17 | Kasprowa Wdowa | — | 4 | Wdowa |
| 18 | Grzegorz Dzyba | — | 21 | Mieszczanin |
| 19 | Woyciech Potocki | — | 2 | Posesjonat |
| 20 | Sebestyan Prządka | — | 2 | Posesjonat |
| 21 | Franciszek Frankiewicz | — | 5 | Exaktor miejski |
| 22 | Petronela Olechowska | — | 10 | Mieszczka |
| 23 | Katarzyna Zaniewska | — | 3 | Mieszczka |
| 24 | Zofia Kłusowska Wdowa | — | 1 | Wdowa uboga |
| 25 | Józef Korzepski | — | 1 | Mieszczanin |
| 26 | Jakub Przymka | — | 4 | Posesjonat |
| 27 | Antoni Pstrykowski | — | 4 | Kowal |
| 28 | Maciey Rycerz | — | 6 | Burmistrz / kowal |
| 29 | Katarzyna Rzeszowska | — | 12 | Mieszczka |
| 30 | Maciej Rycerz [drugi wpis/ogród] | — | 2 | Posesja dodatkowa |
| 31 | Antoni Sadowski | — | 2 | Mieszczanin |
| 32 | Baltazar Latosiewicz | — | 2 | Posesjonat |
| 33 | Mateusz Rycerz | — | 4 | Posesjonat |
| — | **PRIMUM LATUS** | **9** | **3** | **Suma pierwszej kolumny (Miasto)** |

---

### Miasto (Druga kolumna rynkowa):

| Nr | Posesjonat / Podatnik | Złote | Grosze | Kategoria / Uwagi |
| :---: | :--- | :---: | :---: | :--- |
| 34 | Michał Jędrencarz | — | 4 | Mieszczanin |
| 35 | Jan Tokarski | — | 6 | Posesjonat |
| 36 | Marcin Dzyba | — | 3 | Posesjonat |
| 37 | Stanisław Bosoniak | — | 2 | Cechmistrz szewski |
| 38 | Teresa Stachowiczowa | — | 3 | Mieszczka |
| 39 | Jan Mutowski | — | 3 | Posesjonat |
| 40 | Szymon Niewiadzski | — | 1 | Posesjonat |
| 41 | Woyciech Brzezicki | — | 4 | Posesjonat |
| 42 | Jgnacy Szalenczyński | — | 3 | Posesjonat |
| 43 | Marcin Wilk | — | 1 | Posesjonat |

---

### Ulica Lubelska:

| Nr | Posesjonat / Podatnik | Złote | Grosze | Kategoria / Uwagi |
| :---: | :--- | :---: | :---: | :--- |
| 44 | Piotr Szydłowski | — | 4 | Posesjonat przy ul. Lubelskiej |
| 45 | Woyciech Leszczyński | — | 8 | Posesjonat |
| 46 | Woyciech Brzeszowski | — | 4 | Posesjonat |
| 47 | Krzysztof Szuliczyński | — | 7 | Burmistrz / szewc |
| 48 | Piotr Małczyński | — | 4 | Posesjonat |
| 49 | Walenty Łukasik | — | 8 | Współexaktor / ławnik |
| 50 | Antoni Oleyn[ik] | — | 2 | Olejnik |
| 51 | Woyciech Rzeszowski | — | 6 | Posesjonat |
| 52 | Kanapkowszczyzna (w Podlesiu) | — | 6 | Grunt/posesja przypisana |
| 53 | Sebestyan Latoszewicz | — | 3 | Cechmistrz szewski |
| 54 | Wdowa Potokowa | — | 6 | Wdowa |
| 55 | Jan Potocki | — | 3 | Posesjonat |
| 56 | Ewa Pilaszkiewiczowa | — | 9 | Mieszczka |
| 57 | Maryanna Tokarska Wdowa | — | 5 | Wdowa |
| 58 | Józef Tokarski | — | 3 | Posesjonat |
| 59 | Piotr Potocki | — | 9 | Posesjonat |
| 60 | Franciszek Barankiewicz | — | 10 | Burmistrz / deputat |
| 61 | Wawrzyniec Pilaszkiewicz | — | 12 | Ławnik |
| 62 | Petronela Szadowska | — | 3 | Mieszczka |
| 63 | Franciszek Matuszkiewicz | — | 8 | Ławnik |
| 64 | Adam Rępa | — | 2 | Posesjonat |
| 65 | Anna Rępina Wdowa | — | 11 | Wdowa |
| 66 | Tomasz Pilaszkiewicz | — | 14 | Posesjonat |
| 67 | Krzysztof Ruszel | — | 8 | Posesjonat |
| 68 | Franciszek Wilczyński | — | 17 | Posesjonat |
| — | **SECUNDUM LATUS** | **8** | **—** | **Suma Ulicy Lubelskiej** |"""
    },
    "192": {
        "tytul": "Rejestr Sympli Miejskiej z 23 Września 1780 r. – Ulica Lubelska c.d., Przedmieście Piasek i Zarzyce (Latus 3 i Latus 4)",
        "data_rok": "1780-09-23",
        "kategoria": "Rejestr podatkowy / Sympla miejska (Piasek i Zarzyce)",
        "osoby_podmioty": "Sukcesorowie Andlosza, Antoni Piasecki, Jan Boguta, Grzegorz Krasowski, Kacper Kirszlicz, Mikołaj Brzemiński, Krzysztof Pilaszkiewicz, Maciej Walczyński, Jędrzej Rępa, Marianna Rępina, Walenty Jurgiel, Marianna Fratkowska, Maciej Potokowicz, Paweł Piasecki, Sukcesor Manczewicza, Józef Bańka, Paweł Jeś, Jakubowa Młynarczykowa, Szymon Antczyk, Marianna Ciezkowa, Łukasz Lapsa, Stanisławowa Witkowa, Sebastian Kiliś, Piotr Buńcyk, Marcin Łapa, Marianna Rymarzowa (wdowa), Jurowa (wdowa), Antoni Tkaczyk, Jakub Jasionek, Tomasz Jądrzyk, Mateusz Dzyb, Jan Büntek, Jan Wądzik, Anna Tokarzowa (wdowa), Mikołaj Nowak, Franciszek Petka, Jakub Jaczniak, Bartłomiej Zdyb, Katarzyna Olechowska (wdowa), Katarzyna Jaczkowa, Wojciech Celej, Wojciech Ćwieka, Jędrzej z Pogorzałych, Wojciech Słowak, Szymon Wnuk, Jędrzej Łukasik, Wojciech Petka, Wojciech Drąg, Łukasz Petka, Joachim Karobacz, Rozalia Zielińska, Michał Tokarczyk, Piotr Tokarczyk, Marianna Wojciechowa (wdowa), Błażej Rzepniak, Łukasz Tokarczyk, Bartłomiej Stary Brat, Barbara Bielikowa, Stanisław Wójcika żona, Kazimierz Tokarczyk, Kazimierz Celej, Bartłomiej Celej, Stanisław Smolecki, Marianna Lygakowa, Marianna Kiliszkowa, Maciej Szubartowski, Bartłomiej Wiaterko, Grzegorz Jarzynka, Wawrzyniec Stary Brat, Matiasz Rachoń, Marianna Ćwiczkowa (wdowa), Szymon Marzec, Maciej Rydzynek, Kacper Trojczak, Tomasz Zięba, Jędrzej Tokarczyk",
        "opis_pozycji": "Kontynuacja regestru sympli: dokończenie ulicy Lubelskiej (16 posesji), Przedmieście Piasek część pierwsza (23 posesje, 3tium Latus: 12 zł 25 gr), Przedmieście Piasek część druga (22 posesje) oraz początek Przedmieścia Zarzyce (15 posesji – 4tu Latus: 18 zł 0 gr). Wysokie opłaty u przedmieszczan: Wojciech Ćwieka (29 gr), Łukasz Tokarczyk (26 gr), Bartłomiej Celej (1 zł 4 gr), Wawrzyniec Stary Brat (1 zł 10 gr).",
        "kwoty_miary": "3tium Latus (Piasek cz. 1): 12 zł 25 gr; 4tu Latus (Piasek cz. 2 i Zarzyce cz. 1): 18 zł 0 gr. Łącznie z karty: 30 zł 25 gr.",
        "uwagi": "Doskonała dokumentacja demograficzna przedmieść rolniczo-ogrodniczych Kraśnika. Widoczne skupiska rodowe Ćwieków, Tokarczyków, Celejów i Petków.",
        "transkrypcja": """[PAGINA 93]
[Dokończenie Ulicy Lubelskiej, Przedmieście Piasek i Przedmieście Zarzyce]

### Continuatio Ulicy Lubelskiey:

| Nr | Posesjonat / Podatnik | Złote | Grosze | Kategoria / Uwagi |
| :---: | :--- | :---: | :---: | :--- |
| 69 | Sukcesorowie z Andlosz[a] | — | 5 | Sukcesorowie posesji |
| 70 | Antoni Piasecki | — | 14 | Posesjonat |
| 71 | Jan Boguta | — | 10 | Posesjonat |
| 72 | Grzegorz Krasowski | — | 5 | Posesjonat |
| 73 | Kacper Kirszlicz | — | 8 | Posesjonat |
| 74 | Mikołay Brzemiński | — | 6 | Posesjonat |
| 75 | Krzysztof Pilaszkiewicz | — | 11 | Posesjonat |
| 76 | Maciey Walczyński | — | 5 | Posesjonat |
| 77 | Jędrzey Rępa | — | 3 | Posesjonat |
| 78 | Maryanna Rępina | — | 9 | Mieszczka |
| 79 | Walenty Jurgiel | — | 4 | Posesjonat |
| 80 | Maryanna Fratkowska | — | 3 | Mieszczka |
| 81 | Maciey Potokowicz | — | 4 | Szafarz / posesjonat |
| 82 | Paweł Piasecki | — | 17 | Posesjonat |
| 83 | Sukcesor Manczewicza | — | 1 | Sukcesor posesji |
| 84 | Józef Bańka | — | 12 | Posesjonat |

---

### Przedmieście Piasek (Część 1):

| Nr | Posesjonat / Przedmieszczanin | Złote | Grosze | Kategoria / Uwagi |
| :---: | :--- | :---: | :---: | :--- |
| 85 | Paweł Jeś | — | 18 | Przedmieszczanin |
| 86 | Jakubowa Młynarczykowa | — | 6 | Wdowa |
| 87 | Szymon Antczyk | — | 13 | Przedmieszczanin |
| 88 | Maryanna Ciezkowa | — | 14 | Przedmieszczanka |
| 89 | Łukasz Lapsa | — | 19 | Przedmieszczanin |
| 90 | Stanisławowa Witkowa | — | 10 | Wdowa |
| 91 | Sebestyan Kiliś | — | 25 | Przedmieszczanin |
| 92 | Piotr Buńcyk | — | 7 | Przedmieszczanin |
| 93 | Marcin Łapa | — | 12 | Przedmieszczanin |
| 94 | Maryanna Rymarzowa Wdowa | — | 20 | Wdowa |
| 95 | Jurowa Wdowa | — | 20 | Wdowa |
| 96 | Antoni Tkaczyk | — | 21 | Przedmieszczanin |
| 97 | Jakub Jasionek | — | 24 | Przedmieszczanin |
| 98 | Tomasz Jądrzyk | — | 24 | Przedmieszczanin |
| 99 | Mateusz Dzyb | — | 21 | Przedmieszczanin |
| 100 | Jan Büntek | — | 25 | Przedmieszczanin |
| 101 | Jan Wądzik | — | 13 | Przedmieszczanin |
| 102 | Anna Tokarzowa Wdowa | — | 19 | Wdowa |
| 103 | Mikołay Nowak | — | 19 | Przedmieszczanin |
| 104 | Franciszek Petka | — | 14 | Przedmieszczanin |
| 105 | Jakub Jaczniak | — | 14 | Przedmieszczanin |
| 106 | Bartłomiey Zdyb | — | 7 | Przedmieszczanin |
| 107 | Katarz[yna] Olechowska Wdowa | — | 6 | Wdowa |
| — | **3TIUM LATUS** | **12** | **25** | **Suma Piasku (Część 1)** |

---

### Przedmieście Piasek (Druga kolumna – Część 2):

| Nr | Posesjonat / Przedmieszczanin | Złote | Grosze | Kategoria / Uwagi |
| :---: | :--- | :---: | :---: | :--- |
| 108 | Katarzyna Jaczkowa | — | 15 | Przedmieszczanka |
| 109 | Woyciech Celey | — | 14 | Przedmieszczanin |
| 110 | Woyciech Cwieka | — | 29 | Dziesiątnik piaskowy |
| 111 | Jędrzey z Pogorzałych | — | 10 | Pogorzelec |
| 112 | Woyciech Słowak | — | 24 | Przedmieszczanin |
| 113 | Szymon Wnuk | — | 12 | Przedmieszczanin |
| 114 | Jędrzey Łukasik | — | 7 | Przedmieszczanin |
| 115 | Woyciech Petka | — | 14 | Przedmieszczanin |
| 116 | Woyciech Drag | — | 14 | Przedmieszczanin |
| 117 | Łukasz Petka | — | 20 | Przedmieszczanin |
| 118 | Joachim Karobacz | — | 7 | Przedmieszczanin |
| 119 | Rozalia Zielińska | — | 7 | Przedmieszczanka |
| 120 | Michał Tokarczyk | — | 12 | Przedmieszczanin |
| 121 | Piotr Tokarczyk | — | 11 | Przedmieszczanin |
| 122 | Maryanna Woycechowa Wdowa | — | 7 | Wdowa |
| 123 | Błażey Rzepniak z Żon[ą] | — | 11 | Gospodarstwo małżeńskie |
| 124 | Łukasz Tokarczyk | — | 26 | Przedmieszczanin |
| 125 | Bartłomiey stary Brat | — | 24 | Starobrat |
| 126 | Barbara Bielikowa | — | 10 | Przedmieszczanka |
| 127 | Stanisław Woycika Żona | — | 23 | Gospodyni |
| 128 | Kazimierz Tokarczyk | — | 25 | Przedmieszczanin |
| 129 | Kazimierz Celey | — | 29 | Przyszły burmistrz |

---

### Przedmieście Zarzyce (Początek):

| Nr | Posesjonat / Przedmieszczanin | Złote | Grosze | Kategoria / Uwagi |
| :---: | :--- | :---: | :---: | :--- |
| 130 | Bartłomiey Celey | 1 | 4 | Zamożny przedmieszczanin |
| 131 | Stanisław Smolecki | — | 6 | Przedmieszczanin |
| 132 | Maryanna Lygakowa | — | 17 | Przedmieszczanka |
| 133 | Maryanna Kiliszkowa | — | 14 | Przedmieszczanka |
| 134 | Maciey Szubartowski | — | 7 | Przedmieszczanin |
| 135 | Bartł[omiey] Wiaterko | — | 15 | Przedmieszczanin |
| 136 | Grzegorz Jarzynka | — | 22 | Przedmieszczanin |
| 137 | Wawrzyniec stary Brat | 1 | 10 | Starobrat |
| 138 | Matiasz Rachon | — | 14 | Przedmieszczanin |
| 139 | Maryanna Cwiczkowa Wdowa | — | 14 | Wdowa |
| 140 | Szymon Marzec | — | 22 | Przedmieszczanin |
| 141 | Maciey Rydzynek | — | 19 | Przedmieszczanin |
| 142 | Kacper Trojczak | — | 9 | Przedmieszczanin |
| 143 | Tomasz Zięmba | — | 9 | Przedmieszczanin |
| 144 | Jędrzey Tokarczyk | — | 7 | Przedmieszczanin |
| — | **4TU LATUS** | **18** | **—** | **Suma Piasku (cz. 2) i Zarzyc (cz. 1)** |"""
    },
    "193": {
        "tytul": "Rejestr Sympli Miejskiej z 23 Września 1780 r. – Dokończenie Zarzyc oraz Przedmieście Góry i Podlesie (Latus 5 i Latus 6)",
        "data_rok": "1780-09-23",
        "kategoria": "Rejestr podatkowy / Sympla miejska (Zarzyce, Góry i Podlesie)",
        "osoby_podmioty": "Antoni Bańka, Grzegorz Biegaj, Matiasz Piotrzkowski, Marianna Rymarzowa (wdowa), Marcin Drozd, Wojciech Wolak, Marcin Rymarczyk, Marianna Kotworkówna, Anna Łozina (wdowa), Krystyna Merkowa (wdowa), Jędrzej Rządkowski, Kazimierz Olechowski, Jakub Łatczyk, Sebastian Łygak, Józef Dubaj, Michał Dubaj, Kazimierz Decza, Wojciech Biegaj Żyd, Sebastian Mikołajczyk, Tomasz Rządkowski, Łukasz Biegaj, Józef Rozpędzisz, Matiasz Łazarz, Kacper Bączonka, Jędrzej Łazarz, Antoni Rozpędzisz, Bartłomiej Prządka, Matiasz Kuśnierz, Mikołaj Rępa, Łukasz Koza, Mikołaj Biegaj, Wawrzyniec Owczarzyk, Tomasz Marek, Zofia Młynarczykowa, Józef Piotrowski, Szymon Płachta, Grzegorz Wolak, Sukcesor Ziomkowski, Wojciech Gąska, Jacenty Decyk, Wojciech Kawka, Sukcesor Młynarczyka, Jakub Rządkowski, Sebastian Tygryczak, Fabian Trojczak, Jacenty Przymka, Maciej Trojczak, Maciej Rępa, Jędrzej Prządka, Jędrzej Rępa, Józef Sadzik, Tomasz Ręwka, Antoni Polgrezyk, Franek Gąska, Józef Słowak, Wawrzyniec Tokarczyk, Augustyn Przegorczyk, Antoni Wilk, Józefowa Paszczyna (wdowa), Szymon Ćwiek, Marianna Kopeciowa, Zofia Pawliczka, Ewa Tręfczyna, Jan Wilk, Mateusz Dzyba, Zofia Ziemlakowa (wdowa), Franciszek Szupia, Tomasz Wróbel, Maciej Kawka, Grzegorz Dzyba, Wojciech Kowal, Józef Wilk, Błażej Babicz, Józef Stonkowski, Wojciech Bień",
        "opis_pozycji": "Kontynuacja regestru sympli: dokończenie Przedmieścia Zarzyce (36 pozycji, 5tum Latus: 13 zł 21 gr) oraz Przedmieście Góry i Podlesie część pierwsza (39 pozycji, 6tum Latus: 16 zł 15 gr). W rejestrze widnieją gospodarstwa z zarostkami (Dubajowie, Łukasz Koza), pola i ogrody (pola Trojczaka i Rępy, ogród Prządki) oraz unikatowy wpis 'Woyciech Biegay Żyd' (8 gr). Najwyższa stawka na Górach: Wojciech Bień – 1 zł 0 gr.",
        "kwoty_miary": "5tum Latus (Zarzyce c.d.): 13 zł 21 gr; 6tum Latus (Góry i Podlesie cz. 1): 16 zł 15 gr. Łącznie z karty: 30 zł 6 gr.",
        "uwagi": "Wyczerpujący przegląd posesjonatów peryferyjnych, sadów, ogrodów i gruntów zarosłych. Dokumentuje procesy asymilacyjne i specyfikę osadnictwa przedmiejskiego.",
        "transkrypcja": """[PAGINA 93v]
[Sympla Miejska 1780 r. c.d. – Zarzyce oraz Przedmieście Góry i Podlesie]

### Continuatio Przedmieście Zarzycze:

| Nr | Posesjonat / Przedmieszczanin | Złote | Grosze | Kategoria / Uwagi |
| :---: | :--- | :---: | :---: | :--- |
| 145 | Antoni Bańka | — | 7 | Przedmieszczanin |
| 146 | Grzegorz Biegay | — | 12 | Przedmieszczanin |
| 147 | Mathiasz Piotrzkowski | — | 14 | Przedmieszczanin |
| 148 | Maryanna Rymarzowa Wdowa | — | 7 | Wdowa |
| 149 | Marcin Drozd | — | 19 | Przedmieszczanin |
| 150 | Woyciech Wolak | — | 12 | Przedmieszczanin |
| 151 | Marcin Rymarczyk | — | 7 | Przedmieszczanin |
| 152 | Maryanna Kotworkowna | — | 12 | Przedmieszczanka |
| 153 | Anna Łozina Wdowa | — | 10 | Wdowa |
| 154 | Krystyna Merkowa Wdowa | — | 14 | Wdowa |
| 155 | Jędrzey Rządkowski | — | 11 | Przedmieszczanin |
| 156 | Kazimierz Olechowski | — | 7 | Przedmieszczanin |
| 157 | Jakob Łatczyk | — | 5 | Przedmieszczanin |
| 158 | Sebestyan Łygak | — | 5 | Przedmieszczanin |
| 159 | Jozef Dubay z Zarostk[iem] | — | 10 | Grunt z zarostkiem |
| 160 | Michał Dubay z Zar[ostkiem] | — | 10 | Grunt z zarostkiem |
| 161 | Kazimierz Decza | — | 5 | Przedmieszczanin |
| 162 | Woyciech Biegay Żyd | — | 8 | Posesjonat żydowski |
| 163 | Sebestyan Mikołayczyk | — | 23 | Przedmieszczanin |
| 164 | Tomasz Rządkowski | — | 15 | Przedmieszczanin |
| 165 | Łukasz Biegay | — | 15 | Przedmieszczanin |
| 166 | Józef Rozpędzisz z Dzi[ećmi] | — | 12 | Gospodarstwo rodzinne |
| 167 | Matiasz Łazarz | — | 5 | Przedmieszczanin |
| 168 | Kacper Bączonka | — | 18 | Przedmieszczanin |
| 169 | Jędrzey Łazarz | — | 12 | Przedmieszczanin |
| 170 | Antoni Rozpędzisz | — | 12 | Przedmieszczanin |
| 171 | Bartłomiey Prządka | — | 6 | Przedmieszczanin |
| 172 | Matyasz Kuśnierz | — | 12 | Rzemieślnik |
| 173 | Mikołay Rępa | — | 10 | Przedmieszczanin |
| 174 | Łukasz Koza Zarostek | — | 10 | Grunt z zarostkiem |
| 175 | Mikołay Biegay | — | 9 | Przedmieszczanin |
| 176 | Wawrzyniec Owczarzyk | — | 10 | Przedmieszczanin |
| 177 | Tomasz Marek | — | 6 | Przedmieszczanin |
| 178 | Zofia Młynarczykowa z Synem | — | 12 | Wdowa z synem |
| 179 | Józef Piotrowski | — | 12 | Przedmieszczanin |
| 180 | Szymon Płachta | — | 10 | Przedmieszczanin |
| — | **5TUM LATUS** | **13** | **21** | **Suma Zarzyc (Dokończenie)** |

---

### Przedmieście Góry i Podlesie (Część 1):

| Nr | Posesjonat / Przedmieszczanin | Złote | Grosze | Kategoria / Uwagi |
| :---: | :--- | :---: | :---: | :--- |
| 181 | Grzegorz Wolak | — | 5 | Przedmieszczanin |
| 182 | Sukcesor Ziomkowsk[i] | — | 10 | Sukcesorowie posesji |
| 183 | Woyciech Gąska | — | 7 | Przedmieszczanin |
| 184 | Jacenty Decyk | — | 7 | Przedmieszczanin |
| 185 | Woyciech Kawka | — | 6 | Przedmieszczanin |
| 186 | Sukcesor Młynarczyka | — | 24 | Sukcesorowie posesji |
| 187 | Jakob Rządkowski | — | 14 | Przedmieszczanin |
| 188 | Sebestyan Tygryczak | — | 5 | Przedmieszczanin |
| 189 | Fabian Trojczak | — | 10 | Przedmieszczanin |
| 190 | Jacenty Przymka | — | 14 | Przedmieszczanin |
| 191 | Pole Macieja Trojczaka | — | 5 | Rola orna |
| 192 | Pole Macieja Rępy | — | 3 | Rola orna |
| 193 | Ogród Jędrzeia Prządka | — | 2 | Ogród warzywny |
| 194 | Jędrzey Rępa | — | 25 | Przedmieszczanin |
| 195 | Jozef Sadzik | — | 10 | Przedmieszczanin |
| 196 | Tomasz Ręwka | — | 12 | Przedmieszczanin |
| 197 | Antoni Polgrezyk | — | 10 | Przedmieszczanin |
| 198 | Franek Gąska | — | 8 | Przedmieszczanin |
| 199 | Jozef Słowak | — | 14 | Przedmieszczanin |
| 200 | Wawrzyniec Tokarczyk | — | 12 | Przedmieszczanin |
| 201 | Augustyn Przegorczyk | — | 12 | Przedmieszczanin |
| 202 | Antoni Wilk | — | 20 | Przedmieszczanin |
| 203 | Jozefowa Paszczyna Wdowa | — | 20 | Wdowa |
| 204 | Szymon Ćwiek | — | 14 | Przedmieszczanin |
| 205 | Maryanna Kopeciowa | — | 4 | Przedmieszczanka |
| 206 | Zoffia Pawliczka | — | 5 | Wdowa |
| 207 | Ewa Tręfczyna | — | 5 | Przedmieszczanka |
| 208 | Jan Wilk | — | 7 | Przedmieszczanin |
| 209 | Mateusz Dzyba | — | 7 | Przedmieszczanin |
| 210 | Zoffia Ziemlakowa Wdowa | — | 10 | Wdowa |
| 211 | Franciszek Szupia | — | 13 | Przedmieszczanin |
| 212 | Tomasz Wróbl | — | 17 | Przedmieszczanin |
| 213 | Maciej Kawka | — | 17 | Przedmieszczanin |
| 214 | Grzegorz Dzyba | — | 20 | Przedmieszczanin |
| 215 | Wojciech Kowal | — | 14 | Kowal |
| 216 | Józef Wilk | — | 22 | Przedmieszczanin |
| 217 | Błażey Babicz | — | 14 | Przedmieszczanin |
| 218 | Jozef Stonkowski | — | 6 | Przedmieszczanin |
| 219 | Woyciech Bień | 1 | — | Zamożny przedmieszczanin |
| — | **6TUM LATUS** | **16** | **15** | **Suma Gór i Podlesia (Część 1)** |"""
    }
}

with open('/home/ubuntu/workspace/Gen/part11_trans_2.json', 'w', encoding='utf-8') as f:
    json.dump(part2_trans, f, ensure_ascii=False, indent=2)

print("Zapisano part11_trans_2.json pomyślnie.")
