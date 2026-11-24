---
title: "Empower Vision Applications with LoRA LMM"
description: "EuroSys 2025 · LLM Serving · Liang Mi (Nanjing University), Weijun Wang (Institute for AI Industry Research ("
tags:
  - "EuroSys2025"
  - "LLM Serving"
---

# Empower Vision Applications with LoRA LMM

**中文标题：** 利用 LoRA 大型多模态模型增强视觉应用

**所属 Session：** [Session 2.2: LLM Serving](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Serving。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Serving</p>
</div>

**作者**：Liang Mi (Nanjing University), Weijun Wang (Institute for AI Industry Research (AIR), Tsinghua University), Wenming Tu (Institute for AI Industry Research (AIR), Tsinghua University), Qingfeng He (Institute for AI Industry Research (AIR), Tsinghua University), Kui Kong (Institute for AI Industry Research (AIR), Tsinghua University), Xinyu Fang (Institute for AI Industry Research (AIR), Tsinghua University), Yazhu Dong (Institute for AI Industry Research (AIR), Tsinghua University), Yikang Zhang (Nanjing University), Yuanchun Li (Institute for AI Industry Research (AIR), Tsinghua University), Meng Li (Nanjing University), Haipeng Dai (Nanjing University), Guihai Chen (Nanjing University), Yunxin Liu (Institute for AI Industry Research (AIR), Tsinghua University), Weijun Wang (Tsinghua University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717472)

## 英文摘要

Large Multimodal Models (LMMs) have shown significant progress in various complex vision tasks with the solid linguistic and reasoning capacity inherited from large language models (LMMs). Low-rank adaptation (LoRA) offers a promising method to integrate external knowledge into LMMs, compensating for their limitations on domain-specific tasks. However, the existing LoRA model serving is excessively computationally expensive and causes extremely high latency. In this paper, we present an end-to-end solution that empowers diverse vision tasks and enriches vision applications with LoRA LMMs. Our system, VaLoRA, enables accurate and efficient vision tasks by 1) an accuracy-aware LoRA adapter generation approach that generates LoRA adapters rich in domain-specific knowledge to meet application-specific accuracy requirements, 2) an adaptive-tiling LoRA adapters batching operator that efficiently computes concurrent heterogeneous LoRA adapters, and 3) a flexible LoRA adapter orchestration mechanism that manages application requests and LoRA adapters to achieve the lowest average response latency. We prototype VaLoRA on five popular vision tasks on three LMMs. Experiment results reveal that VaLoRA improves 24-62% of the accuracy compared to the original LMMs and reduces 20-89% of the latency compared to the state-of-the-art LoRA model serving systems.

## 中文摘要

大型多模态模型（LMM）继承了大语言模型（LLM）扎实的语言与推理能力，在各种复杂视觉任务上取得了显著进展。低秩适配（LoRA）为将外部知识注入 LMM 提供了一种有前景的方法，可弥补其在领域特定任务上的不足。然而，现有的 LoRA 模型服务计算开销过高，导致延迟极高。本文提出一套端到端方案，以 LoRA LMM 赋能多样化的视觉任务并丰富视觉应用。我们的系统 VaLoRA 通过以下方式实现准确而高效的视觉任务：1）精度感知的 LoRA 适配器生成方法，生成富含领域特定知识的 LoRA 适配器以满足应用特定的精度需求；2）自适应分块的 LoRA 适配器批处理算子，高效计算并发的异构 LoRA 适配器；3）灵活的 LoRA 适配器编排机制，管理应用请求与 LoRA 适配器以实现最低的平均响应延迟。我们在三种 LMM 的五个流行视觉任务上对 VaLoRA 进行了原型实现。实验结果表明，与原始 LMM 相比，VaLoRA 将精度提升 24%–62%；与最先进的 LoRA 模型服务系统相比，将延迟降低 20%–89%。

**英文关键词：** Large language model, Machine learning system

**中文关键词：** 大语言模型、机器学习系统

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
