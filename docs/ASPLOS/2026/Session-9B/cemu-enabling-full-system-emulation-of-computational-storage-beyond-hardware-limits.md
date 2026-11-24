---
title: "CEMU: Enabling Full-System Emulation of Computational Storage beyond Hardware Limits"
description: "ASPLOS 2026 · Session 9B · CEMU：实现超越硬件限制的计算型存储全系统仿真"
tags:
  - "ASPLOS2026"
  - "Session 9B"
  - "Quantum & Emerging Computing"
---

# CEMU: Enabling Full-System Emulation of Computational Storage beyond Hardware Limits

**中文标题：** CEMU：实现超越硬件限制的计算型存储全系统仿真

**所属 Session：** [Session 9B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Qiuyang Zhang (Huazhong University of Science and Technology), Jiapin Wang (Huazhong University of Science and Technology), You Zhou (Huazhong University of Science and Technology), Peng Xu (Research Center for High Efficiency Computing Infrastructure, Zhejiang Lab), Kai Lu (Huazhong University of Science and Technology), Jiguang Wan (Huazhong University of Science and Technology), Fei Wu (Huazhong University of Science and Technology), Tao Lu (DapuStor)

**单位：** Huazhong University of Science and Technology；Research Center for High Efficiency Computing Infrastructure, Zhejiang Lab；DapuStor

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790137) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Computational storage drives (CSDs) present a promising approach to improve system performance through near data processing in SSDs. However, current research platforms are fragmented and inadequate to explore the full design space of CSD systems. Existing hardware and emulator platforms are constrained by physical compute resources, while simulators lack full-system fidelity. To address the problems, we introduce CEMU, a new software-based CSD emulation platform that enables full-system research. It consists of a CSD device emulator and a CSD-oriented software stack. Through a novel virtual machine freezing mechanism, CSD emulation achieves high configurability. While the CSD can utilize the host CPU to physically perform computation to preserve full-system behaviors, the computational delay can be modeled separately to emulate CSDs with CPU-unbounded high computing power. The software stack is designed with two principles, adhering to recent industry CSD standards and being compatible with the existing I/O stack, which is achieved via a newly developed file system FDMFS. We verify CEMU's emulation fidelity across a range of applications by benchmarking against actual CSD hardware, demonstrating average end-to-end performance accuracy of 95% or higher. We also use two case studies on large language model training and LevelDB to demonstrate that CEMU is effective in exploring CSD system research and can uncover insights that have not been discovered in previous research platforms.

## 中文摘要

计算存储盘（CSD）通过在 SSD 中进行近数据处理，为提升系统性能提供了一条有前景的途径。然而，当前的研究平台是碎片化的，不足以探索 CSD 系统的完整设计空间。现有的硬件与仿真器平台受限于物理计算资源，而模拟器则缺乏全系统保真度。为解决这些问题，我们提出 CEMU，一个支持全系统研究的新型基于软件的 CSD 仿真平台。它由一个 CSD 设备仿真器和一个面向 CSD 的软件栈组成。通过一种新颖的虚拟机冻结机制，CSD 仿真实现了高可配置性。CSD 可以利用主机 CPU 实际执行计算以保持全系统行为，同时计算延迟可以被单独建模，从而仿真算力不受 CPU 限制的 CSD。该软件栈的设计遵循两条原则：遵循近期业界 CSD 标准，并与现有 I/O 栈兼容，这是通过新开发的文件系统 FDMFS 实现的。我们通过在实际 CSD 硬件上进行基准测试，在一系列应用中验证了 CEMU 的仿真保真度，展示出平均端到端性能准确度达到 95% 或更高。我们还通过关于大语言模型训练和 LevelDB 的两个案例研究，证明 CEMU 在探索 CSD 系统研究方面是有效的，并能揭示此前研究平台中未被发现的洞见。

## 英文关键词

Computational Storage, Emulation Platform, Software Stack, Storage Systems

## 中文关键词

计算型存储；仿真平台；软件栈；存储系统

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790137)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9B](index.md) · [返回 ASPLOS 2026](../index.md)
