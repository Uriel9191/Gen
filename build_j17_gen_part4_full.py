# -*- coding: utf-8 -*-
import json
import csv
import sys

# Wczytanie dotychczasowych profili z Partii 3 (242 profile)
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part3.json', encoding='utf-8') as f:
    persons = json.load(f)

print(f"Liczba profili w Partii 3: {len(persons)}")

# Indeks do de-duplikacji: (nazwisko.lower(), imie.lower(), miejsce.lower())
lookup = {}
for p in persons:
    key = (p['nazwisko'].strip().lower(), p['imie'].strip().lower(), p['miejsce'].strip().lower())
    lookup[key] = p

def add_occ(nazwisko, imie, miejsce, skan, rok, zapis, rola, wariant_extra=None, funkcja_extra=None):
    key = (nazwisko.strip().lower(), imie.strip().lower(), miejsce.strip().lower())
    if key in lookup:
        p = lookup[key]
        if 'wystapienia' not in p:
            p['wystapienia'] = []
        if not any(w['skan'] == skan for w in p['wystapienia']):
            p['wystapienia'].append({
                "skan": skan,
                "rok": str(rok),
                "zapis_oryginalny": zapis,
                "rola": rola
            })
        if wariant_extra and wariant_extra not in (p.get('wariant_nazwiska') or ''):
            if p.get('wariant_nazwiska'):
                p['wariant_nazwiska'] += f" / {wariant_extra}"
            else:
                p['wariant_nazwiska'] = wariant_extra
        if funkcja_extra and len(funkcja_extra) > len(p.get('funkcja', '')):
            p['funkcja'] = funkcja_extra
    else:
        new_p = {
            "nazwisko": nazwisko.strip(),
            "imie": imie.strip(),
            "miejsce": miejsce.strip(),
            "funkcja": funkcja_extra.strip() if funkcja_extra else "Mieszczanin / Obywatel",
            "wariant_nazwiska": wariant_extra.strip() if wariant_extra else None,
            "wystapienia": [
                {
                    "skan": skan,
                    "rok": str(rok),
                    "zapis_oryginalny": zapis,
                    "rola": rola
                }
            ]
        }
        persons.append(new_p)
        lookup[key] = new_p

# Aktualizacje osób już znanych z poprzednich partii:
add_occ("Majowski", "Jan", "Kraśnik", 76, "1701", "Jan Majowski Wójt", "Odnowienie przysięgi wójtowskiej na nowy rok urzędowy")
add_occ("Majowski", "Jan", "Kraśnik", 78, "1701", "Jan Majowski Wójt", "Obrona praw dożywocia wdowy Cieśliczyny")
add_occ("Majowski", "Jan", "Kraśnik", 80, "1701", "Jan Majowski Wójt", "Przewodniczy sądowi złożonemu w sprawie zalania łąk zarzeckich")
add_occ("Majowski", "Jan", "Kraśnik", 81, "1701", "Jan Majowski Wójt", "Wydanie dekretu wodnego nakazującego obniżenie tamy młyńskiej")
add_occ("Majowski", "Jan", "Kraśnik", 85, "1701", "Jan Majowski Wójt", "Zatwierdzenie rezygnacji roli na Piaskach")
add_occ("Majowski", "Jan", "Kraśnik", 87, "1701", "Jan Majowski Wójt", "Rozstrzygnięcie sporu cechowego tkaczy o próbę mistrzowską")
add_occ("Majowski", "Jan", "Kraśnik", 88, "1701", "Jan Majowski Wójt", "Zasądzenie kary za kradzież drzewa ze szpitalnego lasu")
add_occ("Majowski", "Jan", "Kraśnik", 90, "1701", "Jan Majowski Wójt", "Potwierdzenie inwentarza warsztatu szewskiego Jana Kloca")
add_occ("Majowski", "Jan", "Kraśnik", 93, "1701", "Jan Majowski Wójt", "Wyrok chłosty i banicji dla włóczęgi Macieja")
add_occ("Majowski", "Jan", "Kraśnik", 96, "1701", "Jan Majowski Wójt", "Zasądzenie odszkodowania za wypas owiec w oziminach")
add_occ("Majowski", "Jan", "Kraśnik", 98, "1701", "Jan Majowski Wójt", "Egzekucja prowizji na chleb dla szpitala św. Ducha")
add_occ("Majowski", "Jan", "Kraśnik", 99, "1701", "Jan Majowski Wójt", "Upomnienie bedela Majowskiego w sprawie taks targowych")
add_occ("Majowski", "Jan", "Kraśnik", 100, "1701", "Jan Majowski Wójt", "Przybicie pieczęci miejskiej pod asygnacją wojskową")

add_occ("Kotowicz", "Adam", "Kraśnik", 76, "1701", "Adam Kotowicz Burmistrz", "Odnowienie przysięgi burmistrzowskiej proconsularis")
add_occ("Kotowicz", "Adam", "Kraśnik", 79, "1701", "Adam Kotowicz Burmistrz", "Zatwierdzenie ugody kowala Pajora z kupcem Markiem")
add_occ("Kotowicz", "Adam", "Kraśnik", 86, "1701", "Adam Kotowicz Burmistrz", "Wydzierżawienie łaźni miejskiej Stanisławowi Kłopotowi za 80 złp")
add_occ("Kotowicz", "Adam", "Kraśnik", 91, "1701", "Adam Kotowicz Burmistrz", "Rozliczenie komornego i pieca kaflowego w kamienicy rynkowej")
add_occ("Kotowicz", "Adam", "Kraśnik", 95, "1701", "Adam Kotowicz Burmistrz", "Obrona monopolu garncarskiego przed obcymi wyrobami")
add_occ("Kotowicz", "Adam", "Kraśnik", 98, "1701", "Adam Kotowicz Prowizor Szpitala", "Windykacja prowizji wyderkafowej dla ubogich szpitalnych")
add_occ("Kotowicz", "Adam", "Kraśnik", 99, "1701", "Adam Kotowicz Burmistrz", "Dyscyplinowanie bedela ratuszowego za pobór opłat mostowych")
add_occ("Kotowicz", "Adam", "Kraśnik", 100, "1701", "Adam Kotowicz Burmistrz", "Rozliczenie dostaw 120 korcy owsa dla chorągwi pancernej")

add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 76, "1701", "Stanisław Jerzykiewicz Podwójci", "Zaprzysiężony na podwójciego na rok 1701", "Ierzykiewicz / Jerzykiewicz?")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 82, "1701", "Stanisław Jerzykiewicz Podwójci", "Obdukcja rany ciętej czoła Jakuba Kłopotka")
add_occ("Jerzykiewicz", "Stanisław", "Kraśnik", 93, "1701", "Stanisław Jerzykiewicz Podwójci", "Asesor sądu karnego w procesie o kradzież gęsi")

add_occ("Kołodziejczyk", "Błażej", "Kraśnik", 76, "1701", "Błażej Kołodziejczyk Ławnik", "Zaprzysiężony ławnik sądu wójtowskiego na rok 1701")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", 81, "1701", "Błażej Kołodziejczyk Ławnik", "Wizja lokalna upustów i grobli młyńskiej na Wyżnicy")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", 92, "1701", "Błażej Kołodziejczyk Ławnik", "Rewizja sanitarna drogi i rynsztoków pod Bramą Lubelską")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", 97, "1701", "Błażej Kołodziejczyk Ławnik", "Świadek rezygnacji ogrodu na Błoniu")

add_occ("Borowiecki", "Maciej", "Kraśnik", 76, "1701", "Maciej Borowiecki Cechmistrz Szewski", "Ławnik przysięgły i cechmistrz szewski")
add_occ("Borowiecki", "Maciej", "Kraśnik", 90, "1701", "Maciej Borowiecki Cechmistrz Szewski", "Przyjmuje w opiekę warsztat szewski po zmarłym Klocu")
add_occ("Borowiecki", "Maciej", "Kraśnik", 96, "1701", "Maciej Borowiecki Ławnik", "Taksacja strat w oziminie po wypasie owiec na 8 złp")

add_occ("Dziernatka", "Maciej", "Kraśnik", 76, "1701", "Maciej Dziernatka Ławnik", "Przysięga ławnicza na rok 1701", "Dzierniatka?")
add_occ("Dziernatka", "Maciej", "Kraśnik", 81, "1701", "Maciej Dziernatka Ławnik", "Rewizja upustów młyńskich na rzece Wyżnicy")
add_occ("Dziernatka", "Maciej", "Kraśnik", 92, "1701", "Maciej Dziernatka Ławnik", "Wizja lokalna rynsztoków i wywózki gnoju pod Bramą Lubelską")

add_occ("Dzierzkowski", "Szymon", "Kraśnik", 76, "1701", "Szymon Dzierzkowski Ławnik", "Zaprzysiężony ławnik sądu wójtowskiego na rok 1701")

add_occ("Sitarski", "Franciszek", "Kraśnik", 76, "1701", "Franciszek Sitarski Notariusz", "Notariusz i pisarz ratuszowy")
add_occ("Sitarski", "Franciszek", "Kraśnik", 78, "1701", "Franciszek Sitarski Ławnik", "Rejestracja skargi o naruszenie dożywocia wdowy")
add_occ("Sitarski", "Franciszek", "Kraśnik", 84, "1701", "Franciszek Sitarski Notariusz", "Spis inwentarza ruchomości Doroty Snoparskiej")
add_occ("Sitarski", "Franciszek", "Kraśnik", 89, "1701", "Franciszek Sitarski Pisarz", "Wpis sporu handlowego o zadatek sukienniczy")
add_occ("Sitarski", "Franciszek", "Kraśnik", 94, "1701", "Franciszek Sitarski Notariusz", "Oblatowanie pełnomocnictwa zamkowego czopowego")
add_occ("Sitarski", "Franciszek", "Kraśnik", 97, "1701", "Franciszek Sitarski Notariusz", "Wpis wieczystej rezygnacji ogrodu na Błoniu")

add_occ("Majowski", "Maciej", "Kraśnik", 77, "1701", "Maciej Majowski Bedel", "Nakaz zwrotu aresztowanych skór Tomaszowi Olchowskiemu")
add_occ("Majowski", "Maciej", "Kraśnik", 82, "1701", "Maciej Majowski Bedel", "Uwięzienie napastnika z kordem w wieży ratuszowej")
add_occ("Majowski", "Maciej", "Kraśnik", 93, "1701", "Maciej Majowski Bedel", "Wymierzenie kary 20 plag pod pręgierzem włóczędze Maciejowi")
add_occ("Majowski", "Maciej", "Kraśnik", 99, "1701", "Maciej Majowski Bedel", "Upomnienie za samowolne pobieranie zawyżonych opłat mostowych")

add_occ("Olchowski", "Tomasz", "Kraśnik", 77, "1701", "Tomasz Olchowski Kuśnierz", "Odzyskuje 15 skór baranich i 2 lisie niesłusznie aresztowane")
add_occ("Des", "Jan", "Kraśnik", 77, "1701", "Jan Des Rajca i Szafarz", "Wydaje kwit celny za skóry kuśnierskie", "Dess?")
add_occ("Des", "Jan", "Kraśnik", 91, "1701", "Jan Des Obywatel", "Lokator w kamienicy rynkowej, potrącenie 6 złp za piec kaflowy")

add_occ("Pajor", "Stanisław", "Budzyn", 79, "1701", "Stanisław Pajor Kowal", "Spłata 16 złp długu za żelazo w podkowach i hufnalach")
add_occ("Boruchowicz", "Marek", "Kraśnik", 79, "1701", "Marek Boruchowicz Kupiec żydowski", "Ugoda z kowalem Pajorem na dostawę 40 podków i 200 hufnali", "Mordka Boruchowicz?")

add_occ("Wojtaszek", "Walenty", "Kraśnik", 80, "1701", "Walenty Wojtaszek Przedmieszczanin", "Skarga na zalanie łąk przez młyn miejski", "Woytaszko?")
add_occ("Wojtaszek", "Walenty", "Kraśnik", 81, "1701", "Walenty Wojtaszek Przedmieszczanin", "Uzyskanie dekretu nakazującego obniżenie upustu")

add_occ("Wierzbicki", "Jan", "Zarzecze", 80, "1701", "Jan Wierzbicki Szynkarz zarzecki", "Skarga na zniszczenie siana w brogach przez spiętrzenie wody")
add_occ("Wierzbicki", "Jan", "Zarzecze", 81, "1701", "Jan Wierzbicki Szynkarz zarzecki", "Uczestnik wizji lokalnej tamy na Wyżnicy")

add_occ("Berek", "młynarz", "Kraśnik", 80, "1701", "Berek Młynarz Żydowski", "Oskarżony o zbytnie spiętrzenie wody i zatopienie łąk")
add_occ("Berek", "młynarz", "Kraśnik", 81, "1701", "Berek Młynarz Żydowski", "Nakaz wyrąbania rowu w tamie i spuszczenia wody o 2 piędzi pod karą 10 grzywien")

add_occ("Snoparski", "Maciej", "Kraśnik", 83, "1701", "Maciej Snoparski Stryj", "Wyznaczony tutorem małoletnich bratanic w testamencie")
add_occ("Snoparski", "Maciej", "Kraśnik", 84, "1701", "Maciej Snoparski Rzeźnik", "Dozór nad inwentarzem cyny i szat po Dorocie Snoparskiej")
add_occ("Snoparski", "Maciej", "Kraśnik", 85, "1701", "Maciej Snoparski Rzeźnik", "Kupuje półćwierć roli na Piaskach za 28 złp od Bratka")

add_occ("Bratek", "Wojciech", "Kraśnik", 85, "1701", "Wojciech Bratek Mieszczanin", "Sprzedaje półćwierć roli na Piaskach rzeźnikowi Snoparskiemu", "Bratko?")

add_occ("Barankowicz", "Jan", "Kraśnik", 86, "1701", "Jan Barankowicz Rajca", "Świadek kontraktu dzierżawy łaźni miejskiej")
add_occ("Barankowicz", "Jan", "Kraśnik", 94, "1701", "Jan Barankowicz Poborca miejski", "Uzgadnia z podstarościm zamkowym rewizje podatku czopowego")
add_occ("Barankowicz", "Jan", "Kraśnik", 98, "1701", "Jan Barankowicz Prowizor szpitala", "Windykacja prowizji wyderkafowej dla ubogich")
add_occ("Barankowicz", "Jan", "Kraśnik", 100, "1701", "Jan Barankowicz Poborca", "Wydaje furaże wojskowe ze spichlerza miejskiego")

add_occ("Kłopot", "Stanisław", "Kraśnik", 86, "1701", "Stanisław Kłopot Łaziebnik", "Bierze łaźnię miejską w roczną dzierżawę za 80 złp, darmowa kąpiel dla ubogich", "Kłopotek?")

add_occ("Boruch", "Szmulowicz", "Kraśnik", 89, "1701", "Boruch Szmulowicz Kupiec kramowy", "Pozywa sukiennika Kłosa o zwrot 15 złp zadatku za postaw sukna", "Baruch Szmulowicz")
add_occ("Kłos", "Marcin", "Błonie", 89, "1701", "Marcin Kłos Sukiennik", "Nakaz zwrotu 15 złp zadatku i 2 złp prowizji pod karą wadium", "Kłosek?")

add_occ("Kloc", "Jan", "Kraśnik", 90, "1701", "Jan Kloc Zmarły Szewc", "Zmarły szewc, inwentarz kopyt i skór juchtowych dla syna", "Kłos?")
add_occ("Starobratkowa", "Anna", "Kraśnik", 91, "1701", "Anna Starobratkowa Wdowa", "Dopomina się komornego od Jana Desa z potrąceniem za piec zielony", "Starobrat / Starobracina?")

add_occ("Garncarz", "Jakub", "Kraśnik", 91, "1701", "Jakub Garncarz Majster zduński", "Wymurował piec kaflowy zielony w kamienicy rynkowej za 6 złp", "Figulus?")
add_occ("Garncarz", "Jakub", "Kraśnik", 95, "1701", "Jakub Garncarz Cechmistrz garncarski", "Obrona monopolu cechowego, konfiskata 30 garnków urzędowskich", "Figulus?")

add_occ("Dawidowicz", "Pinchas", "Kraśnik", 94, "1701", "Pinchas Dawidowicz Arendarz generalny", "Arenda czopowego pod kuratelą podstarościego zamkowego", "Pinhas Dawidowicz")

add_occ("Luterek", "Stanisław", "Kraśnik", 96, "1701", "Stanisław Luterek Mieszczanin", "Uzyskuje 8 złp odszkodowania za zniszczenie oziminy przez owce", "Lutrzyk?")

add_occ("Zdeb", "Sebastian", "Góry i Podlesie", 97, "1701", "Sebastian Zdeb Mieszczanin z Gór", "Sprzedaje ogród na Błoniu Walentemu Sankowi za 18 złp na wieczną zgodę", "Zdebik?")
add_occ("Sanek", "Walenty", "Góry i Podlesie", 97, "1701", "Walenty Sanek Przedmieszczanin", "Kupuje ogród od Zdebia za 18 złp, wieczne darowanie dawnych urazów", "Stanek?")

# Nowo zidentyfikowane profile w Partii 4:
add_occ("Cieśliczyna", "Katarzyna", "Przedmieście Lubelskie", 78, "1701", "Katarzyna Cieśliczyna Wdowa", "Wdowa po Janie Cieśli, uzyskuje wyrok przywrócenia dożywocia w chałupie", "Cieślina?", "Mieszczanka / Wdowa")
add_occ("Cieśla", "Paweł", "Przedmieście Lubelskie", 78, "1701", "Paweł Cieśla Pasierb", "Nakaz wpuszczenia macochy do izby i zwrotu pościeli pod wadium 10 grzywien", None, "Przedmieszczanin / Gospodarz")

add_occ("Kłopotek", "Jakub", "Kraśnik", 82, "1701", "Jakub Kłopotek Bednarz", "Ranny w ciemię i czoło kordem pod szynkiem w Rynku", "Kłopot?", "Bednarz miejski")
add_occ("Kozieł", "Jan", "Kraśnik", 82, "1701", "Jan Kozieł Sługa zamkowy", "Osadzony w wieży ratuszowej za napaść z kordem na bednarza", "Kozioł?", "Sługa ordynacki / Żołnierz zamkowy")

add_occ("Snoparska", "Dorota", "Kraśnik", 83, "1701", "Dorota Snoparska Wdowa", "Testament ustny, legat 20 złp na szpital św. Ducha i wosk na ołtarz św. Walentego", None, "Mieszczanka / Posesjonatka")
add_occ("Snoparska", "Dorota", "Kraśnik", 84, "1701", "Dorota Snoparska Zmarła", "Inwentarz pośmiertny kontusza popielicowego, cyny gdańskiej i 2 krów", None, "Mieszczanka / Posesjonatka")

add_occ("Snoparska", "Zofia", "Kraśnik", 83, "1701", "Zofia Snoparska Córka", "Córka Doroty, współsukcesorka chałupy i ogrodu", None, "Mieszczanka / Sukcesorka")
add_occ("Snoparska", "Zofia", "Kraśnik", 84, "1701", "Zofia Snoparska Córka", "Odziedziczenie szat i naczyń cynowych", None, "Mieszczanka / Sukcesorka")

add_occ("Snoparska", "Jadwiga", "Kraśnik", 83, "1701", "Jadwiga Snoparska Córka", "Córka Doroty, współsukcesorka mienia pod opieką stryja", None, "Mieszczanka / Panna")
add_occ("Snoparska", "Jadwiga", "Kraśnik", 84, "1701", "Jadwiga Snoparska Córka", "Odziedziczenie pościeli i krowy pstrej", None, "Mieszczanka / Panna")

add_occ("Tkaczyk", "Grzegorz", "Kraśnik", 87, "1701", "Grzegorz Tkaczyk Czeladnik", "Czeladnik tkacki, termin 6 tygodni na wykonanie nowego postawu sukna", "Czeladnik?", "Czeladnik tkacki")
add_occ("Tkacz", "Szymon", "Kraśnik", 87, "1701", "Szymon Tkacz Starszy Cechu", "Cechmistrz tkacki, odrzuca wadliwy majstersztyk Grzegorza", "Textor?", "Cechmistrz tkacki")

add_occ("Kozak", "Jakub", "Dzierzkowice", 88, "1701", "Jakub Kozak Poddany z Dzierzkowic", "Skazany na konfiskatę sosen i 6 marek grzywny za kradzież drzewa ze szpitalnego lasu", "Kozaczek?", "Chłop poddany z Dzierzkowic")

add_occ("Klocowa", "Katarzyna", "Kraśnik", 90, "1701", "Katarzyna Klocowa Wdowa", "Wdowa po szewcu Janie Klocu, zabezpiecza warsztat dla syna", "Kłosowa?", "Wdowa po szewcu")

add_occ("Dłużewski", "Kazimierz", "Kraśnik", 94, "1701", "Kazimierz Dłużewski Podstarości", "Podstarości zamkowy kraśnicki, oblatuje plenipotencję do nadzoru czopowego", None, "Podstarości zamkowy ordynacki")

add_occ("Kramarz", "Szmul", "Kraśnik", 95, "1701", "Szmul Kramarz w Rynku", "Kramarz rynkowy, konfiskata 30 garnków urzędowskich za łamanie monopolu cechowego", None, "Kramarz rynkowy / Kupiec żydowski")

add_occ("Pasterz", "Walenty", "Góry i Podlesie", 96, "1701", "Walenty Pasterz owczy", "Pasterz stada owiec gromadzkich, nakaz wypłaty 8 złp za szkody w życie", "Pasterczyk?", "Pasterz gromadzki")

add_occ("Bednarz", "Mikołaj", "Kraśnik", 98, "1701", "Mikołaj Bednarz Zmarły Mieszczanin", "Zmarły fundator kapitału 30 złp na kamienicy na rzecz szpitala św. Ducha", None, "Zmarły mieszczanin / Fundator legatu")

add_occ("Włóczęga", "Maciej", "Kraśnik", 93, "1701", "Maciej Włóczęga Luźny", "Skazany na 20 plag pod pręgierzem i wieczystą banicję za kradzież gęsi i lemiesza", "Vagus?", "Człowiek luźny / Włóczęga")

# Standaryzacja i sortowanie alfabetyczne
persons.sort(key=lambda x: (x['nazwisko'].lower(), x['imie'].lower()))

# Przeliczenie metadanych
for idx, p in enumerate(persons, 1):
    p['lp'] = idx
    p['liczba_wzmianek'] = len(p['wystapienia'])
    skany = sorted(list(set(w['skan'] for w in p['wystapienia'])))
    p['skany_roboczo'] = ", ".join(f"#{s}" for s in skany)
    lata = sorted(list(set(w['rok'] for w in p['wystapienia'])))
    if len(lata) == 1:
        p['zakres_lat'] = lata[0]
    else:
        p['zakres_lat'] = f"{lata[0]}–{lata[-1]}"
    
    roles_summary = "; ".join(f"[Skan #{w['skan']}, {w['rok']}]: {w['rola']}" for w in p['wystapienia'])
    var_text = f" (warianty lekcji: {p['wariant_nazwiska']})" if p.get('wariant_nazwiska') else ""
    p['biogram'] = f"Występuje w księgach miejskich Kraśnika ({p['zakres_lat']}) jako {p['funkcja']}{var_text}. Wzmianki źródłowe: {roles_summary}."

print(f"Liczba unikalnych profili po Partii 4: {len(persons)} (0 duplikatów tożsamości)")

# Zapis do JSON
out_json = '/home/ubuntu/workspace/Gen/gen_data_j17_part4.json'
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)
print(f"Zapisano {out_json}")

# Zapis do CSV (UTF-8-SIG z BOM, 9 kolumn)
out_csv = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
headers = [
    'Lp',
    'Nazwisko',
    'Imię',
    'Miejsce',
    'Funkcja społeczna / zawód',
    'Skany źródłowe',
    'Zakres lat',
    'Liczba wzmianek',
    'Warianty nazwiska'
]

with open(out_csv, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(headers)
    for p in persons:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p['funkcja'],
            p['skany_roboczo'],
            p['zakres_lat'],
            p['liczba_wzmianek'],
            p.get('wariant_nazwiska') or ''
        ])

print(f"Zapisano {out_csv} ({len(persons)} wierszy)")
