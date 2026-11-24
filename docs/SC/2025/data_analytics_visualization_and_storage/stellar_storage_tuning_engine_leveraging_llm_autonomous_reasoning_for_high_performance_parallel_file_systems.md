---
title: "STELLAR: Storage Tuning Engine Leveraging LLM Autonomous Reasoning for High-Performance Parallel File Systems"
description: "SC 2025 · Data Analytics, Visualization, and Storage · Chris Egersdoerfer; Philip Carns; Shane Snyder; Robert Ross; Dong Dai"
tags:
  - "SC2025"
  - "Data Analytics, Visualization, and Storage"
---

# STELLAR: Storage Tuning Engine Leveraging LLM Autonomous Reasoning for High-Performance Parallel File Systems

**中文标题：** 利用大语言模型自主推理为高性能并行文件系统调优存储

**所属 Session：** [Data Analytics, Visualization, and Storage](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Data Analytics, Visualization, and Storage。</p>
<p class="paper-seo-summary__tags">SC 2025 · Data Analytics, Visualization, and Storage</p>
</div>

**作者**：Chris Egersdoerfer; Philip Carns; Shane Snyder; Robert Ross; Dong Dai

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap863&sess=sess283)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

I/O performance is crucial to efficiency in data-intensive scientific computing, but tuning large-scale storage systems is complex, costly, and notoriously manpower-intensive, making it inaccessible for most domain scientists. In this study, we propose STELLAR, an autonomous tuner for high-performance parallel file systems. Our evaluations show that STELLAR always selects near-optimal configurations for the parallel file systems within the first five attempts, even for previously unseen applications. STELLAR’s human-like efficiency is fundamentally different from existing auto-tuning methods, which often require hundreds of thousands of iterations to converge. STELLAR achieves this through Retrieval-Augmented Generation, external tool execution, LLM-based reasoning, and a multi-step agent design to stabilize reasoning and combat hallucinations. STELLAR's architecture opens new avenues for addressing complex system optimization problems, especially those characterized by vast search spa

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
