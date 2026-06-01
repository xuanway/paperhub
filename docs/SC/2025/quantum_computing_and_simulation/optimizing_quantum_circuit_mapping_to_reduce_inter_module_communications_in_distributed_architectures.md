---
title: "Optimizing Quantum Circuit Mapping to Reduce Inter-Module Communications in Distributed Architectures"
description: "SC 2025 · Quantum Computing and Simulation · Longshan Xu; Edwin Hsing-Mean Sha; Xiulin Cui; Qingfeng Zhuge"
tags:
  - "SC2025"
  - "Quantum Computing and Simulation"
---

# Optimizing Quantum Circuit Mapping to Reduce Inter-Module Communications in Distributed Architectures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Quantum Computing and Simulation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Quantum Computing and Simulation</p>
</div>

**作者**：Longshan Xu; Edwin Hsing-Mean Sha; Xiulin Cui; Qingfeng Zhuge

**会议**：SC 2025 · St. Louis, MO

## 摘要

Modular quantum architectures have emerged as a promising solution for scalable quantum computing systems. Executing circuits in such distributed systems necessitates non-local operations between modules, incurring significant communication overhead. In this work, an optimized quantum circuit mapping technique called DQTetris is proposed to reduce inter-module communications. DQTetris employs a hierarchical framework that first seeks a global communication-free qubit mapping assignment under module capacity constraints. If infeasible, it searches for subcircuits with local communication-free qubit assignments via layer-wise gate pruning. Executing adjacent subcircuits with different qubit assignments incurs inter-module data teleportation. DQTetris minimizes these overheads by reducing qubit reassignment events through optimal circuit segmentation, qubit assignment selection, and adaptive gate teleportation. Experiments show that compared with existing methods, DQTetris can achieve ave

---

## 一句话总结

> 该工作属于 Quantum Computing and Simulation 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Quantum Computing and Simulation 领域贡献新的设计范式或评估框架。
