# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part7.json', 'r', encoding='utf-8') as f:
    persons = json.load(f)

lookup = {}
for p in persons:
    key = (p['nazwisko'].strip().lower(), p['imie'].strip().lower(), p['miejsce'].strip().lower())
    lookup[key] = p

def add_occ(nazwisko, imie, miejsce, skan, rok, zapis, rola, wariant_extra=None, funkcja_extra=None):
    key = (nazwisko.strip().lower(), imie.strip().lower(), miejsce.strip().lower())
    if key in lookup:
        p = lookup[key]
        if not any(w['skan'] == skan for w in p['wystapienia']):
            p['wystapienia'].append({
                "skan": skan,
                "rok": str(rok),
                "zapis_oryginalny": zapis,
                "rola": rola
            })
        if wariant_extra:
            existing = p.get('wariant_nazwiska') or ''
            for part in [x.strip() for x in wariant_extra.split('/') if x.strip()]:
                if part not in existing:
                    existing = f"{existing} / {part}" if existing else part
            p['wariant_nazwiska'] = existing
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

# SKAN 176 (1700)
add_occ("Oczapka", "Tomasz", "Kraśnik", 176, 1700, "Tomasz Oczapka", "Pozwany o niewypłacenie długu z zapisu", "Oczapko?")
add_occ("Kruk", "Wojciech", "Kraśnik", 176, 1700, "Wojciech Kruk", "Powód przeciw Oczapce", "Kruczek?")
add_occ("Kosik", "Jan", "Kraśnik", 176, 1700, "Jan Kosik", "Strona w sprawie zapisu przed sądem", "Kusik?")
add_occ("Kwaśnica", "Stefan", "Kraśnik", 176, 1700, "Stefan Kwaśnica", "Były burmistrz wspomniany przy rozliczeniu", "Kwaśnik?")
add_occ("Grzesiek", "Rzeźnik", "Kraśnik", 176, 1700, "Grzesiek Rzeźnik", "Dalszy ciąg sprawy o profanację sądu i obrazę ławnika")

# SKAN 177 (1700)
add_occ("Skołowski", "Stanisław", "Kraśnik", 177, 1700, "Stanisław Skołowski", "Strona w sporze majątkowym przed sądem", "Sokołowski?")
add_occ("Bielak", "Adam", "Przedmieście Piaski", 177, 1700, "Adam Białek", "Mieszczanin przedmiejski występujący w sprawie gruntowej", "Białek?")
add_occ("Barankowicz", "Jan", "Kraśnik", 177, 1700, "Jan Barankowicz", "Rajca i ławnik zasiadający w sądzie")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 177, 1700, "Wojciech Szymatowski", "Burmistrz kraśnicki w sprawie miejskiej")

# SKAN 178 (1700)
add_occ("Brońka", "Marcin", "Kraśnik", 178, 1700, "Marcin Brońka", "Strona w sprawie o pobicie i obdukcję", "Bryńka?")
add_occ("Szwed", "Sebastian", "Przedmieście Kraśnickie", 178, 1700, "Sebastian Szwed", "Świadek w sprawie na przedmieściu", "Szwedka?")
add_occ("Pielaszkowicz", "Wawrzyniec", "Kraśnik", 178, 1700, "Wawrzyniec Pielaszkowicz", "Ławnik przysięgły obecny na sesji")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 178, 1700, "Marcin Rymarczyk", "Wójt przedmieścia Piaski w sporze sądowym", "Rymarczyk?")

# SKAN 179 (1700)
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 179, 1700, "Tomasz Zdebik", "Strona dochodząca praw do gruntu po Kondupie", "Zdebik")
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 179, 1700, "Tomasz Kopeć", "Powód przeciw Marcinowi Dymarczykowi o ojcowiznę żony")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 179, 1700, "Marcin Dymarczyk", "Ojczym Marianny Kopciowej, pozwany o zatrzymanie ćwierci roli")

# SKAN 180 (1700)
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 180, 1700, "Tomasz Kopeć", "Mąż Marianny z Jasieńskich, uzyskujący prawo wykupu ojcowizny za 120 złp")
add_occ("Kopciowa", "Marianna z Jasieńskich", "Przedmieście Kraśnickie", 180, 1700, "Marianna z Jasieńskich Kopciowa", "Żona Tomasza Kopcia, córka Augustyna Jasieńskiego i Reginy, pasierbica Dymarczyka", "Jasińska?")
add_occ("Jasieński", "Augustyn", "Przedmieście Kraśnickie", 180, 1700, "Augustyn Jasieński (zmarły)", "Zmarły ojciec Marianny Kopciowej, pierwszy mąż Reginy", "Jasiński?")
add_occ("Jasińska", "Regina", "Przedmieście Kraśnickie", 180, 1700, "Regina Jasieńska / Dymarczykowa", "Matka Marianny Kopciowej, żona Augustyna Jasieńskiego, a następnie Marcina Dymarczyka", "Jasieński")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 180, 1700, "Marcin Dymarczyk", "Ojczym Marianny Kopciowej zobowiązany dekretem Sądu Obojnego do wydania ćwierci roli i stodoły za 120 złp")
add_occ("Majowski", "Jan", "Kraśnik", 180, 1700, "Jan Majowski Wójt", "Wójt kraśnicki przewodniczący Sądowi Obojnemu 30 VII 1700 r.")

# SKAN 181 (1700)
add_occ("Mrokowska", "Barbara z Janaszkowiców", "Kraśnik", 181, 1700, "Barbara de Janaszkowice Mrokowska", "Wdowa po malarzu Adamie Karolu Mrokowskim, zawierająca nowe małżeństwo z Wawrzyńcem Broskowskim", "Janaszkowicówna")
add_occ("Mrokowski", "Adam Karol", "Kraśnik", 181, 1700, "Adamus Carolus Mrokowski (zmarły)", "Zmarły między III a X 1700 r. mistrz malarski, mąż Barbary z Janaszkowiców", None, "Malarz / Mieszczanin (zm. 1700)")
add_occ("Broskowski", "Wawrzyniec", "Kraśnik", 181, 1700, "Laurentius Broskowski z Podlasia", "Nowy mąż Barbary Mrokowskiej przybyły z Podlasia, otrzymujący zapis dożywocia", "Brostkowski? / Brzozowski?")
add_occ("Mrokowski", "Antoni", "Kraśnik", 181, 1700, "Antonius Mrokowski", "Syn Barbary z Janaszkowiców i Adama Karola Mrokowskich, zabezpieczony w zapisie dożywocia")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 181, 1700, "Marcin Dymarczyk", "Dokończenie dekretu w sprawie rozliczeń z Tomaszem Kopciem")

# SKAN 182 (1700)
add_occ("Mrokowska", "Barbara z Janaszkowiców", "Kraśnik", 182, 1700, "Barbara Mrokowska", "Dokończenie zapisu dożywocia z zastrzeżeniem praw syna Antoniego")
add_occ("Broskowski", "Wawrzyniec", "Kraśnik", 182, 1700, "Wawrzyniec Broskowski", "Mąż Barbary Mrokowskiej przyjmujący zapis dożywocia")
add_occ("Żymakowska", "Zofia", "Kraśnik", 182, 1700, "Zofia Żymakowska", "Strona występująca w zapisie sądowym 27 X 1700 r.", "Szymakowska?")
add_occ("Szymatowski", "Wojciech", "Kraśnik", 182, 1700, "Wojciech Szymatowski Burmistrz", "Burmistrz obecny przy zapisie 27 X 1700 r.")

# SKAN 183 (1700)
add_occ("Kłotka", "Wojciech", "Kraśnik", 183, 1700, "Wojciech Kłotka", "Mąż Maryny Kłotkowej, wykonujący przysięgę oczyszczającą w sprawie o czary")
add_occ("Kłotkowa", "Maryna", "Kraśnik", 183, 1700, "Maryna Kłotkowa", "Oczyszczona przysięgą w procesie o czary przeciw Chudzikowi (wadium 120 grzywien pod karą banicji)")
add_occ("Chudzik", "Marcin", "Kraśnik", 183, 1700, "Marcin Chudzik", "Winiarz zobowiązany wyrokiem pod wadium 120 grzywien i banicją do nieponawiania oskarżeń o czary")
add_occ("Madejczyk", "Stanisław", "Przedmieście Kraśnickie", 183, 1700, "Stanisław Madejczyk", "Strona lub świadek na sesji z 29 X 1700 r.", "Maciejczyk?")

# SKAN 184 (1700 - dublet mikrofilmu skanu 183, fol. 89r)
add_occ("Kłotka", "Wojciech", "Kraśnik", 184, 1700, "Wojciech Kłotka (dublet 89r)", "Finał procesu o czary z wadium 120 grzywien (dublet klatki 183)")
add_occ("Kłotkowa", "Maryna", "Kraśnik", 184, 1700, "Maryna Kłotkowa (dublet 89r)", "Oczyszczenie przysięgą w procesie o czary (dublet klatki 183)")
add_occ("Chudzik", "Marcin", "Kraśnik", 184, 1700, "Marcin Chudzik (dublet 89r)", "Zobowiązany wadium 120 grzywien do zachowania pokoju (dublet klatki 183)")

# SKAN 185 (1700)
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 185, 1700, "Tomasz Zdeb", "Powód dochodzący wykupu ćwierci roli po wuju Wojciechu Kondupie")
add_occ("Kondup", "Wojciech", "Przedmieście Kraśnickie", 185, 1700, "Wojciech Kondup (zmarły)", "Zmarły wuj Tomasza Zdeba, dawny właściciel spornej ćwierci roli", "Kondupa?")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 185, 1700, "Andrzej Panek", "Pozwany przez Tomasza Zdeba o wydanie roli po Kondupie za spłatą sumy wykupnej")

# SKAN 186 (1700 - dublet mikrofilmu skanu 185, fol. 89v)
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 186, 1700, "Tomasz Zdeb (dublet 89v)", "Spór o wykup roli po Wojciechu Kondupie (dublet klatki 185)")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 186, 1700, "Andrzej Panek (dublet 89v)", "Pozwany o rolę po Kondupie (dublet klatki 185)")

# SKAN 187 (1700)
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 187, 1700, "Tomasz Zdeb", "Uzyskujący dekret w sprawie wykupu roli po Wojciechu Kondupie")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 187, 1700, "Andrzej Panek", "Pozwany w procesie o rolę i zasiewy na Podlesiu/Zarzeczu")
add_occ("Kwiecień", "Matyasz", "Przedmieście Kraśnickie", 187, 1700, "Matyasz Kwiecień", "Świadek w sprawie gruntowej o granice roli", "Kwietniowa?")

# SKAN 188 (1700)
add_occ("Królik", "Jan", "Kraśnik", 188, 1700, "Jan Królik", "Mieszczanin w sprawie o rozliczenie i świadków", "Królikowski?")
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 188, 1700, "Tomasz Zdeb", "Kontynuacja egzekucji dekretu przeciw Andrzejowi Pankowi")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 188, 1700, "Andrzej Panek", "Odwołujący się od wyceny nakładów na gruncie po Kondupie")

# SKAN 189 (1700)
add_occ("Maciarz", "Kazimierz", "Kraśnik", 189, 1700, "Kazimierz Maciarzyk", "Pozwany przez Berka Moszkowica o dług", "Maciarzyk")
add_occ("Moszkowic", "Berek", "Kraśnik", 189, 1700, "Berek Moszkowic", "Kupiec żydowski procesujący się z Kazimierzem Maciarzykiem", None, "Kupiec / Obywatel żydowski")
add_occ("Madejczyk", "Szymon", "Przedmieście Kraśnickie", 189, 1700, "Szymon Madejczyk", "Świadek lub strona na sesji listopadowej 1700 r.")
add_occ("Łędański", "Maciej", "Kraśnik", 189, 1700, "Maciej Łędański", "Mieszczanin powołany na świadka w procesie listopadowym", "Łądanski?")

# SKAN 190 (1700)
add_occ("Kopeć", "Tomasz", "Przedmieście Kraśnickie", 190, 1700, "Tomasz Kopeć", "Składający 12 XI 1700 r. protestację z gotowością spłaty 120 złp Marcinowi Dymarczykowi")
add_occ("Dymarczyk", "Marcin", "Przedmieście Piaski", 190, 1700, "Marcin Dymarczyk", "Odmawiający przyjęcia sumy wykupnej 120 złp mimo terminu na św. Marcina")
add_occ("Łędański", "Maciej", "Kraśnik", 190, 1700, "Maciej Łędański", "Świadek gotowości spłaty 120 złp przez Tomasza Kopcia")
add_occ("Anczerek", "Tomasz", "Przedmieście Kraśnickie", 190, 1700, "Tomasz Anczerek", "Świadek okazania pieniędzy przez Tomasza Kopcia")
add_occ("Wilk", "Józef", "Kraśnik", 190, 1700, "Józef Wilk", "Młynarz miejski będący świadkiem protestacji Kopcia")

# SKAN 191 (1700)
add_occ("Dalmaczyk", "Wojciech", "Kraśnik", 191, 1700, "Wojciech Dalmaczyk Krawiec", "Krawiec prowadzący śledztwo przeciw Janowi i Agnieszce Barankowicom o pieniądze córki Anny", "Dalmacyk?", "Krawiec")
add_occ("Barankowicz", "Jan", "Kraśnik", 191, 1700, "Jan Barankowicz", "Pozwany przez krawca Dalmaczyka w sprawie zaginionych pieniędzy")
add_occ("Barankowicowa", "Agnieszka", "Kraśnik", 191, 1700, "Agnieszka Barankowicowa", "Żona Jana Barankowicza, pozwana w sprawie córki Dalmaczyka")
add_occ("Kucharski", "Walenty", "Kraśnik", 191, 1700, "Walenty Kucharski", "Świadek zeznający w sprawie krawca Dalmaczyka")

# SKAN 192 (1700)
add_occ("Dalmaczyk", "Wojciech", "Kraśnik", 192, 1700, "Wojciech Dalmaczyk", "Powód przesłuchujący świadków w sprawie pieniędzy córki")
add_occ("Dalmaczykówna", "Anna", "Kraśnik", 192, 1700, "Anna Dalmaczykówna", "Córka krawca Wojciecha Dalmaczyka, służąca lub bywalczyni w domu Barankowiczów")
add_occ("Lubelszczanka", "Maryna", "Kraśnik", 192, 1700, "Maryna Lubelszczanka", "Świadek zeznający z instancji Dalmaczyka o pobycie w domu Barankowicza", "Lublińska?")

# SKAN 193 (1700)
add_occ("Sędłak", "Jan", "Kraśnik", 193, 1700, "Jan Sędłak", "Świadek w procesie krawca Dalmaczyka z Barankowiczem", "Siedlak?")
add_occ("Paryszewski", "Wojciech", "Kraśnik", 193, 1700, "Wojciech Paryszewski", "Mieszczanin zeznający w dochodzeniu o pieniądze", "Parysowski?")
add_occ("Barankowicz", "Jan", "Kraśnik", 193, 1700, "Jan Barankowicz", "Pozwany o rozliczenie pieniędzy córki krawca")

# SKAN 194 (1700)
add_occ("Głuchowski", "Stanisław", "Kraśnik", 194, 1700, "Stanisław Głuchowski", "Świadek zeznający w sprawie z 1700 r.", "Głuch?")
add_occ("Zydaczyk", "Matyasz", "Kraśnik", 194, 1700, "Matyasz Zydaczyk", "Szwagier Augustyna Pielaszkowica, świadek z instancji Dalmaczyka", "Żydaczyk?")
add_occ("Lubelszczanka", "Maryna", "Kraśnik", 194, 1700, "Maryna Lubelszczanka", "Zeznająca o piciu miodu w domu Jana Barankowicza")

# SKAN 195 (1700)
add_occ("Lubelszczanka", "Maryna", "Kraśnik", 195, 1700, "Maryna Lubelszczanka", "Dokończenie zeznania o piciu miodu u Barankowicza")
add_occ("Zydaczyk", "Matyasz", "Kraśnik", 195, 1700, "Matyasz Zydaczyk", "Zeznający o czterech groszach na kluski od pani Barankowicowej dla Anny Dalmaczykówny; pozwany przez szwagra Pielaszkowica")
add_occ("Dalmaczyk", "Wojciech", "Kraśnik", 195, 1700, "Uczciwy Dalmaczyk", "Powód w sprawie z Barankowiczem odłożonej ad octavam")
add_occ("Dalmaczykówna", "Anna", "Kraśnik", 195, 1700, "Anna Dalmaczykówna", "Córka krawca wzmiankowana w zeznaniu Zydaczyka o groszach na kluski")
add_occ("Barankowicz", "Jan", "Kraśnik", 195, 1700, "Jan Barankowicz", "Pozwany przez Dalmaczyka (sprawa ad octavam)")
add_occ("Pielaszkowicz", "Augustyn", "Kraśnik", 195, 1700, "Augustyn Pielaszkowicz", "Powód przeciw szwagrowi Maciejowi Zydaczykowi (komplanacja przed 1 czerwca)")
add_occ("Moszkowic", "Berek", "Kraśnik", 195, 1700, "Berek Moszkowic", "Powód przeciw Kazimierzowi Maciarzykowi")
add_occ("Maciarz", "Kazimierz", "Kraśnik", 195, 1700, "Kazimierz Maciarzyk", "Pozwany przez Berka (odroczenie z powodu braku świadków)")
add_occ("Kępa", "Maciej", "Przedmieście Kraśnickie", 195, 1700, "Maciej Kępa", "Powód przeciw bratu Szymonowi Kępie o chmiel siany")
add_occ("Kępa", "Szymon", "Przedmieście Kraśnickie", 195, 1700, "Szymon Kępa", "Brat rodzony Macieja Kępy, pozwany o chmiel siany")
add_occ("Solicki", "Szymon", "Kraśnik", 195, 1700, "Simon Solicki", "Powód uzyskujący drugą kontumację przeciw Janowi Trawińskiemu")
add_occ("Trawiński", "Jan", "Kraśnik", 195, 1700, "Joannes Trawiński", "Kontumant (2do contumax wobec Solickiego i 1mo wobec Wojciechowicza)")
add_occ("Wojciechowicz", "Obywatel", "Kraśnik", 195, 1700, "Woyciechowicz", "Powód uzyskujący pierwszą kontumację przeciw Trawińskiemu i Rzeczyckiemu")
add_occ("Rzeczycki", "Obywatel", "Kraśnik", 195, 1700, "Rzeczycki", "Pozwany skazany zaocznie (1mo contumax) z instancji Wojciechowicza")
add_occ("Moszkowicz", "Szymon", "Kraśnik", 195, 1700, "Simon Moszkowic", "Powód uzyskujący wyrok zaoczny (in lucro) przeciw Pawłowi Słomkowskiemu")
add_occ("Słomkowski", "Paweł", "Kraśnik", 195, 1700, "Paulus Słomkowski", "Kontumant w sprawie z Szymonem Moszkowicem")

# SKAN 196 (1700)
add_occ("Mazała", "Józef", "Kraśnik", 196, 1700, "Józef Macal", "Skazany na 3 grzywny za niestawiennictwo do przysięgi z Berkiem Moszkowicem o 15 wieprzów/kieprów")
add_occ("Moszkowic", "Berek", "Kraśnik", 196, 1700, "Berek Moszkowic", "Wygrany w sprawie z Józefem Mazałą o 15 wieprzów/kieprów")
add_occ("Sokołowicz", "Adam", "Kraśnik", 196, 1700, "Adam Sokołowicz Burmistrz", "Burmistrz kraśnicki przeprowadzający 20 XI 1700 r. wizję gruntów po Kondupie")
add_occ("Borkiewicz", "Wojciech", "Kraśnik", 196, 1700, "Wojciech Borkiewicz Ławnik", "Ławnik przysięgły uczestniczący w wizji na Zarzeczu i Podlesiu")
add_occ("Lis", "Jakub", "Kraśnik", 196, 1700, "Jakub Lis", "Świadek wizji gruntów po Wojciechu Kondupie")
add_occ("Skatka", "Wojciech", "Przedmieście Kraśnickie", 196, 1700, "Wojciech Skatka", "Świadek wizji gruntów po Wojciechu Kondupie")
add_occ("Kondup", "Wojciech", "Przedmieście Kraśnickie", 196, 1700, "quondam Wojciech Kondup", "Zmarły właściciel ćwierci roli na Zarzeczu i Podlesiu będącej przedmiotem wizji")
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 196, 1700, "Thomas Zdeb", "Upominający się o wizję i wykup ćwierci roli po Kondupie")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 196, 1700, "Andrzej Panek", "Posiadacz spornej ćwierci roli, który zasadził 30 młodych gruszek i jabłonkę")

# SKAN 197 (1700)
add_occ("Pełka", "Maciej", "Kraśnik", 197, 1700, "Maciej Pełka Bedellus", "Woźny urzędu radzieckiego składający relację z doręczenia pozwu do Zamku Zamoyskiego", None, "Woźny miejski (Bedellus)")
add_occ("Grymałowski", "Wojciech", "Kraśnik", 197, 1700, "Wojciech Grymałowski Burmistrz", "Burmistrz kraśnicki pozywający z żoną Teresą Żyda Herszka do Sądu Zamkowego w Zamościu")
add_occ("Grymałowska", "Teresa", "Kraśnik", 197, 1700, "Teresa de gente Janaszkowicowa", "Żona Wojciecha Grymałowskiego, współpowódka przeciw Żydowi Herszkowi")
add_occ("Zamoyska", "Anna z Gnińskich", "Ordynacja Zamoyska", 197, 1700, "Anna z Gnińskich Zamoyska Podskarbina", "Podskarbina Wielka Koronna, w której imieniu wystawiono pozew do Sądu Zamkowego Zamoyskiego")
add_occ("Herszek", "Starozakonny", "Kraśnik", 197, 1700, "Niewierny Herszek", "Pozwany przez burmistrzostwo Grymałowskich do Sądu Zamkowego w Zamościu")
add_occ("Pion", "Matyasz", "Przedmieście Kraśnickie", 197, 1700, "Maciej Pion z Podlesia", "Sprzedawca domu i ogródka na Przedmieściu Piasek za 50 złp")
add_occ("Pionowa", "Agnieszka", "Przedmieście Kraśnickie", 197, 1700, "Agnieszka Pionowa", "Żona Macieja Piona, współsprzedająca nieruchomość na Piasku")
add_occ("Pionowa", "Maryna", "Przedmieście Kraśnickie", 197, 1700, "niegdy Maryna z domu Pionowa", "Poprzednia właścicielka ogrodu i domu na Piasku")
add_occ("Marek", "Augustyn", "Przedmieście Piaski", 197, 1700, "Augustyn Marek", "Sąsiad sprzedanego ogrodu na Przedmieściu Piasek")
add_occ("Bielak", "Adam", "Przedmieście Piaski", 197, 1700, "Adam Bielak", "Nabywca domu i ogródka na Przedmieściu Piasek za 50 złp")
add_occ("Bielakowa", "Agnieszka", "Przedmieście Piaski", 197, 1700, "Agnieszka Bielakowa", "Żona Adama Bielaka, współnabywczyni nieruchomości za 50 złp")

# SKAN 198 (1700)
add_occ("Bielak", "Adam", "Przedmieście Piaski", 198, 1700, "Adam Bielak", "Dokończenie wpisu wieczystego nabycia domu na Piasku")
add_occ("Zapust", "Tomasz", "Kraśnik", 198, 1700, "Thomas Zapust", "Świadek kontraktu sprzedaży między Pionami a Bielakami")
add_occ("Wójcik", "Szymon", "Kraśnik", 198, 1700, "Szymon Wójcik", "Świadek kontraktu sprzedaży między Pionami a Bielakami")
add_occ("Pukliński", "Franciszek", "Kraśnik", 198, 1700, "Franciszek Pukliński", "Świadek kontraktu sprzedaży między Pionami a Bielakami")
add_occ("Zajączek", "Tomasz", "Przedmieście Kraśnickie", 198, 1700, "Tomasz Zayczyk / Zajączek", "Powód przeciw Kacprowi Zajączkowi w sprawie o wóz Wojciecha Zajączka", "Zajączyk? / Zdeb?")
add_occ("Zajączek", "Kacper", "Przedmieście Kraśnickie", 198, 1700, "Kacper Zajączek", "Pozwany zobowiązany do przysięgi z dwoma świadkami", "Łędański?")
add_occ("Brzozowski", "Piotr", "Kraśnik", 198, 1700, "Brzozowski", "Właściciel przejazdu przez wodę wspomniany w sprawie Zajączków")
add_occ("Tkaczyk", "Matyasz", "Kraśnik", 198, 1700, "Matyasz Tkaczyk", "Powód przeciw Marcinowi Hapakowi o białą płachtę i 2 korce grochu")
add_occ("Hapak", "Marcin", "Przedmieście Kraśnickie", 198, 1700, "Marcin Hapak", "Pozwany przez Matyasza Tkaczyka o płachtę, 2 korce grochu i żelazo")
add_occ("Pardyka", "Jan", "Przedmieście Kraśnickie", 198, 1700, "Jan Pardyka", "Powód przeciw Kłopotkowi o 20 lub 23 grosze")
add_occ("Kłopocik", "Jakub", "Przedmieście Kraśnickie", 198, 1700, "Kłopotek", "Pozwany przez Jana Pardykę o 20 gr lub przysięgę na 23 gr", "Kłotczyk?")
add_occ("Dalmaczyk", "Wojciech", "Kraśnik", 198, 1700, "Dalmaczyk Krawiec", "Powód uzyskujący odroczenie inkwizycji przeciw Janowi Barankowiczowi")
add_occ("Barankowicz", "Jan", "Kraśnik", 198, 1700, "Jan Barankowicz", "Pozwany przez Dalmaczyka (dalsza inkwizycja)")
add_occ("Hesia", "Starozakonna", "Kraśnik", 198, 1700, "Niewierna Hesia", "Powódka przeciw Jakubowi Kłopotowi zobowiązana do stawienia Agnieszki z dwoma świadkami", "Fesia?", "Obywatelka żydowska")
add_occ("Kłopot", "Jakub", "Przedmieście Kraśnickie", 198, 1700, "Jakub Kłopot", "Pozwany przez Żydówkę Hesię w sprawie o zastaw")
add_occ("Jakubowska", "Agnieszka", "Kraśnik", 198, 1700, "Agnieszka", "Świadek powołany przez Żydówkę Hesię przeciw Jakubowi Kłopotowi", "Jakubowa?")

# SKAN 199 (1700)
add_occ("Dalmaczyk", "Wojciech", "Kraśnik", 199, 1700, "Wojciech Dalmaczyk", "Manifestujący się 29 XI 1700 r. z powodu choroby świadka Marcina Kudzika i niestawiennictwa poddanych konwentu")
add_occ("Barankowicz", "Jan", "Kraśnik", 199, 1700, "Jan Barankowicz Rezydent", "Pozwany przez krawca Dalmaczyka")
add_occ("Barankowicowa", "Agnieszka", "Kraśnik", 199, 1700, "Agnieszka Barankowicowa", "Żona Jana Barankowicza, współpozwana przez Dalmaczyka")
add_occ("Kudzik", "Marcin", "Kraśnik", 199, 1700, "Marcin Kudzik", "Świadek obłożnie chory w procesie Dalmaczyka z Barankowiczem")
add_occ("Tkaczyk", "Matyasz", "Kraśnik", 199, 1700, "Matyasz Tkaczyk", "Powód przedstawiający świadka Szymona Wójcika przeciw Hapakowi")
add_occ("Hapak", "Marcin", "Przedmieście Kraśnickie", 199, 1700, "Hapak", "Pozwany o półkorzec grochu, stare żelazo i dawny zatarg u młynarza budzyńskiego")
add_occ("Wójcik", "Szymon", "Kraśnik", 199, 1700, "Simon Woycik", "Świadek zeznający o ugodzie Hapaka z Tkaczykiem i pobycie u młynarza w Budzyniu")
add_occ("Budzyński", "Młynarz", "Budzyń", 199, 1700, "Młynarz Budzyński", "Młynarz ze wsi Budzyń, u którego dawniej mieszkał Marcin Hapak", None, "Młynarz")
add_occ("Pielaszkowicz", "Augustyn", "Kraśnik", 199, 1700, "Augustyn Pielaszkowicz", "Zobowiązany dekretem do zgody ze szwagrem Matyaszem Zydaczykiem pod karą 3 grzywien")
add_occ("Zydaczyk", "Matyasz", "Kraśnik", 199, 1700, "Matyasz Zydaczyk", "Szwagier Pielaszkowica objęty nakazem zgody pod wadium 3 grzywien")
add_occ("Hesia", "Starozakonna", "Kraśnik", 199, 1700, "Judaea Hesia", "Powódka przedstawiająca świadka Agnieszkę Jakubowską w sprawie o spódnicę")
add_occ("Jakubowska", "Agnieszka", "Kraśnik", 199, 1700, "Agnieszka Jakubowska", "Świadek zeznający o białej spódnicy zastawionej u Żydówki Hesi", "Jakubowa?")

# SKAN 200 (1700)
add_occ("Jakubowska", "Agnieszka", "Kraśnik", 200, 1700, "Agnieszka Jakubowska", "Dokończenie zeznania o zastawieniu spódnicy za 15 zł u Żydówki Hesi i wódce za 2 grosze")
add_occ("Hesia", "Starozakonna", "Kraśnik", 200, 1700, "Hesia Żydówka", "Odbierająca wyrok nakazujący Jakubowi Kłopotowi zapłatę 8 zł w ciągu 3 dni")
add_occ("Kłopot", "Jakub", "Przedmieście Kraśnickie", 200, 1700, "Jakub Kłopot", "Skazany na oddanie 8 zł Żydówce Hesi i zwrot kosztów prawnych")
add_occ("Kłopotowa", "Marina", "Przedmieście Kraśnickie", 200, 1700, "Kłopotowa", "Namawiająca Agnieszkę Jakubowską do odebrania spódnicy od Hesi")
add_occ("Moszkowic", "Berek", "Kraśnik", 200, 1700, "Berek Żyd", "Powód w sprawie z Kazimierzem Maciarzykiem odesłanej do wysłuchania świadków")
add_occ("Maciarz", "Kazimierz", "Kraśnik", 200, 1700, "Kazimierz Maciarzyk", "Pozwany przez Berka Żyda")
add_occ("Zdeb", "Tomasz", "Przedmieście Kraśnickie", 200, 1700, "Thomas Zdeb", "Składający w sądzie pełne 100 złp (50 + 50 złp) na wykup dóbr po wuju Wojciechu Kondupie")
add_occ("Kondup", "Wojciech", "Przedmieście Kraśnickie", 200, 1700, "quondam Wojciech Kondup", "Zmarły wuj Tomasza Zdeba")
add_occ("Panek", "Andrzej", "Przedmieście Kraśnickie", 200, 1700, "Andrzej Panek", "Odmawiający przyjęcia złożonych 100 złp za dobra po Kondupie")
add_occ("Dubaj", "Wojciech", "Kraśnik", 200, 1700, "Albertus Dubaj", "Składający protestację przeciw Żydowi Abramowi o zatrzymanie konia wartości 14 zł", "Dubas?")
add_occ("Abram", "Starozakonny", "Kraśnik", 200, 1700, "Abram Judaeus", "Pozwany przez Wojciecha Dubaja o zatrzymanie konia za 14 zł")

# Przeliczenie indeksów i normalizacja
for idx, p in enumerate(persons, 1):
    p["lp"] = idx
    scan_nums = sorted(list(set(int(w["skan"]) for w in p["wystapienia"])))
    p["skany_list"] = scan_nums
    p["skany_roboczo"] = ", ".join([f"#{s}" for s in scan_nums])
    years = sorted(list(set(w["rok"] for w in p["wystapienia"])))
    p["zakres_lat"] = f"{min(years)}–{max(years)}" if len(years) > 1 else years[0]
    p["liczba_wystapien"] = len(p["wystapienia"])

print(f"✅ Po Partii 8 mamy {len(persons)} unikalnych profili (Wariant 2, 0 duplikatów).")

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part8.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

csv_path = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
headers = ["Lp", "Nazwisko", "Imię", "Miejsce", "Funkcja społeczna / zawód", "Skany źródłowe", "Zakres lat", "Liczba wzmianek", "Warianty nazwiska"]

with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(headers)
    for p in persons:
        writer.writerow([
            p["lp"],
            p["nazwisko"],
            p["imie"],
            p["miejsce"],
            p["funkcja"],
            p["skany_roboczo"],
            p["zakres_lat"],
            p["liczba_wystapien"],
            p.get("wariant_nazwiska") or ""
        ])

print(f"✅ Zaktualizowano {csv_path} ({len(persons)} wierszy).")
