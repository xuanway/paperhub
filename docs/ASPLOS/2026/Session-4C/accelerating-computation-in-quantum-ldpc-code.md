---
title: "Accelerating Computation in Quantum LDPC Code"
description: "ASPLOS 2026 · Session 4C · 加速量子 LDPC 码中的计算"
tags:
  - "ASPLOS2026"
  - "Session 4C"
  - "Quantum Error Correction"
---

# Accelerating Computation in Quantum LDPC Code

**中文标题：** 加速量子 LDPC 码中的计算

**所属 Session：** [Session 4C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jungmin Cho (Seoul National University), Hyeonseong Jeong (Seoul National University), Junpyo Kim (Seoul National University), Junhyuk Choi (Seoul National University), Juwon Hong (Seoul National University), Jangwoo Kim (Seoul National University / MangoBoost)

**单位：** Seoul National University；Seoul National University / MangoBoost

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790122) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Fault-tolerant quantum computing (FTQC) uses quantum error correction (QEC) codes to execute large-scale quantum programs on noisy quantum computers. Quantum lowdensity parity-check (qLDPC) codes are promising as they use an order of magnitude fewer qubits than widely used surface codes. However, as qLDPC codes support only a limited set of operations, they require programs to be decomposed into many qLDPC-supported operations. This prohibitively increases the execution time of FTQC applications to tens of days, hindering the practical viability of qLDPC codes. In this paper, we propose ACQC, a software–hardware codesign approach to accelerate computation in qLDPC codes, realizing the practical use of qLDPC codes for FTQC. To achieve this goal, we first introduce a novel decomposition– layout co-design that significantly reduces execution time at the cost of qubit overhead. Then, we reduce the qubit overhead by exploiting characteristics of qLDPC codes and our decomposition technique. Lastly, we reduce the qubit overhead of magic state distillation by designing an optimal qLDPC code layout. As there is currently no available hardware for qLDPC codes, we evaluate ACQC with a comprehensive simulation. The results show that ACQC achieves 4.4× speedup over the baseline qLDPC code FTQC and 18.3× qubit reduction over the surface code FTQC on average.

## 中文摘要

容错量子计算（FTQC）使用量子纠错（QEC）码在含噪量子计算机上执行大规模量子程序。量子低密度奇偶校验（qLDPC）码颇具前景，因为它们所用的量子比特数比广泛使用的表面码少一个数量级。然而，由于 qLDPC 码仅支持有限的操作集合，它们要求将程序分解为许多 qLDPC 所支持的操作。这使 FTQC 应用的执行时间被不可接受地增加到数十天，阻碍了 qLDPC 码的实际可行性。在本文中，我们提出 ACQC，一种软硬件协同设计方法，用于加速 qLDPC 码中的计算，从而实现 qLDPC 码在 FTQC 中的实用化。为实现这一目标，我们首先引入一种新颖的分解–布局协同设计，它以量子比特开销为代价显著缩短执行时间。然后，我们利用 qLDPC 码的特性以及我们的分解技术来降低量子比特开销。最后，我们通过设计最优的 qLDPC 码布局来降低魔态蒸馏的量子比特开销。由于目前尚无可用于 qLDPC 码的硬件，我们通过全面的模拟来评估 ACQC。结果表明，ACQC 平均相比基线 qLDPC 码 FTQC 取得 4.4× 的加速，并相比表面码 FTQC 减少 18.3× 的量子比特。

## 英文关键词

Fault-tolerant quantum computing; Quantum error correction; Quantum LDPC code; Quantum architecture

## 中文关键词

容错量子计算；量子纠错；量子 LDPC 码；量子体系结构

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790122)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4C](index.md) · [返回 ASPLOS 2026](../index.md)
