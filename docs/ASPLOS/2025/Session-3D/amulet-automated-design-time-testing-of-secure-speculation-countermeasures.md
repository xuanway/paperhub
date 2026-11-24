---
title: "AMuLeT: Automated Design-Time Testing of Secure Speculation Countermeasures"
description: "ASPLOS 2025 · Session 3D · AMuLeT：安全推测缓解措施的自动化设计期测试"
tags:
  - "ASPLOS2025"
  - "Session 3D"
  - "EDA"
---

# AMuLeT: Automated Design-Time Testing of Secure Speculation Countermeasures

**中文标题：** AMuLeT：安全推测缓解措施的自动化设计期测试

**所属 Session：** [Session 3D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Bo Fu (University of Toronto), Leo Tenenbaum (University of Toronto), David Adler (University of Toronto), Assaf Klein (Technion – Israel Institute of Technology), Arpit Gogia (IMDEA Software Institute), Alaa R. Alameldeen (Simon Fraser University), Marco Guarnieri (IMDEA Software Institute), Mark Silberstein (Technion – Israel Institute of Technology), Oleksii Oleksenko (Azure Research, Microsoft), Gururaj Saileshwar (University of Toronto)

**单位：** University of Toronto；Technion – Israel Institute of Technology；IMDEA Software Institute；Simon Fraser University；Azure Research, Microsoft

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716247) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

In recent years, several hardware-based countermeasures proposed to mitigate Spectre attacks have been shown to be insecure. To enable the development of effective secure speculation countermeasures, we need easy-to-use tools that can automatically test their security guarantees early-on in the design phase to facilitate rapid prototyping. This paper develops AMuLeT, the first tool capable of testing secure speculation countermeasures for speculative leakage early in their design phase in simulators. Our key idea is to leverage model-based relational testing tools that can detect speculative leaks in commercial CPUs, and apply them to micro-architectural simulators to test secure speculation defenses. We identify and overcome several challenges, ∗Bo and Leo contributed equally as lead authors for this paper including designing an expressive yet realistic attacker observer model in a simulator, overcoming the slow simulation speed, and searching the vast micro-architectural state space for potential vulnerabilities. AMuLeT speeds up test throughput by more than 10× compared to a naive design and uses techniques to amplify vulnerabilities to uncover them within a limited test budget. Using AMuLeT, we launch for the first time, a systematic, large-scale testing campaign of four secure speculation countermeasures from 2018 to 2024—InvisiSpec, CleanupSpec, STT, and SpecLFB—and uncover 3 known and 6 unknown bugs and vulnerabilities, within 3 hours of testing. We also show for the first time that the open-source implementation of SpecLFB is insecure.

## 中文摘要

近年来，若干为缓解 Spectre 攻击而提出的基于硬件的缓解措施已被证明并不安全。为了能够开发有效的安全推测缓解措施，我们需要易于使用的工具，能够在设计阶段早期自动测试其安全保证，从而支持快速原型开发。本文提出 AMuLeT，这是首个能够在模拟器中于设计早期阶段测试安全推测缓解措施的推测泄漏的工具。我们的核心思路是利用能够在商用 CPU 中检测推测泄漏的基于模型的关系测试工具，并将其应用于微体系结构模拟器以测试安全推测防御。我们识别并克服了若干挑战，∗Bo 和 Leo 作为本文的共同第一作者贡献相同，包括在模拟器中设计一个表达力强而又贴近现实的攻击者观察者模型、克服缓慢的模拟速度，以及在海量的微体系结构状态空间中搜索潜在漏洞。与朴素设计相比，AMuLeT 将测试吞吐率提升 10 倍以上，并使用多种技术放大漏洞，以在有限的测试预算内发现它们。使用 AMuLeT，我们首次对 2018 至 2024 年的四种安全推测缓解措施——InvisiSpec、CleanupSpec、STT 和 SpecLFB——开展了系统化的大规模测试活动，并在 3 小时的测试时间内发现了 3 个已知和 6 个未知的缺陷与漏洞。我们还首次表明 SpecLFB 的开源实现并不安全。

## 英文关键词

Side Channels, Spectre, Defenses, Fuzzing

## 中文关键词

边信道；Spectre；防御；模糊测试

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716247)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3D](index.md) · [返回 ASPLOS 2025](../index.md)
