---
title: "WarpDrive: GPU-Based Fully Homomorphic Encryption Acceleration Leveraging Tensor and CUDA Cores"
description: "HPCA 2025 · The Poker Face of FHE"
tags:
  - "HPCA2025"
  - "The Poker Face of FHE"
---

# WarpDrive: GPU-Based Fully Homomorphic Encryption Acceleration Leveraging Tensor and CUDA Cores

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Poker Face of FHE。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Poker Face of FHE</p>
</div>

**论文链接**：
**作者**：Guang Fan (Ant Group), Mingzhe Zhang (Ant Group), Fangyu Zheng (University of Chinese Academy of Sciences), Shengyu Fan (Institute of Information Engineering, Chinese Academy of Sciences), Tian Zhou (University of Chinese Academy of Sciences), Xianglong Deng (Institute of Information Engineering, Chinese Academy of Sciences), Wenxu Tang (University of Chinese Academy of Sciences), Liang Kong (Ant Group), Yixuan Song (Ant Group), Shoumeng Yan (Ant Group)
**会议**：HPCA 2025

---

## 中文标题

WarpDrive：利用张量核心与 CUDA 核心的基于 GPU 的全同态加密加速

## 英文摘要

The application of Fully Homomorphic Encryption (FHE) is rapidly gaining traction as a means to maintain data confidentiality while performing computations on encrypted data. Given the accessibility and computational power, GPUs hold promise for significantly accelerating FHE operations. However, existing GPU-based acceleration solutions face several formidable challenges, notably the extensive occurrence of pipeline stalls induced by memory access and suboptimal harnessing of GPU hardware. This paper presents WarpDrive, a comprehensive framework for GPU-based FHE acceleration. Through sophisticated computation decomposition and fine-grained memory access design, WarpDrive significantly reduces the number of instructions by 73% and pipeline stalls by 86% compared to the state-of-the-art solution. Additionally, WarpDrive features a framework that supports the concurrent utilization of CUDA Cores and Tensor Cores within the NTT operation, for the first time, achieving performance that surpasses that of any single type of processing unit. Furthermore, we fully exploit the intra-ciphertext parallelism to elevate both computation and memory utilization, achieving up to 2.12× improvements without the need for ciphertext batching. Experimental results demonstrate that our optimizations highly enhance the performance of homomorphic operations. On an NVIDIA A100 GPU, WarpDrive achieves a throughput of 1218 KOPS for NTT and 305 KOPS for homomorphic multiplication, outperforming the state-of-the-art GPU solution (TensorFHE) by factors of 13.4× and 3.5×, respectively. For the specific FHE workload, even under a much smaller batch size, our approach achieves 2.8× the performance of TensorFHE.

## 中文摘要

全同态加密（FHE）的应用正迅速普及，它可以在对加密数据执行计算的同时保持数据机密性。凭借其易获得性与计算能力，GPU 有望显著加速 FHE 操作。然而现有的基于 GPU 的加速方案面临若干严峻挑战，尤其是内存访问引起的大量流水线停顿以及对 GPU 硬件利用不足。本文提出 WarpDrive，一个完整的基于 GPU 的 FHE 加速框架。通过精细的计算分解与细粒度内存访问设计，WarpDrive 相比最先进的方案将指令数减少 73%，将流水线停顿减少 86%。此外，WarpDrive 提供一个框架，首次支持在 NTT 操作中同时使用 CUDA 核心与张量核心，从而实现超越任何单一类型处理单元的性能。我们还充分利用密文内并行性来提升计算与内存利用率，在无需密文批处理的情况下实现最高 2.12 倍的提升。实验结果表明，我们的优化大幅提升了同态操作的性能。在 NVIDIA A100 GPU 上，WarpDrive 的 NTT 吞吐达到 1218 KOPS，同态乘法吞吐达到 305 KOPS，分别比最先进的 GPU 方案（TensorFHE）高 13.4 倍和 3.5 倍。对于特定的 FHE 负载，即使在批处理规模小得多的情况下，我们的方法也能达到 TensorFHE 的 2.8 倍性能。
