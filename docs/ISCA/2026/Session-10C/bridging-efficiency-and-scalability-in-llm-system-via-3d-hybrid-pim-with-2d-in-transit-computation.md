---
title: "Bridging Efficiency and Scalability in LLM System via 3D Hybrid PIM with 2D In-Transit Computation"
description: "ISCA 2026 · Session 10C · Bridging Efficiency and Scalability in LLM System via 3D Hybrid PIM with 2D In-Transit Computation"
tags:
  - "ISCA2026"
  - "Session 10C"
  - "PIM/PNM, cont."
---

# Bridging Efficiency and Scalability in LLM System via 3D Hybrid PIM with 2D In-Transit Computation

**中文标题：** 以 3D 混合 PIM 与 2D 在途计算弥合 LLM 系统的效率与可扩展性

**所属 Session：** [Session 10C](index.md) · [ISCA 2026](../index.md)

**作者：** Hongyi Li, Songchen Ma, Huanyu Qu, Weihao Zhang, Jia Chen, Junfeng Lin, Fengbin Tu, Rong Zhao

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Large Language Models (LLMs) have transformed society, but their computational and energy needs hinder efficient inference. The memory wall, the growing processor-memory speed disparity, remains a critical bottleneck for LLM. While Process-in-Memory (PIM) architectures address this challenge by co-locating computation with memory, achieving 5-20× higher bandwidth than GPUs, existing scalable PIM solutions face critical trade-offs in flexibility, capacity, and efficiency when handling LLMs’ dynamic memory-compute patterns and operator diversity. DRAM-PIM suffers from inter-bank communication overhead despite its vector parallelism. SRAM-PIM offers sub-10ns latency for matrix operation but is constrained by limited capacity. This work introduces CompAir, a scalable PIM architecture that integrates DRAM-PIM and SRAM-PIM with hybrid bonding, enabling efficient linear computations while unlocking multi-granularity data pathways. We further develop CompAir-NoC, an advanced network-on-chip (NoC) with an embedded arithmetic logic unit that performs non-linear operations during data movement. Such a design offloads the centralized communication bottleneck in the channel level to distributed banks, simultaneously reducing communication overhead and area cost for scalability. Finally, we develop a hierarchical Instruction Set Architecture that ensures both flexibility and programmability of the hybrid PIM. Experiments show CompAir delivers 1.83–7.98× faster prefill and 1.95–6.28× faster decoding versus state-of-the-art PIM designs, with 3.52× lower energy than GPU-PIM hybrids. This work presents the first systematic exploration of hybrid DRAM-PIM and SRAM-PIM architectures with in-network computation, paving the way towards a scalable PIM system for LLM inference.

## 中文摘要

大语言模型（LLM）已经改变了社会，但其计算与能耗需求阻碍了高效推理。内存墙——处理器与内存之间日益拉大的速度差距——仍然是 LLM 的关键瓶颈。虽然存内处理（PIM）架构通过将计算与内存同址部署来应对这一挑战，可实现比 GPU 高 5-20× 的带宽，但现有的可扩展 PIM 方案在处理 LLM 动态的内存-计算模式和算子多样性时，在灵活性、容量和效率方面面临关键权衡。DRAM-PIM 尽管具备向量并行性，却受困于 bank 间通信开销。SRAM-PIM 为矩阵运算提供低于 10ns 的延迟，但受限于容量。本工作提出 CompAir，一种通过混合键合（hybrid bonding）将 DRAM-PIM 与 SRAM-PIM 集成在一起的可扩展 PIM 架构，在实现高效线性计算的同时打通了多粒度数据通路。我们进一步开发了 CompAir-NoC，一种内嵌算术逻辑单元（ALU）的先进片上网络（NoC），在数据搬移过程中执行非线性运算。这样的设计将通道层面的集中式通信瓶颈卸载到分布式 bank，在降低通信开销的同时也降低了可扩展性所需的面积成本。最后，我们开发了一套分层指令集架构，以确保混合 PIM 的灵活性与可编程性。实验表明，与最先进的 PIM 设计相比，CompAir 的预填充（prefill）快 1.83–7.98×、解码（decoding）快 1.95–6.28×，且能耗比 GPU-PIM 混合方案低 3.52×。本工作首次对带有网内计算的混合 DRAM-PIM 与 SRAM-PIM 架构进行了系统性探索，为面向 LLM 推理的可扩展 PIM 系统铺平了道路。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：Man0xbfc00380/comp-air](https://github.com/Man0xbfc00380/comp-air)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10C](index.md) · [返回 ISCA 2026](../index.md)
