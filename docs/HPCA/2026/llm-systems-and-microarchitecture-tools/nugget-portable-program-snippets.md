---
title: "Nugget: Portable Program Snippets"
description: "HPCA 2026 · LLM Systems and Microarchitecture Tools"
tags:
  - "HPCA2026"
  - "LLM Systems and Microarchitecture Tools"
---

# Nugget: Portable Program Snippets

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: LLM Systems and Microarchitecture Tools。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · LLM Systems and Microarchitecture Tools</p>
</div>

**论文链接**：
**作者**：Zhantong Qiu University of California, Davis , Mahyar Samani University of California, Davis , Jason Lowe-Power University of California, Davis & Google
**会议**：HPCA 2026

---

## 中文标题

Nugget：可移植的程序片段

## 英文摘要

Evaluating architectural ideas on realistic workloads is increasingly challenging due to the prohibitive cost of detailed simulation and the lack of portable sampling tools. Existing targeted sampling techniques are often tied to specific binaries, incur significant overhead, and make rapid validation across systems infeasible. To address these limitations, we introduce Nugget, a flexible framework that enables portable sampling across simulators, hardware, architectural differences, and libraries. Nugget leverages LLVM IR to perform binary-independent interval analysis, then generates lightweight, cross-platform executable snippets, nuggets, that can be validated natively on real hardware before use in simulation. This approach decouples samples from specific binaries, dramatically reduces analysis overhead, and allows researchers to iterate on sampling methodologies while efficiently validating samples across diverse systems.

## 中文摘要

在真实负载上评估体系结构想法的难度日益增加，原因在于详细模拟的成本高昂，且缺乏可移植的采样工具。已有的定向采样技术往往绑定特定二进制程序，带来可观开销，并使跨系统快速验证难以实现。为克服这些局限，我们提出 Nugget，一个灵活的框架，支持在模拟器、硬件、体系结构差异与库之间进行可移植采样。Nugget 利用 LLVM IR 执行与二进制无关的区间分析，进而生成轻量、跨平台的可执行片段（nuggets），这些片段可在用于模拟之前先在真实硬件上原生验证。该方法将样本与特定二进制解耦，大幅降低分析开销，并使研究者能够迭代采样方法学，同时在不同系统上高效验证样本。
