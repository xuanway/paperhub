---
title: "R.I.P. Geomean Speedup Use Equal-Work (Or Equal-Time) Harmonic Mean Speedup Instead"
description: "HPCA 2025 · Best of CAL"
tags:
  - "HPCA2025"
  - "Best of CAL"
---

# R.I.P. Geomean Speedup Use Equal-Work (Or Equal-Time) Harmonic Mean Speedup Instead

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Best of CAL。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Best of CAL</p>
</div>

**论文链接**：
**作者**：Lieven Eeckhout (Ghent University)
**会议**：HPCA 2025

---

## 中文标题

R.I.P. 几何平均加速比：请改用等功（或等时）调和平均加速比

## 英文摘要

How to accurately summarize average performance is challenging. While geometric mean speedup is prevalently used, it is meaningless. Instead, this paper argues for harmonic mean speedup which accurately summarizes how much faster a workload executes on a target system relative to a baseline. We propose the equal-work and equal-time harmonic mean speedup metrics to explicitly expose the different assumptions they make, and we further suggest that equal-work speedup is most relevant to computer architecture research. The paper demonstrates that which average speedup is used matters in practice as inappropriate averages may lead to incorrect conclusions.

## 中文摘要

如何准确地概括平均性能是一项颇具挑战性的任务。几何平均加速比虽然被普遍使用，但它是没有意义的。相反，本文主张采用调和平均加速比，因为调和平均能够准确概括这样一个量：一个负载在目标系统上执行，相对于在基线系统上执行，究竟快了多少。为了厘清不同平均方式的含义，我们提出基于等功假设与等时假设的两种调和平均加速比指标，以明确揭示它们各自所依据假设的不同之处，并进一步指出等功加速比与计算机体系结构研究最为相关。本文还表明，实践中究竟采用哪一种平均加速比至关重要，因为不恰当的平均方式可能导致错误的结论，从而影响对系统优劣的判断以及后续的设计取舍。
