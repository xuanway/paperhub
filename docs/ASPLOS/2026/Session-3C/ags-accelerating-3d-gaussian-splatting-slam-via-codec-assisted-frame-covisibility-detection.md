---
title: "AGS: Accelerating 3D Gaussian Splatting SLAM via CODEC-Assisted Frame Covisibility Detection"
description: "ASPLOS 2026 · Session 3C · AGS：通过 CODEC 辅助的帧共视检测加速 3D 高斯泼溅 SLAM"
tags:
  - "ASPLOS2026"
  - "Session 3C"
  - "3D Gaussian Splatting & Rendering"
---

# AGS: Accelerating 3D Gaussian Splatting SLAM via CODEC-Assisted Frame Covisibility Detection

**中文标题：** AGS：通过 CODEC 辅助的帧共视检测加速 3D 高斯泼溅 SLAM

**所属 Session：** [Session 3C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Houshu He (Shanghai Jiao Tong University), Naifeng Jing (Shanghai Jiao Tong University), Li Jiang (Shanghai Jiao Tong University), Xiaoyao Liang (Shanghai Jiao Tong University), Zhuoran Song (Shanghai Jiao Tong University)

**单位：** Shanghai Jiao Tong University

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762229) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Simultaneous Localization and Mapping (SLAM) is a critical task that enables autonomous vehicles to construct maps and localize themselves in unknown environments. Recent breakthroughs combine SLAM with 3D Gaussian Splatting (3DGS) to achieve exceptional reconstruction fidelity. However, existing 3DGS-SLAM systems provide insufficient throughput due to the need for multiple training iterations per frame and the vast number of Gaussians. In this paper, we propose AGS, an algorithm-hardware co-design framework to boost the efficiency of 3DGS-SLAM based on the intuition that SLAM systems process frames in a streaming manner, where adjacent frames exhibit high similarity that can be utilized for acceleration. On the software level: 1) We propose a coarse-then-fine-grained pose tracking method with respect to the robot's movement. 2) We avoid redundant computations of Gaussians by sharing their contribution information across frames. On the hardware level, we propose a frame covisibility detection engine to extract intermediate data from the video CODEC. We also implement a pose tracking engine and a mapping engine with workload schedulers to efficiently deploy the AGS algorithm. Our evaluation shows that AGS achieves up to 17.12×, 6.71×, and 5.41× speedups against the mobile and high-end GPUs, and a state-of-the-art 3DGS accelerator, GSCore.

## 中文摘要

同步定位与建图（SLAM）是一项关键任务，它使自动驾驶汽车能够在未知环境中构建地图并实现自身定位。近期的突破将 SLAM 与 3D 高斯泼溅（3DGS）相结合，实现了卓越的重建保真度。然而，现有的 3DGS-SLAM 系统吞吐量不足，原因在于每一帧都需要多次训练迭代，且高斯数量庞大。本文提出 AGS，一个算法-硬件协同设计框架，其出发点是：SLAM 系统以流式方式处理帧，相邻帧之间具有高度相似性，可被用于加速。在软件层面：1）我们提出一种针对机器人运动的由粗到细的位姿跟踪方法。2）我们通过跨帧共享高斯的贡献信息来避免冗余计算。在硬件层面，我们提出一个帧共视检测引擎，从视频 CODEC 中提取中间数据。我们还实现了带有工作负载调度器的位姿跟踪引擎和建图引擎，以高效部署 AGS 算法。我们的评估表明，AGS 相对于移动端与高端 GPU 以及最先进的 3DGS 加速器 GSCore，分别实现了最高 17.12×、6.71× 和 5.41× 的加速。

## 英文关键词

3DGS, SLAM, CODEC, Frame covisibility

## 中文关键词

3DGS；SLAM；CODEC；帧共视

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762229)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3C](index.md) · [返回 ASPLOS 2026](../index.md)
