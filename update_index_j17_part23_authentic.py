# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part23.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_count = "<li><span>👥</span> <strong>1557</strong> unikalnych profili</li>"
new_count = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_count in html, "Nie znaleziono licznika 1557 w index.html!"
html = html.replace(old_count, new_count, 1)

old_bullet1 = "Partie 1–22: skany 1–550, fol. 1r–268r; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1757"
new_bullet1 = "Partie 1–23: skany 1–575, fol. 1r–281v; lata 1651, 1694, 1700, 1726, 1729–1731, 1753–1757"
assert old_bullet1 in html, "Nie znaleziono bullet1 w index.html!"
html = html.replace(old_bullet1, new_bullet1, 1)

anchor_end = "oraz rewizja pożaru sadzy w kominie Gierszona Catowica (skany 545–546)."
add_part23 = anchor_end + "<br>\n              • Architektura, kodykologia i procesy 1756–1757 (skany 551–575): rewizja stanu ksiąg wieczystych i skrzyni aktowej przez wójta kraśnickiego (skany 559–560), własnoręcznie podpisana ugoda honorowa architekta klasztoru kraśnickiego <strong>Józefa Herbsta</strong> z burmistrzem Stanisławem Bryśkiewiczem (skan 573), proces obyczajowy żony Józefa Nowaka przeciw Pawłowi Frugie (skany 553–556), pretensje chłopów księcia Jabłonowskiego ze wsi Zakrzowa (skan 572) oraz rozliczenie jarmarczne Mikołaja Nowaka z Fejdlą Szyjową (skany 574–575)."
assert anchor_end in html, "Nie znaleziono anchor_end w index.html!"
html = html.replace(anchor_end, add_part23, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
