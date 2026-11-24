---
title: "COMPAS: A Distributed Multi-Party SWAP Test for Parallel Quantum Algorithms"
description: "ASPLOS 2026 · Session 9B · COMPAS：一种用于并行量子算法的分布式多方 SWAP 测试"
tags:
  - "ASPLOS2026"
  - "Session 9B"
  - "Quantum & Emerging Computing"
---

# COMPAS: A Distributed Multi-Party SWAP Test for Parallel Quantum Algorithms

**中文标题：** COMPAS：一种用于并行量子算法的分布式多方 SWAP 测试

**所属 Session：** [Session 9B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Brayden Goldstein-Gelb (Brown University), Kun Liu (Yale University), John M. Martyn (Massachusetts Institute of Technology), Hengyun (Harry) Zhou (QuEra Computing Inc.), Yongshan Ding (Yale University), Yuan Liu (North Carolina State University)

**单位：** Brown University；Yale University；Massachusetts Institute of Technology；QuEra Computing Inc.；North Carolina State University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790143) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The limited number of qubits per chip remains a critical bottleneck in quantum computing, motivating the use of distributed architectures that interconnect multiple quantum processing units (QPUs). However, executing quantum algorithms across distributed systems requires careful co-design of algorithmic primitives and hardware architectures to manage circuit depth and entanglement overhead. We identify multivariate trace estimation as a key subroutine that is naturally suited for distribution, and broadly useful in tasks such as estimating Rényi entropies, virtual cooling and distillation, and certain applications of quantum signal processing. In this work, we introduce COMPAS, an architecture that realizes multivariate trace estimation across a multi-party network of interconnected modular and distributed QPUs by leveraging pre-shared entangled Bell pairs as resources. COMPAS adds only a constant depth overhead and consumes Bell pairs at a rate linear in circuit width, making it suitable for near-term hardware. Unlike other schemes, which must choose between asymptotic optimality in circuit depth or GHZ width, COMPAS achieves both at once. Additionally, we analyze network-level errors and simulate the effects of circuit-level noise on the architecture.1

## 中文摘要

单芯片上有限的量子比特数仍是量子计算的关键瓶颈，这促使人们采用互连多个量子处理单元（QPU）的分布式架构。然而，在分布式系统上执行量子算法需要仔细协同设计算法原语与硬件架构，以管理电路深度和纠缠开销。我们指出，多元迹估计是一类天然适合分布化、并且在估计 Rényi 熵、虚拟冷却与蒸馏以及量子信号处理的某些应用等任务中广泛有用的关键子程序。在本工作中，我们提出 COMPAS，一种通过利用预先共享的纠缠 Bell 对作为资源，在由模块化且分布式的 QPU 互连而成的多方网络中实现多元迹估计的架构。COMPAS 仅增加常数级深度开销，并以与电路宽度成线性的速率消耗 Bell 对，因而适合近期硬件。与其他必须在电路深度的渐近最优性或 GHZ 宽度之间做出取舍的方案不同，COMPAS 同时实现了二者。此外，我们分析了网络级错误，并模拟了电路级噪声对该架构的影响。1

## 英文关键词

Quantum computing; Distributed architectures; Entanglement distillation

## 中文关键词

量子计算；分布式架构；纠缠蒸馏

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790143)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9B](index.md) · [返回 ASPLOS 2026](../index.md)
