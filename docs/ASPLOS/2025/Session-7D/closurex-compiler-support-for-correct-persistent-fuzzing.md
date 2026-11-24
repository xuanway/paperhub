---
title: "ClosureX: Compiler Support for Correct Persistent Fuzzing"
description: "ASPLOS 2025 · Session 7D · ClosureX：面向正确持久化模糊测试的编译器支持"
tags:
  - "ASPLOS2025"
  - "Session 7D"
  - "Fuzz Testing"
---

# ClosureX: Compiler Support for Correct Persistent Fuzzing

**中文标题：** ClosureX：面向正确持久化模糊测试的编译器支持

**所属 Session：** [Session 7D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Rishi Ranjan (Virginia Tech), Ian Paterson (Virginia Tech), Matthew Hicks (Virignia Tech)

**单位：** Virginia Tech；Virignia Tech

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707281) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Fuzzing is a widely adopted and pragmatic methodology for bug hunting as a means of software hardening. Research reveals that increasing fuzzing throughput directly increases bug discovery rate. The highest performance fuzzing strategy is persistent fuzzing, which reuses a single process for all test cases by looping back to the start upon completion, instead of exiting. This eliminates all process creation, initialization, and tear-down costs—which are on-par with execution cost. Unfortunately, persistent fuzzing leads to semantically inconsistent program states because process state changes from one test case remain for subsequent test cases. This semantic inconsistency results in missed crashes, false crashes, and overall incorrectness that undermines fuzzer effectiveness. We observe that existing fuzzing execution mechanisms exist on a continuum, based on the amount of state that gets discarded and restored between test cases. We present ClosureX, a fuzzing execution mechanism that sits at a new spot on this state restoration continuum, where only testcase-execution-specific state is reset. This fine-grain state restoration provides near-persistent performance with the correctness of heavyweight state restoration. We construct ClosureX as a set of LLVM passes that integrate with AFL++. Our evaluation on ten popular open-source fuzzing targets show that ClosureX maintains semantic correctness, while increasing test case execution rate by over 3.5x, on average, compared to AFL++. ClosureX also finds bugs more consistently and 1.9x faster than AFL++, with ClosureX discovering 15 0-day bugs (4 CVEs).

## 中文摘要

模糊测试是一种被广泛采用且务实的方法论，用于以软件加固为目的的缺陷挖掘。研究表明，提升模糊测试吞吐量能直接提高缺陷发现速率。性能最高的模糊测试策略是持久化模糊测试，它通过在每个测试用例执行完成后回到起始位置而不是退出进程，复用单个进程来运行所有测试用例。这消除了全部进程创建、初始化与销毁开销——这些开销与执行开销相当。遗憾的是，持久化模糊测试会导致语义上不一致的程序状态，因为某个测试用例造成的进程状态变化会残留给后续测试用例。这种语义不一致会造成崩溃漏报、崩溃误报以及整体的不正确性，从而削弱模糊测试器的有效性。我们观察到，现有的模糊测试执行机制依据测试用例之间被丢弃与恢复的状态量，构成一个连续谱。我们提出 ClosureX，一种位于该状态恢复连续谱新位置上的模糊测试执行机制，其中只重置与测试用例执行相关的状态。这种细粒度状态恢复在提供接近持久化性能的同时，具备重量级状态恢复的正确性。我们将 ClosureX 构建为一组与 AFL++ 集成的 LLVM pass。在十个流行的开源模糊测试目标上的评估表明，与 AFL++ 相比，ClosureX 在保持语义正确性的同时，将测试用例执行速率平均提升超过 3.5 倍。ClosureX 还能比 AFL++ 更稳定且快 1.9 倍地发现缺陷，共发现 15 个 0-day 缺陷（4 个 CVE）。

## 英文关键词

Fuzzing, System Security, Security and Privacy, Software Testing

## 中文关键词

模糊测试；系统安全；安全与隐私；软件测试

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707281)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7D](index.md) · [返回 ASPLOS 2025](../index.md)
