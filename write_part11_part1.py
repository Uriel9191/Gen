import json

part1_trans = {
    "186": {
        "tytul": "Rachunki miejskie: Percepta końcowa oraz otwarcie Expensy długów delegackich",
        "data_rok": "1781-05-16",
        "kategoria": "Rachunki miejskie / Percepta i Expensa długów delegackich",
        "osoby_podmioty": "Franciszek Frankiewicz (exaktor), Walenty Łukasik (exaktor), arendarz Rubin (Żyd), Kahał kraśnicki, Tomasz Śliwiński (b. pisarz miejski), Franciszek Chrzanowski (dyrektor szkoły), Józef Paszkiewicz (sławetny), stróż nocny",
        "opis_pozycji": "Dokończenie percepty miejskiej za lata 1779–1781: dochód z sochacznego/targowego zarendowanego Żydowi Rubinowi (108 zł), składka kahału na siano dla wojska przechodzącego (28 zł), opłata jateczna (24 zł) oraz szarwarczne żydowskie (20 zł); Zamknięcie Percepty Generalnej na kwotę 5192 zł 22 1/2 gr. Otwarcie Expensy na spłatę dawnych długów z dekretu delegackiego: pensja byłego pisarza Śliwińskiego (24 zł), zaległe solarium dyrektora szkoły (167 zł 20 gr), stróż nocny (3 zł 20 gr) oraz należność Józefa Paszkiewicza (62 zł). Suma Latus: 257 zł 10 gr.",
        "kwoty_miary": "Percepta: Transport 5012 zł 22 1/2 gr, Dochody nowe 180 zł; Suma Generalna Percepty: 5192 zł 22 1/2 gr. Expensa długów: Summa Latus 257 zł 10 gr.",
        "uwagi": "Kluczowe rozliczenie likwidacji dawnych zobowiązań magistratu wobec personelu miejskiego i dostawców wojskowych na mocy dekretu delegacji ordynackiej.",
        "transkrypcja": """[PAGINA 90]
[Rachunki Miejskie: Percepta Końcowa oraz Otwarcie Expensy Długów Delegackich – 16 Maja 1781 r.]

### Continuatio Percepta 90:

| Pozycja / Źródło przychodu | Wyszczególnienie i podstawa prawna | Złote | Grosze |
| :--- | :--- | :---: | :---: |
| **Transport Percepty** | Z poprzedniego regestru rachunkowego (Pag. 89v) | 5012 | 22 1/2 |
| **Sochaczne czyli Targowe** | Żydowi [Rubinowi] zarendowane w Roku przeszłym od S. Jana do S. Jana Roku teraznieyszego 1781 | 108 | — |
| **Od Kahału kraśnickiego** | Na kupno siana dla woyska przechodzącego przyłożyli się i dali | 28 | — |
| **Jateczne mieyskie** | Za Rok ieden od Roku przeszłego do teraznieyszey Elekcyi | 24 | — |
| **Szarwarczne żydowskie** | Od Kahału zarendowane y oddane | 20 | — |
| **IN SUMMA PERETTA PERCEPTY** | **Suma Generalna Przychodu Kasy Miejskiej** | **5192** | **22 1/2** |

*Dicitur per expressum Złł Pol. Pięć Tysięcy Sto Dziewięćdziesiąt Dwa Złote dwadzieścia dwa y pół grosza.*

---

### Expensa Pieniędzy Mieyskich
*Długi wypłacone podług Dekretu Delegackiego a thoto:*

| Pozycja rozchodu | Odbiorca należności i tytuł prawny | Złote | Grosze |
| :--- | :--- | :---: | :---: |
| **Pisarz Mieyski przeszły** | P. [Tomaszowi] Śliwińskiemu Pisarzowi Mieyskiemu przeszłemu podług Kwitu y obrachowania iego wypłacił Exaktor | 24 | — |
| **Dyrektor Szkoły Mieyskiey** | P. [Franciszkowi Chrzanowskiemu] Dyrektorowi uczącemu Dzieci podług Dekretu dawne Solarium podług Kwitów iego | 167 | 20 |
| **Stróż Nocny** | Stróżowi Nocnemu płacy podług Dekretu wypłacono | 3 | 20 |
| **Pretensja mieszczańska** | Sł[awetny] [Józef] Paszkiewicz za kwitem swoim podług tegoż Dekretu Odebrał | 62 | — |
| **SUMMA LATUS** | **Suma wydatków na spłatę długów delegackich** | **257** | **10** |"""
    },
    "187": {
        "tytul": "Rachunki miejskie: Expensa potoczna, utrzymanie woźnego i stróża nocnego, kwaterunek wojskowy i edukacja",
        "data_rok": "1781-05-16",
        "kategoria": "Rachunki miejskie / Expensa potoczna, wojskowa i szkolna",
        "osoby_podmioty": "Wdowa (beneficjentka zapomogi), Urzędnicy magistratu, Ławnicy rewidujący kominy, Woźny miejski, Stróż nocny, Posłańcy (do Zamościa i Zawichwostu), Pisarze łąkowi, Żołnierze wojsk polskich i rosyjskich, Franciszek Chrzanowski (dyrektor szkoły)",
        "opis_pozycji": "Kontynuacja rozchodów kasy miejskiej: asygnacja dla ubogiej wdowy (20 zł); wydatki potoczne 1779–1781: wotywa elekcyjna, rewizje kominiarskie, pochówek ubogich, kłódka sądowa, papier i protokoły urzędowe, proch strzelecki na Boże Ciało (192 zł 17 gr); 18-miesięczne utrzymanie woźnego miejskiego: strawne (96 zł) oraz mundur/barwa, buty, pas, bielizna i leczenie choroby (65 zł 13 gr); pensja stróża nocnego (72 zł); poselstwa do Zawichwosta i Zamościa (5 zł 17 gr); koszenie łąk (2 zł 15 gr); gratyfikacje świąteczne (36 zł); aprowizacja i trunek dla wojsk rosyjskich i polskich (99 zł 9 gr); pensja półtoraroczna dyrektora szkoły (284 zł z sumy 300 zł). Suma Latus: 1119 zł 21 gr.",
        "kwoty_miary": "Transport Expensy 257 zł 10 gr; Suma pozycji bieżących 862 zł 11 gr; Summa Latus: 1119 zł 21 gr.",
        "uwagi": "Szczegółowy obraz kosztów funkcjonowania administracji miejskiej, bezpieczeństwa przeciwpożarowego, woźnego miejskiego oraz obciążeń z tytułu przemarszów wojsk koronnych i carskich.",
        "transkrypcja": """[PAGINA 90v]
[Expensa Potoczna, Woźny Miejski, Stróż Nocny, Przemarsze Wojsk i Pensja Nauczyciela]

### Continuat[io] Dalsza Expensa 90v:

| Pozycja rozchodu | Wyszczególnienie wydatku i asygnacja | Złote | Grosze |
| :--- | :--- | :---: | :---: |
| **Transport Expensy** | Z poprzedniej strony (Pag. 90) | 257 | 10 |
| **Zapomoga mieyska** | Tejże Wdowie podług Kwitu Magistratu Exaktor wypłacił | 20 | — |

---

### Expensa z nowey Dyspozycyi:

| Pozycja / Cel wydatku | Szczegółowy opis pozycji rozchodowej | Złote | Grosze |
| :--- | :--- | :---: | :---: |
| **Expensa Potoczna Administracyjna** | Od Elekcyi przeszłey 1779 do teraznieyszey 1781 r. 16to Maji: na Wotywę Elekcyonatną, Supplement podczas Elekcyi, Ławnikom od Rewizyi Kominow, pochowania Ubogich, za Kłódkę do Rezydencyi Sądowey, za Papier y protokuł do Akt uroczystych po 3 razy, na proch do strzelania na Święto Bożego Ciała y inney Drobney Expensy | 192 | 17 |
| **Woźny Mieyski (Utrzymanie)** | Woźnemu także od przeszłey Elekcyi strawnego za miesięcy Ośmnaście po Złł 5 gr 10 na Miesiąc, czyni Złł 96; za Barwę, Buty, pas, Bieliznę, i na chorobę Jego Złł 65 gr 13 — Efficit: | 161 | 13 |
| **Stróż Nocny** | Stróżowi Nocnemu płacy za pułtora lata na miesiąc po Złł 4 | 72 | — |
| **Posłańcy ordynaccy** | Expensa na Posłańcow do Zawichwosta y do Zamościa z Suppliką | 5 | 17 |
| **Łąki mieyskie** | Pisarzom od koszenia Łąk Mieyskich | 2 | 15 |
| **Zwyczaiowe Świąteczne** | Świątecznego po 3 razy dla PP. Urzędnikow y innych Osób | 36 | — |
| **Wiktuały dla Woyska** | Dla Żołnierzow przechodzących Woyska Moskiewskiego y Polskiego na Trunek, Owies, podwod wypędzenia, za Kawę, Cukier, Rodzynki, Chleb y Jnnych wiktuałow | 99 | 9 |
| **Dyrektor Szkoły Mieyskiey** | Dyrektorowi [Franciszkowi Chrzanowskiemu] uczącemu Dzieci Mieyskie za pułtora lata należy zasług na Rok po Złł 200, a za pułtora lata Złł 300, z tego odebrał z Kassy Mieyskiey Złł Pol. | 284 | — |
| **SUMMA LATUS** | **Łączny rozchód z karty Pag. 90v** | **1119** | **21** |"""
    },
    "188": {
        "tytul": "Rachunki miejskie: Koszty furażu, rewizje urzędowe, podymne koronne i pensja pisarza Alkiewicza",
        "data_rok": "1781-05-16",
        "kategoria": "Rachunki miejskie / Expensa podatkowa i administracyjna",
        "osoby_podmioty": "Franciszek Frankiewicz (exaktor), Leśni miejscy, Młodsi cechowi, Flisacy, Dégin (komisarz rewizji kas), Podwojewodzi Lubelski, Czarnicki (właściciel gruntów), Aleksander Alkiewicz (pisarz miejski), Kanonicy Regularni, Poborca Komory Lubelskiej",
        "opis_pozycji": "Ciąg dalszy expensy miejskiej: zakupy paszy dla wojska (31 zł 23 gr); opłaty dla służby leśnej i cechowej za egzekucje i chwytanie zbiegłych flisów (24 zł 7 gr); ugoszczenie komisarza Dégina podczas rewizji kas (wódka, wino, piwo dubeltowe, obrok – 44 zł 14 gr); taksa i rewizja miar przez Podwojewodziego (31 zł); czynsz dzierżawny dla JP Czarnickiego (8 zł 15 gr); kwartalne rezydencje magistratu (24 zł); pensja pisarza miejskiego Aleksandra Alkiewicza za 1 1/2 roku (225 zł); dwie raty podymnego koronnego za 1780 r. odprowadzone do Komory Lubelskiej (1778 zł) wraz z podwodami (23 zł 27 gr); marcowa rata podymnego za 1781 r. (894 zł) oraz podwoda (16 zł 15 gr). Suma Latus: 4221 zł 2 gr.",
        "kwoty_miary": "Transport Expensy 1119 zł 10 gr; Suma wydatków podatkowo-urzędowych 3101 zł 22 gr; Latus: 4221 zł 2 gr.",
        "uwagi": "Dokumentacja ciężarów państwowych (podatek podymnego Rzeczypospolitej z całego okręgu kraśnickiego) oraz nadzoru miar handlowych przez podwojewodziego.",
        "transkrypcja": """[PAGINA 91]
[Expensa Furażowa, Rewizje Urzędowe, Pisarz Alkiewicz i Podatek Podymnego]

### Continuat[io] Dalsza Expensa 91:

| Pozycja rozchodu | Wyszczególnienie wydatku i podstawa asygnacji | Złote | Grosze |
| :--- | :--- | :---: | :---: |
| **Transport Expensy** | Z poprzedniej strony (Pag. 90v, w kalkulacji: 1119 zł 10 gr) | 1119 | 10 |
| **Furaż dla Woyska** | Za Siano y owies kupione na Expensę przechodzącego Woyska zapłacił Exaktor | 31 | 23 |
| **Egzekucje i Łapanie Flisów** | Leśnym y Młodszym Cechowym od Exekwowania Podatkow, łapania Flisow po kilkarazy za Pracę Jch y na Konestacyą | 24 | 7 |
| **Rewizya Kas (JP Dégin)** | Expensa dla Jmci Pana [Jana] Degina podczas Rewizyi Kas, na Wódkę, Wino, Piwo Dubeltowe, Obrok, siano | 44 | 14 |
| **Rewizya Miar Handlowych** | Od Bytność W. Jmci Pana Podwoiewodzkiego [Lubelskiego] dla Rewizyi Miar, Taxa ustanowienia | 31 | — |
| **Czynsz z Łąk** | Czynszu z Łąk Mieyskich podług Kwitu Jmci P. Czarnickiego | 8 | 15 |
| **Rezydencye Kwartalne** | Podczas Kwartalney Rezydencyi zdaiąc ieden drugiemu Rezydencyą wyszło za Kwartalow 6 | 24 | — |
| **Solarium Pisarza Mieyskiego** | Solarium P. Pisarzowi Mieyskiemu [Aleksandrowi] Alkiewiczowi wypłacił Exaktor za pułtora Roku zupełnie do teraznieyszey Elekcyi | 225 | — |
| **Podymne Koronne 1780** | Podymnego za Rok przeszły 1780 Rat dwie Marcową y Jbrową [Wrześniową] z Miasta, Przedmieścia, z Żydami y Klasztorem Jmć Kanoników Regularnych za dwoma Kwitami z Komory Lubelskiey | 1778 | — |
| **Podwody Podymnego 1780** | Za Podwody y Posłańcowi Odwożącego dworzyszego Podymnego y na supplement | 23 | 27 |
| **Podymne Koronne 1781** | Ao 1781 Wypłacił Exaktor Podymnego Ratę Marcową podług Kwitu | 894 | — |
| **Podwoda Podymnego 1781** | Za Podwodę y supplement odwożącego Ratę Podymnego | 16 | 15 |
| **LATUS** | **Łączny rozchód z karty Pag. 91** | **4221** | **2** |"""
    },
    "189": {
        "tytul": "Rachunki miejskie: Rozliczenie dawnych pretensji exaktora Rycerza, zwolnienie Paszkiewicza i prowizje",
        "data_rok": "1781-05-16",
        "kategoria": "Rachunki miejskie / Rozliczenie pretensji exaktorskich i rewizja",
        "osoby_podmioty": "Kazimierz Rycerz (b. exaktor), Dybek, Tomasz Śliwiński (b. pisarz), Ziębiński (rewizor), Andrzej Wyszyński (sędzia generalny), Józef Paszkiewicz (mieszczanin), Franciszek Frankiewicz (exaktor), Walenty Łukasik (exaktor)",
        "opis_pozycji": "Rozliczenie wzajemnych pretensji finansowych dawnych urzędników: roszczenia Kazimierza Rycerza z 1777 r. (31 zł 24 gr), pretensje despektowe, potrącenia za owies od Dybka, koszty żołnierskie i czynsz łąkowy (15 zł); zwrot za zgubiony przez pisarza Śliwińskiego klucz (1 zł); honorarium sędziego Andrzeja Wyszyńskiego wypłacone przez JP Ziębińskiego za inwentarz sympli i rewizję kas (47 zł 10 gr); wydatki Rycerza z elekcji 1779 r. (97 zł 7 1/2 gr); umorzenie długu 245 zł Józefa Paszkiewicza uwolnionego dekretem delegacji po złożeniu przysięgi oczyszczającej (zaksięgowane bilansowo jako wypłacone); darowizna dla Rycerza i wspólnika (10 zł 27 1/2 gr); prowizja exaktorska dla Frankiewicza i Łukasika za 1 1/2 roku po 100 zł rocznie (150 zł). Suma Latus: 4927 zł 11 gr.",
        "kwoty_miary": "Transport Expensy 4221 zł 2 gr; Pozycje rozchodu 706 zł 9 gr; Latus: 4927 zł 11 gr.",
        "uwagi": "Oficjalne zamknięcie sprawy długu Paszkiewicza z czasów konfederacji barskiej (siano dla pikiet) oraz audyt pretensji dawnej egzakcji Kazimierza Rycerza.",
        "transkrypcja": """[PAGINA 91v]
[Rozliczenie Pretensji Dawnych Exaktorów, Rewizja Kas i Prowizja Frankiewicza]

### Continuatur Dalsza Expensa 91v:

| Pozycja rozchodu | Tytuł wydatku, odbiorca i dekret weryfikacyjny | Złote | Grosze |
| :--- | :--- | :---: | :---: |
| **Transport Expensy** | Z poprzedniej strony (Pag. 91) | 4221 | 2 |
| **Pretensye Kazimierza Rycerza** | Kazimierz Rycerz Regestrem swoim podał Expensy jeszcze in Anno 1777 | 31 | 24 |
| **Despekty i Należności Rycerza** | Tenże Rycerz podał w swoim Regestrze Expensy despektu Złł 4 nieodebranych, od Dybka Złł 2 gr 24 za Owies, Od lal żołnierzy Złł [2] gr 15, Czynszu z Łąki Złł 6 gr 6 | 15 | — |
| **Klucz Kancelaryjny** | Za Klucz przez [Tomasza] Śliwińskiego zgubiony | 1 | — |
| **Honorarium Sędziowskie i Rewizya** | Ao 1780 d. 28 7bris podług Kwitu Jmci P. Ziębińskiego wypłacił Exaktor od ułożenia Jnwentarza Symplowego y Rewizyi Kas, na Fundamencie Jnstrumentu W[ielmożne]mu Panu Sędziemu [Andrzejowi Wyszyńskiemu] Honorarium oznaczone y na supplement | 47 | 10 |
| **Expensa Elekcyjna 1779** | Podług Regestru Kazimierza Rycerza podaney Expensy podczas przeszłey Elekcyi Złł | 97 | 7 1/2 |
| **Zwolnienie Długu Paszkiewicza** | Jozef Paszkiewicz będąc w Retencie do Kassy Mieyskiey winien Złł 245 na które podczas przeszłey Elekcyi 1779 Ao przysiągł przy ukazaniu swoich pretensyi, gdzie Dekretem Delegackim od płacenia iest uwolniony, Dla tego za wypłaconą do linii zaciąga się | 245 | — |
| **Darowizna dla Exaktora** | Do tego Temuż Rycerzowi iako Exaktorowi y Spolnikowi iego darowano zostało | 10 | 27 1/2 |
| **Salarium Exaktorskie** | Salarium Exaktorowie teraznieysi [Frankiewicz i Łukasik] odebrali sobie za pułtora lata na Rok po Złł 100 ff. | 150 | — |
| **LATUS** | **Łączny rozchód z karty Pag. 91v** | **4927** | **11** |"""
    },
    "190": {
        "tytul": "Rachunki miejskie: Zamknięcie bilansu Expensy 1779–1781, rozliczenie retentów i zwrot nadpłaty",
        "data_rok": "1781-05-16",
        "kategoria": "Rachunki miejskie / Zamknięcie bilansu dwuletniego i retenta",
        "osoby_podmioty": "Franciszek Frankiewicz (exaktor), Żyd Kotlarz, Woźny miejski, Stróż nocny, Rezydent magistratu, Błażej Chruściel, Tomasz Śliwiński (b. pisarz), Kazimierz Rycerz (dłużnik z przysięgi)",
        "opis_pozycji": "Ostateczne podsumowanie rozchodów egzakcji Frankiewicza: rekompensata za worek skradziony przez Moskali Żydowi kotlarzowi (18 zł); kwit magistratu na bieżące opłaty woźnego, stróża, diety rezydencjonalne i kuriera z cyrkularzem elekcyjnym do Janowa (19 zł 4 gr); pomocne dla Błażeja Chruściela na koszty sądowe (8 zł 25 gr); ostateczne wyrównanie dla pisarza Śliwińskiego za zasługi, stemplowany papier, klucz i czekoladę (9 zł 15 gr). Zamknięcie Expensy Generalnej: 4884 zł 5 gr. Wykaz retentów (zaległości): dług Rycerza pod przysięgą (163 zł 13 1/2 gr) oraz nieściągnięte symple i podymne (163 zł) – suma retentów i expensy: 5210 zł 26 1/2 gr. Wykazanie nadpłaty exaktora w kwocie 37 zł 3 1/2 gr do zwrotu z kasy miejskiej.",
        "kwoty_miary": "Transport Expensy 4827 zł 11 gr; Suma Peretta Expensy: 4884 zł 5 gr; Retenta: 326 zł 13 1/2 gr; Summa Ogólna: 5210 zł 26 1/2 gr; Nadpłata do zwrotu: 37 zł 3 1/2 gr.",
        "uwagi": "Precyzyjne zamknięcie bilansu miejskiego przed wolną elekcją w maju 1781 r., pieczętujące uczciwe rozliczenie kasy przez Franciszka Frankiewicza.",
        "transkrypcja": """[PAGINA 92]
[Zamknięcie Rachunku Expensy 1779–1781, Retenta Podatkowe i Rozliczenie Nadpłaty]

### Continuat[io] Dalsza Expensa 92:

| Pozycja rozchodu | Opis wydatku i asygnacja Magistratu | Złote | Grosze |
| :--- | :--- | :---: | :---: |
| **Transport Expensy** | Z poprzedniej strony (Pag. 91v, w zapisie: 4827 zł 11 gr) | 4827 | 11 |
| **Szkoda wojenna (Żyd Kotlarz)** | 1780 Za worek wzięty przez Moskalow od Żyda Kotlarza podług Kwitu Magistratu zapłacił Exaktor | 18 | — |
| **Kwit Magistratu z 16 Maja 1781** | Woźnemu Złł 5 gr 10; Stróżowi nocnemu Złł 4; Danie Rezydencyi Rezydentowi Złł 4; Posłańcowi do Janowa z Cyrkularzem z ogłoszeniem Elekcyi Złł 1 gr 15; z Jnney Expensy wynikającey z tegoż Kwitu — facit: | 19 | 4 |
| **Pomocne Sądowe** | Pomocne Błazeiowi Chruścielowi od pozwolenia Rezydencyi na Sędy do zjedzenia | 8 | 25 |
| **Ostateczne rozliczenie Śliwińskiego** | Śliwińskiemu Pisarzowi przeszłemu Reszty Zasług Złł Sześć, za papier stęplowany Złł 2 gr 9, za Klucz Złł 1, za Czekułady Groszy 6, ff. | 9 | 15 |
| **IN SUMMA PERETTA EXPENSY** | **Całkowita Rzeczywista Suma Wydatków Kasy Miejskiej** | **4884** | **5** |

---

### Retenta (Zaległości do Wybrania do Kasy Miejskiej):

| Pozycja retentów | Dłużnik / Kategoria należności | Złote | Grosze |
| :--- | :--- | :---: | :---: |
| **Zaległość Kazimierza Rycerza** | Od Kazimierza Rycerza należy Reszty do Kassy Mieyskiey podług wykonaney przysięgi iego | 163 | 13 1/2 |
| **Zaległości Obywatelskie** | Z Regestrow Symplowych y Dymowych znayduie się do wybrania y dobrania do Kassy Mieyskiey Złł | 163 | — |
| **SUMMARUM ZŁŁ POL.** | **Łączna suma Expensy wraz z Retentami** | **5210** | **26 1/2** |

---

### Deklaracja Nadpłaty Egzaktorskiej:
*Ukazuię się naddanych twierdzą, a że Solarium nieodebrał więc z Kassy Mieyskiey należy Złł Trzydzieści Siedm gro 3 1/2 [37 zł 3 1/2 gr].*"""
    }
}

with open('/home/ubuntu/workspace/Gen/part11_trans_1.json', 'w', encoding='utf-8') as f:
    json.dump(part1_trans, f, ensure_ascii=False, indent=2)

print("Zapisano part11_trans_1.json pomyślnie.")
