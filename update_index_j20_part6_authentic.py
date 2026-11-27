# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part6.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–5: skany 1–125 z 283"
new_part = "Partie 1–6: skany 1–150 z 283"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>125</strong> / 283 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>150</strong> / 283 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>461</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "(#121–#122)."
add_p6 = anchor_end + "<br>\n              • Lata 1684, 1686 i 1694–1697 (skany 126–150): pełna elekcja magistratu, ławy, egzaktorów i cechmistrzów z 12 I 1686 r. (#136–#137), poręczenie za <strong>Katarzynę Chmielównę</strong> (#138), ugoda sierot <strong>Piaseckich</strong> z 1695 r. (#143), sprawy ze wsi <strong>Sulów</strong> (#141, #147) oraz kontumacje żydowskie i mieszczańskie (#146–#150)."
assert anchor_end in html, "Missing anchor_end"
html = html.replace(anchor_end, add_p6, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J20 Partia 6 ({len(gen_data)} profili)")
