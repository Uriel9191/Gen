# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part23.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w Partii 24 (skany 576–600) Jednostki 17 (sygn. 35/40/0/1/17) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 576 ---
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Mieszczanin / Świadek", None, 576, 1757, "Casimirus Młynarski", "Świadek w inkwizycji Przesławskiego przeciw Potokowiczom")
add_occ("Przesławski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 576, 1757, "Jan Przesławski", "Powód w inkwizycji przeciw Potokowiczom")
add_occ("Potokowiczowa", "Piotrowa", "Kraśnik", "Żona Piotra Potokowicza", None, 576, 1757, "Piotrowa Potokowiczowa", "Oskarżona o napaść i obelgę (sprawa o paciorki)")
add_occ("Nowacki", "Szymon", "Kraśnik", "Garbarz / Świadek", None, 576, 1757, "Simon Nowacki", "Garbował skóry u Jana Przesławskiego; świadek zajścia")
add_occ("Potokowicz", "Piotr", "Kraśnik", "Mieszkaniec / Pozwany", None, 576, 1757, "Piotr Potokowicz", "Wspomniany jako ojciec uczestnika zajścia")

# --- Skan 577 ---
add_occ("Przesławski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 577, 1757, "Joannes Przesławski", "Inkwizycja przeciw Haimowi Janklowiczowi; pozwany przez Haimową Janklowiczową")
add_occ("Janklowicz", "Haim", "Kraśnik", "Starozakonny / Kupiec skór", None, 577, 1757, "Infidelis Haim Janklowicz", "Sprzedał skórę za 7 złp 15 gr żonie Szymona Nowackiego")
add_occ("Nowacki", "Szymon", "Kraśnik", "Garbarz / Świadek", None, 577, 1757, "Simon Nowacki", "Świadek w sprawie o skórę po 7 złp 15 gr (zapłata 6 złp)")
add_occ("Janklowiczowa", "Haimowa", "Kraśnik", "Niewierna / Handlarka", None, 577, 1757, "Niewierna Haimowa Janklowiczowa", "Aktorka przeciw Janowi Przesławskiemu o dopłatę za skórę")

# --- Skan 578 ---
add_occ("Przesławski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 578, 1757, "Jan Przesławski", "Nakaz dopłaty 1 złp 25 gr + 3 grzywien; manifestacja przeciw Potokowiczowi")
add_occ("Gąska", "Józef", "Kraśnik", "Przedmieszczanin kraśnicki", None, 578, 1757, "Jozef Gąska", "Manifestacja przeciw Maciejowi Wilczyńskiemu o niestawiennictwo")
add_occ("Wilczyński", "Maciej", "Kraśnik", "Mieszkaniec / Pozwany", None, 578, 1757, "Maciey Wilczyński", "Pozwany o dług, nie stawił się na termin")
add_occ("Potokowicz", "Piotr", "Kraśnik", "Mieszczanin kraśnicki", None, 578, 1757, "Piotr Potokowicz mieszczanin kras.", "Pozwany wraz z żoną w manifestacji Przesławskiego")

# --- Skan 579 ---
add_occ("Habuś", "Starozakonny", "Kraśnik", "Niewierny / Wierzyciel", None, 579, 1757, "Starozakonny Habuś", "Aktor w wyroku przeciw Grzegorzowi Wolaczkowi")
add_occ("Wolaczek", "Grzegorz", "Kraśnik", "Mieszkaniec / Pozwany", None, 579, 1757, "Grzegorz Wolaczek", "Nakaz uspokojenia Habusia pod grzywnami 3")
add_occ("Matuszkiewicz", "Michał", "Kraśnik", "Mieszkaniec / Poszkodowany", None, 579, 1757, "Michał Matuszkiewicz", "Szkoda w życie i jęczmieniu (2 korce żyta, pół korca jęczmienia)")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik przysięgły", None, 579, 1757, "Jan Lubartowski Ławnik Przysięgły", "Deputowany do wizji szkody w zbożu Matuszkiewicza")
add_occ("Pilaszkiewicz", "Antoni", "Kraśnik", "Ławnik przysięgły", None, 579, 1757, "Antoni Pilaszkiewicz Ławnik Przysięgły", "Deputowany do wizji szkody w zbożu Matuszkiewicza")
add_occ("Piasecki", "Augustyn", "Przedmieście Kraśnickie", "Przedmieszczanin / Właściciel bydła", None, 579, 1757, "Augustyn Piasecki", "Jego bydło rogate wyrządziło szkodę u Matuszkiewicza")

# --- Skan 580 ---
add_occ("Krzywiński", "Michał", "Kraśnik", "Wójt kraśnicki", None, 580, 1757, "Michał Krzywiński Woyt Krasnicki", "Manifestacja przeciw burmistrzowi Krzeszowskiemu o zarzut wyrywania kart")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Burmistrz kraśnicki", None, 580, 1757, "Łukasz Krzeszowski Burmistrz Krasnicki", "Pozwany przez wójta Krzywińskiego o zniesławienie i wydanie cyrografu")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat miejski", None, 580, 1757, "Marcin Morel Deputat", "Wspomniany w zarzucie sprzedaży kart z protokołów")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Burmistrz kraśnicki", None, 580, 1757, "Stanisław Bryśkiewicz Burmistrz Krasnicki", "Zadosyćuczynienie i kwitacja z Michałem Stachowiczem")
add_occ("Stachowicz", "Michał", "Kraśnik", "Poddany OO. Franciszkanów", None, 580, 1757, "Michał Stachowicz (+)", "Kwitacja z burmistrzem Bryśkiewiczem (podpis krzyżem)")
add_occ("Pietrowski", "Jerzy", "Lubelskie / Kraśnik", "Chorąży lubelski / Posesor", None, 580, 1757, "WJP Chorąży Lubelski Jerzy Pietrowski", "Posesor z [Karpholu? / Karczmisk?], w którego posesji był Stachowicz")

# --- Skan 581 ---
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Burmistrz i pisarz przysięgły kraśnicki", None, 581, 1757, "Stanisław Bryśkiewicz Burmistrz y Pisarz Przysięgły Kras.", "Manifestacja przeciw Janowi Lubartowskiemu i jego żonie o zniesławienie")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik przysięgły", None, 581, 1757, "Jan Lubartowski Ławnik Przysięgły", "Oskarżony wraz z żoną o 3-letnie zniesławianie żony Bryśkiewicza i najście")

# --- Skan 582 ---
add_occ("Krzywiński", "Michał", "Kraśnik", "Wójt kraśnicki", None, 582, 1757, "Michał Krzywiński Woyt Krasnicki", "Manifestacja o odmowę przyjęcia spłaty długu na ratuszu przez Kofeckiego")
add_occ("Kofecki", "Jędrzej", "Kraśnik", "Szlachetny / Wierzyciel", None, 582, 1757, "JP Jędrzey Kofecki", "Odmówił przyjęcia sumy na ratuszu; areszt na jego pieniądzach")
add_occ("Lubkowska", "Stara", "Kraśnik", "Wierzycielka / Mieszkanka", "Stara Lubkowska? / Starostkowa?", 582, 1757, "[Stara Lubkowska? / Starostkowa?]", "Założyła areszt na pieniądzach JP Jędrzeja Kofeckiego u wójta")

# --- Skan 583 ---
add_occ("Kofecki", "Samuel", "Kraśnik", "Urodzony / Wierzyciel", None, 583, 1757, "Urodzony Samuel Kofecki", "Oblatował skrypt brata Andrzeja na 158 złp 12 gr; założył areszt na Tyrawczyźnie")
add_occ("Kofecki", "Jędrzej", "Kraśnik", "Urodzony / Dłużnik", "Andrzej Kofecki", 583, 1756, "Andrzey Kofecki mp. / Urodzony Jędrzey Kofecki", "Wystawca skryptu dłużnego na 158 złp 12 gr (17 VI 1756) + 23 gr za wóz")
add_occ("Marszałkowski", "Szymon", "Kraśnik", "Mieszkaniec / Posesor niwy", None, 583, 1757, "Szymon Marszałkowski", "Niwa od niego trzymana przez Jędrzeja Kofeckiego objęta aresztem")

# --- Skan 584 ---
add_occ("Kofecki", "Samuel", "Kraśnik", "Urodzony / Wierzyciel", None, 584, 1757, "Urodzony Samuel Kofecki", "Dokończenie aresztu na 158 złp 12 gr przeciw bratu")
add_occ("Kofecki", "Jędrzej", "Kraśnik", "Urodzony / Dłużnik", None, 584, 1757, "Urodzony Jędrzey Kofecki / P. Kofecki", "Dłużnik brata Samuela oraz Gierszona Catowica (4 złp)")
add_occ("Catowic", "Gierszon", "Kraśnik", "Starozakonny / Wierzyciel", None, 584, 1757, "Starozakonny Gierszon Catowic", "Założył areszt na 4 złp u Pana Kofeckiego")

# --- Skan 585 ---
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszkaniec / Powód", None, 585, 1757, "Nicolaus Nowak", "Inkwizycja przeciw Antoniemu Pawłowskiemu")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Mieszkaniec / Pozwany", None, 585, 1757, "Antonius Pawłowski", "Oskarżony o uderzenie Józefa Nowaka i rozdarcie kontusza")
add_occ("Łypa", "Jan", "Kraśnik", "Mieszkaniec / Świadek", None, 585, 1757, "Joannes Łypa", "Świadek w inkwizycji Nowaka przeciw Pawłowskiemu")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Uczestnik zajścia", None, 585, 1757, "Paweł Fruga", "Uczestnik bójki z Nowakiem i Pawłowskim")
add_occ("Nowak", "Józef", "Kraśnik", "Mieszkaniec / Uczestnik zajścia", None, 585, 1757, "Jozef Nowak", "Uderzony przez Antoniego Pawłowskiego")
add_occ("Łypa", "Antoni", "Kraśnik", "Mieszkaniec / Świadek", None, 585, 1757, "Antoni Łypa", "Widział zajście z cymbalikiem i rozdarcie kontusza")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Burmistrz kraśnicki", None, 585, 1757, "Łukasz Krzeszowski Burmistrz Kras.", "Manifestacja przeciw Przesławskiemu i Ćwiekowi o pomówienie o pożyczkę 10 złp na wesele")
add_occ("Ćwiek", "Wojciech", "Kraśnik", "Przedmieszczanin kraśnicki", "Ćwiekowa? / Ćwieko?", 585, 1757, "Woyciech Ćwiek", "Pozwany w manifestacji burmistrza Krzeszowskiego")
add_occ("Ćwiek", "Kazimierz", "Kraśnik", "Karczmarz", "Karczmierz Ćwieka", 585, 1757, "Karczmierz Ćwieka", "Wspomniany przy pomówieniu o pożyczkę 10 złp")

# --- Skan 586 ---
add_occ("Lewkowicz", "Mosiek", "Kraśnik", "Starozakonny / Powód", "Mosiek", 586, 1757, "Starozakonny Mosiek Lewkowicz", "Spór z Czubrowskim i Posuniakiem o 3 korce wapna po 4 złp (12 złp)")
add_occ("Czubrowski", "Franciszek", "Kraśnik", "Uczciwy / Pozwany", None, 586, 1757, "Franciszak Czubrowski", "Pozwany o dostawę wapna (niegaszone vs gaszone), grzywna sądowa 1")
add_occ("Posuniak", "Adam", "Kraśnik", "Uczciwy / Pozwany", None, 586, 1757, "Adam Posuniak", "Pozwany wraz z Czubrowskim przez Mośka Lewkowicza o wapno")

# --- Skan 587 ---
add_occ("Marakiewicz", "Jan Antoni", "Kraśnik", "Sławetny / Strona ugody", "Antoni Marakiewicz", 587, 1757, "Sławetny Jan Antoni Marakiewicz", "Ugoda z Marcinową Ćwiekową o 9 złp (odebrał 4 złp, reszta synowcowi)")
add_occ("Ćwiekowa", "Marcinowa", "Kraśnik", "Wdowa", "Ćwiekowa?", 587, 1757, "Marcinowa Ćwiekowa wdowa", "Ugoda z Janem Antonim Marakiewiczem o 9 złp za wieprza i kury")
add_occ("Mosiek", "Starozakonny", "Kraśnik", "Niewierny / Powód", None, 587, 1757, "Infidelis Mosiek", "Inkwizycja przeciw Czubrowskiemu i Posuniakowi o wapno")
add_occ("Czubrowski", "Franciszek", "Kraśnik", "Uczciwy / Pozwany", None, 587, 1757, "Franciscus Czubrowski", "Pozwany w inkwizycji Mośka o wapno")
add_occ("Posuniak", "Adam", "Kraśnik", "Uczciwy / Pozwany", None, 587, 1757, "Adamus Posuniak", "Pozwany w inkwizycji Mośka o wapno")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 587, 1757, "Stanislaus Bryśkiewicz Consul Cras.", "Świadek przysięgły z urzędu przy zgodzie o wapno")

# --- Skan 588 ---
add_occ("Pawłowski", "Antoni", "Kraśnik", "Uczciwy / Aktor i pozwany", None, 588, 1757, "Antoni Pawłowski", "Wyrok przeciw Nowakom (4 grzywny za pobicie); wyrok z Krzeszowskim o gęsię")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Uczciwy / Pozwany", None, 588, 1757, "Mikołay Nowak", "Skazany z synem na 4 grzywny Pawłowskiemu i 2 sądowi; powód w inkwizycji")
add_occ("Nowak", "Józef", "Kraśnik", "Mieszkaniec / Pozwany", "Nowaczek", 588, 1757, "Jozef Nowak / Jozef Nowaczek", "Skazany z ojcem na grzywny; uczestnik bójki z Pawłem Frugą")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Uczestnik bójki", None, 588, 1757, "Paweł Fruga", "Bronił go Pawłowski; porwał się za łeb z Nowaczkiem")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 588, 1757, "Sławetny Szymon Krzeszowski Ławnik", "Aktor przeciw Pawłowskiemu o gęsię zjedzone przez świnie")
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Świadek", None, 588, 1757, "Laurentius Tokarz", "Świadek bójki Nowaków z Frugą i Pawłowskim")

# --- Skan 589 ---
add_occ("Maliszewski", "Jakub", "Kraśnik", "Proboszcz kraśnicki (Kanonicy Regularni Lateraneńscy)", None, 589, 1757, "Wielebny X. Jakob Maliszewski Proboszcz Kras.", "Aktor w procesie o 33 korce żyta (202 złp 15 gr, po odliczeniu 176 złp 9 gr)")
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszczanin kraśnicki", None, 589, 1757, "Maciey Fruga Mieszczanin Krasnicki", "Dłużnik Konwentu na 176 złp 9 gr (spłata w 4 ratach)")

# --- Skan 590 ---
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszczanin kraśnicki", None, 590, 1757, "Maciey Fruga", "Harmonogram 4 rat po 44 złp 2 gr (1757–1759) oraz rozliczenie pracy w winiarni")
add_occ("Maliszewski", "Jakub", "Kraśnik", "Proboszcz kraśnicki", None, 590, 1757, "Wielmożny Imć X. Proboszcz", "Porachunek z Maciejem Frugą")

# --- Skan 591 ---
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Poszkodowany", None, 591, 1757, "Paweł Fruga", "Obdukcja obrażeń po bójce z Nowakiem i Tokarzem")
add_occ("Nowak", "Józef", "Kraśnik", "Mieszkaniec / Uczestnik bójki", None, 591, 1757, "Jozef Nowak", "Nadskoczył Pawłowi Frudze")
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Uczestnik bójki", None, 591, 1757, "Wawrzyniec Tokarz", "Wspomniany przy obdukcji Frugi")
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszkaniec / Poszkodowany", None, 591, 1757, "Maciey Fruga", "Prezentował siny nos i zadarcia rąk od Mikołaja Nowaka")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszkaniec / Sprawca pobicia", None, 591, 1757, "Mikołay Nowak", "Zdrapał szyję i rozdarł kożuch Maciejowi Frudze")
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Mieszkaniec / Właściciel sadu", None, 591, 1757, "Jakub Woyciechowski", "Wizja szkody w sadzie i płocie (wyceniona na 4–8 złp)")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 591, 1757, "Szymon Krzeszowski Ławnik", "Deputowany do wizji gruntu Jakuba Wojciechowskiego")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki", None, 591, 1757, "Franciszek Barankiewicz Ławnik", "Deputowany do wizji gruntu Jakuba Wojciechowskiego")
add_occ("Szelichowski", "Szymon", "Kraśnik", "Sąsiad / Sprawca szkody", None, 591, 1757, "Szymon Szelichowski", "Nie zagrodził płotu, przez co świnia weszła w sad Wojciechowskiego")
add_occ("Trojczak", "Antoni", "Kraśnik", "Mieszkaniec / Powód", "Troyczak", 591, 1757, "Antonius Troyczak / Antek Troyczak", "Inkwizycja o sukcesję gruntów po dziadzie Rusaka")
add_occ("Ćwiek", "Jan", "Kraśnik", "Mieszkaniec / Świadek", "Ćwieka", 591, 1757, "Joannes Ćwieka", "Świadek w sprawie spadkowej Trojczaka i Rusaka")
add_occ("Rusak", "Krzysztof", "Kraśnik", "Mieszkaniec / Pozwany", None, 591, 1757, "Krzysztof Rusak", "Współspadkobierca spornych gruntów")
add_occ("Trojczak", "Tomasz", "Kraśnik", "Mieszkaniec / Krewny", None, 591, 1757, "Tomasz Trojczak", "Wspomniany w genealogii sukcesji po dziadzie")

# --- Skan 592 ---
add_occ("Rusak", "Krzysztof", "Kraśnik", "Mieszkaniec / Pozwany", None, 592, 1757, "Krzysztof Rusak", "Dalszy ciąg sporu o grunty i woły po dziadku Trojczakowej")
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszkaniec / Powód", None, 592, 1757, "Mathias Fruga", "Inkwizycja przeciw Józefowi Nowakowi")
add_occ("Nowak", "Józef", "Kraśnik", "Mieszkaniec / Pozwany", None, 592, 1757, "Josephus Nowak", "Pozwany w inkwizycji Macieja Frugi; jego żona w interogatoriach Pawła Frugi")
add_occ("Worogrodzki", "Szymon", "Zamość", "Mieszkaniec Zamościa / Świadek", None, 592, 1757, "Simon Worogrodzki Incola Zamoyscensis", "Świadek zajścia w gospodzie i bójki Pawła Frugi")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Zeznający", None, 592, 1757, "Paulus Fruga", "Zeznania (interrogatoria) przeciw żonie Józefa Nowaka")

# --- Skan 593 ---
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Uczciwy / Pozwany", None, 593, 1752, "Kazimierz Młynarski", "Pozwany o podkupienie wieprza stargowanego za 24 złp przez Marcina Morela")
add_occ("Wstruskiowski", "Franciszek", "Kraśnik", "Mieszkaniec / Sprzedawca", "Wstruskiowy", 593, 1752, "Franciszek Wstruskiowski", "Sprzedał wieprza za 24 złp u Chłopowej Struskiej")
add_occ("Wojciechowski", "Wojciech", "Kraśnik", "Uczciwy / Świadek", "Woyciechowski", 593, 1752, "Adalbertus Woyciechowski", "Świadek targu za wieprza za 24 złp")
add_occ("Morel", "Marcin", "Kraśnik", "Sławetny / Kupiec", None, 593, 1752, "Marcin Morel", "Stargował wieprza za 24 złp")
add_occ("Struska", "Chłopowa", "Kraśnik", "Gospodyni / Właścicielka podsienia", None, 593, 1752, "Chłopowa Struska", "Na jej podsieniu odbył się targ za wieprza")
add_occ("Elbiszowski", "Jan", "Kraśnik", "Mieszkaniec / Wystawca asekuracji", None, 593, 1757, "Jan Elbiszowski", "Asekuracja z 1757 r. (czerwony złoty na św. Annę)")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Poszkodowany", None, 593, 1752, "Paweł Fruga", "Obdukcja obrażeń z 1752 r. (zdrapania pod okiem i w uchu)")

# --- Skan 594 ---
add_occ("Pawłowski", "Antoni", "Kraśnik", "Mieszkaniec / Uczestnik zajścia", None, 594, 1752, "Pawłowski", "Bronił Frugi; Mikołaj Nowak podarł na nim kontusz")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Uczestnik zajścia", None, 594, 1752, "Paweł Fruga", "Uciekł do Tymcha przed Nowakiem i Tokarzem; tańcował z żoną Józefa Nowaka")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszkaniec / Sprawca", None, 594, 1752, "Mikołay Nowak", "Szarpał Pawłowskiego i gonił Frugę")
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Uczestnik pogoni", None, 594, 1752, "Wawrzyniec Tokarz", "Gonił Frugę do Tymcha")
add_occ("Bieniawski", "Wojciech", "Kraśnik", "Uczciwy / Świadek", None, 594, 1752, "Adalbertus Bieniawski", "Drugi świadek zajścia między Nowakiem a Pawłowskim")
add_occ("Potokowiczowa", "Krystyna", "Kraśnik", "Uczciwa wdowa / Świadek", None, 594, 1752, "Christina Potokowiczowa Vidua", "Świadek w sprawie Pawła Frugi przeciw Nowakom")
add_occ("Nowakowa", "Józefowa", "Kraśnik", "Żona Józefa Nowaka", None, 594, 1752, "żona Jozefa Nowaka", "Tańcowała z Pawłem Frugą")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat na Trybunał Zamoyski w Rzeszowie", None, 594, 1752, "Marcin Morel Deputat na Rzeszów Trybunału Zamoyskiego", "Upraszał o areszt na wieprza (24 złp) u Kazimierza Młynarskiego")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Mieszkaniec / Pozwany", None, 594, 1752, "Kazimierz Młynarski", "Areszt na wieprza u niego przez urząd położony")

# --- Skan 595 ---
add_occ("Łapina", "Małgorzata", "Kraśnik", "Świadek (żona Mateusza Łapy)", None, 595, 1752, "Małgorzata Łapina", "Drugi świadek potwierdzający zeznanie męża")
add_occ("Starobratowa", "Marianna", "Kraśnik", "Świadek", None, 595, 1752, "Maryanna Starobratowa", "Trzeci świadek tańca Pawła Frugi z żoną Józefa Nowaka")
add_occ("Furman", "Józef", "Kraśnik", "Mieszkaniec / Uczestnik zabawy", None, 595, 1752, "Jozef Furman", "Zapraszał na wódkę w gospodzie")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Poszkodowany", None, 595, 1752, "Paweł Fruga", "Tańcował z żoną Józefa Nowaka, potem pobity na dworze")
add_occ("Nowakowa", "Józefowa", "Kraśnik", "Żona Józefa Nowaka", None, 595, 1752, "żona Jozefa Nowaka", "Uczestniczka tańca w gospodzie")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Uczciwy / Świadek", None, 595, 1752, "Franciscus Barankiewicz", "Świadek pobicia Pawła Frugi przez Tokarza i Nowaków")
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Sprawca pobicia", None, 595, 1752, "Wawrzyniec Tokarz", "Najbardziej bił Pawła Frugę po zaułku")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszkaniec / Sprawca pobicia", None, 595, 1752, "Mikołay Nowak", "Uczestnik bójki; zadrapnął Frugę")
add_occ("Nowak", "Wojciech", "Kraśnik", "Mieszkaniec / Uczestnik bójki", None, 595, 1752, "Woyciech Nowak", "Obecny przy bójce w zaułku")
add_occ("Żołądź", "Bartek", "Kraśnik", "Mieszkaniec / Uczestnik bójki", None, 595, 1752, "Bartek Żołądź", "Obecny przy bójce w zaułku")
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszkaniec / Ojciec Pawła", None, 595, 1752, "Maciey Fruga", "Przybiegł bronić syna Pawła")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Mieszkaniec / Powód", None, 595, 1752, "Antonius Pawłowski", "Inkwizycja przeciw Nowakom")
add_occ("Nowacki", "Szymon", "Kraśnik", "Uczciwy / Świadek", None, 595, 1752, "Simon Nowacki", "Świadek w sprawie Pawłowskiego przeciw Nowakom")
add_occ("Nowak", "Józef", "Kraśnik", "Mieszkaniec / Pozwany", None, 595, 1752, "Jozef Nowak", "Chciał wziąć za łeb Frugę w odzieży żołnierskiej")

# --- Skan 596 ---
add_occ("Morel", "Marcin", "Kraśnik", "Sławetny / Manifestant", None, 596, 1752, "Marcin Morel", "Manifestacja przeciw Kazimierzowi Młynarskiemu o wieprza za 24 złp (dublet wpisu)")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Uczciwy / Pozwany", None, 596, 1752, "Kazimierz Młynarski", "Pozwany o podkupienie wieprza")
add_occ("Wstruskiowski", "Franciszek", "Kraśnik", "Mieszkaniec / Sprzedawca", "Wstruskiowy", 596, 1752, "Franciszek Wstruskiowski", "Sprzedawca wieprza za 24 złp")
add_occ("Wojciechowski", "Wojciech", "Kraśnik", "Uczciwy / Świadek", "Woyciechowski", 596, 1752, "Adalbertus Woyciechowski", "Świadek targu za wieprza")
add_occ("Elbiszowski", "Jan", "Kraśnik", "Mieszkaniec / Wystawca asekuracji", None, 596, 1757, "Jan Elbiszowski", "Asekuracja na św. Annę 1757 r.")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Poszkodowany", None, 596, 1752, "Paweł Fruga", "Obdukcja obrażeń z 1752 r.")

# --- Skan 597 ---
add_occ("Sadowski", "Nieboszczyk", "Kraśnik", "Zmarły posesor", None, 597, 1752, "nieboszczyk Sadowski", "Grodził górę leżącą pustkami przez 6 lat")
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszkaniec / Powód", None, 597, 1752, "Mathias Fruga", "Inkwizycja przeciw Nowakom; pobity broniąc syna")
add_occ("Szafrański", "Walenty", "Kraśnik", "Uczciwy / Świadek", None, 597, 1752, "Valentinus Szafrański", "Pierwszy świadek w inkwizycji Macieja Frugi")
add_occ("Fruga", "Paweł", "Kraśnik", "Mieszkaniec / Poszkodowany", None, 597, 1752, "Paweł Fruga", "Pobity przez Nowaka i Tokarza, uciekł do cyrulika")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Mieszkaniec / Świadek", None, 597, 1752, "Antoni Pawłowski", "Bronił Pawła Frugi")
add_occ("Nowak", "Józef", "Kraśnik", "Mieszkaniec / Sprawca", None, 597, 1752, "Jozef Nowak", "Uderzył w gębę Pawła Frugę")
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Sprawca", None, 597, 1752, "Wawrzyniec Tokarz", "Porwał Pawła Frugę za łeb")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Mieszkaniec / Świadek", None, 597, 1752, "Franciszek Barankiewicz", "Obronił Frugę")
add_occ("Krzeszowski", "Wojciech", "Kraśnik", "Mieszkaniec / Świadek", None, 597, 1752, "Woyciech Krzeszowski", "Obronił Frugę")
add_occ("Młynarska", "Anna", "Kraśnik", "Uczciwa / Świadek", None, 597, 1752, "Anna Młynarska", "Drugi świadek zajścia między Nowakiem, Tokarzem i Frugą")
add_occ("Łapa", "Mateusz", "Kraśnik", "Uczciwy / Świadek", None, 597, 1752, "Mathaeus Łapa", "Świadek w inkwizycji Józefa Nowaka przeciw Pawłowi Frudze")

# --- Skan 598 ---
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Strona ugody", None, 598, 1752, "Laurentius Tokarz", "Ugoda z Marcinem Budzyńskim; zapłacił 3 złp za płot")
add_occ("Budzyński", "Marcin", "Kraśnik", "Mieszkaniec / Strona ugody", None, 598, 1752, "Marcin Budzyński", "Ugoda z Wawrzyńcem Tokarzem")
add_occ("Sołoniak", "Adam", "Kraśnik", "Uczciwy / Powód", None, 598, 1752, "Adamus Sołoniak", "Inkwizycja przeciw Antoniemu Dudkowi o górę Sowińską i kożuch")
add_occ("Dudek", "Antoni", "Kraśnik", "Mieszkaniec / Pozwany", None, 598, 1752, "Antonius Dudek", "Otrzymał górę Sowińską z urzędu")
add_occ("Żołądź", "Bartłomiej", "Kraśnik", "Uczciwy / Świadek", None, 598, 1752, "Bartholomeus Żołądź", "Pierwszy świadek w sprawie o górę Sowińską")
add_occ("Grzywa", "Michał", "Kraśnik", "Uczciwy / Świadek", None, 598, 1752, "Michael Grzywa", "Drugi świadek (o górze Sowińskiej po ciotce)")
add_occ("Sołoniak", "Michał", "Kraśnik", "Uczciwy / Świadek i brat", None, 598, 1752, "Michael Sołoniak", "Trzeci świadek o pożyczeniu kożucha od Jakuba Kaliski do Żabnowa")
add_occ("Kaliski", "Jakub", "Kraśnik", "Mieszkaniec / Właściciel kożucha", None, 598, 1752, "Jakub Kaliski", "Pożyczył kożucha Adamowi Sołoniakowi do Żabnowa")
add_occ("Fruga", "Maciej", "Kraśnik", "Mieszkaniec / Świadek", None, 598, 1752, "Mathaeus Fruga", "Świadek ze strony Antoniego Dudka")

# --- Skan 599 ---
add_occ("Kowalczyk", "Mieszkaniec", "Kraśnik", "Mieszkaniec / Pozwany", None, 599, 1752, "Kowalczyk", "Odmówił egzekucji z komisji od Pana Starosty")
add_occ("Kowalski", "Kazimierz", "Kraśnik", "Mieszkaniec / Świadek", None, 599, 1752, "Kazmierz Kowalski", "Świadek słów Kowalczyka podczas egzekucji")
add_occ("Dunajski", "Łukasz", "Kraśnik", "Żołnierz skarbowy / Świadek", None, 599, 1752, "Łukasz Dunajski", "Świadek przy egzekucji u Kowalczyka i w sprawie Wolfa Jeszkowica")
add_occ("Trojczak", "Antoni", "Kraśnik", "Mieszkaniec / Powód", "Troyczak", 599, 1752, "Antonius Troyczak", "Inkwizycja przeciw Krzysztofowi Rusakowi o rolę na Podlesiu")
add_occ("Rusak", "Krzysztof", "Kraśnik", "Mieszkaniec / Pozwany", None, 599, 1752, "Christophorus Rusak", "Pozwany o grunty na Podlesiu")
add_occ("Ćwiek", "Jan", "Kraśnik", "Mieszkaniec / Świadek", "Ćwieka", 599, 1752, "Joannes Ćwieka", "Świadek o roli babki Trojczakowej na Podlesiu")
add_occ("Budzyński", "Marcin", "Kraśnik", "Mieszkaniec / Powód", None, 599, 1752, "Martinus Budzyński", "Kupił pole z chałupą za 62 złp od Wawrzyńca Tokarza")
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Mieszkaniec / Sprzedawca", None, 599, 1752, "Laurentius Tokarz", "Sprzedał pole z chałupą za 62 złp Marcinowi Budzyńskiemu")
add_occ("Włoch", "Grzegorz", "Kraśnik", "Mieszkaniec / Świadek", None, 599, 1752, "Gregorius Włoch", "Świadek litkupu za 62 złp")
add_occ("Lubartowski", "Jan", "Kraśnik", "Mieszkaniec / Powód", None, 599, 1752, "Joannes Lubartowski", "Inkwizycja przeciw Marcinowi Morelowi (wyjazd na Wyźnicę po trzcinę)")
add_occ("Morel", "Marcin", "Kraśnik", "Mieszkaniec / Pozwany", None, 599, 1752, "Martinus Morel", "Pozwany w inkwizycji Jana Lubartowskiego")
add_occ("Czubrowski", "Franciszek", "Kraśnik", "Komornik u Lubartowskiego / Świadek", None, 599, 1752, "Franciscus Czubrowski", "Pierwszy świadek wyjazdu na Wyźnicę po trzcinę")
add_occ("Łazik", "Antoni", "Kraśnik", "Parobek Jana Lubartowskiego", None, 599, 1752, "Antoni Łazik parobek", "Wiózł trzcinę z Wyźnicy do domu Lubartowskiego")
add_occ("Wyźnicki", "Staś", "Wyźnica", "Gospodarz w Wyźnicy", None, 599, 1752, "Staś Wyźnicki", "U niego zostali świadkowie w Wyźnicy")
add_occ("Orzeł", "Mikołaj", "Kraśnik", "Parobek u Jana Lubartowskiego / Świadek", None, 599, 1752, "Nicolaus Orzeł parobek", "Drugi świadek służby u Jana Lubartowskiego")
add_occ("Jeszkowic", "Wolf", "Kraśnik", "Niewierny / Powód", None, 599, 1752, "Infidelis Wolf Jeszkowicz", "Inkwizycja przeciw Herszkowicowi o podatek kahalny")
add_occ("Herszkowic", "Tomasz", "Kraśnik", "Niewierny / Pozwany", "Tomasz? / Icko?", 599, 1752, "[Tomasz? / Icko?] Herszkowic", "Pozwany o egzekucję podatku od starszego kahalnego")
add_occ("Kryśkowicz", "Żołnierz Skarbowy", "Kraśnik", "Żołnierz skarbowy / Świadek", None, 599, 1752, "Kryśkowicz Żołnierz Skarbowy", "Świadek w inkwizycji Wolfa Jeszkowica")
add_occ("Kowalski", "Stanisław", "Kraśnik", "Mieszkaniec / Świadek", None, 599, 1752, "Stanisław Kowalski", "Świadek w inkwizycji Wolfa Jeszkowica")

# --- Skan 600 ---
add_occ("Hudrikowska", "Uczciwa", "Kraśnik", "Posiadaczka ćwierci bez sukcesora", None, 600, 1759, "Uczciwa Hudrikowska", "Jej ćwierć bez sukcesora objął Benedyk Kawka")
add_occ("Kawka", "Benedyk", "Kraśnik", "Uczciwy / Posiadacz ćwierci", None, 600, 1759, "Benedyk Kawka", "Zadeklarował trzymanie ćwierci po Hudrikowskiej i ukontentowanie magistratu")
add_occ("Ławicki", "Antoni", "Kraśnik", "Mieszkaniec / Manifestant", None, 600, 1759, "Antoni Ławicki", "Manifestacja przeciw Matyaszowi Szymarczykowi o pobicie matki")
add_occ("Szymarczyk", "Matyasz", "Kraśnik", "Uczciwy / Pozwany", None, 600, 1759, "Matyasz Szymarczyk", "Oskarżony o pobicie matki Antoniego Ławickiego na drodze publicznej")
add_occ("Szubartowski", "Imć Pan", "Kraśnik", "Deputat miejski", None, 600, 1759, "Imć Pan Szubartowski", "Deputowany ze skryptu wraz z Szymonem ławnikiem")

# Weryfikacja braku duplikatów (Wariant 2)
keys = [(p['nazwisko'], p['imie'], p['miejsce']) for p in gen_data]
assert len(keys) == len(set(keys)), "DUPLICATE IDENTITY DETECTED!"
for p in gen_data:
    assert p.get('funkcja'), f"EMPTY ROLE: {p}"

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part24.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part24.json ({len(gen_data)} profiles) and CSV exported.")
