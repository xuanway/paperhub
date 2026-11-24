---
title: "PhaseWeave: Phase-Aware Execution on Heterogeneous Chiplet Architectures for Datacenters"
description: "ISCA 2026 · Session 7A · PhaseWeave: Phase-Aware Execution on Heterogeneous Chiplet Architectures for Datacenters"
tags:
  - "ISCA2026"
  - "Session 7A"
  - "Emerging Technologies: Chiplet, Wafer-Scale, etc."
---

# PhaseWeave: Phase-Aware Execution on Heterogeneous Chiplet Architectures for Datacenters

**中文标题：** PhaseWeave: 面向数据中心的异构 chiplet 架构上的阶段感知执行

**所属 Session：** [Session 7A](index.md) · [ISCA 2026](../index.md)

**作者：** Joshua Kim, Chaojie Zhang, Íñigo Goiri, Christopher J. Rossbach, Jovan Stojkovic

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Modern datacenter applications execute in clearly distinct phases, driven by modular microservice architectures, auxiliary “datacenter tax” operations, and diverse execution blocks within the service logic. Our characterization of datacenter workloads reveals that these millisecond-scale phases exhibit recurring patterns and have varying sensitivities to hardware resources such as core frequency, network bandwidth, and memory bandwidth. This fine-grained intra-application heterogeneity leads to inefficiencies when running on traditional homogeneous server architectures, which cannot adapt to dynamic and phase-specific resource demands. As a result, datacenter operators face a trade-off between overprovisioning resources and suffering performance bottlenecks during critical phases. We propose PhaseWeave, a heterogeneous multiple-chiplet server architecture where different chiplet types are optimized for different workload phases (e.g., compute-, memory-, or network-phases). PhaseWeave transparently predicts changes in program phases using hardware counters and the distribution of system calls. Then, it uses OS signals to migrate workloads to chiplets that are best suited for the next phase. By dynamically and transparently steering execution across specialized chiplets, PhaseWeave improves resource utilization and performance without requiring changes to user code. Full-system simulations with a diverse set of datacenter workloads show that PhaseWeave reduces tail latency of datacenter applications by 65% at high loads, increases throughput by 1.6×, and improves Performance/Watt by 1.9× compared to homogeneous iso-area baseline.

## 中文摘要

现代数据中心应用以明显不同的阶段运行，这源于模块化微服务架构、辅助性的“数据中心税”操作以及服务逻辑中多样的执行块。我们对数据中心工作负载的刻画表明，这些毫秒级阶段呈现出反复出现的模式，并且对核心频率、网络带宽和内存带宽等硬件资源具有不同的敏感度。这种细粒度的应用内异构性导致在传统同构服务器架构上运行时效率低下，因为后者无法适应动态的、阶段特定的资源需求。因此，数据中心运营者面临两难：要么过度配置资源，要么在关键阶段遭遇性能瓶颈。我们提出 PhaseWeave，一种异构多 chiplet 服务器架构，其中不同的 chiplet 类型针对不同的工作负载阶段（如计算阶段、内存阶段或网络阶段）进行优化。PhaseWeave 利用硬件计数器和系统调用的分布透明地预测程序阶段的变化，然后通过操作系统信号将工作负载迁移到最适合下一阶段的 chiplet 上。通过在专用 chiplet 之间动态、透明地引导执行，PhaseWeave 无需修改用户代码即可提升资源利用率和性能。针对多种数据中心工作负载的全系统仿真表明，与同构等面积基线相比，PhaseWeave 在高负载下将数据中心应用的尾延迟降低 65%，吞吐量提升 1.6×，性能/瓦特提升 1.9×。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：UTCS-CASCADE/PhaseWeave](https://github.com/UTCS-CASCADE/PhaseWeave)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7A](index.md) · [返回 ISCA 2026](../index.md)
