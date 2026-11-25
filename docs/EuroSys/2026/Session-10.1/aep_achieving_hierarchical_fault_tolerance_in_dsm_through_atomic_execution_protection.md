---
title: "AEP: Achieving Hierarchical Fault Tolerance in DSM Through Atomic Execution Protection"
description: "EuroSys 2026 · Distributed Systems and Multicore · Zixuan Wang (Huazhong University of Science and Technology), Qi Wu (Huazhong Uni"
tags:
  - "EuroSys2026"
  - "Distributed Systems and Multicore"
---

# AEP: Achieving Hierarchical Fault Tolerance in DSM Through Atomic Execution Protection

**中文标题：** AEP：通过原子执行保护在 DSM 中实现层次化容错

**所属 Session：** [Session 10.1: Distributed Systems and Multicore](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Systems and Multicore。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Systems and Multicore</p>
</div>

**作者**：Zixuan Wang (Huazhong University of Science and Technology), Qi Wu (Huazhong University of Science and Technology), Hang Huang (Huazhong University of Science and Technology), Jia Rao (The University of Texas at Arlington), Hui Lu (The University of Texas at Arlington), Hao Fan (Huazhong University of Science and Technology), Zhuo Huang (Huazhong University of Science and Technology), Song Wu (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803602)

## 英文摘要

Recent advances in CXL 3.0 have revitalized Distributed Shared Memory (DSM), enabling zero-copy sharing across machine nodes at near-NUMA latency and making shared-memory communication practical for distributed applications. However, DSM memory allocators remain vulnerable to partial failures: client crashes during critical, non-atomic memory operations can corrupt metadata and stall the entire system. Existing solutions either block all clients during recovery or impose heavy runtime overhead due to distributed fault-tolerance protocols. We propose Atomic Execution Protection (AEP), a kernel-assisted fault tolerance mechanism that guarantees atomic completion of user-space critical operations by deferring termination until protected regions finish. AEP tolerates intra-node partial failures without costly distributed coordination. To extend beyond a single node, we further design AEP-DSM, a hierarchical DSM allocator that combines AEP-protected node-level allocators with cross-node coordination. Our Linux AEP prototype integrated with a cross-node DSM consistency protocol (CXL-SHM) achieves near-native local performance and improves throughput by up to 13.3x over state-of-the-art DSM allocators.

## 中文摘要

CXL 3.0 的最新进展使分布式共享内存（DSM）重新焕发活力，能够在机器节点之间以接近 NUMA 的延迟实现零拷贝共享，使共享内存通信对分布式应用变得实用。然而，DSM 内存分配器仍易受部分故障影响：客户端在关键的非原子内存操作期间崩溃可能破坏元数据，并使整个系统停滞。现有方案要么在恢复期间阻塞所有客户端，要么因分布式容错协议而带来沉重的运行时开销。我们提出原子执行保护（AEP），一种内核辅助的容错机制，通过将终止推迟到受保护区域执行完毕，保证用户空间关键操作的原子完成。AEP 无需昂贵的分布式协调即可容忍节点内的部分故障。为扩展到单节点之外，我们进一步设计了 AEP-DSM，一个层次化的 DSM 分配器，将 AEP 保护的节点级分配器与跨节点协调相结合。我们与跨节点 DSM 一致性协议（CXL-SHM）集成实现的 Linux AEP 原型达到了接近原生的本地性能，并相比最先进的 DSM 分配器将吞吐量最高提升 13.3 倍。

**英文关键词：** Operating Systems, Distributed Shared Memory, CXL, Memory management

**中文关键词：** 操作系统、分布式共享内存、CXL、内存管理

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
