# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j18_part2.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update J18 counts and summary in index.html
old_part = "Partia 1: skany 1–25 z 221"
new_part = "Partie 1–2: skany 1–50 z 221"
assert old_part in html
html = html.replace(old_part, new_part, 1)

old_scans = "<li><span>📄</span> <strong>25</strong> / 221 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>50</strong> / 221 skanów archiwalnych</li>"
assert old_scans in html
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>74</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_prof in html
html = html.replace(old_prof, new_prof, 1)

anchor_end = "i oblig <strong>Reginy Miarowiczówny</strong> na 50 złp."
add_p2 = anchor_end + "<br>\n              • Lata 1656–1661 (skany 26–50): adnotacja o braku rachunków w roku potopu <strong>1656</strong> (#26), rachunek opiekuńczy po <strong>Sebastianie Decu</strong> (#27–#30), wielki proces <strong>Kazimierza Baśkowskiego</strong> przeciw opiekunowi <strong>Marcinowi Sitarskiemu</strong> z oblatą regestru z 1649 r. (544 złp percepty, cytowanie <em>Jus Municipale</em> art. XIV i dekret na 60 złp procentów + 73 złp, #33–#44), inwentarz domu i warsztatów tkackich <strong>Wojciecha Rogalowskiego</strong> za Bramą Staromiejską (#45–#48) oraz sprawa szlachetnego <strong>Mateusza Żmiędy</strong> przeciw <strong>Wawrzyńcowi Łysakowi</strong> (#48–#50)."
assert anchor_end in html
html = html.replace(anchor_end, add_p2, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html dla J18 Partia 2 ({len(gen_data)} profili)")
