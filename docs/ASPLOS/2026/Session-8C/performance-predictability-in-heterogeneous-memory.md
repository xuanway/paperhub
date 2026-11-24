---
title: "Performance Predictability in Heterogeneous Memory"
description: "ASPLOS 2026 · Session 8C · 异构内存中的性能可预测性"
tags:
  - "ASPLOS2026"
  - "Session 8C"
  - "Memory Hierarchy & Performance"
---

# Performance Predictability in Heterogeneous Memory

**中文标题：** 异构内存中的性能可预测性

**所属 Session：** [Session 8C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jinshu Liu (Virginia Tech), Hanchen Xu (Virginia Tech), Daniel S. Berger (Microsoft and University of Washington and CMU), Marcos K. Aguilera (NVIDIA), Huaicheng Li (Virginia Tech)

**单位：** Virginia Tech；Microsoft and University of Washington and CMU；NVIDIA

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790201) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Heterogeneous memory combining DRAM and CXL exhibits variable performance, yet existing metrics correlate weakly with actual slowdown. We present Camp, a principled framework for predicting CXL-induced slowdown. Our key insight is that a DRAM run (plus a CXL run for bandwidth-bound workloads) exposes the causal microarchitectural pressure points where CXL latency translates into additional processor stall cycles. Camp captures these signals using 12 performance counters to analytically decompose slowdown into three orthogonal components: demand reads, cache/prefetching, and stores. Camp also introduces a closed-form model for software-based weighted interleaving that predicts performance across DRAM– CXL ratios. Across 265 workloads on NUMA and three CXL devices, Camp achieves 91–97% prediction accuracy within 10% absolute error. We demonstrate that these models enable practical system policies, including “Best-shot” interleaving and colocated workload placement, improving performance by up to 21% and 23% over existing tiering and colocation approaches.

## 中文摘要

结合 DRAM 与 CXL 的异构内存表现出多变的性能，然而现有指标与实际减速之间的相关性很弱。我们提出 Camp，一个用于预测 CXL 所致减速的具有原理基础的框架。我们的关键洞见是：一次 DRAM 运行（对带宽受限负载再加一次 CXL 运行）能够暴露出导致 CXL 延迟转化为额外处理器停顿周期的因果性微架构压力点。Camp 使用 12 个性能计数器捕获这些信号，以分析方式将减速分解为三个正交分量：需求读取、缓存/预取以及存储。Camp 还引入了基于软件的加权交织的闭式模型，可预测不同 DRAM– CXL 比例下的性能。在 NUMA 与三种 CXL 设备上的 265 个负载中，Camp 在 10% 绝对误差内达到 91–97% 的预测准确率。我们证明这些模型可支撑实用的系统策略，包括“Best-shot”交织与同置负载放置，相比现有分层与同置方法分别提升性能最高 21% 和 23%。

## 英文关键词

CXL Memory, Modeling, Prediction, Interleaving

## 中文关键词

CXL 内存；建模；预测；交织

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790201)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8C](index.md) · [返回 ASPLOS 2026](../index.md)
