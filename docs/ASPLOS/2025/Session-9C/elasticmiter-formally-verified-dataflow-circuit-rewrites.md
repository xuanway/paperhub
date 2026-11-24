---
title: "ElasticMiter: Formally Verified Dataflow Circuit Rewrites"
description: "ASPLOS 2025 · Session 9C · ElasticMiter：形式化验证的数据流电路重写"
tags:
  - "ASPLOS2025"
  - "Session 9C"
  - "Verification & Reliability"
---

# ElasticMiter: Formally Verified Dataflow Circuit Rewrites

**中文标题：** ElasticMiter：形式化验证的数据流电路重写

**所属 Session：** [Session 9C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Ayatallah Elakhras (EPFL), Jiahui Xu (ETH Zurich), Martin Erhart (ETH Zurich), Paolo Ienne (EPFL), Lana Josipovic (ETH Zurich)

**单位：** EPFL；ETH Zurich

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715993) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Dataflow circuits have been studied for decades as a way to implement both asynchronous and synchronous designs, and, more recently, have attracted attention as the target of high-level synthesis (HLS) compilers. Yet, little is known about mechanisms to systematically transform and optimize the datapaths of the obtained circuits into functionally equivalent but simpler ones. The main challenge is that of equivalence verification: The latency-insensitive nature of dataflow circuits is incompatible with the standard notion of sequential equivalence, which prevents the direct usage of standard sequential equivalence verification strategies and hinders the development of formally verified dataflow circuit transformations in HLS. In this paper, we devise a generic framework for verifying the equivalence of latency-insensitive circuits. To showcase the practical usefulness of our verification framework, we develop a graph rewriting system that systematically transforms dataflow circuits into simpler ones. We employ our framework to verify our graph rewriting patterns and thus prove that the obtained circuits are equivalent to the original ones. Our work is the first to formally verify dataflow circuit transformations and is a foundation for building formally verified dataflow HLS compilers.

## 中文摘要

数据流电路作为实现异步与同步设计的一种方式已被研究数十年，近来又作为高层次综合（HLS）编译器的目标而受到关注。然而，对于系统化地变换并优化所得到电路的数据通路、使其成为功能等价但更简单的电路，相关机制仍知之甚少。主要挑战在于等价性验证：数据流电路的延迟不敏感特性与标准的时序等价概念不相容，这导致无法直接使用标准的时序等价验证策略，也阻碍了 HLS 中经形式化验证的数据流电路变换的发展。本文设计了一个用于验证延迟不敏感电路等价性的通用框架。为展示该验证框架的实用价值，我们开发了一个图重写系统，可系统化地将数据流电路变换为更简单的电路。我们运用该框架验证了图重写模式，从而证明所得到的电路与原始电路等价。本工作是首个对数据流电路变换进行形式化验证的工作，并为构建经形式化验证的数据流 HLS 编译器奠定了基础。

## 英文关键词

Dataflow circuits, high-level synthesis, formal verification, model checking

## 中文关键词

数据流电路；高层次综合；形式化验证；模型检验

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715993)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9C](index.md) · [返回 ASPLOS 2025](../index.md)
