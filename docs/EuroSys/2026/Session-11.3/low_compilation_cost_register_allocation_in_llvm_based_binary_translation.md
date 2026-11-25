---
title: "Low-Compilation-Cost Register Allocation in LLVM-Based Binary Translation"
description: "EuroSys 2026 · Virtualization, Containers & OS Specialization · Xiangwei Meng (Lanzhou University), Chen Gao (Lanzhou University), Wei Li (Tsing"
tags:
  - "EuroSys2026"
  - "Virtualization, Containers & OS Specialization"
---

# Low-Compilation-Cost Register Allocation in LLVM-Based Binary Translation

**中文标题：** 基于 LLVM 的二进制翻译中低编译开销的寄存器分配

**所属 Session：** [Session 11.3: Virtualization, Containers & OS Specialization](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Virtualization, Containers & OS Specialization。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Virtualization, Containers & OS Specialization</p>
</div>

**作者**：Xiangwei Meng (Lanzhou University), Chen Gao (Lanzhou University), Wei Li (Tsinghua University), Fengyuan Ren (Lanzhou University / Tsinghua University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803591)

## 英文摘要

Efficiently allocating guest architecture registers to host registers is a crucial technique for improving performance in dynamic binary translation. Translators typically enlarge code regions to reduce context-switching overhead and expose more optimization opportunities. Traditional approaches load guest registers upon entering a code region and save them upon exiting, aiming to retain guest registers in host registers for as long as possible. However, as the size of code region increases, the growing number of intermediate variables and the increasing complexity of control flow lead to higher computational costs for register allocation, thereby increasing compilation overhead.

This paper investigates the causes of increased register allocation overhead in LLVM-based binary translators and proposes a low-compilation-cost strategy called LCCRA. It explicitly restores the semantics of accessing physical guest registers in LLVM IR, facilitating efficient register allocation on mainstream processor architectures. LCCRA propagates guest register values using virtual registers within each basic block. For values that need to cross basic block boundaries, virtual registers are introduced as substitutes for load operations where necessary, and redundant store operations are eliminated based on control flow analysis. Since this optimization is performed at the LLVM IR level, it does not interfere with existing LLVM optimizations, making it applicable to various LLVM-based binary translators.

We implement our strategy in CrossDBT, an LLVM-based binary translator. Evaluation on PARSEC benchmark suite, considering varying code region sizes across two translation scenarios (x86-64 →x86-64 and x86-64 →AArch64), demonstrates that LCCRA achieves a 5.76%-7.79% reduction in end-to-end latency and a 69.55%-74.98% reduction in register allocation time when host registers are limited. In register-abundant scenarios, LCCRA still delivers slightly better end-to-end latency while consistently reducing compilation overhead.

## 中文摘要

在动态二进制翻译中，将客户机体系结构寄存器高效分配到宿主机寄存器是提升性能的关键技术。翻译器通常扩大代码区域，以降低上下文切换开销并暴露更多优化机会。传统方法在进入代码区域时加载客户机寄存器、在退出时保存它们，力求尽可能长时间地将客户机寄存器保留在宿主机寄存器中。然而，随着代码区域规模增大，中间变量数量不断增加、控制流复杂度持续上升，导致寄存器分配的计算开销增大，进而提高编译开销。

本文研究了基于 LLVM 的二进制翻译器中寄存器分配开销上升的原因，并提出一种低编译开销策略 LCCRA。该策略在 LLVM IR 中显式恢复访问物理客户机寄存器的语义，从而便于在主流处理器架构上高效进行寄存器分配。LCCRA 在每个基本块内使用虚拟寄存器传播客户机寄存器值。对于需要跨越基本块边界的值，在必要时引入虚拟寄存器替代加载操作，并基于控制流分析消除冗余的存储操作。由于该优化在 LLVM IR 层面完成，不会干扰 LLVM 现有的优化，因此适用于各类基于 LLVM 的二进制翻译器。

我们将该策略实现在 CrossDBT——一个基于 LLVM 的二进制翻译器中。在 PARSEC 基准测试集上的评估（考虑两种翻译场景 x86-64 → x86-64 与 x86-64 → AArch64 下不同的代码区域大小）表明，在宿主机寄存器受限时，LCCRA 使端到端延迟降低 5.76%–7.79%，寄存器分配时间减少 69.55%–74.98%。在寄存器充裕的场景下，LCCRA 仍能带来略优的端到端延迟，并持续降低编译开销。

**英文关键词：** Binary Translation, LLVM, Register Allocation

**中文关键词：** 二进制翻译、LLVM、寄存器分配

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
