---
title: "CtXnL: A Software-Hardware Co-Designed Solution for Efficient CXL-Based Transaction Processing"
description: "ASPLOS 2025 · Session 5D · CtXnL：面向高效 CXL 事务处理的软硬件协同设计方案"
tags:
  - "ASPLOS2025"
  - "Session 5D"
  - "CXL Storage"
---

# CtXnL: A Software-Hardware Co-Designed Solution for Efficient CXL-Based Transaction Processing

**中文标题：** CtXnL：面向高效 CXL 事务处理的软硬件协同设计方案

**所属 Session：** [Session 5D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Zhao Wang (Peking University, School of Integrated Circuits,Peking University, School of Computer Science), Yiqi Chen (Peking University, School of Integrated Circuits), Cong Li (Peking University, School of Integrated Circuits), Yijin Guan (Alibaba Group, DAMO Academy,Hupan Lab), Dimin Niu (Alibaba Group, DAMO Academy,Hupan Lab), Tianchan Guan (Alibaba Group, DAMO Academy,Hupan Lab), Zhaoyang Du (Alibaba Group, DAMO Academy,Hupan Lab), Xingda Wei (Shanghai Jiao Tong University, Institute of Parallel and Distributed Systems, SEIEE), Guangyu Sun (Peking University, School of Integrated Circuits,Beijing Advanced Innovation Center for Integrated Circuits)

**单位：** Peking University, School of Integrated Circuits,Peking University, School of Computer Science；Peking University, School of Integrated Circuits；Alibaba Group, DAMO Academy,Hupan Lab；Shanghai Jiao Tong University, Institute of Parallel and Distributed Systems, SEIEE；Peking University, School of Integrated Circuits,Beijing Advanced Innovation Center for Integrated Circuits

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716244) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Transaction processing systems are the crux for modern datacenter applications, yet current multi-node systems are slow due to network overheads. This paper advocates for Compute Express Link (CXL) as a network alternative, which enables low-latency and cache-coherent shared memory accesses. However, directly adopting standard CXL primitives leads to performance degradation due to the high cost of maintaining cross-node cache coherence. To address the CXL challenges, this paper introduces CtXnL, a software-hardware co-designed system that implements a novel hybrid coherence primitive tailored to the loosely coherent nature of transactional data. The core innovation of CtXnL is empowering transaction system developers with the ability to selectively achieve data coherence. Our evaluations on OLTP ∗co-corresponding author workloads demonstrate that CtXnL enhances performance, outperforming current network-based systems and achieves up to 2.08x greater throughput than vanilla CXL memory sharing architectures across universal transaction processing policies.

## 中文摘要

事务处理系统是现代数据中心应用的关键所在，然而当前的多节点系统因网络开销而性能低下。本文倡导以 Compute Express Link（CXL）作为网络的替代方案，它能够实现低延迟且缓存一致的共享内存访问。然而，直接采用标准 CXL 原语会因维护跨节点缓存一致性的高昂代价而导致性能下降。为应对 CXL 带来的挑战，本文提出 CtXnL，这是一个软硬件协同设计的系统，实现了一种针对事务数据弱一致性特征而定制的新型混合一致性原语。CtXnL 的核心创新在于赋予事务系统开发者按需选择性地实现数据一致性的能力。我们在 OLTP 工作负载上的评估表明，CtXnL 提升了性能，优于当前基于网络的系统，并在通用的事务处理策略下，相比原生 CXL 内存共享架构实现了最高 2.08 倍的吞吐提升。

## 英文关键词

Compute Express Link, distributed transaction processing systems, cache coherence

## 中文关键词

Compute Express Link；分布式事务处理系统；缓存一致性

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716244)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5D](index.md) · [返回 ASPLOS 2025](../index.md)
