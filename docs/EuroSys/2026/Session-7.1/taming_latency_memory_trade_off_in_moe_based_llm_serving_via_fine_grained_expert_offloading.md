---
title: "Taming Latency-Memory Trade-Off in MoE-Based LLM Serving via Fine-Grained Expert Offloading"
description: "EuroSys 2026 · LLM Inference · Hanfei Yu (Stevens Institute of Technology), Xingqi Cui (Rice University), Hong "
tags:
  - "EuroSys2026"
  - "LLM Inference"
---

# Taming Latency-Memory Trade-Off in MoE-Based LLM Serving via Fine-Grained Expert Offloading

**中文标题：** 通过细粒度专家卸载驾驭基于 MoE 的 LLM 服务中的延迟-内存权衡

**所属 Session：** [Session 7.1: LLM Inference](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Inference。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Inference</p>
</div>

**作者**：Hanfei Yu (Stevens Institute of Technology), Xingqi Cui (Rice University), Hong Zhang (University of Waterloo), Hao Wang (Rutgers University), Hao Wang (Stevens Institue of Technology)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769319)

## 英文摘要

Large Language Models (LLMs) have gained immense success in revolutionizing various applications, including content generation, search and recommendation, and AI-assisted operations. To reduce high training costs, Mixture-of-Experts (MoE) architecture has become a popular backbone for modern LLMs. However, despite the benefits, serving MoE-based LLMs experience severe memory inefficiency due to sparsely activated experts. Recent studies propose to offload inactive experts from GPU memory to CPU memory to improve the serving efficiency of MoE models. However, they either incur high inference latency or high model memory footprints due to coarse-grained designs.

To tame the latency-memory trade-off in MoE serving, we present FineMoE, a fine-grained expert offloading system for MoE serving that achieves low inference latency with memory efficiency. We design FineMoE to extract fine-grained expert selection patterns from MoE models and semantic hints from input prompts to efficiently guide expert prefetching, caching, and offloading decisions. FineMoE is prototyped on top of HuggingFace Transformers and deployed on a six-GPU testbed. Experiments with open-source MoE models and real-world workloads show that FineMoE reduces inference latency by 47% and improves expert hit rate by 39% over state-of-the-art solutions.

## 中文摘要

大语言模型（LLM）在革新各类应用（包括内容生成、搜索与推荐以及 AI 辅助运维）方面取得了巨大成功。为降低高昂的训练成本，专家混合（MoE）架构已成为现代 LLM 流行的主干结构。然而，尽管具备这些优势，服务于基于 MoE 的 LLM 仍因专家的稀疏激活而面临严重的内存低效问题。近期研究提出将未激活的专家从 GPU 内存卸载到 CPU 内存，以提升 MoE 模型的服务效率。但它们或带来较高的推理延迟，或由于粗粒度的设计而占用较高的模型内存。

为驾驭 MoE 服务中的延迟-内存权衡，我们提出 FineMoE，一个细粒度的专家卸载系统，在实现内存高效的同时保持低推理延迟。FineMoE 的设计旨在从 MoE 模型中提取细粒度的专家选择模式，并从输入提示中提取语义线索，以高效指导专家预取、缓存与卸载决策。FineMoE 在 HuggingFace Transformers 之上实现原型，并部署在六 GPU 测试平台上。针对开源 MoE 模型与真实工作负载的实验表明，与最先进的方案相比，FineMoE 将推理延迟降低 47%，并将专家命中率提升 39%。

**英文关键词：** Artificial Intelligence, Large Language Model, Mixture-of-Experts, Model Serving, Offloading

**中文关键词：** 人工智能、大语言模型、专家混合、模型服务、卸载

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
