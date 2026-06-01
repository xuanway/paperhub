---
title: "ODOS-MPI: HPC-Friendly SmartNIC Offloading of Computation/Communication Kernels"
description: "SC 2025 · Programming Frameworks · Muhammad Usman; Mariano Benito; Sergio Iserte; Antonio J. Peña"
tags:
  - "SC2025"
  - "Programming Frameworks"
---

# ODOS-MPI: HPC-Friendly SmartNIC Offloading of Computation/Communication Kernels

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Programming Frameworks。</p>
<p class="paper-seo-summary__tags">SC 2025 · Programming Frameworks</p>
</div>

**作者**：Muhammad Usman; Mariano Benito; Sergio Iserte; Antonio J. Peña

**会议**：SC 2025 · St. Louis, MO

## 摘要

The increasing complexity and scale of high performance computing (HPC) workloads demand innovative approaches to optimize both computation and communication. While OpenMP has been widely adopted for intra-node parallelism and MPI for inter-node communication, emerging SmartNICs introduce new opportunities for offloading communication-intensive tasks. In this work, we extend OpenMP to support MPI kernel offloading to SmartNICs. Our implementation integrates Open MPI communication offloading into the LLVM compiler while utilizing DOCA SDK for efficient interaction with NVIDIA BlueField DPUs. Leveraging OpenMP eliminates the need for direct low-level programming, lowering the entry barrier for domain scientists. We demonstrate our framework’s versatility by implementing a SmartNIC-enabled version of the MPI OSU micro-benchmarks and improving the execution time of an atmospheric weather simulation by over 18%, thanks to concurrent computation and communication.

---

## 一句话总结

> 该工作属于 Programming Frameworks 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Programming Frameworks 领域贡献新的设计范式或评估框架。
