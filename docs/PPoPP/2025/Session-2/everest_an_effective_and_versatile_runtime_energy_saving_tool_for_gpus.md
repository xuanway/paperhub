---
title: "EVeREST: An Effective and Versatile Runtime Energy Saving Tool for GPUs"
description: "PPoPP 2025 Session 2（GPU I）：运行时自动发现 GPU 节能机会，兼顾性能保证与跨厂商可移植"
tags:
  - "PPoPP2025"
  - "Session-2"
  - "GPU I"
  - "Energy Efficiency"
  - "DVFS"
  - "GPU Runtime"
authors:
  - "Anna Yue"
  - "Pen-Chung Yew"
  - "Sanyam Mehta"
session: "Session 2: GPU I"
session_number: 2
session_chair: "Xipeng Shen"
date: "2025-03-03"
time: "11:40–12:00"
room: "Acacia D"
doi: "10.1145/3710848.3710875"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
award: "Distinguished Paper Award"
---

# EVeREST: An Effective and Versatile Runtime Energy Saving Tool for GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 Everest，一个在运行时自动发现 GPU 节能机会的工具，基于低开销性能刻画与 DVFS 在保证性能的前提下降低功耗。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 2: GPU I</p>
</div>

**作者**：Anna Yue, Pen-Chung Yew (University of Minnesota); Sanyam Mehta (Hewlett-Packard Labs)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 11:40–12:00 · Session 2: GPU I（主席：Xipeng Shen）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710875) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

> 🏆 **Distinguished Paper Award**

---

## 一句话总结

> 提出 Everest，一个在运行时自动发现 GPU 节能机会的工具，基于低开销性能刻画与 DVFS 在保证性能的前提下降低功耗。

## 研究问题

GPU 节能面临三重挑战：内存受限应用可节省的空间有限、低开销性能计数器稀缺、以及不同厂商处理器之间的可移植性；同时还要为动态应用阶段做出正确的性能—功耗权衡。

## 方法简述

- 除对内存受限阶段降低核心频率外，额外利用两条基于 DVFS 的 GPU 节能路径。
- 只依赖最少的性能事件完成应用阶段刻画，保持极低开销并支持不同 GPU。
- 以应用阶段为粒度进行调节，并利用内置性能估计提供性能保证。

## 主要结果

- 在最新 NVIDIA 与 AMD GPU 上均优于现有节能方案。
- 在不牺牲性能的前提下实现自动化的运行时节能。

<details>
<summary>原文摘要（英文）</summary>

Amid conflicting demands for ever-improving performance and maximizing energy savings, it is important to have a tool that automatically identifies opportunities to save power/energy at runtime without compromising performance. GPUs in particular present challenges due to (1) reduced savings available from memory bound applications, and (2) limited availability of low overhead performance counters. Thus, a successful tool must address these issues while still tackling the challenges of dynamic application characterization, versatility across processors from different vendors, and effectiveness at making the right power-performance tradeoffs for desired energy savings. We propose Everest, a tool that automatically finds energy saving opportunities across GPUs at runtime. Specifically, Everest finds two unique avenues for saving energy using DVFS in GPUs in addition to the traditional method of lowering core clock for memory bound phases. Everest has very low overhead and works across different GPUs given its reliance on the minimum possible performance events for the needed characterization. Everest works at a finer granularity of individual application phases and utilizes built-in performance estimation to provide desired performance guarantees for an effective solution that outperforms existing solutions on the latest NVIDIA and AMD GPUs.

</details>

---

> 所属 Session：[Session 2: GPU I](index.md) · 返回 [PPoPP 2025 总览](../index.md)
