---
title: "The Memory Processing Unit: A Generalized Interface for End-to-End In-Memory Execution"
description: "HPCA 2026 · Processing-in-Memory Architectures"
tags:
  - "HPCA2026"
  - "Processing-in-Memory Architectures"
---

# The Memory Processing Unit: A Generalized Interface for End-to-End In-Memory Execution

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Processing-in-Memory Architectures。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Processing-in-Memory Architectures</p>
</div>

**论文链接**：
**作者**：Minh S. Q. Truong Carnegie Mellon University , Yiqiu Sun University of Illinois Urbana-Champaign , Dawei Xiong University of Illinois Urbana-Champaign , Amol Shah University of Illinois Urbana-Champaign , Alex Glass Carnegie Mellon University , Abraham Farrell University of Illinois Urbana-Champaign , James A. Bain Carnegie Mellon University , L. Richard Carley Carnegie Mellon University , Saugata Ghose University of Illinois Urbana-Champaign
**会议**：HPCA 2026

---

## 中文标题

内存处理单元：面向端到端存内执行的通用接口

## 英文摘要

The processing-using-memory (PUM; a.k.a. in-memory computing) paradigm aims to eliminate data movement energy and performance costs by using memory cell interactions to directly perform computation. Given PUM’s potential for large savings, prior works have proposed many different datapath microarchitectures to demonstrate how general-purpose PUM benefits a wide range of application kernels. Unfortunately, these efforts largely depend on microarchitecture-specific vector-like interfaces that (1) force many of an application’s operations to be offloaded to a CPU, (2) require significant programmer effort to scale up applications to an entire memory chip, and (3) make it impractical to develop badly-needed systems software and programming tools for PUM. To address these three issues, we propose the memory processing unit (MPU), a microarchitecture-agnostic interface layer for general-purpose PUM with three components. First, we develop an MPU instruction set architecture (ISA) with instructions to facilitate application scaling and task coordination. Second, we propose an ensemble execution model that coordinates execution across millions of PUM vector function units and maps to most general-purpose PUM microarchitectures. Third, we design a comprehensive MPU control path that efficiently executes MPU ISA binaries across multiple ensembles, and can enable CPU-free execution of complex end-to-end applications with PUM. We demonstrate how the MPU maps to multiple previously-proposed PUM datapaths, and how it achieves average performance/energy improvements of 1.79×/3.23× for 21 data-intensive kernels over these prior works (67×/47× vs. a modern GPU), while also achieving performance and energy improvements for the complex end-to-end applications.

## 中文摘要

处理即用内存（PUM，又称存内计算）范式旨在利用存储单元间的相互作用直接完成计算，从而消除数据搬运的能耗与性能开销。鉴于 PUM 的节省潜力，已有工作提出多种数据通路微架构，展示通用 PUM 如何惠及广泛的应用内核。然而这些努力大多依赖特定于微架构的类向量接口：它们迫使应用的许多操作卸载到 CPU，需要程序员付出大量努力才能把应用扩展到整个内存芯片，并使 PUM 急需的系统软件与编程工具难以开发。针对这三点，我们提出内存处理单元（MPU），一种与微架构无关的通用 PUM 接口层，包含三个部分。其一为 MPU 指令集架构（ISA），其指令便于应用扩展与任务协同；其二为集合执行模型，在数百万 PUM 向量功能单元间协调执行，并可映射到大多数通用 PUM 微架构；其三为完整的 MPU 控制路径，可跨多个集合高效执行 MPU ISA 二进制，支持复杂端到端应用的无 CPU 执行。我们展示了 MPU 对多种已有 PUM 数据通路的映射，以及在 21 个数据密集型内核上相比这些工作平均 1.79 倍性能与 3.23 倍能效提升（相比现代 GPU 为 67 倍/47 倍），复杂端到端应用上亦获得性能与能效提升。
