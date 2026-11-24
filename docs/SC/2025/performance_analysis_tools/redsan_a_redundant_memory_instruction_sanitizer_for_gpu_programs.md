---
title: "RedSan: A Redundant Memory Instruction Sanitizer for GPU Programs"
description: "SC 2025 · Performance: Analysis Tools · Yanbo Zhao; Yueming Hao; Zecheng Li; Shuyin Jiao; Xu Liu; Jiajia Li"
tags:
  - "SC2025"
  - "Performance: Analysis Tools"
---

# RedSan: A Redundant Memory Instruction Sanitizer for GPU Programs

**中文标题：** 面向 GPU 程序的冗余内存指令检测器

**所属 Session：** [Performance: Analysis Tools](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Analysis Tools。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Analysis Tools</p>
</div>

**作者**：Yanbo Zhao; Yueming Hao; Zecheng Li; Shuyin Jiao; Xu Liu; Jiajia Li

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap464&sess=sess342)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

CUDA is the de facto programming model for GPUs, widely used in the domains of HPC and AI. To obtain bare-metal performance, vendors and academics develop various profiling tools to guide optimization. However, most existing tools focus on hotspot analysis with limited capabilities in identifying actionable opportunities. To complement existing tools, we present RedSan, a novel profiling tool that leverages binary instrumentation to identify redundant instructions in fully optimized CUDA programs. Guided by RedSan, we are able to optimize programs such as PolybenchGPU, Rodinia, PASTA, DARKNET, and LULESH, yielding up to a 6.27× speedup and 3.00× reduction in memory instructions.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
