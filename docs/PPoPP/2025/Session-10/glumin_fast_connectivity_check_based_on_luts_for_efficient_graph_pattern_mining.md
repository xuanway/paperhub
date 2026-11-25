---
title: "GLUMIN: Fast Connectivity Check Based on LUTs For Efficient Graph Pattern Mining"
description: "PPoPP 2025 Session 10（GPU II）：运行时压缩 LUT 加速连通性检查，GPM 系统提速两个数量级"
tags:
  - "PPoPP2025"
  - "Session-10"
  - "GPU II"
  - "Graph Pattern Mining"
  - "Connectivity Check"
  - "LUT"
authors:
  - "Weichen Cao"
  - "Ke Meng"
  - "Zhiheng Lin"
  - "Guangming Tan"
session: "Session 10: GPU II"
session_number: 10
session_chair: "Zhijia Zhao"
date: "2025-03-05"
time: "10:40–11:00"
room: "Acacia D"
doi: "10.1145/3710848.3710889"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# GLUMIN: Fast Connectivity Check Based on LUTs For Efficient Graph Pattern Mining

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 GLUMIN，通过把 CSR 部分还原为邻接矩阵、在运行时选择性构建压缩查找表（LUT），显著加速图模式挖掘中的连通性判断与公共邻居计数。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 10: GPU II</p>
</div>

**作者**：Weichen Cao, Ke Meng, Zhiheng Lin, Guangming Tan (Institute of Computing Technology, Chinese Academy of Sciences. University of Chinese Academy of Sciences. State Key Laboratory of Processors, ICT, Chinese Academy of Sciences.)

**会议**：PPoPP 2025 · 2025 年 3 月 5 日 10:40–11:00 · Session 10: GPU II（主席：Zhijia Zhao）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710889) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 GLUMIN，通过把 CSR 部分还原为邻接矩阵、在运行时选择性构建压缩查找表（LUT），显著加速图模式挖掘中的连通性判断与公共邻居计数。

## 研究问题

图模式挖掘需要海量边检查——枚举顶点对并判断连通性或统计公共邻居；CSR/邻接表虽能应对图的稀疏性，却丧失了邻接矩阵 O(1) 连通查询的能力。

## 方法简述

- 从 CSR 部分还原为邻接矩阵，选择性构建运行时可低成本重复查询的 LUT。
- 对 LUT 做压缩与裁剪，使其适配 GPU 共享内存、CPU cache 等层次化存储。

## 主要结果

- 将该技术用于 AutoMine、G2Miner、GraphFold 等 SOTA GPM 系统。
- 在 100 多个图、24 种模式上带来两个数量级的加速，体现了通用性。

<details>
<summary>原文摘要（英文）</summary>

Graph Pattern Mining (GPM) has made significant progress in recent years, supporting a range of big data applications. However, GPM applications are memory-intensive as they require a tremendous amount of edge checking, which involves enumerating all possible vertex pairs and checking their connectivity or counting the common neighbors of each pair. Adjacent list or CSR format is widely used in recent GPM systems to overcome the sparsity of real-world graph, at the cost of sacrificing the ability to query the connectivity of two vertices in 𝑂(1) compared with the raw adjacent matrix. In this paper, we rethink the format to store graph in GPM systems, by partial “restoring” graph from CSR to adjacent matrix, we can significantly accelerate checking connectivity or counting common neighbors for GPM algorithms. However, directly storing graph in adjacent matrix is cost-prohibitive, thus we propose GLUMIN, by selectively constructing a lookup table (LUT) at the runtime, which holds the connectivity that can be repeatedly retrieved at low cost. The LUTs are compressed and tailored to fit the hierarchical memory architecture like shared memory of GPU or cache of CPU. We adopt GLUMIN technique to several SOTA GPM systems like AutoMine, G2Miner and GraphFold, bringing two orders of magnitude speedup to them on more than 100 different graphs and 24 patterns, demonstrating the general applicability and significance of our methods.

</details>

---

> 所属 Session：[Session 10: GPU II](index.md) · 返回 [PPoPP 2025 总览](../index.md)
