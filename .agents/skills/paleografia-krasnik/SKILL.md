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
* **Żelazna Zasada 100% Synchronizacji Onomastycznej (Automatyczny Audyt Wariantów)**:
  * **Bezwzględny nakaz mapowania z nawiasów `[...]` do `wariant_nazwiska`**: Każde nazwisko, imię lub przezwisko posiadające w transkrypcji alternatywną lekcję paleograficzną w nawiasie kwadratowym (np. `Antoni Łyżik [Łyżwa / Łyżik? / Pyzik?]`, `Wojciech Drąś [Draj?]`, `Wawrzyniec Starobrat [Starosrat?]`, `Walenty Jordel [Gorgiel?]`) **MUSI natychmiast posiadać zaktualizowane pole `wariant_nazwiska` w tablicy `genData`**.
  * **Zakaz pozostawiania `wariant_nazwiska: null`** dla osób z wątpliwościami źródłowymi. Jeśli w transkrypcji podano wariant, brak wpisania go w `wariant_nazwiska` jest traktowany jako błąd krytyczny.
  * **Obowiązkowy programistyczny test weryfikacyjny**: Przed zamknięciem jakiejkolwiek partii skanów agent ma bezwzględny obowiązek uruchomić automatyczny test (Python/Node) sprawdzający, czy 100% wariantów z nawiasów kwadratowych w danej partii zwraca trafienie w wyszukiwarce `genData`. Brak trafienia blokuje zakończenie partii.
  * **Równoległy eksport do pliku CSV**: Po każdej partii stan bazy `genData` jest eksportowany do pliku `krasnik_jXX_slownik_genealogiczny.csv` z dedykowaną kolumną `Wariant nazwiska`.
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

### Krok 6: Obowiązkowa Aktualizacja Syntezy Monograficznej, Kluczowych Odkryć oraz Weryfikacja Techniczna UI (Standard J40)
* **Po zakończeniu transkrypcji 100% skanów jednostki bezwzględnie wymagana jest całościowa finalizacja obu zakładek analitycznych**:
  1. **Zakładka «Pełna Synteza Monograficzna»**:
     * Nie może pozostać wstępnym szkicem z początku prac. Musi stanowić dojrzałą monografię naukową woluminu (rozdziały: kodykologia i proweniencja, ustrój i elity władzy, gospodarka i skarbowość, oświata i walka z analfabetyzmem, relacje chrześcijańsko-żydowskie i cechy, sądownictwo i dyscyplina, pełna tablica chronologiczna).
  2. **Zakładka «Kluczowe Odkrycia i Przełomy»**:
     * Musi zawierać wyczerpujące, wielopunktowe omówienie przełomów faktograficznych, ustrojowych i genealogicznych jednostki (m.in. demistyfikacja etykiety archiwalnej, udział Żydów w zarządach cechów, modelowa księgowość miejska, fundusze oświatowe KEN, organizacja straży ogniowej).
  3. **Rygorystyczny Audyt Interfejsu i Liczników Genealogicznych**:
     * **Integralność DOM zakładek**: Każda zakładka w pasku nawigacyjnym (`tabs-nav`) musi posiadać odpowiadający jej element `<section id="..." class="tab-content">`. Zabronione jest pomijanie tagu otwierającego `<section>` lub błędy w ID powodujące rzucenie wyjątku JavaScript przy `switchTab`.
     * **Dynamiczna synchronizacja liczników (Zero Hardcodowania)**: Licznik osób w przycisku Słownika Genealogicznego (`.tab-badge`) oraz na kartach KPI musi być powiązany dynamicznie z `genData.length` (oraz `mainData.length`). Niedopuszczalne są zdezaktualizowane, statyczne liczby (np. 780 zamiast rzeczywistej liczby 975 osób).
     * **Odporność wyszukiwarki genealogicznej**: Funkcja filtrująca (`filterGenData`) musi bezpiecznie obsługiwać pola opcjonalne (zabezpieczenie przed błędem `Cannot read properties of undefined (reading 'toLowerCase')`), przeszukiwać wszystkie metadane (imię, nazwisko, warianty, dzielnica, funkcje, skany, biogram) oraz wspierać zapytania wielowyrazowe.
     * **Brak sztucznych limitów**: Paginacja skorowidza genealogicznego musi obejmować pełny zbiór `genData` bez odcinania końcowych rekordów.

### Krok 7: Testy Integralności i Wdrożenie do Repozytorium
* Audyt składni i integralności JSON za pomocą Node.js / Python (`mainData` i `genData`).
* Sprawdzenie, czy 100% skanów posiada transkrypcję i poprawne linki.
* Uruchomienie testów onomastycznych dla wszystkich partii badawczych (100% PASS).
* Sukcesywne commity i push do zdalnego repozytorium GitHub na gałęzi `main`.

--------------------------------------------------------------------------------

## IV. Standard Architektury i UI / UX Kompendium (Żelazny Wzorzec J40)

Każde kompendium jednostki (np. `krasnik_j40_kompendium_calosc.html`) musi zachowywać **identyczną szatę graficzną, ergonomię i układ komponentów „kropka w kropkę jak J40”**. Samowolne modyfikacje liczby kolumn, zmiana nazw nagłówków lub przestawianie domyślnych zakładek są traktowane jako błąd krytyczny. Każda jednostka opracowywana przez dowolnego agenta lub badacza na dowolnej maszynie musi być wizualnie i funkcjonalnie nierozróżnialna od J40.

### 1. Kanoniczny Import Fontów i Zmienne CSS (:root)
W nagłówku `<head>` każdego kompendium bezwzględnie wymagany jest oficjalny zestaw Google Fonts oraz pełna deklaracja zmiennych `:root`.

* **Import Fontów Google Fonts (w tagu `<head>` przed `<style>`)**:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

* **Kanoniczny Blok Zmiennych CSS `:root` (Dark Slate Theme – skopiować 1:1)**:
```css
:root {
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --bg-tertiary: #334155;
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --gold-primary: #f59e0b;
  --gold-glow: rgba(245, 158, 11, 0.25);
  --purple-accent: #8b5cf6;
  --accent-cyan: #06b6d4;
  --border: #334155;
  --card-bg: rgba(30, 41, 59, 0.85);
  --success: #10b981;
}
```

* **Przypisanie krojów pism**:
  - `font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;` dla `body` i całego interfejsu ogólnego,
  - `font-family: 'Cinzel', serif;` dla `h1`, `h2`, `h3`, `.modal-header h3`, tytułów kart monograficznych i analitycznych oraz stylizacji transkrypcji,
  - `font-family: 'JetBrains Mono', monospace;` dla numerów skanów (`#1`), paginacji, liczb w kartach KPI, badge'ów, kwot monetarnych, sum kontrolnych i kodów.

### 2. Kanoniczny Szkielet Dokumentu HTML (DOM Outline)
Hierarchia znaczników `<body>` jest nienaruszalna. Kategorycznie zabrania się stosowania innych nazw klas głównych kontenerów:

```html
<body>

  <!-- 1. NAGŁÓWEK Z LINKIEM POWROTNYM -->
  <header>
    <a href="index.html" class="portal-back-link">← Powrót do Portalu Głównego Jednostek</a><br>
    <div class="header-badge">ARCHIWUM PAŃSTWOWE W LUBLINIE • SYGN. {NR_JEDNOSTKI}</div>
    <h1>Akta Miasta Kraśnika ({LATA})</h1>
    <p class="header-subtitle">
      Księga miejska: {opis charakteru kancelaryjnego, kluczowe warstwy i cezury}.
    </p>
  </header>

  <!-- 2. PASEK GŁÓWNYCH ZAKŁADEK -->
  <nav class="tabs-nav">
    <button class="tab-btn active" onclick="switchTab('main-tab', this)">
      <span>📊 Tabela Indeksowa Skanów</span>
      <span class="tab-badge" id="mainTabBadge">0</span>
    </button>
    <button class="tab-btn gold-tab" onclick="switchTab('genealogy-tab', this)">
      <span>🌳 Słownik Genealogiczny Mieszkańców</span>
      <span class="tab-badge" id="genTabBadge">0</span>
    </button>
    <button class="tab-btn" onclick="switchTab('monograph-tab', this)">
      <span>🏛️ Pełna Synteza Monograficzna</span>
    </button>
    <button class="tab-btn" onclick="switchTab('analytics-tab', this)">
      <span>🔍 Kluczowe Odkrycia i Przełomy</span>
    </button>
  </nav>

  <!-- 3. WYCENTROWANY KONTENER GŁÓWNY (ZAKAZ 'main-container') -->
  <main class="container">
    <section id="main-tab" class="tab-content active">
      <!-- KPI stats-grid -> controls-panel -> pagination-bar -> table-wrapper -->
    </section>

    <section id="genealogy-tab" class="tab-content">
      <!-- KPI stats-grid -> info-box -> controls-panel -> pagination-bar -> table-wrapper -->
    </section>

    <section id="monograph-tab" class="tab-content">
      <div class="monograph-content">
        <!-- Rozdziały syntezy naukowej -->
      </div>
    </section>

    <section id="analytics-tab" class="tab-content">
      <div class="analytics-content">
        <!-- Karty Analityczne i Odkrycia -->
      </div>
    </section>
  </main>

  <!-- 4. MODAL POP-UP ZE SZTYWNYM PASKIEM DOKŁADNIE 3 ZAKŁADEK (ZAKAZ CROPS) -->
  <div id="detailModal" class="modal">
    <div class="modal-content">
      <div class="modal-header">
        <h3 id="modalTitle">Szczegóły</h3>
        <button class="modal-close" onclick="closeModal()">&times;</button>
      </div>
      <div id="modalTabsBar" class="modal-tabs-bar" style="display: none;">
        <button class="modal-tab-btn active" id="tabBtnMeta" onclick="switchModalTab('meta')">📋 Opis i metadane</button>
        <button class="modal-tab-btn" id="tabBtnTrans" onclick="switchModalTab('trans')">📜 Transkrypcja</button>
        <button class="modal-tab-btn" id="tabBtnLink" onclick="switchModalTab('link')">🔗 Link do oryginału</button>
      </div>
      <div class="modal-body" id="modalBody">
        <!-- Wstrzykiwane dynamicznie przez JS -->
      </div>
    </div>
  </div>

  <script>
    // Tablice danych i kanoniczne funkcje JavaScript
  </script>
</body>
```

### 3. Pełny Zestaw Klas CSS (Style Kanoniczne J40)
Wszystkie reguły stylów muszą odpowiadać poniższemu zestawowi reguł J40:

```css
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background-color: var(--bg-primary);
  color: var(--text-main);
  line-height: 1.6;
  padding-bottom: 60px;
}

header {
  background: linear-gradient(180deg, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 0.95) 100%);
  border-bottom: 1px solid var(--border);
  padding: 2.5rem 1.5rem 2rem;
  text-align: center;
  position: relative;
}

.portal-back-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--gold-primary);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  margin-bottom: 1rem;
  padding: 0.35rem 0.85rem;
  border-radius: 6px;
  background: rgba(245, 158, 11, 0.1);
  border: 1px solid rgba(245, 158, 11, 0.25);
  transition: all 0.2s;
}
.portal-back-link:hover {
  background: rgba(245, 158, 11, 0.2);
  transform: translateY(-1px);
}

.header-badge {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--gold-primary);
  background: rgba(245, 158, 11, 0.1);
  border: 1px solid var(--gold-glow);
  padding: 0.35rem 0.85rem;
  border-radius: 9999px;
  margin-bottom: 0.75rem;
}

h1 {
  font-family: 'Cinzel', serif;
  font-size: 2.2rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: 0.5rem;
  color: #fff;
}

.header-subtitle {
  color: var(--text-muted);
  font-size: 1rem;
  max-width: 850px;
  margin: 0 auto;
}

/* NAV TABS */
.tabs-nav {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  padding: 1rem;
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 40;
  flex-wrap: wrap;
}

.tab-btn {
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-muted);
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 0.9rem;
  padding: 0.6rem 1.2rem;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}
.tab-btn:hover {
  color: #fff;
  background: rgba(255, 255, 255, 0.05);
}
.tab-btn.active {
  color: #fff;
  background: var(--bg-tertiary);
  border-color: var(--border);
}
.tab-btn.gold-tab.active {
  border-color: rgba(245, 158, 11, 0.5);
  background: rgba(245, 158, 11, 0.15);
  color: var(--gold-primary);
}

.tab-badge {
  background: rgba(255, 255, 255, 0.1);
  padding: 0.15rem 0.45rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-family: 'JetBrains Mono', monospace;
}

/* KONTENER GŁÓWNY I ZAKŁADKI */
.container {
  max-width: 1500px;
  margin: 0 auto;
  padding: 1.5rem;
}

.tab-content { display: none; }
.tab-content.active { display: block; }

/* KARTY KPI */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.stat-card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 1.25rem;
  position: relative;
  overflow: hidden;
}
.stat-card.gold { border-top: 3px solid var(--gold-primary); }
.stat-card.purple { border-top: 3px solid var(--purple-accent); }
.stat-card.cyan { border-top: 3px solid var(--accent-cyan); }
.stat-card.success { border-top: 3px solid var(--success); }

.stat-title {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-bottom: 0.35rem;
  font-weight: 500;
}
.stat-value {
  font-size: 1.8rem;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  color: #fff;
  margin-bottom: 0.25rem;
}
.stat-desc {
  font-size: 0.8rem;
  color: var(--text-muted);
}

.info-box {
  background: rgba(245, 158, 11, 0.08);
  border: 1px solid rgba(245, 158, 11, 0.25);
  border-radius: 10px;
  padding: 1rem 1.25rem;
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
  line-height: 1.5;
}

/* KONTROLKI, WYSZUKIWARKA, PRZYCISKI */
.controls-panel {
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 1rem 1.25rem;
  margin-bottom: 1.5rem;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: flex-end;
}

.control-group {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  flex: 1;
  min-width: 200px;
}
.control-group.wide {
  flex: 2;
  min-width: 300px;
}

label {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-muted);
}

input[type="text"], input[type="number"], select {
  background: var(--bg-primary);
  border: 1px solid var(--border);
  color: #fff;
  padding: 0.6rem 0.85rem;
  border-radius: 6px;
  font-family: inherit;
  font-size: 0.9rem;
  outline: none;
  transition: border 0.2s;
}
input[type="text"]:focus, input[type="number"]:focus, select:focus {
  border-color: var(--gold-primary);
}

.btn {
  background: var(--bg-tertiary);
  color: #fff;
  border: 1px solid var(--border);
  padding: 0.6rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.85rem;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;
}
.btn:hover { background: #475569; }
.btn-gold {
  background: rgba(245, 158, 11, 0.15);
  border-color: rgba(245, 158, 11, 0.4);
  color: var(--gold-primary);
}
.btn-gold:hover { background: rgba(245, 158, 11, 0.25); }

/* TABELA I KONTENER TABLE-WRAPPER */
.table-wrapper {
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow-x: auto;
  margin-bottom: 1rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
  text-align: left;
}

thead th {
  background: #182234;
  color: var(--text-muted);
  font-weight: 600;
  padding: 0.85rem 1rem;
  border-bottom: 1px solid var(--border);
  white-space: nowrap;
  cursor: pointer;
  user-select: none;
}
thead th:hover {
  color: #fff;
  background: #1e293b;
}

tbody tr {
  border-bottom: 1px solid rgba(51, 65, 85, 0.4);
  transition: background-color 0.15s ease;
  cursor: pointer;
}
tbody tr:hover {
  background: rgba(255, 255, 255, 0.04);
}

td {
  padding: 0.85rem 1rem;
  vertical-align: middle;
}

/* ODZNAKI I BADGE */
.badge-scan {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--gold-primary);
  background: rgba(245, 158, 11, 0.1);
  border: 1px solid rgba(245, 158, 11, 0.2);
  padding: 0.15rem 0.4rem;
  border-radius: 4px;
  display: inline-block;
  margin-right: 0.2rem;
}

.badge-district {
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.2rem 0.55rem;
  border-radius: 9999px;
  background: rgba(139, 92, 246, 0.15);
  color: #c084fc;
  border: 1px solid rgba(139, 92, 246, 0.3);
  display: inline-block;
}

.badge-role {
  font-size: 0.75rem;
  font-weight: 500;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  background: rgba(6, 182, 212, 0.15);
  color: #22d3ee;
  border: 1px solid rgba(6, 182, 212, 0.25);
}

.badge-widow {
  background: rgba(236, 72, 153, 0.15);
  color: #f472b6;
  border: 1px solid rgba(236, 72, 153, 0.3);
}

.badge-officer {
  background: rgba(245, 158, 11, 0.2);
  color: #fbbf24;
  border: 1px solid rgba(245, 158, 11, 0.4);
  font-weight: 700;
}

.badge-years {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  color: #e2e8f0;
  font-weight: 600;
}

/* PAGINACJA */
.pagination-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.85rem 1rem;
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 8px;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.pagination-info {
  font-size: 0.85rem;
  color: var(--text-muted);
}

.pagination-controls {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.page-btn {
  background: var(--bg-tertiary);
  border: 1px solid var(--border);
  color: #fff;
  padding: 0.35rem 0.75rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 600;
}
.page-btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.page-jump {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-left: 0.5rem;
}
.page-jump input {
  width: 55px;
  padding: 0.25rem 0.4rem;
  text-align: center;
  font-size: 0.85rem;
}

/* MODAL I OKNO SZCZEGÓŁÓW */
.modal {
  display: none;
  position: fixed;
  z-index: 100;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 12px;
  max-width: 800px;
  width: 90%;
  margin: 5vh auto;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
}

.modal-header {
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.modal-header h3 {
  font-family: 'Cinzel', serif;
  font-size: 1.3rem;
  color: #fff;
}

.modal-close {
  background: transparent;
  border: none;
  color: var(--text-muted);
  font-size: 1.5rem;
  cursor: pointer;
  line-height: 1;
}
.modal-close:hover { color: #fff; }

.modal-body {
  padding: 1.5rem;
  overflow-y: auto;
  font-size: 0.9rem;
}

.modal-section { margin-bottom: 1.25rem; }
.modal-section-title {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--gold-primary);
  margin-bottom: 0.4rem;
}

.modal-tabs-bar {
  display: flex;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem 0 1.5rem;
  border-bottom: 1px solid var(--border);
  background: rgba(15, 23, 42, 0.4);
  flex-wrap: wrap;
}
.modal-tab-btn {
  background: transparent;
  border: 1px solid transparent;
  border-bottom: none;
  color: var(--text-muted);
  padding: 0.55rem 1.1rem;
  font-size: 0.85rem;
  font-weight: 600;
  border-radius: 6px 6px 0 0;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  transition: all 0.2s ease;
}
.modal-tab-btn:hover {
  color: #fff;
  background: rgba(255, 255, 255, 0.04);
}
.modal-tab-btn.active {
  color: var(--gold-primary);
  background: var(--bg-secondary);
  border-color: var(--border);
  border-bottom: 2px solid var(--gold-primary);
  margin-bottom: -1px;
}

/* POLE TRANSKRYPCJI */
.transcription-box {
  background: #090e18;
  border: 1px solid rgba(212, 175, 55, 0.3);
  border-left: 3px solid var(--gold-primary);
  border-radius: 6px;
  padding: 1.25rem 1.5rem;
  font-family: 'Cinzel', serif, Georgia, serif;
  font-size: 0.95rem;
  line-height: 1.85;
  color: #e2e8f0;
  white-space: pre-wrap;
  word-break: break-word;
  box-shadow: inset 0 2px 8px rgba(0,0,0,0.4);
}
.btn-copy-trans {
  background: rgba(212, 175, 55, 0.1);
  border: 1px solid rgba(212, 175, 55, 0.3);
  color: var(--gold-primary);
  padding: 0.35rem 0.75rem;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.btn-copy-trans:hover {
  background: var(--gold-primary);
  color: #0f172a;
}

/* SZUKAJ W ARCHIWACH (SwA) */
.swa-card {
  background: #0a0f1d;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.25rem;
}
.swa-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  margin-bottom: 1rem;
}
.badge-source {
  background: rgba(34, 197, 94, 0.15);
  border: 1px solid rgba(34, 197, 94, 0.4);
  color: #4ade80;
  font-size: 0.75rem;
  padding: 0.25rem 0.6rem;
  border-radius: 4px;
  font-weight: 600;
}
.swa-meta-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 0.75rem;
  margin-bottom: 1.25rem;
  background: rgba(15, 23, 42, 0.6);
  padding: 0.85rem;
  border-radius: 6px;
  border: 1px solid rgba(255, 255, 255, 0.05);
}
.swa-meta-item {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}
.swa-meta-label {
  font-size: 0.7rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.swa-meta-val {
  font-size: 0.85rem;
  color: #f1f5f9;
  font-weight: 600;
}
.swa-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-bottom: 0.9rem;
}
.btn-swa-primary {
  background: linear-gradient(135deg, #d4af37, #b89628);
  color: #0f172a !important;
  font-weight: 700;
  padding: 0.65rem 1.25rem;
  border-radius: 6px;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9rem;
  box-shadow: 0 4px 12px rgba(212, 175, 55, 0.25);
  transition: all 0.2s ease;
}
.btn-swa-primary:hover {
  background: linear-gradient(135deg, #f6e05e, #d4af37);
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(212, 175, 55, 0.35);
}
.btn-swa-secondary {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border);
  color: #e2e8f0 !important;
  font-weight: 600;
  padding: 0.65rem 1.1rem;
  border-radius: 6px;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.85rem;
  transition: all 0.2s ease;
}
.btn-swa-secondary:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #fff !important;
  border-color: var(--gold-primary);
}
.swa-instruction-box {
  background: rgba(212, 175, 55, 0.08);
  border: 1px solid rgba(212, 175, 55, 0.25);
  border-left: 3px solid var(--gold-primary);
  border-radius: 6px;
  padding: 1rem 1.15rem;
  margin-top: 1rem;
}
.swa-hint {
  font-size: 0.78rem;
  color: var(--text-muted);
  line-height: 1.4;
}

/* TABELA WYSTĄPIEŃ W MODALU OSOBY */
.occs-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 0.5rem;
  font-size: 0.85rem;
}
.occs-table th, .occs-table td {
  padding: 0.5rem 0.75rem;
  border: 1px solid var(--border);
}
.occs-table th {
  background: #182234;
  color: var(--text-muted);
  font-weight: 600;
}

/* MONOGRAFIA I ODKRYCIA */
.monograph-content, .analytics-content {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 2.5rem;
  max-width: 1050px;
  margin: 0 auto;
  line-height: 1.85;
  font-size: 1.05rem;
  color: #e2e8f0;
}
.monograph-content h2, .analytics-content h2 {
  font-family: 'Cinzel', serif;
  color: var(--gold-primary);
  font-size: 1.65rem;
  margin-top: 2.2rem;
  margin-bottom: 1rem;
  border-bottom: 1px solid var(--border);
  padding-bottom: 0.6rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}
.monograph-content h3, .analytics-content h3 {
  font-family: 'Cinzel', serif;
  color: #fff;
  font-size: 1.25rem;
  margin-top: 1.6rem;
  margin-bottom: 0.8rem;
}
.monograph-content p, .analytics-content p { margin-bottom: 1.2rem; }
.monograph-content ul, .monograph-content ol, .analytics-content ul, .analytics-content ol {
  margin-bottom: 1.3rem;
  padding-left: 1.5rem;
}
.monograph-content li, .analytics-content li { margin-bottom: 0.6rem; }
.analytics-card {
  background: #0f172a;
  border: 1px solid var(--border);
  border-left: 4px solid var(--gold-primary);
  border-radius: 8px;
  padding: 1.4rem 1.6rem;
  margin-bottom: 1.6rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
}
.analytics-card h4 {
  font-family: 'Cinzel', serif;
  color: var(--gold-primary);
  font-size: 1.2rem;
  margin-top: 0;
  margin-bottom: 0.6rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.analytics-card p { margin-bottom: 0.8rem; color: #cbd5e1; }
.alert-box {
  background: #0f172a;
  border: 1px solid var(--border);
  border-left: 4px solid var(--gold-primary);
  border-radius: 8px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 1.5rem;
}
.alert-box.emerald { border-left-color: #10b981; }
.alert-box.gold { border-left-color: var(--gold-primary); }
.alert-box.purple { border-left-color: #a855f7; }
.alert-box.cyan { border-left-color: #06b6d4; }
.doc-ref-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  font-weight: 700;
  background: rgba(217, 119, 6, 0.2);
  color: var(--gold-primary);
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  border: 1px solid rgba(217, 119, 6, 0.3);
  display: inline-block;
  margin: 0 0.2rem;
}

@media (max-width: 768px) {
  h1 { font-size: 1.6rem; }
  .container { padding: 0.75rem; }
  .tabs-nav { padding: 0.5rem; }
  .tab-btn { font-size: 0.8rem; padding: 0.4rem 0.75rem; }
  .controls-panel { flex-direction: column; }
  .control-group { width: 100%; }
  .pagination-bar { flex-direction: column; align-items: stretch; }
}
```

### 4. Górny Pasek Metryk KPI
W sekcji `#main-tab` i `#genealogy-tab` umieszczana jest siatka 4 kart KPI z precyzyjnymi klasami akcentów:

```html
<div class="stats-grid">
  <div class="stat-card gold">
    <div class="stat-title">Liczba skanów jednostki</div>
    <div class="stat-value">{LICZBA_SKANOW}</div>
    <div class="stat-desc">Kompletna seria mikrofilmu AP Lublin</div>
  </div>
  <div class="stat-card purple">
    <div class="stat-title">Zakres chronologiczny</div>
    <div class="stat-value">{LATA}</div>
    <div class="stat-desc">Skrajne daty zachowanych protokołów</div>
  </div>
  <div class="stat-card cyan">
    <div class="stat-title">Kluczowe akta ustrojowe</div>
    <div class="stat-value">{LICZBA_AKTOW}</div>
    <div class="stat-desc">Elekcje, rozliczenia szafarzy, dekrety</div>
  </div>
  <div class="stat-card success">
    <div class="stat-title">Spisy podatkowe / Zapisy</div>
    <div class="stat-value">{LICZBA_SERII}</div>
    <div class="stat-desc">Imienne rejestry majątkowe mieszkańców</div>
  </div>
</div>
```

### 5. Pasek Zakładek Głównych (`<nav class="tabs-nav">`) i Przełączanie Zakładek
Dokładny kod paska zakładek i logika JavaScript:

```html
<nav class="tabs-nav">
  <button class="tab-btn active" onclick="switchTab('main-tab', this)">
    <span>📊 Tabela Indeksowa Skanów</span>
    <span class="tab-badge" id="mainTabBadge">252</span>
  </button>
  <button class="tab-btn gold-tab" onclick="switchTab('genealogy-tab', this)">
    <span>🌳 Słownik Genealogiczny Mieszkańców</span>
    <span class="tab-badge" id="genTabBadge">972</span>
  </button>
  <button class="tab-btn" onclick="switchTab('monograph-tab', this)">
    <span>🏛️ Pełna Synteza Monograficzna</span>
  </button>
  <button class="tab-btn" onclick="switchTab('analytics-tab', this)">
    <span>🔍 Kluczowe Odkrycia i Przełomy</span>
  </button>
</nav>
```

* **Funkcja JS `switchTab`**:
```javascript
function switchTab(tabId, btn) {
  document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  const target = document.getElementById(tabId);
  if (target) target.classList.add('active');
  if (btn) btn.classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
```

### 6. Tabela Rejestru Skanów – Rygor 7 Kolumn, Paginacja i Wyszukiwarka
Tabela główna rejestru skanów **musi zawierać dokładnie 7 kolumn** w ściśle określonej kolejności:
1. `Skan ↕` (szerokość 6%, numer skanu z prefiksem `#` np. `#1`, wywołujący `openMainModal(nr_skanu)`)
2. `Pagina ↕` (szerokość 8%, pagina/foliacja oryginalna)
3. `Rok ↕` (szerokość 8%, data roczna zapisu)
4. `Osoby i Podmioty` (szerokość 18%, lista osób; dla wpisów wieloosobowych fioletowy badge `.badge-district` z etykietą `(kliknij, aby rozwinąć)`)
5. `Kategoria ↕` (szerokość 14%, kategoria kancelaryjna)
6. `Opis Sprawy / Treść Aktu` (szerokość elastyczna, wyczerpujący regest)
7. `Kwoty / Podatki` (szerokość 14%, kwoty i taksy formatowane pionowo; jeśli brak: `-`)

* **HTML Panelu Kontrolek i Paginacji**:
```html
<div class="controls-panel">
  <div class="control-group wide">
    <label for="mainSearch">Wyszukaj w rejestrze skanów (osoby, kategoria, treść sprawy)</label>
    <input type="text" id="mainSearch" placeholder="np. elekcja, sympla, Piasek, Zarzecze, Fiszer, Tkaczyk, wójt..." oninput="filterMainData()">
  </div>
  <div class="control-group">
    <label for="mainCategoryFilter">Kategoria aktu</label>
    <select id="mainCategoryFilter" onchange="filterMainData()">
      <option value="">-- Wszystkie kategorie --</option>
    </select>
  </div>
  <button class="btn btn-gold" onclick="exportMainCSV()">📥 Pobierz Indeks CSV</button>
</div>

<div class="pagination-bar">
  <div class="pagination-info" id="mainPaginationInfo">Wyświetlanie...</div>
  <div class="pagination-controls">
    <button class="page-btn" id="mainPrevBtn" onclick="prevMainPage()">Poprzednia</button>
    <span id="mainPageIndicator" style="font-size:0.85rem; font-weight:600; padding:0 0.5rem;">1 / 10</span>
    <button class="page-btn" id="mainNextBtn" onclick="nextMainPage()">Następna</button>
    <div class="page-jump">
      <span>Skocz do:</span>
      <input type="number" id="mainJumpInput" min="1" max="1" value="1">
      <button class="page-btn" onclick="jumpMainPage()">Idź</button>
    </div>
  </div>
</div>

<div class="table-wrapper">
  <table>
    <thead>
      <tr>
        <th onclick="sortMain('nr_skanu')">Skan ↕</th>
        <th onclick="sortMain('strona_pagina')">Pagina ↕</th>
        <th onclick="sortMain('data_rok')">Rok ↕</th>
        <th>Osoby i Podmioty</th>
        <th onclick="sortMain('kategoria')">Kategoria ↕</th>
        <th>Opis Sprawy / Treść Aktu</th>
        <th>Kwoty / Podatki</th>
      </tr>
    </thead>
    <tbody id="mainTableBody"></tbody>
  </table>
</div>
```

* **Funkcja JS `renderMainTable()` (Kanon renderowania wiersza – bez badge'a `📜 Transkr.`)**:
```javascript
function renderMainTable() {
  const tbody = document.getElementById('mainTableBody');
  const totalPages = Math.ceil(filteredMain.length / mainPageSize) || 1;
  if (mainCurrentPage > totalPages) mainCurrentPage = totalPages;

  const start = (mainCurrentPage - 1) * mainPageSize;
  const end = start + mainPageSize;
  const pageData = filteredMain.slice(start, end);

  document.getElementById('mainPaginationInfo').innerText = 
    `Pokazywane ${filteredMain.length > 0 ? start + 1 : 0}–${Math.min(end, filteredMain.length)} z ${filteredMain.length} pozycji`;
  document.getElementById('mainPageIndicator').innerText = `${mainCurrentPage} / ${totalPages}`;
  document.getElementById('mainJumpInput').max = totalPages;
  document.getElementById('mainJumpInput').value = mainCurrentPage;
  document.getElementById('mainPrevBtn').disabled = (mainCurrentPage <= 1);
  document.getElementById('mainNextBtn').disabled = (mainCurrentPage >= totalPages);

  if (pageData.length === 0) {
    tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:2rem; color:var(--text-muted);">Brak wyników spełniających kryteria.</td></tr>';
    return;
  }

  let html = '';
  pageData.forEach(r => {
    let osobyDisplay = '';
    if (r.osoby_skrot && r.osoby_skrot !== r.osoby_podmioty) {
      osobyDisplay = `<span class="badge-district" style="font-size:0.8rem;">${escapeHtml(r.osoby_skrot)}</span> <span style="font-size:0.75rem; color:#94a3b8; display:block; margin-top:3px;">(kliknij, aby rozwinąć)</span>`;
    } else {
      osobyDisplay = escapeHtml(r.osoby_podmioty || '—');
    }

    html += `
      <tr onclick="openMainModal(${r.nr_skanu})">
        <td style="font-family:'JetBrains Mono', monospace; font-weight:700; color:var(--gold-primary);">#${r.nr_skanu}</td>
        <td style="font-family:'JetBrains Mono', monospace; font-size:0.8rem;">${escapeHtml(r.strona_pagina)}</td>
        <td><span class="badge-years">${escapeHtml(r.data_rok)}</span></td>
        <td>${osobyDisplay}</td>
        <td><span style="font-size:0.8rem; font-weight:600; color:#cbd5e1;">${escapeHtml(r.kategoria)}</span></td>
        <td style="color:#cbd5e1; font-size:0.85rem;">${escapeHtml(r.opis_pozycji)}</td>
        <td style="font-family:'JetBrains Mono', monospace; font-size:0.8rem; color:#e2e8f0;">${escapeHtml(r.kwoty_miary || '—')}</td>
      </tr>
    `;
  });
  tbody.innerHTML = html;
}
```

* **Funkcje pomocnicze paginacji i sortowania**:
```javascript
function prevMainPage() { if (mainCurrentPage > 1) { mainCurrentPage--; renderMainTable(); } }
function nextMainPage() { const totalPages = Math.ceil(filteredMain.length / mainPageSize); if (mainCurrentPage < totalPages) { mainCurrentPage++; renderMainTable(); } }
function jumpMainPage() {
  const val = parseInt(document.getElementById('mainJumpInput').value);
  const totalPages = Math.ceil(filteredMain.length / mainPageSize);
  if (val >= 1 && val <= totalPages) {
    mainCurrentPage = val;
    renderMainTable();
  }
}

function filterMainData() {
  const query = document.getElementById('mainSearch').value.toLowerCase().trim();
  const cat = document.getElementById('mainCategoryFilter').value;

  filteredMain = mainData.filter(d => {
    const matchCat = !cat || d.kategoria === cat;
    const matchQuery = !query || 
      d.nr_skanu.toString().includes(query) ||
      (d.strona_pagina && d.strona_pagina.toLowerCase().includes(query)) ||
      (d.data_rok && d.data_rok.toLowerCase().includes(query)) ||
      (d.kategoria && d.kategoria.toLowerCase().includes(query)) ||
      (d.opis_pozycji && d.opis_pozycji.toLowerCase().includes(query)) ||
      (d.osoby_podmioty && d.osoby_podmioty.toLowerCase().includes(query)) ||
      (d.kwoty_miary && d.kwoty_miary.toLowerCase().includes(query)) ||
      (d.transkrypcja && d.transkrypcja.toLowerCase().includes(query));
    return matchCat && matchQuery;
  });

  mainCurrentPage = 1;
  renderMainTable();
}

function sortMain(col) {
  if (mainSortCol === col) { mainSortAsc = !mainSortAsc; } else { mainSortCol = col; mainSortAsc = true; }
  filteredMain.sort((a, b) => {
    let valA = a[col];
    let valB = b[col];
    if (col === 'nr_skanu') { valA = parseInt(valA) || 0; valB = parseInt(valB) || 0; }
    else if (typeof valA === 'string') { valA = valA.toLowerCase(); valB = (valB || '').toLowerCase(); }
    if (valA < valB) return mainSortAsc ? -1 : 1;
    if (valA > valB) return mainSortAsc ? 1 : -1;
    return 0;
  });
  renderMainTable();
}
```

### 7. Trzyczęściowy Modal Skanu (Żelazny Standard Dokładnie 3 Zakładek)
Modal w kanonie J40 składa się z **dokładnie 3 kanonicznych zakładek** (kategoryczny zakaz dodawania lokalnych wycinków cyfrowych `crops` ze względu na prawa autorskie Archiwów Państwowych oraz ochronę przed limitami CDN):
1. **Zakładka 1: `📋 Opis i metadane` (`tabBtnMeta`) – DOMYŚLNA I ZAWSZE AKTYWNA PRZY OTWARCIU**:
   - Zawiera 4 bloki: Identyfikacja archiwalna, Regest i opis, Występujące osoby, Wymiary finansowe.
2. **Zakładka 2: `📜 Transkrypcja` (`tabBtnTrans`)**:
   - Pełny odczyt dyplomatyczny w kontenerze `.transcription-box` z działającym przyciskiem `📋 Kopiuj transkrypcję` (`.btn-copy-trans`).
3. **Zakładka 3: `🔗 Link do oryginału` (`tabBtnLink`)**:
   - Dwa kafle prowadzące do *Szukaj w Archiwach* (złoty kafel do jednostki, pomocniczy do zespołu) oraz boks instrukcji z numerem miniatury `#{item.nr_skanu}`.

* **Kanoniczny kod JS przełączania zakładek modalu i kopiowania transkrypcji**:
```javascript
function switchModalTab(tabKey) {
  const tabs = ['meta', 'trans', 'link'];
  tabs.forEach(t => {
    const btn = document.getElementById('tabBtn' + t.charAt(0).toUpperCase() + t.slice(1));
    const pane = document.getElementById('modalTabContent' + t.charAt(0).toUpperCase() + t.slice(1));
    if (btn) btn.classList.toggle('active', t === tabKey);
    if (pane) pane.style.display = (t === tabKey) ? 'block' : 'none';
  });
}

function copyTranscription() {
  if (!currentModalScan || !currentModalScan.transkrypcja) return;
  navigator.clipboard.writeText(currentModalScan.transkrypcja).then(() => {
    const btn = document.querySelector('.btn-copy-trans');
    if (btn) {
      const orig = btn.innerText;
      btn.innerText = '✅ Skopiowano do schowka!';
      setTimeout(() => { btn.innerText = orig; }, 2000);
    }
  }).catch(err => {
    console.error('Błąd kopiowania:', err);
  });
}
```

* **Kanoniczny kod JS `openMainModal(scanNr)` i `closeModal()`**:
```javascript
function openMainModal(scanNr) {
  const item = mainData.find(d => parseInt(d.nr_skanu) === scanNr);
  if (!item) return;

  currentModalScan = item;
  document.getElementById('modalTitle').innerText = `Skan #${item.nr_skanu} (${item.strona_pagina}) – Rok ${item.data_rok}`;
  
  const tabsBar = document.getElementById('modalTabsBar');
  if (tabsBar) tabsBar.style.display = 'flex';
  switchModalTab('meta');

  const transFormatted = item.transkrypcja ? escapeHtml(item.transkrypcja).replace(/\n/g, '<br>') : '<em style="color:#94a3b8;">Brak transkrypcji tekstowej dla tego skanu.</em>';

  document.getElementById('modalBody').innerHTML = `
    <div id="modalTabContentMeta" class="modal-tab-content">
      <div class="modal-section">
        <div class="modal-section-title">Identyfikacja archiwalna i kodykologiczna</div>
        <div><strong>Jednostka:</strong> AP Lublin, Akta miasta Kraśnika, sygn. {SYGNATURA}</div>
        <div><strong>Oznaczenie skanu:</strong> Skan #${item.nr_skanu} &nbsp;|&nbsp; <strong>Paginacja oryginalna:</strong> ${escapeHtml(item.strona_pagina)}</div>
        <div><strong>Datacja zapisu:</strong> <span class="badge-years">${escapeHtml(item.data_rok)}</span> &nbsp;|&nbsp; <strong>Kategoria:</strong> <span class="badge-role">${escapeHtml(item.kategoria)}</span></div>
      </div>

      <div class="modal-section">
        <div class="modal-section-title">Regest i opis historyczno-dyplomatyczny</div>
        <div style="font-size:0.95rem; line-height:1.6; color:#e2e8f0; background:#0f172a; padding:0.85rem; border-radius:6px; border:1px solid var(--border);">
          ${escapeHtml(item.opis_pozycji)}
        </div>
      </div>

      <div class="modal-section">
        <div class="modal-section-title">Występujące osoby, instytucje i urzędy</div>
        <div style="font-size:0.9rem; line-height:1.6; color:#cbd5e1;">
          ${escapeHtml(item.osoby_podmioty || '—')}
        </div>
      </div>

      <div class="modal-section">
        <div class="modal-section-title">Wymiary finansowe, taksy i jednostki monetarne</div>
        <div style="font-family:'JetBrains Mono', monospace; font-size:0.9rem; color:var(--gold-primary);">
          ${escapeHtml(item.kwoty_miary || 'Brak danych finansowych')}
        </div>
      </div>
    </div>

    <div id="modalTabContentTrans" class="modal-tab-content" style="display:none;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
        <span style="font-size:0.85rem; color:var(--text-muted);">Transkrypcja dyplomatyczna zgodna z Zasadami Wydawania Źródeł Historycznych PAN</span>
        <button class="btn-copy-trans" onclick="copyTranscription()">📋 Kopiuj transkrypcję</button>
      </div>
      <div class="transcription-box">
        ${transFormatted}
      </div>
    </div>

    <div id="modalTabContentLink" class="modal-tab-content" style="display:none;">
      <div class="modal-section">
        <div class="modal-section-title">Dostęp do skanu cyfrowego w zasobie Archiwum Państwowego</div>
        <p style="color:#cbd5e1; font-size:0.9rem; margin-bottom:1rem;">
          Oryginalny skan w pełnej rozdzielczości dostępny jest w państwowym portalu SzukajwArchiwach.gov.pl.
        </p>
        <div class="swa-card">
          <div class="swa-actions">
            <a href="${escapeHtml(item.link_swa || 'https://www.szukajwarchiwach.gov.pl')}" target="_blank" class="btn-swa-primary">
              🏛️ Otwórz jednostkę w Szukaj w Archiwach ↗
            </a>
            <a href="https://www.szukajwarchiwach.gov.pl/zespol/-/zespol/1890" target="_blank" class="btn-swa-secondary">
              📁 Zespół 35/40/0 (Akta m. Kraśnika) ↗
            </a>
          </div>
          <div class="swa-instruction-box">
            <strong>Instrukcja nawigacji do klatki:</strong>
            <p class="swa-hint">W portalu Szukaj w Archiwach przejdź do zakładki <strong>«Skany»</strong> i wybierz miniaturę oznaczoną numerem <strong>#${item.nr_skanu}</strong>.</p>
          </div>
        </div>
      </div>
    </div>
  `;

  document.getElementById('detailModal').style.display = 'block';
}

function closeModal() {
  document.getElementById('detailModal').style.display = 'none';
  currentModalScan = null;
}

window.onclick = function(event) {
  const modal = document.getElementById('detailModal');
  if (event.target == modal) {
    closeModal();
  }
}
```

### 8. Tabela Słownika Genealogicznego i Modal Osoby (`openGenModal`)
Tabela genealogiczna w kanonie J40 posiada **dokładnie 7 kanonicznych kolumn**:
1. `Lp. ↕` (szerokość 5%)
2. `Nazwisko ↕` (szerokość 18%, forma główna wytłuszczona, pod nią ewentualny przydomek vel oraz wariant)
3. `Imię ↕` (szerokość 15%)
4. `Miejsce zamieszkania ↕` (szerokość 18%, pigułka `.badge-district`)
5. `Funkcja społeczna ↕` (szerokość 16%, badge `.badge-role`, `.badge-widow`, `.badge-officer`)
6. `Roboczo: Nr skanów ↕` (szerokość 16%, pigułki `.badge-scan` z łączną liczbą wzmianek)
7. `Zakres lat ↕` (szerokość 12%, font monospace)

* **HTML Panelu Kontrolek i Tabeli Genealogicznej**:
```html
<div class="controls-panel">
  <div class="control-group wide">
    <label for="genSearch">Szukaj mieszkańca (nazwisko, imię, przedmieście, urząd, nr skanu)</label>
    <input type="text" id="genSearch" placeholder="np. Jajczyk, Wiatrek, Tkaczyk, Wolak, Zarzecze, Piaski, wójt, #41..." oninput="filterGenData()">
  </div>
  <div class="control-group">
    <label for="genDistrictFilter">Miejsce zamieszkania (Dzielnica)</label>
    <select id="genDistrictFilter" onchange="filterGenData()">
      <option value="">-- Wszystkie przedmieścia i dzielnice --</option>
      <option value="Śródmieście">Śródmieście (Miasto Kraśnik)</option>
      <option value="Piaski">Przedmieście Piaski</option>
      <option value="Zarzecze">Przedmieście Zarzecze</option>
      <option value="Góry i Podlesie">Przedmieście Góry i Podlesie</option>
      <option value="Kraśnik (ogólne)">Kraśnik (ogólne / władze miejskie)</option>
    </select>
  </div>
  <button class="btn btn-gold" onclick="exportGenCSV()">📥 Pobierz Słownik Genealogiczny (CSV)</button>
</div>

<div class="pagination-bar">
  <div class="pagination-info" id="genPaginationInfo">Wyświetlanie...</div>
  <div class="pagination-controls">
    <button class="page-btn" id="genPrevBtn" onclick="prevGenPage()">Poprzednia</button>
    <span id="genPageIndicator" style="font-size:0.85rem; font-weight:600; padding:0 0.5rem;">1 / 1</span>
    <button class="page-btn" id="genNextBtn" onclick="nextGenPage()">Następna</button>
    <div class="page-jump">
      <span>Skocz do:</span>
      <input type="number" id="genJumpInput" min="1" max="1" value="1">
      <button class="page-btn" onclick="jumpGenPage()">Idź</button>
    </div>
  </div>
</div>

<div class="table-wrapper">
  <table>
    <thead>
      <tr>
        <th onclick="sortGen('lp')" style="width: 5%;">Lp. ↕</th>
        <th onclick="sortGen('nazwisko')" style="width: 18%;">Nazwisko ↕</th>
        <th onclick="sortGen('imie')" style="width: 15%;">Imię ↕</th>
        <th onclick="sortGen('miejsce')" style="width: 18%;">Miejsce zamieszkania ↕</th>
        <th onclick="sortGen('funkcja')" style="width: 16%;">Funkcja społeczna ↕</th>
        <th onclick="sortGen('skany_list')" style="width: 16%;">Roboczo: Nr skanów ↕</th>
        <th onclick="sortGen('min_rok')" style="width: 12%;">Zakres lat ↕</th>
      </tr>
    </thead>
    <tbody id="genTableBody"></tbody>
  </table>
</div>
```

* **Funkcja JS `openGenModal(lp)` (Kanon modalu biograficznego)**:
```javascript
function openGenModal(lp) {
  currentModalScan = null;
  const tabsBar = document.getElementById('modalTabsBar');
  if (tabsBar) tabsBar.style.display = 'none'; // Kategoryczne ukrycie paska zakładek skanu!
  
  const p = genData.find(d => d.lp === lp);
  if (!p) return;

  const imieStr = p.imie || '';
  const funkcjaStr = p.funkcja || p.funkcja_zawod || '';
  const isWidow = imieStr.endsWith('owa') || imieStr === '[Wdowa]' || funkcjaStr.toLowerCase().includes('wdowa');
  const mentions = p.liczba_wystapien || (p.wystapienia ? p.wystapienia.length : (p.skany_list ? p.skany_list.length : 1));
  
  let occsHtml = '';
  if (p.wystapienia && p.wystapienia.length > 0) {
    occsHtml = `
      <table class="occs-table">
        <thead>
          <tr>
            <th style="width:12%;">Skan</th>
            <th style="width:14%;">Rok</th>
            <th style="width:34%;">Zapis w rękopisie</th>
            <th style="width:40%;">Podatek / Rola / Kontekst</th>
          </tr>
        </thead>
        <tbody>
          ${p.wystapienia.map(o => `
            <tr>
              <td style="font-family:'JetBrains Mono', monospace; font-weight:700; color:var(--gold-primary); cursor:pointer;" onclick="openMainModal(${o.skan})">#${o.skan}</td>
              <td style="font-family:'JetBrains Mono', monospace;">${escapeHtml(o.rok)}</td>
              <td style="font-style:italic;"><strong>${escapeHtml(o.zapis_oryginalny)}</strong></td>
              <td>${escapeHtml(o.kwota_ctx || o.rola || '—')}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;
  } else {
    occsHtml = '<div style="color:var(--text-muted); padding:0.5rem;">Brak szczegółowego wykazu wzmianek.</div>';
  }

  document.getElementById('modalTitle').innerText = `${imieStr} ${p.nazwisko} (${p.miejsce || 'Kraśnik'})`;
  document.getElementById('modalBody').innerHTML = `
    <div class="modal-section">
      <div class="modal-section-title">Dane biograficzne i status społeczno-prawny</div>
      <div style="font-size:1.05rem; margin-bottom:0.5rem;">
        <strong>${escapeHtml(imieStr)} ${escapeHtml(p.nazwisko)}</strong>
        &nbsp;•&nbsp; <span class="badge-district">${escapeHtml(p.miejsce || 'Kraśnik')}</span>
        &nbsp;•&nbsp; <span class="badge-role ${isWidow ? 'badge-widow' : ''}">${escapeHtml(funkcjaStr)}</span>
      </div>
      <div style="font-size:0.88rem; color:var(--text-muted);">
        Zakres poświadczeń w księdze: <strong>${escapeHtml(p.zakres_lat || '—')}</strong> &nbsp;|&nbsp; Łączna liczba wzmianek źródłowych: <strong>${mentions}</strong>
      </div>
      ${p.wariant_nazwiska ? `
        <div style="background:#1e293b; border-left:3px solid var(--gold-primary); padding:0.6rem 0.85rem; border-radius:4px; margin-top:0.75rem; font-size:0.88rem; color:#e2e8f0;">
          <strong style="color:var(--gold-primary);">💡 Lekcje i warianty zapisu w rękopisie:</strong> ${escapeHtml(p.wariant_nazwiska)}
          <div style="font-size:0.78rem; color:#94a3b8; margin-top:3px;">Wpisanie dowolnej z tych form w wyszukiwarce natychmiast filtruje ten profil (zasada 1 osoba = 1 rekord).</div>
        </div>
      ` : ''}
    </div>

    ${p.notatka_biograficzna ? `
      <div class="modal-section">
        <div class="modal-section-title">Notatka biograficzna i rola historyczna</div>
        <div style="background:#0f172a; padding:0.85rem; border-radius:6px; border:1px solid var(--border); color:#cbd5e1; font-size:0.9rem; line-height:1.6;">
          ${escapeHtml(p.notatka_biograficzna)}
        </div>
      </div>
    ` : ''}

    <div class="modal-section">
      <div class="modal-section-title">Skany źródłowe</div>
      <div style="line-height:2;">
        ${(p.skany_list || []).map(s => `<span class="badge-scan" style="font-size:0.85rem; padding:0.25rem 0.55rem; margin-right:4px; cursor:pointer;" onclick="openMainModal(${s})">Skan #${s}</span>`).join(' ')}
      </div>
    </div>

    <div class="modal-section">
      <div class="modal-section-title">Wykaz wszystkich poświadczeń źródłowych</div>
      ${occsHtml}
    </div>

    <div class="modal-section">
      <div class="modal-section-title">Uwagi genealogiczne i powiązania rodzinne</div>
      <div style="background:#0f172a; padding:0.75rem; border-radius:6px; border:1px solid var(--border); color:#cbd5e1; font-size:0.88rem;">
        ${escapeHtml(p.uwagi || 'Mieszkaniec odnotowany w spisach podatkowych i rejestrach samorządu miasta Kraśnika.')}
      </div>
    </div>
  `;
  document.getElementById('detailModal').style.display = 'block';
}
```

* **Eksporty CSV i funkcja `downloadBlob`**:
```javascript
function downloadBlob(content, filename, contentType) {
  const blob = new Blob([content], { type: contentType });
  const url = URL.createObjectURL(blob);
  const pom = document.createElement('a');
  pom.href = url;
  pom.setAttribute('download', filename);
  pom.click();
  URL.revokeObjectURL(url);
}

function exportMainCSV() {
  const headers = ['Nr skanu', 'Paginacja', 'Datacja', 'Kategoria', 'Opis / Regest', 'Osoby / Podmioty', 'Kwoty / Miary'];
  let csv = "\ufeff" + headers.join(';') + "\r\n";
  filteredMain.forEach(r => {
    const row = [r.nr_skanu, r.strona_pagina, r.data_rok, r.kategoria, r.opis_pozycji, r.osoby_podmioty, r.kwoty_miary]
      .map(val => `"${String(val || '').replace(/"/g, '""')}"`)
      .join(';');
    csv += row + "\r\n";
  });
  downloadBlob(csv, '{NAZWA_JEDNOSTKI}_indeks_skanow.csv', 'text/csv;charset=utf-8;');
}

function exportGenCSV() {
  const headers = ['Lp.', 'Nazwisko', 'Imię', 'Miejsce zamieszkania', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'];
  let csv = "\ufeff" + headers.join(';') + "\r\n";
  filteredGen.forEach(p => {
    const row = [
      p.lp,
      p.nazwisko,
      p.imie,
      p.miejsce,
      p.funkcja || p.funkcja_zawod || '',
      p.skany_roboczo || (p.skany_list ? p.skany_list.map(s => '#' + s).join(', ') : ''),
      p.zakres_lat,
      p.liczba_wystapien || 1,
      p.wariant_nazwiska || ''
    ].map(val => `"${String(val || '').replace(/"/g, '""')}"`).join(';');
    csv += row + "\r\n";
  });
  downloadBlob(csv, '{NAZWA_JEDNOSTKI}_slownik_genealogiczny.csv', 'text/csv;charset=utf-8;');
}
```

### 9. Dynamiczna Inicjalizacja i Liczniki na Żywo (Zero Hardcodowania)
Pod koniec sekcji `<script>` każdego kompendium umieszczany jest blok inicjalizujący, który dynamicznie wylicza wartości liczników bez jakichkolwiek statycznych liczb:

```javascript
// DYNAMIC COUNTERS & INITIAL RENDER
if (document.getElementById('genTabBadge')) document.getElementById('genTabBadge').innerText = genData.length;
if (document.getElementById('genStatCount')) document.getElementById('genStatCount').innerText = genData.length;
let totalMentionsCalc = genData.reduce((acc, p) => acc + (p.liczba_wystapien || (p.wystapienia ? p.wystapienia.length : (p.skany_list ? p.skany_list.length : 1))), 0);
if (document.getElementById('genMentionsCount')) document.getElementById('genMentionsCount').innerText = totalMentionsCalc;

renderMainTable();
renderGenTable();
```

### 10. Żelazna Tablica Reguł DO / NIE RÓB (Kanon Sprawdzeniowy)

| Obszar | ✅ ZAWSZE STOSUJ (Standard J40) | ❌ KATEGORYCZNIE ZABRONIONE |
|---|---|---|
| **Kontener główny** | `<main class="container">` (max-width: 1500px, margin auto) | `<main class="main-container">`, nieostylowany `<main>` |
| **Kontener tabel** | `<div class="table-wrapper">` | `<div class="table-container">` |
| **Pasek zakładek** | `<nav class="tabs-nav">` z klasami `.tab-btn` | `<nav class="nav-tabs">`, `.nav-tab` |
| **Liczba zakładek strony** | Dokładnie 4 zakładki (`main-tab`, `genealogy-tab`, `monograph-tab`, `analytics-tab`) | Pomijanie zakładek, tworzenie 2 lub 3 zakładek |
| **Kolumny tabeli głównej** | Dokładnie 7 kolumn: `Skan ↕`, `Pagina ↕`, `Rok ↕`, `Osoby i Podmioty`, `Kategoria ↕`, `Opis Sprawy / Treść Aktu`, `Kwoty / Podatki` | 6 kolumn, brak kwot, zamiana nazw nagłówków |
| **Pierwsza kolumna** | Czysty numer `#${r.nr_skanu}` w kolorze złotym font monospace | Doklejanie odznak `📜 Transkr.`, badge'ów |
| **Zakładki modalu** | Dokładnie 3 zakładki: `tabBtnMeta`, `tabBtnTrans`, `tabBtnLink` | Dodawanie 4. zakładki `crops`, dodawanie wycinków |
| **Wycinki cyfrowe** | ZAKAZ lokalnych wycinków. Wyłącznie oficjalne linki do portalu SwA | Tworzenie folderów crops, linki do lokalnych .png/.jpg |
| **Ciemny motyw (Dark Slate)** | `--bg-primary: #0f172a`, tło ciemne, obramowania `#334155` | Jasny motyw, białe tło `#ffffff`, systemowe szarości |
| **Fonty Google Fonts** | Import `Cinzel` + `Inter` + `JetBrains Mono` | Brak importu, brak fontu Cinzel w nagłówkach |
| **Przycisk powrotu** | `.portal-back-link` prowadzący do `index.html` | Brak linku powrotu do portalu głównego |
| **Kodowanie CSV** | `UTF-8-SIG` (BOM `\ufeff`), separator średnik (`;`) | `UTF-8` bez BOM (krzaczy polskie znaki w Excelu) |
| **Kolumny tabeli genealogicznej** | Dokładnie 7 kolumn: `Lp. ↕`, `Nazwisko ↕`, `Imię ↕`, `Miejsce zamieszkania ↕`, `Funkcja społeczna ↕`, `Roboczo: Nr skanów ↕`, `Zakres lat ↕` | Łączenie nazwiska i imienia w 1 kolumnę, redukcja do 6 kolumn |
| **Modal osoby** | `tabsBar.style.display = 'none'` (ukrycie paska skanu) | Pozostawienie widocznego paska zakładek skanu w modalu osoby |

--------------------------------------------------------------------------------

## V. Bezwzględny Pakiet 12 Automatycznych Testów Weryfikacyjnych (Kryteria Odbioru Kanonu J40)

Każda jednostka lub partia przed oddaniem użytkownikowi **musi** przejść zautomatyzowany skrypt testowy weryfikujący zgodność z kanonem J40. Jakikolwiek błąd (FAIL) blokuje zakończenie zadania.

### Test 1: Architektura DOM i Rygor 7 Kolumn Tabeli Głównej
- Sprawdzenie nagłówków `<th>` w tabeli głównej rejestru skanów:
  - Dokładnie 7 elementów `<th>`.
  - Dokładne nazwy i kolejność:
    1. `Skan ↕` (lub `Skan`)
    2. `Pagina ↕` (lub `Pagina`)
    3. `Rok ↕` (lub `Rok`)
    4. `Osoby i Podmioty`
    5. `Kategoria ↕` (lub `Kategoria`)
    6. `Opis Sprawy / Treść Aktu`
    7. `Kwoty / Podatki`
  - Weryfikacja obecności fioletowych pigułek `.badge-district` dla wpisów wieloosobowych.
  - Asercja obecności `<main class="container">` (zgodnie z kanonem J40; zakaz `main-container`).
  - Asercja obecności `<div class="table-wrapper">` (zakaz `table-container`).
  - Asercja braku odznaki `📜 Transkr.` w pierwszej kolumnie tabeli.

### Test 2: Symulacja Kliknięcia i Otwierania Modalu Skanu (`openMainModal`)
- Symulacja wywołania `openMainModal(nr_skanu)` w środowisku jsdom / Node.js VM:
  - Asercja: `#detailModal.style.display === 'block'` (modal staje się fizycznie widoczny).
  - Asercja: pasek zakładek `#modalTabsBar.style.display === 'flex'`.
  - Asercja: domyślnie aktywna jest zakładka `meta` (`tabBtnMeta.classList.contains('active')` oraz `#modalTabContentMeta.style.display === 'block'`).
  - Asercja: obecność dokładnie 3 kanonicznych zakładek (`tabBtnMeta`, `tabBtnTrans`, `tabBtnLink`) w DOM.
  - Asercja: 0 odwołań do wycinków cyfrowych (`crops`) oraz 0 lokalnych tagów `<img>` skanów w kodzie HTML.
  - Asercja: wywołanie `closeModal()` skutkuje `#detailModal.style.display === 'none'`.

### Test 3: Działanie Modalu Genealogicznego (`openGenModal`)
- Symulacja wywołania `openGenModal(lp)`:
  - Asercja: pasek zakładek skanu `#modalTabsBar.style.display === 'none'`.
  - Asercja: `#detailModal.style.display === 'block'`.
  - Asercja: obecność sekcji biograficznej, badge'a wariantów oraz tabeli wystąpień (`.occs-table`).
  - Asercja: kliknięcie w numer skanu w tabeli wystąpień przełącza na `openMainModal(nr_skanu)` i przywraca pasek zakładek.

### Test 4: Integralność Wariantu 2 i 100% Synchronizacji Onomastycznej
- Asercja: 0 duplikatów w unikalnym kluczu tożsamości `(nazwisko, imie, miejsce)` w całej tablicy `genData`.
- Asercja: 100% wariantów z nawiasów `[...]` w transkrypcjach danej partii znajduje się w tablicy `tokens_to_test` i zwraca trafienie w wyszukiwarce bazy `genData`.

### Test 5: Kanoniczny Format Słownika CSV
- Weryfikacja wygenerowanego pliku CSV (`krasnik_jXX_slownik_genealogiczny.csv`):
  - Kodowanie: `UTF-8-SIG` (obecność BOM `\ufeff`).
  - Separator kolumn: średnik (`;`).
  - Dokładnie 9 kanonicznych kolumn w nagłówku:
    `"Lp";"Nazwisko";"Imię";"Miejsce";"Funkcja społeczna / zawód";"Skany źródłowe";"Zakres lat";"Liczba wzmianek";"Warianty nazwiska"`

### Test 6: Spójność Monografii i Kart Analitycznych
- Weryfikacja syntezy monograficznej i sekcji odkryć:
  - Minimum 4 nowe Karty Analityczne na każdą partię 30 skanów.
  - Obecność dedykowanego Aneksu Badawczego dla zrealizowanej partii.
  - Dynamiczna synchronizacja liczników w UI (liczba osób w badge'u nawigacji i KPI odpowiada `genData.length`).

### Test 7: Składnia i Wykonanie w Node.js VM
- Pełna walidacja kodu JavaScript zawartego w pliku HTML za pomocą `vm.createScript` w Node.js:
  - Zero błędów składni (SyntaxError).
  - Prawidłowe załadowanie tablic `mainData` oraz `genData`.

### Test 8: Import Fontów Google Fonts (Cinzel, Inter, JetBrains Mono)
- Weryfikacja w tagu `<head>` obecności odnośników Google Fonts:
  - Obecność `family=Cinzel`, `family=Inter` oraz `family=JetBrains+Mono`.

### Test 9: Kanoniczne Zmienne CSS :root (Dark Slate Theme)
- Weryfikacja obecności kanonicznych zmiennych w bloku `:root`:
  - `--bg-primary: #0f172a`, `--bg-secondary: #1e293b`, `--gold-primary: #f59e0b`, `--purple-accent: #8b5cf6`, `--card-bg: rgba(30, 41, 59, 0.85)`.

### Test 10: Obecność Przycisku Powrotu do Portalu
- Weryfikacja obecności linku z klasą `.portal-back-link` prowadzącego do `index.html`.

### Test 11: Rygor Paska Zakładek Głównych (Dokładnie 4 Zakładki)
- Weryfikacja kontenera `<nav class="tabs-nav">`:
  - Dokładnie 4 przyciski z klasą `tab-btn`.
  - Powiązania z sekcjami: `main-tab`, `genealogy-tab`, `monograph-tab`, `analytics-tab`.

### Test 12: Kanoniczne 7 Kolumn Tabeli Słownika Genealogicznego
- Weryfikacja nagłówków `<th>` w sekcji `#genealogy-tab`:
  - Dokładnie 7 kolumn: `Lp. ↕`, `Nazwisko ↕`, `Imię ↕`, `Miejsce zamieszkania ↕`, `Funkcja społeczna ↕`, `Roboczo: Nr skanów ↕`, `Zakres lat ↕`.

--------------------------------------------------------------------------------

## VI. Procedura Pracy Agenta „Zasada Przed i Po” (Zero Improwizacji)

Aby wyeliminować błędy wykonawcze i regresje w kodzie, agent stosuje żelazną procedurę:

1. **Przed zadaniem (Obowiązkowa Lektura)**:
   - Przed przystąpieniem do jakiejkolwiek edycji kodu lub transkrypcji agent ma bezwzględny obowiązek przeczytać pliki `SKILL.md` oraz `agent.md`.
   - Zakaz polegania na zawodnej pamięci kontekstu – agent odświeża reguły przy każdym etapie.

2. **W trakcie zadania (Kopiowanie z Wzorca J40 zamiast Pisania z Pamięci)**:
   - Kategoryczny zakaz pisania struktur HTML i funkcji modali z pamięci.
   - Kod struktury tabeli, logika zakładek modalu i obsługa zdarzeń mają być kopiowane 1:1 z pliku referencyjnego `krasnik_j40_kompendium_calosc.html`.

3. **Po zadaniu (Obowiązkowa Automatyczna Weryfikacja Testami)**:
   - Przed zakomunikowaniem ukończenia partii lub zgłoszeniem gotowości do odbioru agent ma obowiązek uruchomić automatyczny skrypt testowy weryfikujący wszystkie 12 testów z Sekcji V.
   - Jakikolwiek błąd, brakująca kolumna, niedziałający modal lub brakujący wariant onomastyczny skutkuje natychmiastowym wstrzymaniem i naprawą kodu. Agent nigdy nie przekazuje do odbioru kodu, który nie przeszedł 100% testów.
