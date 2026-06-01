---
title: "Deploying Lightweight Selective Instruction Duplication for HPC Applications"
description: "SC 2025 · Anomaly Detection, Failure Management, and Resilience 1 · Md Hasanur Rahman; Guanpeng Li"
tags:
  - "SC2025"
  - "Anomaly Detection, Failure Management, and Resilience 1"
---

# Deploying Lightweight Selective Instruction Duplication for HPC Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Anomaly Detection, Failure Management, and Resilience 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Anomaly Detection, Failure Management, and Resilience 1</p>
</div>

**作者**：Md Hasanur Rahman; Guanpeng Li

**会议**：SC 2025 · St. Louis, MO

## 摘要

Modern high performance computing (HPC) applications are increasingly vulnerable to silent data corruptions (SDCs) caused by transient hardware faults. While selective instruction duplication (SID) offers an efficient software-level protection strategy, existing SID methods rely on SDC vulnerability profiles derived from only the default reference input often found in application suites. However, they overlook the input-dependent nature of SDC propagation. This leads to significant SDC coverage loss when inputs vary. We present PROTEGO, a novel input-aware SID protection framework that efficiently adapts protection to runtime inputs. PROTEGO performs a one-time vulnerability-guided input exploration to identify a small number of input groups with distinct SID protection patterns. At runtime, PROTEGO uses lightweight features derived from input arguments to select and deploy the appropriate SID protection. Our evaluation across 10 HPC applications demonstrates the effectiveness and effi

---

## 一句话总结

> 该工作属于 Anomaly Detection, Failure Management, and Resilience 1 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Anomaly Detection, Failure Management, and Resilience 1 领域贡献新的设计范式或评估框架。
