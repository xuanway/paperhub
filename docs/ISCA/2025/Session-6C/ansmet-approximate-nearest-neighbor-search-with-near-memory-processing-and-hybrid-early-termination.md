---
title: "ANSMET: Approximate Nearest Neighbor Search with Near-Memory Processing and Hybrid Early Termination"
description: "ISCA 2025 · Session 6C · ANSMET: 近存处理与混合早停的近似最近邻搜索"
tags:
  - "ISCA2025"
  - "Session 6C"
  - "Memory Acceleration"
---

# ANSMET: Approximate Nearest Neighbor Search with Near-Memory Processing and Hybrid Early Termination

**中文标题：** ANSMET: 近存处理与混合早停的近似最近邻搜索

**所属 Session：** [Session 6C](index.md) · [ISCA 2025](../index.md)

**作者：** Yiwei Li, Yuxin Jin, Boyu Tian, Huanchen Zhang, Mingyu Gao

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731013) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Approximate nearest neighbor search (ANNS) is a fundamental operation in modern vector databases to efficiently retrieve nearby vectors to a given query. On general-purpose computing platforms, ANNS is found not only to be highly memory-bound due to the large amount of high-dimensional vectors to access, but also exhibits very low utilization of the fetched data as many memory accesses and computations are wasted on not-so-nearby vectors. To alleviate these two inefficiencies, we propose a hardware-software co-design that integrates near-data processing architectures with a novel hybrid partial-dimension/bit early termination strategy. Distance calculation and comparison in ANNS are offloaded to the near-data processing units at the memory rank level. As a vector is being gradually fetched from memory, we conservatively estimate a lower bound of its distance to the query using the partially fetched data, e.g., a subset of dimensions and/or partial bits of each element. If this lower bound already exceeds a threshold, we could early terminate to avoid future unnecessary data accesses and computations. In the presence of such irregular early termination execution flow, we further optimize the data layouts within a single memory access and across multiple memory ranks in the system, and handle efficient coordination between the near-data units and the host processor that executes the rest of index traversal and result sorting. With all the above optimizations, our design demonstrates an average 5.26×speedup of using near-data processing, and another 1.52× from enabling hybrid early termination on top of it.

## 中文摘要

近似最近邻搜索（ANNS）是现代向量数据库的核心算子，用于快速检索与查询向量相近的向量。在通用计算平台上，ANNS属于强访存瓶颈型负载：需要读取大量高维向量；同时读出数据利用率很低，大量访存与计算消耗在距离较远、无关紧要的向量上。
为解决这两类低效问题，本文提出软硬件协同设计方案，融合近数据处理架构，并提出全新的混合部分维度/部分比特提前终止策略。ANNS中的距离计算与比较逻辑下放到内存颗粒级别的近数据处理单元。向量从内存逐步读出时，方案利用已读出的部分数据（部分维度、或者每个元素的部分比特）保守估算该向量与查询向量距离的下界。如果该下界已经超过阈值，就触发提前终止，省去后续不必要的访存与计算。
针对提前终止带来的不规则执行流，本文进一步优化单次访存内、跨多个内存颗粒的数据布局，并实现近数据单元与主机处理器之间的高效协同；主机负责剩余索引遍历与结果排序。
实验结果表明：仅采用近数据处理平均提速5.26倍；在此基础上叠加混合提前终止机制，可再获得1.52倍提速。

## 英文关键词

approximate nearest neighbor search, hardware acceleration, near-data processing, early termination

## 中文关键词

近似最近邻搜索, 硬件加速, 近数据处理, 提前终止

## 代码与研究制品

- [代码仓库](https://github.com/tsinghua-ideal/ANSMET)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731013)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6C](index.md) · [返回 ISCA 2025](../index.md)
