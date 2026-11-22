---
title: "Synapse: Decoupling Protocol, Topology, and Policy for Automated Synthesis of Coherence Controllers"
description: "MICRO 2026 · Session 2C · Synapse：解耦协议、拓扑与策略，实现一致性控制器自动综合"
tags:
  - "MICRO2026"
---

# Synapse: Decoupling Protocol, Topology, and Policy for Automated Synthesis of Coherence Controllers

**中文标题：** Synapse：解耦协议、拓扑与策略，实现一致性控制器自动综合

**所属 Session：** [Session 2C](index.md) · [MICRO 2026](../index.md)

**作者：** Nicolò Carpentieri, Anatole Lefort, David Schall, Julian Pritzi, Pramod Bhatotia

**来源：** MICRO 2026，pp. 691–706；[DOI](https://doi.org/10.1109/MICRO67795.2026.00060)

## 英文摘要

Designing cache coherence protocols (CCPs) is a highly complex task: modern heterogeneous systems impose distinct constraints on protocols, topologies, and caching policies, and this challenge will only intensify as coherent interconnects push cache coherence beyond chip boundaries toward rack-scale deployments. We propose Synapse, a methodology for synthesizing cache coherence controllers grounded in a key observation: any controller's state machine is fully determined by three orthogonal constituents: protocol specification, system topology, and caching policies. Central to our approach is an abstract controller model that decouples coherence logic from architectural constraints via two protocol-agnostic building blocks, a caching client and manager, enabling automated derivation of controllers for arbitrarily complex configurations. Synapse realizes this through a fully automated synthesis pipeline with a declarative DSL, validates the correctness of the synthesized FSMs for liveness and safety properties, and generates gem5-based implementations for rapid design-space exploration. In our evaluation, Synapse successfully synthesizes diverse protocol variants across SMP, NUMA, multi-host CXL, and heterogeneous chiplet-based SoC scenarios, matching handwritten implementations within 1.0% performance on average. Targeting diverse architectures Synapse surfaces key protocol-policy interactions, offering a systematic framework for designing coherence controllers in increasingly complex environments.

## 中文摘要

设计缓存一致性协议 (CCP) 是一项高度复杂的任务：现代异构系统对协议、拓扑和缓存策略施加了明显的约束，并且随着一致性互连将缓存一致性推向机架规模部署之外的芯片边界，这一挑战只会加剧。我们提出了 Synapse，一种基于关键观察的综合缓存一致性控制器的方法：任何控制器的状态机完全由三个正交组成部分决定：协议规范、系统拓扑和缓存策略。我们方法的核心是一个抽象控制器模型，它通过两个与协议无关的构建块（缓存客户端和管理器）将一致性逻辑与架构约束解耦，从而能够自动派生任意复杂配置的控制器。 Synapse 通过带有声明性 DSL 的全自动合成管道实现了这一点，验证合成 FSM 的活性和安全属性的正确性，并生成基于 gem5 的实现以进行快速设计空间探索。在我们的评估中，Synapse 成功综合了 SMP、NUMA、多主机 CXL 和基于异构 Chiplet 的 SoC 场景的多种协议变体，平均性能与手写实现相差 1.0%。针对不同的架构，Synapse 展示了关键的协议策略交互，为在日益复杂的环境中设计一致性控制器提供了一个系统框架。

## 中文关键词

缓存一致性协议；协议综合；CXL；非均匀内存访问；异构系统；设计空间探索

## 代码与研究制品

- 代码仓库：[https://github.com/TUM-DSE/Synapse](https://github.com/TUM-DSE/Synapse)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21539116](https://doi.org/10.5281/zenodo.21539116)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2C](index.md) · [MICRO 2026 主页](../index.md)
