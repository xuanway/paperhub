---
title: "Zero-Value Code Specialization via Profile-Guided Control Data Flow Analysis"
description: "SC 2025 · Performance: Benchmarks and Optimization · Shaokang Du; Kelun Lei; Xin You; Hailong Yang; Yufan Xu; Zhongzhi Luan; Yi Liu; "
tags:
  - "SC2025"
  - "Performance: Benchmarks and Optimization"
---

# Zero-Value Code Specialization via Profile-Guided Control Data Flow Analysis

**中文标题：** 通过剖析引导的控制数据流分析实现零值代码特化

**所属 Session：** [Performance: Benchmarks and Optimization](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Performance: Benchmarks and Optimization。</p>
<p class="paper-seo-summary__tags">SC 2025 · Performance: Benchmarks and Optimization</p>
</div>

**作者**：Shaokang Du; Kelun Lei; Xin You; Hailong Yang; Yufan Xu; Zhongzhi Luan; Yi Liu; Depei Qian

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap535&sess=sess184)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

Zero-value propagation is a common phenomenon in modern programs, where redundant operations caused by zero values can severely impact performance. Since zero values are often generated dynamically at runtime, eliminating such redundancies through static analysis alone is challenging. In this paper, we propose an efficient static control data flow analysis algorithm to identify redundancies resulting from zero-value propagation. Based on this algorithm, we design and implement ZeroSpec, a fully automated profile-guided code optimizer that detects zero values at runtime and specializes fast paths for them. To maximize performance gains, ZeroSpec also employs a fine-grained cost model that evaluates the optimization potential of individual zero-value instructions to guide the construction of targeted optimization regions. Evaluation on SPEC CPU2017, NPB and real-world applications demonstrates the effectiveness of ZeroSpec, achieving a maximum performance speedup of 1.31x.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
