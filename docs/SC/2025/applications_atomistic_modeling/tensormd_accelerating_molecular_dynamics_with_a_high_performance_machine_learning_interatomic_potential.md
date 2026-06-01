---
title: "TENSORMD: Accelerating Molecular Dynamics with a High-Performance Machine Learning Interatomic Potential"
description: "SC 2025 · Applications: Atomistic Modeling · Yucheng Ouyang; Xin Chen; Ying Liu; Xin Chen; Honghui Shang; Zhenchuan Chen; Ron"
tags:
  - "SC2025"
  - "Applications: Atomistic Modeling"
---

# TENSORMD: Accelerating Molecular Dynamics with a High-Performance Machine Learning Interatomic Potential

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Applications: Atomistic Modeling。</p>
<p class="paper-seo-summary__tags">SC 2025 · Applications: Atomistic Modeling</p>
</div>

**作者**：Yucheng Ouyang; Xin Chen; Ying Liu; Xin Chen; Honghui Shang; Zhenchuan Chen; Rongfen Lin; Xingyu Gao; Lifang Wang; Fang Li; Jiahao Shan; Haifeng Song; Huimin Cui; Xiaobing Feng; Jingling Xue

**会议**：SC 2025 · St. Louis, MO

## 摘要

AI has been integrated into HPC across various scientific fields, significantly enhancing performance. In molecular dynamics simulations, HPC+AI facilitates the investigation of atomic-scale physical properties using machine-learning interatomic potentials (MLIPs). However, general-purpose ML tools (e.g., TensorFlow) used in MLIPs are not optimally matched, leading to missed optimization opportunities due to the higher computational complexity and greater diversity of HPC+AI applications compared to pure AI scenarios. To address this, we introduce TENSORMD, an MLIP independent of existing ML tools, enabling flexible optimizations that standard ML frameworks cannot support. TENSORMD outperforms a state-of-the-art MLIP—winner of the 2020 Gordon Bell Prize and built on an ML tool—by 1.88x on NVIDIA A100 GPU. Additionally, TENSORMD was evaluated on two supercomputers with different architectures, achieving significantly reduced time-to-solution and supporting molecular dynamics simulations

---

## 一句话总结

> 该工作属于 Applications: Atomistic Modeling 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Applications: Atomistic Modeling 领域贡献新的设计范式或评估框架。
