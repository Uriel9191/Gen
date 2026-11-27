# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part8.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–7: skany 1–175 z 283"
new_part = "Partie 1–8: skany 1–200 z 283"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>175</strong> / 283 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>200</strong> / 283 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>656</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "(#155, #172–#175)."
add_p8 = anchor_end + "<br>\n              • Październik 1698 i fascykuł 1664 (skany 176–200): rozliczenia wódki prostej z Żydem <strong>Wygdorem Markowiczem</strong> (#178–#179, #184), czynsze woskowe <strong>Bractwa Literackiego</strong> (#185), bójka rajcy <strong>Jana Barankowicza</strong> u <strong>Borucha alias Halki</strong> (#182–#183, #189–#190, #198), zeznania świadków w procesie po wójcie <strong>Janaszkowiczu</strong> (#195–#197), spór o sieczkę dla żołnierzy (#199) oraz otwarcie fascykułu z <strong>1664 r.</strong> (#200)."
assert anchor_end in html, "Missing anchor_end"
html = html.replace(anchor_end, add_p8, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J20 Partia 8 ({len(gen_data)} profili)")
