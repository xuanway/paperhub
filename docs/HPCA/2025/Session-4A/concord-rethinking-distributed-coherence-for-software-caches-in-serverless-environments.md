---
title: "Concord: Rethinking Distributed Coherence for Software Caches in Serverless Environments"
description: "HPCA 2025 · The Winning System"
tags:
  - "HPCA2025"
  - "The Winning System"
---

# Concord: Rethinking Distributed Coherence for Software Caches in Serverless Environments

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Winning System。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Winning System</p>
</div>

**论文链接**：
**作者**：Jovan Stojkovic (University of Illinois at Urbana-Champaign), Chloe Alverti (University of Illinois at Urbana-Champaign), Alan Andrade (University of Illinois at Urbana-Champaign), Nikoleta Markela Iliakopoulou (University of Illinois at Urbana-Champaign), Hubertus Franke (IBM Research), Tianyin Xu (University of Illinois at Urbana-Champaign), Josep Torrellas (University of Illinois at Urbana-Champaign)
**会议**：HPCA 2025

---

## 中文标题

Concord：重新思考无服务器环境中软件缓存的分布式一致性

## 英文摘要

Costly accesses to global storage substantially limit the performance of serverless functions. To mitigate this overhead, data can be cached in the memory of the nodes where functions are executed. Existing caching schemes either (1) restrict a data item to be cached in a single node, causing frequent remote reads or (2) allow a data item to be cached in multiple nodes concurrently, adding substantial overhead to maintain cache coherence. Unfortunately, current approaches are suboptimal for the access patterns present in serverless workloads, which are characterized by frequent reads to small data items, strong temporal locality, and a small number of nodes that concurrently execute functions of the same application. Driven by these insights, we propose Concord, a distributed software caching system tailored to serverless environments. Concord allows multiple copies of the same data item to be cached in different nodes concurrently, allowing each cache to satisfy local reads. To maintain coherence across software caches, Concord proposes a directory-based distributed coherence protocol. The protocol is inspired by hardware cache coherence, and is enhanced to minimize coherence traffic, reduce contention points, and be robust to node failures and frequent coherence domain changes. Further, with the Concord coherence protocol, we unlock two new capabilities in serverless environments: transactional storage accesses and transparent data-aware function placement. Compared to state-of-the-art severless caching schemes, Concord running on a 16-node cluster speeds-up execution by 2.4× and improves throughput by 1.7×, while using only 6.2MB of otherwise idle application memory (i.e., 4.8% of the total application memory).

## 中文摘要

对全局存储的昂贵访问严重限制了无服务器函数的性能。为缓解这一开销，可以将数据缓存在执行函数的节点内存中。现有的缓存方案要么（1）将数据项限制为只能缓存在单个节点，导致频繁的远程读取；要么（2）允许同一数据项同时缓存在多个节点，但需要为维护缓存一致性付出可观开销。不幸的是，当前方法对无服务器负载中出现的访问模式并非最优，这些模式的特征是对小数据项的频繁读取、强时间局部性，以及并发执行同一应用函数的节点数量较少。基于这些观察，我们提出 Concord，一个为无服务器环境量身定制的分布式软件缓存系统。Concord 允许同一数据项的多个副本同时缓存在不同节点上，使每个缓存都能满足本地读取。为在软件缓存之间维护一致性，Concord 提出基于目录的分布式一致性协议。该协议受硬件缓存一致性启发，并经过增强以最小化一致性流量、减少竞争点，且能耐受节点故障与频繁的一致性域变化。此外借助 Concord 一致性协议，我们在无服务器环境中解锁了两项新能力：事务性存储访问和透明的数据感知函数放置。与最先进的无服务器缓存方案相比，Concord 在 16 节点集群上运行时可带来 2.4 倍的执行加速和 1.7 倍的吞吐提升，同时仅使用 6.2MB 原本空闲的应用内存（即应用总内存的 4.8%）。
