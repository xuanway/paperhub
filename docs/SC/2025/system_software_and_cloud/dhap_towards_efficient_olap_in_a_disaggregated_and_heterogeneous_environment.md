---
title: "DHAP: Towards Efficient OLAP in a Disaggregated and Heterogeneous Environment"
description: "SC 2025 · System Software and Cloud · Guangda Liu; Chenqi Zhang; Yizhou Shan; Hao Feng; Zeke Wang; Shixuan Sun; Minyi "
tags:
  - "SC2025"
  - "System Software and Cloud"
---

# DHAP: Towards Efficient OLAP in a Disaggregated and Heterogeneous Environment

**中文标题：** 面向解耦异构环境的高效联机分析处理

**所属 Session：** [System Software and Cloud](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud</p>
</div>

**作者**：Guangda Liu; Chenqi Zhang; Yizhou Shan; Hao Feng; Zeke Wang; Shixuan Sun; Minyi Guo; Jieru Zhao

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap197&sess=sess287)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Disaggregation of hardware resources and integration of heterogeneous accelerators are two emerging trends in datacenters. Existing data systems focus on either disaggregated systems with CPUs or incorporation of heterogeneous accelerators within traditional monolithic servers. None can adequately address the challenges posed by systems that are both disaggregated and heterogeneous. We present DHAP, an end-to-end framework comprising a query compiler and a specialized runtime, designed to efficiently process online analytical queries in a disaggregated and heterogeneous environment. At higher levels the compiler, a planning module, automatically identifies efficient execution plans. At lower levels, optimizations are applied to generate executable code for heterogeneous back-ends. The runtime efficiently processes queries on disaggregated CPU/GPU compute nodes, facilitating inter-stage pipelined execution and minimizing communication costs. Experiments show that DHAP achieves near-opti

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
