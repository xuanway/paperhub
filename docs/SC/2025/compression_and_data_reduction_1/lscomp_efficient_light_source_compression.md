---
title: "lsCOMP: Efficient Light Source Compression"
description: "SC 2025 · Compression and Data Reduction 1 · Yafan Huang; Sheng Di; Robert Underwood; Peco Myint; Miaoqi Chu; Guanpeng Li; Ni"
tags:
  - "SC2025"
  - "Compression and Data Reduction 1"
---

# lsCOMP: Efficient Light Source Compression

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Compression and Data Reduction 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Compression and Data Reduction 1</p>
</div>

**作者**：Yafan Huang; Sheng Di; Robert Underwood; Peco Myint; Miaoqi Chu; Guanpeng Li; Nicholas Schwarz; Franck Cappello

**会议**：SC 2025 · St. Louis, MO

## 摘要

Light source facilities, which generate X-rays for probing microstructures and dynamic processes, produce intense data streams, reaching up to 250 GB/s and projected to exceed 1 TB/s by the end of this decade. Managing such massive data poses critical challenges due to limited local processing capacity and bandwidth constraints when offloading data to HPC systems. To address these challenges, we propose lsCOMP, a GPU compressor that operates within a single kernel. lsCOMP supports both lossless and configurable lossy compression, ensuring high compression ratios and preserved data quality across diverse light source applications. On one NVIDIA A100 GPU, lsCOMP achieves compression throughputs of 380.89 to 509.21 GB/s in lossless mode, delivering up to 20 times higher performance than industry-leading GPU compressors while achieving superior compression ratios. In lossy modes, lsCOMP further improves throughput and ratios significantly. Additionally, lsCOMP demonstrates versatile perfor

---

## 一句话总结

> 该工作属于 Compression and Data Reduction 1 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Compression and Data Reduction 1 领域贡献新的设计范式或评估框架。
