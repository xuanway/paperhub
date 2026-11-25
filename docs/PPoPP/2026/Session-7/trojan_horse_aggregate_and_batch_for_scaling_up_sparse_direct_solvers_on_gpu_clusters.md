---
title: "Trojan Horse: Aggregate-and-Batch for Scaling Up Sparse Direct Solvers on GPU Clusters"
description: "PPoPP 2026 Session 7（Cluster and Cloud Computing）：小任务聚合+批处理，A100 上 SuperLU_DIST 最高加速 418.79×"
tags:
  - "PPoPP2026"
  - "Session-7"
  - "Cluster and Cloud Computing"
  - "sparse direct solver"
  - "GPU cluster"
  - "task batching"
authors:
  - "Yida Li"
  - "Siwei Zhang"
  - "Yiduo Niu"
  - "Yang Du"
  - "Qingxiao Sun"
  - "Zhou Jin"
  - "Weifeng Liu"
session: "Session 7: Cluster and Cloud Computing"
session_number: 7
session_chair: "Ruslan Nikolaev"
date: "2026-02-03"
time: "12:30–12:50"
room: "Pyrmont"
doi: "10.1145/3774934.3786442"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
award: "Best Paper Nominee"
---

# Trojan Horse: Aggregate-and-Batch for Scaling Up Sparse Direct Solvers on GPU Clusters

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 Trojan Horse 聚合—批处理策略，按优先级聚合小任务后批量送入 GPU 执行，A100 上 SuperLU_DIST 最高加速 418.79 倍。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 7: Cluster and Cloud Computing</p>
</div>

**作者**：Yida Li, Siwei Zhang, Yiduo Niu, Yang Du, Qingxiao Sun, Zhou Jin, and Weifeng Liu — China University of Petroleum-Beijing, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 12:30–12:50 · Session 7: Cluster and Cloud Computing（主席：Ruslan Nikolaev）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786442) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

> 🏆 **Best Paper Nominee**

---

## 英文摘要

Sparse direct solvers are critical building blocks in a range of scientific applications on heterogeneous supercomputers. However, existing sparse direct solvers have not been able to well leverage the high bandwidth and floating-point performance of modern GPUs. The primary challenges are twofold: (1) the absence of a mechanism for aggregating small tasks to saturate the GPU, and (2) the lack of a mechanism for executing a diverse set of small tasks in batch mode on a single GPU. We in this paper propose a strategy called Trojan Horse, which significantly enhances the execution efficiency of sparse direct solvers on GPU clusters. This mechanism divides each process’s work into two stages: Aggregate (with two modules Prioritizer and Container) and Batch (with two modules Collector and Executor). In the Aggregate stage, a process first assesses the urgency of the input tasks through the Prioritizer module, and based on their priority, sends them to the Collector module or the Container module. In the batch stage, the Collector module receives high-priority heterogeneous tasks from the Prioritizer module and retrieves enough tasks from the Container module to send them to the Executor module for batch execution on GPU. In addition, our strategy is independent of solver libraries, and is integrated into SuperLU_DIST and PanguLU. In the scale-up evaluation on a single NVIDIA A100 GPU, the Trojan Horse strategy delivers speedups of up to 418.79x (5.47x on average) for SuperLU_DIST and up to 5.59x (2.84x on average) for PanguLU. In the scale-out evaluation on two 16-GPU clusters from NVIDIA and AMD, respectively, Trojan Horse continues to deliver strong performance gains for both SuperLU_DIST and PanguLU across different GPU counts.

## 中文摘要

稀疏直接求解器是异构超级计算机上一系列科学应用的关键基础构件。然而，现有稀疏直接求解器未能很好地利用现代 GPU 的高带宽与浮点性能。主要挑战有两方面：（1）缺乏将小任务聚合以充分利用 GPU 的机制；（2）缺乏在单个 GPU 上以批处理模式执行多样化小任务集的机制。本文提出一种称为 Trojan Horse 的策略，显著提升了稀疏直接求解器在 GPU 集群上的执行效率。该机制将每个进程的工作划分为两个阶段：Aggregate（聚合阶段，包含 Prioritizer 与 Container 两个模块）与 Batch（批处理阶段，包含 Collector 与 Executor 两个模块）。在 Aggregate 阶段，进程首先通过 Prioritizer 模块评估输入任务的紧迫程度，并依据其优先级将任务发送到 Collector 模块或 Container 模块。在 Batch 阶段，Collector 模块接收来自 Prioritizer 模块的高优先级异构任务，并从 Container 模块中取出足够多的任务，一并送至 Executor 模块在 GPU 上批处理执行。此外，我们的策略与求解器库无关，并已集成到 SuperLU_DIST 与 PanguLU 中。在单块 NVIDIA A100 GPU 上的纵向扩展评测中，Trojan Horse 策略为 SuperLU_DIST 带来最高 418.79 倍（平均 5.47 倍）的加速，为 PanguLU 带来最高 5.59 倍（平均 2.84 倍）的加速。在分别由 NVIDIA 和 AMD 提供的两个 16-GPU 集群上进行的横向扩展评测中，Trojan Horse 在不同 GPU 数量下持续为 SuperLU_DIST 与 PanguLU 带来显著的性能提升。

## 英文关键词

Sparse direct solver, Task aggregation, Batched kernels, GPU cluster

## 中文关键词

稀疏直接求解器；任务聚合；批处理内核；GPU 集群

---

## 一句话总结

> 提出 Trojan Horse 聚合—批处理策略，按优先级聚合小任务后批量送入 GPU 执行，A100 上 SuperLU_DIST 最高加速 418.79 倍。

## 研究问题

现有稀疏直接求解器难以充分利用现代 GPU 的高带宽与浮点性能，既缺少把小任务聚合成足以打满 GPU 的机制，也缺少在单 GPU 上批量执行多种小任务的机制。

## 方法简述

- 提出 Trojan Horse 策略，将每个进程的工作划分为 Aggregate 与 Batch 两个阶段。
- 在 Aggregate 阶段设计 Prioritizer 模块评估输入任务的紧迫性，并按优先级把任务送往 Collector 模块或 Container 模块。
- 在 Batch 阶段由 Collector 接收高优先级异构任务，并从 Container 中取出足够多的任务送入 Executor 在 GPU 上批量执行。
- 将策略与求解器库解耦，使其独立于具体库并集成到 SuperLU_DIST 与 PanguLU 中。

## 主要结果

- 在单张 NVIDIA A100 GPU 上扩展评测中，SuperLU_DIST 最高加速 418.79 倍（平均 5.47 倍），PanguLU 最高加速 5.59 倍（平均 2.84 倍）。
- 在 NVIDIA 与 AMD 各一个 16-GPU 集群上的扩展评测中，Trojan Horse 在不同 GPU 数量下仍为两种求解器带来显著性能提升。

---

> 所属 Session：[Session 7: Cluster and Cloud Computing](index.md) · 返回 [PPoPP 2026 总览](../index.md)
