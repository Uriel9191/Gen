# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part2.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

# Indeks istniejących profili po kluczu (nazwisko, imie, miejsce)
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
        min_y = min(yr_nums) if yr_nums else 1658
        max_y = max(yr_nums) if yr_nums else 1658
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

# === PARTIA 3 (SKANY 51–75) ===
# Skan 51
add_occ("Poszłygarczyk", "Stanisław", "Kraśnik", "Mieszczanin", "Soszłygarczyk [?]", 51, "1658", "Fam. Stanislai Soszlygarczyk", "Powód (skarga o pobicie)", "Występuje w sporach sąsiedzkich i procesach przed Sądem Wójtowskim w 1658 r.")
add_occ("Oleszek", "Wojciech", "Kraśnik", "Mieszczanin", "Oleszkowic [?]", 51, "1658", "Alberti Oleszek", "Pozwany o pobicie", "Pozwany przez Stanisława Poszłygarczyka o pobicie w 1658 r.")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły", None, 51, "1658", "Fam. Gregorius Fox", "Powód (dług fl 25 gr 15)", "Aktywny ławnik i wierzyciel w aktach z 1658 r.")
add_occ("Zdanowa", "Jadwiga", "Kraśnik", "Mieszkanka", "Zdanianka [?]", 51, "1658", "Hedvigis Zdanianka", "Pozwana o dług fl 25 gr 15", "Pozwana przez Grzegorza Foxa o dług fl 25 gr 15.")
add_occ("Sulik", "Marcin", "Kraśnik", "Mieszczanin", "Sulik [?]", 51, "1658", "Martini Sulik", "Powód (relacja woźnego)", "Powód w sprawie przeciw Wojciechowi Siedlatce i Maciejowi Dudzikowi.")
add_occ("Siedlatka", "Wojciech", "Kraśnik", "Mieszczanin", "Siedlatko [?]", 51, "1658", "Albertum Siedlatka", "Pozwany (relacja woźnego)", "Pozwany przez Marcina Sulika w 1658 r.")
add_occ("Dudzik", "Maciej", "Kraśnik", "Mieszczanin", "Dudzik [?]", 51, "1658", "Mathiam Dudzik", "Pozwany (relacja woźnego)", "Pozwany przez Marcina Sulika w 1658 r.")
add_occ("Klatkowski", "Jan", "Kraśnik", "Mieszczanin", "Klatkowski [?]", 51, "1658", "Fam. Joannis Klatkowski", "Strona procesowa (diligentia)", "Występuje w procesach sądowych w 1658 r.")
add_occ("Łatka", "Jan", "Kraśnik", "Mieszczanin", "Łatka [?] / Lotka [?]", 51, "1658", "Joannis Łatka", "Strona procesowa (diligentia)", "Występuje w procesie z Janem Klatkowskim przeciw Poszłygarczykowi.")
add_occ("Kłębski", "Jan", "Kraśnik", "Woźny sądowy przysięgły (Bedellus)", "Kłębski [?]", 51, "1658", "Joannes Kłębski Bedellus", "Woźny składający relację", "Woźny Sądu Wójtowskiego składający relacje z pozwów w 1658 r.")
add_occ("Słodzarski", "Marcin", "Kraśnik", "Mieszczanin", "Słodzarski [?]", 51, "1658", "Fam. Martini Słodzarski", "Pozwany o dług fl 4", "Pozwany przez Grzegorza Łotkę o fl 4.")
add_occ("Łotka", "Grzegorz", "Kraśnik", "Mieszczanin", "Lotka [?]", 51, "1658", "Fam. Gregorii Łotka", "Powód o dług fl 4", "Wierzyciel Marcina Słodzarskiego na sumę fl 4.")

# Skan 52
add_occ("Gębalski", "Wojciech", "Kraśnik", "Mieszczanin", "Gębala [?]", 52, "1658", "Adalbertus Gębalski", "Strona wykonująca dekret", "Występuje w księdze wójtowskiej w 1658 r.")
add_occ("Kurowek", "Mikołaj", "Kraśnik", "Mieszczanin", "Kurowicz [?]", 52, "1658", "Fam. Nicolaus Kurowek", "Powód przeciw Marcinowi Gębalce", "Mieszczanin kraśnicki występujący jako powód i świadek w 1658 r.")
add_occ("Ptaszek", "Marcin", "Kraśnik", "Mieszczanin", "Ptaszek [?]", 52, "1658", "Martinus Ptaszek", "Współpowód przeciw Marcinowi Gębalce", "Współpowód z Mikołajem Kurowkiem w 1658 r.")
add_occ("Gębalka", "Marcin", "Kraśnik", "Mieszczanin", "Gębałka [?]", 52, "1658", "Martinum Gębalka", "Pozwany o dług i szkody", "Pozwany w 1658 r. przez Mikołaja Kurowka, Marcina Ptaszka i Augustyna Kurowica.")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły", None, 52, "1658", "Fam. Gregorii Fox", "Powód w inkwizycji po W. Maruszkowicu", "Dochodzi fl 30 z dóbr po zmarłym Wojciechu Maruszkowicu.")
add_occ("Maruszkowic", "Wojciech", "Kraśnik", "Mieszczanin (zm.)", "Maruszka [?]", 52, "1658", "Nieboszczyk Woyciech Maruszkowic", "Zmarły dłużnik", "Po jego śmierci w 1658 r. toczy się spór wierzycieli (G. Fox, W. Prokopek) o pozostałe dobra.")
add_occ("Dębski", "Stefan", "Kraśnik", "Świadek przysięgły", "Dębowski [?]", 52, "1658", "Stefan Dębski", "Świadek w inkwizycji 8 mężów", "Jeden z 8 mężów zeznających w sprawie po Wojciechu Maruszkowicu.")
add_occ("Kozak", "Maciej", "Kraśnik", "Świadek przysięgły", "Kozłowski [?]", 52, "1658", "Maciej Kozak", "Świadek w inkwizycji 8 mężów", "Świadek w inkwizycji po Wojciechu Maruszkowicu.")
add_occ("Kuśmierz", "Szymon", "Kraśnik", "Świadek przysięgły", "Kuszmir [?]", 52, "1658", "Szymon Kuśmierz", "Świadek w inkwizycji 8 mężów", "Świadek w inkwizycji po Wojciechu Maruszkowicu.")
add_occ("Łysik", "Daniel", "Kraśnik", "Świadek przysięgły", "Łysik [?]", 52, "1658", "Daniel Łysik", "Świadek w inkwizycji 8 mężów", "Świadek w inkwizycji po Wojciechu Maruszkowicu.")
add_occ("Kowal", "Marcin", "Kraśnik", "Świadek przysięgły", "Kowal [?]", 52, "1658", "Marcin Kowal", "Świadek w inkwizycji 8 mężów", "Świadek w inkwizycji po Wojciechu Maruszkowicu.")

# Skan 53
add_occ("Kazimierski", "Jan", "Kraśnik", "Mieszczanin", "Rębiński [?]", 53, "1658", "Fam. Kazimierski", "Powód (spór o drzewo i granice)", "Powód w sporze o naruszenie granic i drzewa.")
add_occ("Zięba", "Sebastian", "Kraśnik", "Mieszczanin", "Zgęba [?]", 53, "1658", "Sebestianus Zięba", "Świadek przysięgły", "Świadek w sprawach Kazimierskiego i Stanisława Poszłygarczyka w 1658 r.")
add_occ("Dąbrowski", "Jan", "Kraśnik", "Mieszczanin", "Bąkowski [?]", 53, "1658", "Joannes Dąbrowski", "Świadek przysięgły", "Zeznaje o szkodzie na fl 8 i fl 3.")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły", None, 53, "1658", "Fam. Gregorii Fox", "Powód w serii pozwów o długi i wyderkafy", "Pozywa dłużników o sumy fl 10 gr 15, fl 100, fl 2 i fl 50.")
add_occ("Głodzik", "Andrzej", "Kraśnik", "Mieszczanin", "Gładysz [?]", 53, "1658", "Andream Głodzik", "Pozwany o dług fl 10 gr 15", "Dłużnik Grzegorza Foxa.")
add_occ("Sułkowicz", "Szymon", "Kraśnik", "Mieszczanin", "Sulik [?]", 53, "1658", "Simonem Sułkowicz", "Pozwany o dług", "Dłużnik Grzegorza Foxa.")
add_occ("Krupiński", "Wojciech", "Kraśnik", "Mieszczanin", "Krupiński [?]", 53, "1658", "Albertum Krupiński", "Pozwany o wyderkaf fl 100", "Dłużnik wyderkafowy Grzegorza Foxa na ogrodzie Łaskowskim.")
add_occ("Miazga", "Michał", "Kraśnik", "Mieszczanin", "Maslik [?]", 53, "1658", "Michaelem Miazga", "Pozwany o dług fl 2", "Dłużnik Grzegorza Foxa na fl 2.")
add_occ("Świątek", "Wawrzyniec", "Kraśnik", "Mieszczanin", "Świątkowicz [?]", 53, "1658", "Laurentium Świątek", "Pozwany o wyderkaf z fl 50", "Dłużnik wyderkafowy Grzegorza Foxa.")

# Skan 54–55
add_occ("Prokopek", "Wawrzyniec", "Kraśnik", "Mieszczanin", None, 54, "1658", "Wawrzyniec Prokopek", "Autor supliki przeciw G. Foxowi", "Autor własnoręcznie podpisanej supliki wklejonej do księgi w sprawie po W. Maruszkowicu.")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły", None, 54, "1658", "Pan Grzegorz Fox", "Pozwany w suplice W. Prokopka", "Zarzuca mu się zajęcie dóbr po W. Maruszkowicu.")
add_occ("Maruszkowic", "Wojciech", "Kraśnik", "Mieszczanin (zm.)", "Maruszka [?]", 54, "1658", "Nieboszczyk Woyciech Maruszkowic", "Zmarły dłużnik", "Wspomniany w suplice Wawrzyńca Prokopka.")
add_occ("Prokopek", "Wawrzyniec", "Kraśnik", "Mieszczanin", None, 55, "1658", "Wawrzyniec Prokopek", "Strona zapiski dorsalnej", "Zapiska dorsalna na odwrociu jego supliki.")

# Skan 56
add_occ("Gębecki", "Jan", "Kraśnik", "Mieszczanin", "Gołecki [?]", 56, "1658", "Joannes Gębecki", "Powód o fl 1 gr 15", "Pozywa Wdowę Krawcową o robotę i towar.")
add_occ("Krawcowa", "[Wdowa]", "Kraśnik", "Wdowa / Mieszkanka", "Kwiecina [?]", 56, "1658", "Viduam Krawcową", "Pozwana o fl 1 gr 15", "Pozwana przez Jana Gębeckiego o fl 1 gr 15.")
add_occ("Prokopek", "Wawrzyniec", "Kraśnik", "Mieszczanin", None, 56, "1658", "Laurentius Prokopek", "Powód o fl 20 i fl 140", "Dochodzi od Jana Gębskiego długu z zapisu na gruncie.")
add_occ("Gębski", "Jan", "Kraśnik", "Mieszczanin", "Grząbka [?]", 56, "1658", "Joannem Gębski", "Pozwany o fl 20 i fl 140", "Pozwany przez Wawrzyńca Prokopka.")
add_occ("Łysik", "Stanisław", "Kraśnik", "Mieszczanin", "Łysik [?]", 56, "1658", "Stanislai Łysik", "Powód o wyderkaf fl 200", "Dochodzi czynszu fl 56 od Jana Marlika.")
add_occ("Marlik", "Jan", "Kraśnik", "Mieszczanin", "Manlik [?]", 56, "1658", "Joannem Marlik", "Pozwany o wyderkaf fl 200", "Pozwany przez Stanisława Łysika o czynsz wyderkafowy.")

# Skan 57
add_occ("Marlik", "Jan", "Kraśnik", "Mieszczanin", "Manlik [?]", 57, "1658", "Joannes Marlik", "Strona odesłana do Sądu Podstarościego", "Dokończenie sprawy o wyderkaf.")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik przysięgły", None, 57, "1658", "Fam. Mathiae Konięga", "Powód o fl 30 i fl 2 podatku", "Dochodzi długu i komornego od Wawrzyńca Paszka.")
add_occ("Paszek", "Wawrzyniec", "Kraśnik", "Mieszczanin", "Bąk [?]", 57, "1658", "Laurentium Paszek", "Pozwany o fl 30 i fl 2", "Dłużnik Macieja Konięgi.")
add_occ("Poszłygarczyk", "Jan", "Kraśnik", "Mieszczanin", None, 57, "1658", "Joannes Poszłygarczyk", "Powód o komorne fl 5 i pobicie", "Pozywa Jadwigę Łopionkę o fl 5 komornego.")
add_occ("Łopionka", "Jadwiga", "Kraśnik", "Mieszkanka", "Łopianka [?]", 57, "1658", "Hedvigim Łopionka", "Pozwana o komorne i pobicie", "Pozwana przez Jana Poszłygarczyka.")
add_occ("Izaak", "[Żyd]", "Kraśnik", "Żyd kraśnicki", "Izaak [?]", 57, "1658", "Judeus Izaak", "Powód o fl 7 i fl 3", "Pozywa Wdowę Lalkę o dług z zastawu.")
add_occ("Lalka", "[Wdowa]", "Kraśnik", "Wdowa / Mieszkanka", "Falka [?]", 57, "1658", "Viduam Lalkę", "Pozwana o dług fl 7 i fl 3", "Pozwana przez Żyda Izaaka.")

# Skan 58
add_occ("Lalka", "[Wdowa]", "Kraśnik", "Wdowa / Mieszkanka", "Falka [?]", 58, "1658", "Pozwana Lalka", "Strona dekretu o fl 1 gr 15 i fl 3", "Nakaz spłaty długu żydowskiego.")
add_occ("Borowiec", "Marcin", "Kraśnik", "Mieszczanin", "Konięga [?]", 58, "1658", "Martini Borowiec", "Powód przeciw szl. P. Słodzarskiemu", "Dochodzi szkód na fl 200 w sprawie o konia i najazd.")
add_occ("Słodzarski", "Piotr", "Kraśnik (okolice)", "Szlachetny (Nobilis)", "Zadzarski [?]", 58, "1658", "Nobilem Petrum Słodzarski", "Pozwany o konia i szkody fl 200", "Szlachcic procesujący się przed sądem miejskim w 1658 r.")
add_occ("Skrzypkowski", "[Pan]", "Kraśnik (okolice)", "Szlachetny / Świadek", "Skrzypkowski [?]", 58, "1658", "p. Skrzypkowskiego", "Świadek powołany przez M. Borowca", "Powołany w sporze z Piotrem Słodzarskim.")
add_occ("Wężyk", "[Pan]", "Kraśnik (okolice)", "Szlachetny / Świadek", "Wężyk [?]", 58, "1658", "p. Wężyka", "Świadek powołany przez M. Borowca", "Powołany w sporze z Piotrem Słodzarskim.")

# Skan 59
add_occ("Babiński", "Jan", "Kraśnik", "Mieszczanin", "Zabiński [?]", 59, "1658", "Joannis Babiński", "Powód o granicę i drzewo", "Procesuje się z Jakubem Soroką o miedzę i płot.")
add_occ("Soroka", "Jakub", "Kraśnik", "Mieszczanin", "Sroka [?]", 59, "1658", "Jacobum Soroka", "Pozwany o granicę i drzewo", "Pozwany przez Jana Babińskiego.")
add_occ("Wiatrak", "[Mieszczanin]", "Kraśnik", "Sąsiad / Posiadacz gruntu", "Wiatrek [?]", 59, "1658", "przy Wiatraku", "Sąsiad graniczny", "Jego grunt stanowi punkt odniesienia granicy.")
add_occ("Kłębski", "Jan", "Kraśnik", "Woźny sądowy przysięgły (Bedellus)", "Kłębski [?]", 59, "1658", "woźny Jan Kłębski", "Woźny pozywający Żyda Iczka Łobodę", "Składa relację z pozwu.")
add_occ("Łoboda", "Iczek", "Kraśnik", "Żyd kraśnicki", "Łabędź [?]", 59, "1658", "Iczek Łoboda perfid. Jud.", "Pozwany o dług fl 2 gr 20", "Skazany zaocznie na zapłatę fl 2 gr 20.")

# Skan 60
add_occ("Zarzycki", "Wojciech", "Kraśnik (okolice)", "Szlachetny (Nobilis)", "Zakrzewski [?]", 60, "1658", "Nob. Alberti Zarzycki", "Powód przeciw Janowi Klatkowskiemu", "Dochodzi długu i szkód w XI 1658 r.")
add_occ("Klatkowski", "Jan", "Kraśnik", "Mieszczanin", "Klatkowski [?]", 60, "1658", "Joannem Klatkowski", "Pozwany o dług", "Nie stawił się na pozew szl. W. Zarzyckiego.")
add_occ("Zieliński", "Jan", "Kraśnik", "Mieszczanin", None, 60, "1658", "Fam. Joannis Zieliński", "Powód o dług fl 6", "Dochodzi fl 6 od Ewy Marcinowej Jędrzejczyk.")
add_occ("Jędrzejczyk", "Ewa Marcinowa", "Kraśnik", "Mieszkanka / Żona Marcina", "Jędrzejowa [?]", 60, "1658", "Evam Martini Jędrzejczyk", "Pozwana o dług fl 6", "Przyznała dług fl 6 wobec Jana Zielińskiego.")
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Mieszczanin", "Żydkowic", 60, "1658", "Laurentii Żydkowic", "Powód przeciw Andrzejowi Łocie", "Występuje jako Żydkowic i Sydkowic w sprawie o klepki i pobicie żony.")
add_occ("Kurowek", "Mikołaj", "Kraśnik", "Mieszczanin", "Kurowicz [?]", 60, "1658", "Nicolaus Kurowek", "Świadek przysięgły", "Zeznaje przeciw Andrzejowi Łocie o kradzież klepek dębowych.")
add_occ("Zota", "Andrzej", "Kraśnik", "Mieszczanin", "Łota", 60, "1658", "Andream Łota", "Pozwany skazany na gr 20 nawiązki", "Skazany za klepki dębowe i pobicie żony W. Żydkowica.")

# Skan 61
add_occ("Zota", "Andrzej", "Kraśnik", "Mieszczanin", "Łota", 61, "1658", "Andrzej Łota", "Strona dekretu o koszty prawne", "Zobowiązany do zapłaty kosztów sądowych.")
add_occ("Poszłygarczyk", "Stanisław", "Kraśnik", "Mieszczanin", "Soszłygarczyk [?]", 61, "1658", "Stanislai Poszłygarczyk", "Powód (kradzież z kramu i spór o siedlisko)", "Powód w procesie ze świadkami oraz przeciw Jadwidze Kopiance.")
add_occ("Bęben", "Kasper", "Kraśnik", "Świadek przysięgły", "Bęben [?]", 61, "1658", "Caspar Bęben", "Świadek przysięgły", "Zeznaje o kradzieży z budki/kramu i bójce.")
add_occ("Zięba", "Sebastian", "Kraśnik", "Mieszczanin", "Zgęba [?]", 61, "1658", "Sebestianus Zięba", "Świadek przysięgły", "Potwierdza kradzież z kramu Poszłygarczyka.")
add_occ("Sadownik", "Andrzej", "Kraśnik", "Świadek przysięgły", None, 61, "1658", "Andreas Sadownik", "Trzeci świadek przysięgły", "Potwierdza zeznania świadków w sprawie Poszłygarczyka.")
add_occ("Kopianka", "Jadwiga", "Kraśnik", "Mieszkanka", "Kępianka [?] / Kępka [?]", 61, "1658", "Hedvigim Kopianka alias Jachima Kępka", "Pozwana o siedlisko i długi", "Pozwana przez Stanisława Poszłygarczyka.")
add_occ("z Łopacina", "Ewa", "Kraśnik", "Mieszkanka", "Łopacina [?]", 61, "1658", "Fam. Evae de Łopacina", "Powódka o wyderkaf fl 50", "Dochodzi wyderkafu od Macieja Gębalskiego.")
add_occ("Gębalski", "Maciej", "Kraśnik", "Mieszczanin", "Gębalski [?]", 61, "1658", "Mathiam Gębalski", "Pozwany o wyderkaf fl 50", "Pozwany przez Ewę z Łopacina.")

# Skan 62
add_occ("z Łopacina", "Ewa", "Kraśnik", "Mieszkanka", "Łopacina [?]", 62, "1658", "Eadem Actrix", "Powódka o wyderkaf fl 50", "Dochodzi wyderkafu od Tomasza Pełki.")
add_occ("Pełka", "Tomasz", "Kraśnik", "Mieszczanin", None, 62, "1658", "Thomam Pełka", "Pozwany o wyderkaf fl 50", "Pozwany o czynsz wyderkafowy na placu i domu.")
add_occ("Prokopek", "Wawrzyniec", "Kraśnik", "Mieszczanin", None, 62, "1658", "Fam. Laurentii Prokopek", "Składający manifestację", "Manifestuje przeciw zajęciu dóbr po Wojciechu Maruszkowicu.")
add_occ("Gołecki", "Jan", "Kraśnik", "Mieszczanin", None, 62, "1658", "Joannis Gołecki", "Powód i manifestant", "Prowadzi sprawę o obelgi oraz manifestuje przeciw Wdowie Daliborce o fl 1.")
add_occ("Kurowek", "Maciej", "Kraśnik", "Mieszczanin", "Kurowek [?]", 62, "1658", "Mathias Kurowek", "Świadek przysięgły", "Zeznaje w sprawie Jana Gołeckiego.")
add_occ("Daliborka", "[Wdowa]", "Kraśnik", "Wdowa / Mieszkanka", "Zabielska [?]", 62, "1658", "Daliborkę Viduam", "Pozwana w manifestacji o fl 1", "Pozwana przez Jana Gołeckiego o ruchomości i fl 1.")
add_occ("Gębalka", "Marcin", "Kraśnik", "Mieszczanin", "Gębałka [?]", 62, "1658", "Marcin Gębalka", "Pozwany o fl 28 gr 20", "Pozwany przez Augustyna Kurowica.")
add_occ("Kurowic", "Augustyn", "Kraśnik", "Ławnik przysięgły", None, 62, "1658", "Augustyn Kurowic", "Powód o fl 28 gr 20", "Egzekwuje dekret przeciw Marcinowi Gębalce.")
add_occ("Grząbka", "Jan", "Kraśnik", "Mieszczanin", None, 62, "1658", "Fam. Joannis Grząbka", "Powód o komorne fl 5", "Pozywa Bartłomieja Grudnia o fl 5 z komornego i izbę.")
add_occ("Grudzień", "Bartłomiej", "Kraśnik", "Mieszczanin", None, 62, "1658", "Bartholomaeum Grudzień", "Pozwany o komorne fl 5", "Pozwany przez Jana Grząbkę 20 XI 1658 r.")

# Skan 63
add_occ("Grudzień", "Bartłomiej", "Kraśnik", "Mieszczanin", None, 63, "1658", "Bartłomiej Grudzień", "Pozwany zobowiązany do zapłaty", "Dokończenie sprawy z Janem Grząbką.")
add_occ("Dubaj", "Wojciech", "Kraśnik", "Mieszczanin", "Dubański [?]", 63, "1658", "Alberti Dubaj", "Powód o dług fl 24", "Dochodzi długu fl 24 z zapisu na Podwyższenie Krzyża Św. 1658 r.")
add_occ("Klatkowski", "Jan", "Kraśnik", "Mieszczanin", "Klatkowski [?]", 63, "1658", "Joannem Klatkowski", "Pozwany i poręczyciel o fl 24", "Skazany na spłatę długu fl 24 w dwóch ratach.")
add_occ("Słodki", "Walenty", "Kraśnik", "Mieszczanin / Sadownik", "Skutka [?]", 63, "1658", "Valentini Słodki", "Powód o jabłka wiezione do Lublina", "Dochodzi zapłaty za jabłka od Grzegorza Orlaka.")
add_occ("Orlak", "Grzegorz", "Kraśnik", "Mieszczanin / Furman", "Orlik [?]", 63, "1658", "Gregorium Orlak", "Pozwany o rozliczenie za jabłka do Lublina", "Potrącił fl 4 za przewóz do Lublina, ma dopłacić fl 1.")

# Skan 64
add_occ("Noster", "Wojciech", "Rudnik", "Pracowity (Laboriosus)", "Kostka [?]", 64, "1658", "Lab. Alberti Noster de Rudnik", "Powód o 7 korcy żyta i pobicie", "Poddany z Rudnika pozywający Felicjana Konięgę.")
add_occ("Rudnicka", "Jadwiga", "Rudnik", "Mieszkanka Rudnika", "Rudnicki [?]", 64, "1658", "Hedvigis Rudnicki de Rudnik", "Współpowódka z Wojciechem Nosterem", "Współpowódka w sprawie o 7 korcy żyta.")
add_occ("Konięga", "Felicjan", "Kraśnik", "Mieszczanin", "Koniński [?]", 64, "1658", "Felicianum Konięga", "Pozwany o 7 korcy żyta i pobicie", "Sprawa odesłana do inkwizycji 22 XI 1658 r.")
add_occ("Szarek", "Szymon", "Kraśnik (okolice)", "Szlachetny (Nobilis)", None, 64, "1658", "Nob. Simonis Szarek", "Powód o fl 7 i fl 2 z ogrodu", "Dochodzi wykupu ogrodu od Jakuba Zięby.")
add_occ("Zięba", "Jakub", "Kraśnik", "Mieszczanin", "Zgęba [?]", 64, "1658", "Jacobum Zięba", "Pozwany o wykup ogrodu", "Zobowiązany do obrachunku z Szymonem Szarkiem.")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik przysięgły", None, 64, "1658", "Fam. Mathiae Konięga Scab. Iur.", "Powód o wyderkaf fl 50", "Dochodzi czynszu fl 3 gr 15 od Jana Liska.")
add_occ("Lisek", "Jan", "Kraśnik", "Mieszczanin", "Cichy [?]", 64, "1658", "Joannem Lisek", "Pozwany o czynsz fl 3 gr 15", "Dłużnik wyderkafowy Macieja Konięgi.")

# Skan 65
add_occ("Szutka", "Szymon", "Kraśnik", "Mieszczanin", "Sutka [?]", 65, "1658", "Simonis Szutka", "Składający przysięgę na fl 5", "Wykonał przysięgę przeciw Żydowi Ickowi.")
add_occ("Icek", "[Żyd]", "Kraśnik", "Żyd kraśnicki", None, 65, "1658", "Judeum Ickum", "Strona przeciwna przysiędze", "Sprawa z Szymonem Szutką o fl 5.")
add_occ("Tomaszczyk", "Jan", "Kraśnik", "Mieszczanin", None, 65, "1658", "Fam. Joannis Tomaszczyk", "Powód przeciw Maciejowi Kępce", "Sprawa o zapłatę i wydanie fantu z udziałem żony Jadwigi.")
add_occ("Tomaszczykowa", "Jadwiga", "Kraśnik", "Mieszkanka / Żona Jana", None, 65, "1658", "Jadwiga żona", "Uczestniczka sprawy o fant", "Żona Jana Tomaszczyka.")
add_occ("Kępka", "Maciej", "Kraśnik", "Mieszczanin", None, 65, "1658", "Mathiam Kępka", "Pozwany o zapłatę i fant", "Pozwany przez Jana Tomaszczyka.")
add_occ("Słodzarski", "Piotr", "Kraśnik (okolice)", "Szlachetny (Nobilis)", "Zadzarski [?]", 65, "1658", "Nob. Petri Słodzarski", "Składający przysięgę sądową", "Wykonał przysięgę przeciw Maciejowi Prusowi.")
add_occ("Prus", "Maciej", "Kraśnik", "Mieszczanin", "Ptaszek [?]", 65, "1658", "Mathiam Prus", "Strona przeciwna przysiędze", "Sprawa ze szl. Piotrem Słodzarskim.")
add_occ("Serba", "Jakub", "Kraśnik", "Mieszczanin", "Sroka [?]", 65, "1658", "Jacobi Serba", "Składający przysięgę na krucyfiks", "Oczyścił się przysięgą przed Zofią Rębińską.")
add_occ("Rębińska", "Zofia", "Kraśnik", "Mieszkanka", "Łębińska [?]", 65, "1658", "Sophiam Rębińska", "Strona przeciwna przysiędze", "Oskarżała Jakuba Serbę o zabór zboża.")
add_occ("Kaczorowski", "Łukasz", "Kraśnik", "Mieszczanin", "Kaczorowski [?]", 65, "1657", "Łukasz Kaczorowski", "Strona ugody dobrowolnej", "Uczestnik ugody przed Urzędem w sobotę przed św. Katarzyną.")
add_occ("Zieliński", "Krzysztof", "Kraśnik", "Mieszczanin", "Zieliński [?]", 65, "1657", "Krzysztof Zieliński", "Strona ugody dobrowolnej", "Uczestnik ugody przed Urzędem w sobotę przed św. Katarzyną.")

# Skan 66–67
add_occ("Koźmianowa", "Ewa", "Kraśnik", "Wdowa / Mieszkanka", "Koźmiańska [?]", 66, "1657", "Ewa Koźmianowa", "Wystawca oryginalnej plenipotencji", "Podpisała własnoręcznie 9 XI 1657 r. plenipotencję do Trybunału Zamojskiego w sprawie przeciw Grzegorzowi Foxowi po Zofii Kowalowej.")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły", None, 66, "1657", "P. Fox", "Strona przeciwna w Trybunale Zamojskim", "Pozwany przez Ewę Koźmianową o dobra po Zofii Kowalowej.")
add_occ("Kowalowa", "Zofia", "Kraśnik", "Mieszkanka (zm.)", None, 66, "1657", "Nieboszczka Zofia Kowalowa", "Zmarła, której dóbr dotyczy spór", "Spadek po niej jest przedmiotem procesu w Trybunale Zamojskim.")
add_occ("Saraczkowic", "Maciej", "Kraśnik", "Sławetny / Plenipotent", "Saraczkowicz [?]", 66, "1657", "Sławetny P. Maciej Saraczkowic", "Plenipotent Ewy Koźmianowej", "Ustanowiony plenipotentem w Trybunale Zamojskim 9 XI 1657 r.")
add_occ("Koźmianowa", "Ewa", "Kraśnik", "Wdowa / Mieszkanka", "Koźmiańska [?]", 67, "1658", "Ewa Koźmianowa", "Wymieniona w zapisce dorsalnej", "Zapiska o płatnościach na odwrociu plenipotencji.")
add_occ("Gębski", "Jan", "Kraśnik", "Mieszczanin", "Gębski [?]", 67, "1658", "Joannes Gębski", "Powód o fl 30", "Dekret w sprawie o dług fl 30.")

# Skan 68
add_occ("Dubaj", "Wojciech", "Kraśnik", "Mieszczanin", "Albrecht Dubaj", 68, "1658", "Albrechtowi Dubajowi", "Wierzyciel z dekretu na fl 24", "Dokończenie dekretu przeciw Janowi Klatkowskiemu.")
add_occ("Klatkowski", "Jan", "Kraśnik", "Mieszczanin", "Klatkowski [?]", 68, "1658", "Jan Klatkowski", "Dłużnik zobowiązany do spłaty fl 24 w 3 ratach", "Sprawa z Albrechtem Dubajem.")
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Mieszczanin", "Żydkowic", 68, "1658", "Fam. Laurentii Żydkowic", "Poszkodowany w obdukcji ran", "Pobity przez Baltazara Żydkowica i Macieja Konięgę (28 XI 1658).")
add_occ("Żydkowic", "Baltazar", "Kraśnik", "Mieszczanin", "Sydkowic [?]", 68, "1658", "Balthasara Żydkowica", "Sprawca pobicia", "Oskarżony o zadanie ran ciętych Wawrzyńcowi Żydkowicowi.")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik przysięgły", None, 68, "1658", "Mathiae Konięga", "Uczestnik bójki oraz powód o fl 2", "Występuje w obdukcji z 28 XI 1658 oraz jako powód przeciw W. Cichowiczowi 29 XI 1658.")
add_occ("Cichowicz", "Wawrzyniec", "Kraśnik", "Mieszczanin", "Cieśliński [?]", 68, "1658", "Laurentium Cichowicz", "Pozwany o dług fl 2", "Pozwany przez Macieja Konięgę.")
add_occ("Poszłygarczyk", "Stanisław", "Kraśnik", "Mieszczanin", None, 68, "1658", "Fam. Stanislai Poszłygarczyk", "Powód (diligentia)", "Zapisuje diligentiam przeciw Maciejowi Zielińskiemu.")
add_occ("Zieliński", "Maciej", "Kraśnik", "Mieszczanin", None, 68, "1658", "Maciej Zieliński", "Pozwany (niestawiennictwo)", "Nie stawił się na pozew Stanisława Poszłygarczyka i w sprawie o skóry.")

# Skan 69
add_occ("Kępa", "Wawrzyniec", "Kraśnik", "Mieszczanin", "Kępka [?]", 69, "1658", "Laur. Kępa", "Powód o dług i fant", "Pozywa Macieja Ptaszka.")
add_occ("Ptaszek", "Maciej", "Kraśnik", "Mieszczanin", "Pępek [?]", 69, "1658", "Mathiam Ptaszek", "Pozwany o dług i fant", "Pozwany przez Wawrzyńca Kępę.")
add_occ("Sydkowic", "Wawrzyniec", "Kraśnik", "Mieszczanin", "Żydkowic", 69, "1658", "Laurentii Żydkowic", "Powód (dekret na gr 21)", "Uzyskuje nawiązkę gr 21 od Andrzeja Łoty.")
add_occ("Zota", "Andrzej", "Kraśnik", "Mieszczanin", "Łota", 69, "1658", "Andream Łota", "Skazany na gr 21 nawiązki", "Skazany pod rygorem więzienia.")
add_occ("Skutka", "Walenty", "Kraśnik", "Mieszczanin", "Słodki [?]", 69, "1658", "Valentini Skutka", "Składający przysięgę na gr 12", "Przysięga przeciw Jakubowi Bobakowi.")
add_occ("Bobak", "Jakub", "Kraśnik", "Mieszczanin", "Dubak [?]", 69, "1658", "Jacobum Bobak", "Strona przeciwna przysiędze", "Sprawa z Walentym Skutką o gr 12.")
add_occ("Marlik", "Andrzej", "Kraśnik", "Mieszczanin", "Manlik [?]", 69, "1658", "Andream Marlik", "Pozwany o wyderkaf", "Sprawa z Rębińskim [?] o wyderkaf.")
add_occ("Łazarz", "Dawid", "Kraśnik", "Żyd kraśnicki / Świadek", "Dawid Łazarz [?]", 69, "1658", "Judaeus Dawid Łazarz", "Świadek przysięgły", "Zeznaje w sprawie Macieja Zielińskiego o kupno skór.")
add_occ("Zieliński", "Maciej", "Kraśnik", "Mieszczanin", None, 69, "1658", "Mathiae Zieliński", "Strona w sprawie o skóry", "W jego sprawie zeznają Dawid Łazarz i Jan Kurza.")
add_occ("Kurza", "Jan", "Kraśnik", "Mieszczanin", "Kurzawa [?]", 69, "1658", "Joannes Kurza", "Drugi świadek przysięgły", "Zeznaje o koniach i skórach w sprawie M. Zielińskiego.")
add_occ("Lejzor", "[Żyd]", "Kraśnik", "Żyd kraśnicki", "Zelman [?]", 69, "1658", "Judaei Lejzor", "Powód o fl 28", "Pozywa Marcina Kępę o fl 28 z dekretu.")
add_occ("Kępa", "Marcin", "Kraśnik", "Mieszczanin", "Kępa [?]", 69, "1658", "Martinum Kępa", "Pozwany o fl 28", "Pozwany przez Żyda Lejzora.")

# Skan 70–75 (Wielki proces spadkowy ze wsi Blinów)
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Wójt i sędzia zwyczajny przysięgły", "Szafrankowic", 70, "1658", "Fam. D. Albertus Szafrankowic Advocatus", "Przewodniczący Sądu Wielkiego Gajonego", "Przewodniczy sesjom Sądu Wielkiego Gajonego w sprawie wsi Blinów.")
add_occ("Kępski", "Marek", "Kraśnik", "Ławnik przysięgły", "Kępski [?]", 70, "1658", "Fam. Marcus Kępski Scabinus", "Ławnik Sądu Gajonego", "Zasiada w ławie podczas procesu o Blinów.")
add_occ("Kurowic", "Augustyn", "Kraśnik", "Ławnik przysięgły", None, 70, "1658", "Augustinus Kurowic Scabinus", "Ławnik Sądu Gajonego", "Zasiada w ławie podczas procesu o Blinów.")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik przysięgły", None, 70, "1658", "Mathias Konięga Scabinus", "Ławnik Sądu Gajonego", "Zasiada w ławie podczas procesu o Blinów.")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły", None, 70, "1658", "Gregorius Fox Scabinus", "Ławnik Sądu Gajonego", "Zasiada w ławie podczas procesu o Blinów.")
add_occ("Janorowski", "Bartłomiej", "Blinów", "Szlachetny / Dzierżawca wsi Blinów", None, 70, "1658", "Imć P. Bartłomiej Janorowski Dzierżawca Blinowski", "Dzierżawca zezwalający na proces poddanych", "Dzierżawca Blinowa w 1658 r., zezwala poddanym na rozprawę przed sądem kraśnickim.")
add_occ("Staroszek", "Wojciech", "Blinów", "Poddany ze wsi Blinów", "Staszek [?] / Rzepka", 70, "1658", "Wojciech Staroszek", "Powód (mąż Jadwigi z Rzepków)", "Dochodzi spadku po Tomaszu Rzepce w imieniu żony Jadwigi.")
add_occ("Staroszkowa", "Jadwiga", "Blinów", "Poddana ze wsi Blinów (z Rzepków)", None, 70, "1658", "Jadwiga Małżonka Wojciecha Staroszka", "Córka Tomasza Rzepki i Agnieszki, powódka", "Jedna z dwóch córek z pierwszego małżeństwa Tomasza Rzepki.")
add_occ("Łysak", "Maciej", "Blinów", "Poddany ze wsi Blinów", None, 70, "1658", "Maciej Łysak", "Powód (mąż Katarzyny z Rzepków)", "Dochodzi spadku po Tomaszu Rzepce w imieniu żony Katarzyny.")
add_occ("Łysakowa", "Katarzyna", "Blinów", "Poddana ze wsi Blinów (z Rzepków)", None, 70, "1658", "Katarzyna Małżonka Macieja Łysaka", "Córka Tomasza Rzepki i Agnieszki, powódka", "Druga z córek z pierwszego małżeństwa Tomasza Rzepki.")
add_occ("Kozieł", "Stanisław", "Blinów", "Poddany ze wsi Blinów", "Kozieł [?]", 70, "1658", "Stanisław Kozieł", "Pozwany w procesie spadkowym", "Współpozwany w sprawie o dobra po Tomaszu Rzepce.")
add_occ("Rzytka", "Tomasz", "Ślinów", "Poddany (zm.)", "Rzepka [?] / Blinów", 70, "1658", "Nieboszczyk Tomasz Rzepka", "Zmarły gospodarz z Blinowa", "W Partii 3 jednoznacznie identyfikowany jako Tomasz Rzepka ze wsi Blinów (dawniej z Potoka).")
add_occ("Rzepkowa", "Agnieszka", "Blinów", "Poddana (zm., z Potoka)", None, 70, "1658", "Agnieszka pierwsza żona Tomasza Rzepki", "Zmarła matka Jadwigi i Katarzyny", "Przez 40 lat dorabiała się z Tomaszem Rzepką.")
add_occ("Rzepka", "Sebastian", "Blinów", "Poddany ze wsi Blinów", None, 70, "1658", "Sebastian Rzepka", "Syn Tomasza Rzepki", "Uczestnik sporu o spadek po ojcu.")
add_occ("Rzepka", "Jakub", "Blinów", "Poddany ze wsi Blinów", None, 70, "1658", "Jakub Rzepka", "Brat Tomasza Rzepki", "Ojciec Wojciecha Rzepki alias Staroszka.")

# Skan 71
add_occ("Rzytka", "Tomasz", "Ślinów", "Poddany (zm.)", "Rzepka [?] / Blinów", 71, "1658", "Tomasz Rzepka", "Zmarły właściciel inwentarza w Blinowie", "Szczegółowy inwentarz jego zbóż, bydła (14 szt.), koni (8) i owiec (36).")
add_occ("Staroszek", "Wojciech", "Blinów", "Poddany ze wsi Blinów", "Rzepka", 71, "1658", "Pracowity Wojciech Rzepka alias Staroszek", "Powód wzywający świadków", "Powód na sesji 20 XII 1658 r.")
add_occ("Staroszkowa", "Jadwiga", "Blinów", "Poddana ze wsi Blinów", None, 71, "1658", "Jadwiga córka", "Uprawniona do działu", "Wzmiankowana przy podziale po kop 30.")
add_occ("Łysakowa", "Katarzyna", "Blinów", "Poddana ze wsi Blinów", None, 71, "1658", "Katarzyna córka", "Uprawniona do działu", "Wzmiankowana przy podziale po kop 30.")

# Skan 72
add_occ("Skórka", "Jan", "Blinów", "Poddany ze wsi Blinów", "Storka [?]", 72, "1658", "Lab. Jan Skórka", "1. świadek przysięgły z Blinowa", "Zeznaje o pierwszej żonie Agnieszce i pochodzeniu Wojciecha Rzepki.")
add_occ("Rzepka", "Paweł", "Blinów", "Poddany ze wsi Blinów", None, 72, "1658", "Lab. Paulus Rzepka", "2. świadek przysięgły z Blinowa", "Zeznaje o braku testamentu i woli Tomasza Rzepki co do córek.")
add_occ("Rzepka", "Jan", "Blinów", "Poddany ze wsi Blinów", None, 72, "1658", "Lab. Joannes Rzepka", "3. świadek przysięgły z Blinowa", "Potwierdza, że Wojciech Rzepka jest synem Jakuba Rzepki.")
add_occ("Grątka", "Andrzej", "Blinów", "Poddany ze wsi Blinów", "Gręta [?]", 72, "1658", "Lab. Andreas Grątka", "4. świadek przysięgły z Blinowa", "Potwierdza zeznania poprzednich świadków.")

# Skan 73
add_occ("Szafraniec", "Wojciech", "Kraśnik", "Wójt i sędzia zwyczajny przysięgły", "Szafrankowic", 73, "1658", "Fam. D. Albertus Szafrankowic", "Przewodniczący Sądu Gajonego", "Przewodniczy sesji z końca 1658 r.")
add_occ("Kępski", "Marek", "Kraśnik", "Ławnik przysięgły", "Kępski [?]", 73, "1658", "Marcus Kępski", "Ławnik Sądu Gajonego", "Zasiada w ławie.")
add_occ("Kurowic", "Augustyn", "Kraśnik", "Ławnik przysięgły", None, 73, "1658", "Augustinus Kurowic", "Ławnik Sądu Gajonego", "Zasiada w ławie.")
add_occ("Szwedowicz", "Stanisław", "Kraśnik", "Ławnik przysięgły", "Szwedowicz [?]", 73, "1658", "Stanislaus Szwedowicz", "Ławnik Sądu Gajonego", "Nowo odnotowany ławnik kraśnicki w grudniu 1658 r.")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik przysięgły", None, 73, "1658", "Mathias Konięga", "Ławnik Sądu Gajonego", "Zasiada w ławie.")
add_occ("Fox", "Grzegorz", "Kraśnik", "Ławnik przysięgły", None, 73, "1658", "Gregorius Fox", "Ławnik Sądu Gajonego", "Zasiada w ławie.")
add_occ("Janorowski", "Bartłomiej", "Blinów", "Szlachetny / Dzierżawca wsi Blinów", None, 73, "1658", "Nob. D. Bartholomaeus Janorowski", "Autor manifestacji (podpis mpp)", "Wnosi manifestację o dobra po T. Rzepce z datą 19 X 1658 r.")
add_occ("Staroszek", "Wojciech", "Blinów", "Poddany ze wsi Blinów", None, 73, "1658", "Wojciech Staroszek", "Składający replikę", "Składa replikę przeciw Katarzynie Rzepkowej.")
add_occ("Łysak", "Maciej", "Blinów", "Poddany ze wsi Blinów", None, 73, "1658", "Maciej Łysak", "Składający replikę", "Składa replikę przeciw Katarzynie Rzepkowej.")
add_occ("Sosnowska", "Katarzyna", "Ślinów", "Poddana / Wdowa po T. Rzepce", "Rzepkowa / Blinów", 73, "1658", "Katarzyna Rzepkowa", "Pozwana w replice spadkowej", "Wdowa po Tomaszu Rzepce ze wsi Blinów.")
add_occ("Zakrzewski", "[J.W. Pan]", "Kraśnik (okolice)", "Wielmożny Pan / Sędzia lub Urzędnik", "Zakrzewski [?]", 73, "1658", "J.W. P. Zakrzewski", "Wystawca wcześniejszego dekretu", "Wspomniany przy dekrecie o 7 sztuk bydła, fl 200 i fl 500.")

# Skan 74
add_occ("Sosnowska", "Katarzyna", "Ślinów", "Poddana / Wdowa po T. Rzepce", "Rzepkowa / Blinów", 74, "1658", "Lab. Catharina Rzepkowa", "Składająca Regestr Uznania i wzywająca świadków", "Przedkłada wykaz majątku i powołuje świadków ze wsi Blinów.")
add_occ("Rzytka", "Tomasz", "Ślinów", "Poddany (zm.)", "Rzepka [?] / Blinów", 74, "1658", "Tomasz Rzepka", "Zmarły mąż Katarzyny Rzepkowej", "Rozporządzał majątkiem w obecności sąsiadów z Blinowa.")
add_occ("Kondlik", "Stefan", "Ślinów", "Poddany ze wsi Blinów", "Kondla / Blinów", 74, "1658", "Stefan Kondla", "Świadek ostatniej woli T. Rzepki", "Obecny przy śmierci Tomasza Rzepki jako sąsiad z Blinowa.")
add_occ("Kondlik", "Andrzej", "Ślinów", "Poddany ze wsi Blinów (z karczmy)", "Kondla / Blinów", 74, "1658", "Andrzej Kondla z karczmy", "Świadek ostatniej woli T. Rzepki", "Brat Stefana Kondli, z karczmy w Blinowie.")
add_occ("Rzepka", "Stanisław", "Blinów", "Poddany ze wsi Blinów", None, 74, "1658", "Lab. Stanisław Rzepka", "1. świadek przysięgły Katarzyny Rzepkowej", "Zeznaje o chorobie i ostatniej woli Tomasza Rzepki.")
add_occ("Karpiński", "Jan", "Ślinów", "Poddany ze wsi Blinów", "Blinów", 74, "1658", "Jan Karpiński", "Obecny przy łożu T. Rzepki", "Wspomniany w zeznaniach Stanisława Rzepki.")

# Skan 75
add_occ("Rzepka", "Stanisław", "Blinów", "Poddany ze wsi Blinów", None, 75, "1658", "Stanisław Rzepka", "1. świadek przysięgły", "Dokończenie zeznań o opiece nad wdową Katarzyną.")
add_occ("Karpiński", "Jan", "Ślinów", "Poddany ze wsi Blinów", "Blinów", 75, "1658", "Lab. Joannes Karpiński", "2. świadek przysięgły z Blinowa", "Zeznaje o spotkaniu w drodze do Budzynia i rozmowach z Tomaszem Rzepką.")
add_occ("Kondlik", "Stefan", "Ślinów", "Poddany ze wsi Blinów", "Kondla / Blinów", 75, "1658", "Lab. Stephanus Kondla", "3. świadek przysięgły z Blinowa", "Potwierdza obecność przy śmierci Tomasza Rzepki i jego rozporządzenia.")
add_occ("Kondlik", "Andrzej", "Ślinów", "Poddany ze wsi Blinów (z karczmy)", "Kondla / Blinów", 75, "1658", "Andrzej Kondla", "Wspomniany brat Stefana Kondli", "Wspomniany w zeznaniach z Blinowa.")

# Zapis gen_data_j20_part3.json
with open('/home/ubuntu/workspace/Gen/gen_data_j20_part3.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j20_part3.json ({len(gen_data)} profili) oraz CSV.")
