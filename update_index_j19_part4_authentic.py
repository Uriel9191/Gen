# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part4.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–3: skany 1–75 z 120"
new_part = "Partie 1–4: skany 1–100 z 120"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>75</strong> / 120 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>100</strong> / 120 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>221</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "oraz początek <em>Laudum o liquorach</em> (#75)."
add_p4 = anchor_end + "<br>\n              • Sierpień 1660 – luty 1661 r. (skany 76–100): kalkulacja kosztów piwa (<code>20 złp</code>) i gorzałki (<code>26 złp 18 gr</code>) w <em>Laudum o liquorach</em> (#76–#77), spór czapników z Lublina i Szczebrzeszyna (#77–#78), konflikt <strong>Stanisława Nawrockiego</strong> z <strong>Wojciechem Szafrankowicem</strong> o folwark na Podlesiu (#83–#86), elekcja 1661 r. (#92) oraz proces <strong>Doroty Bybinej</strong> ze świadectwem zniszczeń z czasów <strong>Potopu Szwedzkiego</strong> (#96–#100)."
assert anchor_end in html, "Missing anchor_end"
html = html.replace(anchor_end, add_p4, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J19 Partia 4 ({len(gen_data)} profili)")
