# -*- coding: utf-8 -*-
with open('/home/ubuntu/workspace/Gen/generate_j17_html.py', encoding='utf-8') as f:
    code = f.read()

# 1. Dodajemy dolny pasek paginacji po tabeli głównej
old_main_table = """      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th onclick="sortMain('nr_skanu')">Skan ↕</th>
              <th onclick="sortMain('strona_pagina')">Pagina ↕</th>
              <th onclick="sortMain('data_rok')">Rok ↕</th>
              <th>Osoby i Podmioty</th>
              <th onclick="sortMain('kategoria')">Kategoria ↕</th>
              <th>Opis Sprawy / Treść Aktu</th>
              <th>Kwoty / Podatki</th>
            </tr>
          </thead>
          <tbody id="mainTableBody"></tbody>
        </table>
      </div>
    </section>"""

new_main_table = """      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th onclick="sortMain('nr_skanu')">Skan ↕</th>
              <th onclick="sortMain('strona_pagina')">Pagina ↕</th>
              <th onclick="sortMain('data_rok')">Rok ↕</th>
              <th>Osoby i Podmioty</th>
              <th onclick="sortMain('kategoria')">Kategoria ↕</th>
              <th>Opis Sprawy / Treść Aktu</th>
              <th>Kwoty / Podatki</th>
            </tr>
          </thead>
          <tbody id="mainTableBody"></tbody>
        </table>
      </div>

      <div class="pagination-bar" style="margin-top: 1rem;">
        <div class="pagination-info" id="mainPaginationInfoBot">Wyświetlanie...</div>
        <div class="pagination-controls">
          <button class="page-btn" id="mainPrevBtnBot" onclick="prevMainPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="mainPageIndicatorBot" style="font-size:0.85rem; font-weight:600; padding:0 0.5rem;">1 / 1</span>
          <button class="page-btn" id="mainNextBtnBot" onclick="nextMainPage()">Następna ›</button>
          <div class="page-jump">
            <span>Skocz do:</span>
            <input type="number" id="mainJumpInputBot" min="1" value="1" onchange="jumpMainPage(this.value)">
          </div>
        </div>
      </div>
    </section>"""

# 2. Dodajemy dolny pasek paginacji po tabeli genealogicznej
old_gen_table = """      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th onclick="sortGen('lp')" style="width: 5%;">Lp. ↕</th>
              <th onclick="sortGen('nazwisko')" style="width: 18%;">Nazwisko ↕</th>
              <th onclick="sortGen('imie')" style="width: 15%;">Imię ↕</th>
              <th onclick="sortGen('miejsce')" style="width: 18%;">Miejsce zamieszkania ↕</th>
              <th onclick="sortGen('funkcja')" style="width: 16%;">Funkcja społeczna ↕</th>
              <th onclick="sortGen('skany_list')" style="width: 16%;">Roboczo: Nr skanów ↕</th>
              <th onclick="sortGen('zakres_lat')" style="width: 12%;">Zakres lat ↕</th>
            </tr>
          </thead>
          <tbody id="genTableBody"></tbody>
        </table>
      </div>
    </section>"""

new_gen_table = """      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th onclick="sortGen('lp')" style="width: 5%;">Lp. ↕</th>
              <th onclick="sortGen('nazwisko')" style="width: 18%;">Nazwisko ↕</th>
              <th onclick="sortGen('imie')" style="width: 15%;">Imię ↕</th>
              <th onclick="sortGen('miejsce')" style="width: 18%;">Miejsce zamieszkania ↕</th>
              <th onclick="sortGen('funkcja')" style="width: 16%;">Funkcja społeczna ↕</th>
              <th onclick="sortGen('skany_list')" style="width: 16%;">Roboczo: Nr skanów ↕</th>
              <th onclick="sortGen('zakres_lat')" style="width: 12%;">Zakres lat ↕</th>
            </tr>
          </thead>
          <tbody id="genTableBody"></tbody>
        </table>
      </div>

      <div class="pagination-bar" style="margin-top: 1rem;">
        <div class="pagination-info" id="genPaginationInfoBot">Wyświetlanie...</div>
        <div class="pagination-controls">
          <button class="page-btn" id="genPrevBtnBot" onclick="prevGenPage()">‹ Poprzednia</button>
          <span class="page-indicator" id="genPageIndicatorBot" style="font-size:0.85rem; font-weight:600; padding:0 0.5rem;">1 / 1</span>
          <button class="page-btn" id="genNextBtnBot" onclick="nextGenPage()">Następna ›</button>
          <div class="page-jump">
            <span>Skocz do:</span>
            <input type="number" id="genJumpInputBot" min="1" value="1" onchange="jumpGenPage(this.value)">
          </div>
        </div>
      </div>
    </section>"""

# 3. Aktualizacja JS w renderMainTable i renderGenTable
old_js_main = """      document.getElementById('mainPaginationInfo').innerText = 
        `Pokazywane ${filteredMain.length > 0 ? start + 1 : 0}–${Math.min(end, filteredMain.length)} z ${filteredMain.length} pozycji`;
      document.getElementById('mainPageIndicator').innerText = `${mainCurrentPage} / ${totalPages}`;
      document.getElementById('mainJumpInput').max = totalPages;
      document.getElementById('mainJumpInput').value = mainCurrentPage;
      document.getElementById('mainPrevBtn').disabled = (mainCurrentPage <= 1);
      document.getElementById('mainNextBtn').disabled = (mainCurrentPage >= totalPages);"""

new_js_main = """      const startRec = filteredMain.length > 0 ? start + 1 : 0;
      const endRec = Math.min(end, filteredMain.length);
      const infoText = `Pokazywane ${startRec}–${endRec} z ${filteredMain.length} pozycji (Strona ${mainCurrentPage} z ${totalPages})`;
      const pageIndicator = `${mainCurrentPage} / ${totalPages}`;

      ['mainPaginationInfo', 'mainPaginationInfoBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.innerText = infoText;
      });
      ['mainPageIndicator', 'mainPageIndicatorBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.innerText = pageIndicator;
      });
      ['mainPrevBtn', 'mainPrevBtnBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.disabled = (mainCurrentPage <= 1);
      });
      ['mainNextBtn', 'mainNextBtnBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.disabled = (mainCurrentPage >= totalPages);
      });
      ['mainJumpInput', 'mainJumpInputBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) { el.value = mainCurrentPage; el.max = totalPages; }
      });"""

old_js_gen = """      document.getElementById('genPaginationInfo').innerText = 
        `Pokazywane ${filteredGen.length > 0 ? start + 1 : 0}–${Math.min(end, filteredGen.length)} z ${filteredGen.length} osób`;
      document.getElementById('genPageIndicator').innerText = `${genCurrentPage} / ${totalPages}`;
      document.getElementById('genJumpInput').max = totalPages;
      document.getElementById('genJumpInput').value = genCurrentPage;
      document.getElementById('genPrevBtn').disabled = (genCurrentPage <= 1);
      document.getElementById('genNextBtn').disabled = (genCurrentPage >= totalPages);"""

new_js_gen = """      const startGen = filteredGen.length > 0 ? start + 1 : 0;
      const endGen = Math.min(end, filteredGen.length);
      const infoGen = `Pokazywane ${startGen}–${endGen} z ${filteredGen.length} osób (Strona ${genCurrentPage} z ${totalPages})`;
      const pageIndicatorGen = `${genCurrentPage} / ${totalPages}`;

      ['genPaginationInfo', 'genPaginationInfoBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.innerText = infoGen;
      });
      ['genPageIndicator', 'genPageIndicatorBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.innerText = pageIndicatorGen;
      });
      ['genPrevBtn', 'genPrevBtnBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.disabled = (genCurrentPage <= 1);
      });
      ['genNextBtn', 'genNextBtnBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.disabled = (genCurrentPage >= totalPages);
      });
      ['genJumpInput', 'genJumpInputBot'].forEach(id => {
        const el = document.getElementById(id);
        if (el) { el.value = genCurrentPage; el.max = totalPages; }
      });"""

code = code.replace(old_main_table, new_main_table)
code = code.replace(old_gen_table, new_gen_table)
code = code.replace(old_js_main, new_js_main)
code = code.replace(old_js_gen, new_js_gen)

with open('/home/ubuntu/workspace/Gen/generate_j17_html.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('Patched generate_j17_html.py with symmetrical pagination!')
