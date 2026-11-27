# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part2.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partia 1: skany 1–25 z 120"
new_part = "Partie 1–2: skany 1–50 z 120"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>25</strong> / 120 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>50</strong> / 120 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>62</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "oraz folwarku za Bramą Lubelską przez <strong>Stanisława Nawrockiego</strong> (#24–#25)."
add_p2 = anchor_end + "<br>\n              • Jesień 1657 – styczeń 1659 r. (skany 26–50): <em>Laudum Commune Czopowe</em> (#30–#31), przyjęcie prawa miejskiego przez <strong>Adama Kapicę</strong> (#34), elekcje magistratu z lat <strong>1658 i 1659</strong> z udziałem komisarza <strong>Krzysztofa Brzostowskiego</strong> (#38–#39, #50), proces o <strong>arszenik</strong> <strong>Jadwigi Wroniny</strong> (#42–#43), inwentarz warsztatu kołodziejskiego (#44), sprzedaż roli na Podlesiu za <code>160 złp</code> (#46–#47) oraz domu przy ul. Lubelskiej za <code>150 złp</code> (#49)."
assert anchor_end in html, f"Missing anchor_end"
html = html.replace(anchor_end, add_p2, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J19 Partia 2 ({len(gen_data)} profili)")
