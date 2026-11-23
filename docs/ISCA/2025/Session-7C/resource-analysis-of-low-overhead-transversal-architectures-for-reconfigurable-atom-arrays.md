---
title: "Resource Analysis of Low-Overhead Transversal Architectures for Reconfigurable Atom Arrays"
description: "ISCA 2025 · Session 7C · 面向可重构原子阵列的低开销横向架构资源分析"
tags:
  - "ISCA2025"
  - "Session 7C"
  - "Quantum II"
---

# Resource Analysis of Low-Overhead Transversal Architectures for Reconfigurable Atom Arrays

**中文标题：** 面向可重构原子阵列的低开销横向架构资源分析

**所属 Session：** [Session 7C](index.md) · [ISCA 2025](../index.md)

**作者：** Hengyun Zhou, Casey Duckering, Chen Zhao, Dolev Bluvstein, Madelyn Cain, Aleksander Kubica, Sheng-Tao Wang, Mikhail D. Lukin

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731039) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Neutral atom arrays have recently emerged as a promising plat- form for fault-tolerant quantum computing. Based on these ad- vances, including dynamically-reconfigurable connectivity and fast transversal operations, we present a low-overhead architecture that supports the layout and resource estimation of large-scale fault-tolerant quantum algorithms. Utilizing recent advances in fault tolerance with transversal gate operations, this architecture achieves a run time speed-up on the order of the code distance 𝑑, which we find directly translates to run time improvements of large-scale quantum algorithms. 

Our architecture consists of functional building blocks of key algorithmic subroutines, including magic state factories, quantum arithmetic units, and quantum look-up tables. These building blocks are implemented using efficient transversal operations, and we de- sign space-time efficient versions of them that minimize interaction distance, thereby reducing atom move times and minimizing the vol- ume for correlated decoding. We further propose models to estimate their logical error performance. We perform resource estimation for a large-scale implementation of Shor’s factoring algorithm, one of the prototypical benchmarks for large-scale quantum algorithms, finding that 2048-bit RSA factoring can be executed with 19 million qubits in 5.6 days, for 1 ms QEC cycle times. This represents close to 50×speed-up of the run-time compared to existing estimates with similar assumptions, with no increase in space footprint.

## 中文摘要

中性原子阵列是近年兴起的、极具潜力的容错量子计算平台。依托该平台的各项进展，包括可动态重构的连接拓扑与高速横向门操作，本文提出一种低开销架构，支持大规模容错量子算法的布局规划与资源评估。该架构利用横向门容错方案，可获得与码距$d$同量级的运行时加速，这一优势能够直接转化为大规模量子算法的性能提升。

本架构由算法核心子模块构成，包括魔法态工厂、量子算术单元以及量子查找表。这些模块均采用高效横向门实现；本文设计了时空高效的版本，最小化相互作用距离，从而缩短原子移动耗时，并降低关联解码所需的时空体积。同时，本文建立模型评估其逻辑错误性能。

我们针对大规模肖尔分解算法开展资源评估，肖尔算法是大规模量子算法的经典基准。在量子纠错周期为1 ms的假设下，2048位RSA分解任务可使用1900万量子比特在5.6天内完成。在同等假设条件下，相比以往估算结果，运行时间接近提速50倍，且没有增加空间资源开销。

## 英文关键词

Quantum Computing, Quantum Error Correction, Quantum Algorithms

## 中文关键词

量子计算, 量子纠错, 量子算法

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731039)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7C](index.md) · [返回 ISCA 2025](../index.md)
