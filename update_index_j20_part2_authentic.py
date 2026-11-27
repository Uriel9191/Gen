# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part2.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partia 1: skany 1–25 z 283"
new_part = "Partie 1–2: skany 1–50 z 283"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>25</strong> / 283 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>50</strong> / 283 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>106</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "za rozmowę po niemiecku (#18)."
add_p2 = anchor_end + "<br>\n              • Grudzień 1657 – listopad 1658 r. (skany 26–50): proces <strong>Andrzeja Marlika [?]</strong> z <strong>Zofią Zielińską [?]</strong> o <code>200 złp</code> (#26–#28), zapis wyderkafowy <strong>Macieja Konięgi</strong> na kamienicy przy Rynku na <code>100 złp</code> (#36–#37), sprawy przed Sądem Podstarościego (#34, #40), kradzież jabłek z sadu ławnika <strong>Augustyna Kurowica</strong> (#45–#46, #50) oraz zeznania poddanych ze wsi <strong>Ślinów [Słodków?]</strong> (#42–#43, #46–#50)."
assert anchor_end in html, "Missing anchor_end"
html = html.replace(anchor_end, add_p2, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J20 Partia 2 ({len(gen_data)} profili)")
