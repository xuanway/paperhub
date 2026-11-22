---
title: "SLOTH: Lightweight Detection and Localization of On-Chip Fail-Slow Failures for DNN Accelerators"
description: "MICRO 2026 · Session 6B · SLOTH：面向 DNN 加速器的片上性能退化故障轻量级检测与定位"
tags:
  - "MICRO2026"
  - "Neural Networks"
---

# SLOTH: Lightweight Detection and Localization of On-Chip Fail-Slow Failures for DNN Accelerators

**中文标题：** SLOTH：面向 DNN 加速器的片上性能退化故障轻量级检测与定位

**所属 Session：** [Session 6B](index.md) · [MICRO 2026](../index.md)

**作者：** Junchi Wu, Xinfei Wan, Zhuoran Li, Guangyu Sun, Yun Liang, Diyu Zhou, Youwei Zhuo

**来源：** MICRO 2026，pp. 1949–1966；[DOI](https://doi.org/10.1109/MICRO67795.2026.00137)

## 英文摘要

Spatial DNN accelerators are essential for high-performance inference, but their performance is undermined by widespread fail-slow failures. Detecting such failures on-chip is challenging, as prior methods from distributed systems are unsuitable due to strict memory limits and their inability to track failures across the hardware topology. We present SLOTH, a lightweight, hardware-aware framework for practical on-chip fail-slow detection in DNN accelerators. SLOTH combines workload-aware instrumentation for operator-level monitoring with minimal overhead, on-the-fly trace compression to operate within kilobytes of memory, and a novel topology-aware ranking algorithm to pinpoint a failure's root cause. We evaluate SLOTH on a wide range of representative DNN workloads. The results demonstrate that SLOTH reduces the storage overhead by an average of 115.9x times, while achieving an average fail-slow detection accuracy from 69.68% to 86.69%.

## 中文摘要

空间 DNN 加速器对于高性能推理至关重要，但其性能因广泛的失败-缓慢故障而受到损害。在片上检测此类故障具有挑战性，因为分布式系统的先前方法由于严格的内存限制且无法跨硬件拓扑跟踪故障而不再适用。我们推出了 SLOTH，这是一种轻量级的硬件感知框架，用于 DNN 加速器中实用的片上故障缓慢检测。 SLOTH 将用于算子级监控的工作负载感知仪器以最小的开销、在千字节内存内运行的动态跟踪压缩以及用于查明故障根本原因的新型拓扑感知排名算法结合起来。我们在各种具有代表性的 DNN 工作负载上评估 SLOTH。结果表明，SLOTH 平均降低了 115.9 倍的存储开销，同时将性能退化故障检测平均准确率从 69.68% 提高到 86.69%。

## 中文关键词

性能退化故障；深度神经网络加速器；故障检测；故障定位

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21551512](https://doi.org/10.5281/zenodo.21551512)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6B](index.md) · [MICRO 2026 主页](../index.md)
