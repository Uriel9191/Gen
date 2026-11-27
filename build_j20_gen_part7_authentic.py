# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part6.json', 'r', encoding='utf-8') as f:
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

# === PARTIA 7 (SKANY 151–175) ===

# Skan 151
add_occ("Rękuta", "Stanisław", "Kraśnik", "Mieszczanin", "Pękuta [?] / Rękuta [Pękuta?]", 151, "1698", "Stanisław Rękuta", "Protestujący w imieniu J. Łazińskiego", "Protestuje przeciw Janowi i Wojciechowi Żydkom o pobicie Jana Łacińskiego [Łazińskiego?].")
add_occ("Żydek", "Jan", "Kraśnik", "Pracowity / Czeladź", "Żydek [?]", 151, "1698", "Jan Żydek", "Pozwany o pobicie", "Oskarżony o pobicie Jana Łacińskiego [Łazińskiego?] na drodze.")
add_occ("Żydek", "Wojciech", "Kraśnik", "Pracowity / Czeladź", "Żydek [?]", 151, "1698", "Wojciech Żydek", "Pozwany o pobicie", "Współoskarżony z Janem Żydkiem o pobicie Jana Łazińskiego.")
add_occ("Łaziński", "Jan", "Kraśnik", "Młynarz (stoki)", "Łaciński [Łaziński?] / Łaziński [Łaciński?]", 151, "1698", "Jan Łaciński", "Poszkodowany (obdukcja ran)", "Pobity na drodze; rana cięta na prawej skroni i karku.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Ławnik przysięgły", None, 151, "1698", "Stefan Kwasowic", "Ławnik przy obdukcji", "Ogląda rany Jana Łazińskiego.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 151, "1698", "Wojciech Grzymałowski", "Ławnik przy obdukcji", "Ławnik przysięgły obecny przy obdukcji ran.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", "Bielaszkowic / Pisarzowic [Bielaszkowic?]", 151, "1698", "Wawrzyniec Bielaszkowic", "Ławnik przy obdukcji", "Ławnik przysięgły w Kraśniku.")
add_occ("Ichowic", "Szmul", "Kraśnik", "Żyd kraśnicki", "Ichowic [?]", 151, "1698", "Szmul Ichowic", "Protestujący o krowę", "Protestuje przeciw A. Pełkowi, J. Lisowi i J. Młynarczykowi o zajętą krowę i szkodę po 1 zł dziennie.")
add_occ("Pełk", "Andrzej", "Kraśnik", "Mieszczanin", "Pełk [?]", 151, "1698", "Andrzej Pełk", "Pozwany o krowę", "Pozwany przez Żyda Szmula Ichowica.")
add_occ("Lis", "Jakub", "Kraśnik", "Mieszczanin", None, 151, "1698", "Jakub Lis", "Pozwany o krowę", "Pozwany wspólnie z A. Pełkiem przez Szmula Ichowica.")
add_occ("Młynarczyk", "Jakub", "Kraśnik", "Mieszczanin", "Młynarczyk [?]", 151, "1698", "Jakub Młynarczyk", "Pozwany o krowę", "Pozwany przez Szmula Ichowica.")

# Skan 152
add_occ("Łaziński", "Jan", "Kraśnik", "Młynarz (stoki)", None, 152, "1698", "Joannes Łaziński", "Prezentujący rany (obdukcja)", "Dokończenie obdukcji ran przed ławnikami.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Ławnik przysięgły", None, 152, "1698", "Stefan Kwasowic", "Ławnik przy obdukcji", "Obecny przy obdukcji Jana Łazińskiego i Piotra.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 152, "1698", "Wojciech Grzymałowski", "Ławnik przy obdukcji", "Obecny przy obdukcji ran.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 152, "1698", "Wawrzyniec Bielaszkowic", "Ławnik przy obdukcji", "Obecny przy obdukcji ran.")
add_occ("[Nieznany]", "Piotr", "Kraśnik", "Uczciwy (poszkodowany)", "Piotr [?]", 152, "1698", "Uczciwy Piotr", "Prezentujący ranę na łopatce", "Prezentuje siną i spuchłą ranę na prawej łopatce.")
add_occ("Stabrawic", "Paweł", "Kraśnik", "Uczciwy", "Stabrawic [?]", 152, "1698", "Paweł Stabrawic", "Wnioskujący o wizję szkody", "Wnosi o wizję szkody w życie Katarzyny Nowackiej.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska (córka Ubalda Janaszkowica)", "Janaszkowicowa [Nowacka?]", 152, "1698", "Pani Katarzyna Nowacka", "Poszkodowana w szkodzie polnej", "W jej życie oszacowano 40 snopów szkody po 8 wołach.")
add_occ("[Parobek Nowackiej]", "Stasiek", "Kraśnik", "Parobek Katarzyny Nowackiej", "Stasik [?]", 152, "1698", "Stasiek parobek Nowackiej", "Świadek szkody w życie", "Świadczy o 8 wołach w życie Katarzyny Nowackiej.")
add_occ("Jędrzejowski", "Paweł", "Kraśnik", "Świadek", "Jędrzejowski [?]", 152, "1698", "Paweł Jędrzejowski", "Świadek szkody w życie", "Składa świadectwo o szkodzie 40 snopów żyta.")

# Skan 153
add_occ("Panek", "Jędrzej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 153, "1698", "Jędrzej Panek", "Protestujący o spasioną łąkę", "Protestuje przeciw Żydowi Feliksowi [?] o spasioną łąkę i zboże.")
add_occ("Feliks", "[Żyd]", "Kraśnik", "Żyd kraśnicki", "Feliks [?]", 153, "1698", "Niewierny Feliks", "Pozwany o szkodę i kontraprotestujący", "Pozwany przez Jędrzeja Panka; składa przerwany wpis protestacji.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", None, 153, "1698", "Paweł Słomkowski", "Świadek w sprawie o łąkę", "Wskazany jako świadek szkody w łące Jędrzeja Panka.")
add_occ("Janczewski", "Michał", "Kraśnik", "Uczciwy (poszkodowany)", "Janczewski [?]", 153, "1698", "Michał Janczewski", "Prezentujący rany", "Prezentuje rany na głowie, skroni i palcach prawej ręki.")
add_occ("Kamiński", "Stanisław", "Kraśnik", "Uczciwy (poszkodowany)", None, 153, "1698", "Stanisław Kamiński", "Prezentujący rany", "Współposzkodowany w bójce z Michałem Janczewskim.")
add_occ("[Woźny]", "Wojciech", "Kraśnik", "Woźny sądowy", "Wojciech [?]", 153, "1698", "Woźny Wojciech", "Woźny składający relację", "Składa relację z obdukcji ran.")
add_occ("Musik", "Jakub", "Kraśnik", "Mieszczanin", "Musik [?]", 153, "1698", "Jakub Musik", "Wskazany w relacji woźnego", "Wymieniony przy relacji woźnego z 31 V 1698.")
add_occ("Grzymek", "Wojciech", "Kraśnik", "Świadek", "Grzymek [?]", 153, "1698", "Wojciech Grzymek", "Świadek przy relacji", "Poświadcza relację o obdukcji ran.")

# Skan 154
add_occ("Starski", "Franciszek", "Kraśnik", "Woźny sądowy", "Starski [?]", 154, "1698", "Woźny Franciszek Starski", "Woźny doręczający pozew trybunalski", "Relacjonuje oddanie pozwu od S. Soleckiego i J. Barankowicza przeciw W. Wardędze.")
add_occ("Solecki", "Stanisław", "Kraśnik", "Rajca / Subdelegat urzędu radzieckiego i burmistrzowskiego", None, 154, "1698", "Stanisław Solecki", "Powód pozywający na Trybunał", "Pozywa Wojciecha Wardęgę na Trybunał wspólnie z Janem Barankowiczem.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 154, "1698", "Jan Barankowicz", "Powód pozywający na Trybunał", "Współpowód ze Stanisławem Soleckim przeciw Wojciechowi Wardędze.")
add_occ("Wardęga", "Wojciech", "Kraśnik", "Pracowity / Poddany", None, 154, "1698", "Wojciech Wardęga", "Pozwany przed Trybunał", "Pozwany przez Soleckiego i Barankowicza.")
add_occ("Panek", "Jędrzej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 154, "1698", "Andrzej Panek", "Protestujący o szkodę w życie", "Protestuje przeciw Żydowi Feliksowi [?] o szkodę w życie.")
add_occ("Feliks", "[Żyd]", "Kraśnik", "Żyd kraśnicki", "Feliks [?]", 154, "1698", "Niewierny Feliks", "Pozwany o szkodę w życie", "Szkoda wizjowana przez ławników Kwasowica i Bielaszkowica.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Ławnik przysięgły", None, 154, "1698", "Stefan Kwasowic", "Ławnik wizjujący szkodę", "Wizjuje szkodę w życie Andrzeja Panka.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 154, "1698", "Wawrzyniec Bielaszkowic", "Ławnik wizjujący szkodę", "Wizjuje szkodę w życie Andrzeja Panka.")
add_occ("Łyszkowic", "Kazimierz", "Kraśnik", "Mieszczanin", "Łyszkowic [?]", 154, "1698", "Kazimierz Łyszkowic", "Powód przeciw M. Paszkowi", "Spór o snopy żyta i P. Kłoskowica.")
add_occ("Paszek", "Marcin", "Kraśnik", "Mieszczanin", "Paszek [?]", 154, "1698", "Marcin Paszek", "Pozwany o snopy żyta", "Nakazane rozliczenie w ciągu tygodnia.")
add_occ("Kłoskowic", "[Pan]", "Kraśnik", "Sławetny", "Kłoskowic [?]", 154, "1698", "P. Kłoskowic", "Osoba wymieniona w sporze o żyto", "Wzmiankowany w sprawie Łyszkowica z Paszkiem.")

# Skan 155
add_occ("Proskowic", "Jan", "Kraśnik", "Mieszczanin", "Proskowic [?]", 155, "1698", "Joannes Proskowic", "Skazany zaocznie (contumacia)", "Skazany zaocznie z instancji Wojciecha Kłopota.")
add_occ("Kłopot", "Wojciech", "Kraśnik", "Mieszczanin", None, 155, "1698", "Albertus Kłopot", "Powód uzyskujący kontumację", "Uzyskuje kontumację przeciw Janowi Proskowicowi.")
add_occ("[Parobek Nowackiej]", "Stasiek", "Kraśnik", "Parobek", "Stasik [?]", 155, "1698", "Stasik", "Skazany zaocznie (contumacia)", "Skazany zaocznie z instancji Jana Murowskiego.")
add_occ("Murowski", "Jan", "Kraśnik", "Mieszczanin", "Murowski [?]", 155, "1698", "Joannes Murowski", "Powód uzyskujący kontumację", "Uzyskuje kontumację przeciw Stasikowi.")
add_occ("Solecki", "Stanisław", "Kraśnik", "Rajca / Subdelegat", None, 155, "1698", "Stanislaus Solecki", "Manifestujący przeciw W. Wardędze", "Współautor manifestacji przeciw Wojciechowi Wardędze.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 155, "1698", "Joannes Barankowicz", "Manifestujący przeciw W. Wardędze", "Współautor manifestacji przeciw Wojciechowi Wardędze.")
add_occ("Wardęga", "Wojciech", "Kraśnik", "Pracowity / Poddany", None, 155, "1698", "Albertus Wardęga", "Strona pozwana w manifestacji", "Przedmiot manifestacji Soleckiego i Barankowicza.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska (córka Ubalda Janaszkowica)", None, 155, "1698", "Katarzyna Nowacka", "Egzekwująca dekret Trybunału Zamojskiego i protestująca", "Domaga się wołów i krowy po ojcu Ubaldzie Janaszkowiczu; protestuje przeciw W. Grzymałowskiemu.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 155, "1698", "Wojciech Grzymałowski", "Pozwany o inwentarz po wójcie", "Pozwany przez Katarzynę Nowacką o woły i krowę po zmarłym wójcie Janaszkowiczu.")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki (zm.)", None, 155, "1698", "Ubald Janaszkowicz", "Zmarły wójt (spadkodawca)", "Wzmiankowany jako zmarły ojciec Katarzyny Nowackiej.")

# Skan 156
add_occ("Panek", "Jędrzej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 156, "1698", "Jędrzej Panek", "Składający skargę (wpis przerwany)", "Zapis z 4 VI 1698 r. urwany na karcie.")

# Skan 157
add_occ("Moszkowicz", "Berek", "Kraśnik", "Żyd kraśnicki", None, 157, "1698", "Niewierny Berek Moszkowicz", "Powód o woły i 4 grzywny", "Sprawa przeciw Pawłowi Kłopotowi.")
add_occ("Kłopot", "Paweł", "Kraśnik", "Mieszczanin", None, 157, "1698", "Paweł Kłopot", "Pozwany o woły", "Zasądzone 2 grzywny dla burmistrza w sporze z Berkiem Moszkowiczem.")
add_occ("Kołkowic", "Tomasz", "Kraśnik", "Mieszczanin", "Kołkowic [?]", 157, "1698", "Tomasz Kołkowic", "Powód przeciw S. Sowińskiemu", "Strona w sprawie z 16 VI 1698 r.")
add_occ("Sowiński", "Sebastian", "Kraśnik", "Mieszczanin", "Sowiński [?]", 157, "1698", "Sebastian Sowiński", "Pozwany", "Pozwany przez Tomasza Kołkowica.")
add_occ("Wilk", "Adam", "Kraśnik", "Mieszczanin", None, 157, "1698", "Adamus Wilk", "Skazany zaocznie (contumacia)", "Skazany zaocznie z instancji Macieja Kłopotka.")
add_occ("Kłopotek", "Maciej", "Kraśnik", "Mieszczanin", "Kłopotek [?]", 157, "1698", "Mathias Kłopotek", "Powód uzyskujący kontumację", "Uzyskuje kontumację przeciw Adamowi Wilkowi.")
add_occ("Trawiński", "Tomasz", "Kraśnik", "Mieszczanin", "Trawiński [?]", 157, "1698", "Thomas Trawiński", "Skazany zaocznie (contumacia)", "Skazany zaocznie z instancji Bartłomieja Piaseckiego.")
add_occ("Piasecki", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 157, "1698", "Bartholomeus Piasecki", "Powód uzyskujący kontumację", "Uzyskuje kontumację przeciw Tomaszowi Trawińskiemu.")

# Skan 158
add_occ("Moszkowicz", "Berek", "Kraśnik", "Żyd kraśnicki", None, 158, "1698 (wzm. 1694)", "Berek Moszkowicz", "Zgłaszający intromisję i manifestujący", "Wpisuje intromisję Kobierskiej z 1694 r. oraz manifestuje przeciw Pawłowi Kłopotowi o konie z wozu.")
add_occ("Kobierska", "Szymonowa", "Kraśnik", "Wdowa", None, 158, "1694", "Wdowa Szymonowa Kobierska", "Strona intromisji z 1694 r.", "Wzmiankowana w intromisji z 15 I 1694 r.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska", None, 158, "1698", "Catharina Nowacka", "Skazana zaocznie (contumacia)", "Kontumacja z instancji Pawła Słomkowskiego.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", None, 158, "1698", "Paulus Słomkowski", "Powód uzyskujący kontumację", "Uzyskuje kontumację przeciw Katarzynie Nowackiej.")
add_occ("Kłopot", "Paweł", "Kraśnik", "Mieszczanin", None, 158, "1698", "Paulus Kłopot", "Pozwany o konie z wozu", "Przedmiot manifestacji Berka Moszkowicza.")
add_occ("Łopatka", "Sebastian", "Kraśnik", "Mieszczanin", "Łopatka [?]", 158, "1698", "Sebastian Łopatka", "Manifestujący przeciw K. Mrozowskiemu", "Składa manifestację w sprawie z Karolem Mrozowskim.")
add_occ("Mrozowski", "Karol", "Kraśnik", "Mieszczanin", "Mroziński [Mrozowski?]", 158, "1698", "Karol Mroziński", "Strona w manifestacji Łopatki", "Wzmiankowany jako Karol Mroziński [Mrozowski?].")

# Skan 159
add_occ("Pietrzak", "Tomasz", "Kraśnik", "Mieszczanin", "Pietrzak [?]", 159, "1698", "Thomas Pietrzak", "Skazany na 3 grzywny i 3 dni wieży", "Skazany zaocznie z instancji Bartłomieja Piaseckiego.")
add_occ("Piasecki", "Bartłomiej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 159, "1698", "Bartholomeus Piasecki", "Powód uzyskujący kontumację", "Uzyskuje kontumację przeciw Tomaszowi Pietrzakowi.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 159, "1698", "Fam. Joannes Majowski Consul", "Pozwany w protestacji", "Przedmiot protestacji z instancji Stefana Zasadzowica.")
add_occ("Zasadzowic", "Stefan", "Kraśnik", "Mieszczanin", "Zasadzowic [?]", 159, "1698", "Stephanus Zasadzowic", "Protestujący przeciw rajcy Majowskiemu", "Składa protestację z 19 VI 1698 r.")
add_occ("Olchowski", "Szymon", "Kraśnik (Piaski)", "Przedmieszczanin z Piasków", "Olchowski [?]", 159, "1695", "Szymon Olchowski", "Protestujący przeciw Żydowi Ickowi", "Wpis z 23 VI 1695 r. o znieważenie i próbę pobicia córki.")
add_occ("Icek", "[syn Biernasia]", "Kraśnik", "Żyd kraśnicki", "Icek [?]", 159, "1695", "Niewierny Icek", "Pozwany o zniewagę", "Syn Biernasia; oskarżony przez Szymona Olchowskiego w 1695 r.")
add_occ("Biernas", "[Żyd]", "Kraśnik", "Żyd kraśnicki (ojciec Icka)", "Biernas [?]", 159, "1695", "Biernas", "Ojciec pozwanego Icka", "Wzmiankowany jako ojciec Icka.")

# Skan 160
add_occ("Solecki", "Stanisław", "Kraśnik", "Rajca / Mieszczanin (cechowy)", None, 160, "1698", "P. Stanisław Solecki", "Poszkodowany (obdukcja ran)", "Rany na głowie, podbite oko, rany na obu rękach i pocięta suknia oraz czapka.")
add_occ("Borucki", "Matyjasz", "Kraśnik", "Mieszczanin (tegoż rzemiosła)", "Borucki [?]", 160, "1698", "Matyasz Borucki", "Wnioskujący o obdukcję ran", "Współproszący o obdukcję ran wraz ze Stanisławem Soleckim.")
add_occ("Dąbrowski", "Paweł", "Kraśnik", "Uczciwy (poszkodowany)", None, 160, "1698", "Paweł Dąbrowski", "Poszkodowany (obdukcja ran)", "Rana cięta na ciemieniu i rana sina na prawej ręce.")
add_occ("Złotnicki", "Jakub", "Kraśnik", "Uczciwy", "Złotnicki [?] / Szczepan Złotnicki [?]", 160, "1698", "Jakub Złotnicki", "Obwiniony o zadanie ran", "Wskazany jako sprawca pobicia Soleckiego (nadpisanie: Szczepan Złotnicki).")
add_occ("Bożkowic", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 160, "1698", "PP. Wojciech Bożkowic", "Ławnik delegowany do obdukcji", "Ogląda rany Stanisława Soleckiego i Pawła Dąbrowskiego.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", "Pisarzowic [Bielaszkowic?]", 160, "1698", "Wawrzyniec Pisarzowic", "Ławnik delegowany do obdukcji", "Ogląda rany przy cyruliku Mojżeszu Abramowicu.")
add_occ("Wolanowski", "[Ławnik]", "Kraśnik", "Ławnik / Urzędnik", "Wolanowski [?]", 160, "1698", "Wolanowski", "Członek komisji obdukcyjnej", "Asystuje przy oględzinach ran.")
add_occ("Abramowic", "Mojżesz", "Kraśnik", "Cyrulik miejski", None, 160, "1698", "Mojżesz Abramowic cyrulik", "Cyrulik dokonujący obdukcji", "Bada rany Soleckiego i Dąbrowskiego.")
add_occ("Dutkowic", "Krzysztof", "Kraśnik", "Mieszczanin", "Dutkowic [?]", 160, "1698", "Krzysztof Dutkowic", "Obwiniony o udział w napaści", "Obwiniany przez poszkodowanych.")
add_occ("Lipczyński", "[Mieszczanin]", "Kraśnik", "Mieszczanin", "Lipczyński [?]", 160, "1698", "Lipczyński", "Obwiniony o udział w napaści", "Obwiniany wspólnie z Dutkowicem.")
add_occ("Wysocki", "[Pan]", "Kraśnik", "Sławetny", None, 160, "1698", "P. Wysocki", "Strona zapowiadająca dochodzenie prawa", "Wymieniony na końcu obdukcji.")
add_occ("Bosacki", "Walenty", "Kraśnik", "Mieszczanin", "Bosacki [Bożkowic?]", 160, "1698", "Walenty Bosacki", "Strona dochodząca prawa", "Wymieniony obok P. Wysockiego.")

# Skan 161
add_occ("Wysocka", "Katarzyna", "Kraśnik", "Sławna Pani (żona Aleksandra Wysockiego)", None, 161, "1698", "Sławna Pani Katarzyna Wysocka", "Protestująca o zniesławienie", "Protestuje przeciw Zofii Pyrzkownej i Zofii Piaseckiej o pomówienie męża o złodziejstwo.")
add_occ("Pyrzkowna", "Zofia", "Kraśnik", "Mieszczanka", "Pyrzkowna [?]", 161, "1698", "Zofia Pyrzkowna", "Pozwana o zniesławienie", "Pozwana przez Katarzynę Wysocką.")
add_occ("Piasecka", "Zofia", "Kraśnik (Przedmieście)", "Przedmieszczanka", None, 161, "1698", "Zofia Piasecka", "Pozwana o zniesławienie", "Współpozwana z Zofią Pyrzkowną.")
add_occ("Wysocki", "Aleksander", "Kraśnik", "Mąż Katarzyny Wysockiej", None, 161, "1698", "Alexander Wysocki", "Pomówiony o złodziejstwo", "Mąż Katarzyny Wysockiej.")
add_occ("Tudorek", "Anna", "Kraśnik (Piaski)", "Uczciwa (córka Stanisława Tudorka)", "Tudorkowa / Tudorek [?]", 161, "1698", "Uciwa Anna Tudorkowa", "Powódka w sprawie roli Tudorkowskiej", "Przeprowadza inkwizycję o kwaterę roli na Piaskach.")
add_occ("Leś", "Matyjasz", "Kraśnik (Piaski)", "Świadek / Sąsiad roli", "Leś [?]", 161, "1698", "Uczciwy Matyasz Leś", "Sąsiad roli i 1. świadek", "Zeznaje o bójce w domu i przy płocie.")
add_occ("Kuczyński", "[Mieszczanin]", "Kraśnik", "Mieszczanin", "Kuczyński [?]", 161, "1698", "Kuczyński", "Uczestnik bójki (w zeznaniu)", "Wymieniony w zeznaniu Matyjasza Lesia.")

# Skan 162
add_occ("Tudorek", "Anna", "Kraśnik (Piaski)", "Uczciwa (córka Stanisława Tudorka)", None, 162, "1698", "Uciwa Anna córka niegdy Stanisława Tudorka", "Powódka w dekrecie o rolę", "Wygrywa sprawę o kwaterę roli Tudorkowskiej; ma kupić 2 pary trzewików.")
add_occ("Tudorek", "Stanisław", "Kraśnik (Piaski)", "Ojciec Anny Tudorkowej (zm.)", "Tudorek [?]", 162, "1698", "niegdy Stanisław Tudorek", "Zmarły ojciec powódki", "Wzmiankowany w dekrecie z 26 VI 1698 r.")
add_occ("Pastuszka Łołkowic", "Stanisław", "Kraśnik (Piaski)", "Ojciec męża Anny Tudorkowej", "Łołkowic [?]", 162, "1698", "Stanisław Pastuszka Łołkowic", "Asystujący synowej w sądzie", "Obecny jako teść powódki.")
add_occ("Gąskowicowa", "Jadwiga", "Kraśnik (Piaski)", "Uczciwa", "Gąskowicowa [?]", 162, "1698", "Uciwa Jadwiga Gąskowicowa", "Pozwana o rolę i poswarki", "Zakazano jej roszczeń do roli pod karą 7 grzywien i 3 dni więzienia.")
add_occ("Brząs", "Sebastian", "Kraśnik", "Uczciwy", "Brząs [?]", 162, "1698", "Sebastianus Brząs", "Strona powołująca świadków", "Sprawa o wóz z podwodą do Zamościa.")
add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 162, "1698", "Uczciwy Rymarczyk", "1. świadek (woźnica podwody)", "Zeznaje o podróży podwodnej pod P. Deputata do Zamościa i pozostawieniu wozu.")

# Skan 163
add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 163, "1698", "Rymarczyk", "Świadek poszukujący wozu", "Szuka zaginionego wozu ze swoim synem i parobkiem.")
add_occ("Olchowski", "Szymon", "Kraśnik (Piaski)", "Przedmieszczanin z Piasków (Kuśmierz alias Olchowski)", None, 163, "1698", "Szymon Olchowski / Kuśmierz alias Olchowski", "Posiadacz stodoły z wozem", "W jego stodole zamknięto wóz; nocą odesłał wóz przez dziecko.")
add_occ("Brząs", "Sebastian", "Kraśnik", "Uczciwy", "Brząs [?]", 163, "1698", "Brząs", "Osoba wskazująca miejsce wozu", "Wskazuje wóz zamknięty u Szymona Olchowskiego.")
add_occ("Kozakowa", "Katarzyna", "Kraśnik", "Uczciwa (żona Kozaka)", None, 163, "1698", "Uciwa Katarzyna Kozakowa", "2. świadek", "Nadybała wóz przykryty słomą idąc do koni.")
add_occ("Kozakowicz", "[Syn Kozaka]", "Kraśnik", "Świadek (syn Kozakowej)", None, 163, "1698", "Syn Kozak", "3. świadek", "Zaprowadził wóz do stodoły Olchowskiego.")

# Skan 164
add_occ("Kozakowicz", "[Syn Kozaka]", "Kraśnik", "Świadek", None, 164, "1698", "Syn Kozak", "3. świadek (dokończenie)", "Kończy zeznanie o wozie w stodole Olchowskiego.")
add_occ("Olchowski", "Szymon", "Kraśnik (Piaski)", "Przedmieszczanin (wyjeżdżający na Wisłę)", None, 164, "1698", "Szymon Olchowski", "Powód i protestujący", "Otrzymuje dylację na Wisłę; protestuje przeciw Marcinowi Rymarczykowi o rzepę i odejście od sądu.")
add_occ("Brząs", "Sebastian", "Kraśnik", "Uczciwy", "Brząs [?]", 164, "1698", "Sebastian Brząz", "Pozwany (dylacja)", "Sprawa odroczona do piątku.")
add_occ("Boguta", "Jakub", "Kraśnik", "Uczciwy", None, 164, "1698", "Jacobus Boguta", "Składający diligentiam", "Wpis diligentia w aktach.")
add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 164, "1698", "Marcin Rymarczyk", "Pozwany w protestacji Olchowskiego", "Oskarżony o odejście od sądu i pomówienie o rzepę.")
add_occ("Stary Kmieć", "Tomasz", "Kraśnik", "Świadek / Pasterz", None, 164, "1698", "Thomas Stary Kmieć", "1. świadek ze strony S. Olchowskiego", "Zeznaje o znalezieniu wozu przykrytego słomą z Kozakową.")
add_occ("Kozakowa", "Katarzyna", "Kraśnik", "Uczciwa", None, 164, "1698", "Kozakowa", "Wzmiankowana w zeznaniu świadka", "Odradziła podział wozu i zaleciła odwiezienie go do domu.")

# Skan 165
add_occ("Taborówna", "Jadwiga", "Kraśnik", "Płócienniczka (żona tokarza)", None, 165, "1698", "Uciwa Jadwiga Taborówna Płócienniczka żona Tokarza", "Strona ugody z pasierbami", "Kwituje pasierbów z pretensji przed sądem wójtowskim.")
add_occ("[Pasierbica Taborówny]", "Małgorzata", "Kraśnik", "Pasierbica Jadwigi Taborówny", None, 165, "1698", "Małgorzata pasierbica", "Strona ugody", "Współukładająca się z macochą.")
add_occ("[Pasierb Taborówny]", "Jędrzej", "Kraśnik", "Pasierb Jadwigi Taborówny", None, 165, "1698", "Jędrzej pasierb", "Strona ugody", "Współukładający się z macochą.")
add_occ("[Syn Taborówny]", "Jan", "Kraśnik", "Mieszczanin / Syn", None, 165, "1698", "Jan", "Uczestnik ugody", "Wymieniony przy ugodzie z 26 IX 1698 r.")
add_occ("[Syn Taborówny]", "Piotr", "Kraśnik", "Mieszczanin / Syn", "Piotr [?]", 165, "1698", "Piotr", "Uczestnik ugody", "Wymieniony obok Jana przy ugodzie.")

# Skan 166
add_occ("Rutkowic", "Stanisław", "Kraśnik", "Świadek", "Rutkowic [?]", 166, "1698", "Stanisław Rutkowic", "2. świadek ze strony S. Olchowskiego", "Potwierdza zeznanie o odebraniu wozu.")
add_occ("Ruchowski", "Jan", "Kraśnik", "Świadek", "Ruchowski [?]", 166, "1698", "Jan Ruchowski", "3. świadek ze strony S. Olchowskiego", "Potwierdza zdarzenie sprzed czterech lat.")
add_occ("Arel", "[Żyd]", "Kraśnik", "Żyd kraśnicki", "Aron [Arel?]", 166, "1698", "Infidelis Arel", "Powód przeciw J. Macalowi", "Spór o szynk; dylacja do poniedziałku.")
add_occ("Macal", "Józef", "Kraśnik", "Mieszczanin (chrześcijanin)", None, 166, "1698", "Josephus Macal Christianus", "Pozwany przez Żyda Arela", "Dylacja w sprawie o szynk.")
add_occ("Olchowski", "Szymon", "Kraśnik (Piaski)", "Przedmieszczanin", None, 166, "1698", "Simon Olchowski", "Powód przeciw Rymarczykowi i Brząsowi", "Sprawa odesłana do wójta i urzędu.")
add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 166, "1698", "Martinus Rymarczyk", "Pozwany", "Sprawa odesłana do wójta.")
add_occ("Brząs", "Sebastian", "Kraśnik", "Uczciwy", "Brząs [?]", 166, "1698", "Sebastianus Brząz", "Pozwany", "Sprawa odesłana do wójta.")

# Skan 167
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Ławnik przysięgły", None, 167, "1698", "PP. Paweł Słomkowski", "Urzędnik przy ugodzie", "Asystuje przy ugodzie z vadium 50 grzywien.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Ławnik przysięgły", None, 167, "1698", "Stephan Kwasowic", "Ławnik przy ugodzie", "Asystuje przy zapisie pojednawczym.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 167, "1698", "Wojciech Grzymałowski", "Ławnik przy ugodzie", "Asystuje przy zapisie pojednawczym.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 167, "1698", "Wawrzyniec Bielaszkowic", "Ławnik przy ugodzie", "Asystuje przy zapisie pojednawczym.")
add_occ("Olchowski", "Szymon", "Kraśnik (Piaski)", "Przedmieszczanin", None, 167, "1698", "Szymon Olchowski", "Strona ugody (przeprosiny i vadium)", "Zabezpieczony vadium 50 grzywien przed dalszymi kalumniami.")

# Skan 168
add_occ("Mrozowski", "Karol", "Kraśnik", "Mieszczanin kraśnicki", None, 168, "1698", "Sławetny Karol Mrozowski", "Składający sumę z dekretu i poszkodowany w tumulcie", "Składa 200/300 zł i grzywny; skarży na nocny tumult w swoim domu.")
add_occ("Solecki", "Stanisław", "Kraśnik", "Rajca / Subdelegat", None, 168, "1698", "P. Stanisław Solecki", "Wierzyciel odmawiający odbioru sumy", "Nie przyjmuje sumy od Karola Mrozowskiego i wychodzi.")
add_occ("Potocki", "Adam", "Kraśnik", "Prokonsul / Rajca kraśnicki", "Potokowicz", 168, "1698", "Adam Potokowic", "Strona dekretu radziecko-wójtowskiego", "Wymieniony obok Stanisława Soleckiego.")
add_occ("[Parobek z Izdebna]", "Stasio", "Izdebno [?]", "Parobek Pani Mundajnej", None, 168, "1698", "Uczciwy Stasio parobek Pani Mundajny", "Uczestnik tumultu w domu Mrozowskiego", "Sprawa o nocny hałas i bójkę.")
add_occ("Mundajna", "[Pani]", "Izdebno [?]", "Szlachcianka / Posesorka", "Mundajna [?]", 168, "1698", "Pani Mundajna z Izdebna", "Pani parobka Stasia", "Wzmiankowana jako chlebodawczyni Stasia.")
add_occ("[Czeladnik z Podgórza]", "Matyjasz", "Kraśnik (Podgórze)", "Uczestnik tumultu", None, 168, "1698", "Matyjasz", "Uczestnik bójki u Mrozowskiego", "Zastany w domu Karola Mrozowskiego podczas tumultu.")
add_occ("[Czeladnik z Podgórza]", "Kazimierz", "Kraśnik (Podgórze)", "Uczestnik tumultu", None, 168, "1698", "Kazimierz", "Uczestnik bójki u Mrozowskiego", "Uczestniczy w zajściu z Matyjaszem.")
add_occ("Pankowa", "[Pani]", "Kraśnik", "Mieszczanka", "Panek [?]", 168, "1698", "P. Pankowa", "Uczestniczka tumultu", "Wzmiankowana przy wyjściu dziewki w tumulcie.")

# Skan 169
add_occ("Mrozowski", "Karol", "Kraśnik", "Mieszczanin kraśnicki", None, 169, "1698", "Sławetny P. Karol Mrozowski", "Gospodarz pobity w tumulcie", "Obudzony ze snu i pobity kijami w swojej izbie.")
add_occ("[Parobek z Izdebna]", "Stasio", "Izdebno [?]", "Parobek", None, 169, "1698", "Stasio", "Uczestnik tumultu", "Wypędzony na dwór przez Mrozowskiego.")
add_occ("Kempionka", "Anna", "Kraśnik", "Żona Matyjasza Piotrowczyka (zm.)", "Kempionka [?]", 169, "1698", "Anna Kempionka", "Zmarła spadkodawczyni (regestr rzeczy)", "Zostawia klacz ze źrebięciem dla syna Babiarczyka i dwie krowy dla młodszych dzieci.")
add_occ("Piotrowczyk", "Matyjasz", "Kraśnik", "Mieszczanin (wdowiec po Annie Kempionce)", None, 169, "1698", "Matyjasz Piotrowczyk", "Mąż zmarłej Anny Kempionki", "Współmałżonek wymieniony w rejestrze spadkowym z 22 IV 1698 r.")
add_occ("Babiarczyk", "[Syn Kempionki]", "Kraśnik", "Syn Anny Kempionki", "Babiarczyk [?]", 169, "1698", "Babiarczyk", "Spadkobierca klaczy ze źrebięciem", "Otrzymuje klacz z zapisu matki.")

# Skan 170
add_occ("Koczorowski", "Grzegorz", "Kraśnik", "Uczciwy", "Koczorowski [?]", 170, "1698", "Grzegorz Koczorowski", "Powód o kulbakę", "Domaga się zwrotu kulbaki od Bartka Białka.")
add_occ("Białek", "Bartek", "Kraśnik", "Uczciwy", "Białek [?]", 170, "1698", "Bartek Białek", "Pozwany o kulbakę", "Skazany na zapłatę za kulbakę i szkody.")
add_occ("Opaskiewicz", "[Pan]", "Kraśnik", "Sławetny", "Opaskiewicz [?]", 170, "1698", "Sławetny P. Opaskiewicz", "Powód o kulbakę", "Sprawa odroczona do poniedziałku.")
add_occ("Chuctry", "A.", "Kraśnik", "Pozwany", "Huctry [?] / Chuctry [Huctry?]", 170, "1698", "A. Chuctry", "Pozwany o kulbakę", "Pozwany przez P. Opaskiewicza.")

# Skan 171
add_occ("Sitarczyk", "Franciszek", "Kraśnik", "Uczciwy (posłaniec / woźny)", "Sitarczyk [?]", 171, "1698", "Uciwy Franciszek Sitarczyk", "Doręczyciel pozwu przez brewe", "Doręcza pozew rajcom kraśnickim od Katarzyny Nowackiej.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska", None, 171, "1698", "Sławetna Pani Katarzyna Nowacka Landwójtowa Urzędowska", "Strona pozywająca rajców", "Wysyła pozew przez brewe.")
add_occ("Łaziński", "Jan", "Kraśnik", "Młynarz (stoki)", None, 171, "1698", "Uciwy Jan Łaziński młynarz stoki", "Protestujący i prezentujący rany", "Pobity na gospodzie przez Jana i Wojciecha Żydków; rana na głowie do kości i pręgi od kijów.")
add_occ("Żydek", "Jan", "Kraśnik", "Pracowity / Czeladź", "Żydek [?]", 171, "1698", "Jan Żydek", "Pozwany o pobicie na gospodzie", "Oskarżony przez młynarza Jana Łazińskiego.")
add_occ("Żydek", "Wojciech", "Kraśnik", "Pracowity / Czeladź", "Żydek [?]", 171, "1698", "Wojciech Żydek", "Pozwany o pobicie na gospodzie", "Oskarżony wspólnie z Janem Żydkiem.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Ławnik przysięgły", None, 171, "1698", "Stephan Kwasowic", "Ławnik przy obdukcji", "Obecny przy obdukcji ran Jana Łazińskiego.")
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 171, "1698", "Wojciech Grzymałowski", "Ławnik przy obdukcji", "Obecny przy obdukcji ran.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 171, "1698", "Wawrzyniec Bielaszkowic", "Ławnik przy obdukcji", "Obecny przy obdukcji ran.")

# Skan 172
add_occ("Kieniewicz", "Jan Onufry", "Kraśnik", "Adwokat ordynaryjny kraśnicki", "Onupkiewicz [?] / Kieniewicz [Onupkiewicz?]", 172, "1698", "Famatus Joannes Onuphrius Kieniewicz Advocatus Ordinarius", "Pełnomocnik powoda", "Występuje przed sądem złożonym.")
add_occ("Mrozowski", "Adam Karol", "Kraśnik", "Magister sztuk wyzwolonych (malarstwa) / Pełnomocnik", None, 172, "1698", "Adamus Carolus Mrozowski artis liberalis Pictorea Magister", "Pełnomocnik pozwanego", "Reprezentuje pozwaną stronę w procesie o kalkulację.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 172, "1698", "Famatus Joannes Majowski Consul Crasnicensis", "Gospodarz komisji ugodowej", "W jego domu wyznaczono komplanację i kalkulację.")
add_occ("Nowacki", "Wojciech", "Kraśnik / Urzędów", "Landwójt / Wicewójt urzędowski", None, 172, "1698", "Famatus Albertus Nowacki", "Pozwany (mąż Katarzyny Nowackiej)", "Strona sporu o rachunki pod karą 14 grzywien.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska", None, 172, "1698", "Catharina Nowacka", "Pozwana o rachunki po wójcie", "Współpozwana z mężem Wojciechem Nowackim.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", None, 172, "1698", "Sławetny Pan Paweł Słomkowski Podwójci Kraśnicki", "Powód manifestujący przeciw Nowackim", "Składa protestację 13 XI 1698 r.")

# Skan 173
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", None, 173, "1698", "Paulus Słomkowski Viceadvocatus Crasnicensis", "Powód i mocodawca pasierba", "Manifestuje o niestawienie się Nowackiej; 24 XI 1698 r. ustanawia pasierba Wojciecha pełnomocnikiem przed Trybunałem Zamojskim.")
add_occ("Nowacki", "Wojciech", "Kraśnik / Urzędów", "Landwójt / Wicewójt urzędowski", None, 173, "1698", "Wojciech Nowacki", "Pozwany jako posesor dóbr po Janaszkowiczu", "Przedmiot manifestacji z 13 XI 1698 r.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska", None, 173, "1698", "Pani Nowacka", "Pozwana nieobecna na kalkulacji", "Nie przyszła na termin kalkulacji aż do wieczora.")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki (zm.)", None, 173, "1698", "Sławetny Pan Ubald Janaszkowic Wójt Kraśnicki", "Zmarły spadkodawca", "Po jego śmierci toczy się spór o długi i dobra.")
add_occ("Solecki", "Stanisław", "Kraśnik", "Subdelegat urzędu radzieckiego i burmistrzowskiego", None, 173, "1698", "Stanisław Solecki Subdelegat", "Przyjaciel strony powoda na kalkulacji", "Sprowadzony przez Pawła Słomkowskiego.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 173, "1698", "Jan Barankowic", "Przyjaciel strony powoda na kalkulacji", "Obecny przy próbie kalkulacji.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Ławnik przysięgły", None, 173, "1698", "Stephan Kwasowic Ławnik", "Ławnik przy próbie kalkulacji", "Obecny z ramienia sądu i stron.")
add_occ("Słomkowski", "Wojciech", "Kraśnik", "Pasierb Pawła Słomkowskiego / Pełnomocnik", None, 173, "1698", "Honoratus Albertus Słomkowski filiaster", "Pełnomocnik przed Trybunałem Zamojskim", "Ustanowiony 24 XI 1698 r. w apelacji przeciw Nowackim.")

# Skan 174
add_occ("Potocki", "Adam", "Kraśnik", "Prokonsul kraśnicki", "Potokowicz", 174, "1698", "Famatus Adamus Potokowicz Proconsul", "Prokonsul w sądzie złożonym", "Przewodniczy sądowi złożonemu 21 XI 1698 r.")
add_occ("Solecki", "Stanisław", "Kraśnik", "Subdelegat urzędu radzieckiego", None, 174, "1698", "Stanislaus Solecki Subdelegatus", "Subdelegat w sądzie złożonym", "Zasiada w sądzie złożonym.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 174, "1698", "Joannes Barankowicz Consul", "Rajca w sądzie złożonym", "Zasiada w sądzie złożonym.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 174, "1698", "Joannes Majowski Consul", "Rajca w sądzie złożonym", "Zasiada w sądzie złożonym.")
add_occ("Bożkowic", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 174, "1698", "Albertus Bożkowic Scabinus Juratus", "Ławnik w sądzie złożonym", "Zasiada w sądzie złożonym.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Ławnik przysięgły", None, 174, "1698", "Stephanus Kwasowic Scabinus Juratus", "Ławnik w sądzie złożonym", "Zasiada w sądzie złożonym.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 174, "1698", "Laurentius Bielaszkowic Scabinus Juratus", "Ławnik w sądzie złożonym", "Zasiada w sądzie złożonym.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 174, "1698", "Famatus Paulus Słomkowski Viceadvocatus Crasnicensis", "Powód o 802 złp 15 gr", "Domaga się sumy 802 złp 15 gr z dóbr po Ubaldzie Janaszkowiczu.")
add_occ("Słomkowski", "Wojciech", "Kraśnik", "Pasierb Pawła Słomkowskiego / Pełnomocnik", None, 174, "1698", "Albertus Słomkowski", "Pełnomocnik (dokończenie wpisu)", "Dokończenie pełnomocnictwa z 24 XI 1698 r.")
add_occ("Nowacki", "Wojciech", "Kraśnik / Urzędów", "Wicewójt urzędowski", None, 174, "1698", "Albertus Nowacki Viceadvocatus Urzędoviensis", "Pozwany o 802 złp 15 gr", "Współpozwany z żoną Katarzyną.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska (córka Ubalda Janaszkowica)", "Janaszkowicowa [Nowacka?]", 174, "1698", "Catharina Janaszkowicowa", "Pozwana o 802 złp 15 gr", "Występuje pod nazwiskiem panieńskim/rodowym Janaszkowicowa.")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki (zm.)", None, 174, "1698", "olim spectabilis Ubaldus Janaszkowicz", "Zmarły spadkodawca", "Wzmiankowany jako poprzedni posiadacz dóbr.")

# Skan 175
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 175, "1698", "Actor (Paulus Słomkowski)", "Powód apelujący do Trybunału Zamojskiego", "Zasądzono mu 4 złp za gwoździe i 1 złp 23 gr za kremat, lecz skazano go na 15 grzywien i 15 dni wieży; apeluje do Zamościa i protestuje o kalumnię.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska", None, 175, "1698", "Catharina Nowacka", "Pozwana uwolniona od grzywny 14 mk", "Zwolniona z kary 14 grzywien; oskarżona o zniewagę słowną w sądzie.")
add_occ("Nowacki", "Wojciech", "Kraśnik / Urzędów", "Wicewójt urzędowski", None, 175, "1698", "Pars Citata", "Współpozwany w dekrecie", "Strona dekretu z 21 XI 1698 r.")

# Zapis gen_data_j20_part7.json
with open('/home/ubuntu/workspace/Gen/gen_data_j20_part7.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j20_part7.json ({len(gen_data)} profili) oraz CSV.")
