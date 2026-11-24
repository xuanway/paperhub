---
title: "Detecting Inconsistencies in ARM CCA’s Formally Verified Specification"
description: "ASPLOS 2026 · Session 3D · 检测 ARM CCA 形式化验证规范中的不一致性"
tags:
  - "ASPLOS2026"
  - "Session 3D"
  - "Trusted Execution Environments"
---

# Detecting Inconsistencies in ARM CCA’s Formally Verified Specification

**中文标题：** 检测 ARM CCA 形式化验证规范中的不一致性

**所属 Session：** [Session 3D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Changho Choi (Samsung Research), Xiang Cheng (Georgia Institute of Technology), Bokdeuk Jeong (Samsung Research), Taesoo Kim (Georgia Institute of Technology, Samsung Research)

**单位：** Samsung Research；Georgia Institute of Technology；Georgia Institute of Technology, Samsung Research

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790152) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Formal verification offers strong guarantees of correctness, robustness, and security. However, these guarantees depend on specification correctness, and even minor flaws can invalidate proofs and introduce critical vulnerabilities. We present Scope, an automated system that identifies specification inconsistencies by combining formal modeling with rule-based consistency checking. Unlike traditional approaches that rely on implementations, Scope treats the specification as the sole ground truth. It translates the specification into a machine-verifiable model using Verus and SMT solvers, then detects inconsistencies in success/failure conditions, dependency rules, and state transitions. We apply Scope to the Realm Management Monitor (RMM) specifications for Arm's Confidential Compute Architecture (CCA), uncovering 35 previously unknown bugs—including security-critical flaws in ABI semantics and missing state transitions—all confirmed by Arm. Compared to modern LLM-based tools, Scope improves inconsistency-detection precision by 7× over GPT-o1 and up to 40× over leading chat models (LLaMA 3.1, GPT-4o, Claude 3.7).

## 中文摘要

形式化验证为正确性、鲁棒性和安全性提供了强有力的保证。然而，这些保证依赖于规范的正确性，即使是微小的缺陷也可能使证明失效并引入严重漏洞。我们提出 Scope，一个将形式化建模与基于规则的一致性检查相结合以识别规范不一致性的自动化系统。与依赖实现的传统方法不同，Scope 将规范视为唯一的事实依据。它使用 Verus 和 SMT 求解器将规范转换为机器可验证的模型，然后检测成功/失败条件、依赖规则和状态转换中的不一致性。我们将 Scope 应用于 Arm 机密计算架构（CCA）的 Realm 管理监视器（RMM）规范，发现了 35 个此前未知的缺陷——包括 ABI 语义中的安全关键缺陷和缺失的状态转换——且全部得到 Arm 的确认。与基于 LLM 的现代工具相比，Scope 将不一致性检测精度相较 GPT-o1 提升了 7 倍，相较领先的对话模型（LLaMA 3.1、GPT-4o、Claude 3.7）最高提升 40 倍。

## 英文关键词

Specification validation; Formal methods; Automated reasoning; Confidential computing; Arm CCA

## 中文关键词

规范验证；形式化方法；自动推理；机密计算；Arm CCA

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790152)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3D](index.md) · [返回 ASPLOS 2026](../index.md)
