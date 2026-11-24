---
title: "Compositional AI Beyond LLMs: System Implications of Neuro-Symbolic-Probabilistic Architectures"
description: "ASPLOS 2026 · Session 5A · 超越 LLM 的组合式 AI：神经-符号-概率架构的系统影响"
tags:
  - "ASPLOS2026"
  - "Session 5A"
  - "Generative Model Serving"
---

# Compositional AI Beyond LLMs: System Implications of Neuro-Symbolic-Probabilistic Architectures

**中文标题：** 超越 LLM 的组合式 AI：神经-符号-概率架构的系统影响

**所属 Session：** [Session 5A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zishen Wan (Georgia Tech), Hanchen Yang (Georgia Tech), Jiayi Qian (Georgia Tech), Ritik Raj (Georgia Tech), Joongun Park (Georgia Tech), Chenyu Wang (Princeton University), Arijit Raychowdhury (Georgia Tech), Tushar Krishna (Georgia Tech)

**单位：** Georgia Tech；Princeton University

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762235) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Large Language Models (LLMs) have driven remarkable progress in artificial intelligence (AI), but their rapid growth faces challenges of unsustainable computation, limited robustness, and poor explainability. Compositional AI, which integrates LLMs with symbolic reasoning and probabilistic inference, has emerged as a promising paradigm to enable interpretability, robustness, trustworthiness, and dataefficient learning. Recent neuro-symbolic-probabilistic systems demonstrate strong potential in agentic applications, advancing reasoning and cognitive capabilities toward humanlike intelligence. In this paper, we aim to understand the system implications of neuro-symbolic-probabilistic architectures. We first develop a taxonomy and analyze the scaling efficiency of neuro-symbolic-probabilistic models. We then perform a detailed characterization across CPUs and GPUs, evaluating their runtime, memory, compute operators, dataflow, scalability, communication, and system behaviors. Our studies reveal that compositional models suffer from inefficiencies on offthe-shelf hardware, constrained by heterogeneous compute kernels, irregular memory access, complex flow control, data dependencies, and high data movement. Guided by these insights, we present several software- and system-level optimizations to demonstrate the potential for improving the performance, efficiency, and scalability of neuro-symbolic edu probabilistic computing. To our knowledge, this is among the first works to holistically assess compositional neurosymbolic AI from system and architectural perspectives.

## 中文摘要

大型语言模型（LLM）推动了人工智能（AI）的显著进展，但其快速增长面临着计算不可持续、鲁棒性有限和可解释性不足等挑战。组合式 AI 将 LLM 与符号推理和概率推断相结合，已成为一种有望实现可解释性、鲁棒性、可信性和数据高效学习的范式。近期的神经-符号-概率系统在智能体应用中展现出强大潜力，将推理与认知能力推向类人智能。本文旨在理解神经-符号-概率架构的系统影响。我们首先建立了一套分类体系，并分析了神经-符号-概率模型的扩展效率。随后，我们在 CPU 和 GPU 上开展了详细的刻画，评估其运行时、内存、计算算子、数据流、可扩展性、通信和系统行为。我们的研究表明，组合式模型在现成硬件上存在低效问题，受限于异构计算内核、不规则内存访问、复杂控制流、数据依赖和高数据移动。在这些洞察的指导下，我们提出了若干软件级和系统级优化，以展示提升神经-符号-概率计算的性能、效率和可扩展性的潜力。据我们所知，这是首批从系统和架构视角对组合式神经符号 AI 进行整体评估的工作之一。

## 英文关键词

Compositional AI, Neuro-Symbolic System, Workload Characterization, Scaling Efficiency, System Optimization

## 中文关键词

组合式 AI；神经符号系统；工作负载刻画；扩展效率；系统优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762235)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5A](index.md) · [返回 ASPLOS 2026](../index.md)
