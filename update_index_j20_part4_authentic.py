# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part4.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–3: skany 1–75 z 283"
new_part = "Partie 1–4: skany 1–100 z 283"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>75</strong> / 283 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>100</strong> / 283 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>293</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "(#70–#75)."
add_p4 = anchor_end + "<br>\n              • Lata 1658, 1666–1668, 1681 i 1683 (skany 76–100): finał dekretu spadkowego wsi <strong>Blinów</strong> (#76–#81), kwitacja Konwentu Kanoników Regularnych na <code>100 złp</code> (#84–#85), proces o rękawik turecki z Żydem <strong>Mamelem</strong> (#82–#83), karta tytułowa i elekcja pisarza <strong>Jana Rogalowskiego</strong> z udziałem kahału (#91–#92) oraz wielka skarga byłego burmistrza <strong>Stanisława Nawrockiego</strong> przeciw <strong>Jakubowi Wardędze</strong> (#93–#99)."
assert anchor_end in html, "Missing anchor_end"
html = html.replace(anchor_end, add_p4, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J20 Partia 4 ({len(gen_data)} profili)")
