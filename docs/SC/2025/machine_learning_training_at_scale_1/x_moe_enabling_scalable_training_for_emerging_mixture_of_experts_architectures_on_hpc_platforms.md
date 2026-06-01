---
title: "X-MoE: Enabling Scalable Training for Emerging Mixture-of-Experts Architectures on HPC Platforms"
description: "SC 2025 · Machine Learning: Training at Scale 1 · Yueming Yuan; Ahan Gupta; Jianping Li; Sajal Dash; Feiyi Wang; Minjia Zhang"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 1"
---

# X-MoE: Enabling Scalable Training for Emerging Mixture-of-Experts Architectures on HPC Platforms

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 1</p>
</div>

**作者**：Yueming Yuan; Ahan Gupta; Jianping Li; Sajal Dash; Feiyi Wang; Minjia Zhang

**会议**：SC 2025 · St. Louis, MO

## 摘要

Emerging expert-specialized Mixture-of-Experts (MoE) architectures, such as DeepSeek-MoE, deliver strong model quality through fine-grained expert segmentation and large top-k routing. However, their scalability is limited by substantial activation memory overhead and costly all-to-all communication. Furthermore, current MoE training systems—primarily optimized for NVIDIA GPUs—perform suboptimally on non-NVIDIA platforms, leaving significant computational potential untapped. In this work, we present X-MoE, a novel MoE training system designed to deliver scalable training performance for next-generation MoE architectures. X-MoE achieves this via several novel techniques, including efficient padding-free MoE training with cross-platform kernels, redundancy-bypassing dispatch, and hybrid parallelism with sequence-sharded MoE blocks. Our evaluation on the Frontier supercomputer, powered by AMD MI250X GPUs, shows that X-MoE scales DeepSeek-style MoEs up to 545 billion parameters across 1,02

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
