---
title: "Jigsaw: Toward Conflict-free Vectorized Stencil Computation by Tessellating Swizzled Registers"
description: "PPoPP 2025 Session 11（Parallel Algorithms and Applications）：swizzle 图块化消除全维度对齐冲突，平均加速 2.31×"
tags:
  - "PPoPP2025"
  - "Session-11"
  - "Parallel Algorithms and Applications"
  - "Stencil Computation"
  - "Vectorization"
  - "Data Alignment"
authors:
  - "Yiwei Zhang"
  - "Kun Li"
  - "Liang Yuan"
  - "Haozhi Han"
  - "Yunquan Zhang"
  - "Ting Cao"
  - "Mao Yang"
session: "Session 11: Parallel Algorithms and Applications"
session_number: 11
session_chair: "Weicong Chen"
date: "2025-03-05"
time: "11:40–12:00"
room: "Acacia D"
doi: "10.1145/3710848.3710886"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Jigsaw: Toward Conflict-free Vectorized Stencil Computation by Tessellating Swizzled Registers

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出无冲突向量化方法 Jigsaw，通过对最细粒度 lane 做 swizzle 图块化（tessellating swizzled registers），在空间与时间各维度上同时消除数据对齐冲突（DAC）。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 11: Parallel Algorithms and Applications</p>
</div>

**作者**：Yiwei Zhang (UCAS; Microsoft Research); Kun Li (Microsoft Research); Liang Yuan (CAS); Haozhi Han (Microsoft Research; Peking University); Yunquan Zhang (CAS); Ting Cao, Mao Yang (Microsoft Research)

**会议**：PPoPP 2025 · 2025 年 3 月 5 日 11:40–12:00 · Session 11: Parallel Algorithms and Applications（主席：Weicong Chen）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710886) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出无冲突向量化方法 Jigsaw，通过对最细粒度 lane 做 swizzle 图块化（tessellating swizzled registers），在空间与时间各维度上同时消除数据对齐冲突（DAC）。

## 研究问题

Stencil 计算广泛采用向量化提升核内并行，但数据对齐冲突（DAC）造成的性能瓶颈此前尚未在所有维度上得到有效解决。

## 方法简述

- Lane-based Butterfly Vectorization：在最细粒度 lane 层面重排向量元素。
- SVD-based Dimension Flattening：用奇异值分解做维度展平，化解跨维度的对齐冲突。
- Iteration-based Temporal Merging：沿迭代维度做时间合并。

## 主要结果

- 在不同机器、多种 stencil kernel 上平均加速 2.31×。
- 性能显著优于当前最先进的 stencil 向量化技术。

<details>
<summary>原文摘要（英文）</summary>

Stencil computation plays a pivotal role in numerous scientific and engineering applications. Previous studies have extensively investigated vectorization techniques to enhance in-core parallelism; however, the performance bottleneck caused by data alignment conflicts (DAC) has not been effectively resolved in all dimensions. This paper proposes Jigsaw, a conflict-free vectorization method to reduce DAC across all dimensions by tessellating swizzled finest-grained lanes. Jigsaw comprises three key components: Lane-based Butterfly Vectorization, SVD-based Dimension Flattening, and Iteration-based Temporal Merging. These components effectively address DAC across spatial and temporal dimensions. Experimental results on different machines demonstrate that Jigsaw could achieve a significant improvement compared to the state-of-the-art techniques, with an average speedup of 2.31x on various stencil kernels.

</details>

---

> 所属 Session：[Session 11: Parallel Algorithms and Applications](index.md) · 返回 [PPoPP 2025 总览](../index.md)
