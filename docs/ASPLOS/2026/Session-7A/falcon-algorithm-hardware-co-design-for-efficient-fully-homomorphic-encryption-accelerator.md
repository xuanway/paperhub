---
title: "Falcon: Algorithm-Hardware Co-Design for Efficient Fully Homomorphic Encryption Accelerator"
description: "ASPLOS 2026 · Session 7A · Falcon：面向高效全同态加密加速器的算法-硬件协同设计"
tags:
  - "ASPLOS2026"
  - "Session 7A"
  - "Fully Homomorphic Encryption"
---

# Falcon: Algorithm-Hardware Co-Design for Efficient Fully Homomorphic Encryption Accelerator

**中文标题：** Falcon：面向高效全同态加密加速器的算法-硬件协同设计

**所属 Session：** [Session 7A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Liang Kong (Ant Group), Shengyu Fan (Chinese Academy of Sciences, CAS), Xianglong Deng (Chinese Academy of Sciences, CAS), Lei Chen (Ant Group), Guang Fan (Ant Group), Yilan Zhu (Ant Group), Geng Yang (Ant Group), Yisong Chang (Ant Group), Shoumeng Yan (Ant Group), Mingzhe Zhang (Ant Group)

**单位：** Ant Group；Chinese Academy of Sciences, CAS

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790160) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Fully homomorphic encryption (FHE) enables computation on encrypted data without compromising privacy, positioning it as a promising solution for secure cloud computing. However, its substantial computational overhead impedes practical deployment, prompting the development of dedicated hardware accelerators. In practice, when deploying cryptographic algorithm optimizations on FHE accelerators, hardware constraints typically such as limited memory capacity, often lead to a disparity between theoretical algorithmic advantage and achievable hardware efficiency. We present Falcon, an algorithm-hardware co-design for efficient FHE acceleration. We first conduct computational analysis of the prevalent minimum key-switching method, and propose hardware-oriented algorithmic optimizations that substantially reduce computational overhead. We then introduce further refinements to decrease the inherent inter-cluster communication overhead in multi-cluster architectures, while preserving computational advantages. By characterizing the arithmetic patterns intrinsic to primary primitives, we devise hardware-specific arithmetic fusion and functional reuse across computational units. Finally, we present a memory-adaptive strategy to effectively deploy Falcon to prior accelerators under constrained on-chip memory budgets. Experimental results demonstrate that applying our algorithm–hardware co-design delivers up to a 1.48× speedup with a negligible area overhead (only a 0.8% increase).

## 中文摘要

全同态加密（FHE）能够在不损害隐私的情况下对加密数据进行计算，使其成为安全云计算的一种有前景的解决方案。然而，其巨大的计算开销阻碍了实际部署，促使人们研发专用硬件加速器。在实践中，当在FHE加速器上部署密码算法优化时，诸如有限内存容量等硬件约束通常会导致理论算法优势与可实现的硬件效率之间出现差距。我们提出Falcon，一种用于高效FHE加速的算法-硬件协同设计。我们首先对普遍采用的极小密钥切换（minimum key-switching）方法进行计算分析，并提出面向硬件的算法优化，大幅降低计算开销。随后我们引入进一步改进，以减少多簇架构中固有的簇间通信开销，同时保持计算优势。通过刻画主要原语所固有的算术模式，我们设计了硬件特定的算术融合以及跨计算单元的功能复用。最后，我们提出一种内存自适应策略，以便在受限的片上内存预算下有效地将Falcon部署到已有的加速器上。实验结果表明，应用我们的算法-硬件协同设计可带来最高1.48×的加速，且面积开销可忽略不计（仅增加0.8%）。

## 英文关键词

Fully homomorphic encryption, efficiency, communication, accelerator, cryptography

## 中文关键词

全同态加密；效率；通信；加速器；密码学

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790160)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7A](index.md) · [返回 ASPLOS 2026](../index.md)
