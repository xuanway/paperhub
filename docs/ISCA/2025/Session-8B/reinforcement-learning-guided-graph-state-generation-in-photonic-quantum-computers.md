---
title: "Reinforcement Learning-Guided Graph State Generation in Photonic Quantum Computers"
description: "ISCA 2025 · Session 8B · 强化学习引导的光子量子计算机图态生成"
tags:
  - "ISCA2025"
  - "Session 8B"
  - "Quantum III"
---

# Reinforcement Learning-Guided Graph State Generation in Photonic Quantum Computers

**中文标题：** 强化学习引导的光子量子计算机图态生成

**所属 Session：** [Session 8B](index.md) · [ISCA 2025](../index.md)

**作者：** Yingheng Li, Yue Dai, Aditya Pawar, Rongchao Dong, Jun Yang, Youtao Zhang, Xulong Tang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731085) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The photonic quantum computer (PQC) is an emerging and promis- ing quantum computing paradigm that has gained momentum in recent years. In PQC, computations are executed by performing measurements on photons in graph states (i.e., a collection of en- tangled photons). The graph state generation process is fulfilled by applying a sequence of quantum gates to quantum emitters, referred to as the “generation sequence”. In a generation sequence, i) the time required to complete the generation sequence, ii) the number of quantum emitters used, and iii) the number of CZ gates performed between emitters greatly affect the fidelity of the generated graph state. In this paper, we propose RLGS (Reinforcement Learning- guided Graph State generation), a novel compilation framework to identify optimal generation sequences that optimize the three fidelity metrics. Experimental results show that RLGS achieves an average reduction in generation time of 31.1%, 49.6%, and 57.5% for small, medium, and large graph states compared to the baseline. Additionally, the reductions in the number of quantum emitters are 13.9%, 16.7%, and 17.5%, whereas the reductions in the number of CZ gates are 37.7%, 53.4%, and 57.8%, respectively.

## 中文摘要

光量子计算机（PQC）是近年快速发展、极具前景的量子计算方案。在光量子计算机中，计算依托对图态（一组纠缠光子）中的光子进行测量完成。图态的生成需要向量子辐射源依次施加量子门，该序列称为**生成序列**。在生成序列中，三个因素会显著影响最终图态的保真度：①生成序列的总耗时；②使用的量子辐射源数量；③辐射源之间执行的CZ门数量。

本文提出RLGS（强化学习引导图态生成，Reinforcement Learning-guided Graph State generation），一套全新编译框架，用于求解最优生成序列，同时优化上述三项保真度相关指标。实验结果表明：对比基线方案，RLGS对小规模、中等规模、大规模图态的生成时间平均分别缩短31.1%、49.6%、57.5%；量子辐射源数量分别减少13.9%、16.7%、17.5%；CZ门数量分别减少37.7%、53.4%、57.8%。

## 英文关键词

Quantum Computing, Photonic, Compiler

## 中文关键词

量子计算, 光量子, 编译器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731085)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8B](index.md) · [返回 ISCA 2025](../index.md)
