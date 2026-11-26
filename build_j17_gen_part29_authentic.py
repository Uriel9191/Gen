# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part28.json', 'r', encoding='utf-8') as f:
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
            "notatka_biograficzna": f"Osoba odnotowana w Partii 29 (skany 701–725) Jednostki 17 (sygn. 35/40/0/1/17) jako: {zapis} ({kwota_ctx})."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# --- Skan 701 ---
add_occ("Pyryk", "Antoni", "Kraśnik", "Uczciwy / Powód i skazany", None, 701, 1758, "Antoni Pyryk", "Dekret z parobkami: 12 grzywien sądowi per medium za samosąd")
add_occ("Tokarz", "Wojciech", "Kraśnik", "Parobek / Pozwany", None, 701, 1758, "Woyciech Tokarz", "Współpozwany w sprawie Pyryka (4 grzywny na parobków)")
add_occ("Wolak", "Stanisław", "Przedmieście Kraśnickie", "Parobek / Pozwany", None, 701, 1758, "Stanisław Wolak", "Współpozwany w sprawie Pyryka")
add_occ("Fś", "Andrzej", "Kraśnik", "Parobek / Pozwany", None, 701, 1758, "Andrzey Fś", "Współpozwany w sprawie Pyryka")
add_occ("Kilianek", "Piotr", "Kraśnik", "Parobek / Pozwany", None, 701, 1758, "Piotr Kilianek", "Współpozwany w sprawie Pyryka")
add_occ("Jarduk", "Józef", "Kraśnik", "Parobek / Pozwany", None, 701, 1758, "Jozef Jarduk", "Współpozwany w sprawie Pyryka")

# --- Skan 702 ---
add_occ("Łapka", "Maciej", "Kraśnik", "Uczciwy / Powód", None, 702, 1758, "Maciey Łapka", "Proces przeciw Bieńdzie i Kiliankowi o spasienie kopy siana (3 złp)")
add_occ("Bieńda", "Paweł", "Przedmieście Kraśnickie", "Przedmieszczanin / Pozwany", "Bienda?", 702, 1758, "Paweł Bienda [Bieńda?]", "Skazany na 3 złp za szkodę w sianie i 1 grzywnę")
add_occ("Kilianek", "Piotr", "Kraśnik", "Przedmieszczanin / Pozwany", None, 702, 1758, "Piotr Kilianek", "Współskazany za spasienie kopy siana")
add_occ("Nowacki", "Mikołaj", "Kraśnik", "Manifestant", None, 702, 1758, "Mikołay Nowacki", "Manifestacja przeciw Antoniemu Pałce o kwartę gorzałki")
add_occ("Pałka", "Antoni", "Kraśnik", "Przedmieszczanin / Pozwany", None, 702, 1758, "Antoni Pałka", "Pozwany w manifestacji Mikołaja Nowackiego")

# --- Skan 703 ---
add_occ("Łypa", "Andrzej", "Kraśnik", "Uczciwy / Powód", None, 703, 1758, "Andrzey Łypa", "Interogatoria i proces przeciw Augustynowej Piaseckiej")
add_occ("Piasecka", "Augustynowa", "Kraśnik", "Uczciwa wdowa / Pozwana", None, 703, 1758, "Augustynowa Piasecka wdowa", "Pozwana w procesie Andrzeja Łypy")
add_occ("Watczyńska", "Matyaszowa", "Kraśnik", "Uczciwa mężatka / Świadek", "Watcryńska?", 703, 1758, "Matyaszowa Watcryńska [Watczyńska?]", "Świadek pobicia kijem w gospodzie")
add_occ("Morel", "Marcin", "Kraśnik", "Sławetny / Świadek", None, 703, 1758, "Martinus Morel", "Świadek wyzwisk w gospodzie")

# --- Skan 704 ---
add_occ("Piasecka", "Augustynowa", "Kraśnik", "Wdowa / Skazana", None, 704, 1758, "Augustynowa Piasecka", "Skazana na 3 grzywny sądowi per medium")
add_occ("Łypa", "Andrzej", "Kraśnik", "Uczciwy / Skazany", None, 704, 1758, "Andrzey Łypa", "Skazany na 2 grzywny (zakład 14 grzywien)")
add_occ("Biegaj", "Mikołaj", "Przedmieście Kraśnickie", "Sławetny / Manifestant", None, 704, 1758, "Mikołay Biegay", "Protestacja przeciw Tomaszowi Młynarczykowi o bydło")
add_occ("Biegaj", "Wawrzyniec", "Kraśnik", "Uczciwy / Manifestant", None, 704, 1758, "Wawrzyniec Biegay", "Współmanifestant przeciw Tomaszowi Młynarczykowi")
add_occ("Młynarczyk", "Tomasz", "Kraśnik", "Młynarczyk / Pozwany", None, 704, 1758, "Tomasz Młynarczyk", "Pozwany o zabranie bydła do dworu pańskiego")
add_occ("Łucki", "Wojciech", "Kraśnik", "Pozwany", None, 704, 1758, "Woyciech Łucki", "Współpozwany w manifestacji Biegajów")

# --- Skan 705 ---
add_occ("Biegaj", "Mikołaj", "Przedmieście Kraśnickie", "Sławetny", None, 705, 1758, "Mikołay Biegay", "Dokończenie protestacji o bydło")
add_occ("Młynarczyk", "Tomasz", "Kraśnik", "Młynarczyk", None, 705, 1758, "Tomasz Młynarczyk", "Wskazany przez administratora")
add_occ("Wilk", "Matyasz", "Kraśnik", "Uczciwy / Skazany", None, 705, 1758, "Matyasz Wilk", "Skazany na 5 grzywien za kontrawencję terminu ze Zdybłem i Zimniakiem")
add_occ("Zdybeł", "Mateusz", "Przedmieście Kraśnickie", "Przedmieszczanin", None, 705, 1758, "Mateusz Zdybeł", "Strona procesu z Matyaszem Wilkiem")
add_occ("Zimniak", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin", None, 705, 1758, "Jakub Zimniak", "Strona procesu z Matyaszem Wilkiem")
add_occ("Deuka", "Matyasz", "Kraśnik", "Uczciwy / Manifestant", None, 705, 1758, "Matyasz Deuk", "Protestacja przeciw Janowi Wiatrowi o spasienie kapusty")
add_occ("Wiatr", "Jan", "Kraśnik", "Uczciwy / Pozwany", None, 705, 1758, "Jan Wiatr", "Pozwany o wypasienie ogrodu z kapustą")

# --- Skan 706 ---
add_occ("Wiatr", "Jan", "Kraśnik", "Uczciwy / Skazany zaocznie", None, 706, 1758, "Jan Wiatrak", "Dekret zaoczny: 3 grzywny sądowi per medium i 2 dni wieży")
add_occ("Gęska", "Józef", "Kraśnik", "Uczciwy / Skazany zaocznie", "Gąska?", 706, 1758, "Jozef Gęska [Gąska?]", "Dekret zaoczny: 2 grzywny sądowi i 2 dni wieży")
add_occ("Tokarz", "Antoni", "Kraśnik", "Uczciwy / Manifestant", None, 706, 1758, "Antoni Tokarz", "Manifestacja przeciw Wojciechowi Pałce o groźby na drodze")
add_occ("Pałka", "Wojciech", "Kraśnik", "Uczciwy / Pozwany", None, 706, 1758, "Woyciech Pałka", "Pozwany o groźby („w mieście psy zbijać”)")

# --- Skan 707 ---
add_occ("Moszkowicz", "Habuś", "Kraśnik", "Starozakonny arendarz puchalski", None, 707, 1758, "Habusz Moszkowicz Arendarz Puchalski", "Interogatoria przeciw Hajmkowi Lejbelowiczowi o konwertytę")
add_occ("Lejbelowicz", "Haimek", "Kraśnik", "Starozakonny / Pozwany", None, 707, 1758, "Haimek Leybelowicz", "Pozwany w interogatoriach Habusia Moszkowicza")
add_occ("Szubertowski", "Tomasz", "Kraśnik", "Syn ławnika Jana / Świadek", None, 707, 1758, "Tomasz Szubertowski filius Joannis", "Zeznanie o Żydzie powracającym z katolicyzmu na judaizm")
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki (ojciec)", None, 707, 1758, "Joannes Szubertowski", "Ojciec świadka Tomasza")
add_occ("Prieszkowski", "Arendarz", "Kraśnik", "Arendarz", "Prieszkoski?", 707, 1758, "Prieszkowski arendarz", "Obiecał 100 czerwonych złotych świadkom katolikom")

# --- Skan 708 ---
add_occ("Kajowicz", "Abraham", "Kock / Kraśnik", "Ojciec konwertyty", None, 708, 1758, "Abraham Kaiowicz", "Wymieniony w zeznaniu jako ojciec konwertyty")
add_occ("Ciwia", "Żydówka", "Kraśnik", "Matka konwertyty", None, 708, 1758, "Ciwia", "Matka konwertyty u arendarza Prieszkowskiego")
add_occ("Beniaś", "Niewierny", "Kraśnik", "Starozakonny / Wierzyciel", None, 708, 1758, "Niewierny Beniaś", "Spłata 52 złp pożyczki przez pospólstwo i przedmieścia")
add_occ("Kozina", "Marcinowa", "Kraśnik", "Uczciwa / Manifestantka", "Korina?", 708, 1758, "Marcinowa Kozina [Korina?]", "Manifestacja przeciw Józefowi Kozie o dług 2 złp")
add_occ("Koza", "Józef", "Przedmieście Góry i Podlesie", "Przedmieszczanin z Podlesia", None, 708, 1758, "Jozef Koza z Podlesia", "Pozwany o napaść przy upominaniu się o dług 2 złp")

# --- Skan 709 ---
add_occ("Kozina", "Marcinowa", "Kraśnik", "Manifestantka", "Korina?", 709, 1758, "Marcinowa Kozina", "Obroniła się u Sławińskiej")
add_occ("Sławińska", "N.", "Kraśnik", "Sławetna / Gospodyni", "Suryflińska?", 709, 1758, "Sławet. Suryflińska [Sławińska?]", "Otworzyła drzwi i obroniła Marcinową Kozinę")
add_occ("Morel", "Marcin", "Kraśnik", "Ławnik kraśnicki / Wierzyciel", None, 709, 1758, "Marcin Morel Ław. Krasnicki", "Oblata skryptu na 8 złp z 20 XII 1752 r.")
add_occ("Chrzanowski", "Wojciech", "Kraśnik", "Dłużnik", None, 709, 1752, "Woyciech Chrzanowski", "Pożyczył 8 złp od Marcina Morela pod zastaw niwki (podpis +)")

# --- Skan 710 ---
add_occ("Tokarz", "Antoni", "Kraśnik", "Uczciwy / Manifestant", None, 710, 1758, "Antoni Tokarz", "Protestacja przeciw Wojciechowi Pałce")
add_occ("Pałka", "Wojciech", "Kraśnik", "Przedmieszczanin", None, 710, 1758, "Woyciech Pałka Przed. kras.", "Tłumaczył zajście szkodą w rzepie")
add_occ("Taraszkiewicz", "Matyasz", "Kraśnik", "Uczciwy / Świadek", None, 710, 1758, "Matyasz Taraszkiewicz", "Świadek oświadczenia przeciw Pałce")
add_occ("Piliński", "Grzegorz", "Kraśnik", "Burmistrz kraśnicki", None, 710, 1758, "Grzegorz Piliński Burm. krasn.", "Deputowany przy sprawie Tokarza")

# --- Skan 711 ---
add_occ("Zdybeł", "Mateusz", "Przedmieście Kraśnickie", "Przedmieszczanin", None, 711, 1758, "Mateusz Zdybeł", "Podwójna kondescensja gruntowa z Jakubem Zimniakiem")
add_occ("Zimniak", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin", None, 711, 1758, "Jakub Zimniak", "Strona kondescensji gruntowej")
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik / Deputowany", None, 711, 1758, "Jan Szubertowski", "Pierwszy skład kondescensji")
add_occ("Zieliński", "Antoni", "Kraśnik", "Ławnik / Deputowany", None, 711, 1758, "Antoni Zieliński", "Pierwszy skład kondescensji")
add_occ("Krzeszowski", "Szymon", "Kraśnik", "Ławnik / Deputowany", None, 711, 1758, "Szymon Krzeszowski", "Pierwszy skład kondescensji")
add_occ("Krzywicki", "Michał Ignacy", "Kraśnik", "Wójt kraśnicki", None, 711, 1758, "Michał Ignacy Krzywicki Woyt", "Drugi skład kondescensji gruntowej")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Pisarz aktualny / Prezydent", None, 711, 1758, "Łukasz Krzeszowski Pisarz aktualnie", "Drugi skład kondescensji gruntowej")
add_occ("Piliński", "Antoni", "Kraśnik", "Prezydent kraśnicki", None, 711, 1758, "Antoni Piliński Prezyd. kras.", "Drugi skład kondescensji gruntowej")
add_occ("Wilk", "Matyasz", "Kraśnik", "Uczciwy / Sąsiad", None, 711, 1758, "Matyasz Wilk", "Posiadacz połowy ćwierci roli")

# --- Skan 712 ---
add_occ("Zimniak", "Jakub", "Przedmieście Kraśnickie", "Manifestant", None, 712, 1758, "Jakub Zimniak", "Protestacja przeciw Mateuszowi Zdybłowi o koszta kondescensji")
add_occ("Zdybeł", "Mateusz", "Przedmieście Kraśnickie", "Przedmieszczanin", None, 712, 1758, "Mateusz Zdybeł", "Dylacja z Maciejem Wilkiem o ćwierć roli")
add_occ("Wilk", "Matyasz", "Kraśnik", "Uczciwy / Pozwany", "Maciej", 712, 1758, "Maciey Wilk", "Dylacja gruntowa do środy")
add_occ("Sławik", "Mikołaj", "Kraśnik", "Uczciwy / Powód", None, 712, 1758, "Mikołay Sławik", "Proces przeciw Józefowi Wilkowi o pobicie żony przy gruszce")
add_occ("Wilk", "Józef", "Kraśnik", "Uczciwy / Pozwany", None, 712, 1758, "Jozef Wilk", "Pozwany o pobicie żony Sławika przy gruszkach")

# --- Skan 713 & 714 (dublet fol. 350r) ---
for s in (713, 714):
    add_occ("Sławik", "Mikołaj", "Kraśnik", "Powód", None, s, 1758, "Mikołay Sławik", "Wyrok w sprawie o gruszki (żona 1 grzywna)")
    add_occ("Wilk", "Józef", "Kraśnik", "Pozwany", None, s, 1758, "Jozef Wilk", "Skazany na 4 grzywny sądowi per medium i przeprosiny (zakład 14 grzywien)")
    add_occ("Winiarczyk", "Marcin", "Gościeradów", "Poddany z Gościeradów P. Starosty", None, s, 1758, "Marcin Winiarczyk Poddany z gościeradów", "Zapiska końcowa na fol. 350r")

# --- Skan 715 ---
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Mieszczanin kraśnicki / Powód", None, 715, 1758, "Jakub Woyciechowski miesc. krasn.", "Skazany na 2 grzywny za wyzwiska córki")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Malarz kraśnicki / Pozwany", None, 715, 1758, "Antoni Pawłowski malarz krasn.", "Skazany na 2 grzywny za nieudowodnione zadanie złodziejstwa")
add_occ("Pankiewicz", "Franciszek", "Kraśnik", "Uczciwy / Rzemieślnik", None, 715, 1758, "Franciszek Pankiewicz", "Wymieniony w inkwizycji (z warsztatu wołał)")
add_occ("Fabrowiczowa", "Katarzyna", "Kraśnik", "Mieszkanka", "Fabrowa?", 715, 1758, "Katarzyna Fabrowiczowa [Fabrowa?]", "Wymieniona w salwie wyroku")

# --- Skan 716 ---
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Mieszczanin", None, 716, 1758, "Jakub Woyciechowski", "Zakład 14 grzywien; żona pozwana przez Pawłowskiego")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Malarz kraśnicki", None, 716, 1758, "Antoni Pawłowski", "Manifestacja przeciw żonie Jakuba Wojciechowskiego o drabinę")
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 716, 1758, "Jan Szubertowski Ławn. krasn.", "Proces o szkodę w tatarce")
add_occ("Zdybeł", "Sebastian", "Przedmieście Kraśnickie", "Przedmieszczanin", None, 716, 1758, "Sobestyan Zdybł", "Pozwany o szkodę w tatarce")
add_occ("Łypa", "Matyasz", "Kraśnik", "Przedmieszczanin", None, 716, 1758, "Matyasz Łypa", "Pozwany o szkodę w tatarce")
add_occ("Posuniak", "Michał", "Kraśnik", "Przedmieszczanin", None, 716, 1758, "Michał Posuniak", "Pozwany o szkodę w tatarce")

# --- Skan 717 ---
add_occ("Szubertowski", "Jan", "Kraśnik", "Ławnik kraśnicki", None, 717, 1758, "Jan Szubertowski", "Wyrok o 3 kopy tatarki")
add_occ("Łypa", "Matyasz", "Kraśnik", "Pozwany", None, 717, 1758, "Matyasz Łypa", "Skazany na oddanie tatarki i grzywnę")
add_occ("Zdybeł", "Sebastian", "Przedmieście Kraśnickie", "Pozwany", None, 717, 1758, "Sobestyan Zdybł", "Współskazany o tatarce")
add_occ("Posuniak", "Michał", "Kraśnik", "Pozwany", None, 717, 1758, "Michał Posuniak", "Współskazany o tatarce")
add_occ("Frankiewicz", "Szymon", "Kraśnik", "Sławetny", None, 717, 1758, "Sławet. Szymon Frankiewicz", "Wzmiankowany w przekreślonej salwie")
add_occ("Eliaszowicz", "Szymon", "Kraśnik", "Starozakonny obywatel kraśnicki", None, 717, 1758, "Szymon Eliaszowicz obywat. kras.", "Proces przeciw Łukaszowi Pałce o dług 2 złp i ucieczkę z aresztu")
add_occ("Pałka", "Łukasz", "Kraśnik", "Uczciwy / Pozwany", None, 717, 1758, "Łukasz Pałka", "Zatrzymany na jarmarku w Bychawie za ucieczkę z aresztu")

# --- Skan 718 ---
add_occ("Pałka", "Łukasz", "Kraśnik", "Skazany", None, 718, 1758, "Łukasz Pałka", "Skazany na dzień więzienia i 2 grzywny sądowi")
add_occ("Zdybeł", "Mateusz", "Przedmieście Kraśnickie", "Powód", None, 718, 1758, "Mateusz Zdybeł", "Dylacja z Maciejem Wilkiem o intromisję")
add_occ("Wilk", "Matyasz", "Kraśnik", "Pozwany", "Maciej", 718, 1758, "Maciey Wilk", "Nakaz przedstawienia intromisji")
add_occ("Pawłowski", "Antoni", "Kraśnik", "Powód", None, 718, 1758, "Antoni Pawłowski", "Sprawa przeciw Jakubowi Wojciechowskiemu o obelgę")
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Mieszczanin / Pozwany", None, 718, 1758, "Jakub Woyciechowski miesc. krasn.", "Sprawa o obelgę żony")

# --- Skan 719 ---
add_occ("Pawłowski", "Antoni", "Kraśnik", "Powód", None, 719, 1758, "Antoni Pawłowski", "Dylacja na inkwizycję")
add_occ("Wojciechowski", "Jakub", "Kraśnik", "Pozwany", None, 719, 1758, "Jakub Woyciechowski", "Dylacja na inkwizycję")
add_occ("Pyryk", "Antoni", "Kraśnik", "Uczciwy / Poszkodowany", None, 719, 1758, "Antoni Pyryk", "Obdukcja ran krwawych i sinych na rękach")
add_occ("Wolak", "Stanisław", "Przedmieście Kraśnickie", "Parobek / Sprawca pobicia", None, 719, 1758, "Stanisław Wolak", "Wskazany w obdukcji Antoniego Pyryka")
add_occ("Tokarz", "Wojciech", "Kraśnik", "Parobek / Sprawca pobicia", "Tokarczyk", 719, 1758, "Woyciech Tokarczyk", "Wskazany w obdukcji Antoniego Pyryka")
add_occ("Szubertowski", "Antoni", "Kraśnik", "Mieszczanin / Świadek obdukcji", None, 719, 1758, "Antoni Szubertowski", "Obecny przy obdukcji Antoniego Pyryka")

# --- Skan 720 ---
add_occ("Zięba", "Wojciech", "Kraśnik", "Pozwany", None, 720, 1758, "Woyciech Zięba", "Wyrok: 15 snopów owsa i 5 grzywien za szkodę")
add_occ("Pałka", "Antoni", "Kraśnik", "Pozwany", None, 720, 1758, "Antoni Pałka", "Współskazany o szkodę w owsie")
add_occ("Piotroszyk", "Jędrzej", "Kraśnik", "Pozwany", "Piotroszkiewicz?", 720, 1758, "Jędrzey Piotroszyk", "Współskazany o szkodę w owsie")
add_occ("Piotroszyk", "Maciej", "Kraśnik", "Pozwany", "Piotroszkiewicz?", 720, 1758, "Maciey Piotroszyk", "Współskazany o szkodę w owsie")
add_occ("Rymarczyk", "Łukasz", "Kraśnik", "Pozwany", None, 720, 1758, "Łukasz Rymarczyk", "Współskazany o szkodę w owsie")
add_occ("Korabek", "Wdowy", "Kraśnik", "Wdowy / Pozwany", None, 720, 1758, "Korabek wdowy", "Współskazany o szkodę w owsie")
add_occ("Witek", "Matyasz", "Przedmieście Kraśnickie", "Przedmieszczanin", "Witerak?", 720, 1758, "Matyasz Witerak [Witek?]", "Sprawa prolongowana do dwóch niedziel")
add_occ("Rymarczyk", "Marcin", "Kraśnik", "Uczciwy / Powód", None, 720, 1758, "Marcin Rymarczyk", "Proces przeciw Marcinowi Kotłunowi o pobicie syna")
add_occ("Kotłun", "Marcin", "Kraśnik", "Sąsiad bliski / Pozwany", "Kotliński?", 720, 1758, "Marcin Kotłun", "Pozwany o pobicie syna Marcina Rymarczyka")

# --- Skan 721 ---
add_occ("Rymarczyk", "Marcin", "Kraśnik", "Powód", None, 721, 1758, "Marcin Rymarczyk", "Salwa o zadanie złodziejstwa")
add_occ("Kotłun", "Marcin", "Kraśnik", "Pozwany", "Kotliński?", 721, 1758, "Marcin Kotłun", "Skazany na 2 grzywny i przeprosiny")
add_occ("Rachoń", "Stanisław", "Kraśnik", "Mieszkaniec kraśnicki / Powód", None, 721, 1758, "Stanislaus Rachoń Incola Cricus", "Interogatoria przeciw sprawcom z Kierznicy")
add_occ("Gąda", "Marcin", "Kierzmyssa / Kierznica", "Pracowity ze wsi Kierznicy", "Gadała? / Juda?", 721, 1758, "Martinus Gąda ex villa Kierzmisy", "Pozwany w interogatoriach Stanisława Rachonia")
add_occ("Krzysztof", "Kowal", "Kierzmyssa / Kierznica", "Kowal ze wsi Kierznicy", None, 721, 1758, "Krzysztof kowal ex villa Kierzmisy", "Pozwany w interogatoriach Stanisława Rachonia")
add_occ("Chapcina", "Helina", "Kraśnik", "Starozakonna / Gospodyni i świadek", "Chapcicha?", 721, 1758, "Starozakonna Helina Chapcina [Chapcicha?]", "Zeznanie o piciu miodu i bitwie o kosę")

# --- Skan 722 ---
add_occ("Chapcina", "Helina", "Kraśnik", "Starozakonna / Świadek", "Chapcicha?", 722, 1758, "Helina Chapcina", "Dokończenie zeznań (wyrwane siwe włosy Rachonia, obrona przez Pisarza)")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Prezydent kraśnicki", None, 722, 1758, "Łukasz Krzeszowski Prezyd. krasn.", "Wizja szkody w owsie (25 snopów) przeciw Szymonowi Frankiewiczowi")
add_occ("Piliński", "Antoni", "Kraśnik", "Ławnik kraśnicki", None, 722, 1758, "Antoni Piliński Ławn. krasn.", "Deputowany do wizji szkody w owsie")
add_occ("Młynarczyk", "Tomasz", "Kraśnik", "Deputowany", None, 722, 1758, "Tomasz Młynarczyk", "Deputowany do wizji szkody w owsie")
add_occ("Frankiewicz", "Szymon", "Kraśnik", "Burmistrz kraśnicki / Pozwany", None, 722, 1758, "Szymon Frankiewicz Burmist. krasn.", "Wskazany jako sprawca szkody 25 snopów owsa")
add_occ("Krzywicki", "Michał Ignacy", "Kraśnik", "Wójt kraśnicki / Manifestant", None, 722, 1758, "Michael Ignatius Krzywicki", "Początek manifestacji przeciw burmistrzowi Stanisławowi Bryśkiewiczowi")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Burmistrz kraśnicki / Pozwany", None, 722, 1758, "Stanislaus Bryśkiewicz Cons. Crasn.", "Pozwany przez wójta Krzywickiego")

# --- Skan 723 ---
add_occ("Krzywicki", "Michał Ignacy", "Kraśnik", "Wójt miasta Kraśnika", None, 723, 1758, "Michał Ignacy Krzywicki Woyt Miasta Kraśnika", "Protestacja przeciw burmistrzowi Bryśkiewiczowi o najście z trzciną i zniewagę na Rynku")
add_occ("Bryśkiewicz", "Stanisław", "Kraśnik", "Burmistrz kraśnicki", None, 723, 1758, "Stanisław Bryśkiewicz Burmistrz Krasnicki", "Areszt stallum burmistrzowskiego do sądu Trybunału Zamojskiego")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", "Burmistrz / Prezydent teraźniejszy", None, 723, 1758, "Łukasz Krzeszowski Burmistrz / Prezydent", "Świadek zniewagi oraz napadnięty przez Bryśkiewicza")
add_occ("Morel", "Marcin", "Kraśnik", "Dawny deputat / Świadek", None, 723, 1758, "Marcin Morel Dawny Deputat", "Świadek pogróżek Bryśkiewicza")
add_occ("Piliński", "Grzegorz", "Kraśnik", "Burmistrz kraśnicki / Świadek", None, 723, 1758, "Grzegorz Piliński Burm. Krasnicki", "Świadek zniewag pod jatkami żydowskimi")
add_occ("Złotkowski", "Andrzej", "Kraśnik", "Exaktor teraźniejszy / Świadek", None, 723, 1758, "Andrzey Złotkowski Exaktor teraźnieyszy", "Świadek zniewag pod jatkami żydowskimi")
add_occ("Młynarczyk", "Tomasz", "Kraśnik", "Przedmieszczanin / Świadek", None, 723, 1758, "Tomasz Młynarczyk", "Świadek zniewag pod jatkami żydowskimi")
add_occ("Rymarczyk", "Marcin", "Kraśnik", "Przedmieszczanin / Świadek", None, 723, 1758, "Marcin Rymarczyk", "Świadek zniewag pod jatkami żydowskimi")
add_occ("Dzierżanowski", "Jan", "Zamość / Ordynacja", "JW. Pan Starosta / Sędzia Trybunału Zamojskiego", None, 723, 1758, "Jan Dzierżanowski Sędzia", "Adresat skargi wójta Krzywickiego w Trybunale Zamojskim")

# --- Skan 724 ---
add_occ("Kadla", "Adam", "Kraśnik", "Ławnik kraśnicki / Dłużnik", "Kadel / Zadel?", 724, 1758, "Adam Zadel [Kadel / Kadla?] Ław. krasn.", "Zobowiązanie zwrotu 20 złp 20 gr i 1 czerwonego złotego (18 złp) Pijarom")
add_occ("Kajetan", "Ksiądz", "Opole / Kraśnik", "Ksiądz Pijar (Scholarum Piarum)", None, 724, 1758, "Ichmość X. Kaicetan [Kajetan]", "Upominał się o dług od ławnika Adama Kadli")
add_occ("Ferdynand", "Ksiądz", "Opole / Kraśnik", "Prokurator Pijarów opolskich", None, 724, 1758, "Ichmość X. Ferdynand", "Wierzyciel ławnika Adama Kadli")

# --- Skan 725 ---
add_occ("Kadla", "Adam", "Kraśnik", "Ławnik kraśnicki / Ślusarz [?]", "Kadel / Zadel?", 725, 1758, "Adam Zadel [Kadel] +", "Podpis krzyżykiem na zwrot długu Pijarom na Trzech Króli 1759 oraz kontrakt na 6 kłódek do kościoła")
add_occ("Gołębiowski", "Piotr", "Kraśnik", "Sławetny / Świadek", None, 725, 1758, "Piotr Gołębiowski", "Przyniósł ciepły chleb kupiony u wdowy żydowskiej do urzędu")

# Zapis gen_data_j17_part29.json
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part29.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part29.json ({len(gen_data)} profiles) and CSV exported.")
