---
title: "Baleen: ML Admission & Prefetching for Flash Caches"
description: "FAST 2024 · AI and Storage · 第 347–372 页"
tags:
  - "FAST2024"
  - "AI and Storage"
---

# Baleen: ML Admission & Prefetching for Flash Caches

**中文标题**：Baleen：面向闪存缓存的机器学习准入与预取

**Session**：AI and Storage · 2024-02-29 10:45–12:00 · Chair：Patrick P. C. Lee（The Chinese University of Hong Kong (CUHK)）

**作者**：Daniel Lin-Kit Wong, Carnegie Mellon University; Hao Wu, Meta; Carson Molder, UT Austin; Sathya Gunasekar, Jimmy Lu, Snehal Khandkar, and Abhinav Sharma, Meta; Daniel S. Berger, Microsoft and University of Washington; Nathan Beckmann and Gregory R. Ganger, Carnegie Mellon University

**会议**：FAST 2024 · Santa Clara, CA · 第 347–372 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/wong](https://www.usenix.org/conference/fast24/presentation/wong)

**论文 PDF**：[fast24-wong.pdf](https://www.usenix.org/system/files/fast24-wong.pdf)

---

## 英文摘要

Flash caches are used to reduce peak backend load for throughput-constrained data center services, reducing the total number of backend servers required. Bulk storage systems are a large-scale example, backed by high-capacity but low-throughput hard disks, and using flash caches to provide a more cost-effective storage layer underlying everything from blobstores to data warehouses.

However, flash caches must address the limited write endurance of flash by limiting the long-term average flash write rate to avoid premature wearout. To do so, most flash caches must use admission policies to filter cache insertions and maximize the workload-reduction value of each flash write.

The Baleen flash cache uses coordinated ML admission and prefetching to reduce peak backend load. After learning painful lessons with our early ML policy attempts, we exploit a new cache residency model (which we call *episodes*) to guide model training. We focus on optimizing for an end-to-end system metric (*Disk-head Time*) that measures backend load more accurately than IO miss rate or byte miss rate. Evaluation using Meta traces from seven storage clusters shows that Baleen reduces *Peak Disk-head Time* (and hence the number of backend hard disks required) by 12% over state-of-the-art policies for a fixed flash write rate constraint. Baleen-TCO, which chooses an optimal flash write rate, reduces our estimated total cost of ownership (TCO) by 17%. Code and traces are available at [https://www.pdl.cmu.edu/CILES/](https://www.pdl.cmu.edu/CILES/).

## 中文摘要

闪存缓存用于降低受吞吐量约束的数据中心服务的峰值后端负载，从而减少所需的后端服务器总数。批量存储系统是一个大规模示例，其后端是高容量但低吞吐量的硬盘，并使用闪存缓存为从对象存储到数据仓库的各种系统提供更具成本效益的存储层。

然而，闪存缓存必须应对闪存有限的写耐久性，通过限制长期平均闪存写入速率来避免过早磨损。为此，大多数闪存缓存必须使用准入策略来过滤缓存插入，并最大化每次闪存写入的工作负载削减价值。

Baleen 闪存缓存使用协同的机器学习准入与预取来降低峰值后端负载。在早期机器学习策略尝试中吸取痛苦教训后，我们利用一种新的缓存驻留模型（我们称之为 *episodes*）来指导模型训练。我们专注于优化端到端系统指标（*Disk-head Time*），它比 IO 缺失率或字节缺失率更能准确衡量后端负载。使用来自七个存储集群的 Meta 跟踪数据进行评估表明，在固定闪存写入速率约束下，与最先进策略相比，Baleen 将 *Peak Disk-head Time*（以及所需后端硬盘数量）降低 12%。Baleen-TCO 会选择最优闪存写入速率，将我们估计的总拥有成本（TCO）降低 17%。代码和跟踪数据可在 [https://www.pdl.cmu.edu/CILES/](https://www.pdl.cmu.edu/CILES/) 获取。
