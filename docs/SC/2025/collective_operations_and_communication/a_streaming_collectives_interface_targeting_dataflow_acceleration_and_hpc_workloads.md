---
title: "A Streaming Collectives Interface Targeting Dataflow Acceleration and HPC Workloads"
description: "SC 2025 · Collective Operations and Communication · Nicholas Contini; Jake Queiser; Bharath Ramesh; Hari Subramoni; Dhabaleswar Pand"
tags:
  - "SC2025"
  - "Collective Operations and Communication"
---

# A Streaming Collectives Interface Targeting Dataflow Acceleration and HPC Workloads

**中文标题：** 面向数据流加速与 HPC 工作负载的流式集合通信接口

**所属 Session：** [Collective Operations and Communication](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Collective Operations and Communication。</p>
<p class="paper-seo-summary__tags">SC 2025 · Collective Operations and Communication</p>
</div>

**作者**：Nicholas Contini; Jake Queiser; Bharath Ramesh; Hari Subramoni; Dhabaleswar Panda

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap339&sess=sess296)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Dataflow accelerators can provide energy-efficient and high-performance alternatives to current popular architectures. However, little work has been done to enable accelerator-initiated, scalable collective communication for these architectures. We develop a high-level synthesis (HLS) interface to bridge this gap through software-hardware co-design. Given the tendency of dataflow applications to use reads and writes to streams to express data transfer, we develop a streaming interface implementing fine-grained transfers to the host processor. Data can then be communicated through MPI and transferred to the receiving accelerator. As a result, the interface uses few hardware resources for communication. As a case study, we enhance the HPL benchmark from HPCC_FPGA with our contributions. We evaluate our final design on up to 16 FPGAs, achieving up to 18% improvement in application throughput and 36% reduced latency in kernel execution. Additionally, we design a stencil benchmark that show

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
