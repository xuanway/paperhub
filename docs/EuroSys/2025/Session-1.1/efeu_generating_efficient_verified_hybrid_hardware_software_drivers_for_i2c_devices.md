---
title: "Efeu: generating efficient, verified, hybrid hardware/software drivers for I2C devices"
description: "EuroSys 2025 · Operating Systems · Daniel Schwyn (ETH Zurich), Zikai Liu (ETH Zurich), Timothy Roscoe (ETH Zurich)"
tags:
  - "EuroSys2025"
  - "Operating Systems"
---

# Efeu: generating efficient, verified, hybrid hardware/software drivers for I2C devices

**中文标题：** 为 I2C 设备生成高效、经过验证的软硬件混合驱动

**所属 Session：** [Session 1.1: Operating Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Operating Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Operating Systems</p>
</div>

**作者**：Daniel Schwyn (ETH Zurich), Zikai Liu (ETH Zurich), Timothy Roscoe (ETH Zurich)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696093)

## 英文摘要

Writing device drivers is notoriously hard, and driver bugs are a major cause of system failures and vulnerabilities. The problem is particularly acute in bus-based protocols like I2C, where driver correctness is only half the story: correct functioning of the complete subsystem depends on all components on the bus interoperating correctly. Unfortunately, developers cannot control all aspects of a platform, and must interact with existing devices (peripherals and/or hardware bus controllers) which may misbehave. Failures in a protocol like I2C, often used in critical low-level system management, can result in permanent damage to the hardware, whether a server or a satellite.

Existing techniques for creating high assurance drivers rarely tackle this interoperability issue. We present Efeu, a framework for implementing verifiably interoperable drivers for I2C devices. Using model checking-based verification, Efeu generates driver implementations in software, reconfigurable logic for FPGAs, and, notably, combinations of both. The split between software and hardware can be varied at implementation time and the hardware/software interface is generated automatically, enabling efficient exploration of the design space. Using Efeu, we design and evaluate a verified I2C driver stack, and demonstrate that Efeu finds optimal hardware/software tradeoffs to favor either throughput, CPU usage or FPGA footprint. For each objective, Efeu generates drivers with performance comparable with hand-optimized hardware/software drivers.

## 中文摘要

编写设备驱动向来以困难著称，驱动程序缺陷是系统故障和漏洞的主要成因之一。在 I2C 这类基于总线的协议中，该问题尤为突出：驱动的正确性只是问题的一半，整个子系统能否正确运行取决于总线上所有组件能否正确互通。然而，开发者无法掌控平台的所有方面，必须与既有的、可能行为异常的设备（外设和/或硬件总线控制器）打交道。I2C 这类协议常用于关键的低层系统管理，一旦出错可能导致硬件永久损坏，无论是一台服务器还是一颗卫星。

现有的高保障驱动构建技术很少处理这种互操作性问题。我们提出 Efeu，一个用于实现可验证互通的 I2C 设备驱动的框架。Efeu 借助基于模型检验的验证，生成软件形式的驱动实现、面向 FPGA 的可重配置逻辑，以及尤为重要的两者的组合。软件与硬件之间的划分可在实现时调整，软硬件接口自动生成，从而能够高效地探索设计空间。使用 Efeu，我们设计并评估了一套经过验证的 I2C 驱动栈，并证明 Efeu 能够找到最优的软硬件折中，以偏向吞吐量、CPU 占用或 FPGA 资源占用中的任一目标。对于每个目标，Efeu 生成的驱动性能均与手工优化的软硬件驱动相当。

**英文关键词：** I2C, interoperability, verified drivers

**中文关键词：** I2C、互操作性、可验证驱动

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
