---
title: "CREATE: Cross-Layer Resilience Characterization and Optimization for Efficient yet Reliable Embodied AI Systems"
description: "ASPLOS 2026 · Session 6A · CREATE：面向高效且可靠的具身智能系统的跨层韧性刻画与优化"
tags:
  - "ASPLOS2026"
  - "Session 6A"
  - "Neural Network Acceleration"
---

# CREATE: Cross-Layer Resilience Characterization and Optimization for Efficient yet Reliable Embodied AI Systems

**中文标题：** CREATE：面向高效且可靠的具身智能系统的跨层韧性刻画与优化

**所属 Session：** [Session 6A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Tong Xie (Peking University), Yijiahao Qi (Peking University), Jinqi Wen (Peking University), Zishen Wan (Georgia Tech), Yanchi Dong (Peking University), Zihao Wang (Peking University), Shaofei Cai (Peking University), Yitao Liang (Peking University), Tianyu Jia (Peking University), Yuan Wang (Peking University), Runsheng Wang (Peking University), Meng Li (Peking University)

**单位：** Peking University；Georgia Tech

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790147) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Embodied Artificial Intelligence (AI) has recently attracted significant attention as it bridges AI with the physical world. Modern embodied AI systems often combine a Large Language Model (LLM)-based planner for high-level task planning and a reinforcement learning (RL)-based controller for low-level action generation, enabling embodied agents to tackle complex tasks in real-world environments. However, deploying embodied agents remains challenging due to their high computation requirements, especially for battery-powered local devices. Although techniques like lowering operating voltage can improve energy efficiency, they can introduce bit errors and result in task failures. rs for synergistic energy-reliability co-optimization. For the first time, we conduct a comprehensive error injection study on modern embodied AI systems and observe an inherent but heterogeneous fault tolerance. Building upon these insights, we develop an anomaly detection and clearance mechanism at the circuit level to eliminate outlier errors. At the model level, we propose a weight-rotation-enhanced planning algorithm to improve the fault tolerance of the LLM-based planner. Furthermore, we introduce an application-level technique, autonomy-adaptive voltage scaling, to dynamically adjust the operating voltage of the controllers. The voltage scaling circuit is co-designed to enable online voltage adjustment. Extensive experiments demonstrate that without compromising task quality, CREATE achieves 40.6% computational energy savings on average over nominal-voltage baselines and 35.0% over prior-art techniques. This further leads to 29.5% to 37.3% chip-level energy savings and approximately a 15% to 30% improvement in battery life.

## 中文摘要

具身人工智能（AI）近来因连接 AI 与物理世界而受到广泛关注。现代具身 AI 系统通常将用于高层任务规划的基于大语言模型（LLM）的规划器与用于底层动作生成的基于强化学习（RL）的控制器相结合，使具身智能体能够处理真实环境中的复杂任务。然而，由于具身智能体计算需求很高——尤其是在电池供电的本地设备上——部署它们仍然充满挑战。尽管降低工作电压等技术可以提升能效，但这些技术会引入位错误并导致任务失败。rs 以实现能量与可靠性的协同优化。我们首次对现代具身 AI 系统开展了全面的错误注入研究，并观察到一种固有但异质的容错性。基于这些洞见，我们在电路层面开发了一种异常检测与清除机制，以消除离群错误。在模型层面，我们提出一种权重旋转增强的规划算法，以提升基于 LLM 的规划器的容错性。此外，我们引入一种应用层技术——自主性自适应电压调节，以动态调整控制器的工作电压。电压调节电路经过协同设计以支持在线电压调整。大量实验表明，在不损害任务质量的前提下，CREATE 相比标称电压基线平均实现 40.6% 的计算能耗节省，相比现有技术实现 35.0% 的节省。这进一步带来 29.5% 至 37.3% 的芯片级能耗节省以及约 15% 至 30% 的电池寿命提升。

## 英文关键词

Embodied AI System; Efficiency; Reliability; Resilience Characterization; Cross-layer Optimization

## 中文关键词

具身 AI 系统；效率；可靠性；韧性刻画；跨层优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790147)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6A](index.md) · [返回 ASPLOS 2026](../index.md)
