# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j20_part7.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = "Partie 1–6: skany 1–150 z 283"
new_part = "Partie 1–7: skany 1–175 z 283"
assert old_part in html, f"Missing {old_part}"
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>150</strong> / 283 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>175</strong> / 283 skanów archiwalnych</li>"
assert old_scans in html, f"Missing {old_scans}"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>563</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html, f"Missing {old_prof}"
html = html.replace(old_prof, new_prof, 1)

anchor_end = "(#146–#150)."
add_p7 = anchor_end + "<br>\n              • Rok 1698 (z wpisami 1694–1695, skany 151–175): obdukcje ran z cyrulikiem <strong>Mojżeszem Abramowicem</strong> (#160, #171), spory o rolę <strong>Tudorkowską</strong> (#161–#162) i zaginiony wóz podwodny do Zamościa (#162–#164, #166–#167), regestr spadkowy po <strong>Annie Kempionce [?]</strong> (#169) oraz proces o 802 złp 15 gr po wójcie <strong>Ubaldzie Janaszkowiczu</strong> między <strong>Pawłem Słomkowskim</strong> a <strong>Nowackimi</strong> (#155, #172–#175)."
assert anchor_end in html, "Missing anchor_end"
html = html.replace(anchor_end, add_p7, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J20 Partia 7 ({len(gen_data)} profili)")
