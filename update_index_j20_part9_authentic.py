# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part9.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–8: skany 1–200 z 283"
new_part = "Partie 1–9: skany 1–225 z 283"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>200</strong> / 283 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>225</strong> / 283 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>727</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "otwarcie fascykułu z <strong>1664 r.</strong> (#200)."
add_p9 = anchor_end + "<br>\n              • Fascykuł 1664 i kwiecień–październik 1698 (skany 201–225): ugoda <strong>Jajczyków</strong> na 220 złp i włamanie do komory (#201–#203), rewizja cechu kuśnierskiego (#204), sprawa dziesiętnika <strong>Pawła Kłopota</strong> (#208–#210), kantor synagogi <strong>Izaak</strong> (#214), wyrok dla wdowy <strong>Elżbiety Okoniowej</strong> (#215–#216), sprzedaż roli <strong>Dubaja</strong> (#218), kompromis <strong>Studzickich</strong> i <strong>Stachowiców</strong> (#221–#224) oraz łaciński hymn maryjny (#225)."
assert anchor_end in html, "Missing anchor_end"
html = html.replace(anchor_end, add_p9, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J20 Partia 9 ({len(gen_data)} profili)")
