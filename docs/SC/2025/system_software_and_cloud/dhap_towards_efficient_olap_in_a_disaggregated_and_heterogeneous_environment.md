---
title: "DHAP: Towards Efficient OLAP in a Disaggregated and Heterogeneous Environment"
description: "SC 2025 · System Software and Cloud · Guangda Liu; Chenqi Zhang; Yizhou Shan; Hao Feng; Zeke Wang; Shixuan Sun; Minyi "
tags:
  - "SC2025"
  - "System Software and Cloud"
---

# DHAP: Towards Efficient OLAP in a Disaggregated and Heterogeneous Environment

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud</p>
</div>

**作者**：Guangda Liu; Chenqi Zhang; Yizhou Shan; Hao Feng; Zeke Wang; Shixuan Sun; Minyi Guo; Jieru Zhao

**会议**：SC 2025 · St. Louis, MO

## 摘要

Disaggregation of hardware resources and integration of heterogeneous accelerators are two emerging trends in datacenters. Existing data systems focus on either disaggregated systems with CPUs or incorporation of heterogeneous accelerators within traditional monolithic servers. None can adequately address the challenges posed by systems that are both disaggregated and heterogeneous. We present DHAP, an end-to-end framework comprising a query compiler and a specialized runtime, designed to efficiently process online analytical queries in a disaggregated and heterogeneous environment. At higher levels the compiler, a planning module, automatically identifies efficient execution plans. At lower levels, optimizations are applied to generate executable code for heterogeneous back-ends. The runtime efficiently processes queries on disaggregated CPU/GPU compute nodes, facilitating inter-stage pipelined execution and minimizing communication costs. Experiments show that DHAP achieves near-opti

---

## 一句话总结

> 该工作属于 System Software and Cloud 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 System Software and Cloud 领域贡献新的设计范式或评估框架。
