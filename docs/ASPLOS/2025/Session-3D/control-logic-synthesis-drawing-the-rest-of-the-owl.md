---
title: "Control Logic Synthesis: Drawing the Rest of the OWL"
description: "ASPLOS 2025 · Session 3D · 控制逻辑综合：绘制 OWL 的其余部分"
tags:
  - "ASPLOS2025"
  - "Session 3D"
  - "EDA"
---

# Control Logic Synthesis: Drawing the Rest of the OWL

**中文标题：** 控制逻辑综合：绘制 OWL 的其余部分

**所属 Session：** [Session 3D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Zachary D. Sisco (University of California, Santa Barbara), Andrew David Alex (University of California, Santa Barbara), Zechen Ma (University of California, Santa Barbara), Yeganeh Aghamohammadi (University of California, Santa Barbara), Boming Kong (University of California, Santa Barbara), Benjamin Darnell (University of Illinois Urbana-Champaign), Timothy Sherwood (University of California, Santa Barbara), Ben Hardekopf (University of California, Santa Barbara), Jonathan Balkind (University of California, Santa Barbara)

**单位：** University of California, Santa Barbara；University of Illinois Urbana-Champaign

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674170) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

System-on-chip (SoC) design requires complex reasoning about the interactions between an architectural specification, the microarchitectural datapath (e.g., functional units), and the control logic (which coordinates the datapath) to facilitate the critical computing tasks on which we all depend. Hardware specialization is now the expectation rather than the exception, meaning we need new hardware design tools to bring ideas to reality with both agility and correctness. We introduce a new technique, “control logic synthesis”, which automatically generates control logic given a datapath description and an architectural specification. This enables an entirely new hardware design process where the designer only needs to write a datapath sketch, leaving the control logic as “holes.” Then, guided by an architectural specification, we adapt program synthesis techniques to automatically generate a correct hardware implementation of the control logic, filling the holes and completing the design. We evaluate control logic synthesis over two classes of control (state machines and instruction decoders) and different architectures (embedded-class RISC-V cores and hardware accelerators for cryptography). We demonstrate how agileoriented SoC developers can iterate over designs without writing control logic by hand yet still retain formal assurances with only minimal microarchitectural information.

## 中文摘要

系统级芯片（SoC）设计需要对架构规格说明、微体系结构数据通路（例如功能单元）以及控制逻辑（负责协调数据通路）三者之间的交互进行复杂的推理，以支撑我们所有人都赖以生存的关键计算任务。硬件专用化如今已是常态而非例外，这意味着我们需要新的硬件设计工具，既能敏捷又能正确地将想法变为现实。我们提出一种新技术——“控制逻辑综合”，它在给定数据通路描述和架构规格说明的情况下自动生成控制逻辑。这催生了一种全新的硬件设计流程：设计者只需编写数据通路草图，将控制逻辑留作“空洞”。随后，在架构规格说明的引导下，我们改造程序综合技术，自动生成控制逻辑的正确硬件实现，填补这些空洞并完成设计。我们在两类控制（状态机和指令译码器）以及不同架构（嵌入式级 RISC-V 核和面向密码学的硬件加速器）上评估了控制逻辑综合。我们展示了面向敏捷开发的 SoC 开发者如何在不手工编写控制逻辑的情况下迭代设计，同时仅凭最少的微体系结构信息仍能保持形式化保证。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674170)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3D](index.md) · [返回 ASPLOS 2025](../index.md)
