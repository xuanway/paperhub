---
title: "XaaS Containers: Performance-Portable Representation with Source and IR Containers"
description: "SC 2025 · Containerization and Software Deployment · Marcin Copik; Eiman Alnuaimi; Alok Kamatar; Valerie Hayot-Sasson; Alberto Madonn"
tags:
  - "SC2025"
  - "Containerization and Software Deployment"
---

# XaaS Containers: Performance-Portable Representation with Source and IR Containers

**中文标题：** XaaS 容器：通过源代码和中间表示容器实现性能可移植表示

**所属 Session：** [Containerization and Software Deployment](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Containerization and Software Deployment。</p>
<p class="paper-seo-summary__tags">SC 2025 · Containerization and Software Deployment</p>
</div>

**作者**：Marcin Copik; Eiman Alnuaimi; Alok Kamatar; Valerie Hayot-Sasson; Alberto Madonna; Todd Gamblin; Kyle Chard; Ian Foster; Torsten Hoefler

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap711&sess=sess171)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

HPC systems and cloud data centers are converging, and containers are becoming the default software deployment method. While containers simplify software management, they face significant performance challenges: they must sacrifice hardware-specific optimizations to achieve portability. Although HPC containers can use runtime hooks to access optimized libraries and devices, they are limited by ABI compatibility and cannot reverse the effects of early-stage compilation decisions. XaaS containers proposed a vision of performance-portable containers, and we present a practical realization with Source and Intermediate Representation (IR) containers. We delay performance-critical decisions until the target system specification is known. We analyze specialization mechanisms in HPC software and propose a new LLM-assisted method for their automatic discovery. By examining the compilation pipeline, we develop a methodology to build containers optimized for target architectures at deployment tim

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
