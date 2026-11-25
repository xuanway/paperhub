---
title: "FAME: A Framework for Accelerating Independent Multi-Agent Reinforcement Learning on Heterogeneous Platforms"
description: "HPDC 2026 · Session 4 — Programming Models, Frameworks & Compilers"
tags:
  - "HPDC2026"
  - "Session 4"
  - "Programming Models, Frameworks & Compilers"
---

# FAME: A Framework for Accelerating Independent Multi-Agent Reinforcement Learning on Heterogeneous Platforms

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 4 — Programming Models, Frameworks & Compilers（2026年7月14日 14:40–15:40 · Session Chair：Dhabaleswar K (DK) Panda）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 4</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807599)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#WigginsGZIP26](https://dblp.org/db/conf/hpdc/hpdc2026.html#WigginsGZIP26)

**作者**：Samuel Wiggins, Nikunj Gupta, Grace Zgheib, Mahesh A. Iyer, Viktor Prasanna

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 4 — Programming Models, Frameworks & Compilers（2026年7月14日 14:40–15:40 · Session Chair：Dhabaleswar K (DK) Panda）

---

## 英文摘要

Multi-Agent Reinforcement Learning (MARL) enables multiple autonomous agents to learn and act in a shared environment. Independent learning (IL) is a widely used MARL paradigm that underpins many real-world applications requiring efficient training at scale. However, accelerating IL at scale is non-trivial. Existing MARL frameworks rely on single-process execution and homogeneous hardware assumptions, limiting scalability and underutilizing modern heterogeneous platforms composed of CPUs, GPUs, and FPGAs. Addressing this gap requires new execution models that increase parallelism while preserving IL training semantics. In this work, we present FAME, a framework that distributes computation across heterogeneous hardware resources while providing flexible interfaces that allow MARL practitioners to prototype and test new IL approaches. FAME is composed of: (1) high-level APIs that simplify IL algorithm development, (2) a heterogeneous IL training protocol that supports concurrent agent training on multiple diverse devices, while maintaining algorithm-agnostic training semantics, (3) automatic hardware configuration generation that optimizes system throughput without needing users to manually fine-tune their system setup, and (4) dynamic load balancing among devices with different compute and memory characteristics. We demonstrate FAME’s capabilities using three representative IL algorithms on a heterogeneous node platform consisting of CPUs, GPUs, and FPGAs. Implementations generated using FAME achieve a geometric mean end-to-end training time speedup of 7.1× over state-of-the-art implementations and up to 2.7× speedup over additional highly parallel baselines developed in this work.

## 中文摘要

多智能体强化学习（MARL）使多个自主智能体能够在共享环境中学习与行动。独立学习（IL）是一种广泛使用的 MARL 范式，支撑着许多需要高效大规模训练的实际应用。然而，大规模加速 IL 并非易事。现有 MARL 框架依赖单进程执行与同构硬件假设，限制了可扩展性，且未能充分利用由 CPU、GPU 和 FPGA 组成的现代异构平台。填补这一空白需要新的执行模型，在保持 IL 训练语义的同时提升并行度。在本工作中，我们提出 FAME，一个将计算分布到异构硬件资源、同时提供灵活接口的框架，使 MARL 从业者能够原型化并测试新的 IL 方法。FAME 由以下部分组成：(1) 简化 IL 算法开发的高层 API；(2) 支持在多种异构设备上并发训练智能体、同时保持算法无关训练语义的异构 IL 训练协议；(3) 自动生成硬件配置，无需用户手动微调系统设置即可优化系统吞吐；(4) 在计算与内存特性不同的设备间进行动态负载均衡。我们在由 CPU、GPU 和 FPGA 组成的异构节点平台上，使用三种代表性 IL 算法展示了 FAME 的能力。使用 FAME 生成的实现相比最先进实现取得 7.1 倍的几何平均端到端训练加速，相比本工作中开发的其他高度并行基线最高取得 2.7 倍加速。

## 英文关键词

Multi-Agent Reinforcement Learning, Independent Learning, Heterogeneous Computing

## 中文关键词

多智能体强化学习，独立学习，异构计算

---

[← 返回 Session 4 — Programming Models, Frameworks & Compilers](index.md)
