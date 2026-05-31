---
title: "Einsum Trees: An Abstraction for Optimizing the Execution of Tensor Expressions"
description: "ASPLOS 2025 · ML Compilers"
tags:
  - "ASPLOS2025"
  - "ML Compilers"
---

# Einsum Trees: An Abstraction for Optimizing the Execution of Tensor Expressions

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: ML Compilers。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · ML Compilers</p>
</div>

**论文链接**：[https://doi.org/10.1145/3676641.3716254](https://doi.org/10.1145/3676641.3716254)
**作者**：Alexander Breuer (Friedrich Schiller University Jena), Mark Blacher (Friedrich Schiller University Jena), Max Engel (Friedrich Schiller University Jena), Joachim Giesen (Friedrich Schiller University Jena), Alexander Heinecke (Intel Corporation), Julien Klaus (Friedrich Schiller University Jena), Stefan Remke (Friedrich Schiller University Jena)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 ML Compilers 场景，围绕 An Abstraction for Optimizing the Execution of Tensor Expressions 提出系统化优化方案，重点涉及 Einsum、Trees、Abstraction 等关键技术点。

## 方法简述

- 以 Einsum Trees 为核心切入点，构建针对 ML Compilers 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 通过模块化设计保持方案可迁移性与工程可落地性。

## 主要结果

- 在性能、能效或可扩展性指标上预期优于基线方案。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
