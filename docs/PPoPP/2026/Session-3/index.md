---
title: "Session 3: Concurrent Data Structures"
description: "PPoPP 2026 Session 3（Concurrent Data Structures），2026 年 2 月 2 日 14:10–15:30，Pyrmont，共 4 篇论文。"
tags:
  - "PPoPP2026"
  - "Session-3"
  - "Concurrent Data Structures"
---

# Session 3: Concurrent Data Structures

**PPoPP 2026 · 2026 年 2 月 2 日 14:10–15:30 · Pyrmont · Session Chair：Calin Cascaval**

围绕并发数据结构：可证明高效的并行批动态树、分片消除与合并的并发栈、首个无锁增强平衡树，以及并行动态空间索引。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2026 Main Conference Papers](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [🏆 UFO Trees: Practical and Provably-Efficient Parallel Batch-Dynamic Trees](ufo_trees_practical_and_provably_efficient_parallel_batch_dynamic_trees.md) | Quinten De Man 等 4 人 | 顺序媲美 link-cut 树，并行批更新工作高效，可扩十亿级 |
| 2 | [Sharded Elimination and Combining for Highly-Efficient Concurrent Stacks](sharded_elimination_and_combining_for_highly_efficient_concurrent_stacks.md) | Ajay Singh 等 3 人 | 分片+消除+合并，多线程高竞争下最高快 2× |
| 3 | [Concurrent Balanced Augmented Trees](concurrent_balanced_augmented_trees.md) | Evan Wrench 等 7 人 | 首个通用增强无锁平衡树，更新快 2.2–30× |
| 4 | [Parallel Dynamic Spatial Indexes](parallel_dynamic_spatial_indexes.md) | Ziyang Men 等 4 人 | P-Orth 与 SPaC-tree：批量更新胜过并行 kd/Orth 树 |

### 获奖

- **UFO Trees: Practical and Provably-Efficient Parallel Batch-Dynamic Trees** —— Best Paper Nominee

---

[← Session 2: Scheduling and Load Balancing](../Session-2/index.md) · [PPoPP 2026 总览](../index.md) · [Session 4: GPU and Heterogeneous Computing →](../Session-4/index.md)
