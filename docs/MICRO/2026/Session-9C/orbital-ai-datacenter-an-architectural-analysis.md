---
title: "Orbital AI Datacenter: An Architectural Analysis"
description: "MICRO 2026 · Session 9C · 轨道 AI 数据中心：架构分析"
tags:
  - "MICRO2026"
---

# Orbital AI Datacenter: An Architectural Analysis

**中文标题：** 轨道 AI 数据中心：架构分析

**所属 Session：** [Session 9C](index.md) · [MICRO 2026](../index.md)

**作者：** Barry Lyu, August Ning, Ronald Dreslinski, Nathaniel Bleier

**来源：** MICRO 2026，pp. 3378–3394；[DOI](https://doi.org/10.1109/MICRO67795.2026.00226)

## 英文摘要

Compute demand for frontier AI training is growing at 5x year, straining compute hardware, terrestrial power grids and cooling infrastructure. Motivated by abundant solar energy and radiative heat rejection without cooling towers or chillers, several recent proposals have suggested moving AI training into orbit, ranging from disaggregated satellite platforms to distributed constellations and monolithic orbital mega-structures. However, the feasibility and economics of orbital AI training remain largely unexplored. This paper presents an architectural and techno-economic analysis of the benefits and limitations of orbital AI datacenters. We characterize the key constraints that distinguish in-space AI training from its terrestrial counterpart, including thermal management, radiation and deployment logistics. Under plausible launch and maintenance rates, orbital datacenters are unlikely to become a primary substitute for terrestrial capacity. We develop a bottom-up, compute-centric cost model to quantify the overhead of sustaining compute in orbit. Orbital compute remains more expensive than terrestrial capacity across the modeled scenarios, even under optimistic hardware and launch assumptions. Our performance analysis further shows that communication bottlenecks and radiation-induced errors lead to severely underutilized compute, compounding the cost disadvantage. We further show that scaling up individual satellites to improve co-location and amortize structural overhead is necessary to mitigate both cost and performance penalties, but that debris avoidance, construction complexity and single-point-of-failure risk render this approach untenable beyond megawatt scales. Under moderate assumptions, even the cost-optimal satellite scale retains a substantial cost disadvantage relative to terrestrial infrastructure. We conclude that edge inference on space-generated data better matches space computing than frontier training because the interconnect, synchronization and reliability demands that defeat training are absent.

## 中文摘要

前沿人工智能训练的计算需求以每年 5 倍的速度增长，给计算硬件、地面电网和冷却基础设施带来压力。受丰富的太阳能和无需冷却塔或冷却器的辐射热排斥的推动，最近的几项提案建议将人工智能训练转移到轨道上，范围从分散的卫星平台到分布式星座和整体轨道巨型结构。然而，轨道人工智能训练的可行性和经济性在很大程度上仍未得到探索。本文对轨道人工智能数据中心的优点和局限性进行了架构和技术经济分析。我们描述了区分太空人工智能训练与地面人工智能训练的关键限制因素，包括热管理、辐射和部署物流。在合理的发射和维护率下，轨道数据中心不太可能成为地面容量的主要替代品。我们开发了一个自下而上、以计算为中心的成本模型，以量化维持轨道计算的开销。在建模场景中，即使在乐观的硬件和发射假设下，轨道计算仍然比地面计算更昂贵。我们的性能分析进一步表明，通信瓶颈和辐射引起的错误导致计算严重未充分利用，从而加剧了成本劣势。我们进一步表明，扩大单个卫星的规模以改善协同定位并分摊结构开销对于减轻成本和性能损失是必要的，但碎片避免、施工复杂性和单点故障风险使得这种方法在超过兆瓦规模时无法维持。在适度的假设下，即使是成本最优的卫星规模，相对于地面基础设施也仍然存在巨大的成本劣势。我们得出的结论是，对空间生成数据的边缘推理比前沿训练更适合空间计算，因为这类推理不存在使前沿训练难以实施的互连、同步与可靠性要求。

## 中文关键词

轨道计算；人工智能数据中心；分布式训练；星间通信；总拥有成本

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.22698121](https://doi.org/10.5281/zenodo.22698121)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9C](index.md) · [MICRO 2026 主页](../index.md)
