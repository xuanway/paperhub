---
title: "The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective"
description: "HPCA 2026 · LLM Inference Serving Systems"
tags:
  - "HPCA2026"
  - "LLM Inference Serving Systems"
---

# The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: LLM Inference Serving Systems。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · LLM Inference Serving Systems</p>
</div>

**论文链接**：
**作者**：Jiin Kim KAIST , Byeongjun Shin KAIST , Jinha Chung KAIST , Minsoo Rhu KAIST
**会议**：HPCA 2026

---

## 中文标题

动态推理的代价：从 AI 基础设施视角解析 AI 智能体与测试时扩展

## 英文摘要

Large-language-model (LLM)–based AI agents have recently showcased impressive versatility by employing dynamic reasoning, an adaptive, multi-step process that coordinates with external tools. This shift from static, single-turn inference to agentic, multi-turn workflows broadens task generalization and behavioral flexibility, but it also introduces serious concerns about system-level cost, efficiency, and sustainability. This paper presents the first comprehensive system-level analysis of AI agents, quantifying their resource usage, latency behavior, energy consumption, and datacenter-wide power consumption demands across diverse agent designs and test-time scaling strategies. We further characterize how AI agent design choices, such as few-shot prompting, reflection depth, and parallel reasoning, impact accuracy-cost tradeoffs. Our findings reveal that while agents improve accuracy with increased compute, they suffer from rapidly diminishing returns, widening latency variance, and unsustainable infrastructure costs. Through detailed evaluation of representative agents, we highlight the profound computational demands introduced by AI agent workflows, uncovering a looming sustainability crisis. These results call for a paradigm shift in agent design toward compute-efficient reasoning, balancing performance with deployability under real-world constraints.

## 中文摘要

近期，基于大语言模型（LLM）的 AI 智能体展现出令人印象深刻的多功能性，它们采用动态推理——一种与外部工具协同的自适应多步过程。这种从静态单轮推理向智能体化多轮工作流的转变，拓宽了任务泛化范围与行为灵活性，但也引发了关于系统级成本、效率与可持续性的严重担忧。本文首次给出 AI 智能体的全面系统级分析，在多种智能体设计与测试时扩展策略下量化其资源使用、时延行为、能耗以及数据中心范围的功耗需求。我们进一步刻画了 AI 智能体设计选择（如少样本提示、反思深度与并行推理）对精度—成本权衡的影响。研究发现，尽管智能体可随算力增加而提升精度，但其收益迅速递减、时延方差不断扩大，且基础设施成本不可持续。通过对代表性智能体的详细评测，我们揭示了 AI 智能体工作流带来的巨大计算需求，暴露出迫近的可持续性危机。这些结果呼唤智能体设计向计算高效推理转变范式，在真实世界约束下平衡性能与可部署性。
