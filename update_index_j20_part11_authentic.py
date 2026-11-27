# -*- coding: utf-8 -*-
import json

with open("gen_data_j20_part11.json", "r", encoding="utf-8") as f:
    gen_data = json.load(f)

profile_count = len(gen_data)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_header = "<strong>Kluczowe akta i tematyka badawcza (Partie 1–10: skany 1–250 z 283):</strong><br>"
new_header = "<strong>Kluczowe akta i tematyka badawcza (Komplet: 283 / 283 skanów (100%)):</strong><br>"
assert old_header in html, "Brak naglowka J20 w index.html"
html = html.replace(old_header, new_header, 1)

old_tail = "(#247–#250)."
new_tail = "(#247–#250).<br>\n              • Zima 1699 – styczeń 1700 r. (skany 251–283, <strong>100% woluminu</strong>): obdukcje po tumulcie przy administratorze <strong>Kazimierzu Długopolskim [?]</strong> (#251–#252), proces braci <strong>Wardęgów</strong> (#260–#262, #267–#268), sprzedaż roli w Budzyniu (#268–#270), własnoręczna zgoda <strong>ks. Tomasza Jaszynki</strong> (#271), śledztwo w sprawie zabójstwa <strong>Zofii Skałczonki</strong> przez młynarza <strong>Jana Latę</strong> (#272, #274, #277–#278, #280), sesja z <strong>11 I 1700 r.</strong> (#281), dublet #282 oraz metryczka końcowa z 30 X 1959 r. (#283)."
assert old_tail in html, "Brak koncowki J20 w index.html"
html = html.replace(old_tail, new_tail, 1)

old_scans = "<li><span>📄</span> <strong>250</strong> / 283 skanów archiwalnych</li>"
new_scans = "<li><span>📄</span> <strong>283</strong> / 283 skanów archiwalnych</li>"
assert old_scans in html, "Brak licznika skanow J20 w index.html"
html = html.replace(old_scans, new_scans, 1)

old_prof = "<li><span>👥</span> <strong>853</strong> unikalnych profili</li>"
new_prof = f"<li><span>👥</span> <strong>{profile_count}</strong> unikalnych profili</li>"
assert old_prof in html, "Brak licznika profili J20 w index.html"
html = html.replace(old_prof, new_prof, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Zaktualizowano index.html: 283/283 skanow, {profile_count} profili.")
