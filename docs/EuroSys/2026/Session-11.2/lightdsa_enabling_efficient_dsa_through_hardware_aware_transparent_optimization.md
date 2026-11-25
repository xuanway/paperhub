---
title: "LightDSA: Enabling Efficient DSA Through Hardware-Aware Transparent Optimization"
description: "EuroSys 2026 · Programmable Networks, SmartNICs & Accelerators · Yuansen Wang (Renmin University of China), Teng Ma (Alibaba Group), Yuanhui Luo "
tags:
  - "EuroSys2026"
  - "Programmable Networks, SmartNICs & Accelerators"
---

# LightDSA: Enabling Efficient DSA Through Hardware-Aware Transparent Optimization

**中文标题：** LightDSA：通过硬件感知的透明优化实现高效 DSA

**所属 Session：** [Session 11.2: Programmable Networks, SmartNICs & Accelerators](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Programmable Networks, SmartNICs & Accelerators。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Programmable Networks, SmartNICs & Accelerators</p>
</div>

**作者**：Yuansen Wang (Renmin University of China), Teng Ma (Alibaba Group), Yuanhui Luo (Renmin University of China), Dongbiao He (CNIC, CAS), Zheng Liu (Alibaba Group), Yunpeng Chai (Renmin University of China)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769356)

## 英文摘要

Data streaming operations consume a significant portion of CPU resources in data centers. The Data Streaming Accelerator (DSA), integrated into modern Intel CPUs in datacenter, offers promising acceleration for these operations with user-friendly features. However, previous studies have overlooked DSA’s internal mechanisms and the performance implications of these features, leaving key performance issues unresolved in real-world usage.

In this paper, we conduct an in-depth analysis of DSA, focusing on five previously overlooked internal mechanisms that significantly impact performance, and summarize seven design principle insights for efficient DSA utilization. Based on these insights, we introduce LightDSA, a user-friendly, asynchronous DSA library featuring low-overhead, run-to-completion optimizations. Evaluations demonstrate that our LightDSA achieves up to 3× improvement in microbenchmarks and achieves 23.6% speedup in an end-to-end Redis case study compared to direct DSA usage, highlighting the power of hardware-aware, transparent optimization in enabling efficient DSA for practical use.

## 中文摘要

数据流操作消耗了数据中心中相当一部分 CPU 资源。集成在现代数据中心 Intel CPU 中的数据流加速器（DSA）以其易用的特性为这些操作提供了颇具前景的加速。然而，先前的研究忽视了 DSA 的内部机制以及这些特性的性能影响，导致实际使用中的关键性能问题仍未得到解决。

本文对 DSA 进行深入分析，聚焦于五个此前被忽视且显著影响性能的内部机制，并总结了七条高效利用 DSA 的设计原则洞见。基于这些洞见，我们提出 LightDSA，一个易用的异步 DSA 库，具备低开销、运行至完成的优化。评估表明，与直接使用 DSA 相比，我们的 LightDSA 在微基准中最高取得 3 倍提升，在端到端 Redis 案例研究中取得 23.6% 的加速，凸显了硬件感知的透明优化在使 DSA 高效实用方面的力量。

**英文关键词：** Data streaming accelerator (DSA), measurement, accelerator, performance characterization

**中文关键词：** 数据流加速器（DSA）、测量、加速器、性能刻画

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
