---
title: "CPU- and GPU-Initiated Communication Strategies for Conjugate Gradient Methods on Large GPU Clusters"
description: "SC 2025 · Performance: Benchmarks and Optimization · James D. Trotter; Sinan Ekmekcibasi; Doğan Sağbili; Johannes Langguth; Xing Cai;"
tags:
  - "SC2025"
  - "Performance: Benchmarks and Optimization"
---

# CPU- and GPU-Initiated Communication Strategies for Conjugate Gradient Methods on Large GPU Clusters

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Benchmarks and Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Benchmarks and Optimization</p>
</div>

**作者**：James D. Trotter; Sinan Ekmekcibasi; Doğan Sağbili; Johannes Langguth; Xing Cai; Didem Unat

**会议**：SC 2025 · St. Louis, MO

## 摘要

Strong scaling of conjugate gradient (CG) algorithms on GPU-based supercomputers is notoriously challenging. These linear system solvers have low computational intensity, making inter-GPU communication and synchronization primary bottlenecks. In light of recent developments in multi-GPU communication, we revisit CG parallelization for large-scale GPU clusters. We implement standard and pipelined CG solvers using three flavors of multi-GPU communication: GPU-aware MPI, NVIDIA's NCCL/AMD's RCCL, and NVIDIA's NVSHMEM. Our monolithic NVSHMEM-based implementation with GPU-initiated communication enables CPU-free execution and thus lower overhead. However, lack of vendor-supported device-side computational kernels means that CPU-controlled CG implementations based on GPU-aware MPI or NCCL/RCCL are still favored for small GPU counts. Compared with state-of-the-art CG implementations, we have also eliminated unnecessary CPU-GPU data transfers and synchronization points. Our CG implementations 

---

## 一句话总结

> 该工作属于 Performance: Benchmarks and Optimization 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Performance: Benchmarks and Optimization 领域贡献新的设计范式或评估框架。
