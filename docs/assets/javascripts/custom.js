/**
 * PaperHub Custom JavaScript
 * - Homepage button injection
 * - Search placeholder (English) + recent searches dropdown
 * - Conference nav strip
 * - Keyword word cloud (homepage only)
 */

(function () {
  "use strict";

  // ─────────────────────────────────────────────
  // 1. RECENT SEARCHES
  // ─────────────────────────────────────────────
  const RECENT_KEY = "paperhub-recent-searches";
  const MAX_RECENT = 6;

  function getRecentSearches() {
    try {
      return JSON.parse(localStorage.getItem(RECENT_KEY) || "[]");
    } catch {
      return [];
    }
  }

  function addRecentSearch(term) {
    if (!term || term.trim().length < 2) return;
    let list = getRecentSearches().filter((t) => t !== term.trim());
    list.unshift(term.trim());
    if (list.length > MAX_RECENT) list = list.slice(0, MAX_RECENT);
    try {
      localStorage.setItem(RECENT_KEY, JSON.stringify(list));
    } catch {}
  }

  function initSearchEnhancements() {
    const searchInput = document.querySelector(".md-search__input");
    if (!searchInput) return;

    // Set English placeholder
    searchInput.placeholder = "Search papers…";

    // Build dropdown container
    const dropdown = document.createElement("div");
    dropdown.className = "ph-recent-dropdown";
    dropdown.innerHTML =
      '<div class="ph-recent-title">Recent Searches</div><ul class="ph-recent-list"></ul>' +
      '<button class="ph-recent-clear">Clear</button>';

    const searchForm = document.querySelector(".md-search__form");
    if (searchForm) {
      searchForm.style.position = "relative";
      searchForm.appendChild(dropdown);
    }

    function updateDropdown() {
      const list = getRecentSearches();
      const ul = dropdown.querySelector(".ph-recent-list");
      const clearBtn = dropdown.querySelector(".ph-recent-clear");
      ul.innerHTML = "";
      if (list.length === 0) {
        dropdown.style.display = "none";
        return;
      }
      list.forEach((term) => {
        const li = document.createElement("li");
        li.className = "ph-recent-item";
        li.innerHTML =
          '<svg class="ph-recent-icon" viewBox="0 0 24 24" width="14" height="14"><path fill="currentColor" d="M13 3a9 9 0 0 0-9 9H1l3.89 3.89.07.14L9 12H6c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42A8.954 8.954 0 0 0 13 21a9 9 0 0 0 0-18zm-1 5v5l4.28 2.54.72-1.21-3.5-2.08V8H12z"/></svg>' +
          '<span>' +
          term.replace(/</g, "&lt;").replace(/>/g, "&gt;") +
          "</span>";
        li.addEventListener("mousedown", (e) => {
          e.preventDefault();
          searchInput.value = term;
          searchInput.dispatchEvent(new Event("input", { bubbles: true }));
          dropdown.style.display = "none";
        });
        ul.appendChild(li);
      });
      clearBtn.style.display = list.length > 0 ? "block" : "none";
    }

    // Show dropdown on focus if no current value
    searchInput.addEventListener("focus", () => {
      if (searchInput.value.trim() === "") {
        updateDropdown();
        const list = getRecentSearches();
        if (list.length > 0) dropdown.style.display = "block";
      }
    });

    // Hide dropdown while typing
    searchInput.addEventListener("input", () => {
      if (searchInput.value.trim() !== "") {
        dropdown.style.display = "none";
      }
    });

    // Save on Enter
    searchInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter" && searchInput.value.trim()) {
        addRecentSearch(searchInput.value.trim());
        dropdown.style.display = "none";
      }
    });

    // Hide when clicking outside
    document.addEventListener("click", (e) => {
      if (!searchForm || !searchForm.contains(e.target)) {
        dropdown.style.display = "none";
      }
    });

    // Clear button
    dropdown.querySelector(".ph-recent-clear").addEventListener("mousedown", (e) => {
      e.preventDefault();
      localStorage.removeItem(RECENT_KEY);
      dropdown.style.display = "none";
    });
  }

  // ─────────────────────────────────────────────
  // 2. CONFERENCE NAV STRIP
  // ─────────────────────────────────────────────
  const CONF_NAV = [
    { label: "HPCA", icon: "⚡", items: [{ y: "2026", href: "HPCA/2026/", count: 15 }, { y: "2025", href: "HPCA/2025/", count: 19 }] },
    { label: "ISCA", icon: "🏗️", items: [{ y: "2025", href: "ISCA/2025/", count: 8 }] },
    { label: "MICRO", icon: "🔬", items: [{ y: "2025", href: "MICRO/2025/", count: null }] },
    { label: "ASPLOS", icon: "🔄", items: [{ y: "2025", href: "ASPLOS/2025/", count: null }] },
    { label: "DAC", icon: "🛠️", items: [{ y: "2025", href: "DAC/2025/", count: null }] },
    { label: "NeurIPS", icon: "🧠", items: [{ y: "2025", href: "NeurIPS/2025/", count: null }] },
    { label: "ICML", icon: "📈", items: [{ y: "2025", href: "ICML/2025/", count: null }] },
  ];

  function getBasePath() {
    // Compute base path relative to current page
    const path = window.location.pathname;
    const depth = (path.match(/\//g) || []).length;
    // On GitHub Pages: /paperhub/ = depth 2, paper pages deeper
    // We return the prefix to reach root
    const parts = path.split("/").filter(Boolean);
    // Remove segments after the repo root
    let base = "/";
    if (parts.length > 0 && parts[0] !== "") {
      // find the repo name segment
      base = "/" + parts[0] + "/";
    }
    return base;
  }

  function initConfNavStrip() {
    const existing = document.querySelector(".ph-conf-strip");
    if (existing) return;

    const base = getBasePath();

    const strip = document.createElement("nav");
    strip.className = "ph-conf-strip";
    strip.setAttribute("aria-label", "Conference navigation");

    const inner = document.createElement("div");
    inner.className = "ph-conf-strip__inner";

    CONF_NAV.forEach((conf) => {
      const group = document.createElement("div");
      group.className = "ph-conf-group";

      const label = document.createElement("span");
      label.className = "ph-conf-group__label";
      label.textContent = conf.icon + " " + conf.label;
      group.appendChild(label);

      conf.items.forEach((item) => {
        const link = document.createElement("a");
        link.className = "ph-conf-year";
        link.href = base + item.href;
        link.textContent = item.y;
        if (item.count) {
          const badge = document.createElement("span");
          badge.className = "ph-conf-badge";
          badge.textContent = item.count;
          link.appendChild(badge);
        }
        group.appendChild(link);
      });

      inner.appendChild(group);
    });

    strip.appendChild(inner);

    // Insert after the header
    const header = document.querySelector(".md-header");
    if (header && header.parentNode) {
      header.parentNode.insertBefore(strip, header.nextSibling);
    }
  }

  // ─────────────────────────────────────────────
  // 3. HOMEPAGE BUTTON (Home icon in header)
  // ─────────────────────────────────────────────
  function initHomeButton() {
    // Show the hidden logo button (it links to home)
    const logoBtn = document.querySelector(".md-header__button.md-logo");
    if (logoBtn) {
      logoBtn.style.display = "inline-flex";
      logoBtn.setAttribute("title", "Homepage");
      logoBtn.setAttribute("aria-label", "Homepage");
    }
  }

  // ─────────────────────────────────────────────
  // 4. WORD CLOUD (homepage only)
  // ─────────────────────────────────────────────

  // Tag data: [text, count, trend(-1=declining,0=stable,1=rising), searchUrl]
  // trend computed from 2025 vs 2026 paper counts
  const WORD_DATA = [
    ["LLM推理",      55, 0,    "search/?q=LLM%E6%8E%A8%E7%90%86"],
    ["硬件安全",     30, 0,    "search/?q=%E7%A1%AC%E4%BB%B6%E5%AE%89%E5%85%A8"],
    ["同态加密",     30, -1,   "search/?q=%E5%90%8C%E6%80%81%E5%8A%A0%E5%AF%86"],
    ["Rowhammer",    25, -1,   "search/?q=Rowhammer"],
    ["PIM",          25, 0,    "search/?q=PIM"],
    ["DRAM安全",     25, -1,   "search/?q=DRAM%E5%AE%89%E5%85%A8"],
    ["量子计算",     25, -1,   "search/?q=%E9%87%8F%E5%AD%90%E8%AE%A1%E7%AE%97"],
    ["FHE",          20, -1,   "search/?q=FHE"],
    ["ML加速器",     15, 0,    "search/?q=ML%E5%8A%A0%E9%80%9F%E5%99%A8"],
    ["Wafer-scale",  15, 0,    "search/?q=Wafer-scale"],
    ["内存安全",     10, 1,    "search/?q=%E5%86%85%E5%AD%98%E5%AE%89%E5%85%A8"],
    ["存内计算",     10, 1,    "search/?q=%E5%AD%98%E5%86%85%E8%AE%A1%E7%AE%97"],
    ["侧信道攻击",   10, 0,    "search/?q=%E4%BE%A7%E4%BF%A1%E9%81%93%E6%94%BB%E5%87%BB"],
    ["KV Cache",     10, 1,    "search/?q=KV+Cache"],
    ["容错量子计算", 10, 0,    "search/?q=%E5%AE%B9%E9%94%99%E9%87%8F%E5%AD%90%E8%AE%A1%E7%AE%97"],
    ["调度",          8, 1,    "search/?q=%E8%B0%83%E5%BA%A6"],
    ["能效",          8, 1,    "search/?q=%E8%83%BD%E6%95%88"],
    ["Bootstrapping", 8, 0,    "search/?q=Bootstrapping"],
    ["DDR5",          8, -1,   "search/?q=DDR5"],
    ["PRAC",          8, -1,   "search/?q=PRAC"],
    ["NMP",           8, 0,    "search/?q=NMP"],
    ["CKKS",          8, -1,   "search/?q=CKKS"],
    ["Spectre",       8, 0,    "search/?q=Spectre"],
    ["CXL",           7, 1,    "search/?q=CXL"],
    ["LoRA",          7, 1,    "search/?q=LoRA"],
    ["量化",          7, 1,    "search/?q=%E9%87%8F%E5%8C%96"],
    ["GPU",           7, 0,    "search/?q=GPU"],
    ["量子纠错",      6, 0,    "search/?q=%E9%87%8F%E5%AD%90%E7%BA%A0%E9%94%99"],
    ["光子计算",      6, 0,    "search/?q=%E5%85%89%E5%AD%90%E8%AE%A1%E7%AE%97"],
    ["激活量化",      6, 0,    "search/?q=%E6%BF%80%E6%B4%BB%E9%87%8F%E5%8C%96"],
    ["近内存计算",    6, 0,    "search/?q=%E8%BF%91%E5%86%85%E5%AD%98%E8%AE%A1%E7%AE%97"],
    ["数据中心",      6, 1,    "search/?q=%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83"],
    ["推测执行",      5, 0,    "search/?q=%E6%8E%A8%E6%B5%8B%E6%89%A7%E8%A1%8C"],
  ];

  // Color mapping by trend
  function tagColor(trend) {
    // Blue-purple gradient palette
    if (trend === 1)  return "#2d0a6e";  // rising → dark deep purple
    if (trend === -1) return "#9c7dcf";  // declining → light lavender
    return "#5b2d9e";                    // stable → mid purple
  }

  function initWordCloud() {
    const canvas = document.getElementById("wordcloud-canvas");
    if (!canvas || typeof WordCloud === "undefined") return;

    // Hide loading indicator
    const loading = document.getElementById("wc-loading");

    // Responsive canvas size
    const container = canvas.parentElement;
    const size = Math.min(container.clientWidth || 600, 620);
    canvas.width = size;
    canvas.height = size;

    const list = WORD_DATA.map((d) => [d[0], d[1]]);
    const urlMap = {};
    WORD_DATA.forEach((d) => { urlMap[d[0]] = d[3]; });
    const trendMap = {};
    WORD_DATA.forEach((d) => { trendMap[d[0]] = d[2]; });

    WordCloud(canvas, {
      list: list,
      weightFactor: (size) => Math.pow(size, 0.52) * (canvas.width / 110),
      fontFamily: "'Noto Sans SC', 'PingFang SC', sans-serif",
      fontWeight: "bold",
      color: (word) => tagColor(trendMap[word] ?? 0),
      backgroundColor: "transparent",
      rotateRatio: 0,
      rotationSteps: 1,
      shape: "circle",
      gridSize: Math.round(canvas.width / 80),
      minSize: 10,
      drawOutOfBound: false,
      shrinkToFit: true,
      click: (item) => {
        // Trigger the site's built-in search with the clicked keyword
        const searchInput = document.querySelector(".md-search__input");
        const searchToggle = document.querySelector(".md-search__overlay") ||
                             document.querySelector("[data-md-toggle='search']");
        if (searchInput) {
          // Open search
          const toggle = document.querySelector("[data-md-toggle='search']");
          if (toggle) toggle.checked = true;
          // Set value and dispatch events
          searchInput.value = item[0];
          searchInput.dispatchEvent(new Event("input", { bubbles: true }));
          searchInput.focus();
        } else {
          // Fallback: navigate to search page
          const url = urlMap[item[0]];
          if (url) window.location.href = getBasePath() + url;
        }
      },
      hover: (item, dimension, event) => {
        canvas.style.cursor = item ? "pointer" : "default";
        // Tooltip
        let tip = document.getElementById("wc-tooltip");
        if (!tip) {
          tip = document.createElement("div");
          tip.id = "wc-tooltip";
          tip.style.position = "fixed";
          document.body.appendChild(tip);
        }
        if (item && dimension) {
          const paper_count = WORD_DATA.find(d => d[0] === item[0])?.[1] ?? 0;
          const trend = trendMap[item[0]] ?? 0;
          const trendText = trend > 0 ? "↑ 热度上升" : trend < 0 ? "↓ 热度下降" : "→ 热度平稳";
          tip.innerHTML = `<strong>${item[0]}</strong><br>${paper_count} 篇相关 &nbsp; ${trendText}`;
          tip.style.display = "block";
          tip.style.left = (event.clientX + 14) + "px";
          tip.style.top = (event.clientY - 10) + "px";
        } else {
          tip.style.display = "none";
        }
      },
    });

    // Remove loading overlay after a short delay
    canvas.addEventListener("wordcloudstop", () => {
      if (loading) loading.style.display = "none";
    });
    setTimeout(() => { if (loading) loading.style.display = "none"; }, 2500);

    // Hide tooltip on scroll
    document.addEventListener("scroll", () => {
      const tip = document.getElementById("wc-tooltip");
      if (tip) tip.style.display = "none";
    }, { passive: true });
  }

  // ─────────────────────────────────────────────
  // 5. INIT on DOM ready
  // ─────────────────────────────────────────────
  function onReady(fn) {
    if (document.readyState !== "loading") {
      fn();
    } else {
      document.addEventListener("DOMContentLoaded", fn);
    }
  }

  onReady(function () {
    initHomeButton();
    initSearchEnhancements();
    initConfNavStrip();

    // Word cloud only on homepage
    const isHome =
      document.getElementById("wordcloud-canvas") !== null;
    if (isHome) {
      // Wait for WordCloud library to load
      if (typeof WordCloud !== "undefined") {
        setTimeout(initWordCloud, 100);
      } else {
        // Poll until available
        let attempts = 0;
        const poll = setInterval(() => {
          if (typeof WordCloud !== "undefined") {
            clearInterval(poll);
            initWordCloud();
          }
          if (++attempts > 50) clearInterval(poll);
        }, 100);
      }
    }
  });

  // Re-init after MkDocs instant navigation
  document.addEventListener("DOMContentSwitch", function () {
    setTimeout(() => {
      initHomeButton();
      initSearchEnhancements();
      initConfNavStrip();
      const isHome = document.getElementById("wordcloud-canvas") !== null;
      if (isHome && typeof WordCloud !== "undefined") {
        setTimeout(initWordCloud, 100);
      }
    }, 50);
  });

})();
