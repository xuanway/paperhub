---
title: "ODOS-MPI: HPC-Friendly SmartNIC Offloading of Computation/Communication Kernels"
description: "SC 2025 · Programming Frameworks · Muhammad Usman; Mariano Benito; Sergio Iserte; Antonio J. Peña"
tags:
  - "SC2025"
  - "Programming Frameworks"
---

# ODOS-MPI: HPC-Friendly SmartNIC Offloading of Computation/Communication Kernels

**中文标题：** 计算与通信内核在智能网卡上的 HPC 友好卸载

**所属 Session：** [Programming Frameworks](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Programming Frameworks。</p>
<p class="paper-seo-summary__tags">SC 2025 · Programming Frameworks</p>
</div>

**作者**：Muhammad Usman; Mariano Benito; Sergio Iserte; Antonio J. Peña

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap318&sess=sess294)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

The increasing complexity and scale of high performance computing (HPC) workloads demand innovative approaches to optimize both computation and communication. While OpenMP has been widely adopted for intra-node parallelism and MPI for inter-node communication, emerging SmartNICs introduce new opportunities for offloading communication-intensive tasks. In this work, we extend OpenMP to support MPI kernel offloading to SmartNICs. Our implementation integrates Open MPI communication offloading into the LLVM compiler while utilizing DOCA SDK for efficient interaction with NVIDIA BlueField DPUs. Leveraging OpenMP eliminates the need for direct low-level programming, lowering the entry barrier for domain scientists. We demonstrate our framework’s versatility by implementing a SmartNIC-enabled version of the MPI OSU micro-benchmarks and improving the execution time of an atmospheric weather simulation by over 18%, thanks to concurrent computation and communication.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
