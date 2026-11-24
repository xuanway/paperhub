---
title: "IONIA: High-Performance Replication for Modern Disk-based KV Stores"
description: "FAST 2024 · Key-Value Systems · 第 225–242 页"
tags:
  - "FAST2024"
  - "Key-Value Systems"
---

# IONIA: High-Performance Replication for Modern Disk-based KV Stores

**中文标题**：IONIA：面向现代基于磁盘的 KV 存储的高性能复制

**Session**：Key-Value Systems · 2024-02-28 14:00–15:40 · Chair：Angela Demke Brown（University of Toronto）

**作者**：Yi Xu, University of California, Berkeley; Henry Zhu, University of Illinois Urbana-Champaign; Prashant Pandey, University of Utah; Alex Conway, Cornell Tech and VMware Research; Rob Johnson, VMware Research; Aishwarya Ganesan and Ramnatthan Alagappan, University of Illinois Urbana-Champaign and VMware Research

**会议**：FAST 2024 · Santa Clara, CA · 第 225–242 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/xu](https://www.usenix.org/conference/fast24/presentation/xu)

**论文 PDF**：[fast24-xu.pdf](https://www.usenix.org/system/files/fast24-xu.pdf)

---

## 英文摘要

We introduce IONIA, a novel replication protocol tailored for modern SSD-based write-optimized key-value (WO-KV) stores. Unlike existing replication approaches, IONIA carefully exploits the unique characteristics of SSD-based WO-KV stores. First, it exploits their interface characteristics to defer parallel execution to the background, enabling high-throughput yet one round trip (RTT) writes. IONIA also exploits SSD-based KV-stores’ performance characteristics to scalably read at any replica without enforcing writes to all replicas, thus providing scalability without compromising write availability; further, it does so while completing most reads in 1RTT. IONIA is the first protocol to achieve these properties, and it does so through its storage-aware design. We evaluate IONIA extensively to show that it achieves the above properties under a variety of workloads.

## 中文摘要

我们提出 IONIA，一种面向现代基于 SSD 的写优化键值（WO-KV）存储的新型复制协议。与现有复制方法不同，IONIA 精心利用基于 SSD 的 WO-KV 存储的独特特性。首先，它利用其接口特性将并行执行推迟到后台，从而实现高吞吐量且仅需一次往返（RTT）的写入。IONIA 还利用基于 SSD 的 KV 存储的性能特性，可在任意副本上可扩展地读取，而无需强制写入所有副本，从而在不损害写可用性的情况下提供可扩展性；此外，它在完成大多数读取时仅需 1RTT。IONIA 是首个实现这些特性的协议，这得益于其存储感知设计。我们广泛评估 IONIA，表明其在多种负载下均能实现上述特性。
