---
title: "Achieving Fairness Generalizability for Learning-based Congestion Control with Jury"
description: "EuroSys 2025 · Network/Network Congestion Control · Han Tian (University of Science and Technology of China), Xudong Liao (Hong Kong"
tags:
  - "EuroSys2025"
  - "Network/Network Congestion Control"
---

# Achieving Fairness Generalizability for Learning-based Congestion Control with Jury

**中文标题：** 利用 Jury 实现基于学习的拥塞控制公平性泛化

**所属 Session：** [Session 3.2: Network/Network Congestion Control](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Network/Network Congestion Control。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Network/Network Congestion Control</p>
</div>

**作者**：Han Tian (University of Science and Technology of China), Xudong Liao (Hong Kong University of Science and Technology), Decang Sun (Hong Kong University of Science and Technology), Chaoliang Zeng (BitIntelligence), Yilun Jin (The Hong Kong University of Science and Technology), Junxue Zhang (Hong Kong University of Science and Technology), Xinchen Wan (Hong Kong University of Science and Technology), Zilong Wang (Hong Kong University of Science and Technology), Yong Wang (Hong Kong University of Science and Technology), Kai Chen (Hong Kong University of Science and Technology)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696065)

## 英文摘要

Internet congestion control (CC) has long posed a challenging control problem in networking systems, with recent approaches increasingly incorporating deep reinforcement learning (DRL) to enhance adaptability and performance. Despite promising, DRL-based CC schemes often suffer from poor fairness, particularly when applied to network environments unseen during training. This paper introduces Jury, a novel DRL-based CC scheme designed to achieve fairness generalizability. At its heart, Jury decouples the fairness control from the principal DRL model with two design elements: i) By transforming network signals, it provides a universal view of network environments among competing flows, and ii) It adopts a post-processing phase to dynamically module the sending rate based on flow bandwidth occupancy estimation, ensuring large flows behave more conservatively and smaller flows more aggressively, thus achieving a fair and balanced bandwidth allocation. We have fully implemented Jury, and extensive evaluations demonstrate its robust convergence properties and high performance across a broad spectrum of both emulated and real-world network conditions.

## 中文摘要

互联网拥塞控制长期以来一直是网络系统中的一个具有挑战性的控制问题，近期的方法越来越多地引入深度强化学习（DRL）以增强适应性和性能。尽管前景可期，基于 DRL 的拥塞控制方案往往公平性较差，尤其是应用于训练期间未见过的网络环境时。本文提出 Jury，一种旨在实现公平性泛化的新型基于 DRL 的拥塞控制方案。其核心是通过两个设计要素将公平性控制与主 DRL 模型解耦：i）通过变换网络信号，为竞争流之间提供网络环境的统一视图；ii）采用后处理阶段，基于流带宽占用估计动态调制发送速率，确保大流行为更保守、小流更激进，从而实现公平且均衡的带宽分配。我们完整实现了 Jury，大量评估表明其在广泛的模拟和真实网络条件下都具有稳健的收敛性和高性能。

**英文关键词：** Congestion Control, Reinforcement Learning, Transport Protocol

**中文关键词：** 拥塞控制、强化学习、传输协议

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
