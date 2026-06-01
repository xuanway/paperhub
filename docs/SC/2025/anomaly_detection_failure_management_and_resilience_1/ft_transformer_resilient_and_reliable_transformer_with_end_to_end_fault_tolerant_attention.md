---
title: "FT-Transformer: Resilient and Reliable Transformer with End-to-End Fault-Tolerant Attention"
description: "SC 2025 · Anomaly Detection, Failure Management, and Resilience 1 · Huangliang Dai; Shixun Wu; Jiajun Huang; Zizhe Jian; Yue Zhu; Haiyang Hu; Zizhon"
tags:
  - "SC2025"
  - "Anomaly Detection, Failure Management, and Resilience 1"
---

# FT-Transformer: Resilient and Reliable Transformer with End-to-End Fault-Tolerant Attention

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Anomaly Detection, Failure Management, and Resilience 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Anomaly Detection, Failure Management, and Resilience 1</p>
</div>

**作者**：Huangliang Dai; Shixun Wu; Jiajun Huang; Zizhe Jian; Yue Zhu; Haiyang Hu; Zizhong Chen

**会议**：SC 2025 · St. Louis, MO

## 摘要

Transformer models rely on high performance computing (HPC) resources for inference, where soft errors are inevitable in large-scale systems, making the reliability of the model particularly critical. Existing fault tolerance frameworks for transformers are designed at the operation level without architectural optimization, leading to significant computational and memory overhead, which in turn reduces protection efficiency and limits scalability to larger models. In this paper, we implement module-level protection for transformers by treating the operations within the attention module as a single kernel and applying end-to-end fault tolerance. This method provides unified protection across multi-step computations, while achieving comprehensive coverage of potential errors in the nonlinear computations. For linear modules, we design a strided algorithm-based fault tolerance (ABFT) that avoids inter-thread communication. Experimental results show that our end-to-end fault tolerance achi

---

## 一句话总结

> 该工作属于 Anomaly Detection, Failure Management, and Resilience 1 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Anomaly Detection, Failure Management, and Resilience 1 领域贡献新的设计范式或评估框架。
