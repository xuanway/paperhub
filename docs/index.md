---
title: "计算机体系结构论文 · 顶会论文解读"
description: "MICRO·ISCA·HPCA·ASPLOS·DAC·FAST·SC·EuroSys·PPoPP·ATC·HPDC 顶会论文解读。"
tags:
  # - "可信计算"
  # - "高效计算"
  - "体系结构"
  # - "硬件安全"
  # - "AI加速"
  # - "HPCA"
  # - "ISCA"
  # - "MICRO"
search:
  exclude: true
hide:
  - toc
  - navigation
---

<div class="hero" markdown>

# 计算机体系结构论文导读

<p class="hero-subtitle">📌聚焦<a href="ccflist/ccf2026‑ranked‑list.pdf" target="_blank">中国计算机学会推荐国际学术会议</a>（计算机体系结构/并行与分布计算/存储系统）<br>✨覆盖 HPCA · ISCA · MICRO · ASPLOS · DAC · FAST · SC · EuroSys · PPoPP · ATC · HPDC 顶级会议<br>🔄持续更新中✍️</p>


<!-- <div class="hero-stats">
<div class="stat"><span class="stat-number" data-stat-key="papers">169</span><span class="stat-label">篇论文</span></div>
<div class="stat"><span class="stat-number" data-stat-key="conferences">11</span><span class="stat-label">个会议</span></div>
</div> -->

<!-- <a class="github-link" href="https://github.com/xuanway/paperhub" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16" style="vertical-align:middle;margin-right:6px;fill:currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg> GitHub</a> -->

</div>

---

<div class="conf-cubes">

<div class="conf-cube conf-cube--hpca">
  <span class="conf-cube__icon">🚀</span>
  <div class="conf-cube__name">HPCA</div>
  <div class="conf-cube__full">IEEE International Symposium on High-Performance Computer Architecture</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="HPCA/2026/">2026</a>
    <a class="conf-cube__year-link" href="HPCA/2025/">2025</a>
  </div>
</div>


<div class="conf-cube conf-cube--isca">
  <span class="conf-cube__icon">🏗️</span>
  <div class="conf-cube__name">ISCA</div>
  <div class="conf-cube__full">International Symposium on Computer Architecture</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="ISCA/2025/">2025</a>
  </div>
</div>

<div class="conf-cube conf-cube--micro">
  <span class="conf-cube__icon">🔬</span>
  <div class="conf-cube__name">MICRO</div>
  <div class="conf-cube__full">IEEE/ACM International Symposium on Microarchitecture</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="MICRO/2025/">2025</a>
  </div>
</div>

<div class="conf-cube conf-cube--asplos">
  <span class="conf-cube__icon">🔄</span>
  <div class="conf-cube__name">ASPLOS</div>
  <div class="conf-cube__full">ACM International Conference on Architectural Support for Programming Languages and Operating Systems</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="ASPLOS/2025/">2025</a>
  </div>
</div>

<div class="conf-cube conf-cube--dac">
  <span class="conf-cube__icon">🛠️</span>
  <div class="conf-cube__name">DAC</div>
  <div class="conf-cube__full">Design Automation Conference</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="DAC/2025/">2025</a>
  </div>
</div>

<div class="conf-cube conf-cube--fast">
  <span class="conf-cube__icon">💾</span>
  <div class="conf-cube__name">FAST</div>
  <div class="conf-cube__full">USENIX Conference on File and Storage Technologies</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="FAST/2025/">2025</a>
  </div>
</div>

<div class="conf-cube conf-cube--sc">
  <span class="conf-cube__icon">🌩️</span>
  <div class="conf-cube__name">SC</div>
  <div class="conf-cube__full">International Conference for High Performance Computing, Networking, Storage and Analysis</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="SC/2025/">2025</a>
  </div>
</div>

<div class="conf-cube conf-cube--eurosys">
  <span class="conf-cube__icon">⚙️</span>
  <div class="conf-cube__name">EuroSys</div>
  <div class="conf-cube__full">European Conference on Computer Systems</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="EuroSys/2025/">2025</a>
  </div>
</div>

<div class="conf-cube conf-cube--ppopp">
  <span class="conf-cube__icon">⚡</span>
  <div class="conf-cube__name">PPoPP</div>
  <div class="conf-cube__full">ACM SIGPLAN Annual Symposium on Principles and Practice of Parallel Programming</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="PPoPP/2025/">2025</a>
  </div>
</div>

<div class="conf-cube conf-cube--atc">
  <span class="conf-cube__icon">🔧</span>
  <div class="conf-cube__name">ATC</div>
  <div class="conf-cube__full">ACM SIGOPS Annual Technical Conference</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="ATC/2025/">2025</a>
  </div>
</div>

<div class="conf-cube conf-cube--hpdc">
  <span class="conf-cube__icon">🧩</span>
  <div class="conf-cube__name">HPDC</div>
  <div class="conf-cube__full">ACM International Symposium on High-Performance Parallel and Distributed Computing</div>
  <div class="conf-cube__years">
    <a class="conf-cube__year-link" href="HPDC/2026/">2026</a>
  </div>
</div>

</div>

---

<div class="directions-section">
  <div class="directions-table-wrap">
    <table class="directions-table" aria-label="研究方向关键词表">
      <tbody id="directions-table-body">
        <tr>
          <td class="directions-table__loading">研究方向加载中…</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="wc-results" id="keyword-results">
  <div class="wc-results__eyebrow">Research Directions</div>
  <div class="wc-results__title" id="keyword-results-title">点击下方研究方向查看对应论文列表</div>
  <div class="wc-results__meta" id="keyword-results-meta">所有关键词按表格方式展示；点击任意关键词即可查看对应论文、会议信息与简介。</div>
  <div class="wc-results__list" id="keyword-results-list">
    <div class="wc-results__empty">选择一个研究方向后，这里会展示匹配论文的标题、会议信息和简介。</div>
  </div>
</div>
