---
title: "Dorado: Clustered Hardware Cache Coherence for 1,000+ Cores"
description: "ISCA 2026 · Session 3D · Dorado: Clustered Hardware Cache Coherence for 1,000+ Cores"
tags:
  - "ISCA2026"
  - "Session 3D"
  - "Microarchitexture"
---

# Dorado: Clustered Hardware Cache Coherence for 1,000+ Cores

**中文标题：** Dorado: 面向 1,000+ 核的簇化硬件缓存一致性

**所属 Session：** [Session 3D](index.md) · [ISCA 2026](../index.md)

**作者：** Jovan Stojkovic, Abraham Farrell, Gerasimos Gerogiannis, Zhangxiaowen Gong, Christopher J. Hughes, Josep Torrellas

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

As processors continue to grow in size, they will soon include over one thousand cores and, in at least some markets, require hardware cache coherence over all of the cores. In these systems, the costs of coherence transaction latency/traffic and directory storage will escalate. An intuitive way to contain these costs is to group cores into clusters and exploit intra-cluster locality. However, latency/traffic gains are thwarted by the need to access home directories in remote clusters, and storage reductions are limited by having to track many sharers. To address these obstacles, this paper introduces Dorado, a new directory-based coherence protocol for 1,000+ cores that exploits clusters. Dorado makes three contributions. First, while each line has a Global home directory slice, it can also have Temporary home directory slices in each of the clusters where and while it is referenced. This minimizes high-latency/traffic transactions. Second, a directory can contain different types of entries and sharer pointers, each behaving differently. To use space efficiently, Dorado allows them all to dynamically share the same hardware structures—adapting their relative space to the workload sharing patterns. Third, to support many-sharer lines with modest directory storage, Dorado introduces a simple mechanism for directory entries to grow into a shared area. Simulations of 1024 cores running a variety of workloads show that Dorado is effective. It attains an average speedup of 1.36× over a same-area limited-pointer protocol by reducing the average load latency by 46.1%. Further, Dorado stays within 1% of the performance of a full bit vector protocol while using 2.75× less directory storage.

## 中文摘要

随着处理器规模不断增长，它们很快将包含超过一千个核，并且至少在某些市场中需要覆盖所有核的硬件缓存一致性。在这些系统中，一致性事务的延迟/流量以及目录存储的成本将不断攀升。将这些成本限制住的一种直观方法是将核分组为簇，并利用簇内局部性。然而，延迟/流量方面的收益会被访问远程簇中主目录的需求所抵消，而存储的减少也因必须跟踪众多共享者而受限。为解决这些障碍，本文提出 Dorado，一种面向 1,000+ 核、利用簇结构的新型基于目录的一致性协议。Dorado 有三项贡献。第一，虽然每一行都有一个全局主目录片（Global home directory slice），但它还可以在其被引用的每个簇中、在被引用期间拥有临时主目录片（Temporary home directory slices）。这使高延迟/高流量的事务降至最少。第二，目录可以包含不同类型的表项与共享者指针，各自行为不同。为高效利用空间，Dorado 允许它们全部动态共享相同的硬件结构——根据工作负载的共享模式调整其相对空间。第三，为以适度的目录存储支持多共享者行，Dorado 引入一种简单机制，使目录表项可以扩展进一个共享区域。对运行多种工作负载的 1024 核进行的仿真表明 Dorado 是有效的。通过将平均加载延迟降低 46.1%，它相比面积相同的有限指针协议取得 1.36× 的平均加速。此外，Dorado 在使用的目录存储少 2.75× 的情况下，性能与完整位向量协议相差不到 1%。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3D](index.md) · [返回 ISCA 2026](../index.md)
