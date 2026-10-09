/* board-corrections.js · per-frame correction boxes + draft layer for every HTML board.
 * Mauro 2026-10-09: "every board needs a correction box per frame, with Copy and Download, like the review queue".
 * One file, copied byte for byte to growthub-os/boards/ and mauro-os/boards/. Injected INLINE (boards stay
 * self-contained) between the board-corrections start and end HTML comment markers:
 *   growthub-os: python3 boards/inject-corrections.py <board.html> ...
 *   mauro-os:    boards/yt/v2/controls.py puts it in every generated board, before the control bar.
 *
 * Frames: window.YTNAV ({count, index, label}) when the board has a slide adapter (one frame on screen at
 * a time: one "Comment" button for the current frame). Otherwise every [data-frame], else .frame, else
 * <section> gets its own small comment button. Heading = data-frame value, else the first h1-h3/.head.
 *
 * Draft layer: D toggles it. ON = review (elements with class "draft" show, the correction tools show,
 * a top note "Draft: comment on any frame, then Download corrections" shows). OFF = recording (all of
 * that is gone). Every board OPENS in draft (Mauro 2026-10-09 v6): D is not kept across reloads.
 * Headless Chrome and ?static open OFF so renders stay clean; ?draft=on / ?draft=off win where the
 * board keeps its URL (a-keynote rewrites it to ?s=N, so use D there). H hides the tools only.
 * Draft UI is fixed-position overlay only: it never changes the board layout, so the content stays
 * centered with D on and with D off.
 * Facecam check (Mauro 2026-10-09 v6): C or F2 cycles a translucent facecam box off, bottom-left,
 * bottom-right. The box is 22% of the width x 28% of the height: the safe zone kept empty in BOTH
 * bottom corners of every frame. ?facecam=left|right shows it on load (also in headless, for checks).
 * Notes in localStorage (every access in try/catch), key per board file.
 * Download: board-corrections-<board-slug>-<date>.txt, one line per note: "Frame N · <heading>: <note>".
 * ~/inbox/run.py files those under ~/review-queue/decisions/boards/.
 */
(function () {
  if (window.__boardCorrections) return;
  window.__boardCorrections = true;
  var Q = new URLSearchParams(location.search);
  var headless = /HeadlessChrome/.test(navigator.userAgent);
  var path = decodeURIComponent(location.pathname);
  var parts = path.split('/').filter(Boolean);
  var slug = (parts.pop() || 'board').replace(/\.html?$/i, '');
  if (/^(board|index)$/i.test(slug) && parts.length) slug = parts[parts.length - 1];
  slug = slug.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'board';
  var KEY = 'board-corrections:' + path, HKEY = 'board-corrections-hidden';
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  var forced = Q.get('draft');
  var draft = true;   // always open in draft; the D choice lives only until the page reloads
  if (headless || Q.has('static')) draft = false;
  if (forced === 'on' || forced === '1') draft = true;
  if (forced === 'off' || forced === '0') draft = false;
  var hidden = get(HKEY) === 'on';
  var FACES = ['off', 'left', 'right'];
  var face = FACES.indexOf(Q.get('facecam') || 'off'); if (face < 0) face = 0;

  var notes = {};
  try { notes = JSON.parse(get(KEY) || '{}') || {}; } catch (e) { notes = {}; }
  function save() { set(KEY, JSON.stringify(notes)); paintCount(); }

  var css = document.createElement('style');
  css.textContent =
    'html.draft-off .draft{display:none!important}' +
    '.bc-ui{font:600 13px/1.3 -apple-system,"Helvetica Neue",Arial,sans-serif;color:#111;box-sizing:border-box}' +
    '.bc-ui *{box-sizing:border-box}' +
    'html.draft-off .bc-ui,html.bc-hide .bc-ui{display:none!important}' +
    '.bc-btn{all:unset;cursor:pointer;background:#F3E3A3;color:#111;border:1.5px solid #111;border-radius:999px;padding:5px 11px;font:700 13px/1 -apple-system,"Helvetica Neue",Arial,sans-serif;white-space:nowrap}' +
    '.bc-btn:hover{background:#ffd84a}.bc-btn.has{background:#111;color:#F3E3A3}' +
    '.bc-pin{position:absolute;top:10px;right:10px;z-index:50}' +
    '.bc-box{display:none;margin:12px 0;background:#fffbe6;border:2px solid #111;border-radius:10px;padding:10px;position:relative;z-index:50}' +
    '.bc-box.on{display:block}.bc-box b{display:block;margin-bottom:6px;font-size:13px}' +
    '.bc-box textarea,#bc-panel textarea{width:100%;min-height:90px;font:500 15px/1.4 -apple-system,"Helvetica Neue",Arial,sans-serif;border:1px solid #999;border-radius:6px;padding:8px;resize:vertical;background:#fff;color:#111}' +
    '#bc-panel{position:fixed;right:14px;bottom:14px;z-index:2147483001;background:#fff;border:2px solid #111;border-radius:14px;padding:10px;width:300px;box-shadow:0 8px 28px rgba(0,0,0,.25)}' +
    '#bc-panel .bc-row{display:flex;gap:6px;align-items:center;flex-wrap:wrap}' +
    '#bc-panel .ttl{font-weight:800;margin-right:auto}#bc-panel .cur{margin-top:8px;display:none}#bc-panel .cur.on{display:block}' +
    '#bc-panel .cur b{display:block;margin-bottom:6px}#bc-panel .msg{font-weight:500;color:#555;margin-top:6px;min-height:1em}' +
    '#bc-draft{position:fixed;left:50%;top:10px;transform:translateX(-50%);z-index:2147483001;background:#bd0a0a;color:#fff;border-radius:999px;padding:8px 16px;font:700 14px/1.2 -apple-system,"Helvetica Neue",Arial,sans-serif;white-space:nowrap;pointer-events:none;box-shadow:0 4px 14px rgba(0,0,0,.2)}' +
    '#bc-draft span{font-weight:500;opacity:.85;margin-left:8px}' +
    '#bc-face{position:fixed;bottom:0;width:22vw;height:28vh;z-index:2147482999;pointer-events:none;display:none;background:rgba(255,40,140,.22);border:3px dashed rgba(255,40,140,.95);box-sizing:border-box;' +
    'font:800 16px/1 -apple-system,"Helvetica Neue",Arial,sans-serif;color:#fff;text-shadow:0 1px 3px rgba(0,0,0,.6);align-items:center;justify-content:center;letter-spacing:2px}' +
    '#bc-face.left{display:flex;left:0}#bc-face.right{display:flex;right:0}';
  document.head.appendChild(css);

  function clean(s) { return String(s == null ? '' : s).replace(/<[^>]*>/g, '').replace(/&[a-z#0-9]+;/gi, ' ').replace(/\s+/g, ' ').trim(); }
  function oneLine(s) { return String(s).replace(/\s*\n\s*/g, ' / ').trim(); }
  function isField(el) { return el && (/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName) || el.isContentEditable); }
  function keepFocus(el) { el.addEventListener('mousedown', function (e) { if (!isField(e.target)) e.preventDefault(); }); }

  var frames = [], NAV = null, panel, curBox, curTa, curLab, countEl, msgEl, frameBtn;

  function heading(el, i) {
    var v = el.getAttribute('data-frame');
    if (v && !/^\d*$/.test(v.trim())) return clean(v).slice(0, 90);
    var h = el.querySelector('h1,h2,h3,.head,.title,.t2');
    var t = clean(h ? h.textContent : el.textContent);
    return (t || 'Frame ' + (i + 1)).slice(0, 90);
  }

  function lines() {
    var ks = Object.keys(notes).filter(function (k) { return notes[k] && notes[k].t && notes[k].t.trim(); })
      .sort(function (a, b) { return a - b; });
    return ks.map(function (k) { return 'Frame ' + k + ' · ' + String(notes[k].h).replace(/:\s+/g, ', ') + ': ' + oneLine(notes[k].t); });  /* the first ": " ends the heading */
  }
  function text() {
    var d = new Date().toISOString().slice(0, 10);
    return 'Board corrections · ' + slug + ' · ' + d + ' · ' + path + '\n' + lines().join('\n') + '\n';
  }
  function paintCount() { if (countEl) countEl.textContent = 'Corrections (' + lines().length + ')'; }
  function flash(s) { if (msgEl) { msgEl.textContent = s; setTimeout(function () { msgEl.textContent = ''; }, 2500); } }

  function setNote(n, h, t) {
    if (t && t.trim()) notes[n] = { h: h, t: t }; else delete notes[n];
    save();
  }

  function buildDom() {
    var sel = document.querySelectorAll('[data-frame]');
    if (!sel.length) sel = document.querySelectorAll('.frame');
    if (!sel.length) sel = document.querySelectorAll('section');
    for (var i = 0; i < sel.length; i++) frames.push(sel[i]);
    frames.forEach(function (el, i) {
      var n = i + 1, h = heading(el, i);
      if (getComputedStyle(el).position === 'static') el.style.position = 'relative';
      var b = document.createElement('button');
      b.className = 'bc-btn bc-pin bc-ui'; b.type = 'button'; b.title = 'Correction for frame ' + n;
      var box = document.createElement('div'); box.className = 'bc-box bc-ui';
      box.innerHTML = '<b></b><textarea placeholder="What to change in this frame"></textarea>';
      box.querySelector('b').textContent = 'Frame ' + n + ' · ' + h;
      var ta = box.querySelector('textarea');
      ta.value = notes[n] ? notes[n].t : '';
      function paintBtn() { b.textContent = ta.value.trim() ? '✎ ' + n + ' ●' : '✎ ' + n; b.classList.toggle('has', !!ta.value.trim()); }
      paintBtn();
      keepFocus(b);
      b.addEventListener('click', function (e) { e.stopPropagation(); box.classList.toggle('on'); if (box.classList.contains('on')) ta.focus(); });
      ta.addEventListener('input', function () { setNote(n, h, ta.value); paintBtn(); });
      ['click', 'mousedown', 'wheel'].forEach(function (ev) { box.addEventListener(ev, function (e) { e.stopPropagation(); }); });
      el.appendChild(b); el.appendChild(box);
    });
  }

  function navSync() {
    if (!NAV || !curBox) return;
    var i = NAV.index(), n = i + 1;
    if (curBox.dataset.n === String(n)) return;
    curBox.dataset.n = String(n);
    var h = clean(NAV.label(i)).slice(0, 90) || 'Frame ' + n;
    curBox.dataset.h = h;
    curLab.textContent = 'Frame ' + n + ' · ' + h;
    curTa.value = notes[n] ? notes[n].t : '';
    frameBtn.textContent = '✎ Frame ' + n + (curTa.value.trim() ? ' ●' : '');
  }

  function buildPanel() {
    panel = document.createElement('div'); panel.id = 'bc-panel'; panel.className = 'bc-ui';
    panel.innerHTML = '<div class="bc-row"><span class="ttl"></span>' +
      (NAV ? '<button class="bc-btn" data-a="frame" type="button"></button>' : '') +
      '<button class="bc-btn" data-a="copy" type="button">Copy corrections</button>' +
      '<button class="bc-btn" data-a="dl" type="button">Download corrections</button></div>' +
      (NAV ? '<div class="cur"><b></b><textarea placeholder="What to change in this frame"></textarea></div>' : '') +
      '<div class="msg">D recording view · C facecam · H hide tools</div>';
    countEl = panel.querySelector('.ttl'); msgEl = panel.querySelector('.msg');
    keepFocus(panel);
    ['click', 'mousedown', 'wheel'].forEach(function (ev) { panel.addEventListener(ev, function (e) { e.stopPropagation(); }); });
    if (NAV) {
      curBox = panel.querySelector('.cur'); curTa = curBox.querySelector('textarea'); curLab = curBox.querySelector('b');
      frameBtn = panel.querySelector('[data-a=frame]');
      curTa.addEventListener('input', function () {
        setNote(+curBox.dataset.n, curBox.dataset.h, curTa.value);
        frameBtn.textContent = '✎ Frame ' + curBox.dataset.n + (curTa.value.trim() ? ' ●' : '');
      });
      setInterval(navSync, 200); navSync();
    }
    panel.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      var a = b.dataset.a;
      if (a === 'frame') { curBox.classList.toggle('on'); if (curBox.classList.contains('on')) curTa.focus(); }
      else if (a === 'copy') {
        var t = text();
        var done = function () { flash('Copied ' + lines().length + ' notes'); };
        try {
          navigator.clipboard.writeText(t).then(done, function () { fallbackCopy(t); done(); });
        } catch (err) { fallbackCopy(t); done(); }
      } else if (a === 'dl') {
        try {
          var blob = new Blob([text()], { type: 'text/plain' });
          var u = URL.createObjectURL(blob), l = document.createElement('a');
          l.href = u; l.download = 'board-corrections-' + slug + '-' + new Date().toISOString().slice(0, 10) + '.txt';
          document.body.appendChild(l); l.click(); l.remove(); setTimeout(function () { URL.revokeObjectURL(u); }, 1000);
          flash('Downloaded');
        } catch (err) { flash('Download failed: ' + err); }
      }
    });
    document.body.appendChild(panel);
    paintCount();
  }
  function fallbackCopy(t) {
    var x = document.createElement('textarea'); x.value = t; x.style.position = 'fixed'; x.style.opacity = '0';
    document.body.appendChild(x); x.select(); try { document.execCommand('copy'); } catch (e) {} x.remove();
  }

  var badge, faceEl;
  function paintFace() {
    if (!faceEl) return;
    faceEl.className = FACES[face] === 'off' ? '' : FACES[face];
    faceEl.textContent = 'FACECAM SAFE ZONE';
  }
  function paint() {
    var r = document.documentElement;   // on <html>: some boards rewrite body.className per slide
    r.classList.toggle('draft-off', !draft);
    r.classList.toggle('draft-on', draft);
    r.classList.toggle('bc-hide', hidden);
  }

  // Keys. Registered now, in the capture phase, so it runs before any board handler injected after it.
  window.addEventListener('keydown', function (e) {
    if (isField(e.target) && e.target.closest && e.target.closest('.bc-ui')) {
      if (e.key === 'Escape') e.target.blur();
      e.stopImmediatePropagation();   // typing in a box never moves the board, hides the bar or toggles a layer
      return;
    }
    if (isField(e.target) || e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key === 'd' || e.key === 'D') {
      draft = !draft; paint();
    } else if (e.key === 'h' || e.key === 'H') {
      hidden = !hidden; set(HKEY, hidden ? 'on' : 'off'); paint();
    } else if (e.key === 'c' || e.key === 'C' || e.key === 'F2') {
      e.preventDefault(); face = (face + 1) % FACES.length; paintFace();
    }
  }, true);

  function init() {
    NAV = window.YTNAV || null;
    if (!NAV) buildDom();
    buildPanel();
    badge = document.createElement('div'); badge.id = 'bc-draft'; badge.className = 'draft';
    badge.innerHTML = 'Draft: comment on any frame, then Download corrections<span>D = recording view · C = facecam</span>';
    document.body.appendChild(badge);
    faceEl = document.createElement('div'); faceEl.id = 'bc-face';
    document.body.appendChild(faceEl); paintFace();
    paint();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { setTimeout(init, 0); });
  else setTimeout(init, 0);
  paint();
})();
