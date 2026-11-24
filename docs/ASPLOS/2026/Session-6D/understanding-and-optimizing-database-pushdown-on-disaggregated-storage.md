---
title: "Understanding and Optimizing Database Pushdown on Disaggregated Storage"
description: "ASPLOS 2026 · Session 6D · 理解并优化分离式存储上的数据库下推"
tags:
  - "ASPLOS2026"
  - "Session 6D"
  - "Disaggregated Memory Systems"
---

# Understanding and Optimizing Database Pushdown on Disaggregated Storage

**中文标题：** 理解并优化分离式存储上的数据库下推

**所属 Session：** [Session 6D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Hua Zhang (University of Wisconsin at Madison/Beihang University), Xiao Li (University of Wisconsin at Madison/Beihang University), Yuebin Bai (Beihang University), Ming Liu (University of Wisconsin–Madison)

**单位：** University of Wisconsin at Madison/Beihang University；Beihang University；University of Wisconsin–Madison

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790243) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Database pushdown is a widely adopted technique under compute-storage disaggregation. The rising network and I/O speeds, coupled with stagnated compute and memory subsystems of a disaggregated storage architecture in the past decade, render state-of-the-art policy-driven pushdown designs ineffective. This is because the query performance bottleneck has shifted from network and I/O to compute, where computing power at the storage layer becomes scarce. This paper rethinks pushdown database design via a systematic characterization and identifies three root causes, i.e., table structure agnostic, lower interference tolerance, and lack of operator scheduling. Based on the gathered insights, we build TapDB, a new pushdown database that targets emerging storage disaggregation. Driven by two key ideas (i.e., lazy evaluation and trading network and I/O for compute), TapDB introduces four new mechanisms: a table-aware operator cost estimator based on in-situ meta-learning and cardinality estimation, an admission control scheme to limit execution concurrency, a ballooning-based DRAM-SSD hybrid table, and a critical path-driven operator scheduler. Our prototype shows 1.3–2.3× speedups compared with prior solutions when running SSB and TPCH benchmarks.

## 中文摘要

数据库下推是计算—存储分离下被广泛采用的技术。过去十年间不断上升的网络与 I/O 速度，加之分离式存储架构中停滞的计算与内存子系统，使得最先进的策略驱动下推设计失效。这是因为查询性能瓶颈已从网络与 I/O 转向计算，而存储层的算力变得稀缺。本文通过系统性的刻画重新思考下推数据库设计，并识别出三个根因，即：与表结构无关、更低的干扰容忍度，以及缺乏算子调度。基于所获得的洞见，我们构建了 TapDB，一个面向新兴存储分离的新型下推数据库。在两大核心思想（即惰性求值与以网络和 I/O 换取计算）的驱动下，TapDB 引入了四项新机制：基于原位元学习与基数估计的表感知算子代价估计器、用于限制执行并发的准入控制方案、基于膨胀（ballooning）的 DRAM-SSD 混合表，以及关键路径驱动的算子调度器。我们的原型在运行 SSB 与 TPCH 基准测试时，相比先前方案实现了 1.3–2.3× 的加速。

## 英文关键词

Computation pushdown, Storage disaggregation, Query optimization

## 中文关键词

计算下推；存储分离；查询优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790243)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6D](index.md) · [返回 ASPLOS 2026](../index.md)
