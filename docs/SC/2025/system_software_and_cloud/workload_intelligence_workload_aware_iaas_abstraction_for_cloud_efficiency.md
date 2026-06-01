---
title: "Workload Intelligence: Workload-Aware IaaS Abstraction for Cloud Efficiency"
description: "SC 2025 · System Software and Cloud · Lexiang Huang; Anjaly Parayil; Jue Zhang; Xiaoting Qin; Chetan Bansal; Jovan Sto"
tags:
  - "SC2025"
  - "System Software and Cloud"
---

# Workload Intelligence: Workload-Aware IaaS Abstraction for Cloud Efficiency

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud</p>
</div>

**作者**：Lexiang Huang; Anjaly Parayil; Jue Zhang; Xiaoting Qin; Chetan Bansal; Jovan Stojkovic; Pantea Zardoshti; Pulkit Misra; Eli Cortez; Raphael Ghelman; Íñigo Goiri; Saravan Rajmohan; Jim Kleewein; Rodrigo Fonseca; Timothy Zhu; Ricardo Bianchini

**会议**：SC 2025 · St. Louis, MO

## 摘要

Today, cloud workloads are largely opaque to the cloud platform. Typically, the only information the platform receives is the virtual machine (VM) type and possibly a decoration to the type (e.g., the VM is evictable). Similarly, workloads receive minimal information from the platform; generally, only telemetry from their VMs or occasional signals (e.g., just before a VM is evicted). The narrow interface between workloads and platforms has several drawbacks: (1) a surge in VM types and decorations in public cloud platforms complicates customer selection; (2) key workload characteristics (e.g., low availability requirements) are often unspecified, hindering platform customization for optimized resource usage and cost savings; and (3) workloads may be unaware of potential optimizations or lack sufficient time to react to platform events. To resolve these issues and improve cloud efficiency, we propose Workload Sage, a framework for enabling dynamic bi-directional communication between cl

---

## 一句话总结

> 该工作属于 System Software and Cloud 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 System Software and Cloud 领域贡献新的设计范式或评估框架。
