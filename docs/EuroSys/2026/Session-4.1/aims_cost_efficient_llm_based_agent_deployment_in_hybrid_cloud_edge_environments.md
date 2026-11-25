---
title: "AIMS: Cost-Efficient LLM-Based Agent Deployment in Hybrid Cloud-Edge Environments"
description: "EuroSys 2026 · On-Device & Federated Learning · Shiyi Liu (University of Virginia), Haiying Shen (University of Virginia), Shuai"
tags:
  - "EuroSys2026"
  - "On-Device & Federated Learning"
---

# AIMS: Cost-Efficient LLM-Based Agent Deployment in Hybrid Cloud-Edge Environments

**中文标题：** AIMS：混合云边环境中成本高效的基于 LLM 的智能体部署

**所属 Session：** [Session 4.1: On-Device & Federated Learning](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：On-Device & Federated Learning。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · On-Device & Federated Learning</p>
</div>

**作者**：Shiyi Liu (University of Virginia), Haiying Shen (University of Virginia), Shuai Che (Microsoft), Mahdi Ghandi (Microsoft), Mingqin Li (Microsoft)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803622)

## 英文摘要

In the realm of AI, large language models (LLMs) like GPT-5, central to the operation of AI agents, predominantly operate in the cloud, incurring high operational costs. With local-based small language models (SLMs) becoming more accurate, the necessity of cloud-exclusive processing is being reconsidered. An AI agent’s response to a user’s request comprises a series of subtasks or iterations. Existing approaches choose either an LLM or SLM for the entire request to ensure similar outputs, but this is ineffective for AI agents as SLMs may generate differing subtasks, compromising final accuracy. In this paper, we first conduct experimental analysis to understand the features of AI agent operations. Leveraging our findings, we propose the Adaptive Iteration-level Model Selector (AIMS), a lightweight scheduler to automatically partition an AI agent’s subtasks between local-based SLM and cloud-based LLM. AIMS considers the varying subtask features and strategically decides the location for each subtask in order to use SLM as much as possible while maintaining the accuracy level. Our experimental results demonstrate that AIMS achieves up to a 27.5% relative improvement in accuracy and up to 31.4% relative increase in SLM usage compared to HybridLLM. It offloads 83.4% of subtasks to a local SLM while attaining similar accuracy on average compared with the cloud-only LLM approach.

## 中文摘要

在 AI 领域，作为 AI 智能体运行核心的大语言模型（LLM，如 GPT-5）主要运行在云端，带来高昂的运营成本。随着本地小语言模型（SLM）越来越准确，仅依赖云端处理的必要性正被重新审视。AI 智能体对用户请求的响应由一系列子任务或迭代组成。现有方法为整个请求选择 LLM 或 SLM 以保证输出相似，但这对 AI 智能体并不有效，因为 SLM 可能生成不同的子任务，从而损害最终准确率。本文首先进行实验分析以理解 AI 智能体运行的特征。基于我们的发现，我们提出自适应迭代级模型选择器（AIMS），一个轻量级调度器，自动在本地 SLM 和云端 LLM 之间划分 AI 智能体的子任务。AIMS 考虑各子任务的不同特征，策略性地决定每个子任务的位置，以尽可能多地使用 SLM 同时保持准确率水平。实验结果表明，与 HybridLLM 相比，AIMS 的准确率相对提升最多 27.5%，SLM 使用率相对提升最多 31.4%。它将 83.4% 的子任务卸载到本地 SLM，同时平均达到与纯云端 LLM 方法相似的准确率。

**英文关键词：** LLM systems, AI agents, hybrid cloud-edge computing, model routing, cost optimization, small language models, scheduling

**中文关键词：** LLM 系统、AI 智能体、混合云边计算、模型路由、成本优化、小语言模型、调度

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
