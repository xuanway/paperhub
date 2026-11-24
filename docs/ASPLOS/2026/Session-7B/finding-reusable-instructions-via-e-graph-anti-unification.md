---
title: "Finding Reusable Instructions via E-Graph Anti-Unification"
description: "ASPLOS 2026 · Session 7B · 通过 E-Graph 反合一发现可复用指令"
tags:
  - "ASPLOS2026"
  - "Session 7B"
  - "Compilers & Code Generation"
---

# Finding Reusable Instructions via E-Graph Anti-Unification

**中文标题：** 通过 E-Graph 反合一发现可复用指令

**所属 Session：** [Session 7B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Youwei Xiao (Peking University), Chenyun Yin (Peking University), Yitian Sun (Peking University), Yuyang Zou (Peking University), Yun Liang (Peking University)

**单位：** Peking University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790162) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Domain-specific accelerators provide an increasingly valuable source of performance for diverse applications. Custom instructions that trigger the execution of dedicated hardware units or accelerators for common application functions become key building blocks in modern computing systems, balancing performance and cost effectiveness. RISC-V, the open and extensible instruction set architecture, is increasingly popularizing this trend. However, exploring custom instructions for an application domain remains challenging. Existing automated approaches suffer from poor reusability and limited performance. They can only identify or merge syntactically similar, scalar instruction sequences while missing semantically equivalent patterns. We present ISAMORE, an end-to-end framework for discovering reusable custom instructions from domain applications. ISAMORE encodes general applications in an e-graph by constructing a structured domain-specific language. Its core methodology, reusable instruction identification (RII), leverages e-graph anti-unification (AU) to identify semantically equivalent common patterns across diverse applications, fully unleashing the potential of custom instructions. RII employs a phase-oriented iterative process with smart heuristics to enhance the scalability when dealing with realworld codebases. Besides, RII introduces the novel pattern vectorization technique, packing common operations from scalar programs into lanes of vectorized custom instructions to exploit data-level parallelism. Moreover, RII's Paretooptimal pattern selection balances performance gains with area overheads, guided by a profiling-based hardware-aware cost model. Evaluation demonstrates ISAMORE's substantial performance gains, 1.12×-2.69×, over baseline approaches. We also demonstrate ISAMORE's practical potentials using various case studies, including library analysis for three application domains and hardware specialization for quantized LLM inference and post-quantum cryptography.

## 中文摘要

领域专用加速器为各类应用提供了日益重要的性能来源。针对常见应用功能触发专用硬件单元或加速器执行的自定义指令，成为现代计算系统中的关键构建模块，在性能与成本效益之间取得平衡。RISC-V 这一开放且可扩展的指令集架构正日益推动该趋势的普及。然而，面向某一应用领域探索自定义指令仍然充满挑战。现有的自动化方法存在可复用性差、性能提升有限的问题。它们只能识别或合并语法相似的标量指令序列，而遗漏了语义等价的模式。我们提出 ISAMORE，一个从领域应用中发掘可复用自定义指令的端到端框架。ISAMORE 通过构建结构化的领域专用语言，将通用应用编码到 e-graph 中。其核心方法——可复用指令识别（RII）——利用 e-graph 反合一（AU）来识别跨多样应用的语义等价公共模式，充分释放自定义指令的潜力。RII 采用带有智能启发式的分阶段迭代过程，以增强处理真实世界代码库时的可扩展性。此外，RII 引入了新颖的模式向量化技术，将标量程序中的公共操作打包进向量化自定义指令的通道，以利用数据级并行性。再者，RII 的帕累托最优模式选择在基于性能剖析的硬件感知代价模型指导下，在性能收益与面积开销之间取得平衡。评估表明，ISAMORE 相较基线方法取得了 1.12× 至 2.69× 的显著性能提升。我们还通过多个案例研究展示了 ISAMORE 的实际潜力，包括针对三个应用领域的库分析，以及面向量化 LLM 推理和后量子密码的硬件专用化。

## 英文关键词

Custom instruction; ASIP; E-graph; Hardwaresoftware co-design; Compiler

## 中文关键词

自定义指令；ASIP；E-graph；软硬件协同设计；编译器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790162)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7B](index.md) · [返回 ASPLOS 2026](../index.md)
