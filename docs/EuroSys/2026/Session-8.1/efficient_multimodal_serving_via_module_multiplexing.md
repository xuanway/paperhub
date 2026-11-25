---
title: "Efficient Multimodal Serving via Module Multiplexing"
description: "EuroSys 2026 · LLM Serving & Agents · Zicong Hong (Hong Kong University of Science and Technology), Yuyan Chen (Sun Ya"
tags:
  - "EuroSys2026"
  - "LLM Serving & Agents"
---

# Efficient Multimodal Serving via Module Multiplexing

**中文标题：** 基于模块多路复用的高效多模态服务

**所属 Session：** [Session 8.1: LLM Serving & Agents](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Serving & Agents。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Serving & Agents</p>
</div>

**作者**：Zicong Hong (Hong Kong University of Science and Technology), Yuyan Chen (Sun Yat-sen University), Haoyue Zhang (Hong Kong University of Science and Technology), Peng Li (Xi'an Jiaotong University), Wuhui Chen (Sun Yat-sen University), Song Guo (Hong Kong University of Science and Technology), Xiaowei Shen (MetaX)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769389)

## 英文摘要

Multimodal learning enables models to process and reason over diverse information sources, unlocking human-like perceptual and cognitive capabilities. As such models gain adoption, efficiently serving them on GPUs has become increasingly important. However, the modular architecture of multimodal models poses significant challenges to existing unimodal serving systems, which treat models as monolithic and overlook inter-module heterogeneity. This results in severe GPU underutilization. To address this, we propose EVEE, a multimodal serving system based on a new scheduling paradigm we call module multiplexing. Unlike prior approaches that execute all modules sequentially with uniform batch sizes, EVEE schedules modality-specific modules concurrently on the same GPU with independently tuned batching and resource allocation. This design enables fine-grained GPU sharing, boosting intra-GPU parallelism and improving request-level throughput. We implement a prototype of EVEE and evaluate it on several representative multimodal models (e.g., CLIP, BLIP, LLaVA, InternVL). Our results show that EVEE significantly outperforms state-of-the-art serving systems in both throughput and GPU utilization.

## 中文摘要

多模态学习使模型能够处理并推理多种信息源，从而释放出类人的感知与认知能力。随着此类模型得到广泛应用，在 GPU 上高效地服务它们变得日益重要。然而，多模态模型的模块化架构给现有的单模态服务系统带来了重大挑战：这些系统将模型视为单体，忽视了模块间的异构性，导致 GPU 利用率严重不足。为解决这一问题，我们提出 EVEE，一个基于我们称之为模块多路复用（module multiplexing）的新调度范式的多模态服务系统。与以往以统一批大小顺序执行所有模块的方法不同，EVEE 在同一 GPU 上并发调度各模态专属模块，并独立调优其批处理与资源分配。该设计实现了细粒度的 GPU 共享，提升了 GPU 内并行度，并改善了请求级吞吐。我们实现了 EVEE 原型，并在若干代表性多模态模型（如 CLIP、BLIP、LLaVA、InternVL）上进行了评估。结果表明，EVEE 在吞吐量与 GPU 利用率上均显著优于最先进的服务系统。

**英文关键词：** Multimodal model, GPU multiplexing, efficient serving system

**中文关键词：** 多模态模型、GPU 多路复用、高效服务系统

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
