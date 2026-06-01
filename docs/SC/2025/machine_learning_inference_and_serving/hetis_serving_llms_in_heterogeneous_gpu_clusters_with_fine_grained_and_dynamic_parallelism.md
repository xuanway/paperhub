---
title: "Hetis: Serving LLMs in Heterogeneous GPU Clusters with Fine-Grained and Dynamic Parallelism"
description: "SC 2025 · Machine Learning: Inference and Serving · Zizhao Mo; Jianxiong Liao; Huanle Xu; Zhi Zhou; ChengZhong Xu"
tags:
  - "SC2025"
  - "Machine Learning: Inference and Serving"
---

# Hetis: Serving LLMs in Heterogeneous GPU Clusters with Fine-Grained and Dynamic Parallelism

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Inference and Serving。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Inference and Serving</p>
</div>

**作者**：Zizhao Mo; Jianxiong Liao; Huanle Xu; Zhi Zhou; ChengZhong Xu

**会议**：SC 2025 · St. Louis, MO

## 摘要

Significant resource demands in LLM serving prompts for full utilization on heterogeneous GPUs. However, existing works often struggle to scale efficiently in heterogeneous environments due to their coarse-grained and static parallelization strategies. In this paper, we introduce Hetis, a system optimized for heterogeneous GPU clusters. Hetis addresses two critical challenges: memory inefficiency caused by the mismatch between memory capacity and computational power, and computational inefficiency arising from performance gaps across different LLM modules. To tackle these issues, Hetis employs a fine-grained and dynamic parallelism design. Specifically, it selectively parallelizes compute-intensive operations to reduce latency and dynamically distributes attention computations to low-end GPUs at a head granularity, leveraging the distinct characteristics of each module. Additionally, Hetis features an online load dispatching policy, continuously optimizing performance by balancing netw

---

## 一句话总结

> 该工作属于 Machine Learning: Inference and Serving 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Machine Learning: Inference and Serving 领域贡献新的设计范式或评估框架。
