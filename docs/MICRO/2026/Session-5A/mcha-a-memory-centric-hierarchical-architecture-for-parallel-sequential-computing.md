---
title: "MCHA: A Memory-Centric Hierarchical Architecture for Parallel-Sequential Computing"
description: "MICRO 2026 · Session 5A · MCHA：面向并行与顺序计算的内存中心分层架构"
tags:
  - "MICRO2026"
---

# MCHA: A Memory-Centric Hierarchical Architecture for Parallel-Sequential Computing

**中文标题：** MCHA：面向并行与顺序计算的内存中心分层架构

**所属 Session：** [Session 5A](index.md) · [MICRO 2026](../index.md)

**作者：** Daijing Shi, Hongxiao Zhao, Yihan Fu, Zhan Chen, Jiayi Li, Yihang Zhu, Anjunyi Fan, Yaoyu Tao, Yuchao Yang, Bonan Yan

**来源：** MICRO 2026，pp. 1578–1594；[DOI](https://doi.org/10.1109/MICRO67795.2026.00115)

## 英文摘要

Emerging workloads, such as Multi-Agent Reinforcement Learning (MARL), large-scale neuromorphic computing, and probabilistic graphical models, intrinsically exhibit parallel-sequential computing patterns. While these tasks demand massive parallelism to achieve high throughput, they are severely bottlenecked by irregular data access patterns centralized to main memory. Consequently, conventional architectures face fundamental limitations when executing these workloads, primarily manifesting as global buffer saturation and memory-bound bottlenecks. To address these challenges, we propose the Memory-Centric Hierarchical Architecture (MCHA), a reconfigurable hardware solution tailored for parallel-sequential execution. MCHA leverages a hierarchical communication strategy that facilitates distributed, inter-core data routing, thereby significantly reducing the bandwidth burden on the global memory. Complementing the hardware, MCHA introduces a novel parallel-sequential programming model that utilizes event-driven conditional triggers to effectively hide data transmission latency within the execution pipeline. We benchmark MCHA against a diverse suite of parallel-sequential tasks, including MARL, Macaque visual cortical areas model, and Markov random fields. Validated through our open-source, cycle-accurate simulator, MCHA demonstrates performance speedups ranging from 153.06× to 2456.96× over NVIDIA A100 GPUs on MARL workloads, while maintaining robust programming flexibility across other application domains. Furthermore, the architecture successfully reduces main memory access from 96% to 5.44%. When synthesized in a 28 nm process, the MCHA implementation occupies an area footprint of 2.92 mm2 and consumes 115.36 mW of power at 200 MHz. MCHA is open-sourced at https://github.com/carabdis/MCHA.

## 中文摘要

新兴工作负载，例如多智能体强化学习 (MARL)、大规模神经形态计算和概率图形模型，本质上表现出并行顺序计算模式。虽然这些任务需要大规模并行性才能实现高吞吐量，但它们受到集中到主内存的不规则数据访问模式的严重瓶颈。因此，传统架构在执行这些工作负载时面临基本限制，主要表现为全局缓冲区饱和和内存限制瓶颈。为了应对这些挑战，我们提出了以内存为中心的分层架构（MCHA），这是一种专为并行顺序执行而定制的可重新配置的硬件解决方案。 MCHA 利用分层通信策略，促进分布式核心间数据路由，从而显着减轻全局内存的带宽负担。作为硬件的补充，MCHA 引入了一种新颖的并行顺序编程模型，该模型利用事件驱动的条件触发器来有效隐藏执行管道内的数据传输时延。我们针对一系列不同的并行顺序任务对 MCHA 进行基准测试，包括 MARL、猕猴视觉皮层区域模型和马尔可夫随机场。通过我们的开源、周期精确模拟器进行验证，MCHA 在 MARL 工作负载上的性能比 NVIDIA A100 GPU 提高了 153.06 倍到 2456.96 倍，同时在其他应用领域保持了强大的编程灵活性。此外，该架构成功地将主内存访问从 96% 减少到 5.44%。当在 28 nm 工艺中综合时，MCHA 实现占用的面积为 2.92 mm2，在 200 MHz 时消耗 115.36 mW 的功率。 MCHA 在 https://github.com/carabdis/MCHA 上开源。

## 中文关键词

可重构架构；以内存为中心；可扩展架构；整体同步并行；数据驱动编程

## 代码与研究制品

- 代码仓库：[https://github.com/carabdis/MCHA](https://github.com/carabdis/MCHA)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 5A](index.md) · [MICRO 2026 主页](../index.md)
