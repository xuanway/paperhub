---
title: "MNEMOS: A GPU-based TFHE Acceleration Framework with Memory Access Optimization"
description: "ISCA 2026 · Session 7D · MNEMOS: A GPU-based TFHE Acceleration Framework with Memory Access Optimization"
tags:
  - "ISCA2026"
  - "Session 7D"
  - "FHE"
---

# MNEMOS: A GPU-based TFHE Acceleration Framework with Memory Access Optimization

**中文标题：** MNEMOS: 面向内存访问优化的 GPU TFHE 加速框架

**所属 Session：** [Session 7D](index.md) · [ISCA 2026](../index.md)

**作者：** Junyi Zhang, Xianglong Deng, Yi Chen, Guang Fan, Lei Chen, Dian Jiao, Shengyu Fan, Zhiwei Wang, Mingzhe Zhang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Fully Homomorphic Encryption over Torus (TFHE) provides a promising approach for privacy-preserving computing by enabling computation directly on encrypted data. However, this strong security guarantee comes at the cost of enormous computational overhead compared with plaintext computation. Modern Graphics Processing Units (GPUs), equipped with thousands of parallel computing cores and high memory bandwidth, offer an attractive platform for accelerating TFHE workloads. By exploiting their massive parallelism, the latency of TFHE primitives can be significantly reduced, making privacy-preserving computing practical. Nevertheless, executing the TFHE applications on the GPU remains limited. In this paper, we propose MNEMOS, a TFHE acceleration framework for GPU platform, optimizing the memory access during TFHE execution. In our study, we observe that severe pipeline stalls occur during TFHE kernel execution, primarily caused by frequent memory accesses and cache misses, which significantly degrade overall performance. Moreover, the utilization of Tensor Cores (TCUs) is far from optimal. Due to the excessive memory access latency caused by frequent memory accesses, the computational throughput of TCUs cannot be fully exploited. To address these issues, we propose a memory-aware algorithmic optimization that improves reuse efficiency through data re-layout and access scheduling. In addition, we introduce a Tensor-Core-optimized FFT mapping strategy that mitigates performance degradation caused by cache misses and enhances the effective utilization of TCUs during PBS computation. Experiments demonstrate that our optimizations highly enhance the performance of TFHE-based applications by 1.96× on average and up to 2.23× in the best case.

## 中文摘要

环面全同态加密（TFHE）通过直接在加密数据上计算，为隐私保护计算提供了有前景的途径。然而，与明文计算相比，这种强大的安全保障以巨大的计算开销为代价。现代图形处理器（GPU）配备数千个并行计算核和高内存带宽，为加速 TFHE 工作负载提供了极具吸引力的平台。借助其大规模并行性，TFHE 原语的延迟可被显著降低，使隐私保护计算变得实用。尽管如此，在 GPU 上执行 TFHE 应用仍受限制。本文提出 MNEMOS，一个面向 GPU 平台的 TFHE 加速框架，优化 TFHE 执行期间的内存访问。在我们的研究中，我们观察到 TFHE 内核执行期间会出现严重的流水线停顿，主要由频繁的内存访问和缓存缺失造成，显著降低了整体性能。此外，Tensor Core（TCU）的利用率远未达到最优。由于频繁内存访问带来的过高内存访问延迟，TCU 的计算吞吐量无法被充分利用。为解决这些问题，我们提出一种内存感知的算法优化，通过数据重布局和访问调度提高重用效率。此外，我们引入一种面向 Tensor Core 优化的 FFT 映射策略，减轻缓存缺失造成的性能下降，并提升 PBS 计算期间 TCU 的有效利用率。实验表明，我们的优化使基于 TFHE 的应用性能平均提升 1.96×，最佳情况下最高提升 2.23×。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7D](index.md) · [返回 ISCA 2026](../index.md)
