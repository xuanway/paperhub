---
title: "Atlas: Towards Real-Time Verification in Large-Scale Networks via a Native Distributed Architecture"
description: "EuroSys 2025 · Network - Van Oldebarneveldt · Mingxiao Ma (State Key Laboratory of Networking and Switching Technology, Beijin"
tags:
  - "EuroSys2025"
  - "Network - Van Oldebarneveldt"
---

# Atlas: Towards Real-Time Verification in Large-Scale Networks via a Native Distributed Architecture

**中文标题：** 通过原生分布式架构实现大规模网络的近实时验证

**所属 Session：** [Session 10.1: Network](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Network - Van Oldebarneveldt。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Network - Van Oldebarneveldt</p>
</div>

**作者**：Mingxiao Ma (State Key Laboratory of Networking and Switching Technology, Beijing University of Post and Telecommunication), Yuehan Zhang (State Key Laboratory of Networking and Switching Technology, Beijing University of Post and Telecommunication), Jingyu Wang (State Key Laboratory of Networking and Switching Technology, Beijing University of Post and Telecommunication), Bo He (State Key Laboratory of Networking and Switching Technology, Beijing University of Post and Telecommunication), Chenyang Zhao (State Key Laboratory of Networking and Switching Technology, Beijing University of Post and Telecommunication), Qi Qi (State Key Laboratory of Networking and Switching Technology, Beijing University of Post and Telecommunication), Zirui Zhuang (State Key Laboratory of Networking and Switching Technology, Beijing University of Post and Telecommunication), Haifeng Sun (State Key Laboratory of Networking and Switching Technology, Beijing University of Post and Telecommunication), Lingqi Guo (State Key Laboratory of Networking and Switching Technology, Beijing University of Post and Telecommunication), Yuebin Guo (State Key Laboratory of Networking and Switching Technology, Beijing University of Post and Telecommunication), Gong Zhang (Huawei Technologies), Jianxin Liao (State Key Laboratory of Networking and Switching Technology, Beijing University of Posts and Telecommunications)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717494)

## 英文摘要

Data plane verification (DPV) can be critical in ensuring the network operates correctly. To be useful in practice, they need to be: (1) fast so as to prevent significant packet loss or security violations; (2) scalable so as to accommodate today’s large-scale network architecture. Current DPV tools struggle to meet these requirements due to their centralized architecture. To be concrete, there is a bottleneck for a single-point server to perform real-time DPV tasks. Furthermore, a single-point server makes it hard to collect real-time data plane updates from every device in large-scale networks.

This paper proposes Atlas, a native distributed data plane verification (DPV) solution, which systematically solves its scalability problem and improves its real-time performance. To achieve this, (1) Atlas designs a hierarchical distributed architecture for DPV in large-scale networks. (2) Atlas proposes a native approach to maximize the parallelism of the architecture. Both dataset-driven simulation experiments and deployments in the wild demonstrate that Atlas is capable of fast and scalable distributed verification. The advantages offered by Atlas continue to expand as network sizes increase. Compared to state-of-the-art solutions, Atlas is 2-7× faster while keeping each component lightweight.

## 中文摘要

数据平面验证（DPV）对于确保网络正确运行至关重要。要在实践中发挥作用，它们需要：(1) 快速，以避免大量丢包或安全违规；(2) 可扩展，以适应当今的大规模网络架构。当前的 DPV 工具由于采用集中式架构，难以满足这些要求。具体而言，单点服务器执行实时 DPV 任务存在瓶颈。此外，单点服务器难以从大规模网络中的每台设备实时收集数据平面更新。

本文提出 Atlas，一种原生分布式数据平面验证（DPV）方案，它系统地解决了 DPV 的可扩展性问题并提升了实时性能。为此，(1) Atlas 为大规模网络中的 DPV 设计了层次化分布式架构；(2) Atlas 提出一种原生方法来最大化该架构的并行度。数据集驱动的仿真实验和真实环境部署均表明，Atlas 能够实现快速且可扩展的分布式验证。随着网络规模增大，Atlas 的优势持续扩大。与最先进的方案相比，Atlas 快 2–7 倍，同时每个组件保持轻量。

**英文关键词：** Network verification, Distributed verification

**中文关键词：** 网络验证、分布式验证

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
