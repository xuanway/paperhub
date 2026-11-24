# EntangledEdge: A Distributed System for Orbital Quantum Sensing and Learning

**中文标题**：EntangledEdge：面向在轨量子感知与学习的分布式系统

**所属 Session**：[Session 20: Quantum Computing](index.md) · [ATC 2026](../index.md)

**作者**：Mohammad Abrarul Hasanat (University of Utah), Amit Samanta (University of Utah), Jason Ludmir (Rice University), Tirthak Patel (Rice University), Rohan Basu Roy (University of Utah)

## 英文摘要
An orbital quantum sensor is more precise than classical and holds its information in a quantum state’s superposition and entanglement, which classical measurement collapses. Learning on quantum-sensed data therefore requires a distributed system in which the data stay quantum from sensor to inference. We present EntangledEdge, the first system architecture to unify orbital quantum sensing and learning end-to-end, with a quantum data plane and a classical control plane. It routes each event to a channel-matched model in a capacity-diverse bank, adapts its detection threshold without labels, and aggregates across stations by hardware fidelity. Evaluated with a hybrid prototype (real quantum processors, simulated orbit-to-ground link) over satellite telemetry, EntangledEdge achieves high-quality inference at bounded per-event cost, improves quantum processor utilization, and scales with fleet size.

## 中文摘要
在轨量子传感器比经典传感器更精确，它把信息保存在量子态的叠加与纠缠之中，而经典测量会使这种状态坍缩。因此，对量子感知数据进行学习需要一个数据从传感器到推理始终保持量子态的分布式系统。我们提出 EntangledEdge，这是首个端到端统一在轨量子感知与学习的系统架构，包含量子数据平面和经典控制平面。它把每个事件路由到容量多样化模型库中与其信道匹配的模型，在无标签的情况下自适应调整检测阈值，并按硬件保真度在站点之间进行聚合。我们使用混合原型（真实量子处理器、模拟的星地链路）在卫星遥测数据上评估，EntangledEdge 在有界的单事件开销下实现了高质量推理，提升了量子处理器利用率，并可随星座规模扩展。

## 英文关键词
Orbital Computing, Quantum Computing, Quantum Sensing, Edge Computing, Distributed Learning

## 中文关键词
在轨计算，量子计算，量子感知，边缘计算，分布式学习

[返回 Session 20](index.md) · [返回 ATC 2026](../index.md)
