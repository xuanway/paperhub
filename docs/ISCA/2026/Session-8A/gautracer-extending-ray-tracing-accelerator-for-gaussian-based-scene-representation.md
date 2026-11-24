---
title: "GauTracer: Extending Ray Tracing Accelerator for Gaussian-based Scene Representation"
description: "ISCA 2026 · Session 8A · GauTracer: Extending Ray Tracing Accelerator for Gaussian-based Scene Representation"
tags:
  - "ISCA2026"
  - "Session 8A"
  - "Rendering"
---

# GauTracer: Extending Ray Tracing Accelerator for Gaussian-based Scene Representation

**中文标题：** GauTracer: 面向高斯场景表示的光线追踪加速器扩展

**所属 Session：** [Session 8A](index.md) · [ISCA 2026](../index.md)

**作者：** Lizhou Wu, Kunchen Zou, Yuzheng Lin, Chixiao Chen, Xiaoyang Zeng, Haozhe Zhu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Gaussian splatting has emerged as a promising paradigm in 3D vision, enabling instant scene reconstruction and photorealistic rendering. However, integrating rasterization-oriented Gaussian representations into ray tracing pipelines remains challenging. Existing ray tracing accelerators (RTAs) lack native support for Gaussian primitives, forcing reliance on software shader, which incurs significant instruction overhead, thread divergence, and excessive memory traffic. To address this, we present GauTracer, a ray tracing accelerator with efficient hardware support for Gaussian primitives. GauTracer elevates Gaussians to first-class primitives via lightweight microarchitectural extensions, including a dedicated Ray-Gauss Intersection Unit (RGIU). To improve versatility, the RGIU adopts a reconfigurable design supporting both 3D ellipsoidal and 2D planar Gaussian primitives with minimal overhead. In addition, a max-heap-based Any-Gauss-Hit Unit (AGHU) maintains a per-ray hit buffer for efficient volumetric blending of Gaussian primitives. To further optimize traversal performance, GauTracer employs a treelet-based BVH traversal scheme with a far-node pruning scheme, reducing unnecessary node visits beyond the buffer’s capacity. Simulation results based on Vulkan-Sim show that GauTracer achieves average performance improvements of 5.8× for 3D Gaussians and 7.3× for 2D Gaussians over the baseline GPU-RTA. It also enhances energy efficiency by 6.6× and 7.5×, respectively.

## 中文摘要

高斯泼溅已成为 3D 视觉中一种颇具前景的范式，能够实现即时场景重建与照片级真实感渲染。然而，将面向光栅化的高斯表示集成到光线追踪流水线中仍然具有挑战性。现有光线追踪加速器（RTA）缺乏对高斯图元的原生支持，只能依赖软件着色器，因而带来显著的指令开销、线程发散与过多的内存流量。为解决这一问题，我们提出 GauTracer，一种对高斯图元提供高效硬件支持的光线追踪加速器。GauTracer 通过轻量级微架构扩展将高斯提升为一等图元，其中包括专用的光线—高斯求交单元（RGIU）。为提升通用性，RGIU 采用可重构设计，以极小的开销同时支持 3D 椭球与 2D 平面两种高斯图元。此外，基于最大堆的任意高斯命中单元（AGHU）为每条光线维护一个命中缓冲区，以高效实现高斯图元的体渲染混合。为进一步优化遍历性能，GauTracer 采用基于树丛（treelet）的 BVH 遍历方案，并结合远节点剪枝方案，减少超出缓冲区容量之外的不必要节点访问。基于 Vulkan-Sim 的模拟结果表明，相较基线 GPU-RTA，GauTracer 对 3D 高斯平均性能提升 5.8×，对 2D 高斯提升 7.3×；能效则分别提升 6.6× 和 7.5×。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 8A](index.md) · [返回 ISCA 2026](../index.md)
