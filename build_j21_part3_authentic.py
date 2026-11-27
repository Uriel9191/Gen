# -*- coding: utf-8 -*-
import json

with open("main_data_j21_part2.json", "r", encoding="utf-8") as f:
    main_data = json.load(f)

assert len(main_data) == 50, f"Oczekiwano 50 skanow, jest {len(main_data)}"

LINK_SWA = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/6989934"
SYGN = "35/40/0/1/21"

raw_scans = [
    (51, "fol. 24r (16 / 24)", "1671",
     "Finał dekretu A. Ablika vs T. Łążkowic (54 złp 20 gr); relacja obdukcji sługi G. Foxa; protestacja A. Toraieckiego [?] przeciw rajcy Sz. Wiązkowicowi",
     "Andrzej Ablik (Żyd), Tomasz Łążkowic, Grzegorz Fox (prokonsul), Ubald Florian Janaszkowicz (wójt), Wojciech Kurewic, Sebastian Balusik, Bartosz Kłopot, Jan Grot, Stanisław Reszka, Andrzej Toraiecki [Poraiecki?], Szymon Wiązkowic, Łukasz Pieniążek [?], Paweł Smarowic",
     "136 złp 26 gr, 54 złp 20 gr, 30 grzywien",
     "Dokończenie dekretu Żyda Andrzeja Ablika przeciw Tomaszowi Łążkowicowi (po rozliczeniu 136 złp 26 gr do spłaty pozostało 54 złp 20 gr); relacja ławników Wojciecha Kurewica i Sebastiana Balusika z ramienia wójta Ubalda Floriana Janaszkowica o obdukcji ran na łopatce i czole oraz szkodach u Bartosza Kłopota z instancji prokonsula Grzegorza Foxa (wzmiankowani Jan Grot i Stanisław Reszka); protestacja Andrzeja Toraieckiego [Poraieckiego?] przeciw rajcy Szymonowi Wiązkowicowi o wydanie ekstraktu kontraktu i 30 grzywien litkupu.",
     """[fol. 24r]
[...] wcale nie przyznaie, aby pozwany miał mu zapłacić y oddać dług zł 136 gr 26 dekretem nakazany; ale iż się pomienionym dekretem y cyrografem pozwanego zatrzymawszy jednak iż pozwany stawił świadki dwóch po sobie [...] gdzie Aktor przysięgą potwierdził że od sumy 136 złp 26 gr tylko 54 złp 20 gr do zapłaty zostało, co pozwany ma oddać.
Relatio Dnor. Scabinorum ex parte Fam. Greg. Fox Consulis.
Ad instantiam et affectationem Famati Dni Gregorii Fox Consulis pro tunc residentis ex brachio Dni Ubaldi Floriani Janaszkowicz Advocati Jurati Crasn. deputati duo fideles Famati Albertus Kurewic et Sebastianus Balusik Scabini Jurati retulerunt: Iż zjechaliśmy na rolę za ogrodem pod laskiem gdzie koń i wół były pobite, na grzbiecie i na łopatkach rany sine [...] u Bartosza Kłopota na drodze spotkany Jan Grot z Stanisławem Reszką zeznali o tym biciu [...]
Protestatio Wielus [?] contra Simonem Wiązkowic.
Ad Officium et Acta praesentia Advocatialia et Scabinalia Crasnicensia personaliter comparens Honestus Andreas Toraiecki [Poraiecki?] civis Crasnicensis protestatus est contra Famatum Simonem Wiązkowic consulem Crasn., iż prosząc od niego ekstraktu kontraktu kupna za który litkup 30 grzywien zapłacił, on przez Łukasza Pieniążka [?] wydać nie chciał i odmówił [...]"""),

    (52, "fol. 24v (16v / 24v)", "1671",
     "Kontumacja S. Nawrockiego; sesja 23 XI 1671 r.: M. Copałka vs S. Babiarzczyk; kwitacja J. Tatara dla S. Bieńka; sesja 27 XI 1671 r.: zeznanie Sz. Łapiguza dla W. Łazińskiego",
     "Stanisław Nawrocki, Matyjasz Bielaszkowic alias Ratuszny, Jan Kresowski (bedel), Marcin Copałka, Stanisław Babiarzczyk, Jakub Tatar (młynarz z Kiełczowic), Adam Drzewiecki, Stanisław Bieniek (ze Stróży), Ignacy Kołaczek [?], Wojciech Łaziński [Lagiński?] (młynarz), Szymon z Laskówki [?]",
     "3 dni wieży",
     "Pierwsza kontumacja Stanisława Nawrockiego z instancji Matyasza Bielaszkowica alias Ratusznego (relacja bedela Jana Kresowskiego); sesja z 23 XI 1671 r.: wyrok skazujący Stanisława Babiarzczyka na 3 dni wieży i zwrot kosztów za pobicie Marcina Copałki; uroczysta kwitacja pracowitego Jakuba Tatara młynarza z Kiełczowic (poddanego Adama Drzewieckiego) dla Stanisława Bieńka ze Stróży i Ignacego Kołaczka [?] po kompromisie z pobicia; sesja z 27 XI 1671 r.: zeznanie Szymona na rzecz młynarza Wojciecha Łazińskiego o bójce we młynie.",
     """[fol. 24v]
Contumacia Stan. Nawrocki ex parte Matthiae Ratuszny alias Bielaszkowic.
Famatus Stanislaus Nawrocki consul antiquus iuxta relationem Providi Joannis Kresowski Bedelli Jurati ex instantia Matthiae Bielaszkowic trina citatione non comparuit, condemnatur in primo termino.

Actum coram Offo Advocat. feria 2da ante festum S. Catharinae V. et Martyris prox[im]a Anno Dni 1671.
Decretum inter Martinum Copałka actorem et Stanislaum Babiarzczyk cittum.
In causa et actione judiciaria z okazania pobicia pozwanego przez aktora toczona [...] Sąd niniejszy nakazuje pozwanemu carceres ad tres dies subire, fideiubere i koszta prawne wrócić.
Jacobus Tatara de Kiełczowice Quietat Stan. Bieniek de Stroża.
Ad Officium et Acta praesentia Advocatialia et Scabinalia Crasnicensia personaliter veniens laboriosus Jacobus Tatara molitor de Kiełczowice subditus Gen. Dni Adami Drzewiecki sanus corpore et mente palam et benevole confessus est: Iż z Stanisławem Bieńkiem ze Stróży i Ignacym Kołaczkiem [?] pomocnikiem jego za kompromisem z obu stron zaspokojony jest i kwituje ich z pobicia i ran w obdukcyi opisanych.

Actum feria sexta ante festum Sancti Andreae Apostoli prox[im]a Anno Dni 1671.
Testimonium ex parte Alberti Lagiński [Łaziński?] molitoris.
Ad instantiam Alberti Łagiński molitoris testificatus est laboriosus Simon de Laskówka [?] iuratus: Byłem natenczas we młynie kiedy gospodarz z żoną swarzyli się o mieszkanie, a Piotr Lisowski [?] zaczął bić i gonić pod skrzynkę [...]"""),

    (53, "fol. 25r (17 / 25)", "1671",
     "Zeznanie Matyasza z Blinowa; przysięga P. Nowaczka z Suchyni; wielki wyrok 100 grzywien vadium M. Bielaszkowica vs S. Nawrocki; S. Nawrocki vs S. Berecki",
     "Matyjasz (z Blinowa), Paweł Nowaczek (z Suchyni), Matyjasz Bielaszkowic alias Ratuszny, Stanisław Nawrocki, Marianna Nawrocka, Marcin Copałka, Stanisław Babiarzczyk, Stanisław Berecki, Szymon Wiązkowic",
     "100 grzywien, 30 grzywien, 20 złp, 5 grzywien",
     "Zeznanie 2. świadka Matyasza z Blinowa dla W. Łazińskiego; przysięga pracowitego Pawła Nowaczka z Suchyni; wielki łacińsko-polski wyrok w procesie Matyasza Bielaszkowica alias Ratusznego przeciw Stanisławowi Nawrockiemu i jego żonie za publiczne zelżenie w kościele i na rynku (kara 30 grzywien po połowie na kościół parafialny i szpital św. Ducha, 4 tygodnie aresztu domowego oraz 100 grzywien vadium na przyszłość!); dekret w sprawie Marcina Copałki vs Stanisław Babiarzczyk; sprawa Stanisława Nawrockiego przeciw Stanisławowi Bereckiemu o kradzież 20 złp, 5 żelaz płużnych i barana (poręczenie rajcy Szymona Wiązkowica).",
     """[fol. 25r]
2dus Testis Matyjasz z Blinowa ad idem Officium accedens iuratus także słowo w słowo jako pierwszy świadek zeznał.
Juramentum Pauli Nowaczek de Suchynia indultum.
Na terminie dzisiejszym stanąwszy oblicznie pracowity Paweł Nowaczek z Suchyni według dekretu JM P. Dzierżawcy gotów był przysięgę wykonać [...]
Decretum inter Matthiam Bielaszkowic ex parte una et Stan. Nawrocki coniuges ex altera cum interpositione vadii marcarum 100.
In termino hodierno [...] Judicium praesens Advocatiale et Scabinale obu stron przesłuchawszy, zważywszy sławne obelgi przez małżonkę pozwanego rzucane publicznie tak w kościele jako i przed domem na osobę aktora i jego żonę [...] skazani są na karę 30 grzywien (medietas ad templum parochiale et altera ad xenodochium S. Spiritus), areszt domowy przez 4 tygodnie i vadium 100 grzywien między stronami założone.
Inter Martinum Copałka Actorem et Stan. Babiarzczyk cittum.
Vigore praesentis decreti demandatum est aby według kompromisu 5 grzywien i przeprosiny odbyły się, a do wieży na 2 dni za nieposłuszeństwo.
Inter Stan. Nawrocki Actorem et Stan. Berecki inculpatum.
Skarżył się aktor na obwinionego że mu w drodze zł 20 ukradł y żelaza płużne 5 y barana zabił [...] pozwany broniąc się prosił o dylacyą przy rękojemstwie Sławetnego Szymona Wiązkowica Rajcy Kraśnickiego [...]"""),

    (54, "fol. 25v (17v / 25v)", "1671",
     "Poręczenie Sz. Wiązkowica za S. Bereckiego; G. Stryczkowski vs M. Kalwa o młot; wyrok Z. Kowalikówny vs W. Kowalik; A. Ablik vs T. Łążkowic (80 złp); obdukcja S. Bereckiego",
     "Szymon Wiązkowic, Stanisław Berecki, Stanisław Nawrocki, Grzegorz Stryczkowski, Marcin Kalwa, Matyjasz Bielaszkowic alias Ratuszny, Zofia Kowalikówna, Wawrzyniec Kowalik, Andrzej Ablik (Żyd), Tomasz Łążkowic (kuśnierz)",
     "10 grzywien, 80 złp, 40 złp",
     "Dokończenie poręczenia rajcy Szymona Wiązkowica za Stanisława Bereckiego; proces Grzegorza Stryczkowica przeciw Marcinowi Kalwie o kradzież młota i żelaza kowalskiego z kłódką; dekret uwalniający Wawrzyńca Kowalika w sporze ze spadkobierczynią Zofią Kowalikówną; dobrowolna submisja kuśnierza Tomasza Łążkowica na spłatę 80 złp Żydowi Andrzejowi Ablikowi w dwóch ratach po 40 złp (w Opolu i Sandomierzu w 1672 r.); początek obdukcji ran Stanisława Bereckiego pobitego przez S. Nawrockiego.",
     """[fol. 25v]
[...] Wiązkowic bierze obwinionego na swą porękę, co jeśli na terminie nie stanie, winy 10 grzywien ma zapłacić [...]
Inter Gregorium Stryczkowski Actorem et Martinum Kalwa inculpatum.
Skarżył się aktor na obwinionego że mu pokradł młot y żelaza kowalskie y kłódkę z kuźni, przy czym Matyjasz Ratuszny zaświadczył o kłótni [...] Sąd nakazuje przysięgę oczyszczającą pozwanemu.
Inter Zophiam Kowalikówna viduam et Tutores eius Actores et Laurentium Kowalik cittum Decretum.
W sprawie i akcyi sądowej przez aktorkę o dziesięć kóp z pozostałości po zmarłym bracie Bartoszu Kowaliku [...] Sąd uwalnia pozwanego od impetycyi aktorki, nakładając wieczne milczenie.
Inter Andream Ablik Judaeum Actorem et Thomam Łążkowic pellionem cittum Submissio ultronea.
Na terminie dzisiejszym w sprawie z Żydem Andrzejem Ablikiem o dług pozostały 80 złp Tomasz Łążkowic kuśnierz dobrowolnie poddał się zapłacić w dwóch ratach po 40 złp na jarmarkach w Opolu i w Sandomierzu w roku 1672.
Visio vulnerum Stanislai Berecki.
Ad instantiam et affectationem Dni Simonis Wiązkowic Consulis Crasn. pro famulo suo Stanislao Berecki ex brachio Officii obdukcja ran zadanych przez Stanisława Nawrockiego na rękach i głowie [...]"""),

    (55, "fol. 26r (18 / 26)", "1671",
     "Dokończenie obdukcji S. Bereckiego; sesja 2 XII 1671 r. (S. Nawrocki vs S. Berecki); sesja 7 XII 1671 r. (A. Pieniążek vs P. Dzierżek i A. Cieślina); sesja 11 XII 1671 r.",
     "Stanisław Berecki, Stanisław Nawrocki, Szymon Wiązkowic, Andrzej Pieniążek (ślusarz), Piotr Dzierżek, Agnieszka Cieślina, Wojciech Cieśla",
     "-",
     "Dokończenie obdukcji ran Stanisława Bereckiego (pobity powrozami i kolanami, wybite zęby); sesja z 2 XII 1671 r.: odroczenie procesu Stanisława Nawrockiego przeciw Stanisławowi Bereckiemu o kradzież w drodze sokalskiej; sesja z 7 XII 1671 r.: sprawa ślusarza Andrzeja Pieniążka przeciw szlachetnemu Piotrowi Dzierżkowi o dług oraz wyrok przeciw Agnieszce żonie Wojciecha Cieśli; sesja z 11 XII 1671 r.: początek rozprawy ostatecznej S. Nawrocki vs S. Berecki.",
     """[fol. 26r]
[...] zapuchłe y sine, od wiązania powronkami, od czego ręka w łokciu we dwoie pokrwawiona i zęby wybite [...]
Actum feria quarta ante festum Sancti Xaverii Indiarum Apostoli prox[im]a Anno Dni 1671.
Inter Stanislaum Nawrocki Actorem et Stanislaum Berecki cittum Dilatio ad respondendum.
In termino hodierno ex dilatione et prorogatione termini incidenti w sprawie sądowej między Sławetnym Stanisławem Nawrockim a pracowitym Stanisławem Bereckim sługą Pana Szymona Wiązkowica o zadanie złodziejstwa w drodze sokalskiej [...] Sąd pozwala dylacyi na dwie niedziele.

Actum feria secunda ante festum Conceptionis Beatae Mariae Virginis prox[im]a Anno 1671.
Inter Andream Pieniążek ferrifabrum Actorem et Petrum Dzierżek cittum Dilatio.
W sprawie i akcyi między Andrzejem Pieniążkiem a Szlachetnym Piotrem Dzierżkiem o dług pewny z zapisu dawnego [...] Sąd pozwala dylacyi do niedziel dwóch.
Inter eundem Andr. Pieniążek Actorem et Agnetem Alberti Cieśla consortem cittam.
Sąd nakazuje aby pozwana w ciągu tygodnia dług aktorowi zapłaciła.

Actum feria sexta post Dnicam 2dam Adventus Dni prox[im]a Anno Dni Millesimo Sexcentesimo Septuagesimo Primo.
Inter Stanislaum Nawrocki Actorem et Stanislaum Berecki inculpatum [...]"""),

    (56, "fol. 26v (18v / 26v)", "1671",
     "Wyrok uwalniający S. Bereckiego (11 XII 1671); protestacja Żyda A. Ablika przeciw T. Łążkowicowi (jarmark urzędowski); sesja 14 XII 1671 r. (nakaz wieży Baba)",
     "Stanisław Nawrocki, Stanisław Berecki, Szymon Wiązkowic, Andrzej Ablik (Żyd), Tomasz Łążkowic (kuśnierz)",
     "40 złp, 6 złp",
     "Ciąg dalszy dekretu w sprawie Stanisława Nawrockiego przeciw komornikowi/słudze Stanisławowi Bereckiemu (nakaz przysięgi oczyszczającej wraz z gospodarzem rajcą Szymonem Wiązkowicem i uwolnienie od zarzutów); protestacja Żyda Andrzeja Ablika przeciw kuśnierzowi Tomaszowi Łążkowicowi o niezapłacenie 40 złp na jarmarku w Urzędowie; sesja z 14 XII 1671 r.: dekret skazujący Tomasza Łążkowica na osadzenie w wieży Baba za dług Żyda Ablika.",
     """[fol. 26v]
[...] z jednej strony a pracowitym Stanisławem Bereckim komornikiem Pana Szymona Wiązkowica Rajcy Kraśnickiego z drugiej strony o zadanie złodziejstwa [...] ponieważ aktor żadnych jasnych dowodów przeciw obwinionemu nie pokazał, Sąd niniejszy nakazuje aby pozwany przysięgą cielesną w obecności Pana Szymona Wiązkowica oczyścił się iż ani pieniędzy ani skór ani żelaza nie brał, po której przysiędze wolnym będzie, a aktor koszta wrócić powinien.
Andrzej Ablik Judaeus contra Thomam Łążkowic pellionem protestatur.
Ad Officium et Acta praesentia Advocatialia et Scabinalia Crasnicensia veniens Perfidus Andrzej Judaeus incola Crasn. protestatus est contra Thomam Łążkowic pellionem civem Crasn., iż według submissyi na jarmarku urzędowskim miał oddać zł 40, a nie oddał i w terminie uchybił [...]

Actum Crasnicii coram Officio Advocatiali et Scabinali feria secunda post Dnicam Tertiam Adventus Dni prox[im]a Anno D. 1671.
Decretum inter Andrzej Ablik Judaeum Actorem et Thomam Łążkowic cittum.
Ponieważ pozwany według swej submissyi aktorowi na pierwszym jarmarku w Urzędowie zł 40 zapłacić uchybił [...] Sąd nakazuje aby poszedł w wieżę zwaną Baba aż do zapłacenia."""),

    (57, "fol. 27r (19 / 27)", "1671",
     "Bractwo Różańcowe vs G. Szadzik; zeznania starszych kahału Kopla i Heliasza Korzennika dla J. Grzebuskiego (pas srebrny); W. Pilchowski vs P. Słonkowski; przysięga S. Bereckiego (18 XII 1671)",
     "Tomasz Łążkowic, Andrzej Ablik, Grzegorz Szadzik, Kopel (starszy synagogi), Heliasz Korzennik (Żyd), Jan Grzebuski (organista), Tomasz Giedel [?], Wojciech Pilchowski, Paweł Słonkowski [Słomkowski], Marcin Dużyk [?], Stanisław Berecki, Szymon Wiązkowic",
     "40 złp, 30 złp",
     "Dokończenie dekretu T. Łążkowica (40 złp); nakaz spłaty długu Bractwu Różańcowemu przez Grzegorza Szadzika do roku 1672; zeznanie starszych żydowskich Kopla i Heliasza Korzennika dla organisty kraśnickiego Jana Grzebuskiego o sprzedaży pasa srebrnego białogłowskiego za 30 złp od Tomasza Giedela [?] z Dzierzkowic; dekret uwalniający Pawła Słonkowskiego [Słomkowskiego] od pozwu Wojciecha Pilchowskiego; kontumacja Marcina Dużyka z instancji Heliasza Korzennika; sesja z 18 XII 1671 r.: złożenie przysięgi przez Stanisława Bereckiego.",
     """[fol. 27r]
[...] fideiubere jako aktorowi ad dies tres bez żadnej dylacyi te 40 złp odliczy y odda.
Inter Procuratores SSmi Rosarii Actores et Gregorium Szadzik cittum.
Vigore praesentis decreti demandatum est aby pozwany jako przyrzekł na Nowy Targ kupnem otrzymał, do Bractwa Różańca Św. zapłacił [...] pod winą 1672.
Testimonii depositio pro parte Joannis Grebuski [Grzebuski] Organarii Crasnicensis.
Przed Urzędem Wóytowskim y Ławniczym Kraśnickim oblicznie stanąwszy Niewierni Żydzi Kopel starszy żydowski i Heliasz Korzennik starsi zboru kraśnickiego zeznali pod przysięgą żydowską Zakonu Mojżeszowego w te słowa: Iż przyszedszy do Krakowa [Kraśnika] Tomasz Giedel [?] przedmieścianin dzierzkowski i pas swój przedając nam, ten pas srebrny białogłowski staroświeckiej roboty za 30 złotych polskich [...] a przedtym w Urzędowie na jarmarku Heliasz Korzennik Żyd widział go y Kopel kupił ten pas monetą dobrą [...] na instancyą P. Jana Grzebuskiego organisty kraśnickiego.
Inter Albertum Pilchowski Actorem et Paulum Słonkowski cittum.
Ponieważ aktor żadnego świadectwa ani dokumentu nie stawił [...] Sąd uwalnia pozwanego od impetycyi aktora.
Martinus Dużyk [?] ex parte Perfidi Heliae Korzennik contumax.
Actum Coram Offo Advocat. et Scabin. feria sexta ante Dnicam Quartam Adventus prox[im]a Anno Dni 1671.
Juramentum Stanislai Berecki praestitum.
In termino hodierno ex decreto lato Stanislaus Berecki famulus Simoni Wiązkowic Consulis iuramentum corporale praestitit [...]"""),

    (58, "fol. 27v (19v / 27v)", "1671",
     "Sesja 23 XII 1671 r.: W. Pilchowski vs P. Słonkowski; A. Pieniążek vs P. Dzierżek (dekret z 1656 r.); wzajemne protestacje S. Nawrockiego i M. Bielaszkowica",
     "Stanisław Berecki, Stanisław Nawrocki, Wojciech Pilchowski, Paweł Słonkowski [Słomkowski], Andrzej Pieniążek, Piotr Dzierżek, Matyjasz Bielaszkowic, Jan Zan",
     "70 złp",
     "Dokończenie aktu przysięgi Stanisława Bereckiego; sesja z środy po 4. Niedzieli Adwentu (23 XII 1671 r.): odroczenie sprawy Wojciecha Pilchowskiego vs Paweł Słonkowski; sprawa ślusarza Andrzeja Pieniążka przeciw szlachetnemu Piotrowi Dzierżkowi (wzmianka o dawnym dekrecie z 1656 r., odłożona na rok 1672 oraz skarga na pobicie w domu Kurewica); wzajemne protestacje Stanisława Nawrockiego i Matyasza Bielaszkowica o niedotrzymanie kompromisu z udziałem dzierżawcy Jana Zana (70 złp).",
     """[fol. 27v]
[...] occasionem aliarum rerum furto ablatarum, ob quam a Stanislao Nawrocki inculpatus erat [...] i Sąd go wolnym czyni.
Actum feria quarta post Dominicam Quartam Adventus Dni prox[im]a Anno Dni 1671.
Inter Albertum Pilchowski Actorem et Paulum Słonkowski [Słomkowski] cittum.
In termino hodierno ex prorogatione termini incidenti [...] Sąd nakazuje aby pozwany przysięgą się oczyścił iż nic nie winien aktorowi.
Inter Andream Pieniążek Actorem et Petrum Dzierżek cittum.
Ponieważ pozwany na terminie dzisiejszym z dylacyi przypadłym nie stawił się do długu którego z dekretu ferowanego in Anno 1656 okazał, Sąd przekłada na rok następny 1672; a tymczasem aktor skarży się o pobicie w domu Kurewica przez przyjaciół pozwanego.
Stanislaus Nawrocki protestatur contra Matthiam Bielaszkowic.
Ad Officium praesentis Advocatialis et Scabinalis veniens Stan. Nawrocki protestatus est contra Matthiam Bielaszkowic, iż według kompromisu do rąk jego nie zapłacił.
Matthias Bielaszkowic Reprotestatur contra Stan. Nawrocki.
In facie eiusdem Officii stans Matthias Bielaszkowic reprotestatus est contra Stan. Nawrocki, iż przy kompromisie przed P. Janem Zanem miał złożyć 70 złp, ale Nawrocki nie przyjął i zwłóczył [...]
Albertus Pilchowski liquifactor, Paulo Słonkowski indulget iuramentum."""),

    (59, "fol. 28r (20 / 28)", "1672",
     "Otwarcie roku 1672 (12 I 1672): sprzedaż domu przy ul. Lubelskiej przez szl. S. Skarbka podwojciemu W. Kurewicowi za 70 złp; A. Pieniążek vs W. Dzierżek (13 I 1672)",
     "Ubald Janaszkowicz (wójt), Stanisław Sebastian Skarbek (szlachetny), Jakub (małoletni), Stefan (małoletni), Antoni (szwagier Skarbka), Wojciech Kurewic, Paweł Słonkowski, Wawrzyniec Zająk [Zając], Andrzej Pieniążek, Wojciech [Piotr] Dzierżek",
     "70 złp, 25 złp, 30 złp, 20 złp",
     "Uroczyste otwarcie roku 1672 ('NOVUS ANNUS Dni 1672'). Sesja z 12 I 1672 r.: przed wójtem Ubaldem Janaszkowiczem i siedmioma ławnikami szlachetny Stanisław Sebastian Skarbek jako opiekun małoletnich siostrzeńców Jakuba i Stefana (po szwagrze Antonim) sprzedaje podwojciemu Wojciechowi Kurewicowi zrujnowany dom na ulicy Lubelskiej (między placem Pawła Słonkowskiego a Grotem), nabyty wcześniej od Wawrzyńca Zająka [Zająca], za 70 złp (25 złp gotówką, 30 złp dla Zająca, 20 złp na Zielone Świątki). Poniżej sesja z 13 I 1672 r.: Andrzej Pieniążek vs Wojciech [Piotr] Dzierżek.",
     """[fol. 28r]
NOVUS ANNUS Dni 1672.
A Partu Virgineo sub felicibus auspiciis Cristi noviter nati Incipit. Utinam faustus sit.
Actum feria tertia post Festum Epiphaniae Dni prox[im]a 1672.
Mercipotus inter Gen. Stan. Sebastianum Skarbek et Albertum Kurewic.
W domu Sławetnego Pana Ubalda Janaszkowica Wójta i Sędziego Przysięgłego Kraśnickiego przy bytności tegoż samego y siedmiu ławników przy boku jego siedzących stał się pewny y nieodmienny targ y kupno w ten niżej opisany sposób: Iż Jaśnie Urodzony Pan Stanisław Sebastian Skarbek jako opiekun z prawa i dziatek małoletnich Jakuba i Stefana pozostałych szwagra swego nieboszczyka Antoniego z przyzwoleniem siostry rodzonej swojej, oddał y sprzedał dom w Kraśniku na ulicy Lubelskiej leżący między placem Pawła Słonkowskiego z jednej strony a z drugiej Grotą mieszczanina kraśnickiego, który był kupił na nieboszczyku Łukaszu [?] od Wawrzyńca Zająka mieszczanina kraśnickiego, Sławetnemu Panu Wojciechowi Kurewicowi za sumę złotych polskich siedmdziesiąt (70 złp), z której już 25 złp odebrał przy targu, 30 złp ma oddać Wawrzyńcowi Zająkowi, a ostatnie 20 złp na Święta Wielkanocne przyszłe 1672 [...]

Actum coram Offo Advocat. et Scabinali feria quarta post Festum Epiphaniarum prox[im]a Anno Dni 1672.
Inter Andream Pieniążek Actorem et Albertum [Petrum] Dzierżek cittum.
Ponieważ pozwany na terminie dzisiejszym stawiwszy się prosił o dylacyą do niedziel czterech na wywiedzenie dokumentów, Sąd pozwala mu do sądu blisko przyszłego."""),

    (60, "fol. 28v (20v / 28v)", "1672",
     "Protestacja A. Pieniążka; G. Stryczkowski vs P. Miedowic (7 korali z pożaru); sesja 15 I 1672 r.: P. Słonkowski; zeznania dla B. Kołodziejczyka o pożarze u B. Kuśmierza",
     "Andrzej Pieniążek, Piotr Dzierżek, Grzegorz Stryczkowski, Paweł Miedowic [Miodowic?], Paweł Słonkowski, Błażej Kołodziejczyk, Paweł Balusik [?], Wojciech [świadek], Bartosz Kuśmierz",
     "5 grzywien",
     "Protestacja ślusarza Andrzeja Pieniążka przeciw Piotrowi Dzierżkowi; wyrok w sprawie Grzegorza Stryczkowskiego z żoną przeciw Pawłowi Miedowicowi [Miodowicowi?] z żoną o 7 korali powierzonych na przechowanie podczas pożaru przez matkę aktorki (nakaz oddania korali, osadzenie w wieży matki na 48 godzin i 5 grzywien kary); sesja z 15 I 1672 r.: zeznanie P. Słonkowskiego dla P. Dzierżka; zeznania 1) Pawła Balusika [?] i 2) Wojciecha dla ławnika Błażeja Kołodziejczyka o pożarze u Bartosza Kuśmierza i ratowaniu domu Kołodziejczyka; otwarcie sesji z 22 I 1672 r.",
     """[fol. 28v]
Protestatio Andreae Pieniążek contra Petrum Dzierżek.
Ad Officium et Acta praesentia Advocatialia et Scabinalia veniens Honestus Andreas Pieniążek sutor [ferrifaber] protestatus est contra Petrum Dzierżek o zwłokę w zapłacie i niepotrzebne dylacye [...]
Inter Gregorium Stryczkowski et coniugem eius Actores et Paulum Miedowic [Miodowic?] et consortem eius cittos.
W sprawie przez aktora z małżonką przeciw pozwanym o wrócenie siedmiu korali które matka aktorki podczas przypadku ogniowego nieszczęsnego bliźniego swego ratując dała pozwanej małżonce do schowania [...] Sąd nakazuje pozwanym oddać korale, zapłacić 5 grzywien sądowi i koszty prawne.

Actum feria 6ta ante festum SS. Fabiani et Sebastiani prox[im]a Ao 1672 [15 I 1672].
Testimonium ex parte Petri Dzierżek.
Paweł Słonkowski na instancyą Piotra Dzierżka zeznał pod przysięgą o rozmowie z Pieniążkiem przy budowaniu stodoły.
Depositiones testium ex parte Blasii Kołodziejczyk.
1mus Testis Paulus Balusik [?] na instancyą Błażeja Kołodziejczyka ławnika zeznał pod przysięgą: Gdy dym wielki z komina od Bartosza Kuśmierza wypadał i ogień na dom Błażeja Kołodziejczyka szedł, rzuciliśmy się do gaszenia [...]
2dus Testis Wojciech zeznał słowo w słowo o pożarze i płomieniu z domu Bartosza Kuśmierza.
Actum Crasnicii coram Officio Advocat. et Scabinal. feria 6ta post Festum S. Agnetis Virginis et Martyris prox[im]a Anno Dni 1672 [22 I 1672]."""),

    (61, "fol. 29r (21 / 29)", "1672",
     "W. Łaziński vs W. Żydek krawiec; protestacja W. Żydka; kontumacja A. Pieniążka; sesja 25 I 1672 r.; P. Smarowic vs A. Łążkowic o suknię pożyczoną",
     "Wojciech Łaziński, Wawrzyniec Żydek (krawiec), Andrzej Pieniążek, Piotr Dzierżek, Jan Kresowski (bedel), Paweł Smarowic, Augustyn Łążkowic",
     "-",
     "Sprawa młynarza Wojciecha Łazińskiego przeciw krawcowi Wawrzyńcowi Żydkowi; protestacja krawca Wawrzyńca Żydka przeciw młynarzowi Wojciechowi Łazińskiemu; kontumacja Andrzeja Pieniążka z instancji Piotra Dzierżka (relacja bedela Jana Kresowskiego); sesja z 25 I 1672 r. (Nawrócenie św. Pawła); wyrok w sprawie Pawła Smarowica przeciw Augustynowi Łążkowicowi o pożyczoną suknię.",
     """[fol. 29r]
Inter Albertum Łaziński molitorem Actorem et Laurentium Żydek sartorem cittum.
Ponieważ pozwany do żadnej rzeczy jako aktorowi tak i w sprawie swojej nie przyznaje się [...] Sąd pozwala dylacyi na dowód.
Protestatio Laurentii Żydek contra Albertum Łaziński molitorem.
Ad Officium Advocatiale et Scabinalia veniens Laurentius Żydek sartor protestatus est contra Albertum Łaziński o zniewagę i obmowy w domu swoim.
Contumacia Andreae Pieniążek ex parte Petri Dzierżek.
Providus Joannes Kresowski Bedellus Juratus retulit se citasse Andream Pieniążek ex instantia Petri Dzierżek, qui non comparuit, condemnatur.
Actum feria 2da ipso die S. Conversionis S. Pauli Apli prox[im]a Anno Dni 1672 [25 I 1672].
[...] dla lepszej informacyi prorogatur a Judicio praesenti [...]
Inter Paulum Smarowic Actorem et Augustinum Łążkowic cittum.
Przypozwany będąc Augustyn Łążkowic od aktora o suknię pożyczaną w komorze [...] Sąd nakazuje według assekuracyi oddać suknię aktorowi w terminie bliskim pod winą i więzieniem."""),

    (62, "fol. 29v (21v / 29v)", "1672",
     "Sesja 1 IV 1672 r.: kontumacje B. Szafrankowica i G. Miecznika; zeznanie B. Kłopota dla W. Kowaliczka; wyrok W. Kowaliczek vs P. Mucha; sesja 4 IV 1672 r.",
     "Wawrzyniec Żydek, Wojciech Łaziński, Baltazar Szafrankowic, Bartłomiej Grudzień (kuśnierz), Grzegorz Miecznik, Paweł Smarowic, Jan Kresowski (bedel), Wawrzyniec Kowaliczek, Bartosz Kłopot, Paweł Mucha [Mazurek?], Zofia (wdowa)",
     "-",
     "Sesja z piątku przed Niedzielą Palmową (1 IV 1672 r.): diligentia krawca Wawrzyńca Żydka przeciw młynarzowi Wojciechowi Łazińskiemu; kontumacja Baltazara Szafrankowica z instancji kuśnierza Bartłomieja Grudnia; kontumacja Grzegorza Miecznika z instancji Pawła Smarowica; zeznanie Bartosza Kłopota na rzecz Wawrzyńca Kowaliczka o targowaniu stodoły na Podlesiu; wyrok w sprawie Wawrzyńca Kowaliczka przeciw Pawłowi Musze [Mazurkowi?]; sesja z 4 IV 1672 r.: Zofia wdowa przeciw Wawrzyńcowi Kowaliczkowi.",
     """[fol. 29v]
Actum coram Officio Advocati et Scabinorum Juratorum Crasnicensium feria 6ta ante Dominicam Passionis prox[im]a A. 1672 [1 IV 1672].
Diligentia H. Laurentii Żydek Sartoris Crasnicensis contra Albertum Łaziński molitorem.
Contumax Baltazar Szafrankowic ex parte Barthol. Grudzień pellionis.
A Bartholomaeo Grudzień kuśnierzem mieszczaninem kraśnickim przed Urzędem niniejszym Baltazar Szafrankowic pozwany nie stanął, skazany na kontumacyą.
Contumax Gregorius Miecznik ex parte F. Pauli Smarowic.
Providus Joannes Kresowski Bedellus Juratus retulit se citasse Gregorium Miecznik ex instantia Pauli Smarowica, qui non comparuit, condemnatur.
Testimonium pro parte Laurentii Kowaliczek.
Bartosz Kłopot przed Urzędem zeznał na instancyą Wawrzyńca Kowaliczka iż pomagał targować stodołę na Podlesiu od Pawła Muchy [Mazurka?].
Inter Laurentium Kowaliczek Actorem et Paulum Mucha [Mazurek?] cittum.
W sprawie sądowej o stodołę na Podlesiu [...] Sąd nakazuje pozwanemu stodołę wydać lub szkodę nagrodzić i przeprosić aktora.
Actum feria 2da post Dnicam Passionis prox[im]a Anno Dni 1672 [4 IV 1672].
Inter Zophiam viduam Actricem et Laurentium Kowaliczek cum uxore cittos."""),

    (63, "fol. 30r (22 / 30)", "1672",
     "Dokończenie wyroku Zofii przeciw W. Kowaliczkowi (15 złp, 30 złp, Budzyń); wielki proces B. Grudnia przeciw B. Szafarowi i J. Czelewowi [?]",
     "Zofia (wdowa), Wawrzyniec Kowaliczek, Andrzej (syn Zofii), Bartosz Grudzień, Jan Grudzień, Baltazar Szafar [Szafrankowic], Jan Czelew [?], Barankowic (syn), Organista (syn)",
     "15 złp, 30 złp, 20 złp",
     "Dokończenie rozbudowanego dekretu w sprawie wdowy Zofii przeciw Wawrzyńcowi Kowaliczkowi o dom w Budzyniu i spłatę 15 złp oraz 30 złp (wzmiankowany Andrzej i dawne kwoty 20 złp). Poniżej obszerny zapis procesu Bartosza Grudnia (syna Jana) przeciw Baltazarowi Szafarowi [Szafrankowicowi] i Janowi Czelewowi [?] o ciężkie pobicie i podrapanie przez syna organisty i syna Barankowica w domu Baltazara Szafra.",
     """[fol. 30r]
[...] zeznał że przedtym miał dom w Budzyniu, przy czym miał oddać 15 złp i 30 złp [...] Sąd dekretuje aby pozwany w terminie blisko przyszłym resztę spłacił, a strony mają się pogodzić pod zakładem.
Inter Bartholomaeum Grudzień Joannis filium Actorem et Baltazarum Szafar et Joannem Czelew [?] cittos.
In causa et actione judiciaria skarżył się aktor na pozwanego Baltazara Szafra i Jana Czelewa [?], iż w domu Baltazara Szafra syn jego wraz z synem organisty i synem Barankowica napadli nań, podrapali na twarzy i piersiach [...] Sąd po wysłuchaniu świadków nakazuje pozwanym zwrot kosztów i karę wieży za pobicie [...]"""),

    (64, "fol. 30v (22v / 30v)", "1672",
     "Dokończenie dekretu B. Grudnia; Z. Kowalikówna vs T. Starybracik; M. Kępka vs B. Kępka; A. Łeżyk vs M. Kępka; wizja graniczna W. Kurewica; sesja 6 IV 1672 r.",
     "Bartosz Grudzień, Baltazar Szafar, Wojciech Kurewic, Zofia Kowalikówna, Wojciech Kowalik, Tomasz Starybracik [Stachyra], Matyjasz Kępka, Bartosz Kępka, Adam Łeżyk, Paweł Smarowic, Sebastian Balusik, Grzegorz [sąsiad]",
     "8 złp, 30 złp",
     "Dokończenie wyroku w sprawie Bartosza Grudnia (wzmiankowany Wojciech Kurewic); wyrok Zofii Kowalikówny z synem Wojciechem przeciw Tomaszowi Starybracikowi o 8 złp; wyrok Matyasza Kępki vs Bartosz Kępka; skarga Adama Łeżyka przeciw Matyjaszowi Kępce o pobicie żony w ciąży; urzędowa wizja graniczna ławników Pawła Smarowica i Sebastiana Balusika między gruntem Wojciecha Kurewica a Grzegorzem; sesja z 6 IV 1672 r.: zeznanie świadka na rzecz Adama Łeżyka.",
     """[fol. 30v]
[...] zawarli który podjąwszy do prawa [...] Sąd nakazuje przeprosiny w domu Sławetnego Pana Wojciecha Kurewica i zapłatę kar.
Inter Zophiam Kowalikówna et Albertum filium suum Actores et Thomam Starybracik cittum.
Skarżyła się aktorka na pozwanego o suknią białą wartości 8 złp y o rany [...] Sąd nakazuje oddać suknię lub zapłacić 8 złp.
Inter Matthiam Kępka Actorem et Bartholomaeum Kępka cittum. Decretum.
Vigore praesentis decreti nakazano aby pozwany aktorowi z sumy 30 złp zadość uczynił.
Inter Adamum Łeżyk Actorem et Matthiam Kępka cittum. Relatio ad inquisitionem.
Skarżył się aktor na pozwanego o pobicie żony swojej ciężarnej na drodze [...] Sąd odsyła do inkwizycyi świadków.
Relatio Officiosa limitationis sive requisitionis.
Famati Paulus Smarowic et Sebastianus Balusik Scabini Jurati Crasnicenses retulerunt o wizji granicznej między gruntem Wojciecha Kurewica Ławnika Kraśnickiego a gruntem Grzegorza [...]
Actum feria quarta post Dnicam Passionis Quadragesimalem [6 IV 1672].
Testimonium pro parte Adami Łeżyk ratione vulnerum a Matthia Kępka.
1mus Testis Wojciech zeznał pod przysięgą o zajściu między Adamem Łeżykiem a Matyaszem Kępką przy stodole."""),

    (65, "fol. 31r (23 / 31)", "1672",
     "Sprawa posagowa o córkę Ewę i zięcia Jana Jędryka (30 złp); Wawrzyniec Miedarczyk [?] vs Bractwo Różańcowe; J. Furman z Zamościa vs Żyd Moszek o 40 złp",
     "Ewa (córka), Jan Jędryk [?], Wawrzyniec Miedarczyk [?], Jan Furman (z Zamościa), Moszek (Żyd z Kraśnika/Urzędowa), Piotrowic (z Końskowoli?)",
     "30 złp, 40 złp",
     "Dokończenie aktu posagowego dotyczącego córki Ewy i zięcia Jana Jędryka [?] (30 złp posagu i zapis w roku 1672); wyrok nakazujący Wawrzyńcowi Miedarczykowi [?] oddać zapis z testamentu żony Bractwu Różańcowemu (na 5 mszy); sprawa Jana Furmana z Zamościa przeciw Żydowi Moszkowi o najem mieszkania i furmankę (wzmiankowany P. Piotrowic).",
     """[fol. 31r]
[...] którą córkę swoją Ewę gdy do siebie zabrał, obligował się po śmierci córki dać 30 złp [...] zięć Jan Jędryk [?] mąż przerzeczonej Ewy jako possessor tej sumy [...] Dni 1672.
Inter Laurentium Miedarczyk [?] cittum et Procuratores SSmi Rosarii actores.
Decreto praesentis iniunctum est aby citatus złożone z testamentu nieboszczki żony swojej Bractwu legowane na 5 mszy świętych blisko przyszłych oddał.
Inter Joannem Vectorem [Furmana] de Zamość Actorem et Perfidum Moszek Judaeum de Krasnik [vel Zamość] cittum.
W sprawie między Janem Furmanem z Zamościa aktorem a Moszkiem Żydem o mieszkanie y bawienie się w drodze przez co wielką szkodę poniósł aktor [...] Sąd nakazuje aby Żyd Moszek aktorowi za szkodę zapłacił, a o dalsze pretensye do P. Piotrowica odesłano."""),

    (66, "fol. 31v (23v / 31v)", "1672",
     "Dokończenie sprawy furmana Jana; wielki proces o czary Bartosza Kłopota z żoną przeciw Balasionie [Balaowej]",
     "Jan Furman, Moszek (Żyd), Bartosz Kłopot, Kłopotowa (żona Bartosza), Balasiona [Balaowa], Maryna Balasiona",
     "-",
     "Dokończenie dekretu Jana Furmana przeciw Żydowi Moszkowi; początek głośnego procesu o zniesławienie i posądzenie o czary: Bartosz Kłopot z żoną przeciw wdowie Balasionie [Balaowej], która publicznie zarzucała żonie Kłopota odebranie mleka krowom za pomocą czarów (nakaz inkwizycji i przysięgi oczyszczającej Kłopota z żoną).",
     """[fol. 31v]
[...] dalszej pretensyi do pomienionego Moszka [...] a gdyby się nie zgodzili, do sądu wrócą.
Inter Bartosza Kłopota et Consortem eius Actores et Balaowa [Balasiona] cittam.
Skarżył się aktor swoim i małżonki swej imieniem na pozwaną Balaową, iż ona zadała małżonce jego jakoby miała czary czynić y mleko krowom odbierać, co przed sąsiadami powtarzała [...] Sąd niniejszy przesłuchawszy inkwizycyi z świadków i nie znajdując żadnego dowodu czarów przeciw żonie aktora, nakazuje aby Bartosz Kłopot z małżonką przysięgą oczyścili się z tego zarzutu [...]"""),

    (67, "fol. 32r (24 / 32)", "1672",
     "Wyrok w sprawie o czary (Balaowa skazana na Szpital św. Ducha i 4 niedziele wieży); sesja 11 VII 1672 r.: Elżbieta Kochanowska vs Świderek; Żyd Feliks vs G. Szadzik",
     "Bartosz Kłopot, Balaowa [Balasiona], Elżbieta Kochanowska [?], Świderek, Feliks (Żyd), Grzegorz Szadzik",
     "6 niedziel na Szpital, 5 grzywien, 5 złp 12 gr",
     "Dokończenie wyroku nad Balaową [Balasioną]: za złośliwe pomówienie o czary skazana na 6 niedziel posługi w Szpitalu św. Ducha, publiczne przeprosiny przez 4 osoby oraz 4 niedziele w klatce pod zakładem 5 grzywien; sesja z poniedziałku przed św. Małgorzatą (11 VII 1672 r.): wyrok w sprawie Żyda Eliasa/Elżbiety przeciw Świderkowi (3 niedziele na Szpital i 5 grzywien); wyrok dla Żyda Feliksa przeciw Grzegorzowi Szadzikowi o dług 5 złp 12 gr.",
     """[fol. 32r]
[...] jako nie jest czarownicą ani z tego powodu winna [...] Przetoż pozwana Balaowa za takową kalumnią y obelgę w klatce więzienia siedzieć będzie niedziel cztery, sześć niedziel na Szpital św. Ducha służyć, aktorów przeprosić przez osób cztery i pod zakładem 5 grzywien winy nie odważać się więcej takowych słów mówić.

Actum Feria 2da ante Festum S. Margarethae Virginis prox[im]a [11 VII 1672].
Inter Infidum Eliam [?] Actorem et Świderek cittum.
Skarżył się pozwany o zatrzymanie winy i na gospodzie [...] Sąd nakazuje 3 niedziele posługi na Szpital i przeprosiny przez dwie osoby.
Inter Felix Judaeum Actorem et Gregorium Szadzik cittum.
Ponieważ się z świadectwa pokazało że pozwany winien bez żadnej wymówki dług zł 5 gr 12 aktorowi Feliksowi [...] Sąd skazuje na więzienie aż do zapłacenia długu 5 złp 12 gr z kosztami."""),

    (68, "fol. 32v (24v / 32v)", "1672",
     "Manifestacja Bractwa Różańcowego przeciw G. Foxowi; kontumacja P. Dzierżka o dziesięcinę; sesja 15 VII 1672 r.: kontumacja J. Wardęgi z instancji S. Jajczyka",
     "Grzegorz Fox (rajca), Piotr Dzierżek, Jan Czarnocki [?], Jakub Wardęga, Sebastian Jajczyk",
     "-",
     "Manifestacja prebendarza Bractwa Różańcowego przeciw rajcy Grzegorzowi Foxowi o niezapłacony dług bracki w wyznaczonym terminie; potrójna kontumacja Piotra Dzierżka z instancji plebana/mieszczanina Jana Czarnockiego [?] o niezapłaconą dziesięcinę kościelną; sesja z piątku w dzień Rozesłania Apostołów (15 VII 1672 r.): kontumacja Jakuba Wardęgi z instancji Sebastiana Jajczyka.",
     """[fol. 32v]
Adm. Rdus Presbiter SSmi Rosarii manifestatur contra Fam. Gregorium Fox Consulem.
In termino hodierno ex vi decreti ad solutionem certi debiti per Famatum Gregorium Fox consulem Crasn. Confraternitati SSmi Rosarii assignato iam elapso, quoniam praefatus citatus neque satisfecit neque comparuit, manifestatus est et in poena contumaciae condemnatur, cum intromissione in bona in triduo.
Petrus Dzierżek ter adcitatus et non comparens ex instantia Honesti Czarnocki [?] ob non solutionem Decimae Ecclesiasticae citatus et condemnatus in contumaciam.

Actum Feria 6ta ipso die Festi Divisionis SS. Apostolorum [15 VII 1672].
Jacobus Wardęga ex instantia Sebastiani Jajczyk ad satisfaciendum debito adcitatus et non comparens est in poena contumaciae condemnatus."""),

    (69, "fol. 33r (25 / 33)", "1672",
     "Protestacja J. Kacowskiego; sesja 8 VIII 1672 r.: S. Nawrocki vs T. Zajączkowski [?]; wyrok Bartoszek vs W. Ziębik [?] o pobicie i zgubę 7 złp",
     "Jacek Kacowski [?], Tomasz Pałątkowicz [?], Stanisław Nawrocki, Tomasz Zajączkowski [?], Bartoszek, Wojciech Ziębik [?], Wojciech Kubica [?]",
     "7 złp, 3 grzywny",
     "Protestacja Jacka Kacowskiego [?] przeciw Tomaszowi Pałątkowiczowi [?] o napaść; sesja z poniedziałku przed św. Wawrzyńcem (8 VIII 1672 r.): odroczenie sprawy Stanisława Nawrockiego vs Tomasz Zajączkowski [?]; wyrok w sprawie Bartoszka przeciw Wojciechowi Ziębikowi [?] o pobicie w sieni i zaginięcie 7 złp (kara klatki, 3 grzywny, wzmiankowany Wojciech Kubica [?]).",
     """[fol. 33r]
Jacek Kacowski [?] protestatur contra Thomam Pałątkowicz [?], iż go zbił bez przyczyny i na drodze napadł, co chce dowodzić.
Actum Feria 2da ante Festum S. Laurentii Martyris prox[im]a [8 VIII 1672].
Inter F. Stan. Nawrocki Actorem et Thomam Zajączkowski [?] cittum.
Że się citatus nie zna aby miał despektować aktora, Sąd pozwala dylacyi na świadectwo do piątku blisko przyszłego.
Inter Bartoszek Actorem et Albertum Ziębik [?] cittum.
W sprawie między stronami o pobicie aktora przez pozwanego y o zgubę pieniędzy złotych siedmiu w sieni toczącej się [...] Sąd niniejszy skazuje pozwanego na więzienie do klatki y winy ma oddać grzywny trzy, a względem zgubionych złotych siedmiu przysięgą ma się oczyścić pozwany przy świadkach i ugodzie z Wojciechem Kubicą [?] [...]"""),

    (70, "fol. 33v (25v / 33v)", "1672",
     "Dokończenie wyroku W. Ziębika; dekret intromisji Bractwa Różańcowego w dobra rajcy Grzegorza Foxa",
     "Bartoszek, Wojciech Ziębik [?], Grzegorz Fox (rajca)",
     "2 złp",
     "Dokończenie dekretu w sprawie Bartoszka przeciw Wojciechowi Ziębikowi [?]; ostateczny wyrok egzekucyjny z powództwa prebendarza i prokuratorów Bractwa Różańcowego przeciw rajcy Grzegorzowi Foxowi: po wyczerpaniu wszystkich dylacji i zapłacie zaledwie 2 złp, sąd nakazuje urzędową intromisję w dobra dłużnika.",
     """[fol. 33v]
[...] ani on sam ani nikt jego, quo praestito liber ratione 7 złp pronuntiabitur. A że citatus na ustęp będąc przy Sądzie ważył się z furyą na aktora następować, Sąd skazuje go za tę zuchwałość na więzienie i winę.
Inter Adm. Rdum Presb. SS. Rosarii et Procuratores Actores et Famatum Gregorium Fox cittum.
W sprawie na terminie dzisiejszym po tak wielu dylacyach przypadłej o dług Bractwu Różańca Świętego należący z obligacyi przez pozwanego danej [...] Ponieważ stary Pan Fox po tak długich dylacyach zaledwie złotych dwa do rąk oddał, a reszty nie płaci, Sąd niniejszy nakazuje intromissyą w dobra i grunty pozwanego odpowiadające długowi aż do zupełnej satysfakcyi."""),

    (71, "fol. 34r (26 / 34)", "1672",
     "Sesja 5 IX 1672 r.: proces piwowarski Walentego Sitarskiego przeciw Żydowi Dawidowi Muszy (24 beczki piwa); zeznanie piwowara Wawrzyńca Zająca",
     "Walenty Sitarski, Dawid Musza (Żyd), Wawrzyniec Zając (mieszczanin), Izaak (Żyd)",
     "24 beczki piwa, 44 beczki, 4 złp",
     "Sesja z poniedziałku przed Narodzeniem NMP (5 IX 1672 r.): protestacja mieszczanina kraśnickiego Walentego Sitarskiego przeciw Żydowi Dawidowi Muszy o nierzetelne rozliczenie i zniszczenie 24 beczek piwa w słodowni; szczegółowe zeznanie 1. świadka mieszczanina Wawrzyńca Zająca o warzeniu piwa w marcu w słodowni Sitarskiego i przejmowaniu beczek przez Żydów Dawida i Izaaka.",
     """[fol. 34r]
Actum Feria 2da ante Festum Nativitatis Beatissimae Virginis Mariae prox[im]a [5 IX 1672].
Valentinus Sitarski protestatur contra Infidum Dawid Musza Judaeum et testimonia producit.
Do Urzędu i Akt niniejszych przyszedłszy Uczciwy Walenty Sitarski mieszczanin kraśnicki z wielkim żalem powiadał przeciwko Niewiernemu Dawidowi Muszy Żydowi kraśnickiemu o to, iż on stargowawszy wziął u niego beczek 24 piwa po złotych 4, z których teraz nie chce płacić i odbiera się że piwo kwaśne [...] stawił świadków poniżej podpisanych:
1mus Testis Wawrzyniec Zając mieszczanin kraśnicki pod przysięgą zeznał: Robiłem w słodowni u Walentego Sitarskiego słód cztery razy w marcu, z którego piwo było dobre i przedawał Żydowi Izaakowi ze Stróży po złotych cztery koniec, a Dawid Musza zaparł pomienionego słodu i wziął w korce ośm, a Żyd Izaak przysyłał po nie do Fary [...]"""),

    (72, "fol. 34v (26v / 34v)", "1672",
     "Zeznania Jędrzeja Piwowara i Wojciecha Lisowskiego w sporze piwnym W. Sitarskiego z Żydem D. Muszą; sprawa Pańkowej [?] vs Zofia Bartkowa",
     "Jędrzej Piwowar, Dawid Musza (Żyd), Wojciech Lisowski, Walenty Sitarski, Pańkowa [Paćkowa?] (wdowa), Zofia Bartkowa, Jan Dudnik [Grudzień?]",
     "3 beczki piwa",
     "Dalsze zeznania świadków w procesie piwowarskim: 2) Jędrzej Piwowar (o warzeniu połowy piwa u Dawida i braku skarg na smak) oraz 3) Wojciech Lisowski (o słabym, choć zdatnym do picia piwie Dawida Muszy); ostateczny wyrok zwalniający Dawida Muszę od części roszczeń i rozliczający strony; na dole dekret wdowy Pańkowej [Paćkowej?] przeciw Zofii Bartkowej o zwrot długu Jana Dudnika [?].",
     """[fol. 34v]
2dus Testis Uczciwy Jędrzej Piwowar pod przysięgą zeznał: Robiłem u Dawida Muszy z połowicę słodów piwa, które było dobre i nie czułem żadnej przygany w smaku, tylko że Żydzi trzy beczki piwa wzięli i wywieźli do Stróży [...]
3tius Testis Uczciwy Wojciech Lisowski pod przysięgą zeznał: Nosiłem piwo Dawida Muszy ze słodowni, ale to piwo było zgoła przebrane, bo miasto połowy wody lano, a samo piwo nie było złe [...]
Nad to tenże Walenty Sitarski przedstawił piwo od pomienionego Żyda [...] Sąd po wysłuchaniu świadków i obejrzeniu piwa nakazuje rozliczenie stron i oddalenie dalszych pretensyi.
Inter Pańkowa [Paćkowa?] Viduam Actricem et Zophiam Bartkowa [?] cittam.
Ponieważ żadnego dowodu winy nie było aby miała pozwana podmawiać Jana Dudnika [?] żeby uciekał [...] Sąd uwalnia pozwaną od impetycyi aktorki."""),

    (73, "fol. 35r (27 / 35)", "1672",
     "Finał procesu o czary Bartosza Kłopota z żoną przeciw Balaowej (3 dni wieży i 2 grzywny); Żyd Feliks vs Grzegorz Wołkowski",
     "Bartosz Kłopot, Kłopotowa (żona Bartosza), Balaowa [Balasiona], Feliks (Żyd), Grzegorz Wołkowski [Wolak?]",
     "2 grzywny, 3 dni wieży",
     "Zakończenie procesu o czary: Bartosz Kłopot z żoną złożyli przysięgę oczyszczającą, a pozwana Balaowa [Balasiona] została skazana na 3 dni wieży, przeprosiny przed sądem i 2 grzywny kary za pomówienie o czary; dekret w sprawie Żyda Feliksa przeciw Grzegorzowi Wołkowskiemu [Wolakowi?] o zwrot zboża w ciągu 3 dni.",
     """[fol. 35r]
Inter Bartholomaeum Kłopot et Consortem eius Actores et Balaowa [Balasiona] cittam.
In termino hodierno ad praestandum iuramentum actoribus assignato comparuit Bartosz Kłopot z małżonką swoją gotów będąc do wykonania przysięgi przeciwko pozwanej, chcąc niewinność swoją pokazać iż ona nie jest żadną czarownicą jako jej pozwana zadała [...] Ponieważ pozwana odpuściła aktorom przysięgę wolną, a pomówienie okazało się fałszywe, Sąd skazuje pozwaną na siedzenie w wieży przez dni trzy i winy grzywien dwie oraz przeprosiny w sądzie.
Inter Felix Judaeum Actorem et Gregorium Wołkowski [Wolak?] cittum.
Decretum est aby pozwany dług zbożowy aktorowi in triduo oddał."""),

    (74, "fol. 35v (27v / 35v)", "1672",
     "Sesja 18 VII 1672 r.: obdukcja ran poddanych ze wsi Krężnica (Jakuba Kutki, Błażeja Wierzbickiego i Stefana Latoszka) pobitych i obrabowanych przez sługi P. Żabickiego",
     "Jakub Kutka, Błażej Wierzbicki, Stefan Latoszek (z Krężnicy), Ubald Janaszkowicz (wójt), Wojciech Kurewic, Paweł Smarowic, Żabicki (szlachcic), Łojowski [?]",
     "-",
     "Sesja z poniedziałku przed św. Marią Magdaleną (18 VII 1672 r.): na żądanie trzech pobitych i obrabowanych poddanych ze wsi Krężnica — Jakuba Kutki, Błażeja Wierzbickiego i Stefana Latoszka — ławnicy Wojciech Kurewic i Paweł Smarowic z ramienia wójta Ubalda Janaszkowica dokonali szczegółowej obdukcji głębokich ran ciętych i tłuczonych głów, rąk oraz pleców, zadanych na drodze przez sługi P. Żabickiego i P. Łojowskiego [?], którzy zrabowali im czapki, pieniądze i pędzili aż za miasto strzelając.",
     """[fol. 35v]
Actum Feria 2da ante Festum S. Mariae Magdalenae [18 VII 1672].
Obductio Vulnerum Laboriosi Jakobi Kutki, Blazii Wierzbicki et Stephani Latoszek subditorum de villa Krężnica.
Na affektacyą tych wyżej specyfikowanych poddanych ze wsi Krężnicy z ramienia Sławetnego Pana Ubalda Janaszkowica Wójta Sędziego Przysięgłego Kraśnickiego byli deputowani Sławetni Wojciech Kurewic i Paweł Smarowic Ławnicy Przysięgli Kraśniccy na oglądanie ran u pomienionych poddanych, którzy w swej relacyi zeznali: Naprzód u Jakuba Kutki na wierzchu głowy raz połatany aż do kości, lewa ręka spuchła krwią zalana, na prawym ramieniu raz siny kością nabity; u Błażeja Wierzbickiego na plecach i pod łokciem sińce krwawe; u Stefana Latoszka w tyle głowy rany dwie krwawe [...] Dali winę w tych razach sługom P. Żabickiego i P. Łojowskiego [?], którzy ich w drodze pobili, czapki i pieniądze pobrali i aż za miasto gonili strzelając."""),

    (75, "fol. 36r (28 / 36)", "1672",
     "Sesja 29 VII 1672 r.: zeznania szl. Piotra Dzierżka dla Żyda Mośka przeciw W. Fajglowi (80 złp) i M. Kowalikowi (najem koni za 60 złp); J. Lisek vs W. Reszka (15 gr)",
     "Mosiek (Żyd), Wawrzyniec Fajgiel (winiarz), Piotr Dzierżek (szlachetny / sędzia), Młodnicki, Matyjasz Kowalik, Wojciech Konopacki, Jakub Piekarski, Jakub Lisek, Wojciech Reszka",
     "80 złp, 20 złp, 60 złp, 15 gr",
     "Sesja z piątku przed św. Dominikiem (29 VII 1672 r.): dwa zaprzysiężone zeznania szlachetnego Piotra Dzierżka z instancji Żyda Mośka: 1) przeciw winiarzowi Wawrzyńcowi Fajglowi o dług 80 złp oraz gorzałkę od P. Młodnickiego za 20 złp; 2) przeciw Matyjaszowi Kowalikowi o kontrakt najmu pary koni za 60 złp przy świadkach Wojciechu Konopackim i Jakubie Piekarskim; poniżej wyrok w sprawie Jakuba Liska przeciw Wojciechowi Reszce o zatrzymanie zapłaty 15 gr za robotę w polu.",
     """[fol. 36r]
Actum Coram Offo Advocat. et Scab. Jurat. Feria 6ta ante Festum S. Dominici prox[im]a [29 VII 1672].
Testimonium ex parte Infideli Judaei Mosiek contra Laurentium Fajgiel.
Szlachetny Piotr Dzierżek sędzia kraśnicki będący słusznie rekwiruwany od Żyda Mośka pod podniesieniem dwóch palców pod przysięgą zeznał: Byłem posłany od Żyda Mośka do Wawrzyńca Fajgla winiarza swego, który mu winien złotych ośmdziesiąt y za trzy spusty gorzałki, gdzie porachowali się y powiedział że mu jeszcze P. Młodnicki winien 20 złp [...]
Eodem die Sub eodem Actu.
Testimonium ex parte Infideli Judaei Mosiek contra Matthiam Kowalik ratione locati equi.
Tenże Szlachetny Piotr Dzierżek pod przysięgą zeznał: Byłem zaproszony z przyjaciółmi na litkup od Żyda Mośka y od Matyasza Kowalika przy sąsiadach Wojciechu Konopackim y Jakubie Piekarskim, gdzie przedał Żyd Mosiek koni parę za złotych sześćdziesiąt Matyjaszowi Kowalikowi [...]
Sub eodem Actu eodem die.
Inter Jacobum Lisek Actorem et Albertum Reszka cittum.
Skarżył się aktor na pozwanego o zatrzymanie płacy za robotę w polu [...] Sąd nakazuje pozwanemu oddać 15 gr za robotę.""")
]

for nr, pagina, rok, kat, osoby, kwoty, opis, trans in raw_scans:
    main_data.append({
        "nr_skanu": nr,
        "numer_pozycji": str(nr),
        "strona_pagina": pagina,
        "sygnatura": SYGN,
        "data_rok": rok,
        "kategoria": kat,
        "osoby_podmioty": osoby,
        "kwoty_podatki": kwoty,
        "opis_pozycji": opis,
        "kwoty_miary": kwoty,
        "transkrypcja": trans,
        "link_swa": LINK_SWA
    })

assert len(main_data) == 75, f"Blad liczby skanow: {len(main_data)}"

with open("main_data_j21_part3.json", "w", encoding="utf-8") as f:
    json.dump(main_data, f, ensure_ascii=False, indent=2)

print(f"Zapisano main_data_j21_part3.json: {len(main_data)} skanow.")
