---
title: "TraceFlow: Efficient Trace Analysis for Large-Scale Parallel Applications via Interaction Pattern-Aware Trace Distribution"
description: "SC 2025 · Performance: Analysis Tools · Yuyang Jin; Xirui Shui; Mingshu Zhai; Zan Zong; Feng Zhang; Felix Wolf; Jidong Z"
tags:
  - "SC2025"
  - "Performance: Analysis Tools"
---

# TraceFlow: Efficient Trace Analysis for Large-Scale Parallel Applications via Interaction Pattern-Aware Trace Distribution

**中文标题：** 通过交互模式感知的轨迹分发高效分析大规模并行应用轨迹

**所属 Session：** [Performance: Analysis Tools](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Analysis Tools。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Analysis Tools</p>
</div>

**作者**：Yuyang Jin; Xirui Shui; Mingshu Zhai; Zan Zong; Feng Zhang; Felix Wolf; Jidong Zhai

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap155&sess=sess342)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Trace analysis of large-scale parallel applications is crucial for understanding and optimizing performance. It primarily focuses on the interaction behaviors between different parallel processes, such as synchronization waits and asynchronous overlaps. The trace size explodes as the parallel scale of applications, thus current methods analyze traces in parallel to ensure analysis speed. However, due to the interaction pattern-agnostic trace distribution, they often introduce inter-process communications to fetch non-local event data during interaction analysis, leading to excessively long trace analysis time. To address this issue, we propose TraceFlow, a trace analysis tool for large-scale parallel applications, which achieves a nearly communication-free analysis through an interaction pattern-aware trace distribution strategy. We evaluate the efficiency of TraceFlow on widely used benchmarks and several real-world applications with up to 8,192 processes. Experimental results show th

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
