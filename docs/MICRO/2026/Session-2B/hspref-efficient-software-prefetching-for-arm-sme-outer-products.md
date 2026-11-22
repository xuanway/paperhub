---
title: "HSPref: Efficient Software Prefetching for ARM SME Outer-Products"
description: "MICRO 2026 · Session 2B · HSPref：面向 ARM SME 外积运算的高效软件预取"
tags:
  - "MICRO2026"
  - "Prefetching"
---

# HSPref: Efficient Software Prefetching for ARM SME Outer-Products

**中文标题：** HSPref：面向 ARM SME 外积运算的高效软件预取

**所属 Session：** [Session 2B](index.md) · [MICRO 2026](../index.md)

**作者：** Han Huang, Lanshu Huang, Xianjie Chen, Xianwei Zhang, Yutong Lu

**来源：** MICRO 2026，pp. 627–643；[DOI](https://doi.org/10.1109/MICRO67795.2026.00056)

## 英文摘要

The Scalable Matrix Extension (SME) in modern Arm processors delivers very high throughput for tensor computation. However, SME's outer-product execution model generates structured, multi-dimensional memory access patterns that are poorly handled by existing hardware and software prefetchers, leading to significant memory bottlenecks. As a result, developers often rely on software prefetching techniques. Nonetheless, existing software prefetching approaches are not well-suited for SME computation. We investigate the challenges of enabling efficient software prefetching for SME computation. Our findings show that the performance of SME software prefetching is limited by inaccurate target selection, suboptimal prefetch distances and poor alignment with the cache hierarchy. We present HSPref, a software prefetching framework that systematically bridges SME computation and cache behavior. HSPref comprises four key design modules: (1) a computation pattern analysis that identifies data access patterns and suitable prefetch targets; (2) an analytical model that determines optimal prefetch distances by jointly considering instruction pipelines and memory latency; (3) a hardware-aware instruction-injection strategy that maps prefetches to appropriate cache levels; and (4) an assembly-level pass with lightweight APIs, enabling practical integration into real-world applications. We evaluate HSPref on LX2 and Apple M4 platforms. Results show that HSPref achieves average speedups of 1.34× and 1.38×, respectively, while reducing MPKI by 23% on average and up to 51%.

## 中文摘要

现代 Arm 处理器中的可扩展矩阵扩展 (SME) 为张量计算提供非常高的吞吐量。然而，SME 的外积执行模型生成结构化的多维内存访问模式，现有的硬件和软件预取器无法很好地处理这些模式，从而导致严重的内存瓶颈。因此，开发人员经常依赖软件预取技术。尽管如此，现有的软件预取方法不太适合 SME 计算。我们研究了为 SME 计算实现高效软件预取的挑战。我们的研究结果表明，SME 软件预取的性能受到不准确的目标选择、次优预取距离以及与缓存层次结构对齐不良的限制。我们提出了 HSPref，这是一种软件预取框架，可以系统地桥接 SME 计算和缓存行为。 HSPref 包括四个关键设计模块：（1）计算模式分析，识别数据访问模式和合适的预取目标； (2)综合考虑指令流水线和内存时延来确定最佳预取距离的分析模型； (3) 硬件感知指令注入策略，将预取映射到适当的缓存级别； (4) 具有轻量级 API 的汇编级通道，可实际集成到实际应用程序中。我们在 LX2 和 Apple M4 平台上评估 HSPref。结果表明，HSPref 的平均加速分别为 1.34 倍和 1.38 倍，同时 MPKI 平均降低 23%，最高可达 51%。

## 中文关键词

ARM；可扩展矩阵扩展；软件预取；外积计算

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21548721](https://doi.org/10.5281/zenodo.21548721)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2B](index.md) · [MICRO 2026 主页](../index.md)
