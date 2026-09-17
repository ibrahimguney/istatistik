(() => {
  'use strict';
  const tools = document.getElementById('catalog-tools');
  const input = document.getElementById('chapter-search');
  const cards = [...document.querySelectorAll('.course[data-search]')];
  const buttons = [...document.querySelectorAll('[data-filter]')];
  const count = document.getElementById('catalog-count');
  const empty = document.getElementById('no-results');
  if (!tools || !input || !cards.length) return;
  let group = 'all';
  const normalize = value => value.toLocaleLowerCase('tr-TR').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/ı/g, 'i').replace(/[^a-z0-9]+/g, ' ').trim();
  const apply = () => {
    const words = normalize(input.value).split(/\s+/).filter(Boolean);
    let shown = 0;
    for (const card of cards) {
      const matches = (group === 'all' || card.dataset.group === group) && words.every(word => normalize(card.dataset.search).includes(word));
      card.hidden = !matches;
      if (matches) shown++;
    }
    count.textContent = `${shown} / ${cards.length} bölüm${words.length || group !== 'all' ? ' · Arama ve filtre sonucu' : ' · Kendi hızınızda öğrenin'}`;
    empty.hidden = shown !== 0;
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === group)));
  };
  buttons.forEach(button => button.addEventListener('click', () => { group = button.dataset.filter; apply(); }));
  input.addEventListener('input', apply);
  document.getElementById('reset-search').addEventListener('click', () => { group = 'all'; input.value = ''; apply(); input.focus(); });
  tools.hidden = false;
  apply();
})();
