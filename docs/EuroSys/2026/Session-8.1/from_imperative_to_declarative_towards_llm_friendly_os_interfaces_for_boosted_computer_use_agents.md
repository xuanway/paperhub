---
title: "From Imperative to Declarative: Towards LLM-friendly OS Interfaces for Boosted Computer-Use Agents"
description: "EuroSys 2026 · LLM Serving & Agents · Yuan Wang (Key Laboratory of System Software (Chinese Academy of Sciences); Inst"
tags:
  - "EuroSys2026"
  - "LLM Serving & Agents"
---

# From Imperative to Declarative: Towards LLM-friendly OS Interfaces for Boosted Computer-Use Agents

**中文标题：** 从命令式到声明式：面向 LLM 友好的操作系统接口以增强计算机使用智能体

**所属 Session：** [Session 8.1: LLM Serving & Agents](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Serving & Agents。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Serving & Agents</p>
</div>

**作者**：Yuan Wang (Key Laboratory of System Software (Chinese Academy of Sciences); Institute of Software, Chinese Academy of Sciences; University of Chinese Academy of Sciences), Mingyu Li (Key Laboratory of System Software (Chinese Academy of Sciences); Institute of Software, Chinese Academy of Sciences), Haibo Chen (Key Laboratory of System Software (Chinese Academy of Sciences); Institute of Software, Chinese Academy of Sciences; Shanghai Jiao Tong University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803576)

## 英文摘要

Computer-use agents (CUAs) powered by large language models (LLMs) have emerged as a promising approach to automating computer tasks, yet they struggle with the existing human-oriented OS interfaces—graphical user interfaces (GUIs). GUIs force LLMs to decompose high-level goals into lengthy, error-prone sequences of fine-grained actions, resulting in low success rates and an excessive number of LLM calls.

We propose Declarative Model Interface (DMI), an abstraction that transforms existing GUIs into three declarative primitives: access, state, and observation, thereby providing novel OS interfaces tailored for LLM agents. Our key idea is policy-mechanism separation: LLMs focus on high-level semantic planning (policy) while DMI handles low-level navigation and interaction (mechanism). DMI does not require modifying the application source code or relying on application programming interfaces (APIs).

We evaluate DMI with Microsoft Office Suite (Word, PowerPoint, Excel) on Windows. Integrating DMI into a leading GUI-based agent baseline improves task success rates by 67% and reduces interaction steps by 43.5%. Notably, DMI completes over 61% of successful tasks with a single LLM call.

## 中文摘要

由大语言模型（LLM）驱动的计算机使用智能体（CUA）已成为自动化计算机任务的一种有前景的途径，但它们难以应对现有面向人类的操作系统接口——图形用户界面（GUI）。GUI 迫使 LLM 将高层目标分解为冗长且易错的细粒度动作序列，导致成功率低、LLM 调用次数过多。

我们提出声明式模型接口（DMI），这是一种将现有 GUI 转换为三种声明式原语的抽象——访问、状态与观测，从而为 LLM 智能体提供量身定制的新型操作系统接口。我们的核心思想是策略与机制分离：LLM 专注于高层语义规划（策略），而 DMI 负责底层导航与交互（机制）。DMI 无需修改应用源代码，也不依赖应用程序编程接口（API）。

我们在 Windows 上使用 Microsoft Office 套件（Word、PowerPoint、Excel）评估 DMI。将 DMI 集成到一个领先的基于 GUI 的智能体基线中，任务成功率提升 67%，交互步数减少 43.5%。值得注意的是，DMI 有超过 61% 的成功任务仅通过一次 LLM 调用即可完成。

**英文关键词：** OS abstraction, Interface design, LLM-friendly OS interfaces

**中文关键词：** 操作系统抽象、接口设计、LLM 友好的操作系统接口

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
