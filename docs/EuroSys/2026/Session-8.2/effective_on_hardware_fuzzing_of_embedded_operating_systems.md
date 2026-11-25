---
title: "Effective On-Hardware Fuzzing of Embedded Operating Systems"
description: "EuroSys 2026 · Security, Privacy & Vulnerabilities · Yuheng Shen (Tsinghua University), Jianzhong Liu (Shandong University), Qiming G"
tags:
  - "EuroSys2026"
  - "Security, Privacy & Vulnerabilities"
---

# Effective On-Hardware Fuzzing of Embedded Operating Systems

**中文标题：** 面向嵌入式操作系统的有效硬件在环模糊测试

**所属 Session：** [Session 8.2: Security, Privacy & Vulnerabilities](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Security, Privacy & Vulnerabilities。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Security, Privacy & Vulnerabilities</p>
</div>

**作者**：Yuheng Shen (Tsinghua University), Jianzhong Liu (Shandong University), Qiming Guo (Beihang University), Yifei Chu (Tsinghua University), Qiang Zhang (Hunan University), Heyuan Shi (Central South University), Yu Jiang (Tsinghua University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769326)

## 英文摘要

Fuzz testing embedded OSs is difficult because their implementations vary widely and rely on specialized hardware. These factors render many existing methods ineffective, since they prevent adapting established fuzzing routines, disrupt communication with the target OS, and impede observation of runtime behavior. This paper introduces EOF, a feedback-guided fuzzer designed to test embedded OSs running on actual hardware. Through the debug port, EOF communicates with the target embedded OS, executes test cases, and collect feedback data, with no dependence on OS services. Then, EOF deploys a cross-platform agent and executes API-aware input across diverse hardware. Last, EOF collects runtime coverage and critical execution events to identify interesting seeds and find potential bugs during fuzzing. We implemented EOF and evaluated its performance on four different embedded OSs, where EOF discovered 19 bugs and achieved a 50.84% coverage improvement on average compared with other comparable fuzzing methods.

## 中文摘要

对嵌入式操作系统进行模糊测试十分困难，因为其实现差异很大且依赖专用硬件。这些因素使许多现有方法失效，因为它们无法适配已有的模糊测试流程、会破坏与目标操作系统的通信，并妨碍对运行时行为的观测。本文提出 EOF，一个反馈引导的模糊测试器，用于测试运行在真实硬件上的嵌入式操作系统。EOF 通过调试端口与目标嵌入式操作系统通信、执行测试用例并收集反馈数据，完全不依赖操作系统服务。随后，EOF 部署跨平台代理，在多种硬件上执行 API 感知的输入。最后，EOF 收集运行时覆盖率和关键执行事件，以识别有价值的种子并在模糊测试过程中发现潜在缺陷。我们实现了 EOF 并在四种不同的嵌入式操作系统上评估其表现，EOF 共发现 19 个缺陷，与其他同类模糊测试方法相比平均覆盖率提升 50.84%。

**英文关键词：** Fuzz Testing, Embedded Operating System

**中文关键词：** 模糊测试、嵌入式操作系统

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
