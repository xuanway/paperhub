---
title: "Characterizing Matrix Multiplication Units across General Parallel Patterns in Scientific Computing"
description: "PPoPP 2026 Session 13（Matrix and Linear Algebra Algorithms）：10 个 MMU 核 + 四象限分类，给出 9 条关键观察"
tags:
  - "PPoPP2026"
  - "Session-13"
  - "Matrix and Linear Algebra Algorithms"
  - "Tensor Cores"
  - "Benchmarking"
  - "Scientific Computing"
authors:
  - "Yuechen Lu"
  - "Hongwei Zeng"
  - "Marc Casas"
  - "Weifeng Liu"
session: "Session 13: Matrix and Linear Algebra Algorithms"
session_number: 13
session_chair: "William S. Moses"
date: "2026-02-04"
time: "10:50–11:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786456"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Characterizing Matrix Multiplication Units across General Parallel Patterns in Scientific Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 Cubie 基准套件，用 10 个 MMU 优化核从性能、功耗、精度与访存四维刻画科学计算模式，将 MMU 利用归纳为四象限并给出九条关键观察。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 13: Matrix and Linear Algebra Algorithms</p>
</div>

**作者**：Yuechen Lu, Hongwei Zeng, Marc Casas, and Weifeng Liu — China University of Petroleum-Beijing, China; Barcelona Supercomputing Center, Spain; Universitat Politècnica de Catalunya, Spain

**会议**：PPoPP 2026 · 2026 年 2 月 4 日 10:50–11:10 · Session 13: Matrix and Linear Algebra Algorithms（主席：William S. Moses）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786456) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Matrix multiplication units (MMUs) in modern parallel processors enable efficient execution of tiled matrix multiplications at varying precisions. While their effectiveness in AI workloads has been well demonstrated, their utility in scientific computing lacks systematic analysis. In this work, we characterize MMUs across a broad range of scientific computing patterns by evaluating performance, power consumption, numerical precision, and memory access behavior. To support this analysis, we develop Cubie, a comprehensive benchmark suite comprising ten MMU-optimized kernels of key parallel patterns. We also categorize MMU utilization patterns into four quadrants and identify the MMU limitations that arise in scientific computing. Through detailed comparisons with vector units, we provide nine key observations on the behavior and implications of MMUs in general scientific workloads, offering valuable insights for architecture, algorithm, and application researchers.

## 中文摘要

现代并行处理器中的矩阵乘法单元（MMU）能够在不同精度下高效执行分块矩阵乘法。尽管其在 AI 工作负载中的有效性已得到充分证明，但其在科学计算中的效用仍缺乏系统分析。在本工作中，我们通过评估性能、功耗、数值精度与访存行为，刻画了 MMU 在广泛的科学计算模式下的表现。为支撑该分析，我们开发了 Cubie，一个包含十种关键并行模式的 MMU 优化核函数 的综合基准测试套件。我们还将 MMU 的利用模式归纳为四个象限，并识别出科学计算中出现的 MMU 局限性。通过与向量单元的详细对比，我们给出关于 MMU 在一般科学工作负载中的行为与影响的九点关键观察，为体系结构、算法与应用研究人员提供了有价值的洞见。

## 英文关键词

Matrix multiplication unit, Parallel pattern, Benchmark suite

## 中文关键词

矩阵乘法单元；并行模式；基准测试套件

---

## 一句话总结

> 提出 Cubie 基准套件，用 10 个 MMU 优化核从性能、功耗、精度与访存四维刻画科学计算模式，将 MMU 利用归纳为四象限并给出九条关键观察。

## 研究问题

现代并行处理器中的矩阵乘法单元（MMU）在 AI 负载上已被证明高效，但其在科学计算中的效用仍缺乏系统分析。

## 方法简述

- 从性能、功耗、数值精度与访存行为四个维度刻画 MMU 在广泛科学计算模式下的表现。
- 开发 Cubie 基准套件，包含 10 个面向关键并行模式的 MMU 优化核。
- 将 MMU 的利用模式归纳为四个象限，并与向量单元细致对比以识别科学计算中暴露的 MMU 局限。

## 主要结果

- 给出科学计算中 MMU 利用模式的四象限分类，并识别出相应的 MMU 局限。
- 通过详细对比形成九条关于 MMU 在通用科学负载中行为与影响的关键观察，为体系结构、算法与应用研究者提供参考。

---

> 所属 Session：[Session 13: Matrix and Linear Algebra Algorithms](index.md) · 返回 [PPoPP 2026 总览](../index.md)
