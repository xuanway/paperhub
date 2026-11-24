---
title: "Understanding Query Optimization Bugs in Graph Database Systems"
description: "ASPLOS 2026 · Session 6C · 理解图数据库系统中的查询优化缺陷"
tags:
  - "ASPLOS2026"
  - "Session 6C"
  - "Graph & Sparse Computing"
---

# Understanding Query Optimization Bugs in Graph Database Systems

**中文标题：** 理解图数据库系统中的查询优化缺陷

**所属 Session：** [Session 6C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zhongxing Yu (Shandong University), Yuyu Chen (Shandong University)

**单位：** Shandong University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790244) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Recent years have witnessed an ever-growing usage of graph database management systems (GDBMSs) in various datadriven applications. Query optimization aims to improve the performance of database queries by identifying the most efficient way to execute them, and is an important stage of GDBMS workflow. Like other sophisticated systems, such as compilers, the query optimization process is complex and its implementation is prone to bugs. This paper conducts the first characteristic study of query optimization bugs in GDBMSs, including the root causes, manifestation methods, and fix strategies, and delivers 10 novel and important findings about them. Based on the characteristic study, we also developed a testing tool tailored to uncover GDBMS query optimization bugs, and the tool found 20 unique GDBMS bugs, 10 of which are query optimization bugs.

## 中文摘要

近年来，图数据库管理系统（GDBMS）在各种数据驱动应用中的使用持续增长。查询优化旨在通过确定执行数据库查询的最高效方式来提升查询性能，是 GDBMS 工作流中的一个重要阶段。与编译器等其他复杂系统一样，查询优化过程十分复杂，其实现容易产生缺陷。本文首次对 GDBMS 中的查询优化缺陷开展特征研究，涵盖根本原因、表现形式和修复策略，并给出了 10 项新颖且重要的相关发现。在该特征研究的基础上，我们还开发了一个专门用于发现 GDBMS 查询优化缺陷的测试工具，该工具发现了 20 个独特的 GDBMS 缺陷，其中 10 个是查询优化缺陷。

## 英文关键词

Query Optimization; Compilers; Software Testing; Graph Database Systems

## 中文关键词

查询优化；编译器；软件测试；图数据库系统

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790244)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6C](index.md) · [返回 ASPLOS 2026](../index.md)
