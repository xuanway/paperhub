---
title: "GenZA: A General and Efficient Accelerator for Diverse Zero-Knowledge Proof Protocols"
description: "ISCA 2026 · Session 10D · GenZA: A General and Efficient Accelerator for Diverse Zero-Knowledge Proof Protocols"
tags:
  - "ISCA2026"
  - "Session 10D"
  - "Domain Specific Accelerators 3"
---

# GenZA: A General and Efficient Accelerator for Diverse Zero-Knowledge Proof Protocols

**中文标题：** GenZA: 面向多样化零知识证明协议的通用高效加速器

**所属 Session：** [Session 10D](index.md) · [ISCA 2026](../index.md)

**作者：** Cheng Wang, Jiangbin Dong, Mingyu Gao

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Zero-knowledge proofs (ZKPs) are widely deployed cryptographic protocols for privacy-preserving blockchains and verifiable computing. Domain-specific hardware has been proposed to accelerate its computationally expensive proof generation phase. But existing designs are limited to each single protocol and specialize in a narrow set of computational kernels, thus failing to cover the diverse algorithms that offer different desired tradeoffs for various application scenarios. Following the unified architecture design philosophy, this paper presents GenZA, a general and efficient accelerator for diverse ZKP protocols including Groth16, HyperPlonk, and Plonky2. GenZA adopts a homogeneous array of hardware units that can be flexibly reconfigured to support multiple data bitwidths from 64-bit up to 768-bit, as well as both general and special algebraic field moduli, with efficient decomposition schemes. It also incorporates a set of novel and optimized kernel mapping strategies for all the dominant kernels in the target protocols, which enable efficient execution of diverse kernels on the same hardware substrate with high resource utilization and good area efficiency. GenZA achieves two orders of magnitude speedups over CPUs, and 1.64× to 2.51× higher performance per area compared to prior ZKP accelerators, demonstrating both more general functionality support and more efficient performance across major modern ZKP protocols.

## 中文摘要

零知识证明（ZKP）是广泛应用于隐私保护区块链和可验证计算的密码学协议。人们已提出领域专用硬件来加速其计算开销高昂的证明生成阶段。但现有设计局限于单一协议，并只针对一小组计算内核进行专门化，因而无法覆盖为不同应用场景提供不同理想折中的多样化算法。遵循统一架构的设计理念，本文提出 GenZA，一款面向多种 ZKP 协议（包括 Groth16、HyperPlonk 和 Plonky2）的通用高效加速器。GenZA 采用由硬件单元组成的同构阵列，可通过灵活重构支持从 64-bit 直至 768-bit 的多种数据位宽，以及通用与专用代数域模数，并配有高效的分解方案。它还为目标协议中所有主导内核引入了一套新颖且经过优化的内核映射策略，使多种内核能够在同一硬件基底上高效执行，并具有较高的资源利用率和良好的面积效率。相比 CPU，GenZA 实现了两个数量级的加速；与先前的 ZKP 加速器相比，其单位面积性能高 1.64× 至 2.51×，在主要现代 ZKP 协议上同时展示了更通用的功能支持和更高效的性能。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10D](index.md) · [返回 ISCA 2026](../index.md)
