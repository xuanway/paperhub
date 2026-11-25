---
title: "AGAThA: Fast and Efficient GPU Acceleration of Guided Sequence Alignment for Long Read Mapping"
description: "PPoPP 2024 Session Applications：AGAThA 较 CPU 基线快 18.8×、最佳 GPU 基线快 9.6×"
tags:
  - "PPoPP2024"
  - "Session-10"
  - "Applications"
  - "GPU Acceleration"
  - "Dynamic Programming"
  - "Long Reads"
authors:
  - "Seongyeon Park"
  - "Junguk Hong"
  - "Jaeyong Song"
  - "Hajin Kim"
  - "Youngsok Kim"
  - "Jinho Lee"
session: "Session 10: Applications"
session_number: 10
session_chair: "Milind Chabbi"
date: "2024-03-06"
time: "11:50–12:10"
room: "Moorfoot"
doi: "10.1145/3627535.3638474"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# AGAThA: Fast and Efficient GPU Acceleration of Guided Sequence Alignment for Long Read Mapping

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 AGAThA，在不改变算法结构的前提下为引导式动态规划序列比对提供精确 GPU 加速，针对跨步/冗余访存与负载不均逐一优化，较 CPU 基线加速 18.8×。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 10: Applications</p>
</div>

**作者**：Seongyeon Park, Junguk Hong, Jaeyong Song (Seoul National University); Hajin Kim, Youngsok Kim (Yonsei University); Jinho Lee (Seoul National University)

**会议**：PPoPP 2024 · 2024 年 3 月 6 日 11:50–12:10 · Session 10: Applications（主席：Milind Chabbi）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638474) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

With the advance in genome sequencing technology, the lengths of deoxyribonucleic acid (DNA) sequencing results are rapidly increasing at lower prices than ever. However, the longer lengths come at the cost of a heavy computational burden on aligning them. For example, aligning sequences to a human reference genome can take tens or even hundreds of hours. The current de facto standard approach for alignment is based on the guided dynamic programming method. Although this takes a long time and could potentially benefit from high-throughput graphic processing units (GPUs), the existing GPU-accelerated approaches often compromise the algorithm’s structure, due to the GPU-unfriendly nature of the computational pattern. Unfortunately, such compromise in the algorithm is not tolerable in the field, because sequence alignment is a part of complicated bioinformatics analysis pipelines. In such circumstances, we propose AGAThA, an exact and efficient GPU-based acceleration of guided sequence alignment. We diagnose and address the problems of the algorithm being unfriendly to GPUs, which comprises strided/redundant memory accesses and workload imbalances that are difficult to predict. According to the experiments on modern GPUs, AGAThA achieves 18.8× speedup against the CPU-based baseline, 9.6× against the best GPU-based baseline, and 3.6× against GPU-based algorithms with different heuristics.

## 中文摘要

随着基因组测序技术的进步，脱氧核糖核酸（DNA）测序结果的长度正以前所未有的低价快速增长。然而，更长的长度以沉重的比对计算负担为代价。例如，将序列比对到人类参考基因组可能需要数十甚至数百小时。当前事实上的标准比对方法基于引导式动态规划（guided dynamic programming）方法。尽管该方法耗时很长且有可能受益于高吞吐的图形处理器（GPU），但由于其计算模式对 GPU 不友好，现有的 GPU 加速方法常常损害算法的结构。遗憾的是，这种算法上的妥协在该领域是不可容忍的，因为序列比对是复杂生物信息学分析流水线的一部分。在此情形下，我们提出 AGAThA，一种精确且高效的基于 GPU 的引导序列比对加速方法。我们诊断并解决了该算法对 GPU 不友好的问题，包括跨步/冗余的内存访问以及难以预测的负载不均衡。在现代 GPU 上的实验表明，AGAThA 相对 CPU 基线取得 18.8× 加速，相对最佳 GPU 基线取得 9.6× 加速，相对采用不同启发式的 GPU 算法取得 3.6× 加速。

## 英文关键词

GPU Acceleration, Genome Sequence Alignment, Long Reads, Dynamic Programming

## 中文关键词

GPU 加速；基因组序列比对；长读长；动态规划

---

## 一句话总结

> 提出 AGAThA，在不改变算法结构的前提下为引导式动态规划序列比对提供精确 GPU 加速，针对跨步/冗余访存与负载不均逐一优化，较 CPU 基线加速 18.8×。

## 研究问题

测序读长快速增长带来沉重的比对计算负担，人类参考基因组比对可达数十甚至数百小时；现有 GPU 加速方法因计算模式对 GPU 不友好而常损害算法结构，这在生物信息学分析流水线中不可接受。

## 方法简述

- 提出 AGAThA，一种精确且高效的基于 GPU 的引导序列比对加速方法，保持原有算法结构不变
- 诊断并解决该算法对 GPU 不友好的问题，包括跨步与冗余的内存访问
- 设计针对性方案应对难以预测的负载不均衡

## 主要结果

- 相对 CPU 基线取得 18.8× 加速
- 相对最佳 GPU 基线取得 9.6× 加速
- 相对采用不同启发式的 GPU 算法取得 3.6× 加速

---

> 所属 Session：[Session 10: Applications](index.md) · 返回 [PPoPP 2024 总览](../index.md)
