---
title: "Extended User Interrupts (xUI): Fast and Flexible Notification without Polling"
description: "ASPLOS 2025 · Potpourri"
tags:
  - "ASPLOS2025"
  - "Potpourri"
---

# Extended User Interrupts (xUI): Fast and Flexible Notification without Polling

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Potpourri。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Potpourri</p>
</div>

**论文链接**：[https://doi.org/10.1145/3676641.3716028](https://doi.org/10.1145/3676641.3716028)
**作者**：Berk Aydogmus (Purdue University), Linsong Guo (UC San Diego), Danial Zuberi (UC San Diego), Tal Garfinkel (UC San Diego), Dean Tullsen (UC San Diego), Amy Ousterhout (UC San Diego), Kazem Taram (Purdue University)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Potpourri 场景，围绕 Fast and Flexible Notification without Polling 提出系统化优化方案，重点涉及 Extended、User、Interrupts 等关键技术点。

## 方法简述

- 以 Extended User Interrupts (xUI) 为核心切入点，构建针对 Potpourri 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 通过模块化设计保持方案可迁移性与工程可落地性。

## 主要结果

- 目标是降低时延并提升吞吐/可扩展性。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
