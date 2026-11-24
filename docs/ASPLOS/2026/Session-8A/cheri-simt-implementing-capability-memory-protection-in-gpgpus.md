---
title: "CHERI-SIMT: Implementing Capability Memory Protection in GPGPUs"
description: "ASPLOS 2026 · Session 8A · CHERI-SIMT：在 GPGPU 中实现能力内存保护"
tags:
  - "ASPLOS2026"
  - "Session 8A"
  - "GPU Programming"
---

# CHERI-SIMT: Implementing Capability Memory Protection in GPGPUs

**中文标题：** CHERI-SIMT：在 GPGPU 中实现能力内存保护

**所属 Session：** [Session 8A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Matthew Naylor (University of Cambridge), Alexandre Joannou (University of Cambridge), A. Theodore Markettos (University of Cambridge), Paul Metzger (University of Cambridge), Simon Moore (University of Cambridge), Timothy M. Jones (University of Cambridge)

**单位：** University of Cambridge

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762234) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

**出版标题：** CHERI-SIMT: Implementing Capability Memory Protection in GPUs

## 英文摘要

Governments are increasingly advising software manufacturers to employ memory-safe languages and technologies to combat adversarial attacks on modern computing infrastructure. This introduces pressures across the entire computing industry, including GPU vendors who provide implementations of unsafe C/C++-based languages, such as CUDA and OpenCL, for programming the devices they produce. One of the memory-safety technologies being recommended is Capability Hardware Enhanced RISC Instructions (CHERI). CHERI builds strong and efficient memory safety into underlying instruction-set architectures allowing continued, but memory-safe, use of C/C++-based languages on top. In this paper, we evaluate the feasibility of incorporating CHERI into GPU architectures by extending a prototype, open-source, synthesisable, SIMT core and CUDA-like programming environment with support for CHERI. We present techniques to considerably ameliorate the costs of CHERI in SIMT designs, reducing register-file storage overheads from 103% to 7%, logic-area overheads by 44% to a cost comparable to one additional multiplier per vector lane, and execution-time overheads to 1.6%. With the proposed techniques, CHERI offers a viable path to strong and efficient GPU memory safety, while avoiding the need to replace established programming practices.

## 中文摘要

各国政府日益建议软件制造商采用内存安全的语言和技术，以抵御针对现代计算基础设施的对抗性攻击。这给整个计算行业带来了压力，包括那些为其生产的设备提供基于不安全的 C/C++ 的语言（如 CUDA 和 OpenCL）实现的 GPU 厂商。被推荐的内存安全技术之一是能力硬件增强 RISC 指令（CHERI）。CHERI 将强健而高效的内存安全构建到基础指令集架构之中，从而允许在其之上继续（但以内存安全的方式）使用基于 C/C++ 的语言。在本文中，我们通过为一个原型化、开源、可综合的 SIMT 核以及类 CUDA 编程环境增加 CHERI 支持，评估了将 CHERI 纳入 GPU 架构的可行性。我们提出了显著降低 CHERI 在 SIMT 设计中开销的技术，将寄存器文件存储开销从 103% 降至 7%，将逻辑面积开销减少 44%，降至与每条向量通道额外增加一个乘法器相当的成本，并将执行时间开销降至 1.6%。借助所提出的技术，CHERI 为强健且高效的 GPU 内存安全提供了一条可行路径，同时避免了替换既有编程实践的需要。

## 英文关键词

Memory Safety; CHERI; GPU; SIMT

## 中文关键词

内存安全；CHERI；GPU；SIMT

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762234)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8A](index.md) · [返回 ASPLOS 2026](../index.md)
