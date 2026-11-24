---
title: "LOONG: Utilizing Long-Stride Reprogramming to Enhance the Performance of SSDs"
description: "ISCA 2026 · Session 2D · LOONG: Utilizing Long-Stride Reprogramming to Enhance the Performance of SSDs"
tags:
  - "ISCA2026"
  - "Session 2D"
  - "Storage"
---

# LOONG: Utilizing Long-Stride Reprogramming to Enhance the Performance of SSDs

**中文标题：** LOONG: 利用长步长重编程提升 SSD 性能

**所属 Session：** [Session 2D](index.md) · [ISCA 2026](../index.md)

**作者：** Congming Gao, Jiancong Zheng, Xufeng Yang, Qiao Li, Jian Chen, Tianyu Ren, Zheng Wan, Yina Lv, Xin Xin, Min Ye, Chun Jason Xue, Jiwu Shu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

NAND flash-based SSDs enforce strict sequential page programming within blocks, primarily due to reliability constraints. However, enabling reprogramming of pages after initial writes could unlock significant optimization opportunities, such as accelerating valid page movement during garbage collection or program operations. Toward this objective, prior work has explored reprogramming. Nevertheless, its effort faces a critical limitation: reprogramming is restricted to a small subset of wordlines per block (i.e., stride), rather than extending to all WLs per block. In this work, we advance beyond this constraint with LOONG, a method that expands the reprogramming stride to encompass entire blocks. LOONG introduces a long-stride reprogram operation, which spatially decouples programming steps. First, all WLs in a block undergo sequential programming in SLC mode to maximize performance. These pages are then uniformly reprogrammed to TLC mode, preserving storage capacity. LOONG requires no hardware modifications and can be deployed solely via firmware updates. We evaluate LOONG’s efficiency with two case studies: GC acceleration and program operation optimization. Experimental results demonstrate average latency is reduced by 37.5% and 18.1%, respectively, in these two scenarios.

## 中文摘要

基于 NAND 闪存的 SSD 主要出于可靠性约束，强制要求块内严格按顺序进行页编程。然而，若能在初次写入之后对页进行重编程，就能解锁诸多重要的优化机会，例如加速垃圾回收或编程操作过程中的有效页迁移。为实现这一目标，已有工作对重编程进行了探索。然而，其努力面临一个关键限制：重编程仅限于块内一小部分字线（即 stride），而无法扩展到块内的所有 WL。在本工作中，我们以 LOONG 超越了这一限制，该方法将重编程步长扩展到覆盖整个块。LOONG 引入了一种长步长重编程操作，在空间上将编程步骤解耦。首先，块内所有 WL 以 SLC 模式进行顺序编程，以最大化性能。随后这些页被统一重编程为 TLC 模式，从而保持存储容量。LOONG 无需任何硬件修改，仅通过固件更新即可部署。我们通过两个案例研究评估 LOONG 的效率：GC 加速与编程操作优化。实验结果表明，在这两种场景下平均延迟分别降低了 37.5% 和 18.1%。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 2D](index.md) · [返回 ISCA 2026](../index.md)
