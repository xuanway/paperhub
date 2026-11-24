---
title: "Don’t Surrender to Low QPS/$: Fast and Cost-Efficient ANNS with TRIDENTANN"
description: "ISCA 2026 · Session 2D · Don’t Surrender to Low QPS/$: Fast and Cost-Efficient ANNS with TRIDENTANN"
tags:
  - "ISCA2026"
  - "Session 2D"
  - "Storage"
---

# Don’t Surrender to Low QPS/$: Fast and Cost-Efficient ANNS with TRIDENTANN

**中文标题：** 不要屈服于低 QPS/$：基于 TRIDENTANN 的快速且成本高效 ANNS

**所属 Session：** [Session 2D](index.md) · [ISCA 2026](../index.md)

**作者：** Yuchen Huang, Baiteng Ma, Erci Xu, Chuliang Weng

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The scale of vector data has been continuously growing. SSD-based approximate nearest neighbor search (ANNS) methods have become popular in handling billion-scale vectors with just one node. While delivering high performance in terms of query per second (QPS), they often fall short in the cost efficiency (i.e., QPS/$). In this paper, we present TRIDENTANN, a high-performance yet cost-efficient system for large-scale ANNS with strengths of SSDs, low-end GPUs, and CPUs. We start by proposing a hybrid noise-clusters index for efficient I/O utilization and parallel search for decoupled noise and clusters. Second, we customize hardware-software architecture for GPU-SSD ANNS, which enables full bandwidth utilization when transferring data between GPUs and SSDs. Third, we orchestrate GPU-CPU-SSD task pipelines in parallel according to hardware characteristics to maximize system efficiency. Evaluations show that, compared to existing ANNS systems, TRIDENTANN performs 1.8-3.4× throughput and 21-70% of the latency. More importantly, it can be deployed on readily available and affordable devices, and achieves much higher cost efficiency (∼2-4× QPS/$) than others.

## 中文摘要

向量数据的规模持续增长。基于SSD的近似最近邻搜索（ANNS）方法在处理仅需单节点的十亿级向量时已变得流行。虽然这些方法在每秒查询数（QPS）方面表现出高性能，但通常在成本效率（即QPS/$）方面有所不足。本文提出TRIDENTANN，一个集SSD、低端GPU和CPU优势的高性能且成本高效的大规模ANNS系统。我们首先提出一种混合噪声-聚类索引，以实现高效的I/O利用和对解耦的噪声与聚类进行并行搜索。其次，我们针对GPU-SSD ANNS定制了软硬件架构，实现了GPU与SSD间数据传输的全带宽利用。第三，我们根据硬件特性并行编排GPU-CPU-SSD任务流水线，以最大化系统效率。评估表明，与现有ANNS系统相比，TRIDENTANN的吞吐量达到1.8–3.4×，延迟降至21–70%。更重要的是，它可部署在现成且廉价的设备上，成本效率（QPS/$）提升了约2–4×。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 2D](index.md) · [返回 ISCA 2026](../index.md)
