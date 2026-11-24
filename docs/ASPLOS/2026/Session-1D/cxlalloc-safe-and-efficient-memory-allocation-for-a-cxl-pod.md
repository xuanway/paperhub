---
title: "Cxlalloc: Safe and Efficient Memory Allocation for a CXL Pod"
description: "ASPLOS 2026 · Session 1D · Cxlalloc：面向 CXL Pod 的安全高效内存分配"
tags:
  - "ASPLOS2026"
  - "Session 1D"
  - "CXL & Memory Fabric"
---

# Cxlalloc: Safe and Efficient Memory Allocation for a CXL Pod

**中文标题：** Cxlalloc：面向 CXL Pod 的安全高效内存分配

**所属 Session：** [Session 1D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Newton Ni (UT Austin), Yan Sun (UIUC), Zhiting Zhu (UT Austin/NVIDIA), Emmett Witchel (UT Austin)

**单位：** UT Austin；UIUC；UT Austin/NVIDIA

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790149) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

A Compute Express Link (CXL) pod is a group of hosts that share CXL-attached memory. A memory allocator for a CXL pod faces novel challenges: (1) CXL devices may not fully support inter-host hardware cache coherence (HWcc), (2) the allocator may be concurrently accessed from different processes, and (3) with more hosts, failures become more likely. We present cxlalloc, a user-space memory allocator that addresses these challenges through careful metadata layout and new protocols to maintain cache coherence in software, coordinate memory mappings across processes, and recover from crashes. Cxlalloc uses compare-and-swap (CAS) for efficient synchronization; to support CXL devices with no HWcc, we present a memory-based CAS (mCAS) primitive implemented in an FPGA. Experiments with in-memory key-value store workloads demonstrate that cxlalloc retains competitive performance while enabling new use-cases. Experiments with a commercial CXL device show that cxlalloc can achieve 80% of its maximum allocation throughput using mCAS.

## 中文摘要

计算快速链路（CXL）Pod 是一组共享 CXL 挂接内存的主机。为 CXL Pod 设计的内存分配器面临新的挑战：(1) CXL 设备可能不完全支持主机间硬件缓存一致性（HWcc），(2) 分配器可能被不同进程并发访问，(3) 随着主机数量增多，故障发生的可能性也更大。我们提出 cxlalloc，一个用户空间内存分配器，它通过精心的元数据布局和新的协议来应对这些挑战，以在软件中维护缓存一致性、跨进程协调内存映射并从崩溃中恢复。cxlalloc 使用比较并交换（CAS）实现高效同步；为了支持不具备 HWcc 的 CXL 设备，我们提出了一种在 FPGA 中实现的基于内存的 CAS（mCAS）原语。使用内存键值存储工作负载的实验表明，cxlalloc 在支持新用例的同时保持了有竞争力的性能。在商用 CXL 设备上的实验表明，使用 mCAS 时 cxlalloc 可以达到其最大分配吞吐量的 80%。

## 英文关键词

Memory allocation; CXL; shared memory; mCAS; cache coherence

## 中文关键词

内存分配；CXL；共享内存；mCAS；缓存一致性

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790149)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1D](index.md) · [返回 ASPLOS 2026](../index.md)
