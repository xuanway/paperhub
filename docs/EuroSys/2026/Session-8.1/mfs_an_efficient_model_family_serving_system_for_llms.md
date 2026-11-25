---
title: "MFS: An Efficient Model Family Serving System for LLMs"
description: "EuroSys 2026 · LLM Serving & Agents · Yunxuan Zhang (Hong Kong University of Science and Technology), Hao Wang (Hong K"
tags:
  - "EuroSys2026"
  - "LLM Serving & Agents"
---

# MFS: An Efficient Model Family Serving System for LLMs

**中文标题：** MFS：面向 LLM 的高效模型族服务系统

**所属 Session：** [Session 8.1: LLM Serving & Agents](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Serving & Agents。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Serving & Agents</p>
</div>

**作者**：Yunxuan Zhang (Hong Kong University of Science and Technology), Hao Wang (Hong Kong University of Science and Technology), Han Tian (University of Science and Technology of China), Liu Yang (Hong Kong University of Science and Technology), Xudong Liao (Hong Kong University of Science and Technology), Wenxue Li (Hong Kong University of Science and Technology), Ping Yin (Inspur), Bowen Liu (Hong Kong University of Science and Technology), Kai Chen (Hong Kong University of Science and Technology)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769355)

## 英文摘要

LLM serving providers typically offer a suite of structurally similar models, known as model families, such as the opensource Llama2 series featuring 7B, 13B, and 70B models. While numerous optimizations for LLM serving have been proposed, the potential for leveraging synergies between models within the same family has not been thoroughly explored. This paper introduces MFS, an innovative multi-tiered LLM model family serving system to exploit the structural similarities and parameter redundancies across different scales of models within a family. By utilizing a novel fine-tuning technique called Knowledge Precipitation, MFS restructures the largest model in a family to encapsulate smaller models within its architecture, enabling a unified multi-tiered serving pipeline. Based on the multi-tiered model, MFS realizes a highly parallelized tiered-level batching approach, significantly enhancing system efficiency. It also enables the sharing of intermediate features and KV-cache between models and facilitates multi-level sampling techniques during the inference phase. Experimental results demonstrate that MFS achieves substantial improvements over existing methods, including a 56.1% reduction in end-to-end token generation latency and a 47.8% decrease in GPU memory footprint without compromising the quality of generated content.

## 中文摘要

LLM 服务提供商通常会提供一组结构相似的模型，称为模型族，例如包含 7B、13B 和 70B 模型的开源 Llama2 系列。尽管已有大量针对 LLM 服务的优化工作，但利用同一模型族内各模型之间协同效应的潜力尚未得到充分探索。本文提出 MFS，一个创新的多层级 LLM 模型族服务系统，旨在利用同一模型族中不同规模模型之间的结构相似性与参数冗余。MFS 采用一种名为知识沉淀（Knowledge Precipitation）的新型微调技术，将模型族中最大的模型重构为在其架构内容纳较小模型，从而实现统一的多层级服务流水线。基于该多层级模型，MFS 实现了高度并行的层级批处理方式，显著提升系统效率。它还使模型之间能够共享中间特征与 KV 缓存，并在推理阶段支持多级采样技术。实验结果表明，MFS 相较现有方法取得显著改进，包括端到端 token 生成延迟降低 56.1%、GPU 显存占用减少 47.8%，且不损害生成内容的质量。

**英文关键词：** Large Language Models, Model Serving, Distributed Systems, Inference Optimization

**中文关键词：** 大语言模型、模型服务、分布式系统、推理优化

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
