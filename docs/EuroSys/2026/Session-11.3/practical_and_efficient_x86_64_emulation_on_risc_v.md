---
title: "Practical and Efficient x86-64 Emulation on RISC-V"
description: "EuroSys 2026 · Virtualization, Containers & OS Specialization · Xiongchuan Tan (Tsinghua Shenzhen International Graduate School, Tsinghua Univer"
tags:
  - "EuroSys2026"
  - "Virtualization, Containers & OS Specialization"
---

# Practical and Efficient x86-64 Emulation on RISC-V

**中文标题：** 在 RISC-V 上实用且高效的 x86-64 模拟

**所属 Session：** [Session 11.3: Virtualization, Containers & OS Specialization](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Virtualization, Containers & OS Specialization。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Virtualization, Containers & OS Specialization</p>
</div>

**作者**：Xiongchuan Tan (Tsinghua Shenzhen International Graduate School, Tsinghua University), Yang Liu (Institute of Software, Chinese Academy of Sciences), Sebastien Chevalier (), Yangyu Chen (College of Computer Science, Chongqing University), Xiaoyi Liu (Department of Computer Science, Tsinghua University), Haohuan Fu (Tsinghua University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803574)

## 英文摘要

As RISC-V increasingly gains traction across various computing domains, the need to run x86-64 applications on RISC-V platforms becomes critical.

Binary translation plays a pivotal role in ensuring software portability across diverse Instruction Set Architectures (ISAs). However, the architectural differences between the widely adopted x86-64 and the emerging RISC-V platforms challenge effective translation while maintaining performance and compatibility. To address this challenge, we extend Box64 to enable efficient execution of x86-64 software on RISC-V systems. Our approach leverages a suite of both general and RISC-V-specific optimization techniques—including an innovative Total Store Ordering (TSO) emulation method, refined indirect and conditional branch optimizations, and dynamic library acceleration—to drastically reduce emulation overhead, improve execution efficiency, and maintain extensive application compatibility. Evaluations show that our solution only incurs an average performance penalty of less than 40% compared to native execution, outperforms QEMU-TCG by 3.3×, and robustly supports a wide range of applications from office suites to video games.

## 中文摘要

随着 RISC-V 在各个计算领域日益受到青睐，在 RISC-V 平台上运行 x86-64 应用的需求变得至关重要。

二进制翻译在确保软件跨多种指令集架构（ISA）的可移植性方面发挥着关键作用。然而，广泛使用的 x86-64 与新兴的 RISC-V 平台之间的架构差异，给在保持性能与兼容性的同时实现有效翻译带来了挑战。为应对这一挑战，我们扩展 Box64，以在 RISC-V 系统上高效执行 x86-64 软件。我们的方法利用了一整套通用与 RISC-V 特有的优化技术——包括创新的全存储顺序（TSO）模拟方法、改进的间接跳转与条件跳转优化，以及动态库加速——从而大幅降低模拟开销、提升执行效率，并保持广泛的应用兼容性。评测显示，我们的方案相比原生执行平均性能损失不到 40%，比 QEMU-TCG 快 3.3 倍，并稳健支持从办公套件到电子游戏在内的众多应用。

**英文关键词：** Dynamic Binary Translation, RISC-V, x86-64, Memory Consistency Models

**中文关键词：** 动态二进制翻译、RISC-V、x86-64、内存一致性模型

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
