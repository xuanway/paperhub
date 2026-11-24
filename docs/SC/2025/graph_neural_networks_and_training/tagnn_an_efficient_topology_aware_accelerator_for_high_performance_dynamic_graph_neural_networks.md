---
title: "TaGNN: An Efficient Topology-Aware Accelerator for High-Performance Dynamic Graph Neural Networks"
description: "SC 2025 · Graph Neural Networks and Training · Hui Yu; Yu Zhang; Ligang He; Bing Peng; Jin Zhao; Zixiao Wang; Hao Qi; Hai Jin"
tags:
  - "SC2025"
  - "Graph Neural Networks and Training"
---

# TaGNN: An Efficient Topology-Aware Accelerator for High-Performance Dynamic Graph Neural Networks

**中文标题：** 面向高性能动态图神经网络的高效拓扑感知加速器

**所属 Session：** [Graph Neural Networks and Training](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Neural Networks and Training。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Neural Networks and Training</p>
</div>

**作者**：Hui Yu; Yu Zhang; Ligang He; Bing Peng; Jin Zhao; Zixiao Wang; Hao Qi; Hai Jin

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap407&sess=sess282)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Existing DGNN solutions still suffer from low data parallelism. To address this problem, we propose the topology-aware DGNN accelerator TaGNN. It presents a topology-aware concurrent execution approach in the accelerator design that calculates the final features of affected vertices while ensuring that unaffected vertices are loaded and computed only once per layer across multiple snapshots, maximizing data parallelism while minimizing memory usage. TaGNN develops a similarity-aware cell skipping strategy to selectively reuse the RNN results from the previous snapshot to bypass RNN operations, further improving data parallelism with minimal accuracy loss. TaGNN on a Xilinx Alveo U280 FPGA shows average speedups of 535.2x and 84.3x, and energy savings of 742.6x and 104.9x over state-of-the-art software DGNNs on Intel Xeon CPUs and NVIDIA A100 GPUs, respectively. TaGNN also outperforms DGNN-Booster, E-DGCN, and Cambricon-DG by average speedups of 13.5x, 10.2x, and 6.5x and energy savings

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
