---
title: "Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles"
description: "ISCA 2026 · Session 5B · Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles"
tags:
  - "ISCA2026"
  - "Session 5B"
  - "Industry Track 2"
---

# Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles

**中文标题：** 理解 LLM 推理扩展：瓶颈、权衡与性能原理

**所属 Session：** [Session 5B](index.md) · [ISCA 2026](../index.md)

**作者：** Moiz Arif, Avinash Maurya, Sudharshan Vazhkudai, Bogdan Nicolae

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The transition from standard generative AI to reasoning-centric architectures, exemplified by models capable of extensive Chain-of-Thought (CoT) processing, marks a fundamental paradigm shift in system requirements. Unlike traditional workloads dominated by compute-bound prefill, reasoning workloads generate long chains of reasoning tokens that shift inference into a Capacity-Bound regime. This paper presents a comprehensive system characterization, evaluating models ranging from 8B to 671B parameters on GPUs clusters. By systematically exploring the interplay between Data, Tensor, and Pipeline parallelism, we identify critical bottlenecks that defy standard scaling heuristics. Our analysis reveals that data parallelism is throughput efficient for small models but hits a capacity trap on reasoning workloads as KV-cache fragmentation forces early throttling resulting in sub-optimal compute utilization. Tensor parallelism unlocks stranded memory and delivers sublinear gains near the 32B crossover. At frontier scale, dense models (e.g., Llama-405B) are interconnect and memory-bandwidth bound and favor high-degree TP, while sparse Mixture-of-Experts (MoE) models (e.g., DeepSeek-R1) are limited by routing and synchronization latency and benefit from hybrid strategies. These insights provide a rigorous decision framework for navigating the reasoning cliff, establishing new architectural imperatives for the next generation of inference infrastructure.

## 中文摘要

从标准生成式 AI 向以推理为中心的架构转变——以能够进行长链思维链（CoT）处理的模型为代表——标志着系统需求上的根本范式转变。与以往由计算受限的预填充（prefill）主导的负载不同，推理负载会生成很长的推理 token 链，使推理进入容量受限（Capacity-Bound）的状态。本文给出了一项系统性的系统刻画，在 GPU 集群上评估了从 8B 到 671B 参数规模的模型。通过系统地探索数据并行、张量并行与流水线并行之间的相互作用，我们识别出违背标准扩展经验法则的关键瓶颈。我们的分析揭示：数据并行对小模型而言吞吐高效，但在推理负载上会遭遇容量陷阱——KV 缓存碎片迫使提前限流，导致计算利用率次优。张量并行可释放滞留的内存，并在接近 32B 这一临界点时带来次线性收益。在前沿规模下，稠密模型（如 Llama-405B）受互连与内存带宽约束，倾向于高并行度的张量并行；而稀疏混合专家（MoE）模型（如 DeepSeek-R1）受路由与同步时延限制，可从混合策略中获益。这些洞见为跨越“推理悬崖”提供了严谨的决策框架，并为下一代推理基础设施确立了新的架构要求。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5B](index.md) · [返回 ISCA 2026](../index.md)
