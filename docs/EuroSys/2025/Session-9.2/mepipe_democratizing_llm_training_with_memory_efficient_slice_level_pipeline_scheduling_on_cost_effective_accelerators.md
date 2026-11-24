---
title: "MEPipe: Democratizing LLM Training with Memory-Efficient Slice-Level Pipeline Scheduling on Cost-Effective Accelerators"
description: "EuroSys 2025 · LLM Training · Zhenbo Sun (Tsinghua University), Shengqi Chen (Tsinghua University), Yuanwei Wa"
tags:
  - "EuroSys2025"
  - "LLM Training"
---

# MEPipe: Democratizing LLM Training with Memory-Efficient Slice-Level Pipeline Scheduling on Cost-Effective Accelerators

**中文标题：** 利用经济型加速器上的内存高效切片级流水线调度普及大语言模型训练

**所属 Session：** [Session 9.2: LLM Training](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Training。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Training</p>
</div>

**作者**：Zhenbo Sun (Tsinghua University), Shengqi Chen (Tsinghua University), Yuanwei Wang (Tsinghua University), Jian Sha (Tsinghua University), Guanyu Feng (Zhipu AI), Wenguang Chen (Tsinghua University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717469)

## 英文摘要

The training of large language models (LLMs) typically needs costly GPUs, such as NVIDIA A100 or H100. They possess substantial high-bandwidth on-chip memory and rapid interconnects like NVLinks. The exorbitant expenses associated with LLM training pose not just an economic challenge but also a societal one, as it restricts the ability to train LLMs from scratch to a selected few organizations.

There is a significant interest in democratizing access to LLM training. This paper explores a potential solution by employing innovative parallel strategies on more affordable accelerators. Budget-friendly options like NVIDIA RTX 4090, while considerably less expensive and comparable in computational power to A100, are hindered by their limited memory capacity and reduced interconnect bandwidth, making the effective training of LLMs challenging.

Conventional parallel strategies often result in high communication costs or excessive memory usage. Our paper introduces MEPipe, a novel approach that includes a slice-level scheduling method for sequence pipeline parallelism. This method minimizes memory consumption without incurring additional communication overhead. Besides, MEPipe utilizes fine-grained weight gradient computation to reduce idle time and mitigate imbalanced computation among slices.

MEPipe has demonstrated up to 1.68× speedup (1.35× on average) on clusters equipped with 64 NVIDIA 4090 GPUs when training Llama models of varying sizes. 35% Model FLOPS Utilization (MFU) is achieved in training Llama 13B model, being 2.5× more cost-effective than A100 clusters.

## 中文摘要

大语言模型（LLM）的训练通常需要昂贵的 GPU，如 NVIDIA A100 或 H100。它们拥有大量高带宽片上内存和快速的互连（如 NVLink）。与 LLM 训练相关的过高费用不仅是经济挑战，也是社会挑战，因为它使得从零开始训练 LLM 的能力仅限于少数组织。

人们对于让 LLM 训练更加普及有着浓厚兴趣。本文通过在更实惠的加速器上采用创新的并行策略来探索一种可能的解决方案。像 NVIDIA RTX 4090 这样价格友好的选择虽然便宜得多且算力与 A100 相当，但受限于其内存容量和互连带宽较低，使得有效训练 LLM 颇具挑战。

传统并行策略往往导致高昂的通信成本或过多的内存占用。本文提出 MEPipe，一种新颖的方法，包含用于序列流水线并行的切片级调度方法。该方法在不引入额外通信开销的情况下最小化内存消耗。此外，MEPipe 利用细粒度的权重梯度计算来减少空闲时间并缓解切片间的计算不均衡。

在配备 64 块 NVIDIA 4090 GPU 的集群上训练不同规模的 Llama 模型时，MEPipe 展现出最高 1.68 倍加速（平均 1.35 倍）。在训练 Llama 13B 模型时达到 35% 的模型浮点运算利用率（MFU），成本效益比 A100 集群高 2.5 倍。

**英文关键词：** distributed deep learning; large language model

**中文关键词：** 分布式深度学习、大语言模型

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
