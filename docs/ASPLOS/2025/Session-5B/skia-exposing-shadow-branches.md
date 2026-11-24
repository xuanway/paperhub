---
title: "Skia: Exposing Shadow Branches"
description: "ASPLOS 2025 · Session 5B · Skia：暴露影子分支"
tags:
  - "ASPLOS2025"
  - "Session 5B"
  - "Microarchitecture"
---

# Skia: Exposing Shadow Branches

**中文标题：** Skia：暴露影子分支

**所属 Session：** [Session 5B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Chrysanthos Pepi (Texas A&M University,Intel), Bhargav Reddy Godala (Princeton University,Intel), Krishnam Tibrewala (Texas A&M University), Gino A. Chacon (Intel,AheadComputing), Paul V. Gratz (Texas A&M University), Daniel A. Jiménez (Texas A&M University,Barcelona Supercomputing Center), Gilles A. Pokam (Intel), David I. August (Princeton University)

**单位：** Texas A&M University,Intel；Princeton University,Intel；Texas A&M University；Intel,AheadComputing；Texas A&M University,Barcelona Supercomputing Center；Intel；Princeton University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716273) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Modern processors implement a decoupled front-end, often using a form of Fetch Directed Instruction Prefetching (FDIP), to avoid front-end stalls. FDIP is driven by the Branch Prediction Unit (BPU), relying on the BPU's accuracy and branch target tracking structures to speculatively fetch instructions into the Instruction Cache (L1-I cache). As contemporary data center applications become more complex, their code footprints also grow, resulting in a high number of Branch Target Buffer (BTB) misses. These BTB missing branches typically have previously been decoded and placed in the BTB, but have since been evicted, leading to BTB misses now. FDIP can alleviate L1-I cache misses, but its reliance on the BPU's tracking structures means that when it encounters a BTB miss, the BPU may not identify the current instruction as a branch to FDIP. This can prevent FDIP from prefetching or cause it to speculate down the wrong path, further polluting the L1-I cache. We observe that the vast majority, 75%, of BTB-missing, unidentified branches are actually present in instruction cache lines that FDIP has previously fetched. Nevertheless, these missing branches have not yet been decoded and inserted into the BTB. This is because the instruction line is * Authors have contributed equally. ‡The work was done while the author was at Princeton University. et of the previous taken branch) till an exit point (taken branch). We call branch instructions present in the ignored portion of the cache line “Shadow Branches.” Here we present Skia, a novel shadow branch decoding technique that identifies and decodes unused bytes in cache lines fetched by FDIP, inserting them into a Shadow Branch Buffer (SBB). The SBB is accessed in parallel with the BTB, allowing FDIP to speculate despite a BTB miss. With a minimal storage state of 12.25KB, Skia delivers a geomean speedup of ∼5.7% over an 8K-entry BTB (78KB) and ∼2% versus adding an equal amount of state to the BTB, across 16 front-end bound applications. Since many branches stored in the SBB are distinct compared to those in a similarly sized BTB, we consistently observe greater performance gains with Skia across all examined sizes until saturation.

## 中文摘要

现代处理器实现了去耦合前端（decoupled front-end），通常采用某种形式的取指导向指令预取（Fetch Directed Instruction Prefetching, FDIP）来避免前端停顿。FDIP 由分支预测单元（BPU）驱动，依赖 BPU 的准确性以及分支目标跟踪结构，将指令投机地取入指令缓存（L1-I 缓存）。随着当代数据中心应用日益复杂，其代码占用空间也不断增长，导致大量分支目标缓冲（BTB）缺失。这些 BTB 缺失的分支通常此前已被解码并放入 BTB，但此后被替换出去，从而造成当前的 BTB 缺失。FDIP 可以缓解 L1-I 缓存缺失，但它对 BPU 跟踪结构的依赖意味着，当遇到 BTB 缺失时，BPU 可能无法识别当前指令是分支，从而无法进行 FDIP。这可能使 FDIP 无法预取，或使其沿错误的路径投机，进一步污染 L1-I 缓存。我们观察到，绝大多数（75%）BTB 缺失且未被识别的分支实际上存在于 FDIP 此前已取入的指令缓存行中。然而，这些缺失的分支尚未被解码并插入 BTB。这是因为，从上一个已执行分支起的指令行剩余部分直到退出点（已执行分支）都未被使用（脚注：* 作者贡献相同。‡ 该工作是在作者于普林斯顿大学期间完成的）。我们称这些位于缓存行被忽略部分中的分支指令为“影子分支”（Shadow Branches）。本文提出 Skia，一种新颖的影子分支解码技术，它识别并解码 FDIP 所取缓存行中未使用的字节，并将其插入影子分支缓冲（Shadow Branch Buffer, SBB）。SBB 与 BTB 并行访问，使 FDIP 即便在 BTB 缺失时也能继续投机。借助仅 12.25KB 的极小存储状态，在 16 个受前端限制的应用上，Skia 相对 8K 项 BTB（78KB）取得约 5.7% 的几何平均加速，相对向 BTB 增加同等容量状态取得约 2% 的加速。由于 SBB 中存储的许多分支与同等规模 BTB 中的分支不同，我们在所有考察的容量下直至饱和都一致观察到 Skia 带来更大的性能收益。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716273)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5B](index.md) · [返回 ASPLOS 2025](../index.md)
