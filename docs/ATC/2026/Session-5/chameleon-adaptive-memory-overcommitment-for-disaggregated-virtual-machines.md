# Chameleon: Adaptive Memory Overcommitment for Disaggregated Virtual Machines

**中文标题**：Chameleon：面向解耦虚拟机的自适应内存超分

**所属 Session**：[Session 5: VM, Containers and Migration](index.md) · [ATC 2026](../index.md)

**作者**：Yilong Luo (Peking University), Yulong Zhang (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Siyuan Xu (Tongji University), Siyi Zhang (SAIS, University of Chinese Academy of Sciences), Yanwen Xia (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Mingyu Wu (Shanghai Jiao Tong University), Diyu Zhou (Peking University), Tao Xie (Peking University), Chenxi Wang (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences)

## 英文摘要
Memory disaggregation enables cold-memory overcommitment for virtual machines (VMs), but two challenges limit its effectiveness: the page-granularity dilemma, where reclaiming 2 MB transparent huge pages (THPs) suffers from hot-bloat issues while splitting them into 4 KB pages sacrifices translation locality and amplifies swap overhead; and the high cost of extended page table (EPT) translation lookaside buffer (TLB) invalidation, where each reclamation flushes all cached translations of the entire VM. To address these challenges, in this paper, we propose Chameleon, an adaptive memory-overcommitment framework for disaggregated VMs, built on two insights: the optimal page-management granularity often lies between the two extremes, and EPT TLB invalidation needs only to be eventually consistent with memory reclamation. Accordingly, Chameleon continuously adapts page granularity to runtime access skewness, exposing cold memory hidden in hot-bloat huge pages while preserving the translation and swap efficiency of larger mappings; it further decouples guest-side reclamation steps from EPT TLB invalidation, allowing expensive EPT TLB flushes to be deferred, batched, and amortized. Under a 5% slowdown bound, Chameleon reclaims on average 3.4× (up to 4.3×) as much memory as HyperAlloc and 2.3× (up to 2.9×) as much as HyperAlloc+Memtis.

## 中文摘要
内存解耦使虚拟机（VM）的冷内存超分成为可能，但有两个挑战限制了其效果：一是页粒度困境，即回收 2 MB 透明大页（THP）会遭遇热膨胀（hot-bloat）问题，而将其拆分为 4 KB 页又会牺牲地址转换局部性并放大换页开销；二是扩展页表（EPT）转换后备缓冲（TLB）失效的代价高昂，每次回收都会冲刷整个 VM 的所有缓存转换条目。为应对这些挑战，本文提出 Chameleon，一个面向解耦 VM 的自适应内存超分框架，它基于两个洞见：最优的页管理粒度往往位于这两个极端之间；EPT TLB 失效只需与内存回收保持最终一致。据此，Chameleon 持续让页粒度适配运行时的访问偏斜，既能发掘出隐藏在热膨胀大页中的冷内存，又保留了较大映射的地址转换与换页效率；它进一步将客户机侧的回收步骤与 EPT TLB 失效解耦，使代价高昂的 EPT TLB 冲刷得以被延迟、批量执行并摊销。在 5% 的性能下降约束下，Chameleon 回收的内存量平均为 HyperAlloc 的 3.4×（最高 4.3×），为 HyperAlloc+Memtis 的 2.3×（最高 2.9×）。

## 英文关键词
Virtual Machine, Overcommitment, Disaggregated Memory, Huge Page

## 中文关键词
虚拟机，超分，解耦内存，大页

[返回 Session 5](index.md) · [返回 ATC 2026](../index.md)
