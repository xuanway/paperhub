---
title: "NNQS-SCI: Tackling Trillion-Dimensional Hilbert Space with Adaptive Neural Network Quantum States"
description: "SC 2025 · Applications: Atomistic Modeling · Bowen Kan; Yumeng Zhou; Daiyou Xie; Pengyu Zhou; Yunquan Zhang; Honghui Shang"
tags:
  - "SC2025"
  - "Applications: Atomistic Modeling"
---

# NNQS-SCI: Tackling Trillion-Dimensional Hilbert Space with Adaptive Neural Network Quantum States

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Applications: Atomistic Modeling。</p>
<p class="paper-seo-summary__tags">SC 2025 · Applications: Atomistic Modeling</p>
</div>

**作者**：Bowen Kan; Yumeng Zhou; Daiyou Xie; Pengyu Zhou; Yunquan Zhang; Honghui Shang

**会议**：SC 2025 · St. Louis, MO

## 摘要

Neural network quantum states (NNQS) offer a powerful variational Monte Carlo (VMC) approach for quantum many-body problems, balancing polynomial scaling with high expressive power. However, scaling NNQS to large chemical systems faces challenges in preserving accuracy with exact energy and managing vast configurations efficiently. In this work, we introduce NNQS-SCI, a high-performance selected configuration interaction (SCI) based NNQS method designed to overcome these limitations. NNQS-SCI employs highly parallelized Slater-Condon rules for fast local energy evaluations, avoiding accuracy loss, while its adaptive SCI engine dynamically manages billions of configurations without space explosion or arbitrary cutoffs that plague other NNQS-CI approaches. Optimized for extreme scalability via multi-level parallelism and memory compression, NNQS-SCI successfully simulates systems up to 152 spin orbitals, tackling Hilbert space dimensions exceeding 10$^{14}$ and demonstrating significant 

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
