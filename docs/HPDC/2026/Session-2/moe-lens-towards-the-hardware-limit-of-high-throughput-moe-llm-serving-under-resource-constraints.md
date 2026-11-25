---
title: "MoE-Lens: Towards the Hardware Limit of High-Throughput MoE LLM Serving Under Resource Constraints"
description: "HPDC 2026 · Session 2 — Scaling Generative Inference"
tags:
  - "HPDC2026"
  - "Session 2"
  - "Scaling Generative Inference"
---

# MoE-Lens: Towards the Hardware Limit of High-Throughput MoE LLM Serving Under Resource Constraints

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 2 — Scaling Generative Inference（2026年7月14日 11:30–12:30 · Session Chair：Bogdan Nicolae）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 2</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807594)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#YuanMT26](https://dblp.org/db/conf/hpdc/hpdc2026.html#YuanMT26)

**作者**：Yichao Yuan, Lin Ma, Nishil Talati

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 2 — Scaling Generative Inference（2026年7月14日 11:30–12:30 · Session Chair：Bogdan Nicolae）

---

## 英文摘要

Mixture of Experts (MoE) LLMs, with sparse activation patterns, offer a promising approach to scaling language models while avoiding proportional cost increases. However, their large parameter sizes pose deployment challenges in resource-constrained environments with limited GPU memory. Typical deployments use CPU-GPU hybrid execution, where the GPU handles compute-intensive GEMM operations and the CPU processes the attention mechanism. This setup introduces a challenge: optimizing resource utilization across CPU and GPU. Prior work designs system optimizations based on performance models with a limited scope that don’t capture complex hardware-system interactions. Therefore, they neither identify nor achieve hardware limits. This paper presents MoE-Lens, a high-throughput MoE LLM inference system designed for resource-constrained environments. MoE-Lens utilizes a novel performance model that holistically analyzes CPU memory capacity, GPU compute power, and workload characteristics to understand the theoretical performance upper bound of MoE inference. It also captures system execution mechanisms, including workload scheduling and the effects of paged KV cache, to identify key hardware bottlenecks and predict achievable throughput. Guided by such a performance model, MoE-Lens introduces a resource-aware scheduler, an execution engine that overlaps computation, a data transfer mechanism for model weights, and an optimized CPU-based attention implementation. Evaluated on diverse MoE models and datasets, MoE-Lens outperforms the state-of-the-art MoE-Lightening by 4.6× (up to 25.5×), with our theoretical model predicting performance with an average 94% accuracy.

## 中文摘要

混合专家（MoE）LLM 凭借稀疏激活模式，为扩展语言模型提供了一种前景广阔的方法，同时避免成本成比例上升。然而，其庞大的参数量给显存有限的资源受限环境带来部署挑战。典型部署采用 CPU-GPU 混合执行：GPU 处理计算密集的 GEMM 运算，CPU 处理注意力机制。这种设置带来一个挑战：优化跨 CPU 与 GPU 的资源利用。已有工作基于适用范围有限、无法刻画复杂硬件-系统交互的性能模型来设计系统优化，因此既无法识别也无法达到硬件极限。本文提出 MoE-Lens，一个面向资源受限环境的高吞吐 MoE LLM 推理系统。MoE-Lens 采用新颖的性能模型，整体分析 CPU 内存容量、GPU 算力与负载特征，以理解 MoE 推理的理论性能上界；同时刻画系统执行机制，包括负载调度与分页 KV cache 的影响，从而识别关键硬件瓶颈并预测可达吞吐。在该性能模型指导下，MoE-Lens 引入资源感知调度器、可重叠计算的执行引擎、面向模型权重的数据传输机制，以及优化的基于 CPU 的注意力实现。在多种 MoE 模型与数据集上的评估表明，MoE-Lens 比最先进的 MoE-Lightening 高出 4.6 倍（最高 25.5 倍），且理论模型预测性能的平均准确率达到 94%。

## 英文关键词

Mixture-of-Experts, large language model inference, CPU-GPU hybrid execution, performance modeling, scheduling, KV cache

## 中文关键词

混合专家，大语言模型推理，CPU-GPU 混合执行，性能建模，调度，KV 缓存

---

[← 返回 Session 2 — Scaling Generative Inference](index.md)
