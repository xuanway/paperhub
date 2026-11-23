---
title: "RAP: Reconfigurable Automata Processor"
description: "ISCA 2025 · Session 6C · RAP: 可重配自动机处理器"
tags:
  - "ISCA2025"
  - "Session 6C"
  - "Memory Acceleration"
---

# RAP: Reconfigurable Automata Processor

**中文标题：** RAP: 可重配自动机处理器

**所属 Session：** [Session 6C](index.md) · [ISCA 2025](../index.md)

**作者：** Ziyuan Wen, Alexis Le Glaunec, Konstantinos Mamouras, Kaiyuan Yang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731106) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Regular pattern matching is essential for applications such as text processing, malware detection, network security, and bioinformat- ics. Recent in-memory automata processors have significantly ad- vanced the energy and memory efficiency over conventional com- puting platforms. However, these processors are typically optimized only for one type of automata, limiting their capability to efficiently support regex processing under diverse real-world workloads. This paper presents RAP, the first reconfigurable in-memory automata processor for efficient regular pattern matching across diverse work- loads. It supports Nondeterministic Finite Automata (NFA), Nonde- terministic Bit Vector Automata (NBVA), and Linear NFA (LNFA) through reconfigurable architecture and circuit designs, and a com- piler for translation. RAP is evaluated in 28nm CMOS PDK, achiev- ing 1.2-1.5×higher energy efficiency and 1.3-2.5×higher compute density compared to SotA automata processors for NFA (CA and CAMA) over diverse real-world benchmarks. It also achieves 1.6× higher compute density and similar energy efficiency as BVAP, a SotA optimized for bounded repetitions. Finally, RAP is >100×and 1000×more energy efficient than SotA GPU and CPU solutions.

## 中文摘要

正则模式匹配在文本处理、恶意代码检测、网络安全、生物信息等场景中不可或缺。已有存内自动机处理器相比传统计算平台，在能效与存储效率上取得很大提升。但这类处理器通常只针对单一类型自动机优化，难以高效处理真实场景下多样化正则表达式负载。
本文提出RAP，首个面向多样化负载、支持正则模式匹配的可重构存内自动机处理器。它依托可重构架构与电路设计，配套编译工具，同时支持非确定有限自动机（NFA）、非确定位向量自动机（NBVA）与线性非确定有限自动机（LNFA）。
基于28nm CMOS工艺包（PDK）开展评估：在多个真实基准测试集上，对比面向NFA的前沿自动机处理器CA、CAMA，RAP能效提升1.2–1.5倍，计算密度提升1.3–2.5倍；对比专门优化有界重复模式的BVAP，RAP计算密度提升1.6倍，能效相当。此外，RAP能效远超前沿GPU与CPU方案，分别高出100倍、1000倍以上。

## 英文关键词

Automata Processor, Nondeterministic Bit Vector Automata, Linear Nondeterministic Finite Automata, Reconfigurability

## 中文关键词

自动机处理器, 非确定位向量自动机, 线性非确定有限自动机, 可重构性

## 代码与研究制品

- [研究制品](https://doi.org/10.5281/zenodo.15080391)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731106)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6C](index.md) · [返回 ISCA 2025](../index.md)
