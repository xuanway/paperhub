---
title: "HP-MDR: High-Performance and Portable Data Refactoring and Progressive Retrieval with Advanced GPUs"
description: "SC 2025 · Compression and Data Reduction 2 · Yanliang Li; Wenbo Li; Qian Gong; Qing Liu; Norbert Podhorszki; Scott Klasky; Xi"
tags:
  - "SC2025"
  - "Compression and Data Reduction 2"
---

# HP-MDR: High-Performance and Portable Data Refactoring and Progressive Retrieval with Advanced GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Compression and Data Reduction 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Compression and Data Reduction 2</p>
</div>

**作者**：Yanliang Li; Wenbo Li; Qian Gong; Qing Liu; Norbert Podhorszki; Scott Klasky; Xin Liang; Jieyang Chen

**会议**：SC 2025 · St. Louis, MO

## 摘要

Scientific applications produce vast amounts of data, posing grand challenges for data management and analytics. Progressive compression is an approach to address this problem, as it allows for on-demand data retrieval with significantly reduced data movement cost. This work proposes HP-MDR, a high-performance and portable data refactoring and progressive retrieval framework for GPUs. Our contributions are threefold: (1) we optimize the bit-plane encoding and lossless encoding to achieve high performance on GPUs; (2) we propose pipeline optimization to further enhance the performance for large data processing; (3) we leverage our framework to enable data retrieval with guaranteed error control for quantities-of-interest; (4) we evaluate HP-MDR using five datasets. Evaluations demonstrate HP-MDR achieves 13.68x and 6.31x average throughput improvement for refactoring and progressive retrieval, respectively. It also leads to 11.22x throughput for recomposing data under quantity-of-intere

---

## 一句话总结

> 该工作属于 Compression and Data Reduction 2 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Compression and Data Reduction 2 领域贡献新的设计范式或评估框架。
