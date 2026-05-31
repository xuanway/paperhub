---
title: "TaintEMU: Decoupling Tracking from Functional Domains for Architecture-Agnostic and Efficient Whole-System Taint Tracking"
description: "ASPLOS 2025 · Security"
tags:
  - "ASPLOS2025"
  - "Security"
---

# TaintEMU: Decoupling Tracking from Functional Domains for Architecture-Agnostic and Efficient Whole-System Taint Tracking

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Security。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Security</p>
</div>

**论文链接**：[https://doi.org/10.1145/3676641.3716023](https://doi.org/10.1145/3676641.3716023)
**作者**：Lei Cui (Guangxi Normal University), Youquan Xian (Guangxi Normal University), Peng Liu (Guangxi Normal University), Longjin Lu (Independent Researcher)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Security 场景，围绕 TaintEMU、Decoupling 相关关键问题 提出系统化优化方案，重点涉及 TaintEMU、Decoupling、Tracking 等关键技术点。

## 方法简述

- 以 TaintEMU 为核心切入点，构建针对 Security 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 通过模块化设计保持方案可迁移性与工程可落地性。

## 主要结果

- 目标是降低时延并提升吞吐/可扩展性。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
