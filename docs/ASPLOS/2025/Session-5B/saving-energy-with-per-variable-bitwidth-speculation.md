---
title: "Saving Energy with Per-Variable Bitwidth Speculation"
description: "ASPLOS 2025 · Session 5B · 通过逐变量位宽投机节省能耗"
tags:
  - "ASPLOS2025"
  - "Session 5B"
  - "Microarchitecture"
---

# Saving Energy with Per-Variable Bitwidth Speculation

**中文标题：** 通过逐变量位宽投机节省能耗

**所属 Session：** [Session 5B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Tommy McMichen (Northwestern University), David Dlott (Northwestern University), Panitan Wongse-ammat (Northwestern University), Nathan Greiner (Northwestern University), Hussain Khajanchi (Northwestern University), Russ Joseph (Northwestern University), Simone Campanoni (Northwestern University)

**单位：** Northwestern University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716271) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Tiny devices have become ubiquitous in people's daily lives. Their applications dictate tight energy budgets, but also require reasonable performance to meet user expectations. To this end, the hardware of tiny devices has been highly optimized, making further optimizations difficult. In this work, we identify a missed opportunity: the bitwidth selection of program variables. Today's compilers directly translate the bitwidth specified in the source code to the binary. However, we observe that most variables do not utilize the full bitwidth specified in the source code for the majority of execution. To leverage this opportunity, we propose BitSpec: a system that performs fine-grained speculation on the bitwidth of program variables. BitSpec is implemented as a compiler-architecture co-design, where the compiler transparently reduces the bitwidth of program variables to their expected needs and the hardware monitors speculative variables, reporting misspeculation to the software, which re-executes at the original bitwidth, ensuring correctness. BitSpec reduces energy consumption by 9.9% on average, up to 28.2%.

## 中文摘要

微型设备已在人们的日常生活中无处不在。它们的应用决定了严格的能耗预算，但同时也需要合理的性能以满足用户期望。为此，微型设备的硬件已被高度优化，使得进一步的优化变得困难。在本工作中，我们识别出一个被忽视的机会：程序变量的位宽选择。如今的编译器直接将源码中指定的位宽翻译到二进制中。然而我们观察到，大多数变量在绝大部分执行时间里并未用满源码中指定的位宽。为利用这一机会，我们提出 BitSpec：一个对程序变量位宽进行细粒度投机的系统。BitSpec 以编译器—体系结构协同设计的方式实现，其中编译器将程序变量的位宽透明地缩减到其预期需求，硬件则监视投机变量，将投机失败报告给软件，软件以原始位宽重新执行，从而保证正确性。BitSpec 平均降低能耗 9.9%，最高达 28.2%。

## 英文关键词

Register Packing; Speculation

## 中文关键词

寄存器打包；投机

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716271)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5B](index.md) · [返回 ASPLOS 2025](../index.md)
