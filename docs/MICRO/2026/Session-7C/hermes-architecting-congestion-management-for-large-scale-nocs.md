---
title: "Hermes: Architecting Congestion Management for Large-Scale NoCs"
description: "MICRO 2026 · Session 7C · Hermes：面向大规模片上网络的拥塞管理架构设计"
tags:
  - "MICRO2026"
  - "Interconnect"
---

# Hermes: Architecting Congestion Management for Large-Scale NoCs

**中文标题：** Hermes：面向大规模片上网络的拥塞管理架构设计

**所属 Session：** [Session 7C](index.md) · [MICRO 2026](../index.md)

**作者：** Yang Zhang, Xu Wang, Lei Xu, Fengyuan Ren

**来源：** MICRO 2026，pp. 2529–2543；[DOI](https://doi.org/10.1109/MICRO67795.2026.00173)

## 英文摘要

With the rapid development of systems-on-chip (SoCs), networks-on-chip (NoCs) experience explosive scale growth. The high network diameter and unpredictable conflicts at intermediate nodes make congestion handling a challenging problem. Inspired by the extensively studied congestion management (CM) schemes in off-chip networks, we investigate the possibility of applying them to large-scale NoCs. Although the methodology is inspiring, we find that both detection mechanisms and control algorithms in existing CM schemes are ill-suited for on-chip requirements. The in-band detection is sluggish and unreliable, and the tentative control incurs unbearable queue fluctuations. To address this, we propose Hermes, a novel CM framework specifically architected for large-scale NoCs. By collaboratively monitoring the data path from both endpoints, double-sided congestion detection (DCD) decouples detection from data transmission, thereby providing timely and accurate visibility into network state. Empowered by DCD, decisive congestion control (DCC) regulates the system based on the deviation from the target state, ensuring fast convergence while mitigating fluctuations. Experiments demonstrate Hermes's effectiveness, and overhead evaluation confirms its on-chip practicality. Simulation on real-world workloads indicates that Hermes effectively alleviates congestion, achieving 26.5% lower network latency and reducing average and peak queue length by 56.0% and 89.9%, respectively.

## 中文摘要

随着片上系统（SoC）的快速发展，片上网络（NoC）经历了爆炸性的规模增长。高网络直径和中间节点不可预测的冲突使得拥塞处理成为一个具有挑战性的问题。受到片外网络中广泛研究的拥塞管理（CM）方案的启发，我们研究了将它们应用于大规模 NoC 的可能性。尽管该方法很鼓舞人心，但我们发现现有 CM 方案中的检测机制和控制算法都不适合片上要求。带内检测缓慢且不可靠，尝试性控制会导致难以忍受的队列波动。为了解决这个问题，我们提出了 Hermes，这是一种专门为大规模 NoC 构建的新型 CM 框架。通过协作监控两个端点的数据路径，双面拥塞检测 (DCD) 将检测与数据传输分离，从而提供及时、准确的网络状态可见性。在DCD的支持下，果断拥塞控制（DCC）根据与目标状态的偏差来调节系统，确保快速收敛，同时减轻波动。实验证明了 Hermes 的有效性，开销评估证实了其片上实用性。对实际工作负载的模拟表明，Hermes 有效缓解了拥塞，网络时延降低了 26.5%，平均和峰值队列长度分别减少了 56.0% 和 89.9%。

## 中文关键词

片上网络；互连网络；拥塞检测；拥塞控制

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7C](index.md) · [MICRO 2026 主页](../index.md)
