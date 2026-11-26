# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part29.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w Partii 30 (skany 726–750) Jednostki 17 (sygn. 35/40/0/1/17) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 726 ---
add_occ("Gołębiowski", "Piotr", "Kraśnik", "Sławetny", None, 726, 1758, "Piotr Gołębiowski", "Kupował chleb u starozakonnej wdowy Moszkowej")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki / Manifestant", None, 726, 1758, "Franciszek Barankiewicz Ławn. krasn.", "Protestacja przeciw Marcinowi Morelowi (przeprosiny i 10 złp)")
add_occ("Morel", "Marcin", "Kraśnik", "Dawny deputat", None, 726, 1758, "Marcin Morel Dawny Deputat", "Przeprosił Franciszka Barankiewicza za zniewagę na Rynku")

# --- Skan 727 ---
add_occ("Fiałkowski", "Marcin", "Kraśnik", "Urodzony / Dziedzic", "Fyatkowski?", 727, 1758, "Urodzony Marcin Fiałkowski", "Zapis regresu o posesję po ojcu")
add_occ("Pionek", "Szymon", "Kraśnik", "Uczciwy / Posiadacz posesji", "Pełonek? / Kalika", 727, 1758, "Kalika alias Szymon Pełonek [Pionek?]", "Trzyma posesję od ok. 10 lat")
add_occ("Jankiewicz", "Franciszek", "Kraśnik", "Urodzony obywatel kraśnicki", "Franiewicz?", 727, 1758, "Urodzony Franciszek Jankiewicz", "Obdukcja ran pod okiem i na czole przeciw Kazimierzowi Młynarskiemu")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Pierwszy cechmistrz szewski", None, 727, 1758, "Kazimierz Młynarski Pierwszy Cechmistrz", "Wskazany w obdukcji Franciszka Jankiewicza")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki", None, 727, 1758, "Franciszek Barankiewicz Scab. Crasn.", "Interogatoria przeciw Marcinowi Morelowi")
add_occ("Kratkowski", "Andrzej", "Kraśnik", "Sławetny / Świadek", "Tratkowski?", 727, 1758, "Andreas Tratkowski [Kratkowski?]", "Świadek obelg Marcina Morela")
add_occ("Morel", "Marcin", "Kraśnik", "Sławetny", None, 727, 1758, "Marcin Morel", "Wspomniany w zeznaniu Andrzeja Kratkowskiego")

# --- Skan 728 ---
add_occ("Kratkowski", "Andrzej", "Kraśnik", "Sławetny / Świadek", "Tratkowski?", 728, 1758, "Andrzey Tratkowski", "Dokończenie zeznań")
add_occ("Fiałkowski", "Marcin", "Kraśnik", "Urodzony / Powód", "Fyatkowski?", 728, 1758, "Martinus Fiałkowski", "Interogatoria przeciw szwagrowi Moszkalikowi i sprawa z Pionkiem")
add_occ("Fiałkowski", "Jan", "Kraśnik", "Ojciec Marcina", None, 728, 1758, "Jan Fiałkowski", "Posiadacz ogrodów za murowaną figurą")
add_occ("Moszkalik", "Szymon", "Kraśnik", "Szwagier / Pozwany", "Moskalik?", 728, 1758, "Szymon Moszkalik", "Pozwany o ogród sprzedany Janowi Przesławskiemu")
add_occ("Petrykowski", "Antoni", "Kraśnik", "Rajca kraśnicki / Świadek", None, 728, 1758, "Antonius Petrykowski Cons. Crasn.", "Zeznanie o ogrodzie przy Walentym Gorgielu")
add_occ("Gorgiel", "Walenty", "Kraśnik", "Sąsiad ogrodu", None, 728, 1758, "Walenty Gorgiel", "Sąsiad sadu trzymanego przez Moszkalika")
add_occ("Przesławski", "Jan", "Kraśnik", "Nabywca ogrodu", None, 728, 1758, "Jan Przesławski", "Kupił ogród za murowaną figurą od Moszkalika")
add_occ("Pionek", "Szymon", "Kraśnik", "Uczciwy / Pozwany", None, 728, 1758, "Szymon Pionek", "Dylacja w sprawie sukcesyjnej z Marcinem Fiałkowskim")

# --- Skan 729 ---
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki", None, 729, 1758, "Franciszek Barankiewicz Ławn. krasn.", "Dylacja z Marcinem Morelem")
add_occ("Morel", "Marcin", "Kraśnik", "Dawny deputat", None, 729, 1758, "Marcin Morel Dawny Deputat", "Prolongata na tydzień")
add_occ("Kilianek", "Bartłomiej", "Kraśnik", "Uczciwy / Poszkodowany", None, 729, 1758, "Bartłomiey Kilianek", "Obdukcja ugryzienia w nos przeciw Grzegorzowi Grzętce")
add_occ("Grzętka", "Grzegorz", "Kraśnik", "Uczciwy / Sprawca", "Grzątka?", 729, 1758, "Grzegorz Grzętka [Grzątka?]", "Pozwany przez Bartłomieja Kilianka")

# --- Skan 730 ---
add_occ("Kilianek", "Bartłomiej", "Kraśnik", "Poszkodowany", None, 730, 1758, "Bartłomiey Kilianek", "Dokończenie obdukcji ran twarzy i sukni")
add_occ("Rosłak", "Antoni", "Wyrwonka / Okolice", "Pracowity / Manifestant", "Resłak?", 730, 1758, "Antoni Rosłak [Resłak?]", "Protestacja przeciw Wawrzyńcowi i Janowi Tokarczykom")
add_occ("Tokarz", "Wawrzyniec", "Kraśnik", "Uczciwy / Sprawca pobicia", "Tokarczyk", 730, 1758, "Wawrzyniec Tokarczyk", "Wskazany w manifestacji Antoniego Rosłaka")
add_occ("Tokarz", "Jan", "Kraśnik", "Uczciwy / Sprawca pobicia", "Tokarczyk", 730, 1758, "Jan Tokarczyk", "Wskazany w manifestacji Antoniego Rosłaka")
add_occ("Pionek", "Szymon", "Kraśnik", "Uczciwy / Manifestant", None, 730, 1758, "Szymon Pionek", "Manifestacja z żoną Marianną przeciw Marcinowi Fiałkowskiemu")
add_occ("Pionkowa", "Marianna", "Kraśnik", "Żona Szymona Pionka", None, 730, 1758, "Marianna Pionkowa", "Współmanifestantka")
add_occ("Tokarz", "Antoni", "Kraśnik", "Sławetny / Brat stryjeczny", None, 730, 1758, "Antoni Tokarz", "Współmanifestant przy Mariannie Pionkowej")
add_occ("Tokarz", "Wojciech", "Kraśnik", "Uczciwy / Brat stryjeczny", None, 730, 1758, "Woyciech Tokarz", "Współmanifestant przy Mariannie Pionkowej")
add_occ("Fiałkowski", "Marcin", "Kraśnik", "Urodzony / Pozwany", "Fyatkowski?", 730, 1758, "Urodzony Marcin Fiałkowski", "Pozwany w manifestacji Pionków")

# --- Skan 731 ---
add_occ("Pionek", "Szymon", "Kraśnik", "Manifestant", None, 731, 1758, "Szymon Pionek", "Wskazał na pochowanie ojca Marcina Fiałkowskiego")
add_occ("Fiałkowski", "Marcin", "Kraśnik", "Urodzony", "Fyatkowski?", 731, 1758, "Marcin Fiałkowski", "Niestawienie się na dylację")
add_occ("Fiałkowski", "Jan", "Kraśnik", "Zmarły ojciec", None, 731, 1758, "Ociec Marcina Fiałkowskiego", "Pochowany po chrześcijańsku przez Pionka")
add_occ("Kozowa", "Józefowa", "Przedmieście Góry i Podlesie", "Żona Józefa Kozy / Poszkodowana", None, 731, 1758, "Jozefa Kozy żona", "Obdukcja ran (oko, ręka, wybite okno) przeciw Wawrzyńcowi Jardakowi")
add_occ("Jardak", "Wawrzyniec", "Kraśnik", "Uczciwy / Sprawca", "Jarduk?", 731, 1758, "Wawrzyniec Jardak [Jarduk?]", "Wskazany w obdukcji żony Józefa Kozy")

# --- Skan 732 ---
add_occ("Kozina", "Marcinowa", "Kraśnik", "Powódka", None, 732, 1758, "Marcinowa Kozina", "Interogatoria i proces o ziarno (22 gr vs 2 grzywny) z Józefem Kozą")
add_occ("Koza", "Józef", "Przedmieście Góry i Podlesie", "Przedmieszczanin / Pozwany", None, 732, 1758, "Jozef Koza", "Pozwany o pogoń i dług za ziarno")
add_occ("Świetlicka", "Pawłowa", "Kraśnik", "Wdowa mieszczanka kraśnicka / Świadek", None, 732, 1758, "Pawłowa Świetlicka wdowa", "Zeznanie o pościgu Józefa Kozy")
add_occ("Susiadek", "Wojciech", "Kraśnik", "Gospodarz", None, 732, 1758, "Woyciech Susiadek", "W jego domu schroniła się Marcinowa Kozina")

# --- Skan 733 ---
add_occ("Kozina", "Marcinowa", "Kraśnik", "Powódka", None, 733, 1758, "Marcinowa Kozina", "Dylacja z Kozą na poniedziałek")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 733, 1758, "Kazimierz Młynarski Cechmistrz", "Interogatoria przeciw Marcinowi Morelowi")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat", None, 733, 1758, "Marcin Morel", "Bójka w gospodzie przy szynkwasie")
add_occ("Okoniowa", "Katarzyna", "Kraśnik", "Mężatka / Świadek", None, 733, 1758, "Katarzyna Okoniowa mężatka", "Szczegółowe zeznanie o bójce Młynarskiego z Morelem i Morelową")

# --- Skan 734 ---
add_occ("Okoniowa", "Katarzyna", "Kraśnik", "Świadek", None, 734, 1758, "Katarzyna Okoniowa", "Dokończenie zeznań")
add_occ("Suliczyński", "Antoni", "Kraśnik", "Ławnik kraśnicki / Deputowany", None, 734, 1758, "Antoni Suliczyński Ławn. krasn.", "Relacja z przesłuchania Żydówki Heliny")
add_occ("Kadla", "Adam", "Kraśnik", "Ławnik kraśnicki / Deputowany", "Zadel?", 734, 1758, "Adam Zadel [Kadla] Ławn. krasn.", "Relacja z przesłuchania Żydówki Heliny")
add_occ("Helina", "Żydówka", "Kraśnik", "Starozakonna / Świadek", None, 734, 1758, "Żydówka Helina", "Relacja o bójce w gospodzie")
add_occ("Dudek", "Antoni", "Kraśnik", "Mieszczanin kraśnicki / Świadek", None, 734, 1758, "Antonius Dudek Civis Crasn.", "Zeznanie o bójce w gospodzie")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 734, 1758, "Kazimierz Młynarski", "Wymieniony w relacji i zeznaniu")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat", None, 734, 1758, "Marcin Morel", "Wymieniony w relacji i zeznaniu")

# --- Skan 735 ---
add_occ("Dudek", "Antoni", "Kraśnik", "Świadek", None, 735, 1758, "Antoni Dudek", "Dokończenie zeznań (pies Morela, Okoń)")
add_occ("Okoń", "Antoni", "Kraśnik", "Magister szewski", None, 735, 1758, "Antoni Okoń", "Wzmiankowany w zeznaniu Dudka")
add_occ("Szubertowski", "Jan", "Kraśnik", "Podskarbi Bractwa Różańcowego", None, 735, 1758, "Jan Szubertowski Podskarbi", "Interogatoria o niwkę Soteckiej")
add_occ("Matyasz", "Mieszczanin", "Kraśnik", "Uczciwy mieszczanin / Świadek", None, 735, 1758, "Matyasz mieszczanin", "Zeznanie o 4 częściach niwki Soteckich")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik", None, 735, 1758, "Szymon Krzeszowski", "Kupił pierwszą część niwki Soteckich")
add_occ("Sotecki", "Kazimierz", "Kraśnik", "Zmarły", None, 735, 1758, "Kazimierz Sotecki", "Objął drugą część niwki")
add_occ("Sotecka", "Marianna", "Kraśnik", "Wdowa", None, 735, 1758, "Marianna Sotecka wdowa", "Żona Kazimierza Soteckiego")
add_occ("Sutakowski", "Szymon", "Kraśnik", "Kantor kościoła kraśnickiego", None, 735, 1758, "Szymon Sutakowski kantor", "Zięć Soteckiego (trzecia część niwki)")
add_occ("Krzanowski", "Wojciech", "Kraśnik", "Wnuk Soteckiego", None, 735, 1758, "Woyciech Krzanowski", "Sprzedał dwie części niwki po matce i ciotce")

# --- Skan 736 ---
add_occ("Sotecka", "Marianna", "Kraśnik", "Wdowa", None, 736, 1758, "Marianna Sotecka wdowa", "Wniosła posag i spłaciła dług Żydówce Marince")
add_occ("Marinka", "Żydówka", "Kraśnik", "Starozakonna / Wierzycielka", None, 736, 1758, "Żydówka Marinka", "Otrzymała spłatę długu od Soteckiej")
add_occ("Potokowicz", "Wojciech", "Kraśnik", "Sławetny / Świadek", None, 736, 1758, "Woyciech Potokowicz", "Zeznanie o niwce Soteckich")
add_occ("Frajka", "Matyasz", "Kraśnik", "Informator", None, 736, 1758, "Matyasz Frajka", "Wspomniany w zeznaniu Potokowicza")
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik / Podskarbi Bractwa", None, 736, 1758, "Jan Szubertowski Ławn. krasn.", "Proces o niwkę testamentową przeciw Morelowi")
add_occ("Morel", "Marcin", "Kraśnik", "Dawny deputat", None, 736, 1758, "Marcin Morel Deputat dawny", "Pozwany o niwkę Soteckiej")

# --- Skan 737 ---
add_occ("Sotecka", "Marianna", "Kraśnik", "Wdowa", None, 737, 1758, "Marianna Sotecka wdowa", "Uzasadnienie dekretu na mocy Prawa Magdeburskiego")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat", None, 737, 1758, "Marcin Morel", "Nakaz trzymania niwki do wyjaśnienia losu sukcesora")

# --- Skan 738 ---
add_occ("Morel", "Marcin", "Kraśnik", "Deputat", None, 738, 1758, "Marcin Morel", "Ma otrzymać 30 złp od burmistrza Bryśkiewicza")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Burmistrz kraśnicki", None, 738, 1758, "Stanisław Bryśkiewicz Bk.", "Nakaz zwrotu 30 złp Marcinowi Morelowi")
add_occ("Lejbusiewicz", "Szmul", "Kraśnik", "Starozakonny obywatel kraśnicki", None, 738, 1758, "Szmul Leybusiewicz obywat. krasn.", "Proces przeciw Józefowi Gęsce o nawóz i kapustę")
add_occ("Gęska", "Józef", "Kraśnik", "Przedmieszczanin / Pozwany", "Gąska?", 738, 1758, "Jozef Gęska [Gąska?] Przed. krasn.", "Pozwany przez Szmula Lejbusiewicza")

# --- Skan 739 ---
add_occ("Lejbusiewicz", "Szmul", "Kraśnik", "Starozakonny", None, 739, 1758, "Szmul Leybusiewicz", "Odesłanie do przyjaciół")
add_occ("Gęska", "Józef", "Kraśnik", "Przedmieszczanin", "Gąska?", 739, 1758, "Jozef Gęska", "Dylacja z Lejbusiewiczem")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik / Deputowany", None, 739, 1758, "Szymon Krzeszowski", "Relacja z zeznania Żyda Gierszona")
add_occ("Kadla", "Adam", "Kraśnik", "Ławnik / Deputowany", "Zadel?", 739, 1758, "Adam Zadel [Kadla] Ław. krasn.", "Relacja z zeznania Żyda Gierszona")
add_occ("Gierszon", "Żyd", "Kraśnik", "Starozakonny / Świadek", None, 739, 1758, "Żyd Gierszon", "Zeznanie o bójce Młynarskiego z Morelem")

# --- Skan 740 ---
add_occ("Gierszon", "Żyd", "Kraśnik", "Świadek", None, 740, 1758, "Gierszon", "Upominał Antoniego Okonia podczas bójki")
add_occ("Okoń", "Antoni", "Kraśnik", "Magister szewski", None, 740, 1758, "Antoni Okoń", "Krzyczał 'bij tego psa'")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 740, 1758, "Kazimierz Młynarski", "Prezentował spuchnięte ramię")
add_occ("Srakiewicz", "Szymon", "Kraśnik", "Sławetny", "Sralkiewicz?", 740, 1758, "Szymon Srakiewicz [Sralkiewicz?]", "Oświadczenie o zaginięciu Kazimierza Soteckiego")
add_occ("Sotecka", "Marianna", "Kraśnik", "Wdowa", None, 740, 1758, "Marianna Sotecka", "Wzmianka o spalonej chacie i odbitej kłódce")
add_occ("Piliński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 740, 1758, "Antoni Piliński", "Oświadczenie w sprawie Soteckiej")

# --- Skan 741 ---
add_occ("Piliński", "Antoni", "Kraśnik", "Ławnik kraśnicki / Manifestant", None, 741, 1758, "Antoni Piliński Ławn. kras.", "Protestacja przeciw Marcinowi Morelowi o zadanie szalbierstwa")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat", None, 741, 1758, "Marcin Morel Deputat kras.", "Pozwany w manifestacji Pilińskiego")
add_occ("Czajkowski", "Józef", "Kraśnik", "Urodzony czeladnik", "Czaykowski?", 741, 1758, "Urodzony Jozef Czaykowski czeladnik", "Areszt na 3 czerwone złote i 4 tynfy")
add_occ("Moszkowicz", "Abraham", "Kraśnik", "Starozakonny (syn)", None, 741, 1758, "Syn Abrahama Moszkowicza", "Strona przy areszcie Czajkowskiego")
add_occ("Wróblewski", "Jan", "Kraśnik", "Parobek Łukasza Pałki", "Wróbleski?", 741, 1758, "Jan Wróbleski Parobek", "Manifestacja przeciw Antoniemu Truyerakowi")
add_occ("Pałka", "Łukasz", "Kraśnik", "Gospodarz", None, 741, 1758, "Łukasz Pałka", "Chlebodawca Jana Wróblewskiego")
add_occ("Truyerak", "Antoni", "Kraśnik", "Uczciwy / Pozwany", None, 741, 1758, "Antoni Truyerak", "Pozwany w manifestacji Wróblewskiego")

# --- Skan 742 ---
add_occ("Wróblewski", "Jan", "Kraśnik", "Parobek", "Wróbleski?", 742, 1758, "Jan Wróbleski", "Dokończenie manifestacji przeciw Truyerakowi i Tokarzowi")
add_occ("Tokarz", "Jan", "Kraśnik", "Sprawca pobicia", None, 742, 1758, "Jan Tokarz", "Współsprawca pobicia w gospodzie")
add_occ("Grzętka", "Grzegorz", "Przedmieście Góry i Podlesie", "Nabywca gruntu", "Grzątka?", 742, 1758, "Grzegorz Grzętka", "Intromisja na kwaterę pola na Podlesiu za 100 złp")
add_occ("Posuniak", "Adam", "Przedmieście Góry i Podlesie", "Sąsiad gruntu", None, 742, 1758, "Adam Posuniak", "Sąsiad na Podlesiu")
add_occ("Ciurko", "Jan", "Przedmieście Góry i Podlesie", "Sprzedający", "Ciurka?", 742, 1758, "Jan Ciurka +", "Sprzedał kwaterę pola na Podlesiu (podpis krzyżykiem)")
add_occ("Ciurko", "Wojciech", "Przedmieście Góry i Podlesie", "Sprzedający", "Ciurka?", 742, 1758, "Woyciech Ciurka +", "Współsprzedający (podpis krzyżykiem)")
add_occ("Krzywicki", "Michał Ignacy", "Kraśnik", "Wójt kraśnicki", None, 742, 1758, "Michał Ignacy Krzywicki Woyt", "Asystował przy intromisji Grzętki")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Pisarz miejski", None, 742, 1758, "Łukasz Krzeszowski Pisarz", "Asystował przy intromisji Grzętki")
add_occ("Piliński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 742, 1758, "Antoni Piliński Ław. kras.", "Asystował przy intromisji Grzętki")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", "Ławnik kraśnicki", None, 742, 1758, "Franc. Barankiewicz Ław. kras.", "Asystował przy intromisji Grzętki")
add_occ("Kadla", "Adam", "Kraśnik", "Ławnik kraśnicki", "Zadel?", 742, 1758, "Adam Zadel [Kadla] Ław. kras.", "Asystował przy intromisji Grzętki")
add_occ("Zdybeł", "Mateusz", "Przedmieście Kraśnickie", "Manifestant", None, 742, 1758, "Mateusz Zdybł", "Początek manifestacji przeciw Jakubowi Zimniakowi")

# --- Skan 743 ---
add_occ("Zdybeł", "Mateusz", "Przedmieście Kraśnickie", "Manifestant", None, 743, 1758, "Mateusz Zdybł", "Dokończenie manifestacji")
add_occ("Zimniak", "Jakub", "Przedmieście Kraśnickie", "Pozwany", None, 743, 1758, "Jakub Zimniak", "Pozwany przez Mateusza Zdybła")
add_occ("Witek", "Antoni", "Kraśnik", "Wierzyciel", "Witck?", 743, 1758, "Antoni Witck", "Areszt na pieniądze intromisyjne Grzętki")
add_occ("Nowak", "Józef", "Kraśnik", "Wierzyciel", None, 743, 1758, "Jozef Nowak", "Areszt na pieniądze intromisyjne Grzętki")
add_occ("Pawlicki", "Sebastian", "Kraśnik", "Wierzyciel", None, 743, 1758, "Sobestyan Pawlicki", "Areszt na pieniądze intromisyjne Grzętki")
add_occ("Kilianek", "Bartłomiej", "Kraśnik", "Posłaniec", None, 743, 1758, "Bartłomiey Kilianek", "Relacja poselstwa od Matyasza Deuki")
add_occ("Deuka", "Matyasz", "Kraśnik", "Przedmieszczanin", None, 743, 1758, "Matyasz Deuk", "Wypowiedź przy poselstwie")

# --- Skan 744 ---
add_occ("Grzętka", "Sebastian", "Kraśnik", "Manifestant", None, 744, 1758, "Sobestyan Grzętka", "Manifestacja przeciw Marcinowi Kotłunowi o kopaninę")
add_occ("Kotłun", "Marcin", "Kraśnik", "Pozwany", None, 744, 1758, "Marcin Kotłun", "Pozwany o kopaninę")
add_occ("Pawlicki", "Sebastian", "Kraśnik", "Wierzyciel", None, 744, 1758, "Sobestyan Pawlicki", "Powtórny areszt pieniędzy Grzętki")
add_occ("Grzętka", "Grzegorz", "Przedmieście Góry i Podlesie", "Nabywca", None, 744, 1758, "Grzegorz Grzętka", "Zakaz wypłaty pieniędzy Janowi Ciurce")
add_occ("Ciurko", "Jan", "Przedmieście Góry i Podlesie", "Sprzedający", None, 744, 1758, "Jan Ciurka", "Objęty aresztem")
add_occ("Okoń", "Antoni", "Kraśnik", "Mistrz kraśnicki", None, 744, 1758, "Antoni Okoń Mistrz kras.", "Protestacja przeciw Kazimierzowi Młynarskiemu")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Pierwszy cechmistrz szewski", None, 744, 1758, "Kazimierz Młynarski", "Pozwany w manifestacji Okonia")

# --- Skan 745 ---
add_occ("Okoń", "Antoni", "Kraśnik", "Mistrz szewski", None, 745, 1758, "Antoni Okoń", "Skarga o zniewagę („parę pańskich ukradłeś”)")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 745, 1758, "Kazimierz Młynarski", "Oskarżony o wyzwiska i pozywanie")
add_occ("Szmul", "Anzelm", "Kraśnik", "Starozakonny obywatel kraśnicki", "Szmulko?", 745, 1758, "Niewierny Anzelm [Szmulko?]", "Proces przeciw Jędrzejowi Małeckiemu o topór i uderzenie")
add_occ("Małecki", "Jędrzej", "Kraśnik", "Magister kunsztu szewskiego", "Maiecki?", 745, 1758, "Jędrzey Małecki [Maiecki?] Magister szewski", "Dylacja w sporze o topór")

# --- Skan 746 ---
add_occ("Piliński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 746, 1758, "Antoni Piliński Ławn. kras.", "Wyrok o wieprza (9 złp i 2 grzywny)")
add_occ("Piurkowski", "Sebastian", "Kraśnik", "Uczciwy / Pozwany i powód", "Jurkowski?", 746, 1758, "Sobestyan Piurkowski [Jurkowski?]", "Skazany o wieprza; proces o tatarce przeciw Kotłunowi i Tomkowskiej")
add_occ("Kotłun", "Marcin", "Kraśnik", "Pozwany (Antoni?)", "Antoni", 746, 1758, "Antoni Kotłun", "Pozwany o 1 kopę 18 snopów tatarki")
add_occ("Tomkowska", "Kazimierzowa", "Kraśnik", "Uczciwa / Pozwana", "Tomkowiczowa?", 746, 1758, "Kazimierzowa Tomkowska", "Pozwana o 50 snopów tatarki")

# --- Skan 747 ---
add_occ("Piurkowski", "Sebastian", "Kraśnik", "Powód", "Jurkowski?", 747, 1758, "Sobestyan Piurkowski", "Dylacja na świadków szkody")
add_occ("Piliński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 747, 1758, "Antoni Piliński Ławnik krasn.", "Dylacja z Marcinem Morelem o infamię")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat kraśnicki", None, 747, 1758, "Marcin Morel Deput. kras.", "Pozwany przez Antoniego Pilińskiego")

# --- Skan 748 & 749 (dublet fol. 367r) ---
for s in (748, 749):
    add_occ("Zdybeł", "Mateusz", "Przedmieście Kraśnickie", "Powód", None, s, 1758, "Mateusz Zdybł", "Proces przeciw Jakubowi Zimniakowi o kopce")
    add_occ("Zimniak", "Jakub", "Przedmieście Kraśnickie", "Pozwany", None, s, 1758, "Jakub Zimniak", "Pozwany o powymowanie kopców")
    add_occ("Petrykowski", "Antoni", "Kraśnik", "Dawny rajca / Powód", None, s, 1758, "Antoni Petrykowski Dawny Rayca", "Proces przeciw Marcinowi Morelowi o pobicie syna i porąbanie dyszla")
    add_occ("Morel", "Marcin", "Kraśnik", "Deputat kraśnicki / Pozwany", None, s, 1758, "Marcin Morel Deput. kras.", "Pozwany przez Antoniego Petrykowskiego")

# --- Skan 750 ---
add_occ("Petrykowski", "Antoni", "Kraśnik", "Rajca kraśnicki", None, 750, 1758, "Antonius Petrykowski Cons. Crasn.", "Odesłanie do przyjaciół z Morelem; świadek w sprawie Młynarskiego")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat kraśnicki", None, 750, 1758, "Marcin Morel Deput. kras.", "Pozwany przez Petrykowskiego i Młynarskiego")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Pierwszy cechmistrz szewski", None, 750, 1758, "Kazimierz Młynarski Cech. Pierwszy Magister", "Interogatoria i początek dekretu przeciw Morelowi i Okoniowi")
add_occ("Macal", "Łukasz", "Kraśnik", "Mieszkaniec", "Macała?", 750, 1758, "Łukasz Macal [Macała?]", "Wzmiankowany w zeznaniu Antoniego Petrykowskiego")
add_occ("Okoń", "Antoni", "Kraśnik", "Magister szewski", None, 750, 1758, "Antoni Okoń", "Współpozwany w sprawie Młynarskiego")

# Zapis gen_data_j17_part30.json
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part30.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

# Eksport CSV UTF-8-SIG zgodnie z SKILL.md
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
    writer.writerow(['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'])
    for p in gen_data:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p.get('funkcja') or p.get('funkcja_zawod') or '',
            p.get('skany_roboczo', ''),
            p.get('zakres_lat', ''),
            p.get('liczba_wystapien', 1),
            p.get('wariant_nazwiska') or ''
        ])

print(f"SUCCESS: gen_data_j17_part30.json ({len(gen_data)} profiles) and CSV exported.")
