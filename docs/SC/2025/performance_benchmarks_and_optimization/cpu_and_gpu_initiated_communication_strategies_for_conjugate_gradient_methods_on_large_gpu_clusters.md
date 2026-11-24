---
title: "CPU- and GPU-Initiated Communication Strategies for Conjugate Gradient Methods on Large GPU Clusters"
description: "SC 2025 · Performance: Benchmarks and Optimization · James D. Trotter; Sinan Ekmekcibasi; Doğan Sağbili; Johannes Langguth; Xing Cai;"
tags:
  - "SC2025"
  - "Performance: Benchmarks and Optimization"
---

# CPU- and GPU-Initiated Communication Strategies for Conjugate Gradient Methods on Large GPU Clusters

**中文标题：** 大型 GPU 集群上共轭梯度方法的 CPU 与 GPU 发起通信策略

**所属 Session：** [Performance: Benchmarks and Optimization](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Benchmarks and Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Benchmarks and Optimization</p>
</div>

**作者**：James D. Trotter; Sinan Ekmekcibasi; Doğan Sağbili; Johannes Langguth; Xing Cai; Didem Unat

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap159&sess=sess184)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Strong scaling of conjugate gradient (CG) algorithms on GPU-based supercomputers is notoriously challenging. These linear system solvers have low computational intensity, making inter-GPU communication and synchronization primary bottlenecks. In light of recent developments in multi-GPU communication, we revisit CG parallelization for large-scale GPU clusters. We implement standard and pipelined CG solvers using three flavors of multi-GPU communication: GPU-aware MPI, NVIDIA's NCCL/AMD's RCCL, and NVIDIA's NVSHMEM. Our monolithic NVSHMEM-based implementation with GPU-initiated communication enables CPU-free execution and thus lower overhead. However, lack of vendor-supported device-side computational kernels means that CPU-controlled CG implementations based on GPU-aware MPI or NCCL/RCCL are still favored for small GPU counts. Compared with state-of-the-art CG implementations, we have also eliminated unnecessary CPU-GPU data transfers and synchronization points. Our CG implementations

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
