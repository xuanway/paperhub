---
title: "ReCA: Integrated Acceleration for Real-Time and Efficient Cooperative Embodied Autonomous Agents"
description: "ASPLOS 2025 · Session 4D · ReCA：面向实时高效协同具身自主智能体的集成加速"
tags:
  - "ASPLOS2025"
  - "Session 4D"
  - "Autonomous Systems"
---

# ReCA: Integrated Acceleration for Real-Time and Efficient Cooperative Embodied Autonomous Agents

**中文标题：** ReCA：面向实时高效协同具身自主智能体的集成加速

**所属 Session：** [Session 4D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Zishen Wan (Georgia Institute of Technology), Yuhang Du (University of Minnesota, Twin Cities), Mohamed Ibrahim (Georgia Institute of Technology), Jiayi Qian (Georgia Institute of Technology), Jason Jabbour (Harvard University), Yang (Katie) Zhao (University of Minnesota, Twin Cities), Tushar Krishna (Georgia Institute of Technology), Arijit Raychowdhury (Georgia Institute of Technology), Vijay Janapa Reddi (Harvard University)

**单位：** Georgia Institute of Technology；University of Minnesota, Twin Cities；Harvard University；Katie

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716016) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Cooperative embodied systems, where multiple agents collaborate through integrated perception, planning, action, and advanced reasoning powered by large language models (LLMs), show great potential for tackling complex, longhorizon, multi-objective tasks in real-world environments. Despite these algorithmic advancements, deploying embodied agents on current systems remains challenging due to prolonged planning and communication latency, limited scalability, and heightened sensitivity in low-level execution, all of which lead to significant system inefficiencies. This work proposes ReCA, a characterization and co-design framework dedicated to cooperative embodied agent system acceleration, aiming to enhance both task efficiency and system scalability. On the algorithm level, ReCA enables efficient local model processing to alleviate the substantial model costs. On the system level, ReCA presents a dual-memory structure with integrated long-term and short-term memory, hierarchical cooperative planning scheme with centralized and decentralized cooperation, and planning-guided multistep execution for highly efficient and scalable cooperative embodied agent computation. On the hardware level, ReCA employs a heterogeneous hardware system with high-level planning GPU subsystem and low-level planning accelerator subsystem to ensure efficient and robust task execution. Evaluated across long-horizon multi-objective tasks, ReCA generalizes across application scenarios and system scales,.3% increase in successful missions with 10.2× speedup compared to the state-of-the-art cooperative embodied autonomous agent systems.

## 中文摘要

协同具身系统通过集成感知、规划、动作以及由大语言模型（LLMs）驱动的先进推理，使多个智能体协同工作，在解决现实环境中复杂、长时程、多目标任务方面展现出巨大潜力。尽管算法层面取得了这些进展，但受限于冗长的规划与通信时延、有限的可扩展性以及对底层执行的高度敏感性，在当前系统上部署具身智能体仍然充满挑战，这些问题都导致明显的系统效率低下。本工作提出 ReCA，一个专用于协同具身智能体系统加速的表征与协同设计框架，旨在同时提升任务效率与系统可扩展性。在算法层面，ReCA 实现高效的本地模型处理，以缓解高昂的模型开销。在系统层面，ReCA 提出集成长时与短时记忆的双记忆结构、包含集中式与去中心化协同的分层协同规划方案，以及由规划引导的多步执行，从而实现高效且可扩展的协同具身智能体计算。在硬件层面，ReCA 采用由高层规划 GPU 子系统与低层规划加速器子系统构成的异构硬件系统，以确保高效且鲁棒的任务执行。在长时程多目标任务上的评估表明，ReCA 可泛化于不同应用场景与系统规模，相较于最先进的协同具身自主智能体系统，任务成功率提升 .3%，并取得 10.2 倍加速。

## 英文关键词

Autonomous Agents, Embodied Systems, Cooperative Intelligence, Hardware Accelerator

## 中文关键词

自主智能体；具身系统；协同智能；硬件加速器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716016)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4D](index.md) · [返回 ASPLOS 2025](../index.md)
