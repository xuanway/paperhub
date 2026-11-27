---
title: "TraceRTL: Agile Performance Evaluation for Microarchitecture Exploration"
description: "HPCA 2026 · LLM Systems and Microarchitecture Tools"
tags:
  - "HPCA2026"
  - "LLM Systems and Microarchitecture Tools"
---

# TraceRTL: Agile Performance Evaluation for Microarchitecture Exploration

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: LLM Systems and Microarchitecture Tools。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · LLM Systems and Microarchitecture Tools</p>
</div>

**论文链接**：
**作者**：Zifei Zhang SKLP, Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences , Yinan Xu SKLP, Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences , Sa Wang SKLP, Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences , Dan Tang SKLP, Institute of Computing Technology, Chinese Academy of Sciences; Beijing Institute of Open Source Chip , Yungang Bao State Key Lab of Processors, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences
**会议**：HPCA 2026

---

## 中文标题

TraceRTL：面向微架构探索的敏捷性能评估

## 英文摘要

While agile chip development methodologies have accelerated RTL design and simulation, performance evaluation remains constrained by three challenges: (1) inefficient feature prototyping caused by the tight coupling between functional correctness and performance evaluation, particularly for large-scale, error-prone microarchitectures; (2) limited workloads due to incomplete peripheral/software environments or unavailable source code; and (3) time-consuming warm-up phases in sampling-based simulation, required to mitigate cold-start effects. To address these challenges, we propose TRACERTL, an agile, trace-driven performance evaluation methodology that decouples the functional and performance components of CPU RTL designs. It introduces three techniques: (1) a trace-driven performance exploration framework that bypasses full functional correctness while preserving performance accuracy; (2) a trace transformation technique, TraceBridge, that replays traces across different formats and instruction sets; and (3) a fast warm-up strategy, TraceDedup, that eliminates redundant traces and efficiently initializes microarchitectural states. Using TRACERTL, we develop the first trace-driven RTL CPU derived from XiangShan, a high-performance out-of-order RISC-V processor. TRACERTL achieves performance accuracies of 99.87% and 99.86% on SPECint2017 and SPECfp2017, respectively. With TraceBridge, we evaluate x86-based Google workload traces on a RISC-V RTL CPU and reveal distinct memory-bound behavior. TraceDedup further accelerates warm-up phases in sampling-based simulations by 1.5× to 11.8×.

## 中文摘要

尽管敏捷芯片开发方法学加速了 RTL 设计与模拟，性能评估仍受三方面制约：(1) 功能正确性与性能评估紧耦合导致特性原型设计效率低下，对大规模、易出错的微架构尤为如此；(2) 因外设/软件环境不完整或源代码不可得，可用负载受限；(3) 基于采样的模拟中，为缓解冷启动效应所需的预热阶段耗时很长。为应对这些挑战，我们提出 TRACERTL，一种敏捷的、轨迹驱动的性能评估方法学，将 CPU RTL 设计的功能部分与性能部分解耦。它引入三项技术：(1) 轨迹驱动的性能探索框架，在保持性能精度的同时绕过完整的功能正确性；(2) 轨迹变换技术 TraceBridge，可在不同格式与指令集之间重放轨迹；(3) 快速预热策略 TraceDedup，消除冗余轨迹并高效初始化微架构状态。借助 TRACERTL，我们开发了首个源自高性能乱序 RISC-V 处理器香山（XiangShan）的轨迹驱动 RTL CPU。TRACERTL 在 SPECint2017 与 SPECfp2017 上的性能精度分别达到 99.87% 与 99.86%。借助 TraceBridge，我们在 RISC-V RTL CPU 上评估了基于 x86 的 Google 负载轨迹，揭示了明显的内存受限行为。TraceDedup 进一步将基于采样的模拟中的预热阶段加速 1.5 倍至 11.8 倍。
