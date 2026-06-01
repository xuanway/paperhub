---
title: "SDR-RDMA: Software-Defined Reliability Architecture for Planetary-Scale RDMA Communication"
description: "SC 2025 · Architectures and Networks: Networking · Mikhail Khalilov; Siyuan Shen; Marcin Chrapek; Tiancheng Chen; Kenji Nakano; Pet"
tags:
  - "SC2025"
  - "Architectures and Networks: Networking"
---

# SDR-RDMA: Software-Defined Reliability Architecture for Planetary-Scale RDMA Communication

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Architectures and Networks: Networking。</p>
<p class="paper-seo-summary__tags">SC 2025 · Architectures and Networks: Networking</p>
</div>

**作者**：Mikhail Khalilov; Siyuan Shen; Marcin Chrapek; Tiancheng Chen; Kenji Nakano; Peter-Jan Gootzen; Salvatore Di Girolamo; Rami Nudelman; Gil Bloch; Jithin Jose; Abdul Kabbani; Sreevatsa Anantharamu; Jie Zhang; Konstantin Taranov; Zhuolong Yu; Scott Moe; Mahmoud Elhaddad; Nicola Mazzoletti; Torsten Hoefler

**会议**：SC 2025 · St. Louis, MO

## 摘要

RDMA is vital for efficient distributed training across datacenters, but millisecond-scale latencies complicate the design of its reliability layer. We show that depending on long-haul link characteristics, such as drop rate, distance, and bandwidth, the widely used Selective Repeat algorithm can be inefficient, warranting alternatives like erasure coding. To enable such alternatives on existing hardware, we propose SDR-RDMA, a software-defined reliability stack for RDMA. Its core is a lightweight SDR SDK that extends standard point-to-point RDMA semantics — fundamental to AI networking stacks — with a receive buffer bitmap. SDR bitmap enables partial message completion to let applications implement custom reliability schemes tailored to specific deployments, while preserving zero-copy RDMA benefits. By offloading the SDR backend to NVIDIA’s Data Path Accelerator (DPA), we achieve line-rate performance, enabling efficient inter-datacenter communication and advancing reliability innovat

---

## 一句话总结

> 该工作属于 Architectures and Networks: Networking 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Architectures and Networks: Networking 领域贡献新的设计范式或评估框架。
