---
title: "TTP: A Hardware-Efficient Design for Precise Prefetching in Ray Tracing"
description: "ISCA 2026 · Session 8A · TTP: A Hardware-Efficient Design for Precise Prefetching in Ray Tracing"
tags:
  - "ISCA2026"
  - "Session 8A"
  - "Rendering"
---

# TTP: A Hardware-Efficient Design for Precise Prefetching in Ray Tracing

**中文标题：** TTP: 面向光线追踪精确预取的硬件高效设计

**所属 Session：** [Session 8A](index.md) · [ISCA 2026](../index.md)

**作者：** Yavuz Selim Tozlu, Anshul Naithani, Huiyang Zhou

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Ray tracing (RT) is a 3D graphics technique that offers highly realistic visuals. It is becoming prominent and accessible as GPU vendors have integrated dedicated ray tracing acceleration hardware. However, tracing millions of rays through 3D scenes consisting of high numbers of triangles in real time is challenging and requires expensive hardware. The main bottleneck in RT workloads is the expensive Bounding Volume Hierarchy (BVH) traversal task, which is a large tree structure that encodes the 3D scene. BVH traversal is a memory-bound problem, as the GPU threads spend most of their time reading tree node data from memory. In this work, we attack the memory latency bottleneck of ray tracing through prefetching. We propose a novel hardware prefetcher, named Tree Traversal Prefetcher (TTP), for ray tracing. The main idea is to leverage the existing tree traversal stack in the RT units for highly accurate prefetching. In particular, TTP prefetches nodes using the addresses already available on the hardware traversal stacks of each thread. For DFS (Depth-first search) based traversal, prefetches are generated when nodes are being popped consecutively from the traversal stack, potentially corresponding to upward traversal through the tree. We evaluate TTP on a cycle-level simulator, Vulkan-sim 2.0, and show that it achieves 1.48x speedup on average (up to 1.89x) compared to the baseline, with nearly negligible hardware overhead. TTP achieves 98.92% average L1 accuracy, which is the ratio of the prefetched blocks being actually referenced by demand loads. The coverage, computed as the ratio of L1 miss reduction over baseline L1 misses, is 31.54%, correlating well with the achieved speedup.

## 中文摘要

光线追踪（RT）是一种能够提供高度逼真视觉效果的三维图形技术。随着 GPU 厂商集成专用的光线追踪加速硬件，它正日益普及并变得易于使用。然而，在包含大量三角形的三维场景中实时追踪数百万条光线仍具挑战性，且需要昂贵的硬件。RT 负载的主要瓶颈是开销高昂的包围盒层次结构（BVH）遍历任务，BVH 是一种编码三维场景的大型树结构。BVH 遍历是一个内存受限的问题，因为 GPU 线程大部分时间都在从内存读取树节点数据。在本工作中，我们通过预取来攻克光线追踪的内存延迟瓶颈。我们提出一种新颖的硬件预取器，称为树遍历预取器（Tree Traversal Prefetcher, TTP），用于光线追踪。其核心思想是利用 RT 单元中已有的树遍历栈来实现高精度预取。具体而言，TTP 使用每个线程硬件遍历栈上已经可用的地址来预取节点。对于基于 DFS（深度优先搜索）的遍历，当节点被连续从遍历栈中弹出时（可能对应沿树向上的遍历），就会生成预取。我们在周期级模拟器 Vulkan-sim 2.0 上评估 TTP，结果表明相较基线它平均取得 1.48× 的加速（最高 1.89×），且硬件开销几乎可以忽略不计。TTP 的平均 L1 准确率达到 98.92%，即预取块实际被需求加载引用的比例。覆盖率（以相对基线 L1 缺失的减少量计算）为 31.54%，与所获得的加速吻合良好。

## 代码与研究制品

论文对应实验代码位于 Vulkan-Sim 仓库的 TTP 分支；该仓库同时收录其他论文的实验材料。

- [代码仓库：yavuz650/vulkan-sim](https://github.com/yavuz650/vulkan-sim)
- [实验材料归档（Zenodo 19394324）](https://zenodo.org/records/19394324)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 8A](index.md) · [返回 ISCA 2026](../index.md)
