---
title: "HPC-R1: Characterizing R1-Like Large Reasoning Models on HPC"
description: "SC 2025 · Machine Learning: Training at Scale 1 · Adam Weingram; Duo Zhang; Zhonghao Chen; Hao Qi; Xiaoyi Lu"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 1"
---

# HPC-R1: Characterizing R1-Like Large Reasoning Models on HPC

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 1</p>
</div>

**作者**：Adam Weingram; Duo Zhang; Zhonghao Chen; Hao Qi; Xiaoyi Lu

**会议**：SC 2025 · St. Louis, MO

## 摘要

Large reasoning models (LRMs) are becoming increasingly popular as they offer advanced capabilities in logical inference, mathematical reasoning, and knowledge synthesis, even beyond those of standard language models. However, their complex training workflows present significant challenges in reproducibility, efficiency, and system-level optimization. This paper introduces HPC-R1, a comprehensive characterization of LRM training on a modern HPC cluster. We analyze all major stages, including supervised fine-tuning (SFT), Group Relative Policy Optimization (GRPO)-based reinforcement learning (RL), autoregressive generation, and distillation using customized state-of-the-art frameworks. Our detailed performance analysis reveals key system scaling behaviors. We find that GRPO-based reinforcement learning training is heavily communication-bound, with over 90% of GPU time spent in non-compute operations, and that SFT achieves stable GPU throughput near 9.8 TFLOPs. We also observe inference 

---

## 一句话总结

> 该工作属于 Machine Learning: Training at Scale 1 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Machine Learning: Training at Scale 1 领域贡献新的设计范式或评估框架。
