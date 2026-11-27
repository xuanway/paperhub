---
title: "LEGO: Supporting LLM-enhanced Games with One Gaming GPU"
description: "HPCA 2026 · GPU Memory Management and Multi-Chiplet Systems"
tags:
  - "HPCA2026"
  - "GPU Memory Management and Multi-Chiplet Systems"
---

# LEGO: Supporting LLM-enhanced Games with One Gaming GPU

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: GPU Memory Management and Multi-Chiplet Systems。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · GPU Memory Management and Multi-Chiplet Systems</p>
</div>

**论文链接**：
**作者**：Han Zhao Shanghai Jiao Tong University , Weihao Cui Shanghai Jiao Tong University , Zeshen Zhang Tongji University , Wenhao Zhang Shanghai Jiao Tong University , Jiangtong Li Tongji University , Quan Chen Shanghai Jiao Tong University, China , Youmin Chen Shanghai Jiao Tong University , Pu Pang Shanghai Jiao Tong University , Zijun Li Shanghai Jiao Tong University , Zhenhua Han The University of Hong Kong , Yuqing Yang Microsoft Research , Minyi Guo Shanghai Jiao Tong University
**会议**：HPCA 2026

---

## 中文标题

LEGO：用单块游戏 GPU 支撑 LLM 增强的游戏

## 英文摘要

Artificial intelligence (AI) has been increasingly applied to gaming, with large language models (LLMs) playing a key role in character control. However, efficiently co-locating game rendering and LLM inference on one GPU presents challenges due to resource constraints, diverse latency requirements, and fine-grained task scheduling. We propose LEGO, an algorithm-system co-design that enables the efficient colocation of LLM inference and game rendering tasks. Algorithm-wise, LEGO features a resource-oriented layer-skipping adaptor, which distills knowledge from skipped layers to reduce computational demand while maintaining inference accuracy. System-wise, LEGO proposes a headroom-maximizing LLM scheduler, which dynamically partitions inference tasks to utilize available rendering headroom. Evaluations on an Nvidia RTX 4090 show that LEGO meets latency targets in all scenarios, improves rendering headroom utilization by up to 28.6%, and reduces LLM inference accuracy loss by up to 86.3% compared to current layer-skipping approaches.

## 中文摘要

人工智能（AI）正日益应用于游戏领域，其中大语言模型（LLM）在角色控制中扮演着关键角色。然而，由于资源受限、时延需求多样以及任务调度粒度细，在同一块 GPU 上高效地共置游戏渲染与 LLM 推理面临诸多挑战。我们提出 LEGO，一种算法与系统协同设计，可实现 LLM 推理任务与游戏渲染任务的高效共置。在算法层面，LEGO 设计了面向资源的跳层适配器，它从被跳过的层中蒸馏知识，从而在保持推理精度的同时降低计算需求。在系统层面，LEGO 提出一种最大化余量的 LLM 调度器，动态划分推理任务，以利用渲染过程中可用的余量。在 NVIDIA RTX 4090 上的评估表明，LEGO 在所有场景下都满足了时延目标，相比当前跳层方法将渲染余量利用率最高提升 28.6%，并将 LLM 推理精度损失最高降低 86.3%。
