---
title: "RoboRebound: Multi-Robot System Defense with Bounded-Time Interaction"
description: "EuroSys 2025 · Fault Tolerance and Consensus · Neeraj Gandhi (University of Pennsylvania), Yifan Cai (University of Pennsylvani"
tags:
  - "EuroSys2025"
  - "Fault Tolerance and Consensus"
---

# RoboRebound: Multi-Robot System Defense with Bounded-Time Interaction

**中文标题：** 具有有界交互时间的多机器人系统防御

**所属 Session：** [Session 2.1: Fault Tolerance and Consensus](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Fault Tolerance and Consensus。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Fault Tolerance and Consensus</p>
</div>

**作者**：Neeraj Gandhi (University of Pennsylvania), Yifan Cai (University of Pennsylvania), Andreas Haeberlen (University of Pennsylvania), Linh Thi Xuan Phan (University of Pennsylvania)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696079)

## 英文摘要

Byzantine Fault Tolerance (BFT) is a classic technique for defending distributed systems against a wide range of faults and attacks. However, existing solutions are designed for systems where nodes can interact only by exchanging messages. They are not directly applicable to systems where nodes have sensors and actuators and can also interact in the physical world – perhaps by blocking each other’s path or by crashing into each other.

In this paper, we take a first stab at extending BFT to this larger class of systems. We focus on multi-robot systems (MRS), an emerging technology that is increasingly being deployed for applications such as target tracking, warehouse logistics, and exploration. An MRS can consist of dozens of interacting robots and is thus a bona-fide distributed system. The classic masking guarantee is not practical in a MRS, but we propose a variant called bounded-time interaction that can be implemented, and we present an algorithm that achieves it, in combination with a few small hardware tweaks. We built a simulator and prototyped wheeled robots to show that our algorithm is effective, and that it has a reasonable overhead.

## 中文摘要

拜占庭容错（BFT）是保护分布式系统抵御各种故障和攻击的经典技术。然而，现有解决方案是针对节点只能通过交换消息进行交互的系统设计的。它们不能直接适用于节点拥有传感器和执行器、并且还能在物理世界中交互（例如通过阻挡彼此路径或相互碰撞）的系统。

在本文中，我们首次尝试将 BFT 扩展到这一更大类别的系统。我们聚焦多机器人系统（MRS），这是一种新兴技术，正越来越多地部署于目标跟踪、仓储物流和探索等应用中。一个 MRS 可能由数十个相互交互的机器人组成，因此是名副其实的分布式系统。经典的遮蔽保证在 MRS 中并不实用，但我们提出了一种可实现的变体，称为有界时间交互，并提出了一个实现该变体的算法，同时结合少量硬件调整。我们构建了模拟器并制作了轮式机器人原型，以表明我们的算法是有效的，并且具有合理的开销。

**英文关键词：** Security, Robotics, Cyber-physical systems

**中文关键词：** 安全、机器人学、信息物理系统

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
