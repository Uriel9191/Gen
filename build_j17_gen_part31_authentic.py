# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part30.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w Partii 31 (skany 751–776) Jednostki 17 (sygn. 35/40/0/1/17) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 751 ---
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Powód", None, 751, 1758, "Casimirus Młynarski Civ. Cras.", "Dylacja i interogatoria przeciw Morelowi i Okoniowi")
add_occ("Morel", "Marcin", "Kraśnik", "Asesor kraśnicki / Pozwany", None, 751, 1758, "Martinus Morel Assessor Cras.", "Pozwany w sprawie o kłótnię o niwkę")
add_occ("Okoń", "Antoni", "Kraśnik", "Pozwany", None, 751, 1758, "Antonius Okoń Civ. Cras.", "Nie stawił się na termin; dylacja")
add_occ("Potokowiczowa", "Jadwiga", "Kraśnik", "Uczciwa / Świadek", "Potocka?", 751, 1758, "Hedvigis Potokowiczowa Mężatka", "Świadek kłótni w gospodzie")

# --- Skan 752 ---
add_occ("Potokowiczowa", "Jadwiga", "Kraśnik", "Świadek", "Potocka?", 752, 1758, "Jadwiga Potokowiczowa", "Dokończenie zeznań o bójce w gospodzie")
add_occ("Okoń", "Antoni", "Kraśnik", "Pozwany", None, 752, 1758, "Antoni Okoń", "Trzymał pieniądze w garści, nie bił")
add_occ("Morelowa", "Marcinowa", "Kraśnik", "Sławetna / Uczestniczka bójki", None, 752, 1758, "Marcinowa Morelowa", "Pchnęła Młynarskiego i biła go razem z mężem")
add_occ("Morel", "Marcin", "Kraśnik", "Pozwany", None, 752, 1758, "Morel", "Bił Młynarskiego z żoną i psem")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Powód", None, 752, 1758, "Młynarski", "Pobity i pogryziony przez psa")
add_occ("Deuka", "Matyasz", "Kraśnik", "Uczciwy / Powód", "Dacka?", 752, 1758, "Matyasz Deuka", "Powód przeciw Matyaszowi Łyżikowi o pobicie i kalumnię")
add_occ("Łyżik", "Matyasz", "Kraśnik", "Uczciwy / Pozwany", "Łyżyk?", 752, 1758, "Matyasz Łyżik", "Skazany zaocznie na grzywny i więzienie")

# --- Skan 753 ---
add_occ("Deuka", "Matyasz", "Kraśnik", "Powód", "Dacka?", 753, 1758, "Matyasz Deuka", "Dokończenie dekretu przeciw Łyżikowi")
add_occ("Łyżik", "Matyasz", "Kraśnik", "Pozwany", "Łyżyk?", 753, 1758, "Matyasz Łyżik", "Skazany do więzienia do zaspokojenia")
add_occ("Grzętka", "Sebastian", "Kraśnik", "Uczciwy / Powód", None, 753, 1758, "Sebestyan Grzętka", "Wyrok zaoczny przeciw Marcinowi Kotłunowi")
add_occ("Kotłun", "Marcin", "Kraśnik", "Uczciwy / Pozwany", None, 753, 1758, "Marcin Kotłun", "Skazany zaocznie na 2 grzywny sądowi per medium")
add_occ("Bednarz", "Tomasz", "Kraśnik", "Mieszczanin kraśnicki / Powód", None, 753, 1758, "Tomasz Bednarz mieszczanin krasnicki", "Dylacja w sprawie przeciw Lewkowi o dekret")
add_occ("Lewek", "Starozakonny", "Kraśnik", "Pozwany", "Lawka?", 753, 1758, "niewierny Lewek [Lawka?]", "Pozwany przez Tomasza Bednarza")
add_occ("Pawlicki", "Sebastian", "Kraśnik", "Mieszczanin kraśnicki / Manifestant", None, 753, 1758, "Sebestyan Pawlicki mieszczanin krasnicki", "Manifestacja przeciw Janowi Ciurce i jego synom")
add_occ("Ciurka", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", "Ciurko", 753, 1758, "Jan Ciurka", "Pozwany przez Sebestyana Pawlickiego")
add_occ("Ciurka", "Grzegorz", "Przedmieście Kraśnickie", "Przedmieszczanin / Syn Jana", "Ciurko", 753, 1758, "Grzegorz Ciurka", "Współpozwany syn Jana Ciurki")
add_occ("Ciurka", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin / Syn Jana", "Ciurko", 753, 1758, "Woyciech Ciurka", "Współpozwany syn Jana Ciurki")

# --- Skany 754 & 755 (dublet fol. 369v) ---
for s in (754, 755):
    add_occ("Pawlicki", "Sebastian", "Kraśnik", "Manifestant", None, s, 1758, "Sebestyan Pawlicki", "Areszt na pieniądze za kwaterę pola za Grzegorzką")
    add_occ("Ciurka", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin", "Ciurko", s, 1758, "Jan Ciurka", "Sprzedał kwaterę pola bez wiedzy Pawlickiego")
    add_occ("Ciurka", "Grzegorz", "Przedmieście Kraśnickie", "Przedmieszczanin", "Ciurko", s, 1758, "Grzegorz Ciurka", "Współsprzedający pole za Grzegorzką")
    add_occ("Ciurka", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin", "Ciurko", s, 1758, "Woyciech Ciurka", "Współsprzedający pole za Grzegorzką")
    add_occ("Markowicz", "Chaim", "Kraśnik", "Starozakonny", "Charm?", s, 1758, "Chaim Markowicz", "Areszt na wyjazd żony przed rozprawą u Marszałka")
    add_occ("Piurkowski", "Sebastian", "Kraśnik", "Uczciwy", "Jurkowski?", s, 1758, "Sebestyan Piurkowski", "Wizja szkody w tatarce")
    add_occ("Kotłun", "Marcin", "Kraśnik", "Uczciwy (Antoni?)", "Antoni", s, 1758, "Antoni Kotłun", "Wizja szkody w tatarce")

# --- Skan 756 ---
add_occ("Kratkowski", "Andrzej", "Kraśnik", "Exaktor miejski kraśnicki", "Tratkowski?", 756, 1758, "Andrzey Kratkowski Exaktor Mieyski", "Wizja szkody po 15 snopów tatarki")
add_occ("Potokowicz", "Antoni", "Kraśnik", "Mieszczanin kraśnicki", None, 756, 1758, "Antoni Potokowicz Mieszczanin Krasn.", "Wizja szkody w tatarce")
add_occ("Piurkowski", "Sebastian", "Kraśnik", "Poszkodowany", "Jurkowski?", 756, 1758, "Sebestyan Piurkowski", "Szkoda w tatarce: 15 snopów")
add_occ("Kotłun", "Marcin", "Kraśnik", "Poszkodowany / Pozwany (Antoni?)", "Antoni", 756, 1758, "Antoni Kotłun / Marcin Kotłun", "Szkoda w tatarce (15 snopów) oraz sprawa z Grzętką o kopaninę")
add_occ("Grzętka", "Sebastian", "Kraśnik", "Powód", None, 756, 1758, "Sobestyan Grzętka", "Proces przeciw Marcinowi Kotłunowi o kopaninę")
add_occ("Laska", "Józef", "Kraśnik", "Przedmieszczanin / Świadek", None, 756, 1758, "Józef Laska przedmieszczanin", "Zeznanie o dwuletnim zaorywaniu kopaniny przez Kotłuna")

# --- Skan 757 ---
add_occ("Grzętka", "Sebastian", "Kraśnik", "Powód", None, 757, 1758, "Sebestyan Grzętka", "Dokończenie dylacji z Kotłunem")
add_occ("Kotłun", "Marcin", "Kraśnik", "Pozwany", None, 757, 1758, "Marcin Kotłun", "Dokończenie dylacji z Grzętką")
add_occ("Ahel", "Rzeźnik", "Kraśnik", "Starozakonny / Obywatel kraśnicki", "Aron? / Anzelm?", 757, 1758, "niewierny Ahel [Aron? / Anzelm?] Rzeźnik", "Proces przeciw kowalowi Małeckiemu o topór")
add_occ("Małecki", "Jędrzej", "Kraśnik", "Kowal / Pozwany", "Maiecki?", 757, 1758, "Jędrzey Małecki kunsztu kowalskiego", "Nakaz reparacji i oddania topora bez zapłaty")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 757, 1758, "Szymon Krzeszowski Ławnik krasnicki", "Dylacja przeciw Antoniemu Kaweckiemu o potrącenie żony w młynie")
add_occ("Kawecki", "Antoni", "Kraśnik", "Mieszczanin kraśnicki", "Kawiecki?", 757, 1758, "Antoni Kawecki mieszczanin krasnicki", "Pozwany przez Szymona Krzeszowskiego")

# --- Skan 758 ---
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 758, 1758, "Szymon Krzeszowski", "Dokończenie dylacji z Kaweckim")
add_occ("Kawecki", "Antoni", "Kraśnik", "Mieszczanin kraśnicki", "Kawiecki?", 758, 1758, "Antoni Kawecki", "Dokończenie dylacji z Krzeszowskim")
add_occ("Piliński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 758, 1758, "Antonius Piliński Scab. Cras.", "Interogatoria przeciw Marcinowi Morelowi")
add_occ("Morel", "Marcin", "Kraśnik", "Asesor kraśnicki / Pozwany", None, 758, 1758, "Martinus Morel Assessor", "Pozwany przez Antoniego Pilińskiego")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Sławetny / Świadek", None, 758, 1758, "Casimirus Młynarski", "Zeznanie w sprawie Pilińskiego przeciw Morelowi")
add_occ("Pilaszkiewicz", "Antoni", "Kraśnik", "Mieszkaniec", None, 758, 1758, "Antoni Pilaszkiewicz", "Wzmiankowany w zeznaniu Kazimierza Młynarskiego")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Rajca kraśnicki / Świadek", None, 758, 1758, "Lucas Krzeszowski Consul Cras.", "Zeznanie o hipińskiej niwce P. Frankiewiczowej")

# --- Skan 759 ---
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Rajca kraśnicki / Świadek", None, 759, 1758, "Łukasz Krzeszowski", "Dokończenie zeznania o bójce i ratowaniu Młynarskiego")
add_occ("Morel", "Marcin", "Kraśnik", "Pozwany", None, 759, 1758, "Morel", "Skakał do Młynarskiego i wyzywał")
add_occ("Morelowa", "Marcinowa", "Kraśnik", "Żona Morela", None, 759, 1758, "żona Morela", "Pchnęła Młynarskiego")
add_occ("Piliński", "Antoni", "Kraśnik", "Ławnik / Powód", None, 759, 1758, "Piliński", "Ratował Młynarskiego")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Sławetny", None, 759, 1758, "Młynarski", "Broniony przez Pilińskiego")
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki / Świadek", "Szubrowski?", 759, 1758, "Joannes Szubertowski Scabinus Crasn.", "Drugi świadek w sprawie Pilińskiego przeciw Morelowi")

# --- Skan 760 ---
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik / Świadek", "Szubrowski?", 760, 1758, "Jan Szubertowski", "Dokończenie zeznania (bronił z Łukaszem Krzeszowskim)")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Rajca kraśnicki", None, 760, 1758, "Łukasz Krzeszowski", "Współbroniący przed zgorszeniem")
add_occ("Piliński", "Antoni", "Kraśnik", "Ławnik kraśnicki / Powód", None, 760, 1758, "Antoni Piliński Ławnik krasnicki", "Dekret przeciw Morelowi o zadanie kradzieży na jarmarku")
add_occ("Morel", "Marcin", "Kraśnik", "Deputat / Pozwany", None, 760, 1758, "Marcin Morel Deputat", "Skazany na 2 grzywny aktorowi, sądowi per medium, przeprosiny i więzienie")

# --- Skany 761 & 762 (dublet fol. 372v) ---
for s in (761, 762):
    add_occ("Piliński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, s, 1758, "Antoni Piliński", "Apelacja do Najwyższego Sądu i areszt apelacji Morela")
    add_occ("Morel", "Marcin", "Kraśnik", "Deputat", None, s, 1758, "Marcin Morel", "Pozwany przez Młynarskiego, Szubertowskiego i Krzeszowskiego")
    add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski / Manifestant", None, s, 1758, "Kazimierz Młynarski Cechmistrz Szewski", "Manifestacja przeciw Morelowi o 7 wieprzków")
    add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki / Manifestant", "Szubrowski?", s, 1758, "Jan Szubertowski Ławnik krasnicki", "Manifestacja przeciw Morelowi o zarzut niesłuszności przy obdukcji")
    add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki / Manifestant", s if False else None, s, 1758, "Szymon Krzeszowski Ławnik krasnicki", "Manifestacja przeciw Morelowi o zarzut niesłuszności przy obdukcji")

# --- Skan 763 ---
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki", "Szubrowski?", 763, 1758, "Jan Szubertowski", "Dokończenie manifestacji przeciw Morelowi")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 763, 1758, "Szymon Krzeszowski", "Dokończenie manifestacji przeciw Morelowi")
add_occ("Pawlicki", "Sebastian", "Kraśnik", "Uczciwy", None, 763, 1758, "Sebestyan Pawlicki", "Areszt na Jana Ciurkę w stodole Bartłomieja Zdybła")
add_occ("Nowak", "Józef", "Kraśnik", "Uczciwy", "Nowaczek", 763, 1758, "Józef Nowak", "Współkładący areszt na Jana Ciurkę")
add_occ("Ciurka", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin", "Ciurko", 763, 1758, "Jan Ciurka", "Objęty aresztem w stodole Bartłomieja Zdybła")
add_occ("Zdybeł", "Bartłomiej", "Przedmieście Kraśnickie", "Gospodarz stodoły", None, 763, 1758, "Bartłomiey Zdybeł", "W jego stodole położono areszt na Ciurkę")
add_occ("Piliński", "Antoni", "Kraśnik", "Sławetny / Wizytator", None, 763, 1758, "Antoni Piliński", "Zeznanie wizji 50 snopów tatarki")
add_occ("Łapka", "Matyasz", "Kraśnik", "Wizytator", None, 763, 1758, "Matyasz Łapka", "Zeznanie wizji 50 snopów tatarki")
add_occ("Tomkowski", "Kazimierz", "Kraśnik", "Strona sprawy", None, 763, 1758, "Kazimierz Tomkowski", "Sprawa z Sebestyanem Piurkowskim o 50 snopów tatarki")
add_occ("Piurkowski", "Sebastian", "Kraśnik", "Strona sprawy", "Jurkowski?", 763, 1758, "Sebestyan Piurkowski", "Sprawa z Kazimierzem Tomkowskim")
add_occ("Milewski", "Mikołaj", "Kraśnik", "Uczciwy / Świadek", "Miliski?", 763, 1758, "Mikołay Milewski [Miliski?]", "Zeznanie przeciw Tomaszowi Bednarzowi o okowitę, spódnicę i Piątkowiznę")
add_occ("Bednarz", "Tomasz", "Kraśnik", "Pozwany", None, 763, 1758, "Tomasz Bednarz", "Wskazany w zeznaniu Mikołaja Milewskiego")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Powód", None, 763, 1758, "Kazimierz Młynarski", "Początek dekretu przeciw Morelowi i Okoniowi")
add_occ("Morel", "Marcin", "Kraśnik", "Pozwany", None, 763, 1758, "Marcin Morel", "Współpozwany w sprawie Młynarskiego")
add_occ("Okoń", "Antoni", "Kraśnik", "Pozwany", None, 763, 1758, "Antoni Okoń", "Współpozwany w sprawie Młynarskiego")

# --- Skan 764 ---
add_occ("Morel", "Marcin", "Kraśnik", "Deputat kraśnicki", None, 764, 1758, "Marcin Morel Deputt. krasn.", "Dokończenie dekretu / dylacji Młynarskiego")
add_occ("Okoń", "Antoni", "Kraśnik", "Obwiniony", None, 764, 1758, "Antoni Okoń", "Nie stawił się na termin do przysięgi; dylacja na dzień jutrzejszy")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Powód", None, 764, 1758, "Kazimierz Młynarski", "Dylacja z urzędu")
add_occ("Pawlicki", "Sebastian", "Kraśnik", "Powód", None, 764, 1758, "Sebestyan Pawlicki", "Sprawa o kwaterę pola z pobudynkami")
add_occ("Nowak", "Józef", "Kraśnik", "Powód", "Nowaczek", 764, 1758, "Józef Nowak", "Współpowód przeciw Ciurkom i Grzętce")
add_occ("Ciurka", "Jan", "Przedmieście Kraśnickie", "Pozwany", "Ciurko", 764, 1758, "Jan Ciurka", "Obiecał spuścić kwaterę pola Pawlickiemu")
add_occ("Ciurka", "Wojciech", "Przedmieście Kraśnickie", "Syn Jana Ciurki", "Ciurko", 764, 1758, "Woyciech syn Jana Ciurki", "Pozwany w sprawie pola za Grzegorzką")
add_occ("Grzętka", "Grzegorz", "Kraśnik", "Pozwany", "Grzątka?", 764, 1758, "Grzegorz Grzętka", "Nakaz stawienia się z Wojciechem Ciurką przed sądem")

# --- Skany 765 & 766 (dublet fol. 374r) ---
for s in (765, 766):
    add_occ("Pawlicki", "Sebastian", "Kraśnik", "Powód", None, s, 1758, "Sebestyan Pawlicki", "Dylacja na dzień jutrzejszy")
    add_occ("Nowak", "Józef", "Kraśnik", "Powód", "Nowaczek", s, 1758, "Józef Nowak", "Dylacja na dzień jutrzejszy")
    add_occ("Potokowiczowa", "Krystyna", "Kraśnik", "Mężatka / Powódka", None, s, 1758, "Krystyna Potokowiczowa mężatka", "Sprawa przeciw Antoniemu Fryczakowi o masło i skrzynkę siostry (15 złp 8 gr)")
    add_occ("Fryczak", "Antoni", "Kraśnik", "Uczciwy / Pozwany", "Frycrak?", s, 1758, "Antoni Frycrak [Fryczak?]", "Sprawa o masło, krochmal, konopie i skrzynkę")
    add_occ("Piurkowski", "Sebastian", "Kraśnik", "Uczciwy / Powód", "Jurkowski?", s, 1758, "Sebestyan Piurkowski", "Wyrok o 20 snopów tatarki i 2 grzywny kosztów")
    add_occ("Kotłun", "Marcin", "Kraśnik", "Mieszczanin kraśnicki / Pozwany (Antoni?)", "Antoni", s, 1758, "Antoni Kotłun Mieszcz. krasn.", "Skazany na oddanie 20 snopów tatarki, 2 grzywny sądowi per medium i więzienie")

# --- Skan 767 ---
add_occ("Ciurka", "Wojciech", "Przedmieście Kraśnickie", "Uczciwy / Donator", "Ciurko / Cuirka", 767, 1758, "Woyciech Ciurka syn Jana Ciurki", "Wieczysta donacja pola Ciurkowskiego szwagrowi Józefowi Nowakowi za 15 złp")
add_occ("Ciurka", "Jan", "Przedmieście Kraśnickie", "Ojciec Wojciecha", "Ciurko", 767, 1758, "Jan Ciurka", "Wzmiankowany jako ojciec donatora")
add_occ("Nowak", "Józef", "Kraśnik", "Uczciwy / Nabywca", "Nowaczek", 767, 1758, "Józef Nowak", "Otrzymał donację pola Ciurkowskiego z żoną Agnieszką")
add_occ("Nowakowa", "Agnieszka z Ciurków", "Kraśnik", "Małżonka Józefa Nowaka", "Ciurkówna / de Gente Ciurkowey", 767, 1758, "Agnieszka de Gente Ciurkowey", "Współnabywczyni kwatery pola Ciurkowskiego")
add_occ("Piliński", "Grzegorz", "Kraśnik", "Burmistrz i ławnik kraśnicki", None, 767, 1758, "Grzegorz Piliński Bur. y Ławn. krasn.", "Świadek donacji Wojciecha Ciurki")
add_occ("Krzywicki", "Michał Ignacy", "Kraśnik", "Pisarz przysięgły", None, 767, 1758, "Michał Ignacy Krzywicki Pisarz Przysięgły", "Spisał i własnoręcznie podpisał donację")

# --- Skan 768 ---
add_occ("Dobrowiczowa", "Katarzyna", "Kraśnik", "Wdowa / Manifestantka", "Dobrowicowa?", 768, 1758, "Katarzyna Dobrowicowa wdowa", "Manifestacja przeciw Jakubowi Śliżewskiemu i żonie o zniewagę słowami")
add_occ("Śliżewski", "Jakub", "Kraśnik", "Uczciwy / Pozwany", "Śliwiński?", 768, 1758, "Jakub Śliżewski [Śliwiński?]", "Pozwany z żoną przez Katarzynę Dobrowiczową")
add_occ("Ład", "Adam", "Kraśnik", "Sławetny", "Łada?", 768, 1758, "Adam Ład", "Ugoda z Mikołajem Kawką o zasiew żyta na kopaninie")
add_occ("Kawka", "Mikołaj", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki", None, 768, 1758, "Mikołay Kawka przed. kras.", "Ugoda z Adamem Ładem o kopaninę")

# --- Skan 769 ---
add_occ("Ład", "Adam", "Kraśnik", "Sławetny", "Łada?", 769, 1758, "Adam Ład", "Zakończenie ugody pod wadium 14 grzywien i 3 dni więzienia")
add_occ("Kawka", "Mikołaj", "Przedmieście Kraśnickie", "Przedmieszczanin", None, 769, 1758, "Mikołay Kawka", "Zakończenie ugody pod wadium 14 grzywien")
add_occ("Potokowicz", "Wojciech", "Kraśnik", "Sławetny / Świadek ugody", None, 769, 1758, "Woyciech Potokowicz", "Świadek przy ugodzie Adama Łada z Mikołajem Kawką")
add_occ("Kratkowski", "Bartłomiej", "Kraśnik", "Uczciwy / Świadek ugody", None, 769, 1758, "Bartłomiey Kratkowski", "Świadek przy ugodzie Adama Łada z Mikołajem Kawką")
add_occ("Dobrowiczowa", "Katarzyna", "Kraśnik", "Wdowa / Powódka", "Dobrowicowa?", 769, 1758, "Katarzyna Dobrowicowa wdowa", "Dylacja przeciw Jakubowi Wojciechowskiemu o kalumnię")
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Uczciwy / Pozwany", None, 769, 1758, "Jakub Woyciechowski", "Dylacja o kalumnię przez żonę pozwanego")

# --- Skan 770 ---
add_occ("Domaniewicz", "Jan", "Kraśnik", "Szlachetnie urodzony / Manifestant", None, 770, 1758, "Szlachetnie urodzony Jan Domaniewicz", "Manifestacja przeciw Antoniemu Kotłunowi o zniewagę na gospodzie")
add_occ("Kotłun", "Marcin", "Kraśnik", "Mieszczanin kraśnicki (Antoni?)", "Antoni", 770, 1758, "Antoni Kotłun miesz. kras.", "Pozwany przez Jana Domaniewicza za obelgi i groźby")
add_occ("Patka", "Wojciech", "Kraśnik", "Uczciwy / Poszkodowany", "Pałka?", 770, 1758, "Woyciech Patka [Pałka?]", "Początek obdukcji ran")

# --- Skan 771 ---
add_occ("Patka", "Wojciech", "Kraśnik", "Uczciwy / Manifestant", "Pałka?", 771, 1758, "Woyciech Patka [Pałka?]", "Obdukcja siebie i żony oraz manifestacja przeciw Joachimowi Karabaszowi")
add_occ("Patkowa", "Marianna", "Kraśnik", "Żona Wojciecha Patki", "Pałkowa?", 771, 1758, "Marianna żona Woyciecha Patki", "Prezentowała sine i zapuchłe rany")
add_occ("Tokarz", "Antoni", "Kraśnik", "Sławetny / Obwiniony", "Kobiarz?", 771, 1758, "Antoni Tokarz [Kobiarz?]", "Wskazany w obdukcji Wojciecha Patki")
add_occ("Kratkowski", "Andrzej", "Kraśnik", "Sławetny / Obwiniony", "Tratkowski?", 771, 1758, "Andrzey Kratkowski", "Wskazany w obdukcji Wojciecha Patki")
add_occ("Karabasz", "Joachim", "Kraśnik", "Starozakonny / Pozwany", "Harabasz?", 771, 1758, "Joachim Karabasz [Harabasz?]", "Nie stawił się na termin i odmówił posłuszeństwa miejskiego")

# --- Skan 772 ---
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki / Deputowany", "Szubrowski?", 772, 1758, "Jan Szubertowski Ławnik krasn.", "Wizja w sprawie zaginionych gęsi u Sołeckiej")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki / Deputowany", None, 772, 1758, "Szymon Krzeszowski Ławnik krasn.", "Wizja w sprawie zaginionych gęsi u Sołeckiej")
add_occ("Kotłun", "Marcin", "Kraśnik", "Mieszczanin kraśnicki (Antoni?)", "Antoni", 772, 1758, "Antoni Kotłun Mieszczanin krasn.", "Żądał wizji o zaginione gęsi")
add_occ("Kotłunowa", "Antoniowa", "Kraśnik", "Żona Antoniego Kotłuna", None, 772, 1758, "Antoniowa Kotłunowa", "Pytała u gospodyni Sołeckiej o gęsi")
add_occ("Sołecka", "Kazimierzowa", "Kraśnik", "Gospodyni / Uczciwa", None, 772, 1758, "Kazimierzowa Sołecka", "Zabiła gęś i gotowała w kuchni")
add_occ("Zdybeł", "Antoni", "Kraśnik", "Uczciwy / Świadek", None, 772, 1758, "Antoni Zdybeł", "Trzeci świadek w sprawie gęsi")
add_occ("Kilianek", "Bartłomiej", "Kraśnik", "Uczciwy / Manifestant", None, 772, 1758, "Bartłomiey Kilianek", "Początek manifestacji")

# --- Skan 773 ---
add_occ("Kilianek", "Bartłomiej", "Kraśnik", "Manifestant", None, 773, 1758, "Bartłomiey Kilianek", "Manifestacja przeciw młynarzowi Jakubowi Bieleckiemu o skrwawione oko")
add_occ("Bielecki", "Jakub", "Kraśnik", "Młynarz grobelny / Pozwany", None, 773, 1758, "Jakub Bielecki młynarz Grobelny", "Nie stanął, powołując się na jurysdykcję dworską")
add_occ("Tarnawski", "Jakub", "Kraśnik", "Mieszczanin kraśnicki / Dłużnik", None, 773, 1758, "Jakub Tarnawski mieszczanin krasnicki", "Winien 17 złp Grzegorzowi Rycerzowi; sprzedał futro Anklowi za 20 złp")
add_occ("Rycerz", "Grzegorz", "Kraśnik", "Mieszczanin kraśnicki / Wierzyciel", None, 773, 1758, "Grzegorz Rycerz mieszczanin krasnicki", "Wierzyciel na 17 złp z zapisu Jakuba Tarnawskiego")
add_occ("Ankel", "Rzeźnik", "Kraśnik", "Starozakonny / Obywatel kraśnicki", "Anzelm?", 773, 1758, "niewierny Ankel Rzeźnik obyw. krasn.", "Kupił futro za 20 złp z obowiązkiem spłaty 17 złp Rycerzowi")

# --- Skan 774 ---
add_occ("Ankel", "Rzeźnik", "Kraśnik", "Starozakonny", "Anzelm?", 774, 1758, "Ankel", "Zapis wadium 3 złp na termin zapłaty")
add_occ("Słamowicz", "Junkiel", "Kraśnik", "Obywatel kraśnicki / Podpisujący", None, 774, 1758, "Junkiel Słamowicz obyw. krasnicki", "Własnoręczny podpis pod zapisem")
add_occ("Nautyl", "Starozakonny", "Kraśnik", "Wierzyciel", "Nawtul?", 774, 1758, "starozakonny Nautyl", "Kwituje Sebestyana Pawlickiego z długu po Janie Ciurce (2 korce żyta i 1 ćwierć)")
add_occ("Ciurka", "Jan", "Przedmieście Kraśnickie", "Zmarły dłużnik", "Ciurko", 774, 1758, "Jan Ciurka", "Dług opisany w testamencie")
add_occ("Pawlicki", "Sebastian", "Kraśnik", "Zięć Jana Ciurki", None, 774, 1758, "Sobestyan Pawlicki", "Spłacił zbożem dług teścia u Nautyla")
add_occ("Buś", "Wojciech", "Kraśnik", "Sławetny", "Bus?", 774, 1758, "Woyciech Buś", "Wymieniony przy areszcie na niwkę Techo")
add_occ("Grzętka", "Matyasz", "Kraśnik", "Mieszkaniec", None, 774, 1758, "Matyasz Grzętka", "Wymieniony przy areszcie na niwkę Techo")

# --- Skan 775 ---
add_occ("Zadel", "Adam", "Kraśnik", "Ławnik kraśnicki / Manifestant", "Żadło?", 775, 1758, "Adam Zadel Ławnik krasn.", "Manifestacja przeciw Marcinowi Morelowi o krwawe pobicie na gospodzie")
add_occ("Morel", "Marcin", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", None, 775, 1758, "Marcin Morel mies. krasn.", "Uderzył w gębę ławnika Adama Zadela aż do krwi")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Burmistrz kraśnicki / Manifestant", None, 775, 1758, "Łukasz Krzeszowski Bur. krasn.", "Manifestacja przeciw Wojciechowi Busiowi o podkupienie niwki Sołeckiej")
add_occ("Buś", "Wojciech", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", "Bus?", 775, 1758, "Woyciech Buś miesz. krasn.", "Pozwany o podkupienie niwki u nieboszczki Sołeckiej")
add_occ("Sołecka", "Kazimierzowa", "Kraśnik", "Nieboszczka", None, 775, 1758, "nieboszczka Sołecka", "Zbyła niwkę burmistrzowi Łukaszowi Krzeszowskiemu")
add_occ("Dzierżawski", "Wielmożny Imć Pan", "Kraśnik", "Urzędnik / Zwierzchność", None, 775, 1758, "Wiel. Imć Pan Dzierżawski [?]", "Rozkazał wystawić pod słup na 3 dni")

# Zapis gen_data_j17_part31.json
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part31.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part31.json ({len(gen_data)} profiles) and CSV exported.")
