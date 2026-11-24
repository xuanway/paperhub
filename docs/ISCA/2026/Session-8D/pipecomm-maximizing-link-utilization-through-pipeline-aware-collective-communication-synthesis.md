---
title: "PipeComm: Maximizing Link Utilization through Pipeline-Aware Collective Communication Synthesis"
description: "ISCA 2026 · Session 8D · PipeComm: Maximizing Link Utilization through Pipeline-Aware Collective Communication Synthesis"
tags:
  - "ISCA2026"
  - "Session 8D"
  - "HPC"
---

# PipeComm: Maximizing Link Utilization through Pipeline-Aware Collective Communication Synthesis

**中文标题：** PipeComm: 通过流水线感知的集合通信合成最大化链路利用率

**所属 Session：** [Session 8D](index.md) · [ISCA 2026](../index.md)

**作者：** Ruifan Xu, Yuze Luo, Yuhao Meng, Size Zheng, Meng Li, Yun Liang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Efficient collective communication is crucial for distributed training. While recent topology-aware synthesis approaches attempt to optimize communication based on the network topology, they struggle with heterogeneous environments where links exhibit distinct bandwidths and asymmetric connections. The main inefficiency arises from single-round communication: toward the end of a communication phase, only a few remaining transfers occupy limited links, leaving most network channels idle. Furthermore, existing methods fail to handle the congestion that naturally occurs under overlapping execution, leading to significant bandwidth underutilization. To address these challenges, we propose PipeComm, a pipeline-aware communication synthesis framework that maximizes bandwidth utilization by intelligently overlapping multiple data chunks. By explicitly modeling pipeline behavior, our method enables congestion-free scheduling across iterations and efficiently utilizes heterogeneous links. We develop an optimal synthesis method for constructing high-quality communication patterns and introduce a complementary incremental strategy that significantly improves scalability for large topologies. Experimental results show that the optimal strategy achieves over a 1.39× speedup compared to the state-of-the-art communication methods. Moreover, PipeComm supports diverse collective operations, demonstrating both efficiency and generality.

## 中文摘要

高效的集合通信对分布式训练至关重要。尽管近期的拓扑感知合成方法尝试基于网络拓扑来优化通信，但它们在链路带宽各异、连接不对称的异构环境中表现不佳。主要的低效源于单轮通信：在通信阶段接近尾声时，只剩少量传输占用有限的链路，而大多数网络通道处于空闲状态。此外，现有方法无法处理重叠执行下自然产生的拥塞，导致带宽利用率显著不足。为应对这些挑战，我们提出 PipeComm，一个流水线感知的通信合成框架，它通过智能地重叠多个数据块来最大化带宽利用率。通过显式建模流水线行为，我们的方法能够跨迭代实现无拥塞调度，并高效利用异构链路。我们开发了一种最优合成方法以构建高质量的通信模式，并引入一种互补的增量策略，显著提升大型拓扑的可扩展性。实验结果表明，相较最先进的通信方法，最优策略实现了超过 1.39× 的加速。此外，PipeComm 支持多种集合操作，兼具高效性与通用性。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：pku-liang/pipecomm](https://github.com/pku-liang/pipecomm)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 8D](index.md) · [返回 ISCA 2026](../index.md)
