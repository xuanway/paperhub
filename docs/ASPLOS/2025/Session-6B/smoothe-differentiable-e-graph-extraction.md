---
title: "SmoothE: Differentiable E-Graph Extraction"
description: "ASPLOS 2025 · Session 6B · SmoothE：可微分的 E-Graph 抽取"
tags:
  - "ASPLOS2025"
  - "Session 6B"
  - "Compilers & Languages"
---

# SmoothE: Differentiable E-Graph Extraction

**中文标题：** SmoothE：可微分的 E-Graph 抽取

**所属 Session：** [Session 6B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yaohui Cai (Cornell University), Kaixin Yang (Cornell University), Chenhui Deng (Cornell University), Cunxi Yu (University of Maryland, College Park), Zhiru Zhang (Cornell University)

**单位：** Cornell University；University of Maryland, College Park

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707262) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

E-graphs have gained increasing popularity in compiler optimization, program synthesis, and theorem proving tasks. They enable compact representation of many equivalent expressions and facilitate transformations via rewrite rules without phase ordering limitations. A major benefit of using e-graphs is the ability to explore a large space of equivalent expressions, allowing the extraction of an expression that best meets certain optimization objectives (or cost models). However, current e-graph extraction methods often face unfavorable scalability-quality trade-offs and only support simple linear cost functions, limiting their applicability to more realistic optimization problems. In this work, we propose SmoothE, a differentiable e-graph extraction algorithm designed to handle complex cost models and optimized for GPU acceleration. More specifically, we approach the e-graph extraction problem from a probabilistic perspective, where the original discrete optimization is relaxed to a continuous differentiable form. This formulation supports any differentiable cost functions and enables efficient searching for solutions using gradient descent. We implement SmoothE in PyTorch to leverage the advancements of the modern machine learning ecosystem. Additionally, we introduce performance optimization techniques to exploit sparsity and data parallelism. We evaluate SmoothE on a variety of realistic e-graphs from five different applications using three distinct cost models, including both linear and non-linear ones. Our experiments demonstrate that SmoothE consistently achieves a favorable trade-off between scalability and solution quality.

## 中文摘要

E-graph 在编译器优化、程序合成与定理证明任务中日益流行。它们能够紧凑地表示大量等价表达式，并借助重写规则促成变换而不受阶段排序的限制。使用 E-graph 的一大好处是能够探索庞大的等价表达式空间，从而抽取最符合某些优化目标（或代价模型）的表达式。然而，当前的 E-graph 抽取方法往往面临不利的可扩展性与质量之间的权衡，并且只支持简单的线性代价函数，这限制了它们在更现实的优化问题上的适用性。在本工作中，我们提出 SmoothE，一种可微分的 E-graph 抽取算法，它面向复杂代价模型设计，并针对 GPU 加速进行了优化。更具体地说，我们从概率视角处理 E-graph 抽取问题，将原本的离散优化松弛为连续可微的形式。该表述支持任意可微代价函数，并能够利用梯度下降高效地搜索解。我们在 PyTorch 中实现 SmoothE，以借助现代机器学习生态系统的进展。此外，我们引入了利用稀疏性与数据并行性的性能优化技术。我们使用三种不同的代价模型（包括线性与非线性模型），在来自五个不同应用的多种真实 E-graph 上评估了 SmoothE。实验表明，SmoothE 始终能在可扩展性与解质量之间取得良好的权衡。

## 英文关键词

Machine learning for systems; Compilers; Programming languages; Equivalence graph

## 中文关键词

面向系统的机器学习；编译器；编程语言；等价图

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707262)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6B](index.md) · [返回 ASPLOS 2025](../index.md)
