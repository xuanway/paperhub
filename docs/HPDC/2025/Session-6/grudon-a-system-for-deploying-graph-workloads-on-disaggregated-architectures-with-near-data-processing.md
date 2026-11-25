---
title: "Grudon: A System for Deploying Graph Workloads on Disaggregated Architectures with Near-Data Processing"
description: "HPDC 2025 · Session 6 — Tuning and Performance"
tags:
  - "HPDC2025"
  - "Session 6"
  - "Tuning and Performance"
---

# Grudon: A System for Deploying Graph Workloads on Disaggregated Architectures with Near-Data Processing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 6 — Tuning and Performance（2025年7月23日 10:30–12:15 · Session Chair：Jay Lofstead）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 6</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731585) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/rao.pdf)

**作者**：Vishal Rao, Nikhil Ram Shashidhar, Suyeon Lee, Ada Gavrilovska

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 6 — Tuning and Performance（2025年7月23日 10:30–12:15 · Session Chair：Jay Lofstead）

---

## 英文摘要

Emerging memory disaggregation and near-data processing (NDP) technologies have shown promise in addressing performance, scaling and efficiency challenges for data-intensive workloads such as graph analytics. However, they expose new tradeoffs related to data movement, runtime, and cost. This paper introduces Grudon, a novel system for deploying graph workloads on Disaggregated NDP (DiNDP) platforms. Grudon combines the benefits of memory disaggregation and NDP to tackle bandwidth limitations, improve resource flexibility, and reduce energy demands to improve overall workload performance. To achieve this, Grudon provides support for dynamic configuration of graph workload deployments on DiNDP platforms via new control plane functionality that enables lightweight evaluation of the tradeoff space and dynamic reconfiguration of operations executed on the different DiNDP elements. Evaluation on an emulated DiNDP testbed demonstrates that Grudon achieves a geomean speedup of 2.12× while reducing energy consumption by 3.3× compared to state-of-the-art distributed runtimes. These results show the potential to unlock the full capabilities of DiNDP platforms for efficient distributed graph analytics.

## 中文摘要

新兴的内存解聚与近数据处理（NDP）技术在应对图分析等数据密集型负载的性能、扩展与效率挑战方面展现出前景。然而，它们也带来了与数据移动、运行时和成本相关的新权衡。本文提出 Grudon，一个在解聚 NDP（DiNDP）平台上部署图负载的新系统。Grudon 结合内存解聚与 NDP 的优势，以缓解带宽限制、提升资源灵活性并降低能耗，从而改善整体负载性能。为此，Grudon 通过新的控制平面功能支持 DiNDP 平台上图负载部署的动态配置，该功能可对权衡空间进行轻量评估，并对在不同 DiNDP 元素上执行的操作进行动态重配置。在仿真 DiNDP 测试床上的评估表明，与最先进的分布式运行时相比，Grudon 取得 2.12 倍的几何平均加速，同时将能耗降低 3.3 倍。这些结果表明了释放 DiNDP 平台全部能力以实现高效分布式图分析的潜力。

---

[← 返回 Session 6 — Tuning and Performance](index.md)
