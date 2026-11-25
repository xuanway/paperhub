---
title: "OptiLog: Assigning Roles in Byzantine Consensus"
description: "EuroSys 2026 · Distributed Consensus, Blockchain & Storage · Hanish Gogada (University of Stavanger), Christian Berger (Friedrich-Alexander-U"
tags:
  - "EuroSys2026"
  - "Distributed Consensus, Blockchain & Storage"
---

# OptiLog: Assigning Roles in Byzantine Consensus

**中文标题：** OptiLog：在拜占庭共识中分配角色

**所属 Session：** [Session 4.2: Distributed Consensus, Blockchain & Storage](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Consensus, Blockchain & Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Consensus, Blockchain & Storage</p>
</div>

**作者**：Hanish Gogada (University of Stavanger), Christian Berger (Friedrich-Alexander-Universität Erlangen-Nürnberg), Leander Jehl (University of Stavanger), Hans P. Reiser (Reykjavik University), Hein Meling (University of Stavanger)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769342)

## 英文摘要

Byzantine Fault-Tolerant (BFT) protocols play an important role in blockchains. As the deployment of such systems extends to wide-area networks, the scalability of BFT protocols becomes a critical concern. Optimizations that assign specific roles to individual replicas can significantly improve the performance of BFT systems. However, such role assignment is highly sensitive to faults, potentially undermining the optimizations’ effectiveness.

To address these challenges, we present OptiLog, a logging framework for collecting and analyzing measurements that help to assign roles in globally distributed systems, despite the presence of faults. OptiLog presents local measurements in global data structures, to enable consistent decisions and hold replicas accountable if they do not perform according to their reported measurements.

We demonstrate OptiLog’s flexibility by applying it to two BFT protocols: (1) Aware, a highly optimized PBFT-like protocol, and (2) Kauri, a tree-based protocol designed for large-scale deployments. OptiLog detects and excludes replicas that misbehave during consensus and thus enables the system to operate in an optimized, low-latency configuration, even under adverse conditions. Experiments show that for tree overlays deployed across 73 worldwide cities, trees found by OptiLog display 39% lower latency than Kauri.

## 中文摘要

拜占庭容错（BFT）协议在区块链中发挥着重要作用。随着此类系统的部署扩展到广域网，BFT协议的可扩展性成为关键问题。为单个副本分配特定角色的优化可以显著提升BFT系统的性能。然而，这种角色分配对故障高度敏感，可能削弱优化的效果。

为应对这些挑战，我们提出OptiLog，一个日志框架，用于收集和分析测量数据，从而在存在故障的情况下帮助在全局分布式系统中分配角色。OptiLog将本地测量呈现于全局数据结构中，以实现一致的决策，并在副本未按其上报的测量数据执行时追究其责任。

我们通过将OptiLog应用于两种BFT协议来展示其灵活性：（1）Aware，一种高度优化的类PBFT协议；（2）Kauri，一种为大规模部署设计的基于树的协议。OptiLog检测并排除在共识过程中行为异常的副本，从而使系统即使在不利条件下也能以优化的低延迟配置运行。实验表明，对于部署于73个全球城市的树形覆盖网络，OptiLog找到的树比Kauri延迟低39%。

**英文关键词：** Byzantine Fault Tolerance, Consensus, Reliability, Performance Optimization, Adaptive Systems, Reconfiguration Framework, Low Latency, Fault Detection

**中文关键词：** 拜占庭容错、共识、可靠性、性能优化、自适应系统、重配置框架、低延迟、故障检测

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
