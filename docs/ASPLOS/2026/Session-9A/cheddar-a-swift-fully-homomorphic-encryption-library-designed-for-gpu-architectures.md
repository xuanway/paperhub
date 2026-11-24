---
title: "Cheddar: A Swift Fully Homomorphic Encryption Library Designed for GPU Architectures"
description: "ASPLOS 2026 · Session 9A · Cheddar：一个为 GPU 架构设计的 Swift 全同态加密库"
tags:
  - "ASPLOS2026"
  - "Session 9A"
  - "Systems Profiling & Optimization"
---

# Cheddar: A Swift Fully Homomorphic Encryption Library Designed for GPU Architectures

**中文标题：** Cheddar：一个为 GPU 架构设计的 Swift 全同态加密库

**所属 Session：** [Session 9A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Wonseok Choi (Seoul National University), Jongmin Kim (Seoul National University), Jung Ho Ahn (Seoul National University)

**单位：** Seoul National University

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762223) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Fully homomorphic encryption (FHE) frees cloud computing from privacy concerns by enabling secure computation on encrypted data. However, its substantial computational and memory overhead results in significantly slower performance compared to unencrypted processing. To mitigate this overhead, we present Cheddar, a high-performance FHE library for GPUs, achieving substantial speedups over previous GPU implementations. We systematically enable 32-bit FHE execution, leveraging the 32-bit integer datapath within GPUs. We optimize GPU kernels using efficient low-level primitives and algorithms tailored to specific GPU architectures. Further, we alleviate the memory bandwidth burden by adjusting common FHE operational sequences and extensively applying kernel fusion. Cheddar delivers performance improvements of 2.18–4.45× for representative FHE workloads compared to state-of-the-art GPU implementations.

## 中文摘要

全同态加密（FHE）使加密数据上的安全计算成为可能，从而让云计算摆脱隐私顾虑。然而，其巨大的计算与内存开销导致其性能相比非加密处理显著更慢。为缓解这一开销，我们提出 Cheddar，一个面向 GPU 的高性能 FHE 库，相比先前的 GPU 实现取得了大幅加速。我们系统地实现了 32 位 FHE 执行，充分利用了 GPU 内部的 32 位整数数据通路。我们使用高效的低层原语和针对特定 GPU 架构定制的算法来优化 GPU 内核。此外，我们通过调整常见的 FHE 操作序列并广泛采用内核融合，减轻了内存带宽负担。相比当前最优的 GPU 实现，Cheddar 在代表性 FHE 工作负载上带来 2.18–4.45× 的性能提升。

## 英文关键词

Fully homomorphic encryption, Cryptography, GPU, Security

## 中文关键词

全同态加密；密码学；GPU；安全

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762223)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9A](index.md) · [返回 ASPLOS 2026](../index.md)
