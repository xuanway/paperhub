---
title: "Formalising CXL Cache Coherence"
description: "ASPLOS 2025 · Session 5D · 形式化 CXL 缓存一致性"
tags:
  - "ASPLOS2025"
  - "Session 5D"
  - "CXL Storage"
---

# Formalising CXL Cache Coherence

**中文标题：** 形式化 CXL 缓存一致性

**所属 Session：** [Session 5D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Chengsong Tan (Kaihong), Alastair F. Donaldson (Imperial College London), John Wickerson (Imperial College London)

**单位：** Kaihong；Imperial College London

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715999) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

We report our experience formally modelling and verifying CXL.cache, the inter-device cache coherence protocol of the Compute Express Link standard. We have used the Isabelle proof assistant to create a formal model for CXL.cache based on the English prose specification. This led to us identifying and proposing fixes to several parts of the specification that were unclear, ambiguous or inaccurate. Nearly all our issues and proposed fixes have been confirmed and tentatively accepted by the CXL consortium for adoption, save for one which is still under discussion. To validate the faithfulness of our model we performed scenario verification of essential restrictions such as “Snoop-pushes-GO”, and used the Isabelle proof assistant to produce a fully mechanised proof of a coherence property of the model. The considerable size of this proof, comprising tens of thousands of lemmas, prompted us to develop new proof automation tools, which we have made available for other Isabelle users working with similarly cumbersome proofs.

## 中文摘要

我们报告了对 CXL.cache（Compute Express Link 标准中设备间缓存一致性协议）进行形式化建模与验证的经验。我们使用 Isabelle 证明助手，依据英文文字规范为 CXL.cache 建立了一个形式化模型。这使我们发现并提出了针对规范中若干不清晰、有歧义或不准确的部分的修正方案。我们提出的几乎所有问题与修正方案都已得到 CXL 联盟（CXL consortium）的确认并被初步接受采纳，仅有一项仍在讨论之中。为验证模型的忠实性，我们对“Snoop-pushes-GO”等关键约束进行了场景验证，并使用 Isabelle 证明助手为该模型的一条一致性（coherence）性质给出了完全机器化的证明。该证明规模相当庞大，包含数万条引理，这促使我们开发了新的证明自动化工具，并将其提供给其他处理类似繁琐证明的 Isabelle 用户使用。

## 英文关键词

CXL, Cache Coherence, Proof Assistant, Heterogeneous Computing, Formal Proof

## 中文关键词

CXL；缓存一致性；证明助手；异构计算；形式化证明

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715999)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5D](index.md) · [返回 ASPLOS 2025](../index.md)
