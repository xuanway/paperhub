---
title: "CXLMC: Model Checking CXL Shared Memory Programs"
description: "ASPLOS 2026 · Session 1D · CXLMC：CXL 共享内存程序的模型检测"
tags:
  - "ASPLOS2026"
  - "Session 1D"
  - "CXL & Memory Fabric"
---

# CXLMC: Model Checking CXL Shared Memory Programs

**中文标题：** CXLMC：CXL 共享内存程序的模型检测

**所属 Session：** [Session 1D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Simon Guo (University of California, Irvine), Conan Truong (University of California, Irvine), Brian Demsky (University of California, Irvine)

**单位：** University of California, Irvine

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790150) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Compute Express Link (CXL) shared memory is an emerging industry standard that will allow for cache coherent sharing of remote memory between many machines. Memory devices will contain large amounts of DRAM that can be shared by many machines in a CXL cluster. This will enable software running on clusters of computers to use shared memory to communicate more efficiently and to share important data between these machines. As CXL clusters grow larger, machine failures will become a significant risk. Software will need to tolerate machine failures. A key challenge is that CXL uses caching of remote memory to hide latency. If a machine fails before it has flushed dirty cache lines back to the CXL shared memory device, the latest stores to those cache lines will be lost. Data structures have been developed that combine crash-consistent designs with flush and fence instructions to ensure that the data structures remain consistent even in the presence of failures. However, developing such crash-consistent data structures is error prone. It is easy to make a design or implementation error. Such crash consistency errors are hard to detect with testing. We propose CXLMC, a model checker that systematically explores crashing executions for the x86-CXL shared memory platform. We have evaluated CXLMC and found 24 bugs in 8 applications including 7 new bugs.

## 中文摘要

计算快速链路（CXL）共享内存是一项新兴的行业标准，它将允许多台机器之间对远程内存进行缓存一致的共享。内存设备将包含大量 DRAM，这些 DRAM 可被 CXL 集群中的多台机器共享。这将使运行在计算机集群上的软件能够使用共享内存更高效地通信，并在这些机器之间共享重要数据。随着 CXL 集群规模增大，机器故障将成为一项重大风险。软件将需要容忍机器故障。一个关键挑战在于，CXL 利用对远程内存的缓存来隐藏延迟。如果一台机器在将脏缓存行刷回 CXL 共享内存设备之前发生故障，那么对这些缓存行的最新存储将会丢失。已有研究提出了将崩溃一致性设计与 flush 和 fence 指令相结合的数据结构，以确保即使在发生故障的情况下这些数据结构仍保持一致。然而，开发此类崩溃一致性数据结构容易出错。很容易出现设计错误或实现错误。此类崩溃一致性错误难以通过测试发现。我们提出 CXLMC，一个针对 x86-CXL 共享内存平台系统地探索发生崩溃的执行的模型检测器。我们评估了 CXLMC，在 8 个应用中发现了 24 个缺陷，其中包括 7 个新缺陷。

## 英文关键词

Crash Consistency, CXL Memory, Partial Failure, Model Checking, Testing

## 中文关键词

崩溃一致性；CXL 内存；部分失效；模型检测；测试

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790150)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1D](index.md) · [返回 ASPLOS 2026](../index.md)
