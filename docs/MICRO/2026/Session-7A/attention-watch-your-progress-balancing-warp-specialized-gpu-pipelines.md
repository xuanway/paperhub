---
title: "Attention, Watch Your Progress: Balancing Warp-Specialized GPU Pipelines"
description: "MICRO 2026 · Session 7A · Attention, Watch Your Progress：平衡线程束专门化 GPU 流水线"
tags:
  - "MICRO2026"
  - "GPU"
---

# Attention, Watch Your Progress: Balancing Warp-Specialized GPU Pipelines

**中文标题：** Attention, Watch Your Progress：平衡线程束专门化 GPU 流水线

**所属 Session：** [Session 7A](index.md) · [MICRO 2026](../index.md)

**作者：** Fangjia Shen, Nicolai Oswald, Timothy G. Rogers

**来源：** MICRO 2026，pp. 2342–2356；[DOI](https://doi.org/10.1109/MICRO67795.2026.00161)

## 英文摘要

Contemporary GPU kernels for deep learning workloads, particularly attention mechanisms in transformers, employ sophisticated parallel programming techniques to maximize hardware utilization. These techniques create software pipelines that synchronize the operation of specialized hardware units such as Tensor Cores, Tensor Memory Accelerators, and SIMT cores at the warp level. However, current warp scheduling mechanisms are not designed for these new programming paradigms, leading to suboptimal performance due to imbalance and inefficient instruction issue patterns. We propose Progress-Aware Warp Scheduling (PAWS), a lightweight scheduling mechanism that adapts to modern attention kernels by leveraging pre-existing machine code information to transmit priority information to the warp scheduler. Our approach enables the warp scheduler to identify and prioritize warps executing slower program phases, thereby improving overall pipeline throughput. We demonstrate that compilers can automatically implement this mechanism, providing significant performance improvements for attention kernels on modern GPU architectures. We perform a comprehensive parameter sweep of 1800 attention implementations that represent both current and anticipated future attention kernels. PAWS consistently performs better than state-of-the-art hardware warp schedulers, delivering 28% speedup when phases are highly skewed and 15% improvement on attention configurations found in QWen3, Llama4, and Grok 1.0. RTL synthesis results indicate low hardware overhead to implement PAWS in silicon.

## 中文摘要

用于深度学习工作负载的当代 GPU 内核，特别是 Transformer 中的注意力机制，采用复杂的并行编程技术来最大限度地提高硬件利用率。这些技术创建了软件管道，可以在线程束级别同步专用硬件单元（例如张量核心、张量内存加速器和 SIMT 核心）的操作。然而，当前的线程束调度机制并不是为这些新的编程范例而设计的，导致由于不平衡和低效的指令发出模式而导致性能不佳。我们提出了进度感知线程束调度（PAWS），这是一种轻量级调度机制，通过利用预先存在的机器代码信息将优先级信息传输到线程束调度器来适应现代注意力内核。我们的方法使 warp 调度程序能够识别执行较慢程序阶段的 warp 并确定其优先级，从而提高整体管道吞吐量。我们证明编译器可以自动实现这种机制，为现代 GPU 架构上的注意力内核提供显着的性能改进。我们对 1800 个注意力实现进行了全面的参数扫描，这些实现代表了当前和预期的未来注意力内核。 PAWS 的性能始终优于最先进的硬件线程束调度器，在阶段高度倾斜时提供 28% 的加速，并且在 QWen3、Llama4 和 Grok 1.0 中发现的注意力配置方面提供 15% 的改进。 RTL 综合结果表明在硅中实现 PAWS 的硬件开销较低。

## 中文关键词

GPU 微架构；线程束调度；注意力内核；Transformer；流水线均衡

## 代码与研究制品

- 代码仓库：[https://github.com/purdue-aalp/progress_aware_warp_scheduling](https://github.com/purdue-aalp/progress_aware_warp_scheduling)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 7A](index.md) · [MICRO 2026 主页](../index.md)
