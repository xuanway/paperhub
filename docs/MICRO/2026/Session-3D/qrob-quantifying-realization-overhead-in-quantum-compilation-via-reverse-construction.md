---
title: "QROB: Quantifying Realization Overhead in Quantum Compilation via Reverse Construction"
description: "MICRO 2026 · Session 3D · QROB：通过逆向构造量化量子编译中的实现开销"
tags:
  - "MICRO2026"
  - "Quantum Computing"
  - "Compiler"
---

# QROB: Quantifying Realization Overhead in Quantum Compilation via Reverse Construction

**中文标题：** QROB：通过逆向构造量化量子编译中的实现开销

**所属 Session：** [Session 3D](index.md) · [MICRO 2026](../index.md)

**作者：** Jintao Li, Kaiqi Li, Rui Wang, Yilun Zhao, Kaixuan Huang, Ying Wang, Jialin Zhang, Zheng-An Wang, Xiaoming Sun, Heng Fan

**来源：** MICRO 2026，pp. 1251–1268；[DOI](https://doi.org/10.1109/MICRO67795.2026.00095)

## 英文摘要

Quantum compilation reconciles a program's idealized interaction topology with hardware locality constraints, yet evaluations at scale lack calibrated references for realization overhead. We present QROB, a scalable reverse-construction methodology that generates compilation instances backward from directly realizable configurations, retaining the inverse paths as feasible, compiler-independent references. QROB provides a common evaluation substrate for NISQ SWAP routing and fault-tolerant lattice-surgery scheduling, while extending its reference-preserving principle to capacity-constrained quantum memory-access scheduling. Across systems ranging from 9 to 156 qubits, evaluations highlight QROB's utility as both a diagnostic benchmark and a data source. First, for compiler characterization, QROB reveals substantial realization gaps in existing tools, with NISQ compilers incurring up to 24.1× the reference SWAP cost and fault-tolerant compilers requiring up to 7.0× the reference makespan. Second, as a supervision source for data-driven compilation, a router trained on QROB references outperforms Qiskit SABRE on 84.8% of real-world application circuits. Finally, on real hardware, QROB reference realizations achieve a median mirror-circuit survival rate $1.65× that of full Qiskit O3 compilations across three 156-qubit IBM Heron-r2 processors, demonstrating that closing algorithmic compilation gaps translates directly into physical fidelity gains.

## 中文摘要

量子编译使程序的理想化交互拓扑与硬件局部性约束相协调，但大规模评估缺乏实现开销的校准参考。我们提出了 QROB，一种可扩展的反向构造方法，它从直接可实现的配置向后生成编译实例，保留反向路径作为可行的、独立于编译器的引用。 QROB 为 NISQ SWAP 路由和容错晶格手术调度提供了通用评估基底，同时将其参考保留原理扩展到容量受限的量子内存访问调度。在 9 到 156 个量子位的系统中，评估强调了 QROB 作为诊断基准和数据源的实用性。首先，对于编译器表征，QROB 揭示了现有工具中的巨大实现差距，NISQ 编译器导致高达 24.1 倍的参考 SWAP 成本，而容错编译器则需要高达 7.0 倍的参考完工时间。其次，作为数据驱动编译的监督源，在 QROB 参考上训练的路由器在 84.8% 的实际应用电路上优于 Qiskit SABRE。最后，在真实硬件上，QROB 参考实现实现了三个 156 量子位 IBM Heron-r2 处理器上完整 Qiskit O3 编译的镜像电路生存率中值 1.65 美元，这表明缩小算法编译差距可以直接转化为物理保真度增益。

## 中文关键词

量子编译；容错量子计算；晶格手术；基准测试；逆向构造

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21539550](https://doi.org/10.5281/zenodo.21539550)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 3D](index.md) · [MICRO 2026 主页](../index.md)
