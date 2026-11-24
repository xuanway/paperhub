---
title: "FlexProf: Flexible, Side-Channel-Free Memory Access"
description: "ASPLOS 2025 · Session 7C · FlexProf：灵活且无侧信道的内存访问"
tags:
  - "ASPLOS2025"
  - "Session 7C"
  - "Side Channels"
---

# FlexProf: Flexible, Side-Channel-Free Memory Access

**中文标题：** FlexProf：灵活且无侧信道的内存访问

**所属 Session：** [Session 7C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jarrett Minton (University of Utah), Rajeev Balasubramonian (University of Utah)

**单位：** University of Utah

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715997) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Secure processors must defend against a wide array of microarchitecture side-channels, including those induced by a shared memory controller. Multiple studies have proposed techniques that allocate "turns" (within the memory controller) to each co-scheduled virtual machine (VM), and introduce gaps between VM turns to prevent resource conflicts and side-channels. In spite of past advancements in secure memory scheduling, the elimination of side-channels imposes a performance slowdown of 2×. We observe that one of the causes of this slowdown is that the memory controller schedule accommodates the worst case, i.e., it is prepared to handle either reads or writes. The key insight in this work is that the schedule can be more efficient if we designate every turn to handle fixed patterns of reads and writes. In particular, we introduce a read-optimized turn and a write-optimized turn. Coarse-grain application profiling helps determine how often the two types of turns are invoked, without leaking sensitive information. We also add flexibility so that a readoptimized turn can opportunistically also issue writes, and vice versa. This provides a good balance between restrictions and flexibility; between throughput and utilization. The proposed FlexProf memory controller improves performance by up to 33% with a geometric mean gain of 8% on mixed workloads, relative to state-of-the-art methods. Over half the memory-intensive programs evaluated exhibit performance gains of over 10%.

## 中文摘要

安全处理器必须防御广泛的微架构侧信道，包括由共享内存控制器所引发的侧信道。多项研究已提出为每个协同调度的虚拟机（VM）在内存控制器内部分配“轮次”（turn），并在 VM 轮次之间引入间隔，以防止资源冲突与侧信道。尽管安全内存调度已有进展，消除侧信道仍带来 2 倍的性能下降。我们观察到，这种下降的原因之一是内存控制器调度需兼顾最坏情况，即它必须准备好处理读或写。本工作的关键洞察是：如果我们将每个轮次指定为处理固定的读写模式，调度可以更加高效。特别地，我们引入了读优化轮次与写优化轮次。粗粒度应用画像有助于确定这两类轮次的调用频率，而不会泄漏敏感信息。我们还增加了灵活性，使读优化轮次可以机会性地发出写操作，反之亦然。这在限制与灵活性之间、吞吐与利用率之间取得了良好平衡。相对于最先进方法，所提出的 FlexProf 内存控制器在混合工作负载上将性能最高提升 33%，几何平均提升 8%。在评估的内存密集型程序中，超过一半的程序性能提升超过 10%。

## 英文关键词

Side-Channel; Hardware Security

## 中文关键词

侧信道；硬件安全

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715997)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7C](index.md) · [返回 ASPLOS 2025](../index.md)
