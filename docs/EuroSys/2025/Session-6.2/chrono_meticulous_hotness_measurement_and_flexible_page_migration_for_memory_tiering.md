---
title: "Chrono: Meticulous Hotness Measurement and Flexible Page Migration for Memory Tiering"
description: "EuroSys 2025 · Memory Tiering and Disaggregation · Zhenlin Qi (Shanghai Jiao Tong University), Shengan Zheng (Shanghai Jiao Tong Un"
tags:
  - "EuroSys2025"
  - "Memory Tiering and Disaggregation"
---

# Chrono: Meticulous Hotness Measurement and Flexible Page Migration for Memory Tiering

**中文标题：** 通过精细热度测量和灵活页面迁移实现内存分层

**所属 Session：** [Session 6.2: Memory Tiering and Disaggregation](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Memory Tiering and Disaggregation。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Memory Tiering and Disaggregation</p>
</div>

**作者**：Zhenlin Qi (Shanghai Jiao Tong University), Shengan Zheng (Shanghai Jiao Tong University), Ying Huang (Intel), Yifeng Hui (Shanghai Jiao Tong University), Bowen Zhang (Shanghai Jiao Tong University), Linpeng Huang (Shanghai Jiao Tong University), Hong Mei (Shanghai Jiao Tong University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717462)

## 英文摘要

As the memory demand continues to surge, the limitations of DRAM scalability have spurred the development of various new memory technologies in today’s data centers. In order to harness the benefits of the heterogeneous memory architecture, tiering has become a widely adopted memory management paradigm. The effectiveness of a tiered memory management system primarily relies on its ability to accurately identify frequently accessed (“hot”) pages and infrequently accessed (“cold”) pages, and efficiently relocate them between tiers. However, existing systems rely on coarse-grained frequency measurement schemes that do not align with the performance characteristics of modern memory devices and memory-intensive applications. Additionally, these systems often incorporate rigid rules or manually configured parameters for page classification, resulting in inflexible migration strategies.

This paper introduces Chrono, a novel OS-level tiering system that offers precise characterization of page access frequencies in different tiers and enables efficient migration of hot and cold pages. By leveraging timers instead of counters, Chrono achieves meticulous measurement of hot page access frequency with low overhead. This approach allows Chrono to automatically tune its page classification parameters, leading to flexible migration strategies that adapt to various workloads. Furthermore, Chrono includes a dynamic cold page identification subsystem, which balances the utilization and availability of tiered memory. We have implemented and evaluated Chrono on existing tiered memory platforms, and experimental results demonstrate that Chrono outperforms state-of-the-art tiering systems by a large margin.

## 中文摘要

随着内存需求持续攀升，DRAM 可扩展性的局限推动了当今数据中心各类新型内存技术的发展。为发挥异构内存架构的优势，分层已成为一种广泛采用的内存管理范式。分层内存管理系统是否有效，主要取决于其能否准确识别频繁访问的（“热”）页和不频繁访问的（“冷”）页，并在各层之间高效地迁移它们。然而，现有系统依赖粗粒度的频率测量方案，与现代内存设备和内存密集型应用的性能特征不相匹配。此外，这些系统往往采用僵化的规则或人工配置的参数进行页分类，导致迁移策略缺乏灵活性。

本文提出 Chrono，一种新颖的操作系统级分层系统，能够精确刻画不同层中的页访问频率，并实现冷热页的高效迁移。Chrono 利用定时器而非计数器，以低开销实现对热页访问频率的细致测量。该方法使 Chrono 能够自动调整其页分类参数，从而形成适应各类工作负载的灵活迁移策略。此外，Chrono 包含一个动态冷页识别子系统，用于平衡分层内存的利用率与可用性。我们在现有的分层内存平台上实现并评估了 Chrono，实验结果表明 Chrono 大幅优于最先进的分层系统。

**英文关键词：** Memory management, Heterogeneous memory, NUMA, Linux kernel

**中文关键词：** 内存管理、异构内存、NUMA、Linux 内核

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
