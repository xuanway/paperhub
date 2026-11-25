---
title: "PASS: A Power Adaptive Storage Server"
description: "EuroSys 2026 · Storage Systems · Dedong Xie (University of Washington), Theano Stavrinos (Databricks), Jonggyu Pa"
tags:
  - "EuroSys2026"
  - "Storage Systems"
---

# PASS: A Power Adaptive Storage Server

**中文标题：** PASS：一种功耗自适应存储服务器

**所属 Session：** [Session 7.3: Storage Systems](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Storage Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Storage Systems</p>
</div>

**作者**：Dedong Xie (University of Washington), Theano Stavrinos (Databricks), Jonggyu Park (University of Washington), Simon Peter (University of Washington), Baris Kasikci (University of Washington), Thomas E. Anderson (University of Washington)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769354)

## 英文摘要

Power management has become important in data centers. Since data center workloads are often dynamic, it is common practice to conserve energy by scaling resources up or down to match the workload. And since data centers often oversubscribe the power delivery infrastructure, operators can add power capping on top of these workload-proportional systems to adjust to available power. We find that this combination leaves performance on the table and provides only a limited power control range. Instead, we argue for power-adaptive systems that attempt to make the best use of the available power budget. To illustrate this approach, we built PASS, a power-adaptive storage system. PASS considers the interactions between different system components, including software and hardware, when making its power management decisions. For example, when under the same power constraint, PASS achieves 3–25× better throughput on filebench workloads than Intel’s SPDK storage stack with Google Thunderbolt, a state of the art power capping system.

## 中文摘要

功耗管理在数据中心中已变得十分重要。由于数据中心的工作负载通常是动态变化的，常见做法是通过扩缩资源来匹配负载以节省能耗。而数据中心往往会超额订购供电基础设施，因此运维人员可以在这些与负载成比例的系统之上再加功耗封顶，以适配可用功率。我们发现，这种组合会使性能潜力未被充分利用，并且只提供有限的功耗控制范围。因此，我们主张采用功耗自适应系统，力求最大限度地利用可用功率预算。为说明这一方法，我们构建了 PASS，一个功耗自适应存储系统。PASS 在做出功耗管理决策时会考虑不同系统组件（包括软件与硬件）之间的相互作用。例如，在相同功耗约束下，PASS 在 filebench 负载上相比搭载 Google Thunderbolt（一种最先进的功耗封顶系统）的 Intel SPDK 存储栈实现了 3–25 倍的吞吐量提升。

**英文关键词：** Data center, storage system, power management

**中文关键词：** 数据中心、存储系统、功耗管理

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
