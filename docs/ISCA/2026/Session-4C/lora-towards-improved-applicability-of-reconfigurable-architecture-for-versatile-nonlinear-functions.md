---
title: "LoRA: Towards Improved Applicability of Reconfigurable Architecture for Versatile Nonlinear Functions"
description: "ISCA 2026 · Session 4C · LoRA: Towards Improved Applicability of Reconfigurable Architecture for Versatile Nonlinear Functions"
tags:
  - "ISCA2026"
  - "Session 4C"
  - "Domain Specific Accelerators 1"
---

# LoRA: Towards Improved Applicability of Reconfigurable Architecture for Versatile Nonlinear Functions

**中文标题：** LoRA: 提升可重构架构对多样非线性函数的适用性

**所属 Session：** [Session 4C](index.md) · [ISCA 2026](../index.md)

**作者：** Yuan Dai, Guibin Zou, Yuanda Yang, Huan Lin, Jiahang Lou, Yiwen Luo, Xinyu Cai, Wenbo Yin, Wai-Shing Luk, Lingli Wang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Coarse-Grained Reconfigurable Architecture (CGRA) emerges as a competitive accelerator for computation-intensive applications. However, most CGRAs primarily focus on linear operations, which makes it challenging to efficiently support nonlinear functions that are increasingly important in emerging applications. This limitation hinders the potential of CGRAs to accelerate modern computation-intensive applications, particularly those that rely on complex nonlinear functions. In this paper, we propose several key approaches to enable CGRA to support versatile nonlinear functions. First, we develop a Chebyshev-based approximation algorithm that employs a novel segmentation strategy, along with considering the properties of the target function to identify a suitable Chebyshev polynomial for each sub-interval. Second, based on the Logarithmic Number System, we design a lightweight unit to efficiently compute the polynomials and complex operations. Finally, we develop a comprehensive end-to-end framework LoRA with architectural and compiler support for implementing nonlinear functions on the CGRA. Experimental results show that LoRA can provide efficient nonlinear function implementation and achieve 23.33× and 2.18× average performance improvements compared to an STM32H750 microcontroller unit and a state-of-the-art (SOTA) CGRA. In addition, LoRA achieves a 2.13× average energy efficiency gain compared to the SOTA CGRA.


## 中文摘要

粗粒度可重构架构（CGRA）已成为计算密集型应用的有竞争力的加速器。然而，大多数 CGRA 主要关注线性操作，这使得高效支持在新兴应用中日益重要的非线性函数颇具挑战。这一限制阻碍了 CGRA 加速现代计算密集型应用（尤其是依赖复杂非线性函数的应用）的潜力。本文提出若干关键方法，使 CGRA 能够支持多样化的非线性函数。首先，我们开发了一种基于 Chebyshev 的近似算法，采用新颖的分段策略，并结合目标函数的特性为每个子区间确定合适的 Chebyshev 多项式。其次，基于对数数制（Logarithmic Number System），我们设计了一个轻量级单元来高效计算多项式和复杂操作。最后，我们开发了一个完整的端到端框架 LoRA，提供架构和编译器支持，用于在 CGRA 上实现非线性函数。实验结果表明，LoRA 能够高效实现非线性函数，相比 STM32H750 微控制器单元和最先进（SOTA）CGRA，平均性能分别提升 23.33× 和 2.18×。此外，LoRA 相比 SOTA CGRA 实现 2.13× 的平均能效提升。

## 代码与研究制品

论文提供了 COFFA 函数融合框架的代码链接；该仓库不等同于完整 LoRA 硬件实现。

- [代码仓库：Dai-dirk/COFFA](https://github.com/Dai-dirk/COFFA)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4C](index.md) · [返回 ISCA 2026](../index.md)
