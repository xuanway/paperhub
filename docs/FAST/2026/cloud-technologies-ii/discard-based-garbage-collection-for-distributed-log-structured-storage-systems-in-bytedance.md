---
title: "Discard-Based Garbage Collection for Distributed Log-Structured Storage Systems in ByteDance"
description: "FAST 2026 · Cloud Technologies II · 第 493–508 页"
tags:
  - "FAST2026"
  - "Cloud Technologies II"
---

# Discard-Based Garbage Collection for Distributed Log-Structured Storage Systems in ByteDance

**中文标题**：字节跳动分布式日志结构存储系统中基于 Discard 的垃圾回收

**Session**：Cloud Technologies II · 2026-02-26 09:00–10:20 · Chair：Uday Kiran Jonnala（Dell Technologies）

**作者**：Runhua Bian, ByteDance and Tsinghua University; Liqiang Zhang, Jinxin Liu, Jiacheng Zhang, Jianong Zhong, and Jiahao Gu, ByteDance; Hao Guo, Tsinghua University; Zhihong Guo, Yunhao Li, Fenghao Zhang, Jiangkun Zhao, Yangming Chen, and Guojun Li, ByteDance; Ruwen Fan, Tsinghua University; Haijia Shen, Chengyu Dong, Yao Wang, and Rui Shi, ByteDance; Jiwu Shu and Youyou Lu, Tsinghua University

**会议**：FAST 2026 · Santa Clara, CA · 第 493–508 页

**论文类型**：Deployed-Systems Paper

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/bian](https://www.usenix.org/conference/fast26/presentation/bian)

**论文 PDF**：[fast26-bian.pdf](https://www.usenix.org/system/files/fast26-bian.pdf)

---

## 英文摘要

ByteStore is a distributed append-only storage system that serves as the foundational storage layer of the ByteDance infrastructure. Initially, storage services on ByteStore use compaction for garbage collection (GC). Additional writes induced by compaction and the SSD space occupied by stale data result in millions of dollars in extra Total Cost of Ownership (TCO) per month. Aggressive compaction releases the SSD space, but at the cost of more write operations and faster SSD wear, thus failing to reduce TCO.

Based on our analysis of the traces from the block storage service (ByteDrive) deployed on ByteStore, we propose DisCoGC, a Discard-and-Compaction combined Garbage Collection scheme, which employs a discard mechanism to reclaim the space occupied by stale data without moving valid data. Production cluster metrics monitor and offline experiments demonstrate that DisCoGC achieves approximately 20% reduction in TCO, without sacrificing performance.

## 中文摘要

ByteStore 是一个分布式追加写存储系统，作为字节跳动基础设施的基础存储层。最初，ByteStore 上的存储服务使用 compaction 进行垃圾回收（GC）。compaction 引入的额外写入以及陈旧数据占用的 SSD 空间，导致每月数百万美元的额外总拥有成本（TCO）。激进的 compaction 可以释放 SSD 空间，但代价是更多写操作和更快的 SSD 磨损，因而无法降低 TCO。

基于对部署在 ByteStore 上的块存储服务（ByteDrive）跟踪数据的分析，我们提出 DisCoGC，一种 Discard 与 Compaction 相结合的垃圾回收方案。它采用 discard 机制回收陈旧数据占用的空间，而无需移动有效数据。生产集群指标监控和离线实验表明，DisCoGC 在约 20% 降低 TCO 的同时不牺牲性能。
