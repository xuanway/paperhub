---
title: "Zettafly: A Network Topology with Flexible Non-blocking Regions for Large-scale AI and HPC Systems"
description: "ISCA 2025 · Session 5B · Zettafly：面向大规模 AI 与 HPC 系统的灵活无阻塞区域网络拓扑"
tags:
  - "ISCA2025"
  - "Session 5B"
  - "HPC for ML/AI"
---

# Zettafly: A Network Topology with Flexible Non-blocking Regions for Large-scale AI and HPC Systems

**中文标题：** Zettafly：面向大规模 AI 与 HPC 系统的灵活无阻塞区域网络拓扑

**所属 Session：** [Session 5B](index.md) · [ISCA 2025](../index.md)

**作者：** Dezun Dong, Ziyu Wang, Fei Lei

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731098) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Interconnection networks are playing an increasingly crucial role in achieving scalability and throughput for post-exascale and zettas- cale computing systems. Resource consumption characteristics of AI and HPC workloads are essential to designing effective network infrastructure. The operation practice of production supercomput- ing systems reveals that small and medium-sized jobs consume most compute-core hours, generating traffic that mainly utilizes a size-restricted portion of the network. Unfortunately, current topologies lack sufficient support for flexible partitioning of dis- tinct concurrent jobs. This study bridges this gap by exploring a new tradeoff among scalability, throughput, and non-blocking re- gions. We present Zettafly, a family of low-diameter topologies with large-scale non-blocking sub-networks, allowing the majority of jobs to be isolated within a single sub-network. Zettafly is a two-layer structure, consisting of non-blocking groups and global routers, such that each minimally routed packet between groups traverses at most one global router. We also introduce simple and efficient adaptive routing algorithms for Zettafly. We conduct exten- sive simulations and analysis to evaluate the performance and cost of Zettafly against state-of-the-art topologies. The results show that Zettafly achieves great performance under typical HPC workloads, offers cost-effectiveness under multi-task mixed traffic, supports flexible configurations and incremental deployments, and is cost- effective to deploy for post-exascale and zettascale systems.

## 中文摘要

互连网络在实现后百亿亿次和泽塔级计算系统的可扩展性和吞吐量方面发挥着越来越重要的作用。 AI 和 HPC 工作负载的资源消耗特征对于设计有效的网络基础设施至关重要。生产超级计算系统的运行实践表明，中小型作业消耗了大部分计算核心时间，产生的流量主要利用网络中大小受限的部分。不幸的是，当前的拓扑缺乏对不同并发作业的灵活分区的足够支持。本研究通过探索可扩展性、吞吐量和非阻塞区域之间的新权衡来弥补这一差距。我们推出了 Zettafly，这是一个具有大规模无阻塞子网络的低直径拓扑系列，允许将大多数作业隔离在单个子网络内。

Zettafly 是一种两层结构，由非阻塞组和全局路由器组成，使得组之间的每个最小路由数据包最多穿过一个全局路由器。我们还为 Zettafly 引入了简单高效的自适应路由算法。我们进行了广泛的模拟和分析，以根据最先进的拓扑来评估 Zettafly 的性能和成本。结果表明，Zettafly 在典型 HPC 工作负载下实现了出色的性能，在多任务混合流量下提供了成本效益，支持灵活的配置和增量部署，并且对于后百亿亿次和 zettascale 系统的部署具有成本效益。

## 英文关键词

Network topology, Non-blocking region, Zettascale computing

## 中文关键词

网络拓扑, 无阻塞区域, Z级计算

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731098)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 5B](index.md) · [返回 ISCA 2025](../index.md)
