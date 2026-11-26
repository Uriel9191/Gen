# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part27.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_count = "<li><span>👥</span> <strong>1747</strong> unikalnych profili</li>"
new_count = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_count in html, "Nie znaleziono licznika 1747 w index.html!"
html = html.replace(old_count, new_count, 1)

old_bullet1 = "Partie 1–26: skany 1–650, fol. 1r–319r; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
new_bullet1 = "Partie 1–27: skany 1–675, fol. 1r–330v; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
assert old_bullet1 in html, "Nie znaleziono bullet1 w index.html!"
html = html.replace(old_bullet1, new_bullet1, 1)

anchor_end = "o konfesaty poddanych (skany 649–650)."
add_part27 = anchor_end + "<br>\n              • Pijarzy opolscy, dzieje młyna podmiejskiego i spory 1758 r. (skany 651–675): protestacja prokuratora <strong>ks. Ferdynanda z zakonu Ojców Pijarów w Opolu</strong> przeciw ławnikowi Adamowi Kadle o 1 czerwony złoty i 20 tynfów na rezydencję (skan 665), wielowątkowa inkwizycja o historię młyna pod gontem przy chacie Bryśkiewicza, wielką powódź i inwestycje ławnika <strong>Jana Lubartowskiego</strong> (skany 666–667, 670–671), konfirmacja długu 100 złp przez wdowę <strong>Małgorzatę Marszałkowską</strong> (skany 657–658) oraz spór cechmistrza <strong>Kazimierza Młynarskiego</strong> i procesy przedmiejskie (skany 672–675)."
assert anchor_end in html, "Nie znaleziono anchor_end w index.html!"
html = html.replace(anchor_end, add_part27, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
