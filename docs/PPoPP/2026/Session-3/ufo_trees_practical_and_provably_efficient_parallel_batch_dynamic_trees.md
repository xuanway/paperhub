---
title: "UFO Trees: Practical and Provably-Efficient Parallel Batch-Dynamic Trees"
description: "PPoPP 2026 Session 3（Concurrent Data Structures）：顺序媲美 link-cut 树，并行批更新工作高效，可扩十亿级"
tags:
  - "PPoPP2026"
  - "Session-3"
  - "Concurrent Data Structures"
  - "Batch-Dynamic Trees"
  - "Parallel Data Structures"
  - "Link-Cut Trees"
authors:
  - "Quinten De Man"
  - "Atharva Sharma"
  - "Kishen N Gowda"
  - "Laxman Dhulipala"
session: "Session 3: Concurrent Data Structures"
session_number: 3
session_chair: "Calin Cascaval"
date: "2026-02-02"
time: "14:10–14:30"
room: "Pyrmont"
doi: "10.1145/3774934.3786431"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
award: "Best Paper Nominee"
---

# UFO Trees: Practical and Provably-Efficient Parallel Batch-Dynamic Trees

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出并行批动态树数据结构 UFO 树，同时支持广泛查询功能与工作高效的并行批更新，顺序执行时与 link-cut 树相当，并可扩展到十亿级输入规模。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 3: Concurrent Data Structures</p>
</div>

**作者**：Quinten De Man, Atharva Sharma, Kishen N Gowda, and Laxman Dhulipala — University of Maryland, USA

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 14:10–14:30 · Session 3: Concurrent Data Structures（主席：Calin Cascaval）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786431) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

> 🏆 **Best Paper Nominee**

---

## 英文摘要

The dynamic trees problem is to maintain a tree under edge updates while supporting queries like connectivity queries or path queries. Despite the first data structure for this fundamental problem—the link-cut tree—being invented 40 years ago, our experiments reveal that they are still the fastest sequential data structure for the problem. However, link-cut trees cannot support parallel batch-dynamic updates and have limitations on the kinds of queries they support. In this paper, we design a new parallel batch-dynamic trees data structure called UFO trees that simultaneously supports a wide range of query functionality, supports work-efficient parallel batch-dynamic updates, and is competitive with link-cut trees when run sequentially. We prove that a key reason for the strong practical performance of both link-cut trees and UFO trees is that they can perform updates and queries in sub-logarithmic time for low-diameter trees. We perform an experimental study of our optimized C++ implementations of UFO trees with ten other dynamic tree implementations, several of which are new, in a broad benchmark of both synthetic and real-world trees of varying diameter and size. Our results show that, in both sequential and parallel settings, UFO trees are the fastest dynamic tree data structure that supports a wide range of queries. Our new implementation of UFO trees has low space usage and easily scales to billion-size inputs, making it a promising building block for implementing more complex dynamic graph algorithms in practice.

## 中文摘要

动态树问题是在进行边更新的同时维护一棵树，并支持诸如连通性查询或路径查询之类的查询。尽管针对这一基础问题的首个数据结构——link-cut 树——早在 40 年前就已被发明，但我们的实验表明，它至今仍是该问题上最快的串行数据结构。然而，link-cut 树无法支持并行批量动态更新，并且在其所支持的查询种类上存在局限。本文设计了一种新的并行批量动态树数据结构，称为 UFO 树，它同时支持广泛的查询功能、支持工作高效的并行批量动态更新，并且在串行运行时与 link-cut 树相比具有竞争力。我们证明了 link-cut 树与 UFO 树之所以都具有很强的实际性能，一个关键原因在于它们对低直径树能够在次对数时间内完成更新与查询。我们在涵盖不同直径与规模的合成树和真实世界树的广泛基准上，将我们优化的 C++ UFO 树实现与其他十种动态树实现（其中若干为新的实现）进行了实验研究。结果表明，在串行与并行两种情形下，UFO 树都是支持广泛查询功能的最快动态树数据结构。我们新的 UFO 树实现空间占用低，并易于扩展到十亿规模的输入，这使其成为在实践中实现更复杂动态图算法的有前景的构建模块。

## 英文关键词

dynamic trees, batch-dynamic trees

## 中文关键词

动态树；批量动态树

---

## 一句话总结

> 提出并行批动态树数据结构 UFO 树，同时支持广泛查询功能与工作高效的并行批更新，顺序执行时与 link-cut 树相当，并可扩展到十亿级输入规模。

## 研究问题

link-cut 树虽已提出四十年且仍是该问题最快的顺序数据结构，但无法支持并行批动态更新，所支持的查询种类也受限，缺少兼顾广泛查询与并行批更新的动态树。

## 方法简述

- 设计新的并行批动态树数据结构 UFO 树，同时支持广泛的动态树查询功能与工作高效的并行批更新。
- 论证 link-cut 树与 UFO 树在实际中表现优异的关键原因：对低直径树可在亚对数时间内完成更新与查询。
- 采用优化的 C++ 实现，与十种其他动态树实现（含若干新实现）在直径和规模各异的合成树与真实世界树上开展广泛基准测试。

## 主要结果

- 在顺序与并行两种设置下，UFO 树都是支持广泛查询功能的最快动态树数据结构。
- 新实现空间占用低，可轻松扩展到十亿规模的输入，有望成为实现更复杂动态图算法的构件。
- 实验同时表明，link-cut 树至今仍是该问题最快的顺序数据结构，而 UFO 树在顺序执行下具有与之竞争的实用性能。

---

> 所属 Session：[Session 3: Concurrent Data Structures](index.md) · 返回 [PPoPP 2026 总览](../index.md)
