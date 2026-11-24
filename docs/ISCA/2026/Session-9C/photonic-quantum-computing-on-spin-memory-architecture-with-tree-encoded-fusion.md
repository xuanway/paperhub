---
title: "Photonic Quantum Computing on Spin Memory Architecture with Tree-Encoded Fusion"
description: "ISCA 2026 · Session 9C · Photonic Quantum Computing on Spin Memory Architecture with Tree-Encoded Fusion"
tags:
  - "ISCA2026"
  - "Session 9C"
  - "Quantum 3"
---

# Photonic Quantum Computing on Spin Memory Architecture with Tree-Encoded Fusion

**中文标题：** 基于树编码聚变的自旋存储器架构上的光子量子计算

**所属 Session：** [Session 9C](index.md) · [ISCA 2026](../index.md)

**作者：** Xiangyu Ren, Yuexun Huang, Zhemin Zhang, Yuchen Zhu, Tsung-Yi Ho, Antonio Barbalace, Zhiding Liang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Photonic quantum computer (PQC) is a promising quantum computation platform, realizing the measurement-based quantum computation (MBQC) model. In MBQC, computation proceeds by preparing a graph state, and this preparation mainly relies on fusion operations. However, fusion operations on a PQC are prone to two types of errors: fusion failure and fusion erasure. Therefore, the MBQC compiler must be carefully designed to tolerate these errors. Previous state-of-the-art MBQC compiler – OneAdapt, is tailored to all-photonic architectures and primarily address fusion failures. However, it neglects fusion erasure errors caused by photon loss, which are more detrimental than fusion failures. To address the challenge of fusion erasure, we propose a novel MBQC scheme that is based on quantum spin memory architecture. We design a tree-encoded fusion scheme that effectively suppresses erasure errors. Then, we integrate this scheme into our compiler framework, with compilation algorithms that reduce execution overhead of quantum programs. We evaluate our framework on a realistic PQC simulator across six typical quantum algorithm benchmarks with various program sizes. Our results show that the proposed tree-encoding scheme outperforms other fusion encoding schemes, and that our compilation framework outperforms OneAdapt with exponential improvement. Moreover, we demonstrate a small-scale QAOA experiment on real PQC hardware, where it outperforms the latest superconducting hardware.

## 中文摘要

光子量子计算机（PQC）是一种有前景的量子计算平台，可实现基于测量的量子计算（MBQC）模型。在 MBQC 中，计算通过制备图态来进行，而这种制备主要依赖于聚变操作。然而，PQC 上的聚变操作容易产生两类错误：聚变失败和聚变擦除。因此，MBQC 编译器必须精心设计以容忍这些错误。以往最先进的 MBQC 编译器——OneAdapt——是针对全光子架构定制的，主要处理聚变失败。然而，它忽略了由光子丢失引起的聚变擦除错误，而后者比聚变失败更具危害性。为应对聚变擦除的挑战，我们提出了一种基于量子自旋存储器架构的新型 MBQC 方案。我们设计了一种树编码聚变方案，能够有效抑制擦除错误。然后，我们将该方案集成到我们的编译器框架中，并配合减少量子程序执行开销的编译算法。我们在一个真实的 PQC 仿真器上，针对不同程序规模的六个典型量子算法基准对我们的框架进行了评估。结果表明，所提出的树编码方案优于其他聚变编码方案，并且我们的编译框架以指数级改进优于 OneAdapt。此外，我们在真实 PQC 硬件上演示了一个小规模 QAOA 实验，其表现优于最新的超导硬件。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9C](index.md) · [返回 ISCA 2026](../index.md)
