# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/index.html', encoding='utf-8') as f:
    text = f.read()

# Zastępujemy liczbę profili dla J17: 68 -> 203
text = text.replace(
    '<li><span>👥</span> <strong>68</strong> unikalnych profili</li>',
    '<li><span>👥</span> <strong>203</strong> unikalnych profili</li>'
)

# Zastępujemy opis zakresu spraw
old_scope = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partia 1: sesje z 1700 r.).<br>
              • Spory rodzinne, wadia 30 grzywien i fundusze na naprawę więzienia oraz Bramy Lubelskiej.<br>
              • Finanse i dobra ziemskie Szpitala Św. Ducha pod zarządem burmistrza Adama Kotowicza.<br>
              • Sprawy kryminalne, kradzieże wozów, bójki karczemne i jurysdykcja nad szynkami.<br>
              • Sprawy ludności żydowskiej (młynarz Berek, arendarz Pinchas Dawidowicz, kramarz Boruch).<br>
              • Wizje lokalne granic miejskich na Podlesiu pod przewodnictwem wójta Jana Majowskiego."""

new_scope = """              <strong>Kluczowe akta i tematyka badawcza (776 skanów):</strong><br>
              • Transkrypcja dyplomatyczna in extenso skanów woluminu (Partie 1–2: sesje z 1700 r., 50 skanów).<br>
              • Spory rodzinne, wadia 30 grzywien i fundusze na naprawę więzienia oraz Bramy Lubelskiej.<br>
              • Finanse i kapitały konwentu Kanoników Regularnych Laterańskich (przeor Pajecki, wyderkaffy, zegar ścienny).<br>
              • Sąd kryminalny i wyrok śmierci na stosie pasterza Szymona Kuparki za sodomię pod prawem saskim i magdeburskim.<br>
              • Władza zamkowa i uniwersały podkanclerzyny Anny z Gnińskich Zamoyskiej dla arendarza Pinchasa Dawidowicza.<br>
              • Drobiazgowe obdukcje ran rzemieślników (pobicie szewca Stelmachowicza) i spory polne o groch i tatarkę."""

if old_scope in text:
    text = text.replace(old_scope, new_scope)
    print("Updated J17 scope in index.html!")
else:
    print("Warning: old_scope not found directly, checking regex")

with open('/home/ubuntu/workspace/Gen/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated index.html successfully!")
