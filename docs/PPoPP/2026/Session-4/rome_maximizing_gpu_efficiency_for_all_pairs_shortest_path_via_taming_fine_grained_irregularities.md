---
title: "ROME: Maximizing GPU Efficiency for All-Pairs Shortest Path via Taming Fine-Grained Irregularities"
description: "PPoPP 2026 Session 4（GPU and Heterogeneous Computing）：空间重构+异步流水线驯服不规则，比 SOTA GPU 快 11.2–338×"
tags:
  - "PPoPP2026"
  - "Session-4"
  - "GPU and Heterogeneous Computing"
  - "All-Pairs Shortest Path"
  - "GPU"
  - "Asynchronous Pipeline"
authors:
  - "Weile Luo"
  - "Yuhan Chen"
  - "Xiangrui Yu"
  - "Qiang Wang"
  - "Ruibo Fan"
  - "Hongyuan Liu"
  - "Xiaowen Chu"
session: "Session 4: GPU and Heterogeneous Computing"
session_number: 4
session_chair: "Frank Mueller"
date: "2026-02-02"
time: "16:50–17:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786461"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# ROME: Maximizing GPU Efficiency for All-Pairs Shortest Path via Taming Fine-Grained Irregularities

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 ROME 系统，通过空间重构把不规则的 APSP 计算规整化并以异步流水线在时间上重叠，相比 SOTA GPU 方案加速 11.2–338.0×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 4: GPU and Heterogeneous Computing</p>
</div>

**作者**：Weile Luo, Yuhan Chen, Xiangrui Yu, Qiang Wang, Ruibo Fan, Hongyuan Liu, and Xiaowen Chu — Hong Kong University of Science and Technology (Guangzhou), China; Harbin Institute of Technology, Shenzhen, China; Stevens Institute of Technology, USA; Hong Kong University of Science and Technology, Hong Kong

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 16:50–17:10 · Session 4: GPU and Heterogeneous Computing（主席：Frank Mueller）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786461) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

All-Pairs Shortest Path (APSP), a fundamental problem in graph analytics, can be solved efficiently by reducing the computational workload through vertex reordering. However, it fails on GPUs due to fine-grained granularity, shape, and dependency irregularities, which cause severe hardware underutilization. We introduce ROME, a system that tames these irregularities by spatially restructuring computation into regularized workloads and temporally overlapping them with an asynchronous pipeline. ROME achieves 14.7-244.5× speedup over the state-of-the-art multicore CPU solution and 11.2-338.0× speedup over the state-of-the-art GPU solution. Notably, our results achieve mostly above 20% and up to 34.7% of peak min-plus OPs across all tested graphs.

## 中文摘要

全对最短路径（APSP）是图分析中的一个基础问题，可通过顶点重排序削减计算量来高效求解。然而在 GPU 上，由于细粒度、形状与依赖关系方面的不规则性导致硬件利用率严重不足，该做法难以奏效。我们提出 ROME，一个通过将计算在空间上重构为规则化工作负载，并在时间上以异步流水线使其相互重叠，从而驯服这些不规则性的系统。ROME 相较最先进的多核 CPU 方案取得 14.7–244.5 倍加速，相较最先进的 GPU 方案取得 11.2–338.0 倍加速。值得注意的是，在所有测试图上，我们的结果大多达到峰值 min-plus 运算量的 20% 以上，最高达 34.7%。

## 英文关键词

GPU Computing, All-Pairs Shortest Path, Irregular Workloads

## 中文关键词

GPU 计算；全对最短路径；不规则工作负载

---

## 一句话总结

> 提出 ROME 系统，通过空间重构把不规则的 APSP 计算规整化并以异步流水线在时间上重叠，相比 SOTA GPU 方案加速 11.2–338.0×。

## 研究问题

通过顶点重排削减 APSP 计算量在 GPU 上失效，细粒度、形状与依赖三类不规则性造成严重的硬件利用率不足。

## 方法简述

- 采用空间重构，把细粒度的不规整计算重组为规整化的工作负载。
- 设计异步流水线，在时间维度上重叠这些工作负载以提升硬件利用率。
- 实现 ROME 系统，针对粒度、形状与依赖三类不规则性进行驯服。

## 主要结果

- 相比最先进的多核 CPU 方案加速 14.7–244.5×。
- 相比最先进的 GPU 方案加速 11.2–338.0×。
- 在所有测试图上大多达到峰值 min-plus 算力的 20% 以上，最高达 34.7%。

---

> 所属 Session：[Session 4: GPU and Heterogeneous Computing](index.md) · 返回 [PPoPP 2026 总览](../index.md)
