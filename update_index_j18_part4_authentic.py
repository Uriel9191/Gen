# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part4.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–3: skany 1–75 z 221"
new_part = "Partie 1–4: skany 1–100 z 221"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>75</strong> / 221 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>100</strong> / 221 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>244</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "pobitego <strong>Tomasza Zięby</strong> (#75)."
add_p4 = anchor_end + "<br>\n              • Koniec 1701 r. i Elekcja Magistratu 1702 r. (skany 76–100): przysięga żydowska na rodał w bożnicy (#76–#77), apelacja do Trybunału Zamoyskiego (#78–#79), najazd na dwór w Wilkołazie (#87–#88) i zamknięcie akt 1701 r. przez wójta <strong>Stanisława Maziewskiego</strong> (#88), wielka kalkulacja skarbowa miasta na <strong>4922 fl 6 gr 6 szel</strong> oraz elekcja magistratu na <strong>1702 r.</strong> z wójtem <strong>Pawłem Słomkowskim</strong> i prokonsulem <strong>Wawrzyńcem Pielaszkowicem</strong> (#89–#97), inwentarz dokumentów z lat 1690–1702 (#96) oraz pierwsze dekrety z stycznia 1702 r. (#98–#100)."
assert anchor_end in html, f"Missing anchor_end"
html = html.replace(anchor_end, add_p4, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J18 Partia 4 ({len(gen_data)} profili)")
