---
title: "Cache-Centric Multi-Resource Allocation for Storage Services"
description: "FAST 2026 · OS · 第 675–690 页"
tags:
  - "FAST2026"
  - "OS"
---

# Cache-Centric Multi-Resource Allocation for Storage Services

**中文标题**：面向存储服务的以缓存为中心的多资源分配

**Session**：OS · 2026-02-26 15:50–17:10 · Chair：Yu Liang（ETH Zurich）

**作者**：Chenhao Ye, Shawn (Wanxiang) Zhong, Andrea C. Arpaci-Dusseau, and Remzi H. Arpaci-Dusseau, University of Wisconsin–Madison

**会议**：FAST 2026 · Santa Clara, CA · 第 675–690 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/ye](https://www.usenix.org/conference/fast26/presentation/ye)

**论文 PDF**：[fast26-ye.pdf](https://www.usenix.org/system/files/fast26-ye.pdf)

---

## 英文摘要

We present HARE, a cache-centric multi-resource allocation algorithm for storage services. HARE introduces a holistic allocation model that captures the demand correlation between cache size and other resources (e.g., I/O, network), and uses a novel two-phase harvest/redistribute method to optimize resource allocation across tenants, maximizing the throughput of each while maintaining fairness. To demonstrate that HARE is widely applicable, we built two systems. The first, HopperKV, is a cloud-native key-value store that modifies Redis to cache data from DynamoDB. The second, BunnyFS, is a microkernel-style local filesystem for NVMe SSDs. Our evaluation shows that HARE is effective for multi-resource allocation in storage. Both systems are scalable and adaptive: HopperKV achieves up to a 1.9x performance improvement, and BunnyFS achieves up to 1.4x.

## 中文摘要

我们提出 HARE，一种以缓存为中心的存储服务多资源分配算法。HARE 引入一种整体分配模型，刻画缓存大小与其他资源（例如 I/O、网络）之间的需求相关性，并使用一种新颖的两阶段收割/再分配方法来优化跨租户的资源分配，在保持公平性的同时最大化每个租户的吞吐量。为证明 HARE 具有广泛适用性，我们构建了两个系统。第一个是 HopperKV，一个云原生键值存储，它修改 Redis 以缓存来自 DynamoDB 的数据。第二个是 BunnyFS，一个面向 NVMe SSD 的微内核风格本地文件系统。我们的评估表明，HARE 在存储多资源分配中十分有效。两个系统都具有可扩展性和自适应性：HopperKV 取得最高 1.9 倍的性能提升，BunnyFS 取得最高 1.4 倍的提升。
