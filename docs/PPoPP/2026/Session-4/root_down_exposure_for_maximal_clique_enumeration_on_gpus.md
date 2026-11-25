---
title: "Root-Down Exposure for Maximal Clique Enumeration on GPUs"
description: "PPoPP 2026 Session 4（GPU and Heterogeneous Computing）：根下暴露免同步拉取，比 SOTA 快 1.25–5.38×"
tags:
  - "PPoPP2026"
  - "Session-4"
  - "GPU and Heterogeneous Computing"
  - "Maximal Clique Enumeration"
  - "GPU"
  - "Load Balancing"
authors:
  - "Zhe Pan"
  - "Peng Qu"
  - "Youhui Zhang"
session: "Session 4: GPU and Heterogeneous Computing"
session_number: 4
session_chair: "Frank Mueller"
date: "2026-02-02"
time: "16:30–16:50"
room: "Pyrmont"
doi: "10.1145/3774934.3786449"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Root-Down Exposure for Maximal Clique Enumeration on GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出根下暴露机制并组合位图中心枚举与激进节点生成规则，形成 GPU 极大团枚举方案 RDMCE，比最优 SOTA GPU 方案快 1.25–5.38×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 4: GPU and Heterogeneous Computing</p>
</div>

**作者**：Zhe Pan, Peng Qu, and Youhui Zhang — Tsinghua University, China; Zhongguancun Laboratory, China

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 16:30–16:50 · Session 4: GPU and Heterogeneous Computing（主席：Frank Mueller）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786449) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Maximal clique enumeration (MCE) in large-scale graphs is critical across various application domains, including social network analysis, bioinformatics, and computer vision. However, existing GPU-based MCE solutions suffer from inefficient load-balancing mechanisms. These mechanisms force busy workers to pause and hand over workloads to idle workers, which introduces significant synchronization overhead and increases memory usage. To address these limitations, we introduce a root-down exposure mechanism where busy workers dynamically expose their current root, enabling idle workers to pull workloads from the exposed node directly without synchronization. We then propose a bitmap-centric MCE scheme and an aggressive node generation rule to further simplify the memory layout and accelerate enumeration. We combine them into RDMCE, a Root-Down MCE solution on GPUs. Across large real-world graphs with up to 146 billion maximal cliques, RDMCE is 1.25-5.38× faster than any next-best state-of-the-art GPU-based solutions and is the only one that completes enumeration on every test dataset, offering a more efficient and scalable MCE solution.

## 中文摘要

大规模图中的极大团枚举（MCE）在社交网络分析、生物信息学与计算机视觉等诸多应用领域中至关重要。然而，现有基于 GPU 的 MCE 方案受制于低效的负载均衡机制。这类机制迫使忙碌的工作者暂停并将其工作负载移交给空闲工作者，从而引入显著的同步开销并增加内存占用。为克服这些局限，我们提出根下沉暴露（root-down exposure）机制：忙碌工作者动态暴露其当前根节点，使空闲工作者无需同步即可直接从被暴露的节点拉取工作负载。在此基础上，我们提出以位图为中心的 MCE 方案与激进的节点生成规则，以进一步简化内存布局并加速枚举。我们将二者结合为 RDMCE，一个 GPU 上的根下沉 MCE 方案。在包含多达 1460 亿个极大团的大规模真实图上，RDMCE 比任何次优的最先进 GPU 方案快 1.25–5.38 倍，并且是唯一在每个测试数据集上均完成枚举的方案，提供了更高效、更具可扩展性的 MCE 解决方案。

## 英文关键词

maximal clique enumeration, GPU, load balancing, bitmap

## 中文关键词

极大团枚举；GPU；负载均衡；位图

---

## 一句话总结

> 提出根下暴露机制并组合位图中心枚举与激进节点生成规则，形成 GPU 极大团枚举方案 RDMCE，比最优 SOTA GPU 方案快 1.25–5.38×。

## 研究问题

现有 GPU 极大团枚举方案的负载均衡机制迫使忙碌工作线程暂停并将工作移交给空闲线程，带来显著同步开销并增加内存占用。

## 方法简述

- 提出根下暴露（root-down exposure）机制：忙碌工作线程动态暴露其当前根，空闲工作线程无需同步即可直接从被暴露节点拉取工作。
- 提出以位图为中心的极大团枚举方案，进一步简化内存布局。
- 设计激进的节点生成规则以加速枚举。
- 将上述机制组合为 GPU 上的 RDMCE 方案。

## 主要结果

- 在含有多达 1460 亿个极大团的真实大规模图上，RDMCE 比任何次优的最先进 GPU 方案快 1.25–5.38×。
- 是唯一在所有测试数据集上都完成枚举的方案，可扩展性更好。

---

> 所属 Session：[Session 4: GPU and Heterogeneous Computing](index.md) · 返回 [PPoPP 2026 总览](../index.md)
