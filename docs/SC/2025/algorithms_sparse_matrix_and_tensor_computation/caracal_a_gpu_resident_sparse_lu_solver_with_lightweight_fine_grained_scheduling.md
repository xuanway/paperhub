---
title: "Caracal: A GPU-Resident Sparse LU Solver with Lightweight Fine-Grained Scheduling"
description: "SC 2025 · Algorithms: Sparse Matrix and Tensor Computation · Jie Ren; Tingxuan Zhong; Yuxi Hong; Guofeng Feng; Xincheng Wang; Weile Jia; Hate"
tags:
  - "SC2025"
  - "Algorithms: Sparse Matrix and Tensor Computation"
---

# Caracal: A GPU-Resident Sparse LU Solver with Lightweight Fine-Grained Scheduling

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Jie Ren; Tingxuan Zhong; Yuxi Hong; Guofeng Feng; Xincheng Wang; Weile Jia; Hatem Ltaief; David Keyes

**会议**：SC 2025 · St. Louis, MO

## 摘要

We address inefficiencies in task scheduling, memory management, and scalability in GPU-resident sparse LU factorization with a two-level approach of sequentially scheduled coarse-grained blocks containing multiple fine-grained blocks managed with a lightweight static scheduler enabling multi-stream parallelism. Additionally, we design an intelligent memory caching mechanism for the fine-grained scheduler, which retains frequently accessed data in GPU memory. To further enhance scalability, we introduce a distributed memory design that partitions the input matrix using a 1D block-cyclic distribution and optimizes inter-GPU communication via NVLink. The multi-GPU design reaches a computational throughput of 6.46 TFLOP/s on four A100 GPUs, demonstrating promising scalability. This is up to 7x speedup over the latest \texttt{SuperLU\_DIST} with 3D communication, 94x speedup over \texttt{PanguLU}, 16x speedup over \texttt{PasTiX}, and 10x speedup over our own coarse-grained dynamic schedul

---

## 一句话总结

> 该工作属于 Algorithms: Sparse Matrix and Tensor Computation 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Algorithms: Sparse Matrix and Tensor Computation 领域贡献新的设计范式或评估框架。
