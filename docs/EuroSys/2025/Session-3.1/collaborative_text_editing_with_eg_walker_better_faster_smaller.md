---
title: "Collaborative Text Editing with Eg-walker: Better, Faster, Smaller"
description: "EuroSys 2025 · Distributed Systems · Joseph Gentle (Independent), Martin Kleppmann (University of Cambridge)"
tags:
  - "EuroSys2025"
  - "Distributed Systems"
---

# Collaborative Text Editing with Eg-walker: Better, Faster, Smaller

**中文标题：** 使用 Eg-walker 协同编辑文本：更好、更快、更小

**所属 Session：** [Session 3.1: Distributed Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Distributed Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Distributed Systems</p>
</div>

**作者**：Joseph Gentle (Independent), Martin Kleppmann (University of Cambridge)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696076)

**获奖：** Gilles Muller 最佳研究制品（[官方获奖名单](https://2025.eurosys.org/awards.html)）

## 英文摘要

Collaborative text editing algorithms allow several users to concurrently modify a text file, and automatically merge concurrent edits into a consistent state. Existing algorithms fall in two categories: Operational Transformation (OT) algorithms are slow to merge files that have diverged substantially due to offline editing; CRDTs are slow to load and consume a lot of memory. We introduce Eg-walker, a collaboration algorithm for text that avoids these weaknesses. Compared to existing CRDTs, it consumes an order of magnitude less memory in the steady state, and loading a document from disk is orders of magnitude faster. Compared to OT, merging long-running branches is orders of magnitude faster. In the worst case, the merging performance of Eg-walker is comparable with existing CRDT algorithms. Eg-walker can be used everywhere CRDTs are used, including peer-to-peer systems without a central server. By offering performance that is competitive with centralised algorithms, our result paves the way towards the widespread adoption of peer-to-peer collaboration software.

## 中文摘要

协同文本编辑算法允许多个用户并发修改一个文本文件，并自动将并发编辑合并为一致状态。现有算法分为两类：操作转换（OT）算法在因离线编辑而产生显著分歧的文件上合并缓慢；CRDT 加载缓慢且占用大量内存。我们提出 Eg-walker，一种避免这些弱点的文本协同算法。与现有 CRDT 相比，它在稳态下消耗的内存少一个数量级，从磁盘加载文档快数个数量级。与 OT 相比，合并长期运行的分支快数个数量级。在最坏情况下，Eg-walker 的合并性能与现有 CRDT 算法相当。Eg-walker 可用于任何使用 CRDT 的场合，包括无中心服务器的点对点系统。通过提供与集中式算法相当的竞争性性能，我们的结果为推动点对点协作软件的广泛采用铺平了道路。

**英文关键词：** collaborative text editing, CRDTs, operational transformation, strong eventual consistency

**中文关键词：** 协同文本编辑、CRDT、操作转换、强最终一致性

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
