# -*- coding: utf-8 -*-
import json
import csv
import sys
import copy

# Wczytujemy istniejący plik gen_data_j17_part2.json
with open('/home/ubuntu/workspace/Gen/gen_data_j17_part2.json', encoding='utf-8') as f:
    persons = json.load(f)

print(f"Liczba profili w Partii 2: {len(persons)}")

# Indeks do wyszukiwania po (nazwisko.lower(), imie.lower(), miejsce.lower())
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

# Aktualizacje osób już znanych z Partii 1 i 2:
add_occ("Majowski", "Jan", "Kraśnik", 51, "1700", "Jan Majowski Wójt", "Wójt miejski, przewodniczący sesji wójtowsko-ławniczej")
add_occ("Majowski", "Jan", "Kraśnik", 54, "1700", "Jan Majowski Wójt", "Potwierdzenie zastawu roli na Górach")
add_occ("Majowski", "Jan", "Kraśnik", 55, "1700", "Jan Majowski Wójt", "Nadzór nad aresztami sądowymi")
add_occ("Majowski", "Jan", "Kraśnik", 57, "1700", "Jan Majowski Wójt", "Przewodniczący sądu złożonego w procesie granicznym")
add_occ("Majowski", "Jan", "Kraśnik", 58, "1700", "Jan Majowski Wójt", "Uczestnik wizji lokalnej i usypania kopców na Piaskach")
add_occ("Majowski", "Jan", "Kraśnik", 65, "1700", "Jan Majowski Wójt", "Zatwierdzenie rezygnacji wieczystej placu")
add_occ("Majowski", "Jan", "Kraśnik", 66, "1700", "Jan Majowski Wójt", "Oblatowanie uniwersału leśnego Ichmościów Zamoyskich")
add_occ("Majowski", "Jan", "Kraśnik", 68, "1700", "Jan Majowski Wójt", "Dekretacja kary kuny dla czeladnika szewskiego")
add_occ("Majowski", "Jan", "Kraśnik", 70, "1700", "Jan Majowski Wójt", "Przyjęcie protestacji przeciwko sługom zamkowym")
add_occ("Majowski", "Jan", "Kraśnik", 71, "1700", "Jan Majowski Wójt", "Taksacja zniszczeń grobli i mostów miejskich")
add_occ("Majowski", "Jan", "Kraśnik", 74, "1700", "Jan Majowski Wójt", "Wydanie ordynacji sanitarnej przeciwko zarazie bydlęcej")
add_occ("Majowski", "Jan", "Kraśnik", 75, "1700", "Jan Majowski Wójt", "Zatwierdzenie generalnego regestru rocznego kasy miejskiej")

add_occ("Kotowicz", "Adam", "Kraśnik", 51, "1700", "Adam Kotowicz Burmistrz", "Burmistrz i asesor sądu wójtowskiego")
add_occ("Kotowicz", "Adam", "Kraśnik", 57, "1700", "Adam Kotowicz Burmistrz", "Przewodniczący sądu złożonego z ramienia rady")
add_occ("Kotowicz", "Adam", "Kraśnik", 58, "1700", "Adam Kotowicz Burmistrz", "Wizja lokalna stodoły i miedzy na Piaskach")
add_occ("Kotowicz", "Adam", "Kraśnik", 65, "1700", "Adam Kotowicz Burmistrz", "Świadek rezygnacji placu na Przedmieściu Lubelskim")
add_occ("Kotowicz", "Adam", "Kraśnik", 67, "1700", "Adam Kotowicz Burmistrz", "Rozsądzenie sporu cechu rzeźników z garncarzami o koryto rzeki")
add_occ("Kotowicz", "Adam", "Kraśnik", 71, "1700", "Adam Kotowicz Burmistrz", "Zarządzenie powszechnego szarwarku na naprawę Bramy Lubelskiej")
add_occ("Kotowicz", "Adam", "Kraśnik", 75, "1700", "Adam Kotowicz Burmistrz", "Przejęcie czystej reszty 38 złp z kasy miejskiej na rok 1701")

add_occ("Barankowicz", "Jan", "Kraśnik", 56, "1700", "Jan Barankowicz Rajca i Pisarz", "Poborca podatku szosowego, kwituje kupca Marka", "Barankowic")
add_occ("Barankowicz", "Jan", "Kraśnik", 72, "1700", "Jan Barankowicz Poborca", "Sporządza regestr zaległości szosowego z Błonia")
add_occ("Barankowicz", "Jan", "Kraśnik", 75, "1700", "Jan Barankowicz Poborca", "Zdaje rachunki z percepty 1450 złp i expens 1412 złp")

add_occ("Płechowicz", "Stanisław", "Kraśnik", 57, "1700", "Stanisław Płechowicz Deputat", "Deputat w sądzie złożonym", "Płech / Płechowicz")
add_occ("Płechowicz", "Stanisław", "Kraśnik", 71, "1700", "Stanisław Płechowicz Rajca", "Uczestnik sesji magistratu w sprawie zniszczeń powodziowych")
add_occ("Płechowicz", "Stanisław", "Kraśnik", 75, "1700", "Stanisław Płechowicz Rajca", "Świadek zamknięcia rocznych rachunków ratusza")

add_occ("Kołodziejczyk", "Błażej", "Kraśnik", 52, "1700", "Błażej Kołodziejczyk Ławnik", "Wizja lokalna zniszczonego ogrodu kapustnego")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", 57, "1700", "Błażej Kołodziejczyk Ławnik", "Asesor sądu złożonego")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", 58, "1700", "Błażej Kołodziejczyk Ławnik", "Wytyczenie miedzy i usypanie kopca granicznego")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", 62, "1700", "Błażej Kołodziejczyk Ławnik", "Spisanie inwentarza ruchomości zmarłego Wojtaszka")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", 63, "1700", "Błażej Kołodziejczyk Ławnik", "Przysięga tutoryjna nad sierotą Jadwigą Wojtaszkówną")
add_occ("Kołodziejczyk", "Błażej", "Kraśnik", 74, "1700", "Błażej Kołodziejczyk Ławnik", "Urzędowa rewizja pastwisk i zarządzenie kwarantanny bydła")

add_occ("Borowiecki", "Maciej", "Kraśnik", 52, "1700", "Maciej Borowiecki Cechmistrz Szewski", "Taksacja strat warzywnych na Górach")
add_occ("Borowiecki", "Maciej", "Kraśnik", 54, "1700", "Maciej Borowiecki Starszy Cechu Szewskiego", "Przyjmuje w zastaw ćwierć roli od Pawła Szymury na 40 złp")
add_occ("Borowiecki", "Maciej", "Kraśnik", 68, "1700", "Maciej Borowiecki Cechmistrz Szewski", "Instygator w procesie o zniewagę przeciwko czeladnikowi Wawrzyńcowi")
add_occ("Borowiecki", "Maciej", "Kraśnik", 71, "1700", "Maciej Borowiecki Ławnik", "Nadzór nad szarwarkiem ciesielskim i naprawą mostów")
add_occ("Borowiecki", "Maciej", "Kraśnik", 74, "1700", "Maciej Borowiecki Ławnik", "Egzekucja zakazu uboju bydła zakaźnego")

add_occ("Sitarski", "Franciszek", "Kraśnik", 53, "1700", "Franciszek Sitarski Ławnik", "Świadek spisu ruchomości i podziału spadkowego Starobratków")
add_occ("Sitarski", "Franciszek", "Kraśnik", 62, "1700", "Franciszek Sitarski Ławnik", "Spisuje inwentarz pośmiertny Walentego Wojtaszka")
add_occ("Sitarski", "Franciszek", "Kraśnik", 64, "1700", "Franciszek Sitarski Pisarz", "Notuje wyrok w sprawie wekslowej Borucha z Dzierżakiem")
add_occ("Sitarski", "Franciszek", "Kraśnik", 66, "1700", "Franciszek Sitarski Notariusz", "Oblatator uniwersału leśnego Ordynacji Zamojskiej")
add_occ("Sitarski", "Franciszek", "Kraśnik", 75, "1700", "Franciszek Sitarski Ławnik", "Świadek rocznego zamknięcia kasy miejskiej")

add_occ("Majowski", "Maciej", "Kraśnik", 55, "1700", "Maciej Majowski Bedel", "Uwalnia z aresztu Jakuba Dudka za poręczeniem")
add_occ("Majowski", "Maciej", "Kraśnik", 59, "1700", "Maciej Majowski Bedel", "Rejestruje rany i obrażenia krawca Marcina Kozłowskiego")
add_occ("Majowski", "Maciej", "Kraśnik", 68, "1700", "Maciej Majowski Bedel", "Egzekucja kary aresztu w kunie dla czeladnika szewskiego")
add_occ("Majowski", "Maciej", "Kraśnik", 73, "1700", "Maciej Majowski Bedel", "Zajęcie krowy czerwonej u Stanisława Luterka na poczet długu")
add_occ("Majowski", "Maciej", "Kraśnik", 74, "1700", "Maciej Majowski Bedel", "Zamknięcie pastwisk zarzeckich i pilnowanie kwarantanny")

add_occ("Szymura", "Paweł", "Góry i Podlesie", 54, "1700", "Paweł Szymura Przedmieszczanin", "Zastawia ćwierć roli na Górach za 40 złp Maciejowi Borowieckiemu", "Szymurka?")
add_occ("Szymura", "Paweł", "Góry i Podlesie", 72, "1700", "Paweł Szymura", "Zalega 2 złp podatku szosowego z ćwierci roli")

add_occ("Zdeb", "Sebastian", "Góry i Podlesie", 52, "1700", "Sebastian Zdeb Przedmieszczanin", "Skarży Walentego Sanka o wtargnięcie inwentarza i zniszczenie kapusty", "Zdebik?")
add_occ("Sanek", "Walenty", "Góry i Podlesie", 52, "1700", "Walenty Sanek Przedmieszczanin", "Skazany na 6 złp odszkodowania za zniszczenie zagonów kapusty", "Stanek?")
add_occ("Sanek", "Stanisław", "Kraśnik", 70, "1700", "Stanisław Sanek Przysięgły", "Świadek zaboru siana z łąki miejskiej przez sługi zamkowe", "Stanek?")

add_occ("Starobratkowa", "Anna", "Kraśnik", 53, "1700", "Anna Starobratkowa Wdowa", "Dział majątku pośmiertnego z zięciem Janem Krawczykiem", "Starobrat / Starobracina?")
add_occ("Starobratek", "Wawrzyniec", "Kraśnik", 53, "1700", "Wawrzyniec Starobratek Defunctus", "Zmarły mieszczanin, spadek szat i sprzętów domowych")

add_occ("Stojek", "Tomasz", "Błonie", 72, "1700", "Tomasz Stojek Przedmieszczanin", "Zaległość szosowego 4 zł 15 gr z chałupy na Błoniu", "Stoyek?")
add_occ("Olchowski", "Tomasz", "Kraśnik", 59, "1700", "Tomasz Olchowski Kuśnierz", "Pobicie kijem dębowym krawca Marcina Kozłowskiego w szynku")
add_occ("Olchowski", "Tomasz", "Kraśnik", 60, "1700", "Tomasz Olchowski Kuśnierz", "Pojednanie, wypłata 18 złp na cyrulika i 2 kamieni wosku na ołtarz św. Anny")

add_occ("Luterek", "Stanisław", "Kraśnik", 73, "1700", "Stanisław Luterek Mieszczanin", "Niezapłacony dług 50 złp u arendarza Pinchasa, areszt krowy", "Lutrzyk?")
add_occ("Jajczyk", "Wojciech", "Kraśnik", 70, "1700", "Wojciech Jajczyk Przedmieszczanin", "Zeznanie pod przysięgą o bezprawnym skoszeniu łąki nad Stawem", "Jayczyk?")
add_occ("Dawidowicz", "Pinchas", "Kraśnik", 73, "1700", "Pinchas Dawidowicz Arendarz Zamkowy", "Areszt majątkowy Luterka na 50 złp za gorzałkę i piwo", "Pinhas Dawidowicz")

add_occ("Pajecki", "Paweł Wilhelm", "Kraśnik", 61, "1700", "Ks. Paweł Wilhelm Pajecki Przeor", "Odbiera legat 10 złp na msze św. z testamentu Wojtaszka")
add_occ("Dzierzkowski", "Szymon", "Kraśnik", 69, "1700", "Szymon Dzierzkowski Ławnik", "Świadek spisu inwentarza kuźniczego na Budzyniu")
add_occ("Zdeb", "Szymon", "Błonie", 72, "1700", "Szymon Zdeb Przedmieszczanin", "Zalega 1 zł 15 gr podatku szosowego z opuszczonej pustki")

add_occ("Berek", "młynarz", "Kraśnik", 55, "1700", "Berek Młynarz Żydowski", "Oskarża sługę Jakuba Dudka o kradzież worka mąki żytniej")
add_occ("Zamoyska", "Anna", "Zamość", 66, "1700", "Anna z Gnińskich Zamoyska Podkanclerzyna", "Uniwersał dworu ordynackiego zezwalający na wolny wyrąb 40 sosen")
add_occ("Janaszkowic", "Walenty", "Kraśnik", 71, "1700", "Walenty Janaszkowic Ławnik", "Uczestnik sesji połączonej w sprawie naprawy zniszczeń grobli")

# Nowe profile (osoby wcześniej nienotowane w Partii 1 i 2):
add_occ("Snoparski", "Maciej", "Kraśnik", 51, "1700", "Maciej Snoparski Rzeźnik", "Pozywa Wojciecha Bratka o zapłatę 14 złp za wieprza i słoninę", None, "Rzeźnik / Starszy Cechu Rzeźnickiego")
add_occ("Snoparski", "Maciej", "Kraśnik", 67, "1700", "Maciej Snoparski Starszy Cechu Rzeźnickiego", "Spór cechu rzeźników z garncarzami o zanieczyszczanie Wyżnicy")

add_occ("Bratek", "Wojciech", "Kraśnik", 51, "1700", "Wojciech Bratek Mieszczanin", "Zalega 14 złp za wieprza, pretenduje szkody w płocie", "Bratko?", "Mieszczanin / Gospodarz")

add_occ("Krawczyk", "Jan", "Kraśnik", 53, "1700", "Jan Krawczyk Zięć", "Dział ruchomości po Wawrzyńcu Starobratku, odbiera misy cynowe", "Krawiec?", "Mieszczanin / Zięć Starobratka")
add_occ("Krawczykowa", "Zofia", "Kraśnik", 53, "1700", "Zofia Krawczykowa Córka", "Córka Wawrzyńca i Anny Starobratków, podział majątku domowego", None, "Mieszczanka / Córka Starobratka")

add_occ("Dudek", "Jakub", "Kraśnik", 55, "1700", "Jakub Dudek Sługa młyński", "Obwiniony o kradzież mąki pytlowanej, zwolniony za poręką", "Duda?", "Sługa młyński")
add_occ("Des", "Jan", "Kraśnik", 55, "1700", "Jan Des Mieszczanin", "Daje rękojemstwo majątkowe 10 grzywien za Jakuba Dudka", "Dess?", "Mieszczanin / Obywatel")

add_occ("Boruchowicz", "Marek", "Kraśnik", 56, "1700", "Marek Boruchowicz Kupiec żydowski", "Opłaca 60 złp podatku szosowego i akcyzy z kramów rynkowych", "Mordka Boruchowicz?", "Kupiec korzenny w Rynku")

add_occ("Kępa", "Grzegorz", "Piaski", 57, "1700", "Grzegorz Kępa Przedmieszczanin", "Spór graniczny ze Stanisławem Mrowcem o zaoranie miedzy", "Kempa?", "Przedmieszczanin / Gospodarz na Piaskach")
add_occ("Kępa", "Grzegorz", "Piaski", 58, "1700", "Grzegorz Kępa Przedmieszczanin", "Wytyczenie miedzy i budowa rowu ociekowego od stodoły")

add_occ("Mrowiec", "Stanisław", "Piaski", 57, "1700", "Stanisław Mrowiec Sąsiad", "Oskarżony o zaoranie 12 skib pszenicy na Piaskach", None, "Przedmieszczanin / Gospodarz na Piaskach")
add_occ("Mrowiec", "Stanisław", "Piaski", 58, "1700", "Stanisław Mrowiec Sąsiad", "Usypanie kopca narożnego z kamieniem, nakaz kopania rowu")

add_occ("Dziernatka", "Maciej", "Kraśnik", 58, "1700", "Maciej Dziernatka Ławnik", "Wizja lokalna gruntów granicznych na Piaskach", "Dzierniatka?", "Ławnik miejski")

add_occ("Kozłowski", "Marcin", "Kraśnik", 59, "1700", "Marcin Kozłowski Krawiec", "Pobity kijem sękatym w szynku na Zarzeczu, rany ciemienia i barku", None, "Krawiec miejski")
add_occ("Kozłowski", "Marcin", "Kraśnik", 60, "1700", "Marcin Kozłowski Krawiec", "Ugoda z Olchowskim, odbiera 18 złp na kurację cyrulicką")

add_occ("Wierzbicki", "Jan", "Zarzecze", 59, "1700", "Jan Wierzbicki Szynkarz", "Świadek bójki w szynku na Zarzeczu, zeznanie pod przysięgą", None, "Szynkarz / Karczmarz na Zarzeczu")

add_occ("Cyrulek", "Stanisław", "Kraśnik", 60, "1700", "Stanisław Cyrulek Felczer", "Leczy rany głowy i barku Marcina Kozłowskiego, inkasuje 18 złp", "Cyrulczyk?", "Cyrulik miejski / Felczer")

add_occ("Wojtaszek", "Walenty", "Kraśnik", 61, "1700", "Walenty Wojtaszek Mieszczanin", "Testament ustny in extremis, legaty na szpitale i ołtarze", "Woytaszko?", "Mieszczanin / Posesjonat")
add_occ("Wojtaszek", "Walenty", "Kraśnik", 62, "1700", "Walenty Wojtaszek Zmarły", "Inwentarz pośmiertny szat sukiennych i 3 krów")

add_occ("Wojtaszkowa", "Jadwiga", "Kraśnik", 61, "1700", "Jadwiga Wojtaszkowa Córka", "Główna spadkobierczyni chałupy i inwentarza ojca", None, "Mieszczanka / Sierota")
add_occ("Wojtaszkowa", "Jadwiga", "Kraśnik", 62, "1700", "Jadwiga Wojtaszkowa Sierota", "Odziedziczenie pościeli, szat i dobytku")
add_occ("Wojtaszkowa", "Jadwiga", "Kraśnik", 63, "1700", "Jadwiga Wojtaszkowa Małoletnia", "Poddana pod opiekę stryja Macieja i ławnika Kołodziejczyka")

add_occ("Wojtaszek", "Maciej", "Kraśnik", 62, "1700", "Maciej Wojtaszek Brat zmarłego", "Obecny przy spisywaniu inwentarza braterskiego", None, "Mieszczanin / Tutor sieroty")
add_occ("Wojtaszek", "Maciej", "Kraśnik", 63, "1700", "Maciej Wojtaszek Stryj i Tutor", "Uroczysta przysięga tutoryjna nad siostrzenicą Jadwigą")

add_occ("Szmulowicz", "Boruch", "Kraśnik", 64, "1700", "Boruch Szmulowicz Kupiec żydowski", "Proces o 28 złp za sukno morawskie i korzenie, potrącenie żyta", "Baruch Szmulowicz", "Kupiec kramarz w Rynku")

add_occ("Dzierżak", "Wojciech", "Błonie", 64, "1700", "Wojciech Dzierżak Przedmieszczanin", "Oddał 4 korce żyta za sukno, dopłaca 12 złp reszty", "Dzierzek?", "Przedmieszczanin / Rolnik na Błoniu")
add_occ("Dzierżak", "Wojciech", "Błonie", 72, "1700", "Wojciech Dzierżak", "Zalega 3 zł 10 gr podatku szosowego z roli nad rzeką")

add_occ("Dudzic", "Kazimierz", "Kraśnik", 65, "1700", "Kazimierz Dudzic Mieszczanin", "Sprzedaje plac z chłodnikiem Janowi Klocowi za 35 złp", "Dudzicz?", "Mieszczanin / Posesjonat")

add_occ("Kloc", "Jan", "Kraśnik", 65, "1700", "Jan Kloc Szewc", "Kupuje plac na Przedmieściu Lubelskim za 35 złp gotówką", "Kłos?", "Szewc miejski")

add_occ("Garncarz", "Jakub", "Kraśnik", 67, "1700", "Jakub Garncarz Starszy Cechu", "Reprezentuje cech garncarski w sporze o czyszczenie Wyżnicy", "Figulus?", "Cechmistrz garncarski")

add_occ("Szewczyk", "Wawrzyniec", "Kraśnik", 68, "1700", "Wawrzyniec Czeladnik szewski", "Skazany na 3 dni kuny ratuszowej za zniewagę mistrza Borowieckiego", "Czeladnik?", "Czeladnik szewski")

add_occ("Pajor", "Michał", "Budzyn", 69, "1700", "Michał Pajor Zmarły Kowal", "Zmarły kowal na Budzyniu, inwentarz kowadła, młotów i miechów", "Paiąk?", "Kowal na Budzyniu")

add_occ("Pajorowa", "Regina", "Budzyn", 69, "1700", "Regina Pajorowa Wdowa", "Zgłasza inwentarz kuźnicy po mężu Michale", "Pajorzyca", "Wdowa po kowalu")

add_occ("Pajor", "Stanisław", "Budzyn", 69, "1700", "Stanisław Pajor Kowal", "Obejmuje warsztat kowalski po ojcu, spłata długów w Urzędowie", None, "Kowal na Budzyniu / Syn Michała")

add_occ("Kłos", "Marcin", "Błonie", 72, "1700", "Marcin Kłos Przedmieszczanin", "Zalega 2 zł 20 gr szosowego z pustego placu po pożarze", "Kłosek?", "Przedmieszczanin na Błoniu")

add_occ("Bednarka", "Regina", "Błonie", 72, "1700", "Regina Bednarka Wdowa", "Zwolniona z podatku szosowego z powodu skrajnego ubóstwa", None, "Uboga wdowa na Błoniu")

# Sortowanie i standaryzacja danych
persons.sort(key=lambda x: (x['nazwisko'].lower(), x['imie'].lower()))

# Przeliczenie pól pomocniczych dla każdego rekordu
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
    
    # Biogram / szczegóły
    roles_summary = "; ".join(f"[Skan #{w['skan']}, {w['rok']}]: {w['rola']}" for w in p['wystapienia'])
    var_text = f" (warianty lekcji: {p['wariant_nazwiska']})" if p.get('wariant_nazwiska') else ""
    p['biogram'] = f"Występuje w księgach miejskich Kraśnika ({p['zakres_lat']}) jako {p['funkcja']}{var_text}. Wzmianki źródłowe: {roles_summary}."

print(f"Liczba unikalnych profili po Partii 3: {len(persons)} (0 duplikatów tożsamości)")

# Zapis do JSON
out_json = '/home/ubuntu/workspace/Gen/gen_data_j17_part3.json'
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)
print(f"Zapisano {out_json}")

# Eksport do CSV (UTF-8-SIG z BOM, separator ';')
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
