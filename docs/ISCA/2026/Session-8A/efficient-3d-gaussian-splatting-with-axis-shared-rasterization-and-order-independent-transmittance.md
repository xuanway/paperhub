---
title: "Efficient 3D Gaussian Splatting with Axis-Shared Rasterization and Order-independent Transmittance"
description: "ISCA 2026 · Session 8A · Efficient 3D Gaussian Splatting with Axis-Shared Rasterization and Order-independent Transmittance"
tags:
  - "ISCA2026"
  - "Session 8A"
  - "Rendering"
---

# Efficient 3D Gaussian Splatting with Axis-Shared Rasterization and Order-independent Transmittance

**中文标题：** 基于轴共享光栅化与顺序无关透射率的高效 3D 高斯泼溅

**所属 Session：** [Session 8A](index.md) · [ISCA 2026](../index.md)

**作者：** Zhican Wang, Guanghui He, Lingjun Gao, Dantong Liu, Shell Xu Hu, Chen Zhang, Zhuoran Song, Nicholas Lane, Hongxiang Fan

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

3D Gaussian Splatting (3DGS) has emerged as a powerful technique for novel view synthesis, combining high-quality reconstruction with efficient rendering. It has been widely adopted in domains such as AR/VR, robotics, and autonomous driving. However, achieving real-time performance on resource-constrained platforms remains challenging due to strict power and area budgets. Prior accelerators improve hardware performance but still overlook key inefficiencies, including insufficient rasterization efficiency, poor sorting scalability, and pipeline imbalance. This paper presents an architecture–algorithm co-design to address these challenges. First, we propose axis-shared rasterization, which precomputes and reuses common terms along the X- and Y-axes, reducing multiply-and-accumulate (MAC) operations by up to 38% while preserving high parallelism. Second, we develop a novel order-independent transmittance method that removes the need for explicit sorting by leveraging a lightweight Multilayer Perceptron (MLP) to directly approximate the transmittance of each Gaussian, enabling efficient α blending with negligible quality loss. Third, we design a unified reconfigurable PE array that supports both rasterization and MLP inference, sustaining high utilization without costly sorting hardware. Our experiments demonstrate that our design preserves rendering quality while achieving a 1.33 ∼1, 88× speedup over the state-of-the-art 3DGS accelerators. Our code is open source at https://github.com/WangZhican/ISCA26_3DGS_Acc.

## 中文摘要

3D 高斯泼溅（3D Gaussian Splatting, 3DGS）已成为一种强大的新视角合成技术，兼具高质量重建与高效渲染能力，已在 AR/VR、机器人与自动驾驶等领域得到广泛应用。然而，由于严格的功耗与面积预算，在资源受限平台上实现实时性能仍然颇具挑战。此前的加速器虽提升了硬件性能，但仍忽视了若干关键的低效问题，包括光栅化效率不足、排序可扩展性差以及流水线不均衡。本文提出一种架构—算法协同设计来应对这些挑战。首先，我们提出轴共享光栅化（axis-shared rasterization），通过预计算并复用沿 X 轴与 Y 轴的公共项，在保持高并行度的同时将乘累加（MAC）操作最多减少 38%。其次，我们提出一种新的顺序无关透射率（transmittance）方法，借助轻量级多层感知机（MLP）直接近似每个高斯球的透射率，从而摆脱显式排序，实现高效的 α 混合且质量损失可忽略。第三，我们设计了一个统一的可重构 PE 阵列，同时支持光栅化与 MLP 推理，无需昂贵的排序硬件即可保持高利用率。实验表明，我们的设计在保持渲染质量的同时，相较最先进的 3DGS 加速器实现了 1.33～1.88× 的加速。代码已开源于 https://github.com/WangZhican/ISCA26_3DGS_Acc。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：WangZhican/ISCA26_3DGS_Acc](https://github.com/WangZhican/ISCA26_3DGS_Acc)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 8A](index.md) · [返回 ISCA 2026](../index.md)
