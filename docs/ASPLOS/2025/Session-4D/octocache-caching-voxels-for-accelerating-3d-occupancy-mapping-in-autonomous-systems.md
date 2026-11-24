---
title: "OctoCache: Caching Voxels for Accelerating 3D Occupancy Mapping in Autonomous Systems"
description: "ASPLOS 2025 · Session 4D · OctoCache：通过缓存体素加速自主系统中的三维占据建图"
tags:
  - "ASPLOS2025"
  - "Session 4D"
  - "Autonomous Systems"
---

# OctoCache: Caching Voxels for Accelerating 3D Occupancy Mapping in Autonomous Systems

**中文标题：** OctoCache：通过缓存体素加速自主系统中的三维占据建图

**所属 Session：** [Session 4D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Peiqing Chen (University of Maryland), Minghao Li (Harvard University), Zishen Wan (Georgia Institute of Technology), Yushun Hsiao (Harvard University), Minlan Yu (Harvard University), Vijay Janapa Reddi (Harvard University), Zaoxing Liu (University of Maryland)

**单位：** University of Maryland；Harvard University；Georgia Institute of Technology

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716263) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

3D mapping systems are crucial for creating digital representations of physical environments, widely used in autonomous robot navigation, 3D visualization, and AR/VR. This paper focuses on OctoMap, a leading 3D mapping framework using an octree-based structure for spatial efficiency. However, OctoMap's performance is limited by slow updates due to costly memory accesses. We introduce OctoCache, a software system that accelerates OctoMap through (1) optimized cache memory access, (2) refined voxel ordering, and (3) workflow parallelization. OctoCache achieves speedups of 45.63%~88.01% in 3D environment construction tasks compared to standard OctoMap. Deployed in UAV navigation scenarios, OctoCache demonstrates up to 3.02× speedup and reduces mission completion time by up to 28%. These results highlight OctoCache's potential to enhance 3D mapping efficiency in autonomous navigation, advancing robotics and environmental modeling.

## 中文摘要

三维建图系统对于构建物理环境的数字化表示至关重要，被广泛应用于自主机器人导航、三维可视化以及 AR/VR 之中。本文聚焦于 OctoMap，这是一个采用八叉树结构以提升空间效率的主流三维建图框架。然而，OctoMap 因访存开销高昂而导致更新缓慢，其性能因此受到限制。我们提出 OctoCache，这是一个通过以下方式加速 OctoMap 的软件系统：(1) 优化的缓存访存；(2) 改进的体素排序；(3) 工作流并行化。在三维环境构建任务中，OctoCache 相比标准 OctoMap 取得 45.63%~88.01% 的加速。在无人机导航场景中部署后，OctoCache 展现出最高 3.02 倍的加速，并将任务完成时间最多缩短 28%。这些结果凸显了 OctoCache 在自主导航中提升三维建图效率的潜力，可推动机器人与环境建模的发展。

## 英文关键词

Caching, Mapping Systems, IoT, UAV Autonomy, OctoMap

## 中文关键词

缓存；建图系统；物联网；无人机自主；OctoMap

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716263)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4D](index.md) · [返回 ASPLOS 2025](../index.md)
