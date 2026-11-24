---
title: "Multi-Grained Specifications for Distributed System Model Checking and Verification"
description: "EuroSys 2025 · Distributed Systems · Lingzhi Ouyang (Nanjing University), Xudong Sun (University of Illinois Urbana-C"
tags:
  - "EuroSys2025"
  - "Distributed Systems"
---

# Multi-Grained Specifications for Distributed System Model Checking and Verification

**中文标题：** 用于分布式系统模型检查与验证的多粒度规约

**所属 Session：** [Session 3.1: Distributed Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Distributed Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Distributed Systems</p>
</div>

**作者**：Lingzhi Ouyang (Nanjing University), Xudong Sun (University of Illinois Urbana-Champaign), Ruize Tang (Nanjing University), Yu Huang (Nanjing University), Madhav Jivrajani (University of Illinois Urbana-Champaign), Xiaoxing Ma (Nanjing University), Tianyin Xu (University of Illinois Urbana-Champaign)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696069)

## 英文摘要

This paper presents our experience specifying and verifying the correctness of ZooKeeper, a complex and evolving distributed coordination system. We use TLA+ to model finegrained behaviors of ZooKeeper and use the TLC model checker to verify its correctness properties; we also check conformance between the model and code. The fundamental challenge is to balance the granularity of specifications and the scalability of model checking—fine-grained specifications lead to state-space explosion, while coarse-grained specifications introduce model-code gaps. To address this challenge, we write specifications with different granularities for composable modules, and compose them into mixed-grained specifications based on specific scenarios. For example, to verify code changes, we compose fine-grained specifications of changed modules and coarse-grained specifications that abstract away details of unchanged code with preserved interactions. We show that writing multi-grained specifications is a viable practice and can cope with model-code gaps without untenable state space, especially for evolving software where changes are typically local and incremental. We detected six severe bugs that violate five types of invariants and verified their code fixes; the fixes have been merged to ZooKeeper. We also improve the protocol design to make it easy to implement correctly.

## 中文摘要

本文介绍我们在为 ZooKeeper（一个复杂且不断演化的分布式协调系统）编写规约并验证其正确性方面的经验。我们使用 TLA+ 对 ZooKeeper 的细粒度行为建模，并使用 TLC 模型检验器验证其正确性性质；我们还检查模型与代码之间的一致性。根本挑战在于平衡规约的粒度与模型检验的可扩展性——细粒度规约会导致状态空间爆炸，而粗粒度规约则引入模型-代码差距。为应对这一挑战，我们为可组合的模块编写不同粒度的规约，并根据具体场景将它们组合成混合粒度规约。例如，为验证代码变更，我们将变更模块的细粒度规约与抽象掉未变更代码细节但保留其交互的粗粒度规约组合起来。我们表明，编写多粒度规约是一种可行的实践，能够在不产生难以承受的状态空间的情况下应对模型-代码差距，尤其是对于变更通常局部且增量的演化软件。我们检测出六个违反五类不变式的严重缺陷，并验证了它们的代码修复；这些修复已被合并到 ZooKeeper 中。我们还改进了协议设计，使其易于正确实现。

**英文关键词：** Distributed systems, model checking, reliability

**中文关键词：** 分布式系统、模型检验、可靠性

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
