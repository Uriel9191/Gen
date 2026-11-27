# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part8.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

by_key = {}
for p in gen_data:
    k = (p["nazwisko"].strip().lower(), p["imie"].strip().lower(), (p.get("miejsce") or "").strip().lower())
    by_key[k] = p

def add_occ(nazwisko, imie, miejsce, funkcja, wariant, skan, rok, zapis_orig, rola, notatka):
    k = (nazwisko.strip().lower(), imie.strip().lower(), miejsce.strip().lower())
    if k in by_key:
        p = by_key[k]
        if wariant:
            existing_w = p.get("wariant_nazwiska") or ""
            parts = [x.strip() for x in existing_w.split("/") if x.strip()]
            for nw in [x.strip() for x in wariant.split("/") if x.strip()]:
                if nw not in parts:
                    parts.append(nw)
            p["wariant_nazwiska"] = " / ".join(parts) if parts else None
        if funkcja and funkcja not in (p.get("funkcja") or ""):
            if p.get("funkcja"):
                p["funkcja"] = f"{p['funkcja']}; {funkcja}"
            else:
                p["funkcja"] = funkcja
        if int(skan) not in p["skany_list"]:
            p["skany_list"].append(int(skan))
            p["skany_list"].sort()
            p["skany_roboczo"] = ", ".join(f"#{s}" for s in p["skany_list"])
        p["wystapienia"].append({
            "skan": int(skan),
            "rok": str(rok),
            "zapis_oryginalny": zapis_orig,
            "rola": rola
        })
        p["liczba_wystapien"] = len(p["wystapienia"])
        years = []
        for w in p["wystapienia"]:
            for y in str(w["rok"]).replace("–", "-").split("-"):
                y = y.strip()
                if y.isdigit():
                    years.append(int(y))
        if years:
            p["min_rok"] = min(years)
            max_y = max(years)
            p["zakres_lat"] = str(p["min_rok"]) if p["min_rok"] == max_y else f"{p['min_rok']}–{max_y}"
        if notatka and notatka not in (p.get("notatka_biograficzna") or ""):
            p["notatka_biograficzna"] = (p.get("notatka_biograficzna") or "").rstrip(".") + ". " + notatka
    else:
        yr_nums = [int(y.strip()) for y in str(rok).replace("–", "-").split("-") if y.strip().isdigit()]
        min_y = min(yr_nums) if yr_nums else 1698
        max_y = max(yr_nums) if yr_nums else 1698
        zakres = str(min_y) if min_y == max_y else f"{min_y}–{max_y}"
        rec = {
            "lp": len(gen_data) + 1,
            "nazwisko": nazwisko,
            "imie": imie,
            "miejsce": miejsce,
            "funkcja": funkcja,
            "wariant_nazwiska": wariant if wariant else None,
            "skany_list": [int(skan)],
            "skany_roboczo": f"#{int(skan)}",
            "min_rok": min_y,
            "zakres_lat": zakres,
            "liczba_wystapien": 1,
            "wystapienia": [{
                "skan": int(skan),
                "rok": str(rok),
                "zapis_oryginalny": zapis_orig,
                "rola": rola
            }],
            "notatka_biograficzna": notatka
        }
        gen_data.append(rec)
        by_key[k] = rec

# === PARTIA 9 (SKANY 201–225) ===

# Skan 201 (1664)
add_occ("Jajczyk", "Kasper", "Kraśnik", "Mieszczanin", None, 201, "1664", "Kasper Jajczyk", "Powód (ugoda na 220 złp)", "Uzyskuje ugodę od Sebastiana Jajczyka na spłatę 220 złp długu po ojcu.")
add_occ("Jajczyk", "Sebastian", "Kraśnik", "Mieszczanin", None, 201, "1664", "Sebastian Jajczyk", "Pozwany (zobowiązany do 220 złp)", "Spłaca dług w ratach: 2 zł, 120 zł po jarmarku, 100 zł na św. Michała.")
add_occ("Łosika", "Katarzyna", "Kraśnik", "Mieszczanka", "Łożyka [?] / Łosika [Łożyka?]", 201, "1664", "Catharina Łosika", "Powódka z córką Agnieszką", "Proces przeciw Magdalenie Piotra Łownej.")
add_occ("Łosika", "Agnieszka", "Kraśnik", "Córka Katarzyny Łosiki", "Łożyka [?]", 201, "1664", "filia eius Agnes", "Współpowódka z matką", "Proces przeciw Magdalenie Piotra Łownej.")
add_occ("Łowna", "Magdalena Piotra", "Kraśnik", "Mieszczanka", None, 201, "1664", "Magdalena Piotra Łowna", "Pozwana", "Pozwana przez Katarzynę i Agnieszkę Łosików.")

# Skan 202 (1664)
add_occ("Łosika", "Katarzyna", "Kraśnik", "Mieszczanka", "Łożyka [?]", 202, "1664", "Katarzyna Łosika", "Powódka (wydzielenie roli za 3 zł 15 gr)", "Sąd nakazuje wydzielić śnież/rolę za 3 zł 15 gr nakładów.")
add_occ("Muszka", "Piotr", "Kraśnik", "Mieszczanin", None, 202, "1664", "Petrus Muszka", "Powód o włamanie do komory i pobicie", "Oskarża Tomasza Jajczyka o kradzież zboża z komory oraz pobicie na drodze z kościoła.")
add_occ("Jajczyk", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 202, "1664", "Thomas Jajczyk", "Pozwany o włamanie i pobicie", "Mieszka u Jakuba Smazanowskiego; przyznaje się do pobicia, wypiera się kradzieży.")
add_occ("Smazanowski", "Jakub", "Kraśnik", "Sławetny (gospodarz Jajczyka)", None, 202, "1664", "Sławetny Jakub Smazanowski", "Świadek na korzyść T. Jajczyka", "Zeznaje, że Tomasz Jajczyk nigdy nie był podejrzany o kradzież.")

# Skan 203 (1664)
add_occ("Muszka", "Piotr", "Kraśnik", "Mieszczanin", None, 203, "1664", "Petrus Muszka", "Powód (nakaz stawienia świadków)", "Ma stawić świadków na pobicie w piątek.")
add_occ("Jajczyk", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 203, "1664", "Thomas Jajczyk", "Pozwany (przysięga oczyszczająca)", "Nakazana przysięga oczyszczająca w piątek.")
add_occ("Lisik", "Maciej", "Kraśnik", "Mieszczanin", None, 203, "1664", "Mathias Lisik", "Powód o dziesięcinę jęczmienia", "Dochodzi należności za jęczmień od Andrzeja Macala.")
add_occ("Macal", "Andrzej", "Kraśnik", "Mieszczanin", None, 203, "1664", "Andreas Macal", "Pozwany z żoną o jęczmień", "Pozwany o dług po pierwszym mężu żony Gabrielu Bąku.")
add_occ("Bąk", "Gabriel", "Kraśnik", "Mieszczanin (zm.)", "Bąk [?]", 203, "1664", "nieboszczyk Gabriel Bąk", "Zmarły pierwszy mąż pozwanej", "Wzmiankowany jako kupujący jęczmień.")

# Skan 204 (1698)
add_occ("Luterski", "Stanisław", "Kraśnik (Przedmieście)", "Przedmieszczanin / Brat cechu kuśnierskiego", None, 204, "1698", "Stanisław Luterski Brat Cechu Kuśnierskiego", "Powód przeciw cechowi kuśnierskiemu", "Wnosi o rewizję ksiąg i przywilejów cechu kuśnierskiego.")
add_occ("Jesurkiewicz", "Stanisław", "Kraśnik", "Stary rajca / Cechmistrz kuśnierski", None, 204, "1698", "Stanisław Jesurkiewicz Cechmistrz", "Przedstawiciel cechu kuśnierskiego", "Staje w sporze ze Stanisławem Luterskim.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły / Cechmistrz kuśnierski", None, 204, "1698", "Wawrzyniec Bielaszkowic Cechmistrz", "Przedstawiciel cechu kuśnierskiego", "Staje w sporze z Luterskim.")
add_occ("Chmielowicz", "Adam Michał", "Kraśnik", "Pisarz kraśnicki", None, 204, "1698", "Adam Michał Chmielowic Pisarz", "Deputowany do rewizji akt cechu", "Wyznaczony przez sąd do rewizji przywilejów.")
add_occ("Solecki", "Stanisław", "Kraśnik", "Rajca kraśnicki", None, 204, "1698", "Stanisław Solecki Radca", "Deputowany do rewizji akt cechu", "Wyznaczony z Janem Barankowiczem.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 204, "1698", "Jan Barankowicz Radca", "Deputowany do rewizji akt cechu", "Wyznaczony przez sąd.")
add_occ("Bartoszek", "Grzegorz", "Kraśnik", "Uczciwy", None, 204, "1698", "H. Gregorius Bartoszek", "Powód uzyskujący kontumację", "Uzyskuje wyrok 3 grzywien przeciw Janowi Smorzikowi.")
add_occ("Smorzik", "Jan", "Kraśnik", "Uczciwy", "Smorzik [?]", 204, "1698", "H. Joannes Smorzik", "Skazany zaocznie na 3 grzywny", "Pozwany o posądzenie o kradzież.")
add_occ("Mutkowic", "Tomasz", "Kraśnik", "Towarzysz rzemiosła szewskiego", None, 204, "1698", "H. Thomas Mutkowic", "Powód uzyskujący 3 grzywny", "Uzyskuje wyrok przeciw majstrowi Szymonowi Soleckiemu.")
add_occ("Solecki", "Szymon", "Kraśnik", "Majster rzemiosła szewskiego", None, 204, "1698", "H. Simon Solecki Magister", "Skazany na 3 grzywny", "Skazany w sporze z Tomaszem Mutkowicem.")

# Skan 205 (1698)
add_occ("Bartoszek", "Grzegorz", "Kraśnik", "Uczciwy", None, 205, "1698", "H. Gregorius Bartoszek", "Protestujący przeciw Smorzikowi", "Protestuje o posądzenie o kradzież klaczy/krowy.")
add_occ("Smorzik", "Jan", "Kraśnik", "Uczciwy", "Smorzik [?]", 205, "1698", "H. Joannes Smorzik", "Pozwany o zniesławienie", "Zarzucił Bartoszkowi kradzież.")
add_occ("Kozak", "Paweł", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 205, "1698", "H. Paulus Kozak suburbanus", "Protestujący i prezentujący rany", "Pobity na drodze publicznej przez Rdzonków.")
add_occ("Rdzonka", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin (syn Bartłomieja)", "Rdzonek [Rozdzeń?] / Rozdzeń [?]", 205, "1698", "Albertus Rdzonek", "Pozwany o pobicie na drodze", "Oskarżony wraz z rodzicami o pobicie Pawła Kozaka.")
add_occ("Rdzonka", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin (ojciec Wojciecha)", "Rdzonek [Rozdzeń?]", 205, "1698", "Bartholomeus Rdzonek", "Współpozwany o pobicie", "Oskarżony z synem i żoną Zofią.")
add_occ("Rdzonkowa", "Zofia", "Kraśnik (Przedmieście)", "Żona Bartłomieja Rdzonka", "Rozdzeniowa [?]", 205, "1698", "Sophia Bartholomei Rdzonek consors", "Współpozwana o pobicie", "Oskarżona z mężem i synem.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 205, "1698", "Paulus Słomkowski Viceadvocatus", "Urzędnik przy obdukcji ran", "Ogląda rany Pawła Kozaka.")
add_occ("Dzymanowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", "Dzimanowski [?] / Dzymanowski [Dzimanowski?]", 205, "1698", "Albertus Dzymanowski Scabinus Juratus", "Ławnik przy obdukcji ran", "Ogląda rany Pawła Kozaka.")

# Skan 206 (1698)
add_occ("Skarz", "Matyjasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Skarz [?]", 206, "1698", "Matyasz Skarz", "Skarżący wójta gromadzkiego", "Pobity laską przez wójta gromadzkiego przy sporze o składkę.")
add_occ("[Wójt gromadzki]", "Wojciech", "Kraśnik (Karczówka)", "Wójt gromadzki", None, 206, "1698", "Wójt Gromadzki Wojciech z Karczówki", "Pozwany o pobicie laską", "Uderzył laską Matyasza Skarza.")
add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 206, "1698", "Martinus Rymarczyk", "Powód powołujący świadka", "Powołuje świadka przeciw żonie Stryczaka.")
add_occ("Skowronek", "Matyjasz", "Kraśnik", "Uczciwy (świadek)", "Skowronek [?]", 206, "1698", "H. Mathias Skowronek", "Świadek zniewagi Rymarczyka", "Zeznaje o słowach Stryczakowej.")

# Skan 207 (1698)
add_occ("Kłopot", "Jakub", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 207, "1698", "Jacobus Kłopot suburbanus", "Skazany zaocznie (2. kontumacja)", "Pozwany przez Tomasza Nowackiego o wypasioną potrawę.")
add_occ("Nowacki", "Tomasz", "Kraśnik", "Mieszczanin", None, 207, "1698", "H. Thomas Nowacki", "Powód uzyskujący 2. kontumację", "Uzyskuje nakaz ujęcia Jakuba Kłopota.")
add_occ("Bożkowic", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 207, "1698", "Pan Wojciech Bożkowic Ławnik", "Powód uzyskujący 1. kontumację", "Uzyskuje kontumację przeciw Adamowi Kowalczykowi o dług.")
add_occ("Kowalczyk", "Adam", "Kraśnik", "Uczciwy", "Kowalczyk [?]", 207, "1698", "Adam Kowalczyk", "Skazany zaocznie (1. kontumacja)", "Pozwany o dług przez Wojciecha Bożkowica.")
add_occ("Peron", "Maciej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 207, "1698", "Mathias Peron suburbanus", "Skazany zaocznie na 3 grzywny", "Pozwany z bratem i synami przez Pawła Słomkowskiego.")
add_occ("Wawrzyło", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 207, "1698", "Albertus Wawrzyło", "Skazany zaocznie na 3 grzywny", "Współpozwany z bratem Maciejem Peronem.")
add_occ("Peron", "Wojciech", "Kraśnik (Przedmieście)", "Syn Macieja Perona", None, 207, "1698", "Albertus Peron", "Współpozwany o sześćdziesiątki żyta", "Skazany z ojcem.")
add_occ("Wawrzyło", "Jakub", "Kraśnik (Przedmieście)", "Syn / Krewny", None, 207, "1698", "Jacobus Wawrzyło", "Współpozwany o sześćdziesiątki żyta", "Skazany z braćmi.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 207, "1698", "Paulus Słomkowski Viceadvocatus", "Powód uzyskujący kontumację", "Uzyskuje karę 3 grzywien.")

# Skan 208 i 209 (dublet) (1698)
add_occ("Skarz", "Matyjasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Skarz [?]", 208, "1698", "Matyasz Skarz", "Powód o pobicie przy składce", "Skarży dziesiętnika Pawła Kłopota.")
add_occ("Kłopot", "Paweł", "Kraśnik", "Dziesiętnik przedmiejski", None, 208, "1698", "Paweł Kłopot Dziesiętnik", "Pozwany skazany na 3 dni wieży i 2 grzywny", "Przysięga, że 2 złp nie brał dla siebie; skazany za pobicie.")
add_occ("Skarz", "Matyjasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Skarz [?]", 209, "1698", "Matyasz Skarz (dublet skanu 208)", "Powód (dublet mikrofilmu)", "Powtórna klatka fol. 104r.")
add_occ("Kłopot", "Paweł", "Kraśnik", "Dziesiętnik przedmiejski", None, 209, "1698", "Paweł Kłopot (dublet skanu 208)", "Pozwany (dublet mikrofilmu)", "Powtórna klatka fol. 104r.")

# Skan 210 (fol. 104v, 1698)
add_occ("Skarz", "Matyjasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Skarz [?]", 210, "1698", "Mathias Skarz", "Powód przeciw W. Tokarczykowi", "Sprawa o pobicie i odmowę składki na folwark.")
add_occ("Tokarczyk", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 210, "1698", "Albertus Tokarczyk", "Pozwany o pobicie", "Dylacja na inkwizycję.")
add_occ("Kłopot", "Paweł", "Kraśnik", "Dziesiętnik przedmiejski", None, 210, "1698", "Honestus Paulus Kłopot", "1. świadek", "Zeznaje o wygnaniu z kijem przez żonę Skarza przy zbieraniu składki.")

# Skan 211 (fol. 105r, 1698)
add_occ("Berkowski", "Jędrzej", "Kraśnik", "Pracowity (poszkodowany)", "Berkowski [?]", 211, "1698", "Laboriosus Andreas Berkowski", "Prezentujący rany (obdukcja)", "Włóczony za włosy, guzy na boku i ręce.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Ławnik przysięgły", None, 211, "1698", "Stephan Kwasowic", "Ławnik przy obdukcji", "Ogląda rany Jędrzeja Berkowskiego.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły / Opiekun", None, 211, "1698", "Wojciech Grzymałowski", "Ławnik i pozwany opiekun", "Ogląda rany; pozwany przez Piotra Tokarczyka o dom po Szymonie Kościńskim.")
add_occ("Tokarczyk", "Piotr", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 211, "1698", "Piotr Tokarczyk Przedmieszczanin", "Powód o pieniądze ze sprzedaży domu w Rynku", "Skarży opiekunów o brak rozliczenia za dom sprzedany Janowi Majowskiemu.")
add_occ("Kościński", "Szymon", "Kraśnik", "Ławnik / Mieszczanin (zm.?)", None, 211, "1698", "Szymon Kościński", "Wzmiankowany przy opiece nad dobrami", "Współopiekun / strona w sporze Tokarczyka.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 211, "1698", "Jan Majowski Rajca", "Nabywca domu w Rynku", "Kupił dom w Rynku w sprawie Tokarczyka.")

# Skan 212 (fol. 105v, 1698)
add_occ("Kłopot", "Wojciech", "Kraśnik", "Mieszczanin", None, 212, "1698", "Albertus Kłopot", "Skazany na 3 grzywny i 3 dni wieży", "Wyrok z 21 VII 1698 r.")
add_occ("Tokarczyk", "Piotr", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 212, "1698", "Petrus Tokarczyk", "Powód (dylacja)", "Sprawa z opiekunami odroczona.")
add_occ("Potocki", "Adam", "Kraśnik", "Prokonsul / Opiekun", "Potokowicz", 212, "1698", "F. Adamus Potokowicz", "Opiekun w sprawie Tokarczyka", "Wymieniony obok Wojciecha Grzymałowskiego.")
add_occ("Michalski", "Kazimierz", "Kraśnik", "Sławetny", None, 212, "1698", "Famatus Casimirus Michalski", "Powód przeciw S. Biegajczykowi", "Dylacja na inkwizycję do środy.")
add_occ("Biegajczyk", "Stanisław", "Kraśnik", "Pozwany", "Biegajczyk [?] / Biegaj [Biegajczyk?]", 212, "1698", "Stanislaus Biegajczyk", "Pozwany", "Sprawa z Kazimierzem Michalskim.")
add_occ("Wierzuk", "Jan", "Kraśnik", "Uczciwy", "Wierzuk [?]", 212, "1698", "Honestus Joannes Wierzuk", "Skazany zaocznie na 2 grzywny", "Skazany z instancji Wojciecha Grzymałowskiego.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 212, "1698", "Albertus Grzymałowski", "Powód uzyskujący kontumację", "Uzyskuje karę 2 grzywien.")
add_occ("Boron", "Matyjasz", "Kraśnik", "Uczciwy", "Boron [?]", 212, "1698", "Uciwy Matyasz Boron", "Protestujący o pobicie", "Pobity w sobotę w drodze do kościoła.")

# Skan 213 (fol. 106r, 1698)
add_occ("Grotowski", "Jan", "Kraśnik", "Uczciwy (nabywca gruntu)", "Grotowski [?]", 213, "1698", "Uciwy Jan Grotowski", "Strona intromisji z 23 III 1698 r.", "Wprowadzony z żoną Ewą w nabyty grunt.")
add_occ("Grotowska", "Ewa", "Kraśnik", "Żona Jana Grotowskiego", "Grotowska [?]", 213, "1698", "Ewa Grotowska", "Współnabywczyni gruntu", "Wprowadzona w posesję z mężem.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci kraśnicki", None, 213, "1698", "Paweł Słomkowski Podwójci", "Deputowany do intromisji", "Przeprowadza intromisję Grotowskich.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 213, "1698", "Wojciech Grzymałowski Ławnik", "Ławnik przy intromisji", "Obecny 23 III 1698 r.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 213, "1698", "Wawrzyniec Bielaszkowic Ławnik", "Ławnik przy intromisji", "Obecny 23 III 1698 r.")
add_occ("Józefkowic", "Jakub", "Kraśnik", "Pracowity", "Josepkowic", 213, "1698", "Jakub Josepkowic", "Przepraszający kowala Rygara", "Odwołuje zarzuty pod vadium 14 grzywien.")
add_occ("Rygar", "Jan", "Kraśnik", "Kowal kraśnicki", "Rygar [?]", 213, "1698", "Jan Rygar Kowal Kraśnicki", "Przeproszony przez J. Józefkowica", "Zawiera zgodę pod zakładem 14 grzywien.")

# Skan 214 (fol. 106v, 1698)
add_occ("Koplowic", "Moszek", "Kraśnik", "Żyd kraśnicki", None, 214, "1698", "Niewierny Moszek Koplowic", "Powód przeciw M. Pilaskiewiczowi", "Dylacja do dalszej informacji.")
add_occ("Pilaskiewicz", "Matyjasz", "Kraśnik", "Sławetny", "Bielaszkowic [?] / Pilaskiewicz [Bielaszkowic?]", 214, "1698", "Matyasz Pilaskiewicz", "Pozwany przez Moszka Koplowica", "Dylacja.")
add_occ("Izaak", "[Kantor synagogi]", "Kraśnik", "Kantor synagogi kraśnickiej", None, 214, "1698", "Infidelis Isaac Cantor Sinagogae Crasnicensis", "Powód uzyskujący kontumację", "Uzyskuje karę 3 grzywien przeciw Janowi Grymuzie.")
add_occ("Ornatowski", "Wojciech", "Kraśnik", "Bedel sądowy", None, 214, "1698", "Albertus Ornatowski Bedellus", "Bedel doręczający pozew", "Relacjonuje pozew kantora synagogi.")
add_occ("Grymuza", "Jan", "Kraśnik", "Sławny (syn Jana Grymuzy)", None, 214, "1698", "Joannes Grymuza", "Skazany zaocznie na 3 grzywny", "Pozwany przez kantora synagogi.")
add_occ("Moszek", "Jakub", "Kraśnik", "Żyd kraśnicki", None, 214, "1698", "Jakub Moszek", "Przypozwany", "Krótki wpis o przypozwie.")
add_occ("Chmielek", "Sebastian", "Kraśnik", "Uczciwy (sukcesor)", None, 214, "1698", "Sebastian Chmielek", "Protestujący o dział dóbr", "Protestuje przeciw Błażejowi i Katarzynie Chmielkom.")
add_occ("Chmielkowa", "Anna", "Kraśnik", "Żona Sebastiana Chmielka", None, 214, "1698", "Anna Chmielkowa", "Współprotestująca", "Zelżona w gospodzie przez Błażeja Chmielka.")
add_occ("Chmielek", "Błażej", "Kraśnik", "Uczciwy", None, 214, "1698", "Błażej Chmielek", "Pozwany o wstrzymywanie działu i zniewagę", "Trzymał dobra kilkanaście lat za życia matki.")
add_occ("Chmielkowa", "Katarzyna", "Kraśnik", "Uczciwa", None, 214, "1698", "Katarzyna Chmielkowa", "Współpozwana o dział dóbr", "Współpozwana z Błażejem Chmielkiem.")

# Skan 215 (fol. 107r, 1698)
add_occ("Pradkowski", "Stanisław", "Kraśnik", "Uczciwy", "Pradkowski [?]", 215, "1698", "Stanisław Pradkowski", "Wnioskujący o wizję szkody", "Wizja szkody parobka Kazimierza.")
add_occ("[Parobek Dubaja]", "Kazimierz", "Kraśnik", "Parobek Wojciecha Dubaja", None, 215, "1698", "Kazimierz parobek Wojciecha Dubaja", "Obwiniony o szkodę na polu", "Przedmiot wizji z 9 IV 1698 r.")
add_occ("Dubaj", "Wojciech", "Kraśnik", "Mieszczanin", None, 215, "1698", "Wojciech Dubaj", "Chlebodawca parobka Kazimierza", "Wzmiankowany w wizji z 9 IV 1698 r.")
add_occ("Oszmarowic", "Kazimierz", "Kraśnik", "Ławnik przysięgły", "Oszmarowic [?]", 215, "1698", "Pan Kazimierz Oszmarowic Ławnik", "Ławnik wizjujący szkodę", "Wizjuje pole 9 IV 1698 r.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", "Pilaszkowic", 215, "1698", "Wawrzyniec Pilaszkowic Ławnik", "Ławnik wizjujący szkodę", "Wizjuje pole 9 IV 1698 r.")
add_occ("Koszykowic", "Kazimierz", "Kraśnik", "Uczciwy", "Koszykowic [?]", 215, "1698", "Kazimierz Koszykowic", "Wnioskujący o wizję płotu", "Spór z Pawłem Ablem o niegrodzenie ogrodu.")
add_occ("Abel", "Paweł", "Kraśnik", "Sławny / Mieszczanin", None, 215, "1698", "Paweł Abel", "Pozwany o grodzenie płotu", "Ma postawić połowę płotu.")
add_occ("Bożkowic", "Stefan", "Kraśnik", "Ławnik przysięgły", "Bożkowic [?]", 215, "1698", "Stephan Bożkowic Ławnik", "Ławnik wizjujący ogród", "Deputowany 11 IV 1698 r.")
add_occ("Bożkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", "Bożkowic [?]", 215, "1698", "Wawrzyniec Bożkowic Ławnik", "Ławnik wizjujący ogród", "Deputowany 11 IV 1698 r.")
add_occ("Okoniowa", "Elżbieta", "Kraśnik (Przedmieście)", "Wdowa (matka Jana Okonia)", None, 215, "1698", "Uciwa Elżbieta pozostała małżonka", "Powódka z synem o 85 złp", "Skarży Adama Wilka o resztę ze 110 złp za karczmę.")
add_occ("Okoń", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin (syn Elżbiety)", None, 215, "1698", "Jan Okoń", "Współpowód z matką", "Dochodzi 85 złp od Adama Wilka.")
add_occ("Wilk", "Adam", "Kraśnik", "Mieszczanin", None, 215, "1698", "Adam Wilk", "Pozwany o 85 złp długu", "Zapłacił dotąd 25 złp ze 110 złp.")

# Skan 216 (fol. 107v, 1698)
add_occ("Wilk", "Adam", "Kraśnik", "Mieszczanin", None, 216, "1698", "Adam Wilk", "Pozwany skazany na spłatę 85 złp", "Ma oddać 30 złp w niedzielę i 55 złp po św. Wojciechu.")
add_occ("Okoniowa", "Elżbieta", "Kraśnik (Przedmieście)", "Wdowa", None, 216, "1698", "Elżbieta Okoniowa", "Powódka wygrywająca 85 złp", "Wyrok z 11 IV 1698 r.")
add_occ("Koszykowic", "Kazimierz", "Kraśnik", "Uczciwy", "Koszykowic [?]", 216, "1698", "Kazimierz Koszykowic", "Powód o ogród", "Dylacja do poniedziałku.")
add_occ("Abel", "Paweł", "Kraśnik", "Mieszczanin", None, 216, "1698", "Paweł Abel", "Pozwany (zastawny posiadacz gruntu)", "Twierdzi, że trzyma grunt zastawem.")

# Skan 217 (fol. 108r, 1698)
add_occ("Studzicki", "Sebastian", "Kraśnik", "Uczciwy", None, 217, "1698", "Uciwy Sebastian Studzicki", "Powód przeciw szwagrowi", "Spór o dobra po zmarłej matce trzymane zastawem.")
add_occ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Szewc / Szwagier Studzickiego", None, 217, "1698", "Błażej Stachowicz Szwagier", "Pozwany (dylacja)", "Prosi o dylację na okazanie dokumentów.")
add_occ("Tomkowic", "Stanisław", "Kraśnik", "Sławetny", "Tomkowic [?]", 217, "1698", "Famatus Stanislaus Tomkowic", "Powód uzyskujący kontumację", "Uzyskuje kontumację przeciw Janowi Trawińskiemu.")
add_occ("Trawiński", "Jan", "Kraśnik", "Mieszczanin", None, 217, "1698", "Honestus Joannes Trawiński", "Skazany zaocznie (2 kontumacje)", "Pozwany przez Stanisława Tomkowica i Stanisława Latoska.")
add_occ("Kurcel", "Wojciech", "Kraśnik", "Uczciwy", "Kurcel [?]", 217, "1698", "Honestus Albertus Kurcel", "Powód uzyskujący kontumację", "Uzyskuje kontumację przeciw Jakubowi Piserkowi.")
add_occ("Piserek", "Jakub", "Kraśnik", "Uczciwy", "Piserek [?]", 217, "1698", "Honestus Jacobus Piserek", "Skazany zaocznie", "Pozwany przez Wojciecha Kurcela.")
add_occ("Latosek", "Stanisław", "Kraśnik", "Uczciwy", "Latosek [?]", 217, "1698", "Honestus Stanislaus Latosek", "Powód uzyskujący kontumację", "Uzyskuje kontumację przeciw Janowi Trawińskiemu.")

# Skan 218 (fol. 108v, 1698)
add_occ("Dubaj", "Jakub", "Kraśnik", "Mieszczanin", None, 218, "1698", "Uciwy Jakub Dubaj", "Sprzedawca ćwierci roli za 180 złp", "Sprzedaje z żoną Anną Zdębiówną ćwierć roli ojcowskiej.")
add_occ("Zdębiówna", "Anna", "Kraśnik", "Żona Jakuba Dubaja", "Zdębiówna [?]", 218, "1698", "Anna Zdębiówna", "Współsprzedawczyni roli", "Zastrzega prawo odkupu.")
add_occ("Dubaj", "Wojciech", "Kraśnik", "Mieszczanin", None, 218, "1698", "Wojciech Dubaj brat", "Obecny przy sprzedaży roli brata", "Asystuje Jakubowi Dubajowi.")
add_occ("Rakowski", "Stanisław", "Kraśnik", "Uczciwy (kupiec roli)", None, 218, "1698", "Uciwy Stanisław Rakowski", "Nabywca ćwierci roli za 180 złp", "Kupuje rolę z żoną Marianną Piotrowczykówną.")
add_occ("Piotrowczykówna", "Marianna", "Kraśnik", "Żona Stanisława Rakowskiego", None, 218, "1698", "Maryanna Piotrowczykówna", "Współnabywczyni roli", "Kupuje rolę z mężem.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci kraśnicki", None, 218, "1698", "Paweł Słomkowski Podwójci", "Deputowany do intromisji", "Wprowadza Rakowskich w posesję roli.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Ławnik przysięgły", None, 218, "1698", "Stefan Kwasowic Ławnik", "Ławnik przy intromisji", "Obecny przy sprzedaży roli.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 218, "1698", "Wojciech Grzymałowski Ławnik", "Ławnik przy intromisji", "Obecny przy sprzedaży roli.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 218, "1698", "Wawrzyniec Bielaszkowic Ławnik", "Ławnik przy intromisji", "Obecny przy sprzedaży roli.")

# Skan 219 (fol. 109r, 1698)
add_occ("Studzicki", "Sebastian", "Kraśnik", "Uczciwy", None, 219, "1698", "Sebastianus Studzicki", "Powód o sukcesję po K. Nogajowej", "Dylacja z 16 IV 1698 r.")
add_occ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Szewc", None, 219, "1698", "Blasius Stachowicz", "Pozwany o sukcesję", "Dylacja do piątku.")
add_occ("Kępa", "Szymon", "Kraśnik", "Uczciwy", None, 219, "1698", "Honestus Kempa Szymon", "Zwolniony z pozwu (niestawiennictwo powoda)", "Pozwany przez Józefa Rabaka.")
add_occ("Rabak", "Józef", "Kraśnik", "Pracowity / Powód", "Rabak [?]", 219, "1698", "Josephus Rabak", "Powód niestawający na termin", "Pozwał Szymona Kępę.")
add_occ("Woszek", "Jakub", "Kraśnik", "Uczciwy", "Woszek [?]", 219, "1698", "Jacobus Woszek", "Pozwany o dobra po matce", "Sprawa z Wojciechem i Agnieszką.")
add_occ("Skowroński", "Andrzej", "Kraśnik", "Uczciwy", "Skowroński [?]", 219, "1698", "Andreas Skowroński", "Powód przeciw Tokarczykom", "Sprawa o egzekucję przeciw Janowi i Matce Tokarczykowej.")
add_occ("Tokarczyk", "Jan", "Kraśnik", "Pozwany", None, 219, "1698", "Joannes Tokarczyk", "Pozwany z matką", "Pozwany przez Andrzeja Skowrońskiego.")
add_occ("Araczniak", "Maciej", "Kraśnik", "Mieszczanin", "Araczniak [?]", 219, "1698", "Mathias Araczniak", "Powód o 22 złp i owies", "Sprawa z Wojciechem Dubajem o zastawioną rolę.")
add_occ("Dubaj", "Wojciech", "Kraśnik", "Mieszczanin", None, 219, "1698", "Albertus Dubaj", "Pozwany o 22 złp i owies", "Zastaw roli za 22 złp.")

# Skan 220 (fol. 109v, 1698)
add_occ("Grymuza", "Jan", "Kraśnik", "Sławny", None, 220, "1698", "Joannes Grymuza", "Uzyskujący areszt na Tękupowskiej", "Areszt na majątku Tękupowskiej.")
add_occ("Abel", "Paweł", "Kraśnik", "Mieszczanin", None, 220, "1698", "Honestus Abel", "Skazany zaocznie na 1 grzywnę", "Skazany z instancji Kazimierza Koszykowica.")
add_occ("Koszykowic", "Kazimierz", "Kraśnik", "Uczciwy", "Koszykowic [?]", 220, "1698", "Casimirus Koszykowic", "Powód uzyskujący karę 1 grzywny", "Sprawa z Pawłem Ablem.")
add_occ("Kaczorkowic", "Grzegorz", "Kraśnik", "Ślusarz / Mieszczanin", None, 220, "1698", "Sławetny Grzegorz Kaczorkowic Ślosarz", "Kwitujący S. Kwasowica po procesie w Trybunale", "Zawiera kompromis pod zakładem 14 grzywien.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Dawny rajca / Ławnik", None, 220, "1698", "Stefan Kwasowic Rajca dawny", "Kwitowany z kondemnaty trybunalskiej i zasiadający w sądzie", "Ukontentował Kaczorkowica.")
add_occ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt i sędzia kraśnicki", "Onupkiewicz [Kieniewicz?]", 220, "1698", "Jan Onupkiewicz Wójt y sędzia", "Przewodniczący sądu przy ugodzie", "Obecny przy kwitacji Kaczorkowica.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci kraśnicki", None, 220, "1698", "P. Paweł Słomkowski Podwójci", "Podwojci w sądzie", "Obecny przy ugodzie.")
add_occ("Bożkowic", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 220, "1698", "Wojciech Bożkowic Ławnik", "Ławnik przy ugodzie", "Obecny przy kwitacji Kaczorkowica.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 220, "1698", "Wawrzyniec Bielaszkowic Ławnik", "Ławnik przy ugodzie", "Obecny przy kwitacji.")

# Skan 221 (fol. 110r, 1698)
add_occ("Rabak", "Józef", "Kraśnik", "Pracowity", "Rabak [?]", 221, "1698", "pracowity Józef Rabak", "Powód o kulbakę i 8 złp", "Sprawa z 18 IV 1698 r. przeciw Grzegorzowi Kaczorkowicowi.")
add_occ("Kaczorkowic", "Grzegorz", "Kraśnik", "Ślusarz / Mieszczanin", None, 221, "1698", "Grzegorz Kaczorkowic ślosarz", "Pozwany o 8 złp za kulbakę", "Prosi o komplanację przyjaciół.")
add_occ("Koszykowic", "Kazimierz", "Kraśnik", "Uczciwy", "Koszykowic [?]", 221, "1698", "Koszykowic", "Powód o ogród", "Spór z Pawłem Ablem.")
add_occ("Abel", "Paweł", "Kraśnik", "Mieszczanin", None, 221, "1698", "Paweł Abel", "Pozwany o grodzenie ogrodu", "Ogród zastawiony przez Panią Jorkową.")
add_occ("Grymuza", "Jan", "Kraśnik", "Sławny", None, 221, "1698", "Jan Grymuza", "Dziedzic niwki Kondupowskiej", "Wpis o niwce przypadającej mu po rodzicu.")
add_occ("Studzicki", "Sebastian", "Kraśnik", "Uczciwy", None, 221, "1698", "Sebastian Studzicki", "Powód o dobra i testament", "Spór ze Stachowicami o udziały dzieci (Balcer, Tomasz, Jan, Sebastian).")
add_occ("Studzicka", "Anna", "Kraśnik", "Żona Sebastiana Studzickiego", None, 221, "1698", "Anna Studzicka", "Współpowódka", "Żona Sebastiana Studzickiego.")
add_occ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Szewc", None, 221, "1698", "Błażej Stachowic", "Pozwany o dobra po matce", "Współpozwany z żoną Katarzyną.")
add_occ("Stachowicowa", "Katarzyna", "Kraśnik (Przedmieście)", "Żona Błażeja Stachowica", None, 221, "1698", "Katarzyna Stachowicowa", "Współpozwana", "Wzmiankowana w testamencie.")

# Skan 222 (fol. 110v, 1698)
add_occ("Studzicki", "Sebastian", "Kraśnik", "Uczciwy", None, 222, "1698", "Sebastian Studzicki", "Ojciec małoletnich (po 30 złp)", "Zapis po 30 złp na każdego z synów.")
add_occ("Studzicka", "Anna", "Kraśnik", "Żona Sebastiana Studzickiego", None, 222, "1698", "Anna Studzicka", "Matka małoletnich", "Zapis po 30 złp na każdego z synów.")
add_occ("Woszek", "Jakub", "Kraśnik", "Uczciwy", "Woszek [?]", 222, "1698", "Uciwy Jakub Woszek", "Pozwany skazany na wydanie wieprza lub 8 złp", "Wyrok z 25 IV 1698 r. na rzecz Wojciecha i Doroty.")

# Skan 223 (fol. 111r, 1698)
add_occ("Michałowic", "Franciszek", "Kraśnik", "Sławny", None, 223, "1698", "Sławny Franciszek Michałowic", "Powód o zniewagę żony na Rynku", "Sprawa z żoną Agnieszką przeciw Grzegorzowi Kaczorkowicowi.")
add_occ("Michałowicowa", "Agnieszka", "Kraśnik", "Żona Franciszka Michałowica", None, 223, "1698", "Agnieszka Michałowicowa", "Współpowódka", "Zelżona na Rynku w sporze z Kaczorkowicem.")
add_occ("Kaczorkowic", "Grzegorz", "Kraśnik", "Ślusarz / Mieszczanin", None, 223, "1698", "Sławny Grzegorz Kaczorkowic", "Pozwany o zniewagę na Rynku", "Twierdzi, że Michałowicowa pierwsza go lżyła.")
add_occ("Grymuza", "Jan", "Kraśnik", "Sławny (syn Jana Grymuzy)", None, 223, "1698", "Sławny Jan Grymuza syn Jana Grymuzy", "Powód o dobra po ojcu przeciw Guckiej", "Domaga się dóbr jako naturalny sukcesor.")
add_occ("Gucka", "[Wdowa]", "Kraśnik", "Sławetna (wdowa po Grzegorzu Guckim)", None, 223, "1698", "Sławetna Pani Gucka", "Pozwana o dobra przez Jana Grymuzę", "Prosi o dylację do środy na opiekunów.")

# Skan 224 (fol. 111v, 1698)
add_occ("Studzicki", "Sebastian", "Kraśnik", "Uczciwy", None, 224, "1698", "Sebastian Studzicki", "Strona kompromisu z 29 IV 1698 r.", "Ugoda o sukcesję po Wojciechu i Katarzynie Nogajach.")
add_occ("Studzicka", "Anna", "Kraśnik", "Żona Sebastiana Studzickiego", None, 224, "1698", "Anna Studzicka", "Strona kompromisu", "Współukłada się ze Stachowicami.")
add_occ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt kraśnicki", "Onupkiewicz [Kieniewicz?]", 224, "1698", "Pan Onupkiewicz Wójt Kraśnicki", "Wójt obecny przy kompromisie", "Obecny 29 IV 1698 r.")
add_occ("Solecki", "Stanisław", "Kraśnik", "Burmistrz kraśnicki", None, 224, "1698", "Sławetny P. Stanisław Solecki Burmistrz", "Rozjemca w kompromisie", "Asystuje przy ugodzie Studzickich i Stachowiców.")
add_occ("Jesurkiewicz", "Stanisław", "Kraśnik", "Dawny rajca kraśnicki", None, 224, "1698", "Sławetny Pan Stanisław Jesurkiewicz Rajca dawny", "Rozjemca w kompromisie", "Asystuje przy ugodzie.")
add_occ("Bożkowic", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 224, "1698", "Pan Wojciech Bożkowic Ławnik", "Ławnik przy kompromisie", "Asystuje przy ugodzie.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 224, "1698", "Pan Wawrzyniec Bielaszkowic Ławnik", "Ławnik przy kompromisie", "Asystuje przy ugodzie.")
add_occ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Szewc", None, 224, "1698", "Błażej Stachowic", "Strona kompromisu o zagony", "Ugoda pod zakładem 14 grzywien.")
add_occ("Stachowicowa", "Anna", "Kraśnik (Przedmieście)", "Żona Błażeja Stachowica", None, 224, "1698", "Anna Stachowicowa", "Strona kompromisu", "Współukłada się ze Studzickimi.")
add_occ("Nogaj", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin (zm.)", None, 224, "1698", "nieboszczyk Wojciech Nogaj", "Zmarły spadkodawca", "Po nim i Katarzynie toczył się spór o sukcesję.")

# Skan 225 (fol. 112r, 1698)
add_occ("Nowacki", "Benedykt", "Kraśnik", "Uczciwy", None, 225, "1698", "Uciwy Benedykt Nowacki", "Protestujący o pobicie w sklepie", "Oskarża Krystynę Carklinę o zadanie trzech krwawych ran.")
add_occ("Carklina", "Krystyna", "Kraśnik", "Uczciwa", "Carklina [?]", 225, "1698", "Uciwa Krystyna Carklina", "Pozwana o pobicie w sklepie", "Pozwana przez Benedykta Nowackiego.")
add_occ("Michalski", "Kazimierz", "Kraśnik", "Sławetny", None, 225, "1698", "Famatus Casimirus Michalski", "Składający diligentiam i protestację", "Sprawa przeciw Biegajczykowi.")
add_occ("Biegajczyk", "Stanisław", "Kraśnik", "Pozwany", "Biegaj [Biegajczyk?]", 225, "1698", "Biegaj", "Przedmiot diligentii Michalskiego", "Wzmiankowany 21 VII 1698 r.")
add_occ("Nowacki", "Tomasz", "Kraśnik", "Mieszczanin", None, 225, "1698", "H. Thomas Nowacki", "Protestujący przeciw Carklinowi", "Protestuje o zajście niedzielne.")
add_occ("Carklin", "[Mąż Krystyny]", "Kraśnik", "Uczciwy", "Carklin [?]", 225, "1698", "H. Carklin", "Pozwany z małżonką", "Pozwany przez Tomasza Nowackiego.")

# Zapis gen_data_j20_part9.json
with open('/home/ubuntu/workspace/Gen/gen_data_j20_part9.json', 'w', encoding='utf-8') as f:
    json.dump(gen_data, f, ensure_ascii=False, indent=2)

# Eksport CSV UTF-8-SIG, średnik, 9 kolumn
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j20_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
    writer.writerow(['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'])
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

print(f"Zapisano gen_data_j20_part9.json ({len(gen_data)} profili) oraz CSV.")
