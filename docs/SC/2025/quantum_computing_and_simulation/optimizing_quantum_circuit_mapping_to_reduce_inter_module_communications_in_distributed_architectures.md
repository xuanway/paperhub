---
title: "Optimizing Quantum Circuit Mapping to Reduce Inter-Module Communications in Distributed Architectures"
description: "SC 2025 · Quantum Computing and Simulation · Longshan Xu; Edwin Hsing-Mean Sha; Xiulin Cui; Qingfeng Zhuge"
tags:
  - "SC2025"
  - "Quantum Computing and Simulation"
---

# Optimizing Quantum Circuit Mapping to Reduce Inter-Module Communications in Distributed Architectures

**中文标题：** 优化量子电路映射以减少分布式架构中的模块间通信

**所属 Session：** [Quantum Computing and Simulation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Quantum Computing and Simulation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Quantum Computing and Simulation</p>
</div>

**作者**：Longshan Xu; Edwin Hsing-Mean Sha; Xiulin Cui; Qingfeng Zhuge

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap226&sess=sess164)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Modular quantum architectures have emerged as a promising solution for scalable quantum computing systems. Executing circuits in such distributed systems necessitates non-local operations between modules, incurring significant communication overhead. In this work, an optimized quantum circuit mapping technique called DQTetris is proposed to reduce inter-module communications. DQTetris employs a hierarchical framework that first seeks a global communication-free qubit mapping assignment under module capacity constraints. If infeasible, it searches for subcircuits with local communication-free qubit assignments via layer-wise gate pruning. Executing adjacent subcircuits with different qubit assignments incurs inter-module data teleportation. DQTetris minimizes these overheads by reducing qubit reassignment events through optimal circuit segmentation, qubit assignment selection, and adaptive gate teleportation. Experiments show that compared with existing methods, DQTetris can achieve ave

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
