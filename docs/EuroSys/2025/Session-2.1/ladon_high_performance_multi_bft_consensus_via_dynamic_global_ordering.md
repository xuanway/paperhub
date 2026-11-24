---
title: "Ladon: High-Performance Multi-BFT Consensus via Dynamic Global Ordering"
description: "EuroSys 2025 · Fault Tolerance and Consensus · Hanzheng Lyu (University of British Columbia), Shaokang Xie (Southern University"
tags:
  - "EuroSys2025"
  - "Fault Tolerance and Consensus"
---

# Ladon: High-Performance Multi-BFT Consensus via Dynamic Global Ordering

**中文标题：** 通过动态全局排序实现高性能多 BFT 共识

**所属 Session：** [Session 2.1: Fault Tolerance and Consensus](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Fault Tolerance and Consensus。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Fault Tolerance and Consensus</p>
</div>

**作者**：Hanzheng Lyu (University of British Columbia), Shaokang Xie (Southern University of Science and Technology), Jianyu Niu (Southern University of Science and Technology), Chen Feng (University of British Columbia), Yinqian Zhang (Southern University of Science and Technology), Ivan Beschastnikh (University of British Columbia)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696102)

## 英文摘要

Multi-BFT consensus runs multiple leader-based consensus instances in parallel, circumventing the leader bottleneck of a single instance. However, it contains an Achilles’ heel: the need to globally order output blocks across instances. Deriving this global ordering is challenging because it must cope with different rates at which blocks are produced by instances. Prior Multi-BFT designs assign each block a global index before creation, leading to poor performance.

We propose Ladon, a high-performance Multi-BFT protocol that allows varying instance block rates. Our key idea is to order blocks across instances dynamically, which eliminates blocking on slow instances. We achieve dynamic global ordering by assigning monotonic ranks to blocks. We pipeline rank coordination with the consensus process to reduce protocol overhead and combine aggregate signatures with rank information to reduce message complexity. Ladon’s dynamic ordering enables blocks to be globally ordered according to their generation, which respects inter-block causality. We implemented and evaluated Ladon by integrating it with both PBFT and HotStuff protocols. Our evaluation shows that Ladon-PBFT (resp., Ladon-HotStuff) improves the peak throughput of the prior art by ≈ 8× (resp., 2×) and reduces latency by ≈ 62% (resp., 23%), when deployed with one straggling replica (out of 128 replicas) in a WAN setting.

## 中文摘要

多 BFT 共识并行运行多个基于领导者的共识实例，从而绕开单个实例的领导者瓶颈。然而它有一个致命弱点：需要跨实例对输出区块进行全局排序。推导这种全局排序颇具挑战，因为它必须应对各实例产出区块速率不同的问题。此前的多 BFT 设计在区块创建之前就为其分配全局索引，导致性能不佳。

我们提出 Ladon，一种允许各实例区块速率不同的高性能多 BFT 协议。其核心思想是动态地对跨实例的区块排序，从而消除对慢实例的阻塞。我们通过为区块分配单调递增的秩来实现动态全局排序。我们将秩协调与共识过程流水线化以减少协议开销，并将聚合签名与秩信息结合以降低消息复杂度。Ladon 的动态排序使区块能够按其生成顺序进行全局排序，从而尊重区块间的因果关系。我们将 Ladon 与 PBFT 和 HotStuff 协议集成，并对其进行了实现与评估。评估表明，在广域网环境下、128 个副本中有一个落后副本时，Ladon-PBFT（相应地，Ladon-HotStuff）相比此前工作将峰值吞吐提升约 8 倍（相应地，2 倍），并将延迟降低约 62%（相应地，23%）。

**英文关键词：** Multi-BFT consensus, Straggler nodes, Dynamic global ordering, Performance

**中文关键词：** 多 BFT 共识、落后节点、动态全局排序、性能

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
