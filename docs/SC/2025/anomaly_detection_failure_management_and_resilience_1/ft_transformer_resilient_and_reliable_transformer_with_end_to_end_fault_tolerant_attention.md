---
title: "FT-Transformer: Resilient and Reliable Transformer with End-to-End Fault-Tolerant Attention"
description: "SC 2025 · Anomaly Detection, Failure Management, and Resilience 1 · Huangliang Dai; Shixun Wu; Jiajun Huang; Zizhe Jian; Yue Zhu; Haiyang Hu; Zizhon"
tags:
  - "SC2025"
  - "Anomaly Detection, Failure Management, and Resilience 1"
---

# FT-Transformer: Resilient and Reliable Transformer with End-to-End Fault-Tolerant Attention

**中文标题：** 具有端到端容错注意力的弹性可靠 Transformer

**所属 Session：** [Anomaly Detection, Failure Management, and Resilience 1](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Anomaly Detection, Failure Management, and Resilience 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Anomaly Detection, Failure Management, and Resilience 1</p>
</div>

**作者**：Huangliang Dai; Shixun Wu; Jiajun Huang; Zizhe Jian; Yue Zhu; Haiyang Hu; Zizhong Chen

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap621&sess=sess289)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Transformer models rely on high performance computing (HPC) resources for inference, where soft errors are inevitable in large-scale systems, making the reliability of the model particularly critical. Existing fault tolerance frameworks for transformers are designed at the operation level without architectural optimization, leading to significant computational and memory overhead, which in turn reduces protection efficiency and limits scalability to larger models. In this paper, we implement module-level protection for transformers by treating the operations within the attention module as a single kernel and applying end-to-end fault tolerance. This method provides unified protection across multi-step computations, while achieving comprehensive coverage of potential errors in the nonlinear computations. For linear modules, we design a strided algorithm-based fault tolerance (ABFT) that avoids inter-thread communication. Experimental results show that our end-to-end fault tolerance achi

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
