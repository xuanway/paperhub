---
title: "RTL Verification for Secure Speculation Using Contract Shadow Logic"
description: "ASPLOS 2025 · Session 9C · 基于 Contract Shadow Logic 的安全推测 RTL 验证"
tags:
  - "ASPLOS2025"
  - "Session 9C"
  - "Verification & Reliability"
---

# RTL Verification for Secure Speculation Using Contract Shadow Logic

**中文标题：** 基于 Contract Shadow Logic 的安全推测 RTL 验证

**所属 Session：** [Session 9C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Qinhan Tan (Princeton University), Yuheng Yang (Massachusetts Institute of Technology), Thomas Bourgeat (École Polytechnique Fédérale de Lausanne), Sharad Malik (Princeton University), Mengjia Yan (Massachusetts Institute of Technology)

**单位：** Princeton University；Massachusetts Institute of Technology；École Polytechnique Fédérale de Lausanne

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707243) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Modern out-of-order processors face speculative execution attacks. Despite various proposed software and hardware mitigations to prevent such attacks, new attacks keep arising from unknown vulnerabilities. Thus, a formal and rigorous evaluation of the ability of hardware designs to deal with speculative execution attacks is urgently desired. This paper proposes a formal verification technique called Contract Shadow Logic that can considerably improve RTL verification scalability with little manual effort while being applicable to different defense mechanisms. In this technique, we leverage computer architecture design insights to improve verification performance for checking security properties formulated as software-hardware contracts for secure speculation. Our verification scheme is accessible to computer architects and requires minimal formal-method expertise. We evaluate our technique on multiple RTL designs, including three out-of-order processors. The experimental results demonstrate that our technique exhibits a significant advantage in finding attacks on insecure designs and deriving complete proofs on secure designs, when compared to the baseline and two state-of-the-art verification schemes, LEAVE and UPEC.

## 中文摘要

现代乱序处理器面临推测执行攻击。尽管已有多种软件和硬件缓解措施被提出以阻止此类攻击，新的攻击仍不断由未知漏洞中涌现。因此，亟需对硬件设计应对推测执行攻击的能力进行形式化且严格的评估。本文提出一种名为 Contract Shadow Logic 的形式化验证技术，它仅需极少的人工投入就能显著提升 RTL 验证的可扩展性，同时可适用于不同的防御机制。在该技术中，我们利用计算机体系结构设计洞见来提升验证性能，用于检查以软硬件契约形式表述的安全推测安全属性。我们的验证方案对计算机体系结构研究者而言易于使用，且几乎不要求形式化方法方面的专业知识。我们在多个 RTL 设计上评估了本技术，其中包括三个乱序处理器。实验结果表明，与基线方案以及两种最先进的验证方案 LEAVE 和 UPEC 相比，我们的技术在发现不安全设计上的攻击、以及为安全设计导出完整证明方面均展现出显著优势。

## 英文关键词

Speculative Execution Attacks, HardwareSoftware Contract, Formal Verification, Shadow Logic

## 中文关键词

推测执行攻击；软硬件契约；形式化验证；Shadow Logic

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707243)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9C](index.md) · [返回 ASPLOS 2025](../index.md)
