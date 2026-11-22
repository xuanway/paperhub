---
title: "Retrofitting Contextual Learning into Set Dueling"
description: "MICRO 2026 · Session 7D · 将上下文学习引入集合竞争机制"
tags:
  - "MICRO2026"
---

# Retrofitting Contextual Learning into Set Dueling

**中文标题：** 将上下文学习引入集合竞争机制

**所属 Session：** [Session 7D](index.md) · [MICRO 2026](../index.md)

**作者：** Diamantis Patsidis, Leeor Peled, Georgios Vavouliotis

**来源：** MICRO 2026，pp. 2669–2686；[DOI](https://doi.org/10.1109/MICRO67795.2026.00182)

## 英文摘要

Dynamic policy arbitration is fundamental to modern CPUs, as no single policy performs optimally across diverse workload domains. Set Dueling (SD) is widely used, both in academia and industry, to select between competing policies at runtime, but relies on a global, context-oblivious counter to make decisions, ignoring richer correlations based on execution context such as control and data flow information. This work proposes Context-Aware Set Dueling (CASD), a framework that elevates SD to a context-aware, policy-agnostic mechanism for fine-grained policy arbitration at runtime. CASD retrofits contextual learning into context-oblivious SD: a lightweight predictive logic learns correlations between execution context and policy effectiveness, anticipating recurring behavior rather than reacting to slow global counter shifts. This allows accurate, fine-grained adaptation even within a single execution phase, while preserving SD's low-overhead training methodology. More broadly, CASD transforms any microarchitectural scheme that uses context-oblivious policy arbitration into a context-aware one, without modifying the underlying policies. To demonstrate the benefits of CASD, we design DuelCeptron, a CASD prototype that uses perceptron learning to correlate contextual information with policy effectiveness. We evaluate DuelCeptron on three SD applications, showing that it consistently outperforms conventional SD with minimal storage overhead across a large and diverse set of workloads. For example, in the case study on cache replacement, DuelCeptron outperforms SD on recently disclosed Google benchmarks by 2.4% (train set) and 2.9% (test set).

## 中文摘要

动态策略仲裁是现代 CPU 的基础，因为没有单一策略能够在不同的工作负载域中实现最佳性能。 Set Dueling (SD) 在学术界和工业界广泛使用，用于在运行时在竞争策略之间进行选择，但依赖于全局的、上下文无关的计数器来做出决策，忽略基于执行上下文（例如控制和数据流信息）的更丰富的相关性。这项工作提出了上下文感知集决斗（CASD），该框架将 SD 提升为上下文感知、策略不可知的机制，用于在运行时进行细粒度的策略仲裁。 CASD 将情境学习改造为情境遗忘 SD：轻量级预测逻辑学习执行情境和政策有效性之间的相关性，预测重复出现的行为，而不是对缓慢的全球反向变化做出反应。即使在单个执行阶段，这也可以实现准确、细粒度的适应，同时保留 SD 的低开销训练方法。更广泛地说，CASD 将任何使用上下文无关策略仲裁的微架构方案转换为上下文感知方案，而无需修改底层策略。为了展示 CASD 的优势，我们设计了 DuelCeptron，这是一种 CASD 原型，它使用感知器学习将上下文信息与政策有效性相关联。我们在三个 SD 应用程序上评估了 DuelCeptron，结果表明，它在大量不同的工作负载中以最小的存储开销始终优于传统 SD。例如，在缓存替换的案例研究中，DuelCeptron 在最近披露的 Google 基准测试中的表现优于 SD 2.4%（训练集）和 2.9%（测试集）。

## 中文关键词

缓存管理；仲裁机制；集合竞争；替换策略；感知机学习；预取

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7D](index.md) · [MICRO 2026 主页](../index.md)
