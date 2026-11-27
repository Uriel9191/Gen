# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part3.json', 'r', encoding='utf-8') as f:
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

# === PARTIA 4 (SKANY 76–100) ===
# Skany 76–81 (Finał procesu spadkowego ze wsi Blinów, 1658)
add_occ("Kondlik", "Stefan", "Ślinów", "Poddany ze wsi Blinów", "Kondla / Blinów", 76, "1658", "Stefan Kondla", "Świadek w procesie blinowskim", "Występuje w końcowych zeznaniach i replikach procesu spadkowego po T. Rzepce.")
add_occ("Rzytka", "Tomasz", "Ślinów", "Poddany (zm.)", "Rzepka [?] / Blinów", 76, "1658", "Tomasz Rzepka", "Zmarły gospodarz z Blinowa", "Przedmiot rozliczeń spadkowych.")
add_occ("Sosnowska", "Katarzyna", "Ślinów", "Poddana / Wdowa po T. Rzepce", "Rzepkowa / Blinów", 76, "1658", "Katarzyna Rzepkowa", "Pozwana wdowa", "Spór o dział spadkowy z córkami Tomasza Rzepki.")
add_occ("Rzepka", "Sebastian", "Blinów", "Poddany ze wsi Blinów", None, 76, "1658", "Sebastian Rzepka", "Syn Tomasza Rzepki", "Wymieniony w rejestrze z Blinowa.")

add_occ("Świderski", "Jan", "Kraśnik (okolice)", "Szlachetny / Sędzia komisaryjny", None, 77, "1658", "J.P. Jan Świderski mpp", "Wystawca wcześniejszego dekretu z 8 III 1658 r.", "Potwierdza ugodę dóbr blinowskich własnoręcznym podpisem.")
add_occ("Rzepka", "Jan", "Blinów", "Wójt blinowski / Poddany", None, 77, "1658", "Jan Rzepka wójt Blinowski", "Wójt wsi Blinów i świadek", "Podpisany w ugodzie przed J.P. Świderskim.")
add_occ("Reszka", "Łukasz", "Blinów", "Poddany ze wsi Blinów", None, 77, "1658", "Łukasz Reszka", "Świadek ugody blinowskiej", "Świadek przy ugodzie dóbr Rzepków.")
add_occ("Reszka", "Stanisław", "Blinów", "Poddany ze wsi Blinów", None, 77, "1658", "Stanisław Reszka", "Świadek ugody blinowskiej", "Świadek przy ugodzie dóbr Rzepków.")
add_occ("Rzepka", "Andrzej", "Blinów", "Poddany ze wsi Blinów", None, 77, "1658", "Andrzej Rzepka", "Świadek ugody blinowskiej", "Świadek z rodziny Rzepków.")
add_occ("Brożek", "Paweł", "Blinów", "Poddany ze wsi Blinów", None, 77, "1658", "Paweł Brożek", "Świadek ugody blinowskiej", "Świadek w procesie blinowskim.")
add_occ("Karpiński", "Jan", "Ślinów", "Poddany ze wsi Blinów", "Blinów", 77, "1658", "Jan [Stanisław] Karpiński", "Świadek ugody blinowskiej", "Świadek z Blinowa.")
add_occ("Kłos", "Mateusz", "Blinów", "Poddany ze wsi Blinów", None, 77, "1658", "Mateusz Kłos", "Świadek ugody blinowskiej", "Świadek z Blinowa.")
add_occ("Wacławic", "Antoni", "Kraśnik", "Urzędnik / Pisarz sądowy", "Wacławic [?]", 77, "1658", "A. Antoni Wacławic mpp", "Podpisujący zatwierdzenie dekretu", "Podpisuje wpis zatwierdzający ugodę z 1658 r.")

add_occ("Kłos", "Wojciech", "Blinów", "Poddany ze wsi Blinów", "Kłos [?]", 78, "1658", "Wojciech Kłos Blinowski", "Wzmiankowany przy rozliczeniu", "Wspomniany w aktach blinowskich z 1658 r.")
add_occ("Sasek", "Sebastian", "Blinów", "Poddany ze wsi Blinów", "Sasek [?]", 78, "1658", "Sebastian Sasek", "Wzmiankowany uczestnik sprawy", "Wzmiankowany po śmierci T. Rzepki.")
add_occ("Kondlik", "Andrzej", "Ślinów", "Poddany ze wsi Blinów", "Kondla / Blinów", 78, "1658", "Andrzej Kondla mpp", "Świadek z własnoręcznym podpisem", "Podpisuje zeznanie o majątku w Blinowie.")
add_occ("Janorowski", "Bartłomiej", "Blinów", "Szlachetny / Dzierżawca wsi Blinów", None, 78, "1658", "J.M.P. Janorowski", "Dzierżawca Blinowa", "Wymieniony w replice z 14 X 1658 r.")
add_occ("Gieracki", "Piotr", "Blinów (okolice)", "Wierzyciel / Posiadacz sumy", None, 78, "1658", "Piotr Gieracki", "Dłużnik z sumy fl 130", "Przechowuje/winien fl 130 z majątku blinowskiego.")

add_occ("Staroszek", "Wojciech", "Blinów", "Poddany ze wsi Blinów", "Rzepka", 79, "1658", "Wojciech Rzepka alias Staroszek", "Powód uzyskujący dekret", "Wygrywa dział spadkowy dla żony Jadwigi.")
add_occ("Staroszkowa", "Jadwiga", "Blinów", "Poddana ze wsi Blinów", None, 79, "1658", "Jadwiga córka", "Uprawniona do działu spadkowego", "Uzyskuje dział po matce Agnieszce i ojcu Tomaszu Rzepce.")
add_occ("Łysak", "Maciej", "Blinów", "Poddany ze wsi Blinów", None, 79, "1658", "Maciej Łysak", "Współpowód uzyskujący dekret", "Wygrywa dział spadkowy dla żony Katarzyny.")
add_occ("Łysakowa", "Katarzyna", "Blinów", "Poddana ze wsi Blinów", None, 79, "1658", "Katarzyna córka", "Uprawniona do działu spadkowego", "Uzyskuje dział po matce Agnieszce i ojcu Tomaszu Rzepce.")

add_occ("Rzytka", "Tomasz", "Ślinów", "Poddany (zm.)", "Rzepka [?] / Blinów", 80, "1658", "Tomasz Rzepka", "Zmarły spadkodawca", "Dekret rozdziela fl 130 i po fl 17 dla córek.")
add_occ("Janorowski", "Bartłomiej", "Blinów", "Szlachetny / Dzierżawca wsi Blinów", None, 80, "1658", "J.P. Bartłomiej Janorowski", "Dzierżawca egzekwujący dekret", "Zabezpieczono jego prawa dworskie w dekrecie.")

add_occ("Zieliński", "Paweł", "Kraśnik", "Mieszczanin", "Zieliński [?]", 81, "1658", "Paweł Zieliński", "Dłużnik zbożowy i pieniężny", "Wspomniany przy egzekucji 12 korcy żyta i fl 15.")
add_occ("Reszka", "Stanisław", "Blinów", "Poddany ze wsi Blinów", None, 81, "1658", "Stanisław Reszka", "Dłużnik z dekretu", "Zobowiązany do zwrotu 12 korcy żyta.")

# Skany 82–83 (1668)
add_occ("Kłopot", "Andrzej", "Kraśnik", "Przedmieszczanin", "Kłopot", 82, "1668", "Brat mój Andrzej [Kłopot]", "Znalazca czerwonego rękawika tureckiego", "Znalazł rękawik i oddał go Żydowi Markowi, co wywołało awanturę jarmarczną.")
add_occ("Marek", "[Żyd]", "Kraśnik", "Żyd kraśnicki", None, 82, "1668", "Żyd Marek", "Odbiorca znalezionego rękawika", "Przechowywał rękawik znaleziony przez Andrzeja.")
add_occ("Mamel", "[Żyd]", "Kraśnik", "Żyd kraśnicki", "Mamele", 82, "1668", "Niewierny Mamel Żyd Kraśnicki", "Pozwany w protestacji o pobicie na jarmarku", "Oskarżony o napad i pobicie na rynku podczas jarmarku w 1668 r.")
add_occ("Kanaszkowic", "[Szewc]", "Kraśnik", "Szewc (Sutor)", "Kanaszek", 82, "1668", "Hon. Kanaszek Sutores", "Powód o areszt na towary i kontusz", "Szewc kraśnicki pozywający w sprawie o sukno i kontusz z Turobina.")
add_occ("Krasnodębski", "Jakub", "Urzędów", "Szlachetny / Mieszczanin z Urzędowa", None, 82, "1668", "Jacobus Krasnodębski de Urzędów", "Świadek w sprawie o kontusz i sukno", "Zeznaje o kontuszu darowanym przez wuja Michała Cębalskiego.")
add_occ("Kramarz", "Iwan", "Kraśnik", "Kramarz / Przyjezdny", "Jan Kramarz", 82, "1668", "Iwan Kramarz", "Właściciel aresztowanych towarów", "Jego towary stoją u P. Bombińskiego.")
add_occ("Bombiński", "[Pan]", "Kraśnik", "Gospodarz / Mieszczanin", "Bombiński [?]", 82, "1668", "P. Bombiński", "Przechowujący towary Kramarza", "U niego złożono aresztowane towary.")
add_occ("Panownik", "Jakub", "Kraśnik", "Mieszczanin", None, 82, "1668", "Jakub Panownik", "Wspomniany dostawca sukna", "Dał sukno w sprawie Kanaszka.")
add_occ("Cębalski", "Michał", "Urzędów", "Wuj Jakuba Krasnodębskiego", None, 82, "1668", "P. Michał Cębalski", "Darujący kontusz", "Wuj Jakuba Krasnodębskiego.")

add_occ("Krasnodębski", "Jakub", "Urzędów", "Szlachetny / Mieszczanin z Urzędowa", None, 83, "1668", "Jakub Krasnodębski", "Świadek o szyciu kontusza w Turobinie", "Dokończenie zeznań o krawcu turobińskim i Franciszkowskim.")
add_occ("Mamel", "[Żyd]", "Kraśnik", "Żyd kraśnicki", "Mamele", 83, "1668", "Infidus Mamele", "Powód w sesji z 11 I 1668 r.", "Pozywa Kłopota o pobicie na jarmarku.")
add_occ("Kłopot", "[Mieszczanin]", "Kraśnik", "Przedmieszczanin", None, 83, "1668", "H. Kłopot Cit.", "Pozwany w procesie z Żydem Mamelem", "Zobowiązany do oczyszczenia się z 2 świadkami w piątek.")

# Skany 84–85 (1666)
add_occ("Dubitowa", "Anna", "Kraśnik", "Mieszczanka (3. żona Macieja Dubita)", "Tuszyńska", 84, "1666", "Honesta Anna Mathiae Dubito Consors", "Kwitująca sumę 100 fl", "20 XII 1666 r. kwituje Macieja Konięgę z sumy 100 złp.")
add_occ("Dubit", "Maciej", "Kraśnik", "Mieszczanin", "Dubito", 84, "1666", "Honesti Mathiae Dubito Civis Crasn.", "Chory mąż Anny Dubitowej", "W czasie choroby zastępuje go ławnik Wojciech Kurowic.")
add_occ("Kurowic", "Wojciech", "Kraśnik", "Ławnik przysięgły", "Kurowicz", 84, "1666", "Fam. Albertus Kurowicz Scabinus Juratus", "Opiekun prawny Anny Dubitowej", "Asystuje Annie Dubitowej i jej synowi Wojciechowi 20 XII 1666 r.")
add_occ("Tuszyński", "Wojciech", "Kraśnik", "Mieszczanin (syn Mikołaja)", None, 84, "1666", "Albertus filius olim Nicolai Tuszyński", "Współkwitujący sumę 100 fl", "Syn z pierwszego małżeństwa Anny Dubitowej.")
add_occ("Tuszyński", "Mikołaj", "Kraśnik", "Mieszczanin (zm.)", None, 84, "1666", "olim Nicolaus Tuszyński", "Zmarły pierwszy mąż Anny", "Ojciec Wojciecha Tuszyńskiego.")
add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik przysięgły", None, 84, "1666", "Honestus Mathias Konięga", "Kwitowany z sumy 100 złp", "Otrzymuje kwitację z sumy zapisanej w wigilię św. Andrzeja 1666 r.")
add_occ("Konięgowa", "Krystyna", "Kraśnik", "Mieszczanka / Żona Macieja", None, 84, "1666", "Christina Coniux", "Współkwitowana z sumy 100 złp", "Żona Macieja Konięgi.")

add_occ("Konięga", "Maciej", "Kraśnik", "Ławnik przysięgły", None, 85, "1666", "Famati Mathiae Konięga", "Kwitowany z sumy 100 złp", "Dokończenie kwitacji z 20 XII 1666 r.")
add_occ("Jastrzębski", "Ludwik", "Kraśnik", "Ks. Doktor Teologii / Prepozyt Kanoników Regularnych", "Jastrzenski [?]", 85, "1666", "Adm. Rndus D. Ludovicus Jastrzenski S.Th.D. Praepositus Crasn.", "Wypłacający sumę 100 złp", "Wypłacił w imieniu Konwentu Kanoników Regularnych 100 złp.")
add_occ("Grot", "Franciszek Antoni", "Kraśnik", "Notariusz przysięgły publiczny", None, 85, "1666", "Franciscus Ant. Grot Notarius Iuratus mpp", "Notariusz uwierzytelniający ekstrakt", "Wypisał i podpisał ekstrakt z protokołów.")

# Skany 86–87 (1668)
add_occ("Węgorzowic", "Andrzej", "Kraśnik", "Były mieszczanin / Pensjonariusz szpitala Św. Ducha", "Węgorzowich", 86, "1668", "Węgorzowich przedtym Mieszczanin", "Testator zapisujący fl 50 na szpital", "Zapisuje fl 50 ze swojej ojcowizny na szpital Św. Ducha oraz resztę wnuczętom.")
add_occ("Macal", "Andrzej", "Kraśnik", "Mieszczanin", None, 86, "1668", "Ucciwy Andrzej Macal", "Dłużnik Andrzeja Węgorzowica na fl 50", "Winien fl 50 z ojcowizny.")
add_occ("Kilianek", "Grzegorz", "Kraśnik", "Mieszczanin", None, 86, "1668", "Grzegorz Kilianek", "Ojciec wnucząt Węgorzowica", "Jego dzieci i żona/córka Maryna są spadkobiercami Węgorzowica.")
add_occ("Kilianka", "Maryna", "Kraśnik", "Wnuczka Andrzeja Węgorzowica", None, 86, "1668", "Maryna Grzegorzowa Kilianka", "Spadkobierczyni A. Węgorzowica", "Wymieniona imiennie w dyspozycji szpitalnej.")
add_occ("Kownicki", "Maciej", "Kraśnik", "Mieszczanin", "Kownicki [?]", 86, "1668", "Maciej Kownicki", "Ojciec wnucząt Węgorzowica", "Jego dzieci są spadkobiercami Węgorzowica.")
add_occ("Jasiemicki", "[Mieszczanin]", "Kraśnik", "Mieszczanin", "Jasiemicki [?]", 86, "1668", "Jasiemicki Cit.", "Pozwany przez plenipotenta ks. Proboszcza", "Sprawa z 23 III 1668 r. o zboże winiarza.")

add_occ("Sitarski", "Marcin", "Kraśnik", "Rajca miejski", None, 87, "1668", "Famatus Martinus Sitarski", "Skazany zaocznie (contumax)", "Skazany na kontumację z powództwa Żyda Andzela w 1668 r.")
add_occ("Andzel", "[Żyd]", "Kraśnik", "Żyd kraśnicki", None, 87, "1668", "Infidelis Judaeus Andzel", "Powód przeciw Marcinowi Sitarskiemu", "Uzyskał wyrok zaoczny przeciw Sitarskiemu.")

# Skany 88–89 (1681)
add_occ("Pieliński", "Maciej", "Kraśnik", "Mieszczanin", "Pielinkowicz [?]", 88, "1681", "Hon. Mathiam Pieliński", "Powód o areszt na konia", "Procesuje się w 1681 r. z Sebastianem Skarżeńskim.")
add_occ("Skarżeński", "Sebastian", "Kraśnik", "Mieszczanin", "Skarzeński [?]", 88, "1681", "Hon. Sebastianum Skarżeński", "Pozwany o zajęcie konia na szkodzie", "Spór przed sądem w 1681 r.")
add_occ("Gorajski", "[Żyd]", "Kraśnik", "Żyd / Obywatel kraśnicki", "Gorayski", 88, "1681", "Niewierny Żyd Gorayski Obywatel Kraśn.", "Składający relację pod przysięgą", "Wycenił trawę na fl 2 i siano na fl 10 (3 III 1681).")
add_occ("Puonik", "Maciej", "Kraśnik", "Mieszczanin", "Płonik [?]", 88, "1681", "Mathiam Puonik", "Powód o trawę i szkody", "Dochodzi fl 10 i fl 15 od Wojciecha Progutki.")
add_occ("Progutka", "Wojciech", "Kraśnik", "Mieszczanin", "Pogutka [?]", 88, "1681", "Albertum Progutka", "Pozwany o skoszenie trawy", "Skazany na zapłatę fl 10 i fl 15.")

add_occ("Sienka", "Mikołaj", "Kraśnik", "Mieszczanin (przyjmujący prawo miejskie)", "Sienka [?]", 89, "1681", "Nicolaus Sienka", "Składający przysięgę na prawo miejskie", "Przyjął prawo miejskie 11 III 1681 r.")
add_occ("Kłopotek", "Paweł", "Kraśnik", "Mieszczanin (przyjmujący prawo miejskie)", "Kłopot", 89, "1681", "Paulus Kłopotek", "Składający przysięgę na prawo miejskie", "Przyjął prawo miejskie 11 III 1681 r.")
add_occ("Kłopotek", "Jan", "Kraśnik", "Mieszczanin (przyjmujący prawo miejskie)", "Kłopot", 89, "1681", "Joannes Kłopotek", "Składający przysięgę na prawo miejskie", "Przyjął prawo miejskie 11 III 1681 r.")
add_occ("Wojtek", "Grzegorz", "Kraśnik", "Mieszczanin (przyjmujący prawo miejskie)", None, 89, "1681", "Gregorius Wojtek", "Składający przysięgę na prawo miejskie", "Przyjął prawo miejskie 11 III 1681 r.")
add_occ("Kołodziej", "Mikołaj", "Kraśnik", "Mieszczanin", "Kołodziej [?]", 89, "1681", "Hon. Nicolaum Kołodziej", "Powód o potwarz", "Procesuje się z Tomaszem Kochanowskim w 1681 r.")
add_occ("Kochanowski", "Tomasz", "Kraśnik", "Mieszczanin", None, 89, "1681", "Hon. Thomam Kochanowski", "Pozwany skazany na przeprosiny", "Skazany na przeprosiny i koszty prawne.")
add_occ("Piotrowski", "Michał", "Kraśnik", "Mieszczanin (przyjmujący prawo miejskie)", None, 89, "1681", "Michael Piotrowski", "Składający przysięgę na prawo miejskie", "Przyjął prawo miejskie 18 III 1681 r.")
add_occ("Kantorek", "Andrzej", "Kraśnik", "Mieszczanin (przyjmujący prawo miejskie)", None, 89, "1681", "Andreas Kantorek", "Składający przysięgę na prawo miejskie", "Przyjął prawo miejskie 18 III 1681 r.")
add_occ("Moszkowa", "[Żydówka]", "Kraśnik", "Żydówka kraśnicka", None, 89, "1681", "Niewierna Żydówka Moszkowa", "Zgłaszająca areszt sądowy", "Położyła areszt na wyprzedaż towarów 18 III 1681 r.")
add_occ("Zbrończyk", "Mikołaj", "Kraśnik", "Mieszczanin (przyjmujący prawo miejskie)", None, 89, "1681", "Nicolaus Zbrończyk", "Składający przysięgę na prawo miejskie", "Przyjął prawo miejskie 18 III 1681 r.")
add_occ("Masłowski", "Sebastian", "Kraśnik", "Świadek przysięgły", None, 89, "1681", "Sebastianus Masłowski", "Świadek w sprawie S. Furmana", "Zeznaje w 1681 r.")
add_occ("Furman", "Sebastian", "Zagórze", "Mieszkaniec Zagórza", None, 89, "1681", "Sebastian Furman z Zagórza", "Strona procesowa", "W jego sprawie zeznaje Sebastian Masłowski.")

# Skany 91–93 (1683 — Karta tytułowa i elekcja pisarza)
add_occ("Zamoyski", "Marcin", "Zamość / Kraśnik", "Ordynat Zamoyski / Wojewoda lubelski i bełski", None, 91, "1683", "Ill. D. Martinus in Zamoscie Zamoyski", "Dziedzic i ordynat kraśnicki", "Wymieniony na stronie tytułowej księgi z 1683 r.")
add_occ("Zamoyska", "Dorota z Leszczkowa", "Zamość / Kraśnik", "Kasztelanowa kijowska / Pani dożywotnia Kraśnika", None, 91, "1683", "Ill. Dna Dorothea de Lesczkow Zamoyska", "Posiadaczka dożywotnia miasta", "Wymieniona na karcie tytułowej księgi z 1683 r.")
add_occ("Rogalowski", "Jan", "Kraśnik", "Patrycjusz i Notariusz przysięgły (Pisarz miejski)", None, 91, "1683", "Joannes Rogalowski Patritius et Notarius Iuratus", "Twórca i pisarz księgi z 1683 r.", "Wybrany na pisarza miejskiego 23 IV 1683 r.")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki", None, 91, "1683", "Spectabilis D. Ubaldus Florianus Janaszkowicz Advocatus", "Wójt kraśnicki w 1683 r.", "Urząd wójtowski w 1683 r. odbywa się pod jego przewodnictwem.")

add_occ("Skrzeszowski", "Jakub", "Kraśnik", "Szlachetny / Administrator dóbr kraśnickich", None, 92, "1683", "Gen. D. Jacobus Skrzeszowski Administrator", "Administrator uczestniczący w elekcji pisarza", "Obecny przy elekcji Jana Rogalowskiego 23 IV 1683 r.")
add_occ("Janaszkowicz", "Ubald Florian", "Kraśnik", "Wójt kraśnicki", None, 92, "1683", "Ubaldus Florianus Janaszkowicz Advocatus", "Wójt i gospodarz posiedzenia elekcyjnego", "Elekcja odbywa się w jego domu.")
add_occ("Gomuza", "Stanisław", "Kraśnik", "Burmistrz kraśnicki (Proconsul)", None, 92, "1683", "Fam. Stanislaus Gomuza Proconsul", "Burmistrz w 1683 r.", "Uczestnik elekcji pisarza miejskiego.")
add_occ("Chmarowicz", "Paweł", "Kraśnik", "Rajca urzędujący", None, 92, "1683", "Paulus Chmarowicz Praesidens", "Rajca w 1683 r.", "Uczestnik elekcji pisarza.")
add_occ("Chmielanowski", "Jakub", "Kraśnik", "Rajca urzędujący", None, 92, "1683", "Jacobus Chmielanowski Praesidens", "Rajca w 1683 r.", "Uczestnik elekcji pisarza.")
add_occ("Błaszkowicz", "Maciej", "Kraśnik", "Rajca urzędujący", None, 92, "1683", "Mathias Błaszkowicz Praesidens", "Rajca w 1683 r.", "Uczestnik elekcji pisarza.")
add_occ("Sitarski", "Marcin", "Kraśnik", "Stary rajca (Antiquus Consul)", None, 92, "1683", "Martinus Sitarski Antiquus Consul", "Stary rajca w 1683 r.", "Uczestnik elekcji pisarza (wcześniej rajca w latach 1656–1668).")
add_occ("Barankowicz", "Jan", "Kraśnik", "Stary rajca (Antiquus Consul)", None, 92, "1683", "Joannes Barankowicz Antiquus Consul", "Stary rajca w 1683 r.", "Uczestnik elekcji pisarza.")
add_occ("Stankowski", "Paweł", "Kraśnik", "Podwójci (Viceadvocatus)", None, 92, "1683", "Paulus Stankowski Viceadvocatus", "Podwójci w 1683 r.", "Uczestnik elekcji pisarza i przewodniczący posiedzeń.")
add_occ("Banaszowicz", "Sebastian", "Kraśnik", "Ławnik przysięgły", None, 92, "1683", "Sebastianus Banaszowicz Scabinus", "Ławnik w 1683 r.", "Uczestnik elekcji pisarza.")
add_occ("Gomuza", "Jan", "Kraśnik", "Ławnik przysięgły", None, 92, "1683", "Joannes Gomuza Scabinus", "Ławnik w 1683 r.", "Uczestnik elekcji pisarza.")
add_occ("Kanaszkowicz", "Wojciech", "Kraśnik", "Ławnik przysięgły", None, 92, "1683", "Albertus Kanaszkowicz Scabinus", "Ławnik w 1683 r.", "Uczestnik elekcji pisarza.")
add_occ("Mucda", "Dawid", "Kraśnik", "Starszy kahału żydowskiego (Senior)", None, 92, "1683", "David Mucda Judaeus Senior", "Starszy kahału przy elekcji pisarza", "Reprezentuje gminę żydowską przy wyborze Jana Rogalowskiego.")
add_occ("Achiaszowicz", "Lejzor", "Kraśnik", "Starszy kahału żydowskiego (Senior)", None, 92, "1683", "Leyzor Achiaszowicz Judaeus Senior", "Starszy kahału przy elekcji pisarza", "Reprezentuje gminę żydowską przy wyborze Jana Rogalowskiego.")
add_occ("Jozwowicz", "Mojżesz Majer", "Kraśnik", "Syndyk / Szkolnik kahału żydowskiego", None, 92, "1683", "Moyzes Maior Jozwowicz Syndicus alias Szkolnik", "Syndyk i szkolnik synagogi kraśnickiej", "Reprezentuje kahał przy elekcji pisarza 23 IV 1683 r.")
add_occ("Rogalowski", "Jan", "Kraśnik", "Patrycjusz i Notariusz przysięgły (Pisarz miejski)", None, 92, "1683", "Honoratus Joannes Rogalowski", "Wybrany jednogłośnie na pisarza", "Obejmuje urząd pisarza miejskiego 23 IV 1683 r.")
add_occ("Zamoyska", "Dorota z Leszczkowa", "Zamość / Kraśnik", "Kasztelanowa kijowska", None, 92, "1683", "Dorothea Zamoyska Castellanissa Kiioviensis", "Wyrażająca zgodę na elekcję", "Zatwierdza elekcję pisarza.")

# Skany 93–99 (Proces Stanisława Nawrockiego przeciw Jakubowi Wardędze, 1683)
add_occ("Rogalowski", "Jan", "Kraśnik", "Notariusz przysięgły", None, 93, "1683", "Joannes Rogalowski", "Składający przysięgę pisarską", "Zaprzysiężony jako pisarz miejski.")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Były burmistrz i stary rajca (Consul antiquus)", None, 93, "1683", "Fam. Stanislaus Nawrocki consul antiquus", "Powód przeciw Jakubowi Wardędze", "Wnosi 28 IV 1683 r. obszerną skargę na Jakuba Wardęgę z Dzierzkowic.")
add_occ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany (dawniej mieszczanin kraśnicki)", None, 93, "1683", "Hon. Jacobus Wardęga Anteoppidanus", "Pozwany o ucieczkę ze składek i zabór koni", "Uciekł przed podatkami z Kraśnika do Dzierzkowic, potem na Budzyń.")
add_occ("Zamoyski", "Jan", "Zamość / Kraśnik", "Ordynat Zamoyski (zm.)", None, 93, "1683", "J.W. J.M. Pan Ordynat", "Wspomniany dawny dziedzic", "Za jego czasów trwały ciężkie kontrybucje.")
add_occ("Zamoyska", "Dorota z Leszczkowa", "Zamość / Kraśnik", "Kasztelanowa kijowska", None, 93, "1683", "Jaśnie Wielmożna Pani Kasztelanowa Kiiowska", "Odsyłająca sprawę do sądu wójtowskiego", "Odesłała sprawę z Miłosnej do Kraśnika.")

add_occ("Nawrocki", "Stanisław", "Kraśnik", "Były burmistrz i stary rajca", None, 94, "1683", "Stanisław Nawrocki", "Powód opisujący zajęcie 6 świń", "Opisuje sekwestr 6 świń na fl 15 przez egzaktorów.")
add_occ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany", None, 94, "1683", "Jakub Wardęga", "Pozwany poddający się P. Młodowskiemu", "Oddał się w poddaństwo na Budzyniu.")
add_occ("Młodowski", "[Pan]", "Kraśnik / Budzyń", "Podstarości kraśnicki", None, 94, "1683", "Pan Młodowski Podstarości", "Podstarości przyjmujący Wardęgę w poddaństwo", "Zmusił Nawrockiego do zapłaty za świnie i konia.")
add_occ("Dzierzgowski", "[Mieszczanin]", "Kraśnik", "Donosiciel / Sąsiad", "Dzierzgowski [?]", 94, "1683", "Dzierzgowski", "Informujący egzaktorów o świniach", "Dał znać egzaktorom o powrocie świń Wardęgi.")

add_occ("Nawrocki", "Stanisław", "Kraśnik", "Były burmistrz i stary rajca", None, 95, "1683", "Stanisław Nawrocki", "Powód opisujący konfiskaty i najazd na pole", "Zmuszony przez Młodowskiego do zapłaty fl 12, fl 6 i fl 15; stracił parę koni.")
add_occ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany", None, 95, "1683", "Jakub Wardęga", "Sprawca zaboru pary koni z bron", "Najechał na pole Nawrockiego i zabrał parę młodych koni.")
add_occ("Młodowski", "[Pan]", "Kraśnik / Budzyń", "Podstarości kraśnicki", None, 95, "1683", "Pan Młodowski", "Wymuszający zapłatę bez sądu miejskiego", "Sądził Nawrockiego z pominięciem sądu miejskiego.")

add_occ("Nawrocki", "Stanisław", "Kraśnik", "Były burmistrz i stary rajca", None, 96, "1683", "Stanisław Nawrocki", "Powód wręczający suplikę Młodowskiemu", "Dochodzi fl 26, fl 15 i fl 100 za utracone konie.")
add_occ("Młodowski", "[Pan]", "Kraśnik / Budzyń", "Podstarości kraśnicki", None, 96, "1683", "Pan Młodowski", "Odbiorca podarunku i grożący gąsiorem", "Przyjął podarunek i groził Nawrockiemu gąsiorem.")
add_occ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany", None, 96, "1683", "Jakub Wardęga", "Spalił chatę na Budzyniu i wrócił na Przedmieście", "Próbował wykręcić się z poddaństwa budzyńskiego.")

add_occ("Nawrocki", "Stanisław", "Kraśnik", "Były burmistrz i stary rajca", None, 97, "1683", "Stanisław Nawrocki", "Powód wyliczający kontrybucje wojenne", "Powołuje się na dekret Ordynata kasujący dekrety Młodowskiego.")
add_occ("Szarowski", "Jan", "Kraśnik", "Mieszczanin", "Szarowski [?]", 97, "1683", "Pan Jan Szarowski", "Poszkodowany w rekwizycjach wojennych", "Jemu także zabrano fanty na potrzeby żołnierskie.")
add_occ("Bębenek", "[Mieszczanin]", "Kraśnik", "Mieszczanin", "Bębenek [?]", 97, "1683", "Bębenek", "Poszkodowany w rekwizycjach wojennych", "Wspomniany wśród mieszczan płacących fantami.")

add_occ("Nawrocki", "Stanisław", "Kraśnik", "Były burmistrz i stary rajca", None, 98, "1683", "Stanisław Nawrocki", "Powód żądający zwrotu szkód i kary więzienia", "Opisuje zabór konia przez żołnierzy ordynata w drodze do Lublina.")
add_occ("Łyś", "[Mieszczanin]", "Kraśnik", "Mieszczanin", "Łyś [?]", 98, "1683", "Łyś", "Poszkodowany przez żołnierzy ordynata", "Stracił konia podobnie jak Nawrocki i Pyzik.")
add_occ("Pyzik", "[Mieszczanin]", "Kraśnik", "Mieszczanin", None, 98, "1683", "Pyzik", "Poszkodowany przez żołnierzy ordynata", "Pospólstwo złożyło mu składkę na wynagrodzenie szkody.")

# Skany 99–100 (Dylacja Wardęgi i proces Szpitala Św. Ducha z Turkowianami)
add_occ("Wardęga", "Jakub", "Dzierzkowice / Budzyń", "Poddany", None, 99, "1683", "Pozwany Jakub Wardęga", "Uzyskujący 7-dniową dylację na odpowiedź", "Stawił się przed sądem i uzyskał termin zawity.")
add_occ("Nawrocki", "Stanisław", "Kraśnik", "Były burmistrz i stary rajca", None, 99, "1683", "Aktor", "Zobowiązany do przedłożenia dowodów", "Otrzymał nakaz przygotowania dowodów.")
add_occ("Turek", "Stanisław", "Kraśnik (Przedmieście)", "Przedmieszczanin (zm.)", None, 99, "1683", "olim Stanislaus Turek Suburbianus", "Zmarły dłużnik wyderkafowy", "Zapis na jego półłanku Popielczanka dla Szpitala Św. Ducha na fl 100 (czynsz fl 5).")
add_occ("Turek", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Turkowian", 99, "1683", "Successores Turkowianos", "Pozwany przez Szpital Św. Ducha", "Sukcesor Stanisława Turka pozwany 28 IV 1683 r.")

add_occ("Stankowski", "Paweł", "Kraśnik", "Podwójci i prowizor Szpitala Św. Ducha", None, 100, "1683", "Fam. Paulus Stankowski Viceadvocatus et Provisor", "Podwójci i prowizor szpitala", "Wyznacza 2 tygodnie na rachunek (calculum) między spadkobiercami Turka.")
add_occ("Turek", "Tomasz", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Turkowian", 100, "1683", "Honestus Thomas Turek Anteoppidanus", "Sukcesor Stanisława Turka", "Występuje w procesie wyderkafowym 28 IV 1683 r.")
add_occ("Turek", "Marcin", "Kraśnik (Przedmieście)", "Przedmieszczanin", "Turkowian", 100, "1683", "Martinus Turek Anteoppidanus", "Sukcesor Stanisława Turka", "Występuje w procesie wyderkafowym 28 IV 1683 r.")

# Zapis gen_data_j20_part4.json
with open('/home/ubuntu/workspace/Gen/gen_data_j20_part4.json', 'w', encoding='utf-8') as f:
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

print(f"Zapisano gen_data_j20_part4.json ({len(gen_data)} profili) oraz CSV.")
