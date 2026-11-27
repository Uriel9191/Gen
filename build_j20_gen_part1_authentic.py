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
            else:
                parts = [x.strip() for x in existing.split('/')]
                for wp in [x.strip() for x in wariant.split('/')]:
                    if wp and wp not in parts:
                        parts.append(wp)
                p['wariant_nazwiska'] = " / ".join(parts)
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
            "min_rok": int(str(rok).split('–')[0]),
            "zakres_lat": str(rok),
            "liczba_wystapien": 1,
            "wystapienia": [{
                "skan": skan,
                "rok": str(rok),
                "zapis_oryginalny": zapis,
                "rola": kwota_ctx,
                "kwota_ctx": kwota_ctx
            }],
            "notatka_biograficzna": f"Osoba odnotowana w księdze wójtowsko-ławniczej Kraśnika (Jednostka 20, skan #{skan}, {rok} r.)."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# Skan 6 (1657)
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły kraśnicki / Aktor", None, 6, 1657, "Błażej Kołodziejczyk", "Relacja ławnika oraz proces przeciw M. Dąbkowi o najście domu")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik przysięgły kraśnicki", None, 6, 1657, "Maciej Konięga", "Relacja ławnika o słowach W. Jatańca")
add_occ("Jataniec", "Wojciech", "Kraśnik", "Mieszczanin / Wzmiankowany", "Jatańczyk [?]", 6, 1657, "Wojciecha Jatańca [Jatańczyka?]", "Wzmiankowany w relacji ławników")
add_occ("Dzierżek", "Błażej", "Piaski", "Wzmiankowany", None, 6, 1657, "Błażeju Dzierżku", "Wzmiankowany w relacji ławników")
add_occ("Dąbek", "Maciej", "Kraśnik", "Pozwany", "Bęben [?]", 6, 1657, "Mathiam Dąbek [Bęben?]", "Proces o najście domu")
add_occ("Baltazarowa", "Katarzyna", "Kraśnik", "Instygatorka", "Balcerzykowa [?]", 6, 1657, "Catharinae Baltazarowa [Balcerzykowa?]", "Sprawa spadkowa")
add_occ("Paplenik", "Marcin", "Kraśnik", "Powód", "Paplenik [?]", 6, 1657, "Martinum Paplenik [?]", "Spór z wdową Frysiową o półkorca żyta")
add_occ("Frysiowa", "Wdowa", "Kraśnik", "Wdowa / Pozwana", "Frysiowa [?]", 6, 1657, "Viduam Frysiowa [?]", "Nakaz zwrotu półkorca żyta")

# Skan 7 (1657)
add_occ("Pękowa", "Anna", "Kraśnik", "Wdowa / Pozwana", "Pękowa [?]", 7, 1657, "Viduam Annam Pękowa [?]", "Proces o dług po nieboszczyku")
add_occ("Lasek", "Walenty", "Kraśnik", "Pozwany / Kondemnat", "Łączek [?]", 7, 1657, "Valentini Lasek [Łączek?]", "Skazany na kontumację")
add_occ("Żyłówka", "Jan", "Kraśnik", "Powód", "Kender [?]", 7, 1657, "Joannes Kender [?] Żyłówka [?]", "Spór z W. Potockim o 15 fl za krowę")
add_occ("Potocki", "Wojciech", "Kraśnik", "Pozwany", None, 7, 1657, "Albertum Potocki", "Spór z J. Żyłówką o 15 fl")
add_occ("Marlik", "Andrzej", "Kraśnik", "Strona w aktach", "Marlik [?]", 7, 1657, "Marlik [?]", "Spór o zagon roli ze Świdnickim")
add_occ("Skwarek", "Walenty", "Kraśnik", "Powód", "Skwarek [?]", 7, 1657, "Valentinum Skwarek [?]", "Spór z W. Batusikiem o koła i robotę kołodziejską")
add_occ("Batusik", "Wojciech", "Kraśnik", "Pozwany", None, 7, 1657, "Albertum Batusik", "Pozwany o niewykonanie roboty kołodziejskiej")

# Skan 8 (1657)
add_occ("Skwarek", "Walenty", "Kraśnik", "Powód", "Skwarek [?]", 8, 1657, "Skwarek", "Dekret nakazujący oddanie roboty lub pieniędzy")
add_occ("Batusik", "Wojciech", "Kraśnik", "Pozwany", None, 8, 1657, "Batusik", "Dekret w sprawie kołodziejskiej")
add_occ("Babińczyk", "Benedykt", "Kraśnik", "Żyd / Składający przysięgę", "Babińczyk [?]", 8, 1657, "Judaeo Benedicto Babińczyk [?]", "Dopuszczony do przysięgi sądowej")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły", None, 8, 1657, "Blasii Kołodziejczyk", "Świadectwo S. Dąbrowicza")
add_occ("Dąbrowicz", "Sebastian", "Bielice", "Pracowity / Świadek", "Dąbrowicz [?]", 8, 1657, "Sebastianus Dąbrowicz [?] de Bielice [?]", "Zeznanie dla B. Kołodziejczyka")
add_occ("Bendralik", "Stanisław", "Kraśnik", "Wzmiankowany", None, 8, 1657, "Stanisław Bendralik", "Wymieniony w zeznaniu S. Dąbrowicza")
add_occ("Marlik", "Andrzej", "Kraśnik", "Powód", "Marlik [?]", 8, 1657, "Andream Marlik [?]", "Proces przeciw Mielchikowi")
add_occ("Łycek", "Paweł", "Kraśnik", "Powód", None, 8, 1657, "Pauli Łycek", "Świadectwo brata Mikołaja Łycka o obligu")
add_occ("Łycek", "Mikołaj", "Kraśnik", "Brat Pawła Łycka / Świadek", None, 8, 1657, "Mikołaj Łycek", "Zeznanie o pożyczce brata")

# Skan 9 (1657)
add_occ("Łycek", "Paweł", "Kraśnik", "Powód", None, 9, 1657, "Paulum Łycek", "Spór z wdową A. Łyckową o opiekę")
add_occ("Łyckowa", "Anna", "Kraśnik", "Wdowa / Pozwana", None, 9, 1657, "Annam Łyckowa", "Dylacja w sporze z P. Łyckiem")
add_occ("Pisak", "Mikołaj", "Kraśnik", "Poszkodowany (obdukcja)", "Rusek [?]", 9, 1657, "Nicolai Pisak [?] alias Rusek [?]", "Obdukcja ran krwawych na skroniach i boku")
add_occ("Kurowic", "Augustyn", "Kraśnik", "Ławnik przysięgły kraśnicki", None, 9, 1657, "Augustynem Kurowicem", "Przeprowadzenie obdukcji ran M. Pisaka")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły kraśnicki", None, 9, 1657, "Grzegorzem Foxem", "Przeprowadzenie obdukcji ran M. Pisaka")
add_occ("Rogalowski", "Jakub", "Kraśnik", "Właściciel domu", "Rogalowski [?]", 9, 1657, "Jakuba Rogalowskiego [?]", "Dom obdukcji ran M. Pisaka")
add_occ("Lech", "Jan", "Kraśnik", "Właściciel domu", None, 9, 1657, "Jana Lecha", "Miejsce pijatyki i pobicia M. Pisaka")
add_occ("Trela", "Stanisław", "Kraśnik", "Powód", None, 9, 1657, "Stanislaum Trela", "Proces przeciw A. Łapczyńskiej o 6 fl 20 gr")
add_occ("Łapczyńska", "Anna", "Kraśnik", "Pozwana dłużniczka", "Łapczyńska [?]", 9, 1657, "Annam Łapczyńska [?]", "Nakaz zapłaty 6 fl 20 gr S. Treli")

# Skan 10 (1657)
add_occ("Trela", "Stanisław", "Kraśnik", "Powód", None, 10, 1657, "Trela", "Rozliczenie 6 fl 20 gr")
add_occ("Łycek", "Paweł", "Kraśnik", "Powód", None, 10, 1657, "Paulum Łycek", "Nakaz przysięgi na 30 fl przeciw wdowie A. Łyckowej")
add_occ("Łyckowa", "Anna", "Kraśnik", "Wdowa / Pozwana", None, 10, 1657, "Annam Viduam Łyckowa", "Spór o 30 fl i 11 lat opieki")
add_occ("Żyłówka", "Anna", "Kraśnik", "Wdowa / Powódka", "Żyłówka [?]", 10, 1657, "Viduam Annam Żyłówka [?]", "Proces przeciw W. Kulce o 7 fl od kotliny")
add_occ("Kulka", "Wojciech", "Kraśnik", "Pozwany", None, 10, 1657, "Albertum Kulka", "Nakaz zapłaty 7 fl")
add_occ("Mazur", "Wojciech", "Kraśnik", "Pozwany", None, 10, 1657, "Albertum Mazur", "Proces o 2 fl na rzecz kościoła i miasta")
add_occ("Sienka", "Jan", "Kraśnik", "Pozwany", "Sienka [?]", 10, 1657, "Joannem Sienka [?]", "Współpozwany o 2 fl")

# Skan 11 (1657)
add_occ("Mazur", "Wojciech", "Kraśnik", "Pozwany", None, 11, 1657, "Mazur", "Dekret w sprawie 2 fl")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Mieszczanin i szewc / Świadek", None, 11, 1657, "Albertus Olęcki Civis et Sutor", "Zeznanie o bójce W. Sydkowica w Łęcznej")
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Strona procesów", None, 11, 1657, "Laurentii Sydkowic", "Procesy z Sz. Jasielskim i A. Laskiem (25 fl 6 gr)")
add_occ("Koniarska", "Mieszkanka", "Kraśnik", "Powódka", "Koniarska [?]", 11, 1657, "Koniarska [?]", "Spór z Z. Jasińską o 1 fl 15 gr i 5 fl")
add_occ("Jasińska", "Zuzanna", "Kraśnik", "Pozwana", "Jasińska [?]", 11, 1657, "Zuzannam Jasińska [?]", "Nakaz zapłaty długu")
add_occ("Jasielski", "Szymon", "Kraśnik", "Pozwany", None, 11, 1657, "Simonem Jasielski", "Dylacja na świadków")
add_occ("Lasek", "Augustyn", "Kraśnik", "Pozwany", "Łycek [?]", 11, 1657, "Augustinum Lasek [Łycek?]", "Spór o 25 fl 6 gr z zapisu")

# Skan 12 (1657)
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik / Świadek", None, 12, 1657, "Maciej Konięga", "Świadectwo w sprawie z Łęcznej")
add_occ("Koniarska", "Mieszkanka", "Kraśnik", "Powódka", "Koniarska [?]", 12, 1657, "Koniarska", "Odesłanie na Brzeg Krakowski")
add_occ("Kuśnierz", "Barbara", "Kraśnik", "Powódka", "Kuśnierz [?]", 12, 1657, "Barbaram Kuśnierz [?]", "Proces przeciw Kudle o 43 złp zapisane na gruncie")
add_occ("Kudła", "Mieszkanka", "Kraśnik", "Pozwana", "Kudła [?]", 12, 1657, "Kudła [?]", "Nakaz zapłaty 43 złp lub puszczenia gruntu")

# Skan 13 (1657)
add_occ("Trela", "Stanisław", "Kraśnik", "Powód", None, 13, 1657, "Stanislaum Trela", "Nakaz zapłaty 6 fl 20 gr dla powoda")
add_occ("Łapczyńska", "Anna", "Kraśnik", "Pozwana", "Łapczyńska [?]", 13, 1657, "Annam Łapczyńska", "Dekret z 4 XII 1657 r.")
add_occ("Domiłek", "Andrzej", "Kraśnik", "Powód", "Domiłek [?]", 13, 1657, "Andream Domiłek [?]", "Proces przeciw Z. Zielińskiej o dług z rejestru")
add_occ("Zielińska", "Zofia", "Kraśnik", "Pozwana", "Zielińska [?]", 13, 1657, "Sophiam Zielińska [?]", "Nakaz zapłaty długu z rejestru")
add_occ("Błażejowska", "Szlachcianka", "Kraśnik", "Powódka", "Błażejowska [?]", 13, 1657, "Nobilem Błażejowska [?]", "Spór z Żyłówką na Brzegu Krakowskim")
add_occ("Szafraniec", "Adam", "Kraśnik", "Powód", "Szafraniec [?]", 13, 1657, "Adamum Szafraniec [?]", "Spór ze Świniarką")
add_occ("Świniarka", "Mieszkanka", "Kraśnik", "Pozwana", "Świniarka [?]", 13, 1657, "Świniarka [?]", "Dylacja w procesie z A. Szafrańcem")

# Skan 14 (1657)
add_occ("Buła", "Jan", "Kraśnik", "Powód", "Buła [?]", 14, 1657, "Joannem Buła [?]", "Spór z W. Oleskiem o 8 fl za krowę")
add_occ("Olesek", "Walenty", "Kraśnik", "Pozwany", "Olesek [?]", 14, 1657, "Valentinum Olesek [?]", "Spór o zapłatę za krowę")
add_occ("Kosek", "Stanisław", "Kraśnik", "Świadek", None, 14, 1657, "Stanisław Kosek", "Świadectwo w sprawie krowy")
add_occ("Jajczykówna", "Zuzanna", "Kraśnik", "Składająca przysięgę", "Jajczykówna [?]", 14, 1657, "Zuzannae Jajczykówna [?]", "Przysięga o krowie")
add_occ("Śliżanka", "Katarzyna", "Kraśnik", "Świadek", "Śliżanka [?]", 14, 1657, "Katarzyna Śliżanka [?]", "Zeznanie przy W. Sitarskim")
add_occ("Sitarski", "Walenty", "Kraśnik", "Świadek", None, 14, 1657, "Walentym Sitarskim", "Obecny przy zeznaniu")
add_occ("Kurowic", "Augustyn", "Kraśnik", "Ławnik przysięgły / Aktor", None, 14, 1657, "Augustini Kurowic", "Proces przeciw Koniarskiej o 23 fl i 11 fl")
add_occ("Paździech", "Augustyn", "Kraśnik", "Świadek", "Paździech [?]", 14, 1657, "Augustinus Paździech [?]", "Zeznanie dla A. Kurowica")
add_occ("Batusik", "Jan", "Kraśnik", "Powód", None, 14, 1657, "Joannem Batusik", "Spór z G. Łapką o dwie kopy żyta")
add_occ("Łapka", "Grzegorz", "Kraśnik", "Pozwany", "Rzepka [?]", 14, 1657, "Gregorium Łapka [Rzepka?]", "Nakaz oddania dwóch kop żyta")

# Skan 15 (1657)
add_occ("Kurowic", "Augustyn", "Kraśnik", "Ławnik przysięgły / Aktor", None, 15, 1657, "Augustinum Kurowic", "Proces przeciw wdowie Boguckiej oraz relacja dla W. Butka")
add_occ("Bogucka", "Wdowa", "Kraśnik", "Wdowa / Pozwana", "Bugajowa [?]", 15, 1657, "Viduam Bogucka [Bugajowa?]", "Spór o zagon roli")
add_occ("Sulski", "Szlachcic", "Kraśnik", "Powód", "Sulski [?]", 15, 1657, "Nobilem Sulski [?]", "Spór z W. Butkiem")
add_occ("Butek", "Wojciech", "Kraśnik", "Pozwany / Strona", "Butek [?]", 15, 1657, "Albertum Butka [?]", "Sprawa o sumy 45 fl i 55 fl")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły", None, 15, 1657, "Grzegorzem Foxem", "Relacja ławników w sprawie W. Butka")
add_occ("Dolski", "Marcin", "Kraśnik", "Szwagier / Świadek", None, 15, 1657, "Marcin Dolski", "Zeznanie o sumach 45 fl i 55 fl W. Butka")

# Skan 16 (1656)
add_occ("Stochański", "Mieszkaniec", "Kraśnik", "Powód", "Stochański [?]", 16, 1656, "Stochański [?]", "Spór z G. Zielińskim o 15 gr")
add_occ("Zieliński", "Grzegorz", "Kraśnik", "Pozwany", None, 16, 1656, "Gregorium Zieliński", "Spór o 15 gr")
add_occ("Kotlarek", "Jan", "Kraśnik", "Powód", None, 16, 1656, "Joannem Kotlarka", "Spór o dobra po Bochanie i Szpakowskim")
add_occ("Kotlarek", "Andrzej", "Kraśnik", "Współpowód", None, 16, 1656, "Andream Kotlarka", "Spór o dobra po Bochanie i Szpakowskim")
add_occ("Kotlarka", "Jadwiga", "Kraśnik", "Współpowódka", None, 16, 1656, "Hedvigim Kotlarka", "Spór o dobra po Bochanie i Szpakowskim")
add_occ("Kurowic", "Augustyn", "Kraśnik", "Opiekun Kotlarków", None, 16, 1656, "Augustini Kurowic", "Opiekun w procesie z Konińskim (9 XII 1656)")
add_occ("Koniński", "Mieszkaniec", "Kraśnik", "Pozwany", "Komiński [?]", 16, 1656, "Koniński [Komiński?]", "Pozwany o dział dóbr po Bochanie")
add_occ("Konińska", "Elżbieta", "Kraśnik", "Żona Konińskiego / Pozwana", "Komińska [?]", 16, 1656, "Elisabetham", "Współpozwana z mężem")
add_occ("Madejski", "Stanisław", "Kraśnik", "Powód", "Madeick [?]", 16, 1656, "Stanislaus Madejski [Madeick?]", "Pozew przeciw W. Rzepce (13 XII 1656)")
add_occ("Rzepka", "Wawrzyniec", "Kraśnik", "Pozwany", None, 16, 1656, "Laurentium Rzepka", "Pozwany przez S. Madejskiego")
add_occ("Rogalka", "Jakub", "Kraśnik", "Woźny przysięgły sądu wójtowskiego", "Rogala [?]", 16, 1656, "Jacobus Rogalka Bedellus", "Relacja z pozwu (13 XII 1656)")

# Skan 17 (1656)
add_occ("Morawek", "Augustyn", "Rudki", "Poddany / Opiekun i powód", "Morawek [?]", 17, 1656, "Augustinum Morawek [?]", "Spór z W. Łysakiem o 54 fl za żyto (15 XII 1656)")
add_occ("Łysak", "Wojciech", "Kraśnik", "Pozwany", "Łysak [?]", 17, 1656, "Albertum Łysak [?]", "Pozwany o 54 fl za żyto")
add_occ("Młodnicka", "Maryna", "Kraśnik", "Wdowa / Protestująca", None, 17, 1656, "Maria Młodnicka vidua", "Protestacja przeciw ślusarzowi A. Pieniążkowi")
add_occ("Pieniążek", "Andrzej", "Kraśnik", "Ślusarz / Pozwany", None, 17, 1656, "Andream Pieniążek senfabrum", "Przedmiot protestacji M. Młodnickiej")
add_occ("Cwik", "Andrzej", "Kraśnik", "Powód", "Cwik [?]", 17, 1656, "Andream Cwik [?]", "Proces przeciw W. Łyckowi o 60 fl")
add_occ("Łycek", "Wojciech", "Kraśnik", "Pozwany", "Łycek [?]", 17, 1656, "Albertum Łycek [?]", "Nakaz zapłaty 60 fl")
add_occ("Starzyński", "Marcin", "Kraśnik", "Ławnik przysięgły", None, 17, 1656, "Martino Starzyński", "Obecny na sesji 18 XII 1656")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły", None, 17, 1656, "Blasio Kołodziejczyk", "Obecny na sesji 18 XII 1656")

# Skan 18 (1656)
add_occ("Espen", "Jerzy", "Lublin", "Sługa J. Deserta / Protestujący", "Espen [?]", 18, 1656, "Georgius Espen [?]", "Protestacja przeciw rajcy M. Sitarskiemu o pobicie (18 XII 1656)")
add_occ("Desert", "Jakub", "Lublin", "Mieszczanin lubelski / Pracodawca", None, 18, 1656, "Jacobi Deserti Civis Lublinensis", "Pracodawca pobitego Jerzego Espena")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca kraśnicki / Pozwany", None, 18, 1656, "Martinum Sitarski Consulem", "Oskarżony o pobicie J. Espena za rozmowę po niemiecku")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 18, 1656, "Stanisława Nawrockiego Rajcy", "Właściciel domu, gdzie doszło do incydentu")
add_occ("Starzyński", "Marcin", "Kraśnik", "Ławnik przysięgły", None, 18, 1656, "Marcin Starzyński", "Obdukcja ran Jerzego Espena")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik przysięgły", None, 18, 1656, "Błażej Kołodziejczyk", "Obdukcja ran Jerzego Espena")

# Skan 19 (1657)
add_occ("Kulka", "Jan", "Kraśnik", "Opiekun dóbr Jajczyków / Powód", None, 19, 1657, "Joannem Kulka", "Proces i areszt przeciw T. Larkowskiemu")
add_occ("Jajczyk", "Szymon", "Kraśnik", "Opiekun dóbr Jajczyków / Powód", None, 19, 1657, "Simonem Jajczyk", "Proces i areszt przeciw T. Larkowskiemu")
add_occ("Jajczyk", "Paweł", "Kraśnik", "Zmarły spadkodawca", None, 19, 1657, "Pauli Jajczyk", "Zmarły ojciec podopiecznych")
add_occ("Larkowski", "Tomasz", "Kraśnik", "Pozwany", None, 19, 1657, "Thomam Larkowski", "Areszt na dobrach po J. Jajczyku w jego domu")
add_occ("Tokarzyk", "Wojciech", "Kraśnik", "Powód", "Tokarzyk [?]", 19, 1657, "Albertum Tokarzyk [?]", "Spór z T. Larkowskim")
add_occ("Tatarczuk", "Jan", "Kraśnik", "Szewc / Aresztujący", None, 19, 1657, "Joannes Tatarczuk Sutor", "Areszt na osobie Szymona")

# Skan 20 (1657)
add_occ("Pieniążek", "Andrzej", "Kraśnik", "Ślusarz / Dłużnik", None, 20, 1657, "Andrzej Pieniążek", "Zeznanie długu 4 fl")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Powód", None, 20, 1657, "Albertum Olęcki", "Spór z P. Tarnowczykiem o 1 fl 15 gr i 3 fl 15 gr")
add_occ("Tarnowczyk", "Paweł", "Kraśnik", "Pozwany", "Tarnowczyk [?]", 20, 1657, "Paulum Tarnowczyk [?]", "Nakaz zapłaty za robotę")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik / Aktor", None, 20, 1657, "Mathiam Konięga", "Skarga na J. Skurę o najście domu")
add_occ("Skura", "Jan", "Kraśnik", "Pozwany", "Skóra [?]", 20, 1657, "Joannem Skura [Skóra?]", "Pozwany o najście domu M. Konięgi")
add_occ("Bybina", "Wdowa", "Kraśnik", "Wdowa / Pozwana", "Bybina [?]", 20, 1657, "Viduam Bybina [?]", "Spór o 12 gr za beczkę i koło")
add_occ("Gabriel", "Paweł", "Kraśnik", "Wzmiankowany", None, 20, 1657, "Pawła Gabriela", "Dostawca beczki i koła")

# Skan 21 (1657)
add_occ("Jajczyk", "Sebastian", "Kraśnik", "Pozwany", None, 21, 1657, "Sebestianum Jajczyk", "Dylacja w procesie z Zielińskim")
add_occ("Zalasek", "Krzysztof", "Kraśnik", "Pozwany", "Zaleski [?]", 21, 1657, "Christophorum Zalasek [Zaleski?]", "Spór o 15 fl z 1653 r.")
add_occ("Cuda", "Andrzej", "Kraśnik", "Pozwany", "Ruda [?]", 21, 1657, "Andream Cuda [Ruda?]", "Współpozwany o 15 fl")
add_occ("Konięga", "Maciej", "Kraśnik", "Poręczyciel", None, 21, 1657, "Maciej Konięga", "Poręczenie za dług z 1653 r.")
add_occ("Jasielski", "Szymon", "Kraśnik", "Strona", None, 21, 1657, "Simonis Jasielski", "Świadectwa o bójce u P. Paździechy")
add_occ("Brzostek", "Michał", "Kraśnik", "Świadek", "Brzostek [?]", 21, 1657, "Michael Brzostek [?]", "Zeznanie o bójce Jasielskiego z Sydkowicem")
add_occ("Kapica", "Adam", "Kraśnik", "Świadek", None, 21, 1657, "Adam Kapica", "Drugi zaprzysiężony świadek bójki")
add_occ("Paździech", "Augustyn", "Kraśnik", "Właściciel domu", "Paździech [?]", 21, 1657, "P. Paździechy [?]", "Dom, w którym doszło do kłótni")

# Skan 22 (1657)
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Strona", None, 22, 1657, "Laurentii Sydkowic", "Skarga przeciw Sz. Jasielskiemu o pobicie")
add_occ("Jasielski", "Szymon", "Kraśnik", "Strona", None, 22, 1657, "Simonem Jasielski", "Reprotestacja o obronie własnej")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik / Aktor", None, 22, 1657, "Blasium Kołodziejczyk", "Spór z M. Siedleckim o skórę butową")
add_occ("Siedlecki", "Marcin", "Kraśnik", "Pozwany", "Sieradzki [?]", 22, 1657, "Martinum Siedlecki [Sieradzki?]", "Nakaz zwrotu lub zapłaty skóry")
add_occ("Szafraniec", "Adam", "Kraśnik", "Powód", None, 22, 1657, "Adamum Szafraniec", "Spór z M. Rzepką o 5 fl za Józefa")
add_occ("Rzepka", "Maciej", "Kraśnik", "Pozwany", "Rzepka [?]", 22, 1657, "Mathiam Rzepka [?]", "Nakaz zapłaty 5 fl")
add_occ("Łycek", "Jan", "Kraśnik", "Powód", None, 22, 1657, "Joannem Łycek", "Spór z G. Kupką o 10 fl i żyto")
add_occ("Kupka", "Grzegorz", "Kraśnik", "Pozwany", "Rzepka [?]", 22, 1657, "Gregorium Kupka [Rzepka?]", "Nakaz rozliczenia długu")

# Skan 23 (1657)
add_occ("Łycek", "Jan", "Kraśnik", "Powód", None, 23, 1657, "Łycek", "Dokończenie dekretu")
add_occ("Delik", "Jan", "Kraśnik", "Powód", None, 23, 1657, "Joannem Delik", "Spór o żyto po 6 gr i 9 fl")
add_occ("Satomski", "Mieszkaniec", "Kraśnik", "Pozwany", "Słomkowski [?]", 23, 1657, "Dnum Satomski [Słomkowski?]", "Odesłanie sprawy do dalszego terminu")
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Powód", None, 23, 1657, "Laurentii Sydkowic", "Zeznania świadków przeciw Sz. Jasielskiemu")
add_occ("Rogalowski", "Wojciech", "Kraśnik", "Świadek", "Rogalowski [?]", 23, 1657, "Albertus Rogalowski [?]", "Zeznanie o wyzwiskach rzucanych przez Jasielskiego")
add_occ("Rzepka", "Maciej", "Kraśnik", "Świadek", "Rzepka [?]", 23, 1657, "Mathias Rzepka [?]", "Drugi świadek przeciw Sz. Jasielskiemu")

# Skan 24 (1657)
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Powód", None, 24, 1657, "Laurentium Sydkowic", "Dopuszczenie do przysięgi z sześcioma świadkami")
add_occ("Jasielski", "Szymon", "Kraśnik", "Pozwany", None, 24, 1657, "Simonem Jasielski", "Proces o zniewagę słowną")
add_occ("Zieliński", "Józef", "Kraśnik", "Pozwany", "Zieliński [?]", 24, 1657, "Josephum Zieliński [?]", "Spór z wójtem o konia kupionego za 12 fl od Bujaka")
add_occ("Bujak", "Sprzedawca", "Kraśnik", "Sprzedawca konia", "Bujak [?]", 24, 1657, "Bujaka [?]", "Sprzedawca konia na jarmarku")

# Skan 25 (1657)
add_occ("Zieliński", "Józef", "Kraśnik", "Pozwany", "Zieliński [?]", 25, 1657, "Josephum Zieliński", "Nakaz dopłaty 2 fl 15 gr oraz sprawa z A. Marlikiem")
add_occ("Łyszkowa", "Zofia", "Kraśnik", "Wdowa / Manifestująca", "Łyszkowa [?]", 25, 1657, "Viduae Łyszkowa [?]", "Manifestacja przed Sz. Jasielskim przeciw P. Łyckowi")
add_occ("Łycek", "Paweł", "Kraśnik", "Pozwany", None, 25, 1657, "Paulum Łycek", "Przedmiot manifestacji wdowy Łyszkowej")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik / Aktor", None, 25, 1657, "Mathiam Konięga", "Proces przeciw J. Kępie o 2 fl za najem izby")
add_occ("Kępa", "Jan", "Kraśnik", "Pozwany", "Kępa [?]", 25, 1657, "Joannem Kępa [?]", "Nakaz zapłaty 2 fl czynszu")
add_occ("Marlik", "Andrzej", "Kraśnik", "Powód", "Marlik [?]", 25, 1657, "Andream Marlik [?]", "Spór z J. i A. Zielińskimi")
add_occ("Zielińska", "Anna", "Kraśnik", "Żona Józefa / Pozwana", None, 25, 1657, "Annam Zielińska", "Współpozwana z mężem")

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part1.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

csv_path = '/home/ubuntu/workspace/Gen/krasnik_j20_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Lp.', 'Nazwisko', 'Imie', 'Miejsce zamieszkania', 'Funkcja spoleczna', 'Warianty nazwiska', 'Numery skanow', 'Zakres lat', 'Liczba wystapien'])
    for p in gen_data:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p['funkcja'],
            p.get('wariant_nazwiska') or '',
            p['skany_roboczo'],
            p['zakres_lat'],
            p['liczba_wystapien']
        ])

print(f"Zapisano gen_data_j20_part1.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
