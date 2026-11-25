---
title: "ECOTE: Priority-Aware Optical Restoration for WAN Traffic Engineering"
description: "EuroSys 2026 · Traffic Engineering, CDNs & Congestion Control · Yiren Zhao (University of Toronto), Kunling He (Tsinghua University), Zhiquan Wa"
tags:
  - "EuroSys2026"
  - "Traffic Engineering, CDNs & Congestion Control"
---

# ECOTE: Priority-Aware Optical Restoration for WAN Traffic Engineering

**中文标题：** ECOTE：面向广域网流量工程的优先级感知光层恢复

**所属 Session：** [Session 7.2: Traffic Engineering, CDNs & Congestion Control](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Traffic Engineering, CDNs & Congestion Control。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Traffic Engineering, CDNs & Congestion Control</p>
</div>

**作者**：Yiren Zhao (University of Toronto), Kunling He (Tsinghua University), Zhiquan Wang (Tsinghua University), Ran Shu (Microsoft Research Asia), Jilong Wang (Tsinghua University), Congcong Miao (Tencent)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803592)

## 英文摘要

Fiber cuts are among the most common and disruptive failures in cloud networks. They can prevent cloud providers from maintaining committed service availability, causing Service Level Agreement (SLA) violations that directly translate into monetary penalties. Existing traffic engineering (TE) approaches enhance failure resilience, and recent systems further incorporate optical restoration to recover lost bandwidth after failures. However, they still treat services largely uniformly and optimize primarily for network throughput rather than the economic impact of heterogeneous SLA penalties. In this paper, we present ECOTE, the first priority-aware TE system with optical restoration that explicitly minimizes revenue loss. Specifically, ECOTE introduces a new optical restoration formulation with a dedicated capacity restoration solver to compute an optimal restoration plan that maximizes restorable capacity under physical constraints. ECOTE also designs a priority-aware TE algorithm that allocates the restored bandwidth capacity according to SLA penalties, thereby reducing monetary cost. We evaluate ECOTE using a production-level WAN testbed and through large-scale simulations. The testbed evaluation demonstrates ECOTE achieves zero loss for high-priority services and more than 10× revenue loss reduction compared to state-of-the-art. Our large-scale simulation results show that ECOTE can support at least 2.5× and 2.0× more demand for different high priority services compared to the state-of-the-art solutions. Meanwhile, ECOTE reduces the revenue loss by at least an order of magnitude less than existing solutions.

## 中文摘要

光纤中断是云网络中最常见且最具破坏性的故障之一。它们可能使云服务商无法维持承诺的服务可用性，导致服务等级协议（SLA）违约，并直接转化为经济处罚。现有的流量工程（TE）方法增强了故障韧性，近期系统进一步引入光层恢复，以在故障后恢复丢失的带宽。然而，这些系统仍基本以统一方式对待各类服务，且主要优化网络吞吐量，而非异构SLA处罚带来的经济影响。本文提出ECOTE，首个显式最小化收入损失的优先级感知光层恢复TE系统。具体而言，ECOTE引入了一种新的光层恢复形式化模型，并配有专用的容量恢复求解器，以在物理约束下计算最大化可恢复容量的最优恢复方案。ECOTE还设计了一种优先级感知的TE算法，根据SLA处罚分配恢复的带宽容量，从而降低经济损失。我们使用生产级广域网测试床并通过大规模仿真评估ECOTE。测试床评估表明，与最先进方案相比，ECOTE对高优先级服务实现零损失，并将收入损失降低10倍以上。大规模仿真结果表明，与最先进方案相比，ECOTE能够为不同的高优先级服务支持至少2.5倍和2.0倍的需求。同时，ECOTE的收入损失至少比现有方案低一个数量级。

**英文关键词：** Wide-area networks, Traffic engineering, Optical restoration, Network optimization

**中文关键词：** 广域网、流量工程、光层恢复、网络优化

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
