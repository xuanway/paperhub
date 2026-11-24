---
title: "Fat-Tree QRAM: A High-Bandwidth Shared Quantum Random Access Memory for Parallel Queries"
description: "ASPLOS 2025 · Session 1B · Fat-Tree QRAM：面向并行查询的高带宽共享量子随机存取存储器"
tags:
  - "ASPLOS2025"
  - "Session 1B"
  - "Quantum Computing"
---

# Fat-Tree QRAM: A High-Bandwidth Shared Quantum Random Access Memory for Parallel Queries

**中文标题：** Fat-Tree QRAM：面向并行查询的高带宽共享量子随机存取存储器

**所属 Session：** [Session 1B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Shifan Xu (Yale Quantum Institute, Yale University), Alvin Lu (Yale Quantum Institute, Yale University), Yongshan Ding (Yale Quantum Institute, Yale University)

**单位：** Yale Quantum Institute, Yale University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716256) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Quantum Random Access Memory (QRAM) is a crucial architectural component for querying classical or quantum data in superposition, enabling algorithms with wide-ranging applications in quantum arithmetic, quantum chemistry, machine learning, and quantum cryptography. In this work, we introduce Fat-Tree QRAM, a novel query architecture capable of pipelining multiple quantum queries simultaneously while maintaining desirable scalings in query speed and fidelity. Specifically, Fat-Tree QRAM performs 𝑂(log(𝑁)) independent queries in 𝑂(log(𝑁)) time using 𝑂(𝑁) qubits, offering immense parallelism benefits over traditional QRAM architectures. To demonstrate its experimental feasibility, we propose modular and on-chip implementations of Fat-Tree QRAM based on superconducting circuits and analyze their performance and fidelity under realistic parameters. Furthermore, a query scheduling protocol is presented to maximize hardware utilization and access the underlying data at an optimal rate. These results suggest that Fat-Tree QRAM is an attractive architecture in a shared memory system for practical quantum computing.

## 中文摘要

量子随机存取存储器（QRAM）是在叠加态下查询经典数据或量子数据的关键体系结构组件，使算法能够广泛应用于量子算术、量子化学、机器学习与量子密码学等领域。在本工作中，我们提出 Fat-Tree QRAM，一种新颖的查询架构，能够同时流水化多个量子查询，同时在查询速度与保真度上保持良好的扩展性。具体而言，Fat-Tree QRAM 使用 𝑂(𝑁) 个量子比特、在 𝑂(log(𝑁)) 时间内完成 𝑂(log(𝑁)) 个独立查询，相比传统 QRAM 架构带来了巨大的并行性收益。为证明其实验可行性，我们提出了基于超导电路的 Fat-Tree QRAM 模块化实现与片上实现，并在真实参数下分析了它们的性能与保真度。此外，本文还提出了一种查询调度协议，以最大化硬件利用率并按最优速率访问底层数据。这些结果表明，Fat-Tree QRAM 是实用量子计算共享内存系统中一种颇具吸引力的架构。

## 英文关键词

Quantum Computing, Quantum Random Access Memory

## 中文关键词

量子计算；量子随机存取存储器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716256)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1B](index.md) · [返回 ASPLOS 2025](../index.md)
