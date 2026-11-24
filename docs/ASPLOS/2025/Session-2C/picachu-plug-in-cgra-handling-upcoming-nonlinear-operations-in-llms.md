---
title: "PICACHU: Plug-In CGRA Handling Upcoming Nonlinear Operations in LLMs"
description: "ASPLOS 2025 · Session 2C · PICACHU：面向 LLM 中新兴非线性运算的插件式 CGRA"
tags:
  - "ASPLOS2025"
  - "Session 2C"
  - "Accelerators"
---

# PICACHU: Plug-In CGRA Handling Upcoming Nonlinear Operations in LLMs

**中文标题：** PICACHU：面向 LLM 中新兴非线性运算的插件式 CGRA

**所属 Session：** [Session 2C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jiajun Qin (New York University,Zhejiang University), Tianhua Xia (New York University), Cheng Tan (Google,Arizona State University), Jeff Zhang (Arizona State University), Sai Qian Zhang (New York University)

**单位：** New York University,Zhejiang University；New York University；Google,Arizona State University；Arizona State University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716013) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Large language models (LLMs) have revolutionized natural language processing (NLP) domain by achieving state-ofthe-art performance across a range of benchmarks. However, nonlinear operations in LLMs significantly contribute to inference latency and present unique challenges that have not been encountered previously. Addressing these challenges requires accelerators that combine efficiency, flexibility, and support for user-defined precision. Our analysis reveals that Coarse-Grained Reconfigurable Arrays (CGRAs) provide an effective solution, offering a balance of performance and flexibility tailored to domain-specific workloads. This paper introduces PICACHU, a plug-in coarse-grained reconfigurable accelerator tailored to efficiently handle nonlinear operations by using custom algorithms and a dedicated compiler toolchain. PICACHU is the first to target all nonlinear operations within LLMs and to consider CGRA as a plug-in accelerator for LLM inference. Our evaluation shows that PICACHU achieves speedups of 1.86× and 1.55× over prior state-of-the-art accelerators in LLM inference.

## 中文摘要

大语言模型（LLM）在一系列基准上取得了最先进的性能，从而革新了自然语言处理（NLP）领域。然而，LLM 中的非线性运算显著增加了推理时延，并带来了此前未曾遇到的独特挑战。应对这些挑战需要兼具高效率、灵活性并支持用户自定义精度的加速器。我们的分析表明，粗粒度可重构阵列（CGRA）是一种有效方案，它针对领域特定负载提供了性能与灵活性之间的平衡。本文提出 PICACHU，一种插件式粗粒度可重构加速器，它通过自定义算法与专用编译器工具链来高效处理非线性运算。PICACHU 是首个覆盖 LLM 中全部非线性运算、并将 CGRA 作为 LLM 推理插件式加速器的工作。我们的评估表明，在 LLM 推理中，PICACHU 相比先前最先进的加速器分别取得 1.86× 与 1.55× 的加速。

## 英文关键词

Domain Specific Architecture (DSA), CoarseGrained Reconfigurable Array (CGRA), Large Language Models (LLM)

## 中文关键词

领域特定架构（DSA）；粗粒度可重构阵列（CGRA）；大语言模型（LLM）

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716013)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2C](index.md) · [返回 ASPLOS 2025](../index.md)
