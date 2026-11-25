---
title: "Dynamo-MoE: Accelerating Sparse Large Model Inference with Dynamic Parallelization"
description: "HPDC 2026 · Session 12 — Emerging Generative & Agentic AI Workloads"
tags:
  - "HPDC2026"
  - "Session 12"
  - "Emerging Generative & Agentic AI Workloads"
---

# Dynamo-MoE: Accelerating Sparse Large Model Inference with Dynamic Parallelization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 12 — Emerging Generative & Agentic AI Workloads（2026年7月16日 14:40–15:40 · Session Chair：Stefan Andrei）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 12</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807820)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#ChenLFWMD26](https://dblp.org/db/conf/hpdc/hpdc2026.html#ChenLFWMD26)

**作者**：Jiahao Chen, Shigang Li, Rongtian Fu, Tong Wu, Zhi Ma, Jingkun Dong

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 12 — Emerging Generative & Agentic AI Workloads（2026年7月16日 14:40–15:40 · Session Chair：Stefan Andrei）

---

## 英文摘要

Mixtral-of-Experts (MoE) has become one of the major model structures in LLMs because of its computational efficiency when scaling the model size. However, MoE model inference suffers from critical load imbalance issue caused by the sparsely and dynamically activated experts. In addition, current inference frameworks are oblivious to the real-time workload fluctuation, a common phenomenon in LLM serving. Therefore, the static model deployment of existing frameworks leads to severe performance limitations. To this end, we propose Dynamo-MoE, an out-of-box MoE inference framework to bridge the performance gap by dynamic parallelization strategies. Specifically, Dynamo-MoE integrates a novel load balancing approach based on token sorting and on-demand expert loading to solve the workload imbalance issue in the scenario of high workload (such as Prefill). Dynamo-MoE is also aware of workload varying to adaptively switch between tensor parallelism (for low latency in small batch scenarios) and expert parallelism (for high throughput in large batch scenarios). Furthermore, the model parameter redistribution overhead of dynamic parallelization is smartly overlapped through sophisticated pipeline orchestration. Compared to the SOTA framework vLLM (w/ and w/o EPLB), Dynamo-MoE achieves up to 6.75× reduction for TTFT, 1.59× reduction for TPOT, and 1.5× improvement for throughput.

## 中文摘要

Mixtral-of-Experts（MoE）已成为 LLM 的主要模型结构之一，因为它在扩展模型规模时具有计算效率。然而，MoE 模型推理因专家稀疏且动态激活而存在严重的负载不均衡问题。此外，当前推理框架对实时负载波动（LLM 服务中的常见现象）不敏感。因此，现有框架的静态模型部署导致严重的性能局限。为此，我们提出 Dynamo-MoE，一个开箱即用的 MoE 推理框架，通过动态并行化策略弥合性能差距。具体而言，Dynamo-MoE 集成了一种基于令牌排序和按需专家加载的新负载均衡方法，以解决高负载场景（如预填充）下的负载不均衡问题。Dynamo-MoE 还能感知负载变化，在张量并行（小批次场景下的低延迟）与专家并行（大批次场景下的高吞吐）之间自适应切换。此外，动态并行化带来的模型参数重分布开销通过精巧的流水线编排被巧妙地重叠隐藏。与最先进框架 vLLM（使用和不使用 EPLB）相比，Dynamo-MoE 将 TTFT 最高降低 6.75 倍、TPOT 降低 1.59 倍，吞吐提升 1.5 倍。

## 英文关键词

LLM Inference, MoE, Distributed AI Infrastructure, Expert Parallelism, Tensor Parallelism, Workload Balancing, Adaptive Parallelism Switching

## 中文关键词

LLM 推理，MoE，分布式 AI 基础设施，专家并行，张量并行，负载均衡，自适应并行切换

---

[← 返回 Session 12 — Emerging Generative & Agentic AI Workloads](index.md)
