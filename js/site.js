(function () {
  var d = document, root = d.documentElement;
  root.classList.add('js');

  // Theme Manager: System (default), Light (bright), Dark
  var themeBtns = d.querySelectorAll('.theme-btn');
  function getStoredTheme() {
    try {
      return localStorage.getItem('theme') || 'system';
    } catch (e) {
      return 'system';
    }
  }
  function applyTheme(t) {
    if (t === 'light' || t === 'dark') {
      root.setAttribute('data-theme', t);
      var meta = d.querySelector('meta[name="color-scheme"]');
      if (meta) meta.content = t;
    } else {
      root.setAttribute('data-theme', 'system');
      var meta = d.querySelector('meta[name="color-scheme"]');
      if (meta) meta.content = 'light dark';
    }
    themeBtns.forEach(function (btn) {
      var isAct = btn.dataset.themeVal === t;
      btn.classList.toggle('active', isAct);
      btn.setAttribute('aria-pressed', isAct ? 'true' : 'false');
    });
  }

  applyTheme(getStoredTheme());

  themeBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var target = btn.dataset.themeVal;
      try {
        if (target === 'system') {
          localStorage.removeItem('theme');
        } else {
          localStorage.setItem('theme', target);
        }
      } catch (e) {}
      applyTheme(target);
    });
  });

  window.addEventListener('storage', function (e) {
    if (e.key === 'theme') {
      applyTheme(getStoredTheme());
    }
  });

  var mql = window.matchMedia('(prefers-color-scheme: dark)');
  if (mql && mql.addEventListener) {
    mql.addEventListener('change', function () {
      if (getStoredTheme() === 'system') {
        applyTheme('system');
      }
    });
  }

  var header = d.querySelector('.site-header');
  var toggle = d.querySelector('.nav-toggle');
  if (header && toggle) {
    toggle.addEventListener('click', function () {
      var open = header.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', open);
    });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && header.classList.contains('nav-open')) {
        header.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
    d.querySelectorAll('.nav-menu a').forEach(function (a) {
      a.addEventListener('click', function () {
        header.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
    var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  var items = d.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  var form = d.getElementById('lead-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var text = 'Hello Arvension, I would like a demo.\n' +
        'Name: ' + f.get('name') + '\n' +
        'Phone: ' + f.get('phone') + '\n' +
        'Interested in: ' + f.get('interest') + '\n' +
        (f.get('message') ? 'Message: ' + f.get('message') : '');
      window.open('https://wa.me/' + form.dataset.wa + '?text=' + encodeURIComponent(text), '_blank', 'noopener');
    });
  }
})();
