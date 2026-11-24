---
title: "PF-LLM: Large Language Model Hinted Hardware Prefetching"
description: "ASPLOS 2026 · Session 8C · PF-LLM：大语言模型提示的硬件预取"
tags:
  - "ASPLOS2026"
  - "Session 8C"
  - "Memory Hierarchy & Performance"
---

# PF-LLM: Large Language Model Hinted Hardware Prefetching

**中文标题：** PF-LLM：大语言模型提示的硬件预取

**所属 Session：** [Session 8C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Ceyu Xu (The Hong Kong University of Science and Technology), Xiangfeng Sun (The Hong Kong University of Science and Technology), Weihang Li (Duke University), Chen Bai (The Hong Kong University of Science and Technology), Bangyan Wang (The Hong Kong University of Science and Technology), Mengming Li (The Hong Kong University of Science and Technology), Zhiyao Xie (The Hong Kong University of Science and Technology), Yuan Xie (The Hong Kong University of Science and Technology)

**单位：** The Hong Kong University of Science and Technology；Duke University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790202) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Hardware data prefetching is a critical technique for mitigating memory latency in modern processors. While sophisticated hardware prefetching algorithms exist, their exclusive reliance on runtime information limits their ability to adapt quickly and comprehend broader program context. Our key insight is that the optimal prefetching strategy for a load instruction is often discernible from its static code context—a task at which experienced developers excel. This motivates our central question: can a Large Language Model (LLM) be trained to perform this analysis automatically? We introduce PF-LLM, an LLM fine-tuned to analyze the assembly context surrounding a load instruction and generate prefetching hints. These offline-generated hints are consumed at runtime by LMHint Prefetcher, a lightweight hardware prefetcher ensemble designed to leverage this static guidance. Our approach boosts the performance of the on-chip hardware prefetcher by moving the hard “when, how, and how aggressively to prefetch” decisions out of the runtime hardware and into an offline LLM-powered analysis. This turns the on-chip prefetcher into a zero-latency, oraclelevel system that always follows the best prefetching policy for every single load instruction. Our evaluation shows that our approach achieves a 9.8% instruction-per-cycle (IPC) improvement on average for memory-intensive SPEC 2017 benchmarks over state-of-the-art hardware prefetching baselines and 18.9% improvement on average over state-of-theart ensemble methods, demonstrating the significant potential of leveraging LLMs to guide microarchitectural decisions.

## 中文摘要

硬件数据预取是缓解现代处理器内存延迟的关键技术。尽管已有复杂的硬件预取算法，但它们完全依赖运行时信息，这限制了其快速适应并理解更广泛程序上下文的能力。我们的关键洞见是：一条加载指令的最优预取策略往往可以从其静态代码上下文中辨识出来——这正是经验丰富的开发者所擅长的任务。这引出了我们的核心问题：能否训练一个大语言模型（LLM）来自动完成这一分析？我们提出 PF-LLM，一个经过微调的 LLM，用于分析加载指令周围的汇编上下文并生成预取提示。这些离线生成的提示在运行时由 LMHint Prefetcher 使用，后者是一个轻量级硬件预取器集成，旨在利用这种静态指导。我们的方法将“何时预取、如何预取、以多激进的方式预取”这些困难决策从运行时硬件转移到离线的 LLM 驱动分析中，从而提升片上硬件预取器的性能。这使片上预取器成为一个零延迟、达到预言机水平的系统，对每一条加载指令都始终遵循最佳预取策略。我们的评估显示，对于访存密集的 SPEC 2017 基准，相比最先进的硬件预取基线，我们的方法平均取得 9.8% 的每周期指令数（IPC）提升；相比最先进的集成方法平均提升 18.9%，展示了利用 LLM 指导微架构决策的巨大潜力。

## 英文关键词

Prefetching, Hardware Prefetcher, Large Language Model, CPU Microarchitecture

## 中文关键词

预取；硬件预取器；大语言模型；CPU 微架构

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790202)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8C](index.md) · [返回 ASPLOS 2026](../index.md)
