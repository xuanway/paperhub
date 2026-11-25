---
title: "HARP: Orchestrating Automated Parallel Training on Heterogeneous GPU Clusters"
description: "EuroSys 2026 · LLM Training at Scale · Antian Liang (Fudan University), Zhigang Zhao (Fudan University), Kai Zhang (Fud"
tags:
  - "EuroSys2026"
  - "LLM Training at Scale"
---

# HARP: Orchestrating Automated Parallel Training on Heterogeneous GPU Clusters

**中文标题：** HARP：在异构 GPU 集群上编排自动化并行训练

**所属 Session：** [Session 3.1: LLM Training at Scale](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Training at Scale。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Training at Scale</p>
</div>

**作者**：Antian Liang (Fudan University), Zhigang Zhao (Fudan University), Kai Zhang (Fudan University), Xuri Shi (Fudan University), Chuantao Li (Shandong Computer Science Center (National Supercomputer Center in Jinan)), Chunxiao Wang (Shandong Computer Science Center (National Supercomputer Center in Jinan)), Zhenying He (Fudan University), Yinan Jing (Fudan University), X. Sean Wang (Fudan University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803603)

## 英文摘要

With the rapid evolution of GPU architectures, the heterogeneity of model training infrastructures is steadily increasing. In such environments, effectively utilizing all available heterogeneous accelerators becomes critical for distributed model training. However, existing frameworks, which are primarily designed for homogeneous clusters, often exhibit significant resource underutilization when deployed on heterogeneous accelerators and networks. In this paper, we present Harp, an automated parallel training framework designed specifically for heterogeneous clusters. Harp introduces a fine-grained planner that efficiently searches a wide space for the inter-operator parallel strategy, enabling Harp to alleviate communication overheads while maintaining balanced loads across heterogeneous accelerators. In addition, Harp implements a heterogeneity-aware 1F1B scheduler that adaptively adjusts the execution timing and ordering of microbatches based on network characteristics, maximizing computation–communication overlap under cross-cluster interconnects while incurring only minimal memory overhead. Our evaluation results show that Harp can deliver 1.3×–1.6× higher performance on heterogeneous clusters than state-of-the-art training frameworks.

## 中文摘要

随着 GPU 架构的快速演进，模型训练基础设施的异构程度持续上升。在此类环境中，有效利用所有可用的异构加速器对分布式模型训练至关重要。然而，现有框架主要面向同构集群设计，部署到异构加速器与网络上时往往表现出严重的资源利用率不足。本文提出 Harp，一个专为异构集群设计的自动化并行训练框架。Harp 引入细粒度规划器，能够高效地在广阔空间中搜索算子间并行策略，从而在异构加速器之间保持负载均衡的同时缓解通信开销。此外，Harp 实现了异构感知的 1F1B 调度器，可根据网络特性自适应调整微批的执行时机与顺序，在跨集群互连下最大化计算与通信的重叠，且仅带来极小的内存开销。我们的评测结果表明，Harp 在异构集群上相比最先进的训练框架可实现 1.3 倍至 1.6 倍的性能提升。

**英文关键词：** Distributed Training, Heterogeneous GPU Clusters

**中文关键词：** 分布式训练、异构 GPU 集群

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
