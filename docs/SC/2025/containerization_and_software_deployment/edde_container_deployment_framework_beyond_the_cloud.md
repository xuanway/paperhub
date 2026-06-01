---
title: "EDDE: Container Deployment Framework Beyond the Cloud"
description: "SC 2025 · Containerization and Software Deployment · Hao Fan; Zhuo Huang; Shadi Ibrahim; Lin Gu; Song Wu"
tags:
  - "SC2025"
  - "Containerization and Software Deployment"
---

# EDDE: Container Deployment Framework Beyond the Cloud

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Containerization and Software Deployment。</p>
<p class="paper-seo-summary__tags">SC 2025 · Containerization and Software Deployment</p>
</div>

**作者**：Hao Fan; Zhuo Huang; Shadi Ibrahim; Lin Gu; Song Wu

**会议**：SC 2025 · St. Louis, MO

## 摘要

Existing cloud-oriented container deployment frameworks fail to address the unique challenges of edge environments, including geographic distribution, device heterogeneity, and resource constraints. This leads to suboptimal performance for latency-sensitive edge services like HPC/AI-powered autonomous driving, which demand rapid startup and immediate responsiveness. Current on-demand image solutions require excessive client-registry communication, resulting in prolonged round-trip time (RTT)—a particularly severe limitation in geographically distributed edge platforms. Furthermore, the user-space file system (FUSE), typically employed to handle device heterogeneity, introduces substantial overhead to the native I/O stack. Our findings reveal that on-demand image solutions exacerbate storage pressure on resource-constrained edge devices. To overcome these challenges, we introduce EDDE, an edge-optimized container deployment framework that redesigns the on-demand image pipeline. When com

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
