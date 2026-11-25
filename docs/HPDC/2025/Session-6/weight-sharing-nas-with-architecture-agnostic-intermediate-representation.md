---
title: "Weight-Sharing NAS with Architecture-Agnostic Intermediate Representation"
description: "HPDC 2025 · Session 6 — Tuning and Performance"
tags:
  - "HPDC2025"
  - "Session 6"
  - "Tuning and Performance"
---

# Weight-Sharing NAS with Architecture-Agnostic Intermediate Representation

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 6 — Tuning and Performance（2025年7月23日 10:30–12:15 · Session Chair：Jay Lofstead）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 6</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731587) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/yu.pdf)

**作者**：Sixing Yu, Arya Mazaheri, Ali Jannesari

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 6 — Tuning and Performance（2025年7月23日 10:30–12:15 · Session Chair：Jay Lofstead）

---

## 代码与研究制品

[OSF 代码仓库](https://github.com/yusx-swapp/OSF)

## 英文摘要

Weight-sharing supernet has been widely adopted in Neural Architecture Search (NAS) as a promising strategy to obtain smaller and more efficient high-performance models. However, constructing supernets requires domain expertise to design architecture-specific rules (e.g., rules for CNNs and Transformers) for generating subnets, and training a supernet demands joint optimization over a vast sample space of subnets, which is computationally expensive. This paper presents OSF (Optimized Supernet Formation), an automated and architecture-agnostic approach that transforms predefined/pretrained models into weight-sharing supernets. Specifically, we propose representing neural architectures using a high-level computational graph intermediate representation (IR) that enables both the conversion of different types of models into supernets and the extraction of executable subnets via graph traversal. To improve supernet training efficiency, we introduce a sampling strategy that prioritizes the most promising subnet candidates during training, and propose a fork-join parallel training approach with gradient accumulation that resolves write-after-write dependencies, enabling concurrent training of multiple subnet architectures with shared weights. Our empirical evaluations demonstrate that OSF successfully builds supernets from various architectures (CNNs, Transformers, SSMs, and MLPs) while achieving superior performance across language and vision benchmarks. Notably, for Vision Transformers (ViT), OSF reduces FLOPs by 49% while maintaining the accuracy, resulting in a 155% increase in throughput and 35% latency reduction. Code Open-sourced at: https://github.com/yusx-swapp/OSF

## 中文摘要

权重共享超网已被广泛用于神经架构搜索（NAS），作为获得更小、更高效高性能模型的一种有前景的策略。然而，构建超网需要领域专业知识来设计架构特定规则（如针对 CNN 与 Transformer 的规则）以生成子网，且训练超网需要对庞大的子网样本空间进行联合优化，计算代价高昂。本文提出 OSF（优化超网构建），一种自动化且架构无关的方法，可将预定义/预训练模型转换为权重共享超网。具体而言，我们提出用高层计算图中间表示（IR）来表示神经架构，既能将不同类型的模型转换为超网，也能通过图遍历提取可执行子网。为提升超网训练效率，我们引入一种在训练期间优先选择最有希望子网候选的采样策略，并提出一种带梯度累积的 fork-join 并行训练方法，解决写后写依赖，从而能够以共享权重并发训练多个子网架构。我们的实证评估表明，OSF 成功地从多种架构（CNN、Transformer、SSM 和 MLP）构建超网，并在语言与视觉基准上取得优异性能。值得注意的是，对于视觉 Transformer（ViT），OSF 在保持精度的同时将 FLOPs 减少 49%，带来 155% 的吞吐提升和 35% 的延迟降低。代码已开源于：https://github.com/yusx-swapp/OSF

---

[← 返回 Session 6 — Tuning and Performance](index.md)
