# HybridQC: Hardware-Grounded Simulation of Tightly Integrated Hybrid Quantum-Classical Systems

**中文标题**：HybridQC：紧耦合混合量子—经典系统的硬件实测锚定仿真

**所属 Session**：[Session 20: Quantum Computing](index.md) · [ATC 2026](../index.md)

**作者**：Panayiotis Christou (Fordham University), Shuwen Kan (Fordham University), Ying Mao (Fordham University)

## 英文摘要
Hybrid quantum–classical performance depends on how quantum processors share classical compute, controllers, memory, and communication links. Circuit simulators and provider measurements expose kernel and job behavior, but leave topology-level questions about controller bottlenecks, quantum capacity, and mixed-workload contention unanswered. We present HybridQC, a discrete-event simulator for configurable hybrid compute units (HCUs). Users specify resource graphs containing classical compute, memory, controllers, quantum annealing (QA) and digital quantum computing (DQC) devices, and links. Jobs become dependent stages for preparation, quantum execution, transfers, reconstruction, and postprocessing. Finite capacities and selectable scheduling policies determine where stages wait and overlap. Service profiles use measurements from D-Wave Advantage 1 and Advantage 2 and IBM Kingston, Marrakesh, and Fez, separating physical quantum-processor occupancy from cloud wall time. Mean absolute percentage errors are 3.92%–8.04% for D-Wave access time and 5.26%–19.01% for IBM quantum seconds. Balanced 10× HCU scaling improves makespan by 2.19×–3.42×, while policy choice changes makespan by 1.80× for a mixed workload with 20 jobs per workload family. Scaling depends on which inputs grow: 100× data growth yields median runtime near 306 s, while 100× joint growth in circuits, shots, and depth reaches 4.806 × 10^7 s on the fixed HCU. HybridQC enables designers to study topology, scheduling, and workload growth before tightly integrated quantum–classical machines exist physically.

## 中文摘要
混合量子—经典系统的性能取决于量子处理器如何共享经典计算、控制器、内存和通信链路。线路仿真器和厂商测量能够揭示内核与作业行为，但对控制器瓶颈、量子容量和混合负载争用等拓扑层面的问题仍未给出答案。我们提出 HybridQC，一个面向可配置混合计算单元（HCU）的离散事件仿真器。用户指定包含经典计算、内存、控制器、量子退火（QA）与数字量子计算（DQC）设备以及链路的资源图。作业被转化为用于准备、量子执行、传输、重构和后处理的依赖阶段。有限容量与可选调度策略决定了各阶段在何处等待与重叠。服务画像使用来自 D-Wave Advantage 1 和 Advantage 2 以及 IBM Kingston、Marrakesh 和 Fez 的测量数据，将物理量子处理器占用与云端墙钟时间区分开。平均绝对百分比误差为：D-Wave 访问时间 3.92%–8.04%，IBM 量子秒 5.26%–19.01%。均衡的 10× HCU 扩展使 makespan 改善 2.19×–3.42×，而在每个负载族 20 个作业的混合负载下，策略选择会使 makespan 变化 1.80×。扩展效果取决于哪些输入在增长：数据增长 100× 时中位运行时间约为 306 s，而线路、shots 和深度共同增长 100× 时，在固定的 HCU 上达到 4.806 × 10^7 s。HybridQC 使设计者能够在紧耦合的量子—经典机器实际存在之前研究拓扑、调度和负载增长。

## 英文关键词
Hybrid quantum-classical computing, discrete-event simulation, resource contention, scheduling, performance modeling

## 中文关键词
混合量子—经典计算，离散事件仿真，资源争用，调度，性能建模

[返回 Session 20](index.md) · [返回 ATC 2026](../index.md)
