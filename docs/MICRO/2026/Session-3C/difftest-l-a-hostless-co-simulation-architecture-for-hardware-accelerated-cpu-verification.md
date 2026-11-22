---
title: "DiffTest-L: A Hostless Co-Simulation Architecture for Hardware-Accelerated CPU Verification"
description: "MICRO 2026 · Session 3C · DiffTest-L：面向硬件加速 CPU 验证的无主机协同仿真架构"
tags:
  - "MICRO2026"
  - "Simulation"
---

# DiffTest-L: A Hostless Co-Simulation Architecture for Hardware-Accelerated CPU Verification

**中文标题：** DiffTest-L：面向硬件加速 CPU 验证的无主机协同仿真架构

**所属 Session：** [Session 3C](index.md) · [MICRO 2026](../index.md)

**作者：** Yinan Xu, Dan Tang, Sa Wang, Ninghui Sun, Yungang Bao

**来源：** MICRO 2026，pp. 1115–1130；[DOI](https://doi.org/10.1109/MICRO67795.2026.00087)

## 英文摘要

Hardware-assisted simulation platforms such as emulators and FPGAs can run at tens to hundreds of MHz, but their effective verification throughput is bottlenecked by communication between hardware-simulated designs under test (DUTs) and host-executed reference models (REFs) during co-simulation. We observe that moving the entire verification framework onto hardware eliminates RTL-host communication and fully exploits hardware-assisted acceleration. To this end, we propose DiffTest-L, a hostless co-simulation architecture that re-architects the REF as synthesizable hardware logic. Within this framework, RCore and RCache leverage DUT execution information to form a hinted REF microarchitecture that eliminates register dependencies and reduces memory traffic, enabling simple yet high-throughput ISA-compliant reference execution. To ensure correctness and debuggability of such synthesizable REFs at both construction time and runtime, DiffTest-L provides a disciplined framework for ISA semantic realization, lifecycle-managed execution hints, and synthesizable software-like debugging primitives. A DiffTest-L prototype supporting the RV64IMACB ISA achieves 60 MHz on FPGA, delivering a 7.7X speedup over the state-of-the-art RTL-host co-simulation framework for CPU verification.

## 中文摘要

仿真器和 FPGA 等硬件辅助仿真平台可以在数十到数百 MHz 的速度下运行，但其有效验证吞吐量受到协同仿真期间硬件仿真待测设计 (DUT) 与主机执行参考模型 (REF) 之间的通信的瓶颈。我们观察到，将整个验证框架转移到硬件上可以消除 RTL 主机通信并充分利用硬件辅助加速。为此，我们提出了 DiffTest-L，这是一种无主机协同仿真架构，它将 REF 重新架构为可综合的硬件逻辑。在此框架内，RCore 和 RCache 利用 DUT 执行信息形成暗示的 REF 微架构，消除寄存器依赖性并减少内存流量，从而实现简单但高吞吐量的 ISA 兼容参考执行。为了确保此类可综合 REF 在构造时和运行时的正确性和可调试性，DiffTest-L 为 ISA 语义实现、生命周期管理的执行提示和可综合软件调试原语提供了严格的框架。支持 RV64IMACB ISA 的 DiffTest-L 原型在 FPGA 上达到 60 MHz，与用于 CPU 验证的最先进的 RTL 主机联合仿真框架相比，速度提高了 7.7 倍。

## 中文关键词

CPU 验证；差分测试；软硬件协同仿真；无主机架构；硬件加速

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/poemonsense/micro26-hola-difftest-ae](https://github.com/poemonsense/micro26-hola-difftest-ae)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21525870](https://doi.org/10.5281/zenodo.21525870)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 3C](index.md) · [MICRO 2026 主页](../index.md)
