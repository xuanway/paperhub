---
title: "GPU Lossy Compression for HPC Can Be Versatile and Ultra-Fast"
description: "SC 2025 · Compression and Data Reduction 2 · Yafan Huang; Sheng Di; Guanpeng Li; Franck Cappello"
tags:
  - "SC2025"
  - "Compression and Data Reduction 2"
---

# GPU Lossy Compression for HPC Can Be Versatile and Ultra-Fast

**中文标题：** 面向 HPC 的 GPU 有损压缩可以兼具通用性与极速

**所属 Session：** [Compression and Data Reduction 2](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Compression and Data Reduction 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Compression and Data Reduction 2</p>
</div>

**作者**：Yafan Huang; Sheng Di; Guanpeng Li; Franck Cappello

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap399&sess=sess280)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

This work proposes VGC, a versatile and ultra-fast GPU lossy compression framework designed to address the growing data challenges in high performance computing (HPC). VGC captures dimension information in scientific data and supports three compression algorithms, achieving high compression ratios across diverse HPC domains. Built with a highly optimized GPU kernel, VGC delivers state-of-the-art throughput with error control. In addition to compression ratio and speed, VGC supports two distinctive modes that enhance its versatility. Memory-efficient compression uses a kernel fission design to compute compressed size, allocate only the required GPU memory, and compress data without waste, effectively reducing memory footprint. Selective decompression introduces an early stopping mechanism that enables direct access to regions of interest without decompressing the entire dataset.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
