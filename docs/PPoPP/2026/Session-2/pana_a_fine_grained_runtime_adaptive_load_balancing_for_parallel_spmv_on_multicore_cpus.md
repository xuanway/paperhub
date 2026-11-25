---
title: "PANA: A Fine-Grained Runtime-Adaptive Load Balancing for Parallel SpMV on Multicore CPUs"
description: "PPoPP 2026 Session 2（Scheduling and Load Balancing）：微操作级细粒度自适应均衡，几何平均 1.36×–7.72×"
tags:
  - "PPoPP2026"
  - "Session-2"
  - "Scheduling and Load Balancing"
  - "SpMV"
  - "Load Balancing"
  - "Multicore"
authors:
  - "Haodong Bian"
  - "Youhui Zhang"
  - "Xiang Fei"
  - "Jianqiang Huang"
  - "Xiaoying Wang"
session: "Session 2: Scheduling and Load Balancing"
session_number: 2
session_chair: "V Krishna Nandivada"
date: "2026-02-02"
time: "12:30–12:50"
room: "Pyrmont"
doi: "10.1145/3774934.3786459"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# PANA: A Fine-Grained Runtime-Adaptive Load Balancing for Parallel SpMV on Multicore CPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出面向多核 CPU 并行 SpMV 的细粒度运行时自适应负载均衡方法 PANA，在微操作级别同时平衡各核的计算与访存。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 2: Scheduling and Load Balancing</p>
</div>

**作者**：Haodong Bian, Youhui Zhang, Xiang Fei, Jianqiang Huang, and Xiaoying Wang — Tsinghua University, China; Qinghai University, China; Zhongguancun Laboratory, China

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 12:30–12:50 · Session 2: Scheduling and Load Balancing（主席：V Krishna Nandivada）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786459) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

SpMV has been widely utilized and is regarded as a significant kernel in various scientific and engineering computing applications, where its parallel performance is heavily influenced by matrix sparsity and hardware architecture. Despite extensive prior research, static partitioning strategies that narrowly target computation or memory access remain a key performance bottleneck, severely stifling performance advancement of SpMV on modern multicore CPUs. This paper presents PANA, a fine-grained runtime-adaptive load balancing for parallel SpMV that operates at the micro-operation level. It employs fine-grained partitioning and a dynamic runtime adjustment mechanism to achieve balanced per-core computation and memory access. Experimental results demonstrate that across 2,898 SuiteSparse matrices, PANA consistently outperforms all baseline methods (CAMLB, CSR5, Merge, CVR, SpV8, MKL, and AOCL) in terms of overall performance, achieving geometric-mean speedups ranging from 1.36× to 7.72× on Intel and AMD CPUs.

## 中文摘要

稀疏矩阵向量乘（SpMV）已被广泛使用，并被视为各类科学与工程计算应用中的重要内核，其并行性能在很大程度上受矩阵稀疏性与硬件体系结构的影响。尽管已有大量研究，但仅狭隘地针对计算或内存访问的静态划分策略仍然是关键的性能瓶颈，严重制约了 SpMV 在现代多核 CPU 上的性能提升。本文提出 PANA，一种面向并行 SpMV 的细粒度运行时自适应负载均衡方法，它在微操作（micro-operation）层面运作。PANA 采用细粒度划分与动态运行时调整机制，以实现每个核上计算与内存访问的均衡。实验结果表明，在 2,898 个 SuiteSparse 矩阵上，PANA 在整体性能上始终优于所有基线方法（CAMLB、CSR5、Merge、CVR、SpV8、MKL 和 AOCL），在 Intel 与 AMD CPU 上取得 1.36× 至 7.72× 的几何平均加速比。

## 英文关键词

sparse matrix-vector multiplication, load balancing, micro-operation, runtime-adaptive, fine-grained partitioning

## 中文关键词

稀疏矩阵向量乘（SpMV）；负载均衡；微操作（micro-operation）；运行时自适应（runtime-adaptive）；细粒度划分

---

## 一句话总结

> 提出面向多核 CPU 并行 SpMV 的细粒度运行时自适应负载均衡方法 PANA，在微操作级别同时平衡各核的计算与访存。

## 研究问题

仅针对计算或访存的静态划分策略仍是 SpMV 在现代多核 CPU 上的关键性能瓶颈。

## 方法简述

- 在微操作级别进行细粒度任务划分。
- 引入运行时动态调整机制，使各核的计算与访存负载保持均衡。

## 主要结果

- 在 2898 个 SuiteSparse 矩阵上整体优于 CAMLB、CSR5、Merge、CVR、SpV8、MKL 与 AOCL。
- 在 Intel 与 AMD CPU 上取得 1.36×–7.72× 的几何平均加速。

---

> 所属 Session：[Session 2: Scheduling and Load Balancing](index.md) · 返回 [PPoPP 2026 总览](../index.md)
