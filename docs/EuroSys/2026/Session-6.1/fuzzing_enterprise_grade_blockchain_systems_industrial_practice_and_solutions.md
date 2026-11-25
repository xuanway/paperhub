---
title: "Fuzzing Enterprise-Grade Blockchain Systems: Industrial Practice and Solutions"
description: "EuroSys 2026 · Security · Fuchen Ma (Tsinghua University), Yuanliang Chen (Tsinghua University), Zhen Yan "
tags:
  - "EuroSys2026"
  - "Security"
---

# Fuzzing Enterprise-Grade Blockchain Systems: Industrial Practice and Solutions

**中文标题：** 对企业级区块链系统进行模糊测试：工业实践与解决方案

**所属 Session：** [Session 6.1: Security](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Security。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Security</p>
</div>

**作者**：Fuchen Ma (Tsinghua University), Yuanliang Chen (Tsinghua University), Zhen Yan (Tsinghua University), Yuanhang Zhou (Tsinghua University), Yu Jiang (Tsinghua University), Mingchao Wan (Beijing Academy of Blockchain and Edge Computing)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803582)

## 英文摘要

Blockchain has been widely adopted across diverse sectors. Yet, enterprise-grade systems remain vulnerable to critical flaws that undermine stability and security. Although academic fuzzing tools such as LOKI and Tyr have shown effectiveness in detecting such issues, their integration into industrial practice remains challenging.

In this paper, we present the industry practice of implementing system-level fuzzing techniques on enterprise-level blockchains. We summarize three main obstacles in industry deployment, namely the hard-to-build state models for fuzzing, the slow convergence of fuzz testing within CI/CD pipelines, and the difficulty of adapting logical bug oracles across diverse blockchain implementations. To address these obstacles, we design Thor, a practical fuzzing framework for industry blockchain systems. Thor uses active and passive packet generation for early stage state-aware testing. To perform efficient fuzzing under strict CI/CD time budgets, Thor adopts a two-tier parallel fuzzing method. And Thor also uses LLM-based oracles to extract logic properties from node logs. Over these years, Thor has discovered 87 bugs in 9 commercial blockchain systems, such as Chainmaker, Go-Ethereum, and WeBank FISCO BCOS.

## 中文摘要

区块链已在多个行业得到广泛应用。然而，企业级系统仍易受关键缺陷影响，危及稳定性与安全性。尽管 LOKI、Tyr 等学术模糊测试工具在检测此类问题方面已显现效果，但将其融入工业实践仍具挑战。

本文介绍在企业级区块链上实施系统级模糊测试技术的工业实践。我们总结了工业部署中的三大障碍，即为模糊测试构建状态模型困难、模糊测试在 CI/CD 流水线中收敛缓慢，以及难以将逻辑缺陷判定器适配到多样化的区块链实现。为应对这些障碍，我们设计了 Thor，一个面向工业区块链系统的实用模糊测试框架。Thor 采用主动与被动数据包生成，用于早期阶段的状态感知测试。为在严格的 CI/CD 时间预算下高效执行模糊测试，Thor 采用双层并行模糊测试方法。此外，Thor 还使用基于 LLM 的判定器从节点日志中提取逻辑属性。多年来，Thor 已在 Chainmaker、Go-Ethereum 和微众银行 FISCO BCOS 等 9 个商用区块链系统中发现 87 个缺陷。

**英文关键词：** Fuzz Testing, Blockchain System

**中文关键词：** 模糊测试、区块链系统

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
