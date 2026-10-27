#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_j40_part6_audit.py
Wdrożenie Partii 6 (Skany 91–105) Akt Miasta Kraśnika J40:
1. Aktualizacja transkrypcji dyplomatycznej z tabelami (Opcja A) dla skanów 91–105.
2. Synchronizacja bazy genealogicznej genData (profile 734-750, aktualizacja wariantów i skanów).
3. Aktualizacja KPI w HTML.
4. Eksport zaktualizowanego skorowidza krasnik_j40_slownik_genealogiczny.csv.
"""

import json
import csv
import re
import os

HTML_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html'
CSV_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_slownik_genealogiczny.csv'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Wyodrębnienie mainData
m_start = html_content.find('const mainData = [')
m_end = html_content.find('];', m_start) + 1
main_data = json.loads(html_content[m_start + len('const mainData = '):m_end])

# Wyodrębnienie genData
g_start = html_content.find('const genData = [')
g_end = html_content.find('];', g_start) + 1
gen_data = json.loads(html_content[g_start + len('const genData = '):g_end])

print(f"Początkowy stan: mainData={len(main_data)}, genData={len(gen_data)}")

# -------------------------------------------------------------
# 1. Definicje zaktualizowanych rekordów mainData dla skanów 91–105
# -------------------------------------------------------------

transkrypcje_p6 = {
    91: {
        "kategoria": "Ustrój miejski / Sądownictwo / Ordynacja Kochowskiego 1775",
        "opis_pozycji": "Punkty 2 i 3 ordynacji Kochowskiego: pisemna forma i procedura doręczania pozwów przez woźnego pod pieczęcią (opłata pisarza 4 gr, wójta 2 gr) oraz rygor trzech kondemnat za niestawiennictwo (odpowiedzialność majątkowa, licytacja gruntu, domu lub ogrodu na rzecz strony dowodowej).",
        "kwoty_miary": "Opłata pisarza: 4 gr;\nOpłata wójta od pieczęci: 2 gr;\nTermin doręczenia pozwu: 3 dni przed sądem;\nLicytacja: do wysokości winy",
        "osoby_podmioty": "Antoni z Kochowa Kochowski komisarz ordynacki, pisarz miejski, wójt kraśnicki, woźny miejski, mieszczanie i przedmieszczanie kraśniccy",
        "osoby_skrot": "Antoni Kochowski, pisarz, wójt, woźny miejski",
        "transkrypcja": """[Na marginesie górnym:] 45 [nad skreślonym: 44]
zysku, lecz sprawiedliwey Bogu się zawsze podo-
baiącey mocno upatruiąc drogi.

2do. Pozwy na piśmie wydawać na dni trzy
przed sprawą, ktore pod pieczęcią dla każdego
Mieszczanina y Przedmieszczanina dyspo-
zycyą maiącego wydane być maią, Woźny
roznieść powinien, Gospodarzowi lub Gospody-
ni oddawać, ktore iako tylko oddane zostaną
natychmiast relacyą zeznać, tę w xięgi zapi-
sać, od ktorey przyięcia Pisarz groszy cztery,
Woyt od pieczęci Pozwow groszy dwa brać po-
winien.

3tio. Jeżeliby ktory zapozwany niestanął, a
strona dowodowa pokazałaby relacyą au-
tentyczną wydanego pozwu, to Sądu ma
prosić o Kondemnatę, ktora tak powinna
bydź zapisana, iako iest forma w porządku
Prawa Magdeburgskiego; a ieżliby na drugie
Sądy stanął, to iednak zapozwany nie może
się rosprawiać aż zniesie kondemnatę, y zapłaci za nie
podług wymiaru występku. Lecz gdyby nie-
stanął, to o drugą Kondemnatę prosić, na
trzecich Sądach o trzecią, a taki nieposłuszny
staie się Banitem y Infamisem. Po otrzyma-
nych trzech Kondemnatach powinien Pisarz
z dwiema Ławnikami wydzielić gruntu podług
proporcyi winy, albo Domostwo, lub Ogrod, iżli
innego nic niebędzie, ten Stronie Dowodowey"""
    },

    92: {
        "kategoria": "Ustrój miejski / Kancelaria i Skarbowość / Ordynacja Kochowskiego 1775",
        "opis_pozycji": "Punkty 4 i 5 ordynacji Kochowskiego: obowiązki pisarza miejskiego Grzegorza Madejskiego (zakaz fałszowania wpisów, umiarkowanie w taksach kancelaryjnych, rejestracja uchwał symplowych i podymnych) oraz rygorystyczny monopol zaprzysiężonego szafarza na ekspensę kasy miejskiej pod kwitem wójta lub rezydentów.",
        "kwoty_miary": "Rygor kasowy: zakaz ekspensy bez kwitu wójta/rezydentów;\nObowiązek rejestracji sum symplowych i podymnych",
        "osoby_podmioty": "Antoni z Kochowa Kochowski komisarz ordynacki, Grzegorz Madejski (Madeyski) pisarz miejski, wójt, zaprzysiężeni szafarze miejscy, rezydenci, dziesiętnicy, pospólstwo Kraśnika",
        "osoby_skrot": "Antoni Kochowski, Grzegorz Madejski pisarz, wójt, szafarz",
        "transkrypcja": """[Na marginesie górnym:] 45 v
oddać pokąd zadosyć nieuczyni Prawu. Wprawi-
wszy w ten Rygor iednego y dziesiątego setni się
będą kaiać.

4to. Sł[awnemu] Madeyskiemu Pisarzowi Mieyskiemu
nayusilniey zalecam aby swoią funkcyą nay-
sprawiedliwiey się rządził, Fabrykacyi w Xię-
gach y Zapisach żadney nieczynił, Od Extra-
ktow y Tranzakcyi Ubogich ludzi nie ciemiężył, lecz
proporcyonalną za swoią pracą kontentował
się nadgrodą. Wszystkie Uchwały Symplowe,
Podymne, iako y teraznieysze do rachunkow nie
weszłe, y inne pod iakimkolwiek bądź tytułem
składki punktualnie z wyrażeniem dnia y
roku aby w ten Prothokuł zapisywał, Regestra
zaś onych osobne Dziesiętnikom wydawał.

5to. Pieniędzmi ani Woyt, ani Rezydent expen-
sować nie powinien, procz iednego na ten koniec
Przysięgłego Szafarza, lub drugiego. Szafarz
zaś naymnieyszey czynić niepowinien Ex-
pensy przez wiadomości y kwitu Woyta lub
ktorego z Rezydentow. Perceptę y Expens
z wyrażeniem dnia y roku y na iakioby obro-
cona interess zapisywać powinien, aby mi nie
tak było, iak podczas tey Elekcyi gdzie ani
Percepty ani Expensy gruntowney domacać
niemożna było, lepiey parę Złotych stracić
na papier, a pospolstwu iawnie pokazać gdzie
ich praca y krew podziała."""
    },

    93: {
        "kategoria": "Porządek publiczny / Bezpieczeństwo pożarowe / Relacje z Żydami i Kościołem 1775",
        "opis_pozycji": "Punkty 6–10 ordynacji Kochowskiego: comiesięczna rewizja kominów katolickich i żydowskich przeciwpożarowa, obowiązek terminowego oddawania kopczyzny proboszczowi, ochrona dochodów ratusznych, wagowych i szarwarków, równe obciążenie podatkowe Żydów do połowy składek oraz zakaz samosądów.",
        "kwoty_miary": "Kontrola kominów: raz w miesiąc;\nPodział składek publicznych: Żydzi do połowy wraz z Katolikami;\nOchrona prowentów: ratuszne, jateczne, szarwarczne",
        "osoby_podmioty": "Antoni z Kochowa Kochowski komisarz ordynacki, ks. proboszcz kraśnicki, wójt i magistrat, szafarz miejski, starsi żydowscy i Żydzi kraśniccy",
        "osoby_skrot": "Antoni Kochowski, ks. proboszcz, szafarz, Żydzi kraśniccy",
        "transkrypcja": """[Na marginesie górnym:] 46 [nad skreślonym: 45]
6to. Ostrożność Ognia, reparacyą drog nowo
obranemu Magistratowi mocno zalecam
y przypominam, aby przynaymniey raz w
Miesiąc tak Katolickie iak Żydowskie zre-
widowane były kominy z uwagą czy Sadze
wycierane bywaią lub nie?

7mo. W. Jmć X. Proboszcz mocno się żali o nie-
oddawanie Mu należącey kopczyzny; Za-
czym surowo nakazuię aby ta w przyzwoi-
tym zawsze czasie wiernie y rzetelnie odda-
waną bywała. A ieżliby kiedy do Urzędu
otę zaszła skarga, tedy Woyt przykładnie
takiego niech ukarze iako Przestępcę Prawa
Boskiego y Koscielnego, y niezwłoczną iemu naka-
że satysfakcyą.

8vo. Dochody Mieyskie aby mi nieupadały, iako to Ra-
tuszne, Jateczne, Szarwarczne, y inne, ale aby podług
Prawa y Zwyczaiu dawnego utrzymywane bywały, temi nikt
szafować niepowinien, procz iednego Szafarza, ktore
do Percepty Jego wchodzić powinny.

9no. Do Składek Mieyskich Publicznych aby Żydzi
podług dawnego zwyczaiu do połowy wraz z Kato-
likami pociągani bywali.

10mo. W wszelkich zachodzących kłotniach y sprzeczkach
z Żydami, aby sobie nikt sprawiedliwości sam nieczy-
nił mocno zakazuie, lecz ukrzywdzony katolik niech
się uda do Starszych Żydowskich a tam sprawiedli-"""
    },

    94: {
        "kategoria": "Finanse miejskie / Likwidacja długów / Dekret Kochowskiego 1775",
        "opis_pozycji": "Asygnacja spłaty długów miejskich ante omnia przez nowo obrany magistrat: 60 zł dla ks. proboszcza (założone za miasto dyrektorowi szkoły), 50 zł reszty pensji p. Kliszewskiego dyrektora szkoły za dosłużony rok, 6 zł 16 gr dla Jakuba Szulca (Szultza) za poselstwo do Węgier oraz nakaz spłaty długu za owies wojskowy u kupców żydowskich Chabusia Judkowicza i Jecka Lejbusiewicza.",
        "kwoty_miary": "Dług ks. Proboszcza: 60 zł;\nReszta pensji dyrektora Kliszewskiego: 50 zł;\nDroga do Węgier Jakuba Szulca: 6 zł 16 gr;\nZobowiązanie za owies wojskowy",
        "osoby_podmioty": "Antoni z Kochowa Kochowski komisarz ordynacki, ks. proboszcz kraśnicki, p. Kliszewski dyrektor szkoły miejskiej, Sł. Jakub Szulc (Szultz / Szulik) poseł miejski do Węgier, Chabuś Judkowicz (Chabusia Judkowicza) kupiec starozakonny, Jecko Leybusiewicz kupiec starozakonny",
        "osoby_skrot": "Antoni Kochowski, ks. proboszcz, p. Kliszewski, Jakub Szulc, Chabuś Judkowicz, Jecko Leybusiewicz",
        "transkrypcja": """[Na marginesie górnym:] 46 v
wość znaydzie, Podobnymże sposobem Ukrzywdzony
Żyd gdy się w Urzędzie uskarży sprawiedliwość zna-
leść powinien.

A ponieważ na tak znaczne dochody y częste Skład-
ki Miasta tego, żadnych Miasto nie uczyniło porząd-
kow, y Długow żadnych choć sprawiedliwych nie
uspokoiło: Zaczym Nowo Obranemu Magi-
stratowi surowo przykazuię y zalecam aby dłu-
gi niżey opisane ante omnia zaspokojone zo-
stały; Jako to Dług W. Jmć Xiędza Proboszcza
Tuteyszego przez Przeszły Urząd Kraśnicki swie-
żo zeszły podpisany na Złot: Pol: 60. przez Tegoż
W. Jmć X. Proboszcza przeszłemu Dyrektorowi
Mieyskiemu za Miasto założonych y zapłaco-
nych, aby niezwłocznie zaspokojonym został.
P. Kliszewskiemu Dyrektorowi Mieyskiemu za
dosłużony Rok aby reszty Zł: 50 Polskich nieza-
wodną y niezwłoczną odebrania onych pozy-
skał satysfakcyą.
Sł[awetnemu] Jakubowi Szultzowi [Szulcowi] za drogę do Węgier do
JW Pana chodzącemu w interessie Mieyskim
Zł: 6 gr 16 wypłacić należy.
Dług Starozakonnego Chabusia [Cnabusia?] Judkowicza y Je-
cka Leybusiewicza za wzięty w nagłey potrze-
bie Owies dla przechodzących Woysk rożnych
przez Magistrat świeżo zeszły, ten iako w pilney
potrzebie stał się ratunkiem Miasta, tak spra-"""
    },

    95: {
        "kategoria": "Finanse miejskie / Wynagrodzenia i Wierzytelności / Dekret Kochowskiego 1775",
        "opis_pozycji": "Dalsza asygnacja spłaty długów miejskich: 73 zł 6 gr za owies dla kupców żydowskich Chabusia i Jecka, 30 zł dla wdowy po pisarzu Brzozowskim (obecnie Gołębiowskiej), 72 zł pożyczki od Szmula Zeywla, nagroda 70 zł dla szafarza Grzegorza Pielaszka, 30 zł na buty dla szafarza Krzysztofa Sulicińskiego oraz 57 zł 20 gr zaległych zasług dla pisarza Grzegorza Madejskiego.",
        "kwoty_miary": "Dług za owies wojskowy: 73 zł 6 gr;\nWdowa Brzozowska 1mo voto (Gołębiowska): 30 zł;\nPożyczka Szmula Zeywla: 72 zł;\nNagroda dla szafarza Pielaszka: 70 zł;\nNa boty dla szafarza Sulicińskiego: 30 zł;\nZasługi pisarza Madejskiego: 57 zł 20 gr",
        "osoby_podmioty": "Antoni z Kochowa Kochowski komisarz ordynacki, Chabuś Judkowicz i Jecko Leybusiewicz kupcy starozakonni, Jmć pani Brzozowska 1mo voto (obecnie Gołębiowska) wdowa po pisarzu miejskim, Szmul Zeywel kupiec starozakonny, Sł. Grzegorz Pilaszek (Pielaszek) były szafarz, Sł. Krzysztof Suliciński szafarz, Grzegorz Madejski (Madeyski) pisarz miejski",
        "osoby_skrot": "Antoni Kochowski, wdowa Gołębiowska, Szmul Zeywel, Grzegorz Pielaszek, Krzysztof Suliciński, Grzegorz Madejski",
        "transkrypcja": """[Na marginesie górnym:] 47 [nad skreślonym: 46]
wiedliwe y nieodwłoczne iak kwity Jego swiadczą
Złt Siedmdziesiąt trzy groszy sześć Polskich za
wzięty od nich owies wynoszących odebrać powi-
nien zaspokoienie nayusilniey przykazuię.
Jmć Brzozofskiey 1mo voto, a teraznieyszey Gołembio-
wskiey, należących nieboszczykowi mężowi za-
sług za pisarską funkcyą Złot: Trzydzieści aby
Urząd teraźnieyszy nakazał onę zaspokoić.
Starozakonnemu Szmulowi Zeywelowi przez
Urząd Kraśnicki pożyczonych przed kilkoma
lat Zł: 72 Polskich na interess Miasta, ten
iako iest sprawiedliwy, bo gotowemi pieniędz-
mi w pilney potrzebie założony, tak spra-
wiedliwe Starozakonny Szmul Zeywel otrzy-
mać powinien zaspokoienie.
Sł[awnemu] Grzegorzowi Pilaszkowi [Pielaszkowi] Szafarzowi Miey-
skiemu w nadgrodę Jego wiernych y podci-
wych usług naznacza się Złotych Siedmdziesiąt.
Sł[awnemu] Krysztowowi Sulicińskiemu Szafarzowi dru-
giemu w zasługach Jego składka potrąca się,
y na boty Złotych Trzydzieści naznacza się.
Wszystkie zaś wyżey wyrażone długi aby nie-
odwłoczną odebrały satysfakcyą surowo
nakazuię.
Sł[awetnemu] P. Madeyskiemu Pisarzowi Mieyskiemu nale-
żących reszty za lat dwa Zasług Złt 57 gr"""
    },

    96: {
        "kategoria": "Ustrój miejski / Woźny miejski / Klauzula sankcyjna ordynacji 1775",
        "opis_pozycji": "Dokończenie ordynacji i dekretu Antoniego Kochowskiego: dopłata 20 gr dla pisarza Madejskiego, nakaz wydania kożucha wiernemu woźnemu miejskiemu Jakubowi Kozłowiczowi za wieloletnią służbę oraz autograficzny podpis burgrabiego i sędziego grodzkiego Antoniego Kochowskiego.",
        "kwoty_miary": "Dopłata dla pisarza: 20 gr (łącznie 57 zł 20 gr);\nŚwiadczenie w naturze: kożuch sukienny dla woźnego",
        "osoby_podmioty": "Antoni z Kochowa Kochowski Sędzia Grodzki Krasnostawski i Burgrabia Trybunału Ordynacji Zamoyskiej, Jakub Kozłowicz były woźny miejski kraśnicki, Grzegorz Madejski pisarz miejski",
        "osoby_skrot": "Antoni z Kochowa Kochowski komisarz, Jakub Kozłowicz woźny",
        "transkrypcja": """[Na marginesie górnym:] 47 v
groszy 20 aby Urząd teraznieyszy niezwłocznie
Jemu nakazał zaspokoienie.
Jakub Kozłowicz przeszły Woźny Mieyski ten
służąc wiernie Miastu, więc za swoie usługi
należący Jemu Kożuch oddany być powinien
y ma mocą ninieyszą nakazuię. —

Antoni z Kochowa Kochowski Sędzia Grodzki
Krasnostawski Burgrabia Trybunału Ordynacyi
Zamoyskiey. —"""
    },

    97: {
        "kategoria": "Ustrój miejski / Dublet fotograficzny skanu 96 / Pag. 47v",
        "opis_pozycji": "Dublet fotograficzny i alternatywne ujęcie skanu 96 (Pag. 47v): nakaz zaspokojenia woźnego Kozłowicza kożuchem i asygnata Antoniego Kochowskiego.",
        "kwoty_miary": "Kożuch sukienny dla woźnego Kozłowicza;\n20 gr dopłaty dla pisarza",
        "osoby_podmioty": "Antoni z Kochowa Kochowski komisarz ordynacki, Jakub Kozłowicz były woźny miejski kraśnicki",
        "osoby_skrot": "Antoni Kochowski, Jakub Kozłowicz woźny",
        "transkrypcja": """[Dublet fotograficzny skanu 96 – Pag. 47v:]
[Na marginesie górnym:] 47 v
groszy 20 aby Urząd teraznieyszy niezwłocznie
Jemu nakazał zaspokoienie.
Jakub Kozłowicz przeszły Woźny Mieyski ten
służąc wiernie Miastu, więc za swoie usługi
należący Jemu Kożuch oddany być powinien
y ma mocą ninieyszą nakazuię. —

Antoni z Kochowa Kochowski Sędzia Grodzki
Krasnostawski Burgrabia Trybunału Ordynacyi
Zamoyskiey. —"""
    },

    98: {
        "kategoria": "Taryfy podatkowe / Sympla / Śródmieście 1775",
        "opis_pozycji": "Taryfa jednej sympli miejskiej uchwalona 29 XI 1775 r. przez zaprzysiężonych symplarzy: wykaz podatników centrum miasta Kraśnika (Kolumna 1 i 2). Suma 1. latusa: 5 zł 19 gr, 2. latusa z transportem: 13 zł 5 gr.",
        "kwoty_miary": "Latus 1 (Miasto Kraśnik): 5 zł 19 gr;\nLatus 2 z transportem: 13 zł 5 gr;\nStawki indywidualne: od 1 gr do 24 gr",
        "osoby_podmioty": "Mieszkańcy Śródmieścia Kraśnika: Jacek Fiszer, Paweł Latosowicz, wójt Józef Tokarski, Mikołaj Łapa, Kazimierz Rycerz, Michał Chrzanowski, Grzegorz Dybiecki, Wojciech Wilk, Tomasz Pilaszkiewicz, Michał Matuszkiewicz i inni",
        "osoby_skrot": "Symplarze przysięgli, Jacek Fiszer, Mikołaj Łapa, Grzegorz Dybiecki, Wojciech Wilk",
        "transkrypcja": """[Na marginesie górnym:] 48 [poprawione z 47]
Sympła przy obraniu Nowego Magistratu przez poprzysię-
głych Symplarzy wyznaczonych 29. 9bris 1775to Ułożona

### [Kolumna 1: Miasto Kraśnik]

| Posesjonat / Mieszczanin (Śródmieście) | Złote | Grosze |
| :--- | :---: | :---: |
| Jacek Fisier [Fiszer] | — | 8 |
| Domek Skrzypielski [Krzywicki?] | — | 2 |
| Paweł Latosowicz | — | 2 |
| Jozef Tokarski [Wójt] | — | 3 |
| Mikołay Łapa | — | 10 |
| Kazimierz Rycerz | — | 14 |
| Michał Chrzanofski [Chrzanowski] | — | 13 |
| Antoni Krzeszofski | — | 5 |
| Jakub Szulik [Szulc?] | — | 5 |
| Piotr Gołembiowski [Gołębiowski] | — | 2 |
| Antoniowa Łaniecka [Zaniewska?] | — | 2 |
| Krysztoufa Wdowa [Kłyszowska?] | — | 2 |
| Jozef Kerczynski [Kurczyński / Korczyński?] | — | 2 |
| Zaiączkowa Wdowa | — | 4 |
| Jakub Grzymek | — | 3 |
| Anto Pempkiefski [Petrykowski?] | — | 6 |
| Maciy Rycerz | — | 5 |
| Jakub Kojek | — | 6 |
| Grzegorz Zdybicki [Dybiecki?] | — | 20 |
| Woyciech Połokowicz | — | 3 |
| Franciszek Frankowicz | — | 6 |
| Mateusz Byzik [Pyzik?] | — | 3 |
| Maciy Cieśla [Ciesielka?] | — | 3 |
| Z Marcowiczowego | — | 2 |
| Antoni Okoń | — | 4 |
| Z Okoniowego Chabuś | — | 2 |
| Baltazar Latosowicz | — | 3 |
| Antoni Sadofski [Sadowski] | — | 2 |
| Woyciech Latoskowicz [Latoszkiewicz] | — | 3 |
| Michał Jędencarz [Jedencarz] | — | 3 |
| Jozef Czaplinski | — | 2 |
| Jan Foliarski [Tokarski?] | — | 5 |
| Domek Bryczkowey | — | 5 |
| Piotr Marczynski | — | 2 |
| Stachowiczowa Wdowa | — | 2 |
| **Summa 1mi Latus** | **5** | **19** |

### [Kolumna 2: Śródmieście cd.]

| Posesjonat / Mieszczanin (Śródmieście cd.) | Złote | Grosze |
| :--- | :---: | :---: |
| *Transp Lato (Latus 1)* | *5* | *19* |
| Jan Mulofski [Mudowski?] | — | 4 |
| Szymon Nowacki | — | 5 |
| Walenta Szafrancka [Szafrański] | — | 2 |
| Antoni Tulicinsski [Suliciński?] | — | 5 |
| Szymonowa Szajofka [Szajowska] | — | 5 |
| Woyciech Bieniaszefski | — | 1 |
| Woyciech Krzeszofski | — | 4 |
| Mateusz Rycerz | — | 6 |
| Jakub Gąska | — | 2 |
| Walenty Łukasik | — | 3 |
| Piotr Młynarczyk | — | 2 |
| Sebestyan Latosowicz | — | 2 |
| Jozef Stemborfki [Stembowski] | — | 16 |
| Antoni Rachon | — | 4 |
| Kazimierz Młynarski | — | 16 |
| Maciejowa Fruzyna [Fruzyńska] | — | 4 |
| Petronella Sadoftka [Sadowska] | — | 10 |
| Michał Matuszkiewicz | — | 24 |
| Tomasz Pilaskiewicz [Pilaszkiewicz] | — | 8 |
| Alexandrowa Bajarska [Boiarska] | — | 2 |
| Woyciech Wilk | — | 15 |
| Antoni Kępa | — | — |
| Krzycha Rusek | — | — |
| Grzegorz Latosiewicz | — | — |
| Jakob Rozmarynofski | — | — |
| Paweł Fuga [Fruga] | — | 12 |
| Adamowa Zeydlerowa [Zejdlerowa] | — | 7 |
| Anto Piasecki | — | 13 |
| Walenta Rachuniowa | — | 12 |
| Jan Boguta | — | 8 |
| Krasoska Wdowa [Krasowska] | — | 6 |
| Piotr Połokowicz | — | 14 |
| Tokarska Wdowa | — | 4 |
| Anto Pilaszkiewiczowa | — | 8 |
| **Summa 2di Latus (z transportem)** | **13** | **5** |"""
    },

    99: {
        "kategoria": "Taryfy podatkowe / Sympla / Przedmieścia Piasek i Zarzyce 1775",
        "opis_pozycji": "Dalszy ciąg taryfy sympli z 29 XI 1775 r.: dokończenie Śródmieścia (Paweł Piasecki 25 gr, Józef Bańka 16 gr), przedmieście Piasek (Stanisław Wolak 1 zł 10 gr, Joachim Kłopot 1 zł) oraz początek Zarzyc. Suma Latus 3: 38 zł 14½ gr, Latus 4: 51 zł 15½ gr.",
        "kwoty_miary": "Latus 3 (Śródmieście i Piasek z transp.): 38 zł 14½ gr;\nLatus 4 (Piasek cd. i Zarzyce z transp.): 51 zł 15½ gr",
        "osoby_podmioty": "Mieszkańcy centrum Kraśnika, przedmieścia Piasek i przedmieścia Zarzyce: Stanisław Posoniak, Paweł Piasecki, Antoni Tkaczyk, Stanisław Wolak, Joachim Kłopot, Kazimierz Czeley, Wawrzyniec Stanbrat i inni",
        "osoby_skrot": "Stanisław Posoniak, Paweł Piasecki, Stanisław Wolak, Wawrzyniec Stanbrat",
        "transkrypcja": """[Na marginesie górnym:] 48 v

### [Kolumna 1: Dokończenie Miasta y Przedmieście Piasek]

| Posesjonat / Mieszczanin (Dokończenie Miasta) | Złote | Grosze |
| :--- | :---: | :---: |
| *Transp Latt (z karty 48)* | *13* | *5* |
| Stanisław Pasoniak [Posoniak] | — | 8 |
| Michałowa Lańska | — | 8 |
| Mikołay Radomski | — | 14 |
| Krysztof Pilaszkiewicz | — | 15 |
| Maciy Wołczynski | — | 7 |
| Jędrzy Kępa | — | 6 |
| Marcin Kępa | — | 5 |
| Maciejowa Kępina | — | 10 |
| Walenty Jurgel [Jurgiel] | — | 8 |
| Woyciech Fijałkoski [Fijałkowski] | — | 3 |
| Paweł Piasecki | — | 25 |
| Woyciech [skreślone/nadpisane: Maciey] Połokowicz | — | 4 |
| Grzegorz Leśnioski [Leśniowski] | — | 7 |
| Szczepan Woycik | — | 3 |
| Jozef Bańka | — | 16 |

#### [Przedmieście Piasek]

| Posesjonat / Przedmieszczanin (Piasek) | Złote | Grosze |
| :--- | :---: | :---: |
| Antoni Tkaczyk | — | 25 |
| Stanisław Wolak | 1 | 10 |
| Szymon Antonik | — | 15 |
| Łukasz Łapa | — | 20 |
| Sebestyan Kilianek | — | 7½ |
| Piotr Kilianek | — | 20 |
| Jan Dzioniek [Dzieniek / Bieniek?] | — | 19 |
| Marcin Łapa | — | 17 |
| Rymarzowa Wdowa | — | 25 |
| Gasiorwa Wdowa [Gąsiorowa] | — | 20 |
| Paweł Jeś | — | 5 |
| Tomek Jażdżyk | 1 | — |
| Maciy Zdyb | — | 25 |
| Jan Woycik | — | 15 |
| [Niewierny] Kopiński | 1 | 5 |
| Mikołay Nowak | — | 15 |
| Franciszek Petka [Pełka?] | — | 15 |
| Jakob Jeczniak [Jacznik?] | — | 15 |
| Bartek Zdyb | — | 7 |
| Franciszek Aszoski [Oszowski / Okposki?] | — | 6 |
| Janowa Gayczykowa | — | 15 |
| Jakub Jasiewicz | — | 20 |
| **Suma 3tii Latus (z transportem)** | **38** | **14½** |

### [Kolumna 2: Przedmieście Piasek cd. y Początek Zarzyc]

| Posesjonat / Przedmieszczanin (Piasek cd.) | Złote | Grosze |
| :--- | :---: | :---: |
| Woyciech Cwicha [Ćwicha] | — | — |
| Andrzy Gaiek [Gajek] | — | — |
| Woyciech Nowak | — | 12 |
| Szymon Woycik | — | 7 |
| Woytek Wiatrek | — | 7 |
| Paweł Zielenski | — | 15 |
| Woytek Petka [Pełka?] | — | 15 |
| Woytek Drąg | — | 20 |
| Łukasz Betka | — | 7 |
| Joachim Kłopot | 1 | — |
| Łukasz Tokarczyk | — | 15 |
| Michał Tokarczyk | — | 15 |
| Piotr Tokarczyk | — | 15 |
| Woyciech Woycik | — | 15 |
| Stach Kępniak | — | 12 |
| Barbara Bielecka | — | 8 |
| Stach Woycik | — | 23 |
| Woyciech Troyczak | — | 25 |
| Kazimierz Troyczak | — | 25 |
| Kazimierz Czeliy [Czeley] | 1 | — |

#### [Przedmieście Zarzycze]

| Posesjonat / Przedmieszczanin (Zarzyce) | Złote | Grosze |
| :--- | :---: | :---: |
| Bartłomiy Czeliy [Czeley] | — | 25 |
| Łysakowa Wdowa | — | 19 |
| Bartek Kielianek | — | 13 |
| Maciy Szubartoski | — | 7 |
| Wiatrkowa Wdowa | — | 18 |
| Grzegorz Jażdżyk | — | 17 |
| Wawrzyniec Stanbrat | 2 | 10 |
| Maciy Rachuń | — | 15 |
| Cuszkowa Wdowa | — | 12 |
| Szymon Marzec | — | 13 |
| Stachowa Rodzonkowa | — | 12 |
| Szymon Marzec [drugi zapis] | — | 25 |
| Łukasz Kielianek | — | 10 |
| Maciek Rodzonek | — | 25 |
| Kasper Troyczak | — | 11 |
| Antoni Panek | — | 18 |
| Grzegorz Biegay | — | 10 |
| **Summa 4ti Latus (z transportem)** | **51** | **15½** |"""
    },

    100: {
        "kategoria": "Taryfy podatkowe / Dublet fotograficzny skanu 99 / Pag. 48v",
        "opis_pozycji": "Dublet fotograficzny i alternatywne ujęcie skanu 99 obejmujące taryfę przedmieść Piasek i Zarzyce z 29 XI 1775 r. (identyczny zestaw pozycji i sum).",
        "kwoty_miary": "Latus 3: 38 zł 14½ gr;\nLatus 4: 51 zł 15½ gr",
        "osoby_podmioty": "Mieszkańcy przedmieść Piasek i Zarzyce (spis sympli)",
        "osoby_skrot": "Mieszkańcy przedmieść Piasek i Zarzyce (dublet)",
        "transkrypcja": """[Dublet fotograficzny skanu 99 – Pag. 48v:]
[Na marginesie górnym:] 48 v

### [Kolumna 1: Dokończenie Miasta y Przedmieście Piasek]

| Posesjonat / Mieszczanin (Dokończenie Miasta) | Złote | Grosze |
| :--- | :---: | :---: |
| *Transp Latt (z karty 48)* | *13* | *5* |
| Stanisław Pasoniak [Posoniak] | — | 8 |
| Michałowa Lańska | — | 8 |
| Mikołay Radomski | — | 14 |
| Krysztof Pilaszkiewicz | — | 15 |
| Maciy Wołczynski | — | 7 |
| Jędrzy Kępa | — | 6 |
| Marcin Kępa | — | 5 |
| Maciejowa Kępina | — | 10 |
| Walenty Jurgel [Jurgiel] | — | 8 |
| Woyciech Fijałkoski [Fijałkowski] | — | 3 |
| Paweł Piasecki | — | 25 |
| Woyciech [skreślone/nadpisane: Maciey] Połokowicz | — | 4 |
| Grzegorz Leśnioski [Leśniowski] | — | 7 |
| Szczepan Woycik | — | 3 |
| Jozef Bańka | — | 16 |

#### [Przedmieście Piasek]

| Posesjonat / Przedmieszczanin (Piasek) | Złote | Grosze |
| :--- | :---: | :---: |
| Antoni Tkaczyk | — | 25 |
| Stanisław Wolak | 1 | 10 |
| Szymon Antonik | — | 15 |
| Łukasz Łapa | — | 20 |
| Sebestyan Kilianek | — | 7½ |
| Piotr Kilianek | — | 20 |
| Jan Dzioniek [Dzieniek / Bieniek?] | — | 19 |
| Marcin Łapa | — | 17 |
| Rymarzowa Wdowa | — | 25 |
| Gasiorwa Wdowa [Gąsiorowa] | — | 20 |
| Paweł Jeś | — | 5 |
| Tomek Jażdżyk | 1 | — |
| Maciy Zdyb | — | 25 |
| Jan Woycik | — | 15 |
| [Niewierny] Kopiński | 1 | 5 |
| Mikołay Nowak | — | 15 |
| Franciszek Petka [Pełka?] | — | 15 |
| Jakob Jeczniak [Jacznik?] | — | 15 |
| Bartek Zdyb | — | 7 |
| Franciszek Aszoski [Oszowski / Okposki?] | — | 6 |
| Janowa Gayczykowa | — | 15 |
| Jakub Jasiewicz | — | 20 |
| **Suma 3tii Latus (z transportem)** | **38** | **14½** |

### [Kolumna 2: Przedmieście Piasek cd. y Początek Zarzyc]

| Posesjonat / Przedmieszczanin (Piasek cd.) | Złote | Grosze |
| :--- | :---: | :---: |
| Woyciech Cwicha [Ćwicha] | — | — |
| Andrzy Gaiek [Gajek] | — | — |
| Woyciech Nowak | — | 12 |
| Szymon Woycik | — | 7 |
| Woytek Wiatrek | — | 7 |
| Paweł Zielenski | — | 15 |
| Woytek Petka [Pełka?] | — | 15 |
| Woytek Drąg | — | 20 |
| Łukasz Betka | — | 7 |
| Joachim Kłopot | 1 | — |
| Łukasz Tokarczyk | — | 15 |
| Michał Tokarczyk | — | 15 |
| Piotr Tokarczyk | — | 15 |
| Woyciech Woycik | — | 15 |
| Stach Kępniak | — | 12 |
| Barbara Bielecka | — | 8 |
| Stach Woycik | — | 23 |
| Woyciech Troyczak | — | 25 |
| Kazimierz Troyczak | — | 25 |
| Kazimierz Czeliy [Czeley] | 1 | — |

#### [Przedmieście Zarzycze]

| Posesjonat / Przedmieszczanin (Zarzyce) | Złote | Grosze |
| :--- | :---: | :---: |
| Bartłomiy Czeliy [Czeley] | — | 25 |
| Łysakowa Wdowa | — | 19 |
| Bartek Kielianek | — | 13 |
| Maciy Szubartoski | — | 7 |
| Wiatrkowa Wdowa | — | 18 |
| Grzegorz Jażdżyk | — | 17 |
| Wawrzyniec Stanbrat | 2 | 10 |
| Maciy Rachuń | — | 15 |
| Cuszkowa Wdowa | — | 12 |
| Szymon Marzec | — | 13 |
| Stachowa Rodzonkowa | — | 12 |
| Szymon Marzec [drugi zapis] | — | 25 |
| Łukasz Kielianek | — | 10 |
| Maciek Rodzonek | — | 25 |
| Kasper Troyczak | — | 11 |
| Antoni Panek | — | 18 |
| Grzegorz Biegay | — | 10 |
| **Summa 4ti Latus (z transportem)** | **51** | **15½** |"""
    },

    101: {
        "kategoria": "Taryfy podatkowe / Sympla / Zarzyce, Góry y Podlesie y Rekapitulacja 1775",
        "opis_pozycji": "Dokończenie taryfy sympli z 29 XI 1775 r. dla Zarzyc oraz przedmieścia Góry i Podlesie (Wojciech Bus 1 zł 18 gr, Szymon Krzeszowski 1 zł 20 gr). Rekapitulacja generalna: 88 zł 19½ gr (Dico per expressum osmdziesiąt osm złotych gr dziewiętnaście y poł) zatwierdzona autografem komisarza Antoniego Kochowskiego.",
        "kwoty_miary": "Latus 5 z transp.: 69 zł 10½ gr;\nSumma Generalis Sympli: 88 [89] zł 19½ gr;\n(Dico per expressum 88 zł 19½ gr)",
        "osoby_podmioty": "Antoni z Kochowa Kochowski komisarz ordynacki, mieszkańcy Zarzyc oraz przedmieścia Góry i Podlesie: Maciej Piotrowski, Jędrzej Rządkowski, Wojciech Bus, Szymon Krzeszowski, Józef Nowak, Józef Gąska, Stanisław Bielach (Pielach) i inni",
        "osoby_skrot": "Antoni Kochowski, Wojciech Bus, Szymon Krzeszowski, Stanisław Bielach",
        "transkrypcja": """[Na marginesie górnym:] 49 [poprawione z 48]

### [Kolumna 1: Dalsze Przedmieście Zarzyce y Początek Gór]

| Posesjonat / Przedmieszczanin (Zarzyce cd.) | Złote | Grosze |
| :--- | :---: | :---: |
| *Transp Lato (z karty 48v)* | *51* | *15½* |
| Maciy Piotrofski [Piotrowski] | — | 20 |
| Łukasz Rymarz | — | 15 |
| Jędrzy Tokarczyk | — | 10 |
| Marcin Drąg | — | 20 |
| Woyciech Wolak | — | 14 |
| Marcin Kołton | — | 10 |
| Marcin Rymarz | — | 13 |
| Łaszczyna Wdowa | — | 12 |
| Martowa Wdowa [Martkowa?] | — | 12 |
| Jędrzy Rządkofski | 1 | — |
| Kazimierz Olichofski [Olechowski] | — | 8 |
| Sobek Łysak | — | 8 |
| Jozef Dubay | — | 12 |
| Sobkowa Dubajowa | — | 10 |
| Kazimierz Deryło [Deuyło?] | — | 8 |
| Sobek Mikołayczyk | 1 | — |
| Tomasz Rządkoski | — | 20 |
| Maciy Chruściel | — | 5 |
| Łukasz Biegay | — | 20 |
| Jozef Koza | — | 15 |
| Maciy Łazarz | — | 8 |
| Kasper Rodzonek | — | 20 |
| Stach Woycik | — | 10 |
| Antoni Koza | — | 12 |
| Bartek Grządka | — | 8 |
| Maciy Kuśnierz | — | 15 |
| Mikołay Kępa | — | 12 |
| Łukasz Koza | — | 12 |
| Wawrzyniec Gęzarek [Gęzarch?] | — | 12 |
| Mikołay Buczek | — | 8 |
| Woyciech Biegay | — | 10 |
| Oszustowa Wdowa | — | 5 |
| Młynarczykowa Wdowa | — | 12 |
| Stach Piotroski | — | 15 |

#### [Góry y Podlesie]

| Posesjonat / Przedmieszczanin (Góry y Podlesie) | Złote | Grosze |
| :--- | :---: | :---: |
| Szymon Płachta | — | 14 |
| Adam Michał | — | 5 |
| Jan Boguta | — | 10 |
| Woyciech Gąska | — | 7 |
| Woyciech Kaska [Kawka?] | — | 17 |
| Młynarczykowa Wdowa | — | 20 |
| **Summa 5ti Latus (z transportem)** | **69** | **10½** |

### [Kolumna 2: Przedmieście Góry y Podlesie cd. y Rekapitulacja]

| Posesjonat / Przedmieszczanin (Góry cd.) | Złote | Grosze |
| :--- | :---: | :---: |
| *Transp Latt (Latus 5)* | *69* | *10½* |
| Jakob Rządkoski | — | 15 |
| Anto Troyczakowa | — | 5 |
| Fabian Troyczak | — | 8 |
| Jacek Grzymek | — | 15 |
| Sobek Troyczak | — | 5 |
| Maciek Troyczak [Brat Jego] | — | 5 |
| Maciy Kępa | — | 5 |
| Mikołay Kawka | — | 15 |
| Jozef Strażnik | — | 15 |
| Tomek Kawka | — | 15 |
| Anto Tokarczyk | — | 25 |
| Sebestyan Szubartoski | — | 25 |
| Szymon Krzeszofski | 1 | 20 |
| Jozef Nowak | — | 25 |
| Wawrzyniec Tokarczyk | — | 12 |
| Augustyn Grzegorczyk | — | 12 |
| Anto Wilk | — | 25 |
| Jozef Gąska | — | 25 |
| Franciszek Kłopot | — | 8 |
| Mikołay Zdyb | — | 5 |
| Szymon Cwieka [Ćwieka] | — | 25 |
| Pawlicka Wdowa | — | 7 |
| Grądzyna Wdowa | — | 5 |
| Jan Wilk | — | 8 |
| Mateusz Zdyb | — | 8 |
| Zimniakowa Wdowa | — | 18 |
| Lenartowa Wdowa | — | 13 |
| Tomek Wilk | — | 18 |
| Maciy Kawka | — | 13 |
| Grzegorz Wolak | — | 8 |
| Andrzy Kępa | — | 14 |
| Augustyn Kawka | — | 15 |
| Jozef Wilk | — | 16 |
| Błaży Babież [Babiarz?] | — | 12 |
| Woyciech Bus [Rus?] | 1 | 18 |
| Krzych Cwieka [Ćwieka] | — | 3 |
| Benedykt Kawka | — | 2 |
| Stach Pielach [Bielach] | — | 14 |
| Walenty Biegay | — | 8 |
| Sebestyan Zdyb | — | 23 |
| Woyciechowa Cwichowa [Ćwichowa] | — | 8 |
| **Summa Generalis Sympli** | **88 [89]** | **19½** |

Dico Osmdziesiąt osm Suma 88 [89] Złotych gr Dziewiętnascie y poł.

Ant:[oni] Kochowski Sędzia Grodz:[ki] Krasnost:[awski] Burgrabia Ord:[ynacyi] Zamoys[kiey] mpp."""
    },

    102: {
        "kategoria": "Ustrój miejski / Elekcja ławników i cechmistrzów / Cechy rzemieślnicze 1775",
        "opis_pozycji": "Uzupełniająca elekcja urzędu ławniczego i władz cechowych w grudniu 1775 r. pod przewodnictwem Antoniego Kochowskiego: powołanie ławników, usunięcie Stanisława Posoniaka za publiczne bluźnierstwo i przeklinanie deputacji na rzecz Michała Jędencarza oraz wybór starszych i podstarszych cechów: tkackiego, szewskiego, kowalskiego i kuśnierskiego (z udziałem starozakonnego Leyby Czapnika).",
        "kwoty_miary": "Skład ławicy: 4 ławników;\nWładze cechowe: 4 cechy (tkacki, szewski, kowalski, kuśnierski)",
        "osoby_podmioty": "Antoni z Kochowa Kochowski komisarz ordynacki, Sebastian Latosowicz major ławnik i cechmistrz szewski, Stanisław Posoniak cechmistrz major szewski (zdyskwalifikowany z ławicy), Michał Jędencarz (Jedencarz) nowo powołany ławnik, Piotr Młynarczyk ławnik, Maciej Rycerz ławnik, Paweł Fruzyński (Fruzynsky) cechmistrz tkacki starszy, Piotr Połokowicz cechmistrz tkacki młodszy, Kazimierz Rycerz cechmistrz kowalski starszy, Łukasz Biegaj cechmistrz kowalski wtóry, Grzegorz Zdyb cechmistrz kuśnierski starszy, Leyba Czapnik starozakonny podstarszy kuśnierski",
        "osoby_skrot": "Antoni Kochowski, Sebastian Latosowicz, Stanisław Posoniak, Michał Jędencarz, Paweł Fruzyński, Grzegorz Zdyb, Leyba Czapnik",
        "transkrypcja": """[Na marginesie górnym:] 49 v
Po Zakończoney Elekcyi przez W:[ielmożne]go Jmć Pana Antonie-
go z Kochowa Kochowskiego Pana y Dobrodzieja
Sędziego Grodzkiego Krasnostawskiego, Burgra-
biego Trybunału Ordynacyi Zamoyskiey. Ła-
scie sb: Urząd Miasta Kraśnika, na Urząd Ławicy,
tudzież y Cechmistrzow takowych obiera Mężow,
jako niżey wyraża sie.

### [Urząd Ławicy Miejskiej]
[Na marginesie lewym:] Na Ławicę przybrał Ławnikow Magistrat Radziecki sb: Mężow w Religii Wyćwiczonych

* Sł:[awetny] Sebastyan Latosowicz major
* Sł:[awetny] Stanisł:[aw] Posoniak
* Sł:[awetny] Piotr Młynarczyk
* Sł:[awetny] Maciy Rycerz

> **[Klauzula dyskwalifikacyjna:]** Na Mieyscu zaś Sł:[awetnego] Stanisł:[awa] Posoniaka, przez Jego zły uczynek że In Publico Deputacyą Dyabłom oddawał, seqvitz [zastępuje go] Sł:[awetny] Michał Jędencarz [Jedencarz].

---

### Elekcyja Cechowa (Władze Cechów Kraśnickich)

#### 1. Cech Tkacki:
* Sł:[awetny] Paweł Fruzynsky [Fruzyński] — Cechmistrz starszy
* Sł:[awetny] Piotr Połokowicz — Cechmistrz młodszy

#### 2. Cech Szewcki:
* Sł:[awetny] Stanisław Posoniak — Cechmistrz Major
* Sł:[awetny] Sebastyan Latosowicz — Cechm:[istrz] wtóry

#### 3. Cech Kowalsky:
* Sł:[awetny] Kz:[imierz] Rycerz — Cechm:[istrz] starszy
* Sł:[awetny] Łukasz Biegay — Cechm:[istrz] wtóry

#### 4. Cech Kuśniersky:
* Sł:[awetny] Grzegorz Zdyb — Cechm:[istrz] starszy
* Subst:[itut] Niewier:[ny] Leyba Czapnik — wtóry"""
    },

    103: {
        "kategoria": "Taryfy podatkowe / Osiem Sympli / Spłata długów miejskich / Śródmieście 1776",
        "opis_pozycji": "Nadzwyczajna taryfa podatkowa „Ułożenie Ośmiu Sympel” z 1776 r. uchwalona przez wójta Józefa Tokarskiego, urząd i pospólstwo na spłatę narosłych długów miejskich. Wykaz posesjonatów Śródmieścia (Kolumna 1 i 2). Suma 1. latusa: 32 zł 15 gr, 2. latusa z transportem: 91 zł 27 gr.",
        "kwoty_miary": "1mus Cfr Latus (Śródmieście): 32 zł 15 gr;\n2dus Latus z transportem: 91 zł 27 gr;\nWymiar podatku: stawki ośmiokrotne",
        "osoby_podmioty": "Józef Tokarski wójt kraśnicki, Jacek Fiszer, Michał Chrzanowski, Grzegorz Zdyb, Michał Matuszkiewicz, Jan Boguta, Paweł Fruga, Wojciech Wilk i inni posesjonaci centrum",
        "osoby_skrot": "Józef Tokarski wójt, Jacek Fiszer, Grzegorz Zdyb, Michał Matuszkiewicz, Jan Boguta",
        "transkrypcja": """[Na marginesie górnym:] 50
Ułożenie Ośmiu Sympel: p:[rzez] Urząd y Całe Pospolstwo
1776to R:[oku] na wypłacenie Długow Spisane

### [Kolumna 1: Miasto Kraśnik]

| Posesjonat / Mieszczanin (Śródmieście) | Złote | Grosze |
| :--- | :---: | :---: |
| Jacek Fisier [Fiszer] | 1 | 10 |
| Domek P. Krzywicki [Krzywcki] | — | 12 |
| Paweł Latosowicz | — | 12 |
| P. Jozef Tokarski Woyt | — | — |
| Mikołay Łapa | 2 | — |
| Kzmr: Rycerz [Kazimierz] | 2 | 24 |
| Michał Chrzanofski [błędnie: Wziąndtki?] | 2 | 10 |
| Anto: Krzeszowski | 1 | — |
| Jakob Szulik [Szulc?] | 1 | — |
| Piotr Gołembiowski [Gołębiowski] | — | 12 |
| Anto. Zaniewska | — | 12 |
| Kłyszowska Wda [Wdowa] | — | 12 |
| Jozefa Korczynskiego Puste | — | — |
| Zaiączkowa Wda | — | 12 |
| Jakob Grzymek | — | 10 |
| Anto: Petrykowski | 1 | 6 |
| Maciy Rycerz Ławnik | — | 15 |
| Jakob Kojek | 1 | 6 |
| Grzegorz Zdyb | 4 | — |
| Woyciech Połokowicz | — | 10 |
| Franc: Frankowicz | 1 | 6 |
| Mateusz Byzik [Pyzik?] | — | 10 |
| Maciy Cieśla [Ciesielka?] | — | 10 |
| Z Marcowiczowego | — | 12 |
| Antoni Okoń | — | 24 |
| Z Okoniowego Chabuś | — | 12 |
| Baltazar Latosowicz | — | 10 |
| Michał Jędencarz [Jedencarz] | — | 10 |
| Anto: Sadowski | — | 12 |
| Woyciech Latoskowicz [Latoszkiewicz] | — | 10 |
| Jozef Czaplinski | — | 12 |
| Jan Tokarski [Foliarski?] | 1 | 10 |
| Domek Bryczkowy | 1 | — |
| Piotr Marczynski | — | 10 |
| Stachowiczowa Wda | — | 12 |
| Jan Mudorski [Mulofski / Mudowski?] | — | 24 |
| **1mus Cfr Latus** | **32** | **15** |

### [Kolumna 2: Śródmieście cd.]

| Posesjonat / Mieszczanin (Śródmieście cd.) | Złote | Grosze |
| :--- | :---: | :---: |
| *Transport 1mi Lat* | *32* | *15* |
| Szymon Nowacki | 1 | — |
| Walenta Szafranska [Szafrański] | — | 12 |
| Anto Suliczyński | 1 | — |
| Woyciech Bieniaszefski | 1 | — |
| Woyciech Krzeszowski | — | 24 |
| Mateusz Rycerz | 1 | 6 |
| Jakob Gąska | — | 12 |
| Walenty Łukasik | — | 10 |
| Piotr Młynarczyk | — | 9 |
| Sebastyan Latosowicz | — | 6 |
| Jozef Stembowski | 3 | 6 |
| Anto Rachon | — | 24 |
| Kz: Młynarski | 3 | 6 |
| Fruzyna Wda [Fruzyńska] | — | 24 |
| Petronella Sadowska | 2 | — |
| Michał Matuszkiewicz | 4 | 24 |
| Tomek Pilaszkiewicz | 1 | 18 |
| Boiarska Wdowa [Bajarska] | — | 12 |
| Woyciech Wilk | 3 | — |
| Paweł Fruga | 2 | 10 |
| Z Zydlowego [Zeydlerowego] | 1 | 12 |
| Anto: Piasecki | 2 | 18 |
| Walenta Rachuniowa | 2 | 12 |
| Jan Boguta | 1 | 18 |
| Krasowska Wda | 1 | 6 |
| Piotr Połokowicz | 2 | 24 |
| Tokarska Wda | — | 24 |
| Antoniowa Pilaszkiewiczowa | 1 | 18 |
| Stanisł: Posoniak | 1 | 18 |
| Lańska Wda | 1 | 18 |
| Mikołay Radomski | 2 | 24 |
| Krysz: Pielach [Pilaszkiewicz] | 3 | — |
| Maciy Wołczynski | 1 | 12 |
| Jędrzey Kępa | 1 | 6 |
| Mar: Kępa | 1 | — |
| Kępina Wda | 2 | — |
| Walenty Jurgiel | 1 | 18 |
| **2dus Latus (z transportem)** | **91** | **27** |"""
    },

    104: {
        "kategoria": "Taryfy podatkowe / Osiem Sympli / Przedmieścia Piasek i Zarzyce 1776",
        "opis_pozycji": "Dalszy ciąg taryfy 8 sympli z 1776 r.: dokończenie Śródmieścia (Paweł Piasecki 5 zł 6 gr, Józef Bańka 3 zł 6 gr), przedmieście Piasek (Stanisław Wolak 8 zł, Tomek Jażdżyk 6 zł, Maciej Zdyb 5 zł) oraz przedmieście Zarzyce (Wawrzyniec Stanbrat 14 zł, Maciek Rodzonek 5 zł).",
        "kwoty_miary": "Stawki 8 sympli: Stanisław Wolak 8 zł, Wawrzyniec Stanbrat 14 zł, Tomek Jażdżyk 6 zł, Paweł Piasecki 5 zł 6 gr",
        "osoby_podmioty": "Mieszkańcy Śródmieścia, Piasku i Zarzyc: Paweł Piasecki, Józef Bańka, Stanisław Wolak, Tomek Jażdżyk, Maciej Zdyb, Wawrzyniec Stanbrat, Kazimierz Czeley, Maciek Rodzonek i inni",
        "osoby_skrot": "Józef Bańka, Paweł Piasecki, Stanisław Wolak, Wawrzyniec Stanbrat",
        "transkrypcja": """[Na marginesie górnym:] 50 v
Dalsze Ułożenie Ośmiu Sympli Spisane

### [Kolumna 1: Dokończenie Miasta y Przedmieście Piasek]

| Posesjonat / Mieszczanin (Dokończenie Miasta) | Złote | Grosze |
| :--- | :---: | :---: |
| *Transport (z karty 50)* | *91* | *27* |
| Jozef Szpiciarzk | — | — |
| Woyciech Fijałkowski | — | 10 |
| Paweł Piasecki | 5 | 6 |
| Maciey Połokowicz | — | 24 |
| Grzegorz Leśniostki [Leśniowski] | 1 | 12 |
| Szczepan Woycik | — | 10 |
| Jozef Bańka | 3 | 6 |

#### [Przedmieście Piasek]

| Posesjonat / Przedmieszczanin (Piasek) | Złote | Grosze |
| :--- | :---: | :---: |
| Anto: Tkaczyk | 5 | — |
| Stach Wolak [Stanisław] | 8 | — |
| Szymon Antonik | 3 | — |
| Łukasz Łapa | 4 | — |
| Seba: Kilianek | 1 | 15 |
| Piotr Kilianek | 4 | — |
| Jan Bieniek [Dzieniek?] | 3 | 24 |
| Mar: Łapa | 3 | 12 |
| Rymarzowa Wda | 3 | — |
| Jasiewa Wda [Gąsiorowa?] | 5 | 24 |
| Paweł Jeś | 1 | — |
| Tomek Jazdżyk [Jażdżyk] | 6 | — |
| Maciy Zdyb | 5 | — |
| Jan Woycik | 3 | — |
| Nb: Kopiński [Niewierny] | 8 | — |
| Mikołay Nowak | 3 | — |
| Franc: Petka [Pełka?] | 3 | — |
| Jakob Jaczniak [Jęczniak?] | 3 | — |
| Bartek Zdyb | 1 | 12 |
| Franc: Okposki [Oszowski?] | 1 | 6 |
| Janowa Gayczykowa | 3 | — |
| Jakob Jasiewicz [Jąśkiewicz] | 5 | 24 |
| Andrzey Gajek | 2 | 12 |
| Woyciech Nowak | 5 | — |
| Szymon Woycik | 2 | 12 |
| Woytek Wiatrek | 1 | 12 |
| Paweł Zielensky | 1 | 12 |
| Woyciech Petka [Pełka?] | 3 | — |
| Woyciech Drąg | 3 | — |
| **3tius Latus** | *[Latus 3]* | *[Latus 3]* |

### [Kolumna 2: Przedmieście Piasek cd. y Przedmieście Zarzyce]

| Posesjonat / Przedmieszczanin (Piasek cd.) | Złote | Grosze |
| :--- | :---: | :---: |
| Łukasz Betka | 4 | — |
| Joachin Kłopot [Joachim] | 1 | 12 |
| Łukasz Tokarczyk | 6 | — |
| Michał Tokarczyk | 2 | 10 |
| Piotr Tokarczyk | 3 | — |
| Woyciech Woycik | 3 | — |
| Stach Kępniak | 3 | — |
| Barbara Bielecka | 2 | 12 |
| Stach Woycik | 1 | 10 |
| Woyciech Troyczak | 4 | 10 |
| Kz: Troyczak [Kazimierz] | 5 | — |
| Kz: Czeley [Kazimierz] | 5 | — |

#### [Przedmieście Zarzyce]

| Posesjonat / Przedmieszczanin (Zarzyce) | Złote | Grosze |
| :--- | :---: | :---: |
| Bartek Czeley | 5 | — |
| Łysakowa Wda | 3 | 24 |
| Bartek Kilianek | 2 | 10 |
| Maciey Szubartoski | 1 | 12 |
| Wiatrkowa Wdowa | 3 | 10 |
| Grzegorz Jazdżyk [Jażdżyk] | 3 | 12 |
| Wawrzyniec Stanbrat | 14 | — |
| Maciey Rachon | 3 | — |
| Cuszkowa Wda | 2 | 12 |
| Marzec Szymek | 2 | 10 |
| Stach: Rodzonkowa Wda | 2 | 12 |
| Łukasz Kilianek | 2 | — |
| Maciek Rodzonek | 5 | — |
| Kasper Troyczak | 2 | 6 |
| Anto Panek | 4 | 10 |
| Grzegorz Biegay | 2 | — |
| Maciey Piotroski | 5 | 24 |
| Łukasz Rymarz | 3 | 10 |
| Jędrzey Tokarczyk | 2 | — |
| Marcin Drąg | 4 | — |
| Woy: Wolak Dzieci | — | — |
| **4tum Latus** | *[Latus 4]* | *[Latus 4]* |"""
    },

    105: {
        "kategoria": "Taryfy podatkowe / Osiem Sympli / Zarzyce oraz Góry y Podlesie 1776",
        "opis_pozycji": "Dokończenie taryfy 8 sympli z 1776 r.: rzemieślnicy i posesjonaci Zarzyc (Andrzej Rządkowski 6 zł, Sobek Mikołajczyk 6 zł) oraz przedmieścia Góry i Podlesie (Wojciech Bus 9 zł 10 gr, Szymon Krzeszowski 6 zł, Józef Nowak 5 zł). Zestawienie końcowe: Suma Ex Lati fecit.",
        "kwoty_miary": "Stawki 8 sympli: Wojciech Bus 9 zł 10 gr, Szymon Krzeszowski 6 zł, Andrzej Rządkowski 6 zł, Sobek Mikołajczyk 6 zł",
        "osoby_podmioty": "Mieszkańcy Zarzyc oraz Gór i Podlesia: Andrzej Rządkowski, Sobek Mikołajczyk, Wojciech Bus, Szymon Krzeszowski, Józef Nowak, Józef Gąska, Stanisław Bielach (Pielach) i inni",
        "osoby_skrot": "Andrzej Rządkowski, Wojciech Bus, Szymon Krzeszowski, Józef Nowak",
        "transkrypcja": """[Na marginesie górnym:] 51 [poprawione z 50]
Dalsze Ułożenie Ośmiu Sympli Spisane

### [Kolumna 1: Dalsze Przedmieście Zarzyce y Początek Gór]

| Posesjonat / Przedmieszczanin (Zarzyce cd.) | Złote | Grosze |
| :--- | :---: | :---: |
| Marc: Kołton | 2 | — |
| Marcin Rymarz | 2 | 10 |
| Łaszczyna Wda | 2 | 12 |
| Markowa Wda [Martkowa?] | 2 | 12 |
| Jędrzey Rządkowski | 6 | — |
| Kz: Olechowski | 1 | 10 |
| Sobek Łysak | 1 | 10 |
| Jozef Dubay | 2 | 12 |
| Sobkowa Dubajowa | 2 | — |
| Kz: Deryło | 1 | 10 |
| Sobek Mikołayczyk | 6 | — |
| Tomek Rządkoski | 4 | — |
| Maciey Chruściel | 1 | 6 |
| Łukasz Biegay | 4 | — |
| Jozef Koza | 3 | — |
| Maciey Łazarz | 1 | 10 |
| Kasper Rodzonek | 4 | — |
| Stach Woycik | 2 | — |
| Anto: Koza | 2 | 12 |
| Bartek Grządka | 1 | 10 |
| Maciey Kuśnierz | 3 | — |
| Mikołay Kępa | 2 | 12 |
| Łukasz Koza | 2 | 12 |
| Warsz: Gęzarek [Wawrzyniec] | 2 | 12 |
| Mikołay Buczek | 1 | 10 |
| Woyciech Biegay | 2 | — |
| Oszustowa Wda | 1 | — |
| Młynarczykowa | 2 | 12 |
| Stach Piotrowski | 3 | — |

#### [Góry y Podlesie]

| Posesjonat / Przedmieszczanin (Góry y Podlesie) | Złote | Grosze |
| :--- | :---: | :---: |
| Szymon Płachta | 2 | 24 |
| Adam Michał | 1 | — |
| Jan Boguta | 2 | — |
| Woyciech Gąska | 1 | 12 |
| **5tum Latus** | *[Latus 5]* | *[Latus 5]* |

### [Kolumna 2: Przedmieście Góry y Podlesie cd. y Suma]

| Posesjonat / Przedmieszczanin (Góry cd.) | Złote | Grosze |
| :--- | :---: | :---: |
| Woyciech Kawka | 3 | 12 |
| Młynarczykowa | 4 | — |
| Jakob Rządkowski | 3 | — |
| Anto Troyczakowa | 1 | — |
| Fabian Troyczak | 1 | 10 |
| Jacek Grzymek | 3 | — |
| Sobek Troyczak | 1 | — |
| Maciy Brat Jego [Trojczak] | 1 | — |
| Maciy Kępa | 1 | — |
| Mikołay Kawka | 3 | — |
| Jozef Strażnik | 3 | — |
| Tomek Kawka Dzieci | — | — |
| Anto Tokarczyk | 5 | — |
| Szym: Krzeszowski | 6 | — |
| Jozef Nowak | 5 | — |
| Aug: Gregorczyk | 2 | 12 |
| Wawrz: Tokarczyk | 2 | 12 |
| Jozef Gąska | 5 | — |
| Franc: Kłopot | 1 | 10 |
| Mikołay Zdyb | 1 | — |
| Szym: Cwieka [Ćwieka] | 5 | — |
| Pawlicka Wda | 1 | 12 |
| Grądzyna Wda | 1 | — |
| Jan Wilk | 1 | 10 |
| Mateusz Zdyb | 1 | 10 |
| Zimniakowa Wda | 3 | 10 |
| Lenartowa Wda | 2 | 10 |
| Tomek Wilk | 3 | 10 |
| Maciy Kawka | 2 | 10 |
| Grzegorz Wolak | 1 | 10 |
| Andrzey Kępa | 2 | 24 |
| Aug: Kawka [Augustyn] | 3 | — |
| Jozef Wilk | 3 | 6 |
| Błach Babiez [Babiarz?] | 2 | 12 |
| Woyciech Bus [Rus?] | 9 | 10 |
| Krzych Cwieka [Ćwieka] | — | 10 |
| Benedykt Kawka | — | 12 |
| Stach Pielach [Bielach] | 2 | 24 |
| Walenty Biegay | 1 | 10 |
| Sobek Zdyb | 4 | 10 |
| Cwichowa Wda [Ćwichowa] | 1 | 10 |
| **Suma Ex Lati fecit** | **—** | **—** |"""
    }
}

# Aplikacja transkrypcji do main_data
for sn, data_update in transkrypcje_p6.items():
    idx = sn - 1
    for k, v in data_update.items():
        main_data[idx][k] = v

print(f"Zaktualizowano transkrypcje i metadane dla skanów 91–105.")

# -------------------------------------------------------------
# 2. Aktualizacja genData (dodanie profili 734-750)
# -------------------------------------------------------------

nowe_profile = [
    {
        "lp": 734,
        "nazwisko": "Kliszewski",
        "wariant_nazwiska": "Kliszewski (Dyrektor szkoły)",
        "imie": "",
        "przydomek": "",
        "funkcja": "Dyrektor szkoły kraśnickiej",
        "miejsce": "Kraśnik",
        "skany_roboczo": "#94",
        "skany_list": [94],
        "zakres_lat": "1775",
        "min_rok": 1775,
        "max_rok": 1775,
        "liczba_wystapien": 1,
        "wystapienia": [
            {
                "nazwisko": "Kliszewski",
                "imie": "",
                "miejsce": "Kraśnik",
                "rola": "Dyrektor szkoły miejskiej w Kraśniku",
                "skan": 94,
                "rok": "1775",
                "zapis_oryginalny": "P. Kliszewskiemu Dyrektorowi Mieyskiemu",
                "kwota_ctx": "Reszta 50 zł za dosłużony rok"
            }
        ],
        "uwagi": "Dyrektor szkoły miejskiej w Kraśniku, wierzyciel kasy miejskiej zatwierdzony dekretem komisarza ordynackiego Antoniego Kochowskiego."
    },
    {
        "lp": 735,
        "nazwisko": "Judkowicz",
        "wariant_nazwiska": "Chabuś? / Chabusia Judkowicza / Cnabuś?",
        "imie": "Chabuś",
        "przydomek": "",
        "funkcja": "Kupiec starozakonny / Dostawca owsa / Posesjonat",
        "miejsce": "Dzielnica żydowska / Kraśnik",
        "skany_roboczo": "#94, #98, #103",
        "skany_list": [94, 98, 103],
        "zakres_lat": "1775–1776",
        "min_rok": 1775,
        "max_rok": 1776,
        "liczba_wystapien": 3,
        "wystapienia": [
            {
                "nazwisko": "Judkowicz",
                "imie": "Chabuś",
                "miejsce": "Kraśnik",
                "rola": "Kupiec starozakonny / Dostawca furażu",
                "skan": 94,
                "rok": "1775",
                "zapis_oryginalny": "Chabusia Judkowicza",
                "kwota_ctx": "73 zł 6 gr za owies wojskowy"
            },
            {
                "nazwisko": "Judkowicz",
                "imie": "Chabuś",
                "miejsce": "Śródmieście",
                "rola": "Posesjonat",
                "skan": 98,
                "rok": "1775",
                "zapis_oryginalny": "Z Okoniowego Chabuś",
                "kwota_ctx": "2 gr."
            },
            {
                "nazwisko": "Judkowicz",
                "imie": "Chabuś",
                "miejsce": "Śródmieście",
                "rola": "Posesjonat",
                "skan": 103,
                "rok": "1776",
                "zapis_oryginalny": "Z Okoniowego Chabuś",
                "kwota_ctx": "12 gr."
            }
        ],
        "uwagi": "Kupiec starozakonny, dostawca owsa dla przechodzących wojsk w nagłej potrzebie miejskiej (73 zł 6 gr); posesjonat przy dworku Okoniowym."
    },
    {
        "lp": 736,
        "nazwisko": "Leybusiewicz",
        "wariant_nazwiska": "Jecko? / Icko? / Leybusiewicz",
        "imie": "Jecko",
        "przydomek": "",
        "funkcja": "Kupiec starozakonny / Dostawca owsa",
        "miejsce": "Dzielnica żydowska / Kraśnik",
        "skany_roboczo": "#94",
        "skany_list": [94],
        "zakres_lat": "1775",
        "min_rok": 1775,
        "max_rok": 1775,
        "liczba_wystapien": 1,
        "wystapienia": [
            {
                "nazwisko": "Leybusiewicz",
                "imie": "Jecko",
                "miejsce": "Kraśnik",
                "rola": "Kupiec starozakonny / Dostawca furażu",
                "skan": 94,
                "rok": "1775",
                "zapis_oryginalny": "Jecka Leybusiewicza",
                "kwota_ctx": "73 zł 6 gr wspólnie z Chabusiem Judkowiczem"
            }
        ],
        "uwagi": "Kupiec starozakonny, dostawca owsa dla wojsk przechodzących przez Kraśnik wspólnie z Chabusiem Judkowiczem."
    },
    {
        "lp": 737,
        "nazwisko": "Zeywel",
        "wariant_nazwiska": "Szmul Zeywel / Zeywel",
        "imie": "Szmul",
        "przydomek": "",
        "funkcja": "Kupiec starozakonny / Pożyczkodawca miejski",
        "miejsce": "Dzielnica żydowska / Kraśnik",
        "skany_roboczo": "#95",
        "skany_list": [95],
        "zakres_lat": "1775",
        "min_rok": 1775,
        "max_rok": 1775,
        "liczba_wystapien": 1,
        "wystapienia": [
            {
                "nazwisko": "Zeywel",
                "imie": "Szmul",
                "miejsce": "Kraśnik",
                "rola": "Kupiec starozakonny / Pożyczkodawca kasy miejskiej",
                "skan": 95,
                "rok": "1775",
                "zapis_oryginalny": "Starozakonnemu Szmulowi Zeywelowi",
                "kwota_ctx": "72 zł gotówką"
            }
        ],
        "uwagi": "Kupiec starozakonny kraśnicki, pożyczył miastu gotówką 72 zł na nagłe wydatki publiczne, zatwierdzone dekretem Kochowskiego."
    },
    {
        "lp": 738,
        "nazwisko": "Kozłowicz",
        "wariant_nazwiska": "Kozłowicz / Kozłowic",
        "imie": "Jakub",
        "przydomek": "",
        "funkcja": "Przeszły woźny miejski",
        "miejsce": "Kraśnik",
        "skany_roboczo": "#96, #97",
        "skany_list": [96, 97],
        "zakres_lat": "1775",
        "min_rok": 1775,
        "max_rok": 1775,
        "liczba_wystapien": 2,
        "wystapienia": [
            {
                "nazwisko": "Kozłowicz",
                "imie": "Jakub",
                "miejsce": "Kraśnik",
                "rola": "Były woźny miejski",
                "skan": 96,
                "rok": "1775",
                "zapis_oryginalny": "Jakub Kozłowicz przeszły Woźny Mieyski",
                "kwota_ctx": "Kożuch za wierne usługi"
            },
            {
                "nazwisko": "Kozłowicz",
                "imie": "Jakub",
                "miejsce": "Kraśnik",
                "rola": "Były woźny miejski (dublet)",
                "skan": 97,
                "rok": "1775",
                "zapis_oryginalny": "Jakub Kozłowicz przeszły Woźny Mieyski",
                "kwota_ctx": "Kożuch sukienny"
            }
        ],
        "uwagi": "Wieloletni wierny woźny miejski Kraśnika, któremu dekretem Antoniego Kochowskiego przyznano zaległy kożuch służbowy w nagrodę za posługi."
    },
    {
        "lp": 739,
        "nazwisko": "Fruzyński",
        "wariant_nazwiska": "Fruzynsky / Fruziński",
        "imie": "Paweł",
        "przydomek": "",
        "funkcja": "Cechmistrz starszy tkacki 1775 / Posesjonat",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#98, #102, #103",
        "skany_list": [98, 102, 103],
        "zakres_lat": "1775–1776",
        "min_rok": 1775,
        "max_rok": 1776,
        "liczba_wystapien": 3,
        "wystapienia": [
            {
                "nazwisko": "Fruzyński",
                "imie": "Paweł",
                "miejsce": "Śródmieście",
                "rola": "Posesjonat (dom Maciejowej Fruzyny)",
                "skan": 98,
                "rok": "1775",
                "zapis_oryginalny": "Maciejowa Fruzyna",
                "kwota_ctx": "4 gr."
            },
            {
                "nazwisko": "Fruzyński",
                "imie": "Paweł",
                "miejsce": "Kraśnik",
                "rola": "Cechmistrz starszy cechu tkackiego",
                "skan": 102,
                "rok": "1775",
                "zapis_oryginalny": "Sl: Paweł Fruzynsky Cechmistrz starszy",
                "kwota_ctx": "Elekcja cechowa 1775"
            },
            {
                "nazwisko": "Fruzyński",
                "imie": "Paweł",
                "miejsce": "Śródmieście",
                "rola": "Posesjonat",
                "skan": 103,
                "rok": "1776",
                "zapis_oryginalny": "Fruzyna Wda",
                "kwota_ctx": "24 gr."
            }
        ],
        "uwagi": "Cechmistrz starszy cechu tkackiego w Kraśniku obrany w grudniu 1775 r. pod protekcją burgrabiego Kochowskiego."
    },
    {
        "lp": 740,
        "nazwisko": "Czapnik",
        "wariant_nazwiska": "Leyba Czapnik / Czapnik",
        "imie": "Leyba",
        "przydomek": "",
        "funkcja": "Podstarszy cechu kuśnierskiego (substitut) / Kuśnierz starozakonny",
        "miejsce": "Dzielnica żydowska / Kraśnik",
        "skany_roboczo": "#102",
        "skany_list": [102],
        "zakres_lat": "1775",
        "min_rok": 1775,
        "max_rok": 1775,
        "liczba_wystapien": 1,
        "wystapienia": [
            {
                "nazwisko": "Czapnik",
                "imie": "Leyba",
                "miejsce": "Kraśnik",
                "rola": "Podstarszy cechu kuśnierskiego (substitut wtóry)",
                "skan": 102,
                "rok": "1775",
                "zapis_oryginalny": "Subst: Niewier: Leyba Czapnik wtóry",
                "kwota_ctx": "Elekcja cechowa 1775"
            }
        ],
        "uwagi": "Rzemieślnik starozakonny (czapnik/kuśnierz), powołany na substytuta wtórego (podstarszego) cechu kuśnierskiego w Kraśniku w grudniu 1775 r."
    },
    {
        "lp": 741,
        "nazwisko": "Gołębiowska",
        "wariant_nazwiska": "Brzozowska 1mo voto / Gołembiewska / Gołębiowska",
        "imie": "",
        "przydomek": "",
        "funkcja": "Mieszkanka / Wdowa po pisarzu miejskim",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#95",
        "skany_list": [95],
        "zakres_lat": "1775",
        "min_rok": 1775,
        "max_rok": 1775,
        "liczba_wystapien": 1,
        "wystapienia": [
            {
                "nazwisko": "Gołębiowska",
                "imie": "",
                "miejsce": "Śródmieście",
                "rola": "Wdowa po pisarzu miejskim Brzozowskim",
                "skan": 95,
                "rok": "1775",
                "zapis_oryginalny": "Jmć Brzozofskiey 1mo voto, a teraznieyszey Gołembiewskiey",
                "kwota_ctx": "30 zł za zasługi pierwszego męża"
            }
        ],
        "uwagi": "Mieszkanka kraśnicka, wdowa 1mo voto po pisarzu miejskim Brzozowskim, 2do voto za Gołębiowskim; przyznano jej 30 zł zaległych zasług pisarskich pierwszego męża."
    },
    {
        "lp": 742,
        "nazwisko": "Posoniak",
        "wariant_nazwiska": "Pasoniak? / Posoniak",
        "imie": "Stanisław",
        "przydomek": "",
        "funkcja": "Cechmistrz starszy szewski 1775 / Niedoszły ławnik miejski / Posesjonat",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#98, #99, #102, #103",
        "skany_list": [98, 99, 102, 103],
        "zakres_lat": "1775–1776",
        "min_rok": 1775,
        "max_rok": 1776,
        "liczba_wystapien": 4,
        "wystapienia": [
            {
                "nazwisko": "Posoniak",
                "imie": "Stanisław",
                "miejsce": "Śródmieście",
                "rola": "Posesjonat",
                "skan": 98,
                "rok": "1775",
                "zapis_oryginalny": "Stanisław Pasoniak",
                "kwota_ctx": "8 gr."
            },
            {
                "nazwisko": "Posoniak",
                "imie": "Stanisław",
                "miejsce": "Śródmieście",
                "rola": "Posesjonat",
                "skan": 99,
                "rok": "1775",
                "zapis_oryginalny": "Stanisław Pasoniak",
                "kwota_ctx": "8 gr."
            },
            {
                "nazwisko": "Posoniak",
                "imie": "Stanisław",
                "miejsce": "Kraśnik",
                "rola": "Cechmistrz major szewski / Zdyskwalifikowany ławnik",
                "skan": 102,
                "rok": "1775",
                "zapis_oryginalny": "Sl: Stanisław Posoniak Cechmistrz Mjor",
                "kwota_ctx": "Dyskwalifikacja z ławicy za obrazę deputacji"
            },
            {
                "nazwisko": "Posoniak",
                "imie": "Stanisław",
                "miejsce": "Śródmieście",
                "rola": "Posesjonat",
                "skan": 103,
                "rok": "1776",
                "zapis_oryginalny": "Stanisł: Posoniak",
                "kwota_ctx": "1 zł 18 gr."
            }
        ],
        "uwagi": "Starszy cechu szewskiego (Cechmistrz Major); obrany ławnikiem w grudniu 1775 r., lecz wykluczony po skandalu publicznym za przeklinanie deputacji miejskiej ('że In Publico Deputacyą Dyabłom oddawał')."
    },
    {
        "lp": 743,
        "nazwisko": "Pilaszek",
        "wariant_nazwiska": "Pielaszek? / Pilaszek",
        "imie": "Grzegorz",
        "przydomek": "",
        "funkcja": "Były szafarz miejski / Posesjonat",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#95",
        "skany_list": [95],
        "zakres_lat": "1775",
        "min_rok": 1775,
        "max_rok": 1775,
        "liczba_wystapien": 1,
        "wystapienia": [
            {
                "nazwisko": "Pilaszek",
                "imie": "Grzegorz",
                "miejsce": "Śródmieście",
                "rola": "Były szafarz miejski",
                "skan": 95,
                "rok": "1775",
                "zapis_oryginalny": "Sł: Grzegorzowi Pilaszkowi Szafarzowi Mieyskiemu",
                "kwota_ctx": "70 zł nagrody za wierną służbę"
            }
        ],
        "uwagi": "Szafarz miejski kraśnicki, któremu komisarz Kochowski przyznał 70 zł w nagrodę za wierne i poczciwe posługi dla kasy miejskiej."
    },
    {
        "lp": 744,
        "nazwisko": "Deryło",
        "wariant_nazwiska": "Deuyło? / Deryło",
        "imie": "Kazimierz",
        "przydomek": "",
        "funkcja": "Posesjonat / Przedmieszczanin",
        "miejsce": "Zarzecze",
        "skany_roboczo": "#101, #105",
        "skany_list": [101, 105],
        "zakres_lat": "1775–1776",
        "min_rok": 1775,
        "max_rok": 1776,
        "liczba_wystapien": 2,
        "wystapienia": [
            {
                "nazwisko": "Deryło",
                "imie": "Kazimierz",
                "miejsce": "Zarzecze",
                "rola": "Płatnik sympli",
                "skan": 101,
                "rok": "1775",
                "zapis_oryginalny": "Kazimierz Deryło [Deuyło?]",
                "kwota_ctx": "8 gr."
            },
            {
                "nazwisko": "Deryło",
                "imie": "Kazimierz",
                "miejsce": "Zarzecze",
                "rola": "Płatnik 8 sympli",
                "skan": 105,
                "rok": "1776",
                "zapis_oryginalny": "Kz: Deryło",
                "kwota_ctx": "1 zł 10 gr."
            }
        ],
        "uwagi": "Gospodarz i posesjonat przedmieścia Zarzyce (zapisywany Deuyło / Deryło)."
    },
    {
        "lp": 745,
        "nazwisko": "Gęzarek",
        "wariant_nazwiska": "Gęzarch? / Gęzarek? / Warsz: Gęzarek",
        "imie": "Wawrzyniec",
        "przydomek": "",
        "funkcja": "Posesjonat / Przedmieszczanin",
        "miejsce": "Zarzecze",
        "skany_roboczo": "#101, #105",
        "skany_list": [101, 105],
        "zakres_lat": "1775–1776",
        "min_rok": 1775,
        "max_rok": 1776,
        "liczba_wystapien": 2,
        "wystapienia": [
            {
                "nazwisko": "Gęzarek",
                "imie": "Wawrzyniec",
                "miejsce": "Zarzecze",
                "rola": "Płatnik sympli",
                "skan": 101,
                "rok": "1775",
                "zapis_oryginalny": "Wawrzyniec Gęzarek [Gęzarch?]",
                "kwota_ctx": "12 gr."
            },
            {
                "nazwisko": "Gęzarek",
                "imie": "Wawrzyniec",
                "miejsce": "Zarzecze",
                "rola": "Płatnik 8 sympli",
                "skan": 105,
                "rok": "1776",
                "zapis_oryginalny": "Warsz: Gęzarek",
                "kwota_ctx": "2 zł 12 gr."
            }
        ],
        "uwagi": "Gospodarz przedmieścia Zarzyce (zapisywany Wawrzyniec Gęzarek / Gęzarch / Warsz: Gęzarek)."
    },
    {
        "lp": 746,
        "nazwisko": "Oszowski",
        "wariant_nazwiska": "Aszoski? / Okposki? / Oszowski",
        "imie": "Franciszek",
        "przydomek": "",
        "funkcja": "Posesjonat / Przedmieszczanin",
        "miejsce": "Piaski",
        "skany_roboczo": "#99, #104",
        "skany_list": [99, 104],
        "zakres_lat": "1775–1776",
        "min_rok": 1775,
        "max_rok": 1776,
        "liczba_wystapien": 2,
        "wystapienia": [
            {
                "nazwisko": "Oszowski",
                "imie": "Franciszek",
                "miejsce": "Piaski",
                "rola": "Płatnik sympli",
                "skan": 99,
                "rok": "1775",
                "zapis_oryginalny": "Franciszek Aszoski",
                "kwota_ctx": "6 gr."
            },
            {
                "nazwisko": "Oszowski",
                "imie": "Franciszek",
                "miejsce": "Piaski",
                "rola": "Płatnik 8 sympli",
                "skan": 104,
                "rok": "1776",
                "zapis_oryginalny": "Franc: Okposki [Oszoski?]",
                "kwota_ctx": "1 zł 6 gr."
            }
        ],
        "uwagi": "Gospodarz przedmieścia Piasek (zapisywany Aszoski / Okposki / Oszowski)."
    },
    {
        "lp": 747,
        "nazwisko": "Sadowska",
        "wariant_nazwiska": "Sadoftka? / Sadowska",
        "imie": "Petronela",
        "przydomek": "",
        "funkcja": "Mieszkanka / Posesjonatka",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#98, #103",
        "skany_list": [98, 103],
        "zakres_lat": "1775–1776",
        "min_rok": 1775,
        "max_rok": 1776,
        "liczba_wystapien": 2,
        "wystapienia": [
            {
                "nazwisko": "Sadowska",
                "imie": "Petronela",
                "miejsce": "Śródmieście",
                "rola": "Posesjonatka",
                "skan": 98,
                "rok": "1775",
                "zapis_oryginalny": "Petronella Sadoftka",
                "kwota_ctx": "10 gr."
            },
            {
                "nazwisko": "Sadowska",
                "imie": "Petronela",
                "miejsce": "Śródmieście",
                "rola": "Posesjonatka",
                "skan": 103,
                "rok": "1776",
                "zapis_oryginalny": "Petronella Sadowska",
                "kwota_ctx": "2 zł."
            }
        ],
        "uwagi": "Posesjonatka w centrum Kraśnika (zapisywana Petronella Sadoftka / Sadowska)."
    },
    {
        "lp": 748,
        "nazwisko": "Stembowski",
        "wariant_nazwiska": "Stemborfki? / Stembowski",
        "imie": "Józef",
        "przydomek": "",
        "funkcja": "Mieszkaniec / Posesjonat",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#98, #103",
        "skany_list": [98, 103],
        "zakres_lat": "1775–1776",
        "min_rok": 1775,
        "max_rok": 1776,
        "liczba_wystapien": 2,
        "wystapienia": [
            {
                "nazwisko": "Stembowski",
                "imie": "Józef",
                "miejsce": "Śródmieście",
                "rola": "Posesjonat",
                "skan": 98,
                "rok": "1775",
                "zapis_oryginalny": "Jozef Stemborfki",
                "kwota_ctx": "16 gr."
            },
            {
                "nazwisko": "Stembowski",
                "imie": "Józef",
                "miejsce": "Śródmieście",
                "rola": "Posesjonat",
                "skan": 103,
                "rok": "1776",
                "zapis_oryginalny": "Jozef Stembowski",
                "kwota_ctx": "3 zł 6 gr."
            }
        ],
        "uwagi": "Posesjonat w centrum Kraśnika (zapisywany Stemborfki / Stembowski)."
    },
    {
        "lp": 749,
        "nazwisko": "Szpiciarz",
        "wariant_nazwiska": "Szpiciarzk? / Szpiciarz",
        "imie": "Józef",
        "przydomek": "",
        "funkcja": "Mieszkaniec / Posesjonat",
        "miejsce": "Śródmieście",
        "skany_roboczo": "#104",
        "skany_list": [104],
        "zakres_lat": "1776",
        "min_rok": 1776,
        "max_rok": 1776,
        "liczba_wystapien": 1,
        "wystapienia": [
            {
                "nazwisko": "Szpiciarz",
                "imie": "Józef",
                "miejsce": "Śródmieście",
                "rola": "Posesjonat",
                "skan": 104,
                "rok": "1776",
                "zapis_oryginalny": "Jozef Szpiciarzk",
                "kwota_ctx": "—"
            }
        ],
        "uwagi": "Mieszkaniec i posesjonat śródmiejski (zapisywany Szpiciarzk)."
    },
    {
        "lp": 750,
        "nazwisko": "Chruściel",
        "wariant_nazwiska": "Chruściel / Chrusciel",
        "imie": "Maciej",
        "przydomek": "",
        "funkcja": "Przedmieszczanin / Posesjonat",
        "miejsce": "Zarzecze",
        "skany_roboczo": "#101, #105",
        "skany_list": [101, 105],
        "zakres_lat": "1775–1776",
        "min_rok": 1775,
        "max_rok": 1776,
        "liczba_wystapien": 2,
        "wystapienia": [
            {
                "nazwisko": "Chruściel",
                "imie": "Maciej",
                "miejsce": "Zarzecze",
                "rola": "Płatnik sympli",
                "skan": 101,
                "rok": "1775",
                "zapis_oryginalny": "Maciy Chruściel",
                "kwota_ctx": "5 gr."
            },
            {
                "nazwisko": "Chruściel",
                "imie": "Maciej",
                "miejsce": "Zarzecze",
                "rola": "Płatnik 8 sympli",
                "skan": 105,
                "rok": "1776",
                "zapis_oryginalny": "Maciey Chruściel",
                "kwota_ctx": "1 zł 6 gr."
            }
        ],
        "uwagi": "Gospodarz i posesjonat na przedmieściu Zarzyce."
    }
]

# Dodanie nowych profili do gen_data
gen_data.extend(nowe_profile)
print(f"Dodano {len(nowe_profile)} nowych profili. genData ma teraz {len(gen_data)} rekordów.")

# -------------------------------------------------------------
# 3. Aktualizacja istniejących profili w genData o wystąpienia i warianty
# -------------------------------------------------------------

def update_profile(lp, add_scans, wariant_append, extra_role=None, extra_years=None):
    p = next((x for x in gen_data if x['lp'] == lp), None)
    if not p:
        print(f"OSTRZEŻENIE: brak profilu lp {lp}")
        return
    # skany
    cur_scans = set(p.get('skany_list', []))
    cur_scans.update(add_scans)
    p['skany_list'] = sorted(list(cur_scans))
    p['skany_roboczo'] = ", ".join(f"#{s}" for s in p['skany_list'])
    # wariant
    if wariant_append:
        cur_w = p.get('wariant_nazwiska', '') or ''
        if wariant_append.lower() not in cur_w.lower():
            if cur_w:
                p['wariant_nazwiska'] = f"{cur_w} / {wariant_append}"
            else:
                p['wariant_nazwiska'] = wariant_append
    # funkcja
    if extra_role:
        cur_f = p.get('funkcja', '')
        if extra_role.lower() not in cur_f.lower():
            p['funkcja'] = f"{cur_f} / {extra_role}"
    # lata
    if extra_years:
        p['zakres_lat'] = extra_years
        # update min_rok, max_rok
        years = [int(y) for y in re.findall(r'\b(17\d\d)\b', extra_years)]
        if years:
            p['min_rok'] = min(p.get('min_rok', min(years)), min(years))
            p['max_rok'] = max(p.get('max_rok', max(years)), max(years))

# Aktualizacje kluczowych postaci
update_profile(3, [101, 105], "Babiez? / Babiarz?", extra_years="1761–1776")
update_profile(44, [101, 105], "Bruś? / Bus? / Rus? / Rusz?", extra_years="1775–1776")
update_profile(67, [98, 103], "Czaplinski? / Czapliński? / Czapla", extra_years="1761–1776")
update_profile(152, [99, 104], "Jęczniak? / Jacznik?", extra_years="1761–1776")
update_profile(167, [98, 102, 103], "Jędencarz? / Jedencarz? / Jedenczarz", extra_role="Ławnik miejski (od 1775)", extra_years="1764–1776")
update_profile(198, [91, 92, 93, 94, 95, 96, 97, 101, 102], "Kochowski (Komisarz ordynacki)", extra_years="1775")
update_profile(286, [91, 92, 94, 95], "Madeyski / Madejski", extra_years="1769–1775")
update_profile(317, [98, 103], "Mulofski? / Muloski / Mudorski? / Mudowski?", extra_years="1775–1778")
update_profile(441, [98, 103], "Byzik? / Pyzik?", extra_years="1761–1776")
update_profile(480, [98, 102, 103], "Rycerz", extra_role="Cechmistrz kowalski starszy 1775", extra_years="1761–1776")
update_profile(481, [98, 102, 103], "Rycerz Ławnik", extra_role="Ławnik miejski 1775", extra_years="1761–1776")
update_profile(494, [98, 103], "Sadofski? / Sadowski", extra_years="1761–1776")
update_profile(510, [95], "Suliciński (Były szafarz 1775)", extra_years="1764–1775")
update_profile(516, [98, 103], "Szafrancka? / Szafrański", extra_years="1761–1776")
update_profile(527, [94, 98, 103], "Szultz? / Szulik? / Szulc", extra_years="1775–1778")
update_profile(544, [98, 103], "Tokarski (Wójt 1775–1776)", extra_role="Wójt kraśnicki 1775–1776", extra_years="1761–1776")
update_profile(649, [98, 102, 103], "Zdyb / Zdybicki?", extra_role="Cechmistrz kuśnierski starszy 1775", extra_years="1761–1776")
update_profile(664, [99, 104], "Ćwicha? / Cwiecha? / Cwicha? / Ćwieka", extra_years="1761–1776")
update_profile(710, [98, 103], "Dybicki? / Dybiecki / Zdybicki?", extra_years="1772–1776")
update_profile(729, [101, 105], "Bielak? / Bielach / Pielach?", extra_years="1772–1776")
update_profile(730, [99, 104], "Polokowicz? / Połokowicz? / Potokowicz", extra_years="1772–1776")
update_profile(731, [98, 102, 103], "Połokowicz? / Potokowicz", extra_role="Cechmistrz tkacki młodszy 1775", extra_years="1772–1776")

print("Zaktualizowano profile istniejące w genData.")

# -------------------------------------------------------------
# 4. Zapis zaktualizowanych danych do pliku HTML
# -------------------------------------------------------------

# Formatowanie JSON
main_data_json = json.dumps(main_data, ensure_ascii=False, indent=2)
gen_data_json = json.dumps(gen_data, ensure_ascii=False, indent=2)

# Podmiana mainData
m_target_start = html_content.find('const mainData = [')
m_target_end = html_content.find('];', m_target_start) + 2
html_content = html_content[:m_target_start] + 'const mainData = ' + main_data_json + ';' + html_content[m_target_end:]

# Podmiana genData
g_target_start = html_content.find('const genData = [')
g_target_end = html_content.find('];', g_target_start) + 2
html_content = html_content[:g_target_start] + 'const genData = ' + gen_data_json + ';' + html_content[g_target_end:]

# Aktualizacja KPI w HTML
# Liczba zidentyfikowanych osób
html_content = re.sub(
    r'(<div[^>]*class="stat-val"[^>]*>)\s*733\s*(</div>)',
    r'\g<1>750\g<2>',
    html_content
)
html_content = re.sub(
    r'733 unikalnych osób',
    f'{len(gen_data)} unikalnych osób',
    html_content
)
html_content = re.sub(
    r'733 osób',
    f'{len(gen_data)} osób',
    html_content
)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Pomyślnie zaktualizowano plik HTML: {HTML_PATH}")

# -------------------------------------------------------------
# 5. Eksport do krasnik_j40_slownik_genealogiczny.csv
# -------------------------------------------------------------

fieldnames = [
    'lp', 'nazwisko', 'wariant_nazwiska', 'imie', 'przydomek',
    'funkcja', 'miejsce', 'skany_roboczo', 'zakres_lat',
    'liczba_wystapien', 'uwagi'
]

with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    for row in gen_data:
        writer.writerow(row)

print(f"Pomyślnie wyeksportowano {len(gen_data)} rekordów do CSV: {CSV_PATH}")
