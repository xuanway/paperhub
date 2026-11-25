---
title: "SBMGT: Scaling Bayesian Multinomial Group Testing"
description: "PPoPP 2025 Session 11（Parallel Algorithms and Applications）：并行乘积格 + BBPA，检测次数降 54%、误分类率降 92%"
tags:
  - "PPoPP2025"
  - "Session-11"
  - "Parallel Algorithms and Applications"
  - "Group Testing"
  - "Bayesian Inference"
  - "Parallel Framework"
authors:
  - "Weicong Chen"
  - "Hao Qi"
  - "Curtis Tatsuoka"
  - "Xiaoyi Lu"
session: "Session 11: Parallel Algorithms and Applications"
session_number: 11
session_chair: "Weicong Chen"
date: "2025-03-05"
time: "12:20–12:40"
room: "Acacia D"
doi: "10.1145/3710848.3710861"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# SBMGT: Scaling Bayesian Multinomial Group Testing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出贝叶斯多项式分组检测模型 BMGT 及可扩展框架 SBMGT，用并行二元编码乘积格、BBPA 池化策略与并行分析框架解决多样本多属性的分组检测问题。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 11: Parallel Algorithms and Applications</p>
</div>

**作者**：Weicong Chen, Hao Qi (University of California, Merced); Curtis Tatsuoka (University of Pittsburgh); Xiaoyi Lu (UC Merced)

**会议**：PPoPP 2025 · 2025 年 3 月 5 日 12:20–12:40 · Session 11: Parallel Algorithms and Applications（主席：Weicong Chen）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710861) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出贝叶斯多项式分组检测模型 BMGT 及可扩展框架 SBMGT，用并行二元编码乘积格、BBPA 池化策略与并行分析框架解决多样本多属性的分组检测问题。

## 研究问题

BGT 等现有分组检测技术难以处理多项式分组检测——样本同时具有多个可分别区分的二元属性，且计算规模难以扩展。

## 方法简述

- 提出新的贝叶斯模型及配套定理，支撑高效而精确的多项式池化策略。
- 设计并行二元编码乘积格模型，效率最高达 99.8%。
- 提出面向并行计算优化的 Bayesian Balanced Partitioning Algorithm（BBPA），并构建可扩展的多项式分组检测分析框架。

## 主要结果

- BBPA 在 4096 核上扩展效率最高达 97.7%。
- 在乌干达 AIDS 与 STD 数据集的真实疾病监测案例中，相比 BGT 检测次数最多减少 54%，误分类率降低 92%。

<details>
<summary>原文摘要（英文）</summary>

Group testing is a widely used binary classification method that efficiently distinguishes between samples with and without a binary-classifiable attribute by pooling and testing subsets of a group. Bayesian Group Testing (BGT) is the state- of-the-art approach, which integrates prior risk information into a Bayesian Boolean Lattice framework to minimize test counts and reduce false classifications. However, BGT, like other existing group testing techniques, struggles with multinomial group testing, where samples have multiple binary-classifiable attributes that can be individually distinguished simultaneously. We address this need by proposing Bayesian Multinomial Group Testing (BMGT), which includes a new Bayesian-based model and supporting theorems for an efficient and precise multinomial pooling strategy. We further design and develop SBMGT, a high-performance and scalable framework to tackle BMGT’s computational challenges by proposing three key innovations: 1) a parallel binary-encoded product lattice model with up to 99.8% efficiency; 2) the Bayesian Balanced Partitioning Algorithm (BBPA), a multinomial pooling strategy optimized for parallel computation with up to 97.7% scaling efficiency on 4096 cores; and 3) a scalable multinomial group testing analytics framework, demonstrated in a real-world disease surveillance case study using AIDS and STDs datasets from Uganda, where SBMGT reduced tests by up to 54% and lowered false classification rates by 92% compared to BGT.

</details>

---

> 所属 Session：[Session 11: Parallel Algorithms and Applications](index.md) · 返回 [PPoPP 2025 总览](../index.md)
