---
name: paleografia-krasnik
description: >-
  Kompleksowy przewodnik i metodyka paleografii staropolskiej XVIII w.,
  transkrypcji dyplomatycznej akt miejskich (Akta Miasta Kraśnika) oraz
  budowy baz genealogiczno-indeksowych i kompendiów cyfrowych.
---

# Metodyka Paleografii, Transkrypcji Dyplomatycznej i Indeksowania Genealogicznego (Akta Miasta Kraśnika)

Niniejszy dokument stanowi oficjalny kanon metodyczny pracy z osiemnastowiecznymi rękopisami miejskimi (w szczególności zespołem Akta Miasta Kraśnika z Archiwum Państwowego w Lublinie, sygn. 35/40/0/1/40 i pokrewne). Łączy on zasady rygorystycznej edycji źródeł historycznych, wytyczne genealogiczne kuzyna oraz wymogi techniczno-interfejsowe użytkownika.

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

--------------------------------------------------------------------------------

## III. Wymogi Techniczne i Interfejsowe (Wytyczne Użytkownika)

1. **Struktura Trzyczęściowa Modalu Skanu w HTML**:
   * **Zakładka 1: Opis i metadane** (data, pagina, kategoria, osoby/podmioty, kwoty, uwagi).
   * **Zakładka 2: Transkrypcja źródłowa** (pełna, rygorystyczna transkrypcja dyplomatyczna z zachowaniem kolumn).
   * **Zakładka 3: Link do oryginału** (oficjalne odnośniki do portalu Szukaj w Archiwach dla danej jednostki i obiektu cyfrowego).
2. **Czytelność Prezentacji Finansowej**:
   * Kwoty w tabelach ułożone pionowo jedna pod drugą, bez nadmiaru poziomych przecinków.
   * Redukcja zbędnych skrótów utrudniających lekturę.
3. **Paginacja i Wyszukiwanie**:
   * Rejestry skanów muszą umożliwiać bezpośrednie przejście do konkretnego numeru strony/skanu, a nie tylko nawigację Poprzednia/Następna.
   * Domyślne sortowanie alfabetyczne nazwisk z możliwością sortowania po innych kolumnach.
4. **Zasady Pracy w Parze z Użytkownikiem**:
   * Najpierw rzetelna analiza problemu, wyjaśnienie wątpliwości i przedstawienie opcji z bilansem zysków i strat.
   * **Ścisła bramka akceptacji**: Żadnego kodowania ani wprowadzania zmian w plikach bez wyraźnej zgody użytkownika w czacie.
   * Po zatwierdzeniu planu etapowego: w pełni autonomiczna realizacja partiami aż do sfinalizowania zadania.
