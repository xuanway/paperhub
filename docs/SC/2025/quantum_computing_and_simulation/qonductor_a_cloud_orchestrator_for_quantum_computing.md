---
title: "Qonductor: A Cloud Orchestrator for Quantum Computing"
description: "SC 2025 · Quantum Computing and Simulation · Emmanouil Giortamis; Francisco Romao; Nathaniel Tornow; Dmitry Lugovoy; Pramod B"
tags:
  - "SC2025"
  - "Quantum Computing and Simulation"
---

# Qonductor: A Cloud Orchestrator for Quantum Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Quantum Computing and Simulation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Quantum Computing and Simulation</p>
</div>

**作者**：Emmanouil Giortamis; Francisco Romao; Nathaniel Tornow; Dmitry Lugovoy; Pramod Bhatotia

**会议**：SC 2025 · St. Louis, MO

## 摘要

We describe Qonductor, a cloud orchestrator for hybrid quantum-classical applications that run on heterogeneous hybrid resources. Qonductor abstracts away the complexity of hybrid programming and resource management by exposing the Qonductor API, a high-level and hardware-agnostic API. The resource estimator strategically balances quantum and classical resources to mitigate resource contention and the effects of hardware noise. The hybrid scheduler automates job scheduling on hybrid resources and balances the tradeoff between users’ objectives of QoS and the cloud operator’s objective of resource efficiency. We implement an open-source prototype and evaluate Qonductor using more than 7,000 real quantum runs on the IBM Quantum Cloud to simulate real cloud workloads. Qonductor achieves up to 54% lower job completion times (JCTs) while sacrificing 3% execution quality; balances the load across QPU, which increases quantum resource utilization by up to 66%; and scales with growing system s

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
