---
title: "Practical Prefetching of a MAC Scheduler on ARM Neoverse"
description: "MICRO 2026 · Session 1C · ARM Neoverse 上 MAC 调度器的实用预取技术"
tags:
  - "MICRO2026"
  - "Prefetching"
---

# Practical Prefetching of a MAC Scheduler on ARM Neoverse

**中文标题：** ARM Neoverse 上 MAC 调度器的实用预取技术

**所属 Session：** [Session 1C](index.md) · [MICRO 2026](../index.md)

**作者：** Jonathan Ling, Paul Cautereels, Dragan Smardzija, Damien Phan, Christope Pavageau, Morgan Cormier, Pierre Delbreil, Henry Wiechert, Krister Wikstrom

**来源：** MICRO 2026，pp. 315–325；[DOI](https://doi.org/10.1109/MICRO67795.2026.00037)

## 英文摘要

Software instruction prefetching of a 5G Medium Access Control (MAC) layer scheduler that has real-time requirements is evaluated. The hardware platform is a Marvell Octeon, a networking system-on-chip with ARM Neoverse N2 CPU cores. Due to complexity and the large code base exceeding the L2 cache size, the CPU is 50% front-end stalled. Experimental results demonstrate significant gains when prefetching from L3 cache to L2 cache. For example, a code section with 2000 cache lines can see a reduction of 12µS when prefetched, yielding a net gain of 6.7µS after accounting for overhead (approximately 50% of the base gain). IPC increased from 1.4 to 1.8, a 28% improvement. Furthermore, profile-guided optimization (PGO) mitigates front-end stalls by reducing long jumps and branches. Experiments indicate complementary gains. Interspersing prefetch statements strategically within the code to effect background prefetching, removing the prefetching overhead, is proposed as a practical next step.

## 中文摘要

对具有实时要求的 5G 媒体访问控制 (MAC) 层调度器的软件指令预取进行了评估。硬件平台是 Marvell Octeon，一种带有 ARM Neoverse N2 CPU 内核的网络片上系统。由于复杂性和超过二级缓存大小的大型代码库，CPU 50% 前端停滞。实验结果表明，从 L3 缓存预取到 L2 缓存时效果显着。例如，具有 2000 个缓存行的代码段在预取时可以减少 12μS，在考虑开销（大约为基本增益的 50%）后产生 6.7μS 的净增益。 IPC 从 1.4 增加到 1.8，提高了 28%。此外，配置文件引导优化 (PGO) 通过减少长跳转和分支来缓解前端停顿。实验表明互补收益。建议将预取语句战略性地散布在代码中以实现后台预取，消除预取开销，作为下一步的实际步骤。

## 中文关键词

指令预取；实时嵌入式软件；介质访问控制调度器；ARM Neoverse

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1C](index.md) · [MICRO 2026 主页](../index.md)
