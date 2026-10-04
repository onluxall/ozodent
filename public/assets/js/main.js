(function () {
  // mobile menu
  var b = document.querySelector('.burger'), m = document.getElementById('menu');
  if (b && m) {
    b.addEventListener('click', function () { var o = m.classList.toggle('open'); b.setAttribute('aria-expanded', o); });
    m.addEventListener('click', function (e) { if (e.target.tagName === 'A') { m.classList.remove('open'); b.setAttribute('aria-expanded', false); } });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { m.classList.remove('open'); b.setAttribute('aria-expanded', false); } });
  }

  // pricing tabs (+ deep link /cennik#chirurgia)
  var tabs = [].slice.call(document.querySelectorAll('.tab'));
  function show(id, focus) {
    var found = false;
    tabs.forEach(function (t) {
      var on = t.dataset.tab === id; if (on) found = true;
      t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1;
      document.getElementById('p-' + t.dataset.tab).hidden = !on;
      if (on && focus) t.focus();
    });
    return found;
  }
  if (tabs.length) {
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { show(t.dataset.tab); history.replaceState(null, '', '#' + t.dataset.tab); });
      t.addEventListener('keydown', function (e) {
        var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (d) { e.preventDefault(); var n = tabs[(i + d + tabs.length) % tabs.length]; show(n.dataset.tab, true); }
      });
    });
    var h = location.hash.slice(1);
    if (h && show(h)) document.querySelector('.tabs').scrollIntoView({ block: 'start' });
    window.addEventListener('hashchange', function () { show(location.hash.slice(1)); });
  }

  // Google map on demand
  document.querySelectorAll('[data-map]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = btn.dataset.map; f.title = 'Mapa dojazdu – OzODent'; f.loading = 'lazy';
      f.referrerPolicy = 'no-referrer-when-downgrade'; f.allowFullscreen = true;
      var box = btn.closest('.map'); box.innerHTML = ''; box.appendChild(f);
    });
  });

  // contact form -> mailto
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form-msg');
      if (!form.checkValidity()) {
        form.reportValidity && form.reportValidity();
        msg.style.background = '#fbeeee'; msg.style.color = '#7a2323';
        msg.textContent = 'Uzupełnij imię, telefon i zaznacz zgodę.'; msg.classList.add('show'); return;
      }
      var d = new FormData(form);
      var body = 'Imię i nazwisko: ' + d.get('name') + '\nTelefon: ' + d.get('phone') +
        (d.get('email') ? '\nE-mail: ' + d.get('email') : '') + '\nUsługa: ' + d.get('service') +
        '\n\n' + (d.get('message') || '');
      location.href = 'mailto:' + form.dataset.mail + '?subject=' + encodeURIComponent('Zapytanie o wizytę – ' + d.get('service')) +
        '&body=' + encodeURIComponent(body);
      msg.style.background = ''; msg.style.color = '';
      msg.textContent = 'Otwieramy Twój program pocztowy z gotową wiadomością. Jeśli nic się nie stało – zadzwoń: 572 555 193.';
      msg.classList.add('show');
    });
  }

  // reveal on scroll
  var els = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: .08, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else els.forEach(function (el) { el.classList.add('in'); });
})();
