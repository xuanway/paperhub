---
title: "FicusDB: Scalable Multi-Versioned Authenticated Archival Storage"
description: "EuroSys 2026 · Distributed Consensus, Blockchain & Storage · Hongbo Zhang (Cornell University), Maofan \"Ted\" Yin (UC Santa Barbara), Robbert "
tags:
  - "EuroSys2026"
  - "Distributed Consensus, Blockchain & Storage"
---

# FicusDB: Scalable Multi-Versioned Authenticated Archival Storage

**中文标题：** FicusDB：可扩展的多版本可认证归档存储

**所属 Session：** [Session 4.2: Distributed Consensus, Blockchain & Storage](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Consensus, Blockchain & Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Consensus, Blockchain & Storage</p>
</div>

**作者**：Hongbo Zhang (Cornell University), Maofan "Ted" Yin (UC Santa Barbara), Robbert van Renesse (Cornell University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803601)

## 英文摘要

As consensus protocols scale, storage has become the dominant bottleneck in modern blockchains. Systems must maintain historical versions, generate integrity proofs, and sustain high throughput as state grows. Prior work often redesigns the authenticated data structure (ADS), but such changes sacrifice compatibility and require disruptive hard forks. We take the complementary approach: redesigning the storage layer while preserving the existing ADS interface.

We present FicusDB, a log-structured archival storage system for copy-on-write tries. FicusDB introduces three innovations: (i) append-only logs with location-based identifiers that eliminate compaction, (ii) a CoW-aware tree-structured cache that avoids LRU thrashing, and (iii) the Aggregated Hash Array (AHA), which decouples proof correctness from storage durability by treating child-hash arrays as verifiable hints. Together, these techniques cut write amplification, improve read locality, and accelerate proof computation.

On 11.5 million Ethereum blocks (≈1B keys), FicusDB achieves 3.7× higher storage throughput and a 66% smaller footprint compared to Geth, while remaining fully compatible. More broadly, FicusDB shows that substantial performance gains are possible without changing ADS semantics, reframing persistence itself as a locus of innovation for blockchain scalability.

## 中文摘要

随着共识协议的可扩展性提升，存储已成为现代区块链的主要瓶颈。系统必须维护历史版本、生成完整性证明，并在状态持续增长的同时保持高吞吐。已有工作往往重新设计可认证数据结构（ADS），但此类改动牺牲了兼容性，并需要破坏性的硬分叉。我们采取互补的思路：在保留现有 ADS 接口的前提下重新设计存储层。

我们提出 FicusDB，一个面向写时复制（CoW）trie 的日志结构归档存储系统。FicusDB 引入三项创新：(i) 采用基于位置的标识符的追加式日志，从而消除压缩；(ii) 感知 CoW 的树形结构缓存，避免 LRU 抖动；(iii) 聚合哈希数组（AHA），通过将子哈希数组视为可验证提示，将证明正确性与存储持久性解耦。这些技术共同降低了写放大、改善了读局部性，并加速了证明计算。

在 1150 万个以太坊区块（约 10 亿个键）上，与 Geth 相比，FicusDB 的存储吞吐量提高 3.7 倍、占用空间缩小 66%，同时保持完全兼容。更广泛地说，FicusDB 表明无需改变 ADS 语义也能获得显著的性能提升，从而将持久化本身重新定位为区块链可扩展性的创新切入点。

**英文关键词：** blockchain storage; authenticated storage; copy-on-write data structures; structure-aware caching

**中文关键词：** 区块链存储、可认证存储、写时复制数据结构、结构感知缓存

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
