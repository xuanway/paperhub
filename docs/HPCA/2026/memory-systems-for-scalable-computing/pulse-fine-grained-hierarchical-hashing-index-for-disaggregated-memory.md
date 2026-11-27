---
title: "Pulse: Fine-Grained Hierarchical Hashing Index for Disaggregated Memory"
description: "HPCA 2026 · Memory Systems for Scalable Computing"
tags:
  - "HPCA2026"
  - "Memory Systems for Scalable Computing"
---

# Pulse: Fine-Grained Hierarchical Hashing Index for Disaggregated Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Memory Systems for Scalable Computing。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Memory Systems for Scalable Computing</p>
</div>

**论文链接**：
**作者**：Guangyang Deng Xiamen University , Zixiang Yu Xiamen University , Zhirong Shen Xiamen University , Qiangsheng Su Xiamen University , Jiwu Shu Xiamen University
**会议**：HPCA 2026

---

## 中文标题

Pulse：面向解耦内存的细粒度分层哈希索引

## 英文摘要

By decoupling compute and memory resources into independent pools that are provisioned and managed separately, disaggregated memory (DM) is promising to break the scaling constraints for memory systems and improve resource utilization. However, it also comes with a new challenge to design a high-performance hashing index to manage the vast memory pool with weak computing power. In this paper, we reconsider this problem and find that existing hashing indexes for DM still experience two fundamental yet unresolved limitations: (i) amplifying traffic under high insertion concurrency, and (ii) introducing significantly high insertion latency, stemming mainly from the directory synchronization and item relocation in resizing process. We resolve the above limitations by designing Pulse, a fine-grained hierarchical hashing index for DM. Pulse comprises the following three design primitives. It proposes a multi-level index structure, which breaks the conventional flat directory into multiple sub-directories that are organized hierarchically, achieving fine-grained directory synchronization. Pulse also maintains a small portion of hashed keys in the memory pool, which aids in item relocation during resizing, thereby reducing resizing traffic and promising system stability. Pulse finally exploits operation parallelism by tailoring the doorbell batching mechanism with selective signaling. We conduct extensive experiments using a variety of benchmarks, showing that Pulse can improve 3.46× of the throughput and reduce 76.3% of the tail latency compared to state-of-the-art hashing indexes.

## 中文摘要

通过将计算与内存资源解耦为独立供给、独立管理的资源池，解耦内存（DM）有望突破内存系统的扩展限制并提升资源利用率。然而，在算力较弱的庞大内存池上设计高性能哈希索引也带来新的挑战。本文重新审视该问题，发现现有面向 DM 的哈希索引仍存在两个根本性且尚未解决的局限：（i）在高并发插入下放大流量；（ii）引入显著偏高的插入时延，主要源于扩容过程中的目录同步与条目迁移。为此我们设计了 Pulse，一种面向 DM 的细粒度分层哈希索引，包含三项设计要素：提出多级索引结构，把传统扁平目录拆分为分层组织的多个子目录，实现细粒度的目录同步；在内存池中保留少量哈希键，辅助扩容时的条目迁移，从而减少扩容流量并提升系统稳定性；利用门铃批处理机制并配合选择性通知，挖掘操作级并行性。我们使用多种基准进行了大量实验，结果表明，相比最先进的哈希索引，Pulse 可将吞吐提升 3.46 倍，并将尾时延降低 76.3%。
