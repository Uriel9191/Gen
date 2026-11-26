# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part25.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w Partii 26 (skany 626–650) Jednostki 17 (sygn. 35/40/0/1/17) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 626 ---
add_occ("Tokarski", "Kazimierz", "Kraśnik", "Urodzony żołnierz artylerii koronnej", None, 626, 1758, "Urodzony Kazimierz Tokarski", "30 lat służby w Regimencie Artylerii Koronnej; proces sukcesyjny po ojcu")
add_occ("Tokarz", "Tomasz", "Kraśnik", "Zmarły ojciec Kazimierza", None, 626, 1758, "Tomasz Tokarz", "Ojciec aktora, po którym pozostał inwentarz")
add_occ("Łypa", "Jan", "Kraśnik", "Uczciwy / Ojczym aktora", None, 626, 1758, "Jan Łypa", "Ojczym Kazimierza Tokarskiego (para wołów za 15 złp)")
add_occ("Jardzyk", "Grzegorz", "Przedmieście Kraśnickie", "Mieszkaniec / Pozwany", None, 626, 1758, "Jardzyk", "Zastał gospodarstwo z bydłem za 20 złp")

# --- Skan 627 ---
add_occ("Jardzyk", "Grzegorz", "Przedmieście Kraśnickie", "Mieszkaniec / Pozwany", None, 627, 1758, "Jardzyk", "Wyposażył dwie pasierbice")
add_occ("Cebula", "Wojciech", "Kraśnik", "Mieszkaniec / Zięć", "Cebeza?", 627, 1758, "Wojciech [Cebula?]", "Mąż starszej pasierbicy")
add_occ("Wilczyński", "Wojciech", "Kraśnik", "Mieszkaniec / Zięć", None, 627, 1758, "Wojciech Wilczyński w Krakowie", "Mąż młodszej pasierbicy")
add_occ("Łypa", "Jan", "Kraśnik", "Uczciwy / Ojczym", None, 627, 1758, "Jan Łypa", "Otrzymał zapis na niwce Piekuta")
add_occ("Ćwiek", "Wojciech", "Kraśnik", "Mieszkaniec / Pozwany", None, 627, 1758, "Wojciech Ćwiek", "Trzyma kwaterę pola po matce")
add_occ("Tokarski", "Kazimierz", "Kraśnik", "Żołnierz artylerii koronnej", None, 627, 1758, "Kazimierz Tokarski", "Przysądzony do kwatery pola wraz z siostrą Ewą")
add_occ("Wykryst", "Wojciech", "Kraśnik", "Mieszkaniec / Szwagier", None, 627, 1758, "Wojciech Wykryst", "Sprzedał z żoną Ewą ćwierć Smokowską Jakubowi Bielickiemu")
add_occ("Bielicki", "Jakub", "Kraśnik", "Mieszkaniec / Nabywca", None, 627, 1758, "Jakub Bielicki", "Kupił ćwierć Smokowską od Wykrysta")
add_occ("Jardzyk", "Jędrzej", "Przedmieście Kraśnickie", "Mieszkaniec / Posiadacz", None, 627, 1758, "Jędrzey Jardzyk", "Okupił grunt Smokowski")
add_occ("Tokarzowa", "Jadwiga", "Kraśnik", "Zmarła dziedziczka", "Jadwiga Smokowska", 627, 1758, "Jadwiga Smokowska", "Dziedziczka ćwierci Smokowskiej")

# --- Skan 628 ---
add_occ("Łypa", "Jan", "Kraśnik", "Uczciwy / Ojczym", None, 628, 1758, "Jan Łypa", "Nakaz oddania 14 złp 10 gr (z 44 złp 10 gr) Kazimierzowi Tokarskiemu")
add_occ("Wojtczak", "Wojciech", "Kraśnik", "Mieszkaniec / Posiadacz pola", "Woytczak", 628, 1758, "Wojciech Wojtczak", "Równy dział pola z Kazimierzem Tokarskim")
add_occ("Tokarski", "Kazimierz", "Kraśnik", "Żołnierz artylerii koronnej", None, 628, 1758, "Kazimierz Tokarski", "Równy dział pola")
add_occ("Kawka", "Mikołaj", "Kraśnik", "Uczciwy / Powód", None, 628, 1758, "Mikołay Kawka", "Proces z Tomaszem Piekarskim o skradzioną spódnicę")
add_occ("Piekarski", "Tomasz", "Kraśnik", "Bednarz / Pozwany", None, 628, 1758, "Tomasz Piekarski Bednarz", "Pozwany przez Mikołaja Kawkę o spódnicę")

# --- Skan 629 ---
add_occ("Kawka", "Mikołaj", "Kraśnik", "Uczciwy / Powód", None, 629, 1758, "Mikołay Kawka", "Koniec wyroku (15 gr / połowa wartości)")
add_occ("Piekarski", "Tomasz", "Kraśnik", "Bednarz / Pozwany", None, 629, 1758, "Tomasz Piekarski", "Skazany na 1 grzywnę sądowi i więzienie na Wyźnicy")
add_occ("Tokarski", "Kazimierz", "Kraśnik", "Urodzony żołnierz artylerii koronnej", None, 629, 1758, "Kazimierz Tokarski (+)", "Donacja na rzecz sióstr przyrodnich (podpis krzyżem)")
add_occ("Jardzykowa", "Marianna", "Kraśnik", "Siostra przyrodnia / Obdarowana", None, 629, 1758, "Marianna Jardzykowa", "Otrzymała donację od brata Kazimierza Tokarskiego")
add_occ("Wykrystowa", "Ewa", "Kraśnik", "Siostra przyrodnia / Obdarowana", None, 629, 1758, "Ewa Wykrystowa", "Otrzymała donację od brata Kazimierza Tokarskiego")
add_occ("Pałka", "Antoni", "Kraśnik", "Przedmieszczanin / Poszkodowany", None, 629, 1758, "Antoni Pałka", "Obdukcja ran głowy i szyi")

# --- Skan 630 (i dublet 631) ---
add_occ("Pałka", "Antoni", "Kraśnik", "Przedmieszczanin / Poszkodowany", None, 630, 1758, "Antoni Pałka", "Oskarżył o pobicie siebie i żony malarza Bieniakowskiego i Tkaczyka")
add_occ("Bieniakowski", "Malarz", "Kraśnik", "Malarz / Sprawca pobicia", None, 630, 1758, "Malarz z Bieniakowskiego", "Oskarżony o pobicie Antoniego Pałki")
add_occ("Tkaczyk", "Czeladnik", "Kraśnik", "Czeladnik tkacki / Sprawca pobicia", None, 630, 1758, "Tkaczyk czeladnik", "Oskarżony o pobicie Antoniego Pałki")
add_occ("Garncarz", "Wawrzyniec", "Kraśnik", "Przedmieszczanin / Poszkodowany", None, 630, 1758, "Wawrzyniec Garncarz", "Obdukcja ran ręki i łopatki przeciw Panu Wornemu")
add_occ("Worny", "Pan", "Kraśnik", "Pozwany o pobicie", "Morny?", 630, 1758, "Pan [Worny? / Morny?]", "Wskazany w obdukcji Wawrzyńca Garncarza")

add_occ("Pałka", "Antoni", "Kraśnik", "Przedmieszczanin / Poszkodowany", None, 631, 1758, "Antoni Pałka", "Dublet mikrofilmowy skanu 630")
add_occ("Garncarz", "Wawrzyniec", "Kraśnik", "Przedmieszczanin / Poszkodowany", None, 631, 1758, "Wawrzyniec Garncarz", "Dublet mikrofilmowy skanu 630")

# --- Skan 632 ---
add_occ("Jardzyk", "Józef", "Kraśnik", "Uczciwy / Strona ugody", None, 632, 1758, "Jozef Jardzyk (+)", "Ugoda z Antonim Pizikiem (14 grzywien wadium, podpis krzyżem)")
add_occ("Pizik", "Antoni", "Kraśnik", "Przedmieszczanin / Strona ugody", None, 632, 1758, "Antoni Pizik (+)", "Ugoda z Józefem Jardzykiem (podpis krzyżem)")
add_occ("Łysiak", "Sebastian", "Zakrzów", "Poddany z Zakrzowa / Manifestant", None, 632, 1758, "Sobestyjan Łysiak", "Manifestacja przeciw Wojciechowi Ćwiekowi i Wojakowi o skradziony kożuch")
add_occ("Ćwiek", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", None, 632, 1758, "Woyciech Ćwiek", "Pozwany przez Sebastiana Łysiaka")
add_occ("Wojak", "Komornik", "Kraśnik", "Komornik Ćwieki", None, 632, 1758, "Wojak komornik", "Odebrał kożuch Łysiakowi na jarmarku")

# --- Skan 633 ---
add_occ("Łysiak", "Sebastian", "Zakrzów", "Poddany z Zakrzowa / Manifestant", None, 633, 1758, "Sobestyjan Łysiak", "Dokończenie manifestacji o kożuch")
add_occ("Rymarczyk", "Marcin", "Kraśnik", "Uczciwy / Powód", None, 633, 1758, "Martinus Rymarczyk", "Inkwizycja przeciw bratu Marcinowi Kotłunkowi o pobicie kijem")
add_occ("Kotłunek", "Marcin", "Kraśnik", "Uczciwy / Pozwany", None, 633, 1758, "Martinus Kotłunek", "Pozwany w inkwizycji Marcina Rymarczyka")
add_occ("Łaska", "Józef", "Kraśnik", "Świadek przysięgły", None, 633, 1758, "Josephus Łaska", "Świadek pobicia Rymarczyka przez Tomasza Kotłunka")
add_occ("Oleckowski", "Józef", "Kraśnik", "Uczciwy / Powód", None, 633, 1758, "Jozef Oleckowski", "Początek procesu przeciw Antoniemu Oleckowskiemu")

# --- Skan 634 ---
add_occ("Oleckowski", "Józef", "Kraśnik", "Uczciwy / Powód", None, 634, 1758, "Jozef Oleckowski", "Proces o pobicie dzieci i szkody")
add_occ("Oleckowski", "Antoni", "Kraśnik", "Uczciwy / Pozwany", None, 634, 1758, "Antoni Oleckowski", "Pozwany o pobicie dzieci pasących bydło")
add_occ("Słomkowska", "Teresa", "Kraśnik", "Uczciwa wdowa", None, 634, 1758, "Teresa Słomkowska wdowa", "Uzyskała prorogację dekretu z Petrykowskim")
add_occ("Łysiak", "Antoni", "Kraśnik", "Uczciwy / Brat Teresy", None, 634, 1758, "Antoni Łysiak", "Wspierał siostrę Teresę Słomkowską przy prorogacji")
add_occ("Petrykowski", "Antoni", "Kraśnik", "Sławetny / Strona", None, 634, 1758, "Antoni Petrykowski", "Strona prorogacji ze Słomkowską")
add_occ("Wróbel", "Jakub", "Kraśnik", "Uczciwy / Pozwany", None, 634, 1758, "Jakub Wróbel", "Kontumacja w sprawie ze starozakonnym Aronem (1 grzywna sądowi)")
add_occ("Aaron", "Arendarz", "Kraśnik", "Starozakonny / Powód", "Aron", 634, 1758, "Starozakonny Aron", "Powód przeciw Jakubowi Wróblowi")

# --- Skan 635 ---
add_occ("Bartnicki", "Ludwik", "Kraśnik", "Towarzysz kunsztu płócienniczego", None, 635, 1758, "Ludwik Bartnicki towarzysz kunsztu płócienniczego", "Obdukcja ran przeciw Antoniemu Pałce")
add_occ("Pałka", "Antoni", "Kraśnik", "Uczciwy / Sprawca pobicia", None, 635, 1758, "Antoni Pałka", "Wskazany w obdukcji Ludwika Bartnickiego")
add_occ("Petrykowski", "Antoni", "Kraśnik", "Sławetny / Strona ugody", None, 635, 1758, "Antoni Petrykowski (+)", "Ugoda z Teresą Słomkowską (14 złp 10 gr, podpis krzyżem)")
add_occ("Marczewski", "Jędrzej", "Kraśnik", "Brat przyrodni / Strona ugody", "Marcewicz", 635, 1758, "Jędrzey Marczewski (+)", "Ugoda z Teresą Słomkowską (podpis krzyżem)")
add_occ("Słomkowska", "Teresa", "Kraśnik", "Uczciwa wdowa / Strona ugody", None, 635, 1758, "Teresa Słomkowska (+)", "Ugoda z Petrykowskim i Marczewskim (podpis krzyżem)")

# --- Skan 636 ---
add_occ("Morel", "Mateusz", "Kraśnik", "Sławetny / Powód", None, 636, 1758, "Mateusz Morel", "Proces przeciw Sebastianowi Piotrowskiemu o zasypywanie trawy")
add_occ("Piotrowski", "Sebastian", "Kraśnik", "Pozwany", None, 636, 1758, "Sebastian Piotrowski", "Pozwany przez Mateusza Morela")
add_occ("Wolak", "Stanisław", "Przedmieście Kraśnickie", "Uczciwy / Nabywca", None, 636, 1758, "Stanisław Wolak", "Intromisja na dwa sznury gruntu przy granicy stypańskiej")
add_occ("Górski", "Józef", "Kraśnik", "Uczciwy / Sąsiad", None, 636, 1758, "Jozef Górski", "Sąsiad przy pierwszym sznurze gruntu")
add_occ("Sroka", "Andrzej", "Kraśnik", "Uczciwy / Sąsiad", None, 636, 1758, "Andrzey [Sroka?]", "Sąsiad przy sznurach gruntu")
add_occ("Kotłunek", "Marcin", "Kraśnik", "Uczciwy / Powód", None, 636, 1758, "Marcin Kotłunek", "Początek procesu przeciw Józefowi Łasce")

# --- Skan 637 ---
add_occ("Kotłunek", "Marcin", "Kraśnik", "Uczciwy / Powód", None, 637, 1758, "Marcin Kotłunek", "Spór z Józefem Łaską o jałówkę")
add_occ("Łaska", "Józef", "Kraśnik", "Uczciwy / Pozwany", None, 637, 1758, "Jozef Łaska", "Pozwany przez Marcina Kotłunka")
add_occ("Kanski", "Stanisław", "Dzierzkowice", "Ks. proboszcz dzierzkowski i wicedziekan urzędowski", None, 637, 1755, "Jegomość X. Pleban Proboszcz Dzierzkowski", "Plenipotencja z 1755 r. dla Jana Lubartowskiego na dług 50 złp po Marszałkowskim")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik i podskarbi kościoła kraśnickiego", None, 637, 1755, "Sławetny Jan Lubartowski Ławnik", "Plenipotent ks. dziekana Kanskiego")
add_occ("Marszałkowski", "Szymon", "Kraśnik", "Dawny wójt i deputat (zmarły)", None, 637, 1755, "Szymon Marszałkowski dawny wójt", "Dłużnik kościoła na 50 złp na ornat ze złotogłowiu")
add_occ("Rycerz", "Wojciech", "Dzierzkowice", "Sołtys dzierzkowski", None, 637, 1755, "Wojciech Rycerz Sołtys Dzierzkowski", "Legował dług na ornat kościelny")

# --- Skan 638 ---
add_occ("Kanski", "Stanisław", "Dzierzkowice", "Ks. proboszcz dzierzkowski", None, 638, 1755, "X. Stanisław Kanski Pleban Dzierzkowski mp.", "Podpis pod plenipotencją na odbiór 32 złp")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik i plenipotent", None, 638, 1755, "Sł. Jan Lubartowski", "Uprawniony do odbioru 32 złp na ornat")
add_occ("Marszałkowski", "Wojciech", "Kraśnik", "Urodzony / Manifestant", None, 638, 1758, "Urodzony Woyciech Marszałkowski", "Manifestacja przy asystencji Dominika Frankiewicza przeciw kredytorom")
add_occ("Frankiewicz", "Dominik", "Kraśnik", "Urodzony wicesgerent / Wuj", None, 638, 1758, "Urodzony P. Dominik Frankiewicz", "Asystował siostrzeńcowi Wojciechowi Marszałkowskiemu")

# --- Skan 639 ---
add_occ("Marszałkowski", "Wojciech", "Kraśnik", "Urodzony / Manifestant", None, 639, 1758, "Woyciech Marszałkowski", "Zakończenie manifestacji przeciw kredytorom")
add_occ("Łaska", "Józef", "Kraśnik", "Uczciwy / Powód", None, 639, 1758, "Jozef Łaska", "Wygrał sprawę o ćwierć roli (17 lat posiadania) przeciw Kotłunkowi")
add_occ("Kotłunek", "Marcin", "Kraśnik", "Uczciwy / Pozwany", None, 639, 1758, "Marcin Kotłunek", "Przegrał roszczenia o ćwierć roli wedle Prawa Magdeburskiego")

# --- Skan 640 ---
add_occ("Łaska", "Józef", "Kraśnik", "Uczciwy / Powód", None, 640, 1758, "Jozef Łaska", "Zobowiązany dać mszę św. za dusze zmarłych")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik i podskarbi kościelny", None, 640, 1758, "Sławetny Jan Lubartowski Ławnik", "Proces przeciw władzom o legat 50 złp Piotra Żyły z Grabówki")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Wójt kraśnicki / Pozwany", None, 640, 1758, "Łukasz Krzeszowski", "Pozwany o legat 50 złp Piotra Żyły")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Burmistrz kraśnicki / Pozwany", None, 640, 1758, "Stanisław Bryśkiewicz Burmistrz", "Pozwany o legat 50 złp Piotra Żyły")
add_occ("Marszałkowski", "Wojciech", "Kraśnik", "Urodzony / Pozwany", None, 640, 1758, "Urodzony Woyciech Marszałkowski", "Pozwany o legat 50 złp Piotra Żyły")
add_occ("Żyła", "Piotr", "Grabówka", "Pracowity / Testator", None, 640, 1758, "Pracowity Piotr Żyła z Grabówki", "Zapisał legat 50 złp")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki / Powód", None, 640, 1758, "Sławetny Franciszek Barankiewicz Ławnik", "Wyrok przeciw Grzegorzowi Jardzykowi o uderzenie (1 grzywna)")
add_occ("Jardzyk", "Grzegorz", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 640, 1758, "Grzegorz Jardzyk", "Skazany na 1 grzywnę aktorowi i 1 sądowi")

# --- Skan 641 ---
add_occ("Petrykowski", "Antoni", "Kraśnik", "Sławetny / Powód", None, 641, 1758, "Antoni Petrykowski", "Odwołanie do świadków przeciw Słomkowskiej; manifestacja przeciw Barankiewiczowi")
add_occ("Marczewski", "Jędrzej", "Kraśnik", "Uczciwy / Współpowód", "Marcewicz", 641, 1758, "Jędrzey Marcewicz", "Współpowód z Antonim Petrykowskim")
add_occ("Słomkowska", "Teresa", "Kraśnik", "Uczciwa wdowa / Pozwana", None, 641, 1758, "Teresa Słomkowska", "Oskarżona o spalenie papierów po Stanisławie Grzymule")
add_occ("Kratkowski", "Bartłomiej", "Kraśnik", "Uczciwy / Ojciec i powód", None, 641, 1758, "Bartłomiey Kratkowski", "Proces z synem Andrzejem Kratkowskim o pretensje")
add_occ("Kratkowski", "Andrzej", "Kraśnik", "Sławetny / Syn i pozwany", None, 641, 1758, "Jędrzey Kratkowski", "Pozwany przez ojca Bartłomieja")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki / Pozwany", None, 641, 1758, "Sławetny Franciszek Barankiewicz Ławnik", "Pozwany w manifestacji Petrykowskiego i Marcewicza")

# --- Skan 642 ---
add_occ("Petrykowski", "Antoni", "Kraśnik", "Sławetny / Manifestant", None, 642, 1758, "Antoni Petrykowski", "Zakończenie manifestacji o kosztach pogrzebu matki (9 gr)")
add_occ("Słomkowski", "Kazimierz", "Kraśnik", "Mieszkaniec", None, 642, 1758, "Kazimierz Słomkowski", "Dał deski i 9 gr na nakrycie śmiertelne")
add_occ("Łaska", "Józef", "Kraśnik", "Uczciwy / Manifestant", None, 642, 1758, "Jozef Łaska", "Manifestacja przeciw Marcinowi Kotłunkowi o wyzwiska")
add_occ("Kotłunek", "Marcin", "Kraśnik", "Uczciwy / Pozwany", None, 642, 1758, "Marcin Kotłunek", "Pozwany przez Józefa Łaskę")
add_occ("Rymarz", "Andrzej", "Kraśnik", "Uczciwy / Świadek", None, 642, 1758, "Andrzey Rymarz", "Świadek w manifestacji Józefa Łaski")
add_occ("Długosz", "Jan", "Stróża", "Pracowity ze Stróży / Manifestant", None, 642, 1758, "Pracowity Jan Długosz ze Stróży", "Manifestacja o pobicie na jarmarku w Kraśniku i zabór sukmany (24 złp)")

# --- Skan 643 ---
add_occ("Kratkowski", "Bartłomiej", "Kraśnik", "Uczciwy / Ojciec", None, 643, 1758, "Bartłomiey Kratkowski (+)", "Wieczna zgoda z synem Andrzejem (2 złp na tydzień, podpis krzyżem)")
add_occ("Kratkowski", "Andrzej", "Kraśnik", "Sławetny / Syn", None, 643, 1758, "Andrzey Kratkowski (+)", "Zobowiązał się płacić ojcu 2 złp tygodniowo (podpis krzyżem)")
add_occ("Rymarz", "Andrzej", "Kraśnik", "Uczciwy / Świadek", None, 643, 1758, "Andrzey Rymarz (+)", "Świadek zgody Kratkowskich (podpis krzyżem)")
add_occ("Łaska", "Józef", "Kraśnik", "Uczciwy / Świadek", None, 643, 1758, "Jozef Łaska (+)", "Świadek zgody Kratkowskich (podpis krzyżem)")
add_occ("Kotłunek", "Marcin", "Kraśnik", "Uczciwy / Świadek", None, 643, 1758, "Marcin Kotłunek (+)", "Świadek zgody Kratkowskich (podpis krzyżem)")

# --- Skan 644 ---
add_occ("Bartnicki", "Ludwik", "Kraśnik", "Towarzysz kunsztu płócienniczego", None, 644, 1758, "Ludwik Bartnicki towarzysz kunsztu płócienniczego", "Manifestacja przeciw Antoniemu Pałce o prowadzenie przez miasto i więzienie")
add_occ("Pałka", "Antoni", "Kraśnik", "Uczciwy / Pozwany", None, 644, 1758, "Antoni Pałka", "Pozwany przez Ludwika Bartnickiego")

# --- Skan 645 ---
add_occ("Bartnicki", "Ludwik", "Kraśnik", "Towarzysz kunsztu płócienniczego", None, 645, 1758, "Ludwik Bartnicki", "Druga manifestacja przeciw Pałce; pozwany w interogatoriach")
add_occ("Pałka", "Antoni", "Kraśnik", "Przedmieszczanin / Powód", None, 645, 1758, "Antonius Pałka", "Interogatoria przeciw Ludwikowi Bartnickiemu")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik przysięgły / Świadek", None, 645, 1758, "Sławetny Jan Lubartowski Ławnik", "Świadek gwałtu w gospodzie")

# --- Skan 646 ---
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik przysięgły / Świadek", None, 646, 1758, "P. Lubartowski", "Rozgromił bijących się w gospodzie")
add_occ("Bartnicki", "Ludwik", "Kraśnik", "Towarzysz tkacki", None, 646, 1758, "Ludwik tkaczyk", "Trzymał Pałkę za włosy w gospodzie")
add_occ("Pałka", "Antoni", "Kraśnik", "Przedmieszczanin / Poszkodowany", None, 646, 1758, "Antoni Pałka", "Pobity w gospodzie; manifestacja przeciw Krzeszowskiemu")

# --- Skan 647 ---
add_occ("Pałka", "Antoni", "Kraśnik", "Przedmieszczanin / Manifestant", None, 647, 1758, "Antoni Pałka", "Manifestacja przeciw burmistrzowi Łukaszowi Krzeszowskiemu")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Burmistrz i cechmistrz płócienniczy", None, 647, 1758, "Łukasz Krzeszowski Burmistrz y Cechmistrz płócienniczy", "Oskarżony o faworyzowanie czeladnika Sierpińskiego")
add_occ("Bartnicki", "Ludwik", "Kraśnik", "Czeladnik płócienniczy", "Sierpiński?", 647, 1758, "Ludwik [Sierpiński?]", "Wspomniany w skardze Pałki")

# --- Skan 648 ---
add_occ("Kubik", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", None, 648, 1758, "Woyciech Kubik Przedmieszczanin Kras.", "Pozwany o koszty w manifestacji")
add_occ("Tokarz", "Antoni", "Kraśnik", "Dawny burmistrz i rajca", "Tokarczyk", 648, 1758, "Sławetny Antoni Tokarczyk dawny burmistrz y rajca", "Wyrok przeciw Mikołajowi Kawce o pobicie wieprzów")
add_occ("Kawka", "Mikołaj", "Kraśnik", "Przedmieszczanin / Pozwany", None, 648, 1758, "Mikołay Kawka przedmieszczanin", "Skazany na 2 grzywny sądowi i taksę za pobicie wieprzów")

# --- Skan 649 ---
add_occ("Kawka", "Mikołaj", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", None, 649, 1758, "Mikołay Kawka", "Apelował do Trybunału Zamoyskiego; pozwany przez Petronelę Sadowską")
add_occ("Sadowska", "Petronela", "Kraśnik", "Pani / Manifestantka", None, 649, 1758, "Pani Petronella Sadowska", "Manifestacja przeciw Mikołajowi Kawce o pobicie na gospodzie")
add_occ("Stanowski", "Jan", "Kraśnik", "Pan / Pełnomocnik", None, 649, 1758, "Pan Jan Stanowski", "Manifestacja w imieniu pryncypała")

# --- Skan 650 ---
add_occ("Stanowski", "Jan", "Kraśnik", "Pan / Pełnomocnik skarbnika", None, 650, 1758, "Pan Jan Stanowski", "Inwestygował konfesaty poddanych z dóbr Sucha")
add_occ("Wybranowski", "Stanisław", "Lubelskie / Sucha", "Skarbnik lubelski", None, 650, 1758, "Jaśnie Wielmożny JMć Pan Stanisław Wybranowski Skarbnik Lubelski", "Pryncypał Jana Stanowskiego w sprawie poddanych z Suchej")
add_occ("Krasnosielski", "Pan", "Kraśnik", "Pisarz skarbowy", None, 650, 1758, "Pan Krasnosielski Pisarz skarbowy", "Odebrał konfesaty poddanych z urzędu")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Urzędnik miejski", None, 650, 1758, "Sławetny Szymon Krzeszowski", "Wspomniany przy konfesatach")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Pisarz miejski", None, 650, 1758, "Sławetny Stanisław Bryśkiewicz", "Obwiniony o zaniedbanie wpisu konfesat mimo pobrania salarium")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Poręczyciel", None, 650, 1758, "Mikołay Nowak (+)", "Poręczyciel za uwolnienie Andrzeja Tokarczyka (podpis krzyżem)")
add_occ("Pitek", "Józef", "Kraśnik", "Mieszczanin / Poręczyciel", None, 650, 1758, "Jozef Pitek (+)", "Poręczyciel za uwolnienie Andrzeja Tokarczyka (podpis krzyżem)")
add_occ("Tokarz", "Andrzej", "Kraśnik", "Uczciwy / Więziony", "Tokarczyk", 650, 1758, "Andrzey Tokarczyk", "Wypuszczony z więzienia za poręką Nowaka i Pitka")

# Weryfikacja braku duplikatów (Wariant 2)
keys = [(p['nazwisko'], p['imie'], p['miejsce']) for p in gen_data]
assert len(keys) == len(set(keys)), "DUPLICATE IDENTITY DETECTED!"
for p in gen_data:
    assert p.get('funkcja'), f"EMPTY ROLE: {p}"

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part26.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part26.json ({len(gen_data)} profiles) and CSV exported.")
