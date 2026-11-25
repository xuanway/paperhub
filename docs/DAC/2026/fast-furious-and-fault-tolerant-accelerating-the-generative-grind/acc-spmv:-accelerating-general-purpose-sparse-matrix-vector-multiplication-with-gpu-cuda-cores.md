Acc-SpMV: Accelerating General-Purpose Sparse Matrix-Vector Multiplication with GPU CUDA Cores
Authors：
[Tang Lei](https://63dac.conference-program.com/?post_type=page&p=15&uid=8311288847492272433)，[Xin Zhikuang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5703834978487208974)，[Wang Zijian](https://63dac.conference-program.com/?post_type=page&p=15&uid=56092686361193611831)，[Zhou Chunbao](https://63dac.conference-program.com/?post_type=page&p=15&uid=32955287907243740251)，[Wang Jue](https://63dac.conference-program.com/?post_type=page&p=15&uid=0711263442376507665)，[Wang Yangang](https://63dac.conference-program.com/?post_type=page&p=15&uid=63484902463030622271)

## 中文标题

Acc-SpMV：利用 GPU CUDA Core 加速通用稀疏矩阵-向量乘法

## 英文摘要

General Sparse Matrix-Vector Multiplication (SpMV) is a fundamental kernel in scientific computing, graph analysis and deep learning. However, to fully unleash the power of CUDA cores performance, systematic optimization is required for SpMV. In this paper, we propose Acc-SpMV, a high-performance SpMV library on CUDA cores, with multiple optimizations, including data-locality-aware reordering, memory-efficient tiling , sparsity-aware load balancing and highly optimized SpMV kernel. Extensive experimental results on various NVIDIA GPU architectures with 2715 matrices show that, Acc-SpMV achieves significant performance improvements on average, 2.58x (up to 6.39x) speedup on RTX 4090, 1.91x (up to 4.92x) speedup on A800, and 1.78x (up to 8.21x) speedup on H100 over cuSPARSE designed for CUDA cores, and 1.93x (up to 15.67x) speedup on RTX 4090, 1.70x (up to 15.02x) speedup on A800, and 1.75x (up to 14.53x) speedup on H100 over DASP designed for Tensor cores.

## 中文摘要

通用稀疏矩阵-向量乘法（SpMV）是科学计算、图分析与深度学习中的基础内核。然而，要充分发挥 CUDA Core 的性能潜力，需要对 SpMV 进行系统性优化。本文提出 Acc-SpMV，一个高性能的、运行于 CUDA Core 之上的 SpMV 库，包含数据局部性感知的重排序、访存高效的 tile 划分、稀疏度感知的负载均衡以及高度优化的 SpMV 内核等多项优化。在多种 NVIDIA GPU 架构、2715 个矩阵上的大量实验结果表明，Acc-SpMV 相比面向 CUDA Core 设计的 cuSPARSE 平均取得显著性能提升：RTX 4090 上 2.58×（最高 6.39×）、A800 上 1.91×（最高 4.92×）、H100 上 1.78×（最高 8.21×）；相比面向 Tensor Core 设计的 DASP，在 RTX 4090 上加速 1.93×（最高 15.67×）、A800 上 1.70×（最高 15.02×）、H100 上 1.75×（最高 14.53×）。

## 英文关键词

GPU, SpMV, High-Performance Computing, CUDA

## 中文关键词

GPU、SpMV、高性能计算、CUDA
