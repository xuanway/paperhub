---
title: "The Sparsity-Aware LazyGPU Architecture"
description: "ISCA 2025 · Session 6B · 稀疏感知 LazyGPU 架构"
tags:
  - "ISCA2025"
  - "Session 6B"
  - "Microarchitecture II"
---

# The Sparsity-Aware LazyGPU Architecture

**中文标题：** 稀疏感知 LazyGPU 架构

**所属 Session：** [Session 6B](index.md) · [ISCA 2025](../index.md)

**作者：** Changxi Liu, Yu Miao, Yifan Sun, Trevor E. Carlson

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731009) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

General-Purpose Graphics Processing Units (GPUs) are essential ac- celerators in data-parallel applications, including machine learning, and physical simulations. Although GPUs utilize fast wavefront context switching to hide memory access latency, memory con- tinues to be a significant bottleneck, limiting overall performance for many important workloads. Current GPU hardware enhance- ments focus on issuing memory requests in advance to help solve the memory bandwidth bottleneck and improve GPU performance. However, this approach can still be inefficient, leading to hardware contention and suboptimal resource utilization. Instead of issuing memory requests in advance, we take an alter- native view on improving GPU performance: lazily issuing memory requests to eliminate memory requests where either (a) the fetched values are zero or (b) they do not affect the result of the execut- ing workload. Building on these insights, we propose LazyGPU, which integrates lazy execution cores with a Zero Cache to elimi- nate memory requests when all data required by a wavefront is zero. Moreover, LazyGPU utilizes instructions, including multiplication and multiply-add, to eliminate memory requests whose fetched val- ues do not affect the outcomes of these instructions. For example, LazyGPU achieves a 2.18×speedup compared with the baseline at 60% weight sparsity for the inference of LLaMA 7B.

## 中文摘要

通用图形处理器（GPU）是数据并行应用（包括机器学习、物理仿真）中不可或缺的加速器。GPU依靠快速的波前上下文切换掩盖访存延迟，但内存依旧是显著瓶颈，制约大量关键负载的整体性能。当前GPU硬件优化思路主要是提前发起内存请求，试图缓解带宽瓶颈、提升性能。但该方式仍存在低效问题，容易引发硬件资源竞争，造成资源利用率不足。

本文不采用提前发起访存的思路，而是从另一个角度优化GPU性能：延迟发起内存请求，在两种场景下直接消除访存：（a）读取的数据为零；（b）读取的数据不会影响最终计算结果。基于该思路，本文提出LazyGPU，集成延迟执行核与零缓存（Zero Cache）：当一个波前所需全部数据都是零时，直接跳过内存请求。同时，LazyGPU利用乘法、乘加等指令的特性，识别并剔除那些读取后不改变指令输出结果的内存请求。
例如，在权重稀疏度60%的LLaMA 7B推理任务上，LazyGPU相比基线GPU实现2.18倍提速。

## 英文关键词

GPU Architecture, Lazy Execution, Zero Cache

## 中文关键词

GPU 架构, 延迟执行, 零缓存

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731009)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6B](index.md) · [返回 ISCA 2025](../index.md)
