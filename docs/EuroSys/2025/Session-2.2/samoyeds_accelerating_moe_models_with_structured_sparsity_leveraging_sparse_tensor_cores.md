---
title: "Samoyeds: Accelerating MoE Models with Structured Sparsity Leveraging Sparse Tensor Cores"
description: "EuroSys 2025 · LLM Serving · Chenpeng Wu (Shanghai Jiao Tong University), Qiqi Gu (Shanghai Jiao Tong Univers"
tags:
  - "EuroSys2025"
  - "LLM Serving"
---

# Samoyeds: Accelerating MoE Models with Structured Sparsity Leveraging Sparse Tensor Cores

**中文标题：** 利用稀疏张量核心和结构化稀疏性加速 MoE 模型

**所属 Session：** [Session 2.2: LLM Serving](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Serving。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Serving</p>
</div>

**作者**：Chenpeng Wu (Shanghai Jiao Tong University), Qiqi Gu (Shanghai Jiao Tong University), Heng Shi (Shanghai Enflame Technology Co.Ltd; Shanghai Jiao Tong University), Jianguo Yao (Shanghai Jiao Tong University), Haibing Guan (Shanghai Jiao Tong University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717455)

## 英文摘要

The escalating size of Mixture-of-Experts (MoE) based Large Language Models (LLMs) presents significant computational and memory challenges, necessitating innovative solutions to enhance efficiency without compromising model accuracy. Structured sparsity emerges as a compelling strategy to address these challenges by leveraging the emerging sparse computing hardware. Prior works mainly focus on the sparsity in model parameters, neglecting the inherent sparse patterns in activations. This oversight can lead to additional computational costs associated with activations, potentially resulting in suboptimal performance.

This paper presents Samoyeds, an innovative acceleration system for MoE LLMs utilizing Sparse Tensor Cores (SpTCs). Samoyeds is the first to apply sparsity simultaneously to both activations and model parameters. It introduces a bespoke sparse data format tailored for MoE computation and develops a specialized sparse-sparse matrix multiplication kernel. Furthermore, Samoyeds incorporates systematic optimizations specifically designed for the execution of dual-side structured sparse MoE LLMs on SpTCs, further enhancing system performance. Evaluations show that Samoyeds outperforms SOTA works by up to 1.99× at the kernel level and 1.58× at the model level. Moreover, it enhances memory efficiency, increasing maximum supported batch sizes by 4.41× on average. Additionally, Samoyeds surpasses existing SOTA structured sparse solutions in both model accuracy and hardware portability.

## 中文摘要

基于混合专家（MoE）的大语言模型（LLM）规模不断增大，带来了显著的计算与内存挑战，因此需要创新方案在不损害模型精度的前提下提升效率。结构化稀疏通过利用新兴的稀疏计算硬件，成为应对这些挑战的一种颇具吸引力的策略。此前的工作主要关注模型参数中的稀疏性，忽略了激活值中固有的稀疏模式。这一疏忽可能导致与激活值相关的额外计算开销，进而造成性能次优。

本文提出 Samoyeds，一种利用稀疏张量核心（SpTC）的面向 MoE LLM 的创新加速系统。Samoyeds 首次将稀疏性同时应用于激活值和模型参数。它引入一种为 MoE 计算量身定制的稀疏数据格式，并开发了专门的稀疏-稀疏矩阵乘法内核。此外，Samoyeds 还集成了专门为在 SpTC 上执行双侧结构化稀疏 MoE LLM 而设计的系统性优化，进一步提升系统性能。评估表明，Samoyeds 在内核级最高比 SOTA 工作快 1.99 倍，在模型级快 1.58 倍。此外，它提升了内存效率，将最大支持的批大小平均提升 4.41 倍。同时，Samoyeds 在模型精度和硬件可移植性上均优于现有 SOTA 结构化稀疏方案。

**英文关键词：** Structured Sparsity, Mixture-of-Experts, Large Language Model, Sparse Tensor Core, System Performance

**中文关键词：** 结构化稀疏、混合专家、大语言模型、稀疏张量核心、系统性能

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
