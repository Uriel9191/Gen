# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part22.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w Partii 23 (skany 551–575) Jednostki 17 (sygn. 35/40/0/1/17) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 551 ---
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 551, 1756, "Józef Gąska", "Zakończenie wizji z Wilczyńskim; manifestacja przeciw Wilkowi")
add_occ("Wilczyński", "Antoni", "Kraśnik", "Mieszkaniec / Pozwany", "Wilk", 551, 1756, "Antoni Wilczyński / Antoni Wilk", "Winny na wizji gruntowej i wrót; pozwany w manifestacji Gąski")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 551, 1756, "Jan Lubartowski Ławnik", "Deputowany ławnik na kondescensji")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 551, 1756, "Szymon Krzeszowski Ławnik", "Deputowany ławnik na kondescensji")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki", None, 551, 1756, "Franciszek Barankiewicz Ławnik", "Deputowany ławnik na kondescensji")
add_occ("Landet", "Adam", "Kraśnik", "Ławnik kraśnicki", None, 551, 1756, "Adam Landet Ławnik", "Deputowany ławnik na kondescensji")

# --- Skan 552 ---
add_occ("Wilczyński", "Antoni", "Kraśnik", "Mieszkaniec / Pozwany", None, 552, 1756, "Antoni Wilk", "Remanifestacja przeciw Józefowi Gąsce i dylacja")
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 552, 1756, "Józef Gąska", "Pozwany w remanifestacji Wilka; dylacja z Antonim i Maciejem Wilkami")
add_occ("Wilczyński", "Maciej", "Kraśnik", "Mieszkaniec / Brat Antoniego", "Wilk", 552, 1756, "Maciej Wilk", "Dylacja z Józefem Gąską o zbieranie pszenicy")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 552, 1756, "Szymon Krzeszowski", "Dylacja z Antonim Pawłowskim")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 552, 1756, "Antoni Pawłowski", "Dylacja z Szymonem Krzeszowskim")
add_occ("Habusz", "Starozakonny", "Kraśnik", "Obywatel starozakonny", None, 552, 1756, "Starozakonny Habusz", "Wyrok w sprawie z Grzegorzem Kołodziejem")
add_occ("Kołodziej", "Grzegorz", "Kraśnik", "Mieszkaniec / Pozwany", None, 552, 1756, "Grzegorz Kołodziej", "Nakaz odprzysiężenia się od 1 złotego")

# --- Skan 553 ---
add_occ("Habusz", "Starozakonny", "Kraśnik", "Obywatel starozakonny", None, 553, 1756, "Habusz", "Zakończenie dekretu z Kołodziejem")
add_occ("Nowakowa", "Józefowa", "Kraśnik", "Żona Józefa Nowaka / Poszkodowana", None, 553, 1756, "Uxor Josephi Nowak", "Zeznanie przeciw Pawłowi Frugie o porwanie z gospody i próbę gwałtu")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Pozwany", None, 553, 1756, "Paweł Fruga", "Oskarżony przez żonę Józefa Nowaka o napaść za miastem")

# --- Skan 554 ---
add_occ("Nowakowa", "Józefowa", "Kraśnik", "Żona Józefa Nowaka / Poszkodowana", None, 554, 1756, "żona Józefa Nowaka", "Dokończenie zeznania przeciw Pawłowi Frugie")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Pozwany", None, 554, 1756, "Paweł Fruga", "Uznany winnym występku w wyroku z Nowakami")
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszkaniec / Ojciec Pawła", None, 554, 1756, "Maciej Fruga", "Aktor z synem Pawłem przeciw Nowakom")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Ojciec Józefa", None, 554, 1756, "Mikołaj Nowak", "Pozwany w wyroku Frugów")
add_occ("Nowak", "Józef", "Kraśnik", "Mieszczanin / Syn Mikołaja", None, 554, 1756, "Józef Nowak", "Uznany winnym samosądu na Frugie")

# --- Skan 555 ---
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Skazany", None, 555, 1756, "Paweł Fruga", "Skazany na 12 grzywien do kościoła, 10 Nowakowi, 4 sądowi i 3 dni wieży")
add_occ("Nowak", "Józef", "Kraśnik", "Mieszczanin / Skazany", None, 555, 1756, "Józef Nowak", "Skazany na 3 grzywny Frugie i 2 grzywny sądowi")
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Skazany", None, 555, 1756, "Wawrzyniec Tokarz", "Skazany na 4 grzywny Frugie i 2 sądowi za pobicie")
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszkaniec / Ojciec Pawła", None, 555, 1756, "Maciej Fruga", "Zobowiązany do odpowiedzialności za syna")

# --- Skan 556 ---
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Strona w wyroku", None, 556, 1756, "Paweł Fruga", "Nakaz deprekacji Józefowi Nowakowi")
add_occ("Nowak", "Józef", "Kraśnik", "Mieszczanin / Strona w wyroku", None, 556, 1756, "Józef Nowak", "Apelacja do sądu radzieckiego")
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Skazany", None, 556, 1756, "Wawrzyniec Tokarz", "Skazany na 1 dzień wieży")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Mieszkaniec / Poszkodowany", None, 556, 1756, "Antoni Pawłowski", "Salwa co do pobicia zostawiona do rozsądzenia")
add_occ("Pietrowski", "Jerzy", "Lubelskie / Kraśnik", "Chorąży lubelski", "Pietrowski?", 556, 1756, "Wielmożny Jerzy Pietrowski [Pietrowski?] Chorążyc Lubelski", "Skarga o pobicie poddanego przez burmistrza Bryśkiewicza")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Burmistrz kraśnicki", None, 556, 1756, "Stanisław Bryśkiewicz Burm. Krasn.", "Areszt na jego urzędzie za pobicie poddanego chorążego")
add_occ("Zdyb", "Grzegorz", "Kraśnik", "Mieszczanin kraśnicki", None, 556, 1756, "Grzegorz Zdyb mieszczanin kras.", "Kupił chałupkę na placu przy starym kierkucie (areszt kahału)")

# --- Skan 557 ---
add_occ("Zdyb", "Grzegorz", "Kraśnik", "Mieszczanin kraśnicki", None, 557, 1756, "Grzegorz Zdyb", "Objęty aresztem kahału oraz aresztem Jana Wolaczka")
add_occ("Wolaczek", "Jan", "Kraśnik", "Młodzian / Spadkobierca", None, 557, 1756, "Jan Wolaczek młodzian", "Kładzie areszt na Grzegorzu Zdybie o pieniądze po macosze")
add_occ("Marachiewicz", "Antoni", "Kraśnik", "Eksaktor kraśnicki", None, 557, 1756, "Antoni Marachiewicz Exaktor Kras.", "Instancja do rewizji zabitego wieprza półrocznego")
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 557, 1756, "Jan Szubertowski Ławnik", "Obecny na rewizji u Marcinowej Cwiekowej")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki", None, 557, 1756, "Franciszek Barankiewicz Ławnik", "Obecny na rewizji u Marcinowej Cwiekowej")
add_occ("Cwiekowa", "Marcinowa", "Przedmieście Kraśnickie", "Przedmieszczanka kraśnicka / Oskarżona", None, 557, 1756, "Marcinowa Cwiekowa Przedmieszczanka kras.", "Oskarżona o zabicie wieprza półrocznego")
add_occ("Bielecka", "Szymonowa", "Kraśnik", "Cieślina / Obywatelka kraśnicka", None, 557, 1756, "Szymonowa Bielecka cieslina", "Początek manifestacji przeciw Wojciechowskiemu")

# --- Skan 558 ---
add_occ("Bielecka", "Szymonowa", "Kraśnik", "Cieślina / Obywatelka kraśnicka", None, 558, 1756, "Szymonowa Bielecka z córką", "Wieczna zgoda z Jakubem Wojciechowskim pod zakładem 30 grzywien")
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Ślusarz / Mieszczanin", None, 558, 1756, "Jakub Woyciechowski ślusarz (+)", "Ugoda z Szymonową Bielecką (podpis krzyżem)")
add_occ("Wojciechowska", "Marianna", "Kraśnik", "Żona Jakuba Wojciechowskiego", None, 558, 1756, "żona Marianna (+)", "Współpodpisana pod ugodą z Szymonową Bielecką")

# --- Skan 559 ---
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Ślusarz / Mieszczanin", None, 559, 1756, "Jakub Woyciechowski", "Kondescensja przeciw Szymonowej Bieleckiej")
add_occ("Bielecka", "Szymonowa", "Kraśnik", "Cieślina / Obywatelka kraśnicka", None, 559, 1756, "żona Bieleckiego", "Ugoda na wizji gruntowej")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 559, 1756, "Szymon Krzeszowski", "Deputowany na kondescensji")
add_occ("Zadel", "Adam", "Kraśnik", "Ławnik kraśnicki", None, 559, 1756, "Adam Zadel", "Deputowany na kondescensji")

# --- Skan 560 ---
add_occ("Zdyb", "Sobestyjan", "Kraśnik", "Mieszkaniec / Strona w ugodzie", None, 560, 1756, "Sobestyan Zdyb (+)", "Ugoda z Abramowiczem według pana gubernatora")
add_occ("Abramowicz", "Starozakonny", "Kraśnik", "Obywatel starozakonny", None, 560, 1756, "Abramowicz (+)", "Ugoda z Sobestyjanem Zdybem (podpis krzyżem)")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 560, 1756, "Jan Lubartowski Ławnik kras.", "Ugoda przez przyjaciół z Marcinem Morelem")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat na Trybunał Zamoyski", None, 560, 1756, "Marcin Morel przełożony Deputat", "Uczynił satysfakcję Janowi Lubartowskiemu")

# --- Skan 561 ---
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 561, 1756, "Jan Lubartowski (+)", "Zapisanie wadium 10 grzywien w ugodzie z Morelem")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat na Trybunał Zamoyski", None, 561, 1756, "Marcin Morel (+)", "Podpisanie ugody z Lubartowskim")
add_occ("Pilaszkiewicz", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 561, 1756, "Antoni Pilaszkiewicz Ławnik kras.", "Świadek ugody Lubartowskiego z Morelem")
add_occ("Zadel", "Adam", "Kraśnik", "Ławnik kraśnicki", None, 561, 1756, "Adam Zadel Ławnik kras.", "Świadek ugody Lubartowskiego z Morelem")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Burmistrz i pisarz kraśnicki", None, 561, 1756, "Stanisław Bryśkiewicz", "Ugoda z winiarzem Tomaszem Renkasem za pobicie")
add_occ("Renkas", "Tomasz", "Kraśnik", "Winiarz u starozakonnej arendarki", None, 561, 1756, "Tomasz Renkas winiarz", "Odbiorca satysfakcji od Stanisława Bryśkiewicza")

# --- Skan 562 ---
add_occ("Renkas", "Tomasz", "Kraśnik", "Winiarz u starozakonnej arendarki", None, 562, 1757, "Tomasz Renkas (+)", "Podpisanie ugody z Bryśkiewiczem")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Pisarz i burmistrz kraśnicki", None, 562, 1757, "Stanisław Bryśkiewicz Pisarz y Burm. Kras.", "Asekuracja ugody dla Renkasa")
add_occ("Wilczyński", "Antoni", "Kraśnik", "Mieszkaniec / Powód", None, 562, 1757, "Antonius Wilczyński", "Inkwizycja przeciw Józefowi Gąsce o zabicie psa")
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 562, 1757, "Josephus Gąska", "Pozwany w inkwizycji o zabicie psa")
add_occ("Cwieka", "Jan", "Kraśnik", "Mieszkaniec / Świadek", None, 562, 1757, "Joannes Cwieka", "Zeznanie pod sumieniem w sprawie zabitego psa")
add_occ("Petrykowski", "Antoni", "Kraśnik", "Burmistrz / Strona w sporze", None, 562, 1757, "Antoni Petrykowski", "Manifestacja przeciw Krzeszowskiemu i Potokowiczowi")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 562, 1757, "Szymon Krzeszowski", "Pozwany w manifestacji Petrykowskiego")
add_occ("Potokowicz", "Wojciech", "Kraśnik", "Mieszkaniec / Poręczyciel", None, 562, 1757, "Wojciech Potokowicz", "Pozwany w manifestacji Petrykowskiego")

# --- Skan 563 ---
add_occ("Petrykowski", "Antoni", "Kraśnik", "Burmistrz / Strona w sporze", None, 563, 1757, "Antoni Petrykowski", "Zakończenie manifestacji o poręczenie")
add_occ("Cwiekowa", "Marcinowa", "Przedmieście Kraśnickie", "Przedmieszczanka kraśnicka", None, 563, 1757, "Marcinowa Cwiekowa", "Niestawiennictwo na termin ugody z Petrykowskim")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 563, 1757, "Szymon Krzeszowski", "Poręczyciel w sprawie Cwiekowej")
add_occ("Potokowicz", "Wojciech", "Kraśnik", "Mieszkaniec / Poręczyciel", None, 563, 1757, "Wojciech Potokowicz", "Poręczyciel w sprawie Cwiekowej")
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 563, 1757, "Józef Gąska", "Wyrok przeciw Antoniemu Wilczyńskiemu o zniewagę")
add_occ("Wilczyński", "Antoni", "Kraśnik", "Mieszkaniec / Skazany", None, 563, 1757, "Antoni Wilczyński", "Skazany na 3 grzywny sądowi, 1 aktorowi i deprekację")
add_occ("Łuszka", "Jan", "Kraśnik", "Mieszkaniec / Właściciel psa", "Łuszka?", 563, 1757, "Jan Łuszka [Łuszka?]", "Właściciel postrzelonego psa")
add_occ("Cwieka", "Jan", "Kraśnik", "Mieszkaniec / Strona", None, 563, 1757, "Jan Cwieka", "Odbiorca deprekacji od Gąski")

# --- Skan 564 ---
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 564, 1757, "Józef Gąska", "Apelacja do Trybunału Zamoyskiego")
add_occ("Wilczyński", "Antoni", "Kraśnik", "Mieszkaniec / Strona", None, 564, 1757, "Antoni Wilczyński", "Przyjął dekret")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Burmistrz kraśnicki", None, 564, 1757, "Łukasz Krzeszowski Burm. Kras.", "Manifestacja przeciw bratu Szymonowi o rzekome pokrewieństwo z Pawłowską")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 564, 1757, "Szymon Krzeszowski Ław. Kras. Brat Rodzony", "Wyłączył brata burmistrza z sądu")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Mieszkaniec / Strona", None, 564, 1757, "Antoni Pawłowski", "Wspomniana jego żona w sporze o pokrewieństwo")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Powód", None, 564, 1757, "Mikołaj Nowak", "Manifestacja przeciw Frugom o niepoprowadzenie apelacji")
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszkaniec / Pozwany", None, 564, 1757, "Maciej Fruga", "Oskarżony o zwlekanie po apelacji")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Pozwany", None, 564, 1757, "Paweł Fruga", "Oskarżony o niepoprowadzenie apelacji")

# --- Skan 565 ---
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Powód", None, 565, 1757, "Mikołaj Nowak", "Areszt na dekrecie z Antonim Pawłowskim")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Mieszkaniec / Pozwany", None, 565, 1757, "Antoni Pawłowski", "Objęty aresztem dekretu")
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 565, 1757, "Józef Gąska", "Manifestacje przeciw Antoniemu i Maciejowi Wilczyńskim")
add_occ("Wilczyński", "Antoni", "Kraśnik", "Mieszkaniec / Pozwany", None, 565, 1757, "Antoni Wilczyński", "Oskarżony o pogróżki na zdrowie i życie Gąski")
add_occ("Jazdyk", "Józef", "Kraśnik", "Mieszkaniec / Wspomniany", None, 565, 1757, "Józef Jazdyk", "Wspomniany w pogróżkach Antoniego Wilczyńskiego")
add_occ("Wilczyński", "Maciej", "Kraśnik", "Mieszkaniec / Pozwany", None, 565, 1757, "Maciej Wilczyński", "Oskarżony o zarzucanie kradzieży na kondescensji")

# --- Skan 566 ---
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 566, 1757, "Józef Gąska", "Zakończenie manifestacji przeciw Maciejowi Wilczyńskiemu")
add_occ("Wilczyński", "Maciej", "Kraśnik", "Mieszkaniec / Pozwany", None, 566, 1757, "Maciej Wilczyński", "Zakończenie manifestacji Gąski")
add_occ("Pągek", "Szymon", "Kraśnik", "Mieszkaniec / Poszkodowany", "Pągnek?", 566, 1757, "Szymon Pągek [Pągek / Pągnek?]", "Wizja szkody w trawie i inkwizycja przeciw Walentemu Jorgiełowi")
add_occ("Jorgieł", "Walenty", "Kraśnik", "Mieszkaniec / Pozwany", None, 566, 1757, "Walenty Jorgieł", "Oskarżony o szkodę w trawie przez konia")
add_occ("Pilaszkiewicz", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 566, 1757, "Antoni Pilaszkiewicz Ławnik", "Deputowany na wizji w sadzie Szymona Pągka")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki", None, 566, 1757, "Franciszek Barankiewicz Ławnik", "Deputowany na wizji w sadzie Szymona Pągka")
add_occ("Tokarzowa", "Katarzyna", "Kraśnik", "Mieszkanka / Świadek", None, 566, 1757, "Katarzyna Tokarzowa", "Zeznanie w sprawie szkody konia Walentego Jorgieła")

# --- Skan 567 ---
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 567, 1757, "Josephus Gąska", "Inkwizycja przeciw Antoniemu i Matyaszowi Wilkom")
add_occ("Wilczyński", "Antoni", "Kraśnik", "Mieszkaniec / Pozwany", None, 567, 1757, "Antonius Wilczyński / Witek", "Świadkowie zeznają o jego rozmowach i sporze o zboże")
add_occ("Grabowski", "Tomasz", "Kraśnik", "Mieszkaniec / Świadek w cegielni", None, 567, 1757, "Thomas Grabowski", "Zeznanie o namowach Antoniego Wilczyńskiego w Cegielni Stróżce")
add_occ("Łypek", "Matyasz", "Kraśnik", "Parobek u Gąski / Świadek", "Łypa?", 567, 1757, "Mathias Łypek [Łypek / Łypa?]", "Zeznanie o wiązaniu pszenicy na pasiece i sporze na gruncie")

# --- Skan 568 ---
add_occ("Łypek", "Matyasz", "Kraśnik", "Parobek u Gąski / Świadek", "Łypa?", 568, 1757, "Mathias Łypa", "Dokończenie zeznania")
add_occ("Wilczyński", "Maciej", "Kraśnik", "Mieszkaniec / Pozwany", "Witek", 568, 1757, "Maciej Witek", "Zabrał snopy pszenicy do lasu")
add_occ("Wolak", "Grzegorz", "Przedmieście Kraśnickie", "Przedmieszczanin / Świadek", None, 568, 1757, "Gregorius Wolak", "Zeznanie o groźbach Macieja Witka wobec Gąski")
add_occ("Wilczek", "Antoni", "Kraśnik", "Mieszkaniec / Świadek", None, 568, 1757, "Antonius Wilczek", "Zeznanie o wstawieniu składu przy spornej miedzy")
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 568, 1757, "Józef Gąska Przedmiesz. Kras.", "Początek dekretu przeciw Antoniemu Wilczyńskiemu")
add_occ("Wilczyński", "Antoni", "Kraśnik", "Mieszkaniec / Pozwany", None, 568, 1757, "Antoni Wilczyński", "Uznany winnym znieważania przedmieszczanina")

# --- Skan 569 ---
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 569, 1757, "Józef Gąska", "Ciąg dalszy wyroku (4 i 3 grzywny od Wilczyńskiego)")
add_occ("Wilczyński", "Antoni", "Kraśnik", "Mieszkaniec / Skazany", None, 569, 1757, "Antoni Wilczyński", "Skazany na grzywny i zwrot pszenicy")

# --- Skan 570 ---
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 570, 1757, "Józef Gąska", "Apelacja do Trybunału Zamoyskiego; dylacja z Matyaszem Wilczyńskim")
add_occ("Wilczyński", "Antoni", "Kraśnik", "Mieszkaniec / Strona", None, 570, 1757, "Antoni Wilczyński", "Przyjął dekret")
add_occ("Wilczyński", "Matyasz", "Kraśnik", "Przedmieszczanin kraśnicki", None, 570, 1757, "Matyasz Wilczyński Przedmieszczanin Kras.", "Dylacja z Józefem Gąską o zarzut kradzieży płotu")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Przedmieszczanin kraśnicki", None, 570, 1757, "Mikołaj Nowak przedmieszczanin kras.", "Manifestacja przeciw Matyaszowi i Pawłowi Frugom")
add_occ("Fruga", "Matyasz", "Kraśnik", "Mieszkaniec / Pozwany", None, 570, 1757, "Matyasz Fruga", "Pozwany w manifestacji Mikołaja Nowaka")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Pozwany", None, 570, 1757, "Paweł Fruga", "Pozwany w manifestacji Mikołaja Nowaka")

# --- Skan 571 ---
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Powód", None, 571, 1757, "Mikołaj Nowak", "Zakończenie manifestacji przeciw Frugom")
add_occ("Fruga", "Matyasz", "Kraśnik", "Mieszkaniec / Pozwany", None, 571, 1757, "Matyasz Fruga", "Zakończenie manifestacji Nowaka")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Pozwany", None, 571, 1757, "Paweł Fruczyński", "Wspomniany jako nieposiadający własnej posesji")
add_occ("Krzywiński", "Michał", "Kraśnik", "Wójt i najpierwszy sędzia Kraśnika", None, 571, 1757, "Michał Krzywiński Wójt y Najpierwszy Sędzia Miasta Kras.", "Manifestacja przeciw JP Janowi Jędrzejowi Kofeckiemu")
add_occ("Kofecki", "Jędrzej", "Kraśnik", "Szlachetny / Pozwany", None, 571, 1757, "JmPan Jędrzej Kofecki", "Pozwany w manifestacji wójta Krzywińskiego")

# --- Skan 572 ---
add_occ("Krzywiński", "Michał", "Kraśnik", "Wójt i sędzia kraśnicki", None, 572, 1757, "Michał Krzywiński", "Zakończenie manifestacji przeciw Kofeckiemu (nazwanie szelmą)")
add_occ("Kofecki", "Jędrzej", "Kraśnik", "Szlachetny / Pozwany", None, 572, 1757, "JmPan Jędrzej Kofecki", "Oskarżony o zniewagę wójta w gospodzie")
add_occ("Jabłonowski", "Książę", "Zakrzów / Okolice", "Książę / Właściciel wsi Zakrzowa", None, 572, 1757, "JOXiążę Jabłonowski", "Wspomniany przy pretensji chłopów z jego wsi Zakrzowa")

# --- Skan 573 ---
add_occ("Szymkowski", "Szymon", "Kraśnik", "Szafarz miejski kraśnicki", None, 573, 1757, "Szymon Szymkowski mieszczanin kras.", "Odebrał szafarstwo bez przysięgi")
add_occ("Kawka", "Mikołaj", "Kraśnik", "Szafarz miejski kraśnicki", None, 573, 1757, "Mikołaj Kawka mieszczanin kras.", "Odebrał szafarstwo bez przysięgi u Antoniego Tokarczyka")
add_occ("Tokarz", "Antoni", "Kraśnik", "Burmistrz / Gospodarz", "Tokarczyk", 573, 1757, "Antoni Tokarczyk", "W jego rezydencji Kawka odebrał szafarstwo")
add_occ("Łukaszowa", "Pani Rezydentowa", "Kraśnik", "Pani Rezydentowa", None, 573, 1757, "Pani Rezydentowa Łukaszowa", "Otrzymała 16 złp od wójta zarzyckiego")
add_occ("Herbst", "Józef", "Kraśnik", "Architekt klasztoru kraśnickiego", None, 573, 1757, "Jozef Herbst architekt klasztoru krasnickiego", "Ugoda honorowa z burmistrzem Bryśkiewiczem (podpis własnoręczny)")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Pisarz i burmistrz kraśnicki", None, 573, 1757, "Stanisław Bryśkiewicz Pisarz y Bur. Kras.", "Ugoda honorowa z architektem Józefem Herbstem")

# --- Skan 574 ---
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Powód", None, 574, 1757, "Mikołaj Nowak", "Wyrok przeciw niewiernej Fejdli Szyjowej o rozliczenie jarmarcznych (60 złp)")
add_occ("Szyjowa", "Fejdla", "Kraśnik", "Niewierna / Handlarka", "Szyjowa?", 574, 1757, "Niewierna Fejdla Szyjowa [Szyjowa?]", "Nakaz zapłaty per medium 29 złp Mikołajowi Nowakowi")

# --- Skan 575 ---
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Powód", None, 575, 1757, "Mikołaj Nowak", "Zakończenie wyroku (29 złp)")
add_occ("Szyjowa", "Fejdla", "Kraśnik", "Niewierna / Handlarka", "Szyjowa?", 575, 1757, "Fejdla Szyjowa", "Nakaz zapłaty 29 złp")
add_occ("Przesławski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 575, 1757, "Joannes Przesławski Scabinus Cras.", "Inkwizycja przeciw Piotrowi Potokowiczowi i jego żonie o zniewagę")
add_occ("Potokowicz", "Piotr", "Kraśnik", "Mieszkaniec / Pozwany", None, 575, 1757, "Petrus Potokowicz", "Pozwany wraz z żoną przez Jana Przesławskiego")
add_occ("Potokowiczowa", "Piotrowa", "Kraśnik", "Żona Piotra Potokowicza", None, 575, 1757, "Piotrowa Potokowiczowa", "Oskarżona o zniesławienie Jana Przesławskiego na mieście")

# Weryfikacja braku duplikatów (Wariant 2)
keys = [(p['nazwisko'], p['imie'], p['miejsce']) for p in gen_data]
assert len(keys) == len(set(keys)), "DUPLICATE IDENTITY DETECTED!"
for p in gen_data:
    assert p.get('funkcja'), f"EMPTY ROLE: {p}"

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part23.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

# Eksport CSV UTF-8-SIG z 9 kanonicznymi kolumnami
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
    writer.writerow(["Lp", "Nazwisko", "Imię", "Miejsce", "Funkcja społeczna / zawód", "Skany źródłowe", "Zakres lat", "Liczba wzmianek", "Warianty nazwiska"])
    for p in gen_data:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p['funkcja'],
            p['skany_roboczo'],
            p['zakres_lat'],
            p['liczba_wystapien'],
            p.get('wariant_nazwiska') or ''
        ])

print(f"SUCCESS: gen_data_j17_part23.json ({len(gen_data)} profiles) and CSV exported.")
