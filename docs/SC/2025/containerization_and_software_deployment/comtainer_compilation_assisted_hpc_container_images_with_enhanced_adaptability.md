---
title: "coMtainer: Compilation-Assisted HPC Container Images with Enhanced Adaptability"
description: "SC 2025 · Containerization and Software Deployment · Yuhao Gu; Haoquan Chen; Xianjie Chen; Jiangsu Du; Zhiguang Chen; Nong Xiao; Xian"
tags:
  - "SC2025"
  - "Containerization and Software Deployment"
---

# coMtainer: Compilation-Assisted HPC Container Images with Enhanced Adaptability

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Containerization and Software Deployment。</p>
<p class="paper-seo-summary__tags">SC 2025 · Containerization and Software Deployment</p>
</div>

**作者**：Yuhao Gu; Haoquan Chen; Xianjie Chen; Jiangsu Du; Zhiguang Chen; Nong Xiao; Xianwei Zhang; Yutong Lu

**会议**：SC 2025 · St. Louis, MO

## 摘要

The increasing interconnectivity of HPC systems has highlighted the need for efficient application migration across different environments. Containers, widely adopted for this purpose, simplify deployment but often fail to deliver optimal performance due to the separated build and execution container workflow. This leads to generic container images that miss out on system-specific software stack advantages, a challenge we define as the adaptability issue. We propose coMtainer, a compilation-assisted image transformation framework that embeds build-time information into images. This enables remote HPC systems to specialize and rebuild the container using native toolchains and libraries. coMtainer preserves image neutrality while resolving the adaptability issue, allowing optimized execution without user involvement. Moreover, the embedded metadata unlocks advanced compiler optimizations such as LTO and PGO. We implement and evaluate coMtainer across a variety of real-world HPC applicati

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
