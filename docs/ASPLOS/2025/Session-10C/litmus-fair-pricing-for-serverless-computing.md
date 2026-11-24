---
title: "Litmus: Fair Pricing for Serverless Computing"
description: "ASPLOS 2025 · Session 10C · Litmus：面向 Serverless 计算的公平定价"
tags:
  - "ASPLOS2025"
  - "Session 10C"
  - "Serverless Computing"
---

# Litmus: Fair Pricing for Serverless Computing

**中文标题：** Litmus：面向 Serverless 计算的公平定价

**所属 Session：** [Session 10C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Qi Pei (Computer Science / Watson School, The State University of New York at Binghamton), Yipeng Wang (Intel Lab., Intel), Seunghee Shin (Computer Science / Watson School, The State University of New York at Binghamton)

**单位：** Computer Science / Watson School, The State University of New York at Binghamton；Intel Lab., Intel

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674181) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Serverless computing has emerged as a market-dominant paradigm in modern cloud computing, benefiting both cloud providers and tenants. While service providers can optimize their machine utilization, tenants only need to pay for the resources they use. To maximize resource utilization, these serverless systems co-run numerous short-lived functions, bearing frequent system condition shifts. When the system gets overcrowded, a tenant's function may suffer from disturbing slowdowns. Ironically, tenants also incur higher costs during these slowdowns, as commercial serverless platforms determine costs proportional to their execution times. This paper argues that cloud providers should compensate tenants for losses incurred when the server is overprovisioned. However, estimating tenants' losses is challenging without pre-profiled information about their functions. Prior studies have indicated that assessing tenant losses leads to heavy overheads. As a solution, this paper introduces a new pricing model that offers discounts based on the machine's state while presuming the tenant's loss under that state. To monitor the machine state accurately, Litmus pricing frequently conducts Litmus tests, an effective and lightweight solution for measuring system congestion. Our experiments show that Litmus pricing can accurately gauge the impact of system congestion and offer nearly ideal prices, with only a 0.2% price difference on average, in a heavily congested system.

## 中文摘要

Serverless 计算已成为现代云计算中占据市场主导地位的范式，使云提供商与租户双方受益。服务提供商可以优化其机器利用率，而租户只需为其使用的资源付费。为最大化资源利用率，这些 Serverless 系统共同运行大量短生命周期函数，因而承受频繁的系统状态变化。当系统过度拥挤时，租户的函数可能遭受令人困扰的减速。讽刺的是，由于商业 Serverless 平台按执行时间成比例地确定费用，租户在这些减速期间反而承担更高的成本。本文主张，云提供商应就服务器超额配置时租户所遭受的损失给予补偿。然而，若没有对其函数进行预先剖析的信息，估计租户的损失颇具挑战。先前的研究表明，评估租户损失会带来沉重开销。作为解决方案，本文提出一种新的定价模型：它基于机器状态提供折扣，同时推定该状态下租户的损失。为准确监测机器状态，Litmus 定价频繁执行 Litmus 测试，这是一种用于度量系统拥塞的有效且轻量的方案。我们的实验表明，在高度拥塞的系统中，Litmus 定价能够准确衡量系统拥塞的影响并提供近乎理想的价格，平均价格差异仅为 0.2%。

## 英文关键词

Serverless Computing, Congestion Estimation, Resource Sharing, Online Pricing

## 中文关键词

Serverless 计算；拥塞估计；资源共享；在线定价

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674181)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10C](index.md) · [返回 ASPLOS 2025](../index.md)
