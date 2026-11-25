---
title: "TierScape: Harnessing Multiple Compressed Tiers to Tame Server Memory TCO"
description: "EuroSys 2026 · OS & Virtualization · Sandeep Kumar (Intel Labs), Aravinda Prasad (Intel Labs), Sreenivas Subramoney ("
tags:
  - "EuroSys2026"
  - "OS & Virtualization"
---

# TierScape: Harnessing Multiple Compressed Tiers to Tame Server Memory TCO

**中文标题：** TierScape：利用多个压缩层级掌控服务器内存 TCO

**所属 Session：** [Session 1.1: OS & Virtualization](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：OS & Virtualization。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · OS & Virtualization</p>
</div>

**作者**：Sandeep Kumar (Intel Labs), Aravinda Prasad (Intel Labs), Sreenivas Subramoney (Intel Labs)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769321)

## 英文摘要

Tiered memory systems are the norm to effectively tackle the increasing memory total cost of ownership (TCO) in modern data centers. We propose TierScape to tame memory TCO through the novel creation and judicious management of multiple compressed memory tiers along with multiple byte-addressable tiers.

As opposed to conventional tiering solutions that employ a single compressed memory tier, we harness multiple compressed tiers implemented through a combination of different compression algorithms, memory allocators for compressed objects, and backing media to store compressed objects. These compressed tiers represent distinct points in the access latency, data compressibility, and unit memory usage cost spectrum, allowing rich and flexible trade-offs between memory TCO savings and application performance impact. A key advantage with TierScape is that it enables aggressive memory TCO saving opportunities by placing warm data in low latency compressed tiers with a reasonable performance impact while simultaneously placing cold data in the best memory TCO saving tiers.

TierScape presents a comprehensive, rigorous, and tunable analytical cost model for performance and TCO trade-off based on continuous monitoring of the application’s data access profile. Guided by this model, TierScape takes informed actions to dynamically manage the placement and migration of application data across multiple compressed and byte-addressable tiers. We believe TierScape represents an important server system configuration and optimization capability to achieve the best SLA-aware performance per dollar for applications hosted in production data center environments. For a set of real-world benchmarks, TierScape reduces memory TCO by 15.1–23.6% percentage points while maintaining performance parity or improves performance by 2.61–10.0% percentage points while maintaining memory TCO parity compared to state-of-the-art tiering solutions.

## 中文摘要

分层内存系统已成为有效应对现代数据中心不断攀升的内存总拥有成本（TCO）的常规做法。我们提出 TierScape，通过新颖地创建并审慎管理多个压缩内存层级以及多个字节可寻址层级，来掌控内存 TCO。

与采用单一压缩内存层的传统分层方案不同，我们利用由不同压缩算法、面向压缩对象的内存分配器以及用于存放压缩对象的后备介质组合而成的多个压缩层级。这些压缩层级分别代表访问延迟、数据可压缩性与单位内存使用成本谱系上的不同位置，从而在节省内存 TCO 与对应用性能的影响之间实现丰富而灵活的权衡。TierScape 的一个关键优势在于，它能够将温数据放置在低延迟压缩层中并仅带来合理的性能影响，同时将冷数据放置在 TCO 节省效果最佳的内存层中，从而实现激进的内存 TCO 节省空间。

TierScape 在持续监控应用数据访问特征的基础上，提出了一个全面、严谨且可调的性能与 TCO 权衡分析成本模型。在该模型指导下，TierScape 采取有依据的行动，动态管理应用数据在多个压缩层与字节可寻址层之间的放置与迁移。我们相信，TierScape 代表了一种重要的服务器系统配置与优化能力，可为生产数据中心环境中托管的应用实现最佳的、SLA 感知的每美元性能。在一组真实基准测试上，与最先进的分层方案相比，TierScape 在保持性能相当的同时将内存 TCO 降低 15.1–23.6 个百分点，或在保持内存 TCO 相当的同时将性能提升 2.61–10.0 个百分点。

**英文关键词：** Memory Tiering, Compressed memory, Memory TCO

**中文关键词：** 内存分层、压缩内存、内存 TCO

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
