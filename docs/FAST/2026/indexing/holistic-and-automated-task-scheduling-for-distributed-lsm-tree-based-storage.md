---
title: "Holistic and Automated Task Scheduling for Distributed LSM-tree-based Storage"
description: "FAST 2026 · Indexing · 第 203–220 页"
tags:
  - "FAST2026"
  - "Indexing"
---

# Holistic and Automated Task Scheduling for Distributed LSM-tree-based Storage

**中文标题**：面向分布式 LSM-tree 存储的整体自动化任务调度

**Session**：Indexing · 2026-02-24 14:00–15:40 · Chair：Zhichao Cao（Arizona State University）

**作者**：Yuanming Ren, Siyuan Sheng, and Zhang Cao, The Chinese University of Hong Kong; Yongkun Li, University of Science and Technology of China; Patrick P. C. Lee, The Chinese University of Hong Kong

**会议**：FAST 2026 · Santa Clara, CA · 第 203–220 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/ren](https://www.usenix.org/conference/fast26/presentation/ren)

**论文 PDF**：[fast26-ren.pdf](https://www.usenix.org/system/files/fast26-ren.pdf)

---

## 英文摘要

Mitigating latency fluctuations for distributed key-value (KV) stores is critical, yet it is often hindered by the tight coupling of foreground and background tasks related to data distribution and storage management. Using Cassandra, a widely deployed distributed LSM-tree-based KV store, as a case study, we observe that foreground read tasks are often interfered with by background compaction tasks, yet compaction tasks are critical for achieving high read performance. We propose HATS, a holistic and automated task scheduling framework that judiciously co-schedules read and compaction tasks, so as to mitigate latency fluctuations and achieve load balancing. HATS features coarse-grained and fine-grained replica selection for reads as well as adaptive rate control for compaction. We implement HATS atop Cassandra and demonstrate its improved latency and throughput performance over state-of-the-art distributed LSM-tree-based KV stores.

## 中文摘要

缓解分布式键值（KV）存储的延迟波动至关重要，但这一目标常常受到与数据分布和存储管理相关的前台任务与后台任务紧耦合的阻碍。我们以 Cassandra（一种广泛部署的分布式 LSM-tree KV 存储）为案例进行研究，观察到前台读任务经常受到后台 compaction（合并）任务的干扰，而 compaction 任务对于实现高读性能又至关重要。我们提出 HATS，一个整体且自动化的任务调度框架，它审慎地协同调度读任务和 compaction 任务，以缓解延迟波动并实现负载均衡。HATS 具有面向读的粗粒度和细粒度副本选择，以及面向 compaction 的自适应速率控制。我们在 Cassandra 之上实现 HATS，并证明其相较于最先进的分布式 LSM-tree KV 存储具有更优的延迟和吞吐性能。
