---
title: "Story of Two GPUs: Characterizing the Resilience of Hopper H100 and Ampere A100 GPUs"
description: "SC 2025 · Anomaly Detection, Failure Management, and Resilience 2 · Shengkun Cui; Archit Patke; Hung Nguyen; Aditya Ranjan; Ziheng Chen; Phuong Cao;"
tags:
  - "SC2025"
  - "Anomaly Detection, Failure Management, and Resilience 2"
---

# Story of Two GPUs: Characterizing the Resilience of Hopper H100 and Ampere A100 GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Anomaly Detection, Failure Management, and Resilience 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Anomaly Detection, Failure Management, and Resilience 2</p>
</div>

**作者**：Shengkun Cui; Archit Patke; Hung Nguyen; Aditya Ranjan; Ziheng Chen; Phuong Cao; Gregory Bauer; Brett Bode; Catello Di Martino; Saurabh Jha; Chandra Narayanaswami; Daby Sow; Zbigniew T. Kalbarczyk; Ravishankar K. Iyer

**会议**：SC 2025 · St. Louis, MO

## 摘要

This study characterizes GPU resilience in Delta, a large-scale AI system that consists of 1,056 A100 and H100 GPUs, with over 1,300 petaflops of peak throughput. We used 2.5 years of operational data (11.7 million GPU hours) on GPU errors. Our major findings include: 1) H100 GPU memory resilience is worse than A100 GPU memory, with 3.2x lower per-GPU MTBE for memory errors. 2) The GPU memory error-recovery mechanisms on H100 GPUs are insufficient to handle the increased memory capacity. 3) H100 GPUs demonstrate significantly improved GPU hardware resilience over A100 GPUs with respect to critical hardware components. 4) GPU errors on both A100 and H100 GPUs frequently result in job failures due to the lack of robust recovery mechanisms at the application level. 5) We project the impact of GPU node availability on larger scales and find that significant overprovisioning of 5% is necessary to handle GPU failures.

---

## 一句话总结

> 该工作属于 Anomaly Detection, Failure Management, and Resilience 2 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Anomaly Detection, Failure Management, and Resilience 2 领域贡献新的设计范式或评估框架。
