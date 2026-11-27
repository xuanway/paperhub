---
title: "EIGEN: Enabling Efficient 3DIC Interconnect with Heterogeneous Dual-Layer Network-on-Active-Interposer"
description: "HPCA 2025 · Colluding to Even the Odds"
tags:
  - "HPCA2025"
  - "Colluding to Even the Odds"
---

# EIGEN: Enabling Efficient 3DIC Interconnect with Heterogeneous Dual-Layer Network-on-Active-Interposer

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Colluding to Even the Odds。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Colluding to Even the Odds</p>
</div>

**论文链接**：
**作者**：Siyao Jia (Fudan University), Bo Jiao (Fudan University), Haozhe Zhu (Fudan University), Chixiao Chen (Fudan University), Qi Liu (Fudan University), Ming Liu (Fudan University)
**会议**：HPCA 2025

---

## 中文标题

EIGEN：以异构双层有源中介层网络实现高效 3DIC 互连

## 英文摘要

Chiplet-based 3DICs have emerged as modular solutions for large-scale, high-performance computing systems. However, unlike monolithic Network-on-Chips (NoCs), 3DICs using active interposers encounter difficulties in managing heterogeneous and high-load network traffic patterns. The emerging field of Networks-on-Active-Interposer (NOAI), independently designed from top dies’ interconnects, is desired to address these challenges by supporting flexible topologies, low-latency memory access, and reduced traffic congestion. To satisfy the requirements, we propose a heterogeneous dual-layer interconnect architecture, EIGEN, for chiplet-interposer systems, along with a reinforcement learning (RL)-based routing framework, which can provide efficient and flexible communication for chiplet-based 3DICs. EIGEN features an application-aware switch-programable interconnection layer (AspLayer) and a dynamic packet-routing interconnection layer (DynLayer) on the interposer, respectively. To optimize inter-chiplet data communication, we also develop an RL-based path routing framework tailored to this dual-layer architecture. The RL framework’s state space includes topology, network, and memory metrics, while the RL reward is set as the product of average packet latency and link utilization. The effectiveness of EIGEN is demonstrated through different applications where CPU, GPU, and AI accelerator chiplets are integrated via NOAI. Simulation results show that the proposed EIGEN achieves up to 67.16% latency reduction, 53.89% hops reduction and 11.21% runtime reduction compared to the state-of-the-art (SOTA) chiplets interconnect architectures. Furthermore, sensitivity analysis of network scaling shows that the EIGEN architecture and framework exhibit strong scalability, with latency reduction of 20.96% to 52.77% and hop reduction of 19.72% to 43.41% as the system scales from 4×4 to 32×32 chiplets.

## 中文摘要

基于芯粒的 3DIC 已成为大规模高性能计算系统的模块化方案。然而，与单片式片上网络（NoC）不同，使用有源中介层的 3DIC 在管理异构且高负载的网络流量模式方面遇到困难。新兴的有源中介层上网络（NOAI）领域与顶层 die 的互连独立设计，被期望通过支持灵活拓扑、低延迟内存访问与减少流量拥塞来应对这些挑战。为满足这些需求，我们为芯粒-中介层系统提出一种异构双层互连架构 EIGEN，以及一个基于强化学习（RL）的路由框架，可为基于芯粒的 3DIC 提供高效灵活的通信。EIGEN 在中介层上分别设有应用感知的可切换编程互连层（AspLayer）与动态分组路由互连层（DynLayer）。为优化芯粒间数据通信，我们还开发了一个为这种双层架构量身定制的基于 RL 的路径路由框架。RL 框架的状态空间包含拓扑、网络与内存指标，而 RL 奖励设为平均分组时延与链路利用率的乘积。EIGEN 的有效性通过集成 CPU、GPU 与 AI 加速器芯粒并经 NOAI 互连的不同应用得到验证。仿真结果表明，与最先进的芯粒互连架构相比，所提出的 EIGEN 最高实现 67.16% 的时延降低、53.89% 的跳数减少与 11.21% 的运行时间降低。此外，网络规模扩展的敏感性分析表明，EIGEN 架构与框架展现出很强的可扩展性，当系统从 4×4 芯粒扩展到 32×32 芯粒时，时延降低 20.96% 至 52.77%，跳数减少 19.72% 至 43.41%。
