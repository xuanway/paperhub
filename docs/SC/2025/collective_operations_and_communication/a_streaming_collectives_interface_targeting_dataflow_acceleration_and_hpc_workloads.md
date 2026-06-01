---
title: "A Streaming Collectives Interface Targeting Dataflow Acceleration and HPC Workloads"
description: "SC 2025 · Collective Operations and Communication · Nicholas Contini; Jake Queiser; Bharath Ramesh; Hari Subramoni; Dhabaleswar Pand"
tags:
  - "SC2025"
  - "Collective Operations and Communication"
---

# A Streaming Collectives Interface Targeting Dataflow Acceleration and HPC Workloads

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Collective Operations and Communication。</p>
<p class="paper-seo-summary__tags">SC 2025 · Collective Operations and Communication</p>
</div>

**作者**：Nicholas Contini; Jake Queiser; Bharath Ramesh; Hari Subramoni; Dhabaleswar Panda

**会议**：SC 2025 · St. Louis, MO

## 摘要

Dataflow accelerators can provide energy-efficient and high-performance alternatives to current popular architectures. However, little work has been done to enable accelerator-initiated, scalable collective communication for these architectures. We develop a high-level synthesis (HLS) interface to bridge this gap through software-hardware co-design. Given the tendency of dataflow applications to use reads and writes to streams to express data transfer, we develop a streaming interface implementing fine-grained transfers to the host processor. Data can then be communicated through MPI and transferred to the receiving accelerator. As a result, the interface uses few hardware resources for communication. As a case study, we enhance the HPL benchmark from HPCC_FPGA with our contributions. We evaluate our final design on up to 16 FPGAs, achieving up to 18% improvement in application throughput and 36% reduced latency in kernel execution. Additionally, we design a stencil benchmark that show

---

## 一句话总结

> 该工作属于 Collective Operations and Communication 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Collective Operations and Communication 领域贡献新的设计范式或评估框架。
