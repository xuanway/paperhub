---
title: "Towards Scalable Unstructured Mesh Computations on Shared Memory Many-Cores"
description: "PPoPP 2024 Session High Performance Computing：递归划分网格构建任务依赖树，工业 CFD 上最高 8.1× 提速"
tags:
  - "PPoPP2024"
  - "Session-3"
  - "High Performance Computing"
  - "unstructured mesh"
  - "task dependency tree"
  - "shared memory parallelism"
authors:
  - "Haozhong Qiu"
  - "Chuanfu Xu"
  - "Jianbin Fang"
  - "Liang Deng"
  - "Jian Zhang"
  - "Qingsong Wang"
  - "Yue Ding"
  - "Zhe Dai"
  - "ShiZhao Chen"
  - "Yonggang Che"
  - "Jie Liu"
session: "Session 3: High Performance Computing"
session_number: 3
session_chair: "Helen Xu"
date: "2024-03-04"
time: "14:40–15:00"
room: "Moorfoot"
doi: "10.1145/3627535.3638473"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Towards Scalable Unstructured Mesh Computations on Shared Memory Many-Cores

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出递归划分并重排非结构网格以构建任务依赖树（TDT），在暴露并行性的同时遵守数据冲突与依赖，并以两种递归策略支持 CPU 与 GPU，在工业 CFD 软件上最高提速 8.1×。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 3: High Performance Computing</p>
</div>

**作者**：Haozhong Qiu (School of Computer Science and Technology, National University of Defense Technology); Chuanfu Xu (Laboratory of Digitizing Software for Frontier Equipment, School of Computer Science and Technology, National University of Defense Technology); Jianbin Fang (School of Computer Science and Technology, National University of Defense Technology); Liang Deng, Jian Zhang (China Aerodynamic Research and Development Center); Qingsong Wang (School of Computer Science and Technology, National University of Defense Technology); Yue Ding (School of Computer Science and Technology, dingyue@nudt.edu.cn); Zhe Dai (China Aerodynamic Research and Development Center); ShiZhao Chen (School of Computer Science and Technology, National University of Defense Technology); Yonggang Che, Jie Liu (Laboratory of Digitizing Software for Frontier Equipment, School of Computer Science and Technology, National University of Defense Technology)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 14:40–15:00 · Session 3: High Performance Computing（主席：Helen Xu）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638473) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Due to data conflicts or data dependences, exploiting shared memory parallelism on unstructured mesh applications is highly challenging. The prior approaches are neither general nor scalable on emerging many-core processors. This paper presents a general and scalable shared memory approach for unstructured mesh computations. We recursively divide and reorder an unstructured mesh to construct a task dependency tree (TDT), where massive parallelism is exposed and data conflicts as well as data dependences are respected. We propose two recursion strategies to support popular programming models on both CPUs and GPUs for TDT. We evaluate our approach by applying it to an industrial unstructured Computational Fluid Dynamics (CFD) software. Experimental results show that our approach significantly outperforms the prior shared memory approaches, delivering up to 8.1× performance improvement over the engineer-tuned implementations.

## 中文摘要

由于数据冲突或数据依赖，在非结构网格应用上开发共享内存并行极具挑战性。已有方法在新兴众核处理器上既不通用也不可扩展。本文提出一种通用且可扩展的非结构网格计算共享内存方法。我们递归地划分并重排一个非结构网格，以构造任务依赖树（TDT），在其中暴露大量并行性，同时遵守数据冲突与数据依赖。我们提出两种递归策略，以在 CPU 和 GPU 上为 TDT 支持流行的编程模型。我们通过将该方法应用于一个工业级非结构计算流体力学（CFD）软件来评估它。实验结果表明，我们的方法显著优于先前的共享内存方法，相对于工程师调优的实现最多带来 8.1× 的性能提升。

## 英文关键词

Unstructured mesh, data conflicts, data dependences, shared memory parallelism, task dependency tree

## 中文关键词

非结构网格；数据冲突；数据依赖；共享内存并行；任务依赖树

---

## 一句话总结

> 提出递归划分并重排非结构网格以构建任务依赖树（TDT），在暴露并行性的同时遵守数据冲突与依赖，并以两种递归策略支持 CPU 与 GPU，在工业 CFD 软件上最高提速 8.1×。

## 研究问题

由于数据冲突或数据依赖，在非结构网格应用上开发共享内存并行极具挑战；已有方法在新兴众核处理器上既不通用也不可扩展。

## 方法简述

- 递归地划分并重排非结构网格，构建任务依赖树（TDT），在暴露大量并行性的同时遵守数据冲突与数据依赖
- 提出两种递归策略，使 TDT 在 CPU 与 GPU 上支持流行的编程模型
- 将该方法应用于一个工业级非结构计算流体力学（CFD）软件进行评估

## 主要结果

- 相比先前的共享内存方法显著更优，相对工程师手工调优的实现最多取得 8.1× 性能提升
- 两种递归策略在 CPU 与 GPU 上均可用，表明方法具有通用性
- 在工业级 CFD 软件上验证了可扩展性

---

> 所属 Session：[Session 3: High Performance Computing](index.md) · 返回 [PPoPP 2024 总览](../index.md)
