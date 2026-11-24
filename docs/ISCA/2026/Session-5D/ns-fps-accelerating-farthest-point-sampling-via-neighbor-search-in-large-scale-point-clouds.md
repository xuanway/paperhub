---
title: "NS-FPS: Accelerating Farthest Point Sampling via Neighbor Search in Large-Scale Point Clouds"
description: "ISCA 2026 · Session 5D · NS-FPS: Accelerating Farthest Point Sampling via Neighbor Search in Large-Scale Point Clouds"
tags:
  - "ISCA2026"
  - "Session 5D"
  - "Potpourri"
---

# NS-FPS: Accelerating Farthest Point Sampling via Neighbor Search in Large-Scale Point Clouds

**中文标题：** NS-FPS: 通过邻居搜索加速大规模点云中的最远点采样

**所属 Session：** [Session 5D](index.md) · [ISCA 2026](../index.md)

**作者：** Jiapei Zheng, Shuan Yang, Siqi He, Qi Liu, Chixiao Chen

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

With the rapid advancement of LiDAR sensors, processing large-scale point clouds has become a significant challenge in applications such as autonomous driving. One critical operation in point cloud processing is Farthest Point Sampling (FPS), which is essential for preserving geometric features in neural networks. However, the computational complexity of FPS grows quadratically with point cloud size, resulting in substantial memory access overhead and high latency. In this paper, we propose NS-FPS, a hardware-software co-designed accelerator that transforms the FPS problem into a neighbor search problem, reducing the complexity from O(N 2) to O(N log N). We observe that distance-cache updates during sampling occur primarily around the current sampled region, implying that most point accesses and distance computations are redundant. Using Voronoi diagram (VD) geometry, we explain this phenomenon and reveal a strong connection between FPS behavior and local neighborhood structure. Leveraging this insight, we introduce a partial-update strategy. We organize point cloud data using Morton codes, developing a three-level memory scheme that exploits spatial locality. Combined with an efficient pipelined neighbor search scheme and a hierarchical maximum candidate search, NS-FPS minimizes memory accesses and computational overhead, fully exploiting the acceleration potential of the reformulated algorithm. We implement NS-FPS as both a CPU software version and a custom ASIC design. Evaluated on real-world point cloud datasets, NS-FPS achieves an 81.6× speedup and 1700× reduction in memory accesses compared to GPU-based implementations, and a 2.9× speedup with 13.4× reduction in memory accesses compared to existing point cloud sampling accelerators. These results highlight that NS-FPS is an efficient and scalable solution for real-time point cloud processing in large-scale applications. The code is available at https://github.com/satreeby/ns-fps/.

## 中文摘要

随着 LiDAR 传感器的快速发展，处理大规模点云已成为自动驾驶等应用中的一项重大挑战。点云处理中的一项关键操作是最远点采样（FPS），它对于在神经网络中保留几何特征至关重要。然而，FPS 的计算复杂度随点云规模呈平方增长，导致大量内存访问开销和高时延。本文提出 NS-FPS，一种软硬件协同设计的加速器，它将 FPS 问题转化为邻居搜索问题，把复杂度从 O(N²) 降至 O(N log N)。我们观察到，采样过程中距离缓存的更新主要发生在当前采样区域附近，这意味着大多数点访问与距离计算都是冗余的。借助 Voronoi 图（VD）几何，我们解释了这一现象，并揭示了 FPS 行为与局部邻域结构之间的紧密联系。基于这一洞见，我们引入了部分更新策略。我们使用 Morton 码组织点云数据，设计了一种利用空间局部性的三级存储方案。结合高效的流水线化邻居搜索方案与分层最大候选搜索，NS-FPS 将内存访问与计算开销降至最低，充分挖掘了重构后算法的加速潜力。我们将 NS-FPS 同时实现为 CPU 软件版本与定制 ASIC 设计。在真实点云数据集上评估，相比基于 GPU 的实现，NS-FPS 实现 81.6× 的加速、内存访问减少 1700×；相比现有点云采样加速器，实现 2.9× 的加速、内存访问减少 13.4×。这些结果表明，NS-FPS 是面向大规模应用中实时点云处理的高效且可扩展的解决方案。代码可在 https://github.com/satreeby/ns-fps/ 获取。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：satreeby/ns-fps](https://github.com/satreeby/ns-fps)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5D](index.md) · [返回 ISCA 2026](../index.md)
