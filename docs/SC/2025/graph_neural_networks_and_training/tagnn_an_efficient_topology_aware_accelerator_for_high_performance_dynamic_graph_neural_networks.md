---
title: "TaGNN: An Efficient Topology-Aware Accelerator for High-Performance Dynamic Graph Neural Networks"
description: "SC 2025 · Graph Neural Networks and Training · Hui Yu; Yu Zhang; Ligang He; Bing Peng; Jin Zhao; Zixiao Wang; Hao Qi; Hai Jin"
tags:
  - "SC2025"
  - "Graph Neural Networks and Training"
---

# TaGNN: An Efficient Topology-Aware Accelerator for High-Performance Dynamic Graph Neural Networks

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Neural Networks and Training。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Neural Networks and Training</p>
</div>

**作者**：Hui Yu; Yu Zhang; Ligang He; Bing Peng; Jin Zhao; Zixiao Wang; Hao Qi; Hai Jin

**会议**：SC 2025 · St. Louis, MO

## 摘要

Existing DGNN solutions still suffer from low data parallelism. To address this problem, we propose the topology-aware DGNN accelerator TaGNN. It presents a topology-aware concurrent execution approach in the accelerator design that calculates the final features of affected vertices while ensuring that unaffected vertices are loaded and computed only once per layer across multiple snapshots, maximizing data parallelism while minimizing memory usage. TaGNN develops a similarity-aware cell skipping strategy to selectively reuse the RNN results from the previous snapshot to bypass RNN operations, further improving data parallelism with minimal accuracy loss. TaGNN on a Xilinx Alveo U280 FPGA shows average speedups of 535.2x and 84.3x, and energy savings of 742.6x and 104.9x over state-of-the-art software DGNNs on Intel Xeon CPUs and NVIDIA A100 GPUs, respectively. TaGNN also outperforms DGNN-Booster, E-DGCN, and Cambricon-DG by average speedups of 13.5x, 10.2x, and 6.5x and energy savings

---

## 一句话总结

> 该工作属于 Graph Neural Networks and Training 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Graph Neural Networks and Training 领域贡献新的设计范式或评估框架。
