---
title: "When RDMA Goes Long-Haul: Characterization, Modeling, and Verbs-Level Emulation with Implications for Federated Learning"
description: "HPDC 2026 · Session 11 — Communication, Workflows & Sustainability"
tags:
  - "HPDC2026"
  - "Session 11"
  - "Communication, Workflows & Sustainability"
---

# When RDMA Goes Long-Haul: Characterization, Modeling, and Verbs-Level Emulation with Implications for Federated Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 11 — Communication, Workflows & Sustainability（2026年7月16日 13:30–14:30 · Session Chair：Mehmet Koyuturk）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 11</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807582)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#LiCL26](https://dblp.org/db/conf/hpdc/hpdc2026.html#LiCL26)

**作者**：Yuke Li, Zhonghao Chen, Xiaoyi Lu

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 11 — Communication, Workflows & Sustainability（2026年7月16日 13:30–14:30 · Session Chair：Mehmet Koyuturk）

---

## 英文摘要

Long-haul Remote Direct Memory Access (RDMA) is rapidly emerging as a viable mechanism for extending high-performance communication beyond traditional datacenter environments into wide-area networks (WANs). However, increased round-trip time (RTT) fundamentally alters RDMA behavior, shifting execution from open-loop injection toward a closed-loop, window-limited regime governed by resource constraints and concurrency effects. Consequently, performance characteristics diverge from established datacenter assumptions, rendering existing models insufficient for predicting performance at WAN scale. Understanding these dynamics requires real-world characterization, yet geographically distributed long-haul testbeds remain expensive, scarce, and difficult to reproduce. To address this challenge, we present the first systematic characterization of real long-haul RDMA networks through deployment on ESnet. Guided by these measurements, we propose a window-aware α–β–γ formulation that explicitly models RTT-dependent window limitations and multi-queue-pair concurrency, capturing the closed-loop performance regime of long-haul RDMA. We further develop a verbs-level long-haul RDMA emulator that enables high-fidelity experimentation without requiring physical WAN-scale RDMA deployment, and matches native long-haul bandwidth within 5.7% maximum error. Using federated learning as a representative communication-intensive workload, we demonstrate that our framework accurately predicts performance, reproduces complex saturation behavior observed in native deployments, and exposes new scaling implications for distributed training over WAN-scale RDMA environments.

## 中文摘要

长距离远程直接内存访问（RDMA）正迅速成为一种可行机制，可将高性能通信从传统数据中心环境扩展到广域网（WAN）。然而，往返时间（RTT）的增加从根本上改变了 RDMA 行为，使执行从开环注入转向由资源约束与并发效应主导的闭环、窗口受限状态。因此，其性能特征偏离了既有的数据中心假设，使现有模型不足以预测 WAN 规模的性能。理解这些动态需要真实世界的刻画，但地理分布的长距离测试床仍然昂贵、稀缺且难以复现。为应对这一挑战，我们通过在 ESnet 上部署，首次对真实长距离 RDMA 网络进行了系统刻画。在这些测量指导下，我们提出窗口感知的 α–β–γ 公式，显式建模依赖 RTT 的窗口限制与多队列对并发，刻画长距离 RDMA 的闭环性能状态。我们进一步开发了一个 verbs 级长距离 RDMA 模拟器，无需物理的 WAN 规模 RDMA 部署即可进行高保真实验，且与原生长距离带宽的最大误差在 5.7% 以内。以联邦学习作为代表性通信密集负载，我们证明该框架能准确预测性能、复现原生部署中观察到的复杂饱和行为，并揭示在 WAN 规模 RDMA 环境下分布式训练的新扩展性影响。

## 英文关键词

Long-Haul RDMA, Performance, Federated Learning

## 中文关键词

长距离 RDMA，性能，联邦学习

---

[← 返回 Session 11 — Communication, Workflows & Sustainability](index.md)
