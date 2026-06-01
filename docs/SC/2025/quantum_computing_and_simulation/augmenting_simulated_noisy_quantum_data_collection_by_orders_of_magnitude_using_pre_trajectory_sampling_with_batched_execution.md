---
title: "Augmenting Simulated Noisy Quantum Data Collection by Orders of Magnitude Using Pre-Trajectory Sampling with Batched Execution"
description: "SC 2025 · Quantum Computing and Simulation · Taylor Lee Patti; Thien Nguyen; Justin Gage Lietz; Alex J. McCaskey; Brucek Khai"
tags:
  - "SC2025"
  - "Quantum Computing and Simulation"
---

# Augmenting Simulated Noisy Quantum Data Collection by Orders of Magnitude Using Pre-Trajectory Sampling with Batched Execution

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Quantum Computing and Simulation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Quantum Computing and Simulation</p>
</div>

**作者**：Taylor Lee Patti; Thien Nguyen; Justin Gage Lietz; Alex J. McCaskey; Brucek Khailany

**会议**：SC 2025 · St. Louis, MO

## 摘要

Classically simulating quantum systems is challenging, as even noiseless $n$-qubit quantum states scale as $2^n$. The complexity of noisy quantum systems is even greater, requiring $2^n \times 2^n$-dimensional density matrices. Various approximations reduce density matrix overhead, including quantum trajectory-based methods, which instead use an ensemble of $m \ll 2^n$ noisy states. While this method is dramatically more efficient, current implementations use unoptimized sampling, redundant state preparation, and single-shot data collection. In this manuscript, we present the Pre-Trajectory Sampling technique, increasing the efficiency and utility of trajectory simulations by tailoring error types, batching sampling without redundant computation, and collecting error information. We demonstrate the effectiveness of our method with both a mature statevector simulation of a 35-qubit quantum error-correction code and a preliminary tensor network simulation of 85 qubits, yielding speedups 

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
