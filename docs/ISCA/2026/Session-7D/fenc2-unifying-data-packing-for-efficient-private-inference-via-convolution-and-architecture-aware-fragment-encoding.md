---
title: "FEnc²: Unifying Data Packing for Efficient Private Inference via Convolution and Architecture-Aware Fragment Encoding"
description: "ISCA 2026 · Session 7D · FEnc²: Unifying Data Packing for Efficient Private Inference via Convolution and Architecture-Aware Fragment Encoding"
tags:
  - "ISCA2026"
  - "Session 7D"
  - "FHE"
---

# FEnc²: Unifying Data Packing for Efficient Private Inference via Convolution and Architecture-Aware Fragment Encoding

**中文标题：** FEnc²: 通过卷积与架构感知片段编码统一数据打包以实现高效隐私推理

**所属 Session：** [Session 7D](index.md) · [ISCA 2026](../index.md)

**作者：** Ran Ran, Zhaoting Gong, Nuo Xu, Yuanchao Xu, Fan Yao, Wujie Wen

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Fully Homomorphic Encryption (FHE) enables privacy-preserving machine learning but incurs extreme computational and memory overhead. These costs stem not only from slow low-level primitives such as Number Theoretic Transform (NTT), rotation, and key-switching, but also from inefficient ciphertext packing at the application level. Existing packing strategies typically preserve either neighboring data elements or feature-grouping information, but not both, leading to wasted ciphertext slots, excessive rotations, and inflated ciphertext counts. We propose FEnc², a unified and principled fragment-based encoding framework that optimizes slot utilization, rotation complexity, and ciphertext density for CKKS-based private convolutional neural network inference. Rather than applying static or layer-isolated heuristics, FEnc² introduces (1) Conv-aware Encoding, which analytically selects an optimal fragment (block) size to decouple spatial dependencies and jointly minimize inner–outer rotations across layers, and (2) Arch-aware Ct Compression, which dynamically restores ciphertext density after feature- or channel-reduction layers. Together, these transformations reshape encrypted workload structure, reducing homomorphic operations by one to two orders of magnitude. With full memory capacity utilized (i.e., at maximum batch size), FEnc² achieves end-to-end latency speedups over the state-of-the-art Orion of up to 228.83× (GPU) and 226.06× (CPU) for LeNet (MNIST), and up to 4.55× (GPU) and 9.43× (CPU) for MobileNet (ImageNet). Importantly, FEnc² is hardware-agnostic but architecturally transformative: by optimizing encrypted tensor layout before execution, it reduces ciphertext count and workload pressure on hardware, complementing primitive-level optimizations (e.g., NTT/keyswitch accelerators). This demonstrates that application-level data layout is a first-order architectural design dimension for encrypted inference and a critical enabler for next-generation FHE systems.

## 中文摘要

全同态加密（FHE）使隐私保护机器学习成为可能，但会带来极高的计算与内存开销。这些代价不仅源于数论变换（NTT）、旋转和密钥切换等缓慢的底层原语，也源于应用层面低效的密文打包。现有打包策略通常要么保留相邻数据元素，要么保留特征分组信息，而无法兼顾两者，导致密文槽位浪费、旋转过多和密文数量膨胀。我们提出 FEnc²，一个统一且有原则的、基于片段的编码框架，针对基于 CKKS 的隐私卷积神经网络推理优化槽位利用率、旋转复杂度和密文密度。FEnc² 不再采用静态或按层孤立的启发式方法，而是引入：(1) 卷积感知编码，它以解析方式选择最优片段（块）大小，以解耦空间依赖关系，并联合最小化跨层的内外旋转；(2) 架构感知密文压缩，它在特征缩减或通道缩减层之后动态恢复密文密度。这些变换共同重塑了加密工作负载的结构，将同态操作减少一到两个数量级。在内存容量充分利用（即在最大批大小）时，FEnc² 相比最先进的 Orion，在 LeNet（MNIST）上实现最高 228.83×（GPU）和 226.06×（CPU）的端到端延迟加速，在 MobileNet（ImageNet）上实现最高 4.55×（GPU）和 9.43×（CPU）的加速。重要的是，FEnc² 与硬件无关，却带来架构层面的变革：通过在执行前优化加密张量的布局，它减少了密文数量和对硬件的负载压力，与（NTT/密钥切换加速器等）原语级优化相辅相成。这表明应用级数据布局是加密推理的一阶架构设计维度，也是下一代 FHE 系统的关键使能因素。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7D](index.md) · [返回 ISCA 2026](../index.md)
