---
title: "Signal Breaker: Fuzzing Digital Signal Processors"
description: "ASPLOS 2026 · Session 7C · Signal Breaker：数字信号处理器的模糊测试"
tags:
  - "ASPLOS2026"
  - "Session 7C"
  - "Testing & Fuzzing"
---

# Signal Breaker: Fuzzing Digital Signal Processors

**中文标题：** Signal Breaker：数字信号处理器的模糊测试

**所属 Session：** [Session 7C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Cameron Garcia (Virginia Tech), Matthew Hicks (Virginia Tech)

**单位：** Virginia Tech

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790220) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Fuzzing is one of the most effective techniques for discovering software vulnerabilities. Fuzzers use feedback from prior executions to generate new test cases via random mutation, executing these inputs to uncover bugs. Fuzzing has been successfully applied to applications, operating systems, processors, and network protocols, making it one of the most widely adopted software testing methodologies. Despite this success, fuzzing has seen little adoption for Digital Signal Processor (DSP) software. DSPs occupy a unique position at the boundary of hardware and software: they ingest signals from the physical world, execute software instructions, and are tightly integrated into data-processing pipelines. Many safety- and security-critical domains, including telecommunications, transportation, and defense, rely heavily on DSPs, making robust DSP testing essential. To address this gap, we introduce SBFUZZ, a coverage-guided fuzzer designed specifically for DSP software. SBFUZZ is driven by three key observations: (1) DSPs expose limited and high-latency execution control and communication interfaces, and (2) DSPs have unique architectures that necessitate new instrumentation and mutation routines, and (3) DSP fuzzing must detect both traditional software bugs manifested as crashes and hardware-style bugs manifested as divergent yet continuing execution. Based on these insights, SBFUZZ advocates a DSP-centric fuzzer decomposition, where the DSP executes most fuzzing tasks autonomously while periodically leveraging a more powerful host for coordination, analysis, and storage. This design allows a single host to concurrently fuzz multiple end devices and supports both physical DSPs and simulated DSPs for re-hosted fuzzing. We implement SBFUZZ on a Texas Instruments TMS320C5515 DSP and evaluate it on 15 DSP benchmark programs. Our results show that SBFUZZ achieves 17.4x higher throughput and 2.6x greater code coverage than prior embedded fuzzing approaches applied to DSPs, uncovering 2491 unique crashes, yielding 34 unique bugs.

## 中文摘要

模糊测试是发现软件漏洞最有效的技术之一。模糊测试器利用先前执行的反馈，通过随机变异生成新的测试用例，并执行这些输入以发现缺陷。模糊测试已成功应用于应用程序、操作系统、处理器和网络协议，使其成为最广泛采用的软件测试方法之一。尽管取得了这些成功，模糊测试在数字信号处理器（DSP）软件中却鲜有采用。DSP 处于硬件与软件的交界处，占据独特的位置：它们从物理世界摄取信号、执行软件指令，并紧密集成到数据处理流水线中。包括电信、交通和国防在内的许多安全与安保关键领域都高度依赖 DSP，因此稳健的 DSP 测试至关重要。为弥补这一空白，我们提出 SBFUZZ，一个专为 DSP 软件设计的覆盖率引导模糊测试器。SBFUZZ 由三个关键观察驱动：（1）DSP 暴露的执行控制与通信接口有限且延迟很高；（2）DSP 具有独特的体系结构，需要新的插桩与变异例程；（3）DSP 模糊测试必须既能检测表现为崩溃的传统软件缺陷，也能检测表现为执行偏离但继续运行的硬件式缺陷。基于这些洞见，SBFUZZ 主张以 DSP 为中心的模糊测试器分解，即由 DSP 自主执行大部分模糊测试任务，同时周期性地借助性能更强的主机进行协调、分析和存储。该设计允许单台主机并发地对多个终端设备进行模糊测试，并同时支持物理 DSP 与模拟 DSP 以实现重托管模糊测试。我们在 Texas Instruments TMS320C5515 DSP 上实现 SBFUZZ，并在 15 个 DSP 基准程序上对其进行评估。结果表明，与先前应用于 DSP 的嵌入式模糊测试方法相比，SBFUZZ 的吞吐量高出 17.4 倍、代码覆盖率高出 2.6 倍，发现了 2491 个唯一崩溃，最终得到 34 个唯一缺陷。

## 英文关键词

Fuzzing, Digital Signal Processors, Re-hosting, Semi-hosting, Embedded Devices

## 中文关键词

模糊测试；数字信号处理器；重托管；半托管；嵌入式设备

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790220)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7C](index.md) · [返回 ASPLOS 2026](../index.md)
