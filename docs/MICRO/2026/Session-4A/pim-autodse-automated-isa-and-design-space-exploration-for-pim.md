---
title: "PIM-AUTODSE: Automated ISA and Design Space Exploration for PIM"
description: "MICRO 2026 · Session 4A · PIM-AUTODSE：面向存内处理的自动化指令集与设计空间探索"
tags:
  - "MICRO2026"
  - "Processing-in-Memory"
---

# PIM-AUTODSE: Automated ISA and Design Space Exploration for PIM

**中文标题：** PIM-AUTODSE：面向存内处理的自动化指令集与设计空间探索

**所属 Session：** [Session 4A](index.md) · [MICRO 2026](../index.md)

**作者：** Abdul Rafae Noor, Farzana Ahmed Siddique, Akash Kothari, Deyuan Guo, Kevin Skadron, Vikram Adve

**来源：** MICRO 2026，pp. 1349–1364；[DOI](https://doi.org/10.1109/MICRO67795.2026.00101)

## 英文摘要

Processing-in-memory (PIM) offers a promising solution to the memory wall, but the Instruction Set Architecture (ISA) of PIM has never been systematically evaluated. PIM ISA choices — such as instruction fusion — directly affect DRAM read/write operations: an unfused instruction spills its intermediate result back to the DRAM array, and each spill costs an ACTIVATE/PRECHARGE pair that inflates application runtime and energy. We present PIM-AUTODSE, a retargetable framework that extends PIMeval, a PIM simulator, to provide cycle-accurate performance and energy analysis supporting features including instruction fusion, register contention, and prefetching. PIM-AUTODSE further extends the synthesis-based compiler MISAAL to provide code generation from high-level languages to diverse PIM architectures, and proposes a methodology for PIM ISA synthesis from pseudocode to automatically generate RISC- and CISC-like ISAs. Using PIM-AUTODSE, we conduct the first systematic study of instruction fusion for PIM, demonstrating up to 3.3x improvement in execution runtime and 2.7x in energy (1.46x and 1.79x geomean) over non-fused baselines across nine workloads and five PIM variants. Our analysis identifies three dimensions by which ISA selection reduces cost without new functional units: fusing operations to eliminate redundant intermediate spills, prioritizing instruction variants that replace host-side accumulation with SIMD add to avoid host-PIM data movement, and selecting scalar-operand instruction variants when operands are constants to avoid unnecessary DRAM Column Select — establishing that effective PIM ISA design must jointly account for intra-row data movement, system-level host interaction, and operand encoding when selecting instructions. PIM-AUTODSE is publicly available at https://github.com/UVA-LavaLab/PIM-AutoDSE.

## 中文摘要

存内处理（PIM）为内存墙提供了一种有前途的解决方案，但 PIM 的指令集架构（ISA）从未得到系统评估。 PIM ISA 选择（例如指令融合）直接影响 DRAM 读/写操作：未融合的指令将其中间结果溢出回 DRAM 阵列，每次溢出都会花费一个 ACTIVATE/PRECHARGE 对，从而增加应用程序运行时间和能源。我们推出 PIM-AUTODSE，这是一个可重定向框架，它扩展了 PIMeval（PIM 模拟器），以提供周期精确的性能和能量分析支持功能，包括指令融合、寄存器争用和预取。 PIM-AUTODSE 进一步扩展了基于综合的编译器 MISAAL，以提供从高级语言到不同 PIM 架构的代码生成，并提出了一种从伪代码进行 PIM ISA 综合的方法，以自动生成类似 RISC 和 CISC 的 ISA。使用 PIM-AUTODSE，我们对 PIM 指令融合进行了首次系统研究，结果表明，与非融合基线相比，在 9 个工作负载和 5 个 PIM 变体中，运行时间最低降至基线的 1/3.3，能耗最低降至基线的 1/2.7（相应改善倍数的几何平均值分别为 1.46 和 1.79）。我们的分析确定了 ISA 选择在没有新功能单元的情况下降低成本的三个维度：融合操作以消除冗余的中间溢出，优先考虑用 SIMD add 代替主机端累加的指令变体以避免主机 PIM 数据移动，以及在操作数为常量时选择标量操作数指令变体以避免不必要的 DRAM 列选择 - 建立有效的 PIM ISA 设计必须在选择指令时共同考虑行内数据移动、系统级主机交互和操作数编码。 PIM-AUTODSE 可在 https://github.com/UVA-LavaLab/PIM-AutoDSE 上公开获取。

## 中文关键词

设计空间探索；存内处理；编译器构建；指令融合；指令集架构设计；仿真

## 代码与研究制品

- 代码仓库：[https://github.com/UVA-LavaLab/PIM-AutoDSE](https://github.com/UVA-LavaLab/PIM-AutoDSE)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 4A](index.md) · [MICRO 2026 主页](../index.md)
