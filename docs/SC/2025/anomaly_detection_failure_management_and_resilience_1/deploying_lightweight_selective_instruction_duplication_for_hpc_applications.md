---
title: "Deploying Lightweight Selective Instruction Duplication for HPC Applications"
description: "SC 2025 · Anomaly Detection, Failure Management, and Resilience 1 · Md Hasanur Rahman; Guanpeng Li"
tags:
  - "SC2025"
  - "Anomaly Detection, Failure Management, and Resilience 1"
---

# Deploying Lightweight Selective Instruction Duplication for HPC Applications

**中文标题：** 为 HPC 应用部署轻量级选择性指令复制

**所属 Session：** [Anomaly Detection, Failure Management, and Resilience 1](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Anomaly Detection, Failure Management, and Resilience 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Anomaly Detection, Failure Management, and Resilience 1</p>
</div>

**作者**：Md Hasanur Rahman; Guanpeng Li

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap431&sess=sess289)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Modern high performance computing (HPC) applications are increasingly vulnerable to silent data corruptions (SDCs) caused by transient hardware faults. While selective instruction duplication (SID) offers an efficient software-level protection strategy, existing SID methods rely on SDC vulnerability profiles derived from only the default reference input often found in application suites. However, they overlook the input-dependent nature of SDC propagation. This leads to significant SDC coverage loss when inputs vary. We present PROTEGO, a novel input-aware SID protection framework that efficiently adapts protection to runtime inputs. PROTEGO performs a one-time vulnerability-guided input exploration to identify a small number of input groups with distinct SID protection patterns. At runtime, PROTEGO uses lightweight features derived from input arguments to select and deploy the appropriate SID protection. Our evaluation across 10 HPC applications demonstrates the effectiveness and effi

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
