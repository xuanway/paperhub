---
title: "Zero-Value Code Specialization via Profile-Guided Control Data Flow Analysis"
description: "SC 2025 · Performance: Benchmarks and Optimization · Shaokang Du; Kelun Lei; Xin You; Hailong Yang; Yufan Xu; Zhongzhi Luan; Yi Liu; "
tags:
  - "SC2025"
  - "Performance: Benchmarks and Optimization"
---

# Zero-Value Code Specialization via Profile-Guided Control Data Flow Analysis

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Benchmarks and Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Benchmarks and Optimization</p>
</div>

**作者**：Shaokang Du; Kelun Lei; Xin You; Hailong Yang; Yufan Xu; Zhongzhi Luan; Yi Liu; Depei Qian

**会议**：SC 2025 · St. Louis, MO

## 摘要

Zero-value propagation is a common phenomenon in modern programs, where redundant operations caused by zero values can severely impact performance. Since zero values are often generated dynamically at runtime, eliminating such redundancies through static analysis alone is challenging. In this paper, we propose an efficient static control data flow analysis algorithm to identify redundancies resulting from zero-value propagation. Based on this algorithm, we design and implement ZeroSpec, a fully automated profile-guided code optimizer that detects zero values at runtime and specializes fast paths for them. To maximize performance gains, ZeroSpec also employs a fine-grained cost model that evaluates the optimization potential of individual zero-value instructions to guide the construction of targeted optimization regions. Evaluation on SPEC CPU2017, NPB and real-world applications demonstrates the effectiveness of ZeroSpec, achieving a maximum performance speedup of 1.31x.

---

## 一句话总结

> 该工作属于 Performance: Benchmarks and Optimization 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Performance: Benchmarks and Optimization 领域贡献新的设计范式或评估框架。
