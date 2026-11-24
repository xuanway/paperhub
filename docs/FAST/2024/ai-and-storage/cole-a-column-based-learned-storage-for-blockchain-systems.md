---
title: "COLE: A Column-based Learned Storage for Blockchain Systems"
description: "FAST 2024 · AI and Storage · 第 329–346 页"
tags:
  - "FAST2024"
  - "AI and Storage"
---

# COLE: A Column-based Learned Storage for Blockchain Systems

**中文标题**：COLE：面向区块链系统的基于列的学习型存储

**Session**：AI and Storage · 2024-02-29 10:45–12:00 · Chair：Patrick P. C. Lee（The Chinese University of Hong Kong (CUHK)）

**作者**：Ce Zhang and Cheng Xu, Hong Kong Baptist University; Haibo Hu, Hong Kong Polytechnic University; Jianliang Xu, Hong Kong Baptist University

**会议**：FAST 2024 · Santa Clara, CA · 第 329–346 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/zhang-ce](https://www.usenix.org/conference/fast24/presentation/zhang-ce)

**论文 PDF**：[fast24-zhang_ce.pdf](https://www.usenix.org/system/files/fast24-zhang_ce.pdf)

---

## 英文摘要

Blockchain systems suffer from high storage costs as every node needs to store and maintain the entire blockchain data. After investigating Ethereum's storage, we find that the storage cost mostly comes from the index, i.e., Merkle Patricia Trie (MPT). To support provenance queries, MPT persists the index nodes during the data update, which adds too much storage overhead. To reduce the storage size, an initial idea is to leverage the emerging learned index technique, which has been shown to have a smaller index size and more efficient query performance. However, directly applying it to the blockchain storage results in even higher overhead owing to the requirement of persisting index nodes and the learned index's large node size. To tackle this, we propose COLE, a novel column-based learned storage for blockchain systems. We follow the column-based database design to contiguously store each state's historical values, which are indexed by learned models to facilitate efficient data retrieval and provenance queries. We develop a series of write-optimized strategies to realize COLE in disk environments. Extensive experiments are conducted to validate the performance of the proposed COLE system. Compared with MPT, COLE reduces the storage size by up to 94% while improving the system throughput by 1.4×-5.4×.

## 中文摘要

区块链系统面临高存储成本，因为每个节点都需要存储并维护整个区块链数据。在考察以太坊的存储后，我们发现存储成本主要来自索引，即默克尔 Patricia 树（MPT）。为支持溯源查询，MPT 在数据更新期间持久化索引节点，这带来了过多的存储开销。为减小存储大小，一个初步想法是利用新兴的学习型索引技术，该技术已被证明具有更小的索引大小和更高效的查询性能。然而，由于需要持久化索引节点以及学习型索引节点较大，直接将其应用于区块链存储会导致更高的开销。为解决这一问题，我们提出 COLE，一种新颖的面向区块链系统的基于列的学习型存储。我们遵循基于列的数据库设计，连续存储每个状态的历史值，并用学习模型对这些值建立索引，以支持高效的数据检索和溯源查询。我们开发了一系列写优化策略，以在磁盘环境中实现 COLE。大量实验验证了所提出 COLE 系统的性能。与 MPT 相比，COLE 将存储大小最多减少 94%，同时将系统吞吐量提升 1.4–5.4 倍。
