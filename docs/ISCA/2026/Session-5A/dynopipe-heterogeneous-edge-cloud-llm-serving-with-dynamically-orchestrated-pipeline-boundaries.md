---
title: "DynoPipe: Heterogeneous Edge-Cloud LLM Serving with Dynamically Orchestrated Pipeline Boundaries"
description: "ISCA 2026 · Session 5A · DynoPipe: Heterogeneous Edge-Cloud LLM Serving with Dynamically Orchestrated Pipeline Boundaries"
tags:
  - "ISCA2026"
  - "Session 5A"
  - "LLM 3"
---

# DynoPipe: Heterogeneous Edge-Cloud LLM Serving with Dynamically Orchestrated Pipeline Boundaries

**中文标题：** DynoPipe: 动态编排流水线边界的异构边云 LLM 服务

**所属 Session：** [Session 5A](index.md) · [ISCA 2026](../index.md)

**作者：** Yanying Lin, Baicheng Chen, Xinyu Zhang, Chengzhong Xu, Kejiang Ye

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Large language model (LLM) deployment at the network edge faces a fundamental paradox: applications require full-scale models for sophisticated reasoning, yet edge devices impose severe resource constraints across computation, memory, and network. Existing approaches fail to effectively orchestrate resources across the edge-cloud continuum, leaving capacity under-utilized while struggling with heterogeneous and volatile distributed environments. We present DynoPipe, an adaptive edge-cloud system that addresses these constraints through dynamic pipeline parallelism with shifting computational boundaries. DynoPipe tackles three core challenges: structural heterogeneity causing 94% pipeline idle time, temporal resource volatility invalidating static partitioning, and boundary migration overhead trapping systems in suboptimal configurations. Through boundary-constrained pipeline construction, proactive multi-configuration orchestration, and hierarchical state management, DynoPipe eliminates the memory wall while preserving data locality, achieving 10.1× throughput improvement over edge-only baselines and 1.6× over cloud-only execution, with 99.2% latency reduction.

## 中文摘要

大语言模型（LLM）在网络边缘的部署面临一个根本性悖论：应用需要全尺寸模型来完成复杂推理，而边缘设备在计算、内存和网络上都受到严重约束。现有方法无法有效编排边缘—云连续体上的资源，导致容量利用率不足，同时难以应对异构且易变的分布式环境。我们提出 DynoPipe——一个自适应的边缘—云系统，通过计算边界可迁移的动态流水线并行来应对这些约束。DynoPipe 解决了三大核心挑战：造成 94% 流水线空闲时间的结构异构性、使静态划分失效的时序资源波动性，以及使系统陷入次优配置的边界迁移开销。通过边界约束的流水线构建、主动式多配置编排和分层状态管理，DynoPipe 在保持数据局部性的同时消除了内存墙，相比纯边缘基线实现 10.1× 的吞吐提升、相比纯云端执行提升 1.6×，并将延迟降低 99.2%。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5A](index.md) · [返回 ISCA 2026](../index.md)
