---
title: "Optimization of GNN Training Through Half-precision"
description: "HPDC 2025 · Session 1 — Numerical Methods"
tags:
  - "HPDC2025"
  - "Session 1"
  - "Numerical Methods"
---

# Optimization of GNN Training Through Half-precision

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 1 — Numerical Methods（2025年7月21日 10:30–12:15 · Session Chair：Jay Lofstead）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 1</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731575) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/tarafder.pdf)

**作者**：Arnab Tarafder, Yidong Gong, Pradeep Kumar

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 1 — Numerical Methods（2025年7月21日 10:30–12:15 · Session Chair：Jay Lofstead）

---

## 英文摘要

Recent trends in lower precision, e.g. half-precision floating point, training have shown improved system performance and reduced memory usage for Deep Learning while maintaining accuracy. However, current GNN systems cannot achieve such goals for GNN, as our analyses show that they massively underperform while showing abnormal accuracy when using half-precision. These systems suffer from under-utilization of hardware resources, poor training performance, and value overflow issues due to lowered precision. To mitigate this, we introduce HalfGNN, a half-precision based GNN system. HalfGNN proposes novel techniques: new vector operations for half-precision data types that improve data load and reduction performance, and discretized SpMM that overcomes the value overflow and natively provides workload balancing. Such techniques improve hardware utilization, reduce memory usage, and remove atomic writes. Evaluations show that HalfGNN achieves on average of 2.30× speedup in training time over DGL (float-based) for GAT, GCN, and GIN respectively while achieving similar accuracy, and saving 2.67× memory.

## 中文摘要

近期低精度（如半精度浮点）训练的趋势表明，在保持精度的同时可提升深度学习系统性能并降低内存占用。然而，当前 GNN 系统无法为 GNN 实现这些目标：我们的分析显示，使用半精度时它们性能大幅下降，并出现异常的精度表现。这些系统存在硬件资源利用率不足、训练性能差以及因精度降低导致的数值溢出问题。为缓解这些问题，我们提出 HalfGNN，一个基于半精度的 GNN 系统。HalfGNN 提出新颖技术：面向半精度数据类型的新向量操作，提升数据加载与归约性能；以及离散化 SpMM，克服数值溢出并原生提供负载均衡。这些技术提升了硬件利用率、降低了内存占用，并消除了原子写入。评估表明，HalfGNN 在 GAT、GCN 和 GIN 上的训练时间相比 DGL（基于浮点）平均加速 2.30 倍，同时取得相近精度，并节省 2.67 倍内存。

## 英文关键词

Graph Neural Networks, GPU, Performance

## 中文关键词

图神经网络，GPU，性能

---

[← 返回 Session 1 — Numerical Methods](index.md)
