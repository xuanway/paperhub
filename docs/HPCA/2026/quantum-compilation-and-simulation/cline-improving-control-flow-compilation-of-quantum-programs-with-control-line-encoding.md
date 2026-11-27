---
title: "CLINE: Improving Control Flow Compilation of Quantum Programs with Control Line Encoding"
description: "HPCA 2026 · Quantum Compilation and Simulation"
tags:
  - "HPCA2026"
  - "Quantum Compilation and Simulation"
---

# CLINE: Improving Control Flow Compilation of Quantum Programs with Control Line Encoding

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Quantum Compilation and Simulation。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Quantum Compilation and Simulation</p>
</div>

**论文链接**：
**作者**：Anbang Wu Shanghai Jiao Tong University , Liqiang Lu Zhejiang University , Jianwei Yin Zhejiang University , Jingwen Leng Shanghai Jiao Tong University , Minyi Guo Shanghai Jiao Tong University
**会议**：HPCA 2026

---

## 中文标题

CLINE：以控制线编码改进量子程序的控制流编译

## 英文摘要

Important applications like quantum search and quantum simulation rely on control flow implemented by oracle circuits, which may account for up to 99% of the total gate count [1] as oracle circuits consist of expensive multi-controlled (MC) quantum operations that formulate the control flow. Existing efforts optimize them by simplifying Boolean expressions associated with MC gates. They merge MC gates, if associated Boolean expressions are adjacent, to reduce the gate cost. Being more aggressive, our work introduces control line encoding (CLE), a technique that even allows merging non-adjacent MC gates by modifying their control (line) polarity. We further develop a plug-in compiler framework that efficiently applies this technique. The framework is grounded in the following observations: 1) Control flows often commute with one another and can be globally reorganized to maximize their merging by CLE; 2) numerous CLE schemes exist to allow gate merge and we can co-design CLE applications to diminish the overhead of CLE itself. Experiments demonstrate that, compared to the baseline, our framework further reduces the CX and T cost, on average by 54.7% and 56.8%, respectively.

## 中文摘要

量子搜索与量子模拟等重要应用依赖由 oracle 线路实现的控制流，由于 oracle 线路由构造控制流的高开销多控（MC）量子操作组成，其门数可占总门数的 99% 以上[1]。已有工作通过化简 MC 门关联的布尔表达式来优化：当布尔表达式相邻时合并 MC 门以降低门开销。我们的工作更为激进，提出控制线编码（CLE），通过修改控制（线）极性，甚至可以合并不相邻的 MC 门。我们进一步开发了插件式编译框架以高效应用该技术。该框架基于以下观察：1) 控制流之间往往可交换，可全局重排以借助 CLE 最大化合并；2) 存在多种可合并门的 CLE 方案，我们可以协同设计 CLE 的应用以削减 CLE 自身开销。实验表明，与基线相比，我们的框架将 CX 与 T 的代价分别平均降低 54.7% 与 56.8%。
