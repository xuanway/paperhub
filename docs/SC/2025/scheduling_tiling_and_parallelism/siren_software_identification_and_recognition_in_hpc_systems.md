---
title: "SIREN: Software Identification and Recognition in HPC Systems"
description: "SC 2025 · Scheduling, Tiling, and Parallelism · Thomas Jakobsche; Fredrik Robertsén; Jessica R. Jones; Utz-Uwe Haus; Florina M. "
tags:
  - "SC2025"
  - "Scheduling, Tiling, and Parallelism"
---

# SIREN: Software Identification and Recognition in HPC Systems

**中文标题：** HPC 系统中的软件识别与辨认

**所属 Session：** [Scheduling, Tiling, and Parallelism](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Scheduling, Tiling, and Parallelism。</p>
<p class="paper-seo-summary__tags">SC 2025 · Scheduling, Tiling, and Parallelism</p>
</div>

**作者**：Thomas Jakobsche; Fredrik Robertsén; Jessica R. Jones; Utz-Uwe Haus; Florina M. Ciorba

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap735&sess=sess286)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

HPC systems use monitoring and operational data analytics to ensure efficiency, performance, and orderly operations. Application-specific insights are crucial for analyzing the increasing complexity and diversity of HPC workloads, particularly through the identification of unknown software and recognition of repeated executions, which facilitate system optimization and security improvements. However, traditional identification methods using job or file names are unreliable for arbitrary user-provided names. Fuzzy hashing the content of executables detects similarities despite different code versions or compilation approaches while preserving privacy and file integrity, overcoming these limitations. We introduce SIREN, a process-level data collection framework for software identification and recognition. SIREN improves observability in HPC job execution by enabling analysis of process metadata, environment information, and executable fuzzy hashes. Findings from an opt-in deployment camp

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
