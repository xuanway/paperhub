---
title: "Evaluating Ruche Networks: Physically Scalable, Cost-Effective, Bandwidth-Flexible NoCs"
description: "ISCA 2025 · Session 6B · 评估 Ruche 网络：物理可扩展、经济高效且带宽灵活的片上网络"
tags:
  - "ISCA2025"
  - "Session 6B"
  - "Microarchitecture II"
---

# Evaluating Ruche Networks: Physically Scalable, Cost-Effective, Bandwidth-Flexible NoCs

**中文标题：** 评估 Ruche 网络：物理可扩展、经济高效且带宽灵活的片上网络

**所属 Session：** [Session 6B](index.md) · [ISCA 2025](../index.md)

**作者：** Dai Cheol Jung, Michael Taylor

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731010) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

2-D mesh has been widely used as an on-chip network topology, because of its low design complexity and physical scalability. How- ever, its poor latency and throughput scaling have been well-noted in the past. Previous solutions to overcome its unscalability relied on outdated assumptions that no longer hold true in recent ar- chitectures. Concentrated routers make an assumption that low injection rate would cause low conflicts; however, recent manycore processors and accelerators require streaming bandwidth for their data-intensive workloads. Widening the channel width to recover the bisection bandwidth halved by concentration assumes that the underlying architecture can flexibly adapt to the wider channel width; however, it comes with an additional cost associated with wider datapaths, serialization, and additional buffering. Ruche Networks retain all the desirable properties of 2-D mesh to remain physically scalable, yet provide an architecturally flexible and cost-effective mechanism to effortlessly scale up the network performance by adding uniform long-range physical links. While their feasibility in real silicon has been demonstrated, there has not been any detailed evaluation of its network performance, scalability, and energy efficiency. This paper aims to fill the gap in research by providing some insight on design tradeoffs. Using RTL-level imple- mentations, we demonstrate that Ruche Networks are superior to 2-D mesh and torus in terms of power, area efficiency, cycle time and network performance.

## 中文摘要

二维网格（2-D mesh）凭借设计复杂度低、物理可扩展性好，被广泛用作片上网络拓扑。但它的延迟与吞吐可扩展性差，这一点早已被学界熟知。以往解决其可扩展性短板的方案，建立在一些过时假设之上，不再适用于当下新型架构。集中式路由器假设低注入流量就会带来低冲突；但现代众核处理器与加速器承载访存密集负载时，需要持续的流式带宽。为补偿集中化带来的二分带宽减半而加宽通道，又默认底层架构可以灵活适配更宽通道；而宽通道会带来数据通路、串并转换、缓存等额外开销。

Ruche网络保留二维网格所有利于物理布局的特性，维持良好的物理可扩展性；同时通过增加均匀的长距离物理链路，提供一种架构灵活、性价比高的方式，轻松提升网络性能。虽然Ruche网络在硅片上的可行性已经得到验证，但还缺少对其网络性能、可扩展性与能效的详细评估。本文旨在填补该研究空白，剖析它的设计权衡。基于RTL实现的实验表明：Ruche网络在功耗、面积效率、周期时间以及网络性能上，均优于二维网格和环网（torus）。

## 英文关键词

Network-on-Chip, VLSI, Parallel Architecture

## 中文关键词

片上网络, 超大规模集成电路, 并行架构

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731010)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6B](index.md) · [返回 ISCA 2025](../index.md)
