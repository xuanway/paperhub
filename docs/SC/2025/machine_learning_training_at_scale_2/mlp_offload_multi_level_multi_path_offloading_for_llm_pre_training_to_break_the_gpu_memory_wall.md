---
title: "MLP-Offload: Multi-Level, Multi-Path Offloading for LLM Pre-Training To Break the GPU Memory Wall"
description: "SC 2025 · Machine Learning: Training at Scale 2 · Avinash Kumar Maurya; M. Mustafa Rafique; Franck Cappello; Bogdan Nicolae"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 2"
---

# MLP-Offload: Multi-Level, Multi-Path Offloading for LLM Pre-Training To Break the GPU Memory Wall

**中文标题：** 面向大语言模型预训练的多级多路径卸载以突破 GPU 内存墙

**所属 Session：** [Machine Learning: Training at Scale 2](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 2</p>
</div>

**作者**：Avinash Kumar Maurya; M. Mustafa Rafique; Franck Cappello; Bogdan Nicolae

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap674&sess=sess167)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Large language models (LLMs) have been rapidly adopted across all domains, supporting divergent use cases with remarkable accuracy. However, training these massive models requires scaling across multiple GPUs. Given the expensive and limited GPU resources, advanced redundancy elimination and parallelization techniques are employed to maximize training throughput. Furthermore, to run LLMs larger than the aggregated memory of multiple GPUs, host memory or disk offloading techniques are leveraged. Despite advanced asynchronous multi-tier read/write strategies, such offloading strategies result in significant I/O overheads in the critical path of training. To this end, we propose MLP-Offload, a novel multi-level, multi-path offloading engine specifically designed for optimizing LLM training on resource-constrained setups by mitigating I/O bottlenecks. We design and implement MLP-Offload to offload the optimizer states across multiple tiers in a cache-efficient and concurrency-controlled fa

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
