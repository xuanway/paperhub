---
title: "Complex Tensor Core: Software-Hardware Co-Design for Accelerating Complex-Valued Neural Networks on GPUs"
description: "MICRO 2026 · Session 1A · 复数张量核：通过软硬件协同设计加速 GPU 上的复值神经网络"
tags:
  - "MICRO2026"
  - "GPU"
  - "Tensor Core"
  - "HW-SW Co-design"
---

# Complex Tensor Core: Software-Hardware Co-Design for Accelerating Complex-Valued Neural Networks on GPUs

**中文标题：** 复数张量核：通过软硬件协同设计加速 GPU 上的复值神经网络

**所属 Session：** [Session 1A](index.md) · [MICRO 2026](../index.md)

**作者：** Eunbi Jeong, Jennifer Choi, Ji Yeong Yi, Jane Rhee, Gunjae Koo, Yunho Oh, Myung Kuk Yoon

**来源：** MICRO 2026，pp. 64–81；[DOI](https://doi.org/10.1109/MICRO67795.2026.00021)

## 英文摘要

Complex-Valued Neural Networks (CVNNs) are a promising class of neural networks that are designed to process complex-valued data across their layers. At the core of CVNNs lies Complex-Valued General Matrix Multiplication (CGEMM), serving much the same purpose as GEMM in real-valued neural networks. However, CGEMM is more computationally expensive, as it requires four multiplications between the real and imaginary matrices. Although modern GPU Tensor Cores have evolved for high-performance GEMMs, they are unaware of complex values, prompting dedicated optimizations for CGEMMs. This work first identifies the challenge of computing CGEMMs on Tensor Cores. Conventionally, CGEMM uses a planar layout, where the real and imaginary values are stored in separate matrices. As each planar fragment holds either real or imaginary values, it must be fetched twice from register files to compute all four products. This leads to redundant register accesses and degrades performance. To address this, this work introduces Complex Tensor Core, an algorithm-hardware co-design that accelerates CVNNs via efficient CGEMM computation. We first propose a novel CGEMM algorithm that exploits an interleaved layout. By collocating real and imaginary values within each fragment, our design fuses two product computations into a single Tensor Core operation. This allows the same fragments to be reused to produce two output components, eliminating redundant register reads. To support this on GPUs, we present a new Tensor Core instruction, CMMA, along with a simple yet effective hardware unit, a Tensor Operand Steering unit. Across representative CVNNs, the proposed design achieves a 16.3% speedup and a 12.8% improvement in GPU energy efficiency over the planar CGEMM on a baseline GPU.

## 中文摘要

复值神经网络（CVNN）是一类有前景的神经网络，其各层处理复数数据。复数通用矩阵乘法（CGEMM）是 CVNN 的核心，作用类似于实值神经网络中的 GEMM。不过，CGEMM 需要对实部与虚部矩阵进行四次乘法，因此计算成本更高。虽然现代 GPU 张量核已针对高性能 GEMM 持续演进，但它们并不直接识别复数，因此 CGEMM 仍需专门优化。本文首先分析在张量核上计算 CGEMM 的挑战。传统 CGEMM 采用平面布局，将实部与虚部分别存入不同矩阵。由于每个平面数据片段只包含实部或虚部，为完成四个乘积，每个片段都必须从寄存器文件中读取两次，造成冗余寄存器访问与性能下降。为此，我们提出 Complex Tensor Core，通过高效 CGEMM 的算法与硬件协同设计加速 CVNN。首先提出利用交错布局的新 CGEMM 算法，将实部与虚部放在同一片段内，把两个乘积计算融合为一次张量核操作。相同片段由此可复用来生成输出的两个分量，消除冗余寄存器读取。为在 GPU 上支持这一机制，我们提出新的张量核指令 CMMA，以及简单而有效的张量操作数导向单元（Tensor Operand Steering）。在代表性 CVNN 上，相比基线 GPU 上采用平面布局的 CGEMM，该设计获得 16.3% 的性能提升和 12.8% 的 GPU 能效提升。

## 中文关键词

张量核；复值神经网络；复数通用矩阵乘法；软硬件协同设计

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1A](index.md) · [MICRO 2026 主页](../index.md)
