---
title: "ICARUS: Criticality and Reuse based Instruction Caching for Datacenter Applications"
description: "ASPLOS 2026 · Session 5D · ICARUS：面向数据中心应用的基于关键性与重用的指令缓存"
tags:
  - "ASPLOS2026"
  - "Session 5D"
  - "Storage & Caching"
---

# ICARUS: Criticality and Reuse based Instruction Caching for Datacenter Applications

**中文标题：** ICARUS：面向数据中心应用的基于关键性与重用的指令缓存

**所属 Session：** [Session 5D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Vedant Kalbande (Indian Institute of Technology Bombay), Hrishikesh Jedhe Deshmukh (Indian Institute of Technology Bombay), Alberto Ros (University of Murcia), Biswabandan Panda (Indian Institute of Technology Bombay)

**单位：** Indian Institute of Technology Bombay；University of Murcia

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790175) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Datacenter applications with huge code footprints suffer from front-end CPU bottlenecks even with a decoupled frontend. These applications are composed of complex system stacks with subtle interdependencies. One of the primary contributors to the front-end bottleneck is instruction misses at L2, which cause decode starvation. State-of-the-art L2 cache replacement policies, such as EMISSARY, utilize frontend criticality to identify instruction lines that cause decode starvation and attempt to keep those critical lines in L2. We observe that only 28.32% of the critical lines retain their criticality behavior, and a significant fraction of the critical instruction lines show dynamic behavior. We propose ICARUS, an L2 replacement policy that incorporates branch history as context information to improve critical instruction line detection. We observe that the reuse distance of instruction lines varies based on the branch history that led to the instruction fetch. Next, we enhance the L2 replacement policy by considering both criticality and the reuse of instruction lines at L2, as we observe that the reuse behavior of critical lines differs from that of non-critical lines. On average, across 12 datacenter applications, ICARUS outperforms Tree-based Pseudo LRU (TPLRU) by 5.6% and as high as 51%. The state-of-the-art replacement policy, EMISSARY, on the other hand, provides an improvement of 2.2% over TPLRU. We demonstrate the robustness of ICARUS across various L1I and L2 cache sizes, as well as its effectiveness in the presence of hardware prefetchers.

## 中文摘要

具有庞大代码足迹的数据中心应用即使采用解耦前端，仍会遭受前端 CPU 瓶颈。这些应用由具有微妙相互依赖关系的复杂系统栈构成。造成前端瓶颈的主要因素之一是 L2 中的指令缺失，它会引发解码饥饿（decode starvation）。最先进的 L2 缓存替换策略（如 EMISSARY）利用前端关键性来识别导致解码饥饿的指令行，并试图将这些关键行保留在 L2 中。我们观察到，只有 28.32% 的关键行保持了其关键性行为，并且相当一部分关键指令行表现出动态行为。我们提出 ICARUS，一种 L2 替换策略，它引入分支历史作为上下文信息，以改进关键指令行的检测。我们观察到，指令行的重用距离会随导致该指令取指的分支历史而变化。接下来，我们通过同时考虑关键性与指令行在 L2 中的重用，进一步增强 L2 替换策略，因为我们观察到关键行的重用行为与非关键行不同。在 12 个数据中心应用上，ICARUS 平均比 Tree-based Pseudo LRU（TPLRU）高出 5.6%，最高达 51%。而最先进的替换策略 EMISSARY 相较 TPLRU 仅带来 2.2% 的提升。我们证明了 ICARUS 在多种 L1I 和 L2 缓存大小下的鲁棒性，以及其在存在硬件预取器时的有效性。

## 英文关键词

Cache Microarchitecture; Cache Replacement Policy; Instruction Caching

## 中文关键词

缓存微架构；缓存替换策略；指令缓存

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790175)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5D](index.md) · [返回 ASPLOS 2026](../index.md)
