---
title: "ArtMem: Adaptive Migration in Reinforcement Learning-Enabled Tiered Memory"
description: "ISCA 2025 · Session 3C · ArtMem: 强化学习驱动的分层内存自适应迁移"
tags:
  - "ISCA2025"
  - "Session 3C"
  - "Storage"
---

# ArtMem: Adaptive Migration in Reinforcement Learning-Enabled Tiered Memory

**中文标题：** ArtMem: 强化学习驱动的分层内存自适应迁移

**所属 Session：** [Session 3C](index.md) · [ISCA 2025](../index.md)

**作者：** Xinyue Yi, Hongchao Du, Yu Wang, Jie Zhang, Qiao Li, Chun Jason Xue

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731001) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

With the increasing memory demands of emerging applications, tiered memory has become a viable solution for reducing data cen- ter hardware costs. Given the low performance of the capacity tiers in tiered memory systems, optimizing memory management is crucial in improving overall system performance. This paper identifies three key limitations in existing tiered memory solutions. First, existing solutions often perform differently across different workloads, leading to suboptimal performance in some workloads. Second, they often fail to adjust migration strategies in response to low fast memory tier access rates, resulting in ineffective data placement. Third, they often miss the opportunity to dynamically tune the memory migration scope based on workload patterns, lead- ing to unnecessary page migrations and under-utilization of tiered memory potential. This paper proposes ArtMem, a reinforcement learning (RL)-driven framework that dynamically manages tiered memory systems and adapts to workload evolution to address these limitations. ArtMem enables better placement of memory pages, enhancing system performance while reducing unnecessary migra- tions. Experimental evaluations show that ArtMem outperforms state-of-the-art tiering systems, achieving 35% - 172% performance improvements over diverse workloads.

## 中文摘要

随着新兴应用对内存需求持续增长，分层内存成为降低数据中心硬件成本的可行方案。分层内存系统中大容量层的性能偏低，因此优化内存管理对提升系统整体性能至关重要。本文指出现有分层内存方案存在三点核心缺陷：第一，现有方案在不同负载下表现差异较大，部分负载下性能达不到最优；第二，当高速内存层访问率较低时，方案无法及时调整迁移策略，造成数据放置效果差；第三，方案难以根据负载特征动态调整内存迁移范围，引发不必要的页迁移，分层内存的潜力未能充分发挥。本文提出ArtMem，一个基于强化学习（RL）驱动的框架，对分层内存系统进行动态管理，适配负载变化，解决上述问题。ArtMem可以实现更优的内存页放置，提升系统性能，同时减少无效迁移。实验评测表明，ArtMem优于现有前沿分层内存管理系统，在各类负载上取得35%~172%的性能提升。

## 英文关键词

Operating system, Tiered memory management, Virtual memory, Reinforcement learning

## 中文关键词

操作系统, 分层内存管理, 虚拟内存, 强化学习

## 代码与研究制品

- [代码仓库](https://github.com/Yitrus/ArtMem)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731001)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3C](index.md) · [返回 ISCA 2025](../index.md)
