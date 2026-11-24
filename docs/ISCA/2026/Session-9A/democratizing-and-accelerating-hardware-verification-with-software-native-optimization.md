---
title: "Democratizing and Accelerating Hardware Verification with Software-Native Optimization"
description: "ISCA 2026 · Session 9A · Democratizing and Accelerating Hardware Verification with Software-Native Optimization"
tags:
  - "ISCA2026"
  - "Session 9A"
  - "Verification and Robustness"
---

# Democratizing and Accelerating Hardware Verification with Software-Native Optimization

**中文标题：** 以软件原生优化实现硬件验证的民主化与加速

**所属 Session：** [Session 9A](index.md) · [ISCA 2026](../index.md)

**作者：** Yunlong Xie, Zhicheng Yao, Fangyuan Song, Jincheng Liu, Junyue Wang, Haojin Tang, Lu Chen, Yinan Xu, Ziqing Zhang, Ziyuan Gao, Duan Yu, Hongtao Zhou, Jiayi Rao, Junyu Yue, Xiaolong Li, Yunqi Lu, Zechen Yang, Hang Zhu, Shan Liu, Xu An, Qi Ge, Jiuyue Ma, Jianyi Meng, Kan Shi, Dan Tang, Tianyi Liu, Sa Wang, Yungang Bao

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Hardware verification accounts for a substantial portion of chip development effort, and improving its efficiency remains an ongoing challenge. Traditional hardware verification emphasizes reuse of verification assets, while emerging software-based frameworks embed verification in general-purpose programming languages to improve usability and attract a broader range of developers. However, these frameworks remain simulator-centric, relying heavily on simulator-controlled timing, transaction lifecycles, and observability, which limits further democratization and acceleration of verification. We present UnityChip Verification (UCV), a software-native verification platform that recenters event scheduling and control within an explicit software event loop while treating simulators as pluggable backends. UCV identifies and addresses three key challenges: the programming paradigm gap between software and hardware timing, the difficulty of composing established verification components, and the performance–debuggability trade-off. Evaluation on XiangShan and RocketChip shows that UCV improves both acceleration and democratization. UCV delivers up to 25× faster runtime and 76% lower memory usage than Cocotb, and achieves 16.6% higher throughput when reusing existing components. In community deployments, newcomers with software backgrounds contributed meaningful verification artifacts, with 26.3% producing runnable tests and 11 collectively uncovering 30 previously unknown bugs, indicating that UCV significantly lowers the entry barrier and broadens participation.

## 中文摘要

硬件验证占芯片开发工作量的很大一部分，提高其效率仍然是一项持续的挑战。传统的硬件验证强调验证资产的重用，而新兴的基于软件的框架将验证嵌入通用编程语言，以提高可用性并吸引更广泛的开发者。然而，这些框架仍然以仿真器为中心，严重依赖仿真器控制的时序、事务生命周期和可观测性，这限制了验证的进一步民主化和加速。我们提出 UnityChip Verification（UCV），一个软件原生的验证平台，它将事件调度和控制重新置于显式的软件事件循环中，同时将仿真器视为可插拔的后端。UCV 识别并解决了三个关键挑战：软件与硬件时序之间的编程范式差距、组合既有验证组件的困难，以及性能与可调试性之间的权衡。在香山和 RocketChip 上的评估表明，UCV 同时提升了加速效果和民主化程度。与 Cocotb 相比，UCV 运行时最高快 25 倍，内存占用降低 76%，在重用现有组件时吞吐量提高 16.6%。在社区部署中，具有软件背景的新手贡献了有意义的验证产物，其中 26.3% 的人产出了可运行的测试，11 人共同发现了 30 个此前未知的缺陷，表明 UCV 显著降低了入门门槛并扩大了参与范围。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：Makiras/UnityChipExp](https://github.com/Makiras/UnityChipExp)
- [实验材料归档（Zenodo 19447034）](https://zenodo.org/records/19447034)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 9A](index.md) · [返回 ISCA 2026](../index.md)
