# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part3.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–2: skany 1–50 z 283"
new_part = "Partie 1–3: skany 1–75 z 283"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>50</strong> / 283 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>75</strong> / 283 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>182</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "(#42–#43, #46–#50)."
add_p3 = anchor_end + "<br>\n              • Listopad–grudzień 1658 r. (skany 51–75): oryginalna suplika <strong>Wawrzyńca Prokopka</strong> przeciw <strong>Grzegorzowi Foxowi</strong> (#54–#55) i plenipotencja <strong>Ewy Koźmianowej</strong> do Trybunału Zamojskiego (#66), obdukcja <strong>Wawrzyńca Żydkowica</strong> (#68) oraz pełny inwentarz i proces spadkowy po <strong>Tomaszu Rzepce</strong> ze wsi <strong>Blinów</strong> (#70–#75)."
assert anchor_end in html, "Missing anchor_end"
html = html.replace(anchor_end, add_p3, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J20 Partia 3 ({len(gen_data)} profili)")
