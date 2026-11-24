---
title: "UPP: Universal Predicate Pushdown to Smart Storage"
description: "ISCA 2025 · Session 3C · UPP: 通用谓词下推到智能存储"
tags:
  - "ISCA2025"
  - "Session 3C"
  - "Storage"
---

# UPP: Universal Predicate Pushdown to Smart Storage

**中文标题：** UPP: 通用谓词下推到智能存储

**所属 Session：** [Session 3C](index.md) · [ISCA 2025](../index.md)

**作者：** Ipoom Jeong, Jinghan Huang, Chuxuan Hu, Dohyun Park, Jaeyoung Kang, Nam Sung Kim, Yongjoo Park

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731005) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

In large-scale analytics, in-storage processing (ISP) can significantly boost query performance by letting ISP engines (e.g., FPGAs) pre- select only the relevant data before sending them to databases. This reduces the amount of not only data transfer between storage and host, but also database computation, facilitating faster query processing. However, existing ISP solutions cannot effectively sup- port a wide range of modern analytical queries because they only support simple combinations of frequently used operators (e.g., =, <), particularly on fixed-length columns. As modern databases al- low filter predicates to include numerous operators/functions (e.g., dateadd) compatible with diverse data formats (and their complex combinations), it becomes more challenging for existing approaches to accelerate such queries efficiently. 

To address the limitations, we propose a new ISP approach, called Universal Predicate Pushdown (UPP), that can accelerate modern analytical databases, leveraging hardware/software co-design for a high level of flexibility. Our core insight is that instead of program- ming for individual filter operators/functions, we should devise a compact instruction set architecture (ISA) tailored explicitly for predicate pushdown. The software (i.e., database) layer recognizes and compiles various general filters (called a universal predicate) to a set of UPP-compliant instructions, which are then processed effi- ciently by FPGA using bitwise comparisons, leveraging lightweight metadata. In our experiments with a 100 GB TPC-H dataset, UPP running on SmartSSD could speed up Spark’s end-to-end query performance by 1.2×–7.9×without changing input data formats.

## 中文摘要

在大规模分析场景中，存储内计算（ISP）能够让ISP引擎（如FPGA）预先筛选出相关数据，再送入数据库，从而显著提升查询性能。这不仅减少存储与主机之间的数据传输量，还降低数据库侧的计算开销，加快查询处理速度。然而现有ISP方案仅支持常用算子（如等于、小于）的简单组合，且大多只能处理定长列，难以广泛支持各类现代分析查询。现代数据库的过滤谓词可以包含大量算子与函数（例如日期加法dateadd），适配多种数据格式并形成复杂组合，这给现有方案的高效加速带来很大挑战。

为解决上述局限，本文提出通用谓词下推（UPP）这一新的ISP方案，依托软硬件协同设计实现高灵活性，用于加速现代分析型数据库。核心思路是：不再针对单个过滤算子或函数单独编程，而是设计一套专门面向谓词下推的精简指令集架构（ISA）。软件层（数据库）识别各类通用过滤条件（称为通用谓词），并编译为符合UPP规范的指令；FPGA借助轻量元数据，通过按位比较高效执行这些指令。我们基于100GB的TPC-H数据集开展实验，在SmartSSD上运行的UPP，在不改动输入数据格式的前提下，将Spark端到端查询性能提升1.2倍至7.9倍。

## 英文关键词

In-Storage Processing (ISP), Instruction Set Architecture (ISA), Com- putational Storage Drive (CSD), Field-Programmable Gate Array (FPGA), Database, Online Analytical Processing (OLAP)

## 中文关键词

存储内计算（ISP）, 指令集架构（ISA）, 计算存储盘（CSD）, 现场可编程门阵列（FPGA）, 数据库, 联机分析处理（OLAP）

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731005)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3C](index.md) · [返回 ISCA 2025](../index.md)
