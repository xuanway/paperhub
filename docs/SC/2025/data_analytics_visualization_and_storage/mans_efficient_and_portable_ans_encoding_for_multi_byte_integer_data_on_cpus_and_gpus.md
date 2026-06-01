---
title: "MANS: Efficient and Portable ANS Encoding for Multi-Byte Integer Data on CPUs and GPUs"
description: "SC 2025 · Data Analytics, Visualization, and Storage · Wenjing Huang; Jinwu Yang; Shengquan Yin; Haoxu Li; Yida Gu; Zedong Liu; Xing Ji"
tags:
  - "SC2025"
  - "Data Analytics, Visualization, and Storage"
---

# MANS: Efficient and Portable ANS Encoding for Multi-Byte Integer Data on CPUs and GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Data Analytics, Visualization, and Storage。</p>
<p class="paper-seo-summary__tags">SC 2025 · Data Analytics, Visualization, and Storage</p>
</div>

**作者**：Wenjing Huang; Jinwu Yang; Shengquan Yin; Haoxu Li; Yida Gu; Zedong Liu; Xing Jing; Zheng Wei; Shiyuan Fu; Hao Hu; Guangming Tan; Dingwen Tao

**会议**：SC 2025 · St. Louis, MO

## 摘要

Lossless compression is a classic technique for reducing data storage and transmission requirements. Asymmetric numeral systems (ANS) is a high-throughput, high-ratio lossless compression algorithm, but it lacks effective support for multi-byte data and cross-platform compatibility. To address this issue, we propose an adaptive data mapping (ADM) scheme, which maps multi-byte integer data into single-byte space based on the data's characteristics, improving the compression ratio of ANS while maintaining low encoding redundancy. We also optimize the ADM algorithm and the ANS encoder for GPU and CPU architectures, respectively, and combine them to create an efficient and portable ANS encoding method for multi-byte integer data, called MANS. Experimental results show that MANS improves compression ratios by an average of 1.24$\times$, achieves 870.27MB/s throughput on CPUs, and delivers up to 288.45$\times$ and 135.86$\times$ speedups on an NVIDIA A100 and an AMD MI210 GPU compared to the

---

## 一句话总结

> 该工作属于 Data Analytics, Visualization, and Storage 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Data Analytics, Visualization, and Storage 领域贡献新的设计范式或评估框架。
