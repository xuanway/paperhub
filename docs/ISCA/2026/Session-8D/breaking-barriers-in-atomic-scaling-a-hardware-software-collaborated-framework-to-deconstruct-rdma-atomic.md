---
title: "Breaking Barriers in Atomic Scaling: A Hardware–Software-Collaborated Framework to Deconstruct RDMA Atomic"
description: "ISCA 2026 · Session 8D · Breaking Barriers in Atomic Scaling: A Hardware–Software-Collaborated Framework to Deconstruct RDMA Atomic"
tags:
  - "ISCA2026"
  - "Session 8D"
  - "HPC"
---

# Breaking Barriers in Atomic Scaling: A Hardware–Software-Collaborated Framework to Deconstruct RDMA Atomic

**中文标题：** 打破原子操作扩展的壁垒：解构 RDMA 原子操作的软硬件协同框架

**所属 Session：** [Session 8D](index.md) · [ISCA 2026](../index.md)

**作者：** Guangyang Deng, Qiangsheng Su, Zhirong Shen, Qing Wang, Yina Lv, Ronglong Wu, Jiwu Shu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Remote Direct Memory Access (RDMA) Atomics are widely adopted to ensure correctness in distributed synchronization. However, their scalability is still seriously constrained by internal locking within RNICs. This paper provides systematic analysis that uncovers fundamental bottlenecks when scaling atomic operations. To break the constraints in RDMA Atomic scaling, we present Fusa, a framework that transparently coordinates server-side hardware (RNIC) and software (CPU) to accelerate atomic executions. Fusa integrates fine-grained contention detection with selective onloading, which executes uncontended operations in hardware while redirecting contended ones to software. Fusa further designs a consensus mechanism for strategy switching. We evaluate Fusa using microbenchmarks and unmodified RDMA-based systems, showing that Fusa improves throughput by up to 4.6×.

## 中文摘要

远程直接内存访问（RDMA）原子操作被广泛用于保障分布式同步的正确性。然而，其可扩展性仍受到 RNIC 内部锁机制的严重制约。本文通过系统性的分析，揭示了原子操作在扩展时存在的根本瓶颈。为打破 RDMA 原子操作扩展中的约束，我们提出 Fusa，一个透明地协调服务器端硬件（RNIC）与软件（CPU）以加速原子执行的框架。Fusa 将细粒度竞争检测与选择性卸载相结合：无竞争的操作在硬件中执行，而有竞争的操作则被重定向到软件。Fusa 还设计了用于策略切换的共识机制。我们使用微基准测试和未经修改的基于 RDMA 的系统评估 Fusa，结果表明 Fusa 将吞吐量最多提升 4.6×。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：xmusys/fusa](https://github.com/xmusys/fusa)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 8D](index.md) · [返回 ISCA 2026](../index.md)
