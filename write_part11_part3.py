import json

part3_trans = {
    "194": {
        "tytul": "Rekapitulacja Rejestru Sympli 1780 r. (Suma 81 zł 24 gr), bilans kasy miejskiej oraz Wolna Elekcja Magistratu z 16 Maja 1781 r.",
        "data_rok": "1781-05-16",
        "kategoria": "Rejestr sympli i Elekcja urzędowa / Podsumowanie i wybór magistratu",
        "osoby_podmioty": "Wojciech Rępa, Krzysztof Ćwiek, Paweł Wawrecki, Walenty Biegaj, Sebastian Dzyba, Reina Ćwielinowa, Mikołaj Dzyba, Marcin Rępa, Błażej Chruściel, Stanisław Bilartowicz, Katarzyna Rachoniowa (wdowa), Franciszek Rodzyn, Sebastian Szubartowski (wójt), Franciszek Barankiewicz (burmistrz), Jakub Gąska (burmistrz), Maciej Rycerz (burmistrz), Krzysztof Suliczyński (burmistrz), Franciszek Frankiewicz (exaktor), Józef Paszkiewicz (deputat trybunalski), Andrzej Wyszyński (sędzia)",
        "opis_pozycji": "Dokończenie Przedmieścia Góry i Podlesie (13 pozycji, 7mu Latus: 3 zł 17 gr). Compendium Latusów: Latus 1 (9 zł 3 gr), Latus 2 (8 zł 0 gr), Latus 3 (12 zł 25 gr), Latus 4 (18 zł 0 gr), Latus 5 (13 zł 21 gr), Latus 6 (16 zł 15 gr), Latus 7 (3 zł 17 gr) – Suma Generalna Sympli: 81 zł 24 gr. Rozliczenie kasy od 26 XI 1780 do 16 V 1781: Percepta 5172 zł 15 gr, Expensa 5209 zł 26 gr, nadpłata exaktora 37 zł 3 1/2 gr. Wolna Elekcja Magistratu: wójt Sebastian Szubartowski, czterej burmistrzowie, exaktor Franciszek Frankiewicz i deputat na Trybunał Józef Paszkiewicz.",
        "kwoty_miary": "7mu Latus: 3 zł 17 gr; Summa Sympli: 81 zł 24 gr. Bilans: Percepta 5172 zł 15 gr; Expensa 5209 zł 26 gr; Nadpłata do zwrotu: 37 zł 3 1/2 gr.",
        "uwagi": "Kluczowa strona podsumowująca podatki miejskie Kraśnika i odnotowująca legalny wybór władz miejskich pod powagą sędziego Andrzeja Wyszyńskiego.",
        "transkrypcja": """[PAGINA 94]
[Rekapitulacja Rejestru Sympli 1780 r., Bilans Rachunków 1780–1781 oraz Wolna Elekcja Magistratu z 16 Maja 1781 r.]

### Continuatio Góry y Podlesie:

| Nr | Posesjonat / Przedmieszczanin | Złote | Grosze | Kategoria / Uwagi |
| :---: | :--- | :---: | :---: | :--- |
| 220 | Woyciech Rępa | — | 5 | Przedmieszczanin |
| 221 | Krzystof Ćwiek | — | 10 | Przedmieszczanin |
| 222 | Paweł Wawrecki | — | 7 | Przedmieszczanin |
| 223 | Walenty Biegay | — | 7 | Przedmieszczanin |
| 224 | Sebestyan Dzyba | — | 16 | Przedmieszczanin |
| 225 | Reina Cwielinowa | — | 24 | Przedmieszczanka |
| 226 | Mikołay Dzyba | — | 14 | Przedmieszczanin |
| 227 | Marcin Rępa | — | 5 | Przedmieszczanin |
| 228 | Błażey Chruściel | — | 10 | Przedmieszczanin |
| 229 | Stanisław Bilartowicz | — | 14 | Przedmieszczanin |
| 230 | Katarzyna Rachoniowa Wdowa | — | 5 | Wdowa |
| 231 | Franciszek Rodzyn | — | 5 | Przedmieszczanin |
| 232 | Szereg Wdów (zbiorczo) | — | 2 | Ubogie wdowy |
| — | **7MU LATUS** | **3** | **17** | **Suma Gór i Podlesia (Dokończenie)** |

---

### Compendium Latusów (Rekapitulacja Rejestru Sympli):

| Latus | Dzielnica / Przedmieście | Złote | Grosze |
| :---: | :--- | :---: | :---: |
| **Latus 1** | Miasto (Rynek i Centrum) | 9 | 3 |
| **Latus 2** | Ulica Lubelska | 8 | — |
| **Latus 3** | Przedmieście Piasek (Część 1) | 12 | 25 |
| **Latus 4** | Przedmieście Piasek (Część 2) i Zarzyce (Początek) | 18 | — |
| **Latus 5** | Przedmieście Zarzyce (Dokończenie) | 13 | 21 |
| **Latus 6** | Przedmieście Góry i Podlesie (Część 1) | 16 | 15 |
| **Latus 7** | Przedmieście Góry i Podlesie (Dokończenie) | 3 | 17 |
| **SUMMA SYMPLI** | **Suma Generalna Sympli Miejskiej Kraśnika** | **81** | **24** |

*Dicitur per expressum: Złł Pols: Ośmdziesiąt Jeden Groszy Dwadzieścia Cztery.*

---

### Rozliczenie Rachunków Kasy Miejskiej (26 XI 1780 – 16 V 1781):

| Pozycja bilansu | Wyszczególnienie kwoty | Złote | Grosze |
| :--- | :--- | :---: | :---: |
| **Percepta Kasy** | Przychód całkowity udowodniony | 5172 | 15 |
| **Expensa Kasy** | Rozchód całkowity udowodniony | 5209 | 26 |
| **SALDO / NADPŁATA** | **Kwota naddana przez Exaktora do zwrotu z proweniencji** | **37** | **3 1/2** |

---

### Elekcya Urzędu na Rok teraznieyszy 1781szy (16 Maja 1781 r.):

*Woytem Obrany iest Sławetny Sebestyan Szubartowski.*

**Burmistrzami obrano czterech mężów:**
1. Sł[awetny] **Franciszek Barankiewicz**
2. Sł[awetny] **Jakub Gąska**
3. Sł[awetny] **Maciey Rycerz**
4. Sł[awetny] **Krzysztof Suliczyński**

- **Exaktorem mieyskim:** Sł[awetny] **Franciszek Frankiewicz**
- **Deputatem na Trybunał Koronny:** Sł[awetny] **Józef Paszkiewicz**"""
    },
    "195": {
        "tytul": "Rekapitulacja Rejestru Sympli 1780 r. oraz Wolna Elekcja Magistratu (Dublet Archiwalny Pag. 94)",
        "data_rok": "1781-05-16",
        "kategoria": "Dublet archiwalny / Rejestr sympli i Elekcja urzędowa",
        "osoby_podmioty": "Wojciech Rępa, Krzysztof Ćwiek, Paweł Wawrecki, Walenty Biegaj, Sebastian Dzyba, Reina Ćwielinowa, Mikołaj Dzyba, Marcin Rępa, Błażej Chruściel, Stanisław Bilartowicz, Katarzyna Rachoniowa (wdowa), Franciszek Rodzyn, Sebastian Szubartowski (wójt), Franciszek Barankiewicz (burmistrz), Jakub Gąska (burmistrz), Maciej Rycerz (burmistrz), Krzysztof Suliczyński (burmistrz), Franciszek Frankiewicz (exaktor), Józef Paszkiewicz (deputat)",
        "opis_pozycji": "Dublet fotograficzny mikrofilmu karty Pagina 94 (tożsamy ze skanem 194). Zawiera dokończenie 7 Latusa sympli, rekapitulację 7 latusów (Suma: 81 zł 24 gr), bilans rachunków (Percepta 5172 zł 15 gr, Expensa 5209 zł 26 gr, nadpłata 37 zł 3 1/2 gr) oraz akt wyboru wójta Szubartowskiego, 4 burmistrzów, exaktora Frankiewicza i deputata Paszkiewicza.",
        "kwoty_miary": "Suma Sympli: 81 zł 24 gr; Nadpłata exaktorska: 37 zł 3 1/2 gr.",
        "uwagi": "Skan 195 stanowi drugie ujęcie fotograficzne (dublet archiwalny mikrofilmu WAP Lublin) karty Pagina 94. Zgodnie z zasadami krytyki tekstu transkrypcja odzwierciedla w pełni treść rękopisu.",
        "transkrypcja": """[PAGINA 94 – DUBLET ARCHIWALNY FOTO]
[Rekapitulacja Rejestru Sympli 1780 r., Bilans Rachunków 1780–1781 oraz Wolna Elekcja Magistratu z 16 Maja 1781 r.]

> [!NOTE]
> **Aparat archiwalno-paleograficzny:** Skan 195 stanowi drugie, alternatywne ujęcie fotograficzne (dublet klatki mikrofilmu WAP Lublin) karty Pagina 94, tożsamej treściowo ze skanem 194.

### Continuatio Góry y Podlesie:

| Nr | Posesjonat / Przedmieszczanin | Złote | Grosze | Kategoria / Uwagi |
| :---: | :--- | :---: | :---: | :--- |
| 220 | Woyciech Rępa | — | 5 | Przedmieszczanin |
| 221 | Krzystof Ćwiek | — | 10 | Przedmieszczanin |
| 222 | Paweł Wawrecki | — | 7 | Przedmieszczanin |
| 223 | Walenty Biegay | — | 7 | Przedmieszczanin |
| 224 | Sebestyan Dzyba | — | 16 | Przedmieszczanin |
| 225 | Reina Cwielinowa | — | 24 | Przedmieszczanka |
| 226 | Mikołay Dzyba | — | 14 | Przedmieszczanin |
| 227 | Marcin Rępa | — | 5 | Przedmieszczanin |
| 228 | Błażey Chruściel | — | 10 | Przedmieszczanin |
| 229 | Stanisław Bilartowicz | — | 14 | Przedmieszczanin |
| 230 | Katarzyna Rachoniowa Wdowa | — | 5 | Wdowa |
| 231 | Franciszek Rodzyn | — | 5 | Przedmieszczanin |
| 232 | Szereg Wdów | — | 2 | Ubogie wdowy |
| — | **7MU LATUS** | **3** | **17** | **Suma Gór i Podlesia (Dokończenie)** |

---

### Compendium Latusów:

| Latus | Obszar podatkowy | Złote | Grosze |
| :---: | :--- | :---: | :---: |
| **Latus 1** | Miasto (Rynek i Centrum) | 9 | 3 |
| **Latus 2** | Ulica Lubelska | 8 | — |
| **Latus 3** | Przedmieście Piasek (Część 1) | 12 | 25 |
| **Latus 4** | Przedmieście Piasek (Część 2) i Zarzyce | 18 | — |
| **Latus 5** | Przedmieście Zarzyce (Dokończenie) | 13 | 21 |
| **Latus 6** | Przedmieście Góry i Podlesie (Część 1) | 16 | 15 |
| **Latus 7** | Przedmieście Góry i Podlesie (Część 2) | 3 | 17 |
| **SUMMA SYMPLI** | **Suma Generalna Sympli Miejskiej** | **81** | **24** |

*Dicitur per expressum: Złł Pols: Ośmdziesiąt Jeden Groszy Dwadzieścia Cztery.*

---

### Rozliczenie Rachunków (26 XI 1780 – 16 V 1781):
- **Percepty:** Złł Pols: Pięć Tysięcy Sto Siedmdziesiąt y dwa złote 1/2 [5172 zł 15 gr]
- **Expensy:** Złł Pols: Pięć Tysięcy Dwieście dziewięć groszy 26 [5209 zł 26 gr]
- **Naddanych przez Exaktora:** Złł Trzydzieści Siedm gro 3 1/2 [37 zł 3 1/2 gr], które z przyszłey proweniencyi odebrać sobie powinien.

---

### Elekcya Urzędu na Rok teraznieyszy 1781szy:
- **Woytem Obrany:** Sławetny **Sebestyan Szubartowski**
- **Burmistrzami:** Franciszek Barankiewicz, Jakub Gąska, Maciey Rycerz, Krzysztof Suliczyński
- **Exaktorem:** Franciszek Frankiewicz
- **Deputat na Trybunał:** Sławetny Józef Paszkiewicz"""
    },
    "196": {
        "tytul": "Dekret i napomnienie ordynackie sędziego generalnego Andrzeja Wyszyńskiego przeciwko pijaństwu, zniewagom i buntom pospólstwa",
        "data_rok": "1781-05-16",
        "kategoria": "Dekret komisarski / Zwalczanie rebelii i obrona powagi magistratu",
        "osoby_podmioty": "Andrzej Wyszyński (skarbnik JKM, sędzia i burgrabia generalny zamku zamoyskiego), Urzędnicy magistratu, Pospólstwo kraśnickie, Leśniczy Grodzki zamoyski",
        "opis_pozycji": "Surowy dekret dyscyplinarny sędziego generalnego Andrzeja Wyszyńskiego wydany po elekcji miejskiej. Sędzia potępia powszechne w Kraśniku nieposłuszeństwo pospólstwa wobec magistratu, uchylanie się od płacenia podatków, niestawianie się na wezwania sądu oraz obelgi i dyfamacje kierowane ku urzędnikom, co paraliżuje obsadę urzędów miejskich. Jako źródło tego stanu wskazuje plagę pijaństwa. Rozkazuje zakuwać opornych i buntowników w kajdany i przy asyście Leśniczego Grodzkiego odsyłać ich do więzienia w Twierdzy Zamojskiej.",
        "kwoty_miary": "Rygor karny: zakuwanie w kajdany i deportacja do więzienia Twierdzy Zamojskiej.",
        "uwagi": "Wstrząsający dokument ukazujący kryzys autorytetu władzy miejskiej, opór podatkowy pospólstwa oraz rygorystyczne środki przymusu stosowane przez Ordynację Zamojską.",
        "transkrypcja": """[PAGINA 94v]
[Dekret i Napomnienie Ordynackie Sędziego Generalnego Andrzeja Wyszyńskiego z 16 Maja 1781 r.]

Niechcąc powtarzać powinności każdego Urzędnika, lecz odsyłam do obszernego opisu w Roku przeszłym [1779] przeze Mnie czynionego, w tych samych obrębach zalecam aby sprawiedliwość była Administrowana, Expens miasta ile możności zmałpkowana [zmniejszona], Złe obyczaie wytępione, Chwała Boska pomnożona, Za co nietylko w doczesnym życiu Panowie Urzędnicy z ktorych całe Pospolstwo wzor mieć będzie zaszczycą obfite Błogosławieństwo Boskie, lecz po skończonym życiu czekać ich będzie obfita nadgroda.

Że zaś sam napatrzyłem się w czasie Elekcyi wielkiego nieposłuszeństwa w Pospolstwie ktorzy zwykli zuchwale ku Urzędowi postępować, składek powinnych nie oddaiąc, za wydanemi pozwami, lub za słownym wezwaniem do tegoż Urzędu niestawiając się, i dotego niewytwornych słow nieuprzeymie lżyć y dyfamować, Przez co żadnego słusznego człeka na Funkcyą ciężkości niezmierna wynaleść; Czego naywiększą iest okazyą obrzydłe pijaństwo, ktorzy aż nazbyt w tym mieyscu znayduią;

Więc gdy to ostatnie napomnienie Moie uskuteczniony niebędzie, Zalecam teraznieyszemu Urzędowi aby bez żadney względności takowego złośliwego Rebelizanta w Kaydany zakuwszy do Fortecy Zamoyskiey dla poprawy dalszego życia odsyłał; Do imania y transportowania dopomoże Urzędowi J[m]ć Pan Leśniczy Grodzki;

Dato w Kraśniku dnia y Roku iako wyżey [16 Maja 1781 r.]

**Andrzey Wyszyński**  
*Skarb[nik] J[ego] K[rólewskiej] M[ości], S[ędzia] G[eneralny] Z[amoyski] mp.*"""
    },
    "197": {
        "tytul": "Wybór ławników i cechmistrzów kraśnickich (szewcy, tkacze, kuśnierze) pod przewodnictwem magistratu",
        "data_rok": "1781-05-18",
        "kategoria": "Elekcja urzędowa i cechowa / Wybór ławników i cechmistrzów",
        "osoby_podmioty": "Andrzej Wyszyński (sędzia generalny), Wojciech Latosiewicz (ławnik starszy), Franciszek Matuszkiewicz (ławnik wtóry), Wawrzyniec Kielaszkiewicz (ławnik 3ci), Walenty Łukasik (ławnik 4ty), Sebastian Latosiewicz (cechmistrz szewski), Stanisław Bosoniak (podcechmistrz szewski), Józef Paszkiewicz (cechmistrz tkacki), Piotr Młynarczyk (podcechmistrz tkacki), Łukasz Dybicki (cechmistrz kuśnierski), Herszek Zeluśkowicz (cechmistrz kuśnierski żydowski)",
        "opis_pozycji": "Kontynuacja procedury elekcyjnej po wyjeździe sędziego Wyszyńskiego. Magistrat Radziecki pod przewodnictwem wójta Szubartowskiego przystępuje do wyboru 4 ławników sądowych oraz starszych cechowych. Na ławicę zatwierdzeni zostają: Wojciech Latosiewicz, Franciszek Matuszkiewicz, Wawrzyniec Kielaszkiewicz oraz Walenty Łukasik. W wyborach cechowych wyłoniono starszych cechu szewskiego, tkackiego oraz kuśnierskiego (w tym chrześcijańskiego mistrza Łukasza Dybickiego i żydowskiego cechmistrza Herszka Zeluśkowicza).",
        "kwoty_miary": "Obsada 4 urzędów ławniczych oraz 3 cechów rzemieślniczych.",
        "uwagi": "Ważny przywilej cechowy Ordynacji Zamojskiej dopuszczający reprezentację rzemieślników żydowskich na stanowisku cechmistrza kuśnierskiego.",
        "transkrypcja": """[PAGINA 95]
[Wybór Ławników i Cechmistrzów Kraśnickich pod Przewodnictwem Magistratu – 18 Maja 1781 r.]

Po zakończoney Elekcyi przez Wielmoznego J[m]ć Pana Wyszyńskiego Dnia 16 Miesiąca Maja Roku 1781.  
Więc Dnia Ośmnastego tegoż Miesiąca y Roku Magistrat Radziecki do przybrania Ławnikow y Obrania Cechomistrzow przystępuie zgodnemi ich w każdym Cechu Głosami:

### Na Ławicę Sądową:
1. **Woyciech Latosiewicz** — *Approbowany Starszy*
2. **Franciszek Matuszkiewicz** — *Approbowany Wtóry*
3. **Wawrzyniec Kielaszkiewicz** — *Approbowany 3ci*
4. **Walenty Łukasik** — *Obrany 4ty*

---

### Wybory Cechowe:

#### Cech Szefski:
- **Sebestyan Latosiewicz** — *Pierwszy Cechmistrz*
- **Stanisław Bosoniak** — *Wtóry Cechmistrz*

#### Cech Tkacki:
- **Jozef Paszkiewicz** — *Pierwszy Cechmistrz*
- **Piotr Młynarczyk** — *Wtóry Cechmistrz*

#### Cech Kusznierski:
- **Łukasz Dybicki** — *Pierwszy Cechmistrz*
- **Herszek Zeluśkowicz** — *Wtóry Cechmistrz (żydowski)*"""
    },
    "198": {
        "tytul": "Dokończenie wyborów cechmistrzów kraśnickich – cech kowalski i krawiecki",
        "data_rok": "1781-05-18",
        "kategoria": "Elekcja cechowa / Cech kowalski i krawiecki",
        "osoby_podmioty": "Jędrzej Barankiewicz (cechmistrz kowalski), Maciej Rycerz (podcechmistrz kowalski), Jakub Grzymek (cechmistrz krawiecki)",
        "opis_pozycji": "Zamknięcie protokołu wyborów cechowych z 18 maja 1781 r.: wybór starszych cechu kowalskiego (Jędrzej Barankiewicz pierwszy, Maciej Rycerz wtóry) oraz pierwszego cechmistrza krawieckiego (Jakub Grzymek).",
        "kwoty_miary": "Obsada cechu kowalskiego i krawieckiego.",
        "uwagi": "Krótki, lecz fundamentalny zapis zamykający skład władz cechowych Kraśnika na kadencję 1781–1782.",
        "transkrypcja": """[PAGINA 95v]
[Dokończenie Wyborów Cechmistrzów Kraśnickich – Kowale i Krawcy]

### Cech Kowalski:
- **Jędrzey Barankiewicz** — *Pierwszy Cechmistrz*
- **Maciey Rycerz** — *Wtóry Cechmistrz*

### Cech Krawiecki:
- **Jakob Grzymek** — *Pierwszy Cechmistrz*"""
    }
}

with open('/home/ubuntu/workspace/Gen/part11_trans_3.json', 'w', encoding='utf-8') as f:
    json.dump(part3_trans, f, ensure_ascii=False, indent=2)

print("Zapisano part11_trans_3.json pomyślnie.")
