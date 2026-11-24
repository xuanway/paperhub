---
title: "PUSHtap: PIM-based In-Memory HTAP with Unified Data Storage Format"
description: "ASPLOS 2026 · Session 4D · PUSHtap：基于 PIM 的统一数据存储格式内存 HTAP 系统"
tags:
  - "ASPLOS2026"
  - "Session 4D"
  - "Processing-in-Memory"
---

# PUSHtap: PIM-based In-Memory HTAP with Unified Data Storage Format

**中文标题：** PUSHtap：基于 PIM 的统一数据存储格式内存 HTAP 系统

**所属 Session：** [Session 4D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yilong Zhao (Shanghai Jiao Tong University), Mingyu Gao (Tsinghua University), Huanchen Zhang (Tsinghua University), Fangxin Liu (Shanghai Jiao Tong University), Gongye Chen (Shanghai Jiao Tong University), He Xian (Shanghai Qi Zhi Institute), Li Jiang (Shanghai Jiao Tong University)

**单位：** Shanghai Jiao Tong University；Tsinghua University；Shanghai Qi Zhi Institute

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736120) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Hybrid transaction/analytical processing (HTAP) is an emerging database paradigm that supports both online transaction processing (OLTP) and online analytical processing (OLAP) workloads. Computing-intensive OLTP operations, involving row-wise data manipulation, are suitable for row-store format. In contrast, memory-intensive OLAP operations, which are column-centric, benefit from column-store format. This data-format dilemma prevents HTAP systems from concurrently achieving three design goals: performance isolation, data freshness, and workload-specific optimization. Another background technology is Processing-in-Memory (PIM), which integrates computing units (PIM units) inside DRAM memory devices to accelerate memory-intensive workloads, including OLAP. Our key insight is to combine the interleaved CPU access and localized PIM unit access to provide two-dimensional access to address the data format contradictions inherent in HTAP. First, we propose a unified data storage format with novel data alignment and placement techniques to optimize the effective bandwidth of CPUs and PIM units and exploit the PIM's parallelism. Second, we implement the multi-version concurrency control (MVCC) essential for single-instance HTAP. Third, we extend the commercial PIM architecture to support the OLAP operations and concurrent access from PIM and CPU. Experiments show that PUSHtap can achieve 3.4×/4.4× OLAP/OLTP throughput improvement compared to multi-instance PIM-based design.

## 中文摘要

混合事务/分析处理（HTAP）是一种新兴的数据库范式，同时支持联机事务处理（OLTP）与联机分析处理（OLAP）负载。计算密集的 OLTP 操作涉及按行数据操作，适合行存储格式；相反，访存密集的 OLAP 操作以列为中心，受益于列存储格式。这一数据格式困境使 HTAP 系统无法同时实现三个设计目标：性能隔离、数据新鲜度与负载特定优化。另一项背景技术是存内处理（Processing-in-Memory，PIM），它将计算单元（PIM 单元）集成到 DRAM 存储设备内部，以加速包括 OLAP 在内的访存密集负载。我们的关键洞见是结合交错的 CPU 访问与本地化的 PIM 单元访问，提供二维访问，从而化解 HTAP 中固有的数据格式矛盾。首先，我们提出一种统一的数据存储格式，采用新颖的数据对齐与放置技术，以优化 CPU 与 PIM 单元的有效带宽并发挥 PIM 的并行性。其次，我们实现了单实例 HTAP 所必需的多版本并发控制（MVCC）。第三，我们扩展商用 PIM 架构，以支持 OLAP 操作以及来自 PIM 与 CPU 的并发访问。实验表明，与基于 PIM 的多实例设计相比，PUSHtap 可实现 3.4×/4.4× 的 OLAP/OLTP 吞吐量提升。

## 英文关键词

Processing-in-Memory (PIM), Hybrid Transactional/Analytical Processing (HTAP), DRAM, Unified Data Format

## 中文关键词

存内处理（PIM）；混合事务/分析处理（HTAP）；DRAM；统一数据格式

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736120)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。

[返回 Session 4D](index.md) · [返回 ASPLOS 2026](../index.md)
