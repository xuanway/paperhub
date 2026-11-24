---
title: "Architecting Scalable Trapped Ion Quantum Computers using Surface Codes"
description: "ASPLOS 2026 · Session 4C · 使用表面码架构可扩展的囚禁离子量子计算机"
tags:
  - "ASPLOS2026"
  - "Session 4C"
  - "Quantum Error Correction"
---

# Architecting Scalable Trapped Ion Quantum Computers using Surface Codes

**中文标题：** 使用表面码架构可扩展的囚禁离子量子计算机

**所属 Session：** [Session 4C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Scott Jones (University of Cambridge), Prakash Murali (University of Cambridge)

**单位：** University of Cambridge

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790128) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Trapped ion (TI) qubits are a leading quantum computing platform. Current TI systems have less than 60 qubits, but a modular architecture known as the Quantum Charge-Coupled Device (QCCD) is a promising path to scale up devices. There is a large gap between the error rates of near-term systems (10−3 to 10−4) and the requirements of practical applications (below 10−9). To bridge this gap, we require Quantum Error Correction (QEC) to build logical qubits that are composed of multiple physical qubits. While logical qubits have been demonstrated on TI qubits, these demonstrations are restricted to small codes and systems. There is no clarity on how QCCD systems should be designed to implement practical-scale QEC. This paper studies how surface codes, a standard QEC scheme, can be implemented efficiently on QCCD-based systems. To examine how architectural parameters of a QCCD system can be tuned for surface codes, we develop a near-optimal topology-aware compilation method that outperforms existing QCCD compilers by an average of 3.8X in terms of logical clock speed. We use this compiler to examine how hardware trap capacity, connectivity and electrode wiring choices can be optimised for surface code implementation. In particular, we demonstrate that small traps of two ions are surprisingly ideal from both a performance-optimal and hardware-efficiency standpoint. This result runs counter to prior intuition that larger traps (20-30 ions) would be preferable, and has the potential to inform design choices for upcoming systems.

## 中文摘要

囚禁离子（TI）量子比特是领先的量子计算平台。当前 TI 系统的量子比特数不足 60 个，而一种被称为量子电荷耦合器件（QCCD）的模块化架构是扩展器件规模的一条有前景的路径。近期系统的错误率（10−3 到 10−4）与实际应用的要求（低于 10−9）之间存在很大差距。为弥合这一差距，我们需要量子纠错（QEC）来构建由多个物理量子比特组成的逻辑量子比特。尽管逻辑量子比特已在 TI 量子比特上得到演示，但这些演示仅限于小规模的码和系统。关于应如何设计 QCCD 系统以实现实用规模的 QEC，目前尚无明确答案。本文研究一种标准 QEC 方案——表面码——如何能在基于 QCCD 的系统中被高效实现。为考察 QCCD 系统的架构参数如何针对表面码进行调优，我们开发了一种近最优的拓扑感知编译方法，其逻辑时钟速度平均比现有 QCCD 编译器快 3.8 倍。我们使用该编译器考察硬件陷阱容量、连通性以及电极布线选择如何针对表面码实现进行优化。特别地，我们证明了容量为两个离子的微小陷阱在性能最优和硬件效率两方面都令人意外地理想。这一结果与“较大陷阱（20-30 个离子）会更可取”的先前直觉相悖，并有望为未来系统的设计选择提供参考。

## 英文关键词

quantum computing; quantum error correction; trapped ion architectures; surface codes; compiler optimization; quantum circuit routing; hardware-software co-design Please use nonacm option or ACM Engage class to enable CC licenses

## 中文关键词

量子计算；量子纠错；囚禁离子架构；表面码；编译器优化；量子电路布线；软硬件协同设计

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790128)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4C](index.md) · [返回 ASPLOS 2026](../index.md)
