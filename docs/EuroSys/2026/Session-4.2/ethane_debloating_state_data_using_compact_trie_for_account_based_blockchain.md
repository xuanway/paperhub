---
title: "Ethane: Debloating State Data using Compact Trie for Account-based Blockchain"
description: "EuroSys 2026 · Distributed Consensus, Blockchain & Storage · Junmo Lee (Seoul National University), Jaehun Kim (Seoul National University), J"
tags:
  - "EuroSys2026"
  - "Distributed Consensus, Blockchain & Storage"
---

# Ethane: Debloating State Data using Compact Trie for Account-based Blockchain

**中文标题：** Ethane：面向账户型区块链使用紧凑 Trie 精简状态数据

**所属 Session：** [Session 4.2: Distributed Consensus, Blockchain & Storage](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Consensus, Blockchain & Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Consensus, Blockchain & Storage</p>
</div>

**作者**：Junmo Lee (Seoul National University), Jaehun Kim (Seoul National University), Jiyong Youn (Seoul National University), Soo-Mook Moon (Seoul National University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769340)

## 英文摘要

Account-based blockchains can suffer from huge state data as the number of accounts soars, as in the current Ethereum. This makes it hard to synchronize and operate as a full node to verify transactions, or as an archive node to maintain all archive data for provenance queries. The problem is mostly caused by the state trie, a tree-like data structure to store account states in its leaves, where an account has a path key to follow to access the account. Whenever an account is updated in the state trie, all trie nodes along the path key from the leaf to the root are newly created, which causes a data explosion. In this paper, we propose a novel state optimization technique called Ethane. Instead of assigning a fixed, hash-based path key for an account as in Ethereum, Ethane assigns a variable, counter-based path key. So, when a transaction creates or updates an account, Ethane creates a new leaf node for the account and assigns a path key of the next counter value, which has an effect of adding the leaf to the rightmost slot of the trie. This compact trie maximizes common parent nodes and minimizes the creation of new non-leaf nodes, significantly reducing the archive data size. In addition, Ethane maintains two types of compact tries: an active trie for frequently updated accounts and an inactive trie for dormant accounts not updated for a long time (e.g., three months). Dormant accounts are transferred to the inactive trie but can be reactivated at any time via a restore transaction. When synchronizing as a full node, we only need to download the active trie and the rightmost path of the inactive trie to function fully, significantly reducing both storage requirements and synchronization overhead. Our evaluation shows that Ethane can downsize the archive state data by 60-85% and the current state trie by 60-94%. It also doubles the block execution performance.

## 中文摘要

账户型区块链在账户数量激增时会遭遇状态数据膨胀，当前的以太坊即是如此。这使得无论是作为全节点同步运行以验证交易，还是作为归档节点保存全部归档数据以支持溯源查询，都变得困难。该问题主要由状态 Trie 引起：这是一种树状数据结构，账户状态存储在其叶节点中，每个账户拥有一条路径键，需沿该键访问账户。每当账户在状态 Trie 中被更新时，沿路径键从叶节点到根节点的所有 Trie 节点都会被重新创建，从而引发数据爆炸。本文提出一种名为 Ethane 的新型状态优化技术。Ethane 不再像以太坊那样为账户分配固定的、基于哈希的路径键，而是分配可变的、基于计数器的路径键。因此，当一笔交易创建或更新账户时，Ethane 为该账户创建新的叶节点，并分配下一个计数器值作为路径键，其效果相当于将该叶节点添加到 Trie 的最右侧槽位。这种紧凑 Trie 最大化了公共父节点、最小化了新非叶节点的创建，从而显著减小归档数据规模。此外，Ethane 维护两类紧凑 Trie：面向频繁更新账户的活跃 Trie，以及面向长期未更新（例如三个月）的休眠账户的非活跃 Trie。休眠账户被转移到非活跃 Trie，但可随时通过恢复交易重新激活。作为全节点同步时，我们只需下载活跃 Trie 以及非活跃 Trie 的最右侧路径即可完整运行，显著降低了存储需求与同步开销。我们的评测显示，Ethane 可将归档状态数据缩减 60–85%，将当前状态 Trie 缩减 60–94%，同时使区块执行性能提升一倍。

**英文关键词：** Blockchain, State trie, Storage overhead

**中文关键词：** 区块链、状态 Trie、存储开销

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
