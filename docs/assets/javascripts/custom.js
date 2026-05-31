/**
 * PaperHub Custom JS v3
 *
 * 1. Homepage button — injected next to the site title in header
 * 2. Search box    — top-10 word-cloud keywords as quick suggestions
 * 3. Conference nav strip — rendered server-side (overrides/main.html)
 * 4. Word cloud    — full-English, loaded from assets/word_data.json
 *    · Skeleton screen while loading
 *    · Hover tooltip: conference name + paper count
 *    · Click: trigger MkDocs search
 *    · Responsive (redraws on window resize)
 */
(function () {
  "use strict";

  /* ───────────────────────────────────────────────────────────
     UTILITY
  ─────────────────────────────────────────────────────────── */
  function getBase() {
    var parts = location.pathname.split("/").filter(Boolean);
    if (parts.length === 0) return "/";
    if (!parts[0].includes(".")) return "/" + parts[0] + "/";
    return "/";
  }

  function esc(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  /* ───────────────────────────────────────────────────────────
     1. HOMEPAGE BUTTON  (injected after site title in header)
  ─────────────────────────────────────────────────────────── */
  function initHomeBtn() {
    if (document.getElementById("ph-homebtn")) return;
    var title = document.querySelector(".md-header__title");
    if (!title) return;

    var btn = document.createElement("a");
    btn.id = "ph-homebtn";
    btn.className = "ph-homebtn";
    btn.href = getBase();
    btn.title = "Return to Homepage";
    btn.setAttribute("aria-label", "Homepage");
    btn.innerHTML =
      '<svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14" aria-hidden="true">' +
      '<path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>' +
      '<span>Home</span>';

    title.after(btn);
  }

  /* ───────────────────────────────────────────────────────────
     2. WORD CLOUD DATA  (fetched once, cached)
  ─────────────────────────────────────────────────────────── */
  var _wcd = null;

  function loadWCD() {
    if (_wcd) return Promise.resolve(_wcd);
    var url = getBase() + "assets/word_data.json?v=" + (Date.now() / 3e5 | 0);
    return fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (d) {
        _wcd = d;
        return d;
      });
  }

  /* ───────────────────────────────────────────────────────────
     3. SEARCH SUGGESTIONS  (top-10 keywords on focus)
  ─────────────────────────────────────────────────────────── */
  function initSearch() {
    var inp = document.querySelector(".md-search__input");
    if (!inp || inp._phInit) return;
    inp._phInit = true;

    inp.placeholder = "Search papers…";

    var form = document.querySelector(".md-search__form");
    if (!form) return;
    form.style.position = "relative";

    var drop = document.createElement("div");
    drop.className = "ph-sdrop";
    drop.setAttribute("role", "listbox");
    drop.setAttribute("aria-label", "Trending keywords");
    form.appendChild(drop);

    function populate(keywords) {
      var html = '<div class="ph-sdrop-hd">&#x1F525; Trending Keywords</div>';
      keywords.slice(0, 10).forEach(function (kw) {
        html += '<div class="ph-sdrop-item" role="option">' +
          '<span class="ph-sdrop-kw">' + esc(kw.text) + '</span>' +
          '<span class="ph-sdrop-cnt">' + kw.count + ' paper' + (kw.count !== 1 ? 's' : '') + '</span>' +
          '</div>';
      });
      drop.innerHTML = html;

      drop.querySelectorAll(".ph-sdrop-item").forEach(function (it, i) {
        it.addEventListener("mousedown", function (e) {
          e.preventDefault();
          inp.value = keywords[i].text;
          inp.dispatchEvent(new Event("input", { bubbles: true }));
          drop.style.display = "none";
          inp.focus();
        });
      });

      drop.style.display = "block";
    }

    inp.addEventListener("focus", function () {
      if (inp.value.trim()) return;
      if (_wcd) {
        populate(_wcd.keywords);
      } else {
        drop.innerHTML = '<div class="ph-sdrop-hd">Loading\u2026</div>';
        drop.style.display = "block";
        loadWCD()
          .then(function (d) {
            if (document.activeElement === inp && !inp.value.trim()) populate(d.keywords);
          })
          .catch(function () { drop.style.display = "none"; });
      }
    });

    inp.addEventListener("input", function () { drop.style.display = "none"; });
    inp.addEventListener("keydown", function (e) { if (e.key === "Escape") drop.style.display = "none"; });
    document.addEventListener("click", function (e) {
      if (!form.contains(e.target)) drop.style.display = "none";
    });
  }

  /* ───────────────────────────────────────────────────────────
     4. WORD CLOUD
  ─────────────────────────────────────────────────────────── */
  var _ci = [0, 0, 0];
  var PALETTES = [
    ["#7c5cbf","#9575cd","#8667b8","#a887d8","#6b4fa8"],   // declining
    ["#4a1d96","#5c2eb5","#3b1278","#6333c0","#3e1a8a"],   // stable
    ["#1a0550","#0d2b7a","#162054","#0a3366","#1e1060"],   // rising
  ];

  function nextColor(trend) {
    var b = trend < 0 ? 0 : trend === 0 ? 1 : 2;
    var c = PALETTES[b][_ci[b] % PALETTES[b].length];
    _ci[b]++;
    return c;
  }

  function showSkeleton(wrap) {
    if (!wrap || wrap.querySelector(".wc-skel")) return;
    var skel = document.createElement("div");
    skel.className = "wc-skel";
    [[100,28],[70,22],[120,30],[55,18],[85,24],[90,22],[60,20],
     [75,24],[105,28],[50,18],[80,22],[45,16],[95,26],[65,20],[115,30]
    ].forEach(function (s) {
      var d = document.createElement("div");
      d.className = "wc-skel-w";
      d.style.width = s[0] + "px";
      d.style.height = s[1] + "px";
      skel.appendChild(d);
    });
    wrap.prepend(skel);
  }

  function hideSkeleton(wrap) {
    if (!wrap) return;
    var s = wrap.querySelector(".wc-skel");
    if (s) { s.style.opacity = "0"; setTimeout(function () { s.remove(); }, 400); }
    var l = wrap.querySelector(".wc-loading");
    if (l) l.style.display = "none";
  }

  function getTip() {
    var t = document.getElementById("wc-tip");
    if (!t) {
      t = document.createElement("div");
      t.id = "wc-tip";
      document.body.appendChild(t);
    }
    return t;
  }

  var _resizeTmr = null;
  var _lastData  = null;

  function renderCloud(data) {
    var canvas = document.getElementById("wordcloud-canvas");
    if (!canvas || typeof WordCloud === "undefined") return;

    _lastData = data;
    _ci = [0, 0, 0];

    var wrap = canvas.closest(".wc-canvas-wrap");
    var size = Math.min(wrap ? wrap.clientWidth - 4 : 620, 620);
    canvas.width  = size;
    canvas.height = size;
    canvas.style.opacity = "0";

    var kws = data.keywords || [];
    var infoMap = {}, trendMap = {};
    kws.forEach(function (k) {
      infoMap[k.text]  = k.conf_info || "";
      trendMap[k.text] = typeof k.trend === "number" ? k.trend : 0;
    });

    var list = kws.map(function (k) { return [k.text, k.count]; });

    WordCloud(canvas, {
      list: list,
      weightFactor: function (s) { return Math.pow(s, 0.5) * (canvas.width / 95); },
      fontFamily: "'Inter','Segoe UI','Helvetica Neue',Arial,sans-serif",
      fontWeight: "700",
      color: function (word) { return nextColor(trendMap[word] || 0); },
      backgroundColor: "transparent",
      rotateRatio: 0,
      rotationSteps: 1,
      shape: "circle",
      gridSize: Math.round(canvas.width / 80),
      minSize: 11,
      drawOutOfBound: false,
      shrinkToFit: true,

      click: function (item) {
        var si  = document.querySelector(".md-search__input");
        var tog = document.querySelector("[data-md-toggle='search']");
        if (si) {
          if (tog) tog.checked = true;
          si.value = item[0];
          si.dispatchEvent(new Event("input", { bubbles: true }));
          si.focus();
        }
        var drop = document.querySelector(".ph-sdrop");
        if (drop) drop.style.display = "none";
      },

      hover: function (item, _dim, evt) {
        canvas.style.cursor = item ? "pointer" : "default";
        var tip = getTip();
        if (item) {
          var kw  = kws.find(function (k) { return k.text === item[0]; });
          var cnt = kw ? kw.count : 0;
          var conf = infoMap[item[0]] || "";
          tip.innerHTML =
            '<div class="wc-tip-kw">'   + esc(item[0]) + "</div>" +
            '<div class="wc-tip-cnt">'  + cnt + " paper" + (cnt !== 1 ? "s" : "") + "</div>" +
            (conf ? '<div class="wc-tip-conf">' + esc(conf) + "</div>" : "");
          tip.style.cssText =
            "display:block;left:" + (evt.clientX + 14) + "px;top:" + (evt.clientY - 8) + "px";
        } else {
          tip.style.display = "none";
        }
      },
    });

    function revealCanvas() {
      hideSkeleton(wrap);
      canvas.style.transition = "opacity 0.45s";
      canvas.style.opacity = "1";
    }
    canvas.addEventListener("wordcloudstop", revealCanvas, { once: true });
    setTimeout(revealCanvas, 3000);

    document.addEventListener("scroll", function () {
      getTip().style.display = "none";
    }, { passive: true });
  }

  function initWordCloud() {
    var canvas = document.getElementById("wordcloud-canvas");
    if (!canvas) return;

    var wrap = canvas.closest(".wc-canvas-wrap");
    showSkeleton(wrap);

    loadWCD()
      .then(function (data) {
        function tryRender() {
          if (typeof WordCloud !== "undefined") {
            renderCloud(data);
          } else {
            var tries = 0;
            var tid = setInterval(function () {
              if (typeof WordCloud !== "undefined") {
                clearInterval(tid); renderCloud(data);
              } else if (++tries > 60) {
                clearInterval(tid); hideSkeleton(wrap);
              }
            }, 80);
          }
        }
        tryRender();
      })
      .catch(function (err) {
        console.warn("[PaperHub] word cloud data failed:", err);
        hideSkeleton(wrap);
      });

    window.addEventListener("resize", function () {
      clearTimeout(_resizeTmr);
      _resizeTmr = setTimeout(function () {
        if (_lastData) renderCloud(_lastData);
      }, 320);
    });
  }

  /* ───────────────────────────────────────────────────────────
     5. BOOT
  ─────────────────────────────────────────────────────────── */
  function boot() {
    initHomeBtn();
    initSearch();
    loadWCD().catch(function () {});
    if (document.getElementById("wordcloud-canvas")) initWordCloud();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  document.addEventListener("DOMContentSwitch", function () {
    setTimeout(function () {
      initHomeBtn();
      initSearch();
      if (document.getElementById("wordcloud-canvas")) initWordCloud();
    }, 60);
  });

})();
