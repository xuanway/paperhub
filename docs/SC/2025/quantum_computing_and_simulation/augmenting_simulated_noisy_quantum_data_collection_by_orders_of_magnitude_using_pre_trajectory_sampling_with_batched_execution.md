---
title: "Augmenting Simulated Noisy Quantum Data Collection by Orders of Magnitude Using Pre-Trajectory Sampling with Batched Execution"
description: "SC 2025 · Quantum Computing and Simulation · Taylor Lee Patti; Thien Nguyen; Justin Gage Lietz; Alex J. McCaskey; Brucek Khai"
tags:
  - "SC2025"
  - "Quantum Computing and Simulation"
---

# Augmenting Simulated Noisy Quantum Data Collection by Orders of Magnitude Using Pre-Trajectory Sampling with Batched Execution

**中文标题：** 利用批量执行的轨迹前采样将模拟含噪量子数据采集提高多个数量级

**所属 Session：** [Quantum Computing and Simulation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Quantum Computing and Simulation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Quantum Computing and Simulation</p>
</div>

**作者**：Taylor Lee Patti; Thien Nguyen; Justin Gage Lietz; Alex J. McCaskey; Brucek Khailany

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap727&sess=sess164)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Classically simulating quantum systems is challenging, as even noiseless $n$-qubit quantum states scale as $2^n$. The complexity of noisy quantum systems is even greater, requiring $2^n \times 2^n$-dimensional density matrices. Various approximations reduce density matrix overhead, including quantum trajectory-based methods, which instead use an ensemble of $m \ll 2^n$ noisy states. While this method is dramatically more efficient, current implementations use unoptimized sampling, redundant state preparation, and single-shot data collection. In this manuscript, we present the Pre-Trajectory Sampling technique, increasing the efficiency and utility of trajectory simulations by tailoring error types, batching sampling without redundant computation, and collecting error information. We demonstrate the effectiveness of our method with both a mature statevector simulation of a 35-qubit quantum error-correction code and a preliminary tensor network simulation of 85 qubits, yielding speedups

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
