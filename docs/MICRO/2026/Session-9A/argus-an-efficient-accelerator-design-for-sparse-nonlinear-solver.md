---
title: "Argus: An Efficient Accelerator Design for Sparse Nonlinear Solver"
description: "MICRO 2026 · Session 9A · Argus：面向稀疏非线性求解器的高效加速器设计"
tags:
  - "MICRO2026"
---

# Argus: An Efficient Accelerator Design for Sparse Nonlinear Solver

**中文标题：** Argus：面向稀疏非线性求解器的高效加速器设计

**所属 Session：** [Session 9A](index.md) · [MICRO 2026](../index.md)

**作者：** Fangzhou Ye, Amir Ghazizadeh Ahsaei, Hao Zheng

**来源：** MICRO 2026，pp. 3243–3257；[DOI](https://doi.org/10.1109/MICRO67795.2026.00218)

## 英文摘要

Nonlinear equations are a fundamental computational primitive in many scientific and engineering applications. The Newton-Raphson method is widely used for solving nonlinear equations due to its strong convergence behavior and broad applicability. However, nonlinear solvers require repeated evaluation of the first-order partial derivatives of the nonlinear equations (i.e., the Jacobian matrix), leading to dynamic and irregular sparsity patterns across iterations. The evolving sparsity patterns require the Jacobian to be reloaded and recomputed at each iteration, reducing the effectiveness of existing accelerator designs for linear solvers and sparse-dense matrix multiplication (SpMM). In this paper, we posit that decoupling the static components from the dynamic Jacobian matrix, rather than recomputing the entire matrix at every iteration, can effectively exploit both data reuse and parallelism. Based on this insight, we propose Argus, a specialized accelerator architecture built on a Schur complement-based reformulation of the Newton-Raphson method. Specifically, we reformulate Jacobian computation through the Schur complement to decouple static and dynamic sparsity patterns from the Newton-Raphson method, reducing the reload and recomputation of the Jacobian matrix over iterations. In addition, the reformulation also converts sparse matrix-vector multiplication (SpMV) of nonlinear computations to general matrix-vector multiplication (GEMV). We further propose a modified weighted k-core decomposition method and construct a new Coupled Dependency Graph to avoid communication bottlenecks while improving the data locality for Schur complement computations. Lastly, we design a novel accelerator architecture and dataflow mapping that can support both Schur complement and GEMV computations. Our evaluation shows that Argus delivers performance speedups of 1.86 times, 5.32 times, and 5.68 times over state-of-the-art iterative solver designs Azul, LevelST, and Telos, respectively.

## 中文摘要

非线性方程是许多科学和工程应用中的基本计算原语。牛顿-拉夫森法因其强收敛性和广泛的适用性而被广泛用于求解非线性方程。然而，非线性求解器需要重复评估非线性方程的一阶偏导数（即雅可比矩阵），导致迭代过程中出现动态和不规则的稀疏模式。不断发展的稀疏模式要求在每次迭代时重新加载和重新计算雅可比行列式，从而降低了线性求解器和稀疏密集矩阵乘法 (SpMM) 的现有加速器设计的有效性。在本文中，我们假设将静态组件与动态雅可比矩阵解耦，而不是在每次迭代时重新计算整个矩阵，可以有效地利用数据重用和并行性。基于这一见解，我们提出了 Argus，这是一种基于 舒尔补重新表述 Newton-Raphson 方法而构建的专用加速器架构。具体来说，我们通过 Schur 补集重新制定雅可比行列式计算，以将静态和动态稀疏模式与牛顿-拉夫森方法解耦，从而减少迭代过程中雅可比矩阵的重新加载和重新计算。此外，重构还将非线性计算的稀疏矩阵向量乘法（SpMV）转换为通用矩阵向量乘法（GEMV）。我们进一步提出了一种改进的加权 k 核分解方法，并构造了一个新的耦合依赖图，以避免通信瓶颈，同时提高 Schur 补计算的数据局部性。最后，我们设计了一种新颖的加速器架构和数据流映射，可以支持 舒尔补和 GEMV 计算。我们的评估表明，Argus 的性能加速分别比最先进的迭代求解器设计 Azul、LevelST 和 Telos 提高了 1.86 倍、5.32 倍和 5.68 倍。

## 中文关键词

非线性求解器；牛顿拉夫逊法；舒尔补；图抽象；加速器

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 9A](index.md) · [MICRO 2026 主页](../index.md)
