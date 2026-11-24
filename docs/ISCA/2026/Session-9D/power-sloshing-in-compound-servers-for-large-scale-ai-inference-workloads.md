---
title: "Power Sloshing in Compound Servers for Large-Scale AI Inference Workloads"
description: "ISCA 2026 · Session 9D · Power Sloshing in Compound Servers for Large-Scale AI Inference Workloads"
tags:
  - "ISCA2026"
  - "Session 9D"
  - "Sustainability and Energy Efficiency"
---

# Power Sloshing in Compound Servers for Large-Scale AI Inference Workloads

**中文标题：** 面向大规模 AI 推理工作负载的复合服务器功耗振荡

**所属 Session：** [Session 9D](index.md) · [ISCA 2026](../index.md)

**作者：** Albert Cho, Jovan Stojkovic, Leonardo Piga, Abhishek Dhanotia, Sultan Mahmud Sajal, Gefei Zuo, Krishna Malladi, Devon Akers, Kalyan Subramanian, Shobhit Kanaujia, Alexandros Daglis

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

AI workloads are rapidly emerging as an important component of datacenter operations, with inference services in particular consuming an ever-increasing share of computational cycles. To keep pace with the growing demand for AI-driven applications, datacenters have begun deploying advanced compound servers that tightly integrate accelerators such as GPUs with traditional CPUs. While these platforms enable high performance, they also drive up the power requirements of datacenters, creating new challenges for scaling the infrastructure. To address these challenges, we conduct a comprehensive characterization of power usage patterns in datacenters hosting AI services. We find that power consumption fluctuates widely across time, models, services, and server components. These observations reveal the inefficiency of applying fixed, uniform power limits across servers, which can result in either under-provisioning and degraded performance, or overprovisioning and wasted planned power. Motivated by these insights, we investigate dynamic power control to optimize both power consumption and performance. Through experiments on production workloads, we demonstrate that controlled power sloshing can deliver benefits, yielding up to 30% power savings. We further develop a scalable, automated algorithm for server-level power management, which could be deployed in datacenters and reduce power by up to 11% without degrading the quality of service. Finally, based on our production experience, we offer practical guidelines for hardware and software co-design in next-generation AI platforms.

## 中文摘要

AI 工作负载正迅速成为数据中心运营的重要组成部分，其中推理服务尤其消耗着越来越多的计算周期。为跟上对 AI 驱动应用日益增长的需求，数据中心已开始部署先进的复合服务器，将 GPU 等加速器与传统 CPU 紧密集成。这些平台虽然实现了高性能，但也推高了数据中心的功耗需求，为基础设施的扩展带来了新的挑战。为应对这些挑战，我们对承载 AI 服务的数据中心的功耗使用模式进行了全面表征。我们发现，功耗在不同时间、模型、服务和服务器组件之间大幅波动。这些观察揭示了在服务器之间应用固定、统一功耗限制的低效性，这可能导致供给不足和性能下降，或者供给过度和计划功耗浪费。受这些见解启发，我们研究了动态功耗控制以同时优化功耗和性能。通过在生产工作负载上的实验，我们证明受控的功耗振荡可以带来收益，实现高达 30% 的功耗节省。我们进一步开发了一种可扩展的自动化服务器级功耗管理算法，可部署在数据中心中，在不降低服务质量的情况下将功耗降低高达 11%。最后，基于我们的生产经验，我们为下一代 AI 平台的软硬件协同设计提供了实用指南。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9D](index.md) · [返回 ISCA 2026](../index.md)
