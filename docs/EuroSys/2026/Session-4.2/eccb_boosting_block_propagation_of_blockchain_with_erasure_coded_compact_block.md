---
title: "ECCB: Boosting Block Propagation of Blockchain with Erasure-Coded Compact Block"
description: "EuroSys 2026 · Distributed Consensus, Blockchain & Storage · Bingyi Cai (Huazhong University of Science and Technology), Shenggang Wan (Huazh"
tags:
  - "EuroSys2026"
  - "Distributed Consensus, Blockchain & Storage"
---

# ECCB: Boosting Block Propagation of Blockchain with Erasure-Coded Compact Block

**中文标题：** ECCB：用纠删码紧凑区块提升区块链的区块传播

**所属 Session：** [Session 4.2: Distributed Consensus, Blockchain & Storage](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Consensus, Blockchain & Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Consensus, Blockchain & Storage</p>
</div>

**作者**：Bingyi Cai (Huazhong University of Science and Technology), Shenggang Wan (Huazhong University of Science and Technology), Hong Jiang (Department of Computer Science and Engineering, The University of Texas at Arlington)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769385)

## 英文摘要

Blockchain, the cornerstone for building the next generation of trustworthy web, suffers from poor scalability. Accelerating block propagation among blockchain nodes through block compression is an effective approach to improving scalability. However, existing block compression techniques, due to either low compression ratios or high recommunication ratios, induce either high transmission latency (proportional to block size, for a given Internet bandwidth) or multi-round Internet delay (dominated by geographical separation), causing significant network latency. To address both issues simultaneously, we propose a novel block propagation protocol, Erasure-Coded Compact Block (ECCB). It is motivated by and designed to exploit the significant transactional redundancy empirically observed in propagating blocks from six Ethereum nodes deployed across three continents. This redundancy refers to two key observations we made. First, most transactions in a propagating block (called hitting transactions) already exist in nodes’ local transaction pools. Second, almost all of the remaining non-hitting transactions in the block (called missing transactions) are overlapping between neighboring nodes. Thus, rather than propagating all transactions within a propagating block, ECCB only propagates the much smaller-sized parity data that is erasure-code generated from these transactions. When receiving an ECCB block, a node combines the parity data with the dominant hitting transactions already existing in the local transaction pool to reconstruct the missing transactions, thus significantly compressing the propagating block. Meanwhile, recommunication is avoided by transmitting slightly more parity data than the predicted total size of all missing transactions, leveraging the high degree of overlap in missing transactions between neighboring nodes. Results from both simulation and prototyping experiments demonstrate the high efficacy of ECCB.

## 中文摘要

区块链是构建下一代可信 Web 的基石，却受困于较差的可扩展性。通过区块压缩加速区块链节点间的区块传播，是提升可扩展性的有效途径。然而，现有区块压缩技术由于压缩率低或重传率高，要么带来高传输时延（在给定互联网带宽下与区块大小成正比），要么带来多轮互联网往返时延（主要受地理分隔支配），从而造成显著的网络时延。为同时解决这两个问题，我们提出一种新颖的区块传播协议——纠删码紧凑区块（ECCB）。它的提出动机源于并有意识地利用我们在横跨三大洲部署的六个以太坊节点传播区块时实际观测到的显著交易冗余。这种冗余指我们得到的两个关键观察。第一，传播区块中的大多数交易（称为命中交易）已存在于节点的本地交易池中。第二，区块中几乎所有剩余的未命中交易（称为缺失交易）在相邻节点之间存在重叠。因此，ECCB 不再传播传播区块中的所有交易，而只传播由这些交易经纠删码生成的、体积小得多的校验数据。节点收到 ECCB 区块后，将校验数据与本地交易池中已存在的大量命中交易相结合，重建缺失交易，从而显著压缩传播区块。同时，通过传输略多于所预测的全部缺失交易总大小的校验数据，并利用相邻节点间缺失交易的高度重叠，避免了重传。仿真与原型实验的结果均表明 ECCB 具有很高的有效性。

**英文关键词：** blockchain, Ethereum, block propagation, peer-to-peer network, erasure coding

**中文关键词：** 区块链、以太坊、区块传播、对等网络、纠删码

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
