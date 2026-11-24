---
title: "Proactive Runtime Detection of Aging-Related Silent Data Corruptions: A Bottom-Up Approach"
description: "ASPLOS 2025 · Session 9C · 老化相关静默数据损坏的主动运行时检测：一种自底向上的方法"
tags:
  - "ASPLOS2025"
  - "Session 9C"
  - "Verification & Reliability"
---

# Proactive Runtime Detection of Aging-Related Silent Data Corruptions: A Bottom-Up Approach

**中文标题：** 老化相关静默数据损坏的主动运行时检测：一种自底向上的方法

**所属 Session：** [Session 9C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jiacheng Ma (University of Michigan), Majd Ganaiem (Technion – Israel Institute of Technology), Madeline Burbage (University of Washington), Theo Gregersen (University of Washington), Rachel McAmis (University of Washington), Freddy Gabbay (The Hebrew University of Jerusalem), Baris Kasikci (University of Washington,Google)

**单位：** University of Michigan；Technion – Israel Institute of Technology；University of Washington；The Hebrew University of Jerusalem；University of Washington,Google

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674182) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Recent advancements in semiconductor process technologies have unveiled the susceptibility of hardware circuits to reliability issues, especially those related to transistor aging. Transistor aging gradually degrades gate performance, eventually causing hardware to behave incorrectly. Such misbehaving hardware can result in silent data corruptions (SDCs) in software—a type of failure that comes without logs or exceptions, but causes miscomputing instructions, bitflips, and broken cache coherency. Alas, while design efforts can be made to mitigate transistor aging, complete elimination of this problem during design and fabrication cannot be guaranteed. This emerging challenge calls for a mechanism that not only detects potentially aged hardware in the field, but also triggers software mitigations at application runtime. We propose Vega, a novel workflow that allows efficient detection of aging-related failures at software runtime. Vega leverages the well-studied gate-level modeling of aging effects to identify susceptible signal propagation paths that could fail due to transistor aging. It then utilizes formal verification techniques to generate short test cases that activate these paths and detect any failure within them. Vega integrates the test cases into a user application by directly fusing them together, or by packaging the test cases into a library that the application can invoke. We demonstrate our proposed techniques on the arithmetic logic unit and floating-point unit of a RISC-V CPU. We show that Vega generates effective test cases and integrates them into applications with an average of 0.8% performance overhead.

## 中文摘要

半导体工艺技术的最新进展揭示了硬件电路对可靠性问题的易感性，尤其是与晶体管老化相关的问题。晶体管老化会逐步降低门级性能，最终导致硬件行为出错。此类行为异常的硬件会在软件中造成静默数据损坏（SDC）——这类故障不产生日志或异常，却会导致指令计算错误、比特翻转以及缓存一致性被破坏。尽管可以通过设计上的努力来缓解晶体管老化，但无法保证在设计与制造阶段完全消除该问题。这一新出现的挑战需要一种机制，不仅能检测现场中可能已老化的硬件，还能在应用运行时触发软件缓解措施。我们提出 Vega，一种新颖的工作流程，可在软件运行时高效检测老化相关故障。Vega 利用已被充分研究的老化效应门级建模，识别可能因晶体管老化而失效的易感信号传播路径。随后它利用形式化验证技术生成简短测试用例，以激活这些路径并检测其中的任何故障。Vega 通过直接将测试用例与应用融合，或将测试用例打包成应用可调用的库，从而将其集成到用户应用中。我们在 RISC-V CPU 的算术逻辑单元与浮点单元上演示了所提出的技术。我们表明，Vega 能生成有效的测试用例并将其集成到应用中，平均性能开销仅为 0.8%。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674182)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9C](index.md) · [返回 ASPLOS 2025](../index.md)
