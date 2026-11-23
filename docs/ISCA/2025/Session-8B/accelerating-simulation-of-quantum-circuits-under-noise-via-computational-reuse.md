---
title: "Accelerating Simulation of Quantum Circuits under Noise via Computational Reuse"
description: "ISCA 2025 · Session 8B · 通过计算复用加速噪声环境下的量子电路模拟"
tags:
  - "ISCA2025"
  - "Session 8B"
  - "Quantum III"
---

# Accelerating Simulation of Quantum Circuits under Noise via Computational Reuse

**中文标题：** 通过计算复用加速噪声环境下的量子电路模拟

**所属 Session：** [Session 8B](index.md) · [ISCA 2025](../index.md)

**作者：** Meng Wang, Swamit Tannu, Prashant J Nair

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3730992) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

To realize the full potential of quantum computers, we must miti- gate qubit errors by developing noise-aware algorithms, compilers, and architectures. Thus, simulating quantum programs on high- performance computing (HPC) systems with different noise models is a de facto tool researchers use. Unfortunately, noisy simulators iteratively execute a similar circuit for thousands of trials, thereby incurring significant performance overheads. To address this, we propose a noisy simulation technique called Tree-Based Quantum Circuit Simulation (TQSim) 1. TQSim exploits the reusability of intermediate results during the noisy simulation, reducing computation. TQSim dynamically partitions a circuit into several subcircuits. It then reuses the intermediate results from these subcircuits during computation. Compared to a noisy Qulacs- based baseline simulator, TQSim achieves a speedup of up to 3.89× for noisy simulations. TQSim is designed to be efficient with multi- node setups while also maintaining tight fidelity bounds.

## 中文摘要

想要充分释放量子计算机的潜力，我们必须研发面向噪声感知的算法、编译器与架构，以此抑制量子比特错误。因此，在高性能计算（HPC）平台上使用不同噪声模型仿真量子程序，已经成为研究者的必备手段。但含噪声模拟器需要对同一线路重复采样上千次，带来巨大的性能开销。

针对该问题，本文提出一种含噪声仿真技术：基于树的量子电路仿真（TQSim）。TQSim利用含噪声仿真过程中中间结果的可复用性，减少重复计算。它将电路动态切分为若干子电路，在计算过程中复用这些子电路的中间结果。
对比基于Qulacs的含噪声基线模拟器，TQSim最高可实现3.89倍的仿真加速。TQSim面向多节点集群做了效率优化，同时能够保证保真度边界的误差可控。

## 英文关键词

Quantum Computing, Noisy Monte Carlo Simulation, State Reuse

## 中文关键词

量子计算, 含噪声蒙特卡洛模拟, 量子态复用

## 代码与研究制品

- [代码仓库](https://github.com/meng-ubc/TQSim)
- [研究制品](https://doi.org/10.5281/zenodo.15104095)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3730992)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8B](index.md) · [返回 ISCA 2025](../index.md)
