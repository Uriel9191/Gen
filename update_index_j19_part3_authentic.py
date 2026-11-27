# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j19_part3.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–2: skany 1–50 z 120"
new_part = "Partie 1–3: skany 1–75 z 120"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>50</strong> / 120 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>75</strong> / 120 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>137</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "oraz domu przy ul. Lubelskiej za <code>150 złp</code> (#49)."
add_p3 = anchor_end + "<br>\n              • Luty 1659 – sierpień 1660 r. (skany 51–75): dublet elekcji 1659 (#51), protestacja burmistrza <strong>Macieja Tharasy</strong> przeciw rajcy <strong>Marcinowi Sitarskiemu</strong> (#57), polska protestacja pisarza <strong>Jana Cichonia</strong> (#58–#59), elekcja 1660 r. (#64–#65), <em>Laudum Pasienia trzody</em> (#68–#69), kwitacja Żydów lubelskich po zabójstwie we wsi <strong>Lipa</strong> (#72–#73) oraz początek <em>Laudum o liquorach</em> (#75)."
assert anchor_end in html, "Missing anchor_end"
html = html.replace(anchor_end, add_p3, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J19 Partia 3 ({len(gen_data)} profili)")
