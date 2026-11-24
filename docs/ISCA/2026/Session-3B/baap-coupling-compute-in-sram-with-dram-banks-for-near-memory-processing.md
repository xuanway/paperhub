---
title: "BAAP: Coupling Compute-in-SRAM with DRAM Banks for Near-Memory Processing"
description: "ISCA 2026 · Session 3B · BAAP: Coupling Compute-in-SRAM with DRAM Banks for Near-Memory Processing"
tags:
  - "ISCA2026"
  - "Session 3B"
  - "DRAM and SRAM PIM/PNM"
---

# BAAP: Coupling Compute-in-SRAM with DRAM Banks for Near-Memory Processing

**中文标题：** BAAP: 将 SRAM 内计算与 DRAM bank 耦合的近内存处理

**所属 Session：** [Session 3B](index.md) · [ISCA 2026](../index.md)

**作者：** Cecilio C. Tamarit, Socrates S. Wong, Akshati Vaishnav, José F. Martínez

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Near-DRAM-bank logic is a form of processing-in-memory (PIM) that lowers access latency and exploits bank-level parallelism to achieve increased throughput. Major classes of memory-bound applications, including pattern matching, vector processing, and graph algorithms, stand to benefit from adding processing capabilities at the bank level. While custom bank-level PIM solutions exist for individual domains, a performant programmable solution that is able to tackle all three remains elusive, as DRAM technology imposes limitations on the complexity and scale of computing logic that can be integrated. Recently, a number of commercial in-DRAM PIM products feature small SRAM-based scratchpads that bridge the last gap between on-die compute logic and DRAM storage. In this paper, we examine the potential and synergies of augmenting such scratchpads with Compute-in-SRAM support. Our Bank-Adjacent Associative Processor (BAAP) repurposes part of the scratchpad to provide additional in situ computing capabilities that are complementary to the existing PIM logic, primarily acting as either a SIMD unit or pattern-matching engine. We employ the commercially available UPMEM PIM architecture as a realistic foundation, although we believe that our insights are also relevant to other scratchpad-augmented PIM designs. We evaluate BAAP using system-level, cycle-approximate, execution-driven simulations, comparing it against detailed models of commercial bank-level designs and other academic proposals, including a host-side associative processor that is also SRAM-based. Our results demonstrate that BAAP can deliver performance improvements of more than an order of magnitude across diverse workloads, including computational genomics, and the Phoenix and PrIM benchmarks.

## 中文摘要

近DRAM bank逻辑是一种处理中内存（PIM）形式，可降低访问延迟并利用bank级并行性来提高吞吐量。主要的内存受限应用类别，包括模式匹配、向量处理和图算法，都可以从在bank级添加处理能力中受益。虽然针对各个领域存在定制化的bank级PIM解决方案，但能够同时处理所有三类工作负载的高性能可编程解决方案仍然难以实现，因为DRAM技术对可集成的计算逻辑的复杂性和规模施加了限制。最近，一些商用DRAM内PIM产品配备了基于SRAM的小型暂存器，弥合了片内计算逻辑与DRAM存储之间的最后差距。在本文中，我们研究了用计算SRAM支持增强此类暂存器的潜力和协同效应。我们的bank邻近关联处理器（BAAP）重新利用部分暂存器来提供额外的原位计算能力，作为现有PIM逻辑的补充，主要充当SIMD单元或模式匹配引擎。我们将商用的UPMEM PIM架构作为现实基础，尽管我们相信我们的见解也适用于其他暂存器增强型PIM设计。我们使用系统级、周期近似、执行驱动的仿真来评估BAAP，并将其与商用bank级设计的详细模型以及其他学术方案（包括同样基于SRAM的主机侧关联处理器）进行比较。我们的结果表明，BAAP可以在多样化的工作负载（包括计算基因组学以及Phoenix和PrIM基准测试）中提供超过一个数量级的性能提升。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3B](index.md) · [返回 ISCA 2026](../index.md)
