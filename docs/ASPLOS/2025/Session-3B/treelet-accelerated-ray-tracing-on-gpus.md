---
title: "Treelet Accelerated Ray Tracing on GPUs"
description: "ASPLOS 2025 · Session 3B · 基于 Treelet 的 GPU 加速光线追踪"
tags:
  - "ASPLOS2025"
  - "Session 3B"
  - "Graphics"
---

# Treelet Accelerated Ray Tracing on GPUs

**中文标题：** 基于 Treelet 的 GPU 加速光线追踪

**所属 Session：** [Session 3B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yuan Hsi Chou (University of British Columbia), Tor M. Aamodt (University of British Columbia)

**单位：** University of British Columbia

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716279) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Despite advances in hardware acceleration, ray tracing use in real-time rendering is limited and often lowers frame rates, leading users such as video game players to disable the feature entirely. Prior work has shown that dividing the BVH tree into smaller subtrees (treelets) and traversing all rays that visit a treelet before switching treelets can significantly reduce memory traffic on a specialized accelerator, but there are many challenges to applying treelets to GPUs. We find that a naive treelet implementation is ineffective and propose optimizations to improve performance. Virtualized Treelet Queues consist of two main components. Ray virtualization increases the number of concurrent rays in flight to create more cache reuse opportunities by terminating raygen shaders that have already issued their trace ray instruction, reclaiming CUDA cores and allowing more raygen shaders to be executed. To take advantage of the increased concurrent rays, we propose a dynamic treelet queue architecture that dynamically switches between traversal modes to increase efficiency. We also find that performing warp repacking boosts SIMT efficiency of warps in the RT unit which is crucial to achieving good traversal performance with treelet queues. Our simulations show virtualized treelet queues achieve on average 95% speedup compared to a baseline GPU with ray tracing acceleration across all scenes in LumiBench rendered with path tracing at one sample per pixel with three max bounces per ray.

## 中文摘要

尽管硬件加速不断进步，光线追踪在实时渲染中的应用仍然有限，并且常常降低帧率，导致电子游戏玩家等用户完全禁用该功能。已有工作表明，将 BVH 树划分为更小的子树（treelet），并在切换 treelet 之前遍历所有访问该 treelet 的光线，可以在专用加速器上显著减少内存流量，但将 treelet 应用于 GPU 仍面临诸多挑战。我们发现朴素的 treelet 实现效果不佳，并提出优化以提升性能。虚拟化 Treelet 队列（Virtualized Treelet Queues）由两个主要部分组成。光线虚拟化通过终止已经发出其 trace ray 指令的 raygen shader、回收 CUDA 核并允许执行更多 raygen shader，来增加在飞行中的并发光线数量，从而创造更多缓存复用机会。为利用增加的并发光线，我们提出一种动态 treelet 队列架构，在遍历模式之间动态切换以提高效率。我们还发现，执行 warp 重打包可提升 RT 单元中 warp 的 SIMT 效率，这对于借助 treelet 队列获得良好的遍历性能至关重要。我们的仿真显示，在 LumiBench 的所有场景上，以每像素一个采样、每根光线最多三次反弹的路径追踪进行渲染时，虚拟化 treelet 队列相较于带光线追踪加速的基线 GPU 平均取得 95% 的加速。

## 英文关键词

Ray Tracing, GPU, Resource Virtualization, Hardware Acceleration

## 中文关键词

光线追踪；GPU；资源虚拟化；硬件加速

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716279)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3B](index.md) · [返回 ASPLOS 2025](../index.md)
