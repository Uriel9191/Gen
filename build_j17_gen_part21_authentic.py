# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part20.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w Partii 21 (skany 501–525) Jednostki 17 (sygn. 35/40/0/1/17) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 501 ---
add_occ("Pałka", "Łukasz", "Kraśnik", "Mieszczanin / Strona w procesie", None, 501, 1757, "Pałka", "Zakończenie manifestacji przeciw Wojciechowi Cwiece")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona w sporze", None, 501, 1757, "Wojciech Cwieka", "Pozwany w manifestacji Łukasza Pałki")
add_occ("Lubrzyński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 501, 1757, "Antoni Lubrzyński Ławnik Kraś.", "Manifestacja przeciw Kazimierzowi Młynarskiemu o spalenie dekretu")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 501, 1757, "Kazimierz Młynarski Cechmistrz Kunsztu Szewskiego", "Oskarżony o spalenie dekretu oraz w manifestacji Adama Posuniaka")
add_occ("Posuniak", "Adam", "Kraśnik", "Mistrz szewski / Mieszczanin", None, 501, 1757, "Adam Posuniak", "Manifestacja przeciw Kazimierzowi Młynarskiemu o zakup skór")
add_occ("Posuniak", "Michał", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 501, 1757, "Michał [Mikołaj?] Posuniak", "Wspomniany w dekrecie między braćmi Posuniakami")
add_occ("Koza", "Wojciech", "Kraśnik", "Mieszkaniec / Świadek", None, 501, 1757, "Wojciech Koza", "Zeznał, że sprzedał skóry Adamowi Posuniakowi, nie Stachowiczowi")
add_occ("Stachowicz", "Wojciech", "Kraśnik", "Mistrz szewski", None, 501, 1757, "Wojciech Stachowicz", "Spór o skóry kupione od Wojciecha Kozy")

# --- Skan 502 (i dublet 503) ---
add_occ("Posuniak", "Adam", "Kraśnik", "Mistrz szewski / Mieszczanin", None, 502, 1757, "Adam Posuniak", "Zakończenie manifestacji przeciw Kazimierzowi Młynarskiemu")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 502, 1757, "Kazimierz Młynarski Cechmistrz", "Oskarżony o odsądzenie od skór i koszty")
add_occ("Krzywiński", "Michał", "Kraśnik", "Wójt kraśnicki", None, 502, 1757, "Michał Krzywiński Wójt Kraś.", "Manifestacja przeciw Wawrzyńcowi Starobratowi o zniewagę na sesji")
add_occ("Starobrat", "Wawrzyniec", "Kraśnik", "Mieszczanin / Strona w sporze", None, 502, 1757, "Wawrzyniec Starobrat", "Manifestacja przeciw wójtowi o przyjmowanie pretensji Nowaka (50 złp, 10 złp)")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Strona w sporze", None, 502, 1757, "Mikołaj Nowak", "Pretensje do Wawrzyńca Starobrata (50 złp i 10 złp)")

# --- Skan 504 ---
add_occ("Starobrat", "Wawrzyniec", "Kraśnik", "Mieszczanin / Strona w sporze", None, 504, 1757, "Wawrzyniec Starobrat", "Manifestacja przeciw ojczymowi Mikołajowi Nowakowi")
add_occ("Krzywiński", "Michał", "Kraśnik", "Wójt kraśnicki", None, 504, 1757, "Michał Krzywiński Wójt Kraś.", "Zakończenie manifestacji Wawrzyńca Starobrata")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Ojczym Starobrata", None, 504, 1757, "Mikołaj Nowak Ojczym", "Pozwany w manifestacji pasierba Wawrzyńca Starobrata")
add_occ("Lubartowski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 504, 1757, "Jan Lubartowski Ławnik Kraś.", "Aktor w sprawie przeciw Augustynowi Piaseckiemu o 6 korcy żyta")
add_occ("Piasecki", "Augustyn", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona w sporze", None, 504, 1757, "Augustyn Piasecki", "Dekret nakazujący przysięgę z żoną w sprawie żyta z młyna")
add_occ("Kowalik", "Mikołaj", "Kraśnik", "Żyd we młynie / Młynarz?", None, 504, 1757, "Mikołaj Kowalik Żyd we młynie", "W jego młynie zginęło sześć korcy żyta żydowskiego")

# --- Skan 505 ---
add_occ("Starobrat", "Wawrzyniec", "Kraśnik", "Mieszczanin / Strona w sporze", None, 505, 1757, "Wawrzyniec Starobrat", "Wyrok w sporze z Mikołajem Nowakiem (17 złp, 13 złp 15 gr, 8 złp 20 gr)")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Strona w sporze", None, 505, 1757, "Mikołaj Nowak", "Wyrok nakazujący zwrot 8 złp 20 gr i 2 grzywien; manifestacja na marginesie")

# --- Skan 506 ---
add_occ("Pałka", "Łukasz", "Kraśnik", "Mieszczanin / Strona w procesie", None, 506, 1757, "Łukasz Pałka", "Manifestacja przeciw Wojciechowi Cwiece o niedopuszczenie do przysięgi Nowaka")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona w sporze", None, 506, 1757, "Wojciech Cwieka", "Pozwany w manifestacji Łukasza Pałki")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Strona w sporze", None, 506, 1757, "Mikołaj Nowak", "Niedopuszczony do przysięgi przez Cwiekę")
add_occ("Radkowski", "Józef", "Kraśnik", "Mieszczanin / Poszkodowany", None, 506, 1757, "Józef Radkowski", "Manifestacja przeciw Bartłomiejowi Czelejowi o podejrzenie spalenia Młyna na Grebieniu")
add_occ("Czelej", "Bartłomiej", "Przedmieście Kraśnickie", "Przedmieszczanin / Podejrzany", "Celec?", 506, 1757, "Bartłomiej Czelej [Celec? / Czelej?]", "Oskarżony o groźby podpalenia i podejrzenie spalenia młyna na Grebieniu")

# --- Skan 507 ---
add_occ("Radkowski", "Józef", "Kraśnik", "Mieszczanin / Poszkodowany", None, 507, 1757, "Józef Radkowski", "Zakończenie manifestacji przeciw Bartłomiejowi Czelejowi")
add_occ("Czelej", "Bartłomiej", "Przedmieście Kraśnickie", "Przedmieszczanin / Podejrzany", "Celec?", 507, 1757, "Bartłomiej Czelej [Celec? / Czelej?]", "Zakończenie manifestacji Radkowskiego")
add_occ("Radkowski", "Jan", "Przedmieście Zarzecze", "Przedmieszczanin / Strona w sporze", None, 507, 1757, "Jan Radkowski", "Pozwany przez pospólstwo Zarzecza o przyprowadzenie zapowietrzonego bydła")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 507, 1757, "Szymon Krzeszowski Ławnik Kraś.", "Aktor przeciw Antoniemu Lubrzyńskiemu i Kazimierzowi Młynarskiemu")
add_occ("Lubrzyński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 507, 1757, "Antoni Lubrzyński Ławnik Kraś.", "Uznany winnym wzniecenia kłótni o spalenie dekretu")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 507, 1757, "Kazimierz Młynarski Cechmistrz Pierwszy Szewskiego Kunsztu", "Pozwany w dekrecie w sprawie Krzeszowskiego")
add_occ("Dobrowolski", "Jan", "Kraśnik", "Mieszkaniec / Świadek", None, 507, 1757, "Jan Dobrowolski", "Wyznał prawdę przed Kazimierzem Młynarskim w sprawie dekretu")

# --- Skan 508 ---
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 508, 1757, "Szymon Krzeszowski", "Zakończenie wyroku z Lubrzyńskim i Młynarskim")
add_occ("Lubrzyński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 508, 1757, "Antoni Lubrzyński", "Skazany na 1 grzywnę aktorowi, 5 grzywien sądowi i deprekację")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 508, 1757, "Kazimierz Młynarski", "Strona w dekrecie, przyjął wyrok")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona w sporze", None, 508, 1757, "Wojciech Cwieka", "Manifestacja przeciw Łukaszowi Pałce o przysięgę")
add_occ("Pałka", "Łukasz", "Kraśnik", "Mieszczanin / Strona w procesie", None, 508, 1757, "Łukasz Pałka", "Pozwany w manifestacji Wojciecha Cwieki")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Strona w sporze", None, 508, 1757, "Mikołaj Nowak", "Wspomniany w sporze przysięgowym Cwieki z Pałką")
add_occ("Jazdyk", "Grzegorz", "Kraśnik", "Mieszczanin / Strona w sporze", None, 508, 1757, "Grzegorz Jazdyk", "Aktor przeciw Jackowi Jazdykowi")

# --- Skan 509 ---
add_occ("Jazdyk", "Grzegorz", "Kraśnik", "Mieszczanin / Strona w sporze", None, 509, 1757, "Grzegorz Jazdyk", "Dylacja na obrachunek przez 2 ludzi z Jackiem Jazdykiem")
add_occ("Jazdyk", "Jacek", "Kraśnik", "Mieszczanin / Strona w sporze", None, 509, 1757, "Jacek Jazdyk", "Pozwany przez Grzegorza Jazdyka o różne pretensje")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik kraśnicki", None, 509, 1757, "Szymon Krzeszowski Ławnik Kraś.", "Deputowany do aresztu w domu Mośka piekarza")
add_occ("Mosiek", "Starozakonny", "Kraśnik", "Piekarz starozakonny", None, 509, 1757, "Mosiek piekarz", "Areszt w jego domu na instancję Maciejowej Pietruszkowej")
add_occ("Pietruszkowa", "Maciejowa", "Kraśnik", "Mieszkanka / Strona w sporze", None, 509, 1757, "Maciejowa Pietruszkowa", "Instancja do aresztu w domu Mośka piekarza za 1,5 korca pszenicy")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Strona w sporze", None, 509, 1757, "Mikołaj Nowak", "Manifestacja przeciw Wojciechowi Cwiece o niedopuszczenie do juramentu")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona w sporze", None, 509, 1757, "Wojciech Nowak Cwieka", "Pozwany w manifestacji Mikołaja Nowaka")

# --- Skan 510 ---
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Strona w sporze", None, 510, 1757, "Mikołaj Nowak", "Zakończenie manifestacji przeciw Cwiece (czekał od rana do 11:00)")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona w sporze", None, 510, 1757, "Wojciech Cwieka", "Niestawiennictwo do juramentu")
add_occ("Świdziński", "Wojciech", "Kraśnik", "Młynarczyk Młyna Grebieńskiego", None, 510, 1757, "Wojciech Świdziński Młynarczyk służący Młyna Grebieńskiego", "Zeznanie pod sumieniem o spaleniu Młyna Grebieńskiego przez pijanego Żyda piekarza")

# --- Skan 511 ---
add_occ("Świdziński", "Wojciech", "Kraśnik", "Młynarczyk Młyna Grebieńskiego", None, 511, 1757, "Wojciech Świdziński Młynarczyk", "Zakończenie zeznania o ucieczce tylnymi drzwiami z płonącego młyna")
add_occ("Posuniak", "Adam", "Kraśnik", "Mistrz szewski / Mieszczanin", None, 511, 1757, "Adam Posuniak", "Dylacja ze Stachowiczem o podkupienie skór u Kozy (2 złp)")
add_occ("Stachowicz", "Wojciech", "Kraśnik", "Mistrz szewski", None, 511, 1757, "cech Stachowicz Majster kunsztu szewskiego", "Spór z Posuniakiem o podkupienie skór")
add_occ("Koza", "Wojciech", "Kraśnik", "Mieszkaniec / Sprzedawca skór", None, 511, 1757, "Wojciech Koza", "Sprzedaż skór (2 złp)")
add_occ("Gacek", "Antoni", "Kraśnik", "Mieszkaniec / Poręczyciel", None, 511, 1757, "Antoni Gacek", "Bierze na porękę ojczyma Marcina Kozę w sprawie ze Stanisławem Wójcikiem")
add_occ("Koza", "Marcin", "Kraśnik", "Mieszkaniec / Ojczym Gacka", None, 511, 1757, "Marcin Koza Ojczym", "Wzięty na porękę przez pasierba Antoniego Gacka")
add_occ("Wójcik", "Stanisław", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona w sporze", None, 511, 1757, "Stanisław Wójcik", "Odbiorca zadośćuczynienia od Marcina Kozy")

# --- Skan 512 ---
add_occ("Kozyna", "Józefowa", "Kraśnik", "Mieszkanka / Poszkodowana", None, 512, 1757, "Józefowa Kozyna", "Obdukcja pobitych ran w obecności męża, oskarża Stanisława Kowalika")
add_occ("Kowalik", "Stanisław", "Kraśnik", "Magister kunsztu szewskiego", None, 512, 1757, "Stanisław Kowalik kunsztu szewskiego magister", "Oskarżony o ciężkie pobicie Józefowej Kozyny")
add_occ("Pilaszkiewicz", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 512, 1757, "Antoni Pilaszkiewicz Ław. Kraś.", "Obecny przy obdukcji Józefowej Kozyny")

# --- Skan 513 ---
add_occ("Stachowicz", "Wojciech", "Kraśnik", "Mieszczanin i magister szewski", None, 513, 1757, "Wojciech Stachowicz mieszczanin kraś. kunsztu szewskiego magister", "Manifestacja przeciw Adamowi Posuniakowi o apelację do dworu stróżkiego i zabór 4 skór")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin i magister szewski", None, 513, 1757, "Adam Posuniak mieszczanin kraś. tegoż kunsztu szewskiego magister", "Oskarżony o sprowadzenie służby dworskiej i zabór 4 skór wołowych")

# --- Skan 514 ---
add_occ("Stachowicz", "Wojciech", "Kraśnik", "Mieszczanin i magister szewski", None, 514, 1757, "Wojciech Stachowicz kunsztu szewskiego magister", "Zakończenie manifestacji przeciw Posuniakowi oraz manifestacja przeciw Lubrzyńskiemu")
add_occ("Lubrzyński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 514, 1757, "Antoni Lubrzyński Ławnik Kraś.", "Oskarżony przez Stachowicza o wyparcie się wiedzy o Posuniaku")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin i magister szewski", None, 514, 1757, "Adam Posuniak", "Wspomniany w manifestacji Stachowicza przeciw Lubrzyńskiemu")
add_occ("Cwieka", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona w sporze", None, 514, 1757, "Wojciech Cwieka", "Ugoda z Mikołajem Nowakiem, zapłata 1 grzywny sądowi")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Strona w sporze", None, 514, 1757, "Mikołaj Nowak", "Kwituje Wojciecha Cwiekę pod zakładem 12 grzywien")

# --- Skan 515 ---
add_occ("Posuniakowa", "Adamowa", "Kraśnik", "Mieszkanka / Pełnomocniczka chorego męża", None, 515, 1757, "Adamowa Posuniakowa", "Areszt na świadkach Młynarskiego oraz manifestacje przeciw Okoniowi")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin i magister szewski", None, 515, 1757, "Adam Posuniak chory mąż", "Ciężko chory w domu po pobiciu na gospodzie")
add_occ("Młynarski", "Kazimierz", "Kraśnik", "Cechmistrz szewski", None, 515, 1757, "Kazimierz Młynarski", "Stawiał świadków objętych aresztem Posuniakowej")
add_occ("Okoń", "Antoni", "Kraśnik", "Sławetny / Mieszczanin", None, 515, 1757, "Antoni Okoń", "Oskarżony o pobicie Adama Posuniaka na gospodzie")

# --- Skan 516 ---
add_occ("Surowicki", "Jędrzej", "Kraśnik", "Sługa miejski kraśnicki", None, 516, 1757, "Jędrzej Surowicki Sługa Miejski Kraś.", "Aktor z żoną przeciw Baltazarowi Kaczmarskiemu o pobicie")
add_occ("Surowicka", "Jadwiga", "Kraśnik", "Żona sługi miejskiego (z domu Kaczmarska / 1v. Biegonowa)", None, 516, 1757, "żona Jędrzeja Surowickiego", "Pobita i spoliczkowana przez brata Baltazara Kaczmarskiego")
add_occ("Kaczmarski", "Baltazar", "Kraśnik", "Mieszczanin / Strona w sporze", None, 516, 1757, "Baltazar Kaczmarski", "Skazany na 4 grzywny sądowi, 2 stronie i 2 dni aresztu; dylacja z siostrą")
add_occ("Rypkowski", "Jan", "Kraśnik", "Pisarz miejski?", "Rypkowski?", 516, 1757, "Johannes Rypkowski [Rypkowski?]", "Podpisany pod dekretem Surowickiego z Kaczmarskim")
add_occ("Zdyb", "Bartłomiej", "Kraśnik", "Mieszczanin / Strona w sporze", None, 516, 1757, "Bartłomiej Zdyb", "Manifestacja przeciw Adamowi Posuniakowi o bezprawny areszt gruntu")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin i magister szewski", None, 516, 1757, "Adam Posuniak", "Pozwany w manifestacji Bartłomieja Zdyba")

# --- Skan 517 ---
add_occ("Surowicki", "Jędrzej", "Kraśnik", "Sługa miejski kraśnicki", None, 517, 1757, "Jędrzej Surowicki Sługa miejski", "Manifestacja z żoną Jadwigą przeciw Baltazarowi Kaczmarskiemu o sukcesję")
add_occ("Surowicka", "Jadwiga", "Kraśnik", "Żona sługi miejskiego (z domu Kaczmarska / 1v. Biegonowa)", None, 517, 1757, "Jadwiga Biegonowa niegdyś Pawła Biegona pozostała małżonka z domu Kaczmarska", "Manifestacja przeciw bratu o zagarnięcie sukcesji po rodzicach")
add_occ("Biegon", "Paweł", "Kraśnik", "Zmarły pierwszy mąż Jadwigi", None, 517, 1757, "niegdyś Paweł Biegon", "Wspomniany jako pierwszy zmarły mąż Jadwigi Surowickiej")
add_occ("Kaczmarski", "Baltazar", "Kraśnik", "Mieszczanin / Strona w sporze", None, 517, 1757, "Baltazar Kaczmarski Brat rodzony", "Pozwany o zagarnięcie sukcesji po rodzicach")
add_occ("Stankowski", "Stanisław", "Kraśnik", "Ławnik kraśnicki", None, 517, 1757, "Stanisław Stankowski Ławnik Kraś.", "Manifestacja przeciw Jakóbowi Stankowskiemu o podatek kahałny i obelgę")
add_occ("Stankowski", "Jakób", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 517, 1757, "Jakób Stankowski", "Pozwany w manifestacji Stanisława Stankowskiego")

# --- Skan 518 ---
add_occ("Stankowski", "Stanisław", "Kraśnik", "Ławnik kraśnicki", None, 518, 1757, "Stanisław Stankowski", "Zakończenie manifestacji przeciw Jakóbowi Stankowskiemu")
add_occ("Stankowski", "Jakób", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 518, 1757, "Jakób Stankowski", "Oskarżony o zarzucanie złodziejstwa")
add_occ("Jazdykowa", "Wojciechowa", "Kraśnik", "Mieszkanka / Poszkodowana", None, 518, 1757, "Wojciechowa Jazdykowa", "Obdukcja ran (drapanie, sinice) zadanych przez Ewę Błażejową; wspomniana przy błocie")
add_occ("Błażejowa", "Ewa", "Kraśnik", "Mieszkanka u Mikołaja Nowaka", None, 518, 1757, "Ewa Błażejowa u Mikołaja Nowaka", "Oskarżona o pobicie Wojciechowej Jazdykowej")
add_occ("Nowak", "Mikołaj", "Kraśnik", "Mieszczanin / Gospodarz", None, 518, 1757, "Mikołaj Nowak", "Manifestacja przeciw Józefowej Żołądkowej o rzucenie błotem")
add_occ("Żołądkowa", "Józefowa", "Kraśnik", "Mieszkanka / Strona w sporze", None, 518, 1757, "Józefowa Żołądkowa", "Oskarżona o rzucenie błotem na Mikołaja Nowaka")
add_occ("Pinkwasowicz", "Mosiek", "Kraśnik", "Obywatel kraśnicki (starozakonny)", None, 518, 1757, "Niew. Mosiek Pinkwasowicz Obywatel Kraśnicki", "Daje plenipotencję bratu rodzonemu Szłomie Pinkwasowiczowi")
add_occ("Pinkwasowicz", "Szłoma", "Zamość", "Obywatel zamojski / Pełnomocnik", None, 518, 1757, "Szłoma Brat rodzony", "Odbiera plenipotencję od brata Mośka")

# --- Skan 519 ---
add_occ("Pinkwasowicz", "Mosiek", "Kraśnik", "Obywatel kraśnicki (starozakonny)", None, 519, 1757, "Mosiek Pinkwasowicz", "Plenipotencja do Sądu Komisarskiego Zamku Zamoyskiego")
add_occ("Pinkwasowicz", "Szłoma", "Zamość", "Obywatel zamojski / Pełnomocnik", None, 519, 1757, "Szłoma Pinkwasowicz Obywatel Zamojski", "Pełnomocnik w sprawie z Aronem Lejbowiczem przed Sądem Zamku Zamoyskiego")
add_occ("Lejbowicz", "Aron", "Kraśnik", "Obywatel kraśnicki (starozakonny)", None, 519, 1757, "Niewierny Aron Lejbowicz Obywatel Kraśnicki", "Strona pozwana przed Sądem Komisarskim Zamku Zamoyskiego")
add_occ("Marszałkowski", "Szymon", "Kraśnik", "Sławetny / Mieszczanin", None, 519, 1757, "Szymon Marszałkowski", "Manifestacja przeciw braciom Kawkom o 22-letni zastaw niwki Błuczorskiej")
add_occ("Kawka", "Maciej", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona w sporze", None, 519, 1757, "Maciej Kawka brat rodzony", "Pozwany o oranie zastawionej niwki Błuczorskiej mimo aresztu")
add_occ("Kawka", "Mikołaj", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 519, 1757, "Mikołaj Kawka brat rodzony", "Pozwany wraz z bratem Maciejem o niwkę Błuczorską")

# --- Skan 520 ---
add_occ("Marszałkowski", "Szymon", "Kraśnik", "Sławetny / Mieszczanin", None, 520, 1757, "Szymon Marszałkowski", "Manifestacja przeciw Grzegorzowi Pilaszkiewiczowi o kopanie na gruncie Kofeckiego")
add_occ("Pilaszkiewicz", "Grzegorz", "Kraśnik", "Rady starszej / Mieszczanin", None, 520, 1757, "Grzegorz Pilaszkiewicz rady starszej", "Oskarżony o bezprawne kopanie na gruncie Kofeckiego")
add_occ("Kofecki", "Jan", "Kraśnik", "Mieszkaniec / Zastawnik", None, 520, 1757, "Jan Kofecki", "Trzyma w zastawie grunt od Szymona Marszałkowskiego")
add_occ("Zdyb", "Bartłomiej", "Kraśnik", "Mieszczanin / Strona w sporze", None, 520, 1757, "Bartłomiej Zdyb", "Dylacja z Adamem Posuniakiem na okazanie dokumentów i testamentu")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin i magister szewski", None, 520, 1757, "Adam Posuniak", "Dylacja z Bartłomiejem Zdybem o wywód dziedziny i testament")

# --- Skan 521 ---
add_occ("Kuśnierz", "Andrzej", "Kraśnik", "Woźny przysięgły kraśnicki", "Kuśmierek?", 521, 1757, "Andreas Kusnierz [Kuśnierz / Kuśmierek?] Ministerialis Juratus Crasn.", "Relacja o położeniu pozwu z Sądu Komisarskiego Zamku Zamoyskiego")
add_occ("Aronowicz", "Szloma", "Bełżyce", "Obywatel bełżycki (starozakonny)", None, 521, 1757, "Infidelis Szloma Aronowicz Incola Bełżycensis", "Powód w mandacie Sądu Komisarskiego Zamku Zamoyskiego (26 IV 1757)")
add_occ("Zamoyski", "Jan Jakub", "Zamość", "Ordynat zamojski / Starosta lubelski i rostocki", None, 521, 1757, "Jan Jakub z Zamościa Zamoyski", "Wystawca mandatu opiekuńczego Ordynacji Zamoyskiej")
add_occ("Granowski", "Jan Aleksander", "Zamość / Lwów", "Doktor obojga praw, Kanonik lwowski, Dziekan infułat zamojski", None, 521, 1757, "Jan Alexander z Granowa Granowski", "Współopiekun Ordynacji Zamoyskiej")
add_occ("Dzierżanowski", "Franciszek Grzymała", "Zamość", "Łowczy ziemi łukowskiej, Burgrabia Ordynacji Zamoyskiej", None, 521, 1757, "Franciszek Grzymała Dzierżanowski", "Współopiekun Ordynacji Zamoyskiej")
add_occ("Radkowski", "Krzysztof", "Kraśnik", "Obywatel kraśnicki / Pozwany", "Radkowski?", 521, 1757, "Krzysztof Radkowski [Radkowski?] Obywatel Kraś.", "Pozwany przed Sąd Komisarski Zamku Zamoyskiego na 26 IV 1757 r.")

# --- Skan 522 ---
add_occ("Aronowicz", "Szloma", "Bełżyce", "Obywatel bełżycki (starozakonny)", None, 522, 1757, "Szloma Aronowicz", "Zakończenie pozwu o dług ze wspólnego handlu zbożem")
add_occ("Zdyb", "Bartłomiej", "Kraśnik", "Mieszczanin / Strona w sporze", None, 522, 1757, "Bartłomiej Zdyb", "Spór z córką Jakubową Węgorkową i zięciem o 40 złp na wesele")
add_occ("Węgorkowa", "Jakubowa", "Kraśnik", "Córka Bartłomieja Zdyba", None, 522, 1757, "Jakubowa Węgorkowa", "Pozwana o 40 złp pożyczonych na jej wesele")
add_occ("Węgorek", "Jakub", "Kraśnik", "Zięć Bartłomieja Zdyba", None, 522, 1757, "Jakub Węgorek", "Wezwany do osobistego przyznania długu 40 złp z Posuniakiem")
add_occ("Posuniak", "Adam", "Kraśnik", "Mieszczanin i magister szewski", None, 522, 1757, "Adam Posuniak", "Wspomniany przy pożyczce 40 złp na wesele Węgorkowej")

# --- Skan 523 ---
add_occ("Zdyb", "Bartłomiej", "Kraśnik", "Mieszczanin / Strona w sporze", None, 523, 1757, "Bartłomiej Zdyb", "Zakończenie dylacji z córką Jakubową Węgorkową (posesja izby)")
add_occ("Węgorkowa", "Jakubowa", "Kraśnik", "Córka Bartłomieja Zdyba", None, 523, 1757, "Jakubowa Węgorkowa", "Spór o izbę")
add_occ("Posuniak", "Wawrzyniec", "Kraśnik", "Tokarz / Mieszczanin", None, 523, 1757, "Wawrzyniec Posuniak tokarz", "Dylacja z Marcinem Kudryńskim o ugodę na chałupkę z gruntem; pozwany przez Szafrańskiego")
add_occ("Kudryński", "Marcin", "Kraśnik", "Mieszkaniec / Strona w sporze", "Kudryński?", 523, 1757, "Marcin Kudryński [Kudryński?]", "Dylacja na stawienie świadectwa co do chałupki z gruntem")
add_occ("Szafrański", "Antoni", "Przedmieście Góry i Podlesie", "Przedmieszczanin / Strona w sporze", None, 523, 1757, "Antoni Szafrański", "Spór z pospólstwem o ćwierć pola Koperowską na Podlesiu oraz manifestacja z żoną o pobicie")
add_occ("Szafrański", "Tomasz", "Przedmieście Góry i Podlesie", "Przedmieszczanin / Strona w sporze", None, 523, 1757, "Tomasz Szafrański", "Współpowód z Antonim Szafrańskim o ćwierć pola na Podlesiu")
add_occ("Jordyk", "Augustyn", "Kraśnik", "Mieszkaniec / Pozwany", "Jazdyk?", 523, 1757, "Augustyn Jordyk [Jordyk / Jazdyk?]", "Oskarżony wraz z Wawrzyńcem Posuniakiem o pobicie Antoniego Szafrańskiego")

# --- Skan 524 ---
add_occ("Szafrański", "Antoni", "Przedmieście Góry i Podlesie", "Przedmieszczanin / Poszkodowany", None, 524, 1757, "Antoni Szafrański", "Zakończenie manifestacji z krwawą raną od noża przeciw Posuniakowi i Jordykowi")
add_occ("Posuniak", "Wawrzyniec", "Kraśnik", "Tokarz / Mieszczanin", None, 524, 1757, "Wawrzyniec Posuniak", "Oskarżony o wyzwanie nożem i pobicie Szafrańskiego")
add_occ("Jordyk", "Augustyn", "Kraśnik", "Mieszkaniec / Pozwany", "Jazdyk?", 524, 1757, "Augustyn Jordyk [Jordyk / Jazdyk?]", "Oskarżony o kilkukrotne uderzenie w głowę Szafrańskiego")
add_occ("Marszałkowski", "Szymon", "Kraśnik", "Sławetny / Mieszczanin", None, 524, 1757, "Szymon Marszałkowski", "Wyrok przeciw braciom Kawkom o niwkę Błuczorską (110 złp, 95 złp do zwrotu)")
add_occ("Kawka", "Maciej", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona w sporze", None, 524, 1757, "Maciej Kawka brat rodzony", "Wyrok nakazujący ustąpienie z niwki Błuczorskiej za 95 złp")
add_occ("Kawka", "Mikołaj", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 524, 1757, "Mikołaj Kawka brat rodzony", "Wyrok nakazujący ustąpienie z niwki Błuczorskiej")

# --- Skan 525 ---
add_occ("Marszałkowski", "Szymon", "Kraśnik", "Sławetny / Mieszczanin", None, 525, 1757, "Szymon Marszałkowski", "Zakończenie wyroku z Kawkami (apelacja do Trybunału Zamojskiego) oraz areszt konwentu")
add_occ("Kawka", "Maciej", "Przedmieście Kraśnickie", "Przedmieszczanin / Strona w sporze", None, 525, 1757, "Maciej Kawka", "Zakończenie wyroku o niwkę Błuczorską")
add_occ("Kawka", "Mikołaj", "Kraśnik", "Mieszkaniec / Strona w sporze", None, 525, 1757, "Mikołaj Kawka", "Zakończenie wyroku o niwkę Błuczorską")
add_occ("Kuciński", "Sławetny", "Kraśnik", "Mieszczanin / Strona w rozliczeniu", None, 525, 1757, "Sław. Kuciński", "Pieniądze za niego odbierane przez Marszałkowskiego objęte aresztem konwentu")
add_occ("Bielecki", "Szymon", "Kraśnik", "Mieszczanin / Właściciel gruntu", None, 525, 1757, "Szymon Bielecki", "Wizja na jego gruncie kupionym od Agnieszki Makondyszowej i Stanisława Pańczyka")
add_occ("Makondyszowa", "Agnieszka", "Kraśnik", "Mieszkanka / Poprzednia właścicielka", None, 525, 1757, "Agnieszka Makondyszowa", "Poprzednia właścicielka gruntu kupionego przez Szymona Bieleckiego")
add_occ("Pańczyk", "Stanisław", "Kraśnik", "Mularz / Poprzedni właściciel", None, 525, 1757, "Stanisław Pańczyk Mularz", "Sprzedawca gruntu Szymonowi Bieleckiemu")
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Ślusarz / Sąsiad", None, 525, 1757, "Jakub Wojciechowski ślusarz", "Wszedł na sznur gruntu Szymona Bieleckiego podczas ogrodzenia")
add_occ("Lubrzyński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 525, 1757, "Antoni Lubrzyński Ław. Kraś.", "Świadek wizji gruntowej Szymona Bieleckiego")

# Weryfikacja braku duplikatów (Wariant 2)
keys = [(p['nazwisko'], p['imie'], p['miejsce']) for p in gen_data]
assert len(keys) == len(set(keys)), "DUPLICATE IDENTITY DETECTED!"
for p in gen_data:
    assert p.get('funkcja'), f"EMPTY ROLE: {p}"

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part21.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part21.json ({len(gen_data)} profiles) and CSV exported.")
