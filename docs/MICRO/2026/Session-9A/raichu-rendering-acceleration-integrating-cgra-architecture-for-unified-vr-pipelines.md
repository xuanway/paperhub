---
title: "RAICHU: Rendering Acceleration Integrating CGRA arcHitecture for Unified VR Pipelines"
description: "MICRO 2026 · Session 9A · RAICHU：融合 CGRA 架构实现统一 VR 流水线的渲染加速"
tags:
  - "MICRO2026"
  - "Reconfigurable Computing"
---

# RAICHU: Rendering Acceleration Integrating CGRA arcHitecture for Unified VR Pipelines

**中文标题：** RAICHU：融合 CGRA 架构实现统一 VR 流水线的渲染加速

**所属 Session：** [Session 9A](index.md) · [MICRO 2026](../index.md)

**作者：** Yanzhou Tang, Haiyu Wang, Cheng Tan, Sai Qian Zhang

**来源：** MICRO 2026，pp. 3226–3242；[DOI](https://doi.org/10.1109/MICRO67795.2026.00217)

## 英文摘要

Virtual reality (VR) systems often execute multiple tasks concurrently, among which rendering typically dominates overall execution time. This computational dominance poses a fundamental challenge, as the system must simultaneously deliver high visual fidelity and maintain real-time frame rates, both essential for achieving responsive and immersive user interaction. Ray tracing and neural rendering such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) each offer distinct tradeoffs between performance and fidelity, which in turn motivates the shift towards hybrid rendering in modern VR pipelines. However, the diverse workloads within these pipelines stress different resources, and typical edge devices lack the architectural capability to support all of them efficiently. We present RAICHU, a Rendering Acceleration Integrating CGRA arcHitecture for Unified VR Pipelines that directly ad- dresses this challenge via a comprehensive software-hardware co- design. At the software level, a reconfigurable dataflow toolchain maps these heterogeneous kernels onto the CGRA and optimizes their dataflow. At the hardware level, a heterogeneous CGRA is co-designed with the compiler, addressing the inherent limitations of dataflow architectures in handling memory bound tasks. To our knowledge, RAICHU is the first rendering framework to accelerate multiple rendering pipelines within a single architec- ture. Evaluation shows up to 109.65× higher performance than NVIDIA Jetson Orin NX and 12.33× better energy efficiency than other unified rendering accelerators.

## 中文摘要

虚拟现实 (VR) 系统通常同时执行多个任务，其中渲染通常主导整个执行时间。这种计算优势带来了根本性的挑战，因为系统必须同时提供高视觉保真度并保持实时帧速率，这对于实现响应式和沉浸式用户交互至关重要。光线追踪和神经渲染（例如神经辐射场 (NeRF) 和 3D 高斯溅射 (3DGS)）各自在性能和保真度之间提供了独特的权衡，这反过来又推动了现代 VR 管道向混合渲染的转变。然而，这些管道中的不同工作负载对不同的资源产生压力，并且典型的边缘设备缺乏有效支持所有这些工作负载的架构能力。我们推出了 RAICHU，一种集成 CGRA 架构的渲染加速统一 VR 管道，通过全面的软件硬件协同设计直接应对这一挑战。在软件层面，可重新配置的数据流工具链将这些异构内核映射到 CGRA 并优化其数据流。在硬件层面，异构CGRA与编译器共同设计，解决了数据流架构在处理内存限制任务方面的固有局限性。据我们所知，RAICHU 是第一个在单一架构中加速多个渲染管道的渲染框架。评估显示，性能比 NVIDIA Jetson Orin NX 高出 109.65 倍，能效比其他统一渲染加速器高出 12.33 倍。

## 中文关键词

虚拟现实；渲染；三维高斯泼溅；神经辐射场；光线追踪；粗粒度可重构阵列

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21537289](https://doi.org/10.5281/zenodo.21537289)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9A](index.md) · [MICRO 2026 主页](../index.md)
