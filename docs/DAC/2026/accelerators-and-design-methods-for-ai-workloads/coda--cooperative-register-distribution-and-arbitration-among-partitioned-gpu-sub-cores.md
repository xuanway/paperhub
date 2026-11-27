CODA: Cooperative Register Distribution and Arbitration Among Partitioned GPU Sub-Cores
Authors：
[Bo Yuan](https://63dac.conference-program.com/?post_type=page&p=15&uid=88914333023124197861)，[Sheng Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7630233184226704819)，[Yang Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=9806740372827205661)，[Zekun Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=19378881409638887431)，[Jianfeng Cui](https://63dac.conference-program.com/?post_type=page&p=15&uid=93829206898712559221)

## 中文标题

CODA：分区 GPU 子核间的协同寄存器分配与仲裁

## 英文摘要

The partitioned microarchitecture of Streaming Multiprocessor (SM) is a fundamental design that enables massive parallelism in modern General-Purpose Graphics Processing Units (GPGPUs). This approach, however, inherently introduces two critical inefficiencies: vast data redundancy across distributed private registers and severe conflicts and load imbalance in the limited banks. To holistically address these cross-partition bottlenecks, this paper introduces CODA, a cooperative Register File (RF) distribution and arbitration framework. CODA is composed of two synergistic mechanisms: the Cooperative Register Renaming (CRR), which eliminates data redundancy by maintaining a single physical copy of shared data across sub-cores, and the Dual-Skewed Arbitrator (DSA) that mitigates fine-grained bank conflicts by incorporating the operand collector ID into its arbitration logic. Evaluations on a diverse suite of deep learning workloads show that CODA exhibits superior performance compared to its baseline architecture, achieving a speedup of 28.9% alongside a 15.6% reduction in RF power consumption. These gains are directly attributed to a 15.9% reduction in RF load imbalance and a 12.7% lower bank conflict rate.

## 中文摘要

流式多处理器（SM）的分区微架构是现代通用图形处理器（GPGPU）实现大规模并行的基础设计。然而，这种方法本质上会带来两个关键的低效问题：分布式私有寄存器之间存在大量数据冗余，以及有限 bank 中严重的冲突和负载不均衡。为整体解决这些跨分区瓶颈，本文提出了 CODA，一种协同寄存器堆（RF）分配与仲裁框架。CODA 由两个协同机制组成：协同寄存器重命名（CRR）通过在子核之间为共享数据维护单一物理副本以消除数据冗余；双偏斜仲裁器（DSA）通过将操作数收集器 ID 纳入仲裁逻辑来缓解细粒度 bank 冲突。在多种深度学习工作负载上的评估表明，CODA 相比其基线架构表现出更优性能，实现了 28.9% 的加速，同时将 RF 功耗降低 15.6%。这些收益直接归因于 RF 负载不均衡降低 15.9% 以及 bank 冲突率降低 12.7%。

## 英文关键词

GPGPU, GEMM, Register File, Redundant Load, Sub-Core

## 中文关键词

GPGPU、GEMM、寄存器堆、冗余加载、子核
