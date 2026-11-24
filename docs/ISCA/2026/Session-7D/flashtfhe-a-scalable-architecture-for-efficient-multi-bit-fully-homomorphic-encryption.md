---
title: "FlashTFHE: A Scalable Architecture for Efficient Multi-bit Fully Homomorphic Encryption"
description: "ISCA 2026 · Session 7D · FlashTFHE: A Scalable Architecture for Efficient Multi-bit Fully Homomorphic Encryption"
tags:
  - "ISCA2026"
  - "Session 7D"
  - "FHE"
---

# FlashTFHE: A Scalable Architecture for Efficient Multi-bit Fully Homomorphic Encryption

**中文标题：** FlashTFHE: 面向高效多比特全同态加密的可扩展架构

**所属 Session：** [Session 7D](index.md) · [ISCA 2026](../index.md)

**作者：** Jiaao Ma, Ceyu Xu, Ning Liang, Lisa Wu Wills

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Fully Homomorphic Encryption (FHE) enables secure processing of encrypted data in untrusted cloud environments, but its computational overhead remains a critical bottleneck. The FHE over Torus (TFHE) scheme, originally designed for Boolean gates that each require a costly bootstrapping operation, has been extended to encrypt multi-bit integers, yielding large end-to-end speedups by amortizing bootstrapping cost across many fast linear operations. However, current implementations are constrained to narrow numeric representations because securely supporting wider representations (i.e., beyond 4 bits) demands significantly larger cryptographic parameter sets. We reveal that these new parameters expose fundamental scalability barriers in state-of-the-art spatial accelerators by reshaping internal data dimensions and reuse patterns: scaling computation throughput causes severe memory bandwidth bottlenecks, mismatched data reuse patterns reduce hardware utilization, and buffering massive intermediate states becomes area-prohibitive. To address this, we introduce FlashTFHE, an accelerator featuring a temporal data reuse strategy. By time-multiplexing on-chip key data across parallel bootstrappings, FlashTFHE decouples computational throughput from memory bandwidth constraints. This architecture enables the use of highly efficient functional units and leverages adaptive batching to maximize utilization. FlashTFHE efficiently supports up to 10-bit ciphertexts, achieving speedups of up to 2529× over CPUs, 1320× over GPUs, and 7× over the state-of-the-art TFHE accelerator.

## 中文摘要

全同态加密（FHE）使在不可信云环境中安全处理加密数据成为可能，但其计算开销仍是关键瓶颈。环面全同态加密（TFHE）方案最初针对布尔门设计，每个门都需要一次昂贵的自举（bootstrapping）操作；该方案已被扩展用于加密多比特整数，通过将自举成本分摊到许多快速线性操作上，带来可观的端到端加速。然而，当前实现受限于较窄的数值表示，因为安全地支持更宽的表示（即超过 4 比特）需要显著更大的密码参数集。我们揭示，这些新参数通过重塑内部数据维度和重用模式，暴露了最先进空间加速器的根本可扩展性障碍：提升计算吞吐量会引发严重的内存带宽瓶颈；不匹配的数据重用模式会降低硬件利用率；缓冲海量中间状态在面积上变得不可承受。为解决这一问题，我们提出 FlashTFHE，一种采用时间数据重用策略的加速器。通过将片上关键数据在多个并行自举之间进行时分复用，FlashTFHE 将计算吞吐量与内存带宽约束解耦。该架构能够使用高效的功能单元，并利用自适应批处理最大化利用率。FlashTFHE 可高效支持最多 10 比特的密文，相比 CPU 实现最高 2529× 的加速，相比 GPU 实现 1320× 的加速，相比最先进的 TFHE 加速器实现 7× 的加速。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7D](index.md) · [返回 ISCA 2026](../index.md)
