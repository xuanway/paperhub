---
title: "ARC: Warp-level Adaptive Atomic Reduction in GPUs to Accelerate Differentiable Rendering"
description: "ASPLOS 2025 · Session 3B · ARC：GPU 中面向可微渲染加速的 Warp 级自适应原子归约"
tags:
  - "ASPLOS2025"
  - "Session 3B"
  - "Graphics"
---

# ARC: Warp-level Adaptive Atomic Reduction in GPUs to Accelerate Differentiable Rendering

**中文标题：** ARC：GPU 中面向可微渲染加速的 Warp 级自适应原子归约

**所属 Session：** [Session 3B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Sankeerth Durvasula (Vector Institute, University of Toronto), Adrian Zhao (Vector Institute, University of Toronto), Fan Chen (University of Toronto), Ruofan Liang (Vector Institute, University of Toronto), Pawan Kumar Sanjaya (Vector Institute, University of Toronto), Yushi Guan (Vector Institute, University of Toronto), Christina Giannoula (Vector Institute, University of Toronto), Nandita Vijaykumar (Vector Institute, University of Toronto)

**单位：** Vector Institute, University of Toronto；University of Toronto

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707238) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Differentiable rendering is widely used in emerging applications that represent any 3D scene as a model trained using gradient descent from 2D images. Recent works (e.g., 3D Gaussian Splatting) use rasterization to enable rendering photo-realistic imagery at high speeds from these learned 3D models. These rasterization-based differentiable rendering methods have been demonstrated to be very promising, providing state-of-art quality for various important tasks. However, training a model to represent a scene is still timeconsuming even on powerful GPUs. In this work, we observe that the gradient computation step during model training is a significant bottleneck due to the large number of atomic operations. These atomics overwhelm the atomic units in the L2 cache of GPUs, causing long stalls. To address this, we leverage the observations that during gradient computation: (1) for most warps, all threads atomically update the same memory locations; and (2) warps generate varying amount of atomic traffic. We propose ARC, a primitive that accelerates atomic operations based on two key ideas: First, we enable warp-level reduction at the GPU cores using registers to leverage the locality in intra-warp atomic updates. Second, we distribute atomic computation between the cores and the L2 atomic units to increase the throughput of atomic computation. We propose two implementations of ARC: ARC-HW, a hardware-based approach and ARC-SW, a software-only approach. We demonstrate significant speedups with ARC of 2.6× on average (up to 5.7×) for widely used differentiable rendering workloads.

## 中文摘要

可微渲染被广泛应用于新兴应用中，这类应用将任意 3D 场景表示为一个由 2D 图像经梯度下降训练得到的模型。近期工作（如 3D Gaussian Splatting）使用光栅化，从而能够从这些已学习的三维模型高速渲染出照片级真实感的图像。这些基于光栅化的可微渲染方法已被证明极具前景，在多种重要任务上提供了最先进的画质。然而，即使在强大的 GPU 上，训练一个用于表示场景的模型仍然十分耗时。在本工作中，我们观察到模型训练过程中的梯度计算步骤因大量原子操作而成为显著瓶颈。这些原子操作使 GPU L2 缓存中的原子单元不堪重负，造成长时间的停顿。为解决这一问题，我们利用梯度计算过程中的以下观察：(1) 对大多数 warp 而言，所有线程都以原子方式更新相同的内存位置；(2) 不同 warp 产生的原子流量各不相同。我们提出 ARC，这是一种基于两个关键思想来加速原子操作的原语：第一，我们在 GPU 核内利用寄存器实现 warp 级归约，以利用 warp 内原子更新的局部性；第二，我们在核与 L2 原子单元之间分配原子计算，以提升原子计算的吞吐量。我们提出 ARC 的两种实现：ARC-HW（基于硬件的方法）与 ARC-SW（纯软件的方法）。我们展示了 ARC 在广泛使用的可微渲染工作负载上取得显著加速，平均为 2.6×（最高达 5.7×）。

## 英文关键词

Differentiable Rendering, Atomics, Gaussian Splatting, Machine Learning, Graphics Processing Unit

## 中文关键词

可微渲染；原子操作；高斯泼溅；机器学习；图形处理器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707238)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3B](index.md) · [返回 ASPLOS 2025](../index.md)
