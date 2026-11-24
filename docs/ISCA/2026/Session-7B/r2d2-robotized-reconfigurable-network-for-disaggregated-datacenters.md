---
title: "R2D2: Robotized Reconfigurable Network for Disaggregated Datacenters"
description: "ISCA 2026 · Session 7B · R2D2: Robotized Reconfigurable Network for Disaggregated Datacenters"
tags:
  - "ISCA2026"
  - "Session 7B"
  - "Performance Modeling / Datacenter"
---

# R2D2: Robotized Reconfigurable Network for Disaggregated Datacenters

**中文标题：** R2D2: 面向分解式数据中心的机器人化可重构网络

**所属 Session：** [Session 7B](index.md) · [ISCA 2026](../index.md)

**作者：** Linus Y. Wong, Zhiyao Tang, Justin R. Yu, Zhilei Zheng, Jonathan M. Smith, André DeHon, Jing Li

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Disaggregated datacenters present unique network challenges. Current network hardware serving disaggregation traffic is spatially overprovisioned with statically configured all-to-all connectivity and temporally overprovisioned with static, per-packet switching costs, regardless of actual network traffic patterns. This leads to significant underutilization and reduces the cost benefits of resource disaggregation. To address this, we propose R2D2, a robot-enabled reconfigurable datacenter network architecture. Through software-hardware co-design, R2D2 exploits the spatial and temporal locality of network traffic to achieve efficient network specialization. In particular, for the first time, R2D2 leverages mature commodity robotics to reconfigure the network and establish direct, single-hop physical connections between disaggregated resources on demand, eliminating the spatial overprovisioning of all-to-all connections. Furthermore, R2D2 dynamically reconfigures the network on demand to adapt to changing traffic patterns, thereby removing the need for continuous per-packet switching; hence, avoiding temporal overprovisioning. Lastly, we introduce a co-optimized runtime system, co-designed with the robotized network architecture, to improve performance, resource-efficiency, and availability. We demonstrated the feasibility of R2D2 with comprehensive experimental evaluations and a robot prototype, using real-world applications and datacenter allocation traces. Our results show that R2D2 achieves up to 38% reduction in network costs and up to 84% savings in network energy consumption, while delivering comparable end-to-end application performance compared to state-of-the-art fat-tree and OCS networks.

## 中文摘要

分解式数据中心带来了独特的网络挑战。当前服务于分解流量的网络硬件在空间上以静态配置的全互联连接过度配置，在时间上又以静态的逐包交换开销过度配置，而不管实际的网络流量模式如何。这导致显著的利用率不足，削弱了资源分解的成本优势。为此，我们提出 R2D2，一种由机器人驱动的可重构数据中心网络架构。通过软硬件协同设计，R2D2 利用网络流量的空间与时间局部性，实现高效的网络专门化。特别是，R2D2 首次利用成熟的商用机器人技术来重构网络，按需在分解资源之间建立直接的单跳物理连接，从而消除全互联连接的空间过度配置。此外，R2D2 按需动态重构网络以适应变化的流量模式，从而无需持续的逐包交换，避免了时间上的过度配置。最后，我们引入与机器人化网络架构协同设计的、共同优化的运行时系统，以提升性能、资源效率和可用性。我们通过全面的实验评估和机器人原型，使用真实应用与数据中心分配轨迹，验证了 R2D2 的可行性。结果表明，与最先进的 fat-tree 和 OCS 网络相比，R2D2 在提供相当的端到端应用性能的同时，网络成本降低最多 38%，网络能耗节省最多 84%。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7B](index.md) · [返回 ISCA 2026](../index.md)
