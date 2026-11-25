---
title: "DiggerBees: Depth First Search Leveraging Hierarchical Block-Level Stealing on GPUs"
description: "PPoPP 2026 Session 2（Scheduling and Load Balancing）：两级栈 + 块内/块间窃取，较 GPU DFS 平均最高 30.18×"
tags:
  - "PPoPP2026"
  - "Session-2"
  - "Scheduling and Load Balancing"
  - "DFS"
  - "GPU"
  - "Work Stealing"
authors:
  - "Yuyao Niu"
  - "Yuechen Lu"
  - "Weifeng Liu"
  - "Marc Casas"
session: "Session 2: Scheduling and Load Balancing"
session_number: 2
session_chair: "V Krishna Nandivada"
date: "2026-02-02"
time: "12:10–12:30"
room: "Pyrmont"
doi: "10.1145/3774934.3786457"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# DiggerBees: Depth First Search Leveraging Hierarchical Block-Level Stealing on GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 GPU 并行 DFS 算法 DiggerBees，用两级栈、warp 级块内窃取与块间窃取，解决 GPU 上 DFS 的栈容量、块内效率与跨块负载不均问题。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 2: Scheduling and Load Balancing</p>
</div>

**作者**：Yuyao Niu, Yuechen Lu, Weifeng Liu, and Marc Casas — Barcelona Supercomputing Center, Spain; Universitat Politècnica de Catalunya, Spain; China University of Petroleum-Beijing, China

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 12:10–12:30 · Session 2: Scheduling and Load Balancing（主席：V Krishna Nandivada）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786457) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Depth First Search (DFS) is a fundamental graph traversal algorithm with broad applications. While existing work-stealing DFS approaches achieve strong performance on CPUs, mapping them to modern GPUs faces three major challenges: (1) limited shared memory cannot accommodate deep stacks, (2) frequent stack operations hinder efficient intra-block execution, and (3) irregular workloads complicate scalable inter-block execution. In this paper, we propose DiggerBees, a GPU-optimized parallel DFS algorithm with hierarchical block-level stealing, consisting of three components. First, we introduce a two-level stack structure to mitigate shared memory limitations. Second, we employ warp-level DFS with intra-block work stealing to enable efficient execution within a block. Third, we implement inter-block work stealing to achieve scalable execution across blocks and sustain high parallelism. Experimental results on the latest NVIDIA GPUs show that DiggerBees outperforms existing DFS approaches, CKL-PDFS, ACR-PDFS, and NVG-DFS, achieving average speedups of 1.37×, 1.83×, and 30.18×, respectively. Moreover, DiggerBees even surpasses high-performance GPU BFS implementations on graphs with deep and narrow traversal paths, and scales efficiently across GPU generations.

## 中文摘要

深度优先搜索（Depth First Search，DFS）是一种基础的图遍历算法，应用广泛。尽管现有的工作窃取式 DFS 方法在 CPU 上取得了很好的性能，但将其映射到现代 GPU 上面临三大挑战：(1) 有限的共享内存无法容纳较深的栈；(2) 频繁的栈操作阻碍了高效的块内执行；(3) 不规则的工作负载使可扩展的块间执行变得复杂。本文提出 DiggerBees，一种面向 GPU 优化、具有层次化块级窃取的并行 DFS 算法，它由三个部分组成。首先，我们引入两级栈结构以缓解共享内存的限制。其次，我们采用带块内工作窃取的 warp 级 DFS，以在块内实现高效执行。第三，我们实现块间工作窃取，以在块之间实现可扩展的执行并维持高并行度。在最新 NVIDIA GPU 上的实验结果表明，DiggerBees 优于现有 DFS 方法 CKL-PDFS、ACR-PDFS 和 NVG-DFS，平均加速比分别为 1.37×、1.83× 和 30.18×。此外，在具有深而窄的遍历路径的图上，DiggerBees 甚至超过了高性能的 GPU BFS 实现，并且能够跨 GPU 代际高效扩展。

## 英文关键词

Depth First Search, work stealing, GPU

## 中文关键词

深度优先搜索（DFS）；工作窃取；GPU

---

## 一句话总结

> 提出 GPU 并行 DFS 算法 DiggerBees，用两级栈、warp 级块内窃取与块间窃取，解决 GPU 上 DFS 的栈容量、块内效率与跨块负载不均问题。

## 研究问题

把工作窃取 DFS 映射到 GPU 面临三大挑战：共享内存容不下深栈、频繁栈操作阻碍块内执行、不规则负载难以跨块扩展。

## 方法简述

- 设计两级栈结构，缓解共享内存对深栈的限制。
- 采用 warp 级 DFS 与块内工作窃取，提升块内执行效率。
- 实现块间工作窃取，在多个 block 间保持高并行度。

## 主要结果

- 在最新 NVIDIA GPU 上相比 CKL-PDFS、ACR-PDFS、NVG-DFS 平均加速 1.37×、1.83×、30.18×。
- 在深而窄的遍历图上甚至超过高性能 GPU BFS，并能跨 GPU 代际高效扩展。

---

> 所属 Session：[Session 2: Scheduling and Load Balancing](index.md) · 返回 [PPoPP 2026 总览](../index.md)
