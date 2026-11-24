---
title: "Robustness Verification for Checking Crash Consistency of Non-volatile Memory"
description: "ASPLOS 2025 · Session 9C · 面向非易失性内存崩溃一致性检查的鲁棒性验证"
tags:
  - "ASPLOS2025"
  - "Session 9C"
  - "Verification & Reliability"
---

# Robustness Verification for Checking Crash Consistency of Non-volatile Memory

**中文标题：** 面向非易失性内存崩溃一致性检查的鲁棒性验证

**所属 Session：** [Session 9C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Zhilei Han (School of Software, Tsinghua University), Fei He (School of Software, Tsinghua University)

**单位：** School of Software, Tsinghua University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707269) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The emerging non-volatile memory (NVM) technologies provide competitive performance with DRAM and ensure data persistence in the event of system failure. However, it exhibits weak behaviour in terms of the order in which stores are committed to NVMs, and therefore requires extra efforts from developers to flush pending writes. To ensure correctness of this error-prone task, it is crucial to develop a rigid method to check crash consistency of programs running on NVM devices. Most existing solutions are testing-based and rely on user guidance to dynamically detect such deficiencies. In this paper, we present a fully automated method to verify robustness, a newly established property for ensuring crash consistency of such programs. The method is based on the observation that, reachability of a post-crash non-volatile state under a given pre-crash execution can be reduced to validity of the pre-crash execution with additional ordering constraints. Our robustness verification algorithm employs a search-based framework to explore all partial executions and states, and checks if any non-volatile state is reachable under certain pre-crash execution. Once a reachable non-volatile state is obtained, we further check its reachability under memory consistency model. The algorithm is implemented in a prototype tool PMVerify that leverages symbolic encoding of the program and utilizes an SMT solver to efficiently explore all executions and states. The method is integrated into the DPLL(T) framework to optimize the robustness checking algorithm. Experiments on the PMDK example benchmark show that PMVerify is competitive with the state-of-the-art dynamic tool, PSan, in terms of robustness violation detection.

## 中文摘要

新兴的非易失性内存（NVM）技术提供了与 DRAM 相媲美的性能，并能在系统故障时确保数据持久性。然而，它在存储操作提交至 NVM 的顺序方面表现较弱，因此需要开发者额外付出努力来刷写尚未完成的写操作。为确保这一易错任务的正确性，发展一种严格的方法来检查运行于 NVM 设备上的程序的崩溃一致性至关重要。现有解决方案大多基于测试，并依赖用户引导来动态检测此类缺陷。本文提出一种全自动方法来验证鲁棒性——这是为保障此类程序崩溃一致性而新确立的一种性质。该方法基于如下观察：给定崩溃前执行下崩溃后非易失状态的可达性，可归约为带附加顺序约束的崩溃前执行的有效性。我们的鲁棒性验证算法采用基于搜索的框架来探索所有部分执行与状态，并检查在某种崩溃前执行下是否有任何非易失状态可达。一旦获得可达的非易失状态，我们进一步检查其在内存一致性模型下的可达性。该算法在原型工具 PMVerify 中实现，它利用程序的符号化编码并使用 SMT 求解器来高效探索所有执行与状态。该方法被集成到 DPLL(T) 框架中以优化鲁棒性检查算法。在 PMDK 示例基准上的实验表明，在鲁棒性违规检测方面，PMVerify 与最先进的动态工具 PSan 具有竞争力。

## 英文关键词

persistent memory, non-volatile memory, robustness, program verification, crash consistency

## 中文关键词

持久内存；非易失性内存；鲁棒性；程序验证；崩溃一致性

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707269)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9C](index.md) · [返回 ASPLOS 2025](../index.md)
