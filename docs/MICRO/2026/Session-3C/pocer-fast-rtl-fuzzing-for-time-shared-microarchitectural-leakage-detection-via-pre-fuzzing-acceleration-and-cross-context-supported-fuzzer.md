---
title: "PoCer: Fast RTL Fuzzing for Time-Shared Microarchitectural Leakage Detection via Pre-Fuzzing Acceleration and Cross-Context-Supported Fuzzer"
description: "MICRO 2026 · Session 3C · PoCer：通过预模糊测试加速与跨上下文支持，实现分时微架构泄漏的快速 RTL 模糊测试"
tags:
  - "MICRO2026"
  - "RTL"
---

# PoCer: Fast RTL Fuzzing for Time-Shared Microarchitectural Leakage Detection via Pre-Fuzzing Acceleration and Cross-Context-Supported Fuzzer

**中文标题：** PoCer：通过预模糊测试加速与跨上下文支持，实现分时微架构泄漏的快速 RTL 模糊测试

**所属 Session：** [Session 3C](index.md) · [MICRO 2026](../index.md)

**作者：** Pingfei Wu, Haixia Wang, Yun Chen, Pengfei Qiu, Dapeng Ju, Rihui Sun, Zikang Tao, Dongsheng Wang

**来源：** MICRO 2026，pp. 1166–1180；[DOI](https://doi.org/10.1109/MICRO67795.2026.00090)

## 英文摘要

Microarchitectural leakage remains a critical threat to modern CPUs, enabling side and covert channels that under mine fundamental isolation guarantees. Although recent RTL fuzzing techniques have shown promise, they still face two major challenges: inefficient testcase generation and inadequate evaluation under context switches. In this paper, we propose POCER, a novel fuzzing frame work that advances both the efficiency and practicality of CPU microarchitectural leakage detection. POCER integrates a frontend analyzer, POCER-FRONTEND, with a backend RTL fuzzer, POCER-BACKEND. POCER-FRONTEND is a general-purpose module that can synthesize high-quality testcases. By maximizing early exploration of microarchitectural states and instruction interactions, POCER-FRONTEND serves as a drop-in accelerator for existing leakage fuzzing frameworks. Experimental results show that integrating POCER-FRONTEND reduces the fuzzing time of state-of-the-art baselines by an average of 2.88&times;, while preserving the same coverage. To comprehensively evaluate microarchitectural leakages at context switch, POCER-FRONTEND incorporates context-switch simulation and passes state-retention insights to POCER BACKEND, enabling systematic discovery of cross-context leak ages. Unlike approaches that assume Trojan and spy execute within the same thread or process, POCER-BACKEND captures covert channels that persist across context switches, reflecting different security risk. POCER further defines minimal signal interfaces for easy integration into diverse RTL designs. We evaluate POCER on four open-source RISC-V cores—BOOMv3, CVA6, NutShell, and XiangShan—and successfully uncover all previously detected covert channels, along with 19 previously undocumented cross-process triggers. We further evolve these channels into practical side-channel leakages, demonstrating broader vulnerability coverage than the state-of-the-art.

## 中文摘要

微架构泄漏仍然是现代 CPU 的一个严重威胁，在基本隔离保证下启用侧通道和隐蔽通道。尽管最近的 RTL 模糊测试技术已显示出希望，但它们仍然面临两个主要挑战：低效的测试用例生成和上下文切换下的评估不足。在本文中，我们提出了 POCER，一种新颖的模糊框架，可提高 CPU 微架构泄漏检测的效率和实用性。 POCER 集成了前端分析器 POCER-FRONTEND 和后端 RTL 模糊器 POCER-BACKEND。 POCER-FRONTEND是一个通用模块，可以合成高质量的测试用例。通过最大化对微架构状态和指令交互的早期探索，POCER-FRONTEND 可充当现有泄漏模糊测试框架的嵌入式加速器。实验结果表明，集成 POCER-FRONTEND 将最先进基线的模糊时间平均减少了 2.88 倍，同时保持相同的覆盖范围。为了全面评估上下文切换时的微架构泄漏，POCER-FRONTEND 结合了上下文切换模拟，并将状态保留见解传递给 POCER BACKEND，从而能够系统地发现跨上下文泄漏年龄。与假设木马和间谍在同一线程或进程中执行的方法不同，POCER-BACKEND 捕获跨上下文切换持续存在的隐蔽通道，反映了不同的安全风险。 POCER 进一步定义了最小信号接口，以便轻松集成到不同的 RTL 设计中。我们在四个开源 RISC-V 内核（BOOMv3、CVA6、NutShell 和香山）上评估 POCER，并成功发现了所有先前检测到的隐蔽通道，以及 19 个先前未记录的跨进程触发器。我们进一步将这些通道发展为实用的侧通道泄漏，展示了​​比最先进技术更广泛的漏洞覆盖范围。

## 中文关键词

硬件安全；模糊测试；侧信道攻击；RTL；时分共享

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3C](index.md) · [MICRO 2026 主页](../index.md)
