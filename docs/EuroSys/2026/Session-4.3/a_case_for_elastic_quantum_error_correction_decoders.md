---
title: "A Case for Elastic Quantum Error Correction Decoders"
description: "EuroSys 2026 · Fault Tolerance, Reliability & Debugging · Satvik Maurya (University of Wisconsin-Madison), Abtin Molavi (University of Wis"
tags:
  - "EuroSys2026"
  - "Fault Tolerance, Reliability & Debugging"
---

# A Case for Elastic Quantum Error Correction Decoders

**中文标题：** 论弹性量子纠错解码器

**所属 Session：** [Session 4.3: Fault Tolerance, Reliability & Debugging](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Fault Tolerance, Reliability & Debugging。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Fault Tolerance, Reliability & Debugging</p>
</div>

**作者**：Satvik Maurya (University of Wisconsin-Madison), Abtin Molavi (University of Wisconsin-Madison), Aws Albarghouthi (University of Wisconsin-Madison), Swamit Tannu (University of Wisconsin-Madison)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803584)

## 英文摘要

Large-scale quantum computers promise transformative speedups, but their viability hinges on fast and reliable quantum error correction (QEC). At the center of QEC are decoders—classical algorithms running on hardware such as FPGAs, GPUs, or CPUs that process error syndromes to detect errors every microsecond to preserve fault-tolerance. Quantum processors, therefore, operate not in isolation, but as accelerators tightly coupled with powerful classical digital hardware. A key challenge is that decoder demand fluctuates unpredictably: bursts of activity can require orders of magnitude more decodes than idle periods. Provisioning hardware for the worst case wastes resources, while provisioning for the average case risks catastrophic slowdowns. We show that this mismatch is a systems problem of capacity planning and scheduling, and propose a two-level framework that treats decoders as shared accelerators managed by the quantum operating system. Our approach reduces decoder requirements by 10–40% across fault-tolerant benchmarks, demonstrating that efficient decoder scheduling is essential to making FTQC practical.

## 中文摘要

大规模量子计算机有望带来变革性的加速，但其可行性取决于快速可靠的量子纠错（QEC）。QEC 的核心是解码器——运行在 FPGA、GPU 或 CPU 等硬件上的经典算法，它们每微秒处理一次错误综合症以检测错误，从而维持容错能力。因此，量子处理器并非孤立运行，而是作为与强大的经典数字硬件紧密耦合的加速器。一个关键挑战在于解码器需求会不可预测地波动：突发活动所需的解码次数可能比空闲期高出数个数量级。按最坏情况配置硬件会浪费资源，而按平均情况配置则可能带来灾难性的性能下降。我们证明这种不匹配是一个关于容量规划与调度的系统问题，并提出一个两级框架，将解码器视为由量子操作系统管理的共享加速器。我们的方法在各类容错基准测试中将解码器需求降低了 10%–40%，表明高效的解码器调度对于使容错量子计算（FTQC）走向实用至关重要。

**英文关键词：** Decoders, Quantum Error Correction, Decoding Systems

**中文关键词：** 解码器、量子纠错、解码系统

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
