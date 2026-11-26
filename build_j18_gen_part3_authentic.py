# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part2.json', 'r', encoding='utf-8') as f:
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
            else:
                parts = [x.strip() for x in existing.split('/')]
                for wp in [x.strip() for x in wariant.split('/')]:
                    if wp and wp not in parts:
                        parts.append(wp)
                p['wariant_nazwiska'] = " / ".join(parts)
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
            "min_rok": int(str(rok).split('–')[0]),
            "zakres_lat": str(rok),
            "liczba_wystapien": 1,
            "wystapienia": [{
                "skan": skan,
                "rok": str(rok),
                "zapis_oryginalny": zapis,
                "rola": kwota_ctx,
                "kwota_ctx": kwota_ctx
            }],
            "notatka_biograficzna": f"Osoba odnotowana w księdze miejskiej Kraśnika (Jednostka 18, skan #{skan}, {rok} r.)."
        }
        gen_data.append(new_p)
        profile_map[key] = new_p

# Skan 51 (1661)
add_occ("Żmiędzianka", "Marianna", "Kraśnik", "Sierota (zmarła w Szpitalu św. Ducha)", "Maryey / Maryna", 51, 1661, "Siostry iego Maryny", "Podopieczna opiekuna (wydatki na ubranie i pogrzeb 2 fl 25 gr)")
add_occ("Żmięda", "Mateusz", "Kraśnik", "Szlachetny, powód (dawny sierota)", "Matus / Matys", 51, 1661, "chłopca Matusa / temuz Matysowi", "Wychowanek opiekuna W. Łysaka w latach 1649–1651")
add_occ("Śnieżek", "Łukasz", "Kraśnik", "Mieszkaniec (usługa pogrzebowa)", "Śnieżkowi [?]", 51, 1661, "Łukaszowi Śnieżkowi[?]", "Odbiorca opłaty za sprawę pogrzebową Marianny")
add_occ("Zając", "Jakub", "Kraśnik", "Mieszkaniec / Chlebodawca", "Zaięczy [?]", 51, 1661, "Jakuba Zaięczego[?]", "Służba siostry Maryny od Gód do Przewodniej Niedzieli (3 fl 10 gr)")
add_occ("Zając", "Łukasz", "Kraśnik", "Mieszkaniec / Majster lub gospodarz", "Zaięczy [?]", 51, 1661, "do Łukasza Zaięczego[?]", "Miejsce pobytu młodego Mateusza Żmiędy (2 fl 20 gr)")
add_occ("Kowal", "Grzygiel", "Kraśnik", "Kowal / Wierzyciel", "Grzyglowi Kowalowi", 51, 1661, "Grzyglowi Kowalowi", "Spłata długu z sum opiekuńczych")
add_occ("Łysak", "Wawrzyniec", "Kraśnik", "Opiekun sierot Żmiędów", None, 51, 1661, "Pozwany opiekun (rachunek)", "Rozliczenie expensy 51 fl 22 gr za lata 1649–1651")

# Skan 52 (1661)
add_occ("Łysak", "Wawrzyniec", "Kraśnik", "Opiekun sierot Żmiędów", None, 52, 1661, "Pozwany (obrona)", "Obrona przed zarzutami o 20 fl i konia")
add_occ("Zając", "Jakub", "Kraśnik", "Mieszkaniec / Chlebodawca", "Zaięcki", 52, 1661, "od Nieboszczyka Zaięckiego", "Wzmianka o rzekomym długu 20 fl i koniu (zmarły)")
add_occ("Kulka", "Bartosz", "Kraśnik", "Mieszkaniec / Dłużnik", None, 52, 1661, "Bartosz Kulka", "Zarzut kradzieży krowy i wpłata 2 fl")
add_occ("Byk", "Wojciech", "Kraśnik", "Zmarły mieszkaniec", None, 52, 1661, "Nieboszczyka Pana Wojciecha Byka", "Wzmianka w dekrecie o niezapłaconych latach")

# Skan 53 (1661)
add_occ("Żmięda", "Mateusz", "Kraśnik", "Szlachetny, powód", None, 53, 1661, "Aktor", "Zasądzone 42 złp do rąk aktora w 6 niedziel")
add_occ("Łysak", "Wawrzyniec", "Kraśnik", "Opiekun sierot Żmiędów", None, 53, 1661, "Pozwany", "Zobowiązany dekretem do zapłaty 42 złp i 7 złp 10 gr")
add_occ("Kordek", "Wawrzyniec", "Kraśnik", "Zmarły mieszkaniec", None, 53, 1661, "po Nieboszczyku Wawrzyńcu Kordku", "Wzmianka o granicy i inwentarzu")
add_occ("Zając", "Jakub", "Kraśnik", "Mieszkaniec / Chlebodawca", "Zaięcki", 53, 1661, "od Nieboszczyka Jakuba Zaięckiego", "Kwestia 25 złp w Lublinie")
add_occ("Kulka", "Bartosz", "Kraśnik", "Mieszkaniec / Zmarły", None, 53, 1661, "Nieboszczyka Bartosza Kulki", "Zasądzone 7 złp 10 gr na dzieci B. Kulki")
add_occ("Byk", "Wawrzyniec", "Kraśnik", "Zmarły mieszkaniec", None, 53, 1661, "Nieboszczyka Wawrzyńca Byka", "Zastrzeżenie praw aktora w dekrecie")

# Skan 54 (1661–1662)
add_occ("Grzętka", "Jan", "Kraśnik", "Opiekun starszych dzieci Rogalowskiego", None, 54, "1661–1662", "Jan Grzętka", "Prezentacja taksy i działu dóbr W. Rogalowskiego")
add_occ("Batusik", "Sebastian", "Kraśnik", "Opiekun młodszych dzieci Rogalowskiego", "Batuś", 54, "1661–1662", "Sebastian Batuś / Batusik", "Prezentacja taksy i działu dóbr W. Rogalowskiego")
add_occ("Rogalowski", "Wojciech", "Przedmieście Kraśnickie", "Tkacz i jałmużnik (zmarły)", "Sosnowski", 54, "1661–1662", "Wojciechu Rogalowskim al[ia]s Sosnowskim", "Przedmiot taksy i działu majątkowego")
add_occ("Kwasowic", "Wojciech", "Kraśnik", "Burmistrz kraśnicki", None, 54, "1661–1662", "Sławetnego Pana Wojciecha Kwasowica Burmistrza", "Wydanie rozkazu taksacji")
add_occ("Szafrankowic", "Wojciech", "Kraśnik", "Rajca kraśnicki", None, 54, "1661–1662", "Wojciecha Szafrankowica Radziec", "Członek kolegium radzieckiego")
add_occ("Koniega", "Maciej", "Kraśnik", "Rajca i ławnik kraśnicki", None, 54, "1661–1662", "Macieja Koniegi Radziec", "Członek kolegium radzieckiego")
add_occ("Rogalowska", "Maryna", "Przedmieście Kraśnickie", "Sierota (starsza córka W. Rogalowskiego)", None, 54, "1661–1662", "Marynie", "Starsza sierota po W. Rogalowskim z 1. żony")
add_occ("Rogalowska", "Zofia", "Przedmieście Kraśnickie", "Sierota (starsza córka W. Rogalowskiego)", "Zophiei", 54, "1661–1662", "Zophiei", "Starsza sierota po W. Rogalowskim z 1. żony")
add_occ("Rogalowska", "Ewa", "Przedmieście Kraśnickie", "Sierota (starsza córka W. Rogalowskiego)", None, 54, "1661–1662", "Ewie", "Starsza sierota po W. Rogalowskim z 1. żony")
add_occ("Kłopotek", "Gabriel", "Przedmieście Kraśnickie", "Przedmieszczanin / Taksator", "Kłopot", 54, "1661–1662", "Gabryel Kłopot przedmieszczanin", "Zaproszony taksator z ramienia J. Grzętki")
add_occ("Jeżykowic", "Matyjasz", "Kraśnik", "Exactor przysięgły / Taksator", "Matyiasz Jeżykowic", 54, "1661–1662", "Matyiasz Jeżykowic Exactor", "Zaproszony taksator z ramienia J. Grzętki")

# Skan 55 (1661–1662)
add_occ("Jeżykowic", "Matyjasz", "Kraśnik", "Exactor przysięgły / Taksator", None, 55, "1661–1662", "Exactor na ten czas Przysięgły", "Udział w taksacji")
add_occ("Batusik", "Sebastian", "Kraśnik", "Opiekun", None, 55, "1661–1662", "Sebastiana Batusika", "Opiekun młodszych dzieci Rogalowskiego")
add_occ("Rogalowska", "Katarzyna", "Przedmieście Kraśnickie", "Sierota (młodsza córka W. Rogalowskiego)", None, 55, "1661–1662", "Katarzyny", "Młodsza sierota z Katarzyny Węgorkiewiczówny")
add_occ("Rogalowska", "Agnieszka", "Przedmieście Kraśnickie", "Sierota (młodsza córka W. Rogalowskiego)", None, 55, "1661–1662", "Agnieszki", "Młodsza sierota z Katarzyny Węgorkiewiczówny")
add_occ("Rogalowski", "Ignacy", "Przedmieście Kraśnickie", "Sierota (młodszy syn W. Rogalowskiego)", None, 55, "1661–1662", "Ignacego", "Młodszy sierota z Katarzyny Węgorkiewiczówny")
add_occ("Rogalowski", "Kazimierz", "Przedmieście Kraśnickie", "Sierota (młodszy syn W. Rogalowskiego)", None, 55, "1661–1662", "Kazimierza", "Młodszy sierota z Katarzyny Węgorkiewiczówny")
add_occ("Rogalowska", "Katarzyna", "Przedmieście Kraśnickie", "Ostatnia żona W. Rogalowskiego (z d. Węgorkiewiczówna)", "Węgorkiewiczówna", 55, "1661–1662", "Katarzyny Węgorkiewiczowny Żony ostatniej", "Matka młodszych sierot")
add_occ("Węgorek", "Sebastian", "Kraśnik", "Dziad i opiekun testamentowy sierot Rogalowskich", "Węgorkiewicz", 55, "1661–1662", "Sebastiana Węgorkiewicza Dziada tych Sierot", "Opiekun testamentowy i urzędowy")
add_occ("Szwankowic", "Stanisław", "Kraśnik", "Ławnik przysięgły kraśnicki", None, 55, "1661–1662", "Stanisław Szwankowic Ławnik", "Taksator nieruchomości")
add_occ("Celica", "Stanisław", "Kraśnik", "Ławnik przysięgły kraśnicki", "Celica [?]", 55, "1661–1662", "Stanisław Celica[?] Ławnik", "Taksator nieruchomości")
add_occ("Młynarowski", "Cynda", "Przedmieście Kraśnickie", "Sąsiad za Bramą Lubelską", None, 55, "1661–1662", "miedzą Cynda Młynarowskiego", "Sąsiad domu Rogalowskiego")
add_occ("Madejowska", "Cyroń", "Przedmieście Kraśnickie", "Sąsiadka na Zarzeczu", "Madeiowska", 55, "1661–1662", "miedzą Cyroni Madeiowskiej", "Sąsiadka półłanka na Zarzeczu")
add_occ("Dworzański", "Sąsiad", "Przedmieście Kraśnickie", "Posiadacz półłanka na Zarzeczu", None, 55, "1661–1662", "Dworzanskiego Półłanka", "Sąsiad roli na Zarzeczu")
add_occ("Krokoszowski", "Stanisław", "Przedmieście Kraśnickie", "Sąsiad na Stawiskach", None, 55, "1661–1662", "Stanisława Krokoszowskiego", "Sąsiad ogrodu na Stawiskach (16 fl)")
add_occ("Kowalik", "Matyjasz", "Przedmieście Kraśnickie", "Sąsiad na Stawiskach", None, 55, "1661–1662", "Matyjasza Kowalika", "Sąsiad ogrodu na Stawiskach")
add_occ("Czaja", "Wojciech", "Przedmieście Kraśnickie", "Sąsiad na Podlesiu", "Czaia", 55, "1661–1662", "Wojciecha Czaia", "Sąsiad roli za Podlesiem (150 złp)")

# Skan 56 (1661–1662)
add_occ("Węgorek", "Sebastian", "Kraśnik", "Dziad i opiekun", "Węgorkiewicz", 56, "1661–1662", "Sebastiana Węgorkiewicza", "Uczestnik działu po W. Rogalowskim")
add_occ("Batusik", "Sebastian", "Kraśnik", "Opiekun", None, 56, "1661–1662", "Sebastiana Batusika", "Uczestnik działu po W. Rogalowskim")
add_occ("Rogalowski", "Jan", "Przedmieście Kraśnickie", "Sierota (młodszy syn W. Rogalowskiego)", None, 56, "1661–1662", "Jana / Janowi", "Młodszy syn (przydzielony ogród na Podlesiu i Stawiskach)")
add_occ("Temliński", "Paweł", "Kraśnik", "Rozjemca / Taksujący dział", "Temliński [?]", 56, "1661–1662", "Paweł Temliński[?]", "Zaproszony do działu z ramienia młodszych sierot")
add_occ("Olkowski", "Jan", "Kraśnik", "Rozjemca / Taksujący dział", None, 56, "1661–1662", "Jan Olkowski", "Zaproszony do działu z ramienia młodszych sierot")
add_occ("Kłopotek", "Gabriel", "Przedmieście Kraśnickie", "Rozjemca / Taksujący dział", "Kłopot", 56, "1661–1662", "Gabryel Kłopot", "Zaproszony do działu")
add_occ("Grzętka", "Jan", "Kraśnik", "Opiekun starszych dzieci", None, 56, "1661–1662", "Jana Grzętki", "Opiekun Maryny, Zofii i Ewy")
add_occ("Rogalowska", "Anna", "Przedmieście Kraśnickie", "Pierwsza żona W. Rogalowskiego (zmarła)", None, 56, "1661–1662", "Anny Rogalowskiej", "Matka starszych dzieci")
add_occ("Baty", "Jan", "Przedmieście Kraśnickie", "Rozjemca / Przedmieszczanin", None, 56, "1661–1662", "Jan Baty przedmieszczanin", "Zaproszony do działu z ramienia starszych dzieci")
add_occ("Jeżykowic Skarnik", "Kacper", "Kraśnik", "Mieszczanin / Rozjemca", None, 56, "1661–1662", "Kacper Jeżykowic Skarnik", "Zaproszony do działu z ramienia starszych dzieci")

# Skan 57 (1661–1662)
add_occ("Kwasowic", "Wojciech", "Kraśnik", "Burmistrz kraśnicki", None, 57, 1661, "P. Wojciecha Kwasowica Burmistrza", "Dział potwierdzony w domu burmistrza w 1661 r.")
add_occ("Grzętka", "Jan", "Kraśnik", "Opiekun", None, 57, 1662, "Janem Grzętką", "Strona procesu w 1662 r.")
add_occ("Węgorek", "Sebastian", "Kraśnik", "Dziad sierot / Powód", "Węgorkiewicz", 57, 1662, "Sebastianem Węgorkiewiczem Aktorem", "Skarga przeciw S. Batusikowi o brak rachunków i testamentu")
add_occ("Batusik", "Sebastian", "Kraśnik", "Opiekun / Pozwany", None, 57, 1662, "Sebastianem Batusikiem Pozwanym", "Pozwany przez S. Węgorkiewicza")

# Skan 58 (1662)
add_occ("Rogalowski", "Wojciech", "Przedmieście Kraśnickie", "Zmarły", "Sosnowski", 58, 1662, "Nieboszczyka Wojciecha Rogalowskiego al[ia]s Sosnowskiego", "Przedmiot rachunku dochodu (20 złp) i kosztów pogrzebu")
add_occ("Zięba", "Wawrzyniec", "Kraśnik", "Dłużnik W. Rogalowskiego", None, 58, 1662, "od Wawrzyńca Zięby", "Wpłata 12 złp do masy spadkowej")
add_occ("Węgorek", "Sebastian", "Kraśnik", "Dziad sierot", "Węgorkiewicz", 58, 1662, "P. Węgorkiewiczowi", "Odbiór 7 gr od odbierania bramy")

# Skan 60 (1701)
add_occ("Sprawski", "Stanisław", "Kraśnik", "Obywatel kraśnicki / Zeznający oblig", "Sprawsky", 60, 1701, "Stanisław Sprawski", "Oblig na 300 złp na wykup półłanka Rędzinskiego od T. Anczarka")
add_occ("Sprawska", "Anna", "Kraśnik", "Małżonka Stanisława Sprawskiego", None, 60, 1701, "Anna małżonkowie", "Współzeznająca oblig na 300 złp")
add_occ("Anczarek", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Posiadacz gruntu", None, 60, 1701, "Tomasza Anczarka Przedmieszczanina", "Posiadacz półłanka Rędzinskiego wykupywanego przez Sprawskich")
add_occ("Safrankowiec", "Baltazar", "Kraśnik", "Zmarły obywatel kraśnicki", None, 60, 1701, "po niegdy Uciwym Baltazarze Safrankowcu", "Poprzedni właściciel półłanka Rędzinskiego")
add_occ("Rzędecki", "Andrzej", "Kraśnik", "Administrator klucza kraśnickiego", None, 60, 1701, "Jegomości Pana Andrzeia Rzędeckiego Administratora", "Wierzyciel 300 złp płatnych na św. Wojciecha 1702")

# Skan 61 (1701)
add_occ("Sprawski", "Stanisław", "Kraśnik", "Obywatel kraśnicki", "Sprawsky", 61, 1701, "Stanisław Sprawsky", "Podpis pod obligiem")
add_occ("Sprawska", "Anna", "Kraśnik", "Małżonka Stanisława Sprawskiego", None, 61, 1701, "Anna Sprawska", "Podpis pod obligiem")
add_occ("Jędryszek", "Sebastian", "Kraśnik", "Majster rzemiosła szewskiego", None, 61, 1701, "Sebastian Jędryszek mieszczanin rzemiosła szewskiego Majster", "Protestacja przeciw braciom Grymusom o prawa cechowe")
add_occ("Grymus", "Jamiel", "Kraśnik", "Mieszczanin kraśnicki / Członek cechu", "Jamiel [?]", 61, 1701, "Sławetnemu Jamielowi[?] Grymusowi", "Pozwany w protestacji S. Jędryszka")
add_occ("Grymus", "Jan", "Kraśnik", "Mieszczanin kraśnicki / Członek cechu", None, 61, 1701, "Janowi Grymusom", "Pozwany w protestacji S. Jędryszka o obelgę")
add_occ("Beski", "Wojciech", "Kraśnik", "Ławnik kraśnicki", None, 61, 1701, "Sławetnego Woyciecha Beskiego Ławnika", "Świadek zajścia przy stole cechowym")

# Skan 62 (1701)
add_occ("Sobiec", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Protestant", None, 62, 1701, "Tomasz Sobiec Przedmieszczanin", "Protestacja przeciw burmistrzowi J. Sokołowiczowi")
add_occ("Sokołowicz", "Jan", "Kraśnik", "Burmistrz kraśnicki", "Sokołowski [?]", 62, 1701, "Panu Janowi Sokołowiczowi[?] Burmistrzowi", "Oskarżony o niedotrzymanie kontraktu na pustki Kuchniowskie")
add_occ("Janny", "Stanisław", "Kraśnik", "Mieszczanin kraśnicki / Kontrahent", None, 62, 1701, "Stanisław Janny mieszczanin", "Strona transakcji pustek Kuchniowskich z ogrodem Liderlińskim")

# Skan 63 (1701)
add_occ("Maziarczyk", "Stanisław", "Kraśnik", "Mieszczanin kraśnicki", None, 63, 1701, "Stanislai Maziarczyk", "Strona w sporze o zalewanie słodu i żyto")
add_occ("Stachowski", "Andrzej", "Kraśnik", "Obywatel kraśnicki / Świadek", "Andreas Stachowski", 63, 1701, "H. Andreas Stachowski Obywatel", "Świadek rozmowy o życie i słodzie na targu")
add_occ("Aucek", "Starozakonny", "Kraśnik", "Kupiec żydowski", None, 63, 1701, "żydów Aucka", "Nabywca żyta na pierwszym targu")
add_occ("Berek", "Starozakonny", "Kraśnik", "Kupiec żydowski", None, 63, 1701, "y Berka", "Nabywca żyta na pierwszym targu")

# Skan 64 (1701)
add_occ("Dawidowicz", "Huczek", "Kraśnik", "Kupiec, obywatel kraśnicki / Aktor", None, 64, 1701, "Huczkiem Dawidowiczem Kupcem", "Powód w sporze ze S. Maziarczykiem o 9 spustów wódki")
add_occ("Maziarczyk", "Stanisław", "Kraśnik", "Mieszczanin kraśnicki / Pozwany", None, 64, 1701, "Stanisławem Maziarczykiem", "Składający przysięgę na rocie o wyrobie wódki")
add_occ("Maziarczyk", "Kazimierz", "Przedmieście Kraśnickie", "Mieszkaniec / Strona w sporze", None, 64, 1701, "Kazimierzem Maziarzykiem", "Spór z W. Radzikiem o grunt na przedmieściu")
add_occ("Radzik", "Wawrzyniec", "Przedmieście Kraśnickie", "Mieszkaniec / Strona w sporze", None, 64, 1701, "Wawrzyńcem Radzikiem", "Spór z K. Maziarczykiem o grunt na przedmieściu")
add_occ("Koza", "Kazimierz", "Kraśnik", "Kraśniczanin / Aktor", None, 64, 1701, "Kazimierzem Kozą Kraśniczaninem", "Powód przeciw szwagrowi Matyjaszowi o 33 gr i siekierę")
add_occ("Szwagier", "Matyjasz", "Kraśnik", "Pozwany (szwagier Kazimierza Kozy)", None, 64, 1701, "Matyiaszem Szwagrem", "Nakaz oddania 4 gr 8 szel. i siekiery po Marcinie Pielku")
add_occ("Pielka", "Marcin", "Kraśnik", "Zmarły mieszkaniec", "Pielk [?]", 64, 1701, "po śmierci Marcina Pielku[?]", "Właściciel siekiery w sporze K. Kozy")
add_occ("Mierzwa", "Bartłomiej", "Kraśnik", "Powód / Aktor", "Mierzwa [?]", 64, 1701, "Bartłomiejem [Mierzwa?]", "Spór z M. Biernatem o żyto z brogu i słomę")
add_occ("Biernat", "Matyjasz", "Kraśnik", "Pozwany", None, 64, 1701, "Matyiaszem Biernatem", "Pozwany o żyto z brogu")

# Skan 65 (1701)
add_occ("Lis", "Jakub", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Aktor", None, 65, 1701, "Jakubem Lisiem Przedmieszczaninem", "Spór o zagrodę z S. Sąsadkiem")
add_occ("Sąsadek", "Sobestian", "Przedmieście Kraśnickie", "Pozwany", None, 65, 1701, "Sobestianem Sąsadkiem", "Spór o zagrodę z J. Lisem")
add_occ("Suchek", "Wojciech", "Przedmieście Kraśnickie", "Ojciec / Strona w sporze", "Suchek [?]", 65, 1701, "Woyciechem Suchkiem[?] Ojcem", "Współuczestnik ugody o zagrodę")
add_occ("Sokołowicz", "Maciej", "Kraśnik", "Mieszkaniec / Manifestant", "Sokołowicz [?]", 65, 1701, "Maciej Sokołowicz[?]", "Manifestacja przeciw W. Misowiczowi")
add_occ("Misowicz", "Wojciech", "Kraśnik", "Pozwany", "Misowicz [?]", 65, 1701, "Woyciecha Misowicza[?]", "Pozwany przez M. Sokołowicza")
add_occ("Kraśnicki", "Wawrzyniec", "Kraśnik", "Wierzyciel", None, 65, 1701, "Wawrzyńca Krasnickiego", "Sprawa przeciw J. Brawowskiemu o dług")
add_occ("Brawowski", "Jan", "Kraśnik", "Dłużnik (3tio Contumax)", None, 65, 1701, "Jan Brawowski", "Trzykrotnie nie stawił się w sądzie")
add_occ("Ciesielski", "Stefan", "Kraśnik", "Ławnik kraśnicki / Sprzedawca", None, 65, 1701, "Stefan Ciesielski Ławnik", "Sprzedaż placu i budynku M. Nowackiemu")
add_occ("Ciesielska", "Jadwiga", "Kraśnik", "Małżonka ławnika S. Ciesielskiego", None, 65, 1701, "Jadwiga małżonkowie", "Współsprzedająca plac i budynek")
add_occ("Nowacki", "Maciej", "Kraśnik", "Mieszczanin i obywatel kraśnicki / Nabywca", None, 65, 1701, "Maciejowi Nowackiemu", "Nabywca budynku od S. Ciesielskiego")
add_occ("Nowacka", "Ewa", "Kraśnik", "Małżonka Macieja Nowackiego", None, 65, 1701, "Ewie małżonkom", "Współnabywczyni budynku")

# Skan 66 (1701)
add_occ("Ciesielski", "Stefan", "Kraśnik", "Ławnik kraśnicki", None, 66, 1701, "Stefana Ciesielskiego Ławnika", "Rezygnacja budynku za 45 złp")
add_occ("Jarzykowa", "Anna", "Przedmieście Kraśnickie", "Małżonka Wojciecha Jarzyka / Oblatująca", None, 66, 1701, "Anna Uciwego Woyciecha Jarzyka małżonka", "Oblata testamentu męża W. Jarzyka")
add_occ("Jarzyk", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Testator", None, 66, 1701, "Woyciecha Jarzyka", "Autor oblatowanego testamentu")
add_occ("Jeżewicz", "Stanisław", "Kraśnik", "Burmistrz kraśnicki", "Jeżewicz [?]", 66, 1701, "Pana Stanisława Jeżewicza[?] Burmistrza", "Asysta przy oblacie testamentu")
add_occ("Madejczyk", "Józef", "Przedmieście Kraśnickie", "Przedmieszczanin i ławnik kraśnicki", None, 66, 1701, "Józef Madejczyk Przedmieszczanin", "Współoblatujący testament W. Jarzyka")

# Skan 67 (1701)
add_occ("Jarzyk", "Wojciech", "Przedmieście Kraśnickie", "Przedmieszczanin / Testator", None, 67, 1701, "Wojciech Jarzyk", "Dyspozycja pogrzebu i wykaz majątku w testamencie")
add_occ("Jarzykowa", "Anna", "Przedmieście Kraśnickie", "Żona W. Jarzyka", None, 67, 1701, "żony swoiey Annie", "Wykonawczyni dyspozycji pogrzebowych i spłaty długu")
add_occ("Anisarek", "Mateusz", "Kraśnik", "Wierzyciel", "Anisarek [?]", 67, 1701, "Mateuszowi Anisarkowi[?]", "Wierzyciel 32 złp w testamencie W. Jarzyka")
add_occ("Chleb", "Marcin", "Przedmieście Kraśnickie", "Poprzedni właściciel gruntu", None, 67, 1701, "U Marcina Chleba przedmieszczanina", "Sprzedał pusty grunt W. Jarzykowi przed 40 laty za 436 złp")
add_occ("Jarzykowa", "Zofia", "Przedmieście Kraśnickie", "Pierwsza żona W. Jarzyka", None, 67, 1701, "z pierwszą żoną ... Zofia", "Wzmianka w testamencie o pierwszej żonie")

# Skan 68 (1701)
add_occ("Jarzyk", "Wojciech", "Przedmieście Kraśnickie", "Testator", None, 68, 1701, "J.J.K.", "Zakończenie testamentu i zapis dożywocia")
add_occ("Jarzykówna", "Jadwiga", "Przedmieście Kraśnickie", "Córka W. Jarzyka", None, 68, 1701, "Jadwigą", "Córka wzmiankowana przy rozliczeniu z M. Kudrelem")
add_occ("Kudrel", "Matyjasz", "Przedmieście Kraśnickie", "Mieszkaniec / Powinowaty", None, 68, 1701, "Uciwego Matyasza Kudrela", "Rozliczenie gruntu i sukni za 12 złp")
add_occ("Jarzyk", "Józef", "Przedmieście Kraśnickie", "Syn Wojciecha i Anny Jarzyków", None, 68, 1701, "Na synów Józefa", "Spadkobierca dóbr po śmierci matki")
add_occ("Jarzyk", "Andrzej", "Przedmieście Kraśnickie", "Syn Wojciecha i Anny Jarzyków", None, 68, 1701, "y Andrzeia moich", "Spadkobierca dóbr po śmierci matki")
add_occ("Sobek", "Adam", "Przedmieście Kraśnickie", "Sąsiad roli w ulicy", None, 68, 1701, "Adam Sobek", "Sąsiad ćwierci roli w testamencie W. Jarzyka")
add_occ("Jeżewicz", "Stanisław", "Kraśnik", "Burmistrz kraśnicki / Egzekutor testamentu", "Jeżewicz [?]", 68, 1701, "Panu Stanisławie Jeżewiczu Burmistrzu", "Egzekutor testamentu W. Jarzyka")
add_occ("Madejczyk", "Józef", "Przedmieście Kraśnickie", "Ławnik kraśnicki / Egzekutor testamentu", None, 68, 1701, "Ławnika Józefa Madejczyka", "Egzekutor testamentu W. Jarzyka")

# Skan 69 (1701)
add_occ("Sosnowski", "Franciszek", "Kraśnik", "Woźny przysięgły (authentyczny)", None, 69, 1701, "Franciszek Sosnowski Woźny authentyczny", "Relacja z aresztu 400 złp na domu Joska Moszkowica")
add_occ("Moszkowic", "Lewek", "Kraśnik", "Szkolnik synagogi kraśnickiej", None, 69, 1701, "Lewkiem Moszkowicem Szkolnikiem synagogi", "Współrelacjonujący areszt na domu J. Moszkowica")
add_occ("Rzędecki", "Andrzej", "Kraśnik", "Administrator klucza kraśnickiego", None, 69, 1701, "Imci Pana Andrzeja Rzędeckiego Administratora", "Zlecający areszt i sędzia w sprawie K. Chudzikowej")
add_occ("Doktor", "Starozakonny", "Kraśnik", "Lekarz żydowski synagogi kraśnickiej", None, 69, 1701, "Doctora Żyda tutejszego Synagogi", "Strona objęta aresztem sumy 400 złp")
add_occ("Moszkowic", "Josek", "Kraśnik", "Obywatel kraśnicki (starozakonny)", None, 69, 1701, "Żyda Joska Moszkowica", "Właściciel domu obłożonego aresztem i pozwany przez Chudzikową")
add_occ("Krawiec", "Sebastian", "Kraśnik", "Dworzanin kasztelana lubelskiego / Wierzyciel", None, 69, 1701, "Panu Sobestianowi Krawcowi na dworze Kasztelana Lubelskiego", "Wierzyciel z tytułu długu na domu J. Moszkowica")
add_occ("Chudzikowa", "Katarzyna", "Kraśnik", "Wdowa, winiarka kraśnicka / Aktorka", None, 69, 1701, "Katarzyną Chudzikową wdową winiarką", "Proces z J. Moszkowicem o dzierżawę wódki")

# Skan 70 (1701)
add_occ("Chudzikowa", "Katarzyna", "Kraśnik", "Wdowa, winiarka / Aktorka", None, 70, 1701, "Aktorkę", "Wyrok w sprawie o dzierżawę wódki i porycie ogrodu")
add_occ("Moszkowic", "Josek", "Kraśnik", "Obywatel kraśnicki", None, 70, 1701, "oskarzony", "Zobowiązania przysięgowe w sporze z Chudzikową")
add_occ("Jadwiga", "Świadek / Strona", "Kraśnik", "Uczestniczka procesu Chudzikowej", None, 70, 1701, "Jadwiga podania sądowego", "Wzmianka w wyroku o przysiędze")
add_occ("Zuzanna", "Strona / Odbiorczyni", "Kraśnik", "Uczestniczka procesu Chudzikowej", None, 70, 1701, "Zuzanna", "Zasądzone 4 złp 20 gr")
add_occ("Tatarski", "Franciszek", "Kraśnik", "Woźny przysięgły", None, 70, 1701, "Franciszek Tatarski Woźny authentyczny", "Relacja z rezygnacji i intromisji domu")
add_occ("Chmielowic", "Adam Michał", "Kraśnik", "Pisarz miejski przysięgły", None, 70, 1701, "Adam Michał Chmielowic Pisarz Miejski", "Relacja z rezygnacji i intromisji domu")
add_occ("Rzędecki", "Andrzej", "Kraśnik", "Administrator klucza kraśnickiego", None, 70, 1701, "Andrzeja Rzędeckiego Administratora", "Konsens na rezygnację domu")
add_occ("Sokołowicz", "Jan", "Kraśnik", "Sąsiad / Burmistrz kraśnicki", None, 70, 1701, "P. Jana Sokołowicza", "Sąsiad sprzedawanego domu")

# Skan 71 (1701)
add_occ("Chapon", "Jachym", "Kraśnik", "Brat / Poprzedni właściciel", "Chaponiów", 71, 1701, "Brata Jachymów Chaponiów Drawidowych", "Wzmianka przy sprzedaży domu J. Moszkowicowi")
add_occ("Moszkowic", "Josek", "Kraśnik", "Obywatel kraśnicki / Nabywca domu", None, 71, 1701, "Niewiernego Joska Moszkowica", "Intromisja w dom kupiony za 1000 złp")
add_occ("Dudek", "Stanisław", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Sprzedawca", None, 71, 1701, "Stanisław Dudek", "Sprzedawca roli na Podlesiu po ojcu Wawrzyńcu")
add_occ("Dudek", "Wawrzyniec", "Przedmieście Kraśnickie", "Zmarły przedmieszczanin kraśnicki", None, 71, 1701, "Uczciwego Wawrzyńca Dudka", "Ojciec Stanisława i Franciszka Dudków")
add_occ("Dudkowa", "Zofia", "Przedmieście Kraśnickie", "Wdowa po Wawrzyńcu Dudku (z d. Jantunówna)", "Jantunówna [?]", 71, 1701, "z Zofią z domu Jantunówną[?]", "Matka Stanisława i Franciszka Dudków")
add_occ("Struski", "Szymon", "Przedmieście Kraśnickie", "Przedmieszczanin / Sąsiad na Podlesiu", None, 71, 1701, "Szymona Struskiego", "Sąsiad roli Dudków na Podlesiu")
add_occ("Kuropka", "Wojciech", "Kraśnik", "Mieszczanin kraśnicki / Wierzyciel zastawny", None, 71, 1701, "Wojciechowi Kuropkowi", "Posiadacz zastawu na roli Dudków (120 złp)")

# Skan 72 (1701)
add_occ("Kuropka", "Wojciech", "Kraśnik", "Mieszczanin / Wierzyciel", None, 72, 1701, "Kuropkowi mieszczaninowi", "Wierzyciel 120 złp na roli Dudka")
add_occ("Zamoyska", "Ludwika Salomea", "Kraśnik", "Księżna / Fundatorka konwentu", None, 72, 1701, "Panny Ludwiki Salomei Zamoyskiey Xiężney", "Fundacja zakonna w Kraśniku (wierzytelność 120 złp)")
add_occ("Anczarek", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin / Nabywca roli", None, 72, 1701, "Tomaszowi Anczarkowi", "Kupno roli z chałupką od S. Dudka za 240 złp")
add_occ("Dudek", "Stanisław", "Przedmieście Kraśnickie", "Przedmieszczanin / Sprzedawca", None, 72, 1701, "zeznawaiący", "Odbiór 70 złp zaliczki z 240 złp")

# Skan 73 (1701)
add_occ("Berek", "Starozakonny", "Kraśnik", "Wierzyciel / Aktor", None, 73, 1701, "Infidelis Berek", "Uzyskał dekret sekwestru na Dąbrowskich")
add_occ("Skarczykowic Dąbrowski", "Maciej", "Kraśnik", "Pozwany (2do quarto contumax)", "Skarczyk", 73, 1701, "Mathia ... Skarczykowie Dąbrowski", "Dekret sekwestru za dług wobec Żyda Berka")
add_occ("Skarczykowic Dąbrowski", "Jan", "Kraśnik", "Pozwany (2do quarto contumax)", "Skarczyk", 73, 1701, "Joannes Skarczykowie Dąbrowski", "Dekret sekwestru za dług wobec Żyda Berka")
add_occ("Rudzikowa", "Katarzyna", "Kraśnik", "Wdowa", None, 73, 1701, "Katarzyna Rudzikowa Wdowa", "Uwolniona od przysięgi sądowej")
add_occ("Snopek", "Jan", "Przedmieście Kraśnickie", "Przedmieszczanin / Aktor", None, 73, 1701, "Janem Snopkiem", "Sprawa z Tomaszem Nowakiem (termin zawity)")
add_occ("Nowak", "Tomasz", "Kraśnik", "Pozwany", None, 73, 1701, "Tomaszem Nowakiem", "Sprawa z Janem Snopkiem")
add_occ("Jędrych", "Józef", "Kraśnik", "Syn / Aktor", None, 73, 1701, "Józefem Jędrychiem", "Spór z bratem Grzegorzem")
add_occ("Jędrych", "Grzegorz", "Kraśnik", "Brat Józefa Jędrycha / Pozwany", None, 73, 1701, "Grzegorzem", "Spór z bratem Józefem")

# Skan 74 (1701)
add_occ("Jędrych", "Józef", "Kraśnik", "Aktor", None, 74, 1701, "Aktorowi", "Wyrok w sporze z bratem Grzegorzem")
add_occ("Wójcikowic", "Jakub", "Kraśnik", "Obywatel kraśnicki / Aktor", None, 74, 1701, "Jakubem Wójcikowicem", "Spór z wdową Zofią Ziębiną o zbroję miejską i 3 talary")
add_occ("Ziębina", "Zofia", "Kraśnik", "Wdowa po Adamie Ziębie / Pozwana", None, 74, 1701, "Zofią wdową Adama Zięby", "Sprawa o 3 talary i krzyż dla Bractwa Różańca Świętego")
add_occ("Zięba", "Adam", "Kraśnik", "Zmarły mieszkaniec", None, 74, 1701, "Adama Zięby", "Zmarły mąż Zofii")
add_occ("Dudkowa", "Zofia", "Przedmieście Kraśnickie", "Wdowa po Wawrzyńcu Dudku", "Jantunówna", 74, 1701, "Zofia z domu Jantunówna", "Aprobacja sprzedaży roli przez syna Stanisława (podpis krzyżykiem)")
add_occ("Dudek", "Franciszek", "Przedmieście Kraśnickie", "Syn Wawrzyńca i Zofii Dudków", None, 74, 1701, "Franciszek Dudek syn", "Aprobacja sprzedaży roli przez brata Stanisława (podpis krzyżykiem)")
add_occ("Dudek", "Stanisław", "Przedmieście Kraśnickie", "Sprzedawca roli", None, 74, 1701, "Stanisława Dudka", "Zapis aprobowany przez matkę i brata")
add_occ("Anczarek", "Tomasz", "Przedmieście Kraśnickie", "Nabywca roli", None, 74, 1701, "Tomasza Anczarka", "Nabywca w aprobacji Dudków")

# Skan 75 (1701)
add_occ("Zięba", "Tomasz", "Przedmieście Kraśnickie", "Przedmieszczanin kraśnicki / Pobity protestant", None, 75, 1701, "Tomasz Zięba Przedmieszczanin", "Obdukcja ciężkich ran zadanych brzeszczotem i kijem na drodze do Sadkowiska")
add_occ("Ziębina", "Maryna", "Przedmieście Kraśnickie", "Żona Tomasza Zięby / Poszkodowana", None, 75, 1701, "Maryny małżonki", "Chora po szamotaniu w trakcie napaści")
add_occ("Chrzanowski", "Walenty", "Rudnik", "Pracowity, poddany ze wsi Rudnika", None, 75, 1701, "Walentemu Chrzanowskiemu ze wsi Rudnika", "Oskarżony o pobicie T. Zięby i jego żony w dzień św. Marcina 1701 r.")
add_occ("Bielski", "Pan", "Rudnik", "Dziedzic / Posiadacz wsi Rudnika", None, 75, 1701, "Jegomości Pana Bielskiego", "Pan Walentego Chrzanowskiego")

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part3.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

# Eksport CSV z 9 kanonicznymi kolumnami (UTF-8-SIG, ;)
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j18_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Lp.', 'Nazwisko', 'Imie', 'Miejsce zamieszkania', 'Funkcja spoleczna', 'Warianty nazwiska', 'Numery skanow', 'Zakres lat', 'Liczba wystapien'])
    for p in gen_data:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p['funkcja'],
            p.get('wariant_nazwiska') or '',
            p['skany_roboczo'],
            p['zakres_lat'],
            p['liczba_wystapien']
        ])

print(f"Zapisano gen_data_j18_part3.json: {len(gen_data)} unikalnych profili.")
print(f"Zapisano {csv_path}")
