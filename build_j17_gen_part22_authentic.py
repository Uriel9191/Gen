# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part21.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w Partii 22 (skany 526–550) Jednostki 17 (sygn. 35/40/0/1/17) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 526 ---
add_occ("Radkowski", "Bartłomiej", "Kraśnik", "Mieszkaniec / Świadek", None, 526, 1757, "Bartłomiej Radkowski", "Świadek na wizji gruntowej Szymona Bieleckiego i Jakuba Wojciechowskiego")
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Ślusarz / Mieszczanin", None, 526, 1757, "Jakub Wojciechowski", "Nakaz rozebrania płotu na gruncie Bieleckiego, zachowanie chlewka")
add_occ("Bielecki", "Szymon", "Kraśnik", "Mieszczanin / Właściciel gruntu", None, 526, 1757, "Szymon Bielecki", "Wizja gruntowa przeciw Jakubowi Wojciechowskiemu")
add_occ("Lubrzyński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 526, 1757, "Antoni Lubrzyński", "Świadek i ławnik na wizji gruntowej")
add_occ("Pankiewicz", "Szymon", "Kraśnik", "Sławetny / Członek komisji wizyjnej", None, 526, 1757, "Szymon Pankiewicz", "Uczestnik komisji wizyjnej")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Sławetny / Członek komisji wizyjnej", None, 526, 1757, "Łukasz Krzeszowski", "Uczestnik komisji wizyjnej")
add_occ("Petrykowski", "Antoni", "Kraśnik", "Burmistrz kraśnicki", None, 526, 1757, "Antoni Petrykowski Burm.", "Burmistrz obecny na wizji gruntowej")
add_occ("Przesławski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 526, 1757, "Jan Przesławski Ławnik Kras.", "Ławnik na wizji gruntowej")
add_occ("Brzyski", "Stanisław", "Kraśnik", "Pisarz miejski kraśnicki", None, 526, 1757, "Stanisław Brzyski Pisarz", "Pisarz miejski na wizji gruntowej")
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 526, 1757, "Wawrzyniec Tokarz", "Aktor w sprawie przeciw Marcinowi Budzyńskiemu")
add_occ("Budzyński", "Marcin", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 526, 1757, "Marcin Budzyński", "Pozwany przez Wawrzyńca Tokarza")

# --- Skan 527 ---
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 527, 1757, "Wawrzyniec Tokarz", "Skazany na 4 grzywny pozwanemu i 2 grzywny sądowi za zawód")
add_occ("Budzyński", "Marcin", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 527, 1757, "Marcin Budzyński", "Odbiorca 4 grzywien i deprekacji od Tokarza")
add_occ("Trzciński", "Antoni", "Kraśnik", "Mieszkaniec / Strona w sporze spadkowym", None, 527, 1757, "Antoni Trzciński", "Spór z Krzysztofem Kofeckim o sukcesję po dziadkach")
add_occ("Grabowski", "Tomasz", "Kraśnik", "Mieszkaniec / Strona w sporze spadkowym", None, 527, 1757, "Tomasz Grabowski", "Współpowód z Antonim Trzcińskim; wspomniany w dekrecie z Maziarczykiem")
add_occ("Kofecki", "Krzysztof", "Kraśnik", "Mieszkaniec / Strona w sporze spadkowym", None, 527, 1757, "Krzysztof Kofecki", "Dylacja na wywód sukcesji po dziadkach")
add_occ("Maziarczyk", "Józef", "Kraśnik", "Mieszkaniec / Strona w dekrecie", None, 527, 1757, "Józef Maziarczyk", "Wspomniany w dekrecie z Tomaszem Grabowskim")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin i magister szewski", None, 527, 1757, "Adam Posuniak", "Aktor przeciw Antoniemu Dudkowi o 22 złp długu")
add_occ("Dudek", "Antoni", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 527, 1757, "Antoni Dudek", "Pozwany o 22 złp za Sebastiana Świderskiego")
add_occ("Świderski", "Sebastian", "Kraśnik", "Mieszkaniec / Dłużnik (zmarły?)", "Świderski?", 527, 1757, "Sebastian Świderski [Świderski?]", "Wspomniany przy pożyczce 22 złp przed kilkunastu laty")

# --- Skan 528 ---
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin i magister szewski", None, 528, 1757, "Adam Posuniak", "Dylacja z Antonim Dudkiem o 22 złp")
add_occ("Dudek", "Antoni", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 528, 1757, "Antoni Dudek", "Dylacja z Adamem Posuniakiem")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 528, 1757, "Kazimierz Młynarski", "Poręczyciel za Wawrzyńca Tokarza; manifestacja przeciw Frankiewiczowi")
add_occ("Kawka", "Mikołaj", "Kraśnik", "Mieszkaniec / Poręczyciel", None, 528, 1757, "Mikołaj Kawka", "Poręczyciel za Wawrzyńca Tokarza (podpis krzyżem)")
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 528, 1757, "Wawrzyniec Tokarz", "Zwolniony z więzienia za poręką Młynarskiego i Kawki")
add_occ("Budzyński", "Marcin", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 528, 1757, "Marcin Budzyński", "Odbiorca satysfakcji od Tokarza")
add_occ("Frankiewicz", "Wojciech", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 528, 1757, "Wojciech Frankiewicz", "Pozwany przez Młynarskiego o zaoranie żyta i skargę do gubernatora stróżkiego")
add_occ("Chrzanowski", "Jan", "Stróża / Kraśnik", "Gubernator stróżki (klucza kraśnickiego)", None, 528, 1757, "ImPan Chrzanowski Gubernator Stróżki", "Odbiorca skargi żony Frankiewicza przeciw mieszczaninowi Młynarskiemu")

# --- Skan 529 ---
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 529, 1757, "Kazimierz Młynarski", "Zakończenie manifestacji przeciw Frankiewiczowi (pobicie przez hajduka)")
add_occ("Frankiewicz", "Wojciech", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 529, 1757, "Wojciech Frankiewicz", "Zakończenie manifestacji Młynarskiego")
add_occ("Kofecki", "Jędrzej", "Kraśnik", "Szlachetny / Mieszkaniec", None, 529, 1757, "JmPan Jan Jędrzej Kofecki", "Manifestacja przeciw Krengli Osypowej o utratę konia (8 talarów) i rzeczy (5 złp 23 gr)")
add_occ("Osypowa", "Krengla", "Kraśnik", "Starozakonna / Strona pozwana", None, 529, 1757, "Niew. Krengla Osypowa", "Pozwana o utratę konia i sprzętu w drodze z paniami")

# --- Skan 530 ---
add_occ("Kofecki", "Jędrzej", "Kraśnik", "Szlachetny / Mieszkaniec", None, 530, 1757, "JmPan Jędrzej Kofecki", "Remanifestacja przeciw Szymonowi Marszałkowskiemu o 60 złp długu i zastaw klina")
add_occ("Marszałkowski", "Szymon", "Kraśnik", "Sławetny / Mieszczanin", None, 530, 1757, "Szymon Marszałkowski", "Pozwany przez Kofeckiego o oranie gruntu mimo niespłaconego długu 60 złp")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", "Rady starszej / Mieszczanin", None, 530, 1757, "Grzegorz Pilaszkiewicz", "Orał na gruncie za pozwoleniem JPana Kofeckiego")
add_occ("Habusz", "Starozakonny", "Kraśnik", "Obywatel starozakonny / Powód", None, 530, 1757, "Starozak. Habusz", "Aktor w sprawie przeciw Jędrzejowi Rymarczykowi i żonie")
add_occ("Rymarczyk", "Jędrzej", "Kraśnik", "Mieszkaniec / Strona pozwana", None, 530, 1757, "Jędrzej Rymarczyk", "Pozwany wraz z żoną przez starozakonnego Habusia")
add_occ("Chrzanowski", "Jan", "Stróża / Kraśnik", "Gubernator klucza kraśnickiego", None, 530, 1757, "JmPan Chrzanowski Gubernator na ten czas klucza Kraśnickiego", "Zasiadał w sądzie w sprawie Habusia z Rymarczykiem")

# --- Skan 531 ---
add_occ("Habusz", "Starozakonny", "Kraśnik", "Obywatel starozakonny / Powód", None, 531, 1757, "Habusz", "Dochodzi 37 czerwonych złotych i 37 tynfów zgubionych w woreczku")
add_occ("Rymarczyk", "Jędrzej", "Kraśnik", "Mieszkaniec / Strona pozwana", None, 531, 1757, "Jędrzej Rymarczyk", "Zeznał, że nie wiedział o pieniądzach znalezionych przez żonę")
add_occ("Rymarczykowa", "Jędrzejowa", "Kraśnik", "Żona Jędrzeja Rymarczyka", None, 531, 1757, "Jędrzeja Rymarczyka żona", "Znalazła woreczek na pogrzebie Katarzyny córki Maliny i ukryła przed mężem")
add_occ("Malina", "Katarzyna", "Kraśnik", "Zmarła córka Maliny", None, 531, 1757, "Katarzyna córka Maliny", "W dzień jej pogrzebu znaleziono zgubiony woreczek z pieniędzmi")

# --- Skan 532 ---
add_occ("Habusz", "Starozakonny", "Kraśnik", "Obywatel starozakonny / Powód", None, 532, 1757, "Habusz", "Wyrok nakazujący Rymarczykowej zwrot 4 czerwonych złotych i 1 złp")
add_occ("Rymarczyk", "Jędrzej", "Kraśnik", "Mieszkaniec / Strona pozwana", None, 532, 1757, "Jędrzej Rymarczyk", "Strona w dekrecie z Habuszem")
add_occ("Rymarczykowa", "Jędrzejowa", "Kraśnik", "Żona Jędrzeja Rymarczyka", None, 532, 1757, "pozwana", "Skazana na zwrot 4 czerwonych złotych i przysięgę w kościele kraśnickim")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin i magister szewski", None, 532, 1757, "Adam Posuniak", "Dylacja z Antonim Dudkiem")
add_occ("Dudek", "Antoni", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 532, 1757, "Antoni Dudek", "Dylacja z Adamem Posuniakiem")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 532, 1757, "Kazimierz Młynarski", "Dylacja przeciw Wojciechowi Frankiewiczowi")
add_occ("Frankiewicz", "Wojciech", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 532, 1757, "Wojciech Frankiewicz", "Nakaz stawienia żony do sądu")
add_occ("Bielecki", "Szymon", "Kraśnik", "Mieszczanin / Właściciel gruntu", None, 532, 1757, "Szymon Bielecki", "Początek manifestacji przeciw Jakubowi Wojciechowskiemu")

# --- Skan 533 ---
add_occ("Bielecki", "Szymon", "Kraśnik", "Mieszczanin / Właściciel gruntu", None, 533, 1757, "Szymon Bielecki", "Manifestacja przeciw Wojciechowskiemu o trzecią wizję gruntu")
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Ślusarz / Mieszczanin", None, 533, 1757, "Jakub Wojciechowski", "Remanifestacja przeciw Bieleckiemu o przywłaszczenie kawałka gruntu")

# --- Skan 534 ---
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Ślusarz / Mieszczanin", None, 534, 1757, "Jakub Wojciechowski", "Zakończenie remanifestacji przeciw Bieleckiemu")
add_occ("Bielecki", "Szymon", "Kraśnik", "Mieszczanin / Właściciel gruntu", None, 534, 1757, "Szymon Bielecki", "Pozwany w remanifestacji Wojciechowskiego")
add_occ("Petrykowski", "Antoni", "Kraśnik", "Burmistrz kraśnicki", None, 534, 1757, "Antoni Petrykowski Burmistrz", "Obecny na wizji gruntowej")
add_occ("Pilaszkiewicz", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 534, 1757, "Antoni Pilaszkiewicz", "Świadek na wizji gruntowej")
add_occ("Zdyb", "Jan", "Kraśnik", "Mieszczanin / Świadek", None, 534, 1757, "Jan Zdyb", "Świadek pamiętający granice gruntu")
add_occ("Przesławska", "Janowa", "Kraśnik", "Mieszkanka / Świadek", None, 534, 1757, "Janowa Przesławska", "Świadek pamiętający granice gruntu")
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszkaniec / Ojciec Pawła", None, 534, 1757, "Maciej Fruga", "Manifestacja w imieniu swoim i syna Pawła przeciw Nowakom o pobicie")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Poszkodowany", None, 534, 1757, "Paweł Fruga", "Pobity przez Nowaków w gospodzie; pozwany przez Józefa Nowaka")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Pozwany", None, 534, 1757, "Mikołaj Nowak", "Oskarżony o pobicie Pawła Frugi")
add_occ("Nowak", "Józef", "Kraśnik", "Mieszczanin / Strona w sporze", None, 534, 1757, "Józef Nowak", "Oskarżony o pobicie Frugi; manifestacja przeciw Frugie o napad na żonę")
add_occ("Nowak", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Pozwany", None, 534, 1757, "Wawrzyniec Nowak", "Oskarżony wraz z ojcem i bratem o pobicie Pawła Frugi")

# --- Skan 535 ---
add_occ("Nowak", "Józef", "Kraśnik", "Mieszczanin / Strona w sporze", None, 535, 1757, "Józef Nowak", "Zakończenie manifestacji przeciw Pawłowi Frugie")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 535, 1757, "Paweł Fruga", "Dylacja z Nowakiem, Tokarzem i Kiliankiem z powodu choroby po pobiciu")
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszkaniec / Ojciec Pawła", None, 535, 1757, "Maciej Fruga", "Dylacja w sprawie pobicia syna")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Pozwany", None, 535, 1757, "Mikołaj Nowak", "Dylacja z Frugami")
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Pozwany", None, 535, 1757, "Wawrzyniec Tokarz", "Pozwany w sprawie z Frugami")
add_occ("Kilianek", "Bartłomiej", "Kraśnik", "Mieszczanin / Pozwany", None, 535, 1757, "Bartłomiej Kilianek", "Pozwany w sprawie z Frugami")
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Ślusarz / Mieszczanin", None, 535, 1757, "Jakub Wojciechowski Ślusarz", "Trzecia wizja jego gruntu spornego z Bieleckim")
add_occ("Bielecki", "Szymon", "Kraśnik", "Mieszczanin / Właściciel gruntu", None, 535, 1757, "Szymon Bielecki", "Uczestnik wizji gruntowej")

# --- Skan 536 ---
add_occ("Bielecki", "Szymon", "Kraśnik", "Mieszczanin / Właściciel gruntu", None, 536, 1757, "Szymon Bielecki", "Zakończenie trzeciej wizji gruntowej i dylacja z Wojciechowskim")
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Ślusarz / Mieszczanin", None, 536, 1757, "Jakub Wojciechowski", "Zakończenie wizji i dylacja na zgodę przez 2 ludzi")
add_occ("Tokarz", "Antoni", "Kraśnik", "Burmistrz kraśnicki", None, 536, 1757, "Antoni Tokarz Burm.", "Obecny na wizji gruntowej")
add_occ("Pilaszkiewicz", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 536, 1757, "Antoni Pilaszkiewicz", "Obecny na wizji gruntowej")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 536, 1757, "Szymon Krzeszowski Ław.", "Obecny na wizji gruntowej")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", "Radca starszy", None, 536, 1757, "Grzegorz Pilaszkiewicz Radca Stary", "Obecny na wizji gruntowej")
add_occ("Jańczyk", "Stanisław", "Kraśnik", "Poprzedni właściciel gruntu", None, 536, 1757, "Stanisław Jańczyk przedawca tego gruntu", "Zeznał o sprzedaży gruntu Bieleckiemu i starych kołkach")
add_occ("Zdyb", "Bartłomiej", "Kraśnik", "Mieszczanin / Świadek", None, 536, 1757, "Bartłomiej Zdyb", "Świadek na wizji potwierdzający dokument i granice")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin / Świadek", None, 536, 1757, "Adam Posuniak", "Świadek na wizji gruntowej")
add_occ("Janowski", "Stanisław", "Kraśnik", "Sławetny / Świadek", "Janowicz?", 536, 1757, "Sław. Janowski [Janowski / Janowicz?]", "Świadek pamiętający grunt Jakuba Wojciechowskiego")
add_occ("Nachymowicz", "Lebuś", "Kraśnik / Turobin", "Obywatel starozakonny / Właściciel kamienicy", None, 536, 1757, "Lebuś Nachymowicz", "Wizja jego zdewastowanego domu murowanego w Kraśniku")

# --- Skan 537 ---
add_occ("Nachymowicz", "Lebuś", "Kraśnik / Turobin", "Obywatel starozakonny / Właściciel kamienicy", None, 537, 1757, "Lebuś Nachymowicz Obywatel Turobiński [?]", "Obciążony odpowiedzialnością za dezolację kamienicy")
add_occ("Szymkowski", "Szymon", "Kraśnik", "Sławetny / Członek komisji wizyjnej", None, 537, 1757, "Szymon Szymkowski", "Obecny na wizji domu murowanego")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Sławetny / Członek komisji wizyjnej", None, 537, 1757, "Łukasz Krzeszowski", "Obecny na wizji domu murowanego")
add_occ("Tokarz", "Antoni", "Kraśnik", "Sławetny / Członek komisji wizyjnej", None, 537, 1757, "Antoni Tokarz", "Obecny na wizji domu murowanego")
add_occ("Petrykowski", "Antoni", "Kraśnik", "Burmistrz kraśnicki", None, 537, 1757, "Antoni Petrykowski Bur. Kras.", "Obecny na wizji domu murowanego")
add_occ("Pilaszkiewicz", "Antoni", "Kraśnik", "Sławetny / Członek komisji wizyjnej", None, 537, 1757, "Antoni Pilaszkiewicz", "Obecny na wizji domu murowanego")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 537, 1757, "Szymon Krzeszowski Ław. Kras.", "Obecny na wizji domu murowanego")
add_occ("Brzyski", "Stanisław", "Kraśnik", "Burmistrz i pisarz kraśnicki", None, 537, 1757, "Stanisław Brzyski Burm. y Pisarz Kras.", "Obecny na wizjach kamienicy i gruntu Mazurkiewicza")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 537, 1757, "Jan Lubartowski Ław. Kras.", "Manifestacja przeciw Marcinowi Morelowi")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat na Trybunał Zamoyski", None, 537, 1757, "Marcin Morel Deputat na Trybunał Zamoyski", "Pozwany w manifestacji Jana Lubartowskiego")
add_occ("Mazurkiewicz", "Antoni", "Kraśnik", "Sławetny / Właściciel gruntu", None, 537, 1757, "Antoni Mazurkiewicz", "Wizja jego gruntu Chmarowiczowskiego po wywróceniu płotu przez mieszkańców Podlesia")
add_occ("Landet", "Adam", "Kraśnik", "Ławnik kraśnicki", None, 537, 1757, "Adam Landet Ław.", "Deputowany z urzędu wójtowskiego na wizję gruntu Mazurkiewicza")

# --- Skan 538 ---
add_occ("Łypa", "Marcin", "Kraśnik", "Mieszkaniec / Powód", None, 538, 1757, "Marcin Łypa", "Wyrok przeciw Maciejowi Szewcowi o kradzież z ogrodu i komory")
add_occ("Szewc", "Maciej", "Kraśnik", "Mieszkaniec / Pozwany", "Szmiek?", 538, 1757, "Maciej Szewc [Szewc / Szmiek?]", "Skazany na 1 grzywnę sądowi i deprekację za czyny żony")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat na Trybunał Zamoyski", None, 538, 1757, "Marcin Morel", "Dylacja z Kazimierzem Młynarskim w sprawie kupna wieprza")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 538, 1757, "Kazimierz Młynarski", "Nakaz stawienia sprzedawcy wieprza")

# --- Skan 539 ---
add_occ("Morel", "Marcin", "Kraśnik", "Deputat na Trybunał Zamoyski", None, 539, 1757, "Marcin Morel Dep. na Sąd Tryb. Zamoy.", "Manifestacja przeciw sądowi oraz remanifestacja sądu przeciw niemu")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 539, 1757, "Kazimierz Młynarski", "Strona w sporze o podkupienie wieprza")

# --- Skan 540 ---
add_occ("Morel", "Marcin", "Kraśnik", "Deputat na Trybunał Zamoyski", None, 540, 1757, "Marcin Morel", "Oskarżony o znieważanie sądu miejskiego zarzutami korupcji")
add_occ("Węgorek", "Jakub", "Kraśnik / Lublin", "Obywatel lubelski (dawniej kraśnicki)", None, 540, 1757, "Jakub Węgorek przedtym Kraśnicki teraz Obywatel Lubelski", "Manifestacja przeciw Adamowi Posuniakowi o publikowanie żony")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin i magister szewski", None, 540, 1757, "Adam Posuniak", "Oskarżony o niesłuszne pretensje i zniesławianie Węgorkowej")

# --- Skan 541 ---
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszkaniec / Ojciec Pawła", None, 541, 1757, "Maciej Fruga", "Manifestacja z synem Pawłem przeciw Nowakom o bezprawny areszt roboty")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Poszkodowany", None, 541, 1757, "Paweł syn Macieja Frugi", "Aresztowano mu robotę u majstra fabryki kościelnej")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Pozwany", None, 541, 1757, "Mikołaj Nowak", "Pozwany za bezprawne aresztowanie roboty Frugi")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat na Trybunał Zamoyski", None, 541, 1757, "Marcin Morel", "Początek wyroku w sprawie o wieprza za 24 złp")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 541, 1757, "Kazimierz Młynarski", "Pozwany w wyroku o wieprza za 24 złp")
add_occ("Szafrański", "Jacek", "Kraśnik", "Sprzedawca wieprza", "Jacek?", 541, 1757, "JmPan Jacek [Jacek / Szafrański?]", "Zeznał w sądzie jako przedawca wieprza za 24 złp")

# --- Skan 542 ---
add_occ("Morel", "Marcin", "Kraśnik", "Deputat na Trybunał Zamoyski", None, 542, 1757, "Marcin Morel", "Skazany na 1 grzywnę sądowi i przeproszenie")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 542, 1757, "Kazimierz Młynarski", "Uznany za prawnego kupca wieprza")
add_occ("Węgorek", "Jakub", "Kraśnik / Lublin", "Obywatel lubelski", None, 542, 1757, "Jakub Węgorek", "Wyrok przeciw Adamowi Posuniakowi o 40 złp (16 złp spłacone)")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin i magister szewski", None, 542, 1757, "Adam Posuniak", "Pozwany bez dokumentu w sprawie 40 złp")

# --- Skan 543 ---
add_occ("Węgorek", "Jakub", "Kraśnik / Lublin", "Obywatel lubelski", None, 543, 1757, "Jakub Węgorek", "Zakończenie wyroku z Posuniakiem i areszt na grunt Zdyba")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin i magister szewski", None, 543, 1757, "Adam Posuniak", "Skazany na 1 grzywnę aktorowi i 2 sądowi; apelacja do JW Pana")
add_occ("Habusz", "Starozakonny", "Kraśnik", "Obywatel starozakonny", None, 543, 1757, "Starozakonny Habusz", "Dylacja z Grzegorzem Kołodziejem")
add_occ("Kołodziej", "Grzegorz", "Kraśnik", "Mieszkaniec / Pozwany", None, 543, 1757, "Grzegorz Kołodziej", "Dylacja z Habuszem na porachunek")
add_occ("Zdyb", "Bartłomiej", "Kraśnik", "Mieszczanin / Właściciel gruntu", None, 543, 1757, "Bartłomiej Zdyb", "Areszt na jego gruncie przed pretensjami Posuniaka")
add_occ("Węgorkowa", "Jakubowa", "Kraśnik", "Córka Bartłomieja Zdyba", None, 543, 1757, "Jakubowa Węgorkowa", "Instancja o areszt na grunt; wspomniana jako siostra żony Latosiewicza")
add_occ("Chlebowski", "Jan", "Sandomierz", "Przybysz z Sandomierza / Sprawca zranienia", None, 543, 1757, "Jan Chlebowski z Sandomierza", "Notatka z 14 V 1757 r.: uciął palec w ręce Bartłomiejowi z Budzynia")
add_occ("Bartłomiej", "Z Budzynia", "Budzyń", "Przedmieszczanin / Poszkodowany", None, 543, 1757, "Bartłomiej z Budzynia", "Poszkodowany ucięciem palca przez Jana Chlebowskiego")

# --- Skan 544 ---
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 544, 1756, "Józef Gąska Przedmieszczanin kraśnicki", "Manifestacja przeciw braciom Wilczyńskim o przeoranie miedzy")
add_occ("Wilczyński", "Antoni", "Kraśnik", "Mieszkaniec / Pozwany", None, 544, 1756, "Antoni Wilczyński", "Oskarżony o przeoranie miedzy i zabranie palów")
add_occ("Wilczyński", "Matyasz", "Kraśnik", "Mieszkaniec / Pozwany", None, 544, 1756, "Matyasz Wilczyński", "Oskarżony wraz z bratem Antonim o przeoranie miedzy")
add_occ("Latosiewicz", "Jakub", "Kraśnik", "Obywatel kraśnicki / Kominiarz generalny", None, 544, 1756, "Jakub Latosiewicz obywatel kraśnicki", "Powołany przez urząd miejski i synagogę na generalnego kominiarza")

# --- Skan 545 ---
add_occ("Latosiewicz", "Jakub", "Kraśnik", "Obywatel kraśnicki / Kominiarz generalny", None, 545, 1756, "Jakub Latosiewicz (+)", "Zapis o pensji tygodniowej od kominów i obowiązku wobec kahału")
add_occ("Catowic", "Gierszon", "Kraśnik", "Obywatel starozakonny", None, 545, 1756, "Starozakonny Gierszon Catowic obywatel kraśnicki", "Pożar sadzy w kominie jego domu, rewizja ławników")
add_occ("Pośrybawczowa", "Sztenzla", "Kraśnik", "Komornica starozakonna", "Pośrybawczowa?", 545, 1756, "komornica Sztenzla Pośrybawczowa [Pośrybawczowa?]", "Od jej komina zajął się ogień w domu Gierszona Catowica")

# --- Skan 546 ---
add_occ("Catowic", "Gierszon", "Kraśnik", "Obywatel starozakonny", None, 546, 1756, "Gierszon Catowic", "Dokończenie rewizji pożaru sadzy i słomy w kominie")
add_occ("Osypowiczowa", "Krengla", "Kraśnik", "Starozakonna / Mieszkanka", None, 546, 1756, "starozakonna Krengla Osypowiczowa", "Zuchwale spierała się z deputowanymi urzędnikami przy rewizji komina")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 546, 1756, "Jan Lubartowski", "Deputowany ławnik na rewizji ogniowej")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 546, 1756, "Szymon Krzeszowski Ławnik kras.", "Na rewizji ogniowej oraz manifestacja przeciw Kazimierzowi Młynarskiemu")
add_occ("Zadel", "Adam", "Kraśnik", "Sławetny / Członek komisji rewizyjnej", None, 546, 1756, "Adam Zadel", "Deputowany na rewizji ogniowej u Catowica")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 546, 1756, "Kazimierz Młynarski cechmistrz kunsztu szewskiego", "Oskarżony o znieważenie ławnika Krzeszowskiego w izbie sądowej")

# --- Skan 547 ---
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 547, 1756, "Szymon Krzeszowski", "Zakończenie manifestacji przeciw Młynarskiemu")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 547, 1756, "Kazimierz Młynarski", "Zakończenie manifestacji Krzeszowskiego")
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Ślusarz / Mieszczanin", None, 547, 1756, "Jakub Wojciechowski ślusarz", "Aktor przeciw Szymonowi Bieleckiemu o zrujnowanie płotu")
add_occ("Bielecki", "Szymon", "Kraśnik", "Mieszczanin / Właściciel gruntu", None, 547, 1756, "Szymon Bielecki", "Pozwany o przywłaszczenie kawałka gruntu")
add_occ("Jańczyk", "Stanisław", "Kraśnik", "Poprzedni właściciel gruntu", None, 547, 1756, "Stanisław Jańczyk", "Świadek potwierdzający granice na korzyść Wojciechowskiego")

# --- Skan 548 ---
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Ślusarz / Mieszczanin", None, 548, 1756, "Jakub Wojciechowski", "Wyrok przyznający mu 4 złp kosztów i deprekację od Bieleckiego")
add_occ("Bielecki", "Szymon", "Kraśnik", "Mieszczanin / Właściciel gruntu", None, 548, 1756, "Szymon Bielecki", "Skazany na 4 złp kosztów, 3 grzywny sądowi i deprekację")
add_occ("Trzciński", "Antoni", "Kraśnik", "Mieszkaniec / Strona w sporze spadkowym", None, 548, 1756, "Antoni Trzciński", "Wyrok z Grabowskim przeciw Kofeckiemu o ćwierć gruntu po babce")
add_occ("Grabowski", "Tomasz", "Kraśnik", "Mieszkaniec / Strona w sporze spadkowym", None, 548, 1756, "Tomasz Grabowski", "Wyrok przeciw Krzysztofowi Kofeckiemu o sukcesję")
add_occ("Kofecki", "Krzysztof", "Kraśnik", "Mieszkaniec / Strona w sporze spadkowym", None, 548, 1756, "Krzysztof Kofecki", "Zobowiązany do spłaty sukcesji po babce")

# --- Skan 549 ---
add_occ("Trzciński", "Antoni", "Kraśnik", "Mieszkaniec / Strona w sporze spadkowym", None, 549, 1756, "Antoni Trzciński", "Zakończenie wyroku (15 złp i 2 złp na mszę)")
add_occ("Grabowski", "Tomasz", "Kraśnik", "Mieszkaniec / Strona w sporze spadkowym", None, 549, 1756, "Tomasz Grabowski", "Zakończenie wyroku z Kofeckim")
add_occ("Kofecki", "Krzysztof", "Kraśnik", "Mieszkaniec / Strona w sporze spadkowym", None, 549, 1756, "Krzysztof Kofecki", "Zakończenie wyroku o 15 złp i 2 złp na mszę")
add_occ("Okoń", "Antoni", "Kraśnik", "Sławetny / Mieszczanin", None, 549, 1756, "Antoni Okoń", "Kondescensja na jego grunt z wbiciem palów")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Ojciec Józefa", None, 549, 1756, "Mikołaj Nowak", "Manifestacja w imieniu swoim i syna Józefa przeciw Maciejowi Frugie")
add_occ("Nowak", "Józef", "Kraśnik", "Mieszczanin / Syn Mikołaja", None, 549, 1756, "Józef syn Mikołaja Nowaka", "Współpowód w manifestacji przeciw Maciejowi Frugie")
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszkaniec / Pozwany", None, 549, 1756, "Maciej Fruga", "Oskarżony o przewlekanie sprawy i niestawianie świadków")

# --- Skan 550 ---
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 550, 1756, "Józef Gąska Przedmieszczanin Kraś.", "Kondescensja przeciw Antoniemu Wilczyńskiemu o przeoranie 3 zagonów i wrota")
add_occ("Wilczyński", "Antoni", "Kraśnik", "Mieszkaniec / Pozwany", None, 550, 1756, "Antoni Wilczyński", "Oskarżony o przeoranie gruntu i zabranie wrót")

# Weryfikacja braku duplikatów (Wariant 2)
keys = [(p['nazwisko'], p['imie'], p['miejsce']) for p in gen_data]
assert len(keys) == len(set(keys)), "DUPLICATE IDENTITY DETECTED!"
for p in gen_data:
    assert p.get('funkcja'), f"EMPTY ROLE: {p}"

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part22.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part22.json ({len(gen_data)} profiles) and CSV exported.")
