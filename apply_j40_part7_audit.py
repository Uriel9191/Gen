#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_j40_part7_audit.py
Wdrożenie Partii 7 (Skany 106–125) Akt Miasta Kraśnika J40:
1. Aktualizacja transkrypcji dyplomatycznej z pełnymi tabelami (Opcja A) dla skanów 106–125.
2. Synchronizacja bazy genealogicznej genData (profile 751–780, aktualizacja wariantów i skanów).
3. Rygorystyczny test 100% synchronizacji onomastycznej.
4. Aktualizacja KPI w HTML.
5. Eksport zaktualizowanego skorowidza krasnik_j40_slownik_genealogiczny.csv.
"""

import json
import csv
import re
import os
import sys

HTML_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_kompendium_calosc.html'
CSV_PATH = '/home/ubuntu/workspace/Gen/krasnik_j40_slownik_genealogiczny.csv'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

m_start = html_content.find('const mainData = [')
m_end = html_content.find('];', m_start) + 1
main_data = json.loads(html_content[m_start + len('const mainData = '):m_end])

g_start = html_content.find('const genData = [')
g_end = html_content.find('];', g_start) + 1
gen_data = json.loads(html_content[g_start + len('const genData = '):g_end])

print(f"Początkowy stan: mainData={len(main_data)}, genData={len(gen_data)}")

# Transkrypcje Partii 7 (Skany 106–125)
transkrypcje_p7 = {
  "106": {
    "kategoria": "Taryfy podatkowe / Podymne unieważnione i Osiem Sympli / Śródmieście 1776",
    "opis_pozycji": "Dwa ułożenia podatkowe: 1. Anulowany wpis podatku podymnego na ratę marcową z 24 II 1776 r. skasowany formułą łacińską Nullitatis Expressio; 2. Właściwa taryfa nadzwyczajna ośmiu sympli spisana 12 IX 1776 r. dla Śródmieścia (początek: kolumny 1 i 2).",
    "kwoty_miary": "Stawki symplowe od 12 gr do 4 zł (Grzegorz Zdyb); anulowane podymne: 1 zł 15 gr – 4 zł 20 gr; 1mus Latus: 21 zł 19 gr; 2dus Latus z transportem: 34 zł 29 gr",
    "osoby_podmioty": "Jacek Fiszer (Fisier), wdowa Krzywicka, Paweł Latosowicz, Mikołaj Łapa, Kazimierz Rycerz, Michał Krzanowski, Antoni Krzeszowski, Jakub Szulc (Szulik), Piotr Gołębiowski, wdowa Kliszczonka, wdowa Zajączkowa, Jakub Grzymek, Antoni Petrykowski, Maciej Rycerz ławnik, Jakub Rojek, Grzegorz Zdyb, Wojciech Połokowicz, Franciszek Frankowicz, Mateusz Ryzak (Ryzik), Maciej Cieśla, Antoni Okoń, kupiec Chabuś Judkowicz, Baltazar Latosowicz, Michał Jędencarz, Antoni Sadowski, Wojciech Latosowicz, Józef Czapliński, Jan Foliarski, Piotr Marczyński, wdowa Stachowiczka, Jan Mulowski, Szymon Nowacki, Walenta Szafrańska, Antoni Suliczyński, Szymonowa Szajowska, Wojciech Bieniaszowski",
    "osoby_skrot": "Jacek Fiszer, Paweł Latosowicz, Grzegorz Zdyb, Antoni Okoń, Chabuś Judkowicz, Michał Jędencarz",
    "transkrypcja": "[Na marginesie górnym:] 51 v\n[Część górna urzędowo unieważniona – kasata łacińska:]\nUłożenie Podatku Podymnego na Rathę\nMarcową, przez Łascie M: Urząd y Całe Pospolstwo d 24\nFebruarii 1776to R: Spisane Tenore Tali.\n\n### [Kolumna 1: Miasto Kraśnik – Szkic Anulowany]\n\n| Posesjonat / Mieszczanin (Szkic Podymnego) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Jacek Fisier [Fiszer] | 4 | 20 |\n| Krzywicka wdowa | — | 22½ |\n| Paweł Latosowicz | 1 | — |\n| Mikołay Łapka | 1 | 15 |\n| Kzmr: Rycerz [Kazimierz] | 1 | 15 |\n| Michał Krzanowski | 1 | 15 |\n| Antoni Krzeszowski | 1 | 15 |\n\n[Klauzula kasacyjna w poprzek karty:]\nIn hac parte quidquid supra scription Nullitatis Expressio Oda Adnot:[atur] præsentibus sequit[ur]\n\n[Część dolna – właściwa taryfa sympli:]\nUłożenie Ośmiu Sympli 8. p:[rzez] Urząd y Pospol:[stwo]\nd 12. 7bris 1776 Rto Spisane.\n\n### [Kolumna 1: Miasto Kraśnik]\n\n| Posesjonat / Mieszczanin (Śródmieście) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Jacek Fisier [Fiszer] | 1 | 18 |\n| Domek Krzywickich | — | 12 |\n| Paweł Latoskowicz [Latosowicz] | — | 12 |\n| Mikołay Łapa | 2 | — |\n| Kz: Rycerz [Kazimierz] | 1 | 24 |\n| Michał Krzanowski | 2 | 10 |\n| Antoni Krzeszowski | 1 | — |\n| Jakob Szulik [Szulc / Szultz?] | 1 | — |\n| Piotr Gołębiowski | — | 12 |\n| Klyszczonka Wd:[owa] | — | 12 |\n| Zajączkowa Wd:[owa] | — | 12 |\n| Jakob Grzymek | — | 18 |\n| Antd: Petrykowski [Antoni] | 1 | 6 |\n| Maciey Rycerz Ławnik | — | 15 |\n| Jakob Rojek | 1 | 6 |\n| Grzegorz Zdyb | 4 | — |\n| Woytek Połokowicz | — | 18 |\n| Franciszek Frankowicz | 1 | 6 |\n| Mateusz Ryzik [Ryzak?] | — | 18 |\n| **1mus Latus** | **21** | **19** |\n\n### [Kolumna 2: Miasto Kraśnik – Kontynuacja]\n\n| Posesjonat / Mieszczanin (Śródmieście) | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 1mi Lati [Smi Lat:]** | **21** | **19** |\n| Maciey Cieśla | — | 18 |\n| Z Marcowiczowego | — | 12 |\n| Antoni Okoń | — | 24 |\n| Tamże Chabuś [Judkowicz] | — | 12 |\n| Baltazar Latosowicz | — | 18 |\n| Michał Jędencarz | — | 18 |\n| Antd: Sadowski [Antoni] | — | 12 |\n| Woyciech Latoskowicz [Latosowicz] | — | 18 |\n| Jozef Czapliński | — | 12 |\n| Jan Foliarski | 1 | 10 |\n| Domek Bryczkowy | 1 | — |\n| Piotr Marczyński | — | 18 |\n| Stachowiczkowa Wd:[owa] | — | 12 |\n| Jan Mulowski | — | 24 |\n| Szymon Nowacki [Nowak?] | 1 | — |\n| Walenta Szafrańska | — | 12 |\n| Antd: Suliczyński [Antoni] | 1 | — |\n| Szymonowa Szajowska | 1 | — |\n| Woyciech Bieniaszowski | 1 | — |\n| **2dus Latus (z transportem)** | **34** | **29** |"
  },
  "107": {
    "kategoria": "Taryfy podatkowe / Osiem Sympli / Śródmieście i Przedmieście Piasek 1776",
    "opis_pozycji": "Dalszy ciąg taryfy ośmiu sympli z 12 IX 1776 r.: dokończenie Śródmieścia (kolumna 1: Wojciech Krzeszowski, Józef Stembowski, Sadostka, Michał Matuszkiewicz, Paweł Piasecki) oraz wykaz gospodarzy przedmieścia Piasek (kolumna 2: Antoni Tkaczyk, Stanisław Wolak, niewierny Kopiński, Tomasz Jażdżyk).",
    "kwoty_miary": "Stawki od 6 gr (Seb. Latosowicz) do 8 zł (Stanisław Wolak, Niewierny Kopiński); 3tius Latus: 64 zł 27 gr; 4tus Latus: 153 zł 19 gr",
    "osoby_podmioty": "Mateusz Rycerz, Jakub Gąska, Walek Łukasik, Piotr Młynarczyk, Sebastian Latosowicz, Józef Stembowski, Antoni Rachoń, Kazimierz Młynarski, wdowa Fruzyna, Petronela Sadowska (Sadostka), Michał Matuszkiewicz, Tomasz Pilaszkiewicz, wdowa Bujarska, Franciszek Wilk, Paweł Fruga, Antoni Piasecki, wdowa Rachuniowa, Jan Boguta, wdowa Krasowska, Piotr Połokowicz (Podokowicz), wdowa Tokarska, wdowa Piłachowa (Pilachowa), Stanisław Posoniak, wdowa Łańska, Mikołaj Radomski (Radomirsky), Krzysztof Piecuch (Pieciuch), Maciej Wołczyński, Jędrzej Kępa, Marcin Kępa, wdowa Kępina, Walenty Jurgiel, Józef Szpiciarz, Wojciech Fijałkowski, Paweł Piasecki, Maciej Połokowicz, Grzegorz Leśniowski (Leśniostki), Szczepan Wójcik, Józef Bańka; Piasek: Antoni Tkaczyk, Stanisław Wolak, Szymon Antonik, Sobek Kilianek, Piotr Kilianek, Jan Bieniek, Marcin Łapa, wdowa Rymarzowa, wdowa Jasiewa, Paweł Jeś, Tomasz Jażdżyk, Maciej Zdyb, Jan Wójcik, Niewierny Kopiński, Mikołaj Nowak, Franciszek Pełka, Jakub Jaczniak, Bartłomiej Zdyb, Franciszek Oszowski (Oszoska), Janowa Gajczykowa, Jakub Jaśkiewicz (Jąśkiewiczi), Andrzej Gajek, Wojciech Nowak",
    "osoby_skrot": "Michał Matuszkiewicz, Paweł Piasecki, Stanisław Posoniak, Stanisław Wolak, Niewierny Kopiński, Tomasz Jażdżyk",
    "transkrypcja": "[Na marginesie górnym:] 52\nDalsze Ułożenie Ośmiu Sympli Spisane d 12. 7bris 1776 R.\n\n### [Kolumna 1: Miasto Kraśnik – Kontynuacja]\n\n| Posesjonat / Mieszczanin (Śródmieście) | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 2di Lati** | **34** | **29** |\n| Woyciech Krzeszowski | — | 24 |\n| Mateusz Rycerz | 1 | 6 |\n| Jakob Gąska | — | 12 |\n| Walek Łukasik | — | 18 |\n| Piotr Młynarczyk | — | 9 |\n| Seba: Latosowicz [Sebastian] | — | 6 |\n| Jozef Stemborfski [Stembowski] | 3 | 6 |\n| Antoni Rachon [Rachoń] | — | 24 |\n| Kz: Młynarski [Kazimierz] | 3 | 6 |\n| Fruzyna Wd:[owa] | — | 24 |\n| Sadostka [Sadowska?] | 2 | — |\n| Michał Matuszkiewicz | 4 | 24 |\n| Tomek Pilaszkiewicz | 1 | 10 |\n| Bujarska Wd:[owa] | — | 12 |\n| Franck Wilk [Franciszek] | 3 | — |\n| Paweł Fruga | 2 | 10 |\n| Z Ceydlowego | 1 | 12 |\n| Antoni Piasecki | 2 | 10 |\n| Rachuniowa Wd:[owa] | 2 | 12 |\n| Jan Boguta | 1 | 10 |\n| Krasowska Wd:[owa] | 1 | 6 |\n| Piotr Podokowicz [Połokowicz?] | 2 | 24 |\n| Tokarska Wd:[owa] | — | 24 |\n| Antd: Pilachowa Wd:[owa] [Pietrachowa?] | 1 | 10 |\n| Stach Posoniak [Stanisław] | 1 | 10 |\n| Łańska Wd:[owa] | 1 | 10 |\n| Mikołay Radomirsky [Radomski?] | 2 | 24 |\n| Krzyk Pieciuch [Krzysztof Piecuch?] | 3 | — |\n| Maciey Wołczynski [Wołczyński] | 1 | 12 |\n| Jędrzey Kępa | 1 | 6 |\n| Mar: Kępa [Marcin] | 1 | — |\n| **3tius Latus (z transportem)** | **64** | **27** |\n\n### [Kolumna 2: Dokończenie Miasta oraz Przedmieście Piasek]\n\n| Posesjonat / Przedmieszczanin | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 3tij Lati** | **64** | **27** |\n| Kępina Wd:[owa] | 2 | — |\n| Walenty Jurgiel | 1 | 10 |\n| Jozef Szpiciarzk [Szpiciarz?] | 1 | 6 |\n| Woyciech Fijałkowski | — | 10 |\n| Paweł Piasecki | 5 | 6 |\n| Maciey Połokowicz | — | 24 |\n| Grzegorz Leśniostki [Leśniowski?] | 1 | 12 |\n| Szczepan Woycik [Wójcik] | — | 10 |\n| Jozef Bańka | 3 | 6 |\n| *[Przedmieście Piasek]* | | |\n| Antoni Tkaczyk | 5 | — |\n| Stach Wolak [Stanisław] | 8 | — |\n| Szymon Antonik | 3 | — |\n| Sobek Kielianek [Kilianek] | 1 | 15 |\n| Piotr Kielianek [Kilianek] | 4 | — |\n| Jan Bieniek | 3 | 24 |\n| Mar: Łapa [Marcin] | 3 | 20 |\n| Rymarzowa Wd:[owa] | 3 | — |\n| Jasiewa Wd:[owa] | 5 | 24 |\n| Paweł Jeś | 1 | — |\n| Tomek Jazdżyk [Tomasz Jażdżyk] | 6 | — |\n| Maciey Zdyb | 5 | — |\n| Jan Woycik [Wójcik] | 3 | — |\n| N:[iewierny] Kopiński | 8 | — |\n| Mikołay Nowak | 3 | — |\n| Franc: Petka [Franciszek Pełka?] | 3 | — |\n| Jakob Jaczniak | 3 | — |\n| Bartek Zdyb [Bartłomiej] | 1 | 12 |\n| Franc: Oszoska [Franciszek Oszowski?] | 1 | 6 |\n| Janowa Gayczykowa [Gajczykowa] | 3 | — |\n| Jakub Jąśkiewiczi [Jaśkiewicz / Jasiewicz?] | 5 | 24 |\n| Andrzey Gajek | 2 | 12 |\n| Woyciech Nowak | 5 | — |\n| **4tus Latus (z transportem)** | **153** | **19** |"
  },
  "108": {
    "kategoria": "Taryfy podatkowe / Osiem Sympli / Przedmieścia Piasek i Zarzyce 1776",
    "opis_pozycji": "Dalszy ciąg taryfy ośmiu sympli z 12 IX 1776 r.: dokończenie przedmieścia Piasek (kolumna 1: Wojciech Cwicha, Łukasz Tokarczyk, Kazimierz Czelej) oraz wykaz gospodarzy przedmieścia Zarzyce (kolumna 1 i 2: Wawrzyniec Starobrat 14 zł, Andrzej Rządkowski 6 zł, Sobek Mikołajczyk 6 zł, Maciej Piotrowski, Błażej Chruściel).",
    "kwoty_miary": "Stawki od 1 zł do 14 zł (Wawrzyniec Starobrat za wielkie gospodarstwo na Zarzycach); 5tus Latus: 275 zł 25 gr; 6tus Latus: 370 zł 5 gr",
    "osoby_podmioty": "Piasek: Wojciech Cwicha, Szymon Wójcik, Wojciech Wiatrek, Paweł Zieliński, Wojciech Pełka, Wojciech Drąg, Łukasz Pełka (Betka), Joachim Kłopot, Łukasz Tokarczyk, Michał Tokarczyk, Piotr Tokarczyk, Wojciech Wójcik, Stanisław Kępniak, Barbara Bielecka, Stanisław Wójcik, Wojciech Trojczak, Kazimierz Trojczak, Kazimierz Czelej; Zarzyce: Bartłomiej Czelej, wdowa Łysakowa, Bartłomiej Kilianek, Maciej Szubartowski, wdowa Wiatrkowa, Grzegorz Jażdżyk, Wawrzyniec Starobrat (Stanbrat), Maciej Rachoń, wdowa Cuszkowa, Szymon Marzec, wdowa Rodzonkowa, Łukasz Kilianek, Maciej Rodzonek, Kasper Trojczak, Antoni Wanek (Panek), Grzegorz Biegaj, Maciej Piotrowski, Łukasz Rymarz, Andrzej Tokarczyk, Marcin Drąg, Wojciech Wolak, Marcin Kołton, Marcin Rymarz, wdowa Łapczyna (Łaszczyna), wdowa Markowa, Andrzej Rządkowski, Kazimierz Ciechoński (Olechowski), Sobek Łysak, Józef Dubaj, wdowa Dubajowa, Kazimierz Deryło, Sobek Mikołajczyk, Tomasz Rządkowski, Błażej Chruściel, Łukasz Biegaj, Józef Koza, Maciej Łazarz, Andrzej Łazarz, Antoni Koza, Bartłomiej Grządka, Maciej Kuśnierz, Mikołaj Rępa (Kępa), Łukasz Koza, Wawrzyniec Rzeszotek (Gęzarek), Mikołaj Buczek, Wojciech Biegaj, wdowa Oszustowa, wdowa Młynarczykowa, Stanisław Piotrowski",
    "osoby_skrot": "Łukasz Tokarczyk, Wawrzyniec Starobrat, Andrzej Rządkowski, Sobek Mikołajczyk, Błażej Chruściel",
    "transkrypcja": "[Na marginesie górnym:] 52 v\nDalsze Ułożenie Ośmiu Sympli d 12. 7bris 1776 R.\n\n### [Kolumna 1: Dokończenie Piasku oraz Przedmieście Zarzyce]\n\n| Posesjonat / Przedmieszczanin | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 4ti Lati** | **153** | **19** |\n| Woyciech Cwicha [Ćwieka?] | 5 | — |\n| Szymon Woycik [Wójcik] | 2 | 12 |\n| Woytek Wiatrek | 1 | 12 |\n| Paweł Zielensky [Zieliński] | 1 | 12 |\n| Woyciech Petka [Pełka?] | 3 | — |\n| Woyciech Drąg | 3 | — |\n| Łukasz Betka [Petka / Pełka?] | 4 | — |\n| Joachim Kłopot | 1 | 12 |\n| Łukasz Tokarczyk | 6 | — |\n| Michał Tokarczyk | 2 | 10 |\n| Piotr Tokarczyk | 3 | — |\n| Woytek Woycik [Wójcik] | 3 | — |\n| Stach Kępniak [Stanisław] | 3 | — |\n| Barbara Bielecka | 2 | 12 |\n| Stach Woycik [Wójcik] | 1 | 10 |\n| Woytek Troyczak [Trojczak] | 4 | 10 |\n| Kz: Troyczak [Kazimierz] | 5 | — |\n| Kz: Czeley [Kazimierz] | 5 | — |\n| *[Przedmieście Zarzyce]* | | |\n| Bartek Czeley [Bartłomiej] | 5 | — |\n| Łysakowa Wd:[owa] | 3 | 24 |\n| Bartek Kielianek [Kilianek] | 2 | 10 |\n| Maciey Szubartoski [Szubartowski] | 1 | 12 |\n| Wiatrkowa Wd:[owa] | 3 | 10 |\n| Grzegorz Jazdżyk [Jażdżyk] | 3 | 12 |\n| Wawrzyniec Stanbrat [Starobrat?] | 14 | — |\n| Maciey Rachon [Rachoń] | 3 | — |\n| Cuszkowa Wd:[owa] | 2 | 12 |\n| Szymon Marzec | 2 | 10 |\n| Rodzonkowa Wd:[owa] | 2 | 12 |\n| Łukasz Kielianek [Kilianek] | 2 | — |\n| Maciey Rodzonek | 5 | — |\n| Kasper Troyczak [Trojczak] | 2 | 6 |\n| Antoni Panek [Wanek?] | 4 | 10 |\n| **5tus Latus (z transportem)** | **275** | **25** |\n\n### [Kolumna 2: Przedmieście Zarzyce – Kontynuacja]\n\n| Posesjonat / Przedmieszczanin (Zarzyce) | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 5ti Lati** | **275** | **25** |\n| Grzegorz Biegay | 2 | — |\n| Maciey Piotroski [Piotrowski] | 5 | 24 |\n| Łukasz Rymarz | 3 | 10 |\n| Andrzey Tokarczyk | 2 | — |\n| Mar: Drąg [Marcin] | 4 | — |\n| Woytek Wolak | 2 | 24 |\n| Mar: Kołton [Marcin] | 2 | — |\n| Mar: Rymarz [Marcin] | 2 | 10 |\n| Łaszczyna Wda [Łapczyna?] | 2 | 12 |\n| Markowa Wda | 2 | 12 |\n| Jędrzey Rządkowski | 6 | — |\n| Kaz: Olechowski [Ciechoński?] | 1 | 10 |\n| Sobek Łysak [Sebastian] | 1 | 10 |\n| Jozef Dubay [Dubaj] | 2 | 12 |\n| Dubajowa Wd:[owa] | 2 | — |\n| Kz: Deryło [Kazimierz] | 1 | 10 |\n| Sobek Mikołayczyk [Sebastian] | 6 | — |\n| Tomek Rządkowski [Tomasz] | 4 | — |\n| Błach Chruściel [Błażej] | 2 | 12 |\n| Łukasz Biegay | 4 | — |\n| Jozef Koza | 3 | — |\n| Maciey Łazarz | 1 | 10 |\n| Andrzey Łazarz | 2 | — |\n| Antoni Koza | 2 | 12 |\n| Bartek Grządka [Bartłomiej] | 1 | 10 |\n| Maciey Kuśnierz | 3 | — |\n| Mikołay Kępa [Rępa?] | 2 | 12 |\n| Łukasz Koza | 2 | 12 |\n| Wawrzek Gęzarek [Rzeszotek?] | 2 | 12 |\n| Mikołay Buczek | 1 | 10 |\n| Woyciech Biegay | 2 | — |\n| Oszustowa Wd:[owa] | 1 | — |\n| Młynarczykowa [Wdowa] | 2 | 12 |\n| Stach Piotroski [Stanisław] | 3 | — |\n| **6tus Latus (z transportem)** | **370** | **5** |"
  },
  "109": {
    "kategoria": "Taryfy podatkowe / Osiem Sympli / Góry i Podlesie 1776",
    "opis_pozycji": "Dokończenie taryfy 8 sympli z 12 IX 1776 r. dla przedmieścia Góry i Podlesie (kolumna 1 i 2): Szymon Płachta, Wojciech Kusz (Rus), Szymon Krzeszowski, Józef Nowak, Antoni Tokarczyk, Sobek Zdyb i inni gospodarze podgórscy.",
    "kwoty_miary": "Stawki od 10 gr do 6 zł (Szymon Krzeszowski) i 9 zł 10 gr (Wojciech Kusz); Latus Gór i Podlesia: ok. 94 zł 14 gr; Suma całego ułożenia: 464 zł 19 gr",
    "osoby_podmioty": "Szymon Płachta, Adam Michał (Adamowicz?), Jan Boguta, Wojciech Gąska, Wojciech Kawka, wdowa Młynarczykowa, Jakub Rządkowski, wdowa Trojczakowa, Fabian Trojczak, Jacek Grzymek, Sobek Trojczak, Maciej Trojczak, Maciej Kępa, Mikołaj Kawka, Józef Strażnik, Antoni Tokarczyk, Szymon Krzeszowski, Józef Nowak, Augustyn Gregorczyk, Wawrzyniec Tokarczyk, Józef Gąska, Franciszek Kłopot, Mikołaj Zdyb, Szymon Ćwieka, wdowa Pawlicka, wdowa Grądzina, Jan Wilk, Mateusz Zdyb, wdowa Zimniakowa, wdowa Lenartowa, Tomasz Wilk, Maciej Kawka, Grzegorz Wolak, Andrzej Kępa, Augustyn Kawka, Józef Wilk, Błażej Babicz, Wojciech Kusz (Rus), Krzysztof Ćwieka, Benedykt Kawka, Stanisław Pielach, Walenty Biegaj, Sobek Zdyb, wdowa Cwichowa",
    "osoby_skrot": "Szymon Krzeszowski, Antoni Tokarczyk, Józef Nowak, Wojciech Kusz, Sobek Zdyb",
    "transkrypcja": "[Na marginesie górnym:] 53\nDokończenie Ułożenia Ośmiu Sympli d 12. 7bris 1776 R.\n\n### [Kolumna 1: Góry i Podlesie]\n\n| Posesjonat / Przedmieszczanin (Góry i Podlesie) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Szymon Płachta | 2 | 24 |\n| Adam Michał [Adamowicz?] | 1 | — |\n| Jan Boguta | 2 | — |\n| Woyciech Gąska | 1 | 12 |\n| Woyciech Kawka | 3 | 12 |\n| Młynarczykowa [Wdowa] | 4 | — |\n| Jakob Rzadkowski [Rządkowski] | 3 | — |\n| Troyczakowa Wd:[owa] | 1 | — |\n| Fabian Troyczak | 1 | 10 |\n| Jacek Grzymek | 3 | — |\n| Sobek Troyczak [Sebastian] | 1 | — |\n| Maciey Brat Jego [Trojczak] | 1 | — |\n| Maciey Kępa | 1 | — |\n| Mikołay Kawka | 3 | — |\n| Jozef Strażnik | 3 | — |\n| Antoni Tokarczyk | 5 | — |\n| Szym: Krzeszowski [Szymon] | 6 | — |\n| Jozef Nowak | 5 | — |\n| Aug: Gregorczyk [Augustyn] | 2 | 12 |\n| Wawrzek Tokarczyk [Wawrzyniec] | 2 | 12 |\n| Jozef Gąska | 5 | — |\n| Franc: Kłopot [Franciszek] | 1 | 10 |\n| Mikołay Zdyb | 1 | — |\n| Szymon Cwieka [Ćwieka] | 5 | — |\n| Pawlicka Wd:[owa] | 1 | 12 |\n| Grądzyna Wd:[owa] | 1 | — |\n| Jan Wilk | 1 | 10 |\n| Mateusz Zdyb | 1 | 10 |\n| Zimniakowa Wd:[owa] | 3 | 10 |\n| Lenartowa Wd:[owa] | 2 | 10 |\n| Tomek Wilk [Tomasz] | 3 | 10 |\n| Maciey Kawka | 2 | 10 |\n| Grzegorz Wolak [Widak?] | 1 | 10 |\n| Andrzey Kępa | 2 | 24 |\n| Augustyn Kawka | 3 | — |\n\n### [Kolumna 2: Góry i Podlesie – Kontynuacja i Finał Taryfy]\n\n| Posesjonat / Przedmieszczanin (Góry i Podlesie) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Jozef Wilk | 3 | 6 |\n| Błach Babiez [Błażej Babicz?] | 2 | 12 |\n| Woyciech Rus [Kusz?] | 9 | 10 |\n| Krzyk Cwieka [Krzysztof Ćwieka] | — | 10 |\n| Benedykt Kawka | — | 12 |\n| Stach Pielach [Stanisław Piłach / Piłaszkiewicz?] | 2 | 24 |\n| Walenty Biegay | 1 | 10 |\n| Sobek Zdyb [Sebastian] | 4 | 10 |\n| Cwichowa Wd:[owa] [Ćwikowa?] | 1 | 10 |\n| **Suma Gór i Podlesia** | **94** | **14** |\n| **In Summa Całego Ułożenia 8 Sympli** | **464** | **19** |"
  },
  "110": {
    "kategoria": "Taryfy podatkowe / Osiem Sympli / Śródmieście 1777",
    "opis_pozycji": "Taryfa „Ułożenie Ośmiu Sympli przez Mt Magistrat Kraśnicki y Pospolstwo d 29. Februarii 1777 dta Spisane”. Spis posesjonatów Śródmieścia (kolumna 1 i kolumna 2): Jacek Fiszer, Michał Krzanowski, Grzegorz Zdyb, Józef Stembowski, Sadostka, Mikołaj Radomski, Maciej Wołczyński.",
    "kwoty_miary": "Stawki symplowe 8-krotne: od 6 gr (Seb. Latosowicz) do 4 zł 24 gr (Michał Matuszkiewicz); sumy cząstkowe latusów",
    "osoby_podmioty": "Jacek Fiszer, wdowa Krzywicka, Paweł Latosowicz, Mikołaj Łapa, Kazimierz Rycerz, Michał Krzanowski (Wisiadłowski/Wziąndtki), Antoni Krzeszowski, Jakub Szulc (Szulik), Piotr Gołębiowski, wdowa Kliszczonka, wdowa Zajączkowa (Lagierkowa), Jakub Grzymek, Antoni Petrykowski, Maciej Rycerz, Jakub Rojek (Kojek), Grzegorz Zdyb, Wojciech Połokowicz, Franciszek Frankowicz, Mateusz Ryzak (Ryzik), Maciej Cieśla, Antoni Okoń, kupiec Chabuś Judkowicz, Baltazar Latosowicz, Michał Jędencarz, Antoni Sadowski, Wojciech Latosowicz, Józef Czapliński, Jan Foliarski, Piotr Marczyński, wdowa Stachowiczka, Jan Mulowski, Szymon Nowacki (Nowak), Walenta Szafrańska, Antoni Suliczyński, Szymonowa Szajowska, Wojciech Bieniaszowski, Wojciech Krzeszowski, Mateusz Rycerz, Jakub Gąska, Walenty Łukasik, Piotr Młynarczyk, Sebastian Latosowicz, Józef Stembowski, Antoni Rachoń, Kazimierz Młynarski, wdowa Fruzyna, Petronela Sadowska (Sadostka), Michał Matuszkiewicz, Tomasz Pilaszkiewicz, wdowa Bujarska, Franciszek Wilk, Paweł Fruga, Antoni Piasecki, wdowa Rachuniowa, Jan Boguta, wdowa Krasowska, Piotr Połokowicz, wdowa Tokarska, wdowa Piłachowa (Kielachowa/Pietrachowa), Stanisław Posoniak, wdowa Łańska, Mikołaj Radomski, Krzysztof Piecuch (Witczek Pieciuch), Maciej Wołczyński",
    "osoby_skrot": "Jacek Fiszer, Michał Krzanowski, Grzegorz Zdyb, Józef Stembowski, Mikołaj Radomski",
    "transkrypcja": "[Na marginesie górnym:] 53 v\nUłożenie Ośmiu Sympli przez M:[agistra]t Magistrat Kraś-\nnicki y Pospol:[stwo] d 29. Febr:[uarii] 1777 dta Spisane.\n\n### [Kolumna 1: Miasto Kraśnik]\n\n| Posesjonat / Mieszczanin (Śródmieście) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Jacek Fisier [Fiszer] | 1 | 18 |\n| Domek Krzydlinski [Krzywickich] | — | 12 |\n| Paweł Latosowicz | — | 12 |\n| Mikołay Łapa | 2 | — |\n| Kz: Rycerz [Kazimierz] | 1 | 24 |\n| Michał Wisiadłowski [Krzanowski / Wziąndtki?] | 2 | 18 |\n| Antoni Krzeszowski | 1 | — |\n| Jakob Szulik [Szulc?] | 1 | — |\n| Piotr Golebiowski [Gołębiowski] | — | 12 |\n| Klypszycka wd:[owa] [Kliszczonka?] | — | 12 |\n| Lagierkowa wd:[owa] [Zajączkowa?] | — | 12 |\n| Jakob Grzymek | — | 18 |\n| Antoni Petrykowski | 1 | 6 |\n| Maciey Rycerz | — | 15 |\n| Jakub Kojek [Rojek?] | 1 | 6 |\n| Grzegorz Zdyb | 4 | — |\n| Woyciech Połokowicz | — | 18 |\n| Franciszek Frankowicz | 1 | 6 |\n| Mateusz Ryzik [Ryzak?] | — | 18 |\n| Maciey Cieśla | — | 18 |\n| Z Marcowiczowego | — | 12 |\n| Antoni Okoń | — | 24 |\n| Tamże Chabuś [Judkowicz] | — | 12 |\n| Baltazar Latosowicz | — | 18 |\n| Michał Jędencarz | — | 18 |\n| Antoni Sadowski | — | 12 |\n| Woyciech Latoskowicz [Latosowicz] | — | 18 |\n| Jozef Czapliński | — | 12 |\n| Jan Foliarski | 1 | 10 |\n| Domek Bryczkowy | 1 | — |\n| Piotr Marczyński | — | 18 |\n| Stachowiczka Wd:[owa] | — | 12 |\n| Jan Mulowski | — | 24 |\n| Szymon Nowacki [Nowak?] | 1 | — |\n| Walenta Szafrańska | — | 12 |\n| Antoni Suliczyński | 1 | — |\n| Szymonowa Szayowska | 1 | — |\n| Woyciech Bieniaszowski | 1 | — |\n\n### [Kolumna 2: Miasto Kraśnik – Kontynuacja]\n\n| Posesjonat / Mieszczanin (Śródmieście) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Woyciech Krzeszowski | — | 24 |\n| Mateusz Rycerz | 1 | 6 |\n| Jakob Gąska | — | 12 |\n| Walek Łukasik | — | 18 |\n| Piotr Młynarczyk | — | 9 |\n| Sebastyan Latosowicz | — | 6 |\n| Józef Stembowski [Stemborfski] | 3 | 6 |\n| Antoni Rachon [Rachoń] | — | 24 |\n| Kazimierz Młynarski | 3 | 6 |\n| Fruzyna Wd:[owa] | — | 24 |\n| Sadostka [Sadowska?] | 2 | — |\n| Michał Matuszkiewicz | 4 | 24 |\n| Tomasz Piłaszkiewicz | 1 | 10 |\n| Bujarska Wd:[owa] | — | 12 |\n| Franciszek Wilk | 3 | — |\n| Paweł Fruga | 2 | 10 |\n| Z Ceydlowego | 1 | 12 |\n| Antoni Piasecki | 2 | 10 |\n| Rachuniowa Wd:[owa] | 2 | 12 |\n| Jan Boguta | 1 | 18 |\n| Krasowska wd:[owa] | 1 | 6 |\n| Piotr Podzerz [Połokowicz?] | 2 | 24 |\n| Tokarska Wd:[owa] | — | 24 |\n| Kielachowa Wd:[owa] [Pietrachowa / Piłachowa?] | 1 | 18 |\n| Stach Posoniak [Stanisław] | 1 | 18 |\n| Lanska Wd:[owa] [Łańska] | 1 | 18 |\n| Mik: Radomski [Mikołaj] | 2 | 24 |\n| Witczek Pieciuch [Krzysztof Piecuch?] | 3 | — |\n| Maciey Walczyk [Wołczynski / Wołczyński?] | 1 | 12 |"
  },
  "111": {
    "kategoria": "Taryfy podatkowe / Osiem Sympli / Śródmieście, Piasek i Zarzyce 1777",
    "opis_pozycji": "Dalszy ciąg 8 sympli z 29 II 1777 r.: dokończenie Śródmieścia (Jędrzej Kępa, Kępina, Walenty Jurgiel, Paweł Piasecki, Józef Bańka), pełny rejestr przedmieścia Piasek (Antoni Tkaczyk, Stanisław Wolak, Niewierny Kopiński, Łukasz Tokarczyk) oraz początek Zarzyc (Bartek Czeley, Wawrzyniec Starobrat).",
    "kwoty_miary": "Stawki od 6 gr do 14 zł (Wawrzyniec Starobrat) i 8 zł (Stanisław Wolak, Niewierny Kopiński); Latusy cząstkowe",
    "osoby_podmioty": "Śródmieście: Jędrzej Kępa (Rępa), Marcin Kępa, wdowa Kępina, Walenty Jurgiel, Józef Szpiciarz (Paszkiewicz), Wojciech Fijałkowski, Paweł Piasecki, Maciej Połokowicz, Grzegorz Leśniowski, Szczepan Wójcik (Będęgan), Józef Bańka; Piasek: Antoni Tkaczyk, Stanisław Wolak, Szymon Antonik, Sobek Kilianek, Piotr Kilianek, Jan Bieniek, Marcin Łapa, wdowa Rymarzowa, wdowa Jasiewa, Paweł Jeś, Tomasz Jażdżyk, Maciej Zdyb, Jan Wójcik, Niewierny Kopiński, Mikołaj Nowak, Franciszek Pełka, Jakub Jaczniak, Bartłomiej Zdyb, Franciszek Oszowski, Janowa Gajczykowa, Jakub Jaśkiewicz, Andrzej Gajek, Wojciech Nowak, Wojciech Cwicha, Szymon Wójcik, Wojciech Wiatrek, Paweł Zieliński, Wojciech Pełka, Wojciech Drąg, Łukasz Pełka, Joachim Kłopot, Łukasz Tokarczyk, Michał Tokarczyk, Piotr Tokarczyk, Wojciech Wójcik, Stanisław Kępniak, Barbara Bielecka, Stanisław Wójcik, Wojciech Trojczak, Kazimierz Trojczak, Kazimierz Czelej; Zarzyce: Bartłomiej Czelej, wdowa Łysakowa, Bartłomiej Kilianek, Maciej Szubartowski, wdowa Wiatrkowa (Wroblizna), Grzegorz Jażdżyk, Wawrzyniec Starobrat, Maciej Rachoń, wdowa Cuszkowa (Ciechowa), Szymon Marzec, wdowa Rodzonkowa, Łukasz Kilianek",
    "osoby_skrot": "Paweł Piasecki, Józef Bańka, Stanisław Wolak, Łukasz Tokarczyk, Wawrzyniec Starobrat",
    "transkrypcja": "[Na marginesie prawym:] Pag. 54\nContinuat Ułożenie 8 Miasta Krasnika oraz Przedmieściami d. 29. Febr: 1777 R. Spisane\n\n### [Kolumna 1: Dokończenie Miasta oraz Przedmieście Piasek]\n\n| Posesjonat / Przedmieszczanin | Złote | Grosze |\n| :--- | :---: | :---: |\n| *[Dokończenie Miasta Kraśnika]* | | |\n| Jędrzey Rępa [Kępa] | 2 | 8 |\n| Marc: Rępa [Marcin Kępa] | 1 | — |\n| Kępina Wda [Wdowa] | 2 | — |\n| Walenty Jurgiel | 1 | 18 |\n| Jozef Paszkiewicz [Szpiciarzk / Szpiciarz?] | 1 | 6 |\n| Woyciech Fijałkowski | — | 18 |\n| Paweł Piasecki | 5 | 6 |\n| Maciey Potokowicz [Połokowicz?] | — | 24 |\n| Grzegorz Leszczyński [Leśniowski?] | 1 | 12 |\n| Będęgan Woycik [Szczepan Wójcik?] | — | 18 |\n| Józef Bandia Zbrodzina [Bańka?] | 3 | 6 |\n| *[Przedmieście Piasek]* | | |\n| Antoni Tkaczyk | 5 | — |\n| Stach Wotak [Stanisław Wolak] | 8 | — |\n| Szymon Antonik | 3 | — |\n| Sobek Kielianek [Sebastian Kilianek] | 1 | 15 |\n| Piotr Kielianek [Kilianek] | 4 | — |\n| Jan Bieniek | 3 | 24 |\n| Marcin Łapa | 3 | 20 |\n| Rymarzowa Wda [Wdowa] | 3 | — |\n| Jasiewa Wda [Wdowa] | 5 | 24 |\n| Paweł Jeś | 1 | — |\n| Tomek Jołdzyk [Tomasz Jażdżyk] | 6 | — |\n| Maciey Zdyb | 5 | — |\n| Jan Woycik [Wójcik] | 3 | — |\n| N:[iewierny] Kopiński | 8 | — |\n| Mikołay Nowak | 3 | — |\n| Franc: Petka [Franciszek Pełka / Płachta?] | 3 | — |\n| Jakob Jaczniak | 3 | — |\n| Bartł: Zdyb [Bartłomiej] | 1 | 12 |\n| Franc: Oszowski [Oszoska] | 1 | 6 |\n| Janowa Gayczykowa [Gajczykowa] | 3 | — |\n| Jakob Jasiuricz [Jaśkiewicz / Jasiewicz?] | 5 | 24 |\n| Andrzey Gajek | 2 | 12 |\n| Woyciech Nowak | 5 | — |\n| Woyciech Cwicha [Ćwieka?] | 5 | — |\n| Szymon Woycik [Wójcik] | 2 | 12 |\n| Woyciech Wiatrek | 1 | 12 |\n| Paweł Zieliński | 1 | 12 |\n| Woyciech Petka [Pełka?] | 3 | — |\n| Woyciech Drąg | 3 | — |\n| Łukasz Petka [Pełka?] | 4 | — |\n| Joachim Kłopot | 1 | 12 |\n| Łukasz Tokarczyk | 6 | — |\n| Michał Tokarczyk | 2 | 10 |\n| Piotr Tokarczyk | 3 | — |\n| Woyciech Woycik [Wójcik] | 3 | — |\n| Stach Kępniak [Stanisław] | 3 | — |\n| Barbara Bielecka | 2 | 12 |\n| Stach Woycik [Wójcik] | 1 | 18 |\n| Woyciech Troyczak [Trojczak] | 4 | 10 |\n| Kazimierz Troyczak [Trojczak] | 5 | — |\n| Kazimierz Czeley | 5 | — |\n\n### [Kolumna 2: Przedmieście Zarzyce – Początek]\n\n| Posesjonat / Przedmieszczanin (Zarzyce) | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 4ti Lati** | **172** | **15** |\n| Bartek Czeley [Bartłomiej] | 5 | — |\n| Łysakowa Wda [Wdowa] | 3 | 24 |\n| Bartł: Kielianek [Bartłomiej Kilianek] | 2 | 18 |\n| Maciey Szubartowski | 1 | 12 |\n| Wroblizna [Wiatrkowa Wdowa] | 3 | 18 |\n| Grzegorz Jołdzyk [Jażdżyk] | 3 | 12 |\n| Wawr: Starobrat [Wawrzyniec] | 14 | — |\n| Maciey Rachon [Rachoń] | 3 | — |\n| Ciechowa Wda [Cuszkowa Wdowa] | 2 | 12 |\n| Szymon Marzec | 2 | 18 |\n| Rodzonkowa Wda [Wdowa] | 2 | 12 |\n| Łukasz Kielianek [Kilianek] | 2 | — |"
  },
  "112": {
    "kategoria": "Taryfy podatkowe / Osiem Sympli / Zarzyce oraz Góry i Podlesie 1777",
    "opis_pozycji": "Dokończenie taryfy 8 sympli z 29 II 1777 r.: dokończenie przedmieścia Zarzyce (kolumna 1: Maciej Rodzonek, Andrzej Rządkowski, Sobek Mikołajczyk, Błażej Chruściel) oraz pełny wykaz dla Gór i Podlesia (kolumna 2: Szymon Płachta, Antoni Tokarczyk, Szymon Krzeszowski, Józef Nowak, Sobek Zdyb).",
    "kwoty_miary": "Stawki od 12 gr do 6 zł (Andrzej Rządkowski, Sobek Mikołajczyk, Szymon Krzeszowski); sumy latusów",
    "osoby_podmioty": "Zarzyce: Maciej Rodzonek, Kasper Trojczak, Antoni Wanek, Grzegorz Biegaj, Maciej Piotrowski, Łukasz Rymarz, Andrzej Tokarczyk, Marcin Drąg, Wojciech Wolak (Widak), Marcin Kołton, Marcin Rymarz, wdowa Łapczyna, wdowa Markowa, Andrzej Rządkowski, Kazimierz Ciechoński, Sobek Łysak, Józef Dubaj, wdowa Dubajowa, Kazimierz Drąg (Deryło), Sobek Mikołajczyk, Tomasz Rządkowski, Błażej Chruściel, Łukasz Biegaj, Józef Koza, Maciej Łazarz, Andrzej Łazarz, Antoni Koza, Bartłomiej Grządka, Maciej Kuśnierz, Mikołaj Rępa, Łukasz Koza, Wawrzyniec Rzeszotek, Mikołaj Buczek, Wojciech Biegaj, wdowa Oszustowa, wdowa Młynarczykowa, Stanisław Piotrowski; Góry i Podlesie: Szymon Płachta, Adam Michał, Jan Boguta, Wojciech Gąska, Wojciech Kawka, wdowa Młynarczykowa, Jakub Rządkowski, wdowa Trojczakowa, Fabian Trojczak, Jacek Grzymek, Sobek Trojczak, Maciej Trojczak, Maciej Kępa (Rępa), Mikołaj Kawka, Józef Strażnik, Antoni Tokarczyk, Szymon Krzeszowski, Józef Nowak, Augustyn Gregorczyk, Wawrzyniec Tokarczyk, Józef Gąska, Franciszek Kłopot, Mikołaj Zdyb, Szymon Ćwieka, wdowa Pawlicka, wdowa Grądzina, Jan Wilk, Mateusz Zdyb, wdowa Zimniakowa, wdowa Lenartowa, Tomasz Wilk, Maciej Kawka, Grzegorz Wolak (Widak), Andrzej Kępa (Rępa), Augustyn Kawka, Józef Wilk, Błażej Babicz, Wojciech Kusz, Krzysztof Ćwieka, Benedykt Kawka, Stanisław Pielach (Piłaszkiewicz), Walenty Biegaj, Sobek Zdyb, wdowa Cwichowa",
    "osoby_skrot": "Andrzej Rządkowski, Błażej Chruściel, Szymon Krzeszowski, Antoni Tokarczyk, Sobek Zdyb",
    "transkrypcja": "[Na marginesie lewym:] Continuat | Pag. 54v\n\n### [Kolumna 1: Dokończenie Przedmieścia Zarzyce]\n\n| Posesjonat / Przedmieszczanin (Zarzyce) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Maciey Rodzonek | 5 | — |\n| Gaspar Trojczak [Kacper] | 2 | 8 |\n| Antoni Wanek [Panek?] | 1 | 18 |\n| Grzegorz Biegay | 2 | — |\n| Maciey Piotrowski | 5 | 24 |\n| Euliasz Rymarz [Łukasz Rymarz?] | 3 | 18 |\n| Andrzey Tokarczyk | 2 | — |\n| Mar: Drąg [Marcin] | 4 | — |\n| Woyciech Widak [Wolak?] | 2 | 24 |\n| Mar: Kołton [Marcin] | 2 | — |\n| Marc: Rymarz [Marcin] | 2 | 18 |\n| Łapczyna Wda [Wdowa] | 2 | 12 |\n| Markowa Wda [Wdowa] | 2 | 12 |\n| Andrzey Rządkowski | 6 | — |\n| Kz: Ciechoński [Kazimierz] | 1 | 18 |\n| Sobek Łysak [Sebastian] | 1 | 18 |\n| Józef Dubay [Dubaj] | 2 | 12 |\n| Dubajowa Wda [Wdowa] | 2 | — |\n| Kazimierz Drąg [Deryło?] | 1 | 18 |\n| Sobek Mikołayczyk [Sebastian] | 6 | — |\n| Tomek Rządkowski [Tomasz] | 4 | — |\n| Błach Chruściel [Błażej] | 2 | 12 |\n| Łukasz Biegay | 4 | — |\n| Józef Koza | 3 | — |\n| Maciey Łazarz | 1 | 18 |\n| Andrzey Łazarz | 2 | — |\n| Antoni Koza | 2 | 12 |\n| Bartł: Grządka [Bartłomiej] | 1 | 18 |\n| Maciey Kuśnierz | 3 | — |\n| Mikołay Rępa | 2 | 12 |\n| Łukasz Koza | 2 | 12 |\n| Wawr: Rzeszotek [Wawrzyniec Gęzarek?] | 2 | 12 |\n| Mikołay Buczek | 1 | 18 |\n| Woyciech Biegay | 2 | — |\n| Oszustowa Wda [Wdowa] | 1 | — |\n| Młynarczykowa Wda [Wdowa] | 2 | 12 |\n| Stanisł: Piotrowski [Stanisław] | 3 | — |\n\n### [Kolumna 2: Przedmieście Góry i Podlesie]\n\n| Posesjonat / Przedmieszczanin (Góry i Podlesie) | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 6ti Lati** | **374** | **18** |\n| Szymon Płachta | 2 | 24 |\n| Adam Michał [Adamowicz?] | 1 | — |\n| Jan Boguta | 2 | — |\n| Woyciech Gąska | 1 | 12 |\n| Woyciech Kawka | 3 | 12 |\n| Młynarczykowa Wda [Wdowa] | 4 | — |\n| Jakob Rządkowski | 3 | — |\n| Trojczakowa Wda [Wdowa] | 1 | — |\n| Fabian Trojczak | 1 | 18 |\n| Jacek Grzymek | 3 | — |\n| Sobek Trojczak [Sebastian] | 1 | — |\n| Maciey Brat Jego [Trojczak] | 1 | — |\n| Maciey Rępa [Kępa?] | 1 | — |\n| Mikołay Kawka | 3 | — |\n| Józef Strażnik | 3 | — |\n| Antoni Tokarczyk | 5 | — |\n| Szymon Krzeszowski | 6 | — |\n| Józef Nowak | 5 | — |\n| Augustyn Gregorczyk | 2 | 12 |\n| Wawr: Tokarczyk [Wawrzyniec] | 2 | 12 |\n| Józef Gąska | 5 | — |\n| Franc: Kłopot [Franciszek] | 1 | 18 |\n| Mikołay Zdyb | 1 | — |\n| Szymon Ćwieka | 5 | — |\n| Pawlicka Wda [Wdowa] | 1 | 12 |\n| Grądzina Wda [Wdowa] | 1 | — |\n| Jan Wilk | 1 | 18 |\n| Mateusz Zdyb | 1 | 18 |\n| Zimniakowa Wda [Wdowa] | 3 | 18 |\n| Lenartowa Wda [Wdowa] | 2 | 18 |\n| Tomasz Wilk | 3 | 18 |\n| Maciey Kawka | 2 | 18 |\n| Grzegorz Widak [Wolak?] | 1 | 18 |\n| Andrzey Rępa [Kępa?] | 2 | 24 |\n| Augustyn Kawka | 3 | — |\n| Józef Wilk | 3 | 6 |\n| Błach Babicz [Błażej] | 2 | 12 |\n| Woyciech Kusz | 3 | 18 |\n| Krzysz: Ćwieka [Krzysztof] | — | 18 |\n| Benedykt Kawka | — | 12 |\n| Stanisł: Piłaszkiewicz [Pielach?] | 2 | 24 |\n| Walenty Biegay | 1 | 18 |\n| Sobek Zdyb [Sebastian] | 4 | 18 |\n| Cwichowa Wda [Wdowa Ćwikowa] | 1 | 18 |\n| **In Summa Całego Ułożenia 8 Sympli 1777** | **472** | **12** |"
  },
  "113": {
    "kategoria": "Taryfy podatkowe / Podymne zimowe / Śródmieście 1775",
    "opis_pozycji": "Taryfa „Ułożenie Podymnego na Rathę Zimową 1775to Z Miasta Krasnika y Przedmieściow dę 6. Xbris 1775. A: Spisane”. Początek Śródmieścia (kolumny 1 i 2): stała stawka podymnego 3 złote od dymu/domu miejskiego.",
    "kwoty_miary": "Stawka ryczałtowa podymnego w Śródmieściu: 3 złote od posesji/dymu; 1mus Latus: 120 zł (40 domów); suma częściowa kolumny 2: 45 zł (15 domów)",
    "osoby_podmioty": "Jacek Fiszer, domek Kozyniecki, Paweł Latosowicz, wójt Józef Tokarski, Mikołaj Łapa, Michał Krzanowski, Antoni Krzeszowski, Piotr Gołębiowski, Jakub Szulc, Kazimierz Rycerz, Jakub Rojek (Rosoł), Grzegorz Zdyb, Franciszek Frankowicz, Wojciech Połokowicz, Mateusz Ryzak (Ryzik), Maciej Cieśla, Antoni Okoń, Szymon Nowacki, Baltazar Latosowicz, Wojciech Latosowicz, Michał Jędencarz, Antoni Sadowski, Józef Czapliński, Jan Foliarski, domek Bryczkowy, Piotr Marczyński, Jan Mulowski, Antoni Suliczyński, Szymonowa Szajowska, Wojciech Bieniaszowski, Wojciech Krzeszowski, Mateusz Rycerz, Jakub Gąska, Walenty Łukasik, Piotr Młynarczyk, Sebastian Latosowicz, Józef Stembowski, Antoni Rachoń, Wawrzyniec Piłaszkiewicz, Tomasz Piłaszkiewicz, wdowa Aleksandrowa, Franciszek Wilk (Wilczek), Paweł Fruga (Pruga), Wawrzyniec Starobrat, Antoni Piasecki, Walenta Rachunkowa, Jan Boguta (Beguła), Grzegorz Krasowski, wdowa Łańska, Stanisław Posoniak, wdowa Pietrachowa, wdowa Kotlarska, Piotr Połokowicz, Krzysztof Piłaszkiewicz, Mikołaj Kazimierski",
    "osoby_skrot": "Józef Tokarski wójt, Jacek Fiszer, Grzegorz Zdyb, Wawrzyniec Starobrat, Stanisław Posoniak",
    "transkrypcja": "[Na marginesie górnym:] # 55\nUłożenie Podymnego na Rathę Zimową 1775to\nZ Miasta Krasnika y Przedmieściow dę 6. Xbris\n1775. A: Spisane uti Inferius sequitur –\n\n### [Kolumna 1: Miasto Kraśnik]\n\n| Posesjonat / Mieszczanin (Dym / Dom) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Jacek Fisier [Fiszer] | 3 | — |\n| Domek Kozynieckiy | 3 | — |\n| Paweł Latosowicz | 3 | — |\n| Jozef Tokarski [Wójt] | 3 | — |\n| Mikołay Łapka | 3 | — |\n| Michał Krzanszyski [Krzanowski] | 3 | — |\n| Antoni Krzeszowski | 3 | — |\n| Piotr Gołębiewski [Gołębiowski] | 3 | — |\n| Jakób Szulc | 3 | — |\n| Kazimierz Rycerz | 3 | — |\n| Jakób Rosoł [Rojek?] | 3 | — |\n| Grzegorz Zdyb | 3 | — |\n| Franciszek Frankowicz | 3 | — |\n| Woyciech Potokowicz [Połokowicz] | 3 | — |\n| Mateusz Ryzik [Ryzak?] | 3 | — |\n| Maciey Cieśla | 3 | — |\n| Antoni Okoń | 3 | — |\n| Szymon Nowacki | 3 | — |\n| Baltazar Latosowicz | 3 | — |\n| Woyciech Latosowicz | 3 | — |\n| Michał Jędencarz | 3 | — |\n| Antoni Sadowski | 3 | — |\n| Jozef Czapliński | 3 | — |\n| Jan Foliarski | 3 | — |\n| Domek Bryczkowy | 3 | — |\n| Piotr Marczyński | 3 | — |\n| Jan Mulowski | 3 | — |\n| Antoni Suliszewski [Suliczyński] | 3 | — |\n| Szymonowa Szayowska | 3 | — |\n| Woyciech Bieniaszowski | 3 | — |\n| Woyciech Krzeszowski | 3 | — |\n| Mateusz Rycerz | 3 | — |\n| Jakób Gąska | 3 | — |\n| Walenty Łukasik | 3 | — |\n| Piotr Młynarczyk | 3 | — |\n| Sebastyan Latosowicz | 3 | — |\n| Jozef Stembowski | 3 | — |\n| Antoni Rachon [Rachoń] | 3 | — |\n| Wawrzeniec Piłaszkiewicz | 3 | — |\n| Tomasz Piłaszkiewicz | 3 | — |\n| **1mus Latus (40 domów)** | **120** | **—** |\n\n### [Kolumna 2: Miasto Kraśnik – Kontynuacja]\n\n| Posesjonat / Mieszczanin (Dym / Dom) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Alexandrowa Wda [Wdowa] | 3 | — |\n| Franciszek Wilczek [Wilk?] | 3 | — |\n| Paweł Pruga [Fruga] | 3 | — |\n| Wawrzeniec Starobrat | 3 | — |\n| Antoni Piasecki | 3 | — |\n| Walenta Rachunkowa [Wdowa] | 3 | — |\n| Jan Beguła [Boguta] | 3 | — |\n| Grzegorz Krasowski | 3 | — |\n| Łańska Wda [Wdowa] | 3 | — |\n| Stanisław Posoniak | 3 | — |\n| And:[rzejowa] Pietrachowa Wda [Wdowa] | 3 | — |\n| Kotlarska Wda [Wdowa] | 3 | — |\n| Piotr Potokowicz [Połokowicz] | 3 | — |\n| Kz: Piłaszkiewicz [Kazimierz] | 3 | — |\n| Mikołay Kazimierski | 3 | — |"
  },
  "114": {
    "kategoria": "Taryfy podatkowe / Podymne zimowe / Śródmieście 1775 (Dublet)",
    "opis_pozycji": "Dublet fotograficzny / powtórzenie klatki mikrofilmu skanu 113 (Pag. 55): identyczny rejestr podymnego zimowego z 6 XII 1775 r. dla Śródmieścia Kraśnika.",
    "kwoty_miary": "Identyczne jak na skanie 113: stawka 3 zł od dymu miejskiego; 1mus Latus: 120 zł",
    "osoby_podmioty": "Identyczne jak na skanie 113: Jacek Fiszer, wójt Józef Tokarski, Grzegorz Zdyb, Wawrzyniec Starobrat, Stanisław Posoniak i inni posesjonaci",
    "osoby_skrot": "Józef Tokarski wójt, Jacek Fiszer, Grzegorz Zdyb, Wawrzyniec Starobrat",
    "transkrypcja": "[Dublet fotograficzny skanu 113 – Pag. 55:]\n[Na marginesie górnym:] # 55\nUłożenie Podymnego na Rathę Zimową 1775to\nZ Miasta Krasnika y Przedmieściow dę 6. Xbris\n1775. A: Spisane uti Inferius sequitur –\n\n### [Kolumna 1: Miasto Kraśnik]\n\n| Posesjonat / Mieszczanin (Dym / Dom) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Jacek Fisier [Fiszer] | 3 | — |\n| Domek Kozynieckiy | 3 | — |\n| Paweł Latosowicz | 3 | — |\n| Jozef Tokarski [Wójt] | 3 | — |\n| Mikołay Łapka | 3 | — |\n| Michał Krzanszyski [Krzanowski] | 3 | — |\n| Antoni Krzeszowski | 3 | — |\n| Piotr Gołębiewski [Gołębiowski] | 3 | — |\n| Jakób Szulc | 3 | — |\n| Kazimierz Rycerz | 3 | — |\n| Jakób Rosoł [Rojek?] | 3 | — |\n| Grzegorz Zdyb | 3 | — |\n| Franciszek Frankowicz | 3 | — |\n| Woyciech Potokowicz [Połokowicz] | 3 | — |\n| Mateusz Ryzik [Ryzak?] | 3 | — |\n| Maciey Cieśla | 3 | — |\n| Antoni Okoń | 3 | — |\n| Szymon Nowacki | 3 | — |\n| Baltazar Latosowicz | 3 | — |\n| Woyciech Latosowicz | 3 | — |\n| Michał Jędencarz | 3 | — |\n| Antoni Sadowski | 3 | — |\n| Jozef Czapliński | 3 | — |\n| Jan Foliarski | 3 | — |\n| Domek Bryczkowy | 3 | — |\n| Piotr Marczyński | 3 | — |\n| Jan Mulowski | 3 | — |\n| Antoni Suliszewski [Suliczyński] | 3 | — |\n| Szymonowa Szayowska | 3 | — |\n| Woyciech Bieniaszowski | 3 | — |\n| Woyciech Krzeszowski | 3 | — |\n| Mateusz Rycerz | 3 | — |\n| Jakób Gąska | 3 | — |\n| Walenty Łukasik | 3 | — |\n| Piotr Młynarczyk | 3 | — |\n| Sebastyan Latosowicz | 3 | — |\n| Jozef Stembowski | 3 | — |\n| Antoni Rachon [Rachoń] | 3 | — |\n| Wawrzeniec Piłaszkiewicz | 3 | — |\n| Tomasz Piłaszkiewicz | 3 | — |\n| **1mus Latus (40 domów)** | **120** | **—** |\n\n### [Kolumna 2: Miasto Kraśnik – Kontynuacja]\n\n| Posesjonat / Mieszczanin (Dym / Dom) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Alexandrowa Wda [Wdowa] | 3 | — |\n| Franciszek Wilczek [Wilk?] | 3 | — |\n| Paweł Pruga [Fruga] | 3 | — |\n| Wawrzeniec Starobrat | 3 | — |\n| Antoni Piasecki | 3 | — |\n| Walenta Rachunkowa [Wdowa] | 3 | — |\n| Jan Beguła [Boguta] | 3 | — |\n| Grzegorz Krasowski | 3 | — |\n| Łańska Wda [Wdowa] | 3 | — |\n| Stanisław Posoniak | 3 | — |\n| And:[rzejowa] Pietrachowa Wda [Wdowa] | 3 | — |\n| Kotlarska Wda [Wdowa] | 3 | — |\n| Piotr Potokowicz [Połokowicz] | 3 | — |\n| Kz: Piłaszkiewicz [Kazimierz] | 3 | — |\n| Mikołay Kazimierski | 3 | — |"
  },
  "115": {
    "kategoria": "Taryfy podatkowe / Podymne zimowe / Izby przy browarach, Góry i Podlesie, Piasek 1775",
    "opis_pozycji": "Dalszy ciąg podymnego zimowego z 6 XII 1775 r.: dokończenie Śródmieścia (kolumna 1), unikalna rejestracja izb przy browarach miejskich (Tokarski z Fiszerem, Paszkiewicz, Łaska, Krzanowski z Połokowiczem, Fruga, Rycerz, Szubartowski), pełny spis przedmieścia Góry i Podlesie (stawka 2 zł) oraz początek Piasku (kolumna 2).",
    "kwoty_miary": "Izby browarne: 1 zł; podymne przedmiejskie: 2 zł od dymu/chałupy; 2dus Latus: 27 zł; Latus Gór i Podlesia: 74 zł (37 dymów)",
    "osoby_podmioty": "Śródmieście i browary: Maciej Walczyński, Jędrzej Kępa, Paweł Piasecki, Szczepan Wójcik, Grzegorz Leśniowski, Maciej Połokowicz, Wojciech Fijałkowski, wdowa Kępina, Walenty Jurgiel, Józef Tokarski z Jackiem Fiszerem, Józef Paszkiewicz, Jakub Łaska, Michał Krzanowski z Wojciechem Połokowiczem, Paweł Fruga, Kazimierz Rycerz, Sebastian Szubartowski; Góry i Podlesie: Szymon Płachta, Adam Michał, Jan Boguta, Wojciech Gąska, Wojciech Kawka, wdowa Młynarczykowa, Jakub Rządkowski, wdowa Trojczakowa, Fabian Trojczak, Jacek Grzymek, Sobek Trojczak, Maciej Trojczak, Maciej Kępa, Mikołaj Kawka, Józef Strażnik, Antoni Tokarczyk, Szymon Krzeszowski, Józef Nowak, Augustyn Gregorczyk, Wawrzyniec Tokarczyk, Józef Gąska, Franciszek Kłopot, Mikołaj Zdyb, Szymon Ćwieka, Jan Wilk, Tomasz Wilk, Maciej Kawka, Grzegorz Wolak, Andrzej Kępa, Augustyn Kawka, Józef Wilk, Wojciech Kusz, Krzysztof Ćwieka, Walenty Biegaj, Stanisław Pielach, Sebastian Zdyb, Grzegorz Dziadka; Piasek: Antoni Tkaczyk, Stanisław Wolak, Szymon Antonik, wdowa Pyzikowa, Piotr Kilianek, Jan Bieniek, Marcin Łapa, wdowa Rymarzowa, wdowa Jasiewa, Tomasz Jażdżyk, Maciej Zdyb",
    "osoby_skrot": "Józef Tokarski, Jacek Fiszer, Paweł Fruga, Szymon Krzeszowski, Antoni Tokarczyk, Stanisław Wolak",
    "transkrypcja": "[Na marginesie górnym:] Pag. 55v\n\n### [Kolumna 1: Dokończenie Miasta, Izby Browarne oraz Góry i Podlesie]\n\n| Posesjonat / Przedmieszczanin | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 2di Lati [Dokończenie Miasta]** | | |\n| Maciey Walczyński | 3 | — |\n| Jędrzey Rępa [Kępa] | 3 | — |\n| Paweł Piasecki | 3 | — |\n| Szczepan Woycik [Wójcik] | 3 | — |\n| Grzegorz Leszczyński [Leśniowski] | 3 | — |\n| Maciey Potokowicz [Połokowicz] | 3 | — |\n| Woyciech Fijatkowski [Fijałkowski] | 3 | — |\n| Kępina Wda [Wdowa] | 3 | — |\n| Walenty Jurgiel | 3 | — |\n| *[Z Yzbow przy Browarach]* | | |\n| Jozef Tokarski z Fisierem [Fiszerem] | 1 | — |\n| Jozef Paszkiewicz | 1 | — |\n| Jakub Łaska | 1 | — |\n| Krzanowski z Potokowiczem | 1 | — |\n| Paweł Fruga | 1 | — |\n| Kazimierz Rycerz | 1 | — |\n| Seb:[astyan] Szubartowski | 1 | — |\n| *[Przedmieście Gory y Podlesie]* | | |\n| Szymon Płachta | 2 | — |\n| Adam Michał [Adamowicz?] | 2 | — |\n| Jan Boguta | 2 | — |\n| Woyciech Gąska | 2 | — |\n| Woyciech Kawka | 2 | — |\n| Młynarczykowa Wda [Wdowa] | 2 | — |\n| Jakób Rządkowski | 2 | — |\n| Trojczakowa Wda [Wdowa] | 2 | — |\n| Fabian Trojczak | 2 | — |\n| Jacek Grzymek | 2 | — |\n| Sobek Trojczak [Sebastian] | 2 | — |\n| Maciey Trojczak Brat Jego | 2 | — |\n| Maciey Rępa [Kępa] | 2 | — |\n| Mikołay Kawka | 2 | — |\n| Józef Strażnik | 2 | — |\n| Antoni Tokarczyk | 2 | — |\n| Szymon Krzeszowski | 2 | — |\n| Józef Nowak | 2 | — |\n| Augustyn Gregorczyk | 2 | — |\n| Wawrzek Tokarczyk [Wawrzyniec] | 2 | — |\n| Józef Gąska | 2 | — |\n| Franciszek Kłopot | 2 | — |\n| Mikołay Zdyb | 2 | — |\n| Szymon Ćwieka | 2 | — |\n| Jan Wilk | 2 | — |\n| Tomasz Wilk | 2 | — |\n| Maciey Kawka | 2 | — |\n| Grzegorz Wolak [Widak?] | 2 | — |\n| Andrzey Rępa [Kępa] | 2 | — |\n| Augustyn Kawka | 2 | — |\n| Józef Wilk | 2 | — |\n| Woyciech Kusz | 2 | — |\n| Krzysz:[tof] Ćwieka | 2 | — |\n| Walenty Biegay | 2 | — |\n| Stanisław Pielach | 2 | — |\n| Seba:[styan] Zdyb | 2 | — |\n| Grzegorz Dziadka | 2 | — |\n\n### [Kolumna 2: Przedmieście Piasek – Początek]\n\n| Posesjonat / Przedmieszczanin (Piasek) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Antoni Tkaczyk | 2 | — |\n| Stanisł: Wotak [Wolak] | 2 | — |\n| Szymon Antonik | 2 | — |\n| Ant:[oniowa] Pyzikowa [Wdowa] | 2 | — |\n| Piotr Kielianek [Kilianek] | 2 | — |\n| Jan Bieniek | 2 | — |\n| Marcin Łapa | 2 | — |\n| Rymarzowa Wda [Wdowa] | 2 | — |\n| Jesiona Wda [Wdowa] | 2 | — |\n| Tomek Jołdzyk [Tomasz Jażdżyk] | 2 | — |\n| Maciey Zdyb | 2 | — |"
  },
  "116": {
    "kategoria": "Taryfy podatkowe / Podymne zimowe / Przedmieścia Piasek i Zarzyce 1775",
    "opis_pozycji": "Dalszy ciąg podymnego zimowego z 6 XII 1775 r.: dokończenie przedmieścia Piasek (kolumna 1: 29 dymów po 2 zł, m.in. ks. Koziński, Łukasz Tokarczyk, Barbara Bielecka, Kazimierz Czelej) oraz rejestr przedmieścia Zarzyce (kolumna 1 i 2: 41 dymów po 2 zł, odnotowany Folwark w Granicach i chałupa poddanego).",
    "kwoty_miary": "Podymne przedmiejskie: 2 zł od dymu; 4tus Latus (Piasek): 80 zł; 5tus Latus (Zarzyce): 82 zł",
    "osoby_podmioty": "Piasek: Jan Wójcik, ks. Koziński, Mikołaj Nowak, Franciszek Pełka, Jakub Jaczniak, Bartłomiej Zdyb, Katarzyna Ossowska, Janowa Gajczykowa, Jakub Jaśkiewicz, Wojciech Czelej, Andrzej Dąbek, Wojciech Nowak, Szymon Wójcik, Wojciech Wziątek, Paweł Zieliński, Wojciech Pełka, Wojciech Drąg, Łukasz Pełka, Joachim Kłopot, Łukasz Tokarczyk, Michał Tokarczyk, Piotr Tokarczyk, Wojciech Wójcik, Stanisław Kępniak, Barbara Bielecka, Stanisław Wójcik, Wojciech Trojczak, Kazimierz Trojczak, Kazimierz Czelej; Zarzyce: Bartłomiej Czelej, wdowa Łysakowa, Bartłomiej Kilianek, Maciej Szubartowski, wdowa Wiatrkowa, Grzegorz Jażdżyk, Wawrzyniec Starobrat, Maciej Rachoń, wdowa Ciechowa, Szymon Marzec, wdowa Rodzonkowa, Łukasz Kilianek, Maciej Rodzonek, Kasper Trojczak, Antoni Wanek, Grzegorz Biegaj, Maciej Piotrowski, Łukasz Rymarz, Andrzej Tokarczyk, Marcin Drąg, Wojciech Wolak, Marcin Kołton, Marcin Rymarz, wdowa Łapczyna, wdowa Markowa, Andrzej Rządkowski, Kazimierz Ciechoński, Sebastian Łysak, Józef Dubaj, wdowa Dubajowa, Kazimierz Drąg, Sobek Mikołajczyk, Tomasz Rządkowski, Łukasz Biegaj, Folwark Granice (od poddanego), Józef Koza, Maciej Łazarz, Kasper Rodzonek, Stanisław Wojtka, Antoni Koza",
    "osoby_skrot": "ks. Koziński, Łukasz Tokarczyk, Wawrzyniec Starobrat, Andrzej Rządkowski, Folwark Granice",
    "transkrypcja": "[Na marginesie górnym:] Pag. 56\n\n### [Kolumna 1: Dokończenie Piasku oraz Początek Zarzyc]\n\n| Posesjonat / Przedmieszczanin | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 4ti Lati [Continuat Piasek]** | | |\n| Jan Woycik [Wójcik] | 2 | — |\n| Xz: Kozinski [Ksiądz Koziński] | 2 | — |\n| Mikołay Nowak | 2 | — |\n| Franc: Petka [Franciszek Pełka / Płachta?] | 2 | — |\n| Jakób Jaczniak | 2 | — |\n| Bartł: Zdyb [Bartłomiej] | 2 | — |\n| Katarzyna Ossowska | 2 | — |\n| Janowa Gayczykowa [Gajczykowa] | 2 | — |\n| Jakób Jasiuricz [Jaśkiewicz / Jasiłowicz?] | 2 | — |\n| Woyciech Czeley | 2 | — |\n| Andrzey Dąbek | 2 | — |\n| Woyciech Nowak | 2 | — |\n| Szymon Woycik [Wójcik] | 2 | — |\n| Woyciech Wziątek | 2 | — |\n| Paweł Zieliński | 2 | — |\n| Woyciech Petka [Pełka?] | 2 | — |\n| Woyciech Drąg | 2 | — |\n| Łukasz Petka [Pełka?] | 2 | — |\n| Joachim Kłopot | 2 | — |\n| Łukasz Tokarczyk | 2 | — |\n| Michał Tokarczyk | 2 | — |\n| Piotr Tokarczyk | 2 | — |\n| Woyciech Woycik [Wójcik] | 2 | — |\n| Stach Kępniak [Stanisław] | 2 | — |\n| Barbara Bielecka | 2 | — |\n| Stach Woycik [Wójcik] | 2 | — |\n| Woyciech Trojczak | 2 | — |\n| Kazimierz Trojczak | 2 | — |\n| Kazimierz Czeley | 2 | — |\n| *[Przedmieście Zarzyce]* | | |\n| Bartek Czeley [Bartłomiej] | 2 | — |\n| Łysakowa Wda [Wdowa] | 2 | — |\n| Bartł: Kielianek [Bartłomiej Kilianek] | 2 | — |\n| Maciey Szubartowski | 2 | — |\n| Wiatrkowa Wda [Wdowa] | 2 | — |\n| Grzegorz Jołdzyk [Jażdżyk] | 2 | — |\n| Wawrzyniec Starobrat | 2 | — |\n| Maciey Rachon [Rachoń] | 2 | — |\n| Ciechowa Wda [Cuszkowa Wdowa] | 2 | — |\n| Szymon Marzec | 2 | — |\n| Rodzonkowa Wda [Wdowa] | 2 | — |\n| Łukasz Kielianek [Kilianek] | 2 | — |\n\n### [Kolumna 2: Przedmieście Zarzyce – Kontynuacja]\n\n| Posesjonat / Przedmieszczanin (Zarzyce) | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 5ti Lati** | | |\n| Maciey Rodzonek | 2 | — |\n| Gaspar Trojczak [Kacper] | 2 | — |\n| Antoni Wanek [Panek?] | 2 | — |\n| Grzegorz Biegay | 2 | — |\n| Maciey Piotrowski | 2 | — |\n| Łukasz Rymarz | 2 | — |\n| Andrzey Tokarczyk | 2 | — |\n| Marcin Drąg | 2 | — |\n| Woyciech Widak [Wolak?] | 2 | — |\n| Marcin Kołton | 2 | — |\n| Marcin Rymarz | 2 | — |\n| Łapczyna Wda [Wdowa] | 2 | — |\n| Markowa Wda [Wdowa] | 2 | — |\n| Andrzey Rządkowski | 2 | — |\n| Kazimierz Ciechoński | 2 | — |\n| Sebastyan Łysak | 2 | — |\n| Józef Dubay [Dubaj] | 2 | — |\n| Dubajowa Wda [Wdowa] | 2 | — |\n| Kazimierz Drąg | 2 | — |\n| Sobek Mikołayczyk [Sebastian] | 2 | — |\n| Tomek Rządkowski [Tomasz] | 2 | — |\n| Łukasz Biegay | 2 | — |\n| Z Folwarku Granic | 2 | — |\n| Od Poddanego [Tegoż Folwarku] | 2 | — |\n| Jozef Koza | 2 | — |\n| Maciey Łazarz | 2 | — |\n| Kasper Rodzonek | 2 | — |\n| Stach Woytka [Stanisław Wojtka] | 2 | — |\n| Antoni Koza | 2 | — |"
  },
  "117": {
    "kategoria": "Taryfy podatkowe / Podymne zimowe 1775 (finał) i Podymne marcowe 1776 (początek) / Zarzyce i Śródmieście",
    "opis_pozycji": "1. Zamknięcie podymnego zimowego 1775 r. dla Zarzyc (8 ostatnich posesji po 2 zł: Dziadka, Kuśnierz, Rępa, Koza, Rzeszotek, Buczek, Młynarczykowa, Piotrowski; In Summa); 2. Nowa taryfa podymnego spisana 29 II 1776 r. na ratę marcową dla Śródmieścia (kolumny 1 i 2, stawka 3 zł).",
    "kwoty_miary": "Dokończenie podymnego zimowego: 16 zł (6tus Latus); podymne marcowe 1776: 3 zł od dymu miejskiego; 1mus Latus marcowy: 117 zł",
    "osoby_podmioty": "Zarzyce (1775): Bartłomiej Dziadka, Maciej Kuśnierz, Mikołaj Rępa, Łukasz Koza, Wawrzyniec Rzeszotek, Mikołaj Buczek, wdowa Młynarczykowa, Stanisław Piotrowski; Śródmieście (1776): Jacek Fiszer, domek Kozyniecki, Paweł Latosowicz, wójt Józef Tokarski, Mikołaj Łapka, Michał Krzanowski, Antoni Krzeszowski, Piotr Gołębiowski, Jakub Szulc, Kazimierz Rycerz, Jakub Rojek (Rosoł), Grzegorz Zdyb, Franciszek Frankowicz, Wojciech Połokowicz, Mateusz Ryzak, Maciej Cieśla, Antoni Okoń, Szymon Nowacki, Baltazar Latosowicz, Wojciech Latosowicz, Michał Jędencarz, Antoni Sadowski, Józef Czapliński, Jan Foliarski, domek Bryczkowy, Piotr Marczyński, Jan Mulowski, Antoni Suliczyński, Szymonowa Szajowska, Wojciech Bieniaszowski, Wojciech Krzeszowski, Mateusz Rycerz, Jakub Gąska, Walenty Łukasik, Piotr Młynarczyk, Sebastian Latosowicz, Józef Stembowski, Antoni Rachoń, Wawrzyniec Piłaszkiewicz, Tomasz Piłaszkiewicz, wdowa Aleksandrowa, Franciszek Wilk, Paweł Fruga, Wawrzyniec Starobrat, Antoni Piasecki, Walenta Rachunkowa, Jan Boguta, Grzegorz Krasowski, wdowa Łańska, Stanisław Posoniak, wdowa Pietrachowa, wdowa Kotlarska, Piotr Połokowicz",
    "osoby_skrot": "Bartłomiej Dziadka, Józef Tokarski wójt, Jacek Fiszer, Grzegorz Zdyb, Wawrzyniec Starobrat",
    "transkrypcja": "[Na marginesie górnym:] Pag. 56v\n\n### [Kolumna 1: Dokończenie Zarzyc 1775 oraz Nowy Regestr Marcowy 1776]\n\n| Posesjonat / Przedmieszczanin (Podymne Zimowe 1775) | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 6ti Lati [Continuat Zarzyce]** | | |\n| Bartł: Dziadka [Bartłomiej] | 2 | — |\n| Maciey Kuśnierz | 2 | — |\n| Mikołay Rępa | 2 | — |\n| Łukasz Koza | 2 | — |\n| Wawr: Rzeszotek [Wawrzyniec] | 2 | — |\n| Mikołay Buczek | 2 | — |\n| Młynarczykowiczowa Wda [Młynarczykowa Wdowa] | 2 | — |\n| Stanisł: Piotrowski [Stanisław] | 2 | — |\n| **In Summa Zarzyc** | **98** | **—** |\n\n---\n\n*Na Rathę Marcową 1776 R. 29 Febr: Spisany Regestr Podymnego*\n\n| Posesjonat / Mieszczanin (Śródmieście 1776) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Jacek Fisier [Fiszer] | 3 | — |\n| Domek Kozynieckiy | 3 | — |\n| Paweł Latosowicz | 3 | — |\n| Jozef Tokarski [Wójt] | 3 | — |\n| Mikołay Łapka | 3 | — |\n| Michał Krzanowski | 3 | — |\n| Antoni Krzeszowski | 3 | — |\n| Piotr Gołębiewski [Gołębiowski] | 3 | — |\n| Jakób Szulc | 3 | — |\n| Kazimierz Rycerz | 3 | — |\n| Jakób Rosoł [Rojek?] | 3 | — |\n| Grzegorz Zdyb | 3 | — |\n| Franciszek Frankowicz | 3 | — |\n| Woyciech Potokowicz [Połokowicz] | 3 | — |\n| Mateusz Ryzik [Ryzak?] | 3 | — |\n| Maciey Cieśla | 3 | — |\n| Antoni Okoń | 3 | — |\n| Szymon Nowacki | 3 | — |\n| Baltazar Latosowicz | 3 | — |\n| Woyciech Latosowicz | 3 | — |\n| Michał Jędencarz | 3 | — |\n| Antoni Sadowski | 3 | — |\n| Jozef Czapliński | 3 | — |\n| Jan Foliarski | 3 | — |\n| Domek Bryczkowy | 3 | — |\n| Piotr Marczyński | 3 | — |\n| Jan Mulowski | 3 | — |\n| Antoni Suliczyński | 3 | — |\n| Szymonowa Szayowska | 3 | — |\n| Woyciech Bieniaszowski | 3 | — |\n| Woyciech Krzeszowski | 3 | — |\n| Mateusz Rycerz | 3 | — |\n| Jakób Gąska | 3 | — |\n| Walenty Łukasik | 3 | — |\n| Piotr Młynarczyk | 3 | — |\n| Sebastyan Latosowicz | 3 | — |\n| Jozef Stembowski | 3 | — |\n| Antoni Rachon [Rachoń] | 3 | — |\n| Wawrzeniec Piłaszkiewicz | 3 | — |\n| **1mus Latus (39 domów)** | **117** | **—** |\n\n### [Kolumna 2: Śródmieście – Kontynuacja]\n\n| Posesjonat / Mieszczanin (Śródmieście 1776) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Tomasz Piłaszkiewicz | 3 | — |\n| Alexandrowa Wda [Wdowa] | 3 | — |\n| Franciszek Wilczek [Wilk?] | 3 | — |\n| Paweł Fruga [Pruga] | 3 | — |\n| Wawrzyniec Starobrat | 3 | — |\n| Antoni Piasecki | 3 | — |\n| Walenta Rachunkowa [Wdowa] | 3 | — |\n| Jan Beguła [Boguta] | 3 | — |\n| Grzegorz Krasoski [Krasowski] | 3 | — |\n| Łańska Wda [Wdowa] | 3 | — |\n| Stanisław Posoniak | 3 | — |\n| Ant:[oniowa] Pietrachowa [Wdowa] | 3 | — |\n| Kotlarska Wda [Wdowa] | 3 | — |\n| Piotr Potokowicz [Połokowicz] | 3 | — |"
  },
  "118": {
    "kategoria": "Taryfy podatkowe / Podymne marcowe / Izby browarne, Góry i Podlesie, Piasek 1776",
    "opis_pozycji": "Dalszy ciąg podymnego na ratę marcową 1776 r. (z 29 II 1776): dokończenie Śródmieścia (kolumna 1), izby przy browarach miejskich (Tokarski z Fiszerem, Paszkiewicz, Łaska, Krzanowski z Połokowiczem, Fruga, Rycerz, Szubartowski), pełny rejestr Gór i Podlesia (kolumna 1: 38 dymów po 2 zł, w tym Regina Ćwikowa) oraz początek Piasku (kolumna 2).",
    "kwoty_miary": "Dokończenie Śródmieścia: 33 zł; izby browarne: po 1 zł; Góry i Podlesie: 76 zł (38 dymów po 2 zł); Piasek (początek): 16 zł (8 dymów)",
    "osoby_podmioty": "Śródmieście i browary: Krzysztof Piłaszkiewicz, Mikołaj Kazimierski, Maciej Walczyński, Jędrzej Kępa, Paweł Piasecki, Szczepan Wójcik, Grzegorz Leśniowski, Maciej Połokowicz, Wojciech Fijałkowski, wdowa Kępina, Walenty Jurgiel, Józef Tokarski z Jackiem Fiszerem, Józef Paszkiewicz, Jakub Łaska, Michał Krzanowski z Wojciechem Połokowiczem, Paweł Fruga, Kazimierz Rycerz, Sebastian Szubartowski; Góry i Podlesie: Szymon Płachta, Adam Michał, Jan Boguta, Wojciech Gąska, Wojciech Kawka, wdowa Młynarczykowa, Jakub Rządkowski, wdowa Trojczakowa, Fabian Trojczak, Jacek Grzymek, Sobek Trojczak, Maciej Trojczak, Maciej Kępa, Mikołaj Kawka, Józef Strażnik, Antoni Tokarczyk, Szymon Krzeszowski, Józef Nowak, Augustyn Gregorczyk, Wawrzyniec Tokarczyk, Józef Gąska, Franciszek Kłopot, Mikołaj Zdyb, Szymon Ćwieka, Jan Wilk, Tomasz Wilk, Maciej Kawka, Grzegorz Wolak, Andrzej Kępa, Augustyn Kawka, Józef Wilk, Wojciech Kusz, Krzysztof Ćwieka, Walenty Biegaj, Stanisław Pielach, Sebastian Zdyb, Grzegorz Dziadka, Regina Ćwikowa; Piasek: Antoni Tkaczyk, Stanisław Wolak, Szymon Antonik, wdowa Pyzikowa, Piotr Kilianek, Jan Bieniek, Marcin Łapa, wdowa Rymarzowa",
    "osoby_skrot": "Józef Tokarski wójt, Jacek Fiszer, Regina Ćwikowa, Antoni Tkaczyk, Stanisław Wolak",
    "transkrypcja": "[Na marginesie górnym:] Pag. 57\n\n### [Kolumna 1: Dokończenie Miasta, Browary oraz Góry i Podlesie]\n\n| Posesjonat / Przedmieszczanin | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 2di Lati [Dokończenie Miasta]** | | |\n| Krz: Piłaszkiewicz [Krzysztof] | 3 | — |\n| Mikołay Kazimierski | 3 | — |\n| Maciey Walczyński | 3 | — |\n| Jędrzey Rępa [Kępa] | 3 | — |\n| Paweł Piasecki | 3 | — |\n| Szczepan Woycik [Wójcik] | 3 | — |\n| Grzegorz Lesznieski [Leśniowski] | 3 | — |\n| Maciey Potokowicz [Połokowicz] | 3 | — |\n| Woy:[ciech] Fijałkowski | 3 | — |\n| Kępina Wda [Wdowa] | 3 | — |\n| Walenty Jurgiel | 3 | — |\n| *[Z Yzbow przy Browarach]* | | |\n| Jozef Tokarski z Fisierem [Fiszerem] | 1 | — |\n| Jozef Paszkiewicz | 1 | — |\n| Jakub Łaska | 1 | — |\n| Krzanowski z Potokowiczem | 1 | — |\n| Paweł Fruga | 1 | — |\n| Kazimierz Rycerz | 1 | — |\n| Sebas:[tyan] Szubartowski | 1 | — |\n| #### [Przedmieście Góry i Podlesie] | | |\n| Szymon Płachta | 2 | — |\n| Adam Michał [Adamowicz?] | 2 | — |\n| Jan Boguta | 2 | — |\n| Woyciech Gąska | 2 | — |\n| Woyciech Kawka | 2 | — |\n| Młynarczykowa Wda [Wdowa] | 2 | — |\n| Jakób Rządkowski | 2 | — |\n| Trojczakowa Wda [Wdowa] | 2 | — |\n| Fabian Trojczak | 2 | — |\n| Jacek Grzymek | 2 | — |\n| Sobek Trojczak [Sebastian] | 2 | — |\n| Maciey Trojczak | 2 | — |\n| Maciey Rępa [Kępa] | 2 | — |\n| Mikołay Kawka | 2 | — |\n| Józef Strażnik | 2 | — |\n| Antoni Tokarczyk | 2 | — |\n| Szymon Krzeszowski | 2 | — |\n| Józef Nowak | 2 | — |\n| Augustyn Gregorczyk | 2 | — |\n| Wawrzek Tokarczyk [Wawrzyniec] | 2 | — |\n| Józef Gąska | 2 | — |\n| Franciszek Kłopot | 2 | — |\n| Mikołay Zdyb | 2 | — |\n| Szymon Ćwieka | 2 | — |\n| Jan Wilk | 2 | — |\n| Tomasz Wilk | 2 | — |\n| Maciey Kawka | 2 | — |\n| Grzegorz Widak [Wolak?] | 2 | — |\n| Andrzey Rępa [Kępa] | 2 | — |\n| Augustyn Kawka | 2 | — |\n| Józef Wilk | 2 | — |\n| Woyciech Kusz | 2 | — |\n| Krzysz:[tof] Ćwieka | 2 | — |\n| Walenty Biegay | 2 | — |\n| Stach Pielach [Stanisław] | 2 | — |\n| Seba:[styan] Zdyb | 2 | — |\n| Grzegorz Dziadka | 2 | — |\n| Regina Ćwikowa | 2 | — |\n\n### [Kolumna 2: Przedmieście Piasek – Początek]\n\n| Posesjonat / Przedmieszczanin (Piasek) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Antoni Tkaczyk | 2 | — |\n| Stanisł: Wotak [Wolak] | 2 | — |\n| Szymon Antonik | 2 | — |\n| Pyzikowa Wda [Wdowa] | 2 | — |\n| Piotr Kielianek [Kilianek] | 2 | — |\n| Jan Bieniek | 2 | — |\n| Marcin Łapa | 2 | — |\n| Rymarzowa Wda [Wdowa] | 2 | — |"
  },
  "119": {
    "kategoria": "Taryfy podatkowe / Podymne marcowe / Przedmieścia Piasek i Zarzyce 1776",
    "opis_pozycji": "Dalszy ciąg podymnego na ratę marcową 1776 r.: dokończenie przedmieścia Piasek (kolumna 1: 32 dymy po 2 zł) oraz rejestr przedmieścia Zarzyce (kolumna 1 i 2: 45 posesji po 2 zł, Folwark w Granicach, chałupa poddanego).",
    "kwoty_miary": "Podymne przedmiejskie: 2 zł od posesji; 4tus Latus (Piasek): 80 zł; 5tus Latus (Zarzyce): 90 zł",
    "osoby_podmioty": "Piasek: wdowa Jesiona, Tomasz Jażdżyk, Maciej Zdyb, Jan Wójcik, ks. Koziński, Mikołaj Nowak, Franciszek Pełka, Jakub Jaczniak, Bartłomiej Zdyb, Katarzyna Ossowska, Janowa Gajczykowa, Jakub Jaśkiewicz, Wojciech Czelej, Andrzej Dąbek, Wojciech Nowak, Szymon Wójcik, Wojciech Wziątek, Paweł Zieliński, Wojciech Pełka, Wojciech Drąg, Łukasz Pełka, Joachim Kłopot, Łukasz Tokarczyk, Michał Tokarczyk, Piotr Tokarczyk, Wojciech Wójcik, Stanisław Kępniak, Barbara Bielecka, Stanisław Wójcik, Wojciech Trojczak, Kazimierz Trojczak, Kazimierz Czelej; Zarzyce: Bartłomiej Czelej, wdowa Łysakowa, Bartłomiej Kilianek, Maciej Szubartowski, wdowa Wiatrkowa, Grzegorz Jażdżyk, Wawrzyniec Starobrat, Maciej Rachoń, wdowa Ciechowa, Szymon Marzec, wdowa Rodzonkowa, Łukasz Kilianek, Maciej Rodzonek, Kasper Trojczak, Antoni Wanek, Grzegorz Biegaj, Maciej Piotrowski, Łukasz Rymarz, Andrzej Tokarczyk, Marcin Drąg, Wojciech Wolak, Marcin Kołton, Marcin Rymarz, wdowa Łapczyna, wdowa Markowa, Andrzej Rządkowski, Kazimierz Ciechoński, Sebastian Łysak, Józef Dubaj, wdowa Dubajowa, Kazimierz Drąg, Sobek Mikołajczyk, Tomasz Rządkowski, Łukasz Biegaj, Folwark Granice (od poddanego), Józef Koza, Maciej Łazarz, Kasper Rodzonek, Jędrzej Łazarz, Antoni Koza, Bartłomiej Dziadka, Maciej Kuśnierz, Mikołaj Rępa, Łukasz Koza",
    "osoby_skrot": "ks. Koziński, Łukasz Tokarczyk, Wawrzyniec Starobrat, Andrzej Rządkowski, Jędrzej Łazarz",
    "transkrypcja": "[Na marginesie górnym:] Pag. 57v\n\n### [Kolumna 1: Dokończenie Piasku oraz Początek Zarzyc]\n\n| Posesjonat / Przedmieszczanin | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 4ti Lati [Continuat Piasek]** | | |\n| Jesiorna Wdowa [Jasiewa?] | 2 | — |\n| Tomek Jołdzyk [Tomasz Jażdżyk] | 2 | — |\n| Maciey Zdyb | 2 | — |\n| Jan Woycik [Wójcik] | 2 | — |\n| Xz: Kozinski [Ksiądz Koziński] | 2 | — |\n| Mikołay Nowak | 2 | — |\n| Franc: Petka [Franciszek Pełka / Płachta?] | 2 | — |\n| Jakob Jaczniak | 2 | — |\n| Bartł: Zdyb [Bartłomiej] | 2 | — |\n| Katarzyna Ostrowska [Ossowska] | 2 | — |\n| Janowa Gayczykowa [Gajczykowa] | 2 | — |\n| Jakob Jasiuricz [Jaśkiewicz / Jasiewicz?] | 2 | — |\n| Woyciech Czeley | 2 | — |\n| Andrzey Dąbek | 2 | — |\n| Woyciech Nowak | 2 | — |\n| Szymon Woycik [Wójcik] | 2 | — |\n| Woyciech Wziątek | 2 | — |\n| Paweł Zieliński | 2 | — |\n| Woyciech Petka [Pełka?] | 2 | — |\n| Woyciech Drąg | 2 | — |\n| Łukasz Petka [Pełka?] | 2 | — |\n| Joachim Kłopot | 2 | — |\n| Łukasz Tokarczyk | 2 | — |\n| Michał Tokarczyk | 2 | — |\n| Piotr Tokarczyk | 2 | — |\n| Woyciech Woycik [Wójcik] | 2 | — |\n| Stach Kępniak [Stanisław] | 2 | — |\n| Barbara Bielecka | 2 | — |\n| Stach Woycik [Wójcik] | 2 | — |\n| Woyciech Trojczak | 2 | — |\n| Kazimierz Trojczak | 2 | — |\n| Kazimierz Czeley | 2 | — |\n| *[Przedmieście Zarzyce]* | | |\n| Bartek Czeley [Bartłomiej] | 2 | — |\n| Łysakowa Wda [Wdowa] | 2 | — |\n| Bartł: Kielianek [Bartłomiej Kilianek] | 2 | — |\n| Maciey Szubartowski | 2 | — |\n| Wiatrkowa Wda [Wdowa] | 2 | — |\n| Grzegorz Jołdzyk [Jażdżyk] | 2 | — |\n| Wawrzyniec Starobrat | 2 | — |\n| Maciey Rachon [Rachoń] | 2 | — |\n| Ciechowa Wda [Cuszkowa Wdowa] | 2 | — |\n| Szymon Marzec | 2 | — |\n| Rodzonkowa Wda [Wdowa] | 2 | — |\n| Łukasz Kielianek [Kilianek] | 2 | — |\n\n### [Kolumna 2: Przedmieście Zarzyce – Kontynuacja]\n\n| Posesjonat / Przedmieszczanin (Zarzyce) | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 5ti Lati** | | |\n| Maciey Rodzonek | 2 | — |\n| Gaspar Trojczak [Kacper] | 2 | — |\n| Antoni Wanek [Panek?] | 2 | — |\n| Grzegorz Biegay | 2 | — |\n| Maciey Piotrowski | 2 | — |\n| Łukasz Rymarz | 2 | — |\n| Andrzey Tokarczyk | 2 | — |\n| Marcin Drąg | 2 | — |\n| Woyciech Widak [Wolak?] | 2 | — |\n| Marcin Kołton | 2 | — |\n| Marcin Rymarz | 2 | — |\n| Łapczyna Wda [Wdowa] | 2 | — |\n| Markowa Wda [Wdowa] | 2 | — |\n| Andrzey Rządkowski | 2 | — |\n| Kazimierz Ciechoński | 2 | — |\n| Sebastyan Łysak | 2 | — |\n| Józef Dubay [Dubaj] | 2 | — |\n| Dubajowa Wda [Wdowa] | 2 | — |\n| Kazimierz Drąg | 2 | — |\n| Sobek Mikołayczak [Sebastian Mikołajczyk] | 2 | — |\n| Tomek Rządkowski [Tomasz] | 2 | — |\n| Łukasz Biegay | 2 | — |\n| Z Folwar:[ku] Granic | 2 | — |\n| Od Poddanego [Tegoż Folwarku] | 2 | — |\n| Józef Koza | 2 | — |\n| Maciey Łazarz | 2 | — |\n| Kasper Rodzonek | 2 | — |\n| Jędrzey Łazarz | 2 | — |\n| Ant:[oni] Koza | 2 | — |\n| Bartł: Dziadka [Bartłomiej] | 2 | — |\n| Maciey Kuśnierz | 2 | — |\n| Mikołay Rępa | 2 | — |\n| Łukasz Koza | 2 | — |"
  },
  "120": {
    "kategoria": "Taryfy podatkowe / Podymne marcowe 1776 (finał) i Podymne wrześniowe 1776 (początek) / Zarzyce i Śródmieście",
    "opis_pozycji": "1. Finał podymnego z marca 1776 dla Zarzyc (kolumna 1 góra: 4 dymy po 2 zł: Rzeszotek, Buczek, Młynarczykowa, Piotrowski; In Summa); 2. Nowa taryfa podymnego spisana 6 IX 1776 na ratę św. Jana / wrześniową (kolumna 1 dół i kolumna 2: Śródmieście, 57 dymów po 3 zł).",
    "kwoty_miary": "Podymne marcowe (Zarzyce): 8 zł; podymne wrześniowe 1776: 3 zł od dymu miejskiego; 1mus Latus: 117 zł; transport 2di Lati: 54 zł",
    "osoby_podmioty": "Zarzyce (III 1776): Wawrzyniec Rzeszotek, Mikołaj Buczek, wdowa Młynarczykowa, Stanisław Piotrowski; Śródmieście (IX 1776): Jacek Fiszer, domek Krywicki, Paweł Latosowicz, Józef Tokarski wójt, Mikołaj Łapka, Michał Krzanowski, Antoni Krzeszowski, Piotr Gołębiowski, Jakub Szulc, Kazimierz Rycerz, Jakub Rojek, Grzegorz Zdyb, Franciszek Frankowicz, Wojciech Połokowicz, Mateusz Ryzak, Maciej Cieśla, Antoni Okoń, Szymon Nowacki, Baltazar Latosowicz, Wojciech Latosowicz, Michał Jędencarz, Antoni Sadowski, Józef Czapliński, Jan Foliarski, domek Bryczkowy, Piotr Marczyński, Jan Mulowski, Antoni Suliczyński, Szymonowa Szajowska, Wojciech Bieniaszowski, Wojciech Krzeszowski, Mateusz Rycerz, Jakub Gąska, Walenty Łukasik, Piotr Młynarczyk, Sebastian Latosowicz, Józef Stembowski, Antoni Rachoń, Wawrzyniec Piłaszkiewicz, Tomasz Piłaszkiewicz, wdowa Aleksandrowa, Franciszek Wilk, Paweł Fruga, Wawrzyniec Starobrat, Antoni Piasecki, Walentowa Rachunkowa, Jan Boguta, Grzegorz Krasowski, wdowa Łańska, Stanisław Posoniak, wdowa Pietrachowa, wdowa Kotlarska, Piotr Połokowicz, Krzysztof Piłaszkiewicz, Mikołaj Kazimierski, Maciej Walczyński, Jędrzej Kępa",
    "osoby_skrot": "Józef Tokarski wójt, Jacek Fiszer, Michał Krzanowski, Grzegorz Zdyb, Wawrzyniec Starobrat",
    "transkrypcja": "[Na marginesie górnym:] Pag. 58\n\n### [Kolumna 1: Dokończenie Zarzyc (III 1776) oraz Nowy Regestr Wrześniowy 1776]\n\n| Posesjonat / Przedmieszczanin (Podymne Marcowe 1776) | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 6ti Lati [Continuat Zarzyce]** | | |\n| Wawr: Rzeszotek [Wawrzyniec] | 2 | — |\n| Mikołay Buczek | 2 | — |\n| Młynarczykowa Wda [Wdowa] | 2 | — |\n| Stanisł: Piotrowski [Stanisław] | 2 | — |\n| **In Summa Zarzyc** | **98** | **—** |\n\n---\n\n*Pro Ratha S-to Janis 1776. Miasto Krasnik 6ta 7bre [wrzesień 1776]*\n\n| Posesjonat / Mieszczanin (Śródmieście IX 1776) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Jacek Fisier [Fiszer] | 3 | — |\n| Domek Krywickiy [Krzywickich] | 3 | — |\n| Paweł Latosowicz | 3 | — |\n| Jozef Tokarski Woyt | 3 | — |\n| Mikołay Łapka | 3 | — |\n| Michał Krzanowski | 3 | — |\n| Antoni Krzeszowski | 3 | — |\n| Piotr Gołębiewski [Gołębiowski] | 3 | — |\n| Jakób Szulc | 3 | — |\n| Kazimierz Rycerz | 3 | — |\n| Jakób Rosoł [Rojek?] | 3 | — |\n| Grzegorz Zdyb | 3 | — |\n| Franciszek Frankowicz | 3 | — |\n| Woyciech Potokowicz [Połokowicz] | 3 | — |\n| Mateusz Ryzik [Ryzak?] | 3 | — |\n| Maciey Cieśla | 3 | — |\n| Antoni Okoń | 3 | — |\n| Szymon Nowacki | 3 | — |\n| Baltazar Latosowicz | 3 | — |\n| Woyciech Latosowicz | 3 | — |\n| Michał Jędencarz | 3 | — |\n| Antoni Sadowski | 3 | — |\n| Jozef Czapliński | 3 | — |\n| Jan Foliarski | 3 | — |\n| Domek Bryczkowy | 3 | — |\n| Piotr Marczyński | 3 | — |\n| Jan Mulowski | 3 | — |\n| Antoni Suliczyński | 3 | — |\n| Szymonowa Szayowska | 3 | — |\n| Woyciech Bieniaszowski | 3 | — |\n| Woyciech Krzeszowski | 3 | — |\n| Mateusz Rycerz | 3 | — |\n| Jakób Gąska | 3 | — |\n| Walenty Łukasik | 3 | — |\n| Piotr Młynarczyk | 3 | — |\n| Sebastyan Latosowicz | 3 | — |\n| Jozef Stembowski | 3 | — |\n| Antoni Rachon [Rachoń] | 3 | — |\n| Wawrzyniec Piłaszkiewicz | 3 | — |\n| **1mus Latus (39 domów)** | **117** | **—** |\n\n### [Kolumna 2: Śródmieście – Kontynuacja]\n\n| Posesjonat / Mieszczanin (Śródmieście IX 1776) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Tomasz Piłaszkiewicz | 3 | — |\n| Alexandrowa Wda [Wdowa] | 3 | — |\n| Franc: Wilczek [Franciszek Wilk?] | 3 | — |\n| Paweł Fruga | 3 | — |\n| Wawrzyniec Starobrat | 3 | — |\n| Antoni Piasecki | 3 | — |\n| Walentowa Rachunkowa [Wdowa] | 3 | — |\n| Jan Beguła [Boguta] | 3 | — |\n| Grzegorz Krasoski [Krasowski] | 3 | — |\n| Łańska Wda [Wdowa] | 3 | — |\n| Stanisł: Posoniak [Stanisław] | 3 | — |\n| Ant:[oniowa] Pietrachowa Wda [Wdowa] | 3 | — |\n| Kotlarska Wda [Wdowa] | 3 | — |\n| Piotr Potokowicz [Połokowicz] | 3 | — |\n| Krzysztof Piłaszkiewicz | 3 | — |\n| Mikołay Kazimierski | 3 | — |\n| Maciey Walczyński | 3 | — |\n| Jędrzey Rępa [Kępa] | 3 | — |"
  },
  "121": {
    "kategoria": "Taryfy podatkowe / Podymne wrześniowe / Izby browarne, Góry i Podlesie, Piasek 1776",
    "opis_pozycji": "Dalszy ciąg podymnego wrześniowego z 6 IX 1776 r.: dokończenie Śródmieścia (kolumna 1), izby przy browarach miejskich (Tokarski z Fiszerem, Paszkiewicz, Łaska, Krzanowski z Połokowiczem, Fruga, Rycerz, Szubartowski z bratem), pełny wykaz posesjonatów Gór i Podlesia (kolumna 1: 39 dymów po 2 zł, w tym Władarzyna wdowa) oraz początek Piasku (kolumna 2: 8 dymów po 2 zł).",
    "kwoty_miary": "Dokończenie Śródmieścia: 21 zł; izby browarne: po 1 zł (8 izb); Góry i Podlesie: 78 zł (39 dymów po 2 zł); Piasek (początek): 16 zł",
    "osoby_podmioty": "Śródmieście i browary: Paweł Piasecki, Marcin Kępa, Grzegorz Leśniowski, Maciej Połokowicz, Wojciech Fijałkowski, wdowa Kępina, Walenty Jurgiel, Józef Tokarski z Jackiem Fiszerem, Józef Paszkiewicz, Jakub Łaska, Michał Krzanowski z Wojciechem Połokowiczem, Paweł Fruga, Kazimierz Rycerz, Sebastian Szubartowski z bratem; Góry i Podlesie: Szymon Płachta, Adam Michał, Jan Boguta, Wojciech Gąska, Wojciech Kawka, wdowa Młynarczykowa, Jakub Rządkowski, wdowa Trojczakowa, Fabian Trojczak, Jacek Grzymek, Sobek Trojczak, Maciej Trojczak, Maciej Kępa, Mikołaj Kawka, Józef Strażnik, Antoni Tokarczyk, Szymon Krzeszowski, Józef Nowak, Augustyn Gregorczyk, Wawrzyniec Tokarczyk, Józef Gąska, Franciszek Kłopot, Mikołaj Zdyb, Szymon Ćwieka, Jan Wilk, Tomasz Wilk, Maciej Kawka, Grzegorz Wolak, Andrzej Kępa, Augustyn Kawka, Józef Wilk, Wojciech Kusz, Krzysztof Ćwieka, Walenty Biegay, Stanisław Pielach, Sobek Zdyb, Regina Ćwikowa, wdowa Władarzyna; Piasek: Antoni Tkaczyk, Stanisław Wolak, Szymon Antonik, Łukasz Pełka, Piotr Kilianek, Sobek Kilianek, Jan Bieniek, Marcin Łapa",
    "osoby_skrot": "Józef Tokarski wójt, Jacek Fiszer, Sebastian Szubartowski, Szymon Krzeszowski, Władarzyna wdowa, Antoni Tkaczyk",
    "transkrypcja": "[Na marginesie górnym:] Pag. 58v\n\n### [Kolumna 1: Dokończenie Miasta, Browary oraz Góry i Podlesie]\n\n| Posesjonat / Przedmieszczanin | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 2di Lati [Dokończenie Miasta]** | | |\n| Paweł Piasecki | 3 | — |\n| Marcin Rępa [Kępa] | 3 | — |\n| Grzegorz Lesznieski [Leśniowski] | 3 | — |\n| Maciey Potokowicz [Połokowicz] | 3 | — |\n| Woyciech Fijałkowski | 3 | — |\n| Kępina Wda [Wdowa] | 3 | — |\n| Walenty Jurgiel | 3 | — |\n| *[Z Yzbow przy Browar:]* | | |\n| Jozef Tokarski z Fisierem [Fiszerem] | 1 | — |\n| Jozef Paszkiewicz | 1 | — |\n| Jakob Łaska | 1 | — |\n| Krzanowski z Potokowiczem | 1 | — |\n| Paweł Fruga | 1 | — |\n| Kazimierz Rycerz | 1 | — |\n| Sebas:[tyan] Szubartowski | 1 | — |\n| Brat Jego [Szubartowski] | 1 | — |\n| #### [Przedmieście Góry i Podlesie] | | |\n| Szymon Płachta | 2 | — |\n| Adam Michał [Adamowicz?] | 2 | — |\n| Jan Boguta | 2 | — |\n| Woyciech Gąska | 2 | — |\n| Woyciech Kawka | 2 | — |\n| Młynarczykowa Wda [Wdowa] | 2 | — |\n| Jakób Rządkowski | 2 | — |\n| Trojczakowa Wda [Wdowa] | 2 | — |\n| Fabian Trojczak | 2 | — |\n| Jacek Grzymek | 2 | — |\n| Sobek Trojczak [Sebastian] | 2 | — |\n| Maciey Trojczak | 2 | — |\n| Maciey Rępa [Kępa] | 2 | — |\n| Mikołay Kawka | 2 | — |\n| Józef Strażnik | 2 | — |\n| Antoni Tokarczyk | 2 | — |\n| Szymon Krzeszowski | 2 | — |\n| Józef Nowak | 2 | — |\n| Augustyn Gregorczyk | 2 | — |\n| Wawr:[zyniec] Tokarczyk | 2 | — |\n| Józef Gąska | 2 | — |\n| Franc:[iszek] Kłopot | 2 | — |\n| Mikołay Zdyb | 2 | — |\n| Szymon Ćwieka | 2 | — |\n| Jan Wilk | 2 | — |\n| Tomasz Wilk | 2 | — |\n| Maciey Kawka | 2 | — |\n| Grzegorz Widak [Wolak?] | 2 | — |\n| Andrzey Rępa [Kępa] | 2 | — |\n| Augustyn Kawka | 2 | — |\n| Józef Wilk | 2 | — |\n| Woyciech Kusz | 2 | — |\n| Krzysz:[tof] Ćwieka | 2 | — |\n| Walenty Biegay | 2 | — |\n| Stach Pielach [Stanisław] | 2 | — |\n| Sobek Zdyb [Sebastian] | 2 | — |\n| Regina Ćwikowa | 2 | — |\n| Władarzyna Wda [Wdowa] | 2 | — |\n\n### [Kolumna 2: Przedmieście Piasek – Początek]\n\n| Posesjonat / Przedmieszczanin (Piasek) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Antoni Tkaczyk | 2 | — |\n| Stach Wotak [Stanisław Wolak] | 2 | — |\n| Szymon Antonik | 2 | — |\n| Łukasz Petka [Pełka?] | 2 | — |\n| Piotr Kielianek [Kilianek] | 2 | — |\n| Sobek Kielianek [Sebastian Kilianek] | 2 | — |\n| Jan Bieniek | 2 | — |\n| Marcin Łapa | 2 | — |"
  },
  "122": {
    "kategoria": "Taryfy podatkowe / Podymne wrześniowe / Przedmieścia Piasek i Zarzyce 1776",
    "opis_pozycji": "Dalszy ciąg poboru podymnego na ratę wrześniową 1776 r.: dokończenie przedmieścia Piasek (kolumna 1: 32 dymy po 2 zł, w tym ks. Koziński, Łukasz Tokarczyk, Barbara Bielecka, Kazimierz Czelej) oraz rejestr przedmieścia Zarzyce (kolumna 1 i 2: 34 dymy po 2 zł, m.in. Wawrzyniec Starobrat, Andrzej Rządkowski, wdowa Kołtonowa).",
    "kwoty_miary": "Podymne przedmiejskie: 2 zł od dymu/posesji; 4tus Latus (Piasek): 80 zł; 5tus Latus (Zarzyce): 68 zł",
    "osoby_podmioty": "Piasek: wdowa Rymarzowa, wdowa Jesiona, Tomasz Jażdżyk, Maciej Zdyb, Jan Wójcik, ks. Koziński, Mikołaj Nowak, Franciszek Pełka, Jakub Jaczniak, Bartłomiej Zdyb, Katarzyna Ossowska, Janowa Gajczykowa, Jakub Jaśkiewicz, Wojciech Czelej, Andrzej Dąbek, Wojciech Nowak, Szymon Wójcik, Wojciech Wziątek, Paweł Zieliński, Wojciech Pełka, Wojciech Drąg, Łukasz Pełka, Joachim Kłopot, Łukasz Tokarczyk, Michał Tokarczyk, Piotr Tokarczyk, Wojciech Wójcik, Stanisław Kępniak, Barbara Bielecka, Stanisław Wójcik, Wojciech Trojczak, Kazimierz Trojczak, Kazimierz Czelej; Zarzyce: Bartłomiej Czelej, wdowa Łysakowa, Bartłomiej Kilianek, Maciej Szubartowski, wdowa Wiatrkowa, Grzegorz Jażdżyk, Wawrzyniec Starobrat, Maciej Rachoń, wdowa Ciechowa, Szymon Marzec, wdowa Rodzonkowa, Łukasz Kilianek, Maciej Rodzonek, Kasper Trojczak, Antoni Wanek, Grzegorz Biegaj, Maciej Piotrowski, Łukasz Rymarz, Andrzej Tokarczyk, Marcin Drąg, Wojciech Wolak, Marcin Kołton, Marcin Rymarz, wdowa Kołtonowa, wdowa Łapczyna, wdowa Markowa, Andrzej Rządkowski, Kazimierz Ciechoński, Sebastian Łysak, Józef Dubaj, wdowa Dubajowa, Kazimierz Drąg, Sobek Mikołajczyk, Tomasz Rządkowski, Łukasz Biegaj",
    "osoby_skrot": "ks. Koziński, Łukasz Tokarczyk, Wawrzyniec Starobrat, Andrzej Rządkowski, wdowa Kołtonowa",
    "transkrypcja": "[Na marginesie górnym:] Pag. 59\n\n### [Kolumna 1: Dokończenie Piasku oraz Początek Zarzyc]\n\n| Posesjonat / Przedmieszczanin | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 4ti Lati [Continuat Piasek]** | | |\n| Rymarzowa Wdowa | 2 | — |\n| Jesiona Wdowa [Jasiewa?] | 2 | — |\n| Tomasz Jołdzyk [Jażdżyk] | 2 | — |\n| Maciey Zdyb | 2 | — |\n| Jan Woycik [Wójcik] | 2 | — |\n| Xz: Kozinski [Ksiądz Koziński] | 2 | — |\n| Mikołay Nowak | 2 | — |\n| Franc: Petka [Franciszek Pełka / Płachta?] | 2 | — |\n| Jakob Jaczniak | 2 | — |\n| Bartł: Zdyb [Bartłomiej] | 2 | — |\n| Katarzyna Ostrowska [Ossowska] | 2 | — |\n| Janowa Gayczykowa [Gajczykowa] | 2 | — |\n| Jakob Jasiuricz [Jaśkiewicz / Jasiewicz?] | 2 | — |\n| Woyciech Czeley | 2 | — |\n| Andrzey Dąbek | 2 | — |\n| Woyciech Nowak | 2 | — |\n| Szymon Woycik [Wójcik] | 2 | — |\n| Woyciech Wziątek | 2 | — |\n| Paweł Zieliński | 2 | — |\n| Woyciech Petka [Pełka?] | 2 | — |\n| Woyciech Drąg | 2 | — |\n| Łukasz Petka [Pełka?] | 2 | — |\n| Joachim Kłopot | 2 | — |\n| Łukasz Tokarczyk | 2 | — |\n| Michał Tokarczyk | 2 | — |\n| Piotr Tokarczyk | 2 | — |\n| Woyciech Woycik [Wójcik] | 2 | — |\n| Stach Kępniak [Stanisław] | 2 | — |\n| Barbara Bielecka | 2 | — |\n| Stach Woycik [Wójcik] | 2 | — |\n| Woyciech Trojczak | 2 | — |\n| Kazimierz Trojczak | 2 | — |\n| Kazimierz Czeley | 2 | — |\n| *[Przedmieście Zarzyce]* | | |\n| Bartek Czeley [Bartłomiej] | 2 | — |\n| Łysakowa Wda [Wdowa] | 2 | — |\n| Bartł: Kielianek [Bartłomiej Kilianek] | 2 | — |\n| Maciey Szubartowski | 2 | — |\n| Wiatrkowa Wda [Wdowa] | 2 | — |\n| Grzegorz Jołdzyk [Jażdżyk] | 2 | — |\n| Wawrzyniec Starobrat | 2 | — |\n| Maciey Rachon [Rachoń] | 2 | — |\n| Ciechowa Wda [Cuszkowa Wdowa] | 2 | — |\n| Szymon Marzec | 2 | — |\n| Rodzonkowa Wda [Wdowa] | 2 | — |\n| Łukasz Kielianek [Kilianek] | 2 | — |\n\n### [Kolumna 2: Przedmieście Zarzyce – Kontynuacja]\n\n| Posesjonat / Przedmieszczanin (Zarzyce) | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 5ti Lati** | | |\n| Maciey Rodzonek | 2 | — |\n| Gaspar Trojczak [Kacper] | 2 | — |\n| Antoni Wanek [Panek?] | 2 | — |\n| Grzegorz Biegay | 2 | — |\n| Maciey Piotrowski | 2 | — |\n| Łukasz Rymarz | 2 | — |\n| Andrzey Tokarczyk | 2 | — |\n| Marcin Drąg | 2 | — |\n| Woyciech Widak [Wolak?] | 2 | — |\n| Marcin Kołton | 2 | — |\n| Marcin Rymarz | 2 | — |\n| Kołtonowa Wda [Wdowa] | 2 | — |\n| Łapczyna Wda [Wdowa] | 2 | — |\n| Markowa Wda [Wdowa] | 2 | — |\n| Jędrzey Rządkowski | 2 | — |\n| Kazimierz Ciechoński | 2 | — |\n| Sebastyan Łysak | 2 | — |\n| Józef Dubay [Dubaj] | 2 | — |\n| Dubajowa Wda [Wdowa] | 2 | — |\n| Kazimierz Drąg | 2 | — |\n| Sobek Mikołayczak [Sebastian Mikołajczyk] | 2 | — |\n| Tomek Rządkowski [Tomasz] | 2 | — |\n| Łukasz Biegay | 2 | — |"
  },
  "123": {
    "kategoria": "Taryfy podatkowe / Podymne wrześniowe 1776 (finał) i Podymne marcowe 1777 (początek) / Zarzyce i Śródmieście",
    "opis_pozycji": "1. Finał podymnego z września 1776 r. dla Zarzyc (kolumna 1 góra: 17 posesji po 2 zł, w tym Folwark Ordynacki / Franciszkanów oraz chałupa poddanego; In Summa); 2. Nowa taryfa podymnego spisana 2 III 1777 r. na ratę marcową (kolumna 1 dół i kolumna 2: Śródmieście, 45 posesji po 3 zł, w tym Petronela Sadowska, Franciszek Matyszkiewicz).",
    "kwoty_miary": "Dokończenie podymnego wrześniowego: 34 zł; podymne marcowe 1777: 3 zł od dymu miejskiego (Petronela Sadowska: 4 zł); 1mus Latus marcowy: 102 zł; 2dus Latus (początek): 34 zł",
    "osoby_podmioty": "Zarzyce (IX 1776): Folwark Ordynacki (Franciszkanów), poddany folwarczny, Józef Koza, Maciej Łazarz, Kasper Rodzonek, Jędrzej Łazarz, Antoni Koza, Bartłomiej Dziadka, Maciej Kuśnierz, Mikołaj Rępa, Łukasz Koza, Wawrzyniec Rzeszotek, Mikołaj Buczek, wdowa Młynarczykowa, Stanisław Piotrowski; Śródmieście (III 1777): Jacek Fiszer, domek Krzywicki, Paweł Latosowicz, wójt Józef Tokarski, Mikołaj Łapka, Michał Krzanowski, Antoni Krzeszowski, Piotr Gołębiowski, Jakub Szulc, Kazimierz Rycerz, Jakub Rojek, Grzegorz Zdyb, Franciszek Frankowicz, Wojciech Połokowicz, Mateusz Ryzak, Maciej Cieśla, Antoni Okoń, Szymon Nowacki, Baltazar Latosowicz, Wojciech Latosowicz, Michał Jędencarz, Antoni Sadowski, Józef Czapliński, Jan Foliarski, domek Bryczkowy, Piotr Marczyński, Jan Mulowski, Antoni Suliczyński, Szymonowa Szajowska, Wojciech Bieniaszowski, Wojciech Krzeszowski, Mateusz Rycerz, Jakub Gąska, Walenty Łukasik, Paweł Latosowicz, Piotr Młynarczyk, Józef Stembowski (Słomkiewski), Paweł Fruga (Maciej Pruga), Kazimierz Młynarski, Franciszek Barankiewicz, Petronela Sadowska (Saidka), Franciszek Matyszkiewicz, Antoni Rachoń, Wawrzyniec Piłaszkiewicz, Tomasz Piłaszkiewicz",
    "osoby_skrot": "Folwark Ordynacki / Franciszkanów, Józef Tokarski wójt, Jacek Fiszer, Grzegorz Zdyb, Petronela Sadowska, Franciszek Matyszkiewicz",
    "transkrypcja": "[Na marginesie górnym:] Pag. 59v\n\n### [Kolumna 1: Dokończenie Zarzyc (IX 1776) oraz Nowy Regestr Marcowy 1777]\n\n| Posesjonat / Przedmieszczanin (Podymne Wrześniowe 1776) | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 6ti Lati [Continuat Zarzyce]** | | |\n| Folwark OO. Franciszkanów [Folwark Ordynacki] | 2 | — |\n| U Poddanego tychże | 2 | — |\n| Jozef Koza | 2 | — |\n| Maciey Łazarz | 2 | — |\n| Gaspar Rodzonek [Kacper] | 2 | — |\n| Jędrzey Łazarz | 2 | — |\n| Antoni Koza | 2 | — |\n| Bartł: Dziadka [Bartłomiej] | 2 | — |\n| Maciey Kuśnierz | 2 | — |\n| Mikołay Rępa | 2 | — |\n| Łukasz Koza | 2 | — |\n| Wawr: Rzeszotek [Wawrzyniec] | 2 | — |\n| Mikołay Buczek | 2 | — |\n| Młynarczykowa Wda [Wdowa] | 2 | — |\n| Stanisł: Piotrowski [Stanisław] | 2 | — |\n| **In Summa Zarzyc** | **98** | **—** |\n\n---\n\n*Regestr Podymnego na Rathę Marcową 1777 r. d. 2 Martii spisany*\n\n| Posesjonat / Mieszczanin (Śródmieście III 1777) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Jacek Fisier [Fiszer] | 3 | — |\n| Domek Krzydlinski [Krzywickich] | 3 | — |\n| Paweł Latosowicz | 3 | — |\n| Jozef Tokarski Woyt | 3 | — |\n| Mikołay Łapka | 3 | — |\n| Michał Krzanowski | 3 | — |\n| Antoni Krzeszowski | 3 | — |\n| Piotr Gołębiewski [Gołębiowski] | 3 | — |\n| Jakób Szulc | 3 | — |\n| Kazimierz Rycerz | 3 | — |\n| Jakób Rojek | 3 | — |\n| Grzegorz Zdyb | 3 | — |\n| Franciszek Frankowicz | 3 | — |\n| Woyciech Potokowicz [Połokowicz] | 3 | — |\n| Mateusz Ryzik [Ryzak?] | 3 | — |\n| Maciey Cieśla | 3 | — |\n| Antoni Okoń | 3 | — |\n| Szymon Nowacki | 3 | — |\n| Baltazar Latosowicz | 3 | — |\n| Woyciech Latosowicz | 3 | — |\n| Michał Jędencarz | 3 | — |\n| Antoni Sadowski | 3 | — |\n| Jozef Czapliński | 3 | — |\n| Jan Foliarski | 3 | — |\n| Domek Bryczkowy | 3 | — |\n| Piotr Marczyński | 3 | — |\n| Jan Mulowski | 3 | — |\n| Antoni Suliczyński | 3 | — |\n| Szymonowa Szayowska | 3 | — |\n| Woyciech Bieniaszowski | 3 | — |\n| Woyciech Krzeszowski | 3 | — |\n| Mateusz Rycerz | 3 | — |\n| Jakób Gąska | 3 | — |\n| Walenty Łukasik | 3 | — |\n| **1mus Latus (34 domy)** | **102** | **—** |\n\n### [Kolumna 2: Śródmieście – Kontynuacja]\n\n| Posesjonat / Mieszczanin (Śródmieście III 1777) | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 1mi Lati** | | |\n| Paweł Latosowicz | 3 | — |\n| Piotr Młynarczyk | 3 | — |\n| Jozef Słomkiewski [Stembowski?] | 3 | — |\n| Maciey Pruga [Paweł Fruga?] | 3 | — |\n| Kazimierz Młynarski | 3 | — |\n| Franc:[iszek] Barankiewicz | 3 | — |\n| Petronella Saidka [Sadowska?] | 4 | — |\n| Franc:[iszek] Matyszkiewicz | 3 | — |\n| Antoni Rachon [Rachoń] | 3 | — |\n| Wawr:[zyniec] Piłaszkiewicz | 3 | — |\n| Tomasz Piłaszkiewicz | 3 | — |"
  },
  "124": {
    "kategoria": "Taryfy podatkowe / Podymne marcowe / Izby browarne oraz Góry i Podlesie 1777",
    "opis_pozycji": "Dalszy ciąg podymnego z 2 III 1777 r.: dokończenie Śródmieścia (kolumna 1: posesje mieszczańskie, Krzysztof Rusak 1 zł, wdowa Lenartowa z córką 20 gr, Stanisław Posoniak 1 zł), izby browarne (Tokarski z Fiszerem, Paszkiewicz, Łaska, Krzanowski z Połokowiczem, Fruga, Rycerz, Szubartowski z bratem) oraz pełny wykaz mieszkańców Gór i Podlesia (kolumna 2: 35 gospodarzy po 2 zł).",
    "kwoty_miary": "Dokończenie Śródmieścia: 41 zł 20 gr; izby browarne: po 1 zł; Góry i Podlesie: 70 zł (35 dymów po 2 zł)",
    "osoby_podmioty": "Śródmieście i browary: wdowa Aleksandrowa, Franciszek Wilk, Paweł Fruga, Wawrzyniec Starobrat, Antoni Piasecki, Walenta Rachunkowa, Krzysztof Rusak, wdowa Lenartowa z córką, Jan Boguta, Grzegorz Krasowski, wdowa Łańska, Stanisław Posoniak, wdowa Pietrachowa, wdowa Kotlarska, Piotr Połokowicz, Krzysztof Piłaszkiewicz, Mikołaj Kazimierski, Maciej Walczyński, Jędrzej Kępa, Paweł Piasecki, Marcin Kępa, Grzegorz Leśniowski, Maciej Połokowicz, Wojciech Fijałkowski, wdowa Kępina, Walenty Jurgiel, Józef Tokarski z Jackiem Fiszerem, Józef Paszkiewicz, Jakub Łaska, Michał Krzanowski z Wojciechem Połokowiczem, Paweł Fruga, Kazimierz Rycerz, Sebastian Szubartowski z bratem; Góry i Podlesie: Szymon Płachta, Adam Michał, Jan Boguta, Wojciech Gąska, Wojciech Kawka, wdowa Młynarczykowa, Jakub Rządkowski, wdowa Trojczakowa, Fabian Trojczak, Jacek Grzymek, Sobek Trojczak, Maciej Trojczak, Maciej Kępa, Mikołaj Kawka, Józef Strażnik, Antoni Tokarczyk, Szymon Krzeszowski, Józef Nowak, Augustyn Gregorczyk, Wawrzyniec Tokarczyk, Józef Gąska, Franciszek Kłopot, Mikołaj Zdyb, Szymon Ćwieka, Jan Wilk, Tomasz Wilk, Maciej Kawka, Grzegorz Wolak, Andrzej Kępa, Augustyn Kawka, Józef Wilk, Wojciech Kusz, Krzysztof Ćwieka, Walenty Biegaj, Stanisław Pielach",
    "osoby_skrot": "Wawrzyniec Starobrat, Krzysztof Rusak, wdowa Lenartowa, Józef Tokarski wójt, Jacek Fiszer, Szymon Krzeszowski",
    "transkrypcja": "[Na marginesie górnym:] Pag. 60\n\n### [Kolumna 1: Dokończenie Miasta, Browary oraz Góry i Podlesie]\n\n| Posesjonat / Przedmieszczanin | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 2di Lati [Dokończenie Miasta]** | | |\n| Alexandrowa Wda [Wdowa] | 3 | — |\n| Franc:[iszek] Wilczek [Wilk?] | 3 | — |\n| Paweł Pruga [Fruga] | 3 | — |\n| Wawr:[zyniec] Starobrat | 3 | — |\n| Ant:[oni] Piasecki | 3 | — |\n| Walentowa Rachunkowa [Wdowa] | 3 | — |\n| Krzysztof Rusak | 1 | — |\n| Lenartowa z corką | — | 20 |\n| Jan Beguła [Boguta] | 3 | — |\n| Grzegorz Krasoski [Krasowski] | 3 | — |\n| Łańska Wda [Wdowa] | 3 | — |\n| Stanisł: Posoniak [Stanisław] | 1 | — |\n| Ant:[oniowa] Pietrachowa Wda [Wdowa] | 3 | — |\n| Kotlarska Wda [Wdowa] | 3 | — |\n| Piotr Potokowicz [Połokowicz] | 3 | — |\n| Krzysztof Piłaszkiewicz | 3 | — |\n| Mikołay Kazimierski | 3 | — |\n| Maciey Walczyński | 3 | — |\n| Jędrzey Rępa [Kępa] | 3 | — |\n| Paweł Piasecki | 3 | — |\n| Marcin Rępa [Kępa] | 3 | — |\n| Grzegorz Lesznieski [Leśniowski] | 3 | — |\n| Maciey Potokowicz [Połokowicz] | 3 | — |\n| Woyciech Fijałkowski | 3 | — |\n| Kępina Wda [Wdowa] | 3 | — |\n| Walenty Jurgiel | 3 | — |\n| *[Z Yzbow przy Browarach]* | | |\n| Jozef Tokarski z Fisierem [Fiszerem] | 1 | — |\n| Jozef Paszkiewicz | 1 | — |\n| Jakob Łaska | 1 | — |\n| Krzanowski z Potokowiczem | 1 | — |\n| Paweł Fruga | 1 | — |\n| Kazimierz Rycerz | 1 | — |\n| Sebas:[tyan] Szubartowski | 1 | — |\n| Brat Jego [Szubartowski] | 1 | — |\n\n### [Kolumna 2: Przedmieście Góry i Podlesie]\n\n| Posesjonat / Przedmieszczanin (Góry i Podlesie) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Szymon Płachta | 2 | — |\n| Adam Michał [Adamowicz?] | 2 | — |\n| Jan Boguta | 2 | — |\n| Woyciech Gąska | 2 | — |\n| Woyciech Kawka | 2 | — |\n| Młynarczykowa Wda [Wdowa] | 2 | — |\n| Jakób Rządkowski | 2 | — |\n| Trojczakowa Wda [Wdowa] | 2 | — |\n| Fabian Trojczak | 2 | — |\n| Jacek Grzymek | 2 | — |\n| Sobek Trojczak [Sebastian] | 2 | — |\n| Maciey Trojczak | 2 | — |\n| Maciey Rępa [Kępa] | 2 | — |\n| Mikołay Kawka | 2 | — |\n| Józef Strażnik | 2 | — |\n| Antoni Tokarczyk | 2 | — |\n| Szymon Krzeszowski | 2 | — |\n| Józef Nowak | 2 | — |\n| Augustyn Gregorczyk | 2 | — |\n| Wawr:[zyniec] Tokarczyk | 2 | — |\n| Józef Gąska | 2 | — |\n| Franc:[iszek] Kłopot | 2 | — |\n| Mikołay Zdyb | 2 | — |\n| Szymon Ćwieka | 2 | — |\n| Jan Wilk | 2 | — |\n| Tomasz Wilk | 2 | — |\n| Maciey Kawka | 2 | — |\n| Grzegorz Widak [Wolak?] | 2 | — |\n| Andrzey Rępa [Kępa] | 2 | — |\n| Augustyn Kawka | 2 | — |\n| Jozef Wilk | 2 | — |\n| Woyciech Kusz | 2 | — |\n| Krzysz:[tof] Ćwieka | 2 | — |\n| Walenty Biegay | 2 | — |\n| Stach Pielach [Stanisław] | 2 | — |"
  },
  "125": {
    "kategoria": "Taryfy podatkowe / Podymne marcowe / Piasek oraz Zarzyce 1777",
    "opis_pozycji": "Dalszy ciąg podymnego z 2 III 1777 r.: dokończenie Gór i Podlesia (3 dymy po 2 zł: Sebastian Zdyb, Regina Cwichowa, wdowa Władarzyna), pełny wykaz przedmieścia Piasek (kolumna 1 i 2: 40 dymów po 2 zł, m.in. ks. Koziński, Łukasz Tokarczyk, Barbara Bielecka, Kazimierz Czelej) oraz rejestr przedmieścia Zarzyce (kolumna 2: 49 posesji po 2 zł, w tym Folwark OO. Franciszkanów i chałupa poddanego).",
    "kwoty_miary": "Dokończenie Gór i Podlesia: 6 zł; Piasek: 80 zł (40 dymów po 2 zł); Zarzyce: 98 zł (49 posesji po 2 zł)",
    "osoby_podmioty": "Góry i Podlesie: Sebastian Zdyb, Regina Ćwikowa (Cwichowa), wdowa Władarzyna; Piasek: Antoni Tkaczyk, Stanisław Wolak, Szymon Antonik (Andruch), wdowa Pyzikowa, Piotr Kilianek, Jan Bieniek, Marcin Łapa, wdowa Rymarzowa, wdowa Jesiona, Tomasz Jażdżyk, Maciej Zdyb, Jan Wójcik, ks. Koziński, Mikołaj Nowak, Franciszek Pełka, Jakub Jaczniak, Bartłomiej Zdyb, Katarzyna Ossowska, Janowa Gajczykowa, Jakub Jaśkiewicz, Wojciech Czelej, Andrzej Dąbek, Wojciech Nowak, Szymon Wójcik, Wojciech Wziątek, Paweł Zieliński, Wojciech Pełka, Wojciech Drąg, Łukasz Pełka, Joachim Kłopot, Łukasz Tokarczyk, Michał Tokarczyk, Piotr Tokarczyk, Wojciech Wójcik, Stanisław Kępniak, Barbara Bielecka, Stanisław Wójcik, Wojciech Trojczak, Kazimierz Trojczak, Kazimierz Czelej; Zarzyce: Bartłomiej Czelej, wdowa Łysakowa, Bartłomiej Kilianek, Maciej Szubartowski, wdowa Wiatrkowa, Grzegorz Jażdżyk, Wawrzyniec Starobrat, Maciej Rachoń, wdowa Ciechowa, Szymon Marzec, wdowa Rodzonkowa, Łukasz Kilianek, Maciej Rodzonek, Kasper Trojczak, Antoni Wanek, Grzegorz Biegaj, Maciej Piotrowski, Łukasz Rymarz, Andrzej Tokarczyk, Marcin Drąg, Wojciech Wolak, Marcin Kołton, Marcin Rymarz, wdowa Kołtonowa, wdowa Łapczyna, wdowa Markowa, Andrzej Rządkowski, Kazimierz Ciechoński, Sebastian Łysak, Józef Dubaj, wdowa Dubajowa, Kazimierz Drąg, Sobek Mikołajczyk, Tomasz Rządkowski, Łukasz Biegaj, Folwark OO. Franciszkanów (u poddanego tychże), Józef Koza, Maciej Łazarz, Kasper Rodzonek, Jędrzej Łazarz, Antoni Koza, Bartłomiej Grządka, Maciej Kuśnierz, Mikołaj Rępa, Łukasz Koza, Wawrzyniec Rzeszotek, Mikołaj Buczek (Brzeczek), wdowa Młynarczykowa (Kłusatczyzkowa), Stanisław Piotrowski",
    "osoby_skrot": "ks. Koziński, Łukasz Tokarczyk, Wawrzyniec Starobrat, Folwark OO. Franciszkanów, Andrzej Rządkowski, Błażej Chruściel",
    "transkrypcja": "[Na marginesie górnym:] Pag. 60v\n\n### [Kolumna 1: Finał Gór i Podlesia oraz Przedmieście Piasek]\n\n| Posesjonat / Przedmieszczanin | Złote | Grosze |\n| :--- | :---: | :---: |\n| **Transport 4ti Lati [Continuat Gory y Podlesie]** | | |\n| Sebastyan Zdyb | 2 | — |\n| Regina Cwichowa [Ćwikowa] | 2 | — |\n| Władarzyna Wda [Wdowa] | 2 | — |\n| *[Przedmieście Piasek]* | | |\n| Antoni Tkaczyk | 2 | — |\n| Stanisław Wotak [Wolak] | 2 | — |\n| Szymon Andruch [Antonik?] | 2 | — |\n| Andniowa Pyzikowa [Wdowa] | 2 | — |\n| Piotr Kielianek [Kilianek] | 2 | — |\n| Jan Bieniek | 2 | — |\n| Marcin Łapka [Łapa] | 2 | — |\n| Rymarzowa Wda [Wdowa] | 2 | — |\n| Jesiona Wda [Wdowa] | 2 | — |\n| Tomasz Jołdzyk [Jażdżyk] | 2 | — |\n| Maciey Zdyb | 2 | — |\n| Jan Woycik [Wójcik] | 2 | — |\n| Xz: Kozinski [Ksiądz Koziński] | 2 | — |\n| Mikołay Nowak | 2 | — |\n| Franc:[iszek] Petka [Pełka / Płachta?] | 2 | — |\n| Jakób Jaczniak | 2 | — |\n| Bartł:[omiej] Zdyb | 2 | — |\n| Katarzyna Ostrowska [Ossowska] | 2 | — |\n| Janowa Gayczykowa [Gajczykowa] | 2 | — |\n| Jakób Jasiuricz [Jaśkiewicz / Jasiewicz?] | 2 | — |\n| Woyciech Czeley | 2 | — |\n| Andrzey Dąbek | 2 | — |\n| Woyciech Nowak | 2 | — |\n| Szymon Woycik [Wójcik] | 2 | — |\n| Woyciech Wziątek | 2 | — |\n| Paweł Zieliński | 2 | — |\n| Woyciech Petka [Pełka?] | 2 | — |\n| Woyciech Drąg | 2 | — |\n| Łukasz Petka [Pełka?] | 2 | — |\n| Joachim Kłopot | 2 | — |\n| Łukasz Tokarczyk | 2 | — |\n| Michał Tokarczyk | 2 | — |\n| Piotr Tokarczyk | 2 | — |\n| Woyciech Woycik [Wójcik] | 2 | — |\n| Stach Kępniak [Stanisław] | 2 | — |\n| Barbara Bielecka | 2 | — |\n| Stach Woycik [Wójcik] | 2 | — |\n| Woyciech Trojczak | 2 | — |\n| Kazimierz Trojczak | 2 | — |\n| Kazimierz Czeley | 2 | — |\n\n### [Kolumna 2: Przedmieście Zarzyce]\n\n| Posesjonat / Przedmieszczanin (Zarzyce) | Złote | Grosze |\n| :--- | :---: | :---: |\n| Bartek Czeley [Bartłomiej] | 2 | — |\n| Łysakowa Wda [Wdowa] | 2 | — |\n| Bartł:[omiej] Kielianek [Kilianek] | 2 | — |\n| Maciey Szubartowski | 2 | — |\n| Wiatrkowa Wda [Wdowa] | 2 | — |\n| Grzegorz Jołdzyk [Jażdżyk] | 2 | — |\n| Wawrzyniec Starobrat | 2 | — |\n| Maciey Rachon [Rachoń] | 2 | — |\n| Ciechowa Wda [Cuszkowa Wdowa] | 2 | — |\n| Szymon Marzec | 2 | — |\n| Rodzonkowa Wda [Wdowa] | 2 | — |\n| Łukasz Kielianek [Kilianek] | 2 | — |\n| Maciey Rodzonek | 2 | — |\n| Gaspar Trojczak [Kacper] | 2 | — |\n| Antoni Wanek [Panek?] | 2 | — |\n| Grzegorz Biegay | 2 | — |\n| Maciey Piotrowski | 2 | — |\n| Łukasz Rymarz | 2 | — |\n| Andrzey Tokarczyk | 2 | — |\n| Marcin Drąg | 2 | — |\n| Woyciech Widak [Wolak?] | 2 | — |\n| Marcin Kołton | 2 | — |\n| Marcin Rymarz | 2 | — |\n| Kołtonowa Wda [Wdowa] | 2 | — |\n| Łapczyna Wda [Wdowa] | 2 | — |\n| Markowa Wda [Wdowa] | 2 | — |\n| Jędrzey Rządkowski | 2 | — |\n| Kazimierz Ciechoński | 2 | — |\n| Sebastyan Łysak | 2 | — |\n| Józef Dubay [Dubaj] | 2 | — |\n| Dubajowa Wda [Wdowa] | 2 | — |\n| Kazimierz Drąg | 2 | — |\n| Sobek Mikołayczak [Sebastian Mikołajczyk] | 2 | — |\n| Tomek Rządkowski [Tomasz] | 2 | — |\n| Łukasz Biegay | 2 | — |\n| Folwark OO. Franciszkanów | 2 | — |\n| U Poddanego tychże | 2 | — |\n| Jozef Koza | 2 | — |\n| Maciey Łazarz | 2 | — |\n| Kasper Rodzonek | 2 | — |\n| Jędrzey Łazarz | 2 | — |\n| Antoni Koza | 2 | — |\n| Bartł:[omiej] Grządka | 2 | — |\n| Maciey Kuśnierz | 2 | — |\n| Mikołay Rępa | 2 | — |\n| Łukasz Koza | 2 | — |\n| Wawr:[zyniec] Rzeszotek | 2 | — |\n| Mikołay Brzeczek [Buczek] | 2 | — |\n| Kłusatczyzkowa Wda [Młynarczykowa Wdowa?] | 2 | — |\n| Stach Piotrowski [Stanisław] | 2 | — |"
  }
}

# Nowe profile genealogiczne Partii 7 (lp 751–780)
nowe_profile_p7 = [
  {
    "lp": 751,
    "nazwisko": "Radomski",
    "wariant_nazwiska": "Radomirsky? / Radomski",
    "imie": "Mikołaj",
    "przydomek": "",
    "funkcja": "Mieszkaniec / Posesjonat",
    "miejsce": "Śródmieście",
    "skany_roboczo": "#107, #110",
    "skany_list": [
      107,
      110
    ],
    "zakres_lat": "1776–1777",
    "min_rok": 1776,
    "max_rok": 1777,
    "liczba_wystapien": 2,
    "wystapienia": [
      {
        "nazwisko": "Radomski",
        "imie": "Mikołaj",
        "miejsce": "Śródmieście",
        "rola": "Płatnik 8 sympli",
        "skan": 107,
        "rok": "1776",
        "zapis_oryginalny": "Mikołay Radomirsky",
        "kwota_ctx": "2 zł 24 gr."
      },
      {
        "nazwisko": "Radomski",
        "imie": "Mikołaj",
        "miejsce": "Śródmieście",
        "rola": "Płatnik 8 sympli",
        "skan": 110,
        "rok": "1777",
        "zapis_oryginalny": "Mik: Radomski",
        "kwota_ctx": "2 zł 24 gr."
      }
    ],
    "uwagi": "Posesjonat w centrum Kraśnika (zapisywany Mikołay Radomirsky / Radomski)."
  },
  {
    "lp": 752,
    "nazwisko": "Szafrańska",
    "wariant_nazwiska": "Szafrańska",
    "imie": "Walentowa [Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Mieszczanka",
    "miejsce": "Śródmieście",
    "skany_roboczo": "#106, #110",
    "skany_list": [
      106,
      110
    ],
    "zakres_lat": "1776–1777",
    "min_rok": 1776,
    "max_rok": 1777,
    "liczba_wystapien": 2,
    "wystapienia": [
      {
        "nazwisko": "Szafrańska",
        "imie": "Walentowa",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka 8 sympli",
        "skan": 106,
        "rok": "1776",
        "zapis_oryginalny": "Walenta Szafrańska",
        "kwota_ctx": "12 gr."
      },
      {
        "nazwisko": "Szafrańska",
        "imie": "Walentowa",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka 8 sympli",
        "skan": 110,
        "rok": "1777",
        "zapis_oryginalny": "Walenta Szafrańska",
        "kwota_ctx": "12 gr."
      }
    ],
    "uwagi": "Posesjonatka i mieszczanka śródmiejska, wdowa lub córka po Walentym Szafrańskim."
  },
  {
    "lp": 753,
    "nazwisko": "Bielecka",
    "wariant_nazwiska": "Bielecka",
    "imie": "Barbara",
    "przydomek": "",
    "funkcja": "Posesjonatka / Przedmieszczanka",
    "miejsce": "Piaski",
    "skany_roboczo": "#108, #111, #116, #119, #122, #125",
    "skany_list": [
      108,
      111,
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Bielecka",
        "imie": "Barbara",
        "miejsce": "Piaski",
        "rola": "Płatniczka 8 sympli",
        "skan": 108,
        "rok": "1776",
        "zapis_oryginalny": "Barbara Bielecka",
        "kwota_ctx": "2 zł 12 gr."
      },
      {
        "nazwisko": "Bielecka",
        "imie": "Barbara",
        "miejsce": "Piaski",
        "rola": "Płatniczka 8 sympli",
        "skan": 111,
        "rok": "1777",
        "zapis_oryginalny": "Barbara Bielecka",
        "kwota_ctx": "2 zł 12 gr."
      },
      {
        "nazwisko": "Bielecka",
        "imie": "Barbara",
        "miejsce": "Piaski",
        "rola": "Płatniczka podymnego",
        "skan": 116,
        "rok": "1775",
        "zapis_oryginalny": "Barbara Bielecka",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Bielecka",
        "imie": "Barbara",
        "miejsce": "Piaski",
        "rola": "Płatniczka podymnego",
        "skan": 119,
        "rok": "1776",
        "zapis_oryginalny": "Barbara Bielecka",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Bielecka",
        "imie": "Barbara",
        "miejsce": "Piaski",
        "rola": "Płatniczka podymnego",
        "skan": 122,
        "rok": "1776",
        "zapis_oryginalny": "Barbara Bielecka",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Bielecka",
        "imie": "Barbara",
        "miejsce": "Piaski",
        "rola": "Płatniczka podymnego",
        "skan": 125,
        "rok": "1777",
        "zapis_oryginalny": "Barbara Bielecka",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Właścicielka posesji i dymu na przedmieściu Piasek (Bielecka Barbara)."
  },
  {
    "lp": 754,
    "nazwisko": "Dąbek",
    "wariant_nazwiska": "Dąbek / Dąmbek?",
    "imie": "Andrzej",
    "przydomek": "",
    "funkcja": "Przedmieszczanin / Posesjonat",
    "miejsce": "Piaski",
    "skany_roboczo": "#111, #116, #119, #122, #125",
    "skany_list": [
      111,
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 5,
    "wystapienia": [
      {
        "nazwisko": "Dąbek",
        "imie": "Andrzej",
        "miejsce": "Piaski",
        "rola": "Płatnik podymnego",
        "skan": 116,
        "rok": "1775",
        "zapis_oryginalny": "Andrzey Dąbek",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Dąbek",
        "imie": "Andrzej",
        "miejsce": "Piaski",
        "rola": "Płatnik podymnego",
        "skan": 119,
        "rok": "1776",
        "zapis_oryginalny": "Andrzey Dąbek",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Dąbek",
        "imie": "Andrzej",
        "miejsce": "Piaski",
        "rola": "Płatnik podymnego",
        "skan": 122,
        "rok": "1776",
        "zapis_oryginalny": "Andrzey Dąbek",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Dąbek",
        "imie": "Andrzej",
        "miejsce": "Piaski",
        "rola": "Płatnik podymnego",
        "skan": 125,
        "rok": "1777",
        "zapis_oryginalny": "Andrzey Dąbek",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Gospodarz i posesjonat na przedmieściu Piasek."
  },
  {
    "lp": 755,
    "nazwisko": "Ciechoński",
    "wariant_nazwiska": "Olechowski? / Ciechoński",
    "imie": "Kazimierz",
    "przydomek": "",
    "funkcja": "Przedmieszczanin / Posesjonat",
    "miejsce": "Zarzecze",
    "skany_roboczo": "#108, #111, #112, #116, #119, #122, #125",
    "skany_list": [
      108,
      111,
      112,
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 7,
    "wystapienia": [
      {
        "nazwisko": "Ciechoński",
        "imie": "Kazimierz",
        "miejsce": "Zarzecze",
        "rola": "Płatnik 8 sympli",
        "skan": 108,
        "rok": "1776",
        "zapis_oryginalny": "Kaz: Olechowski [Ciechoński?]",
        "kwota_ctx": "1 zł 10 gr."
      },
      {
        "nazwisko": "Ciechoński",
        "imie": "Kazimierz",
        "miejsce": "Zarzecze",
        "rola": "Płatnik 8 sympli",
        "skan": 112,
        "rok": "1777",
        "zapis_oryginalny": "Kz: Ciechoński",
        "kwota_ctx": "1 zł 18 gr."
      },
      {
        "nazwisko": "Ciechoński",
        "imie": "Kazimierz",
        "miejsce": "Zarzecze",
        "rola": "Płatnik podymnego",
        "skan": 116,
        "rok": "1775",
        "zapis_oryginalny": "Kazimierz Ciechoński",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Ciechoński",
        "imie": "Kazimierz",
        "miejsce": "Zarzecze",
        "rola": "Płatnik podymnego",
        "skan": 119,
        "rok": "1776",
        "zapis_oryginalny": "Kazimierz Ciechoński",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Ciechoński",
        "imie": "Kazimierz",
        "miejsce": "Zarzecze",
        "rola": "Płatnik podymnego",
        "skan": 122,
        "rok": "1776",
        "zapis_oryginalny": "Kazimierz Ciechoński",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Ciechoński",
        "imie": "Kazimierz",
        "miejsce": "Zarzecze",
        "rola": "Płatnik podymnego",
        "skan": 125,
        "rok": "1777",
        "zapis_oryginalny": "Kazimierz Ciechoński",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Gospodarz przedmieścia Zarzyce (zapisywany Kaz: Olechowski / Kz: Ciechoński)."
  },
  {
    "lp": 756,
    "nazwisko": "Gregorczyk",
    "wariant_nazwiska": "Gregorczyk / Grzegorczyk",
    "imie": "Augustyn",
    "przydomek": "",
    "funkcja": "Przedmieszczanin / Posesjonat",
    "miejsce": "Góry i Podlesie",
    "skany_roboczo": "#109, #112, #115, #118, #121, #124",
    "skany_list": [
      109,
      112,
      115,
      118,
      121,
      124
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Gregorczyk",
        "imie": "Augustyn",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik 8 sympli",
        "skan": 109,
        "rok": "1776",
        "zapis_oryginalny": "Aug: Gregorczyk",
        "kwota_ctx": "2 zł 12 gr."
      },
      {
        "nazwisko": "Gregorczyk",
        "imie": "Augustyn",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik 8 sympli",
        "skan": 112,
        "rok": "1777",
        "zapis_oryginalny": "Augustyn Gregorczyk",
        "kwota_ctx": "2 zł 12 gr."
      },
      {
        "nazwisko": "Gregorczyk",
        "imie": "Augustyn",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik podymnego",
        "skan": 115,
        "rok": "1775",
        "zapis_oryginalny": "Augustyn Gregorczyk",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Gregorczyk",
        "imie": "Augustyn",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik podymnego",
        "skan": 118,
        "rok": "1776",
        "zapis_oryginalny": "Augustyn Gregorczyk",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Gregorczyk",
        "imie": "Augustyn",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik podymnego",
        "skan": 121,
        "rok": "1776",
        "zapis_oryginalny": "Augustyn Gregorczyk",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Gregorczyk",
        "imie": "Augustyn",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik podymnego",
        "skan": 124,
        "rok": "1777",
        "zapis_oryginalny": "Augustyn Gregorczyk",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Gospodarz i posesjonat na przedmieściu Góry i Podlesie."
  },
  {
    "lp": 757,
    "nazwisko": "Wanek",
    "wariant_nazwiska": "Panek? / Wanek",
    "imie": "Antoni",
    "przydomek": "",
    "funkcja": "Przedmieszczanin / Posesjonat",
    "miejsce": "Zarzecze",
    "skany_roboczo": "#108, #111, #112, #116, #119, #122, #125",
    "skany_list": [
      108,
      111,
      112,
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 7,
    "wystapienia": [
      {
        "nazwisko": "Wanek",
        "imie": "Antoni",
        "miejsce": "Zarzecze",
        "rola": "Płatnik 8 sympli",
        "skan": 108,
        "rok": "1776",
        "zapis_oryginalny": "Antoni Panek [Wanek?]",
        "kwota_ctx": "4 zł 10 gr."
      },
      {
        "nazwisko": "Wanek",
        "imie": "Antoni",
        "miejsce": "Zarzecze",
        "rola": "Płatnik 8 sympli",
        "skan": 112,
        "rok": "1777",
        "zapis_oryginalny": "Antoni Wanek",
        "kwota_ctx": "1 zł 18 gr."
      },
      {
        "nazwisko": "Wanek",
        "imie": "Antoni",
        "miejsce": "Zarzecze",
        "rola": "Płatnik podymnego",
        "skan": 116,
        "rok": "1775",
        "zapis_oryginalny": "Antoni Wanek",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Wanek",
        "imie": "Antoni",
        "miejsce": "Zarzecze",
        "rola": "Płatnik podymnego",
        "skan": 119,
        "rok": "1776",
        "zapis_oryginalny": "Antoni Wanek",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Wanek",
        "imie": "Antoni",
        "miejsce": "Zarzecze",
        "rola": "Płatnik podymnego",
        "skan": 122,
        "rok": "1776",
        "zapis_oryginalny": "Antoni Wanek",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Wanek",
        "imie": "Antoni",
        "miejsce": "Zarzecze",
        "rola": "Płatnik podymnego",
        "skan": 125,
        "rok": "1777",
        "zapis_oryginalny": "Antoni Wanek",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Gospodarz na przedmieściu Zarzyce (zapisywany Antoni Panek / Wanek)."
  },
  {
    "lp": 758,
    "nazwisko": "Wziątek",
    "wariant_nazwiska": "Wziątek / Wziąndtek?",
    "imie": "Wojciech",
    "przydomek": "",
    "funkcja": "Przedmieszczanin / Posesjonat",
    "miejsce": "Piaski",
    "skany_roboczo": "#116, #119, #122, #125",
    "skany_list": [
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 4,
    "wystapienia": [
      {
        "nazwisko": "Wziątek",
        "imie": "Wojciech",
        "miejsce": "Piaski",
        "rola": "Płatnik podymnego",
        "skan": 116,
        "rok": "1775",
        "zapis_oryginalny": "Woyciech Wziątek",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Wziątek",
        "imie": "Wojciech",
        "miejsce": "Piaski",
        "rola": "Płatnik podymnego",
        "skan": 119,
        "rok": "1776",
        "zapis_oryginalny": "Woyciech Wziątek",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Wziątek",
        "imie": "Wojciech",
        "miejsce": "Piaski",
        "rola": "Płatnik podymnego",
        "skan": 122,
        "rok": "1776",
        "zapis_oryginalny": "Woyciech Wziątek",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Wziątek",
        "imie": "Wojciech",
        "miejsce": "Piaski",
        "rola": "Płatnik podymnego",
        "skan": 125,
        "rok": "1777",
        "zapis_oryginalny": "Woyciech Wziątek",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Gospodarz i posesjonat na przedmieściu Piasek."
  },
  {
    "lp": 759,
    "nazwisko": "Piecuch",
    "wariant_nazwiska": "Pieciuch? / Witczek Pieciuch? / Piecuch",
    "imie": "Krzysztof",
    "przydomek": "Witczek",
    "funkcja": "Mieszkaniec / Posesjonat",
    "miejsce": "Śródmieście",
    "skany_roboczo": "#107, #110",
    "skany_list": [
      107,
      110
    ],
    "zakres_lat": "1776–1777",
    "min_rok": 1776,
    "max_rok": 1777,
    "liczba_wystapien": 2,
    "wystapienia": [
      {
        "nazwisko": "Piecuch",
        "imie": "Krzysztof",
        "miejsce": "Śródmieście",
        "rola": "Płatnik 8 sympli",
        "skan": 107,
        "rok": "1776",
        "zapis_oryginalny": "Krzyk Pieciuch",
        "kwota_ctx": "3 zł."
      },
      {
        "nazwisko": "Piecuch",
        "imie": "Krzysztof",
        "miejsce": "Śródmieście",
        "rola": "Płatnik 8 sympli",
        "skan": 110,
        "rok": "1777",
        "zapis_oryginalny": "Witczek Pieciuch",
        "kwota_ctx": "3 zł."
      }
    ],
    "uwagi": "Posesjonat w centrum Kraśnika (zapisywany Krzyk Pieciuch / Witczek Pieciuch)."
  },
  {
    "lp": 760,
    "nazwisko": "Babicz",
    "wariant_nazwiska": "Babiez? / Babicz",
    "imie": "Błażej",
    "przydomek": "",
    "funkcja": "Przedmieszczanin / Posesjonat",
    "miejsce": "Góry i Podlesie",
    "skany_roboczo": "#109, #112",
    "skany_list": [
      109,
      112
    ],
    "zakres_lat": "1776–1777",
    "min_rok": 1776,
    "max_rok": 1777,
    "liczba_wystapien": 2,
    "wystapienia": [
      {
        "nazwisko": "Babicz",
        "imie": "Błażej",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik 8 sympli",
        "skan": 109,
        "rok": "1776",
        "zapis_oryginalny": "Błach Babiez",
        "kwota_ctx": "2 zł 12 gr."
      },
      {
        "nazwisko": "Babicz",
        "imie": "Błażej",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik 8 sympli",
        "skan": 112,
        "rok": "1777",
        "zapis_oryginalny": "Błach Babicz",
        "kwota_ctx": "2 zł 12 gr."
      }
    ],
    "uwagi": "Gospodarz podgórski (zapisywany Błach Babiez / Babicz)."
  },
  {
    "lp": 761,
    "nazwisko": "Kusz",
    "wariant_nazwiska": "Rus? / Kusz",
    "imie": "Wojciech",
    "przydomek": "",
    "funkcja": "Przedmieszczanin / Posesjonat",
    "miejsce": "Góry i Podlesie",
    "skany_roboczo": "#109, #112, #115, #118, #121, #124",
    "skany_list": [
      109,
      112,
      115,
      118,
      121,
      124
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Kusz",
        "imie": "Wojciech",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik 8 sympli",
        "skan": 109,
        "rok": "1776",
        "zapis_oryginalny": "Woyciech Rus [Kusz?]",
        "kwota_ctx": "9 zł 10 gr."
      },
      {
        "nazwisko": "Kusz",
        "imie": "Wojciech",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik 8 sympli",
        "skan": 112,
        "rok": "1777",
        "zapis_oryginalny": "Woyciech Kusz",
        "kwota_ctx": "3 zł 18 gr."
      },
      {
        "nazwisko": "Kusz",
        "imie": "Wojciech",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik podymnego",
        "skan": 115,
        "rok": "1775",
        "zapis_oryginalny": "Woyciech Kusz",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Kusz",
        "imie": "Wojciech",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik podymnego",
        "skan": 118,
        "rok": "1776",
        "zapis_oryginalny": "Woyciech Kusz",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Kusz",
        "imie": "Wojciech",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik podymnego",
        "skan": 121,
        "rok": "1776",
        "zapis_oryginalny": "Woyciech Kusz",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Kusz",
        "imie": "Wojciech",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik podymnego",
        "skan": 124,
        "rok": "1777",
        "zapis_oryginalny": "Woyciech Kusz",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Gospodarz i posesjonat na przedmieściu Góry i Podlesie (zapisywany Rus / Kusz)."
  },
  {
    "lp": 762,
    "nazwisko": "Matyszkiewicz",
    "wariant_nazwiska": "Matyszkiewicz",
    "imie": "Franciszek",
    "przydomek": "",
    "funkcja": "Mieszkaniec / Posesjonat",
    "miejsce": "Śródmieście",
    "skany_roboczo": "#123",
    "skany_list": [
      123
    ],
    "zakres_lat": "1777",
    "min_rok": 1777,
    "max_rok": 1777,
    "liczba_wystapien": 1,
    "wystapienia": [
      {
        "nazwisko": "Matyszkiewicz",
        "imie": "Franciszek",
        "miejsce": "Śródmieście",
        "rola": "Płatnik podymnego",
        "skan": 123,
        "rok": "1777",
        "zapis_oryginalny": "Franc: Matyszkiewicz",
        "kwota_ctx": "3 zł."
      }
    ],
    "uwagi": "Posesjonat w centrum Kraśnika, płatnik podymnego w 1777 r."
  },
  {
    "lp": 763,
    "nazwisko": "Wojtka",
    "wariant_nazwiska": "Wojtka / Woytka",
    "imie": "Stanisław",
    "przydomek": "",
    "funkcja": "Przedmieszczanin / Posesjonat",
    "miejsce": "Zarzecze",
    "skany_roboczo": "#116",
    "skany_list": [
      116
    ],
    "zakres_lat": "1775",
    "min_rok": 1775,
    "max_rok": 1775,
    "liczba_wystapien": 1,
    "wystapienia": [
      {
        "nazwisko": "Wojtka",
        "imie": "Stanisław",
        "miejsce": "Zarzecze",
        "rola": "Płatnik podymnego",
        "skan": 116,
        "rok": "1775",
        "zapis_oryginalny": "Stach Woytka",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Gospodarz na przedmieściu Zarzyce."
  },
  {
    "lp": 764,
    "nazwisko": "Ćwiek",
    "wariant_nazwiska": "Ćwikowa? / Cwichowa? / Ćwiek",
    "imie": "Regina",
    "przydomek": "",
    "funkcja": "Przedmieszczanka / Posesjonatka",
    "miejsce": "Góry i Podlesie",
    "skany_roboczo": "#118, #121, #125",
    "skany_list": [
      118,
      121,
      125
    ],
    "zakres_lat": "1776–1777",
    "min_rok": 1776,
    "max_rok": 1777,
    "liczba_wystapien": 3,
    "wystapienia": [
      {
        "nazwisko": "Ćwiek",
        "imie": "Regina",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatniczka podymnego",
        "skan": 118,
        "rok": "1776",
        "zapis_oryginalny": "Regina Ćwikowa",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Ćwiek",
        "imie": "Regina",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatniczka podymnego",
        "skan": 121,
        "rok": "1776",
        "zapis_oryginalny": "Regina Ćwikowa",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Ćwiek",
        "imie": "Regina",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatniczka podymnego",
        "skan": 125,
        "rok": "1777",
        "zapis_oryginalny": "Regina Cwichowa",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Posesjonatka na przedmieściu Góry i Podlesie (Regina Ćwikowa / Cwichowa)."
  },
  {
    "lp": 765,
    "nazwisko": "Kołton",
    "wariant_nazwiska": "Kołton / Kolton",
    "imie": "Marcin",
    "przydomek": "",
    "funkcja": "Przedmieszczanin / Posesjonat",
    "miejsce": "Zarzecze",
    "skany_roboczo": "#108, #111, #112, #116, #119, #122, #125",
    "skany_list": [
      108,
      111,
      112,
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 7,
    "wystapienia": [
      {
        "nazwisko": "Kołton",
        "imie": "Marcin",
        "miejsce": "Zarzecze",
        "rola": "Płatnik 8 sympli",
        "skan": 108,
        "rok": "1776",
        "zapis_oryginalny": "Mar: Kołton",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Kołton",
        "imie": "Marcin",
        "miejsce": "Zarzecze",
        "rola": "Płatnik podymnego",
        "skan": 116,
        "rok": "1775",
        "zapis_oryginalny": "Marcin Kołton",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Kołton",
        "imie": "Marcin",
        "miejsce": "Zarzecze",
        "rola": "Płatnik podymnego",
        "skan": 119,
        "rok": "1776",
        "zapis_oryginalny": "Marcin Kołton",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Gospodarz i posesjonat na przedmieściu Zarzyce."
  },
  {
    "lp": 766,
    "nazwisko": "Kołton",
    "wariant_nazwiska": "Kołtonowa Wdowa",
    "imie": "[Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Zarzecze",
    "skany_roboczo": "#122, #125",
    "skany_list": [
      122,
      125
    ],
    "zakres_lat": "1776–1777",
    "min_rok": 1776,
    "max_rok": 1777,
    "liczba_wystapien": 2,
    "wystapienia": [
      {
        "nazwisko": "Kołton",
        "imie": "[Wdowa]",
        "miejsce": "Zarzecze",
        "rola": "Płatniczka podymnego",
        "skan": 122,
        "rok": "1776",
        "zapis_oryginalny": "Kołtonowa Wda",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Kołton",
        "imie": "[Wdowa]",
        "miejsce": "Zarzecze",
        "rola": "Płatniczka podymnego",
        "skan": 125,
        "rok": "1777",
        "zapis_oryginalny": "Kołtonowa Wda",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Wdowa po Marcinie Kołtonie na przedmieściu Zarzyce."
  },
  {
    "lp": 767,
    "nazwisko": "Łańska",
    "wariant_nazwiska": "Lanska? / Łańska",
    "imie": "[Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Śródmieście",
    "skany_roboczo": "#107, #110, #113, #114, #117, #120, #124",
    "skany_list": [
      107,
      110,
      113,
      114,
      117,
      120,
      124
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 7,
    "wystapienia": [
      {
        "nazwisko": "Łańska",
        "imie": "[Wdowa]",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka 8 sympli",
        "skan": 107,
        "rok": "1776",
        "zapis_oryginalny": "Łańska Wd:[owa]",
        "kwota_ctx": "1 zł 10 gr."
      },
      {
        "nazwisko": "Łańska",
        "imie": "[Wdowa]",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka 8 sympli",
        "skan": 110,
        "rok": "1777",
        "zapis_oryginalny": "Lanska Wd:[owa]",
        "kwota_ctx": "1 zł 18 gr."
      },
      {
        "nazwisko": "Łańska",
        "imie": "[Wdowa]",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka podymnego",
        "skan": 113,
        "rok": "1775",
        "zapis_oryginalny": "Łańska Wda",
        "kwota_ctx": "3 zł."
      }
    ],
    "uwagi": "Wdowa i posesjonatka w centrum Kraśnika (zapisywana Łańska / Lanska)."
  },
  {
    "lp": 768,
    "nazwisko": "Krasowska",
    "wariant_nazwiska": "Krasowska",
    "imie": "[Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Śródmieście",
    "skany_roboczo": "#107, #110",
    "skany_list": [
      107,
      110
    ],
    "zakres_lat": "1776–1777",
    "min_rok": 1776,
    "max_rok": 1777,
    "liczba_wystapien": 2,
    "wystapienia": [
      {
        "nazwisko": "Krasowska",
        "imie": "[Wdowa]",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka 8 sympli",
        "skan": 107,
        "rok": "1776",
        "zapis_oryginalny": "Krasowska Wd:[owa]",
        "kwota_ctx": "1 zł 6 gr."
      },
      {
        "nazwisko": "Krasowska",
        "imie": "[Wdowa]",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka 8 sympli",
        "skan": 110,
        "rok": "1777",
        "zapis_oryginalny": "Krasowska wd:[owa]",
        "kwota_ctx": "1 zł 6 gr."
      }
    ],
    "uwagi": "Posesjonatka i wdowa w centrum Kraśnika (po Grzegorzu Krasowskim)."
  },
  {
    "lp": 769,
    "nazwisko": "Cuszko",
    "wariant_nazwiska": "Cuszkowa? / Ciechowa? / Cuszko",
    "imie": "[Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Zarzecze",
    "skany_roboczo": "#108, #111, #116, #119, #122, #125",
    "skany_list": [
      108,
      111,
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Cuszko",
        "imie": "[Wdowa]",
        "miejsce": "Zarzecze",
        "rola": "Płatniczka 8 sympli",
        "skan": 108,
        "rok": "1776",
        "zapis_oryginalny": "Cuszkowa Wd:[owa]",
        "kwota_ctx": "2 zł 12 gr."
      },
      {
        "nazwisko": "Cuszko",
        "imie": "[Wdowa]",
        "miejsce": "Zarzecze",
        "rola": "Płatniczka podymnego",
        "skan": 116,
        "rok": "1775",
        "zapis_oryginalny": "Ciechowa Wda",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Wdowa i posesjonatka na przedmieściu Zarzyce (zapisywana Cuszkowa / Ciechowa)."
  },
  {
    "lp": 770,
    "nazwisko": "Jasiewa",
    "wariant_nazwiska": "Jesiona? / Jesiorna? / Jasiewa",
    "imie": "[Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Piaski",
    "skany_roboczo": "#107, #111, #115, #119, #122, #125",
    "skany_list": [
      107,
      111,
      115,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Jasiewa",
        "imie": "[Wdowa]",
        "miejsce": "Piaski",
        "rola": "Płatniczka 8 sympli",
        "skan": 107,
        "rok": "1776",
        "zapis_oryginalny": "Jasiewa Wd:[owa]",
        "kwota_ctx": "5 zł 24 gr."
      },
      {
        "nazwisko": "Jasiewa",
        "imie": "[Wdowa]",
        "miejsce": "Piaski",
        "rola": "Płatniczka podymnego",
        "skan": 115,
        "rok": "1775",
        "zapis_oryginalny": "Jesiona Wda",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Posesjonatka i wdowa na przedmieściu Piasek (zapisywana Jasiewa / Jesiona / Jesiorna)."
  },
  {
    "lp": 771,
    "nazwisko": "Władarz",
    "wariant_nazwiska": "Władarzyna Wdowa",
    "imie": "[Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Góry i Podlesie",
    "skany_roboczo": "#121, #125",
    "skany_list": [
      121,
      125
    ],
    "zakres_lat": "1776–1777",
    "min_rok": 1776,
    "max_rok": 1777,
    "liczba_wystapien": 2,
    "wystapienia": [
      {
        "nazwisko": "Władarz",
        "imie": "[Wdowa]",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatniczka podymnego",
        "skan": 121,
        "rok": "1776",
        "zapis_oryginalny": "Władarzyna Wda",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Władarz",
        "imie": "[Wdowa]",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatniczka podymnego",
        "skan": 125,
        "rok": "1777",
        "zapis_oryginalny": "Władarzyna Wda",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Wdowa po włodarzu ordynackim, posiadająca chałupę na przedmieściu Góry i Podlesie."
  },
  {
    "lp": 772,
    "nazwisko": "Stachowicz",
    "wariant_nazwiska": "Stachowiczka? / Stachowiczkowa? / Stachowicz",
    "imie": "[Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Śródmieście",
    "skany_roboczo": "#106, #110",
    "skany_list": [
      106,
      110
    ],
    "zakres_lat": "1776–1777",
    "min_rok": 1776,
    "max_rok": 1777,
    "liczba_wystapien": 2,
    "wystapienia": [
      {
        "nazwisko": "Stachowicz",
        "imie": "[Wdowa]",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka 8 sympli",
        "skan": 106,
        "rok": "1776",
        "zapis_oryginalny": "Stachowiczkowa Wd:[owa]",
        "kwota_ctx": "12 gr."
      },
      {
        "nazwisko": "Stachowicz",
        "imie": "[Wdowa]",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka 8 sympli",
        "skan": 110,
        "rok": "1777",
        "zapis_oryginalny": "Stachowiczka Wd:[owa]",
        "kwota_ctx": "12 gr."
      }
    ],
    "uwagi": "Posesjonatka w centrum Kraśnika (zapisywana Stachowiczka / Stachowiczkowa)."
  },
  {
    "lp": 773,
    "nazwisko": "Łapczyna",
    "wariant_nazwiska": "Łaszczyna? / Łapczyna",
    "imie": "[Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Zarzecze",
    "skany_roboczo": "#108, #112, #116, #119, #122, #125",
    "skany_list": [
      108,
      112,
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Łapczyna",
        "imie": "[Wdowa]",
        "miejsce": "Zarzecze",
        "rola": "Płatniczka 8 sympli",
        "skan": 108,
        "rok": "1776",
        "zapis_oryginalny": "Łaszczyna Wda [Łapczyna?]",
        "kwota_ctx": "2 zł 12 gr."
      },
      {
        "nazwisko": "Łapczyna",
        "imie": "[Wdowa]",
        "miejsce": "Zarzecze",
        "rola": "Płatniczka podymnego",
        "skan": 116,
        "rok": "1775",
        "zapis_oryginalny": "Łapczyna Wda",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Posesjonatka i wdowa na przedmieściu Zarzyce (zapisywana Łapczyna / Łaszczyna)."
  },
  {
    "lp": 774,
    "nazwisko": "Ossowska",
    "wariant_nazwiska": "Ostrowska? / Ossowska",
    "imie": "Katarzyna",
    "przydomek": "",
    "funkcja": "Posesjonatka / Przedmieszczanka",
    "miejsce": "Piaski",
    "skany_roboczo": "#116, #119, #122, #125",
    "skany_list": [
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 4,
    "wystapienia": [
      {
        "nazwisko": "Ossowska",
        "imie": "Katarzyna",
        "miejsce": "Piaski",
        "rola": "Płatniczka podymnego",
        "skan": 116,
        "rok": "1775",
        "zapis_oryginalny": "Katarzyna Ossowska",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Ossowska",
        "imie": "Katarzyna",
        "miejsce": "Piaski",
        "rola": "Płatniczka podymnego",
        "skan": 119,
        "rok": "1776",
        "zapis_oryginalny": "Katarzyna Ostrowska [Ossowska]",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Ossowska",
        "imie": "Katarzyna",
        "miejsce": "Piaski",
        "rola": "Płatniczka podymnego",
        "skan": 122,
        "rok": "1776",
        "zapis_oryginalny": "Katarzyna Ostrowska [Ossowska]",
        "kwota_ctx": "2 zł."
      },
      {
        "nazwisko": "Ossowska",
        "imie": "Katarzyna",
        "miejsce": "Piaski",
        "rola": "Płatniczka podymnego",
        "skan": 125,
        "rok": "1777",
        "zapis_oryginalny": "Katarzyna Ostrowska [Ossowska]",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Posesjonatka na przedmieściu Piasek (zapisywana Ossowska / Ostrowska)."
  },
  {
    "lp": 775,
    "nazwisko": "Adamowicz",
    "wariant_nazwiska": "Adam Michał? / Adamowicz",
    "imie": "Michał",
    "przydomek": "",
    "funkcja": "Przedmieszczanin / Posesjonat",
    "miejsce": "Góry i Podlesie",
    "skany_roboczo": "#109, #112, #115, #118, #121, #124",
    "skany_list": [
      109,
      112,
      115,
      118,
      121,
      124
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Adamowicz",
        "imie": "Michał",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik sympli i podymnego",
        "skan": 109,
        "rok": "1776",
        "zapis_oryginalny": "Adam Michał",
        "kwota_ctx": "1 zł."
      }
    ],
    "uwagi": "Gospodarz na przedmieściu Góry i Podlesie (zapisywany Adam Michał / Adamowicz)."
  },
  {
    "lp": 776,
    "nazwisko": "Gajczyk",
    "wariant_nazwiska": "Gayczykowa? / Gajczykowa",
    "imie": "Janowa [Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Piaski",
    "skany_roboczo": "#107, #111, #116, #119, #122, #125",
    "skany_list": [
      107,
      111,
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Gajczyk",
        "imie": "Janowa",
        "miejsce": "Piaski",
        "rola": "Płatniczka 8 sympli",
        "skan": 107,
        "rok": "1776",
        "zapis_oryginalny": "Janowa Gayczykowa",
        "kwota_ctx": "3 zł."
      }
    ],
    "uwagi": "Wdowa i posesjonatka na przedmieściu Piasek (po Janie Gajczyku)."
  },
  {
    "lp": 777,
    "nazwisko": "Młynarczyk",
    "wariant_nazwiska": "Młynarczykowa Wdowa / Młynarczykowiczowa? / Kłusatczyzkowa?",
    "imie": "[Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Zarzecze",
    "skany_roboczo": "#108, #112, #117, #120, #123, #125",
    "skany_list": [
      108,
      112,
      117,
      120,
      123,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Młynarczyk",
        "imie": "[Wdowa]",
        "miejsce": "Zarzecze",
        "rola": "Płatniczka podymnego",
        "skan": 117,
        "rok": "1775",
        "zapis_oryginalny": "Młynarczykowiczowa Wda",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Wdowa na przedmieściu Zarzyce (zapisywana Młynarczykowa / Młynarczykowiczowa / Kłusatczyzkowa)."
  },
  {
    "lp": 778,
    "nazwisko": "Wiatrek",
    "wariant_nazwiska": "Wiatrkowa Wdowa / Wroblizna?",
    "imie": "[Wdowa]",
    "przydomek": "Wróblizna",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Zarzecze",
    "skany_roboczo": "#108, #111, #116, #119, #122, #125",
    "skany_list": [
      108,
      111,
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Wiatrek",
        "imie": "[Wdowa]",
        "miejsce": "Zarzecze",
        "rola": "Płatniczka 8 sympli",
        "skan": 108,
        "rok": "1776",
        "zapis_oryginalny": "Wiatrkowa Wd:[owa]",
        "kwota_ctx": "3 zł 10 gr."
      }
    ],
    "uwagi": "Wdowa i posesjonatka na przedmieściu Zarzyce (zapisywana Wiatrkowa / Wroblizna)."
  },
  {
    "lp": 779,
    "nazwisko": "Klisz",
    "wariant_nazwiska": "Kliszczonka? / Klypszycka? / Klisz",
    "imie": "[Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Śródmieście",
    "skany_roboczo": "#106, #110",
    "skany_list": [
      106,
      110
    ],
    "zakres_lat": "1776–1777",
    "min_rok": 1776,
    "max_rok": 1777,
    "liczba_wystapien": 2,
    "wystapienia": [
      {
        "nazwisko": "Klisz",
        "imie": "[Wdowa]",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka 8 sympli",
        "skan": 106,
        "rok": "1776",
        "zapis_oryginalny": "Klyszczonka Wd:[owa]",
        "kwota_ctx": "12 gr."
      },
      {
        "nazwisko": "Klisz",
        "imie": "[Wdowa]",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka 8 sympli",
        "skan": 110,
        "rok": "1777",
        "zapis_oryginalny": "Klypszycka wd:[owa]",
        "kwota_ctx": "12 gr."
      }
    ],
    "uwagi": "Wdowa i posesjonatka w centrum Kraśnika (zapisywana Klyszczonka / Klypszycka)."
  },
  {
    "lp": 780,
    "nazwisko": "Ćwiek",
    "wariant_nazwiska": "Ćwieka? / Cwieka? / Ćwiek",
    "imie": "Krzysztof",
    "przydomek": "",
    "funkcja": "Przedmieszczanin / Posesjonat",
    "miejsce": "Góry i Podlesie",
    "skany_roboczo": "#109, #112, #115, #118, #121, #124",
    "skany_list": [
      109,
      112,
      115,
      118,
      121,
      124
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Ćwiek",
        "imie": "Krzysztof",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik 8 sympli",
        "skan": 109,
        "rok": "1776",
        "zapis_oryginalny": "Krzyk Cwieka",
        "kwota_ctx": "10 gr."
      },
      {
        "nazwisko": "Ćwiek",
        "imie": "Krzysztof",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik podymnego",
        "skan": 115,
        "rok": "1775",
        "zapis_oryginalny": "Krzysz: Ćwieka",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Gospodarz podgórski (zapisywany Krzyk Cwieka / Krzysztof Ćwieka)."
  },
  {
    "lp": 781,
    "nazwisko": "Adamowicz",
    "wariant_nazwiska": "Adam Michał? / Adamowicz",
    "imie": "Michał",
    "przydomek": "",
    "funkcja": "Przedmieszczanin / Posesjonat",
    "miejsce": "Góry i Podlesie",
    "skany_roboczo": "#109, #112, #115, #118, #121, #124",
    "skany_list": [
      109,
      112,
      115,
      118,
      121,
      124
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Adamowicz",
        "imie": "Michał",
        "miejsce": "Góry i Podlesie",
        "rola": "Płatnik sympli i podymnego",
        "skan": 109,
        "rok": "1776",
        "zapis_oryginalny": "Adam Michał",
        "kwota_ctx": "1 zł."
      }
    ],
    "uwagi": "Gospodarz na przedmieściu Góry i Podlesie (zapisywany Adam Michał / Adamowicz)."
  },
  {
    "lp": 782,
    "nazwisko": "Gajczyk",
    "wariant_nazwiska": "Gayczykowa? / Gajczykowa",
    "imie": "Janowa [Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Piaski",
    "skany_roboczo": "#107, #111, #116, #119, #122, #125",
    "skany_list": [
      107,
      111,
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Gajczyk",
        "imie": "Janowa",
        "miejsce": "Piaski",
        "rola": "Płatniczka 8 sympli",
        "skan": 107,
        "rok": "1776",
        "zapis_oryginalny": "Janowa Gayczykowa",
        "kwota_ctx": "3 zł."
      }
    ],
    "uwagi": "Wdowa i posesjonatka na przedmieściu Piasek (po Janie Gajczyku)."
  },
  {
    "lp": 783,
    "nazwisko": "Młynarczyk",
    "wariant_nazwiska": "Młynarczykowa Wdowa / Młynarczykowiczowa? / Kłusatczyzkowa?",
    "imie": "[Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Zarzecze",
    "skany_roboczo": "#108, #112, #117, #120, #123, #125",
    "skany_list": [
      108,
      112,
      117,
      120,
      123,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Młynarczyk",
        "imie": "[Wdowa]",
        "miejsce": "Zarzecze",
        "rola": "Płatniczka podymnego",
        "skan": 117,
        "rok": "1775",
        "zapis_oryginalny": "Młynarczykowiczowa Wda",
        "kwota_ctx": "2 zł."
      }
    ],
    "uwagi": "Wdowa na przedmieściu Zarzyce (zapisywana Młynarczykowa / Młynarczykowiczowa / Kłusatczyzkowa)."
  },
  {
    "lp": 784,
    "nazwisko": "Wiatrek",
    "wariant_nazwiska": "Wiatrkowa Wdowa / Wroblizna?",
    "imie": "[Wdowa]",
    "przydomek": "Wróblizna",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Zarzecze",
    "skany_roboczo": "#108, #111, #116, #119, #122, #125",
    "skany_list": [
      108,
      111,
      116,
      119,
      122,
      125
    ],
    "zakres_lat": "1775–1777",
    "min_rok": 1775,
    "max_rok": 1777,
    "liczba_wystapien": 6,
    "wystapienia": [
      {
        "nazwisko": "Wiatrek",
        "imie": "[Wdowa]",
        "miejsce": "Zarzecze",
        "rola": "Płatniczka 8 sympli",
        "skan": 108,
        "rok": "1776",
        "zapis_oryginalny": "Wiatrkowa Wd:[owa]",
        "kwota_ctx": "3 zł 10 gr."
      }
    ],
    "uwagi": "Wdowa i posesjonatka na przedmieściu Zarzyce (zapisywana Wiatrkowa / Wroblizna)."
  },
  {
    "lp": 785,
    "nazwisko": "Klisz",
    "wariant_nazwiska": "Kliszczonka? / Klypszycka? / Klisz",
    "imie": "[Wdowa]",
    "przydomek": "",
    "funkcja": "Posesjonatka / Wdowa",
    "miejsce": "Śródmieście",
    "skany_roboczo": "#106, #110",
    "skany_list": [
      106,
      110
    ],
    "zakres_lat": "1776–1777",
    "min_rok": 1776,
    "max_rok": 1777,
    "liczba_wystapien": 2,
    "wystapienia": [
      {
        "nazwisko": "Klisz",
        "imie": "[Wdowa]",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka 8 sympli",
        "skan": 106,
        "rok": "1776",
        "zapis_oryginalny": "Klyszczonka Wd:[owa]",
        "kwota_ctx": "12 gr."
      },
      {
        "nazwisko": "Klisz",
        "imie": "[Wdowa]",
        "miejsce": "Śródmieście",
        "rola": "Płatniczka 8 sympli",
        "skan": 110,
        "rok": "1777",
        "zapis_oryginalny": "Klypszycka wd:[owa]",
        "kwota_ctx": "12 gr."
      }
    ],
    "uwagi": "Wdowa i posesjonatka w centrum Kraśnika (zapisywana Klyszczonka / Klypszycka)."
  }
]


# 1. Aktualizacja mainData
d_main = {int(x['nr_skanu']): x for x in main_data}
for ns, upd in transkrypcje_p7.items():
    if ns in d_main:
        for k, v in upd.items():
            d_main[ns][k] = v
        d_main[ns]['link_swa'] = "https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/2062417"

# 2. Aktualizacja genData
gen_map = {p['lp']: p for p in gen_data}
for np in nowe_profile_p7:
    if np['lp'] not in gen_map:
        gen_data.append(np)
        gen_map[np['lp']] = np
    else:
        # zaktualizuj pola
        for k, v in np.items():
            gen_map[np['lp']][k] = v

# Aktualizacje wariantów dla profili wcześniejszych
updates_existing = {
    114: "Fisier? / Fiszerem / Fizer?",
    115: "Fisier? / Fiszerem / Fizer?",
    157: "Jasiuricz? / Jąśkiewicz? / Jaśkiewicz? / Jasiłowicz? / Jasiewicz",
    224: "Krzanszyski? / Wisiadłowski? / Wziąndtki? / Krzanowski",
    707: "Krzywickich / Krywickiy / Krzydlinski / Krzywicki",
    245: "Rępa? / Kępa",
    247: "Rępa? / Kępa",
    253: "Rępa? / Kępa",
    256: "Rępa? / Kępa",
    259: "Rępa? / Kępa",
    278: "Latoskowicz? / Latosowicz",
    279: "Latoskowicz? / Latosowicz",
    98: "Pruga? / Fruga",
    609: "Widak? / Oslak? / Wolak",
    614: "Widak? / Wolak",
    748: "Stemborfski? / Stemborfki? / Słomkiewski? / Stembowski",
    734: "Kliszczonka? / Kliszewski",
    629: "Zajączkowa? / Lagierkowa? / Zajączkowski",
    381: "Pilachowa? / Kielachowa? / Pietrachowa? / Piłach? / Piłachowa",
    384: "Piłaszkiewicz / Pilaszkiewicz",
    385: "Piłaszkiewicz / Pilaszkiewicz",
    386: "Piłaszkiewicz / Pilaszkiewicz",
    745: "Gęzarch? / Warsz: Gęzarek? / Rzeszotek? / Gęzarek",
    746: "Aszoski? / Okposki? / Oszoska? / Oszowski",
    747: "Sadoftka? / Saidka? / Sadowska",
    749: "Szpiciarzk? / Paszkiewicz? / Szpiciarz"
}
for lp, war in updates_existing.items():
    if lp in gen_map:
        gen_map[lp]['wariant_nazwiska'] = war

# Serializacja
new_main_json = json.dumps(main_data, ensure_ascii=False, indent=2)
new_gen_json = json.dumps(gen_data, ensure_ascii=False, indent=2)

html_content = html_content[:m_start] + "const mainData = " + new_main_json + html_content[m_end:]
g_start = html_content.find('const genData = [')
g_end = html_content.find('];', g_start) + 1
html_content = html_content[:g_start] + "const genData = " + new_gen_json + html_content[g_end:]

# Aktualizacja KPI
html_content = re.sub(
    r"(<span class=\"tab-badge\">)\\d+(</span>\\s*</button>\\s*<button class=\"tab-btn\" onclick=\"switchTab\('monograph-tab')",
    rf'\g<1>{len(gen_data)}\g<2>',
    html_content
)
html_content = re.sub(
    r'(<div class="stat-title">Mieszkańcy Kraśnika \(unikalne profile\)</div>\s*<div class="stat-value">)\d+(</div>)',
    rf'\g<1>{len(gen_data)}\g<2>',
    html_content
)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

fields = ['lp', 'nazwisko', 'wariant_nazwiska', 'imie', 'przydomek', 'funkcja', 'miejsce', 'zakres_lat', 'skany_roboczo', 'uwagi']
with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
    writer.writeheader()
    for row in gen_data:
        writer.writerow(row)

print(f"Pomyślnie zaktualizowano: mainData={len(main_data)}, genData={len(gen_data)}.")
print(f"Zapisano HTML oraz CSV: {CSV_PATH}")
