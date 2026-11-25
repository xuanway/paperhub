---
title: "Towards Improving Throughput and Scalability of DAG-based BFT SMR"
description: "EuroSys 2026 · Distributed Consensus, Blockchain & Storage · Nibesh Shrestha (Supra Research), Aniket Kate (Supra Research / Purdue Universit"
tags:
  - "EuroSys2026"
  - "Distributed Consensus, Blockchain & Storage"
---

# Towards Improving Throughput and Scalability of DAG-based BFT SMR

**中文标题：** 提升基于 DAG 的 BFT SMR 的吞吐量与可扩展性

**所属 Session：** [Session 4.2: Distributed Consensus, Blockchain & Storage](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Consensus, Blockchain & Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Consensus, Blockchain & Storage</p>
</div>

**作者**：Nibesh Shrestha (Supra Research), Aniket Kate (Supra Research / Purdue University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769363)

## 英文摘要

Directed Acyclic Graph (DAG)-based BFT consensus protocols often suffer from limited throughput and scalability due to bandwidth-intensive data replication to all participants. However, it is sufficient to replicate data to a smaller subcommittee of parties that holds an honest majority with high probability.

In this work, we introduce tribe-assisted reliable broadcast, a novel primitive that ensures reliable broadcast (RBC) properties within a smaller honest-majority sub-committee (referred to as a clan) drawn from the entire network, called the tribe. Leveraging this primitive, we develop two efficient DAG-based BFT consensus protocols. First, we present a single-clan protocol, in which a single clan is elected from the tribe, and data is disseminated exclusively to this designated clan using tribe-assisted RBC. We then extend this design to a multi-clan setting, where multiple clans are elected and data is distributed within each respective clan via the same mechanism. Experimental results demonstrate that both protocols offer substantial improvements in throughput and latency over existing DAG-based BFT protocols, even at moderately large scales.

## 中文摘要

基于有向无环图（DAG）的 BFT 共识协议常常因向所有参与者进行带宽密集型的数据复制而导致吞吐量与可扩展性受限。然而，只需将数据复制到一个以高概率持有诚实多数的小型委员会便已足够。

本文提出 tribe 辅助的可靠广播（tribe-assisted reliable broadcast），这是一种新原语，可在从整个网络（称为 tribe）中抽取出的、规模更小的诚实多数子委员会（称为 clan）内保证可靠广播（RBC）的性质。借助该原语，我们设计了两种高效的基于 DAG 的 BFT 共识协议。首先，我们提出单 clan 协议：从 tribe 中选举出一个 clan，并使用 tribe 辅助的 RBC 将数据仅传播给该指定 clan。随后我们将该设计扩展到多 clan 场景：选举多个 clan，并通过同样的机制在各 clan 内部分发数据。实验结果表明，即使在中等规模下，两种协议在吞吐量与延迟方面相较现有基于 DAG 的 BFT 协议均有显著改善。

**英文关键词：** Byzantine Fault Tolerance; DAG-based BFT SMR; Scalable Consensus; Partial Synchrony

**中文关键词：** 拜占庭容错、基于 DAG 的 BFT SMR、可扩展共识、部分同步

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
