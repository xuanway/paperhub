---
title: "Caracal: A GPU-Resident Sparse LU Solver with Lightweight Fine-Grained Scheduling"
description: "SC 2025 · Algorithms: Sparse Matrix and Tensor Computation · Jie Ren; Tingxuan Zhong; Yuxi Hong; Guofeng Feng; Xincheng Wang; Weile Jia; Hate"
tags:
  - "SC2025"
  - "Algorithms: Sparse Matrix and Tensor Computation"
---

# Caracal: A GPU-Resident Sparse LU Solver with Lightweight Fine-Grained Scheduling

**中文标题：** 采用轻量细粒度调度的 GPU 常驻稀疏 LU 求解器

**所属 Session：** [Algorithms: Sparse Matrix and Tensor Computation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Algorithms: Sparse Matrix and Tensor Computation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Algorithms: Sparse Matrix and Tensor Computation</p>
</div>

**作者**：Jie Ren; Tingxuan Zhong; Yuxi Hong; Guofeng Feng; Xincheng Wang; Weile Jia; Hatem Ltaief; David Keyes

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap255&sess=sess170)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

We address inefficiencies in task scheduling, memory management, and scalability in GPU-resident sparse LU factorization with a two-level approach of sequentially scheduled coarse-grained blocks containing multiple fine-grained blocks managed with a lightweight static scheduler enabling multi-stream parallelism. Additionally, we design an intelligent memory caching mechanism for the fine-grained scheduler, which retains frequently accessed data in GPU memory. To further enhance scalability, we introduce a distributed memory design that partitions the input matrix using a 1D block-cyclic distribution and optimizes inter-GPU communication via NVLink. The multi-GPU design reaches a computational throughput of 6.46 TFLOP/s on four A100 GPUs, demonstrating promising scalability. This is up to 7x speedup over the latest \texttt{SuperLU\_DIST} with 3D communication, 94x speedup over \texttt{PanguLU}, 16x speedup over \texttt{PasTiX}, and 10x speedup over our own coarse-grained dynamic schedul

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
