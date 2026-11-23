---
title: "Neo: Towards Efficient Fully Homomorphic Encryption Acceleration using Tensor Core"
description: "ISCA 2025 · Session 1B · Neo: 基于张量核心的高效FHE加速"
tags:
  - "ISCA2025"
  - "Session 1B"
  - "Crypto & Fully Homomorphic Encryption"
---

# Neo: Towards Efficient Fully Homomorphic Encryption Acceleration using Tensor Core

**中文标题：** Neo: 基于张量核心的高效FHE加速

**所属 Session：** [Session 1B](index.md) · [ISCA 2025](../index.md)

**作者：** Dian Jiao, Xianglong Deng, Zhiwei Wang, Shengyu Fan, Yi Chen, Dan Meng, Rui Hou, Mingzhe Zhang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731408) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Fully Homomorphic Encryption (FHE) is an emerging cryptographic technique for privacy-preserving computation, which enables computations on the encrypted data. Nonetheless, the massive computational demands of FHE prevent its further application to real-world workloads. To tackle this problem, several studies focus on the ASIC-based acceleration for FHE. However, the rapid evolution of FHE algorithms poses challenges to the generality of ASIC accelerator design. By contrast, a number of works rely on GPGPUs for FHE accelerations, due to the high parallelism and flexibility provided by GPGPUs.

In this work, we propose a GPGPU-based acceleration solution that supports the Cheon-Kim-Kim-Song (CKKS) scheme by further exploiting Tensor Core(TCU) capabilities. In our study, we first analyze the FHE applications based on GPGPUs and emphasize the poor data reuse of some FHE kernels. Subsequently, we highlight the inefficient usage of TCUs due to the unused FP64 components. To address these issues, we propose a novel FHE acceleration solution based on GPGPU named Neo, which features: 1) algorithmic optimizations that transform scalar multiplication and element-wise multiplication into matrix multiplication; 2) data layout optimizations for FHE kernels to optimize for matrix multiplications; 3) Accelerating matrix multiplication with the floating-point components in TCUs to leverage the strengths of various components within the GPU. Experimental results demonstrate that within NVIDIA A100 GPGPU, Neo outperforms TensorFHE by 3.28×.

## 中文摘要

全同态加密（FHE）是一种新兴的隐私保护计算密码技术，可以对加密数据进行计算。尽管如此，FHE 的大量计算需求阻碍了其进一步应用于现实世界的工作负载。为了解决这个问题，一些研究重点关注基于 ASIC 的 FHE 加速。然而，FHE算法的快速发展对ASIC加速器设计的通用性提出了挑战。相比之下，由于 GPGPU 提供的高并行性和灵活性，许多工作依赖 GPGPU 进行 FHE 加速。在这项工作中，我们提出了一种基于 GPGPU 的加速解决方案，通过进一步利用 Tensor Core（TCU）功能来支持 Cheon-Kim-Kim-Song（CKKS）方案。

在我们的研究中，我们首先分析了基于 GPGPU 的 FHE 应用，并强调了一些 FHE 内核的数据重用性较差。随后，我们强调由于未使用 FP64 组件而导致 TCU 使用效率低下。为了解决这些问题，我们提出了一种基于 GPGPU 的新型 FHE 加速解决方案 Neo，其特点是：1）算法优化，将标量乘法和逐元素乘法转换为矩阵乘法； 2) FHE 内核的数据布局优化，以优化矩阵乘法； 3) 利用 TCU 中的浮点组件加速矩阵乘法，以充分利用 GPU 中各种组件的优势。实验结果表明，在 NVIDIA A100 GPGPU 中，Neo 的性能优于 TensorFHE 3.28 倍。

## 英文关键词

Fully Homomorphic Encryption, GPGPU, CKKS, Tensor Core

## 中文关键词

全同态加密, 通用图形处理器, CKKS方案, 张量核心

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731408)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 1B](index.md) · [返回 ISCA 2025](../index.md)
