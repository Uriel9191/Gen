# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part14.json', 'r', encoding='utf-8') as f:
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

# SKAN 351 (1754)
add_occ("Panek", "Piotr", "Urzędów / Kraśnik", 351, 1754, "Petrus Panek", "Dokończenie zeznania o uderzeniu wójta pałaszem przez żołnierza")
add_occ("Marczukowski", "Szymon", "Kraśnik", 351, 1754, "P. Woyt", "Wójt kraśnicki zaatakowany pałaszem przez żołnierza w gospodzie", "Marmutowski?")
add_occ("Skowroński", "Podchorąży", "Kraśnik", 351, 1754, "P. Skowroński", "Podchorąży piechoty rozmawiający z Czubkowskim u Żydówki Kali")
add_occ("Kala", "Żydówka", "Kraśnik", 351, 1754, "niewierna Kala", "Właścicielka gospody, w której doszło do zajścia z żołnierzami")
add_occ("Czubkowski", "Franciszek", "Kraśnik", 351, 1754, "Franciscus Czubkowski", "Drugi świadek w sprawie wójta Marczukowskiego przeciw Skowrońskiemu", "Czupkowski?")

# SKAN 352 (1754)
add_occ("Czubkowski", "Franciszek", "Kraśnik", 352, 1754, "Franciscus Czubkowski", "Dokończenie zeznania o groźbach odcięcia kłódki przez Skowrońskiego", "Czupkowski?")
add_occ("Skowroński", "Podchorąży", "Kraśnik", 352, 1754, "Pan Skowroński", "Grożący odcięciem kłódki od aresztu i pijący piwo do wójta")
add_occ("Okoniowa", "Antoniowa", "Kraśnik", 352, 1754, "Antoniowa Okoniowa", "Świadek przesłuchania Marianny Tkaczykówny w obecności Kołtuna")
add_occ("Kołtun", "Antoni", "Kraśnik", 352, 1754, "Antoniy Kołtun", "Świadek przyznania się Marianny Tkaczykówny do relacji z malarzem i kucharzem")
add_occ("Tkaczykówna", "Marianna", "Kraśnik", 352, 1754, "Maryna", "Przyznająca się przed Kołtunem i Okoniową do spraw z malarzem i kucharzem")

# SKAN 353 (1754)
add_occ("Tkaczykówna", "Marianna", "Kraśnik", 353, 1754, "Maryna", "Relacja z wyprowadzenia przez malarza i kucharza z chałupy pod cmentarz")
add_occ("Marczukowski", "Szymon", "Kraśnik", 353, 1754, "Symon Marczukowski advocatus", "Wójt wnoszący inkwizycję przeciw podchorążemu Skowrońskiemu")
add_occ("Skowroński", "Podchorąży", "Kraśnik", 353, 1754, "Pan Skowroński", "Zastany w komorze u Żyda Dawidka z córką Łatosiewicza")
add_occ("Potokowicz", "Andrzej", "Kraśnik", 353, 1754, "Andreas Potokowicz", "Pierwszy świadek zeznający o zajściu u Żyda Dawidka")
add_occ("Dawidek", "Żyd", "Kraśnik", 353, 1754, "Dawidek", "Gospodarz żydowski, u którego w komorze przebywał Skowroński", None, "Gospodarz / Obywatel żydowski")
add_occ("Łatosiewicz", "Matyasz", "Kraśnik", 353, 1754, "nieboszczyk Matyasz Łatosiewicz", "Zmarły ojciec dziewki zastanej w komorze u Dawidka")
add_occ("Łatosiewiczówna", "Córka Matyasza", "Kraśnik", 353, 1754, "córka Matyasza Łatosiewicza", "Córka zmarłego Matyasza Łatosiewicza zastana w komorze ze Skowrońskim")

# SKAN 354 (1754)
add_occ("Mnichowski", "Tomasz", "Turobin / Kraśnik", 354, 1754, "Tomasz Mnichowski", "Powód przeciw Marcinowi Morelowi i Antoniemu Petrykowskiemu")
add_occ("Morel", "Marcin", "Kraśnik", 354, 1754, "Martinus Morel", "Pozwany przez Mnichowskiego o śliwki w ogrodzie Adama Radła")
add_occ("Petrykowski", "Antoni", "Kraśnik", 354, 1754, "Anto: Petrikowski", "Pozwany przez Mnichowskiego w sprawie śliwek", "Petrikowski?")
add_occ("Kutek", "Mikołaj", "Turobin / Kraśnik", 354, 1754, "Nicolaus Kutek Incola Turobinensis", "Mieszkaniec Turobina zeznający o zbieraniu śliwek w ogrodzie Adama Radła")
add_occ("Radło", "Adam", "Kraśnik", 354, 1754, "Adam Radeł", "Właściciel ogrodu ze śliwkami i pozwany przez Grzegorza Pitaszkiewicza (12 X 1754)")
add_occ("Młynarczykowski", "Stanisław", "Kraśnik", 354, 1754, "Stanisław Młynarczykowski", "Powód przeciw Kazimierzowi Młynarskiemu")
add_occ("Młynarski", "Kazimierz", "Kraśnik", 354, 1754, "Kazimierz Młynarski", "Pozwany przez Stanisława Młynarczykowskiego")
add_occ("Pilaszkiewicz", "Antoni", "Kraśnik", 354, 1754, "Antonius Pilaszkiewicz", "Świadek w sprawie Młynarczykowski vs Młynarski")
add_occ("Pitaszkiewicz", "Grzegorz", "Kraśnik", 354, 1754, "Gregorius Pielaskiewicz", "Powód 12 X 1754 r. przeciw Adamowi Radle o zapłatę za oranie roli", "Pielaskiewicz?")
add_occ("Tokarski", "Kazimierz", "Kraśnik", 354, 1754, "Casimirus Tokarski", "Świadek poselstwa od Pitaszkiewicza do Radła (3 tynfy vs 5 złp)")
add_occ("Fruga", "Matyasz", "Kraśnik", 354, 1754, "Mathias Fruga", "Powód przeciw Franciszkowi Barankiewiczowi o bójkę przy młóceniu")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", 354, 1754, "Franciscus Barankiewicz", "Pozwany przez Matyasza Frugę o bójkę w chałupie")
add_occ("Olepar", "Franciszek", "Kraśnik", 354, 1754, "Franciscus Olepar", "Świadek młócący w chałupie Frugi podczas zajścia z Barankiewiczem", "Olechowski?")

# SKAN 355 (1754)
add_occ("Barankiewicz", "Stanisław", "Kraśnik", 355, 1754, "Stanislaus Brankiewicz", "Powód w inkwizycji zeznanej przez Wojciecha Wiaterka", "Brankiewicz?")
add_occ("Wiaterek", "Wojciech", "Przedmieście Kraśnickie", 355, 1754, "Adalbertus Wieterek", "Świadek rozmowy z Michałem Wieterkiem o jego żonie i Wróblowej", "Wieterek?")
add_occ("Wiaterek", "Michał", "Przedmieście Kraśnickie", 355, 1754, "Michał Wieterek", "Mąż żony służącej u Wróblowej", "Wieterek?")
add_occ("Petrykowski", "Antoni", "Kraśnik", 355, 1754, "Ant. Petrikowski", "Powód z Marcinem Morelem przeciw Katarzynie Mnichowskiej z Turobina", "Petrikowski?")
add_occ("Morel", "Marcin", "Kraśnik", 355, 1754, "Martinus Morel", "Powód przeciw Katarzynie Mnichowskiej o śliwki w sadzie Radłowej")
add_occ("Mnichowska", "Katarzyna", "Turobin / Kraśnik", 355, 1754, "Catharina Mnichowska Incola Turobinensis", "Mieszkanka Turobina pozwana o handel śliwkami")
add_occ("Kucharzowa", "Elżbieta", "Kraśnik", 355, 1754, "Elisabeth Kuchanowa", "Pierwsza świadek widząca z budy w sadzie Petrykowskiego i Morela", "Kuchanowa?")
add_occ("Bednarka", "Anastazya", "Kraśnik", 355, 1754, "Anastazya Tomaszowa Bednarka", "Druga świadek rozmowy Morela z Mnichowską o 2 talarach bitych")

# SKAN 356 (1754)
add_occ("Mnichowska", "Katarzyna", "Turobin / Kraśnik", 356, 1754, "Katarzyna Mnichowska", "Kupująca śliwki w sadzie Adama Radła")
add_occ("Radło", "Adam", "Kraśnik", 356, 1754, "Adam Radeł", "Zeznający, że sprzedał śliwki wyłącznie Katarzynie Mnichowskiej")
add_occ("Petrykowski", "Antoni", "Kraśnik", 356, 1754, "Antoni Petrikowski", "Targujący śliwki u Adama Radła bez dobicia targu")
add_occ("Posuniak", "Adam", "Kraśnik", 356, 1754, "Adam Posoniak", "Powód w sprawie zapaski i córki z pastuchami Bieniaszewskiego")
add_occ("Jędrzyna", "Józefowa", "Kraśnik", 356, 1754, "Jozefowa Jędrzyna", "Świadek kłótni córki Posuniaka z pastuchem Bieniaszewskiego o zapaskę", "Igrzyna?")
add_occ("Bieniaszewski", "Wojciech", "Kraśnik", 356, 1754, "Woyciech Bieniaszewski", "Właściciel pastuchów w sporze z córką Adama Posuniaka")
add_occ("Falkiewiczowa", "Katarzyna", "Kraśnik", 356, 1754, "Katarzyna Falkiewiczowa", "Druga świadek w sprawie zaginionej zapaski", "Jatkowiczowa?")

# SKAN 357 (1754)
add_occ("Falkiewiczowa", "Katarzyna", "Kraśnik", 357, 1754, "Katarzyna Falkiewiczowa", "Dokończenie zeznania o znalezieniu zapaski przez Kaspra Zagajskiego", "Jatkowiczowa?")
add_occ("Zagajski", "Kasper", "Kraśnik", 357, 1754, "Kasper Zagajski", "Znalazca zapaski w sprawie córki Adama Posuniaka", "Gagaj?")
add_occ("Posuniak", "Adam", "Kraśnik", 357, 1754, "Adam Posoniak", "Ojciec dziewczyny w sprawie zaginionej zapaski")
add_occ("Koza", "Józef", "Kraśnik", 357, 1754, "Jozef Koza", "Świadek w sprawie Bieniaszewiczów")
add_occ("Bieniaszewska", "Wojciechowa", "Kraśnik", 357, 1754, "Woyciechowa Bieniaszewska", "Wołająca na pastuchów pasących bydło po wyjściu z kościoła")
add_occ("Fruga", "Matyasz", "Kraśnik", 357, 1754, "Mathias Fruga", "Powód przeciw Barankiewiczowi oraz świadek szkód w tatarce Krzeszowskiego")
add_occ("Tokarz", "Antoni", "Kraśnik", 357, 1754, "Antoniy Tokarz Con: Cra:", "Rajca zeznający o słowach Franciszka Barankiewicza do Frugi")
add_occ("Barankiewicz", "Franciszek", "Kraśnik", 357, 1754, "Franciszek Barankiewicz", "Mówiący Matyaszowi Frudze o pastuchu do świń")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 357, 1754, "Simon Krzeszowski Scab: Cras:", "Ławnik skarżący się na świnie sześciu gospodarzy w swojej tatarce")
add_occ("Kawka", "Mikołaj", "Kraśnik", 357, 1754, "Mikołaj Kawka", "Właściciel świń wchodzących w tatarkę Szymona Krzeszowskiego")
add_occ("Bruś", "Wojciech", "Kraśnik", 357, 1754, "Woyciech Bruś", "Właściciel świń wchodzących w tatarkę Szymona Krzeszowskiego")
add_occ("Macała", "Łukasz", "Kraśnik", 357, 1754, "Łukasz Macała", "Właściciel świń wchodzących w tatarkę Szymona Krzeszowskiego")
add_occ("Drozd", "Józef", "Kraśnik", 357, 1754, "Jozef Drozd", "Właściciel świń wchodzących w tatarkę Szymona Krzeszowskiego")
add_occ("Zdyb", "Antoni", "Kraśnik", 357, 1754, "Antoni Zdyb", "Właściciel świń wchodzących w tatarkę Szymona Krzeszowskiego")
add_occ("Łysy", "Antoni", "Kraśnik", 357, 1754, "Antoni Łysy", "Właściciel świń wchodzących w tatarkę Szymona Krzeszowskiego")

# SKAN 358 (1754)
add_occ("Piotrowczyk", "Matyasz", "Kraśnik", 358, 1754, "Mathias Piotrowczyk", "Powód 25 X 1754 r. przeciw Antoniemu Pankowi i macosze o majątek po ojcu")
add_occ("Panek", "Antoni", "Kraśnik", 358, 1754, "Antonius Panek", "Pozwany 25 X 1754 r. przez Matyasza Piotrowczyka")
add_occ("Kilianek", "Bartosz", "Kraśnik", 358, 1754, "Bartłomiej Kilianek", "Pierwszy świadek 25 X 1754 r. zeznający o wyganianiu pasierba z chałupy", "Bartłomiej?")
add_occ("Piotrowczykowa", "Augustynowa", "Kraśnik", 358, 1754, "Augustynowa Piotrowczykowa", "Macocha Matyasza Piotrowczyka, wdowa z Zdybów po Augustynie")
add_occ("Łysak", "Matyasz", "Kraśnik", 358, 1754, "Matyasz Łysak", "Drugi świadek, dawny parobek Augustyna Piotrowczyka, zeznający o wołach za 101 złp 15 gr", None, "Parobek")
add_occ("Piotrowski", "Augustyn", "Kraśnik", 358, 1754, "nieboszczyk Augustyn Piotrowczyk", "Zmarły gospodarz i ojciec Matyasza, Andrzeja oraz Katarzyny")
add_occ("Sobranek", "Piotr", "Kraśnik", 358, 1754, "Piotr Sobranek", "Sprzedawca wołu zmarłemu Augustynowi Piotrowczykowi")
add_occ("Biegaj", "Mikołaj", "Przedmieście Kraśnickie", 358, 1754, "Mikołaj Biegaj", "Trzeci świadek 25 X 1754 r. zeznający o komplanacji o pszenicę z pasieki")
add_occ("Piotrowczyk", "Andrzej", "Kraśnik", 358, 1754, "Andrzey Piotrowczyk", "Brat Matyasza uczestniczący w podziale pszenicy z pasieki ojca")
add_occ("Piotrowczykówna", "Katarzyna", "Kraśnik", 358, 1754, "Siostra Ich Katarzyna", "Siostra Matyasza i Andrzeja Piotrowczyków biorąca udział w podziale pszenicy")

# SKAN 359 (1754)
add_occ("Biegaj", "Mikołaj", "Przedmieście Kraśnickie", 359, 1754, "świadek", "Dokończenie zeznania o podziale pszenicy i kłótni z Pankiem")
add_occ("Piotrowczyk", "Andrzej", "Kraśnik", 359, 1754, "Andrzey Piotrowczyk", "Obecny przy wydawaniu pszenicy siostrze Katarzynie z polecenia wójta")
add_occ("Piotrowczykówna", "Katarzyna", "Kraśnik", 359, 1754, "Katarzyna Piotrowczykówna", "Otrzymująca 4 miary pszenicy z polecenia pana wójta")
add_occ("Panek", "Antoni", "Kraśnik", 359, 1754, "Antoni Panek", "Spierający się z Matyaszem Piotrowczykiem pod chałupą o pszenicę")
add_occ("Piotrowczyk", "Matyasz", "Kraśnik", 359, 1754, "Matyasz Piotrowczyk", "Odmawiający przyjęcia pszenicy spod chałupy od Antoniego Panka")
add_occ("Laska", "Józef", "Kraśnik", 359, 1754, "Jozef Laska", "Czwarty świadek 25 X 1754 r. zeznający o oddaniu 20 złp długu Augustynowi")
add_occ("Kilianek", "Stanisław", "Kraśnik", 359, 1754, "nieboszczyk Stanisław Kilianek", "Zmarły dzielący się 20 złp z Augustynem Piotrowczykiem na Mszę św.")
add_occ("Piotrowczykowa", "Augustynowa", "Kraśnik", 359, 1754, "Augustynowa Piotrowczykowa de gente Zdybionka", "Wdowa z domu Zdyb nieobecna przy odbiorze 20 złp i 12 złp", "de gente Zdybionka")
add_occ("Wolak", "Stanisław", "Przedmieście Kraśnickie", 359, 1754, "Stanisław Wolak", "Piąty świadek zeznający o oddaniu 12 złp reszty z ćwierci Kiliankowskiej")

# SKAN 360 (1754)
add_occ("Zandel", "Adam", "Kraśnik", 360, 1754, "Adam Zandel", "Powód przeciw Szymonowi Szankiewiczowi, nabywca i naprawca dworu kolarzów")
add_occ("Szankiewicz", "Szymon", "Kraśnik", 360, 1754, "Simon Szankiewicz Cons: Cras:", "Rajca kraśnicki podający się w Lublinie za Wielkopolanina w rozmowie z kapitanem", None, "Rajca miejski")
add_occ("Tokarz", "Antoni", "Kraśnik", 360, 1754, "Antonius Tokarz Consul Cras:", "Rajca zeznający o pobycie w Lublinie w 1753 r. z kapitanem Gomulińskim")
add_occ("Gomuliński", "Piotr", "Kraśnik", 360, 1754, "Jmci Pan Gomuliński Kapitan", "Kapitan rozmawiający w Lublinie z Szankiewiczem o stancji w Kraśniku", None, "Kapitan / Porucznik")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 360, 1754, "Lucas Krzeszowski Cons: Cras:", "Rajca zeznający o rozmowach Szankiewicza z kapitanem i rachowaniu pieniędzy")
add_occ("Posuniak", "Adam", "Kraśnik", 360, 1754, "Adamus Posuniak", "Powód 30 X 1754 r. przeciw Łukaszowi Krzeszowskiemu")
add_occ("Fruga", "Matyasz", "Kraśnik", 360, 1754, "Matyasz Fruga", "Świadek 30 X 1754 r. kłótni Adamowej Posuniakowej z Łukaszem Krzeszowskim")
add_occ("Posuniakowa", "Adamowa", "Kraśnik", 360, 1754, "Adamowa Posuniakowa", "Żona Adama Posuniaka kłócąca się z Łukaszem Krzeszowskim")

# SKAN 361 (1754)
add_occ("Krzeszowska", "Łukaszowa", "Kraśnik", 361, 1754, "Łukaszowa Krzeszowska", "Współuczestniczka kłótni z Adamem Posuniakiem")
add_occ("Posuniak", "Adam", "Kraśnik", 361, 1754, "Adam Posuniak", "Rzucający się z pięścią do Łukasza Krzeszowskiego po obrazie ojca")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 361, 1754, "Łukasz Krzeszowski", "Zaatakowany słownie i pięścią przez Adama Posuniaka")
add_occ("Panek", "Antoni", "Kraśnik", 361, 1754, "Antonius Panek", "Powód przeciw Matyaszowi Piotrowczykowi o testament ojca")
add_occ("Piotrowczyk", "Matyasz", "Kraśnik", 361, 1754, "Matyasz Piotrowczyk", "Najstarszy syn z pierwszego małżeństwa obecny przy testamencie Augustyna")
add_occ("Szubertowski", "Jan", "Kraśnik", 361, 1754, "Joannes Szubertowski", "Ławnik spisujący z urzędu testament Augustyna Piotrowczyka")
add_occ("Pitaszkiewicz", "Antoni", "Kraśnik", 361, 1754, "Anto: Pitaszkiewicz", "Wysłany przez deputowanych po syna Matyasza przed spisaniem testamentu")
add_occ("Piotrowski", "Augustyn", "Kraśnik", 361, 1754, "Augustyn Piotrowczyk", "Testator oddający wszystko żonie i dziatkom ze spłodzonym małżeństwem")

# SKAN 362 (1754)
add_occ("Nowacki", "Szymon", "Kraśnik", 362, 1754, "Szymon Nowacki", "Sprawca bójki z Janem Tokarzem u Welusia, uciekający przed aresztem")
add_occ("Tokarz", "Jan", "Kraśnik", 362, 1754, "Jan Tokarz", "Uczestnik bójki z Nowackim o pęcherz i paciorki")
add_occ("Szubertowski", "Jan", "Kraśnik", 362, 1754, "Jan Szubertowski", "Ławnik doprowadzający Nowackiego do wójta i trzeci świadek w sprawie")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 362, 1754, "Łukasz Krzeszowski", "Skarżący się wójtowi na bunty i chałasy Szymona Nowackiego")

# SKAN 363 (1754)
add_occ("Nowacki", "Szymon", "Kraśnik", 363, 1754, "Nowacki", "Skazany przez wójta, lecz ułaskawiony na prośbę Pana Prezydenta")
add_occ("Bryszkiewicz", "Stanisław", "Kraśnik", 363, 1754, "Stanislaus Bryszkiewicz", "Powód przeciw Janowi Wróblowi i jego żonie o awanturę w komorze")
add_occ("Wróbel", "Jan", "Kraśnik", 363, 1754, "Joannes Wrubel", "Pozwany przez Stanisława Bryszkiewicza")
add_occ("Panek", "Antoni", "Kraśnik", 363, 1754, "Antoniy Panek", "Świadek kłótni żony Jana Wróbla z żoną Stanisława Bryszkiewicza o rzepę")
add_occ("Wróblowa", "Janowa", "Kraśnik", 363, 1754, "żona Jana Wróbla", "Spierająca się z Bryszkiewiczową o wyganianie prosiąt i kaczek w rzepę")
add_occ("Bryszkiewiczowa", "Stanisławowa", "Kraśnik", 363, 1754, "żona Stanisława Bryszkiewicza", "Wyzwana przez Janową Wróblową podczas sporu w komorze")

# SKAN 364 (1754)
add_occ("Bryszkiewicz", "Stanisław", "Kraśnik", 364, 1754, "Stanisław Bryszkiewicz", "Broniący żony w sporze z Janem Wróblem o konia na trawie i podatki")
add_occ("Wróbel", "Jan", "Kraśnik", 364, 1754, "Jan Wrubel", "Grożący Bryszkiewiczowi z koniem i zapowiadający skargę do komisarza")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 364, 1754, "Symon Krzeszowski", "Świadek kłótni Jakuba Wróbla z Stanisławem Bryszkiewiczem")
add_occ("Wróbel", "Jakub", "Kraśnik", 364, 1754, "Jakub Wrubel", "Kłócący się ze Stanisławem Bryszkiewiczem")
add_occ("Wróbel", "Wawrzyniec", "Kraśnik", 364, 1754, "Laurentius Wrubel", "Powód przeciw Stanisławowi Bryszkiewiczowi")
add_occ("Posuniak", "Adam", "Kraśnik", 364, 1754, "Adamus Posuniak", "Świadek kłótni Wawrzyńcowej Wróblowej z Bryszkiewiczową na ustępie")
add_occ("Wróblowa", "Wawrzyńcowa", "Kraśnik", 364, 1754, "żona Wawrzyńca Wrubla", "Kłócąca się z Bryszkiewiczową na ustępie")
add_occ("Bryszkiewiczowa", "Stanisławowa", "Kraśnik", 364, 1754, "Bryszkiewiczowa", "Kłócąca się z Wawrzyńcową Wróblową")

# SKAN 365 (1754)
add_occ("Bryszkiewiczowa", "Stanisławowa", "Kraśnik", 365, 1754, "Bryszkiewiczowa", "Nazywająca Wawrzyńcową Wróblową czarownicą")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 365, 1754, "Lucas Krzeszowski", "Powód 17 X 1754 r. w sprawie zajścia u Welusia")
add_occ("Pizik", "Mateusz", "Stróża / Kraśnik", 365, 1754, "Matheus Pizik ex Stróża subditus", "Poddany ze Stróży zeznający 17 X 1754 r. o ucieczce Nowackiego z gałęzią", "Pezik?")
add_occ("Weluś", "Żyd", "Kraśnik", 365, 1754, "niewierny Weluś", "Gospodarz żydowski, u którego wybuchła bójka")
add_occ("Kędzierzowa", "Szynkarka", "Kraśnik", 365, 1754, "szynkarka Kędzierowa", "Szynkarka przynosząca wyrwane włosy do izby po pomoc", None, "Szynkarka")
add_occ("Nowacki", "Szymon", "Kraśnik", 365, 1754, "Szymon Nowacki", "Uciekający przed sługą miejskim na tarni pod fórką z gałęzią")
add_occ("Piotrowczyk", "Matyasz", "Kraśnik", 365, 1754, "Mathias Piotrowczyk", "Powód w zeznaniu Hiacynta Łysaka z Sulowa")
add_occ("Łysak", "Hiacynt", "Sulów / Kraśnik", 365, 1754, "Chiacinti Łysak ex villa Sulow", "Poddany ze wsi Sulów zeznający w sprawie Matyasza Piotrowczyka")

# SKAN 366 (1754)
add_occ("Nowacki", "Szymon", "Kraśnik", 366, 1754, "Symon Nowacki", "Powód przeciw burmistrzowi Łukaszowi Krzeszowskiemu o zajście u Welusia")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 366, 1754, "Lucas Krzeszowski Cons: Cras:", "Pozwany przez Szymona Nowackiego")
add_occ("Krzemianowski", "Jakub", "Kraśnik", 366, 1754, "Jakub Krzemianowski", "Świadek pijący piwo w kuchni u Welusia Berkowicza z Tokarzem i Nowackim", "Kośmierzowski?")
add_occ("Weluś", "Żyd", "Kraśnik", 366, 1754, "niewierny Weluś Berkowicz", "Właściciel gospody (Weluś Berkowicz)", "Berkowicz")
add_occ("Tokarz", "Jan", "Kraśnik", 366, 1754, "Jan Tokarz / Tokarczyk", "Szturchający Nowackiego w brodę podczas sporu o paciorki")
add_occ("Wróbel", "Jakub", "Kraśnik", 366, 1754, "Jakobus Wrubel", "Powód przeciw Stanisławowi Bryszkiewiczowi o zniesławienie w stodole")
add_occ("Bryszkiewicz", "Stanisław", "Kraśnik", 366, 1754, "Stanislaus Bryszkiewicz", "Pozwany przez Jakuba Wróbla")
add_occ("Orłowski", "Mikołaj", "Kraśnik", 366, 1754, "Nicolaus Orłowski juvenis", "Pierwszy świadek słyszący zwadę Bryszkiewiczowej z Jakubem Wróblem w stodole")
add_occ("Bryszkiewiczowa", "Stanisławowa", "Kraśnik", 366, 1754, "Bryszkiewiczowa", "Kłócąca się z Jakubem Wróblem w stodole gospodarskiej")

# SKAN 367 (1754)
add_occ("Orłowski", "Mikołaj", "Kraśnik", 367, 1754, "Nicolaus Orłowski", "Dokończenie zeznania o wyzwiskach w stodole przy parobku młynarskim")
add_occ("Bryszkiewiczowa", "Stanisławowa", "Kraśnik", 367, 1754, "Bryszkiewiczowa", "Wyzywająca matkę Jakuba Wróbla od czarownic")
add_occ("Wróbel", "Jakub", "Kraśnik", 367, 1754, "Jakub Wrubel", "Pijący piwo w gospodzie Dawida z siostrą Anny Mielczarskiej")
add_occ("Mielczarska", "Anna", "Kraśnik", 367, 1754, "Anna Mielczarska", "Druga świadek zeznająca o swojej siostrze Mariannie u Dawida")
add_occ("Mielczarska", "Marianna", "Kraśnik", 367, 1754, "Marianna", "Siostra Anny Mielczarskiej pijąca piwo u Żyda Dawida")
add_occ("Dawid", "Żyd", "Kraśnik", 367, 1754, "niewierny Dawid", "Właściciel gospody, w której przebywała Marianna Mielczarska")

# SKAN 368 (1754)
add_occ("Bryszkiewiczowa", "Stanisławowa", "Kraśnik", 368, 1754, "Bryszkiewiczowa", "Wspomniana w dokończeniu zeznania Anny Mielczarskiej")
add_occ("Wróbel", "Jakub", "Kraśnik", 368, 1754, "Jakub Wrubel", "Wspomniany w dokończeniu zeznania Anny Mielczarskiej")
add_occ("Zajowski", "Szymon", "Kraśnik", 368, 1754, "Szymon Zaiowski kunsztu szewskiego magister", "Mistrz szewski skarżący 26 XI 1754 r. cechmistrza Wojciecha Potokowicza o pobicie", "Zaiowski?", "Mistrz szewski")
add_occ("Potokowicz", "Wojciech", "Kraśnik", 368, 1754, "Woyciech Potokowicz cechmistrz szewski", "Cechmistrz szewski pozwany 26 XI 1754 r. o uderzenie w gębę i targanie za łeb", None, "Cechmistrz szewski")

# SKAN 369 (1754)
add_occ("Potokowiczowa", "Jadwiga", "Kraśnik", 369, 1754, "Jadwiga Potokowiczowa Piotra Potokowicza żona", "Skarżąca 26 XI 1754 r. Antoniego Okonia o oplucie i pchnięcie w błoto u Żydówki", "Potocka?")
add_occ("Potokowicz", "Piotr", "Kraśnik", 369, 1754, "Piotr Potokowicz", "Mąż Jadwigi Potokowiczowej (26 XI 1754)")
add_occ("Okoń", "Antoni", "Kraśnik", 369, 1754, "Antoni Okoń", "Pozwany przez Jadwigę Potokowiczową oraz skarżący ją o zniewagę żony")
add_occ("Okoniowa", "Antoniowa", "Kraśnik", 369, 1754, "Protestanta żona", "Żona Antoniego Okonia nazwana „bestią” przez Piotrową Potokowiczową")

# SKAN 370 (1754)
add_occ("Potokowiczowa", "Jadwiga", "Kraśnik", 370, 1754, "Piotrowa Potocka", "Oskarżona przez Okonia o pomówienie jego żony o kradzież płótna", "Potocka?")
add_occ("Okoniowa", "Antoniowa", "Kraśnik", 370, 1754, "Protestantki żona", "Oczyszczona z zarzutu kradzieży płótna przez wizję sądową")
add_occ("Okoń", "Antoni", "Kraśnik", 370, 1754, "Antoni Okoń kunsztu szewskiego magister", "Mistrz szewski żądający 26 XI 1754 r. rewizji własnego domu", None, "Mistrz szewski")
add_occ("Buś", "Wojciech", "Kraśnik", 370, 1754, "Woyciech Bus", "Manifestujący 26 XI 1754 r. przeciw ławnikowi Szymonowi Krzeszowskiemu o tatarkę", "Bus?")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 370, 1754, "Szymon Krzeszowski ławnik", "Ławnik pozwany przez Wojciecha Busia w sprawie tatarki")
add_occ("Szaliczyński", "Antoni", "Kraśnik", 370, 1754, "Ant: Szaliczyński ławnik kras:", "Ławnik dokonujący rewizji w domu Antoniego Okonia", None, "Ławnik")
add_occ("Krzyżanowski", "Michał", "Kraśnik", 370, 1754, "Michał Krzyżanowski not: jurat: Cras:", "Pisarz przysięgły kraśnicki obecny na wizji w domu Antoniego Okonia", None, "Pisarz przysięgły")

# SKAN 371 (1754)
add_occ("Rzepka", "Stanisław", "Wilkołaz / Kraśnik", 371, 1754, "Stanisław Rzepka poddany z Wilkołaza Wiel:", "Poddany z Wilkołaza skarżący 2 XII 1754 r. Jana Tokarczyka o worki i pobicie")
add_occ("Tokarczyk", "Jan", "Przedmieście Kraśnickie", 371, 1754, "Jan Tokarczyk przedmieszczanin kras:", "Skazany 2 XII 1754 r. na zwrot 2 worków, 4 grzywny i więzienie")
add_occ("Pełka", "Łukasz", "Kraśnik", 371, 1754, "Łukasz Pełka", "Powód 11 XII 1754 r. przeciw bratu Wojciechowi Pełce", "Petka?")
add_occ("Pełka", "Wojciech", "Kraśnik", 371, 1754, "Woyciech Pełka", "Brat Łukasza Pełki pozwany 11 XII 1754 r.", "Petka?")

# SKAN 372 (1754)
add_occ("Pełka", "Łukasz", "Kraśnik", 372, 1754, "Łukasz Pełka", "Godzący się z bratem Wojciechem 11 XII 1754 r. w sprawie porąbanego pługa", "Petka?")
add_occ("Pełka", "Wojciech", "Kraśnik", 372, 1754, "Woyciech Pełka", "Godzący się z bratem Łukaszem 11 XII 1754 r.", "Petka?")
add_occ("Jorgiel", "Walenty", "Kraśnik", 372, 1754, "Valentinus Jorgiel", "Powód 13 XII 1754 r. przeciw Grzegorzowi Jurdzikowi o kradzież jęczmienia", "Gorgiel? / Jordel?")
add_occ("Jurdzik", "Grzegorz", "Kraśnik", 372, 1754, "Gregorius Jurdzik", "Zastany o świcie w stodole Jorgiela z niemłóconym jęczmieniem")
add_occ("Grzonka", "Grzegorz", "Kraśnik", 372, 1754, "Gregorius Grzonka", "Świadek młócący jęczmień u Walentego Jorgiela 13 XII 1754 r.")

# SKAN 373 (1754)
add_occ("Grzonka", "Grzegorz", "Kraśnik", 373, 1754, "Grzegorz", "Dokończenie zeznania o szukaniu 23 brakujących snopków w komorze Jurdzika")
add_occ("Jorgiel", "Walenty", "Kraśnik", 373, 1754, "Walenty Jorgiel", "Wypatrujący przez szparę snopka jęczmienia w komorze Jurdzika", "Gorgiel? / Jordel?")
add_occ("Jurdzik", "Grzegorz", "Kraśnik", 373, 1754, "Jurdzik", "Tłumaczący zaginięciem klucza u dziewki przed otwarciem komory")

# SKAN 374 (1754)
add_occ("Jorgiel", "Walenty", "Kraśnik", 374, 1754, "Jorgiel", "Odbierający snopek jęczmienia po otwarciu komory Jurdzika", "Gorgiel? / Jordel?")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 374, 1754, "Szymon Krzeszowski", "Powód 13 XII 1754 r. o szkody w zbożu od bydła i koni")
add_occ("Łysy", "Jan", "Kraśnik", 374, 1754, "Jan Łysy", "Pozwany 13 XII 1754 r. przez Szymona Krzeszowskiego o szkody w zbożu")
add_occ("Wiaterek", "Matyasz", "Przedmieście Kraśnickie", 374, 1754, "Maty: Witerka", "Pozwany 13 XII 1754 r. przez Szymona Krzeszowskiego o szkody w zbożu", "Witerka?")
add_occ("Buś", "Wojciech", "Kraśnik", 374, 1754, "Woyciech Buś", "Pozwany 13 XII 1754 r. przez Szymona Krzeszowskiego o szkody w zbożu", "Bus?")
add_occ("Zimnik", "Jakub", "Kraśnik", 374, 1754, "Jakub Zimnik", "Pozwany 13 XII 1754 r. przez Szymona Krzeszowskiego o szkody w zbożu")
add_occ("Wiaterek", "Wojciech", "Przedmieście Kraśnickie", 374, 1754, "Woyciech Wiatrek", "Brat Jana Wiaterka domagający się spłaty z testamentu ojca 13 XII 1754 r.")
add_occ("Wiaterek", "Jan", "Przedmieście Kraśnickie", 374, 1754, "Jan Wiatrek", "Brat Wojciecha Wiaterka zobowiązany do spłaty według testamentu ojca")

# SKAN 375 (1754)
add_occ("Wiaterek", "Jan", "Przedmieście Kraśnickie", 375, 1754, "Jan Wiatrek", "Skazany 13 XII 1754 r. na dopłatę 5 złp reszty z 20 złp bratu pod rygorem więzienia")
add_occ("Wiaterek", "Wojciech", "Przedmieście Kraśnickie", 375, 1754, "Brat jego", "Odbierający zasądzone 5 złp reszty od brata Jana")
add_occ("Pełka", "Łukasz", "Kraśnik", 375, 1754, "Łukasz Petka", "Brat rodzony Wojciecha Pełki zawierający ugodę przyjacielską 13 XII 1754 r.", "Petka?")
add_occ("Pełka", "Wojciech", "Kraśnik", 375, 1754, "Woyciech Petka", "Brat rodzony Łukasza Pełki darujący połowę grzywien i pretensje", "Petka?")
add_occ("Jurdzik", "Grzegorz", "Kraśnik", 375, 1754, "Gregorius Jurdzik", "Świadek 13 XII 1754 r. na ugodzie przyjacielskiej braci Pełków")

# Przeliczenie agregatów (Wariant 2)
for idx, p in enumerate(persons, 1):
    p['lp'] = idx
    p['wystapienia'] = sorted(p['wystapienia'], key=lambda w: int(w['skan']))
    skany = [int(w['skan']) for w in p['wystapienia']]
    lata = sorted(set(str(w['rok']) for w in p['wystapienia']))
    p['skany_list'] = skany
    p['skany_roboczo'] = ", ".join(str(s) for s in skany)
    p['zakres_lat'] = lata[0] if len(lata) == 1 else f"{lata[0]}–{lata[-1]}"
    p['liczba_wystapien'] = len(p['wystapienia'])

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part15.json', 'w', encoding='utf-8') as f:
    json.dump(persons, f, ensure_ascii=False, indent=2)

# Eksport CSV UTF-8-SIG z separatorem ; oraz 9 kanonicznymi kolumnami z SKILL.md
csv_path = '/home/ubuntu/workspace/Gen/krasnik_j17_slownik_genealogiczny.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Lp', 'Nazwisko', 'Imię', 'Miejsce', 'Funkcja społeczna / zawód', 'Skany źródłowe', 'Zakres lat', 'Liczba wzmianek', 'Warianty nazwiska'])
    for p in persons:
        writer.writerow([
            p['lp'],
            p['nazwisko'],
            p['imie'],
            p['miejsce'],
            p.get('funkcja') or '',
            p['skany_roboczo'],
            p['zakres_lat'],
            p['liczba_wystapien'],
            p.get('wariant_nazwiska') or ''
        ])

print(f"SUCCESS: gen_data_j17_part15.json ({len(persons)} profiles) and CSV exported.")
