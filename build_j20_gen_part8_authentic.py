# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part7.json', 'r', encoding='utf-8') as f:
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

# === PARTIA 8 (SKANY 176–200) ===

# Skan 176
add_occ("Więckowicz", "Jan", "Kraśnik", "Mieszczanin", "Wierckowicz [?] / Więckowicz [Wierckowicz?]", 176, "1698", "Joannes Więckowicz", "Powód uzyskujący kontumację", "Uzyskuje kontumację z nakazem aresztu przeciw Wojciechowi Wojcikowicowi o futro.")
add_occ("Wojcikowicz", "Wojciech", "Kraśnik", "Mieszczanin", "Woycikowicz [?] / Wojcikowicz [Woycikowicz?]", 176, "1698", "Albertus Wojcikowicz", "Skazany zaocznie (contumacia)", "Skazany o nieoddanie futra.")

# Skan 177
add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 177, "1698", "Honestus Martinus Rymarczyk suburbanus", "Powód i protestujący o rolę Tatarską", "Spór z Janem Stryczakiem o niedotrzymanie słowa w sprawie arendy roli Tatarskiej.")
add_occ("Stryczak", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Struczak [?] / Stryczak [Struczak?]", 177, "1698", "Honestus Joannes Stryczak", "Pozwany o arendę roli Tatarskiej", "Pozwany przez Marcina Rymarczyka.")
add_occ("[Rękojmia roli]", "Szymon", "Kraśnik", "Mieszczanin", "Szymon [?]", 177, "1698", "Szymon", "Strona pierwotnego słowa o rolę", "Wzmiankowany w sporze Rymarczyka ze Stryczakiem.")

# Skan 178
add_occ("Markowicz", "Wygdor", "Kraśnik", "Żyd kraśnicki (obywatel kraśnicki)", None, 178, "1698", "Perfidus Wygdor Markowicz Judaeus", "Wierzyciel (wódka prosta)", "Dochodzi od Szymona Draganka półósma spustu wódki prostej.")
add_occ("Kuzokowicz", "Stanisław", "Kraśnik", "Sławetny (świadek)", "Kuzakowicz [?] / Kuzokowicz [Kuzakowicz?]", 178, "1698", "Famatus Stanislaus Kuzokowicz", "1. świadek w sprawie o wódkę", "Zeznaje o ugodzie na 5 spustów wódki w domu Wygdora.")
add_occ("Draganek", "Szymon", "Kraśnik", "Winiarz / Przedmieszczanin", None, 178, "1698", "Simon Draganek winiarz", "Dłużnik o wódkę prostą", "Winien Żydowi Wygdorowi półósma spustu wódki prostej.")
add_occ("Nowak", "Benedykt", "Kraśnik", "Uczciwy (świadek)", None, 178, "1698", "Honestus Benedykt Nowak", "2. świadek", "Słyszał w domu Wygdora obietnicę Draganka.")

# Skan 179
add_occ("Markowicz", "Wygdor", "Kraśnik", "Żyd kraśnicki", None, 179, "1698", "Wygdor Markowicz", "Wierzyciel uzyskujący 2 grzywny", "Uzyskuje wyrok przeciw Szymonowi Dragankowi.")
add_occ("Draganek", "Szymon", "Kraśnik", "Winiarz / Przedmieszczanin", None, 179, "1698", "Honestus Simon Draganek", "Skazany na 2 grzywny", "Zasądzony za nieoddanie 5 spustów wódki prostej.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", None, 179, "1698", "Famatus Paulus Słomkowski", "Powód o szkodę w życie", "Oskarża Macieja Perona i Wojciecha Wawrzyła o szkodę i nieposłuszeństwo.")
add_occ("Peron", "Maciej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 179, "1698", "H. Mathias Peron", "Pozwany (skazany na 3 grzywny)", "Pozwany z synem Wojciechem o szkodę w życie.")
add_occ("Wawrzyło", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 179, "1698", "Albertus Wawrzyło suburbanus", "Współpozwany o szkodę w życie", "Skazany na 3 grzywny wraz z Maciejem Peronem.")

# Skan 180
add_occ("Rymarczyk", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 180, "1698", "Martinus Rymarczyk", "Powód wygrywający w sprawie o rolę i zniewagę", "Ma dopłacić 1 zł 10 gr za rolę Tatarską i zebrać żyto.")
add_occ("Stryczak", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Struczak [?]", 180, "1698", "Joannes Stryczak", "Skazany na tydzień wieży i 6 grzywien", "Skazany za zniewagę Rymarczyka przez żonę w sklepie.")
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 180, "1698", "Spectabilis Joannes Majowski Consul", "Powód uzyskujący kontumację", "Uzyskuje kontumację przeciw Wojciechowi Piaseckiemu o pobicie.")
add_occ("Piasecki", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 180, "1698", "Albertus Piasecki", "Skazany zaocznie (contumacia)", "Skazany z instancji Jana Majowskiego.")
add_occ("Maśniarczyk", "Kazimierz", "Kraśnik", "Uczciwy", "Maśniarczyk [?]", 180, "1698", "Kazimierz Maśniarczyk", "Powód o zatrzymanie sika w ogrodzie", "Uzyskuje 1. kontumację przeciw Stanisławowi Torańskiemu.")
add_occ("Torański", "Stanisław", "Kraśnik", "Uczciwy", "Torański [?]", 180, "1698", "Stanislaus Torański", "Skazany zaocznie (contumacia)", "Skazany o zatrzymanie sika w ogrodzie.")

# Skan 181
add_occ("Nowacki", "Benedykt", "Kraśnik", "Uczciwy", None, 181, "1698", "H. Benedictus Nowacki", "Powód w sprawie inwentarza", "Wnosi o rozliczenie inwentarza przez bedela Ornatowskiego.")
add_occ("Ornatowski", "Wojciech", "Kraśnik", "Bedel sądowy", None, 181, "1698", "Albertus Ornatowski Bedellus", "Bedel składający relację", "Składa przysięgłą relację z inwentarza.")
add_occ("Dalmacki", "Wojciech", "Kraśnik", "Rzemiosło krawieckie / Mieszczanin", "Dalmacki [?]", 181, "1698", "Uciwy Wojciech Dalmacki Rzemiosła Krawieckiego", "Wnioskujący o wizję po Zychowiczowej", "Wnioskuje o spisanie pozostałości po zmarłej Zychowiczowej.")
add_occ("Zychowiczowa", "[Wdowa]", "Kraśnik", "Mieszczanka (zm.)", None, 181, "1698", "olim Honesta Zychowiczowa Vidua", "Zmarła spadkodawczyni", "W jej domu spisano inwentarz (w tym 1 zł 16 gr w woreczkach).")
add_occ("Chmielowicz", "Adam", "Kraśnik", "Delegowany przez wójta / Pisarz", None, 181, "1698", "P. Adam Chmielowic", "Delegat do wizji pośmiertnej", "Spisuje rzeczy w domu Zychowiczowej.")
add_occ("Petek", "Stefan", "Kraśnik", "Ławnik miejski", "Petkowicz [?]", 181, "1698", "Stephan Petek Ławnik", "Ławnik przy wizji pośmiertnej", "Współautor relacji z wizji po Zychowiczowej.")
add_occ("[Prezentująca Zofia]", "Zofia", "Kraśnik", "Mieszkanka / Opiekunka", None, 181, "1698", "Zofia", "Osoba prezentująca koszt koszuli śmiertelnej", "Przedkłada 7 pism na koszulę śmiertelną i 1 zł 16 gr.")

# Skan 182
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 182, "1698", "Sławetny Pan Jan Barankowicz Radca", "Protestujący o pobicie w gospodzie", "Oskarża Błażeja Stachowicza o zniewagę słowną, uderzenie w gębę i targanie za włosy.")
add_occ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Przedmieszczanin / Szewc", None, 182, "1698", "Błażej Stachowicz Przedmieszczanin", "Pozwany o pobicie rajcy", "Oskarżony o zniewagę i pobicie Jana Barankowicza w gospodzie.")
add_occ("Żmienda", "Jan", "Kraśnik", "Uczciwy (krewny Barankowicza)", "Żmienda [?]", 182, "1698", "Uciwy Jan Żmienda", "Krewny rajcy obecny w gospodzie", "Wymieniony jako krewny, z którym Barankowicz poszedł na rozmowę.")

# Skan 183
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 183, "1698", "Jan Barankowicz", "Prezentujący rany w rezydencji wójta", "Okazuje krwawą pręgę na twarzy i ból głowy.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", "Pilaszkowic [Bielaszkowic?]", 183, "1698", "Wawrzyniec Pilaszkowic Ławnik", "Ławnik przy obdukcji", "Obecny przy obdukcji ran Barankowicza.")
add_occ("Trzelowicz", "Adam", "Kraśnik", "Pisarz urzędu wójtowskiego", "Chmielowicz [Trzelowicz?]", 183, "1698", "Adamus Chmielowic Pisarz Urzędu", "Pisarz spisujący obdukcję", "Wpisuje obdukcję ran rajcy Barankowicza.")
add_occ("Barankowiczowa", "Anna", "Kraśnik", "Sławetna Pani (żona Jana Barankowicza)", None, 183, "1698", "Sławetna Pani Anna Barankowiczowa", "Protestująca o zniesławienie na Rynku", "Protestuje przeciw Franciszce Sitarskiej o pomówienie o pokrewieństwo z Zychowiczową.")
add_occ("Sitarska", "Franciszka", "Kraśnik", "Żona Marcina Sitarskiego", None, 183, "1698", "Uciwa Franciszka żony Marcina Sitarskiego", "Pozwana o zniesławienie", "Pomówiła Annę Barankowiczową na Rynku.")
add_occ("Sitarski", "Marcin", "Kraśnik", "Mąż Franciszki Sitarskiej / Rajca", None, 183, "1698", "Marcin Sitarski", "Mąż pozwanej Franciszki", "Wzmiankowany w protestacji Anny Barankowiczowej.")

# Skan 184
add_occ("Boron", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Boron [?]", 184, "1698", "H. Martinus Boron suburbanus", "Rękojmia (fideiussor) za S. Draganka", "Ręczy za uwolnienie Szymona Draganka z więzienia i spłatę 5 spustów wódki.")
add_occ("Skakha", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Skakha [?]", 184, "1698", "Albertus Skakha suburbanus", "Współrękojmia za S. Draganka", "Ręczy wspólnie z Marcinem Boronem.")
add_occ("Draganek", "Szymon", "Kraśnik", "Winiarz / Przedmieszczanin", None, 184, "1698", "H. Simon Draganek", "Dłużnik zwolniony za poręczeniem", "Zwolniony z więzienia z rozłożeniem długu na raty.")
add_occ("Markowicz", "Wygdor", "Kraśnik", "Żyd kraśnicki", None, 184, "1698", "Infidelis Wygdor Markowicz", "Wierzyciel odbierający poręczenie", "Zabezpieczony na majątku rękojemców.")

# Skan 185
add_occ("Pałuskiewicz", "Baltazar", "Kraśnik", "Kanonik regularny / Promotor Bractwa Literackiego", None, 185, "1698", "Venerabilis Baltazar Pałuskiewicz", "Powód o czynsze w wosku dla Bractwa", "Pozywa dłużników zalegających z woskiem do ołtarza Bractwa Literackiego.")
add_occ("Ornatowski", "Wojciech", "Kraśnik", "Bedel sądowy", None, 185, "1698", "Albertus Ornatowski Bedellus", "Bedel pozywający dłużników bractwa", "Doręcza pozwy dłużnikom czynszowym.")
add_occ("Jankowski", "Szymon", "Kraśnik", "Mieszczanin", None, 185, "1698", "Simon Jankowski", "Skazany na pół funta wosku", "Zalegał z czynszem na ołtarz Bractwa Literackiego.")
add_occ("Pielichowicz", "Maciej", "Kraśnik", "Mieszczanin", None, 185, "1698", "Mathias Pielichowicz", "Skazany zaocznie (contumacia)", "Zalegał z czynszem Bractwu Literackiemu.")
add_occ("Jesurkiewicz", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", None, 185, "1698", "Stanislaus Jesurkiewicz", "Skazany zaocznie o czynsz bractwa", "Zalegał z czynszem od ostatniego kwitu.")
add_occ("Rebiński", "Stanisław", "Kraśnik", "Mieszczanin", None, 185, "1698", "Stanislaus Rebiński", "Skazany na pół funta wosku", "Zalegał z czynszem Bractwu Literackiemu.")
add_occ("Abel", "Maciej", "Kraśnik", "Mieszczanin (Camax)", None, 185, "1698", "Mathias Abel Camax", "Skazany na pół funta wosku", "Zalegał z czynszem Bractwu Literackiemu.")
add_occ("Nowacki", "Tomasz", "Kraśnik", "Mieszczanin", None, 185, "1698", "Tomasz Nowacki", "Skazany na pół funta wosku", "Zalegał z czynszem Bractwu Literackiemu.")
add_occ("Dubaj", "Jakub", "Kraśnik", "Mieszczanin", None, 185, "1698", "Jacobus Dubaj", "Skazany zaocznie o czynsz bractwa", "Zalegał z czynszem Bractwu Literackiemu.")

# Skan 186
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 186, "1698", "Pan Barankowicz Radca", "Powód w sporze ze Stachowiczem", "Sprawa odroczona z powodu choroby pozwanego.")
add_occ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Przedmieszczanin / Szewc", None, 186, "1698", "Błażej Stachowicz", "Pozwany zgłaszający chorobę", "Żona zgłasza legalitas infirmitatis po pobiciu.")
add_occ("Jardzioch", "Tomasz", "Kraśnik", "Uczciwy (świadek)", "Jardzioch [?]", 186, "1698", "Uciwy Tomasz Jardzioch", "Świadek w sprawie P. Słomkowskiego", "Zeznaje o spotkaniu nocą z Wojciechem Peronem i Jakubem Wawrzyłem wiozącymi snopki.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", None, 186, "1698", "Famatus Paulus Słomkowski Viceadvocatus", "Powód o kradzież snopków", "Uzyskuje wyrok 3 dni wieży dla Peronów.")
add_occ("Peron", "Wojciech", "Kraśnik (Przedmieście)", "Syn Matyjasza Perona", None, 186, "1698", "Wojciech Peron syn Matyasza", "Obwiniony o nocny przewóz snopków", "Widziany na wozie drabiniastym w święto św. Bartłomieja.")
add_occ("Peron", "Maciej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 186, "1698", "Mathias Peron", "Ojciec Wojciecha Perona (dekret 3 dni wieży)", "Skazany z synem na 3 dni wieży.")
add_occ("Wawrzyło", "Jakub", "Kraśnik (Przedmieście)", "Brat Wojciecha Perona", None, 186, "1698", "Jakub Wawrzyło", "Współuczestnik nocnego przewozu snopków", "Jechał na wozie drabiniastym z Wojciechem Peronem.")
add_occ("Wawrzyło", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 186, "1698", "Albertus Wawrzyło", "Pozwany (wezwany przez bedela)", "Ma stawić się przez bedela przed sądem.")

# Skan 187
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska", None, 187, "1698", "Catharina Nowacka", "Skazana zaocznie (1. kontumacja)", "Pozwana o dług po Ubaldzie Janaszkowiczu.")
add_occ("Nowacki", "Wojciech", "Kraśnik / Urzędów", "Wicewójt urzędowski", None, 187, "1698", "Albertus Nowacki", "Skazany zaocznie (1. kontumacja)", "Współpozwany o dług po Ubaldzie Janaszkowiczu.")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki (zm.)", None, 187, "1698", "olim Ubaldus Janaszkowicz", "Zmarły spadkodawca", "Wzmiankowany w kontumacji sukcesorów.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", None, 187, "1698", "Paulus Słomkowski", "Powód i przyjmujący poręczenie", "Uzyskuje kontumację Nowackich; przyjmuje poręczenie za Matyjasza Perona.")
add_occ("Piasecki", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 187, "1698", "Wojciech Piasecki", "Rękojmia za Matyjasza Perona", "Wyręcza Matyjasza Perona z więzienia.")
add_occ("Świeczka", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 187, "1698", "Marcin Świeczka", "Współrękojmia za Matyjasza Perona", "Ręczy z Wojciechem Piaseckim na dobrach ruchomych i nieruchomych.")
add_occ("Peron", "Maciej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 187, "1698", "Matyasz Peron", "Uwięziony zwolniony za poręczeniem", "Zwolniony z więzienia w sprawie o szkodę syna Wojciecha.")

# Skan 188
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 188, "1698", "Famatus Paulus Słomkowski Viceadvocatus", "Urzędnik dokonujący intromisji", "Dokonuje pomiaru i intromisji w rolę Jurkowską.")
add_occ("Trzelowicz", "Adam", "Kraśnik", "Pisarz urzędu wójtowskiego", "Chmielowicz [Trzelowicz?]", 188, "1698", "Honoratus Adamus Trzelowicz Notarius", "Pisarz przy intromisji", "Wpisuje pomiar i intromisję roli Jurkowskiej.")
add_occ("Tokarzowa", "Jadwiga", "Kraśnik (Przedmieście)", "Wdowa po Janie Tokarzu", None, 188, "1698", "Jadwiga Tokarzowa wdowa", "Wnioskująca o intromisję", "Wdowa po przedmieszczaninie Janie Tokarzu.")
add_occ("Tokarz", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin (zm.)", None, 188, "1698", "niegdy Jan Tokarz", "Zmarły mąż Jadwigi Tokarzowej", "Wzmiankowany w akcie intromisji z 9 X 1698 r.")
add_occ("Kieniewicz", "Jan Onufry", "Kraśnik", "Wójt / Adwokat ordynaryjny kraśnicki", "Onupkiewicz [Kieniewicz?]", 188, "1698", "Famatus Joannes Onupkiewicz Advocatus", "Zlecający intromisję", "Deputuje wicewójta i pisarza do pomiaru dóbr Jurkowskich.")
add_occ("Jurek", "Paweł", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 188, "1698", "Uciwy Paweł Jurek", "Sąsiad roli Jurkowskiej", "Posiada sąsiednią kwaterę roli.")
add_occ("Kowalik", "Wawrzyniec", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 188, "1698", "Uciwy Wawrzyniec Kowalik", "Sąsiad roli Jurkowskiej", "Posiada sąsiednią kwaterę roli.")
add_occ("Skowronek", "Jan", "Kraśnik (Przedmieście)", "Przedmieszczanin (zm.)", None, 188, "1698", "olim Honestus Joannes Skowronek", "Poprzedni nabywca roli (zm.)", "Wzmiankowany przy sprzedaży roli z Zofią.")

# Skan 189
add_occ("Jesurkiewicz", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", None, 189, "1698", "Sławetny P. Stanisław Jesurkiewicz Consul antiquus", "Świadek bójki u Żyda Borucha", "Zeznaje o spotkaniu z Barankowiczem, Żmiendą i Stachowiczem w szynku.")
add_occ("Ornatowski", "Wojciech", "Kraśnik", "Bedel sądowy", None, 189, "1698", "Ornatowski Bedellus", "Bedel odbierający przysięgę", "Zaprzysięga Stanisława Jesurkiewicza.")
add_occ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Szewc (majster) / Przedmieszczanin", None, 189, "1698", "Honoratus Blasius Stachowicz szewskiego majstra", "Sprawca bójki (powołujący świadka)", "Prosi Jesurkiewicza na kwater piwa do Żyda Borucha.")
add_occ("Boruch", "[Halka]", "Kraśnik", "Żyd kraśnicki (szynkarz)", "Halka", 189, "1698", "Żyd Boruch alias Halka", "Szynkarz, u którego doszło do bójki", "W jego szynku pito piwo i miód 6 X 1698 r.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 189, "1698", "JP. Jan Barankowicz Radca", "Uczestnik bójki u Borucha", "Wszedł ze Żmiendą na półgarca miodu i wdał się w kłótnię ze Stachowiczem.")
add_occ("Żmienda", "Jan", "Kraśnik", "Uczciwy (towarzysz Barankowicza)", "Żmienda [?]", 189, "1698", "Uciwy Jan Żmienda", "Towarzysz Barankowicza", "Pił miód z rajcą Barankowiczem.")
add_occ("Stępień", "Jan", "Kraśnik", "Szwagier Błażeja Stachowicza", None, 189, "1698", "Jan Stępień szwagier", "Osoba, z którą Stachowicz miał się pogodzić", "Wzmiankowany w zeznaniu Jesurkiewicza.")

# Skan 190
add_occ("Jesurkiewicz", "Stanisław", "Kraśnik", "Stary rajca (Antiquus Consul)", None, 190, "1698", "Stanislaus Jesurkiewicz Antiquus Consul", "Świadek i asesor sądowy", "Kończy zeznanie o uderzeniu Barankowicza przez Stachowicza; zasiada w sądzie 10 X 1698 r.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 190, "1698", "P. Barankowicz", "Poszkodowany w bójce i rajca", "Uderzony pięścią przez Stachowicza; zasiada w sądzie 10 X 1698 r.")
add_occ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Szewc (majster)", None, 190, "1698", "Błażej Stachowicz", "Sprawca uderzenia i wyzywania urzędu", "Wyzywał Barankowicza i cały urząd.")
add_occ("Żmienda", "Jan", "Kraśnik", "Uczciwy", None, 190, "1698", "Żmienda", "Rozdzielający bijących się", "Trzymał Barankowicza w pół podczas bójki.")
add_occ("Kieniewicz", "Jan Onufry", "Kraśnik", "Adwokat ordynaryjny kraśnicki", "Onupkiewicz [Kieniewicz?]", 190, "1698", "Famatus Joannes Onupkiewicz Advocatus Ordinarius", "Adwokat w składzie sądu", "Obecny na sesji z 10 X 1698 r.")
add_occ("Potocki", "Adam", "Kraśnik", "Prokonsul kraśnicki", "Potokowicz", 190, "1698", "Adamus Potokowicz Proconsul", "Prokonsul w składzie sądu", "Przewodniczy sesji z 10 X 1698 r.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 190, "1698", "Paulus Słomkowski Viceadvocatus", "Wicewójt w składzie sądu", "Obecny na sesji z 10 X 1698 r.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Rajca / Ławnik kraśnicki", None, 190, "1698", "Stephanus Kwasowic", "Członek sądu", "Obecny na sesji z 10 X 1698 r.")
add_occ("Piasecki", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 190, "1698", "Honestus Albertus Piasecki", "Powód przeciw J. Murowskiemu", "Otrzymuje dylację na inkwizycję.")
add_occ("Murowski", "Jan", "Kraśnik", "Rajca kraśnicki", "Murowski [?]", 190, "1698", "Joannes Murowski Consul", "Pozwany przez W. Piaseckiego", "Dylacja na inkwizycję.")

# Skan 191
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", None, 191, "1698", "Sławetny Pan Paweł Słomkowski", "Powód o 802 złp 15 gr", "Dopuszcza się mu dowodu z zeznań i przysięgi do tygodnia.")
add_occ("Nowacki", "Wojciech", "Kraśnik / Urzędów", "Landwójt urzędowski", None, 191, "1698", "Wojciech Nowacki Landwójt Urzędowski", "Pozwany o 802 złp 15 gr", "Ma stawić się osobiście z dokumentami.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska", "Janaszkowicowa", 191, "1698", "Katarzyna Janaszkowicowa", "Współpozwana o 802 złp 15 gr", "Współpozwana jako dziedziczka Ubalda Janaszkowica.")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki (zm.)", None, 191, "1698", "Śp. P. Ubaldy Janaszkowic", "Zmarły spadkodawca", "Wzmiankowany w dekrecie o 802 złp 15 gr.")
add_occ("Brzozowski", "Andrzej", "Kraśnik", "Urodzony / Pełnomocnik", "Brzozowski [?]", 191, "1698", "Urodzony Pan Andrzej Brzozowski plenipotent", "Pełnomocnik strony pozwanej", "Staje w imieniu Nowackich przed sądem.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 191, "1698", "Famatus Joannes Barankowicz", "Strona sporu ze Stachowiczem", "Dalsza dylacja na inkwizycję.")
add_occ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Szewc (majster)", None, 191, "1698", "Blasius Stachowicz", "Strona sporu z Barankowiczem", "Dalsza dylacja na inkwizycję.")

# Skan 192
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 192, "1698", "Famatus Paulus Słomkowski Viceadvocatus", "Powód przeciw M. Peronowi", "Dalsze postępowanie o karę więzienia.")
add_occ("Peron", "Maciej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 192, "1698", "H. Mathias Peron", "Pozwany z synem", "Sprawa odesłana do egzekucji.")
add_occ("Sitarski", "Franciszek", "Kraśnik", "Mieszczanin", None, 192, "1698", "Franciscus Sitarski", "Skazany na 7 dni wieży (contumacia)", "Skazany zaocznie z instancji Jana Barankowicza.")
add_occ("Bzówka", "[Mieszczanin]", "Kraśnik", "Mieszczanin", "Bzówka [?]", 192, "1698", "Bzówka", "Skazany na 7 dni wieży (contumacia)", "Skazany wspólnie z Franciszkiem Sitarskim.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 192, "1698", "Spectabilis Joannes Barankowicz Consul", "Powód uzyskujący kontumację", "Uzyskuje wyrok 7 dni wieży dla Sitarskiego i Bzówki.")
add_occ("Pacławkowic", "Jan", "Kraśnik", "Uczciwy (świadek)", "Pacławkowic [?]", 192, "1698", "Honestus Joannes Pacławkowic", "Świadek przewozu snopów w nocy", "Widział nocą wóz ze snopami koło domu Bartłomieja syna Piwnika.")
add_occ("Piwnik", "Bartłomiej", "Kraśnik", "Syn Piwnika", "Piwnik [?]", 192, "1698", "Bartłomiej syn Piwnika", "Właściciel gumna/stodoły", "Koło jego domu przejeżdżano nocą ze snopami.")
add_occ("Trzelowicz", "Adam", "Kraśnik", "Pisarz urzędu wójtowskiego", None, 192, "1698", "Adamus Trzelowicz Notarius", "Urzędnik wizjujący szkodę", "Wizjuje łąkę Tropycaka z ławnikiem Bielaszkowicem.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 192, "1698", "Laurentius Bielaszkowic Scabinus", "Ławnik wizjujący szkodę", "Wizjuje szkodę na gruncie Tropycaka.")
add_occ("Kieniewicz", "Jan Onufry", "Kraśnik", "Adwokat ordynaryjny kraśnicki", "Onupkiewicz [Kieniewicz?]", 192, "1698", "Joannes Onupkiewicz Advocatus", "Zlecający wizję szkody", "Wyznacza pisarza i ławnika do wizji.")
add_occ("Tropycak", "Krzysztof", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Tropycak [?]", 192, "1698", "H. Christophorus Tropycak suburbanus", "Poszkodowany w szkodzie polnej", "Wnioskuje o wizję spasionego ogrodu.")

# Skan 193
add_occ("Tropycak", "Krzysztof", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Tropycak [?]", 193, "1698", "Krzysztof Tropycak", "Poszkodowany na łące i płocie", "Okazuje wyjedzoną trawę i brak płotu sąsiedzkiego.")
add_occ("Kondyszek", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin (sąsiad)", "Kondyszek [?]", 193, "1698", "Wojciech Kondyszek", "Pozwany o szkodę bydłem i niegrodzenie płotu", "Nie chce grodzić płota między ogrodami.")
add_occ("Dutkiewicz", "Stanisław", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 193, "1698", "Honestus Stanislaus Dutkiewicz suburbanus", "Protestujący o pobicie w domu wójta", "Składa protestację z 13 X 1698 r. przeciw Marcinowi Rzepce.")
add_occ("Rzepka", "Marcin", "Kraśnik", "Mieszczanin", None, 193, "1698", "Uciwy Marcin Rzepka", "Pozwany o uderzenie i rzucenie pod ławę", "Wszczyna awanturę przy stole u wójta o dług za półkurca.")
add_occ("Petek", "Adam", "Kraśnik", "Uczciwy (świadek)", "Petek [?]", 193, "1698", "Uciwy Adam Petek", "Rozmówca Dutkiewicza przy stole", "Wymieniony w protestacji z 13 X 1698 r.")

# Skan 194
add_occ("Mutkowic", "Tomasz", "Kraśnik", "Towarzysz rzemiosła szewskiego", None, 194, "1698", "Thomas Mutkowic towarzysz szewski", "Protestujący przeciw majstrowi", "Oskarża byłego majstra Szymona Soleckiego o zniesławienie w cechu.")
add_occ("Solecki", "Szymon", "Kraśnik", "Majster rzemiosła szewskiego", None, 194, "1698", "Szymon Solecki Majster szewski", "Pozwany o obrazę towarzysza", "Pozwany przez Tomasza Mutkowica.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 194, "1698", "Słomkowski", "Powód przeciw Nowackiej", "Proces z 17 X 1698 r.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska", None, 194, "1698", "Nowacka", "Pozwana reprezentowana przez pełnomocnika", "Nie stawia się osobiście mimo dekretu.")
add_occ("Potocki", "Adam", "Kraśnik", "Prokonsul / Rajca", "Potokowicz", 194, "1698", "Adamus Potokowicz", "Sędzia na sesji", "Obecny 17 X 1698 r.")
add_occ("Murowski", "Jan", "Kraśnik", "Rajca kraśnicki", "Murowski [?]", 194, "1698", "Joannes Murowski", "Sędzia na sesji", "Obecny 17 X 1698 r.")
add_occ("Kwasowic", "Stefan", "Kraśnik", "Ławnik przysięgły", None, 194, "1698", "Stephanus Kwasowic", "Ławnik na sesji", "Obecny 17 X 1698 r.")
add_occ("Bielaszkowic", "Wawrzyniec", "Kraśnik", "Ławnik przysięgły", None, 194, "1698", "Laurentius Bielaszkowic", "Ławnik na sesji", "Obecny 17 X 1698 r.")
add_occ("Wierzbicki", "Stefan", "Kraśnik", "Pełnomocnik", "Wierzbicki [?]", 194, "1698", "Stephanus Wierzbicki plenipotent", "Pełnomocnik strony pozwanej", "Staje za Katarzynę Nowacką.")

# Skan 195
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska", None, 195, "1698", "Pani Nowacka", "Pozwana skazana na 2 grzywny", "Ma okazać dokumenty pod karą 14 grzywien.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 195, "1698", "Famatus Słomkowski", "Powód pod karą 14 grzywien do dowodu", "Powołuje świadka Jana Barankowicza.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 195, "1698", "Spectabilis Joannes Barankowicz Consul", "Świadek w sprawie Słomkowskiego", "Zeznaje o długach po wójcie Janaszkowiczu (160 złp i 60 złp).")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki (zm.)", None, 195, "1698", "olim Ubaldus Janaszkowicz Advocatus", "Zmarły dłużnik / spadkodawca", "Wzmiankowany jako winien pieniądze Słomkowskiemu.")
add_occ("Wojtanowski", "[Pan]", "Kraśnik", "Szlachcic / Mieszczanin", "Wojtanowski [?]", 195, "1698", "P. Wojtanowski", "Strona transakcji w zeznaniu", "Wymieniony obok Piotra Koronnego.")
add_occ("Koronny", "Piotr", "Kraśnik", "Mieszczanin", "Koronny [?]", 195, "1698", "P. Piotr Koronny", "Strona transakcji w zeznaniu", "Wymieniony w zeznaniu Barankowicza.")

# Skan 196
add_occ("Grzymałowski", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 196, "1698", "Famatus Albertus Grzymałowski Scabinus Juratus", "Świadek w sprawie Słomkowskiego", "Zeznaje o zleceniu od Słomkowskiego w sprawie długów po Janaszkowiczu.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", None, 196, "1698", "Pan Paweł Słomkowski Podwójci", "Powód w dwóch sprawach", "Powołuje świadków przeciw Nowackim oraz przeciw Peronowi.")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki (zm.)", None, 196, "1698", "P. Ubald Janaszkowic Wójt", "Zmarły spadkodawca", "Wzmiankowany w zeznaniu Grzymałowskiego.")
add_occ("Potocki", "Adam", "Kraśnik", "Prokonsul / Rajca", "Potokowski [Potocki?]", 196, "1698", "Potokowski", "Wzmiankowany w zeznaniu Grzymałowskiego", "Wymieniony jako pretendujący do długów.")
add_occ("Peron", "Maciej", "Kraśnik (Przedmieście)", "Przedmieszczanin", None, 196, "1698", "Peron", "Strona sporu ze Słomkowskim", "Dalsza dylacja na inkwizycję.")
add_occ("Wereszczyna", "Agnieszka", "Kraśnik", "Wdowa po Tomaszu Jutratku", None, 196, "1698", "H. Agnes Wereszczyna Vidua", "Powódka uzyskująca kontumację", "Sprawa przeciw Tomaszowi Jutratkowi [?] o len i płótno.")
add_occ("Jutratek", "Tomasz", "Kraśnik", "Mieszczanin", "Jutratek [?]", 196, "1698", "H. Thomas Jutratek", "Pozwany o len i płótno (contumax)", "Skazany zaocznie z instancji Agnieszki Wereszczyny.")
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 196, "1698", "Joannes Barankowicz Consul", "Strona sporu ze Stachowiczem", "Dalsza dylacja na inkwizycję.")
add_occ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Szewc", None, 196, "1698", "Blasius Stachowicz", "Strona sporu z Barankowiczem", "Dalsza dylacja na inkwizycję.")
add_occ("Parciak", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Parciak [?]", 196, "1698", "Honestus Thomas Parciak suburbanus", "Świadek ze strony P. Słomkowskiego", "Składa przysięgłe zeznanie 18 X 1698 r.")

# Skan 197
add_occ("Parciak", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Parciak [?]", 197, "1698", "Thomas Parciak", "Świadek o budowie na folwarku", "Zeznaje o zwiezieniu 40 płatw i 20 słupów sosnowych od Słomkowskiego dla wójta Janaszkowica przed 30 laty.")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki (zm.)", None, 197, "1698", "Nieboszczyk P. Ubaldy Janaszkowic", "Zmarły dłużnik", "Pożyczał budulec oraz faskę gwoździ gontowych od Słomkowskiego.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Podwojci / Wicewójt kraśnicki", None, 197, "1698", "Pan Słomkowski Podwójci", "Wierzyciel zmarłego wójta", "Wierzyciel z tytułu budulca i gwoździ gontowych.")
add_occ("Nowacka", "Katarzyna", "Kraśnik / Urzędów", "Landwójtowa urzędowska", None, 197, "1698", "P. Nowacka", "Strona supplikująca", "Wzmiankowana w zeznaniu Parciaka.")
add_occ("Zuławski", "[Pan]", "Kraśnik", "Szlachcic / Urzędnik", "Zuławski [?]", 197, "1698", "Pan Zuławski", "Adresat suppliki Nowackiej", "Wzmiankowany w zeznaniu Parciaka.")
add_occ("Wójcik", "Szymon", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Wojcik", 197, "1698", "Honestus Simon Wójcik suburbanus", "Świadek o pożyczce gwoździ", "Przyniósł od Słomkowskiego faskę gwoździ dla śp. wójta Janaszkowica.")
add_occ("Stadnicki", "[Pan]", "Kraśnik", "Stolnik czernihowski", None, 197, "1698", "Jegomość Pan Stadnicki Stolnik Czerniechowski", "Odbiorca gwoździ (w zeznaniu)", "Dla niego śp. wójt Janaszkowicz pożyczył gwoździe od Słomkowskiego.")

# Skan 198
add_occ("Barankowicz", "Jan", "Kraśnik", "Rajca kraśnicki", None, 198, "1698", "Joannes Barankowicz Consul", "Powód uzyskujący wyrok 7 grzywien i 3 dni wieży", "Powołuje świadka Jana Żmiendę i uzyskuje wyrok przeciw Stachowiczowi.")
add_occ("Żmienda", "Jan", "Kraśnik", "Uczciwy (świadek)", None, 198, "1698", "H. Joannes Żmienda", "Świadek bójki u Borucha", "Potwierdza zeznanie Stanisława Jesurkiewicza o uderzeniu w twarz Barankowicza.")
add_occ("Boruch", "[Halka]", "Kraśnik", "Żyd kraśnicki (szynkarz)", None, 198, "1698", "Żyd Boruch", "Właściciel szynku", "Wzmiankowany w zeznaniu Jana Żmiendy.")
add_occ("Stachowicz", "Błażej", "Kraśnik (Przedmieście)", "Szewc", None, 198, "1698", "Honestus Blasius Stachowicz", "Skazany zaocznie na 7 grzywien i 3 dni wieży", "Skazany na egzekucję przez czeladź miejską.")
add_occ("Słomkowski", "Paweł", "Kraśnik", "Wicewójt kraśnicki", None, 198, "1698", "Sławetny Pan Paweł Słomkowski", "Powód w sprawie o żyto", "Sąd nakazuje obwinionym odprzysiąc się w sprawie zabrania żyta.")

# Skan 199
add_occ("Majowski", "Jan", "Kraśnik", "Rajca kraśnicki", None, 199, "1698", "Famatus Joannes Majowski Consul", "Protestujący przeciw szafarzowi", "Oskarża Wojciecha Piaseckiego o najście domu z czeladzią żołnierską po sieczkę.")
add_occ("Piasecki", "Wojciech", "Kraśnik (Przedmieście)", "Przedmieszczanin (Longer) / Szafarz miejski", None, 199, "1698", "H. Albertus Piasecki Suburbanus Longerus", "Reprotestujący szafarz miejski", "Tłumaczy pobór sieczki służbowym obowiązkiem zaopatrzenia przejeżdżających żołnierzy.")

# Skan 200 (fascykuł z 1664 r.)
add_occ("Szmara", "Paweł", "Kraśnik", "Mieszczanin (syn starego Szmary)", None, 200, "1664", "Paulus Szmara", "Powód w imieniu ojca o 3 zł", "Dochodzi 3 zł długu za Marcina Biernata od Macieja Szykowica.")
add_occ("Szmara", "[Stary]", "Kraśnik", "Mieszczanin (ojciec Pawła)", None, 200, "1664", "stary Szmara", "Właściwy wierzyciel (ma złożyć przysięgę)", "Wezwany do złożenia przysięgi w piątek.")
add_occ("Szykowic", "Maciej", "Kraśnik", "Mieszczanin", None, 200, "1664", "Mathias Szykowic", "Pozwany o poręczenie 3 zł", "Skazany warunkowo na zapłatę 3 zł z prawem regresu do Biernata.")
add_occ("Biernat", "Marcin", "Kraśnik", "Mieszczanin", None, 200, "1664", "Marcin Biernat", "Dłużnik pierwotny (w regresie)", "Wzmiankowany jako dłużnik 3 zł.")
add_occ("Jajczyk", "Kasper", "Kraśnik", "Mieszczanin", None, 200, "1664", "Casparus Jajczyk", "Powód w sprawie ugodowej", "Zawiera zgodę przed sądem z Sebastianem Jajczykiem.")
add_occ("Jajczyk", "Sebastian", "Kraśnik", "Mieszczanin", None, 200, "1664", "Sebastianus Jajczyk", "Pozwany w sprawie ugodowej", "Zawiera ugodę z Kasprem Jajczykiem.")

# Zapis gen_data_j20_part8.json
with open('/home/ubuntu/workspace/Gen/gen_data_j20_part8.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j20_part8.json ({len(gen_data)} profili) oraz CSV.")
