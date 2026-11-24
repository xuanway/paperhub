---
title: "Scaling Automated Database System Testing"
description: "ASPLOS 2026 · Session 7C · 扩展自动化数据库系统测试"
tags:
  - "ASPLOS2026"
  - "Session 7C"
  - "Testing & Fuzzing"
---

# Scaling Automated Database System Testing

**中文标题：** 扩展自动化数据库系统测试

**所属 Session：** [Session 7C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Suyang Zhong (National University of Singapore), Manuel Rigger (National University of Singapore)

**单位：** National University of Singapore

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790215) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Recently, various automated testing approaches have been proposed that use specialized test oracles to find hundreds of logic bugs in mature, widely-used Database Management Systems (DBMSs). These test oracles require database and query generators, which must account for the often significant differences between the SQL dialects of these systems. Since it can take weeks to implement such generators, many DBMS developers are unlikely to invest the time to adopt such automated testing approaches. In short, existing approaches fail to scale to the plethora of DBMSs. In this work, we present both a vision and a platform, SQLancer++, to apply test oracles to any SQL-based DBMS that supports a subset of common SQL features. Our technical core contribution is a novel architecture for an adaptive SQL statement generator. This adaptive SQL generator generates SQL statements with various features, some of which might not be supported by the given DBMS, and then learns through interaction with the DBMS, which of these are understood by the DBMS. Thus, over time, the generator will generate mostly valid SQL statements. We evaluated SQLancer++ across 18 DBMSs and discovered a total of 196 unique, previously unknown bugs, of which 180 were fixed after we reported them. While SQLancer++ is the first major step towards scaling automated DBMS testing, various follow-up challenges remain.

## 中文摘要

近来，人们提出了多种自动化测试方法，它们使用专门的测试预言（test oracle）在成熟且广泛使用的数据库管理系统（DBMS）中发现数百个逻辑缺陷。这些测试预言需要数据库与查询生成器，而这些生成器必须考虑各系统 SQL 方言之间往往显著的差异。由于实现此类生成器可能需要数周时间，许多 DBMS 开发者不太可能投入时间去采用这类自动化测试方法。简而言之，现有方法无法扩展到数量众多的 DBMS。在本工作中，我们提出一个愿景和一个平台 SQLancer++，用于将测试预言应用于任何支持常见 SQL 特性子集的基于 SQL 的 DBMS。我们的核心技术贡献是一种自适应 SQL 语句生成器的新颖架构。该自适应 SQL 生成器生成带有各种特性的 SQL 语句，其中一些可能不被给定 DBMS 支持，然后通过与 DBMS 交互来学习其中哪些能被该 DBMS 理解。因此，随着时间推移，生成器将主要生成有效的 SQL 语句。我们在 18 个 DBMS 上评估了 SQLancer++，共发现 196 个此前未知的唯一缺陷，其中 180 个在我们报告之后得到修复。虽然 SQLancer++ 是朝着扩展自动化 DBMS 测试迈出的第一个重要步骤，但仍有各种后续挑战存在。

## 英文关键词

Database systems; automated testing; test case generation

## 中文关键词

数据库系统；自动化测试；测试用例生成

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790215)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7C](index.md) · [返回 ASPLOS 2026](../index.md)
