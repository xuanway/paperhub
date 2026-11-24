---
title: "Understanding and Detecting SQL Function Bugs: Using Simple Boundary Arguments to Trigger Hundreds of DBMS Bugs"
description: "EuroSys 2025 · Bug finding · Jingzhou Fu (Tsinghua University), Jie Liang (Tsinghua University), Zhiyong Wu ("
tags:
  - "EuroSys2025"
  - "Bug finding"
---

# Understanding and Detecting SQL Function Bugs: Using Simple Boundary Arguments to Trigger Hundreds of DBMS Bugs

**中文标题：** 理解和检测 SQL 函数缺陷：使用简单边界参数触发数百个数据库管理系统缺陷

**所属 Session：** [Session 8.1: Bug finding](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Bug finding。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Bug finding</p>
</div>

**作者**：Jingzhou Fu (Tsinghua University), Jie Liang (Tsinghua University), Zhiyong Wu (Tsinghua University), Yanyang Zhao (Tsinghua University), Shanshan Li (National University of Defense Technology), Yu Jiang (Tsinghua University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696064)

## 英文摘要

Built-in SQL functions are crucial in Database Management Systems (DBMSs), supporting various operations and computations across multiple data types. They are essential for querying, data transformation, and aggregation. Despite their importance, the bugs in SQL functions have caused widespread problems in the real world, from system failures to arbitrary code execution. However, the understanding of the bug characteristics is limited. More importantly, conventional function testing methods struggle to generate semantically correct SQL test cases, while DBMS testing efforts are hard to measure built-in SQL functions.

This paper presents a comprehensive study of 318 built-in SQL function bugs, shedding light on their characteristics and root causes. Our investigation reveals that 87.4% of these bugs were caused by improper handling of boundary values of arguments. The boundary values of arguments come from three sources: literal values, type castings, and nested functions. By studying the bugs from three sources, we summarized 10 SQL patterns of bug-inducing queries. Moreover, we designed Soft, a testing tool based on the patterns to test seven widely used DBMSs, including PostgreSQL, MySQL, and ClickHouse. Soft discovered and confirmed 132 previously unknown SQL function bugs. The DBMS vendors took these bugs seriously and fixed 97 bugs in three days. For example, the CTO of ClickHouse commented on one bug: “We must fix it immediately or get rid of this function.”

## 中文摘要

内置 SQL 函数在数据库管理系统（DBMS）中至关重要，支持跨多种数据类型的各类操作与计算。它们对于查询、数据转换和聚合不可或缺。尽管十分重要，SQL 函数中的缺陷却在现实世界中造成了广泛问题，从系统故障到任意代码执行。然而，人们对这些缺陷特征的理解仍然有限。更重要的是，传统的函数测试方法难以生成语义正确的 SQL 测试用例，而 DBMS 测试工作也难以度量内置 SQL 函数。

本文对 318 个内置 SQL 函数缺陷进行了全面研究，揭示了其特征与根本原因。我们的调查发现，其中 87.4% 的缺陷由对参数边界值处理不当引起。参数的边界值来自三种来源：字面量、类型转换和嵌套函数。通过研究来自这三种来源的缺陷，我们总结了 10 种可诱发缺陷的查询 SQL 模式。此外，我们设计了 Soft，一个基于这些模式的测试工具，用于测试包括 PostgreSQL、MySQL 和 ClickHouse 在内的七种广泛使用的 DBMS。Soft 发现并确认了 132 个此前未知的 SQL 函数缺陷。各 DBMS 厂商认真对待这些缺陷，在三天内修复了 97 个。例如，ClickHouse 的 CTO 就其中一个缺陷评论道：“我们必须立即修复它，否则就去掉这个函数。”

**英文关键词：** DBMS, SQL Function, Vulnerability Detection

**中文关键词：** DBMS、SQL 函数、漏洞检测

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
