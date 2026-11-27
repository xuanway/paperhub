---
title: "PhasedStore: Supporting High-performance Write-through Cache-coherence Protocols under TSO"
description: "HPCA 2026 · Cache Coherence and Chiplet Interconnects"
tags:
  - "HPCA2026"
  - "Cache Coherence and Chiplet Interconnects"
---

# PhasedStore: Supporting High-performance Write-through Cache-coherence Protocols under TSO

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Cache Coherence and Chiplet Interconnects。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Cache Coherence and Chiplet Interconnects</p>
</div>

**论文链接**：
**作者**：Burak Ocalan University of Illinois Urbana-Champaign , Chloe Alverti University of Illinois at Urbana-Champaign , Shashwat Jaiswal University of Illinois Urbana-Champaign, USA , Antonis Psistakis University of Illinois Urbana-Champaign , David Koufaty Unaffiliated , Suyash Mahar UC San Diego , Steven Swanson University of California San Diego , Josep Torrellas University of Illinois at Urbana-Champaign
**会议**：HPCA 2026

---

## 中文标题

PhasedStore：在 TSO 下支持高性能写直达缓存一致性协议

## 英文摘要

Current multiprocessors that support the total store order (TSO) memory consistency model invariably use writeback (WB) cache-coherence protocols. When their hardware needs to issue write-through (WT) stores as in uncached operations, their performance may suffer: writes to main memory have to be fully serialized, potentially forcing the program to observe the full latency of round trips to memory. To solve this problem, this paper presents a novel architecture that supports high-performance cache-coherent WT stores under TSO. The architecture, called PhasedStore, extends the store queue in the cores and the directory. Individual WT stores fully overlap with other stores and still satisfy TSO. PhasedStore is useful in environments that require a WT cache-coherence protocol. This can be the case in resilience-critical platforms where node failures should not cause the loss of shared program state, or platforms with CPUs and accelerators where programs follow a producer-consumer pattern. This paper evaluates PhasedStore in the first environment, namely a CXL-based distributed shared-memory platform where shared data in the program uses a WT protocol to enable recovery. Our evaluation shows that PhasedStore is very effective. Compared to using the conventional approach to implement WT under TSO, PhasedStore reduces the average execution time of a set of parallel applications by 1.88x.

## 中文摘要

当前支持全存储序（TSO）内存一致性模型的多处理器无不采用写回（WB）缓存一致性协议。当其硬件需要像非缓存操作那样发出写直达（WT）存储时，性能可能受损：对主存的写必须完全串行化，可能迫使程序承受往返内存的完整时延。为解决该问题，本文提出一种在 TSO 下支持高性能缓存一致 WT 存储的新架构。该架构名为 PhasedStore，扩展了核内的存储队列与目录。单个 WT 存储与其他存储完全重叠，同时仍满足 TSO。PhasedStore 适用于需要 WT 缓存一致性协议的环境，例如韧性至关重要的平台——节点故障不应导致共享程序状态丢失，或同时具备 CPU 与加速器且程序遵循生产者—消费者模式的平台。本文在第一种环境中评估 PhasedStore，即基于 CXL 的分布式共享内存平台，其中程序中的共享数据采用 WT 协议以支持恢复。评估表明 PhasedStore 十分有效：与在 TSO 下实现 WT 的传统方法相比，PhasedStore 将一组并行应用的平均执行时间缩短了 1.88 倍。
