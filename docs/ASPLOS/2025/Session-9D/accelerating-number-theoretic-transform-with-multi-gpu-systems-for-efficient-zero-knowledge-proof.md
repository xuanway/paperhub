---
title: "Accelerating Number Theoretic Transform with Multi-GPU Systems for Efficient Zero Knowledge Proof"
description: "ASPLOS 2025 · Session 9D · 面向高效零知识证明的多 GPU 系统数论变换加速"
tags:
  - "ASPLOS2025"
  - "Session 9D"
  - "Trust"
---

# Accelerating Number Theoretic Transform with Multi-GPU Systems for Efficient Zero Knowledge Proof

**中文标题：** 面向高效零知识证明的多 GPU 系统数论变换加速

**所属 Session：** [Session 9D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Zhuoran Ji (School of Cyber Science and Technology, Shandong University), Jianyu Zhao (School of Cyber Science and Technology, Shandong University), Peimin Gao (School of Cyber Science and Technology, Shandong University), Xiangkai Yin (School of Cyber Science and Technology, Shandong University), Lei Ju (Quan Cheng Laboratory)

**单位：** School of Cyber Science and Technology, Shandong University；Quan Cheng Laboratory

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707241) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Zero-knowledge proofs validate statements without revealing any information, pivotal for applications such as verifiable outsourcing and digital currencies. However, their broad adoption is limited by the prolonged proof generation times, mainly due to two operations: Multi-Scalar Multiplication (MSM) and Number Theoretic Transform (NTT). While MSM has been efficiently accelerated using multi-GPU systems, NTT has not, due to the high inter-GPU communication overhead incurred by its permutation data access pattern. This paper identifies the necessity of multi-GPU NTT support for end-to-end proof generation. It introduces UniNTT, an NTT algorithm tailored for multi-GPU systems. The data access pattern of NTT incurs communication across all levels of the multi-GPU hierarchy (i.e., warp, thread block, GPU, and multi-GPU), complicating the implementation of multiGPU NTT. To this end, UniNTT proposes a novel, overheadfree decomposition approach that recursively decomposes an NTT into smaller NTTs, enabling all hierarchy levels execute the same NTT computations at different scales. It promotes a uniform design of NTT optimizations based on an abstract hardware model, which are then tailored and applied to different levels of the hierarchy. UniNTT not only simplifies the optimization process but also shows that optimizations typically specific to one level can also be effectively generalized to others. Experiments show that UniNTT achieves an average 4.26× speedup compared to leading NTT implementations when both are executed on an 8-GPU system.

## 中文摘要

零知识证明能够在不泄露任何信息的前提下验证陈述，对可验证外包和数字货币等应用至关重要。然而，其广泛采用受限于冗长的证明生成时间，这主要源于两项操作：多标量乘法（Multi-Scalar Multiplication，MSM）与数论变换（Number Theoretic Transform，NTT）。MSM 已借助多 GPU 系统得到高效加速，而 NTT 尚未如此，原因在于其置换式数据访问模式带来了高昂的 GPU 间通信开销。本文指出，端到端的证明生成需要多 GPU NTT 支持，并提出 UniNTT——一种为多 GPU 系统定制的 NTT 算法。NTT 的数据访问模式会在多 GPU 层次结构的所有层级（即 warp、线程块、GPU 和多 GPU）引发通信，从而使 multiGPU NTT 的实现复杂化。为此，UniNTT 提出一种新颖且无额外开销的分解方法，递归地将一个 NTT 分解为更小的 NTT，使所有层级都能在不同规模上执行相同的 NTT 计算。该方法基于抽象硬件模型推动 NTT 优化的统一设计，再将这些优化裁剪后应用于层次结构的不同层级。UniNTT 不仅简化了优化过程，还表明通常只针对某一层级的优化同样可以有效推广到其他层级。实验表明，在 8-GPU 系统上运行时，UniNTT 相比领先的 NTT 实现平均取得 4.26× 的加速。

## 英文关键词

Zero knowledge proof; number theoretic transform; multi-GPU systems

## 中文关键词

零知识证明；数论变换；多 GPU 系统

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707241)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9D](index.md) · [返回 ASPLOS 2025](../index.md)
