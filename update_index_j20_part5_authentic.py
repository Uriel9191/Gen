# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part5.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–4: skany 1–100 z 283"
new_part = "Partie 1–5: skany 1–125 z 283"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>100</strong> / 283 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>125</strong> / 283 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>373</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "(#93–#99)."
add_p5 = anchor_end + "<br>\n              • Lata 1682–1684 (skany 101–125): oblata z Urzędowa o kupnie roli <em>Turek</em> przez <strong>Marcina Rymarczyka</strong> za <code>70 złp</code> (#103–#106), protestacja przeciw oskarżeniom o czary po pożarze młyna (#117, #124), sesja z 9 X 1684 r. datowana przed świętem <em>Wiktorii nad Turkami</em> (#118) oraz sprawa malarza <strong>Kazimierza Szartowskiego</strong> z mieszczaninem sandomierskim (#121–#122)."
assert anchor_end in html, "Missing anchor_end"
html = html.replace(anchor_end, add_p5, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J20 Partia 5 ({len(gen_data)} profili)")
