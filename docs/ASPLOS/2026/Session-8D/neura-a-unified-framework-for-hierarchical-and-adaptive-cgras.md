---
title: "Neura: A Unified Framework for Hierarchical and Adaptive CGRAs"
description: "ASPLOS 2026 · Session 8D · Neura：面向层次化与自适应 CGRA 的统一框架"
tags:
  - "ASPLOS2026"
  - "Session 8D"
  - "Reconfigurable Architectures"
---

# Neura: A Unified Framework for Hierarchical and Adaptive CGRAs

**中文标题：** Neura：面向层次化与自适应 CGRA 的统一框架

**所属 Session：** [Session 8D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Cheng Tan (Google/ASU), Miaomiao Jiang (Shandong University), Yuqi Sun, Ruihong Yin (University of Minnesota Twin Cities), Yanghui Ou (Cornell University), Qing Zhong (Google), Lei Ju (Shandong University), Jeff Zhang (Arizona State University)

**单位：** Google/ASU；Shandong University；University of Minnesota Twin Cities；Cornell University；Google；Arizona State University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790193) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Coarse-Grained Reconfigurable Arrays (CGRAs) are a promising solution for energy-efficient acceleration across multiple application domains. Yet, CGRAs face significant scalability challenges that hinder their widespread adoption, stemming from three main concerns: (1) Mapping Scalability — existing mapping algorithms struggle to find feasible and optimal solutions as the design complexity grows; (2) Architectural Limitations — rigid mapping granularity and memory access restrict flexibility and performance; and (3) Dynamic Multi-Kernel Support — dynamic and simultaneous execution of multiple kernels are not thoroughly explored, limiting the applicability of CGRAs in complex multi-kernel scenarios. In this paper, we propose Neura, an open-source unified framework towards scalable CGRAs to address these challenges. Neura introduces a novel hierarchical spatial-temporal CGRA architecture combined with a migration-aware mapping algorithm. This combination uniquely enables dynamic resource allocation and kernel migration, addressing key scalability and utilization challenges in multikernel scenarios. Our experimental results demonstrate that Neura achieves a throughput improvement of 1.64× to 3.85× and significant higher utilization, across different scenarios over a conventional CGRA at the same scale.

## 中文摘要

粗粒度可重构阵列（Coarse-Grained Reconfigurable Arrays，CGRA）是在多个应用领域实现高能效加速的一种有前景的方案。然而，CGRA 面临显著的可扩展性挑战，阻碍了其广泛采用，这些挑战源于三个主要问题：（1）映射可扩展性——随着设计复杂度增长，现有映射算法难以找到可行且最优的解；（2）体系结构局限——僵化的映射粒度与内存访问限制了灵活性和性能；（3）动态多内核支持——多个内核的动态与同时执行尚未得到充分探索，限制了 CGRA 在复杂多内核场景中的适用性。本文提出 Neura，一个面向可扩展 CGRA 的开源统一框架，以应对这些挑战。Neura 引入了新颖的层次化时空（hierarchical spatial-temporal）CGRA 体系结构，并结合迁移感知（migration-aware）映射算法。这一组合独特地实现了动态资源分配与内核迁移，解决了多内核场景中关键的可扩展性与利用率挑战。我们的实验结果表明，在同等规模的常规 CGRA 之上，Neura 在不同的场景中实现了 1.64× 到 3.85× 的吞吐量提升以及显著更高的利用率。

## 英文关键词

Domain Specific Architecture (DSA); CoarseGrained Reconfigurable Array (CGRA)

## 中文关键词

领域专用体系结构（DSA）；粗粒度可重构阵列（CGRA）

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790193)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8D](index.md) · [返回 ASPLOS 2026](../index.md)
