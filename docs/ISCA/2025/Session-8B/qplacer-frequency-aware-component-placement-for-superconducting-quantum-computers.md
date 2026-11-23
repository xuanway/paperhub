---
title: "QPlacer: Frequency-Aware Component Placement for Superconducting Quantum Computers"
description: "ISCA 2025 · Session 8B · Qplacer: 超导量子计算机的频率感知元件布局"
tags:
  - "ISCA2025"
  - "Session 8B"
  - "Quantum III"
---

# QPlacer: Frequency-Aware Component Placement for Superconducting Quantum Computers

**中文标题：** Qplacer: 超导量子计算机的频率感知元件布局

**所属 Session：** [Session 8B](index.md) · [ISCA 2025](../index.md)

**作者：** Junyao Zhang, Hanrui Wang, Qi Ding, Jiaqi Gu, Reouven Assouly, William D. Oliver, Song Han, Kenneth R. Brown, Hai "Helen" Li, Yiran Chen

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3730994) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Quantum Computers face a critical limitation in qubit numbers, hindering their progression towards large-scale and fault-tolerant quantum computing. A significant challenge impeding scaling is crosstalk, characterized by unwanted interactions among neighbor- ing components on quantum chips, including qubits, resonators, and substrates. We motivate a general approach to systematically resolving multifaceted crosstalks in a limited substrate area. We propose QPlacer, a frequency-aware electrostatic-based placement framework tailored for superconducting quantum computers, to alleviate crosstalk by isolating these components in spatial and frequency domains alongside compact substrate design. QPlacer commences with a frequency assigner that ensures fre- quency domain isolation for qubits and resonators. It then incor- porates a padding strategy and resonator partitioning for layout flexibility. Central to our approach is the conceptualization of quan- tum components as charged particles, enabling strategic spatial isolation through a ‘frequency repulsive force’ concept. Our results demonstrate that QPlacer carefully crafts the physical component layout in mitigating various crosstalk impacts while maintaining a compact substrate size. On various device topologies and NISQ benchmarks, QPlacer improves fidelity by an average of 37.5×and reduces spatial violations (susceptible to crosstalk) by an average of 12.76×, compared to classical placement engines. Regarding area optimization, compared to manual designs, QPlacer can reduce the required layout area by 2.14×on average.

## 中文摘要

量子计算机目前受限于量子比特规模，阻碍了向大规模容错量子计算演进。制约系统扩容的一大难题是串扰：量子芯片上相邻单元（量子比特、谐振腔、衬底等）之间产生非预期耦合干扰。本文提出一种通用方案，在有限衬底面积内系统性处理多类型串扰。我们设计QPlacer——一款面向超导量子计算机、具备频率感知、基于静电模型的布局框架，在紧凑衬底设计的约束下，从空间域与频率域隔离器件，从而缓解串扰。

QPlacer首先通过频率分配器，保证量子比特和谐振腔在频率域相互隔离；再引入填充策略与谐振腔拆分方案，提升布局灵活性。本方案的核心思想是将量子器件类比为带电粒子，借助“频率排斥力”实现有策略的空间隔离。实验结果表明：QPlacer可以合理规划器件物理布局，在控制衬底面积紧凑的前提下抑制各类串扰。在多种器件拓扑与NISQ基准线路上，对比传统布局引擎，QPlacer平均将保真度提升37.5倍，容易引发串扰的空间冲突违规平均减少12.76倍；在面积优化上，相比人工布局，QPlacer平均缩减布局面积2.14倍。

## 英文关键词

Quantum Computing, Crosstalk Mitigation, Superconducting Quantum Computer

## 中文关键词

量子计算, 串扰抑制, 超导量子计算机

## 代码与研究制品

- [代码仓库](https://github.com/JJJayyyy/QPlacer)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3730994)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8B](index.md) · [返回 ISCA 2025](../index.md)
