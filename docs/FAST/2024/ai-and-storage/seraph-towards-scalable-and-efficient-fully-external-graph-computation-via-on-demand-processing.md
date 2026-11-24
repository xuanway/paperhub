---
title: "Seraph: Towards Scalable and Efficient Fully-external Graph Computation via On-demand Processing"
description: "FAST 2024 · AI and Storage · 第 373–388 页"
tags:
  - "FAST2024"
  - "AI and Storage"
---

# Seraph: Towards Scalable and Efficient Fully-external Graph Computation via On-demand Processing

**中文标题**：Seraph：通过按需处理实现可扩展且高效的全外存图计算

**Session**：AI and Storage · 2024-02-29 10:45–12:00 · Chair：Patrick P. C. Lee（The Chinese University of Hong Kong (CUHK)）

**作者**：Tsun-Yu Yang, Yizou Chen, Yuhong Liang, and Ming-Chang Yang, The Chinese University of Hong Kong

**会议**：FAST 2024 · Santa Clara, CA · 第 373–388 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/yang-tsun-yu](https://www.usenix.org/conference/fast24/presentation/yang-tsun-yu)

**论文 PDF**：[fast24-yang-tsun-yu.pdf](https://www.usenix.org/system/files/fast24-yang-tsun-yu.pdf)

---

## 英文摘要

Fully-external graph computation systems exhibit optimal scalability by computing the ever-growing, large-scale graph with constant amount of memory on a single machine. In particular, they keep the entire massive graph data in storage and iteratively load parts of them into memory for computation. Nevertheless, despite the merit of optimal scalability, their unreasonably-low efficiency often makes them uncompetitive, and even unpractical, to the other types of graph computation systems. The key rationale is that most existing fully-external graph computation systems over-emphasize retrieving graph data from storage through sequential access. Although this principle achieves high storage bandwidth, it often causes reading excessive and irrelevant data, which can severely degrade their overall efficiency.

Therefore, this work presents Seraph, a fully-external graph computation system that achieves optimal Scalability while toward satisfactory Efficiency improvement. Particularly, inspired by the modern storage offering comparable sequential and random access speeds, Seraph adopts the principle of *on-demand processing* to access the necessary graph data for saving I/O while enjoying the decent speed in random access. On the basis of this principle, Seraph further devises three practical designs to bring excellent performance leap to fully-external graph computation: 1) the hybrid format to represent the graph data for striking a good balance between I/O amount and access locality, 2) the vertex passing to enable efficient vertex updates on top of hybrid format, and 3) the selective pre-computation to re-use the loaded data for I/O reduction. Our evaluations reveal that Seraph notably outperforms other state-of-the-art fully-external systems under all the evaluated billion-scale graphs and representative graph algorithms by up to two orders of magnitude.

## 中文摘要

全外存图计算系统通过在单机上以恒定内存量计算不断增长的大规模图，展现出最优的可扩展性。具体而言，它们将整个海量图数据保存在存储中，并迭代地将其中一部分加载到内存进行计算。然而，尽管具有最优可扩展性的优点，其低得不合理的效率往往使其相对于其他类型的图计算系统缺乏竞争力，甚至不切实际。关键原因在于，大多数现有全外存图计算系统过度强调通过顺序访问从存储中取回图数据。尽管这一原则实现了高存储带宽，但它常常导致读取过多且无关的数据，从而严重降低整体效率。

因此，本工作提出 Seraph，一个全外存图计算系统，在实现最优可扩展性的同时，朝着令人满意的效率提升迈进。特别地，受现代存储提供可比顺序与随机访问速度的启发，Seraph 采用 *按需处理* 原则，只访问必要的图数据以节省 I/O，同时享受随机访问的良好速度。在此原则基础上，Seraph 进一步设计三项实用技术，为全外存图计算带来卓越的性能飞跃：1) 混合格式表示图数据，在 I/O 量与访问局部性之间取得良好平衡；2) 顶点传递，在混合格式之上实现高效的顶点更新；3) 选择性预计算，复用已加载的数据以减少 I/O。我们的评估表明，在所有评估的十亿级图和代表性图算法下，Seraph 显著优于其他最先进的全外存系统，最高可达两个数量级。
