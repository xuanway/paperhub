---
title: "Workload Intelligence: Workload-Aware IaaS Abstraction for Cloud Efficiency"
description: "SC 2025 · System Software and Cloud · Lexiang Huang; Anjaly Parayil; Jue Zhang; Xiaoting Qin; Chetan Bansal; Jovan Sto"
tags:
  - "SC2025"
  - "System Software and Cloud"
---

# Workload Intelligence: Workload-Aware IaaS Abstraction for Cloud Efficiency

**中文标题：** 工作负载智能：面向云效率的工作负载感知 IaaS 抽象

**所属 Session：** [System Software and Cloud](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud</p>
</div>

**作者**：Lexiang Huang; Anjaly Parayil; Jue Zhang; Xiaoting Qin; Chetan Bansal; Jovan Stojkovic; Pantea Zardoshti; Pulkit Misra; Eli Cortez; Raphael Ghelman; Íñigo Goiri; Saravan Rajmohan; Jim Kleewein; Rodrigo Fonseca; Timothy Zhu; Ricardo Bianchini

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap585&sess=sess287)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Today, cloud workloads are largely opaque to the cloud platform. Typically, the only information the platform receives is the virtual machine (VM) type and possibly a decoration to the type (e.g., the VM is evictable). Similarly, workloads receive minimal information from the platform; generally, only telemetry from their VMs or occasional signals (e.g., just before a VM is evicted). The narrow interface between workloads and platforms has several drawbacks: (1) a surge in VM types and decorations in public cloud platforms complicates customer selection; (2) key workload characteristics (e.g., low availability requirements) are often unspecified, hindering platform customization for optimized resource usage and cost savings; and (3) workloads may be unaware of potential optimizations or lack sufficient time to react to platform events. To resolve these issues and improve cloud efficiency, we propose Workload Sage, a framework for enabling dynamic bi-directional communication between cl

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
