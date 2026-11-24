---
title: "DRBoost: Boosting Degraded Read Performance in MSR-Coded Storage Clusters"
description: "FAST 2026 · Integrity · 第 613–630 页"
tags:
  - "FAST2026"
  - "Integrity"
---

# DRBoost: Boosting Degraded Read Performance in MSR-Coded Storage Clusters

**中文标题**：DRBoost：提升 MSR 编码存储集群的降级读性能

**Session**：Integrity · 2026-02-26 14:00–15:20 · Chair：Gala Yadgar（Technion—Israel Institute of Technology）

**作者**：Xiao Niu, Guangyan Zhang, Zhiyue Li, and Sijie Cai, Tsinghua University

**会议**：FAST 2026 · Santa Clara, CA · 第 613–630 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/niu](https://www.usenix.org/conference/fast26/presentation/niu)

**论文 PDF**：[fast26-niu.pdf](https://www.usenix.org/system/files/fast26-niu.pdf)

---

## 英文摘要

Minimum Storage Regenerating (MSR) codes have strong potential for building efficient and reliable storage systems due to their excellent fault tolerance and low repair bandwidth. However, to meet MSR code constraints and optimize storage performance, systems often adopt large chunk sizes. This leads to significant I/O amplification during degraded reads, as entire chunks must be reconstructed to access a single object.

In this paper, we propose DRBoost, an approach that boosts degraded read performance in MSR-coded storage clusters by reducing repair bandwidth and eliminating access fragmentation for healthy data. DRBoost introduces three key techniques: (1) a partial-chunk reconstruction algorithm that reduces repair bandwidth by leveraging two forms of data reuse; (2) a reconstruction-friendly coding layout that improves reuse efficiency and accommodates objects of diverse sizes; and (3) a fragmentation-free storage layout that avoids unnecessary request splitting. Extensive experiments under various conditions and workloads show that DRBoost reduces degraded read latency by one to two orders of magnitude, significantly improving system responsiveness.

## 中文摘要

最小存储再生（MSR）码凭借优异的容错能力和低修复带宽，在构建高效可靠的存储系统方面具有很大潜力。然而，为满足 MSR 码约束并优化存储性能，系统通常采用较大的块大小。这导致降级读期间出现显著的 I/O 放大，因为必须重建整个块才能访问单个对象。

本文提出 DRBoost，一种通过降低修复带宽并消除健康数据的访问碎片化来提升 MSR 编码存储集群降级读性能的方法。DRBoost 引入三项关键技术：(1) 一种部分块重建算法，利用两种数据复用形式降低修复带宽；(2) 一种对重建友好的编码布局，提高复用效率并适应不同大小的对象；(3) 一种无碎片化的存储布局，避免不必要的请求拆分。在各种条件和负载下的大量实验表明，DRBoost 将降级读延迟降低一到两个数量级，显著提升系统响应能力。
