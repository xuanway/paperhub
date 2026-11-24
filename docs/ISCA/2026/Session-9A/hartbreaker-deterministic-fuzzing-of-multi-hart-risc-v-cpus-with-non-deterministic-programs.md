---
title: "HARTBREAKER: Deterministic Fuzzing of Multi-Hart RISC-V CPUs with Non-Deterministic Programs"
description: "ISCA 2026 · Session 9A · HARTBREAKER: Deterministic Fuzzing of Multi-Hart RISC-V CPUs with Non-Deterministic Programs"
tags:
  - "ISCA2026"
  - "Session 9A"
  - "Verification and Robustness"
---

# HARTBREAKER: Deterministic Fuzzing of Multi-Hart RISC-V CPUs with Non-Deterministic Programs

**中文标题：** HARTBREAKER: 面向非确定性程序的多 Hart RISC-V CPU 确定性模糊测试

**所属 Session：** [Session 9A](index.md) · [ISCA 2026](../index.md)

**作者：** Quentin Bordier, Tobias Kovats, Flavien Solt, Kaveh Razavi

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Hardware bugs threaten the correctness and security of modern CPUs. Relying on a deterministic correct baseline, pre-silicon fuzzing has proven to be an effective strategy for discovering deviations from correct behavior (i.e., bugs) in single-core CPUs. Modern CPUs, however, often feature multiple cores with complex interconnects that implement communication channels such as inter-processor interrupts or shared memory. Is it possible to effectively fuzz multicore CPUs despite their inherent non-deterministic operations? We make a key observation that multi-hart interactions may result in non-deterministic data flows, control flows, or combinations thereof. An efficient fuzzing campaign needs to manage this non-determinism without limiting the exploration of the possible state space that may lead to bugs. Our new multi-hart RISC-V fuzzer, called HARTBREAKER, achieves this with a judicious use of three determinism anchors: control- and data-flow anchors enable non-deterministic control- and data-flow interactions between harts while ensuring a correct execution of multi-hart test programs, achieving high testing throughput and simplified bug detection. Synchronization anchors bound the non-deterministic window across harts, enabling HARTBREAKER to detect bugs that do not contaminate the control flow. We test HARTBREAKER on five multi-hart designs, namely Rocket, BOOM, Toooba, NaxRiscv and XiangShan. HARTBREAKER discovers five new concurrency bugs in these designs.

## 中文摘要

硬件缺陷威胁现代 CPU 的正确性和安全性。依托确定性正确基线，流片前模糊测试已被证明是在单核 CPU 中发现偏离正确行为（即缺陷）的有效策略。然而，现代 CPU 通常具有多个核心以及实现处理器间中断或共享内存等通信通道的复杂互连。尽管多核 CPU 固有的非确定性操作，是否有可能对其进行有效模糊测试？我们做出一个关键观察：多 hart 交互可能导致非确定性的数据流、控制流或其组合。高效的模糊测试活动需要在不限制可能通向缺陷的状态空间探索的前提下管理这种非确定性。我们的新多 hart RISC-V 模糊测试器 HARTBREAKER 通过明智地使用三个确定性锚点来实现这一点：控制和数据流锚点使 hart 之间能够进行非确定性的控制流和数据流交互，同时确保多 hart 测试程序的正确执行，从而实现高测试吞吐量并简化缺陷检测。同步锚点约束了跨 hart 的非确定性窗口，使 HARTBREAKER 能够检测不会污染控制流的缺陷。我们在五种多 hart 设计上测试了 HARTBREAKER，即 Rocket、BOOM、Toooba、NaxRiscv 和香山。HARTBREAKER 在这些设计中发现了五个新的并发缺陷。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：comsec-group/hartbreaker](https://github.com/comsec-group/hartbreaker)
- [实验材料归档（Zenodo 19417381）](https://zenodo.org/records/19417381)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9A](index.md) · [返回 ISCA 2026](../index.md)
