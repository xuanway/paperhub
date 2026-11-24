---
title: "Chips Need DIP: Time-Proportional Per-Instruction Cycle Stacks at Dispatch"
description: "ASPLOS 2026 · Session 7D · 芯片需要 DIP：分发阶段按时间比例的逐指令周期栈"
tags:
  - "ASPLOS2026"
  - "Session 7D"
  - "Processor Microarchitecture"
---

# Chips Need DIP: Time-Proportional Per-Instruction Cycle Stacks at Dispatch

**中文标题：** 芯片需要 DIP：分发阶段按时间比例的逐指令周期栈

**所属 Session：** [Session 7D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Silvio Campelo de Santana (Norwegian University of Science and Technology (NTNU)), Joseph Rogers (Norwegian University of Science and Technology (NTNU)), Lieven Eeckhout (Ghent University), Magnus Jahre (Norwegian University of Science and Technology (NTNU))

**单位：** Norwegian University of Science and Technology (NTNU)；Ghent University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790139) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Despite continuous accelerator improvements, high single-thread performance remains crucial due to Amdahl's Law. With technology scaling slowing, developers must produce code that is as performant as possible, which often involves instruction-level performance analysis. Such analysis can be visualized as Per-Instruction Cycle Stacks (PICS), which, when created at the commit stage of the processor, report each static instruction's contribution to overall execution time and capture the performance events it was subject to. Sadly, PICS at commit (PICS𝐶) often cannot explain performance because they solely capture how effectively instructions egress from the processor core's out-of-order execution window. In contrast, developers must typically also gain insight into how efficiently instructions ingress into the execution window to fully understand application performance. PICS𝐶must hence be complemented by PICS at dispatch (PICS𝐷) because execution window ingress issues result in specific instructions exhibiting high dispatch latencies. We therefore propose dispatch-time profiling (DIP), which combines time-proportional at dispatch attribution policies with statistical sampling to accurately report each static instruction's contribution to dispatch time as well as list the reason(s) for delayed ingress. DIP is simple to implement and incurs low overhead, i.e., storage and execution time and overheads of 49 bytes and ∼1%, respectively, while delivering high accuracy (average profile error of 5.2%). This is a significant improvement over the 26.9% error of state-of-the-art dispatch-tagging as implemented in AMD IBS, Arm SPE, and IBM RIS. We demonstrate that needing PICS𝐷and PICS𝐶is the common case by showing that 18 out of our 22 SPEC2017 benchmarks simultaneously exhibit both ingress and egress issues. Additionally, we leverage DIP's PICS𝐷to optimize the fotonik3d benchmark, improving its performance by 8.5%.

## 中文摘要

尽管加速器持续改进，由于 Amdahl 定律，高单线程性能仍然至关重要。随着技术缩放放缓，开发者必须编写尽可能高性能的代码，这通常涉及指令级性能分析。此类分析可以可视化为逐指令周期栈（Per-Instruction Cycle Stacks，PICS）；当在处理器提交阶段生成时，PICS 报告每条静态指令对总体执行时间的贡献，并捕获其所经历的性能事件。遗憾的是，提交阶段的 PICS（PICS𝐶）往往无法解释性能，因为它们只捕获指令从处理器核乱序执行窗口中流出的效率。相反，开发者通常还必须深入了解指令进入执行窗口的效率，才能全面理解应用性能。因此，PICS𝐶 必须由分发阶段的 PICS（PICS𝐷）来补充，因为执行窗口进入方面的问题会导致特定指令表现出很高的分发延迟。为此我们提出分发时剖析（dispatch-time profiling，DIP），它将分发阶段的时间比例归因策略与统计采样相结合，准确报告每条静态指令对分发时间的贡献，并列出进入延迟的原因。DIP 实现简单且开销低，即存储开销与执行时间开销分别为 49 字节和约 1%，同时具有高准确度（平均剖析误差为 5.2%）。相比 AMD IBS、Arm SPE 和 IBM RIS 中所实现的最先进分发标记技术 26.9% 的误差，这是显著的改进。我们通过表明 22 个 SPEC2017 基准中有 18 个同时表现出进入与流出问题，证明了同时需要 PICS𝐷 和 PICS𝐶 是常见情形。此外，我们利用 DIP 的 PICS𝐷 优化 fotonik3d 基准，使其性能提升 8.5%。

## 英文关键词

Performance analysis, dispatch-time profiling, per-instruction cycle stacks

## 中文关键词

性能分析；分发时剖析；逐指令周期栈

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790139)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7D](index.md) · [返回 ASPLOS 2026](../index.md)
