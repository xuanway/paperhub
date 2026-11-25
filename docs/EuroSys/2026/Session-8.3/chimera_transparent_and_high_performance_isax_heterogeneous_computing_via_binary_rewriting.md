---
title: "Chimera: Transparent and High-Performance ISAX Heterogeneous Computing via Binary Rewriting"
description: "EuroSys 2026 · Architecture, Accelerators & Heterogeneous Computing · Jiatai He (Institute of Software Chinese Academy of Sciences; University of Chin"
tags:
  - "EuroSys2026"
  - "Architecture, Accelerators & Heterogeneous Computing"
---

# Chimera: Transparent and High-Performance ISAX Heterogeneous Computing via Binary Rewriting

**中文标题：** Chimera：通过二进制重写实现透明且高性能的ISAX异构计算

**所属 Session：** [Session 8.3: Architecture, Accelerators & Heterogeneous Computing](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Architecture, Accelerators & Heterogeneous Computing。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Architecture, Accelerators & Heterogeneous Computing</p>
</div>

**作者**：Jiatai He (Institute of Software Chinese Academy of Sciences; University of Chinese Academy of Sciences), Qinglin Pan (Institute of Software Chinese Academy of Sciences; University of Chinese Academy of Sciences), Ruilin Zhao (Institute of Software Chinese Academy of Sciences; University of Chinese Academy of Sciences), Ji Qi (Institute of Software Chinese Academy of Sciences; Key Laboratory of System Software (Chinese Academy of Sciences)), Kaiwen Liang (Hohai University; Institute of Software Chinese Academy of Sciences; University of Chinese Academy of Sciences, Nanjing; Nanjing Institute of Software Technology), Jiahao Xu (Institute of Software Chinese Academy of Sciences; University of Chinese Academy of Sciences), Zhiyuan Li (University of Chinese Academy of Sciences; Institute of Software Chinese Academy of Sciences; University of Chinese Academy of Sciences, Nanjing; Nanjing Institute of Software Technology), Yuexiang Wang (Institute of Software Chinese Academy of Sciences), Jiageng Yu (Institute of Software Chinese Academy of Sciences), Yanjun Wu (Institute of Software Chinese Academy of Sciences)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769323)

## 英文摘要

ISAX heterogeneous processors integrate cores that share a common base ISA, with certain cores offering extension ISAs (e.g., vector extension) to accelerate computation. ISAX balances performance and energy efficiency while facilitating the reuse of existing software ecosystems. RISC-V, which adopts the ISAX architecture, has gained extensive attention in both industry and academia. Binary translation via binary rewriting enables transparent ISAX heterogeneous computing by translating extension instructions when migrating a program to cores without extension support. However, current binary rewriting methods still struggle to achieve both high performance and correctness.

We propose Chimera, an ISAX heterogeneous computing system via binary rewriting that achieves both correctness and high performance. Prior binary rewriting methods ensure correctness by proactive fault checking, incurring unnecessary runtime overhead in normal executions unlikely to encounter faults. Chimera introduces a new binary rewriting method that passively triggers fault-handling only when faults actually occur, minimizing runtime overhead. We evaluated Chimera and notable ISAX heterogeneous computing systems using real-world workloads. In mixed matrix computational workloads, Chimera achieved only 3.2% performance overhead compared to native compilation, and only 5.3% in real-world workloads like OpenBLAS. On SPEC CPU2017 benchmarks, our method achieved up to 42.5% performance improvement over existing binary rewriting methods on average. Chimera ’s code is released on https://github.com/Eurosys26p57/Chimera.

## 中文摘要

ISAX异构处理器集成了共享同一基础ISA的多个核心，其中某些核心提供扩展ISA（例如向量扩展）以加速计算。ISAX在性能与能效之间取得平衡，同时便于复用现有软件生态。采用ISAX架构的RISC-V在工业界和学术界都获得了广泛关注。通过二进制重写的二进制翻译在将程序迁移到不支持扩展的核心时翻译扩展指令，从而实现透明的ISAX异构计算。然而，当前的二进制重写方法仍难以同时实现高性能与正确性。

我们提出Chimera，一个通过二进制重写同时实现正确性与高性能的ISAX异构计算系统。此前的二进制重写方法通过主动故障检查来保证正确性，在不太可能遇到故障的正常执行中引入了不必要的运行时开销。Chimera引入一种新的二进制重写方法，仅在实际发生故障时才被动触发故障处理，从而将运行时开销降至最低。我们使用真实负载评估了Chimera和若干知名的ISAX异构计算系统。在混合矩阵计算负载中，与本地编译相比Chimera仅带来3.2%的性能开销，在OpenBLAS等真实负载中仅为5.3%。在SPEC CPU2017基准测试上，我们的方法平均比现有二进制重写方法最高提升42.5%的性能。Chimera的代码发布于https://github.com/Eurosys26p57/Chimera。

**英文关键词：** Heterogeneous computing, binary rewriting, operating system

**中文关键词：** 异构计算、二进制重写、操作系统

## 代码与研究制品

- [代码](https://github.com/Eurosys26p57/Chimera)（论文摘要提供）

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
