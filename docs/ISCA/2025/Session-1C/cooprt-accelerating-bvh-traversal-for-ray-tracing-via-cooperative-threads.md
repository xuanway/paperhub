---
title: "CoopRT: Accelerating BVH Traversal for Ray Tracing via Cooperative Threads"
description: "ISCA 2025 · Session 1C · CoopRT: 通过协作线程加速BVH遍历"
tags:
  - "ISCA2025"
  - "Session 1C"
  - "GPUs & Ray Tracing"
---

# CoopRT: Accelerating BVH Traversal for Ray Tracing via Cooperative Threads

**中文标题：** CoopRT: 通过协作线程加速BVH遍历

**所属 Session：** [Session 1C](index.md) · [ISCA 2025](../index.md)

**作者：** Yavuz Selim Tozlu, Huiyang Zhou

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731118) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Ray Tracing is a rendering technique to simulate the way light interacts with objects to create realistic images. It has become prominent thanks to the latest hardware support on Graphics Processing Units (GPUs), i.e., the Ray-Tracing (RT) unit, specially designed to accelerate ray tracing operations. Despite such hardware advances, ray tracing remains a performance bottleneck for high-performance graphics workloads, such as real-time path tracing (PT), which is an application of ray tracing where multiple bouncing rays are traced per pixel. The key reasons are (a) the costly Bounding Volume Hierarchy (BVH) traversal operation, and (b) low Single-Instruction-Multiple-Thread (SIMT) efficiency as the rays in the same warp deviate inevitably in their traversal paths.

In this work, we propose a novel architecture design for cooperative BVH traversal that exploits the parallelism present in the BVH traversal process. The key idea of our CoopRT scheme is to make use of the idle threads, either completely inactive when the ray tracing instruction is executed or partially idle due to early completion, to help the long running threads in the same warp. Specifically, we enable idle threads in a GPU warp to utilize their readily available traversal hardware to help traverse the BVH tree for the busy threads, therefore helping them finish their traversal much faster. This approach is implemented purely in hardware, requiring no changes to the programming model. We present our architecture design and show that it only involves small changes to the existing RT unit.

We evaluated CoopRT in Vulkan-sim, a cycle-level simulator, and observed up to 5.11x speedup over the baseline, with a geometric mean of 2.15x speedup at the cost of a moderate area overhead of 3.0% of the warp buffer in the RT unit. Using the energy-delay product, our CoopRT achieves an average of 2.29x improvement over the baseline.

## 中文摘要

光线追踪是一种渲染技术，通过模拟光线与物体的交互来生成真实感图像。得益于图形处理器（GPU）上专门用于加速光线追踪运算的光线追踪（RT）单元，光线追踪技术得到广泛应用。尽管已有上述硬件支持，光线追踪在高性能图形负载下仍然存在性能瓶颈，例如实时光线追踪路径追踪（PT）——该技术属于光线追踪的一类，需要为每个像素追踪多次弹射的光线。主要瓶颈来自两点：（a）包围体层次结构（BVH）遍历操作开销巨大；（b）单指令多线程（SIMT）执行效率低，同一warp内各光线的遍历路径不可避免地发生分支发散。

本文提出一种协同BVH遍历的新型架构设计，挖掘BVH遍历过程中的并行性。CoopRT方案的核心思路是复用空闲线程：这些线程或是在执行光线追踪指令时完全闲置，或是因提前完成任务而部分空闲，利用它们协助同一个warp内耗时较长的线程。具体来说，我们让GPU warp中的空闲线程使用自身可用的遍历硬件，为繁忙线程分担BVH树的遍历任务，从而加快遍历完成速度。该方案完全在硬件侧实现，无需修改编程模型。本文给出架构设计方案，仅需对现有RT单元做少量改动。

我们在周期级模拟器Vulkan-sim上对CoopRT开展评测。相比基线方案，最高可获得5.11倍加速，几何平均加速比为2.15倍；代价是RT单元内warp缓冲区仅增加3.0%的面积开销。以能量延迟积作为指标，CoopRT相比基线平均提升2.29倍。

## 英文关键词

Ray tracing, GPU, 3D graphics

## 中文关键词

光线追踪, 图形处理器, 三维图形

## 代码与研究制品

- [研究制品](https://doi.org/10.5281/zenodo.15103378)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731118)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 1C](index.md) · [返回 ISCA 2025](../index.md)
