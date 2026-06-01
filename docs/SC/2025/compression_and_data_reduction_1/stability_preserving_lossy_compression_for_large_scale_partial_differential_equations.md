---
title: "Stability-Preserving Lossy Compression for Large-Scale Partial Differential Equations"
description: "SC 2025 · Compression and Data Reduction 1 · Qian Gong; Mark Ainsworth; Jieyang Chen; Xin Liang; Liangji Zhu; Ethan Klasky; T"
tags:
  - "SC2025"
  - "Compression and Data Reduction 1"
---

# Stability-Preserving Lossy Compression for Large-Scale Partial Differential Equations

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Compression and Data Reduction 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Compression and Data Reduction 1</p>
</div>

**作者**：Qian Gong; Mark Ainsworth; Jieyang Chen; Xin Liang; Liangji Zhu; Ethan Klasky; Tushar Athawale; Qing Liu; Anand Rangarajan; Sanjay Ranka; Scott Klasky

**会议**：SC 2025 · St. Louis, MO

## 摘要

Checkpoint/Restart (C/R) strategies are vital for fault tolerance in PDE-based scientific simulations, yet traditional checkpointing incurs significant I/O overhead. Lossy compression offers a scalable solution by reducing checkpoint data size, but conventional methods often lack control over physical invariants (e.g., energy), leading to instability such as oscillations or divergence in partial differential equation (PDE) systems. This paper introduces a stability-preserving compression approach tailored for PDE simulations by explicitly controlling kinetic and potential energy perturbations to ensure stable restarts. Extensive experiments conducted across diverse PDE configurations demonstrate that our method maintains numerical stability with minimal error magnification—even across multiple checkpoint-restart cycles—outperforming state-of-the-art lossy compressors. Parallel evaluations on the Frontier supercomputer show up to 8.4× improvement in checkpoint write performance and 6.3×

---

## 一句话总结

> 该工作属于 Compression and Data Reduction 1 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Compression and Data Reduction 1 领域贡献新的设计范式或评估框架。
