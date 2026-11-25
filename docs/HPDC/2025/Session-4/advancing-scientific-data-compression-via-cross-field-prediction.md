---
title: "Advancing Scientific Data Compression via Cross-Field Prediction"
description: "HPDC 2025 · Session 4 — Efficiency and Sustainability"
tags:
  - "HPDC2025"
  - "Session 4"
  - "Efficiency and Sustainability"
---

# Advancing Scientific Data Compression via Cross-Field Prediction

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 4 — Efficiency and Sustainability（2025年7月22日 10:30–12:15 · Session Chair：Jarek Nabrzyski）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 4</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731592) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/liu.pdf)

**作者**：Youyuan Liu, Wenqi Jia, Taolue Yang, Jiang Bo, Miao Yin, Sian Jin

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 4 — Efficiency and Sustainability（2025年7月22日 10:30–12:15 · Session Chair：Jarek Nabrzyski）

---

## 英文摘要

Scientific applications generate massive amounts of data, leading to significant storage and I/O bottlenecks. Lossy compression is a crucial technique for reducing data volume in scientific computing, balancing storage efficiency and data fidelity. Such scientific data often consists of multiple fields representing various physical metrics, which exhibit inherent correlations. However, existing compression solutions predominantly rely on local information within a single field, overlooking cross-field correlations that could enhance compression efficiency. In this paper, we introduce a novel compression framework that integrates both local and cross-field information to enhance predictive accuracy. With the help of a carefully designed neural network, our approach effectively captures complex correlations across fields, significantly improving compression ratios. Additionally, our method can rely solely on cross-field prediction to reconstruct fields, achieving extremely high compression ratios under relaxed accuracy constraints. We evaluate our approach on two real-world scientific applications across 85 data fields, demonstrating compression ratio improvements of up to 103.4% for a single field and up to 19.3% overall.

## 中文摘要

科学应用产生海量数据，造成严重的存储与 I/O 瓶颈。有损压缩是科学计算中减少数据量的关键技术，可在存储效率与数据保真度之间取得平衡。此类科学数据往往由表示不同物理量的多个场组成，这些场之间存在内在相关性。然而，现有压缩方案主要依赖单个场内的局部信息，忽略了可提升压缩效率的跨场相关性。本文提出一种新颖的压缩框架，融合局部与跨场信息以提升预测精度。借助精心设计的神经网络，我们的方法有效捕捉跨场的复杂相关性，显著提升压缩比。此外，我们的方法可以仅依靠跨场预测来重建场，在放宽精度约束时实现极高的压缩比。我们在两个真实科学应用的 85 个数据场上评估该方法，单个场的压缩比最高提升 103.4%，整体最高提升 19.3%。

## 英文关键词

Lossy Compression, Scientific Application

## 中文关键词

有损压缩，科学应用

---

[← 返回 Session 4 — Efficiency and Sustainability](index.md)
