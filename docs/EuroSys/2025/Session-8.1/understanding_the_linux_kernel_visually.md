---
title: "Understanding the Linux Kernel, Visually"
description: "EuroSys 2025 · Bug finding · Hanzhi Liu (Nanjing University), Yanyan Jiang (Nanjing University), Chang Xu (Na"
tags:
  - "EuroSys2025"
  - "Bug finding"
---

# Understanding the Linux Kernel, Visually

**中文标题：** 可视化理解 Linux 内核

**所属 Session：** [Session 8.1: Bug finding](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Bug finding。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Bug finding</p>
</div>

**作者**：Hanzhi Liu (Nanjing University), Yanyan Jiang (Nanjing University), Chang Xu (Nanjing University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696095)

**获奖：** 最佳学生论文（春季投稿）（[官方获奖名单](https://2025.eurosys.org/awards.html)）

## 英文摘要

Understanding the Linux kernel is challenging due to its large and complex program state. While existing kernel debugging tools provide full access to kernel states at arbitrary levels of detail, developers often spend a significant amount of time sifting through redundant information to find what is truly useful. Additionally, the textual results provided by traditional debuggers are often insufficient for expressing high-dimensional information in a readable manner.

This paper presents Visualinux, the first debugging framework that can simplify the program state of the Linux kernel to a level that can be visually understood with low programming complexity and effort. Visualinux includes a domain-specific language for specifying simplifications of a kernel object graph, an SQL-like domain-specific language for customizing the simplified object graph, and a panel-based interactive debugger. Evaluation results show that Visualinux can visualize various complex kernel components and efficiently assist developers in diagnosing sophisticated kernel bugs.

## 中文摘要

理解 Linux 内核颇具挑战，因为其程序状态庞大而复杂。虽然现有内核调试工具能以任意细节层次完全访问内核状态，但开发者常常花费大量时间在冗余信息中筛选真正有用的内容。此外，传统调试器提供的文本结果往往不足以可读地表达高维信息。

本文提出 Visualinux，首个能够以低编程复杂度和工作量将 Linux 内核程序状态简化到可被可视化理解程度的调试框架。Visualinux 包含一种用于指定内核对象图简化的领域特定语言、一种用于定制简化后对象图的类 SQL 领域特定语言，以及一个基于面板的交互式调试器。评估结果表明，Visualinux 能够可视化各种复杂的内核组件，并高效地辅助开发者诊断复杂的内核缺陷。

**英文关键词：** Linux Kernel, Software Visualization, Debugging

**中文关键词：** Linux 内核、软件可视化、调试

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
