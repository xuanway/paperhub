---
title: "Unlocking Pipeline Parallelism for Bootstrapping: A Pipelined Multi-Chiplet TFHE Accelerator"
description: "ISCA 2026 · Session 7D · Unlocking Pipeline Parallelism for Bootstrapping: A Pipelined Multi-Chiplet TFHE Accelerator"
tags:
  - "ISCA2026"
  - "Session 7D"
  - "FHE"
---

# Unlocking Pipeline Parallelism for Bootstrapping: A Pipelined Multi-Chiplet TFHE Accelerator

**中文标题：** 解锁自举的流水线并行：流水化的多 Chiplet TFHE 加速器

**所属 Session：** [Session 7D](index.md) · [ISCA 2026](../index.md)

**作者：** Yibo Du, Mengdi Wang, Cangyuan Li, Yinhe Han, Ying Wang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

TFHE (FHE over the Torus) is a promising fully homomorphic encryption scheme, but it suffers from significant performance overhead. Its performance is severely constrained by the n iterations of Homomorphic MUXs (HMUXs) within the bootstrapping procedure (n is an encryption parameter). To address this, prior works have proposed TFHE accelerators, which process these n iterations of HMUXs sequentially, fundamentally bottlenecking the overall throughput. In this paper, we explore the previously overlooked pipeline parallelism across HMUXs, overcoming the sequential execution bottleneck to achieve extraordinary throughput. However, unleashing this pipeline parallelism incurs extreme memory bandwidth pressure, as each of the HMUXs requires access to a bootstrapping key (BSK) represented as high-degree polynomials, and n HMUXs access different BSKs. Conventional HBM-based solutions struggle to handle the massive concurrent BSK accesses needed to sustain the across-HMUX pipeline parallelism. To address this challenge, we propose a multi-chiplet pipelined architecture, which features a distributed SRAM hierarchy to buffer all BSKs so that BSK movement over off-chip memory can be eliminated. By keeping the BSKs resident within distributed on-chip SRAMs, which we call the BSK-distributed strategy, this distributed memory hierarchy confines intensive BSK access within each chiplet, resolving simultaneous BSK access conflicts. Furthermore, this architecture enables both intra- and inter-chiplet polynomial coefficient-grained pipeline to maximize resource utilization. Another challenge arises from the inter-HMUX ciphertext transfers, which could cause frequent die-to-die communication, and this inter-die communication has higher latency than intra-die access. To address this, we propose an Interleaved-Fusion policy that fuses multiple contiguous HMUXs into groups and interleaves these groups across chiplets. As the optimal interleaved-fusion mapping varies under different encryption parameters (e.g., different iteration count n), we propose an Offline Interleaved-Fusion Scheduler with an Interleaved-Fusion Cost Model and a dynamic programming algorithm, minimizing the total execution time. Evaluation demonstrates a 3.1×–30.5× performance-per-area improvement on TFHE applications over state-of-the-art TFHE accelerators.

## 中文摘要

TFHE（环面全同态加密）是一种很有前景的全同态加密方案，但其性能开销巨大。其性能受到自举过程中 n 次同态多路复用器（HMUX）迭代的严重制约（n 为加密参数）。为此，已有工作提出了 TFHE 加速器，但它们顺序处理这 n 次 HMUX 迭代，从根本上限制了整体吞吐量。本文探索了此前被忽视的 HMUX 间流水线并行性，克服顺序执行瓶颈以实现非凡的吞吐量。然而，释放这种流水线并行性会带来极大的内存带宽压力，因为每个 HMUX 都需要访问以高次多项式表示的自举密钥（BSK），而 n 个 HMUX 访问不同的 BSK。传统基于 HBM 的方案难以应对维持 HMUX 间流水线并行所需的海量并发 BSK 访问。为应对这一挑战，我们提出一种多 chiplet 流水线架构，它采用分布式 SRAM 层次结构来缓冲所有 BSK，从而消除 BSK 在片外内存中的移动。通过将 BSK 常驻于分布式片上 SRAM 中（我们称之为 BSK 分布式策略），这种分布式存储层次将密集的 BSK 访问限制在每个 chiplet 内部，解决了同时访问 BSK 的冲突。此外，该架构还支持 chiplet 内和 chiplet 间多项式系数粒度的流水线，以最大化资源利用率。另一个挑战来自 HMUX 间的密文传输，它可能引发频繁的 die-to-die 通信，而 die 间通信的延迟高于 die 内访问。为此，我们提出一种交错融合（Interleaved-Fusion）策略，将多个连续 HMUX 融合成组，并在各 chiplet 之间交错这些组。由于最优的交错融合映射在不同加密参数（如不同的迭代次数 n）下会变化，我们提出一种离线交错融合调度器，配备交错融合成本模型和动态规划算法，以最小化总执行时间。评估表明，相比最先进的 TFHE 加速器，本方案在 TFHE 应用上实现了 3.1×–30.5× 的每面积性能提升。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7D](index.md) · [返回 ISCA 2026](../index.md)
