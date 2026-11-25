---
title: "PiLLM: Resource-Efficient LLM Inference Using Workload Prediction"
description: "EuroSys 2026 · LLM Serving & Agents · Yunqian Fan (ShanghaiTech University), Shihao Bai (SenseTime), Ruihao Gong (Beih"
tags:
  - "EuroSys2026"
  - "LLM Serving & Agents"
---

# PiLLM: Resource-Efficient LLM Inference Using Workload Prediction

**中文标题：** PiLLM：利用工作负载预测实现资源高效的 LLM 推理

**所属 Session：** [Session 8.1: LLM Serving & Agents](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Serving & Agents。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Serving & Agents</p>
</div>

**作者**：Yunqian Fan (ShanghaiTech University), Shihao Bai (SenseTime), Ruihao Gong (Beihang University), Zaijun Wang (SenseTime), Rui Fan (ShanghaiTech University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769393)

## 英文摘要

LLM inference demands substantial GPU resources, but its highly variable workload characteristics create efficiency challenges at both inter-GPU and intra-GPU levels. To meet Service Level Objectives (SLOs), existing systems typically overprovision resources in two ways: allocating excess GPUs to handle peak loads and reserving excessive memory per request to prevent out-of-memory during token generation. We introduce PiLLM (Predictable inference for LLMs), a system that addresses these inefficiencies through accurate workload prediction and dynamic resource allocation.

PiLLM’s core lies in the statistical prediction algorithm that accurately models computational and memory requirements by analyzing input/output sequence lengths distribution and request patterns. This enables two complementary optimizations: (1) an elastic inter-GPU dispatch mechanism that dynamically scales GPUs based on workload forecasts, and (2) an intra-GPU scheduler that improves utilization but reduces eviction through precise memory allocation.

We implement PiLLM on top of the disaggregated prefill/decode paradigm for fine-grained GPU saving. Extensive evaluation on production workloads with load fluctuations demonstrates that PiLLM significantly improves resource efficiency without compromising SLOs. Our inter-GPU dispatch reduces average usage by 1.6- 3.1x while maintaining SLO compliance, and our intra-GPU scheduler achieves throughput improvements with negligible eviction rates (<0.1%).

## 中文摘要

LLM 推理需要大量 GPU 资源，而其高度可变的工作负载特征在 GPU 间和 GPU 内两个层面都带来了效率挑战。为满足服务等级目标（SLO），现有系统通常以两种方式过度配置资源：分配多余的 GPU 以应对峰值负载，以及为每个请求预留过多内存以避免 token 生成过程中出现内存不足。我们提出 PiLLM（面向 LLM 的可预测推理），一个通过准确的工作负载预测和动态资源分配来解决这些低效问题的系统。

PiLLM 的核心是一个统计预测算法，它通过分析输入/输出序列长度分布和请求模式，准确建模计算与内存需求。这带来了两项互补的优化：(1) 一种弹性 GPU 间调度机制，根据工作负载预测动态伸缩 GPU；(2) 一种 GPU 内调度器，通过精确的内存分配提高利用率并减少换出。

我们在解耦的 prefill/decode 范式之上实现 PiLLM，以实现细粒度的 GPU 节省。在生产工作负载上针对负载波动的广泛评估表明，PiLLM 在不损害 SLO 的前提下显著提升了资源效率。我们的 GPU 间调度在保持 SLO 合规的同时将平均使用量降低 1.6–3.1 倍，GPU 内调度器则实现了吞吐提升，而换出率可忽略（<0.1%）。

**英文关键词：** Large Model Inference, GPU Management, Efficient Computation, Load Prediction, Quality of Service

**中文关键词：** 大模型推理、GPU 管理、高效计算、负载预测、服务质量

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
