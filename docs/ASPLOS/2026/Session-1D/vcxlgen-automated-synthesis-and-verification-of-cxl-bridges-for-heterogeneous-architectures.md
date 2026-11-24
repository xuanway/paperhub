---
title: "vCXLGen: Automated Synthesis and Verification of CXL Bridges for Heterogeneous Architectures"
description: "ASPLOS 2026 · Session 1D · vCXLGen：面向异构架构的 CXL 桥自动综合与验证"
tags:
  - "ASPLOS2026"
  - "Session 1D"
  - "CXL & Memory Fabric"
---

# vCXLGen: Automated Synthesis and Verification of CXL Bridges for Heterogeneous Architectures

**中文标题：** vCXLGen：面向异构架构的 CXL 桥自动综合与验证

**所属 Session：** [Session 1D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Anatole Lefort (Technical University of Munich), Julian Pritzi (Technical University of Munich), Nicolò Carpentieri (Technical University of Munich), David Schall (Technical University of Munich), Simon Dittrich (Technical University of Munich), Soham Chakraborty (TU Delft), Nicolai Oswald (NVIDIA), Pramod Bhatotia (Technical University of Munich)

**单位：** Technical University of Munich；TU Delft；NVIDIA

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790245) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Compute Express Link (CXL) offers byte-addressable, cache-coherent remote memory accesses across multiple hosts. Unfortunately, the CXL specification lacks mechanisms to ensure safe interoperability between heterogeneous host architectures with diverse cache coherence (CC) protocols and memory consistency models (MCMs). This semantic gap poses fundamental challenges and a significant barrier to adopting CXL in modern heterogeneous data centers. We propose CXL bridges, an abstraction that interposes between hosts and CXL to reconcile differences in CC protocols and MCMs. We present vCXLGen, the first system that automatically synthesizes and verifies these CXL bridges. We make two core contributions: (1) a fully automated approach to synthesize CXL bridges from machine-readable CC protocol specifications, and (2) a compositional formal verification approach for scalable model-checking of liveness properties. Our evaluation shows that vCXLGen is general, i.e., it supports diverse protocols (both SWMR and relaxed consistency) and is easily extensible when integrating new protocols, such as CXL.mem. Our performance evaluations indicate that synthesised bridges achieve comparable results to manually designed homogeneous protocols. Finally, for correctness, our formal verification rigorously proves the safety and liveness of synthesized bridges, all while achieving significant scalability in liveness verification of complex heterogeneous systems.

## 中文摘要

计算快速链路（CXL）提供跨多个主机的字节可寻址、缓存一致的远程内存访问。遗憾的是，CXL 规范缺乏相应机制来确保具有不同缓存一致性（CC）协议和内存一致性模型（MCM）的异构主机架构之间实现安全的互操作。这一语义鸿沟带来了根本性挑战，也成为在现代异构数据中心采用 CXL 的重大障碍。我们提出 CXL 桥（CXL bridges），一种介于主机与 CXL 之间、用于调和 CC 协议与 MCM 差异的抽象。我们提出 vCXLGen，这是首个自动综合并验证这些 CXL 桥的系统。我们做出两项核心贡献：(1) 一种从机器可读的 CC 协议规范自动综合 CXL 桥的全自动方法；(2) 一种组合式形式化验证方法，用于对活性性质进行可扩展的模型检测。我们的评估表明 vCXLGen 具有通用性，即它支持多种协议（包括 SWMR 和宽松一致性），并且在集成新协议（如 CXL.mem）时易于扩展。我们的性能评估表明，综合得到的桥可取得与手工设计的同构协议相当的结果。最后，在正确性方面，我们的形式化验证严格证明了综合所得桥的安全性与活性，同时在复杂异构系统的活性验证中实现了显著的可扩展性。

## 英文关键词

Cache, coherence; CXL; Disaggregated, systems

## 中文关键词

缓存一致性；CXL；解聚系统

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790245)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1D](index.md) · [返回 ASPLOS 2026](../index.md)
