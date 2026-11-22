---
title: "Ray-by-Ray: Fine-Grained Resource Management for GPU Ray Tracing Units"
description: "MICRO 2026 · Session 1A · Ray-by-Ray：面向 GPU 光线追踪单元的细粒度资源管理"
tags:
  - "MICRO2026"
  - "GPU"
  - "Ray Tracing"
  - "Resource Management"
---

# Ray-by-Ray: Fine-Grained Resource Management for GPU Ray Tracing Units

**中文标题：** Ray-by-Ray：面向 GPU 光线追踪单元的细粒度资源管理

**所属 Session：** [Session 1A](index.md) · [MICRO 2026](../index.md)

**作者：** Junrui Pan, Cesar Avalos Baddouh, Kai Ze Ee, Timothy G. Rogers

**来源：** MICRO 2026，pp. 1–16；[DOI](https://doi.org/10.1109/MICRO67795.2026.00017)

## 英文摘要

Ray tracing (RT) generates photorealistic images by simulating the physical behavior of light as it interacts with surfaces in a virtual scene. In film production and high-end rendering pipelines, this technique computes global illumination, reflections, refractions, and soft shadows by tracing millions of light rays per frame and accurately modeling their bounces and attenuation. Contemporary GPUs incorporate specialized ray tracing hardware to accelerate key operations in the traversal pipeline. By accelerating these stages in hardware, the unit enables real-time ray tracing for complex scenes that previously required offline computation. However, ray tracing introduces substantial control and data divergence. Each ray may traverse a different set of nodes in the acceleration structure, encounter distinct materials, or terminate at varying depths. This irregularity reduces thread coherence and exposes a fundamental disparity between the GPU SIMT and per-thread execution model of dedicated RT units, where each ray progresses independently. In this work, we seek to validate assumptions made in open-source infrastructure and identify potential inefficiencies in resource management within the ray tracing pipeline. To address inefficiency caused by mismatches between SIMT and RT granularities, we propose Ray-by-Ray, which decomposes on-chip buffers into the granularity of individual rays and introduces lightweight management structures that enable more warps to run in parallel without increasing buffer capacity. This approach improves ray tracing unit utilization and increases memory-level parallelism. Experimental results show that Ray-by-Ray achieves an average performance improvement of 1.91x over the baseline, with an area overhead of 0.19%.

## 中文摘要

光线追踪（RT）通过模拟光与虚拟场景表面相互作用的物理行为生成逼真图像。在电影制作和高端渲染流程中，它逐帧追踪数百万条光线，精确模拟光线的反弹与衰减，从而计算全局光照、反射、折射和软阴影。现代 GPU 配备专用光线追踪硬件，加速遍历流水线中的关键操作，使过去需要离线计算的复杂场景能够实时渲染。然而，光线追踪会产生显著的控制流与数据分歧：不同光线可能遍历加速结构中的不同节点，遇到不同材质，或在不同深度终止。这种不规则性削弱了线程执行的一致性，并暴露出 GPU 的 SIMT 执行方式与专用 RT 单元逐线程执行方式之间的根本差异；在 RT 单元中，每条光线独立推进。本文验证开源基础设施中的相关假设，并识别光线追踪流水线资源管理的潜在低效之处。针对 SIMT 与 RT 执行粒度不匹配的问题，我们提出 Ray-by-Ray：将片上缓冲区细分到单条光线粒度，并引入轻量级管理结构，在不增加缓冲区容量的情况下支持更多线程束并行运行。这提高了光线追踪单元利用率与内存级并行性。实验表明，Ray-by-Ray 的平均性能达到基线的 1.91 倍，面积开销为 0.19%。

## 中文关键词

图形处理器；光线追踪；图形渲染；SIMT 执行效率

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21542536](https://doi.org/10.5281/zenodo.21542536)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 1A](index.md) · [MICRO 2026 主页](../index.md)
