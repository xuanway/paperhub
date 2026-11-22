---
title: "Non-Speculative Redundant Load Elimination"
description: "MICRO 2026 · Session 3A · 非推测式冗余加载消除"
tags:
  - "MICRO2026"
---

# Non-Speculative Redundant Load Elimination

**中文标题：** 非推测式冗余加载消除

**所属 Session：** [Session 3A](index.md) · [MICRO 2026](../index.md)

**作者：** Minchan Kim, Ho Je Lee, Jaewon Kwon, Mingu Jung, Ipoom Jeong, Won Woo Ro

**来源：** MICRO 2026，pp. 944–959；[DOI](https://doi.org/10.1109/MICRO67795.2026.00076)

## 英文摘要

Modern programs exhibit abundant memory-value reuse, which provides an opportunity to eliminate redundant loads through physical register sharing. However, current hardware fails to fully exploit this opportunity due to unknown redundancy and the limited physical register lifetime. Since load redundancy remains unknown at rename, early execution of redundant loads necessitates prediction, which fundamentally limits its coverage to a subset of redundant loads. Furthermore, the limited lifetime of physical registers restricts the reusable window of a memory value and thus constrains the potential of redundant load elimination. We observe that late allocation, which delays physical register allocation until writeback, provides the two capabilities required to unlock the potential of redundant load elimination. Based on this observation, we propose Möbius, which judiciously leverages late allocation to non-speculatively eliminate a broader set of redundant loads beyond the limits of current hardware. First, by delaying physical register allocation until after address generation, Möbius non-speculatively eliminates redundant loads without predicting load redundancy. Second, Möbius utilizes the additional PRF capacity provided by late allocation to retain memory values longer in the PRF and thereby capture redundant loads across longer reuse distances. Across 43 workloads, Möbius improves performance by 9.04% on average over the baseline while eliminating 56.6% of data fetch operations. Owing to its broader elimination coverage, Möbius outperforms prior frontend load bypass/elimination techniques, SMB and Constable, which improve performance by 3.07% and 4.85%, respectively.

## 中文摘要

现代程序表现出丰富的内存值重用，这提供了通过物理寄存器共享消除冗余负载的机会。然而，由于未知的冗余和有限的物理寄存器寿命，当前的硬件未能充分利用这个机会。由于重命名时负载冗余仍然未知，因此冗余负载的早期执行需要进行预测，这从根本上将其覆盖范围限制为冗余负载的子集。此外，物理寄存器的有限寿命限制了存储器值的可重用窗口，从而限制了冗余负载消除的潜力。我们观察到，时延分配（将物理寄存器分配时延到回写）提供了释放冗余负载消除潜力所需的两种功能。基于这一观察，我们提出了莫比乌斯，它明智地利用后期分配来非推测性地消除超出当前硬件限制的更广泛的冗余负载。首先，通过将物理寄存器分配时延到地址生成之后，莫比乌斯非推测性地消除了冗余负载，而无需预测负载冗余。其次，莫比乌斯利用后期分配提供的额外 PRF 容量，将内存值保留在 PRF 中更长时间，从而在更长的重用距离上捕获冗余负载。在 43 个工作负载中，Möbius 的性能比基准平均提高了 9.04%，同时消除了 56.6% 的数据获取操作。由于其更广泛的消除覆盖范围，Möbius 优于之前的前端负载旁路/消除技术、SMB 和 Constable，性能分别提高了 3.07% 和 4.85%。

## 中文关键词

冗余加载消除；乱序处理器；指令级并行性；寄存器重命名；物理寄存器文件

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3A](index.md) · [MICRO 2026 主页](../index.md)
