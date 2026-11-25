---
title: "Wayfinder: Automated Operating System Specialization"
description: "EuroSys 2026 · Virtualization, Containers & OS Specialization · Alexander Jung (Lancaster University), Cezar Crăciunoiu (Politehnica University "
tags:
  - "EuroSys2026"
  - "Virtualization, Containers & OS Specialization"
---

# Wayfinder: Automated Operating System Specialization

**中文标题：** Wayfinder：自动化操作系统特化

**所属 Session：** [Session 11.3: Virtualization, Containers & OS Specialization](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Virtualization, Containers & OS Specialization。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Virtualization, Containers & OS Specialization</p>
</div>

**作者**：Alexander Jung (Lancaster University), Cezar Crăciunoiu (Politehnica University of Bucharest), Nikolaos Karaolidis (The University of Manchester), Hugo Lefeuvre (The University of British Columbia), Daniel Oñoro Rubio (NEC Laboratories Europe), Felipe Huici (Unikraft GmbH), Charalampos Rotsos (Lancaster University), Pierre Olivier (The University of Manchester)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803589)

## 英文摘要

Operating system specialization is a well-known approach to optimize a specific application’s performance, memory usage, security, or other important metrics. Specializing an OS for an application is typically a manual process that requires great expertise. Specialization through configuration lends itself well to automation; however, it is challenging due to the sheer size of the configuration space of modern OSes, the difficulty to quantify that space, the long time it takes to evaluate a configuration, and the large number of invalid configurations. Hence, existing attempts at specializing OSes automatically are limited to switching features on and off to minimize memory consumption or attack surface, and cannot target metrics such as performance.

We present Wayfinder, a framework specializing the configuration of OSes completely automatically and without expert knowledge. It can specialize all aspects of an OS configuration (compile-/boot-/run-time) towards any quantifiable performance, resource consumption, or security metric, for an application processing a given workload on a given hardware setup. Wayfinder consists of an automated OS benchmarking platform, and a neural network-based search algorithm driving the specialization process. This is achieved by learning on the fly which configuration parameters and values impact performance the most, and which ones lead to runtime failures. Optionally, a model pre-trained on one application can be reused to accelerate the specialization of related applications. We evaluate Wayfinder on two OSes, four applications, and two target metrics: Wayfinder fully automatically identifies specialized configurations with up to 24% application performance improvement and 8.5% memory usage reduction compared to default configurations. We highlight the benefits of our neural network, reaching good solutions faster than competing approaches (random and Bayesian), and successfully transferring knowledge between related applications.

## 中文摘要

操作系统特化是一种广为人知的方法，用于优化特定应用的性能、内存使用、安全性或其他重要指标。为某个应用特化操作系统通常是一个需要高超专业知识的纯手工过程。通过配置进行特化很适合自动化；然而，由于现代操作系统配置空间规模庞大、难以量化该空间、评估单个配置耗时很长，以及存在大量无效配置，这一过程充满挑战。因此，现有的操作系统自动特化尝试仅限于开启和关闭各种特性，以最小化内存消耗或攻击面，无法针对性能等指标。

我们提出Wayfinder，一个无需专家知识即可完全自动地特化操作系统配置的框架。它可以针对在给定硬件配置上处理给定负载的应用，将操作系统配置的所有方面（编译期/启动期/运行期）特化至任何可量化的性能、资源消耗或安全指标。Wayfinder由自动化操作系统基准测试平台和驱动特化过程的基于神经网络的搜索算法组成。这通过在运行过程中学习哪些配置参数及取值对性能影响最大、哪些会导致运行时故障来实现。可选地，在一个应用上预训练的模型可被复用以加速相关应用的特化。我们在两种操作系统、四个应用和两个目标指标上评估Wayfinder：与默认配置相比，Wayfinder完全自动地找出特化配置，使应用性能最高提升24%、内存使用降低8.5%。我们突显了所用神经网络的优势：它比竞争方法（随机搜索和贝叶斯方法）更快达到良好解，并成功在相关应用之间迁移知识。

**英文关键词：** Operating Systems, Specialization

**中文关键词：** 操作系统、特化

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
