---
title: "RANGE-BLOCKS: A Synchronization Facility for Domain-Specific Architectures"
description: "ASPLOS 2025 · Session 2C · RANGE-BLOCKS：面向领域特定架构的同步设施"
tags:
  - "ASPLOS2025"
  - "Session 2C"
  - "Accelerators"
---

# RANGE-BLOCKS: A Synchronization Facility for Domain-Specific Architectures

**中文标题：** RANGE-BLOCKS：面向领域特定架构的同步设施

**所属 Session：** [Session 2C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Anagha Molakalmur Anil Kumar (Simon Fraser University), Aditya Prasanna (Simon Fraser University), Arrvindh Shriraman (Simon Fraser University)

**单位：** Simon Fraser University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707225) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Current domain-speci!c architectures (DSAs) work predominantly with static data structures and! nd it challenging to insert or remove data (they only support in-place updates). However, as DSAs target real-world applications, it is necessary to support mutable and dynamically resizable data structures. DSAs cannot support dynamic data structures since they lack a synchronization facility. DSAs are forced to either use address-based atomics or batch updates on the host. Unfortunately, both approaches introduce prohibitive performance penalties and require large caches for the locks. Range-blocks (RBlox) develops a hardware synchronization facility for DSAs to support dynamic data structures. Our idea is to use key ranges to capture synchronization boundaries and tap into the inherent parallelism of the datastructure layout. We make two novel observations that enable a practical hardware implementation: i) Range locks are symbolic and can compactly represent mutexes on multiple nested objects. Thus, any operation requires fewer range locks, and a small on-chip table su"ces (2kb) compared to large caches (256kb) for address-based locks [79, 81]. ii) Ranges also explicitly represent the region of interest, and we can instantly achieve mutual exclusion (instead of relying on ordering). On a 128-tile data#ow DSA, we improve performance by 15→, reduce DRAM bandwidth by 4→, save 70% of on-chip tra"c, and require 6.6% of on-chip energy.

## 中文摘要

当前的领域特定架构（DSA）主要面向静态数据结构工作，并且难以插入或删除数据（它们仅支持原地更新）。然而，随着 DSA 面向真实世界应用，就必须支持可变且可动态调整大小的数据结构。由于缺少同步设施，DSA 无法支持动态数据结构。DSA 被迫要么使用基于地址的原子操作，要么在主机上进行批量更新。遗憾的是，这两种方法都会带来难以承受的性能开销，并且需要大容量缓存来存放锁。Range-blocks（RBlox）为 DSA 开发了一种硬件同步设施，以支持动态数据结构。我们的思路是利用键区间（key ranges）来刻画同步边界，并挖掘数据结构布局固有的并行性。我们提出两个新颖观察，使实用的硬件实现成为可能：i) 区间锁是符号化的，可以紧凑地表示多个嵌套对象上的互斥锁。因此，任意操作所需的区间锁更少，一个小的片上表（2KB）就足够，而基于地址的锁[79, 81]需要大容量缓存（256KB）。ii) 区间还显式地表示关注区域，我们能够即时实现互斥（而不依赖顺序）。在 128 tile 的数据流 DSA 上，我们将性能提升 15→，将 DRAM 带宽降低 4→，节省 70% 的片上流量，并且只需要 6.6% 的片上能耗。

## 英文关键词

Domain-speci!c Architectures, Synchronization, Locks, Hierarchical data-structures

## 中文关键词

领域特定架构；同步；锁；层次化数据结构

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707225)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2C](index.md) · [返回 ASPLOS 2025](../index.md)
