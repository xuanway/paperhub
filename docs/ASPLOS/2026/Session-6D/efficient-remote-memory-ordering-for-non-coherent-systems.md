---
title: "Efficient Remote Memory Ordering for Non-Coherent Systems"
description: "ASPLOS 2026 · Session 6D · 面向非一致性系统的高效远程内存排序"
tags:
  - "ASPLOS2026"
  - "Session 6D"
  - "Disaggregated Memory Systems"
---

# Efficient Remote Memory Ordering for Non-Coherent Systems

**中文标题：** 面向非一致性系统的高效远程内存排序

**所属 Session：** [Session 6D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Wei Siew Liew (University of Utah), Md Ashfaqur Rahaman (University of Utah), Adarsh Patil (Arm), Ryan Stutsman (University of Utah), Vijay Nagarajan (University of Utah)

**单位：** University of Utah；Arm

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790156) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Software using non-coherent interconnects like PCI Express requires fine-grained memory ordering, but current hardware mandates the use of costly source-side serialization. We show that this architectural mismatch severely limits the performance of two critical applications: (1) the transmission of network packets from a CPU to a NIC (requiring write-to-write ordering) and (2) key-value store lookups by an RDMA-enabled NIC (requiring read-to-read ordering). We address this by proposing a new destination-based ordering model and the hardware-software co-design comprising PCIe extensions and ISA extensions that allow software to express ordering intent efficiently. Novel microarchitecture at the Root Complex enforces these expressed semantics, eliminating source-side stalls. Our approach significantly improves the throughput of these application kernels and enables new, simpler protocols that outperform the state-ofthe-art.

## 中文摘要

使用 PCI Express 等非一致性互连的软件需要细粒度的内存排序，但当前硬件强制使用代价高昂的源端串行化。我们表明，这种架构失配严重限制了两个关键应用的性能：（1）从 CPU 向 NIC 传输网络数据包（需要写—写排序），以及（2）由支持 RDMA 的 NIC 进行键值存储查找（需要读—读排序）。为解决这一问题，我们提出一种新的基于目的端的排序模型，以及由 PCIe 扩展和 ISA 扩展构成的软硬件协同设计，使软件能够高效地表达排序意图。Root Complex 处的新颖微架构强制执行这些被表达的语义，从而消除源端停顿。我们的方法显著提升了这些应用内核的吞吐量，并支持新的、更简单的协议，其性能优于现有最先进方案。

## 英文关键词

Memory Consistency Models, I/O Interconnects, Non-Coherent Interconnects, RDMA, PCIe

## 中文关键词

内存一致性模型；I/O 互连；非一致性互连；RDMA；PCIe

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790156)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6D](index.md) · [返回 ASPLOS 2026](../index.md)
