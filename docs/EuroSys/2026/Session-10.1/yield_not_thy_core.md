---
title: "Yield Not Thy Core"
description: "EuroSys 2026 · Distributed Systems and Multicore · Achilles Benetopoulos (University of California, Santa Cruz), Peter Alvaro (U. C"
tags:
  - "EuroSys2026"
  - "Distributed Systems and Multicore"
---

# Yield Not Thy Core

**中文标题：** 勿使核心空转

**所属 Session：** [Session 10.1: Distributed Systems and Multicore](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Systems and Multicore。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Systems and Multicore</p>
</div>

**作者**：Achilles Benetopoulos (University of California, Santa Cruz), Peter Alvaro (U. C. Santa Cruz), Andi Quinn (UC Santa Cruz), Robert Soule (Yale University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803616)

## 英文摘要

Programming distributed systems has never been easier, but making them perform well and efficiently exploit available resources remains difficult. Fast programs on a single host slow to a crawl when given more resources, while systems designed for scale squander resources on modest problems.

We present Magpie, a programming model and framework for building high-performance, data-intensive applications. Magpie provides the straightforward guarantee that fast code remains fast when distributed. Because application code performs best when executed without interruptions, Magpie takes protocol off the critical path, automatically orchestrating the placement of data and computation to ensure uninterrupted local compute whenever possible. This flexibility requires extreme adaptivity, postponing all decisions about movement and placement until runtime. To support this fine-grained adaptivity, distributed computations in Magpie are structured as compositions of lightweight transactions over distributed objects, both of which may move freely through the system.

To showcase Magpie’s performance and generality, we develop two very different libraries: a high-performance key-value store and a graph processing system. We show that Magpie achieves parity with or outperforms state of the art systems in both areas while providing richer guarantees.

## 中文摘要

编写分布式系统从未如此容易，但让它们性能良好并高效利用可用资源仍然困难。在单机上运行很快的程序，在获得更多资源后反而变得极其缓慢；而为大规模场景设计的系统在处理中等规模问题时又会浪费资源。

我们提出 Magpie，一个用于构建高性能数据密集型应用的编程模型与框架。Magpie 提供一项直观的保证：快速的代码在分布式环境下依然快速。由于应用代码在不被打断地执行时性能最佳，Magpie 将协议移出关键路径，自动编排数据与计算的位置，尽可能保证本地计算不被打断。这种灵活性要求极强的自适应性，将所有关于移动与放置的决策推迟到运行时。为支持这种细粒度自适应性，Magpie 中的分布式计算被构造为对分布式对象的轻量级事务的组合，而对象与事务都可以在系统中自由移动。

为展示 Magpie 的性能与通用性，我们开发了两个差异很大的库：一个高性能键值存储和一个图处理系统。我们表明 Magpie 在这两个领域都达到或超过了最先进系统的水平，同时提供了更丰富的保证。

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
