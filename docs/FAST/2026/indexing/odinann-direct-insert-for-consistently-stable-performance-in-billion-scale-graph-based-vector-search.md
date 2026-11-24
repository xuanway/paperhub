---
title: "OdinANN: Direct Insert for Consistently Stable Performance in Billion-Scale Graph-Based Vector Search"
description: "FAST 2026 · Indexing · 第 133–148 页"
tags:
  - "FAST2026"
  - "Indexing"
---

# OdinANN: Direct Insert for Consistently Stable Performance in Billion-Scale Graph-Based Vector Search

**中文标题**：OdinANN：直接插入以实现十亿级图向量检索的一致稳定性能

**Session**：Indexing · 2026-02-24 14:00–15:40 · Chair：Zhichao Cao（Arizona State University）

**作者**：Hao Guo and Youyou Lu, Tsinghua University

**会议**：FAST 2026 · Santa Clara, CA · 第 133–148 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/guo](https://www.usenix.org/conference/fast26/presentation/guo)

**论文 PDF**：[fast26-guo.pdf](https://www.usenix.org/system/files/fast26-guo.pdf)

---

## 英文摘要

Approximate Nearest Neighbor Search (ANNS) is widely used in various scenarios. For billion-scale ANNS, on-disk graph-based indexes, which organize the vectors as a graph and store them on disk, are favored for their performance and cost-efficiency. However, existing indexes can not maintain a stable search performance while inserting new vectors.

In this paper, we propose to use direct insert, which directly inserts vectors into the on-disk index, rather than buffering them in memory and merging them to disk in batches like existing systems. This approach can even out the interference of insert with frontend search, thus stabilizing the performance. We evaluate direct insert by integrating it into a billion-scale graph-based ANNS index named OdinANN. With a fixed insert rate, OdinANN outperforms state-of-the-art ANNS indexes in search latency and throughput, and it consistently shows stable performance in billion-scale vector datasets.

## 中文摘要

近似最近邻搜索（ANNS）被广泛用于各种场景。对于十亿级 ANNS，磁盘上的图索引因性能与成本效益而备受青睐，这类索引将向量组织成图并存储在磁盘上。然而，现有索引在插入新向量时无法保持稳定的搜索性能。

本文提出采用直接插入：直接将向量插入磁盘上的索引，而不是像现有系统那样先在内存中缓冲，再批量合并到磁盘。这种方法可以平抑插入对前端搜索的干扰，从而稳定性能。我们通过将直接插入集成到名为 OdinANN 的十亿级图 ANNS 索引中来评估它。在固定插入速率下，OdinANN 在搜索延迟和吞吐量方面优于最先进的 ANNS 索引，并在十亿级向量数据集上持续表现出稳定的性能。
