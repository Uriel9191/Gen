# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part28.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_count = "<li><span>👥</span> <strong>1783</strong> unikalnych profili</li>"
new_count = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_count in html, "Nie znaleziono licznika 1783 w index.html!"
html = html.replace(old_count, new_count, 1)

old_bullet1 = "Partie 1–27: skany 1–675, fol. 1r–330v; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
new_bullet1 = "Partie 1–28: skany 1–700, fol. 1r–343v; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
assert old_bullet1 in html, "Nie znaleziono bullet1 w index.html!"
html = html.replace(old_bullet1, new_bullet1, 1)

anchor_end = "i procesy przedmiejskie (skany 672–675)."
add_part28 = anchor_end + "<br>\n              • Spór cechmistrza Młynarskiego z deputatem Morelem, młyn żydowskich arendarzy i bójki przedmiejskie 1758 r. (skany 676–700): kondescensja gruntowa <strong>Matyasza Witcka</strong>, <strong>Mateusza Zdybła</strong> i <strong>Jakuba Zimniaka</strong> (skany 676–678), wieloetapowy proces cechmistrza szewskiego <strong>Kazimierza Młynarskiego</strong> z deputatem <strong>Marcinem Morelem</strong> (z apelacją do <strong>Trybunału Zamojskiego</strong>, skany 679–684, 689–691), manifestacja starozakonnego <strong>Hli Moszkowicza</strong> w imieniu arendarzy przeciw młynarzowi <strong>Janowi Szubertowskiemu</strong> (skan 686), sprawa testamentowej niwki wdowy <strong>Marianny Soteckiej</strong> (skany 687–690), spór <strong>Wojciecha Ciuci</strong> z <strong>Szymonem Wójcikiem</strong> o lichtarz (skany 692–696) oraz obdukcje przeciw sprawcom z <strong>Kierznicy (Kierzmyssy)</strong> i <strong>Antoniemu Pyrykowi</strong> (skany 697–700)."
assert anchor_end in html, "Nie znaleziono anchor_end w index.html!"
html = html.replace(anchor_end, add_part28, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
