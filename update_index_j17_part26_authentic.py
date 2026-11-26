# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part26.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_count = "<li><span>👥</span> <strong>1708</strong> unikalnych profili</li>"
new_count = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_count in html, "Nie znaleziono licznika 1708 w index.html!"
html = html.replace(old_count, new_count, 1)

old_bullet1 = "Partie 1–25: skany 1–625, fol. 1r–306v; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
new_bullet1 = "Partie 1–26: skany 1–650, fol. 1r–319r; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
assert old_bullet1 in html, "Nie znaleziono bullet1 w index.html!"
html = html.replace(old_bullet1, new_bullet1, 1)

anchor_end = "oraz roszczenia sukcesyjne żołnierza artylerii koronnej <strong>Kazimierza Tokarskiego</strong> (skany 617–618, 621, 624–625)."
add_part26 = anchor_end + "<br>\n              • Konflikty cechowe, donacje żołnierskie i konfesaty skarbowe 1755–1758 (skany 626–650): wyrok i donacja żołnierza artylerii koronnej <strong>Kazimierza Tokarskiego</strong> dla sióstr przyrodnich (skany 626–629), plenipotencja ks. dziekana <strong>Stanisława Kanskiego</strong> na dług po wójcie Szymonie Marszałkowskim na ornat ze złotogłowiu (skany 637–638), wielowątkowy spór płócienników <strong>Ludwika Bartnickiego</strong> i <strong>Antoniego Pałki</strong> przeciw burmistrzowi <strong>Łukaszowi Krzeszowskiemu</strong> (skany 635, 644–647) oraz skarga pełnomocnika skarbnika lubelskiego <strong>Stanisława Wybranowskiego</strong> o konfesaty poddanych (skany 649–650)."
assert anchor_end in html, "Nie znaleziono anchor_end w index.html!"
html = html.replace(anchor_end, add_part26, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
