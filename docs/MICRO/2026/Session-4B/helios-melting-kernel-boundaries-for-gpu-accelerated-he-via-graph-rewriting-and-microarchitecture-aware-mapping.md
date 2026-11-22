---
title: "Helios: Melting Kernel Boundaries for GPU-Accelerated HE via Graph Rewriting and Microarchitecture-Aware Mapping"
description: "MICRO 2026 · Session 4B · Helios：通过图重写与微架构感知映射消除 GPU 同态加密加速中的内核边界"
tags:
  - "MICRO2026"
  - "GPU"
  - "Cryptography"
  - "Graph Processing"
---

# Helios: Melting Kernel Boundaries for GPU-Accelerated HE via Graph Rewriting and Microarchitecture-Aware Mapping

**中文标题：** Helios：通过图重写与微架构感知映射消除 GPU 同态加密加速中的内核边界

**所属 Session：** [Session 4B](index.md) · [MICRO 2026](../index.md)

**作者：** Yi Chen, Ziyu Tang, Chao Yang, Guang Fan, Mingzhe Zhang, Meng Li

**来源：** MICRO 2026，pp. 1413–1427；[DOI](https://doi.org/10.1109/MICRO67795.2026.00105)

## 英文摘要

Homomorphic encryption (HE) enables computation on encrypted data, but its practical deployment remains limited by the high cost of real workloads. GPUs are an attractive platform for HE acceleration, yet modern FHE workloads remain strongly memory-bound because even a single ciphertext often exceeds GPU on-chip storage by one to two orders of magnitude, forcing frequent DRAM traffic. Kernel fusion is therefore essential, but existing GPU FHE systems still fail to realize its full benefit. Two obstacles dominate: Number Theoretic Transform (NTT)-containing cryptographic operators fragment the graph into small fusible regions, while naive fusion over enlarged regions often causes severe hardware inefficiency. We show that FHE programs should not be optimized through opportunistic fusion over a fixed operator graph. Instead, end-to-end execution is largely concentrated in a small set of recurring hot modules, which expose opportunities beyond local fusion. Based on this view, we present Helios, a compiler-driven GPU optimization framework for FHE that fits naturally in existing FHE compilation stacks. Helios combines FHE-specific graph rewriting with hardware-aware mapping: it treats hot modules as the optimization unit, rewrites them to defer, fold, or eliminate movable barriers and restructure dependency-heavy subgraphs, and maps the resulting fused regions efficiently to GPUs. Across representative CKKS workloads, Helios achieves 1.54x–2.26x speedup on A100-80GB and up to 2.49x on H100 over strong compiler-generated GPU baselines. On rotation-accumulation-dominated workloads, Helios on A100-80GB already outperforms a prior expert-tuned H100 result.

## 中文摘要

同态加密（HE）可以对加密数据进行计算，但其实际部署仍然受到实际工作负载的高成本的限制。 GPU 是 HE 加速的一个有吸引力的平台，但现代 FHE 工作负载仍然受到内存的严重限制，因为即使是单个密文也常常超过 GPU 片上存储一到两个数量级，从而迫使 DRAM 流量频繁流动。因此，内核融合至关重要，但现有的 GPU FHE 系统仍然无法充分发挥其优势。主要存在两个障碍：包含数论变换 (NTT) 的密码运算符将图分割成小的可融合区域，而扩大区域上的简单融合通常会导致严重的硬件效率低下。我们表明，FHE 程序不应该通过固定算子图上的机会融合来优化。相反，端到端执行主要集中在一小组重复出现的热模块中，这暴露了本地融合之外的机会。基于这一观点，我们提出了 Helios，这是一个用于 FHE 的编译器驱动的 GPU 优化框架，它自然地适合现有的 FHE 编译堆栈。 Helios 将 FHE 特定的图重写与硬件感知映射相结合：它将热模块视为优化单元，重写它们以推迟、折叠或消除可移动障碍并重构依赖重的子图，并将生成的融合区域有效地映射到 GPU。在代表性的 CKKS 工作负载中，与强大的编译器生成的 GPU 基准相比，Helios 在 A100-80GB 上实现了 1.54 倍至 2.26 倍的加速，在 H100 上实现了 2.49 倍的加速。在以旋转累积为主的工作负载上，A100-80GB 上的 Helios 的表现已经优于之前经过专家调整的 H100 结果。

## 中文关键词

同态加密；GPU 加速；图重写；内核融合；微架构感知映射

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 4B](index.md) · [MICRO 2026 主页](../index.md)
