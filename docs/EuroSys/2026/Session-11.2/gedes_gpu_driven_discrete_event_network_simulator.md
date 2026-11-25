---
title: "GeDES: GPU-Driven Discrete Event Network Simulator"
description: "EuroSys 2026 · Programmable Networks, SmartNICs & Accelerators · Qinyong Li (University of Electronic Science and Technology of China), Zhiwei Zh"
tags:
  - "EuroSys2026"
  - "Programmable Networks, SmartNICs & Accelerators"
---

# GeDES: GPU-Driven Discrete Event Network Simulator

**中文标题：** GeDES：GPU 驱动的离散事件网络模拟器

**所属 Session：** [Session 11.2: Programmable Networks, SmartNICs & Accelerators](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Programmable Networks, SmartNICs & Accelerators。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Programmable Networks, SmartNICs & Accelerators</p>
</div>

**作者**：Qinyong Li (University of Electronic Science and Technology of China), Zhiwei Zhao (University of Electronic Science and Technology of China), Geyong Min (Department of Computer Science, University of Exeter), Zi Wang (University of Electronic Science and Technology of China), Luwei Fu (University of Electronic Science and Technology of China)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769327)

## 英文摘要

Discrete event network simulator (DES) is a fundamental service for the design, validation and optimization of various networked systems, including traditional computer networks and the recent LLM training/inference systems. Efficient DES is strongly demanded by the community yet not delivered. The reason is: while DES allows for node-level parallelism, its concurrency potential has been significantly under-utilized (usually <5%) due to the limited number of CPU cores. Meanwhile, GPUs, with thousands of cores, have long been overlooked in the design of DES systems due to the incompatibility between GPUs’ SIMT architecture and DES’s sequential model. In this paper, we aim to achieve ground-breaking performance improvement for DES by designing a novel GPU-driven simulation engine. By carefully manipulating the life cycles of network events and orchestrating them with long- and short-term alignments, we overcome the incompatibility barriers and established GeDES, a high-level parallel and cost-effective DES system. Extensive simulation experiments show that GeDES significantly boosts DES by 33-2400× speedups compared to the SOTA works Unison and DONS. The code is available at https://github.com/mobinets/GeDES.

## 中文摘要

离散事件网络模拟器（DES）是为各类网络化系统（包括传统计算机网络以及近期的 LLM 训练/推理系统）进行设计、验证和优化的基础服务。社区对高效 DES 有强烈需求，却始终未能得到满足。原因在于：尽管 DES 允许节点级并行，但由于 CPU 核数有限，其并发潜力被严重地低效利用（通常低于 5%）。与此同时，拥有数千核的 GPU 长期以来在 DES 系统设计中被忽视，因为 GPU 的 SIMT 架构与 DES 的顺序模型不兼容。本文旨在通过设计一种新颖的 GPU 驱动模拟引擎，为 DES 带来突破性的性能提升。通过精心操纵网络事件的生命周期，并以长时与短时对齐的方式对其进行编排，我们克服了不兼容性障碍，建立了 GeDES，一个高层次并行且高性价比的 DES 系统。大量模拟实验表明，与先进工作 Unison 和 DONS 相比，GeDES 将 DES 加速 33–2400 倍。代码见 https://github.com/mobinets/GeDES。

**英文关键词：** Network Simulation, Discrete Event Simulation, GPU-Driven Simulations

**中文关键词：** 网络模拟、离散事件模拟、GPU 驱动模拟

## 代码与研究制品

- [代码](https://github.com/mobinets/GeDES)（论文摘要提供）

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
