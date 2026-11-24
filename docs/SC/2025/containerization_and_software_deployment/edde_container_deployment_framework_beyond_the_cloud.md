---
title: "EDDE: Container Deployment Framework Beyond the Cloud"
description: "SC 2025 · Containerization and Software Deployment · Hao Fan; Zhuo Huang; Shadi Ibrahim; Lin Gu; Song Wu"
tags:
  - "SC2025"
  - "Containerization and Software Deployment"
---

# EDDE: Container Deployment Framework Beyond the Cloud

**中文标题：** 超越云环境的容器部署框架

**所属 Session：** [Containerization and Software Deployment](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Containerization and Software Deployment。</p>
<p class="paper-seo-summary__tags">SC 2025 · Containerization and Software Deployment</p>
</div>

**作者**：Hao Fan; Zhuo Huang; Shadi Ibrahim; Lin Gu; Song Wu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap624&sess=sess171)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Existing cloud-oriented container deployment frameworks fail to address the unique challenges of edge environments, including geographic distribution, device heterogeneity, and resource constraints. This leads to suboptimal performance for latency-sensitive edge services like HPC/AI-powered autonomous driving, which demand rapid startup and immediate responsiveness. Current on-demand image solutions require excessive client-registry communication, resulting in prolonged round-trip time (RTT)—a particularly severe limitation in geographically distributed edge platforms. Furthermore, the user-space file system (FUSE), typically employed to handle device heterogeneity, introduces substantial overhead to the native I/O stack. Our findings reveal that on-demand image solutions exacerbate storage pressure on resource-constrained edge devices. To overcome these challenges, we introduce EDDE, an edge-optimized container deployment framework that redesigns the on-demand image pipeline. When com

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
