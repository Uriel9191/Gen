---
name: paleografia-krasnik
description: >-
  Kompleksowy przewodnik i metodyka paleografii staropolskiej XVIII w.,
  transkrypcji dyplomatycznej akt miejskich (Akta Miasta Kraśnika),
  budowy baz genealogiczno-indeksowych, procedury opracowania nowych jednostek
  oraz architektury UI/UX kompendiów cyfrowych na wzór Jednostki 40.
---

# Metodyka Paleografii, Transkrypcji Dyplomatycznej, Indeksowania Genealogicznego i Standardu UI Kompendiów (Akta Miasta Kraśnika)

Niniejszy dokument stanowi oficjalny, nienaruszalny kanon metodyczny pracy z osiemnastowiecznymi rękopisami miejskimi (w szczególności zespołem Akta Miasta Kraśnika z Archiwum Państwowego w Lublinie, sygn. 35/40/0/1/40 i jednostkami pokrewnymi). 

Łączy on zasady rygorystycznej edycji źródeł historycznych, wytyczne genealogiczne kuzyna, procedurę weryfikacji post-transkrypcyjnej oraz wymogi techniczno-interfejsowe użytkownika zrealizowane w Jednostce 40.

--------------------------------------------------------------------------------

## I. Kanon Transkrypcji Źródłowej i Rozwiązywania Wątpliwości

### 1. Zasada Dosłowności Dyplomatycznej
* Transkrypcja odzwierciedla **dokładne, oryginalne brzmienie tekstu**: archaizmy, ortografię epoki (np. *y* zamiast *i*, *x* w zapisie łacińskim i liczebnikach, formy typu *pospulstwo*, *expensa*, *percepta*), fleksję i skróty kancelaryjne.
* Zachowujemy oryginalny układ akapitów, nagłówków, kolumn oraz rozliczeń kasowych.

### 2. Oznaczenia Niepewności `[opcja 1? / opcja 2?]` (Kluczowa Zasada)
Gdy dukt pisma, uszkodzenie papieru, zalanie atramentem lub kontrast skanu powoduje dwuznaczność:
* **NIGDY nie zgadujemy ani nie wybieramy lekcji „na siłę”**.
* Zapisujemy niepewny fragment w **nawiasach kwadratowych ze znakiem zapytania**:
  * **Imiona**: np. `Szymon [lub Szymonik?]`, `Wojciech [Woytek?]`, `Jan [Janusz?]`.
  * **Nazwiska**: np. `Pełka [lub Petka?]`, `Drąś [lub Dray / Drąg?]`, `Rachoń [lub Bachoń?]`, `Zieliński [lub Dieliński?]`, `Jaczniak [lub Jacniak?]`.
  * **Miejscowości i Przedmieścia**: np. `Zarzyce [lub Zarzecze?]`, `Piasek [lub Piaski?]`.
  * **Kwoty i Liczby**: np. `18 [lub 10?]`, `28 [lub 20?]`, `13 [lub 18?]`.
  * **Wielowariantowość**: Dopuszczalne i zalecane jest podawanie więcej niż dwóch opcji w nawiasie: `[Wariant A / Wariant B / Wariant C?]`.

### 3. Paleografia Osiemnastowieczna – Zasady Rozpoznawania Znaków
* **Cyfra `8` vs `0`**: Pisarze epoki stanisławowskiej kreślili cyfrę `8` jako owal z wewnętrzną skośną poprzeczką lub z otwartą górną pętlą. Przy mocnym kontraście czarno-białego mikrofilmu poprzeczka może zlewać się z konturem, przez co `18` i `28` wyglądają złudnie jak `10` i `20`. Każda wątpliwa cyfra musi być sprawdzona w powiększeniu oraz zweryfikowana z sumą kolumny (`Latus`).
* **Litery `ł` vs `t`**: W polskiej kursywie XVIII w. litera *ł* była często kreślona z poziomą kreską przecinającą trzon identycznie jak *t* (stąd pomyłki typu *Petka* zamiast *Pełka*). Należy weryfikować kontekst onomastyczny i rodzinny.
* **Litery `R` vs `B`**: Majuskuła *R* w pismach kancelaryjnych posiadała dekoracyjny, zamknięty brzuszek, przypominający literę *B* (np. *Rachoń* vs *Bachoń*). Weryfikować poprzez porównanie z niewątpliwymi słowami na tej samej karcie (np. *Ratusz*, *Regestr*).
* **Litery `Z` vs `D`**: Ozdobna majuskuła *Z* kreślona z dolną pętlą schodzącą pod linię bazową bywa mylona z *D* (np. *Zieliński* vs *Dieliński*).
* **Litery `ś` vs `y` na końcu wyrazu**: Końcowe *ś* z zamaszystym ogonkiem w dół bywa mylone z *y* (np. *Drąś* vs *Dray*).

### 4. Matematyczne Bilansowanie Rejestrów Skarbowych (Złote i Grosze)
* Przelicznik monetarny Rzeczypospolitej: **1 Złoty polski (Floren) = 30 Groszy**.
* Przed zatwierdzeniem taryfy sympli, podymnego lub percept/expens należy **bezwzględnie przeliczyć sumę kontrolną kolumny**:
  $$\text{Suma Groszy} = \sum (\text{Złote} \times 30 + \text{Grosze})$$
* Jeśli suma pozycji różni się od wpisanego na karcie `1mu Latus` lub `2dum Latus`, w pierwszej kolejności sprawdzane są pozycje z cyframi `0/8`, `13/18`, `23/28` oraz kolumnowe przesunięcia (np. `11 gr` vs `1 zł 1 gr`).

### 5. Integralność Kolumnowa i Kierunek Czytania
* **ZAKAZ czytania poprzecznego (wierszami z lewej do prawej przez całą stronę)**, jeśli strona ma strukturę dwukolumnową z osobnymi nagłówkami i osobnymi sumowaniami `Latus`.
* Zawsze czytamy **od góry do dołu całą Kolumnę 1**, a następnie **od góry do dołu Kolumnę 2**.
* Zmiana nagłówka terytorialnego wewnątrz kolumny (np. pojawienie się podtytułu `Przedmie: Zarzyce` w połowie prawej kolumny) dotyczy **wyłącznie pozycji poniżej tego nagłówka w tej samej kolumnie**, a nie pozycji z sąsiedniej kolumny.

--------------------------------------------------------------------------------

## II. Standard Skorowidza Genealogicznego (Wytyczne Kuzyna)

Skorowidz genealogiczny to baza konkretnych osób fizycznych żyjących i działających w Kraśniku, służąca do rekonstrukcji drzew rodzinnych i badań demograficznych.

### 1. Struktura Kolumn Tabeli Genealogicznej
1. **Lp.** (Liczba porządkowa)
2. **Nazwisko** (Standaryzowane do formy współczesnej)
3. **Imię** (Standaryzowane do formy współczesnej)
4. **Miejsce zamieszkania** (Miasto Kraśnik, Piaski, Góry i Podlesie, Zarzecze, Budzyn, Cegielnia itp.)
5. **Funkcja społeczna / Zawód / Urząd** (Wójt, Burmistrz, Ławnik, Pisarz, Exaktor, Szewc, Cechmistrz tkacki, Kahał itp.)
6. **Nr skanów** (Wszystkie skany, na których dana osoba występuje w jednostce)
7. **Zakres lat** (Skrajne daty wystąpień w aktach, np. 1761–1788)

### 2. Eliminacja Podmiotów Nieosobowych
* **Bezwzględnie usuwać ze spisu genealogicznego**:
  * Podmioty techniczno-archiwalne: operator mikrofilmu, Archiwum Państwowe, Sąd Pokoju Powiatu Kraśnickiego,
  * Podmioty zbiorowe i ogólne: *Przedmieszczanie Gór i Podlesia*, *Mieszkańcy Zarzecza*, *Pospólstwo*, *Kahał żydowski (zbiorczo)*.
* W skorowidzu umieszczać **wyłącznie konkretne, pojedyncze osoby**.

### 3. Standaryzacja Nazwisk i Imion
* W kolumnach głównych wpisujemy formy współczesne (np. *Wojciech Pełka*, a nie *Woyciech Petka*).
* Oryginalny zapis źródłowy podajemy w oknie szczegółów/uwag po kliknięciu na rekord.
* Nie wprowadzamy osób bez imion, chyba że z bezpośredniego kontekstu aktu (relacji rodzinnych, spadkowych) da się to imię jednoznacznie ustalić.
* **Kobiety i Wdowy**:
  * Zapisy typu *Janowa Jajczykowa*, *Stachowa Rodzonkowa*, *Kępina Wdowa*:
    * Nazwisko: forma męska podstawowa (*Jajczyk*, *Rodzonek*, *Kępa* – po usunięciu końcówek *-owa*, *-ina*),
    * Imię: forma odnotowana (*Janowa*, *Stanisławowa*).
    * Jeśli w spisie występuje zmarły mąż, wdowę umieszczamy bezpośrednio po nim.

### 4. Kryteria Tożsamości Osób (De-duplikacja)
* Jeśli dana osoba pojawia się na wielu skanach, w skorowidzu ma **dokładnie jeden rekord**, a kolejne skany i lata dopisywane są w ostatnich dwóch kolumnach.
* **Tożsamość**: To samo imię i nazwisko na tym samym przedmieściu, w sąsiedztwie tych samych gospodarzy = ta sama osoba.
* **Odrębność**: Ta sama kombinacja imienia i nazwiska występująca na innym przedmieściu lub w zupełnie innej epoce = odrębna pozycja na liście.
* **Weryfikacja w Lubgens**: Wykorzystywana wyłącznie w przypadku realnych wątpliwości onomastycznych; w razie braku potwierdzenia stosować oznaczenie `[?]`.
* **Zakaz zgadywania zawodu po nazwisku**: Nie wnioskować zawodu szewca z nazwiska *Szewc/Szewczyk*, rymarza z *Rymarczyk* itp. Jeśli zawód wynika z kontekstu, ale nie jest pewny, opatrywać go symbolem `[?]`.
* **Ograniczenie łaciny**: Krótkie glosy łacińskie dopuszczalne wyłącznie w nawiasie w szczegółach rekordu.

### 5. Postępowanie z Nazwiskami Niepewnymi i Alternatywnymi Lekcjami (Wariant 2 - Obowiązujący Standard)
* **Zasada bezwzględna: 1 fizyczna osoba = 1 rekord w bazie**:
  * Kategoryczny zakaz tworzenia sztucznych, zdublowanych wierszy w skorowidzu dla wariantów nazwiska tej samej osoby (np. zakaz tworzenia jednego rekordu dla *Jan Drąś* i drugiego dla *Jan Drozd*).
  * Zdublowane wpisy tworzą nieistniejące „osoby-widma” i zniekształcają statystyki zaludnienia, podatków oraz posesjonatów.
* **Struktura danych i pole `wariant_nazwiska`**:
  * W obiekcie `genData` wprowadzamy dedykowane pole:
    `"nazwisko": "Drąś", "wariant_nazwiska": "Drozd?"`
* **Prezentacja wizualna w komórce tabeli (Dwupoziomowy układ)**:
  * W komórce „Nazwisko” renderujemy formę główną w `<strong>`, a bezpośrednio pod nią subtelny, ciemny badge z wariantem:
    ```html
    <strong>Drąś</strong>
    <div style="font-size:0.75rem; color:#94a3b8; margin-top:2px; display:inline-block; padding:1px 5px; background:rgba(255,255,255,0.05); border-radius:3px; border:1px solid #334155;">wariant: Drozd?</div>
    ```
* **Integracja z wyszukiwarką na żywo**:
  * Silnik wyszukiwarki przeszukuje równolegle oba pola:
    `d.nazwisko.toLowerCase().includes(query) || (d.wariant_nazwiska && d.wariant_nazwiska.toLowerCase().includes(query))`
  * Wpisanie zarówno formy głównej (*Drąś*), jak i alternatywnej (*Drozd*) natychmiast filtruje i wyświetla ten sam jeden rekord.
* **Okno szczegółów osoby (Modal Genealogiczny)**:
  * Po kliknięciu wiersza w tabeli, w oknie modalnym prezentowana jest sekcja:
    *Warianty nazwiska i uwagi paleograficzne: [Drąś / Drozd?]. Przyczyna wątpliwości: litery -ąś/-ozd zatarte w zgięciu karty rękopisu na Skanie #41.*

--------------------------------------------------------------------------------

## III. Procedura Opracowania Nowej Jednostki (End-to-End Workflow)

Każda nowa jednostka archiwalna przechodzi przez ustrukturyzowany, 6-etapowy proces badawczy:

### Krok 1: Inwentaryzacja i Kodykologia Surowych Skanów
* Pobranie paczki skanów (Google Drive lub portal *Szukaj w Archiwach*), rozpakowanie do katalogu roboczego (`krasnik_skany_jX`).
* Sprawdzenie ciągłości numeracji plików, odnalezienie klatek metryk archiwalnych (początkowej i końcowej) oraz identyfikacja klatek podwójnych (dubletów mikrofilmu).
* Rozpoznanie charakteru jednostki: księga elekcji/rachunków, protokoły sądowe radzieckie/wójtowskie, regestry podatkowe czy fascykuły luźne.
* Sprawdzenie układu foliacji i paginacji (karty paginowane, nieliczbowane, pagina vs folio).

### Krok 2: Przygotowanie Planu Etapowego i Bramka Akceptacji
* Podział jednostki na logiczne partie robocze (zwykle po 15–20 skanów).
* Przedstawienie szczegółowego planu w czacie i oczekiwanie na wyraźną akceptację użytkownika przed rozpoczęciem modyfikacji kodu.

### Krok 3: Rygorystyczna Transkrypcja 100% Skanów i Zasady Linkowania do Szukaj w Archiwach
* **Każdy skan jednostki bez wyjątku** musi posiadać:
  * Wypełnione pole `transkrypcja`: rygorystyczny, pełny odczyt dyplomatyczny z zachowaniem kolumn i notacją wątpliwości `[opcja 1? / opcja 2?]` (bezwzględny zakaz zgadywania liter; szczególny rygor dla imion, nazwisk, toponimów i kwot).
  * Wypełnione pole `link_swa`: oficjalny odnośnik do **całej jednostki archiwalnej** w portalu *Szukaj w Archiwach* (`https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/{id_jednostki}`).
* **Zasada techniczna linkowania do Szukaj w Archiwach (SwA)**:
  * Portal SwA działa w architekturze Single Page Application – otwarcie skanu w przeglądarce portalu nie modyfikuje adresu URL jednostki.
  * **Kategoryczny zakaz linkowania do poszczególnych plików/obiektów cyfrowych** (odnośniki do `obiekty/ID` prowadzą jedynie do ubogiej metryczki tekstowej, a nie do przeglądarki skanu).
  * Obowiązuje standard wypracowany w J40:
    1. Przycisk główny (złoty): link do **całej jednostki archiwalnej** (`https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/{id_jednostki}`).
    2. Przycisk pomocniczy: link do **całego Zespołu 35/40/0 (Akta m. Kraśnika)** (`https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/1890`).
    3. Boks instrukcji nawigacji: krok po kroku informujący użytkownika, aby w portalu przeszedł do zakładki **„Skany”** i wybrał miniaturę oznaczoną numerem **#{item.nr_skanu}**.
* Matematyczne bilansowanie kolumn skarbowych (`Latus`, 1 zł = 30 gr).

### Krok 4: Równoległe Zasilanie Skorowidza Genealogicznego
* Wraz z transkrypcją każdego skanu prowadzona jest systematyczna ekstrakcja osób do tablicy `genData` zgodnie ze standardem z Rozdziału II.

### Krok 5: Post-Transkrypcyjna Weryfikacja i Uzgodnienie (Reconciliation Pass)
* **Po ukończeniu pełnej transkrypcji wszystkich skanów jednostki**:
  * Przeprowadzana jest całościowa konfrontacja wstępnych opisów (`opis_pozycji`), kategorii (`kategoria`), dat rocznych (`data_rok`) oraz syntezy monograficznej z gotowymi transkrypcjami.
  * **Obowiązkowa korekta rozbieżności**: Wszelkie błędy datowania wynikające ze wstępnego szacowania (np. akt z marca 1766 r. błędnie oznaczony wcześniej jako 1764 r.), niedokładności streszczeń lub przeoczone nazwiska stron transakcji są bezwzględnie poprawiane w metadanych i monografii.

### Krok 6: Testy Integralności i Wdrożenie do Repozytorium
* Audyt składni i integralności JSON za pomocą Node.js / Python (`mainData` i `genData`).
* Sprawdzenie, czy 100% skanów posiada transkrypcję i poprawne linki.
* Sukcesywne commity i push do zdalnego repozytorium GitHub na gałęzi `main`.

--------------------------------------------------------------------------------

## IV. Standard Architektury i UI / UX Kompendium (Wzorzec J40)

Każde kompendium jednostki (np. `krasnik_j40_kompendium_calosc.html`) musi zachowywać **identyczną szatę graficzną, ergonomię i układ komponentów**:

### 1. Stylistyka i Paleta Kolorów (Dark Slate Theme)
* Tło strony i kontenerów: głęboki grafit/granat (`#0f172a`, `#1e293b`),
* Krawędzie kart i separatory: stonowany łupek (`#334155`),
* Akcenty, nagłówki i przyciski aktywne: ciepły bursztyn/złoto (`#f59e0b`, `#d97706`),
* Statusy i wskaźniki pomyślności: szmaragdowa zieleń (`#10b981`),
* Czcionki: nowoczesny, bezszeryfowy krój systemowy (Inter, Segoe UI) dla interfejsu; czcionka stałej szerokości (*monospace*: Menlo, Consolas, Monaco) dla pola transkrypcji.

### 2. Górny Pasek Metryk KPI
* 4 karty statystyk u góry strony:
  1. *Liczba skanów jednostki*,
  2. *Zakres chronologiczny (daty skrajne)*,
  3. *Liczba zidentyfikowanych osób fizycznych*,
  4. *Wolumen transkrypcji dyplomatycznej (100% ukończenia)*.

### 3. Sekcja Monograficzna i Odkrycia Źródłowe
* Zorganizowana w przejrzyste, zwijane panele (Accordion) obejmujące:
  * Kodykologię i charakterystykę źródłoznawczą,
  * Ustrój samorządowy i elity władzy,
  * Gospodarkę, finanse i wielkie bilanse,
  * Odkrycia społeczno-religijne i oświatowe,
  * Tablicę chronologiczną przełomowych faktów.

### 4. Tabela Rejestru Skanów
* Kolumny tabeli: *Nr skanu, Pagina, Data/Rok, Kategoria, Osoby/Podmioty, Opis pozycji, Kwoty/Miary, Akcje (Szczegóły)*.
* Wyszukiwarka tekstowa na żywo filtrująca wszystkie pola rekordu.
* Filtry kategoryczne i chronologiczne.
* **Paginacja ze skokiem bezpośrednim**: Kontrolki Poprzednia / Następna oraz pole tekstowe umożliwiające **wpisanie z klawiatury dokładnego numeru skanu i natychmiastowe przejście do niego**.
* Kwoty w kolumnie *Kwoty/Miary* formatowane pionowo, jedna pod drugą, z redukcją nadmiaru skrótów.

### 5. Trzyczęściowy Modal Skanu (Pop-up)
Każdy rekord po kliknięciu otwiera modal z trzema zakładkami:
* **Zakładka 1: Opis i metadane** (kompletna metryka archiwalna, pagina, data, osoby, kwoty, uwagi).
* **Zakładka 2: Transkrypcja źródłowa** (pełny tekst z przyciskiem kopiowania do schowka, zachowaniem podziału na kolumny i notacją wątpliwości `[opcja?]`).
* **Zakładka 3: Link do oryginału** (oficjalne kafle przekierowujące do całej jednostki w SwA i zespołu 35/40/0, wraz z instrukcją przejścia do zakładki «Skany» i wyboru miniatury danego skanu).

### 6. Tabela Skorowidza Genealogicznego
* Dedykowana tabela osób fizycznych zintegrowana z bazą `genData`.
* Sortowanie po dowolnej kolumnie (domyślnie alfabetycznie po nazwisku).
* Modal/okno szczegółów osoby prezentujące wszystkie wystąpienia na skanach oraz oryginalny zapis źródłowy.
