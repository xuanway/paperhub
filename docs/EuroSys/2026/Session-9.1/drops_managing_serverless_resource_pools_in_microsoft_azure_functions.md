---
title: "DROPS: Managing Serverless Resource Pools in Microsoft Azure Functions"
description: "EuroSys 2026 · Cloud · Ahmed Alquraan (University of Waterloo), Abdelrahman Baba (University of Waterlo"
tags:
  - "EuroSys2026"
  - "Cloud"
---

# DROPS: Managing Serverless Resource Pools in Microsoft Azure Functions

**中文标题：** DROPS：在 Microsoft Azure Functions 中管理无服务器资源池

**所属 Session：** [Session 9.1: Cloud](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Cloud。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Cloud</p>
</div>

**作者**：Ahmed Alquraan (University of Waterloo), Abdelrahman Baba (University of Waterloo), Rafael Mendes (Microsoft Research), Sameh Elnikety (Microsoft Research), Paul Batum (Microsoft), Yan Chen (Microsoft), Hamid Henry Safi (Microsoft), Seth Fine (Microsoft), Samer Al-Kiswany (University of Waterloo)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769350)

## 英文摘要

Azure Functions maintains pools of pre-warmed containers to avoid the high container-allocation latency. The size of a pool is important: a pool that is too small leads to high allocation latency, whereas a pool that is too large wastes resources and increases cost. Service providers typically oversize pools to meet service-level objectives (SLOs). Our findings indicate that the cost of maintaining pre-warmed container pools dominates the overall platform cost, motivating the need for effective pool management strategies.

We characterize container-allocation traces from Azure Functions, revealing key findings: the demand for container allocation is highly bursty, while the supply of new containers is virtually unlimited but may have long delays. Traditional resource management approaches, which rely on prediction or reactive techniques, fail to reduce costs while meeting the target SLO due to the bursty nature of the workload. These insights lead us to develop a new statistical, data-driven pool optimization method that uses historical traces to compute the size of each pool. Our evaluation shows that the proposed method meets the target SLO while reducing the operational cost by 41% compared to the static approach employed earlier in the production platform.

## 中文摘要

Azure Functions 维护预热容器池以避免高昂的容器分配延迟。池的规模十分重要：池过小会导致分配延迟高，而池过大则会浪费资源并增加成本。服务提供商通常会超额配置池以满足服务等级目标（SLO）。我们的发现表明，维护预热容器池的成本在平台总成本中占主导地位，这促使我们需要有效的池管理策略。

我们刻画了来自 Azure Functions 的容器分配轨迹，揭示了若干关键发现：容器分配需求具有高度突发性，而新容器的供给几乎是无限的，但可能存在较长延迟。传统资源管理方法依赖预测或反应式技术，由于工作负载的突发性，无法在满足目标 SLO 的同时降低成本。这些洞见促使我们开发了一种新的统计式、数据驱动的池优化方法，该方法利用历史轨迹计算每个池的规模。我们的评测表明，与生产平台早期采用的静态方法相比，所提方法在满足目标 SLO 的同时将运营成本降低了 41%。

**英文关键词：** serverless computing, cloud platforms, resource management, performance optimization

**中文关键词：** 无服务器计算、云平台、资源管理、性能优化

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
