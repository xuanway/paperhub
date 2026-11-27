---
title: "QuCo: Efficient and Flexible Hardware-Driven Automatic Configuration of Tile Transfers in GPUs"
description: "HPCA 2026 · GPU Kernel Optimization and Resource Sharing"
tags:
  - "HPCA2026"
  - "GPU Kernel Optimization and Resource Sharing"
---

# QuCo: Efficient and Flexible Hardware-Driven Automatic Configuration of Tile Transfers in GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: GPU Kernel Optimization and Resource Sharing。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · GPU Kernel Optimization and Resource Sharing</p>
</div>

**论文链接**：
**作者**：Nicolas Meseguer University of Murcia , daoxuan xu William & Mary , Yifan Sun William&Mary , Michael Pellauer Nvidia , José L. Abellán University of Murcia , Manuel E. Acacio Universidad de Murcia (UMU)
**会议**：HPCA 2026

---

## 中文标题

QuCo：面向 GPU 瓦片传输的高效灵活硬件驱动自动配置

## 英文摘要

The growing complexity and parallelism demands of modern GPU workloads have driven architectural innovations toward asynchronous tile transfers (ATTs) to overlap computation and data movement. While ATT units such as the NVIDIA’s Tensor Memory Accelerator (TMA) introduce high-throughput memory transfers, programmers must deal with wavefront specialization, select tile sizes, queue slots, and synchronization primitives, all of which are hardware-specific and workload-dependent. Existing GPU libraries fall short—offering limited ATT support and configurability—so developers still resort to manual exploration of this vast parameter space, which is laborious, error-prone, and fundamentally limits performance portability across GPUs. In this work, we present QuCo (Queue Configurator), a single lightweight hardware unit embedded in the GPU that fully automates the ATT configuration process. Inspired by Blackwell GPU design, QuCo includes a compact RISC-V processor, small memory structures for instructions and data, and a GPU Specification Table (GST) storing key architectural parameters. Using the GST and workload characteristics, along with built-in heuristics, QuCo computes optimal queue configurations at kernel launch. This relieves the programmer of the tedious, time-consuming task of tuning and offline profiling, while simultaneously increasing post-compilation performance portability.

## 中文摘要

现代 GPU 负载在复杂度与并行度上的需求不断增长，推动架构创新转向异步瓦片传输（ATT），以实现计算与数据搬运的重叠。尽管 NVIDIA 的张量内存加速器（TMA）等 ATT 单元带来了高吞吐的内存传输，程序员仍须处理波前特化、瓦片大小、队列槽位与同步原语的选择，而这些都是硬件相关且依赖负载的。现有 GPU 库对 ATT 的支持与可配置能力有限，开发者只能手工探索这一庞大的参数空间，既费力又易出错，并且从根本上限制了跨 GPU 的性能可移植性。为此，我们提出 QuCo（Queue Configurator），一个嵌入 GPU 的轻量级硬件单元，可完全自动化 ATT 配置过程。受 Blackwell GPU 设计的启发，QuCo 包含一个紧凑的 RISC-V 处理器、用于指令与数据的小型存储结构，以及存放关键架构参数的 GPU 规格表（GST）。QuCo 依据 GST 与负载特征，并结合内置启发式规则，在内核启动时计算出最优队列配置。这使程序员无需再进行繁琐耗时的调优与离线剖析，同时提升了编译后的性能可移植性。
