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
    var script = document.querySelector('script[src*="assets/javascripts/custom.js"]');
    if (script) {
      try {
        var url = new URL(script.getAttribute("src"), window.location.href);
        return url.pathname.replace(/assets\/javascripts\/custom\.js.*$/, "");
      } catch (_err) {}
    }

    var parts = location.pathname.split("/").filter(Boolean);
    if (parts.length === 0) return "/";
    if (parts.length > 1 && parts[0] === "paperhub") return "/paperhub/";
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
      '<svg viewBox="0 0 24 24" fill="currentColor" width="18" height="18" aria-hidden="true">' +
      '<path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>';
    // btn.innerHTML =
    //   '<svg viewBox="0 0 24 24" fill="currentColor" width="14" height="14" aria-hidden="true">' +
    //   '<path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>' +
    //   '<span>Home</span>';

    title.after(btn);
  }

  /* ───────────────────────────────────────────────────────────
     2. WORD CLOUD DATA  (fetched once, cached)
  ─────────────────────────────────────────────────────────── */
  var _wcd = null;
  var _wcdPromise = null;

  function loadWCD() {
    if (_wcd) return Promise.resolve(_wcd);
    if (_wcdPromise) return _wcdPromise;
    var url = getBase() + "assets/word_data.json";
    _wcdPromise = fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (d) {
        _wcd = d;
        _wcdPromise = null;
        return d;
      })
      .catch(function (err) {
        _wcdPromise = null;
        throw err;
      });
    return _wcdPromise;
  }

  /* ───────────────────────────────────────────────────────────
     3. SEARCH SUGGESTIONS  (top-10 keywords on focus)
  ─────────────────────────────────────────────────────────── */
  function initSearch() {
    var inp = document.querySelector(".md-search__input");
    if (!inp || inp._phInit) return;
    inp._phInit = true;

    inp.placeholder = "Search papers";

    var form = document.querySelector(".md-search__form");
    if (!form) return;
    form.style.position = "relative";

    var drop = document.createElement("div");
    drop.className = "ph-sdrop";
    drop.setAttribute("role", "listbox");
    drop.setAttribute("aria-label", "Trending keywords");
    form.appendChild(drop);

    function showSuggestions() {
      if (inp.value.trim()) {
        drop.style.display = "none";
        return;
      }

      if (_wcd) {
        populate(_wcd.keywords);
        return;
      }

      drop.innerHTML = '<div class="ph-sdrop-hd">Loading\u2026</div>';
      drop.style.display = "block";
      loadWCD()
        .then(function (d) {
          if (document.activeElement === inp && !inp.value.trim()) populate(d.keywords);
        })
        .catch(function () { drop.style.display = "none"; });
    }

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

    inp.addEventListener("focus", showSuggestions);
    inp.addEventListener("click", showSuggestions);
    form.addEventListener("focusin", function (e) {
      if (e.target === inp) showSuggestions();
    });

    inp.addEventListener("input", function () {
      if (inp.value.trim()) {
        drop.style.display = "none";
      } else if (document.activeElement === inp) {
        showSuggestions();
      }
    });
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
  var _scrollTipBound = false;
  var _resizeListenerAdded = false;
  var _directionsData = null;
  var _directionsResizeTmr = null;
  var _directionsResizeAdded = false;

  function getKeywordParam() {
    try {
      return new URL(window.location.href).searchParams.get("keyword") || "";
    } catch (_err) {
      return "";
    }
  }

  function setKeywordParam(keyword) {
    try {
      var url = new URL(window.location.href);
      if (keyword) {
        url.searchParams.set("keyword", keyword);
      } else {
        url.searchParams.delete("keyword");
      }
      history.replaceState(null, "", url.toString());
    } catch (_err) {}
  }

  function paperHref(relUrl) {
    return getBase() + String(relUrl || "").replace(/^\/+/, "");
  }

  function renderKeywordResults(keyword, keywordData, shouldScroll) {
    var section = document.getElementById("keyword-results");
    var title = document.getElementById("keyword-results-title");
    var meta = document.getElementById("keyword-results-meta");
    var list = document.getElementById("keyword-results-list");
    if (!section || !title || !meta || !list) return;

    if (!keywordData || !keywordData.papers || !keywordData.papers.length) {
      title.textContent = "没有找到对应论文";
      meta.textContent = keyword ? (keyword + " 当前没有可展示的论文列表。") : "点击下方研究方向查看对应论文列表";
      list.innerHTML = '<div class="wc-results__empty">选择一个研究方向后，这里会展示匹配论文的标题、会议信息和简介。</div>';
      section.classList.remove("is-active");
      setKeywordParam("");
      return;
    }

    title.textContent = keyword;
    meta.textContent = keywordData.count + " 篇相关论文 · " + (keywordData.conf_info || "");
    list.innerHTML = keywordData.papers.map(function (paper) {
      return (
        '<article class="wc-paper-card">' +
          '<div class="wc-paper-card__conf">' + esc(paper.conf || "") + '</div>' +
          '<a class="wc-paper-card__title" href="' + esc(paperHref(paper.url)) + '">' + esc(paper.title || keyword) + '</a>' +
          '<p class="wc-paper-card__summary">' + esc(paper.summary || "Open the paper page for the full note.") + '</p>' +
        '</article>'
      );
    }).join("");

    section.classList.add("is-active");
    setKeywordParam(keyword);

    if (shouldScroll) {
      section.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  function getDirectionsColumnCount(width) {
    if (width >= 1440) return 6;
    if (width >= 1120) return 5;
    if (width >= 840) return 4;
    if (width >= 620) return 3;
    return 2;
  }

  function renderDirectionsTable(data) {
    var body = document.getElementById("directions-table-body");
    if (!body) return;

    _directionsData = data;

    var keywords = (data.keywords || []).slice().sort(function (left, right) {
      if (right.count !== left.count) return right.count - left.count;
      return String(left.text).localeCompare(String(right.text));
    });

    if (!keywords.length) {
      body.innerHTML = '<tr><td class="directions-table__loading">暂无研究方向数据</td></tr>';
      return;
    }

    var tableWrap = body.closest(".directions-table-wrap");
    var width = tableWrap ? tableWrap.clientWidth : window.innerWidth;
    var columns = getDirectionsColumnCount(width);
    var directionsCount = (data.stats && (data.stats.keywords_count || data.stats.directions_count)) || keywords.length;
    var html = '<tr><td class="directions-table__heading" colspan="' + columns + '">研究方向（' + directionsCount + '）</td></tr>';

    for (var index = 0; index < keywords.length; index += columns) {
      html += "<tr>";
      for (var offset = 0; offset < columns; offset++) {
        var keywordData = keywords[index + offset];
        if (keywordData) {
          html +=
            '<td class="directions-table__cell">' +
              '<button type="button" class="directions-table__button" data-keyword-index="' + (index + offset) + '">' +
                '<span class="directions-table__text">' + esc(keywordData.text) + '</span>' +
                '<span class="directions-table__count">' + keywordData.count + '</span>' +
              '</button>' +
            '</td>';
        } else {
          html += '<td class="directions-table__cell directions-table__cell--empty"></td>';
        }
      }
      html += "</tr>";
    }

    body.innerHTML = html;

    body.querySelectorAll(".directions-table__button").forEach(function (button) {
      button.addEventListener("click", function () {
        var keywordIndex = parseInt(button.getAttribute("data-keyword-index") || "-1", 10);
        var selected = keywordIndex >= 0 ? (keywords[keywordIndex] || null) : null;
        var keyword = selected ? selected.text : "";
        renderKeywordResults(keyword, selected, true);
      });
    });

    var initialKeyword = getKeywordParam();
    if (initialKeyword) {
      var initialData = keywords.find(function (entry) {
        return entry.text === initialKeyword;
      }) || null;
      renderKeywordResults(initialKeyword, initialData, false);
    }
  }

  function initDirectionsTable() {
    var body = document.getElementById("directions-table-body");
    if (!body) return;

    loadWCD()
      .then(function (data) {
        renderDirectionsTable(data);
      })
      .catch(function () {
        body.innerHTML = '<tr><td class="directions-table__loading">研究方向加载失败</td></tr>';
      });

    if (!_directionsResizeAdded) {
      window.addEventListener("resize", function () {
        clearTimeout(_directionsResizeTmr);
        _directionsResizeTmr = setTimeout(function () {
          if (_directionsData && document.getElementById("directions-table-body")) {
            renderDirectionsTable(_directionsData);
          }
        }, 180);
      });
      _directionsResizeAdded = true;
    }
  }

  function renderCloud(data) {
    var canvas = document.getElementById("wordcloud-canvas");
    if (!canvas || typeof WordCloud === "undefined") return;

    _lastData = data;
    _ci = [0, 0, 0];

    var wrap = canvas.closest(".wc-canvas-wrap");
    var width = wrap ? Math.max(200, wrap.clientWidth - 4) : 920;
    var height = wrap ? Math.max(420, wrap.clientHeight - 4) : 576;
    canvas.width  = width;
    canvas.height = height;
    canvas.style.opacity = "1";

    var kws = data.keywords || [];
    var infoMap = {}, trendMap = {}, keywordMap = {};
    kws.forEach(function (k) {
      infoMap[k.text]  = k.conf_info || "";
      trendMap[k.text] = typeof k.trend === "number" ? k.trend : 0;
      keywordMap[k.text] = k;
    });

    var list = kws.map(function (k) { return [k.text, k.count]; });

    WordCloud(canvas, {
      list: list,
      weightFactor: function (s) {
        return Math.pow(s, 0.68) * (Math.min(canvas.width, canvas.height) / 54);
      },
      fontFamily: "'Inter','Segoe UI','Helvetica Neue',Arial,sans-serif",
      fontWeight: "700",
      color: function (word) { return nextColor(trendMap[word] || 0); },
      backgroundColor: "transparent",
      rotateRatio: 0,
      rotationSteps: 1,
      shape: "square",
      ellipticity: 0.92,
      gridSize: Math.max(5, Math.round(Math.min(canvas.width, canvas.height) / 120)),
      minSize: 10,
      drawOutOfBound: false,
      shrinkToFit: true,

      click: function (item) {
        var keywordData = keywordMap[item[0]] || null;
        renderKeywordResults(item[0], keywordData, true);
        getTip().style.display = "none";
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

    canvas.addEventListener("wordclouddrawn", revealCanvas, { once: true });
    canvas.addEventListener("wordcloudstop", revealCanvas, { once: true });
    setTimeout(revealCanvas, 1200);

    var initialKeyword = getKeywordParam();
    if (initialKeyword && keywordMap[initialKeyword]) {
      renderKeywordResults(initialKeyword, keywordMap[initialKeyword], false);
    }

    if (!_scrollTipBound) {
      document.addEventListener("scroll", function () {
        getTip().style.display = "none";
      }, { passive: true });
      _scrollTipBound = true;
    }
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

    if (!_resizeListenerAdded) {
      window.addEventListener("resize", function () {
        clearTimeout(_resizeTmr);
        _resizeTmr = setTimeout(function () {
          if (_lastData && document.getElementById("wordcloud-canvas")) renderCloud(_lastData);
        }, 320);
      });
      _resizeListenerAdded = true;
    }
  }

  /* ───────────────────────────────────────────────────────────
     5. HERO STATS  (read from word_data.json, update homepage)
  ─────────────────────────────────────────────────────────── */
  function initHeroStats() {
    // Stat numbers (data-stat-key="papers|conferences|directions")
    var statEls = document.querySelectorAll("[data-stat-key]");
    // Conf-count divs (data-conf-key="HPCA 2025" etc.)
    var confEls = document.querySelectorAll("[data-conf-key]");
    // Area-tags (data-track-key="HPCA/2025/fhe" etc.)
    var trackEls = document.querySelectorAll("[data-track-key]");

    if (!statEls.length && !confEls.length && !trackEls.length) return;

    loadWCD().then(function (data) {
      var stats = data.stats || {};

      // Hero stats
      statEls.forEach(function (el) {
        var key = el.getAttribute("data-stat-key");
        if (key === "papers" && stats.total_papers != null) {
          el.textContent = stats.total_papers;
        } else if (key === "conferences" && stats.conferences_count != null) {
          el.textContent = stats.conferences_count;
        } else if (key === "directions" && stats.directions_count != null) {
          el.textContent = stats.directions_count;
        }
      });

      // Conf-card counts (e.g. "19 篇 · Las Vegas, NV, USA")
      if (stats.per_conf) {
        confEls.forEach(function (el) {
          var key = el.getAttribute("data-conf-key");
          var location = el.getAttribute("data-conf-location") || "";
          var info = stats.per_conf[key];
          if (info) {
            el.textContent =
              info.total + " 篇" +
              (location ? " · " + location : "");
          }
        });
      }

      // Area-tag counts (e.g. "同态加密 4")
      if (stats.per_track) {
        trackEls.forEach(function (el) {
          var key = el.getAttribute("data-track-key");
          var label = el.getAttribute("data-track-label") || "";
          var count = stats.per_track[key];
          if (count != null) {
            el.textContent = label + " " + count;
          }
        });
      }
    }).catch(function () {});
  }

  /* ───────────────────────────────────────────────────────────
     6. VISIT MAP
  ─────────────────────────────────────────────────────────── */
  var _MMV_SRC = "https://mapmyvisitors.com/map.js?d=VK6_Uhjas4vA0CDps3EFeB0Fotb8hU50SYT4Fcq5nUI&cl=ffffff&w=a";
  var _VISITOR_GEO_API = "https://ipwho.is/?lang=zh";
  var _mmvLoadTimer = null;
  var _mmvPollTimer = null;
  var _visitorHintPromise = null;

  function loadVisitorHint() {
    if (_visitorHintPromise) return _visitorHintPromise;

    _visitorHintPromise = fetch(_VISITOR_GEO_API, { cache: "no-store" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (d) {
        if (!d || d.success === false) throw new Error("geo lookup failed");
        var city = d.city || d.region || "未知城市";
        var country = d.country || "未知国家";
        return "当前访问来源：" + city + "，" + country;
      })
      .catch(function () {
        var tz = "";
        try {
          tz = Intl.DateTimeFormat().resolvedOptions().timeZone || "";
        } catch (_err) {}
        return tz
          ? "当前访问时区：" + tz + "（定位服务受限）"
          : "当前访问来源：定位信息暂不可用";
      });

    return _visitorHintPromise;
  }

  function clearVisitMapState(container) {
    clearInterval(_mmvPollTimer);
    clearTimeout(_mmvLoadTimer);
    _mmvPollTimer = null;
    _mmvLoadTimer = null;
    while (container.firstChild) container.removeChild(container.firstChild);
    var oldScript = document.getElementById("mapmyvisitors");
    if (oldScript) oldScript.remove();
    var oldWidget = document.getElementById("mapmyvisitors-widget");
    if (oldWidget) oldWidget.remove();
  }

  function renderVisitMapFallback(container, reason) {
    clearVisitMapState(container);

    var panel = document.createElement("div");
    panel.className = "homepage-pageviews__fallback";

    var mapFrame = document.createElement("div");
    mapFrame.className = "homepage-pageviews__fallback-mapframe";

    var mapImg = document.createElement("img");
    mapImg.className = "homepage-pageviews__fallback-map";
    mapImg.src = getBase() + "assets/world.svg";
    mapImg.alt = "世界地图底图";
    mapFrame.appendChild(mapImg);

    var title = document.createElement("div");
    title.className = "homepage-pageviews__fallback-title";
    title.textContent = "实时访客地图服务不可达";

    var desc = document.createElement("div");
    desc.className = "homepage-pageviews__fallback-desc";
    desc.textContent = reason || "地图服务连接超时，请稍后重试。";

    var loc = document.createElement("div");
    loc.className = "homepage-pageviews__fallback-loc";
    loc.textContent = "正在获取当前访问来源...";
    loadVisitorHint().then(function (msg) {
      loc.textContent = msg;
    });

    var retry = document.createElement("button");
    retry.type = "button";
    retry.className = "homepage-pageviews__retry";
    retry.textContent = "重试实时地图";
    retry.addEventListener("click", function () {
      initVisitMap();
    });

    panel.appendChild(mapFrame);
    panel.appendChild(title);
    panel.appendChild(desc);
    panel.appendChild(loc);
    panel.appendChild(retry);
    container.appendChild(panel);
  }

  function hasVisitMapWidget(container) {
    if (!container) return false;
    if (document.getElementById("mapmyvisitors-widget")) return true;

    var script = document.getElementById("mapmyvisitors");
    if (script && script.nextElementSibling) {
      var html = script.nextElementSibling.outerHTML || "";
      if (/mapmyvisitors/i.test(html)) return true;
    }

    return false;
  }

  // Called on SPA navigation back to home — clears old widget and reinjects the script.
  // map.js has no $(window).load dependency: it auto-runs once its jQuery CDN load
  // completes, finds #mapmyvisitors, and inserts #mapmyvisitors-widget after it.
  function initVisitMap() {
    var container = document.getElementById("mmvst_globe_container");
    if (!container) return;

    clearVisitMapState(container);

    var loading = document.createElement("div");
    loading.className = "homepage-pageviews__loading";
    loading.textContent = "访客地图加载中...";
    container.appendChild(loading);

    var s = document.createElement("script");
    s.id = "mapmyvisitors";
    s.type = "text/javascript";
    s.src = _MMV_SRC;
    s.async = true;

    s.onerror = function () {
      renderVisitMapFallback(container, "无法连接地图服务（网络或服务端不可达）。");
    };

    s.onload = function () {
      // map.js may inject the widget asynchronously after script load.
      var checks = 0;
      var maxChecks = 6;
      _mmvPollTimer = setInterval(function () {
        checks += 1;
        if (hasVisitMapWidget(container)) {
          clearInterval(_mmvPollTimer);
          _mmvPollTimer = null;
          var loadingNode = container.querySelector(".homepage-pageviews__loading");
          if (loadingNode) loadingNode.remove();
        } else if (checks >= maxChecks) {
          clearInterval(_mmvPollTimer);
          _mmvPollTimer = null;
          renderVisitMapFallback(container, "地图脚本已加载，但未返回可渲染内容。");
        }
      }, 500);
    };

    container.appendChild(s);

    _mmvLoadTimer = setTimeout(function () {
      if (!hasVisitMapWidget(container)) {
        renderVisitMapFallback(container, "地图加载超时，请检查网络后重试。");
      }
    }, 3500);
  }

  /* ───────────────────────────────────────────────────────────
     7. BOOT
  ─────────────────────────────────────────────────────────── */

  function reinit() {
    initHomeBtn();
    initSearch();
    initHeroStats();
    initDirectionsTable();
    initVisitMap();
  }

  function boot() {
    initHomeBtn();
    initSearch();
    initHeroStats();
    initDirectionsTable();
    initVisitMap();
    loadWCD().catch(function () {});
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  // MkDocs Material instant navigation: subscribe to document$ (RxJS Subject)
  // This fires on every page swap including back-navigation.
  // Fall back to legacy DOMContentSwitch for non-Material environments.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(function () {
      reinit();
    });
  } else {
    document.addEventListener("DOMContentSwitch", function () {
      setTimeout(reinit, 60);
    });
  }

})();
