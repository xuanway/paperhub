---
title: "RT–BarnesHut: Accelerating Barnes–Hut Using Ray-Tracing Hardware"
description: "PPoPP 2025 Session 2（GPU I）：把 Barnes–Hut 树遍历重构为光线追踪，利用 RT core 加速 n-body"
tags:
  - "PPoPP2025"
  - "Session-2"
  - "GPU I"
  - "Ray Tracing"
  - "n-body Simulation"
  - "Barnes–Hut"
authors:
  - "Vani Nagarajan"
  - "Rohan Gangaraju"
  - "Kirshanthan Sundararajah"
  - "Artem Pelenitsyn"
  - "Milind Kulkarni"
session: "Session 2: GPU I"
session_number: 2
session_chair: "Xipeng Shen"
date: "2025-03-03"
time: "11:20–11:40"
room: "Acacia D"
doi: "10.1145/3710848.3710885"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# RT–BarnesHut: Accelerating Barnes–Hut Using Ray-Tracing Hardware

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">把 Barnes–Hut n-body 算法重构为光线追踪问题并基于 NVIDIA OptiX 实现，用 GPU 光线追踪单元加速原本不适合 shader core 的树遍历。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 2: GPU I</p>
</div>

**作者**：Vani Nagarajan (Purdue University); Rohan Gangaraju (University of Texas at Austin); Kirshanthan Sundararajah (Virginia Tech); Artem Pelenitsyn, Milind Kulkarni (Purdue University)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 11:20–11:40 · Session 2: GPU I（主席：Xipeng Shen）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710885) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 把 Barnes–Hut n-body 算法重构为光线追踪问题并基于 NVIDIA OptiX 实现，用 GPU 光线追踪单元加速原本不适合 shader core 的树遍历。

## 研究问题

Barnes–Hut 通过树结构把 n-body 模拟降到 O(n·lg n)，但其树遍历模式难以用传统 GPU shader core 高效加速；n-body 模拟本身计算代价极高。

## 方法简述

- 将 Barnes–Hut 的树遍历与受力近似计算映射为光线追踪查询。
- 基于 NVIDIA OptiX 实现 RT-BarnesHut，利用 RT core 处理不规则树遍历。

## 主要结果

- 在评估中优于当前最先进的 GPU Barnes–Hut 实现。
- 验证了光线追踪硬件在树型计算上的优势可迁移到 n-body 模拟。

<details>
<summary>原文摘要（英文）</summary>

The 𝑛-body problem involves calculating the effect of bodies on each other. 𝑛-body simulations are ubiquitous in the fields of physics and astronomy and notoriously computationally expensive. The naïve algorithm for 𝑛-body simulations has the prohibiting 𝑂(𝑛2) time complexity. Reducing the time complexity to 𝑂(𝑛· lg(𝑛)), the tree-based Barnes–Hut algorithm approximates the effect of bodies beyond a certain threshold distance. Other than algorithmic improvements, extensive research has gone into accelerating 𝑛-body simulations on GPUs and multi-core systems. However, Barnes–Hut is a tree-traversal algorithm, which makes it a poor target for acceleration using traditional GPU shader cores. In contrast, recent work shows that, for tree-based computations, GPU ray-tracing (RT) cores dominate shader cores. In this work, we reformulate the Barnes–Hut algorithm as a ray-tracing problem and implement it with NVIDIA OptiX. Our evaluation shows that the resulting system, RT-BarnesHut, outperforms current state-of-the-art GPU-based implementations. We thank the anonymous PPoPP reviewers and our shepherd for their valuable feedback. We thank Dr. Tom Quinn for answering our questions about ChaNGa. This work was funded by NSF grants CCF-1908504, CCF1919197 and CCF-2216978. This work is licensed under.

</details>

---

> 所属 Session：[Session 2: GPU I](index.md) · 返回 [PPoPP 2025 总览](../index.md)
