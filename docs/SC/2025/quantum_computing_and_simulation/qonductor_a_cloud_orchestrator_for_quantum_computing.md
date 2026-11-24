---
title: "Qonductor: A Cloud Orchestrator for Quantum Computing"
description: "SC 2025 · Quantum Computing and Simulation · Emmanouil Giortamis; Francisco Romao; Nathaniel Tornow; Dmitry Lugovoy; Pramod B"
tags:
  - "SC2025"
  - "Quantum Computing and Simulation"
---

# Qonductor: A Cloud Orchestrator for Quantum Computing

**中文标题：** 面向量子计算的云编排器

**所属 Session：** [Quantum Computing and Simulation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Quantum Computing and Simulation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Quantum Computing and Simulation</p>
</div>

**作者**：Emmanouil Giortamis; Francisco Romao; Nathaniel Tornow; Dmitry Lugovoy; Pramod Bhatotia

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap193&sess=sess164)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

We describe Qonductor, a cloud orchestrator for hybrid quantum-classical applications that run on heterogeneous hybrid resources. Qonductor abstracts away the complexity of hybrid programming and resource management by exposing the Qonductor API, a high-level and hardware-agnostic API. The resource estimator strategically balances quantum and classical resources to mitigate resource contention and the effects of hardware noise. The hybrid scheduler automates job scheduling on hybrid resources and balances the tradeoff between users’ objectives of QoS and the cloud operator’s objective of resource efficiency. We implement an open-source prototype and evaluate Qonductor using more than 7,000 real quantum runs on the IBM Quantum Cloud to simulate real cloud workloads. Qonductor achieves up to 54% lower job completion times (JCTs) while sacrificing 3% execution quality; balances the load across QPU, which increases quantum resource utilization by up to 66%; and scales with growing system s

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
