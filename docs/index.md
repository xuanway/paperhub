---
title: "可信高效计算论文 · 顶会论文解读"
description: "MICRO·ISCA·HPCA·ASPLOS·DAC·NeurIPS·ICML 顶会论文解读，聚焦可信高效计算，覆盖硬件安全、AI加速器、同态加密、量子计算等方向。"
tags:
  - "可信计算"
  - "高效计算"
  - "体系结构"
  - "硬件安全"
  - "AI加速"
  - "HPCA"
  - "ISCA"
  - "MICRO"
search:
  exclude: true
hide:
  - toc
  - navigation
---

<div class="hero" markdown>

# 可信高效计算论文

<p class="hero-subtitle">聚焦体系结构安全与高效计算 · 涵盖硬件安全 · AI加速器 · 同态加密 · 量子计算等前沿方向<br>覆盖 HPCA · ISCA · MICRO · ASPLOS · DAC · NeurIPS · ICML 等顶级会议<br>持续更新中</p>

<div class="hero-stats">
<div class="stat"><span class="stat-number" data-stat-key="papers">169</span><span class="stat-label">篇论文</span></div>
<div class="stat"><span class="stat-number" data-stat-key="conferences">7</span><span class="stat-label">个会议</span></div>
<div class="stat"><span class="stat-number" data-stat-key="directions">11</span><span class="stat-label">个研究方向</span></div>
</div>

<!-- <a class="github-link" href="https://github.com/xuanway/paperhub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16" style="vertical-align:middle;margin-right:6px;fill:currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg> GitHub</a> -->

</div>

---

<div class="wc-section">
<div class="wc-section__title">🔍 关键词热度词云</div>
<div class="wc-section__subtitle">点击关键词跳转相关论文 · 字体大小 = 论文覆盖频次 · 颜色深浅 = 热度趋势</div>
<div class="wc-legend">
  <span class="wc-legend-item"><span class="wc-legend-dot" style="background:#2d0a6e"></span> 热度上升</span>
  <span class="wc-legend-item"><span class="wc-legend-dot" style="background:#5b2d9e"></span> 热度平稳</span>
  <span class="wc-legend-item"><span class="wc-legend-dot" style="background:#9c7dcf"></span> 热度下降</span>
</div>
<div class="wc-canvas-wrap">
  <canvas id="wordcloud-canvas" width="600" height="600"></canvas>
  <div class="wc-loading" id="wc-loading">词云加载中…</div>
</div>

<div class="wc-results" id="keyword-results">
  <div class="wc-results__eyebrow">Keyword Paper List</div>
  <div class="wc-results__title" id="keyword-results-title">点击词云中的关键词查看对应论文列表</div>
  <div class="wc-results__meta" id="keyword-results-meta">每个关键词都会展示对应论文；点击论文标题可进入详细解读页面。</div>
  <div class="wc-results__list" id="keyword-results-list">
    <div class="wc-results__empty">选择一个关键词后，这里会展示匹配论文的标题、会议信息和简介。</div>
  </div>
</div>
</div>

---

<div class="conf-cubes">

<div class="conf-cube conf-cube--hpca">
  <span class="conf-cube__icon">⚡</span>
  <div class="conf-cube__name">HPCA</div>
  <div class="conf-cube__full">High-Performance Computer Architecture</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="HPCA/2026/">2026</a>
    <a class="conf-cube__year-link" href="HPCA/2025/">2025</a>
  </div>
  <div class="conf-cube__stat">136 篇 · Las Vegas / Sydney</div>
</div>

<div class="conf-cube conf-cube--isca">
  <span class="conf-cube__icon">🏗️</span>
  <div class="conf-cube__name">ISCA</div>
  <div class="conf-cube__full">Int'l Symp. on Computer Architecture</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="ISCA/2025/">2025</a>
  </div>
  <div class="conf-cube__stat" data-conf-key="ISCA 2025">135 篇 · Tokyo, Japan</div>
</div>

<div class="conf-cube conf-cube--micro">
  <span class="conf-cube__icon">🔬</span>
  <div class="conf-cube__name">MICRO</div>
  <div class="conf-cube__full">IEEE/ACM Int'l Symp. on Microarchitecture</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="MICRO/2025/">2025</a>
  </div>
  <div class="conf-cube__stat" data-conf-key="MICRO 2025">123 篇 · Seoul, Korea</div>
</div>

<div class="conf-cube conf-cube--asplos">
  <span class="conf-cube__icon">🔄</span>
  <div class="conf-cube__name">ASPLOS</div>
  <div class="conf-cube__full">Architectural Support for Programming Languages &amp; OS</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="ASPLOS/2025/">2025</a>
  </div>
  <div class="conf-cube__stat" data-conf-key="ASPLOS 2025">184 篇 · Rotterdam</div>
</div>

<div class="conf-cube conf-cube--dac">
  <span class="conf-cube__icon">🛠️</span>
  <div class="conf-cube__name">DAC</div>
  <div class="conf-cube__full">Design Automation Conference</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="DAC/2025/">2025</a>
  </div>
  <div class="conf-cube__stat">更新中 · San Francisco</div>
</div>

<div class="conf-cube conf-cube--neurips">
  <span class="conf-cube__icon">🧠</span>
  <div class="conf-cube__name">NeurIPS</div>
  <div class="conf-cube__full">Conf. on Neural Information Processing Systems</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="NeurIPS/2025/">2025</a>
  </div>
  <div class="conf-cube__stat">更新中 · Vancouver</div>
</div>

<div class="conf-cube conf-cube--icml">
  <span class="conf-cube__icon">🤖</span>
  <div class="conf-cube__name">ICML</div>
  <div class="conf-cube__full">Int'l Conf. on Machine Learning</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="ICML/2025/">2025</a>
  </div>
  <div class="conf-cube__stat">更新中 · Vancouver</div>
</div>

</div>

---

<div class="homepage-pageviews">
  <!-- <div class="homepage-pageviews__header">
    <span class="homepage-pageviews__title">📊 Pageviews</span>
    <span class="homepage-pageviews__subtitle">实时访客地图 · 由 mapmyvisitors.com 提供</span>
  </div> -->
  <div id="mmvst_globe_container" class="homepage-pageviews__globe">
    <script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=VK6_Uhjas4vA0CDps3EFeB0Fotb8hU50SYT4Fcq5nUI&cl=ffffff&w=a"></script>
  </div>
</div>
