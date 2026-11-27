---
title: "TidalMesh: Topology-Driven AllReduce Collective Communication for Mesh Topology"
description: "HPCA 2025 · Colluding to Even the Odds"
tags:
  - "HPCA2025"
  - "Colluding to Even the Odds"
---

# TidalMesh: Topology-Driven AllReduce Collective Communication for Mesh Topology

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Colluding to Even the Odds。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Colluding to Even the Odds</p>
</div>

**论文链接**：
**作者**：Dongkyun Lim (KAIST), John Kim (KAIST)
**会议**：HPCA 2025

---

## 中文标题

TidalMesh：面向网格拓扑的拓扑驱动 AllReduce 集合通信

## 英文摘要

In deep learning workloads, collective communication across multiple nodes is a critical component in determining overall performance. AllReduce (as well as ReduceScatter and AllGather) is a commonly used collective communication for not only training but also inference. The performance of AllReduce depends on the algorithm utilized (or the “logical” topology) as well as the physical topology of the system that interconnects the nodes together. There has been many work on improving AllReduce performance but prior work have often been topology-aware approach where existing AllReduce algorithms were optimized for a given physical topology. In this work, we propose a topology-driven approach where the topology characteristics are exploited to propose a novel AllReduce collective communication algorithm; thus, the logical topology of the algorithm maps well to the physical topology. In particular, as 2D mesh topology is widely used in various scale-out systems, we propose TidalMesh AllReduce algorithm – a novel approach that exploits the inherent characteristics of the physical 2D mesh topology by pushing flows between the endpoint nodes, similar to a tidal wave, to achieve near-optimal performance for AllReduce. We propose how Sparse TidalMesh AllReduce minimizes bandwidth overhead of TidalMesh with no loss in performance. In addition, we demonstrate how collective communication unrolling can be exploited to enable “software pipelining” of collective communication while exploiting the unique opportunity of superimposing different phases of AllReduce. As a result, TidalMesh results in up to 24% improvement in AllReduce performance across various deep learning models on a 64-node 8x8 2D mesh, compared to the state-of-the-art while maintaining the simplicity of a logical ring algorithm.

## 中文摘要

在深度学习负载中，跨多个节点的集合通信是决定整体性能的关键组成部分。AllReduce（以及 ReduceScatter 与 AllGather）不仅是训练、也是推理中常用的集合通信。AllReduce 的性能取决于所采用的算法（或其“逻辑”拓扑）以及把节点互连在一起的系统物理拓扑。已有许多工作致力于提升 AllReduce 性能，但先前工作往往是拓扑感知的方法，即针对给定物理拓扑优化已有的 AllReduce 算法。在本工作中，我们提出一种拓扑驱动的方法，利用拓扑特征来提出一种新颖的 AllReduce 集合通信算法；于是该算法的逻辑拓扑能很好地映射到物理拓扑。特别地，由于 2D 网格拓扑被广泛用于各种横向扩展系统，我们提出 TidalMesh AllReduce 算法——一种新颖方法，通过像潮汐波一样在端点节点之间推送流，利用物理 2D 网格拓扑的固有特性，为 AllReduce 实现近最优性能。我们提出 Sparse TidalMesh AllReduce 如何在无性能损失的情况下最小化 TidalMesh 的带宽开销。此外，我们演示了如何利用集合通信展开来实现集合通信的“软件流水”，同时利用叠加 AllReduce 不同阶段的独特机会。最终，在 64 节点 8x8 2D 网格上，与最先进方案相比，TidalMesh 在各种深度学习模型上使 AllReduce 性能最高提升 24%，同时保持逻辑环算法的简洁性。
