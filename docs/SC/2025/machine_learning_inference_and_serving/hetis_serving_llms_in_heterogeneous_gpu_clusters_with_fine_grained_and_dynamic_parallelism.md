---
title: "Hetis: Serving LLMs in Heterogeneous GPU Clusters with Fine-Grained and Dynamic Parallelism"
description: "SC 2025 · Machine Learning: Inference and Serving · Zizhao Mo; Jianxiong Liao; Huanle Xu; Zhi Zhou; ChengZhong Xu"
tags:
  - "SC2025"
  - "Machine Learning: Inference and Serving"
---

# Hetis: Serving LLMs in Heterogeneous GPU Clusters with Fine-Grained and Dynamic Parallelism

**中文标题：** 通过细粒度动态并行在异构 GPU 集群上提供大语言模型服务

**所属 Session：** [Machine Learning: Inference and Serving](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Inference and Serving。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Inference and Serving</p>
</div>

**作者**：Zizhao Mo; Jianxiong Liao; Huanle Xu; Zhi Zhou; ChengZhong Xu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap192&sess=sess168)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Significant resource demands in LLM serving prompts for full utilization on heterogeneous GPUs. However, existing works often struggle to scale efficiently in heterogeneous environments due to their coarse-grained and static parallelization strategies. In this paper, we introduce Hetis, a system optimized for heterogeneous GPU clusters. Hetis addresses two critical challenges: memory inefficiency caused by the mismatch between memory capacity and computational power, and computational inefficiency arising from performance gaps across different LLM modules. To tackle these issues, Hetis employs a fine-grained and dynamic parallelism design. Specifically, it selectively parallelizes compute-intensive operations to reduce latency and dynamically distributes attention computations to low-end GPUs at a head granularity, leveraging the distinct characteristics of each module. Additionally, Hetis features an online load dispatching policy, continuously optimizing performance by balancing netw

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
