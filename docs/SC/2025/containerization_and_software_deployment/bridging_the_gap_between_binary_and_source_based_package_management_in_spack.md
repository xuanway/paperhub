---
title: "Bridging the Gap Between Binary and Source-Based Package Management in Spack"
description: "SC 2025 · Containerization and Software Deployment · John Gouwar; Gregory Becker; Tamara Dahlgren; Nathan Hanford; Arjun Guha; Todd G"
tags:
  - "SC2025"
  - "Containerization and Software Deployment"
---

# Bridging the Gap Between Binary and Source-Based Package Management in Spack

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Containerization and Software Deployment。</p>
<p class="paper-seo-summary__tags">SC 2025 · Containerization and Software Deployment</p>
</div>

**作者**：John Gouwar; Gregory Becker; Tamara Dahlgren; Nathan Hanford; Arjun Guha; Todd Gamblin

**会议**：SC 2025 · St. Louis, MO

## 摘要

Binary package managers install software quickly but limit configurability due to rigid ABI requirements that ensure compatibility between binaries. Source package managers provide flexibility in building software, but compilation can be slow. For example, installing an HPC code with a new MPI implementation typically results in a full rebuild. Spack, a widely deployed, HPC-focused package manager, can use source and pre-compiled binaries, but without a binary compatibility model, it is unable to install binaries not built together. We present {\it splicing}, an extension to Spack that models binary compatibility between packages and allows seamless mixing of source and binary distributions. Splicing augments Spack's packaging language and dependency resolution engine to reuse compatible binaries while maintaining the flexibility of source builds. This extension incurs minimal installation-time overhead, and it allows rapid installation from binaries, even for ABI-sensitive dependencie

---

## 一句话总结

> 该工作属于 Containerization and Software Deployment 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Containerization and Software Deployment 领域贡献新的设计范式或评估框架。
