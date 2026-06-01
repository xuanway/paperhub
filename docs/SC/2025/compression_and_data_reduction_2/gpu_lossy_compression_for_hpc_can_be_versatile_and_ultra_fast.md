---
title: "GPU Lossy Compression for HPC Can Be Versatile and Ultra-Fast"
description: "SC 2025 · Compression and Data Reduction 2 · Yafan Huang; Sheng Di; Guanpeng Li; Franck Cappello"
tags:
  - "SC2025"
  - "Compression and Data Reduction 2"
---

# GPU Lossy Compression for HPC Can Be Versatile and Ultra-Fast

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Compression and Data Reduction 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Compression and Data Reduction 2</p>
</div>

**作者**：Yafan Huang; Sheng Di; Guanpeng Li; Franck Cappello

**会议**：SC 2025 · St. Louis, MO

## 摘要

This work proposes VGC, a versatile and ultra-fast GPU lossy compression framework designed to address the growing data challenges in high performance computing (HPC). VGC captures dimension information in scientific data and supports three compression algorithms, achieving high compression ratios across diverse HPC domains. Built with a highly optimized GPU kernel, VGC delivers state-of-the-art throughput with error control. In addition to compression ratio and speed, VGC supports two distinctive modes that enhance its versatility. Memory-efficient compression uses a kernel fission design to compute compressed size, allocate only the required GPU memory, and compress data without waste, effectively reducing memory footprint. Selective decompression introduces an early stopping mechanism that enables direct access to regions of interest without decompressing the entire dataset.

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
