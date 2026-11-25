---
title: "ESG: Pipeline-Conscious Efficient Scheduling of DNN Workflows on Serverless Platforms with Shareable GPUs"
description: "HPDC 2024 · Session 7 — Resource Management"
tags:
  - "HPDC2024"
  - "Session 7"
  - "Resource Management"
---

# ESG: Pipeline-Conscious Efficient Scheduling of DNN Workflows on Serverless Platforms with Shareable GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 7 — Resource Management（2024年6月7日 11:45–13:00 · Session Chair：Kento Sato）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 7</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658657)

**作者**：Xinning Hui, Yuanchao Xu, Zhishan Guo, Xipeng Shen

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 7 — Resource Management（2024年6月7日 11:45–13:00 · Session Chair：Kento Sato）

---

## 英文摘要

Recent years have witnessed increasing interest in machine learning inferences on serverless computing for its auto-scaling and cost effective properties. Existing serverless computing, however, lacks effective job scheduling methods to handle the schedule space dramatically expanded by GPU sharing, task batching, and inter-task relations. Prior solutions have dodged the issue by neglecting some important factors, leaving some large performance potential locked. This paper presents ESG, a new scheduling algorithm that directly addresses the difficulties. ESG treats sharable GPU as a first-order factor in scheduling. It employs an optimality-guided adaptive method by combining A*-search and a novel dual-blade pruning to dramatically prune the scheduling space without compromising the quality. It further introduces a novel method, dominator-based SLO distribution, to ensure the scalability of the scheduler. The results show that ESG can significantly improve the SLO hit rates (61%-80%) while saving 47%-187% costs over prior work.

## 中文摘要

近年来，由于其自动伸缩与成本效益特性，无服务器计算上的机器学习推理日益受到关注。然而，现有无服务器计算缺乏有效的作业调度方法，难以应对由 GPU 共享、任务批处理与任务间关系大幅扩展的调度空间。先前方案通过忽略一些重要因素来回避该问题，使若干巨大性能潜力被锁死。本文提出 ESG，一种直接应对这些难点的新调度算法。ESG 将可共享 GPU 视为调度中的一阶因素。它采用最优性引导的自适应方法，结合 A* 搜索与新颖的双刃剪枝，在不损害质量的前提下大幅剪枝调度空间。它进一步引入一种新方法——基于支配者的 SLO 分配，以确保调度器的可扩展性。结果表明，ESG 能显著提升 SLO 命中率（61%–80%），同时相比先前工作节省 47%–187% 的成本。

## 英文关键词

Cloud computing, Serverless Computing, Quality of Service, Function-as-a-Service, Resource Management, Resource Allocation, Resource Efficiency, Machine Learning for Systems, Deep Learning

## 中文关键词

云计算，无服务器计算，服务质量，函数即服务，资源管理，资源分配，资源效率，面向系统的机器学习，深度学习

---

[← 返回 Session 7 — Resource Management](index.md)
