---
title: "Efficient ML Model Updates for Deeply Embedded Microcontrollers"
description: "EuroSys 2026 · Edge Computing, IoT & Embedded AI · Shishir G. Patil (University of California, Berkeley), Sam Kumar (University of "
tags:
  - "EuroSys2026"
  - "Edge Computing, IoT & Embedded AI"
---

# Efficient ML Model Updates for Deeply Embedded Microcontrollers

**中文标题：** 面向深度嵌入式微控制器的高效机器学习模型更新

**所属 Session：** [Session 12.2: Edge Computing, IoT & Embedded AI](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Edge Computing, IoT & Embedded AI。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Edge Computing, IoT & Embedded AI</p>
</div>

**作者**：Shishir G. Patil (University of California, Berkeley), Sam Kumar (University of California, Los Angeles), Prabal Dutta (University of California, Berkeley), Joseph Gonzalez (University of California, Berkeley)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803613)

## 英文摘要

Frequent updates to machine learning (ML) models are essential for maintaining accuracy in dynamic environments. However, updating models deployed on IoT devices with low-power microcontrollers remains challenging. Because the model, application, and system are all linked together into a monolithic program, model updates are typically accomplished through full device firmware updates (DFUs). Unfortunately, DFUs are disruptive, inflexible, energy-intensive, and inefficient. We present Minerva, an end-to-end ML model update system for microcontroller-based IoT devices. At the heart of Minerva is a new abstraction and mechanism called capsules. Capsules encapsulate ML models as pure, independent functions and decouple the model from the rest of the system. These properties enable updates that are lightweight, avoiding the time and energy costs of a DFU both in communication and flash reprogramming, and non-disruptive, eliminating the need for a full reboot. Because capsules work at the application level, they require no modifications to the underlying OS or firmware, and thus apply broadly to existing IoT systems. Minerva reduces model update time by up to 89× compared to a full DFU, and up to 73× compared to a state-of-the-art embedded OS, enabling the growing number of deeply embedded devices to receive regular model updates. Minerva is an open-source project available at https://github.com/ShishirPatil/minerva.

## 中文摘要

频繁更新机器学习（ML）模型对于在动态环境中保持精度至关重要。然而，更新部署在搭载低功耗微控制器的物联网设备上的模型仍然颇具挑战。由于模型、应用与系统都被链接进一个单体程序，模型更新通常通过完整的设备固件更新（DFU）来完成。遗憾的是，DFU 具有破坏性、不灵活、能耗高且效率低下。我们提出 Minerva，一个面向基于微控制器的物联网设备的端到端 ML 模型更新系统。Minerva 的核心是一种称为胶囊（capsule）的新抽象与机制。胶囊将 ML 模型封装为纯的、独立的函数，并将模型与系统其余部分解耦。这些特性使更新既轻量——避免 DFU 在通信与闪存重编程上的时间与能耗开销，又非破坏性——无需完整重启。由于胶囊工作在应用层，无需修改底层 OS 或固件，因此可广泛适用于现有物联网系统。与完整 DFU 相比，Minerva 将模型更新耗时最多缩短 89 倍；与最先进的嵌入式 OS 相比最多缩短 73 倍，从而使数量日益增长的深度嵌入式设备能够接收定期的模型更新。Minerva 是开源项目，地址为 https://github.com/ShishirPatil/minerva。

## 代码与研究制品

- [代码](https://github.com/ShishirPatil/minerva)（论文摘要提供）

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
