---
title: "LRM-GPU: Alleviating Synchronization Overhead for Multi-Chiplet GPU Architecture"
description: "HPCA 2026 · GPU Memory Management and Multi-Chiplet Systems"
tags:
  - "HPCA2026"
  - "GPU Memory Management and Multi-Chiplet Systems"
---

# LRM-GPU: Alleviating Synchronization Overhead for Multi-Chiplet GPU Architecture

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: GPU Memory Management and Multi-Chiplet Systems。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · GPU Memory Management and Multi-Chiplet Systems</p>
</div>

**论文链接**：
**作者**：Baiqing Zhong Sun Yat-Sen University , Zhirong Ye Sun Yat-Sen University , Xiaojie Li Sun Yat-Sen University , Peilin Wang Sun Yat-Sen University , Haiqiu Huang Sun Yat-Sen University , Zhaolin Li Tsinghua University , Zhiyi Yu Sun Yat-sen University , Mingyu Wang Sun Yat-Sen University
**会议**：HPCA 2026

---

## 中文标题

LRM-GPU：缓解多芯粒 GPU 架构的同步开销

## 英文摘要

With the slowdown of process scaling and the advancement of packaging technologies, multi-chiplet GPUs have emerged as a highly promising architecture to improve the scalability of GPU performance further. Moreover, requiring adherence to atomicity and memory consistency models for shared data efficient synchronization is crucial to leverage the performance advantages of the multi-chiplet GPU architecture. However, the memory systems of multi-chiplet GPUs introduce deeper cache hierarchies and increased non-uniformity, both of which significantly exacerbate the overhead of synchronization. Specifically, acquire/release synchronization operations should invalidate/flush caches, an overhead that is significantly increased by the presence of additional cache level, and atomic operations for synchronization performed across chiplets are further impacted by the limited bandwidth of inter-chiplet links. To address these challenges, this paper proposes LRM-GPU to provide efficient synchronization support for multi-chiplet GPUs. In order to reduce the overhead caused by the additional cache level, LRM-GPU leverages lazy release consistency in multi-chiplet GPUs, whereby the additional level of cache only performs coherence actions when the ownership of synchronization variables changes between different chiplets. LRM-GPU also implements a directory in the last-level cache to track the synchronization variables. To mitigate the overhead of atomic operations for inter-chiplet synchronization under limited inter-chiplet bandwidth, LRM-GPU proposes an in-network synchronization atomic merging unit to merge atomic requests across chiplets, thereby reducing the inter-chiplet synchronization traffic of atomic operations. Experimental evaluation demonstrates that, compared with the MCM-GPU, LRM-GPU achieves an average speedup of 1.33×. Moreover, compared with the state-of-the-art work HMG, it also achieves the speedup of 1.22×, reduces 52% of inter-chiplet traffic, and reduces 32% of energy consumption on average.

## 中文摘要

随着工艺缩放放缓与封装技术的进步，多芯粒 GPU 已成为进一步提升 GPU 性能可扩展性的极具前景的架构。共享数据的高效同步需遵循原子性与内存一致性模型，这对发挥多芯粒 GPU 架构的性能优势至关重要。然而，多芯粒 GPU 的内存系统带来了更深的缓存层级与更强的不均匀性，二者都显著加剧了同步开销：获取与释放同步操作需使缓存失效或刷新，额外缓存层级的存在使该开销大幅增加；跨芯粒执行的同步原子操作还进一步受限于芯粒间链路的有限带宽。为应对这些挑战，本文提出 LRM-GPU，为多芯粒 GPU 提供高效的同步支持。为降低额外缓存层级带来的开销，LRM-GPU 在多芯粒 GPU 中采用惰性释放一致性，使额外的缓存层级仅在同步变量的所有权于不同芯粒间转移时才执行一致性操作；并在末级缓存中实现目录以跟踪同步变量。为缓解芯粒间带宽有限时跨芯粒同步原子操作的开销，LRM-GPU 提出网内同步原子合并单元，将跨芯粒的原子请求合并，从而减少原子操作的芯粒间同步流量。实验评估表明，与 MCM-GPU 相比，LRM-GPU 平均取得 1.33 倍的加速比；与最先进工作 HMG 相比也取得 1.22 倍的加速比，并将芯粒间流量减少 52%、平均能耗降低 32%。
