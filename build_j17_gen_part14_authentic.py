# -*- coding: utf-8 -*-
import json
import csv

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part13.json', 'r', encoding='utf-8') as f:
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

# SKAN 326 (1753)
add_occ("Tokarczyk", "Antoni", "Kraśnik", 326, 1753, "Antoni Tokarczyk", "Uczestnik bójki z Aleksandrem Bujarskim w gospodzie", None, "Rajca / Mieszczanin")
add_occ("Szubertowski", "Jan", "Kraśnik", 326, 1753, "Jan Szubertowski", "Uczestnik bójki w gospodzie, nazwany „mielnikiem” przez Bujarskiego")
add_occ("Bujarski", "Aleksander", "Kraśnik", 326, 1753, "Alexander Bujarski", "Uczestnik bójki w gospodzie z Tokarczykiem i Szubertowskim")
add_occ("Bujarski", "Antoni", "Kraśnik", 326, 1753, "Antoni Bujarski", "Syn Aleksandra Bujarskiego w sporze słownym w gospodzie")
add_occ("Macutki", "Łukasz", "Kraśnik", 326, 1753, "Lucas Macutki", "Drugi świadek bójki w gospodzie obecny z Panem Organistą", "Macut?")

# SKAN 327 (1753)
add_occ("Macutki", "Łukasz", "Kraśnik", 327, 1753, "Lucas Macutki", "Dokończenie zeznań o bójce w gospodzie między Bujarskimi a Tokarczykiem", "Macut?")
add_occ("Bujarski", "Antoni", "Kraśnik", 327, 1753, "Antoni Bujarski", "Broniący ojca Aleksandra w trakcie bójki w gospodzie")
add_occ("Bujarski", "Aleksander", "Kraśnik", 327, 1753, "Alexander Bujarski", "Współuczestnik bójki w sieni i pod gankiem")
add_occ("Tokarczyk", "Antoni", "Kraśnik", 327, 1753, "Antoni Tokarczyk", "Uczestnik bójki z Bujarskimi w gospodzie")
add_occ("Szubertowski", "Jan", "Kraśnik", 327, 1753, "Jan Szubertowski", "Uczestnik bójki z Bujarskimi w gospodzie")
add_occ("Malinowski", "Jan", "Kraśnik", 327, 1753, "Joannes Malinowski", "Trzeci świadek zeznający z relacji żony o bójce w gospodzie")
add_occ("Cełc", "Matyasz", "Kraśnik", 327, 1753, "Matyasz Cełc", "Delator i gospodarz wnoszący skargę na Szymona Wójcika (29 XI 1753)", "Calc?")
add_occ("Wójcik", "Szymon", "Przedmieście Kraśnickie", 327, 1753, "Szymon Woycik", "Obwiniony 29 XI 1753 r. o występek obyczajowy z Jakubową Krasowską")
add_occ("Krasowska", "Jakubowa", "Kraśnik", 327, 1753, "Jakubowa", "Wdowa obwiniona o występek z Szymonem Wójcikiem", None, "Wdowa")

# SKAN 328 (1753-1754)
add_occ("Krasowska", "Jakubowa", "Kraśnik", 328, 1753, "Jakubowa Krasowska wdowa", "Skazana 29 XI 1753 r. na 200 plag cielesnych i wyświecenie z miasta")
add_occ("Wójcik", "Szymon", "Przedmieście Kraśnickie", 328, 1753, "Szymon Woycik", "Skazany 29 XI 1753 r. na 100 plag kańczugiem i 3 dni leżenia krzyżem")
add_occ("Cełc", "Matyasz", "Kraśnik", 328, 1753, "Matyasz Cełc", "Skazany na 10 grzywien i 3 dni więzienia za spóźnione doniesienie", "Calc?")
add_occ("Morel", "Marcin", "Kraśnik", 328, 1754, "Marcin Morel", "Mistrz cechu tkackiego wnoszący inkwizycję 2 I 1754 r.", None, "Mistrz cechu tkackiego")
add_occ("Łatosiewicz", "Antoni", "Kraśnik", 328, 1754, "Antoni Łatosiewicz Wicecechmistrz", "Wicecechmistrz cechu tkackiego obecny na sesji 2 I 1754 r.", None, "Wicecechmistrz tkacki")
add_occ("Zdybkiewicz", "Michał", "Kraśnik", 328, 1754, "Michał Zdybkiewicz", "Brat cechowy tkacki obecny na sesji 2 I 1754 r.")
add_occ("Wróbel", "Wawrzyniec", "Kraśnik", 328, 1754, "Wawrzyniec Wróbel", "Ojciec starający się o wyzwoliny syna Jakuba do cechu tkackiego (6 złp)")
add_occ("Wróbel", "Jakub", "Kraśnik", 328, 1754, "Jakub", "Syn Wawrzyńca Wróbla zgłaszany do wyzwolin w cechu tkackim", None, "Czeladnik / Uczeń tkacki")

# SKAN 329 (1754)
add_occ("Wróbel", "Wawrzyniec", "Kraśnik", 329, 1754, "Wróbel", "Spierający się w cechu tkackim o 2 talary bite od syna Jakuba")
add_occ("Wróbel", "Jakub", "Kraśnik", 329, 1754, "Jakub", "Syn Wawrzyńca Wróbla wyzwalany w cechu tkackim")
add_occ("Łatosiewicz", "Antoni", "Kraśnik", 329, 1754, "Antoni Łatosiewicz", "Podcechmistrz odbierający klucz od skarbu cechowego")
add_occ("Morel", "Marcin", "Kraśnik", 329, 1754, "Marcin Morel", "Spierający się z cechmistrzem i Krasowskim w cechu tkackim")
add_occ("Krasowski", "Tomasz", "Kraśnik", 329, 1754, "Tomasz Krasowski", "Brat cechowy wstawiający się za Wawrzyńcem Wróblem")
add_occ("Pitaszkiewicz", "Grzegorz", "Kraśnik", 329, 1754, "Grzegorz Pielaskiewicz", "Powód w inkwizycji 3 I 1754 r. w sprawie Anny Jaździkówny", "Pielaskiewicz?")
add_occ("Maciejowski", "Szymon", "Kraśnik", 329, 1754, "Szymon Maciejowski", "Parobek gościnny zeznający 3 I 1754 r. o Annie Jaździkównie i Szafrańskim", None, "Parobek gościnny")
add_occ("Jazdzikówna", "Anna", "Kraśnik", 329, 1754, "Anna Jazdzikowna", "Obserwowana na muzyce i w drodze do stodoły młynarskiej w 1753 r.")
add_occ("Szafrański", "Stanisław", "Kraśnik", 329, 1754, "Szafrański", "Obserwowany z Anną Jaździkówną w 1753 r.")
add_occ("Potokowicz", "Wojciech", "Kraśnik", 329, 1754, "Woyciech Potokowicz", "Świadek spotkania na ulicy przed wyjazdem do Urzędowa")

# SKAN 330 (1754)
add_occ("Morel", "Marcin", "Kraśnik", 330, 1754, "Martinus Morel", "Powód 4 I 1754 r. i pozwany 9 I 1754 r. w sprawach cechu tkackiego")
add_occ("Łatosiewicz", "Antoni", "Kraśnik", 330, 1754, "Antoniy Łatosiewicz", "Drugi świadek 4 I 1754 r. w sprawie cechu tkackiego")
add_occ("Wróbel", "Wawrzyniec", "Kraśnik", 330, 1754, "Wawrzyniec Wróbel", "Wspomniany w zeznaniu Łatosiewicza z 4 I 1754 r.")
add_occ("Macała", "Matyasz", "Kraśnik", 330, 1754, "Matyasz Macała", "Członek cechu tkackiego przywołany jako świadek 4 I 1754 r.")
add_occ("Fruga", "Matyasz", "Kraśnik", 330, 1754, "Mathias Fruga", "Powód 9 I 1754 r. przeciw Szymonowi Krzeszowskiemu o partanki i sierp")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 330, 1754, "Symon Krzeszowski", "Pozwany 9 I 1754 r. przez Matyasza Frugę")
add_occ("Szubertowski", "Jan", "Kraśnik", 330, 1754, "Joannes Szubertowski", "Ławnik i pierwszy świadek 9 I 1754 r. w sprawie Fruga vs Krzeszowski")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 330, 1754, "Lucas Krzeszowski", "Powód 9 I 1754 r. przeciw Marcinowi Morelowi")
add_occ("Macutki", "Łukasz", "Kraśnik", 330, 1754, "Lucas Macut", "Pierwszy świadek 9 I 1754 r. w sprawie Krzeszowski vs Morel", "Macut?")

# SKAN 331 (1754)
add_occ("Macutki", "Łukasz", "Kraśnik", 331, 1754, "Lucas Macut", "Zeznający o spotkaniu z Marcinem Morelem w drodze na kolację do cechmistrza", "Macut?")
add_occ("Morel", "Marcin", "Kraśnik", 331, 1754, "Marcin Morel", "Krytykujący cechmistrza i skarżący się w gospodzie u Struszki")
add_occ("Kawecki", "Jan", "Kraśnik", 331, 1754, "Janek Kawecki", "Młodszy brat cechowy proszący Macuta do cechu")
add_occ("Szubertowski", "Jan", "Kraśnik", 331, 1754, "Januszek Szubrowski", "Młodszy brat cechowy towarzyszący Jankowi Kaweckiemu", "Szubrowski?")
add_occ("Łatosiewicz", "Antoni", "Kraśnik", 331, 1754, "Antoniy Łatosiewicz", "Drugi świadek rozmowy Morela z Łukaszową Krzeszowską u Struszki")
add_occ("Krzeszowska", "Łukaszowa", "Kraśnik", 331, 1754, "Łukaszowa Krzeszowska", "Żona cechmistrza broniąca się przed zarzutami Morela u Struszki")

# SKAN 332 (1754)
add_occ("Czupiński", "Wojciech", "Kraśnik", 332, 1754, "Woyciech Crupiński", "Świadek uderzenia Łukasza Traca przez Antoniego Okonia przy porachunku", "Crupiński?")
add_occ("Okoń", "Antoni", "Kraśnik", 332, 1754, "Antoni Okoń", "Uderzający Łukasza Traca laską na gospodzie i podsieniu")
add_occ("Trac", "Łukasz", "Kraśnik", 332, 1754, "Łukasz Trac", "Pobity przez Antoniego Okonia przy porachunku", "Szac?")
add_occ("Bonecki", "Krzysztof", "Kraśnik", 332, 1754, "Krzysztof Bonecki", "Świadek pobicia Łukasza Traca na gospodzie i podsieniu")
add_occ("Morel", "Marcin", "Kraśnik", 332, 1754, "Martinus Morel", "Powód 11 I 1754 r. przeciw Łukaszowi Krzeszowskiemu")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 332, 1754, "Lucas Krzeszowski", "Pozwany 11 I 1754 r. przez Marcina Morela")
add_occ("Krasowski", "Tomasz", "Kraśnik", 332, 1754, "Tomas Krasowski", "Świadek kłótni na ustępie między Morelem a Łukaszową Krzeszowską")
add_occ("Krzeszowska", "Łukaszowa", "Kraśnik", 332, 1754, "Łukaszowa Krzeszowska", "Spierająca się z Morelem o spódnicę zadłową kupioną u Dąbrowskiej")
add_occ("Zdybkiewicz", "Michał", "Kraśnik", 332, 1754, "Michał Zdybkiewicz", "Drugi świadek kłótni na ustępie między Morelem a Krzeszowską")
add_occ("Fruga", "Matyasz", "Kraśnik", 332, 1754, "Mathias Fruga", "Wnioskujący inkwizycję na dole fol. 163r")

# SKAN 333 (1754)
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 333, 1754, "Lucas Krzeszowski", "Powód 18 I i 22 I 1754 r. przeciw Marcinowi Morelowi")
add_occ("Morel", "Marcin", "Kraśnik", 333, 1754, "Marcin Morel", "Oskarżony o obrazę prawa cechowego („jebał pies prawo”)")
add_occ("Szubertowski", "Jan", "Kraśnik", 333, 1754, "Joannes Szubertowski", "Świadek 18 I 1754 r. rozmowy Morela z Łatosiewiczem u Struszki")
add_occ("Łatosiewicz", "Antoni", "Kraśnik", 333, 1754, "Antoni Łatosiewicz", "Rozmówca Marcina Morela w gospodzie u Struszki 18 I 1754 r.")
add_occ("Krzeszowska", "Łukaszowa", "Kraśnik", 333, 1754, "Łukaszowa Krzeszowska", "Uczestniczka sporu w gospodzie u Struszki")
add_occ("Kawecki", "Antoni", "Kraśnik", 333, 1754, "Antonius Kawecki", "Świadek 22 I 1754 r. w sprawie Krzeszowski vs Morel")
add_occ("Krzeszowski", "Tomasz", "Kraśnik", 333, 1754, "Tomasz Krzeszowski", "Wspomniany w zeznaniu Antoniego Kaweckiego z 22 I 1754 r.")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 333, 1754, "Szymon Krzeszowski", "Wspomniany w zeznaniu Antoniego Kaweckiego z 22 I 1754 r.")
add_occ("Zdybkiewicz", "Michał", "Kraśnik", 333, 1754, "Michał Zdybkiewicz", "Drugi świadek 22 I 1754 r. potwierdzający słowa Kaweckiego")
add_occ("Fruga", "Matyasz", "Kraśnik", 333, 1754, "Mathias Fruga", "Powód przeciw Michałowi Biegajowi")
add_occ("Biegaj", "Michał", "Kraśnik", 333, 1754, "Michaël Bielgus", "Mieszczanin kraśnicki pozwany przez Matyasza Frugę", "Biegus? / Bielgus?")
add_occ("Piotrowczyk", "Andrzej", "Kraśnik", 333, 1754, "Andreas Piotrowczyk", "Pierwszy świadek zeznający o pożyczonej płachcie u Mikołaja Biegaja")
add_occ("Biegaj", "Mikołaj", "Przedmieście Kraśnickie", 333, 1754, "Mikołaj Biegaj", "Pożyczający płachtę i strona sporów sąsiedzkich")
add_occ("Czupiński", "Józef", "Kraśnik", 333, 1754, "Josephus Crupiński", "Drugi świadek w sprawie Fruga vs Biegaj", "Crupiński?")

# SKAN 334 (1754)
add_occ("Czupiński", "Józef", "Kraśnik", 334, 1754, "Josephus Crupiński", "Świadek zeznający przed sądem o Mikołaju Biegaju", "Crupiński?")
add_occ("Biegaj", "Mikołaj", "Przedmieście Kraśnickie", 334, 1754, "Nicolaus Biegay", "Strona inkwizycji przeciw Matyaszowi Frudze")
add_occ("Kuładza", "Matyasz", "Kraśnik", 334, 1754, "Matyasz Kuładza", "Zeznający o 20 złp danych Matyaszowi Jędrzejowi na jarmark do Kraśnika", "Kuładzy?")
add_occ("Szubertowski", "Jan", "Kraśnik", 334, 1754, "Joannes Szubertowski", "Świadek zeznający z ramienia Mikołaja Biegaja o Frugę i Morela")
add_occ("Fruga", "Matyasz", "Kraśnik", 334, 1754, "Matyasz Fruga", "Rozmówca Morela i strona ugody za 15 złp")
add_occ("Morel", "Marcin", "Kraśnik", 334, 1754, "Martinus Morel", "Świadek zeznający przed krucyfiksem o ugodzie Frugi przy Żydzie gorzałczanym")
add_occ("Morel", "Jan", "Kraśnik", 334, 1754, "Jan Morel", "Świadek przygodny ugody Matyasza Frugi za 15 złp")
add_occ("Jaździk", "Józef", "Kraśnik", 334, 1754, "Jozef Jazdzik", "Świadek przygodny ugody Matyasza Frugi za 15 złp")
add_occ("Wiaterek", "Matyasz", "Przedmieście Kraśnickie", 334, 1754, "Mathias Wieterek", "Powód 6 III 1754 r. przeciw Sebastianowi Pawlickiemu", "Wieterek?")
add_occ("Pawlicki", "Sebastian", "Kraśnik", 334, 1754, "Sebastianus Pawlicki", "Pozwany 6 III 1754 r. przez Matyasza Wiaterka o zajście w lesie")
add_occ("Wiaterek", "Antoni", "Przedmieście Kraśnickie", 334, 1754, "Antonius Wieterek", "Pierwszy świadek 6 III 1754 r. w sprawie Pawlickiego", "Wieterek?")

# SKAN 335 (1754)
add_occ("Wiaterek", "Antoni", "Przedmieście Kraśnickie", 335, 1754, "Antonius Wieterek", "Dokończenie zeznania o zwadzie i wyzwiskach w lesie", "Wieterek?")
add_occ("Fruga", "Matyasz", "Kraśnik", 335, 1754, "Mathias Fruga", "Powód w interrogatoriach przeciw Józefowi Czaplińskiemu")
add_occ("Czapliński", "Józef", "Kraśnik", 335, 1754, "Josephus Czaplinski", "Pozwany przez Matyasza Frugę")
add_occ("Michalska", "Szymonowa", "Kraśnik", 335, 1754, "Szymonowa Michalska", "Świadek zeznający o lnie przyniesionym w kapie i uszytej zapasce")
add_occ("Patek", "Józef", "Kraśnik", 335, 1754, "Josephus Patek", "Powód w inkwizycji przeciw Matyaszowi Frudze", "Pątek?")
add_occ("Marczewicz", "Andrzej", "Kraśnik", 335, 1754, "Andreas Marczewic", "Świadek w sprawie Józefa Patka przeciw Matyaszowi Frudze")
add_occ("Mech", "Jan", "Kraśnik", 335, 1754, "Jan Mech", "Oskarżony 9 IV 1754 r. i skazany na 200 plag oraz wyświecenie z miasta")
add_occ("Zdybkówna", "Marianna", "Kraśnik", 335, 1754, "Marianna Zdybkowa", "Skazana 9 IV 1754 r. na 200 plag i wyświecenie z miasta za cudzołóstwo z Janem Mechem")
add_occ("Strusiek", "Moszek", "Kraśnik", 335, 1754, "Mosiek Strusiek Żyd", "Gospodarz, u którego zastano Jana Mecha i Mariannę Zdybkównę", None, "Gospodarz / Obywatel żydowski")
add_occ("Mech", "Regina", "Kraśnik", 335, 1754, "Regina prawowita żona", "Żona Jana Mecha obecna przy ujęciu oskarżonych 9 IV 1754 r.")
add_occ("Brudny", "Tomasz", "Kraśnik", 335, 1754, "Tomasz Brudny winiarz kraśnicki", "Winiarz kraśnicki uczestniczący w ujęciu oskarżonych 9 IV 1754 r.", None, "Winiarz kraśnicki")
add_occ("Sadoska", "Petronela", "Kraśnik", 335, 1754, "Petronella Sadoska", "Powódka 17 IV 1754 r. przeciw Stanisławowi Szankiewiczowi o klucz")
add_occ("Szankiewicz", "Stanisław", "Kraśnik", 335, 1754, "Stanislaus Szankiewicz", "Pozwany 17 IV 1754 r. przez Petronelę Sadoską")
add_occ("Orłowski", "Kasper", "Kraśnik", 335, 1754, "Gaspar Orłowski", "Świadek rozmowy na rezydencji u Szankiewicza 17 IV 1754 r.")
add_occ("Zdybkówna", "Agnieszka", "Kraśnik", 335, 1754, "Agnieszka Zdybkowna", "Świadek zeznający 17 IV 1754 r. o wyjściu Sadoskiej z Szankiewiczową")

# SKAN 336 (1754)
add_occ("Sokierunka", "Paweł", "Kraśnik", 336, 1754, "Paulus Sokierunka non uxoratus", "Kawaler będący stroną inkwizycji 17 IV 1754 r.")
add_occ("Michorek", "Walenty", "Kraśnik", 336, 1754, "Valentinus Michorek", "Świadek w sprawie Pawła Sokierunki (17 IV 1754 r.)", "Michoń?")
add_occ("Zdęb", "Marcin", "Kraśnik", 336, 1754, "Martinus Zdeb", "Powód 22 IV 1754 r. przeciw Wojciechowi Drozdowi")
add_occ("Drozd", "Wojciech", "Kraśnik", 336, 1754, "Adalbertus Drozd", "Pozwany 22 IV 1754 r. o porwanie Maćka Zdęba za czuprynę")
add_occ("Cełc", "Matyasz", "Kraśnik", 336, 1754, "Mathias Cełc", "Pierwszy świadek 22 IV 1754 r. w sprawie Zdęb vs Drozd", "Calc?")
add_occ("Tokarczyk", "Antoni", "Kraśnik", 336, 1754, "Antoni Tokarczyk", "Rzucił snopek z karczmy w sprawie z 22 IV 1754 r.")
add_occ("Zdęb", "Maciej", "Kraśnik", 336, 1754, "Maciek Zdęb", "Pochwycony za czuprynę przez Wojciecha Drozda")
add_occ("Jurdzik", "Józef", "Kraśnik", 336, 1754, "Josephus Jurdzik", "Powód 9 VI 1754 r.")
add_occ("Piotroska", "Helena", "Kraśnik", 336, 1754, "Helena Piotroska", "Świadek 9 VI 1754 r. w sprawie Józefa i Jędrzeja Jurdzików")
add_occ("Jurdzik", "Jędrzej", "Kraśnik", 336, 1754, "Jędrzey Jurdzik", "Wspomniany w zeznaniu Heleny Piotroskiej 9 VI 1754 r.")
add_occ("Tokarski", "Wawrzyniec", "Kraśnik", 336, 1754, "Laurentius Tokarski", "Świadek zeznający w sprawie Kaspra Żyda i arendarza miejskiego")
add_occ("Posuniak", "Wawrzyniec", "Kraśnik", 336, 1754, "Laurentius Posuniak", "Powód 25 VI 1754 r. przeciw Adamowi Posuniakowi")
add_occ("Posuniak", "Adam", "Kraśnik", 336, 1754, "Adamus Posuniak", "Żądający 4 złp reszty od brata Wawrzyńca Posuniaka")
add_occ("Potokowicz", "Wojciech", "Kraśnik", 336, 1754, "Adalbertus Potokowicz", "Świadek poselstwa między braćmi Posuniakami 25 VI 1754 r.")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 336, 1754, "Lucas Krzeszowski", "Powód 28 VI 1754 r. przeciw Marcinowi Morelowi o cielę")
add_occ("Morel", "Marcin", "Kraśnik", 336, 1754, "Martinus Morel", "Zajmujący cielę Banasiewiczowej na swym owsie 28 VI 1754 r.")
add_occ("Jurdzik", "Wawrzyniec", "Kraśnik", 336, 1754, "Laurentius Jurdzik", "Świadek 28 VI 1754 r. zajścia o cielę między Morelem a Banasiewiczową")
add_occ("Banasiewiczowa", "Wojciechowa", "Kraśnik", 336, 1754, "Woyciechowa Banasiewiczowa", "Wdowa prosząca Morela o oddanie własnego cielęcia", None, "Wdowa")

# SKAN 337 (1754)
add_occ("Banasiewiczowa", "Wojciechowa", "Kraśnik", 337, 1754, "Woyciechowa", "Uderzona kijem po łopatkach przez Marcina Morela przy odbiorze cielęcia")
add_occ("Morel", "Marcin", "Kraśnik", 337, 1754, "Marcin Morel", "Prowadzący cielę podleską drogą do domu")
add_occ("Tokarski", "Kazimierz", "Kraśnik", 337, 1754, "Casimirus Tokarski", "Drugi świadek widzący w kuźni u Wieterka prowadzone cielę")
add_occ("Wiaterek", "Wojciech", "Przedmieście Kraśnickie", 337, 1754, "Woyciech Wieterek", "Kowal, w którego kuźni przebywał Kazimierz Tokarski i Pitaszkiewicz", "Wieterek?", "Kowal")
add_occ("Pitaszkiewicz", "Grzegorz", "Kraśnik", 337, 1754, "Grzegorz Pitaszkiewicz", "Świadek obecny w kuźni Wojciecha Wieterka", "Pielaskiewicz?")
add_occ("Piotrowczyk", "Andrzej", "Kraśnik", 337, 1754, "Andreas Piotrowczyk", "Powód przeciw Antoniemu Pankowi o przeoranie gruntu")
add_occ("Panek", "Antoni", "Kraśnik", 337, 1754, "Antonius Panek", "Pozwany przez Andrzeja Piotrowczyka o przeoranie miedzy")
add_occ("Rymarczyk", "Łukasz", "Kraśnik", 337, 1754, "Lucas Rymarczyk", "Pierwszy świadek sporu na polu między Piotrowczykiem a Pankiem")
add_occ("Szubertowski", "Jan", "Kraśnik", 337, 1754, "Joannes Szubertowski Scabinus", "Ławnik deputowany z urzędu na wizję przeoranego gruntu", None, "Ławnik")
add_occ("Piotrowczyk", "Matyasz", "Kraśnik", 337, 1754, "Matyasz Piotrowczyk", "Obecny na gruncie przy nadejściu deputowanych urzędowych")

# SKAN 338 (1754)
add_occ("Szubertowski", "Jan", "Kraśnik", 338, 1754, "Joannes Szubertowski", "Zeznający o najemnikach Matyasza Frugi przeorujących jęczmień")
add_occ("Fruga", "Matyasz", "Kraśnik", 338, 1754, "Matyasz Fruga", "Zleceniodawca najemników z pasieki przeorujących pługiem jęczmień")
add_occ("Piotrowska", "Szymonowa", "Kraśnik", 338, 1754, "Szymonowa Piotrowska", "Protestująca przeciw przechodzeniu z pługiem przez jęczmień")
add_occ("Piotrowczyk", "Andrzej", "Kraśnik", 338, 1754, "Jędrzey Piotrowczyk", "Strona wizji i pomiaru pól przeciw Antoniemu Pankowi")
add_occ("Panek", "Antoni", "Kraśnik", 338, 1754, "Antonius Panek", "Strona pomiaru pól i rozgraniczenia z Piotrowczykiem")
add_occ("Pankowa", "Antoniowa", "Kraśnik", 338, 1754, "Pankowa", "Kłócąca się z Jędrzejem Piotrowczykiem podczas pomiaru gruntu")
add_occ("Tokarczyk", "Antoni", "Kraśnik", 338, 1754, "Antoni Tokarczyk", "Obecny przy drugiej wizji polowej i sporze o rowek")

# SKAN 339 (1754)
add_occ("Morel", "Marcin", "Kraśnik", 339, 1754, "Martinus Morel", "Powód przeciw Łukaszowi Krzeszowskiemu")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 339, 1754, "Lucas Krzeszowski", "Pozwany przez Marcina Morela")
add_occ("Pałka", "Łukasz", "Kraśnik", 339, 1754, "Lucas Pałka", "Świadek zeznający o zajściu w gospodzie u Żyda Berka", "Patka?")
add_occ("Berek", "Żyd", "Kraśnik", 339, 1754, "Żyd Berek", "Właściciel gospody, w której przebywała żona Krzeszowskiego", None, "Gospodarz / Obywatel żydowski")
add_occ("Krzeszowska", "Łukaszowa", "Kraśnik", 339, 1754, "żona Łukasza Krzeszowskiego", "Obecna w gospodzie u Żyda Berka")
add_occ("Panek", "Antoni", "Kraśnik", 339, 1754, "Antonius Panek", "Powód 12 VII 1754 r. przeciw Andrzejowi Piotrowczykowi")
add_occ("Piotrowczyk", "Andrzej", "Kraśnik", 339, 1754, "Andreas Piotrowczyk", "Pozwany 12 VII 1754 r. przez Antoniego Panka")
add_occ("Tokarczyk", "Antoni", "Kraśnik", 339, 1754, "Antonius Tokarczyk", "Świadek 12 VII 1754 r. słów Panka po odejściu z urzędu")
add_occ("Szaliczyński", "Antoni", "Kraśnik", 339, 1754, "Antonius Szaliczyński", "Powód przeciw Adamowi Posuniakowi o zapłatę za pracę")
add_occ("Posuniak", "Adam", "Kraśnik", 339, 1754, "Adamus Posuniak", "Żądający zapłaty za pracę od Antoniego Szaliczyńskiego")
add_occ("Moszek", "Świadek", "Kraśnik", 339, 1754, "Infidelis Moszek", "Świadek zeznający w sprawie Szaliczyński vs Posuniak", None, "Obywatel żydowski")
add_occ("Piotrowczyk", "Matyasz", "Kraśnik", 339, 1754, "Mathias Piotrowczyk", "Powód przeciw Antoniemu Pankowi o rozliczenia po Augustynie Piotrowskim")
add_occ("Kraskowski", "Bartłomiej", "Kraśnik", 339, 1754, "Bartolomeus Kraskowski", "Świadek zeznający o pożyczce 30 złp na wołu i śmierci Augustyna w Zamościu", "Krasowski?")
add_occ("Olechowski", "Szymon", "Kraśnik", 339, 1754, "Szymon Olechowski", "Teść Augustyna Piotrowskiego udzielający mu pożyczki 30 złp na wołu", "Ołechowski?")
add_occ("Piotrowski", "Augustyn", "Kraśnik", 339, 1754, "Augustyn Piotrowski", "Zięć Olechowskiego, zmarły i pochowany w Zamościu przez tamtejszego ślusarza")

# SKAN 340 (1754)
add_occ("Piotrowski", "Augustyn", "Kraśnik", 340, 1754, "Augustyn", "Wspomniany przy wykupie ogrodu za 30 złp i spłacie skryptu ślusarzowi")
add_occ("Panek", "Antoni", "Kraśnik", 340, 1754, "Antonius Panek", "Powód 24 VII 1754 r. przeciw Matyaszowi Piotrowczykowi")
add_occ("Piotrowczyk", "Matyasz", "Kraśnik", 340, 1754, "Mathias Piotrowczyk", "Brat Andrzeja Piotrowczyka pozwany 24 VII 1754 r. przez Panka")
add_occ("Piotrowczyk", "Andrzej", "Kraśnik", 340, 1754, "Andreas Piotrowczyk", "Świadek 24 VII 1754 r. rozmowy ze starszym bratem Matyaszem oraz właściciel koni")
add_occ("Wróbel", "Jakub", "Kraśnik", 340, 1754, "Jakobus Wrubel", "Powód w inkwizycji przeciw pozwanym o szkody końskie")
add_occ("Jurdzik", "Grzegorz", "Kraśnik", 340, 1754, "Gregorius Jurdzik", "Świadek zeznający o widzeniu koni we wsi")
add_occ("Wiaterek", "Jan", "Przedmieście Kraśnickie", 340, 1754, "Jan Wiatrek", "Właściciel koni widzianych we wsi w sprawie Jakuba Wróbla", "Wieterek?")
add_occ("Kraskowski", "Andrzej", "Kraśnik", 340, 1754, "Andrzey Kraskowski", "Właściciel koni widzianych we wsi w sprawie Jakuba Wróbla")

# SKAN 341 (1754) - suplika zbiorowa Miasta z Pospólstwem (brak indywidualnych nazwisk)

# SKAN 342 (1754)
add_occ("Gomuliński", "Piotr", "Kraśnik", 342, 1754, "Piotr Gomuliński Porucznik", "Porucznik infanterii buławy wielkiej koronnej wnoszący inkwizycję 15 IV 1754 r.", None, "Porucznik infanterii buławy wielkiej koronnej")
add_occ("Wierzbicki", "Ignacy", "Kraśnik", 342, 1754, "Ignatij Wierzbicki", "Pierwszy świadek 15 IV 1754 r. zeznający o groźbie podpalenia przez Adama Radłę")
add_occ("Radło", "Adam", "Kraśnik", 342, 1754, "Adam Radło", "Obwiniony 15 IV 1754 r. o groźbę spalenia domostwa mimo powrotu Hetmana")
add_occ("Łuczewicz", "Antoni", "Kraśnik", 342, 1754, "Antoni Łuczewicz", "Drugi świadek 15 IV 1754 r. słyszący groźbę Adama Radła w sieni", "Kuźmiewicz?")
add_occ("Fruga", "Matyasz", "Kraśnik", 342, 1754, "Mathias Fruga", "Powód 17–18 V 1754 r. przeciw Szymonowi Krzeszowskiemu")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 342, 1754, "Symon Krzeszowski", "Pozwany o szkatułkę brata Łukasza (17 V) i szkody bydła (18 V)")
add_occ("Szubertowski", "Jan", "Kraśnik", 342, 1754, "Joannes Szubertowski", "Świadek 17 V 1754 r. kłótni braci Krzeszowskich o szkatułkę")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 342, 1754, "Łukasz Krzeszowski", "Spierający się z bratem Szymonem o szkatułkę (17 V 1754)")
add_occ("Koza", "Józef", "Kraśnik", 342, 1754, "Josephus Koza", "Mieszkaniec kraśnicki zeznający 18 V 1754 r. o pasieniu bydła Krzeszowskiego na niwkach Frugi")

# SKAN 343 (1754)
add_occ("Koza", "Józef", "Kraśnik", 343, 1754, "świadek", "Dokończenie zeznania o wyganianiu bydła ze szkody")
add_occ("Morel", "Marcin", "Kraśnik", 343, 1754, "Martinus Morel", "Powód i pozwany 21 V 1754 r. w sporach z braćmi Krzeszowskimi")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 343, 1754, "Łukasz Krzeszowski Burmistrz y Cechmistrz", "Burmistrz i cechmistrz cechu tkackiego pozwany o płótno za 8 złp wyrobione przez córkę", None, "Burmistrz i cechmistrz cechu tkackiego")
add_occ("Szubertowski", "Jan", "Kraśnik", 343, 1754, "Joannes Szubertowski Scabinus", "Ławnik zeznający 21 V 1754 r. w sprawie Morela i Łukasza Krzeszowskiego")
add_occ("Łatosiewicz", "Antoni", "Kraśnik", 343, 1754, "Antoni Łatosiewicz", "Świadek obecny z Szubertowskim w gospodzie 21 V 1754 r.")
add_occ("Krzeszowski", "Szymon", "Kraśnik", 343, 1754, "Szymon Krzeszowski", "Powód 21 V 1754 r. przeciw Morelowi o zniewagę („ma urząd zaaresztowany”)")
add_occ("Tokarczyk", "Antoni", "Kraśnik", 343, 1754, "Antonius Tokarczyk Consul", "Rajca kraśnicki zeznający 21 V 1754 r. w sprawie Szymona Krzeszowskiego")
add_occ("Łatosiewicz", "Jan", "Kraśnik", 343, 1754, "Joannes Łatosiewicz", "Najęty przez Szymona Krzeszowskiego do orania pługiem w jęczmieniu")

# SKAN 344 (1754)
add_occ("Aaron", "Arendarz", "Kraśnik", 344, 1754, "Infidelis Aaron", "Żyd arendarz wnoszący inkwizycję 31 VII 1754 r.", None, "Arendarz żydowski")
add_occ("Zdęb", "Bartłomiej", "Kraśnik", 344, 1754, "Bartolomeus Zdeb", "Świadek 31 VII 1754 r. o maślance na wozie przy kościele")
add_occ("Posuniak", "Michał", "Kraśnik", 344, 1754, "Michael Posuniak", "Powód 21 VIII 1754 r. przeciw Walentemu Szafrańskiemu o pobicie żony")
add_occ("Szafrański", "Walenty", "Kraśnik", 344, 1754, "Valentinus Szafrański", "Pozwany 21 VIII 1754 r. o zniewagę Posuniaka i uderzenie jego żony w zęby")
add_occ("Kępa", "Andrzej", "Kraśnik", 344, 1754, "Andreas Kępa", "Świadek bójki w gospodzie szynkowanej przez swoją żonę 21 VIII 1754 r.")
add_occ("Młynarski", "Kazimierz", "Kraśnik", 344, 1754, "Kazimierz Młynarski Pisarz miejski", "Pisarz miejski wspomniany w skardze Kępy przed Posuniakiem", None, "Pisarz miejski")
add_occ("Posuniakowa", "Michałowa", "Kraśnik", 344, 1754, "żona Michała Posuniaka", "Uderzona w zęby przez Walentego Szafrańskiego w gospodzie")
add_occ("Potokowicz", "Grzegorz", "Kraśnik", 344, 1754, "Grzegorz Potokowicz", "Uderzający Szafrańskiego miotłą po plecach w obronie Posuniakowej")

# SKAN 345 (1754)
add_occ("Potokowicz", "Andrzej", "Kraśnik", 345, 1754, "Andreas Potokowicz", "Drugi świadek w sprawie Posuniaka przeciw Szafrańskiemu")
add_occ("Stachowicz", "Wojciech", "Kraśnik", 345, 1754, "Adalbertus Stachowicz", "Trzeci świadek w sprawie Posuniaka przeciw Szafrańskiemu")
add_occ("Zajowski", "Szymon", "Kraśnik", 345, 1754, "Szymon Zaiowski", "Czwarty świadek w sprawie Posuniaka przeciw Szafrańskiemu", "Zaiowski?")
add_occ("Kołtunowa", "Antoniowa", "Kraśnik", 345, 1754, "Antoniowa Kołtunowa", "Piąty świadek (ze strony Wawrzyńca Szafrańskiego)")
add_occ("Szafrański", "Wawrzyniec", "Kraśnik", 345, 1754, "Laurentius Szafrański", "Strona wskazująca świadka Antoniową Kołtunową")
add_occ("Morel", "Marcin", "Kraśnik", 345, 1754, "Martinus Morel", "Powód 20 IX 1754 r. przeciw ławnikowi Janowi Przesławskiemu")
add_occ("Przesławski", "Jan", "Kraśnik", 345, 1754, "Joannes Przesławski Scab. Cras.", "Ławnik kraśnicki pozwany 20 IX 1754 r. przez Marcina Morela", None, "Ławnik")
add_occ("Szubertowski", "Jan", "Kraśnik", 345, 1754, "Joannes Szubertowski Scab. Cras.", "Ławnik zeznający 20 IX 1754 r. o sporze Morela z Przesławskim")
add_occ("Szaliczyński", "Antoni", "Kraśnik", 345, 1754, "Antoniy Szaliczyński", "Drugi świadek 20 IX 1754 r. w sprawie Morel vs Przesławski")
add_occ("Fruga", "Matyasz", "Kraśnik", 345, 1754, "Mathias Fruga", "Powód 20 IX 1754 r. przeciw Antoniemu Kołtonowi o kupno śliwek")
add_occ("Kołton", "Antoni", "Kraśnik", 345, 1754, "Antonius Kołton", "Sprzedawca śliwek w sadzie za 14–15 złp", "Kołtun?")
add_occ("Potokowicz", "Wojciech", "Kraśnik", 345, 1754, "Adalbertus Potokowicz", "Świadek targu o śliwki między Frugą a Kołtonem")
add_occ("Kołtonowa", "Antoniowa", "Kraśnik", 345, 1754, "żona Antoniego Kołtona", "Zbierająca śliwki w sadzie przy targu z Matyaszem Frugą", "Kołtunowa?")

# SKAN 346 (1754)
add_occ("Kołton", "Antoni", "Kraśnik", 346, 1754, "Antoni Kołton", "Sprzedający śliwki ostatecznie Marcinowi Morelowi za 22 złp", "Kołtun?")
add_occ("Fruga", "Matyasz", "Kraśnik", 346, 1754, "Matyasz Fruga", "Niedoszły nabywca śliwek za 15 złp")
add_occ("Morel", "Marcin", "Kraśnik", 346, 1754, "Marcin Morel", "Przebijający ofertę na śliwki (22 złp) oraz przyjaciel Łukasza Pałki")
add_occ("Rachuniowa", "Powódka", "Kraśnik", 346, 1754, "Honesta Rachuniowa", "Powódka przeciw Kazimierzowi Młynarskiemu")
add_occ("Młynarski", "Kazimierz", "Kraśnik", 346, 1754, "Kazimierz Młynarski", "Pozwany przez Rachuniową o schadzki w ogrodzie młynarskim")
add_occ("Krasowski", "Tomasz", "Kraśnik", 346, 1754, "Tomasz Krasowski", "Pierwszy świadek zeznający w sprawie Rachuniowej przeciw Młynarskiemu")
add_occ("Tokarski", "Krzysztof", "Kraśnik", 346, 1754, "Krzysztof Tokarski", "Wspomniany przy spotkaniach na ogrodzie młynarskim")
add_occ("Bogdina", "Andrzejowa", "Kraśnik", 346, 1754, "Andrzejowa Bogdina", "Drugi świadek zeznający o schadzkach na jęczmieniu młynarskim", "Pogdina?")
add_occ("Kotlarz", "Aleksander", "Kraśnik", 346, 1754, "Alexander Kotlarz", "Zbrojarski, w którego sieni wymieniono świadków schadzek", None, "Kotlarz / Zbrojarski")
add_occ("Pałka", "Łukasz", "Kraśnik", 346, 1754, "Łukasz Pałka", "Pasierb Jakuba Bieleckiego zawierający ugodę o ćwierć borowską", "Patka?")
add_occ("Bielecki", "Jakub", "Kraśnik", 346, 1754, "Jakub Bielecki", "Ojczym Łukasza Pałki w sporze o ćwierć borowską")
add_occ("Tokarczyk", "Antoni", "Kraśnik", 346, 1754, "Antoni Tokarczyk", "Rozjemca zaproszony przez Łukasza Pałkę do Jakuba Bieleckiego")

# SKAN 347 (1754)
add_occ("Bielecki", "Jakub", "Kraśnik", 347, 1754, "Bielecki", "Ustępujący pasierbowi ćwierć borowską za 40 złp (w tym 16 złp gotówką)")
add_occ("Witkowski", "Wojciech", "Zamość / Kraśnik", 347, 1754, "Woyciech Witkowski", "Odbierający w Zamościu spłatę za żołnierza od Bieleckiego")
add_occ("Pałka", "Łukasz", "Kraśnik", 347, 1754, "Łukasz Pałka", "Płacący 16 złp ojczymowi przy ugodzie o ćwierć borowską", "Patka?")
add_occ("Wiaterek", "Wojciech", "Przedmieście Kraśnickie", 347, 1754, "Woyciech Witerek", "Świadek ugody między Adamem Radłem a Grzegorzem Pitaszkiewiczem o oranie", "Witerek?")
add_occ("Radło", "Adam", "Kraśnik", 347, 1754, "Adam Radło", "Oferujący 4 złp za oranie pola Radzieckiego i zapowiadający wyjazd do Zamościa")
add_occ("Pitaszkiewicz", "Grzegorz", "Kraśnik", 347, 1754, "Grzegorz Pitaszkiewicz", "Żądający 5–6 złp od Adama Radła za oranie pola z konsensu komisarza", "Pielaskiewicz?")
add_occ("Dzierznowski", "Komisarz", "Kraśnik / Ordynacja", 347, 1754, "JW. P. Komisarz Dzierznowski", "Komisarz ordynacji nadający konsens na pole zwane Radzieckie", "Dzierżanowski?", "Komisarz ordynacji")

# SKAN 348 (1754)
add_occ("Tkaczykówna", "Marianna", "Kraśnik", 348, 1754, "Marianna Tkaczykowna", "Panna poddana chłoście, która przyznała się do nierządu z malarzem i kucharzem")
add_occ("Dimeczewski", "Franciszek", "Kraśnik", 348, 1754, "Franciscus Dimeczewski", "Młodzieniec zeznający o spotkaniu z mistrzem Młynarskim i przeprowadzeniu dziewki przez płoty", "Dimczewski?")
add_occ("Młynarski", "Kazimierz", "Kraśnik", 348, 1754, "Kazimierz Młynarski", "Mistrz garbarski/sądowy skarżący się na malarza i kucharza w stodole")
add_occ("Fruga", "Matyasz", "Kraśnik", 348, 1754, "Matyasz Fruga", "Właściciel ogrodu, przez którego płoty przeniesiono Mariannę Tkaczykównę")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 348, 1754, "Lucas Krzeszowski Consul", "Rajca/burmistrz wnoszący inkwizycję 5 X 1754 r.", None, "Rajca / Burmistrz")
add_occ("Nowacki", "Szymon", "Kraśnik", 348, 1754, "Szymon Nowacki", "Pozwany 5 X 1754 r. w sprawie burmistrza Łukasza Krzeszowskiego")

# SKAN 349 (1754)
add_occ("Petrykowski", "Antoni", "Kraśnik", 349, 1754, "Antoniy Petrikowski", "Rajca kraśnicki zeznający pod sumieniem o bójce u Żyda Welusia", "Petrikowski?", "Rajca miejski")
add_occ("Weluś", "Żyd", "Kraśnik", 349, 1754, "niewierny Weluś", "Gospodarz żydowski, u którego doszło do bójki 5 X 1754 r.", None, "Gospodarz / Obywatel żydowski")
add_occ("Nowacki", "Szymon", "Kraśnik", 349, 1754, "Szymon Nowacki", "Targający za włosy Tokarza i ściskający pięść na Pana Prezydenta")
add_occ("Kołtun", "Antoni", "Kraśnik", 349, 1754, "Antoniy Kołtun", "Drugi świadek bójki przy kuchni u Żyda Welusia (spór o łyżki)")
add_occ("Kwiatkowski", "Marcin", "Kraśnik", 349, 1754, "Marcin Kwiatkowski", "Leżący w sieni na Jakubie Tokarzu podczas bójki u Welusia")
add_occ("Tokarz", "Jakub", "Kraśnik", 349, 1754, "J. Tokarz", "Targany za włosy przez Szymona Nowackiego w sieni u Welusia")
add_occ("Krzeszowski", "Łukasz", "Kraśnik", 349, 1754, "Łukasz Krzeszowski Burmistrz", "Burmistrz pijący w izbie u Welusia przed wybuchem bójki")
add_occ("Radło", "Adam", "Kraśnik", 349, 1754, "Adam Radło", "Obecny z burmistrzem Krzeszowskim w izbie u Welusia")
add_occ("Tokarz", "Jan", "Kraśnik", 349, 1754, "Jan Tokarz", "Wchodzący do kuchni u Welusia z Szymonem Nowackim")

# SKAN 350 (1754)
add_occ("Marczukowski", "Szymon", "Kraśnik", 350, 1754, "Symon Marczukowski Advocatus et Judex", "Wójt i sędzia kraśnicki wnoszący skargę przeciw podchorążemu Skowrońskiemu", "Marmutowski?", "Wójt i sędzia kraśnicki")
add_occ("Skowroński", "Podchorąży", "Kraśnik", 350, 1754, "Magnificus Skowronski subVexilifer", "Podchorąży piechoty pozwany przez wójta Marczukowskiego", None, "Podchorąży piechoty")
add_occ("Panek", "Piotr", "Urzędów / Kraśnik", 350, 1754, "Petrus Panek Incola Urzędoviensis", "Mieszkaniec Urzędowa zeznający o groźbach żołnierzy wobec Wójta u Kali")
add_occ("Kala", "Żydówka", "Kraśnik", 350, 1754, "niewierna Kala", "Właścicielka gospody, w której żołnierze grozili odbiciem więźniów", None, "Gospodyni / Obywatelka żydowska")

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

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part14.json', 'w', encoding='utf-8') as f:
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

print(f"SUCCESS: gen_data_j17_part14.json ({len(persons)} profiles) and CSV exported.")
