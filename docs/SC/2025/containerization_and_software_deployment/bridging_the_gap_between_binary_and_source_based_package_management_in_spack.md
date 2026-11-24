---
title: "Bridging the Gap Between Binary and Source-Based Package Management in Spack"
description: "SC 2025 · Containerization and Software Deployment · John Gouwar; Gregory Becker; Tamara Dahlgren; Nathan Hanford; Arjun Guha; Todd G"
tags:
  - "SC2025"
  - "Containerization and Software Deployment"
---

# Bridging the Gap Between Binary and Source-Based Package Management in Spack

**中文标题：** 弥合 Spack 中二进制与源码包管理的差距

**所属 Session：** [Containerization and Software Deployment](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Containerization and Software Deployment。</p>
<p class="paper-seo-summary__tags">SC 2025 · Containerization and Software Deployment</p>
</div>

**作者**：John Gouwar; Gregory Becker; Tamara Dahlgren; Nathan Hanford; Arjun Guha; Todd Gamblin

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap246&sess=sess171)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Binary package managers install software quickly but limit configurability due to rigid ABI requirements that ensure compatibility between binaries. Source package managers provide flexibility in building software, but compilation can be slow. For example, installing an HPC code with a new MPI implementation typically results in a full rebuild. Spack, a widely deployed, HPC-focused package manager, can use source and pre-compiled binaries, but without a binary compatibility model, it is unable to install binaries not built together. We present {\it splicing}, an extension to Spack that models binary compatibility between packages and allows seamless mixing of source and binary distributions. Splicing augments Spack's packaging language and dependency resolution engine to reuse compatible binaries while maintaining the flexibility of source builds. This extension incurs minimal installation-time overhead, and it allows rapid installation from binaries, even for ABI-sensitive dependencie

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
