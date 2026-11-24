---
title: "VertexSurge: Variable Length Graph Pattern Match on Billion-edge Graphs"
description: "ASPLOS 2025 · Session 4C · VertexSurge：十亿边图上的变长图模式匹配"
tags:
  - "ASPLOS2025"
  - "Session 4C"
  - "Potpourri 1"
---

# VertexSurge: Variable Length Graph Pattern Match on Billion-edge Graphs

**中文标题：** VertexSurge：十亿边图上的变长图模式匹配

**所属 Session：** [Session 4C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Weiyu Xie (Department of Computer Science and Technology, Beijing National Research Center for Information Science and Technology (BNRist), Tsinghua University), MingXing Zhang (Department of Computer Science and Technology, Beijing National Research Center for Information Science and Technology (BNRist), Tsinghua University), Xia Liao (Department of Computer Science and Technology, Beijing National Research Center for Information Science and Technology (BNRist), Tsinghua University), Kang Chen (Department of Computer Science and Technology, Beijing National Research Center for Information Science and Technology (BNRist), Tsinghua University), Jinlei Jiang (Department of Computer Science and Technology, Beijing National Research Center for Information Science and Technology (BNRist), Tsinghua University), YongWei Wu (Department of Computer Science and Technology, Beijing National Research Center for Information Science and Technology (BNRist), Tsinghua University)

**单位：** BNRist

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674173) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Variable-Length Graph Pattern Matching (VLGPM) is a critical functionality in graph databases, pivotal for identifying patterns where the number of connecting edges between two matched vertices is variable. This function plays a vital role in analyzing complex and dynamic networks such as social networks or bank transfers networks, where relationships can vary extensively in both length and structure. However, despite its importance, current graph databases, optimized primarily for single-hop subgraph matching, struggle with VLGPM over large graphs. To bridge this gap between essential user requirements and the lack of efficient support in existing systems, we introduce VertexSurge. Central to VertexSurge is an innovative variable-length expand (VExpand) operator, which incorporates several microarchitecture-friendly optimizations to efficiently compute the reachability matrix between two sets of vertices. These optimizations enable VertexSurge to handle the surge of vertex count due to variable length with high performance. Additionally, VertexSurge combines VExpand with effective multi-set intersection for pattern matching, ruled-based planning, and disk offloading for large datasets, to implement a full-fledged VLGPM engine. Our evaluations with real-world graph datasets and representative patterns demonstrate that VertexSurge significantly outperforms existing systems in VLGPM, validating its efficacy in handling large-scale graph pattern matching challenges.

## 中文摘要

变长图模式匹配（Variable-Length Graph Pattern Matching, VLGPM）是图数据库中的一项关键功能，对于识别两个匹配顶点之间连接边数量可变的模式至关重要。该功能在分析社交网络或银行转账网络等复杂动态网络时发挥着重要作用，这些网络中的关系在长度和结构上都可能大幅变化。然而，尽管其重要性显著，当前主要针对单跳子图匹配进行优化的图数据库在大图上的 VLGPM 上表现不佳。为弥合关键用户需求与现有系统缺乏高效支持之间的这一差距，我们提出 VertexSurge。VertexSurge 的核心是一个创新的变长扩展（VExpand）算子，它集成了多项对微体系结构友好的优化，以高效计算两组顶点之间的可达性矩阵。这些优化使 VertexSurge 能够以高性能应对变长带来的顶点数量激增。此外，VertexSurge 将 VExpand 与用于模式匹配的高效多重集求交、基于规则的规划以及面向大数据集的磁盘卸载相结合，实现了一个完整的 VLGPM 引擎。我们使用真实世界图数据集与代表性模式的评测表明，VertexSurge 在 VLGPM 上显著优于现有系统，验证了其在应对大规模图模式匹配挑战方面的有效性。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674173)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4C](index.md) · [返回 ASPLOS 2025](../index.md)
