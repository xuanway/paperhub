---
title: "Hassert: Hardware Assertion-Based Verification Framework with FPGA Acceleration"
description: "ASPLOS 2025 · Session 2D · Hassert：一种带 FPGA 加速的硬件断言验证框架"
tags:
  - "ASPLOS2025"
  - "Session 2D"
  - "FPGAs"
---

# Hassert: Hardware Assertion-Based Verification Framework with FPGA Acceleration

**中文标题：** Hassert：一种带 FPGA 加速的硬件断言验证框架

**所属 Session：** [Session 2D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Ziqing Zhang (State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences), Weijie Weng (Xiamen University of Technology), Yaning Li (University College Dublin), Lijia Cai (Hong Kong University of Science and Technology), Haoyu Wang (Zhejiang University), David Boland (The University of Sydney), Yungang Bao (State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences), Kan Shi (State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences)

**单位：** State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences；Xiamen University of Technology；University College Dublin；Hong Kong University of Science and Technology；Zhejiang University；The University of Sydney

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3698899) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Hardware verification is typically the bottleneck of the chip development cycle, mainly due to the time-consuming simulation and debugging process using software simulators. Assertion-Based Verification (ABV) has been widely adopted to provide better visibility into microarchitecture details and automatically detect unexpected behaviors. While ABV significantly improves verification efficiency, checking assertions using software simulators requires extremely long times for large benchmarks. Prototyping designs on an FPGA is a potential alternative to verify hardware, but it lacks fine-grained debugging capabilities for when errors occur. To address these challenges, we present Hassert, an efficient ABV framework that combines high-performance verification on FPGAs with fine-grained debugging in software. Hassert automates the scheduling and mapping of SystemVerilog Assertions (SVAs) to the available FPGA fabric with the design-under-test (DUT), allowing for extensive hardware testing. Hassert also enables dynamic switching ∗Weijie Weng, Yaning Li, Lijia Cai and Haoyu Wang finish this work during internship at the State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences. mons Attribution-NonCommercial-ShareAlike International 4.0 License d or based on SVA coverage satisfaction, by partially reconfiguring the FPGA at runtime, eliminating the need to recompile the DUT. To further improve debugging efficiency, we also propose a microarchitecture-guided hardware snapshot scheme. If any assertion is fired, Hassert automatically generates snapshots of the current status of the entire FPGA hardware. These snapshots are then transferred to an external simulator, where the operation is reconstructed in software for further debugging. We demonstrate that these contributions can improve significant verification efficiency over traditional software simulation-based approaches for various hardware benchmarks and RISC-V processor designs whilst maintaining full visibility and debugging capabilities at the cost of only a small area overhead.

## 中文摘要

硬件验证通常是芯片开发周期的瓶颈，主要原因是使用软件模拟器进行仿真与调试的过程十分耗时。基于断言的验证（ABV）已被广泛采用，它能更好地呈现微架构细节，并自动检测非预期行为。尽管 ABV 显著提升了验证效率，但使用软件模拟器检查断言对于大规模基准仍需极长的时间。在 FPGA 上进行原型验证是验证硬件的一种潜在替代方案，但它在错误发生时缺乏细粒度的调试能力。为应对这些挑战，我们提出 Hassert，一个高效的 ABV 框架，它将 FPGA 上的高性能验证与软件中的细粒度调试相结合。Hassert 自动化地将 SystemVerilog 断言（SVA）与待测设计（DUT）一起调度并映射到可用的 FPGA 资源上，从而实现大规模的硬件测试。Hassert 还支持根据 SVA 覆盖率满足情况动态切换，通过在运行时对 FPGA 进行部分重构，无需重新编译 DUT。为进一步提高调试效率，我们还提出一种微架构引导的硬件快照方案。若任一断言被触发，Hassert 会自动生成整个 FPGA 硬件当前状态的快照。这些快照随后被传输到外部模拟器中，在软件中重建其运行过程以进行进一步调试。我们证明，对于各类硬件基准和 RISC-V 处理器设计，这些贡献相比传统的基于软件仿真的方法可显著提升验证效率，同时以很小的面积开销保持完整的可见性与调试能力。

## 英文关键词

FPGA, Debugging, Assertion, Verification, Emulation, Acceleration

## 中文关键词

FPGA；调试；断言；验证；仿真；加速

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3698899)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2D](index.md) · [返回 ASPLOS 2025](../index.md)
