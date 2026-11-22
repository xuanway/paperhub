---
title: "SPMC: Speculative Multicast for GPU Address Translation Sharing"
description: "MICRO 2026 · Session 7A · SPMC：用于 GPU 地址转换共享的推测式多播"
tags:
  - "MICRO2026"
  - "GPU"
  - "Address Translation"
---

# SPMC: Speculative Multicast for GPU Address Translation Sharing

**中文标题：** SPMC：用于 GPU 地址转换共享的推测式多播

**所属 Session：** [Session 7A](index.md) · [MICRO 2026](../index.md)

**作者：** Zengshi Wang, Zhuoyuan Yang, Wenbin Liao, Xin Yang, Xiaoyan Xiang, Jianyi Meng, Chao Fu, Jun Han

**来源：** MICRO 2026，pp. 2310–2325；[DOI](https://doi.org/10.1109/MICRO67795.2026.00159)

## 英文摘要

Address virtualization is a fundamental feature of modern GPUs, as it simplifies programming and enables flexible resource management. However, the L1 Translation Lookaside Buffer (TLB) remains a major performance bottleneck in address translation due to its high miss penalty and high miss rate. Our analysis shows that most L1 TLB misses are repeated misses, where the same page misses in multiple SMs because of page sharing. As prior techniques overlook the page sharing behavior, they are ineffective at reducing repeated misses and thus deliver only limited benefits. Based on these observations, we propose SPMC, a sharing-aware SPeculative MultiCast mechanism. SPMC predicts which SMs share a page in the L2 TLB and speculatively multicasts the translation result to them, reducing repeated TLB misses across SMs. It introduces a multi-level page sharer predictor operating at the context, kernel, and instruction granularities, respectively, where higher-level predictors achieve broad coverage through superior generalization, and lower-level predictors ensure high accuracy. SPMC also incorporates a multicast-aware replacement policy and a traffic filter to mitigate interference and congestion caused by the explosive growth of multicast traffic. Experimental results demonstrate that SPMC delivers an average performance improvement of 1.34x on the NVIDIA Ampere architecture. Moreover, when integrated with advanced TLB Probing and L1, L2 TLB Prefetch techniques, the improvement increases to 1.49x, 1.55x, and 1.39x, respectively.

## 中文摘要

地址虚拟化是现代 GPU 的基本功能，因为它简化了编程并实现了灵活的资源管理。然而，L1 转换后备缓冲器 (TLB) 由于其较高的未命中损失和较高的未命中率，仍然是地址转换中的主要性能瓶颈。我们的分析表明，大多数 L1 TLB 未命中都是重复未命中，即由于页面共享而导致多个 SM 中的同一页面未命中。由于现有技术忽略了页面共享行为，因此它们无法有效减少重复错过，因此只能带来有限的好处。基于这些观察，我们提出了 SPMC，一种共享感知的 SPeculative MultiCast 机制。 SPMC 预测哪些 SM 共享 L2 TLB 中的页面，并推测性地将转换结果多播给它们，从而减少 SM 之间重复的 TLB 丢失。它引入了分别在上下文、内核和指令粒度上运行的多级页面共享器预测器，其中较高级别的预测器通过卓越的泛化实现广泛的覆盖范围，而较低级别的预测器则确保高精度。 SPMC 还结合了多播感知替换策略和流量过滤器，以减轻多播流量爆炸性增长造成的干扰和拥塞。实验结果表明，SPMC 在 NVIDIA Ampere 架构上的平均性能提升了 1.34 倍。此外，当与先进的 TLB 探测和 L1、L2 TLB 预取技术集成时，性能提升分别达到 1.49 倍、1.55 倍和 1.39 倍。

## 中文关键词

通用 GPU 计算；地址转换；地址转换后备缓冲器；推测多播

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7A](index.md) · [MICRO 2026 主页](../index.md)
