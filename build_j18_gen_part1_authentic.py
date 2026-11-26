# -*- coding: utf-8 -*-
import json
import csv

gen_data = []
profile_map = {}

def add_occ(nazwisko, imie, miejsce, funkcja, wariant, skan, rok, zapis, kwota_ctx):
    key = (nazwisko, imie, miejsce)
    if key in profile_map:
        p = profile_map[key]
        if wariant:
            existing = p.get('wariant_nazwiska')
            if not existing:
                p['wariant_nazwiska'] = wariant
            elif wariant not in existing:
                p['wariant_nazwiska'] = f"{existing} / {wariant}"
        if skan not in p['skany_list']:
            p['skany_list'].append(skan)
            p['skany_list'].sort()
            p['skany_roboczo'] = ", ".join(f"#{s}" for s in p['skany_list'])
        p['wystapienia'].append({
            "skan": skan,
            "rok": str(rok),
            "zapis_oryginalny": zapis,
            "rola": kwota_ctx,
            "kwota_ctx": kwota_ctx
        })
        p['liczba_wystapien'] = len(p['wystapienia'])
        years = []
        for w in p['wystapienia']:
            for part in str(w['rok']).replace('–', '-').split('-'):
                if part.strip().isdigit():
                    years.append(int(part.strip()))
        if years:
            p['min_rok'] = min(years)
            mn, mx = min(years), max(years)
            p['zakres_lat'] = f"{mn}" if mn == mx else f"{mn}–{mx}"
    else:
        new_lp = len(gen_data) + 1
        new_p = {
            "lp": new_lp,
            "nazwisko": nazwisko,
            "imie": imie,
            "miejsce": miejsce,
            "funkcja": funkcja or "Mieszkaniec / Strona w aktach",
            "wariant_nazwiska": wariant,
            "skany_list": [skan],
            "skany_roboczo": f"#{skan}",
            "min_rok": int(rok),
            "zakres_lat": str(rok),
            "liczba_wystapien": 1,
            "wystapienia": [{
                "skan": skan,
                "rok": str(rok),
                "zapis_oryginalny": zapis,
                "rola": kwota_ctx,
                "kwota_ctx": kwota_ctx
            }],
            "notatka_biograficzna": f"Osoba odnotowana w Partii 1 (skany 1–25) Jednostki 18 (sygn. 35/40/0/1/18) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 5 (wyklejka 1625 r.) ---
add_occ("Zdebik", "Mieszkaniec", "Kraśnik", "Płatnik poboru", "Zdobyk?", 5, 1625, "Zdebik [Zdobyk?]", "Zapisek poborowy z 1625 r. od bramy")
add_occ("Feliks", "Mieszkaniec", "Kraśnik", "Płatnik poboru", "Felix", 5, 1625, "Felix", "Zapisek poborowy z 1625 r. (groszy)")
add_occ("Barankowic", "Mieszkaniec", "Kraśnik", "Płatnik poboru", None, 5, 1625, "Barankowic", "Zapisek poborowy z 1625 r. (groszy)")

# --- Skan 7 (fol. 1r) ---
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Burmistrz kraśnicki", None, 7, 1653, "Famatus Ubaldus Janaszkowic Proconsul", "Założyciel księgi Acta Pupillorum")
add_occ("Doliński", "F.", "Kraśnik", "Sędzia pokoju (1827 r.)", "Doliński?", 7, 1827, "F. Doliński [?]", "Poświadczenie księgi w Sądzie Pokoju (15 X 1827 r.)")

# --- Skan 8 (fol. 2r) ---
add_occ("Giża", "Tomasz", "Kraśnik", "Zmarły mieszkaniec", None, 8, 1653, "olim Thomas Giża", "Ojciec małoletnich córek Katarzyny, Krystyny i Zofii")
add_occ("Giżanka", "Katarzyna", "Kraśnik", "Sierota / Córka Tomasza Giży", "Giża", 8, 1653, "Catharina filia Thomae Giża", "Otrzymała opiekunów")
add_occ("Giżanka", "Krystyna", "Kraśnik", "Sierota / Córka Tomasza Giży", "Giża", 8, 1653, "Christina filia Thomae Giża", "Otrzymała opiekunów")
add_occ("Giżanka", "Zofia", "Kraśnik", "Sierota / Córka Tomasza Giży", "Giża", 8, 1653, "Sophia filia Thomae Giża", "Otrzymała opiekunów")
add_occ("Kaczmarczyk", "Szymon", "Kraśnik", "Opiekun sierot / Mieszczanin", None, 8, 1653, "Simon Kaczmarczyk Civis Crasnicensis", "Wyznaczony opiekunem córek Tomasza Giży")
add_occ("Sokołowicz", "Wawrzyniec", "Kraśnik", "Opiekun sierot / Mieszczanin", None, 8, 1653, "Laurentius Sokołowicz Civis Crasnicensis", "Wyznaczony opiekunem córek Tomasza Giży")
add_occ("Koniega", "Maciej", "Kraśnik", "Opiekun sierot", None, 8, 1653, "Mathias Koniega", "Rozliczenie opieki po Wojciechu Kłopotku")
add_occ("Kłopotek", "Paweł", "Kraśnik", "Opiekun / Strona", None, 8, 1653, "Paulus Kłopotek", "Sprawa rozliczenia po Wojciechu Kłopotku")
add_occ("Kłopotek", "Wojciech", "Kraśnik", "Zmarły", None, 8, 1653, "nieboszczyk Woyciech Kłopotek", "Spadek po nim (koń za 72 złp, jałówka za 24 złp)")
add_occ("Kłopotek", "Sebastian", "Kraśnik", "Nabywca / Krewny", None, 8, 1653, "Sebestyan", "Kupił konia za 72 złp")
add_occ("Borytkowski", "Wierzyciel", "Kraśnik", "Wierzyciel", "Borytkowski?", 8, 1653, "Borytkowski", "Rozliczenie długu 55 złp 13 gr i 13 złp 15 gr")

# --- Skan 9 (fol. 2v) ---
add_occ("Główniarka", "Jadwiga", "Suchynia", "Pracowita / Powódka", "Głównia?", 9, 1653, "Laboriosa Hedvigis de Suchynia", "Proces przeciw Katarzynie Błaszczykowej o ruchomości i 70 złp")
add_occ("Błaszczykowa", "Katarzyna", "Kraśnik", "Żona Pawła Błaszczyka", None, 9, 1653, "Catharina Pauli Błaszczyk consors", "Pozwana o rzeczy ruchome i pogrzebowe (3 złp)")
add_occ("Błaszczyk", "Paweł", "Kraśnik", "Mąż Katarzyny", None, 9, 1653, "Paulus Błaszczyk", "Wzmiankowany jako mąż pozwanej")
add_occ("Koniega", "Maciej", "Kraśnik", "Powód / Opiekun", None, 9, 1653, "Koniega", "Otwarcie wpisu z 12 XII 1653 r.")

# --- Skan 10 (fol. 3r) ---
add_occ("Koniega", "Maciej", "Kraśnik", "Opiekun sierot", None, 10, 1653, "Mathias Koniega Tutor", "Rozliczenie opiekuńcze z Kłopotkami")
add_occ("Kłopotek", "Paweł", "Kraśnik", "Opiekun / Strona", None, 10, 1653, "Paulus Kłopotek", "Rozliczenie przed Sądem Radzieckim")
add_occ("Kłopotek", "Bartłomiej", "Kraśnik", "Sukcesor Wojciecha Kłopotka", None, 10, 1653, "Bartholomaeus Kłopotek", "Rozliczenie wydatków pogrzebowych")
add_occ("Kłopotek", "Jan", "Kraśnik", "Sukcesor Wojciecha Kłopotka", None, 10, 1653, "Joannes Kłopotek", "Rozliczenie wydatków pogrzebowych")
add_occ("Kłopotek", "Gabriel", "Kraśnik", "Sukcesor Wojciecha Kłopotka", None, 10, 1653, "Gabriel Kłopotek", "Rozliczenie wydatków pogrzebowych")
add_occ("Kłopotek", "Wojciech", "Kraśnik", "Zmarły", None, 10, 1653, "nieboszczyk Woyciech Kłopotek", "Spadek i pokwitowanie opieki")

# --- Skan 11 (fol. 3v) ---
add_occ("Kwasowic", "Augustyn", "Kraśnik", "Sławetny / Sukcesor", None, 11, 1653, "Famatus Augustinus Kwasowic", "Kwitował opiekunów oraz dochodził części po zmarłej Zofii")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki / Opiekun", None, 11, 1653, "Stanisław Nawrocki", "Pokwitowany z opieki nad Augustynem Kwasowicem")
add_occ("Jasielski", "Szymon", "Kraśnik", "Ławnik przysięgły / Opiekun", None, 11, 1653, "Simon Jasielski Scabinus Juratus", "Pokwitowany z opieki nad Kwasowicami")
add_occ("Koniega", "Maciej", "Kraśnik", "Opiekun sierot Kwasowskich", None, 11, 1653, "Mathias Koniega Tutor Pupillorum", "Przedłożył rachunek opiekuńczy")
add_occ("Kwasowska", "Zofia", "Kraśnik", "Zmarła w powietrzu (zarazie)", None, 11, 1653, "nieboszczka Zofia", "Spadek po zmarłej w zarazie")
add_occ("Kwasowic", "Fabian", "Kraśnik", "Zmarły brat Augustyna", None, 11, 1653, "Fabian", "Wspomniany w sprawie sukcesyjnej")

# --- Skan 12 (fol. 4r) ---
add_occ("Kwasowic", "Augustyn", "Kraśnik", "Sukcesor", None, 12, 1653, "Augustyn Kwasowic", "Rachunek majątkowy (629 złp, 314 złp 15 gr, 122 złp 10 gr)")
add_occ("Kwasowska", "Zofia", "Kraśnik", "Zmarła w zarazie", None, 12, 1653, "Zofia", "Wyliczenie jej masy spadkowej (629 złp)")
add_occ("Kwasowic", "Tomasz", "Kraśnik", "Sukcesor / Krewny", None, 12, 1653, "Tomasz Kwasowic", "Rozliczenie 102 złp u Reszki")
add_occ("Reszka", "Mieszczanin", "Kraśnik", "Dłużnik / Strona", None, 12, 1653, "surowy Reszka", "Rozliczenie sumy 102 złp")

# --- Skan 13 (fol. 4v) ---
add_occ("Kwasowic", "Augustyn", "Kraśnik", "Sukcesor", None, 13, 1653, "Augustyn Kwasowic", "Dokończenie rachunku (337 złp 23 gr, 950 złp z domem)")
add_occ("Reszka", "Mieszczanin", "Kraśnik", "Strona rozliczeń", None, 13, 1653, "Reszka z żoną", "Rozliczenie z Gieradą i opiekunami")
add_occ("Gierada", "Piotr", "Kraśnik", "Krewny / Strona", "Gierad?", 13, 1653, "Gierada", "Wspomniany w dziale majątkowym")

# --- Skan 14 (fol. 5r) ---
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Burmistrz kraśnicki", None, 14, 1654, "Ubaldus Janaszkowic Proconsul", "Przewodniczył sesji 6 II 1654 r.")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki", None, 14, 1654, "Martinus Sitarski Consul", "Obecny przy ustanowieniu opiekunów")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 14, 1654, "Stanislaus Nawrocki Consul", "Obecny przy ustanowieniu opiekunów")
add_occ("Tarasa", "Maciej", "Kraśnik", "Rajca kraśnicki", None, 14, 1654, "Mathias Tarasa Consul", "Obecny przy ustanowieniu opiekunów")
add_occ("Maziewski", "Stanisław", "Przedmieście Kraśnickie", "Przedmieszczanin / Wnioskodawca", None, 14, 1654, "Stanislaus Maziewski anteoppidanus", "Wnioskował o opiekunów dla Bartłomieja Rodzonka")
add_occ("Rodzonek", "Bartłomiej", "Przedmieście Kraśnickie", "Małoletni sierota", None, 14, 1654, "Bartholomaeus Rodzonek", "Otrzymał opiekunów Gabriela Buta i Bartłomieja Kulkę")
add_occ("But", "Gabriel", "Kraśnik", "Opiekun sieroty / Mieszczanin", None, 14, 1654, "Gabriel But Civis Crasnicensis", "Wyznaczony opiekunem Bartłomieja Rodzonka")
add_occ("Kulka", "Bartłomiej", "Przedmieście Kraśnickie", "Opiekun sieroty / Przedmieszczanin", None, 14, 1654, "Bartholomaeus Kulka anteoppidanus", "Wyznaczony opiekunem Bartłomieja Rodzonka")
add_occ("Zdebik", "Adam", "Kraśnik", "Małoletni sierota", None, 14, 1654, "Adamus Zdebik", "Otrzymał opiekuna Jana Kozika alias Szczęsnego")
add_occ("Kozik", "Jan", "Kraśnik", "Opiekun sieroty", "Szczęsny", 14, 1654, "Joannes Kozik alias Szczęsny", "Wyznaczony opiekunem Adama Zdebika")
add_occ("Szczygieł", "Szymon", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona działu", None, 14, 1654, "Simon Szczygieł anteoppidanus", "Początek działu majątkowego z Matyaszem Paluchem")
add_occ("Paluch", "Matyasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Szwagier", None, 14, 1654, "Mathias Paluch anteoppidanus", "Dział majątkowy z Szymonem Szczygiełem")

# --- Skan 15 (fol. 5v) ---
add_occ("Paluch", "Matyasz", "Przedmieście Kraśnickie", "Zięć / Strona działu", None, 15, 1654, "Matyasz Paluch", "Otrzymał parę wołów, krowę z cielęciem i jałówkę")
add_occ("Szczygieł", "Szymon", "Przedmieście Kraśnickie", "Szwagier / Strona działu", None, 15, 1654, "Szymon Szczygieł", "Odliczył 17 złp za pogrzeb ojca i odpuścił 3 złp")
add_occ("Sikier", "Marcin", "Przedmieście Kraśnickie", "Rozjemca / Przedmieszczanin", None, 15, 1654, "Marcin Sikier", "Przyjaciel przy dziale Palucha ze Szczygiełem")
add_occ("Świętek", "Bartosz", "Przedmieście Kraśnickie", "Rozjemca / Przedmieszczanin", None, 15, 1654, "Bartosz Świętek", "Przyjaciel przy dziale Palucha ze Szczygiełem")
add_occ("Tokarczyk", "Wojciech", "Przedmieście Kraśnickie", "Rozjemca / Przedmieszczanin", None, 15, 1654, "Woyciech Tokarczyk", "Przyjaciel przy dziale Palucha ze Szczygiełem")
add_occ("Koniega", "Maciej", "Kraśnik", "Rozjemca", None, 15, 1654, "Maciey Koniega", "Przyjaciel przy dziale ze strony Szymona Szczygła")
add_occ("Węgorek", "Sebastian", "Kraśnik", "Rozjemca", None, 15, 1654, "Sebestyan Węgorek", "Przyjaciel przy dziale ze strony Szymona Szczygła")

# --- Skan 16 (fol. 6r) ---
add_occ("Szczygieł", "Szymon", "Przedmieście Kraśnickie", "Strona działu", None, 16, 1654, "Szymon Szczygieł", "Otrzymał ćwierć z ogrodem i budynkiem")
add_occ("Paluch", "Matyasz", "Przedmieście Kraśnickie", "Strona działu", None, 16, 1654, "Matyasz Paluch", "Zatrzymał chałupę, spłatę 90 złp")
add_occ("Kordek", "Sąsiad", "Przedmieście Kraśnickie", "Posesjonat", "Kordek?", 16, 1654, "granice Kordkowe", "Wzmiankowany jako sąsiad graniczny")

# --- Skan 17 (fol. 6v) ---
add_occ("Szczygieł", "Szymon", "Przedmieście Kraśnickie", "Strona działu", None, 17, 1654, "Szymon Szczygieł", "Wadium działu (20, 10, 10, 5 grzywien)")
add_occ("Paluch", "Matyasz", "Przedmieście Kraśnickie", "Strona działu", None, 17, 1654, "Matyasz Paluch", "Wadium działu")
add_occ("Nowak", "Benedykt", "Kraśnik", "Powód / Sierota", None, 17, 1654, "Benedictus Nowak", "Skarga z siostrą Elżbietą przeciw opiekunom i matce")
add_occ("Nowakówna", "Elżbieta", "Kraśnik", "Powódka / Siostra Benedykta", None, 17, 1654, "Helizabet soror Benedicti Nowak", "Współpowódka przeciw opiekunom i matce")
add_occ("Sęk", "Szymon", "Kraśnik", "Opiekun / Mieszczanin", None, 17, 1654, "Simon Sęk Civis Crasnicensis", "Opiekun sierot Nowaków")
add_occ("Ciszkowic", "Stanisław", "Kraśnik", "Opiekun / Mieszczanin", None, 17, 1654, "Stanislaus Ciszkowic Civis Crasnicensis", "Opiekun sierot Nowaków")
add_occ("Stolska", "Maryna", "Przedmieście Kraśnickie", "Matka powódki / Pozwana", "Ciasnosukowa?", 17, 1654, "Marina Stolska [Ciasnosukowa?]", "Pozwana o brak rachunku za 7 lat opieki po pierwszym mężu Nowaku")
add_occ("Dudka", "Matyasz", "Kraśnik", "Zmarły drugi mąż Maryny", None, 17, 1654, "nieboszczyk Matias Dudka", "Był opiekunem sierot Nowaków")
add_occ("Stolski", "Marcin", "Przedmieście Kraśnickie", "Obecny mąż Maryny", None, 17, 1654, "Marcin Stolski", "Obecny mąż pozwanej Maryny")

# --- Skan 18 (fol. 7r) ---
add_occ("Nowak", "Benedykt", "Kraśnik", "Powód", None, 18, 1654, "Benedykt Nowak", "Dekret przyznający 313 złp 25 gr reszty")
add_occ("Nowakówna", "Elżbieta", "Kraśnik", "Powódka", None, 18, 1654, "Elżbieta Nowakówna", "Dekret w sprawie spadku po ojcu")
add_occ("Stolska", "Maryna", "Przedmieście Kraśnickie", "Pozwana", "Ciasnosukowa?", 18, 1654, "Maryna Stolska", "Nakaz zapłaty i złożenia przysięgi")
add_occ("Szydło", "Łukasz", "Kraśnik", "Szewc / Wierzyciel", None, 18, 1654, "Łukasz Szydło", "Otrzymał 23 złp 10 gr z masy spadkowej")
add_occ("Dudka", "Wojciech", "Kraśnik", "Brat nieboszczyka Matyasza", None, 18, 1654, "Woyciech Dudka brat nieboszczykowskiego", "Otrzymał 17 złp 27 gr")

# --- Skan 19 (fol. 7v) ---
add_occ("Nowakówna", "Elżbieta", "Kraśnik", "Cedująca spadek (wyjazd do Lublina)", None, 19, 1654, "Helizabet Nowakówna", "Zrzekła się części na rzecz brata Benedykta przed wyjazdem do Lublina")
add_occ("Nowak", "Benedykt", "Kraśnik", "Beneficjent cesji siostry", None, 19, 1654, "Benedykt Nowak", "Otrzymał prawa od siostry Elżbiety")
add_occ("Stolska", "Maryna", "Przedmieście Kraśnickie", "Pozwana", "Ciasnosukowa?", 19, 1654, "Maryna Stolska", "Dokończenie dekretu Nowaków")
add_occ("Dudka", "Matyasz", "Kraśnik", "Zmarły opiekun", None, 19, 1654, "Matyas Dudka", "Zabezpieczenie 313 złp 25 gr na jego dobrach")
add_occ("Kańkowa", "Dorota", "Kraśnik", "Wdowa", None, 19, 1654, "Dorothea Kańkowa vidua", "Otrzymała opiekuna Augustyna Kwasowica (4 V 1654 r.)")
add_occ("Kwasowic", "Augustyn", "Kraśnik", "Opiekun wdowy", None, 19, 1654, "Augustinus Kwasowic", "Wyznaczony opiekunem Doroty Kańkowej")

# --- Skan 20 (fol. 8r) ---
add_occ("Kamińska", "Zofia", "Kraśnik", "Wdowa", None, 20, 1654, "Zophia Kamińska vidua", "Otrzymała opiekuna Jana Kępę alias Sołeckiego")
add_occ("Kępa", "Jan", "Kraśnik", "Opiekun wdowy", "Sołecki", 20, 1654, "Joannes Kępa alias Sołecki", "Wyznaczony opiekunem Zofii Kamińskiej")
add_occ("Rodzonek", "Stanisław", "Przedmieście Kraśnickie", "Zmarły", None, 20, 1654, "Stanislaus Rodzonek", "Spisano pośmiertny inwentarz jego dóbr (18 V 1654 r.)")
add_occ("Rodzonek", "Bartłomiej", "Przedmieście Kraśnickie", "Sierota / Syn Stanisława", None, 20, 1654, "Bartholomaeus Rodzonek", "Sukcesor dóbr z inwentarza")
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Rajca kraśnicki", None, 20, 1654, "Ubaldus Janaszkowic Consul", "Delegujący komisję inwentarzową")
add_occ("Tarasa", "Maciej", "Kraśnik", "Rajca kraśnicki", None, 20, 1654, "Mathias Tarasa Consul", "Delegujący komisję inwentarzową")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Deputowany", None, 20, 1654, "Martinus Sitarski Consul", "Deputowany do spisania inwentarza Rodzonka")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Burmistrz kraśnicki / Deputowany", None, 20, 1654, "Stanislaus Nawrocki Proconsul", "Burmistrz delegowany do inwentarza Rodzonka")
add_occ("But", "Gabriel", "Kraśnik", "Opiekun sieroty", None, 20, 1654, "Gabriel But", "Obecny przy spisie inwentarza Rodzonka")
add_occ("Kulka", "Bartłomiej", "Przedmieście Kraśnickie", "Opiekun sieroty", None, 20, 1654, "Bartholomaeus Kulka", "Obecny przy spisie inwentarza Rodzonka")
add_occ("Piotrowski", "Sebastian", "Przedmieście Kraśnickie", "Sąsiad", None, 20, 1654, "Sebestyan Piotrowski", "Sąsiad gruntu Rodzonków na Zarzeczu")
add_occ("Maziewski", "Stanisław", "Przedmieście Kraśnickie", "Posiadacz / Sąsiad", None, 20, 1654, "Stanisław Maziewski", "Mieszkał w domu Rodzonków")
add_occ("Kaczmarczyk", "Jan", "Przedmieście Kraśnickie", "Mieszkaniec", None, 20, 1654, "Jan Kaczmarczyk", "Wspomniany w inwentarzu domu")

# --- Skan 21 (fol. 8v) ---
add_occ("Rodzonek", "Stanisław", "Przedmieście Kraśnickie", "Zmarły", None, 21, 1654, "Stanisław Rodzonek", "Dokończenie inwentarza sprzętów, zabudowań i 3 ćwierci roli")
add_occ("Piotrowski", "Sebastian", "Przedmieście Kraśnickie", "Sąsiad", None, 21, 1654, "Sebestyan Piotrowski", "Sąsiad pierwszej ćwierci roli")
add_occ("Maziewski", "Stanisław", "Przedmieście Kraśnickie", "Sąsiad", None, 21, 1654, "Stanisław Maziewski", "Sąsiad drugiej ćwierci roli")
add_occ("Łowicki", "Sąsiad", "Piaski", "Posesjonat", None, 21, 1654, "Łowicki", "Sąsiad ćwierci roli na Piasku")
add_occ("Grzebieniowski", "Sąsiad", "Piaski", "Posesjonat", None, 21, 1654, "Grzebieniowski", "Sąsiad ćwierci roli na Piasku")

# --- Skan 22 (fol. 9r) ---
add_occ("Piotrowski", "Sebastian", "Przedmieście Kraśnickie", "Sąsiad", None, 22, 1654, "Sebestyan Piotrowski", "Sąsiad ogrodu śliwowego")
add_occ("Paczanowski", "Łukasz", "Kraśnik", "Małoletni / Podopieczny", None, 22, 1654, "Lucas Paczanowski", "Sprawa opieki (12 VIII 1654 r.)")
add_occ("Paczanowski", "Jakub", "Kraśnik", "Wnioskodawca", None, 22, 1654, "Jacobus Paczanowski", "Wnioskował o opiekuna")
add_occ("Kępa", "Jan", "Przedmieście Kraśnickie", "Opiekun", "Sołecki / Hanus?", 22, 1654, "Joannes Kępa alias Hanus", "Wyznaczony opiekunem w sprawie Paczanowskich")

# --- Skan 23 (fol. 9v) ---
add_occ("Koniega", "Maciej", "Kraśnik", "Ławnik przysięgły i opiekun", None, 23, 1655, "Maciey Koniega Ławnik Przysięgły", "Złożył rachunek z dóbr Jana Miarowica")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Mieszczanin i opiekun", None, 23, 1655, "Woyciech Olęcki Mieszczanin krasnicki", "Współopiekun dóbr Jana Miarowica")
add_occ("Miarowic", "Jan", "Kraśnik", "Małoletni zmarły", None, 23, 1655, "Jan Miarowic", "Rozliczenie jego masy majątkowej")
add_occ("Kwasowic", "Augustyn", "Kraśnik", "Ławnik przysięgły", None, 23, 1655, "Augustyn Kwasowic Ławnik Przysięgły", "Obecny przy rachunku opiekunów Miarowica")
add_occ("Piasecki", "Dłużnik", "Kraśnik", "Dłużnik", None, 23, 1655, "Piasecki", "Pożyczył 100 złp z masy Miarowica")
add_occ("Wójcik", "Jan", "Kraśnik", "Dłużnik", None, 23, 1655, "Jan Woycik", "Dług 109 złp (odsetki 30 złp i 20 złp)")
add_occ("Kowal", "Stanisław", "Kraśnik", "Dłużnik", None, 23, 1655, "Stanisław Kowal", "Dług 50 złp z masy Miarowica")
add_occ("Kotlarka", "Wdowa", "Kraśnik", "Wdowa / Dłużniczka", None, 23, 1655, "Kotlarka wdowa", "Wpłaciła 7 złp oraz 30 złp z dekretu")

# --- Skan 24 (fol. 10r) ---
add_occ("Koniega", "Maciej", "Kraśnik", "Opiekun", None, 24, 1655, "Maciey Koniega", "Zatwierdzenie rachunku opiekunów Miarowica (100 złp)")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Opiekun", None, 24, 1655, "Woyciech Olęcki", "Zatwierdzenie rachunku opiekunów Miarowica")
add_occ("Miarowic", "Jan", "Kraśnik", "Zmarły", None, 24, 1655, "Jan Miarowic", "Dekret z 1655 r. dotyczący rachunków opieki")
add_occ("Kwasowic", "Augustyn", "Kraśnik", "Ławnik przysięgły / Dłużnik", None, 24, 1655, "Augustinus Kwasowic Scabinus Juratus", "Zeznał dług 50 złp wobec opiekunów Miarowica")

# --- Skan 25 (fol. 10v) ---
add_occ("Miarowiczówna", "Regina", "Kraśnik", "Sierota / Dłużniczka", None, 25, 1655, "Panna Regina Miarowiczówna", "Zapisała oblig 50 złp na domu w Rynku i rolach na Podlesiu")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Opiekun", None, 25, 1655, "Woyciech Olęcki Opiekun", "Wyraził zgodę na oblig Reginy Miarowiczówny")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki / Opiekun i sąsiad", None, 25, 1655, "Stanisław Nawrocki Rayca krasnicki", "Wierzyciel obligu 50 złp i sąsiad domu w Rynku")
add_occ("Dudka", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin / Sąsiad", None, 25, 1655, "Jan Dudka", "Sąsiad roli na Podlesiu")
add_occ("Łyś", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin / Sąsiad", "Łysy?", 25, 1655, "Woyciech Łyś", "Sąsiad roli na Podlesiu")

# Zapis gen_data_j18_part1.json
with open('/home/ubuntu/workspace/Gen/gen_data_j18_part1.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

# Eksport CSV UTF-8-SIG zgodnie z SKILL.md
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j18_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
    writer.writerow(['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'])
    for p in gen_data:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p.get('funkcja') or '',
            p.get('skany_roboczo', ''),
            p.get('zakres_lat', ''),
            p.get('liczba_wystapien', 1),
            p.get('wariant_nazwiska') or ''
        ])

print(f"SUCCESS: gen_data_j18_part1.json ({len(gen_data)} profiles) and CSV exported.")
