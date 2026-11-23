---
title: "AQB8: Energy-Efficient Ray Tracing Accelerator through Multi-Level Quantization"
description: "ISCA 2025 · Session 3B · AQB8：基于多级量化的高能效光线追踪加速器"
tags:
  - "ISCA2025"
  - "Session 3B"
  - "Domain Specific Accelerators I"
---

# AQB8: Energy-Efficient Ray Tracing Accelerator through Multi-Level Quantization

**中文标题：** AQB8：基于多级量化的高能效光线追踪加速器

**所属 Session：** [Session 3B](index.md) · [ISCA 2025](../index.md)

**作者：** Yen-Chieh Huang, Chen-Pin Yang, Tsung Tai Yeh

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731104) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Ray tracing (RT) is a rendering technique that produces high-fidelity

images by simulating how light physically interacts with objects

in a scene. This realism comes at a high computational and mem-

ory cost, largely driven by the need to find numerous ray-object

intersections. To accelerate this process, scenes are typically struc-

tured using bounding volume hierarchy (BVH) trees, where objects

are grouped within bounding boxes to minimize the number of

required intersection tests. Specialized hardware, known as RT

accelerators, accelerates BVH processing to boost computational

speed, yet memory traffic persists as a major bottleneck, largely

due to the bandwidth consumed by standard 32-bit floating-point

(FP32) bounding boxes. Consequently, previous work has aimed to

reduce memory traffic by compressing these boxes into low-bit (e.g.,

8-bit) representations. However, existing compression techniques

typically require decompressing bounding boxes back to FP32 for in-

tersection tests, thus failing to eliminate the computational burden

and energy cost associated with complex FP32 arithmetic during

BVH traversal. This work introduces AQB8, an RT accelerator de-

signed to operate on a quantized BVH tree constructed using a novel

multi-level quantization technique. This approach enables RT to

operate directly on low-bit integers using simpler, area-efficient

hardware units, thereby drastically reducing the need for FP32 arith-

metic during BVH traversal while mitigating overheads associated

with reduced precision. As a result, across various scenes, AQB8

achieves a 70% reduction in DRAM accesses, a 49% reduction in

energy consumption, a 27% hardware area reduction, and a 1.82x

performance speedup over modern GPU RT accelerators. Our code

is publicly available at https://github.com/nycu-caslab/AQB8.

## 中文摘要

光线追踪 (RT) 是一种渲染技术，通过模拟光线与场景中的对象的物理交互方式来生成高保真图像。这种真实感的代价是很高的计算和内存成本，这主要是由于需要找到大量的射线与物体相交。为了加速这一过程，通常使用包围体层次结构 (BVH) 树来构建场景，其中对象在包围盒中分组，以最大限度地减少所需的相交测试的数量。称为 RT 加速器的专用硬件可加速 BVH 处理以提高计算速度，但内存流量仍然是主要瓶颈，这主要是由于标准 32 位浮点 (FP32) 包围盒消耗的带宽。因此，之前的工作旨在通过将这些框压缩为低位（例如 8 位）表示来减少内存流量。

然而，现有的压缩技术通常需要将包围盒解压回 FP32 进行相交测试，因此无法消除 BVH 遍历期间与复杂 FP32 算法相关的计算负担和能量成本。这项工作介绍了 AQB8，这是一种 RT 加速器，设计用于在使用新颖的多级量化技术构建的量化 BVH 树上运行。这种方法使 RT 能够使用更简单、节省空间的硬件单元直接对低位整数进行操作，从而大大减少 BVH 遍历期间对 FP32 算术的需求，同时减轻与精度降低相关的开销。因此，在各种场景中，AQB8 与现代 GPU RT 加速器相比，实现了 DRAM 访问量减少 70%、能耗降低 49%、硬件面积减少 27%、性能加速 1.82 倍。代码可在 https://github.com/nycu-caslab/AQB8 上公开获取。

## 英文关键词

Ray Tracing, Domain-Specific Accelerator, GPU

## 中文关键词

光线追踪, 特定领域加速器, GPU

## 代码与研究制品

- [代码仓库](https://github.com/nycu-caslab/AQB8)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731104)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3B](index.md) · [返回 ISCA 2025](../index.md)
