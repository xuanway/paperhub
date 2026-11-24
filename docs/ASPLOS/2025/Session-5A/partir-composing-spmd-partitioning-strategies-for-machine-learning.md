---
title: "PartIR: Composing SPMD Partitioning Strategies for Machine Learning"
description: "ASPLOS 2025 · Session 5A · PartIR：面向机器学习的 SPMD 分片策略组合"
tags:
  - "ASPLOS2025"
  - "Session 5A"
  - "ML Systems 1"
---

# PartIR: Composing SPMD Partitioning Strategies for Machine Learning

**中文标题：** PartIR：面向机器学习的 SPMD 分片策略组合

**所属 Session：** [Session 5A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Sami Alabed (Google DeepMind), Daniel Belov (Google DeepMind), Bart Chrzaszcz (Google DeepMind), Juliana Franco (Google DeepMind), Dominik Grewe (Google DeepMind), Dougal Maclaurin (Google DeepMind), James Molloy (Google DeepMind), Tom Natan (Google DeepMind), Tamara Norman (Google DeepMind), Xiaoyue Pan (Google DeepMind), Adam Paszke (Google DeepMind), Norman Alexander Rink (Google DeepMind), Michael Schaarschmidt (Isomorphic Labs), Timur Sitdikov (Google DeepMind), Agnieszka Swietlik (Google DeepMind), Dimitrios Vytiniotis (Google DeepMind), Joel Wee (Google DeepMind)

**单位：** Google DeepMind；Isomorphic Labs

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707284) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Training modern large neural networks (NNs) requires a com- bination of parallelization strategies, including data, model, or optimizer sharding. To address the growing complexity of these strategies, we introduce PartIR, a hardware-and- runtime agnostic NN partitioning system. PartIR is: 1) Ex- pressive: It allows for the composition of multiple sharding strategies, whether user-defined or automatically derived; 2) Decoupled: the strategies are separate from the ML im- plementation; and 3) Predictable: It follows a set of well- defined general rules to partition the NN. PartIR utilizes a schedule-like API that incrementally rewrites the ML pro- gram intermediate representation (IR) after each strategy, allowing simulators and users to verify the strategy's perfor- mance. PartIR has been successfully used both for training large models and across diverse model architectures, demon- strating its predictability, expressiveness, and performance.

## 中文摘要

训练现代大型神经网络（NN）需要组合多种并行化策略，包括数据、模型或优化器分片。为应对这些策略日益增长的复杂性，我们提出 PartIR，一个与硬件和运行时无关的 NN 划分系统。PartIR 具备：1）表达性：它允许组合多种分片策略，无论是用户定义的还是自动推导的；2）解耦性：这些策略与 ML 实现相分离；3）可预测性：它遵循一组定义明确的通用规则来划分 NN。PartIR 采用类似 schedule 的 API，在每个策略之后增量地重写 ML 程序的中间表示（IR），使模拟器与用户能够验证该策略的性能。PartIR 已成功用于训练大模型，并应用于多种模型架构，展示了其可预测性、表达性与性能。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707284)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5A](index.md) · [返回 ASPLOS 2025](../index.md)
