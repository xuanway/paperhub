---
title: "Getting the MOST out of your Storage Hierarchy with Mirror-Optimized Storage Tiering"
description: "FAST 2026 · Tiering, Mobile, and SSDs · 第 561–578 页"
tags:
  - "FAST2026"
  - "Tiering, Mobile, and SSDs"
---

# Getting the MOST out of your Storage Hierarchy with Mirror-Optimized Storage Tiering

**中文标题**：借助镜像优化分层（MOST）充分利用存储层次结构

**Session**：Tiering, Mobile, and SSDs · 2026-02-26 10:50–12:30 · Chair：Vasily Tarasov（IBM Research）

**作者**：Kaiwei Tu, University of Wisconsin–Madison; Kan Wu, Google; Andrea C. Arpaci-Dusseau and Remzi H. Arpaci-Dusseau, University of Wisconsin–Madison

**会议**：FAST 2026 · Santa Clara, CA · 第 561–578 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/tu](https://www.usenix.org/conference/fast26/presentation/tu)

**论文 PDF**：[fast26-tu.pdf](https://www.usenix.org/system/files/fast26-tu.pdf)

---

## 英文摘要

We present Mirror-Optimized Storage Tiering (MOST), a novel tiering-based approach optimized for modern storage hierarchies. The key idea of MOST is to combine the load-balancing advantages of mirroring with the space-efficiency advantages of tiering. Specifically, MOST dynamically mirrors a small amount of hot data across storage tiers to efficiently balance load, avoiding costly migrations. As a result, MOST is as space-efficient as classic tiering while achieving better bandwidth utilization under I/O-intensive workloads. We implement MOST in Cerberus, a user-level storage management layer based on CacheLib. We show the efficacy of Cerberus through a comprehensive empirical study: across a range of static and dynamic workloads, Cerberus achieves better throughput than competing approaches on modern storage hierarchies especially under I/O-intensive and dynamic workloads.

## 中文摘要

我们提出镜像优化存储分层（MOST），一种面向现代存储层次结构优化的新型分层方法。MOST 的核心思想是将镜像的负载均衡优势与分层的空间效率优势相结合。具体而言，MOST 将少量热数据跨存储层动态镜像，以高效均衡负载，避免代价高昂的迁移。因此，MOST 在空间效率上与经典分层相当，同时在 I/O 密集型负载下实现更好的带宽利用率。我们在 Cerberus 中实现 MOST，这是一个基于 CacheLib 的用户级存储管理层。我们通过全面的实证研究展示 Cerberus 的有效性：在一系列静态和动态负载下，Cerberus 在现代存储层次结构上比竞争方案取得更高吞吐量，尤其是在 I/O 密集型和动态负载下。
