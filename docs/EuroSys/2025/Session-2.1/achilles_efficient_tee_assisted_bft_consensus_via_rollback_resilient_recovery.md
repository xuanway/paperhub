---
title: "Achilles: Efficient TEE-Assisted BFT Consensus via Rollback Resilient Recovery"
description: "EuroSys 2025 · Fault Tolerance and Consensus · Jianyu Niu (Southern University of Science and Technology), Guanlong Wu (Souther"
tags:
  - "EuroSys2025"
  - "Fault Tolerance and Consensus"
---

# Achilles: Efficient TEE-Assisted BFT Consensus via Rollback Resilient Recovery

**中文标题：** 通过抗回滚恢复实现高效可信执行环境辅助 BFT 共识

**所属 Session：** [Session 2.1: Fault Tolerance and Consensus](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Fault Tolerance and Consensus。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Fault Tolerance and Consensus</p>
</div>

**作者**：Jianyu Niu (Southern University of Science and Technology), Guanlong Wu (Southern University of Science and Technology), Shengqi Liu (Southern University of Science and Technology.), Xiaoqing Wen (University of British Columbia), Jiangshan Yu (The University of Sydney), Yinqian Zhang (Southern University of Science and Technology (SUSTech))

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717457)

## 英文摘要

BFT consensus that uses Trusted Execution Environments (TEEs) to improve the system tolerance and performance is gaining popularity. However, existing works suffer from TEE rollback issues, resulting in a tolerance-performance tradeoff. In this paper, we propose Achilles, an efficient TEE-assisted BFT protocol that breaks the tradeoff. The key idea behind Achilles is removing the expensive rollback prevention of TEEs from the critical path of committing transactions. To this end, Achilles adopts a rollback resilient recovery mechanism, which allows nodes to assist each other in recovering their states. Besides, Achilles follows the chaining spirit in modern chained BFT protocols and leverages customized chained commit rules to achieve linear message complexity, end-to-end transaction latency of four communication steps, and fault tolerance for the minority of Byzantine nodes. Achilles is the first TEE-assisted BFT protocol in line with CFT protocols in these metrics. We implement a prototype of Achilles based on Intel SGX and evaluate it in both LAN and WAN, showcasing its outperforming performance compared to several state-of-the-art counterparts.

## 中文摘要

利用可信执行环境（TEE）提升系统容错能力与性能的 BFT 共识正日益流行。然而，现有工作受 TEE 回滚问题困扰，导致容错与性能之间的权衡。本文提出 Achilles，一种高效的 TEE 辅助 BFT 协议，打破了这一权衡。Achilles 的核心思想是将 TEE 昂贵的回滚防止机制从提交事务的关键路径中移除。为此，Achilles 采用一种抗回滚的恢复机制，允许节点相互协助恢复各自的状态。此外，Achilles 遵循现代链式 BFT 协议中的链式思想，并利用定制的链式提交规则实现线性消息复杂度、四个通信步骤的端到端事务延迟，以及对少数拜占庭节点的容错能力。在这些指标上，Achilles 是首个与 CFT 协议相当的 TEE 辅助 BFT 协议。我们基于 Intel SGX 实现了 Achilles 原型，并在局域网和广域网中进行了评估，展示了其优于若干最先进同类方案的性能。

**英文关键词：** BFT consensus, TEE, Rollback, CFT consensus

**中文关键词：** BFT 共识、TEE、回滚、CFT 共识

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
