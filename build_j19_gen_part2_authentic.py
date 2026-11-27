# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part1.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

profile_map = {(p['nazwisko'], p['imie'], p['miejsce']): p for p in gen_data}

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
        new_lp = max(x['lp'] for x in gen_data) + 1
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
            "notatka_biograficzna": f"Osoba odnotowana w księdze radzieckiej Kraśnika (Jednostka 19, skan #{skan}, {rok} r.)."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# Skan 26 (1657)
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca kraśnicki / Nabywca", None, 26, 1657, "Stanisława Nawrockiego", "Kupno gruntu przy drodze do Ladańska od R. Butowej za 120 złp")
add_occ("Nawrocka", "Jadwiga", "Kraśnik", "Żona rajcy Stanisława Nawrockiego", "Kupska [?]", 26, 1657, "Jadwigi", "Współnabywczyni gruntu")
add_occ("Nawrocki", "Wojciech", "Kraśnik", "Syn Stanisława i Jadwigi Nawrockich", None, 26, 1657, "Wojciecha", "Wymieniony w kontrakcie rodziców")
add_occ("Butowa", "Regina", "Kraśnik", "Wdowa po Gabrielu Bucie / Zbywczyni", "Gabrielowa Bucina", 26, 1657, "Reginą Buciną wdową", "Sprzedaż gruntu S. Nawrockiemu za 120 złp")
add_occ("Tłaczyński", "Piotr", "Kraśnik", "Brat Reginy Butowej / Asystent", "Tłaczyński [?]", 26, 1657, "Piotra Tłaczyńskiego [?]", "Asystent siostry przy sprzedaży")
add_occ("Sikor", "Stanisław", "Kraśnik", "Pisarz przysięgły i opiekun", None, 26, 1657, "Stanisława Sikora Pisarza", "Opiekun Reginy Butowej")

# Skan 27 (1657)
add_occ("Butowa", "Regina", "Kraśnik", "Wdowa / Zbywczyni", None, 27, 1657, "Reginą Buciną", "Sprzedaż placu przy ul. Lubelskiej W. Zętkowicowi za 42 złp")
add_occ("Zętkowic", "Wawrzyniec", "Kraśnik", "Mieszczanin kraśnicki / Nabywca", "Żętkowic [?]", 27, 1657, "Wawrzyńcem Zętkowicem [Żętkowicem?]", "Zakup placu przy ul. Lubelskiej za 42 złp")
add_occ("Zętkowicowa", "Katarzyna", "Kraśnik", "Żona Wawrzyńca Zętkowica", "Żętkowicowa [?]", 27, 1657, "Katarzyną", "Współnabywczyni placu")
add_occ("Grzymuszka", "Jan", "Kraśnik", "Sąsiad placu przy ul. Lubelskiej", None, 27, 1657, "Jana Grzymuszki", "Sąsiad sprzedanego placu")

# Skan 28 (1657)
add_occ("Zętkowic", "Wawrzyniec", "Kraśnik", "Dłużnik", "Żętkowic [?]", 28, 1657, "Laurentius Zętkowic", "Oblig na 10 złp dla Reginy Butowej")
add_occ("Tharasa", "Maciej", "Kraśnik", "Burmistrz / Strona ugody", None, 28, 1657, "Mathiam Tharasa", "Ugoda przyjacielska z Sz. Szczygłem")
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca / Strona ugody", None, 28, 1657, "Martinum Sitarski", "Ugoda przyjacielska z Sz. Szczygłem")
add_occ("Szczygieł", "Szymon", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona ugody", "Sczygieł", 28, 1657, "Simonem Sczygieł", "Ugoda z rajcami Tharasą i Sitarskim")

# Skan 29 (1657)
add_occ("Szczygłowa", "Zofia", "Przedmieście Kraśnickie", "Żona Szymona Szczygła", None, 29, 1657, "Zofią", "Współuczestniczka ugody")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Rajca / Rozjemca", None, 29, 1657, "Stanisław Nawrocki Rajca", "Przyjaciel-rozjemca w ugodzie Szczygła")
add_occ("Dorada", "Jan", "Kraśnik", "Rozjemca", "Dorada [?]", 29, 1657, "Jan Dorada [?]", "Przyjaciel-rozjemca w ugodzie Szczygła")
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", "Rozjemca", None, 29, 1657, "Paweł Kłopot", "Przyjaciel-rozjemca w ugodzie Szczygła")

# Skan 30 (1657)
add_occ("Tharasa", "Maciej", "Kraśnik", "Ustępujący prokonsul", None, 30, 1657, "Mathia Tharasa", "Przekazał urząd prokonsula U. Janaszkowicowi")
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Nowy prokonsul kraśnicki", None, 30, 1657, "Ubaldum Janaszkowic", "Objął urząd prokonsula w październiku 1657 r.")

# Skan 31 (1657)
add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca / Aktor", None, 31, 1657, "Martini Sitarski Consulis", "Wyrok o 20 złp przeciw P. Niedbałce")
add_occ("Niedbałka", "Paweł", "Kraśnik", "Pozwany / Dłużnik", None, 31, 1657, "Paulum Niedbałka", "Nakaz zapłaty 20 złp")
add_occ("Kapica", "Adam", "Kraśnik", "Gorzałcznik (crematarius)", "Kapicha [?]", 31, 1657, "Adamus Kapicha [Kapica?]", "Kwitacja Reginy Butowej ze spadku po G. Bucie")
add_occ("Barkowic", "Maciej", "Przedmieście Kraśnickie", "Przedmieszczanin / Zbywca", "Barkowic [?]", 31, 1657, "Mathias Barkowic [?]", "Cesja gruntu na rzecz S. Skroda z Rzeczycy")
add_occ("Skród", "Stanisław", "Rzeczyca", "Pracowity ze wsi Rzeczycy / Nabywca", "Skrod [?]", 31, 1657, "Stanislao Skrod [?] de Villa Rzeczyca", "Nabywca gruntu od M. Barkowica")

# Skan 32 (1657)
add_occ("Janaszkowic", "Ubald", "Kraśnik", "Burmistrz / Sąsiad na Podlesiu", None, 32, 1657, "Ubalda Janaszkowica Burmistrza", "Sąsiad gruntu na Podlesiu")
add_occ("Kłopot", "Paweł", "Przedmieście Kraśnickie", "Sąsiad na Podlesiu", None, 32, 1657, "Pawła Kłopota", "Sąsiad gruntu na Podlesiu")
add_occ("Pieniążek", "Andrzej", "Kraśnik", "Kowal / Aktor", None, 32, 1657, "Andreae Pieniążek", "Spór z P. Różyckim o plac w Rynku")
add_occ("Różycki", "Paweł", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", None, 32, 1657, "Paulum Różycki", "Pozwany o plac w Rynku po Zofii Dzierżkowej")
add_occ("Dzierżkowa", "Zofia", "Kraśnik", "Poprzednia właścicielka placu (200 złp)", None, 32, 1657, "Zofii Dzierżkowej", "Sprzedała plac w Rynku P. Różyckiemu za 200 złp")

# Skan 33 (1657)
add_occ("Różycki", "Paweł", "Kraśnik", "Aktor", None, 33, 1657, "Paweł Różycki", "Wyrok przeciw A. Pieniążkowi o 30 złp i 80 złp")

# Skan 34 (1657)
add_occ("Kapica", "Adam", "Kraśnik", "Gorzałcznik (crematarius)", None, 34, 1657, "Adamus Kapica Crematarius", "Przyjęcie prawa miejskiego magdeburskiego (Jus Civile)")
add_occ("Kłopot", "Gabriel", "Przedmieście Kraśnickie", "Aktor", "Kłopotek", 34, 1657, "Gabrielis Kłopotek", "Wyrok przeciw G. Niedbałce o 10 złp")
add_occ("Niedbałka", "Grzegorz", "Kraśnik", "Pozwany", None, 34, 1657, "Gregorium Niedbałka", "Nakaz zapłaty 10 złp")
add_occ("Dzierżek", "Maciej", "Kraśnik", "Zmarły (sieroty)", "Dzierżek [?]", 34, 1657, "Mathiae Dzierżek [?]", "Spór opiekuna M. Sitarskiego o 50 złp")
add_occ("Łopata", "Wojciech", "Kraśnik", "Opiekun / Pozwany", "Łopata [?]", 34, 1657, "Alberti Łopata [?]", "Pozwany o dług 50 złp")

# Skan 35 (1657)
add_occ("Karwaczek", "Jędrzej", "Stojeszyn", "Pracowity ze wsi Stojeszyn / Aktor", None, 35, 1657, "Andreae Karwaczek de Stojeszyn", "Proces przeciw S. Cwikowi o porwanie klaczy")
add_occ("Cwik", "Stanisław", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 35, 1657, "Stanislaum Cwik", "Oskarżony o zabranie klaczy na szkodzie")
add_occ("Błaszczyk", "Stanisław", "Stojeszyn", "Pracowity ze Stojeszyna / Świadek", None, 35, 1657, "Stanisława Błaszczyka", "Świadek J. Karwaczka o klaczy")
add_occ("Bucha", "Wincenty", "Stojeszyn", "Pracowity ze Stojeszyna / Świadek", None, 35, 1657, "Wincentego Buchę", "Świadek J. Karwaczka o klaczy")
add_occ("Fortuna", "Mikołaj", "Kraśnik", "Obecny przy oględzinach klaczy", None, 35, 1657, "Mikołaja Fortuny", "Wzmiankowany w sprawie klaczy")

# Skan 36 (1657)
add_occ("Zarzyka", "Sebastian", "Kraśnik", "Świadek", None, 36, 1657, "Sebastian Zarzyka", "Świadek w sprawie klaczy J. Karwaczka")
add_occ("Kowalik", "Szymon", "Przedmieście Kraśnickie", "Instygator świadków", None, 36, 1657, "Simonis Kowalik", "Świadek w jego sprawie o spadek Pezików")
add_occ("Sobol", "Józef", "Przedmieście Kraśnickie", "Świadek", None, 36, 1657, "Joseph Sobol", "Świadek o sierocie Zofii Pezikównie")
add_occ("Pezik", "Wawrzyniec", "Przedmieście Kraśnickie", "Zmarły ojciec Zofii Pezikówny", None, 36, 1657, "Wawrzyniec Pezik", "Zmarły brat Sebastiana Pezika")
add_occ("Pezik", "Sebastian", "Przedmieście Kraśnickie", "Zmarły stryj Zofii Pezikówny", None, 36, 1657, "Sebastiana Pezika", "Wzmiankowany w genealogii Pezików")
add_occ("Kowalikowa", "Zofia", "Przedmieście Kraśnickie", "Córka Wawrzyńca Pezika, żona Sz. Kowalika", "Pezikówna", 36, 1657, "Zofią Pezikównę", "Spadkobierczyni po Pezikach")
add_occ("Batusik", "Sebastian", "Przedmieście Kraśnickie", "Zmarły opiekun Zofii Pezikówny", "Batuś", 36, 1657, "Sebastian Batusik", "Były opiekun sierot Pezików")
add_occ("Zdebik", "Michał", "Przedmieście Kraśnickie", "Opiekun sierot Pezików", None, 36, 1657, "Michał Zdebik", "Były opiekun sierot Pezików")
add_occ("Giża", "Maciej", "Przedmieście Kraśnickie", "Opiekun sierot Pezików", None, 36, 1657, "Maciej Giza", "Były opiekun sierot Pezików")
add_occ("Bednarz", "Paweł", "Kraśnik", "Dłużnik", None, 36, 1657, "Pawłowi Bednarzowi", "Odbiorca pieniędzy sierocych na procent")
add_occ("Stolarz", "Szymon", "Kraśnik", "Zbywca domu", None, 36, 1657, "Szymon Stolarz", "Sprzedał dom Pawłowi Bednarzowi")

# Skan 37 (1657)
add_occ("Dzek", "Szymon", "Kraśnik", "Kowal (serri faber) / Świadek", "Dzik [?]", 37, 1657, "Simon Dzek [Dzik?] Serri faber", "Świadek Sz. Kowalika o długu P. Bednarza")
add_occ("Dzek", "Jakub", "Kraśnik", "Brat Szymona Dzeka / Dłużnik", "Dzik [?]", 37, 1657, "Jakubowi Dzekowi [Dzikowi?]", "Odbiorca 20 złp z długu Bednarza")
add_occ("Batusik", "Jan", "Przedmieście Kraśnickie", "Brat i sukcesor S. Batusika / Pozwany", None, 37, 1657, "Joannem Batusik", "Pozwany przez Sz. Kowalika i Z. Pezikównę")

# Skan 38 (1658)
add_occ("Rzepka", "Jan", "Kraśnik", "Zmarły właściciel domu Rzepczyńskiego", None, 38, 1658, "Jan Rzepka", "Nabywca domu Rzepczyńskiego")
add_occ("Zamoyski", "Jan", "Zamość", "Podczaszy koronny, dziedzic Kraśnika", None, 38, 1658, "Joannis de Zamoście Zamoyski", "Z jego ramienia elekcja 1658 r.")
add_occ("Brzostowski", "Krzysztof", "Zamość", "Podczaszy czernihowski, komisarz ordynacki", "Brzozowski [?]", 38, 1658, "Christophorus Brzostowski [Brzozowski?]", "Komisarz elekcji magistratu 1658 r.")
add_occ("Borkowski", "Stanisław", "Zamość", "Komisarz ordynacki", None, 38, 1658, "Stanislao Borkowski Commissario", "Komisarz elekcji magistratu 1658 r.")
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Wójt i sędzia ordynaryjny (1658)", "Albertus Szafraniec", 38, 1658, "Albertum Szafraniec", "Wybrany wójtem w elekcji 1658 r.")

# Skan 39 (1658)
add_occ("Skarzyński", "Marcin", "Kraśnik", "Ławnik kraśnicki (1658)", None, 39, 1658, "Martinus Skarzyński", "Ławnik w elekcji 1658 r.")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", "Ławnik i cechmistrz szewski (1658)", None, 39, 1658, "Blasius Kołodziejczyk", "Ławnik i cechmistrz szewski w 1658 r.")
add_occ("Zdebikowic", "Jan", "Kraśnik", "Ławnik kraśnicki (1658)", None, 39, 1658, "Joannes Zdebikowic", "Ławnik w elekcji 1658 r.")
add_occ("Szczurkowic", "Jan", "Kraśnik", "Ławnik kraśnicki (1658)", None, 39, 1658, "Joannes Szczurkowic", "Ławnik w elekcji 1658 r.")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik kraśnicki (1658)", None, 39, 1658, "Mathias Konięga", "Ławnik w elekcji 1658 r.")
add_occ("Kwasowic", "Augustyn", "Kraśnik", "Ławnik kraśnicki (1658)", None, 39, 1658, "Augustinus Kwasowic", "Ławnik w elekcji 1658 r.")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik kraśnicki (1658)", None, 39, 1658, "Gregorius Fox", "Ławnik w elekcji 1658 r.")
add_occ("Tharasa", "Maciej", "Kraśnik", "Asesor do Trybunału i cechmistrz kuśnierski", None, 39, 1658, "Mathiam Tharasa", "Asesor i cechmistrz kuśnierski w 1658 r.")
add_occ("Zętkowic", "Wawrzyniec", "Kraśnik", "Cechmistrz krawiecki (1658)", None, 39, 1658, "Laurentium Zętkowic", "Cechmistrz krawiecki w 1658 r.")
add_occ("Święcicki", "Bartłomiej", "Kraśnik", "Cechmistrz kowalski (1658)", None, 39, 1658, "Bartholomaeum Święcicki", "Cechmistrz kowalski w 1658 r.")
add_occ("Różycki", "Maciej", "Kraśnik", "Cechmistrz tkacki (1658)", None, 39, 1658, "Mathiam Różycki", "Cechmistrz tkacki w 1658 r.")
add_occ("Potokowic", "Jan", "Kraśnik", "Egzaktor miejski (1658)", None, 39, 1658, "Joannem Potokowic", "Egzaktor w elekcji 1658 r.")
add_occ("Bożęborski", "Bartłomiej", "Kraśnik", "Egzaktor miejski (1658)", None, 39, 1658, "Bartholomaeum Bożęborski", "Egzaktor w elekcji 1658 r.")
add_occ("Jarzębek", "Maciej", "Kraśnik", "Egzaktor słodowy (1658)", None, 39, 1658, "Mathias Jarzębek", "Egzaktor słodowy w elekcji 1658 r.")
add_occ("Prokopek", "Wawrzyniec", "Przedmieście Kraśnickie", "Przedmieszczanin / Instygator", None, 39, 1658, "Laurentii Prokopek", "Sprawa z opiekunem dzieci Kowalików o 12 złp 5 gr")
add_occ("Kowalik", "Andrzej", "Przedmieście Kraśnickie", "Zmarły ojciec dzieci", None, 39, 1658, "Andreae Kowalików", "Wzmiankowany przy małoletnich Bartoszu, Kalinie i Lidwinie")
add_occ("Kowalikowa", "Anna", "Przedmieście Kraśnickie", "Matka małoletnich", None, 39, 1658, "Annae Kowalików", "Matka Bartosza, Kaliny i Lidwiny")

# Skan 40 (1658)
add_occ("Prokopek", "Wawrzyniec", "Przedmieście Kraśnickie", "Instygator świadków", None, 40, 1658, "Laurentii Prokopek", "Zeznanie świadka S. Węgorkiewicza o 30 złp za konia")
add_occ("Węgorkiewicz", "Sebastian", "Przedmieście Kraśnickie", "Świadek", None, 40, 1658, "Sebastianus Węgorkiewicz", "Świadek W. Prokopka")
add_occ("Batusik", "Jan", "Przedmieście Kraśnickie", "Aktor", None, 40, 1658, "Joannis Batusik", "Proces przeciw B. Bożęborskiemu o 20 złp na placu Rzepczyńskim")
add_occ("Bożęborski", "Bartłomiej", "Kraśnik", "Pozwany", None, 40, 1658, "Bartholomaei Bożęborski", "Pozwany o 20 złp po J. Dzeku")

# Skan 41 (1658)
add_occ("Nowak", "Benedykt", "Przedmieście Kraśnickie", "Aktor", None, 41, 1658, "Benedicto Nowak", "Wyrok o 35 złp przeciw W. Olęckiemu")
add_occ("Olęcki", "Wojciech", "Kraśnik", "Pozwany", None, 41, 1658, "Alberto Olęcki", "Nakaz zapłaty 35 złp w 3 dni")
add_occ("Młodnicki", "Jędrzej", "Kraśnik", "Aktor", None, 41, 1658, "Andreae Młodnicki", "Uzyskał zamknięcie P. Niedbałki na Bramie Lubelskiej")
add_occ("Niedbałka", "Paweł", "Kraśnik", "Skazany na więzienie", None, 41, 1658, "Pauli Niedbałka", "Skazany na zamknięcie na Bramie Lubelskiej")

# Skan 42 (1658)
add_occ("Olkowski", "Jan", "Kraśnik", "Świadek", None, 42, 1658, "Joannes Olkowski", "Świadek W. Prokopka o 30 złp")
add_occ("Królik", "Grzegorz", "Przedmieście Kraśnickie", "Aktor", None, 42, 1658, "Gregorio Królik", "Wyrok o 20 złp przeciw S. Cwikowi")
add_occ("Cwik", "Stanisław", "Przedmieście Kraśnickie", "Pozwany", None, 42, 1658, "Stanislao Cwik", "Nakaz zapłaty 20 złp G. Królikowi")
add_occ("Wronina", "Jadwiga", "Kraśnik", "Wdowa / Aktorka", None, 42, 1658, "Hedvigis Viduae Wronina", "Proces o arszenik przeciw W. Kotyczowi i jego żonie")
add_occ("Kotycz", "Wojciech", "Kraśnik", "Pozwany", "Kotłyk [?]", 42, 1658, "Albertum Kotycz [Kotłyk?]", "Oskarżony z żoną w sprawie o arszenik")

# Skan 43 (1658)
add_occ("Wronina", "Jadwiga", "Kraśnik", "Aktorka", None, 43, 1658, "Aktorka", "Skazana na basztę i przysięgę oczyszczającą ws. arszeniku")
add_occ("Sikora", "Stanisław", "Kraśnik", "Świadek", None, 43, 1658, "Stanisław Sikora", "Świadek w sprawie J. Batusika i B. Bożęborskiego")

# Skan 44 (1658)
add_occ("Kołodziej", "Wojciech", "Kraśnik", "Zmarły rzemieślnik (inwentarz)", None, 44, 1658, "Wojciechu Kołodzieju", "Spisano inwentarz jego warsztatu kołodziejskiego (23 II 1658 r.)")
add_occ("Sitarczyk", "Walenty", "Kraśnik", "Mieszczanin / Taksator inwentarza", None, 44, 1658, "Walentego Sitarczyka", "Spisywał inwentarz po Wojciechu Kołodzieju")
add_occ("Zdebikowic", "Jan", "Kraśnik", "Rajca kraśnicki / Taksator", None, 44, 1658, "Jana Zdebikowica Rajcę", "Spisywał inwentarz po Wojciechu Kołodzieju")

# Skan 45 (1658)
add_occ("Mrowski", "Marcin", "Kraśnik", "Ksiądz, przeor konwentu św. Augustyna", None, 45, 1658, "J. X. Marcina Mrowskiego Przeora", "Zeznanie o testamencie i legacie 20 złp śp. J. Jasińskiej")
add_occ("Jasińska", "Jadwiga", "Kraśnik", "Zmarła testatorka", "Jasinek [?]", 45, 1658, "Jadwiga Jasińska", "Zapisała w testamencie 20 złp na kościół")

# Skan 46 (1658)
add_occ("Niedźwiadek", "Augustyn", "Lublin", "Dłużnik", None, 46, 1658, "Augustynowi Niedźwiadkowi", "Winien 20 złp z legatu J. Jasińskiej")
add_occ("Kosińska", "Marianna Zofia", "Lublin", "Żona A. Niedźwiadka / Dłużniczka", None, 46, 1658, "Mariannie Zofii Kosińskiej", "Współdłużniczka na 20 złp w Lublinie")
add_occ("Piasecki", "Jan", "Przedmieście Kraśnickie", "Zbywca roli na Podlesiu", None, 46, 1658, "Janem Piaseckim", "Sprzedaż roli na Podlesiu M. Sitarskiemu za 160 złp")
add_occ("Piasecka", "Regina", "Przedmieście Kraśnickie", "Żona Jana Piaseckiego / Zbywczyni", "Płazińska [?]", 46, 1658, "Reginą Płazińską [?]", "Współsprzedająca rolę na Podlesiu")
add_occ("Sitarska", "Regina", "Kraśnik", "Żona rajcy Marcina Sitarskiego / Nabywczyni", "Szałkowicówna [?]", 46, 1658, "Reginą Szałkowicówną [?]", "Współnabywczyni roli na Podlesiu")

# Skan 47 (1658)
add_occ("Jurkowic", "Stanisław", "Kraśnik", "Egzaktor przysięgły / Aktor", None, 47, 1658, "Stanislao Jurkowic Exactori", "Proces przeciw J. Skarzykowi o 16 złp 17 gr składek")
add_occ("Skarzyk", "Jan", "Kraśnik", "Mieszczanin / Pozwany", None, 47, 1658, "Joanne Skarzyk", "Nakaz zapłaty 16 złp 17 gr składek")

# Skan 48 (1658)
add_occ("Bielikowa", "Anna", "Rzeczyca", "Wdowa po Macieju Bieliku / Instygatorka", "Bielińska [?]", 48, 1658, "Annae Bielikowa [Bielińska?]", "Zeznania o długach męża w Lublinie (24, 7 i 8 złp)")
add_occ("Bielik", "Maciej", "Rzeczyca", "Zmarły mąż Anny", None, 48, 1658, "Mathiam Bielik de Rzeczyca", "Zmarły wierzyciel w Lublinie")
add_occ("Jarzyk", "Walenty", "Kraśnik", "Mieszczanin kraśnicki / Asystent", None, 48, 1658, "Valentini Jarzyk", "Asystent wdowy A. Bielikowej")
add_occ("Cirulik", "Samuel", "Lublin", "Dłużnik", None, 48, 1658, "Samuela Cirulika", "Winien 24 złp śp. Maciejowi Bielikowi")

# Skan 49 (1659)
add_occ("Cwikielski", "Michał", "Kraśnik", "Nabywca domu przy ul. Lubelskiej", "Chucholski [?]", 49, 1659, "Michałem Cwikielskim [Chucholskim?]", "Zakup domu od M. Sitarskiego za 150 złp")
add_occ("Cwikielska", "Zofia", "Kraśnik", "Żona Michała Cwikielskiego / Nabywczyni", "Biernatówna", 49, 1659, "Zofią Biernatówną", "Współnabywczyni domu przy ul. Lubelskiej")
add_occ("Grabowski", "Mieszkaniec", "Kraśnik", "Sąsiad przy ul. Lubelskiej", None, 49, 1659, "placem Grabowskim", "Sąsiad sprzedanego domu")
add_occ("Mikołajewski", "Mieszkaniec", "Kraśnik", "Sąsiad przy ul. Lubelskiej", None, 49, 1659, "placem Mikołajewskim", "Sąsiad sprzedanego domu")

# Skan 50 (1659)
add_occ("Szwed", "Paweł", "Kraśnik", "Cechmistrz krawiecki (1659)", "Szwed [?]", 50, 1659, "Paulum Szwed [?]", "Wybrany cechmistrzem krawieckim w elekcji 1659 r.")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik i asesor do Trybunału (1659)", None, 50, 1659, "Gregorium Fox", "Wybrany ławnikiem i asesorem w 1659 r.")

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part2.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

csv_path = '/home/ubuntu/workspace/Gen/krasnik_j19_slownik_genealogiczny.csv'
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

print(f"Zapisano gen_data_j19_part2.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
