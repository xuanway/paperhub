---
title: "LAIKA: Machine Learning-Assisted In-Kernel APU Acceleration"
description: "ASPLOS 2026 · Session 4A · LAIKA：机器学习辅助的内核内 APU 加速"
tags:
  - "ASPLOS2026"
  - "Session 4A"
  - "ML Training & Monitoring"
---

# LAIKA: Machine Learning-Assisted In-Kernel APU Acceleration

**中文标题：** LAIKA：机器学习辅助的内核内 APU 加速

**所属 Session：** [Session 4A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Haoming Zhuo (South China Normal University), Dingding Li (South China Normal University), Ronghua Lin (South China Normal University), Yong Tang (South China Normal University)

**单位：** South China Normal University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790181) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The integration of machine learning (ML) into OS kernels is severely hampered by the high latency of offloading to discrete GPUs (dGPUs), where data transfers across the PCIe bus can consume over 93% of the total execution time. This paper argues that for many latency-sensitive kernel tasks, the solution is not a more powerful dGPU but a fundamental shift to an I/O-efficient architecture: the integrated GPU (iGPU) found in modern APUs. We present LAIKA, a kernel-space acceleration framework that fully exploits the APU's unified memory. LAIKA combines three key mechanisms: a lightweight API proxy (AProxy) to safely bridge the kernel-user boundary, a tridomain shared memory manager (AShm) for true zero-copy data exchange, and APU Persistent Kernel (APK) to eliminate control-path overhead. Across a suite of representative kernel workloads, our evaluation shows that by eliminating the I/O bottleneck, LAIKA slashes end-to-end inference latency by up to 9.7× and reduces total system power to as little as 28.9% of an optimized dGPU baseline. Our work identifies iGPUs as a practical and highly efficient alternative for machine learning acceleration within OS kernels.

## 中文摘要

将机器学习（ML）集成到操作系统内核中，严重受制于卸载到独立 GPU（dGPU）的高延迟——跨 PCIe 总线的数据传输可占去总执行时间的 93% 以上。本文认为，对于许多对延迟敏感的内核任务，解决方案并非更强大的 dGPU，而是向 I/O 高效架构的根本性转变：现代 APU 中的集成 GPU（iGPU）。我们提出 LAIKA，一个充分利用 APU 统一内存的内核空间加速框架。LAIKA 结合三项关键机制：轻量级 API 代理（AProxy），用于安全地桥接内核—用户边界；三域共享内存管理器（AShm），用于实现真正的零拷贝数据交换；以及 APU 持久内核（APK），用于消除控制路径开销。在一系列具有代表性的内核工作负载上，我们的评估表明，通过消除 I/O 瓶颈，LAIKA 将端到端推理延迟最多降低 9.7×，并将系统总功耗降至优化后 dGPU 基线的 28.9%。我们的工作表明，iGPU 是操作系统内核内机器学习加速的一种实用且高效的替代方案。

## 英文关键词

ML for Systems; Integrated GPU (iGPU); Operating Systems; Zero-Copy Acceleration; Unified Memory Architecture; Low-Latency Inference; Energy Efficiency

## 中文关键词

面向系统的机器学习；集成 GPU（iGPU）；操作系统；零拷贝加速；统一内存架构；低延迟推理；能效

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790181)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4A](index.md) · [返回 ASPLOS 2026](../index.md)
