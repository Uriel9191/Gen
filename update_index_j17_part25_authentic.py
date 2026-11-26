# -*- coding: utf-8 -*-
import json

with open('/home/ubuntu/workspace/Gen/gen_data_j17_part25.json', 'r', encoding='utf-8') as f:
    gen_data = json.load(f)

with open('/home/ubuntu/workspace/Gen/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_count = "<li><span>👥</span> <strong>1635</strong> unikalnych profili</li>"
new_count = f"<li><span>👥</span> <strong>{len(gen_data)}</strong> unikalnych profili</li>"
assert old_count in html, "Nie znaleziono licznika 1635 w index.html!"
html = html.replace(old_count, new_count, 1)

old_bullet1 = "Partie 1–24: skany 1–600, fol. 1r–295r; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
new_bullet1 = "Partie 1–25: skany 1–625, fol. 1r–306v; lata 1651, 1694, 1700, 1726, 1729–1731, 1752–1759"
assert old_bullet1 in html, "Nie znaleziono bullet1 w index.html!"
html = html.replace(old_bullet1, new_bullet1, 1)

anchor_end = "oraz zapisy z 1759 r. o ćwierci po Hudrikowskiej (skan 600)."
add_part25 = anchor_end + "<br>\n              • Spory cechowe, kramarskie i sukcesyjne 1758–1759 (skany 601–625): zatarg cechmistrza kowalskiego <strong>Kazimierza Młynarskiego</strong> z urzędem i wójtem przed krucyfiksem (skany 606–607), manifestacja kramarzy pod wodzą <strong>Kazimierza Żebrowskiego</strong> przeciw arendarzowi targowemu <strong>Aznerowi</strong> (skany 619–620), wielowątkowy proces spadkowy szlachetnego <strong>Antoniego Petrykowskiego</strong> z wdową <strong>Teresą Słomkowską</strong> z analizą trzech testamentów (skany 621–624) oraz roszczenia sukcesyjne żołnierza artylerii koronnej <strong>Kazimierza Tokarskiego</strong> (skany 617–618, 621, 624–625)."
assert anchor_end in html, "Nie znaleziono anchor_end w index.html!"
html = html.replace(anchor_end, add_part25, 1)

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Zaktualizowano index.html ({len(gen_data)} profili)")
