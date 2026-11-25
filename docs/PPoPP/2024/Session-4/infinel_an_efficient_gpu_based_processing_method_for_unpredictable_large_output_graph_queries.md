---
title: "INFINEL: An efficient GPU-based processing method for unpredictable large output graph queries"
description: "PPoPP 2024 Session Graph Processing：单阶段 GPU 大输出图查询，三角形列举较两阶段最高快 31.5×"
tags:
  - "PPoPP2024"
  - "Session-4"
  - "Graph Processing"
  - "Graph query processing"
  - "GPU"
  - "Large output"
authors:
  - "Sungwoo Park"
  - "Seyeon Oh"
  - "Min-Soo Kim"
session: "Session 4: Graph Processing"
session_number: 4
session_chair: "Xipeng Shen"
date: "2024-03-04"
time: "16:10–16:30"
room: "Moorfoot"
doi: "10.1145/3627535.3638490"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# INFINEL: An efficient GPU-based processing method for unpredictable large output graph queries

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">INFINEL 以每线程分块分配与 kernel 停止/重启的单阶段方法，在 GPU 上处理输出规模不可预测的大输出图查询，三角形列举最高加速 31.5 倍。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 4: Graph Processing</p>
</div>

**作者**：Sungwoo Park (Korea Advanced Institute of Science and Technology); Seyeon Oh (GraphAI); Min-Soo Kim (Korea Advanced Institute of Science and Technology)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 16:10–16:30 · Session 4: Graph Processing（主席：Xipeng Shen）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638490) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

With the introduction of GPUs, which are specialized for iterative parallel computations, the execution of computation-intensive graph queries using a GPU has seen significant performance improvements. However, due to the memory constraints of GPUs, there has been limited research on handling large-scale output graph queries with unpredictable output sizes on a GPU. Traditionally, two-phase methods have been used, where the query is re-executed after splitting it into sub-tasks while only considering the size of the output in a static manner. However, two-phase methods become highly inefficient when used with graph data with extreme skew, failing to maximize the GPU performance. This paper proposes INFINEL, which handles unpredictable large output graph queries in a one-phase method through chunk allocation per thread and kernel stop/restart methods. We also propose applicable optimization techniques due to the corresponding unique characteristics of operating with low time/space overhead and not heavily relying on the GPU output buffer size. Through extensive experiments, we demonstrate that our one-phase method of INFINEL improves the performance by up to 31.5 times over the conventional two-phase methods for triangle listing ULO query.

## 中文摘要

随着专为迭代并行计算设计的 GPU 的引入，使用 GPU 执行计算密集型图查询已获得显著性能提升。然而，受 GPU 内存约束，针对输出规模不可预测的大规模输出图查询在 GPU 上的处理研究仍然有限。传统上采用两阶段方法，即在将查询拆分为子任务后重新执行查询，且仅以静态方式考虑输出大小。然而，当用于具有极端倾斜的图数据时，两阶段方法变得非常低效，无法最大化 GPU 性能。本文提出 INFINEL，它通过每线程分块分配以及 kernel 停止/重启方法，以单阶段方式处理输出不可预测的大输出图查询。我们还针对其独特特性提出了适用的优化技术，这些技术具有较低的时间/空间开销，且不过度依赖 GPU 输出缓冲区大小。通过大量实验，我们证明 INFINEL 的单阶段方法在三角形列举 ULO 查询上相比传统两阶段方法将性能提升最高达 31.5 倍。

## 英文关键词

Graph query processing, Large output, Parallel computing, GPU

## 中文关键词

图查询处理；大输出；并行计算；GPU

---

## 一句话总结

> INFINEL 以每线程分块分配与 kernel 停止/重启的单阶段方法，在 GPU 上处理输出规模不可预测的大输出图查询，三角形列举最高加速 31.5 倍。

## 研究问题

GPU 内存受限，输出规模不可预测的大输出图查询难以在其上处理；传统两阶段方法只静态考虑输出大小、需拆分重执行，在极端倾斜图上效率极低，无法发挥 GPU 性能。

## 方法简述

- 提出每线程分块分配（chunk allocation per thread）机制，使输出缓冲区随查询执行动态增长，无需预先静态估算输出规模。
- 设计 kernel 停止/重启（kernel stop/restart）方法，在输出溢出时暂停并重启内核，从而以单阶段方式完成不可预测的大输出查询。
- 针对单阶段执行的独特特性提出配套优化技术，兼具低时间/空间开销，且不过度依赖 GPU 输出缓冲区大小。

## 主要结果

- 在三角形列举（triangle listing）ULO 查询上，相比传统两阶段方法性能最高提升 31.5 倍。
- 以单阶段方式处理输出不可预测的查询，在极端倾斜图数据上避免了拆分重执行带来的开销。

---

> 所属 Session：[Session 4: Graph Processing](index.md) · 返回 [PPoPP 2024 总览](../index.md)
