---
title: "Lit Silicon: A Case Where Thermal Imbalance Couples Concurrent Execution in Multiple GPUs"
description: "ISCA 2026 · Session 9D · Lit Silicon: A Case Where Thermal Imbalance Couples Concurrent Execution in Multiple GPUs"
tags:
  - "ISCA2026"
  - "Session 9D"
  - "Sustainability and Energy Efficiency"
---

# Lit Silicon: A Case Where Thermal Imbalance Couples Concurrent Execution in Multiple GPUs

**中文标题：** Lit Silicon: 热失衡耦合多 GPU 并发执行的一个案例

**所属 Session：** [Session 9D](index.md) · [ISCA 2026](../index.md)

**作者：** Marco Kurzynski, Shaizeen Aga

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

GPU systems are increasingly powering modern datacenters at scale. Despite being highly performant, GPU systems can exhibit performance variation at the node and cluster levels. Such performance variation can significantly impact both high-performance computing and artificial intelligence workloads, such as cutting-edge large language models (LLMs). In this work, we analyze the performance of a single-node multi-GPU system running LLM training, and observe that the kernel-level performance variation is highly correlated with concurrent computation and communication (C3), a technique to overlap computation and communication across GPUs for performance gains. We then take a further step to reason that thermally induced straggling coupled with C3 impacts performance variation, which we coin the Lit Silicon effect. More specifically, Lit Silicon describes that in a multi-GPU node, thermal imbalance across GPUs can introduce node-level straggler GPUs (hotter and slower), which in turn slow down the leader GPUs (cooler and faster). Lit Silicon can lead to node-level performance variation and inefficiency, potentially impacting the entire datacenter. We propose analytical performance and power models for Lit Silicon, to understand the potential system-level gains. We further design simple detection and mitigation techniques to effectively address the Lit Silicon problem, and evaluate three different power management solutions, including (1) power optimization under GPU thermal design power, (2) performance optimization under node-level GPU power capping, and (3) performance optimization under node-level CPU power sloshing. We conduct experiments on two workloads on two AMD Instinct™MI300X GPU systems under two LLM training frameworks, and observe up to 6% performance and 4% power improvements, potentially saving several tens of millions of dollars in electricity costs in datacenters. Our solution consists of approximately 200 lines of PyTorch code, requires no GPU kernel modifications, and can be deployed in datacenters as a new node-level power management layer. Our code is available on GitHub: https://github.com/UnaryLab/lit_silicon_tuning_amd.

## 中文摘要

GPU 系统正日益大规模地驱动现代数据中心。尽管性能很高，GPU 系统仍可能在节点和集群层面表现出性能波动。这种性能波动会显著影响高性能计算和人工智能工作负载，例如前沿的大语言模型（LLM）。在这项工作中，我们分析了运行 LLM 训练的单节点多 GPU 系统的性能，并观察到内核级性能波动与并发计算与通信（C3）高度相关，C3 是一种跨 GPU 重叠计算和通信以提升性能的技术。我们进一步推理认为，热引起的落后者与 C3 耦合会影响性能波动，我们将其命名为 Lit Silicon 效应。更具体地说，Lit Silicon 描述了在多 GPU 节点中，GPU 之间的热失衡会引入节点级落后 GPU（更热、更慢），进而拖慢领先 GPU（更冷、更快）。Lit Silicon 可能导致节点级性能波动和低效，并可能影响整个数据中心。我们为 Lit Silicon 提出了分析性的性能和功耗模型，以理解潜在的系统级收益。我们进一步设计了简单的检测和缓解技术以有效解决 Lit Silicon 问题，并评估了三种不同的功耗管理方案，包括（1）在 GPU 热设计功耗下的功耗优化，（2）在节点级 GPU 功耗上限下的性能优化，以及（3）在节点级 CPU 功耗振荡下的性能优化。我们在两种 LLM 训练框架下，于两个 AMD Instinct™ MI300X GPU 系统上对两个工作负载进行了实验，观察到高达 6% 的性能提升和 4% 的功耗改善，有可能为数据中心节省数千万美元的电费。我们的方案由约 200 行 PyTorch 代码组成，无需修改 GPU 内核，并可作为新的节点级功耗管理层部署在数据中心。我们的代码已在 GitHub 上提供：https://github.com/UnaryLab/lit_silicon_tuning_amd。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：UnaryLab/lit_silicon_tuning_amd](https://github.com/UnaryLab/lit_silicon_tuning_amd)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9D](index.md) · [返回 ISCA 2026](../index.md)
