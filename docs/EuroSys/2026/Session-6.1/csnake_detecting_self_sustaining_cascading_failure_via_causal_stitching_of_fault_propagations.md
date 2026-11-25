---
title: "CSnake: Detecting Self-Sustaining Cascading Failure via Causal Stitching of Fault Propagations"
description: "EuroSys 2026 · Security · Shangshu Qian (Purdue University), Lin Tan (Purdue University), Yongle Zhang (Pu"
tags:
  - "EuroSys2026"
  - "Security"
---

# CSnake: Detecting Self-Sustaining Cascading Failure via Causal Stitching of Fault Propagations

**中文标题：** CSnake：通过故障传播的因果拼接检测自持级联故障

**所属 Session：** [Session 6.1: Security](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Security。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Security</p>
</div>

**作者**：Shangshu Qian (Purdue University), Lin Tan (Purdue University), Yongle Zhang (Purdue University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769373)

## 英文摘要

Recent studies have revealed that self-sustaining cascading failures in distributed systems frequently lead to widespread outages, which are challenging to contain and recover from. Existing failure detection techniques struggle to expose such failures prior to deployment, as they typically require a complex combination of specific conditions to be triggered. This challenge stems from the inherent nature of cascading failures, as they typically involve a sequence of fault propagations, each activated by distinct conditions.

This paper presents CSnake, a fault injection framework to expose self-sustaining cascading failures in distributed systems. CSnake uses the novel idea of causal stitching, which causally links multiple single-fault injections in different test workloads to simulate complex fault propagation chains. To identify propagation chains between faults, CSnake designs a counterfactual causality analysis of fault propagations – fault causality analysis (FCA): FCA compares the execution trace of a fault injection run with its corresponding profile run (i.e., running the same test without the injection) and identifies any additional faults triggered, which are considered to have a causal relationship with the injected fault.

To address the large search space of fault and workload combinations, CSnake employs a three-phase allocation (3PA) protocol of test budget that prioritizes faults with unique and diverse causal consequences, thereby increasing the likelihood of uncovering conditional fault propagations. Furthermore, to avoid incorrectly connecting fault propagations from workloads with incompatible conditions, CSnake performs a local compatibility check that approximately checks the compatibility of the path constraints associated with connected fault propagations with low overhead.

CSnake has detected 15 bugs that resulted in self-sustaining cascading failures in five widely deployed distributed systems, five of which have been confirmed with two fixed.

## 中文摘要

近期研究表明，分布式系统中的自持级联故障常常导致大范围服务中断，且难以遏制和恢复。现有故障检测技术难以在部署前暴露此类故障，因为它们通常需要特定条件的复杂组合才能被触发。这一挑战源于级联故障的固有本质：它们通常涉及一系列故障传播，每一次传播都由不同条件激活。

本文提出 CSnake，一个用于暴露分布式系统中自持级联故障的故障注入框架。CSnake 采用因果拼接这一新思路，将不同测试工作负载中的多次单故障注入进行因果关联，以模拟复杂的故障传播链。为识别故障之间的传播链，CSnake 设计了一种针对故障传播的反事实因果分析——故障因果分析（FCA）：FCA 将故障注入运行的执行轨迹与其对应的剖析运行（即在不注入故障的情况下运行同一测试）进行比较，并识别出被额外触发的故障，这些故障被认为与所注入的故障存在因果关系。

为应对故障与工作负载组合的巨大搜索空间，CSnake 采用测试预算的三阶段分配（3PA）协议，优先考虑具有独特且多样因果后果的故障，从而提高发现条件性故障传播的可能性。此外，为避免错误地连接来自条件不兼容工作负载的故障传播，CSnake 执行本地兼容性检查，以低开销近似检查所连接故障传播相关路径约束的兼容性。

CSnake 在五个广泛部署的分布式系统中检测出 15 个导致自持级联故障的缺陷，其中 5 个已得到确认，2 个已被修复。

**英文关键词：** Distributed System, Cascading Failure, Bug Detection, Fault Injection, Cloud Computing

**中文关键词：** 分布式系统、级联故障、缺陷检测、故障注入、云计算

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
