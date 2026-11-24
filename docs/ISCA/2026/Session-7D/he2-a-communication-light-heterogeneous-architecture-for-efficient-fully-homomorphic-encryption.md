---
title: "HE²: A Communication-Light Heterogeneous Architecture for Efficient Fully Homomorphic Encryption"
description: "ISCA 2026 · Session 7D · HE²: A Communication-Light Heterogeneous Architecture for Efficient Fully Homomorphic Encryption"
tags:
  - "ISCA2026"
  - "Session 7D"
  - "FHE"
---

# HE²: A Communication-Light Heterogeneous Architecture for Efficient Fully Homomorphic Encryption

**中文标题：** HE²: 面向高效全同态加密的通信轻量异构架构

**所属 Session：** [Session 7D](index.md) · [ISCA 2026](../index.md)

**作者：** Shangyi Shi, Husheng Han, Zhaoxuan Kan, Yinghao Yang, Jianan Mu, Tenghui Hua, Ge Yu, Xinyao Zheng, Ling Liang, Zidong Du, Xing Hu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

CKKS, an emerging fully homomorphic encryption (FHE) scheme, has been promising in privacy-preserving applications by enabling SIMD fixed-point computations on ciphertexts. Despite its strong security guarantees, CKKS involves both compute-intensive operators (ComOps) with high computational cost and memory-intensive operators (MemOps) with large memory footprints, making existing ASIC-based or NMP-based acceleration approaches suffer from high hardware overhead and limited efficiency. This observation motivates the integration of the architectural advantages of both paradigms into a heterogeneous xPU (ASIC)-xMU (NMP) architecture. However, in such a design, frequent and long-latency heterogeneous communication caused by the dominant keyswitch operator remains a key performance bottleneck. In this paper, we propose HE², a communication-light xPU-xMU heterogeneous FHE accelerator with dataflow graph (DFG) optimization and architecture co-design. First, we observe that the majority of communication arises at the interface between ModUp/ModDown and neighboring MemOps. To address this, we propose a DFG-level optimization framework to fully exploit the ModUp/ModDown reduction potential of the hoisting algorithm by identifying parallel keyswitch blocks and fusing them for reduced communication frequency. Second, we design an efficient heterogeneous architecture that adopts a group-level pipelined execution to effectively hide communication latency by leveraging the inherent parallelism across decomposed groups. End-to-end evaluation results show that HE² achieves 1.66× speedup and 9.23× lower EDAP (Energy-Delay-Area Product) compared to the state-of-the-art accelerator, with communication stalls accounting for only 6.67% of the total latency.

## 中文摘要

CKKS 是一种新兴的全同态加密（FHE）方案，它通过在密文上支持 SIMD 定点计算，在隐私保护应用中展现出良好前景。尽管具有强大的安全保障，CKKS 同时涉及计算成本高的计算密集型算子（ComOps）和内存占用大的访存密集型算子（MemOps），使得现有基于 ASIC 或基于 NMP 的加速方案面临硬件开销高、效率有限的问题。这一观察促使我们将两种范式的架构优势整合进一种异构的 xPU（ASIC）-xMU（NMP）架构。然而，在这种设计中，由占主导地位的密钥切换算子所引起的频繁且长延迟的异构通信仍是关键性能瓶颈。本文提出 HE²，一种通信轻量的 xPU-xMU 异构 FHE 加速器，采用数据流图（DFG）优化与架构协同设计。首先，我们观察到大部分通信发生在 ModUp/ModDown 与相邻 MemOps 之间的接口处。为此，我们提出一个 DFG 级优化框架，通过识别并融合并行的密钥切换块，充分挖掘提升（hoisting）算法在减少 ModUp/ModDown 方面的潜力，从而降低通信频率。其次，我们设计了一种高效的异构架构，采用组级流水化执行，借助分解后各组之间固有的并行性有效隐藏通信延迟。端到端评估结果表明，与最先进的加速器相比，HE² 实现了 1.66× 的加速和 9.23× 更低的 EDAP（能量-延迟-面积积），通信停顿仅占总延迟的 6.67%。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7D](index.md) · [返回 ISCA 2026](../index.md)
