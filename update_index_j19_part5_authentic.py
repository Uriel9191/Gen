# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part5.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–4: skany 1–100 z 120"
new_part = "Komplet: 120 / 120 skanów (100%)"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>100</strong> / 120 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>120</strong> / 120 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>260</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "ze świadectwem zniszczeń z czasów <strong>Potopu Szwedzkiego</strong> (#96–#100)."
add_p5 = anchor_end + "<br>\n              • Luty – grudzień 1661 r. (skany 101–120, <strong>100% woluminu</strong>): intromisja na przedmieściu Piasek (#102), spory opiekuńcze <strong>Stanisława Pyrka</strong> (#107–#108) i <strong>Stanisława Łęckowica</strong> (#108–#110), pościg za czeladnikiem <strong>JMP Podchorodeńskiego</strong> (#111), dublet #113 = #112, <em>Proclamatio Novi Thelonei</em> z 29 XII 1661 r. (#118) oraz atestacja Sądu Pokoju z 1827 r. (#119)."
assert anchor_end in html, "Missing anchor_end"
html = html.replace(anchor_end, add_p5, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J19 Partia 5 / Komplet ({len(gen_data)} profili)")
