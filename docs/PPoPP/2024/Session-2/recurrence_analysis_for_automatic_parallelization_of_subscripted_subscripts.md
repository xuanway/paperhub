---
title: "Recurrence Analysis for Automatic Parallelization of Subscripted Subscripts"
description: "PPoPP 2024 Session Compilers and Runtimes for Parallel Systems：递归分析判定 a[b[i]] 不规则/多维单调性，10/12 基准提速"
tags:
  - "PPoPP2024"
  - "Session-2"
  - "Compilers and Runtimes for Parallel Systems"
  - "subscripted subscript"
  - "monotonicity"
  - "recurrence"
authors:
  - "Akshay Bhosale"
  - "Rudolf Eigenmann"
session: "Session 2: Compilers and Runtimes for Parallel Systems"
session_number: 2
session_chair: "Mohamed Riyadh Baghdadi"
date: "2024-03-04"
time: "12:30–12:50"
room: "Moorfoot"
doi: "10.1145/3627535.3638493"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Recurrence Analysis for Automatic Parallelization of Subscripted Subscripts

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出编译期递归关系分析算法，判定一维下标数组的不规则或间歇单调性与多维下标数组的单调性，使自动并行器在 12 个基准中的 10 个（83.33%）上获得性能提升。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 2: Compilers and Runtimes for Parallel Systems</p>
</div>

**作者**：Akshay Bhosale, Rudolf Eigenmann (University of Delaware, USA)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 12:30–12:50 · Session 2: Compilers and Runtimes for Parallel Systems（主席：Mohamed Riyadh Baghdadi）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638493) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Introducing correct and optimal OpenMP parallelization directives in applications is a challenge. To parallelize a loop in an input application code automatically, parallelizing compilers need to disprove dependences with respect to variables across iterations of the loop. Performing such dependence analysis in the presence of index arrays or subscripted subscripts – a[b[i]] – has long been a challenge for automatic parallelizers. Loops with subscripted subscripts can be parallelized if the subscript array is known to possess a property such as monotonicity. This paper presents a compile-time algorithm that can analyze complex recurrence relations and determine irregular or intermittent monotonicity of one-dimensional and monotonicity of multi-dimensional subscript arrays. The new algorithm builds on a prior approach that is capable of analyzing simple recurrence relations and determining monotonic one-dimensional subscript arrays. Experimental results show that automatic parallelizers equipped with our new analysis techniques can substantially improve the performance of ten out of twelve or 83.33% of the benchmarks evaluated, 25-33.33% more than possible with state-of-the-art compile-time automatic parallelization techniques.

## 中文摘要

在应用中引入正确且最优的 OpenMP 并行化指令是一项挑战。要自动并行化输入应用代码中的循环，并行化编译器需要排除循环迭代之间关于变量的依赖。在存在索引数组或下标下标（subscripted subscripts）——a[b[i]]——的情况下进行这样的依赖分析，长期以来一直是自动并行化器的难题。如果已知下标数组具有诸如单调性这样的性质，那么含下标下标的循环就可以被并行化。本文提出一种编译期算法，能够分析复杂的递归关系，并判定一维下标数组的不规则或间歇单调性以及多维下标数组的单调性。该新算法建立在一种先前方法之上，后者能够分析简单的递归关系并判定单调的一维下标数组。实验结果表明，装备了我们新分析技术的自动并行器显著提升了所评估 12 个基准中 10 个（即 83.33%）的性能，比最先进的编译期自动并行化技术所能做到的还多 25%–33.33%。

## 英文关键词

Subscripted Subscript, Monotonicity, Recurrence

## 中文关键词

下标下标；单调性；递归

---

## 一句话总结

> 提出编译期递归关系分析算法，判定一维下标数组的不规则或间歇单调性与多维下标数组的单调性，使自动并行器在 12 个基准中的 10 个（83.33%）上获得性能提升。

## 研究问题

在存在索引数组或下标下标 a[b[i]] 时进行依赖分析，长期是自动并行化的难题；已有编译期方法只能分析简单递归关系、判定一维单调下标数组，覆盖面不足。

## 方法简述

- 提出编译期算法，用于分析复杂的递归关系
- 在该算法中判定一维下标数组的不规则或间歇（irregular/intermittent）单调性
- 进一步判定多维下标数组的单调性，把分析对象从一维扩展到多维
- 建立在仅能处理简单递归关系、判定一维单调下标数组的先前方法之上

## 主要结果

- 在评估的 12 个基准中，装备该分析的自动并行器显著提升了 10 个（83.33%）的性能
- 相比最先进的编译期自动并行化技术，可并行化的基准多出 25%–33.33%
- 证明递归分析可显著拓宽含下标下标循环的自动并行化适用范围

---

> 所属 Session：[Session 2: Compilers and Runtimes for Parallel Systems](index.md) · 返回 [PPoPP 2024 总览](../index.md)
