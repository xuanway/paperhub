---
title: "DataStates-LLM: Lazy Asynchronous Checkpointing for Large Language Models"
description: "HPDC 2024 · Session 2 — Resilience"
tags:
  - "HPDC2024"
  - "Session 2"
  - "Resilience"
---

# DataStates-LLM: Lazy Asynchronous Checkpointing for Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 2 — Resilience（2024年6月5日 14:00–15:15 · Session Chair：Changhee Jung）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 2</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658685)

**作者**：Avinash Maurya, Robert Underwood, M. Mustafa Rafique, Franck Cappello, Bogdan Nicolae

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 2 — Resilience（2024年6月5日 14:00–15:15 · Session Chair：Changhee Jung）

---

## 英文摘要

LLMs have seen rapid adoption in all domains. They need to be trained on high-end high-performance computing (HPC) infrastructures and ingest massive amounts of input data. Unsurprisingly, at such a large scale, unexpected events (e.g., failures of components, instability of the software, undesirable learning patterns, etc.), are frequent and typically impact the training in a negative fashion. Thus, LLMs need to be checkpointed frequently so that they can be rolled back to a stable state and subsequently fine-tuned. However, given the large sizes of LLMs, a straightforward checkpointing solution that directly writes the model parameters and optimizer state to persistent storage (e.g., a parallel file system), incurs significant I/O overheads. To address this challenge, in this paper we study how to reduce the I/O overheads for enabling fast and scalable checkpointing for LLMs that can be applied at high frequency (up to the granularity of individual iterations) without significant impact on the training process. Specifically, we introduce a lazy asynchronous multi-level approach that takes advantage of the fact that the tensors making up the model and optimizer state shards remain immutable for extended periods of time, which makes it possible to copy their content in the background with minimal interference during the training process. We evaluate our approach at scales of up to 180 GPUs using different model sizes, parallelism settings, and checkpointing frequencies. The results show up to 48× faster checkpointing and 2.2× faster end-to-end training runtime compared with the state-of-art checkpointing approaches.

## 中文摘要

LLM 已在各领域迅速普及。它们需要在高性能计算（HPC）基础设施上训练，并摄入海量输入数据。不足为奇的是，在如此大规模下，意外事件（如组件故障、软件不稳定、不良学习模式等）频繁发生，通常对训练造成负面影响。因此，LLM 需要频繁检查点，以便回滚到稳定状态并随后微调。然而，鉴于 LLM 规模庞大，直接将模型参数与优化器状态写入持久存储（如并行文件系统）的朴素检查点方案会带来显著的 I/O 开销。为应对这一挑战，本文研究如何降低 I/O 开销，以实现可高频应用（精细到单次迭代粒度）、且对训练过程影响不大的快速可扩展 LLM 检查点。具体而言，我们引入一种惰性异步多级方法，利用构成模型与优化器状态分片的张量在较长时间内保持不变这一事实，从而能够在训练过程中以最小干扰在后台复制其内容。我们在多达 180 块 GPU 的规模上，使用不同模型大小、并行设置与检查点频率评估该方法。结果表明，与最先进的检查点方法相比，检查点速度最高提升 48 倍，端到端训练运行时间最高提升 2.2 倍。

## 英文关键词

LLMs and transformers; scalable checkpointing; asynchronous multilevel checkpointing

## 中文关键词

LLM 与 Transformer；可扩展检查点；异步多级检查点

---

[← 返回 Session 2 — Resilience](index.md)
