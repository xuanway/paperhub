---
title: "SAS: Sparse Attention Synthesizer for Efficient Language Model Inference"
description: "EuroSys 2026 · AI · Yuan Zhou (Amazon), Shaojie Xiang (Amazon), Lingfan Yu (Amazon), Zhenyu Song (Am"
tags:
  - "EuroSys2026"
  - "AI"
---

# SAS: Sparse Attention Synthesizer for Efficient Language Model Inference

**中文标题：** SAS：面向高效语言模型推理的稀疏注意力合成器

**所属 Session：** [Session 5.1: AI](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：AI。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · AI</p>
</div>

**作者**：Yuan Zhou (Amazon), Shaojie Xiang (Amazon), Lingfan Yu (Amazon), Zhenyu Song (Amazon), Charith Mendis (Amazon), Yida Wang (Amazon)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769364)

## 英文摘要

Modern large language models rely on attention mechanisms that attend to all tokens in a sequence, resulting in quadratic computational complexity that limits scalability. While sparse attention reduces compute and memory requirements by attending to only important tokens, implementing these techniques presents significant challenges due to the complexity of combining static and dynamic sparse patterns and optimizing key-value (KV) cache management.

To address these challenges, we present SAS, a sparse attention synthesizer that automatically generates performant sparse attention kernels for large language model inference. SAS introduces a set of primitives that effectively encapsulate both static and dynamic sparse attention mechanisms, enabling users to compose complex attention patterns through logic operators and declarative functions. The system employs a geometric-based pattern analyzer to optimize for KV caching by determining minimal cache sizes and automatically generating cache management functions. Supporting both Nvidia GPU and AWS Trainium backends, SAS demonstrates significant performance improvements: 1.10-1.22× speedup for context encoding and 2.68-2.80× speedup for token generation over FlexAttention, a state-of-the-art flexible attention kernel synthesis tool, on GPUs, and 1.41-6.49× speedup for context encoding and 1.39-10.87× speedup for token generation over optimized dense attention on Trainium.

## 中文摘要

现代大语言模型依赖对序列中所有 token 进行注意力计算的机制，导致计算复杂度呈二次增长，限制了可扩展性。稀疏注意力通过只关注重要 token 来降低计算与内存需求，但由于静态与动态稀疏模式的组合十分复杂，且键值（KV）缓存管理需要优化，实现这些技术面临重大挑战。

为应对这些挑战，我们提出 SAS，一个稀疏注意力合成器，可为大语言模型推理自动生成高性能稀疏注意力内核。SAS 引入一组原语，有效封装了静态与动态稀疏注意力机制，使用户能够通过逻辑运算符和声明式函数组合出复杂的注意力模式。该系统采用基于几何的模式分析器来确定最小缓存大小并自动生成缓存管理函数，从而针对 KV 缓存进行优化。SAS 同时支持 Nvidia GPU 与 AWS Trainium 后端，并展现出显著的性能提升：在 GPU 上，相比最先进的灵活注意力内核合成工具 FlexAttention，上下文编码加速 1.10–1.22 倍，token 生成加速 2.68–2.80 倍；在 Trainium 上，相比优化后的稠密注意力，上下文编码加速 1.41–6.49 倍，token 生成加速 1.39–10.87 倍。

**英文关键词：** Sparse Attention, Kernel Synthesis, Domain Specific Language, LLM Inference

**中文关键词：** 稀疏注意力、内核合成、领域特定语言、LLM 推理

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
