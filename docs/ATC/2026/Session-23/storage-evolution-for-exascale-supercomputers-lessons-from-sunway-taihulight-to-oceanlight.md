# Storage Evolution for Exascale Supercomputers: Lessons from Sunway TaihuLight to OceanLight

**中文标题**：面向 E 级超算的存储演进：从神威·太湖之光到神威·海洋之光的经验

**所属 Session**：[Session 23: Storage and OS Policies](index.md) · [ATC 2026](../index.md)

**作者**：Bin Yang (Tianjin University), Cheng Su (Tianjin University), Hao Wei (Tsinghua University), Wenze Du (Tianjin University), Jiwei Yan (Tianjin University), Shihan Zhang (Tianjin University), Wei Xue (Tsinghua University), Ce Yu (Tianjin University)

## 英文摘要
Modern supercomputers are transitioning from homogeneous to heterogeneous architectures supporting mixed HPC, AI, and HTC workloads. However, traditional storage design assumptions, single schedulers, static load balancing, and pure write optimization are failing under this new paradigm. This paper presents a longitudinal analysis of eight years of production data from two generations of Sunway supercomputers: TaihuLight and its exascale successor, OceanLight. Analyzing 10 million jobs and 60 TB of I/O traces, we reveal several counterintuitive bottlenecks: scheduler congestion from HTC bursts; Round-Robin load balancing that trades reduced interference frequency for more severe degradation and collapsed cache locality; the burst buffer dilemma where write gains come with read variability; and write-read asymmetry where write-optimized layouts cause severe post-processing slowdowns. Building on these findings, we implement and evaluate two mitigation mechanisms on OceanLight hardware: token-bucket traffic shaping and domain-aware forwarding scheduling. We also discuss design principles for coordinated burst buffer draining, load-aware dynamic mapping, and layout-aware I/O guidance as future directions. These insights offer actionable guidance for designing next-generation supercomputers that efficiently support converged mixed workloads.

## 中文摘要
现代超级计算机正从同构架构转向支持 HPC、AI 与 HTC 混合负载的异构架构。然而，传统的存储设计假设——单一调度器、静态负载均衡与纯写优化——在这一新范式下正逐渐失效。本文对两代神威超级计算机（太湖之光及其 E 级后继机型神威·海洋之光）八年生产数据进行了纵向分析。通过分析 1000 万个作业与 60 TB 的 I/O trace，我们揭示了若干反直觉的瓶颈：HTC 突发引发的调度器拥塞；轮询负载均衡以降低干扰频率为代价换取了更严重的性能退化，并使缓存局部性崩塌；突发缓冲困境，即写入收益伴随着读取波动性；以及写读不对称，即写优化的布局导致严重的后处理变慢。基于这些发现，我们在神威·海洋之光硬件上实现并评估了两种缓解机制：令牌桶流量整形与域感知转发调度。我们还讨论了协同突发缓冲排空、负载感知动态映射与布局感知 I/O 指导等未来方向的设计原则。这些洞见为设计能够高效支持融合混合负载的下一代超级计算机提供了可操作的指导。

## 英文关键词
Data analysis, Storage system, Workload characterization, supercomputer, I/O performance

## 中文关键词
数据分析，存储系统，负载刻画，超级计算机，I/O 性能

[返回 Session 23](index.md) · [返回 ATC 2026](../index.md)
