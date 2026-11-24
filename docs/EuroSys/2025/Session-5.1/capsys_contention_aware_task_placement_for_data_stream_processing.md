---
title: "CAPSys: Contention-aware task placement for data stream processing"
description: "EuroSys 2025 · Graph and Stream processing · Yuanli Wang (Boston University), Lei Huang (Boston University), Zikun Wang (Bost"
tags:
  - "EuroSys2025"
  - "Graph and Stream processing"
---

# CAPSys: Contention-aware task placement for data stream processing

**中文标题：** 面向数据流处理的争用感知任务放置

**所属 Session：** [Session 5.1: Graph and Stream processing](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Graph and Stream processing。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Graph and Stream processing</p>
</div>

**作者**：Yuanli Wang (Boston University), Lei Huang (Boston University), Zikun Wang (Boston University), Vasiliki Kalavri (Boston University), Ibrahim Matta (Boston University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696085)

## 英文摘要

In the context of streaming dataflow queries, the task placement problem aims to identify a mapping of operator tasks to physical resources in a distributed cluster. We show that task placement not only significantly affects query performance but also the convergence and accuracy of auto-scaling controllers. We propose CAPSys, an adaptive resource controller for dataflow stream processors, that considers auto-scaling and task placement in concert. CAPSys relies on Contention-Aware Placement Search (CAPS), a new placement strategy that ensures compute-intensive, I/O-intensive, and network-intensive tasks are balanced across available resources.

We integrate CAPSys with Apache Flink and show that it consistently achieves higher throughput and lower backpressure than Flink’s strategies, while it also improves the convergence of the DS2 auto-scaling controller under variable workloads. When compared with the state-of-the-art ODRP placement strategy, CAPSys computes the task placement in orders of magnitude lower time and achieves up to 6× higher throughput.

## 中文摘要

在流式数据流查询场景中，任务放置问题旨在确定算子任务到分布式集群中物理资源的映射。我们表明，任务放置不仅显著影响查询性能，还影响自动伸缩控制器的收敛性与准确性。我们提出 CAPSys，一个面向数据流流处理器的自适应资源控制器，它协同考虑自动伸缩与任务放置。CAPSys 依赖于竞争感知放置搜索（CAPS），这是一种新的放置策略，可确保计算密集型、I/O 密集型和网络密集型任务在可用资源之间保持均衡。

我们将 CAPSys 与 Apache Flink 集成，结果表明，与 Flink 的策略相比，它始终能获得更高的吞吐量和更低的反压，同时在负载变化的情况下改善了 DS2 自动伸缩控制器的收敛性。与当前最先进的 ODRP 放置策略相比，CAPSys 计算任务放置的时间低几个数量级，吞吐量最高提升 6 倍。

**英文关键词：** Stream Processing, Distributed systems, Resource management, Scheduling

**中文关键词：** 流处理、分布式系统、资源管理、调度

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
