---
title: "Maat: Analyzing and Optimizing Overcharge on Blockchain Storage"
description: "FAST 2025 · Cloud Storage · 把 gas 核算从 opcode 下沉到存储操作，消除共识安全的重复计费，手续费降 32%"
tags:
  - "FAST2025"
  - "Cloud Storage"
  - "blockchain storage"
  - "transaction fee mechanism"
---

# Maat: Analyzing and Optimizing Overcharge on Blockchain Storage

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">以太坊按 opcode 收 gas，与真实存储负载脱节：同一对象在块内被反复访问仍要重复计费。Maat 以存储操作为粒度采集 gas 与访问语义，只用共识保证一致的高层语义推断可省费用，并预分配资源保证跨客户端一致，使手续费降低 32%，每周省 5.6M USD。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Cloud Storage</p>
</div>

**中文标题**：Maat：区块链存储过度收费的分析与优化

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/he](https://www.usenix.org/conference/fast25/presentation/he)

**论文 PDF**：[fast25-he.pdf](https://www.usenix.org/system/files/fast25-he.pdf)

**作者**：Zheyuan He（University of Electronic Science and Technology of China）；Zihao Li（The Hong Kong Polytechnic University）；Ao Qiao、Jingwei Li（University of Electronic Science and Technology of China）；Feng Luo（The Hong Kong Polytechnic University）；Sen Yang（University of Electronic Science and Technology of China）；Gelei Deng（Nanyang Technological University）；Shuwei Song、XiaoSong Zhang、Ting Chen（University of Electronic Science and Technology of China）；Xiapu Luo（The Hong Kong Polytechnic University）

**会议**：FAST 2025 · Santa Clara, CA · 第 123–137 页

**Session**：Cloud Storage · 2025-02-25 14:00–15:20 · Chair：Ming Zhao（Arizona State University）

**所属 Session**：[Cloud Storage](index.md) · [FAST 2025](../index.md)

**关键词**：blockchain storage, transaction fee mechanism, gas, Ethereum, consensus

---

## 英文摘要

Blockchain, such as Ethereum, relies on a transaction fee mechanism (TFM) to allocate the costs of on-chain resources, including storage, network, and computation. However, the inconsistency between the transaction fee and the storage workload results in overcharging issues for users.

In this paper, we present Maat, a tool designed to address these overcharging issues on blockchain storage. Maat employs three key techniques: (i) Fine-grained data collection, which captures detailed information on gas fees at the storage operation level (i.e., the operations interact with blockchain storage), enabling precise tracking of resource usage and charges for identifying overcharges; (ii) Consensus-oriented optimizations, which ensure that fee optimizations are consistent across all blockchain nodes by analyzing high-level storage semantics (e.g., accessing account and slot) of storage operations; and (iii) Resource pre-allocation, which ensures storage operation consistent across heterogeneous nodes and clients via preemptively specifying and allocating necessary resources. Extensive evaluations of Maat on Ethereum reveal a 32% reduction in transaction fees, amounting to 5.6M USD in weekly savings and nearly outperforming the baseline by nearly three times. Additionally, Maat achieves optimizations with a minimal performance overhead of 1.4% in block processing time and a 5.6% increase in memory consumption. Finally, Maat demonstrates its scalability, yielding a 31% reduction in transaction fees on Binance Smart Chain (1.54M USD per week).

## 中文摘要

以太坊等区块链依赖交易费机制（TFM）为链上存储、网络与计算资源分配成本。然而，交易费与实际存储负载之间的不一致，导致用户被过度收费。本文提出 Maat，一种旨在解决区块链存储过度收费问题的工具。Maat 采用三项关键技术：(i) 细粒度数据采集——在存储操作层面（即与区块链存储交互的操作）捕获 gas 费用的详细信息，从而精确追踪资源使用与收费以识别过度收费；(ii) 面向共识的优化——通过分析存储操作的高层存储语义（例如访问账户与槽位），确保费用优化在所有区块链节点间保持一致；(iii) 资源预分配——通过预先指定并分配必要资源，确保异构节点与客户端之间的存储操作一致。在以太坊上的大量评估表明，Maat 使交易费降低 32%，每周节省 5.6M USD，近乎达到基线的三倍；同时，Maat 的优化仅带来 1.4% 的区块处理时间开销与 5.6% 的内存占用增加。最后，Maat 展示了可扩展性：在 Binance Smart Chain 上使交易费降低 31%（每周 1.54M USD）。

## 一句话总结

> 手续费按 opcode 收，真实代价却取决于对象是否已在内存里：把计费下沉到存储操作语义，才能既省费又保持共识一致。

## 研究背景与问题

- 以太坊用交易费机制（TFM）里的 gas 为链上存储、计算与带宽定价，防止海量交易耗尽磁盘 I/O；代价是费用高昂，2023 年以太坊用户共支付 2.4 billion USD 手续费。
- 已有优化各管一段：EIP-4844 用非持久化的 blob 降低费用，SuperStack 优化合约代码生成，EIP-2929 按实际存储访问调整 opcode 价格（如同一交易内重复访问账户从 2,600 gas 降到 100 gas），都没有系统处理存储操作与收费之间的偏差。
- 作者分析 geth、besu、nethermind、erigon 四个客户端实现，归纳出三类过度收费：块内对同一对象的连续访问、跨有限个区块对同一对象的连续访问、重复部署合约。
- 约四个月的以太坊实测显示，这三类问题波及 117M 笔交易（70.4%）与 147M USD 手续费（42.0%）；BSC（Binance Smart Chain）上波及 156M 笔交易（92.8%）与 11M USD（41.7%），而以太坊的 TFM 被 500 多条链复用。

## 核心贡献

- 识别并量化区块链实现中的三类过度收费（overcharge）问题，在以太坊与 BSC 上给出受影响交易比例与费用比例。
- 细粒度数据采集：把 gas 与访问信息对应到存储操作而非 opcode，覆盖 account/slot/bytecode 的 load/store 六种高层语义。
- 共识导向优化：只用区块链共识保证一致的高层语义关系推断优化后的 gas，使所有节点算出相同费用。
- 资源预分配：预先指定客户端参数并预分配内存，保证异构节点与不同客户端上存储操作一致，并为缓存补上 write-ahead log 以支持恢复。

## 方法与技术要点

- 采集：以存储操作为单位记录 gas 与访问语义，避开 opcode 粒度下的语义噪声，从而精确定位过度收费来自哪次重复加载。
- 规则化推断：依据 account load/store、slot load/store、bytecode load/store 之间的关系推断可省去的重复加载费用；刻意采用轻量规则而非复杂算法，以保住实时处理能力与客户端集成成本。
- 一致性保障：优化结果只依赖共识层已保证的高层语义，因此各节点一致；MPT cache、bytecode cache 等因客户端与环境而异的部分不生成规则，以守住安全原则。
- 资源预分配：固定客户端参数（如 cache 大小）并预留内存，抹平异构节点上的缓存差异；write-ahead log 保证缓存状态在客户端终止后可恢复。
- 跨链移植：与以太坊共享 TFM 与存储组件代码的 50 条链可直接部署，BSC 上已验证。

## 评估与主要结果

- 以太坊约四个月交易数据与四客户端实现分析：Maat 使手续费降低 32%，每周节省 5.6M USD，约为 EIP-2929 基线的三倍。
- 运行开销：区块处理时间增加 1.4%（结论处亦称 1%），内存占用增加 5.6%，即便算入 WAL 的总时间开销仍为 1.4%。
- 可扩展性：BSC 上手续费降低 31%，每周 1.54M USD；移植到 50 条共享同一 TFM 与存储组件代码的链上同样有效。
- 优化范围：为最近 128 个区块的访问数据维护缓冲，约占 230 MiB 内存，作者把它视为优化精度与资源开销之间的显式折中。

[返回 Cloud Storage](index.md) · [返回 FAST 2025](../index.md)
