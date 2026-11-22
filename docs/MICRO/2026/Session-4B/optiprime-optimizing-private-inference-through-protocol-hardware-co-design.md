---
title: "OptiPrime: Optimizing Private Inference through Protocol-Hardware Co-Design"
description: "MICRO 2026 · Session 4B · OptiPrime：通过协议与硬件协同设计优化隐私推理"
tags:
  - "MICRO2026"
  - "HW-SW Co-design"
---

# OptiPrime: Optimizing Private Inference through Protocol-Hardware Co-Design

**中文标题：** OptiPrime：通过协议与硬件协同设计优化隐私推理

**所属 Session：** [Session 4B](index.md) · [MICRO 2026](../index.md)

**作者：** Jiangrui Yu, Ye Yu, Si Chen, Chenqi Lin, Wenxuan Zeng, Junfeng Fan, Mingyu Gao, Meng Li

**来源：** MICRO 2026，pp. 1428–1443；[DOI](https://doi.org/10.1109/MICRO67795.2026.00106)

## 英文摘要

Private deep neural network (DNN) inference based on hybrid homomorphic encryption (HE) and multi-party computation (MPC) can protect user data with a formal guarantee, but at the cost of significant latency overhead due to HE. Customized HE accelerators have been proposed and have achieved orders-of-magnitude speedup for individual HE operations. However, when directly applying a commercial HE accelerator to state-of-the-art HE-MPC frameworks, we observe only limited end-to-end performance gain. This is because HE-MPC frameworks often require wireless transmission of input and output ciphertexts for each HE operation, leading to a severe network communication bottleneck. To overcome this challenge, we introduce OptiPrime, a protocol-hardware co-optimization framework for efficient private DNN inference. OptiPrime features a novel HE protocol for convolutions that substantially reduces the number of transmitted output ciphertexts and mitigates the network communication bottleneck. Meanwhile, as the new protocol introduces complex computation for fewer output ciphertexts, we observe new memory access challenges due to a high volume of weight plaintexts and intermediate ciphertexts. Hence, we further propose a lightweight compression system for the weight plaintexts, reducing memory traffic by 10×, as well as a specialized dataflow to maximize on-chip data reuse of intermediate ciphertexts. Extensive experiments show that our framework outperforms the Cheetah baseline by at most 5.7× on CPUs and 4.2× with an accelerator.

## 中文摘要

基于混合同态加密 (HE) 和多方计算 (MPC) 的私有深度神经网络 (DNN) 推理可以通过形式保证保护用户数据，但代价是 HE 带来的显着时延开销。定制的 HE 加速器已经被提出，并且已经为各个 HE 操作实现了数量级的加速。然而，当直接将商业 HE 加速器应用于最先进的 HE-MPC 框架时，我们仅观察到有限的端到端性能增益。这是因为HE-MPC框架通常需要无线传输每个HE操作的输入和输出密文，导致严重的网络通信瓶颈。为了克服这一挑战，我们引入了 OptiPrime，一种用于高效私有 DNN 推理的协议硬件协同优化框架。 OptiPrime 采用新颖的 HE 卷积协议，可大幅减少传输的输出密文数量并缓解网络通信瓶颈。同时，由于新协议为更少的输出密文引入了复杂的计算，我们观察到由于大​​量的权重明文和中间密文而带来的新的内存访问挑战。因此，我们进一步提出了一种用于权重明文的轻量级压缩系统，将内存流量减少了 10 倍，以及一个专门的数据流，以最大限度地提高中间密文的片上数据重用。大量实验表明，我们的框架在 CPU 上的性能比 Cheetah 基线的性能最多高出 5.7 倍，在加速器上的性能比 Cheetah 基线高 4.2 倍。

## 中文关键词

隐私推理；同态加密；多方计算；硬件加速；协议与硬件协同设计

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 4B](index.md) · [MICRO 2026 主页](../index.md)
