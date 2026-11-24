---
title: "IDEA-GP: Instruction-Driven Architecture with Efficient Online Workload Allocation for Geometric Perception"
description: "ISCA 2025 · Session 8C · IDEA-GP：面向几何感知高效在线负载分配的指令驱动架构"
tags:
  - "ISCA2025"
  - "Session 8C"
  - "Domain Specific Accelerators II"
---

# IDEA-GP: Instruction-Driven Architecture with Efficient Online Workload Allocation for Geometric Perception

**中文标题：** IDEA-GP：面向几何感知高效在线负载分配的指令驱动架构

**所属 Session：** [Session 8C](index.md) · [ISCA 2025](../index.md)

**作者：** Suquan Zhang, Yu Hu, Yunfei Xiang, Dawei Zhao, Yuanfan Xu, Qingmin Liao, Jincheng Yu, Yu Wang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731080) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The algorithmic complexity of robotic systems presents significant challenges to achieving generalized acceleration in robot applica- tions. On the one hand, the diversity of operators and computational flows within similar task categories prevents the reuse of special- ized computational units. On the other hand, task variations and environmental dynamics can cause workload fluctuations, leading to inefficient resource utilization. This paper focuses on the geometric perception capability of robots, taking localization and mapping as the basic applications, and proposes IDEA-GP, an Instruction-Driven Architecture with Efficient online workload Allocation for Geometric Perception. Built around an array of general computational units designed for spatial positioning representations, IDEA-GP supports a wide range of robot pose-related computational tasks. IDEA-GP employs a com- piler to perform online workload analysis and resource allocation. It generates instructions tailored to processing elements (PEs) to schedule computations, thereby accelerating optimization problems and enhancing geometric perception performance. Deployed on the ZCU102 evaluation board, IDEA-GP demonstrates an average speedup of 7.5×over the Intel CPU and 19.7×over the ARM CPU in Simultaneous Localization and Mapping (SLAM) tasks, and a 16.4×speedup over the Intel CPU and 41.6×over the ARM CPU in Structure from Motion (SfM) tasks.

## 中文摘要

机器人系统的算法复杂度，给机器人应用的通用加速带来巨大挑战。一方面，同类任务内部算子与计算流的多样性，使得专用计算单元难以复用；另一方面，任务变化与环境动态性会造成负载波动，导致资源利用率低下。

本文聚焦机器人的几何感知能力，以定位与建图作为基础应用，提出IDEA-GP：面向几何感知、支持高效在线负载分配的指令驱动架构（Instruction-Driven Architecture with Efficient online workload Allocation for Geometric Perception）。IDEA-GP以面向空间位姿表征设计的通用计算单元阵列为核心，支持多种机器人位姿相关计算任务。该架构借助编译器完成在线负载分析与资源分配，生成适配处理单元（PE）的指令以调度计算，从而加速优化求解，提升几何感知性能。

在ZCU102评估板上部署验证：在同步定位与建图（SLAM）任务中，IDEA-GP相比Intel CPU平均提速7.5倍，相比ARM CPU平均提速19.7倍；在运动恢复结构（SfM）任务中，相比Intel CPU平均提速16.4倍，相比ARM CPU平均提速41.6倍。

## 英文关键词

Robot, Instruction Set Architecture, Hardware Accelerator, Geometric Perception, Optimization

## 中文关键词

机器人, 指令集架构, 硬件加速器, 几何感知, 优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731080)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8C](index.md) · [返回 ISCA 2025](../index.md)
