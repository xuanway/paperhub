---
title: "Ratte: Fuzzing for Miscompilations in Multi-Level Compilers Using Composable Semantics"
description: "ASPLOS 2025 · Fuzz Testing"
tags:
  - "ASPLOS2025"
  - "Fuzz Testing"
---

# Ratte: Fuzzing for Miscompilations in Multi-Level Compilers Using Composable Semantics

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Fuzz Testing。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Fuzz Testing</p>
</div>

**论文链接**：[https://doi.org/10.1145/3676641.3716270](https://doi.org/10.1145/3676641.3716270)
**作者**：Pingshi Yu (Imperial College London), Nicolas Wu (Imperial College London), Alastair F. Donaldson (Imperial College London)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Fuzz Testing 场景，围绕 Fuzzing for Miscompilations in Multi-Level Compilers Using Composable Semantics 提出系统化优化方案，重点涉及 Ratte、Fuzzing、Miscompilations 等关键技术点。

## 方法简述

- 以 Ratte 为核心切入点，构建针对 Fuzz Testing 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 通过编译/调度策略改进代码生成与执行。

## 主要结果

- 提升端到端执行效率。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
