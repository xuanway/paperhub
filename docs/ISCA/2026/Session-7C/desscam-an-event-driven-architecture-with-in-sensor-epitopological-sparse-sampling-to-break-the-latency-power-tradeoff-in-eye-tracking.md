---
title: "DESSCam: An Event-Driven Architecture with In-Sensor Epitopological Sparse Sampling to Break the Latency-Power Tradeoff in Eye Tracking"
description: "ISCA 2026 · Session 7C · DESSCam: An Event-Driven Architecture with In-Sensor Epitopological Sparse Sampling to Break the Latency-Power Tradeoff in Eye Tracking"
tags:
  - "ISCA2026"
  - "Session 7C"
  - "Domain Specific Accelerators 2"
---

# DESSCam: An Event-Driven Architecture with In-Sensor Epitopological Sparse Sampling to Break the Latency-Power Tradeoff in Eye Tracking

**中文标题：** DESSCam: 以传感器内表拓扑稀疏采样打破眼动追踪延迟-功耗权衡的事件驱动架构

**所属 Session：** [Session 7C](index.md) · [ISCA 2026](../index.md)

**作者：** Zhijie Jian, Shangyu Yang, Yuan Hua, Jilin Zhang, Ziyi Cheng, Hong Chen

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Eye tracking is crucial for emerging augmented/virtual reality (AR/VR) platforms, yet existing eye trackers suffer from high end-to-end latency (>15ms) and high power consumption (>2W), resulting in motion sickness and thermal discomfort, and thus making prolonged immersive interaction infeasible. These primarily arise from the frame-based dense sampling mechanism of image sensors, which mismatches the temporally varying and spatially sparse nature of eye movements. To address these problems, we propose DESSCam, a 3D-stacked event-driven image sensor architecture with a dynamic sparse imaging paradigm, which achieves low latency through temporally dynamic sampling adaptive to eye movement speed, and low power consumption by spatially pixel-wise sparse sampling. In particular, we put forward a novel in-sensor epitopological sparse sampling (ESS) mechanism, which achieves attention-guided 50× pixel downsampling while preserving global data correlations. Moreover, we introduce a patch activation mechanism that only allows the events to be read out from the pixel blocks whose event count exceeds a threshold, and a robust vision transformer to accurately extract global features from sparse data. Furthermore, we implement DESSCam’s hardware through co-optimized pixel and peripheral circuits with minimal overhead. Our experimental results show up to 2.7× power saving and 15.2× end-to-end latency reduction compared to the state-of-the-art eye tracking system, enabling sub-millisecond gaze updates and unlocking deeply immersive AR/VR experiences.

## 中文摘要

眼动追踪对新兴的增强/虚拟现实（AR/VR）平台至关重要，但现有眼动追踪器存在端到端延迟高（>15ms）和功耗高（>2W）的问题，导致晕动症和热不适，从而使长时间的沉浸式交互不可行。这些问题主要源于图像传感器基于帧的稠密采样机制，它与眼动在时间上变化、在空间上稀疏的特性不匹配。为解决这些问题，我们提出 DESSCam，一种具有动态稀疏成像范式的 3D 堆叠事件驱动图像传感器架构，它通过与眼动速度自适应的时域动态采样实现低延迟，并通过空间上逐像素的稀疏采样实现低功耗。特别地，我们提出一种新颖的传感器内表拓扑稀疏采样（ESS）机制，在保持全局数据相关性的同时实现注意力引导的 50× 像素降采样。此外，我们引入一种分块激活机制，仅允许从事件计数超过阈值的像素块中读出事件，并采用稳健的视觉 Transformer 从稀疏数据中准确提取全局特征。此外，我们通过协同优化的像素电路与外设电路，以极小开销实现了 DESSCam 的硬件。实验结果表明，与最先进的眼动追踪系统相比，DESSCam 最多节省 2.7× 的功耗并将端到端延迟降低 15.2×，实现亚毫秒级的注视更新，开启深度沉浸的 AR/VR 体验。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7C](index.md) · [返回 ISCA 2026](../index.md)
