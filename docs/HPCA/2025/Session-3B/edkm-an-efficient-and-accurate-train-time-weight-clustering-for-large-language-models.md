---
title: "eDKM: An Efficient and Accurate Train-Time Weight Clustering for Large Language Models"
description: "HPCA 2025 · Best of CAL"
tags:
  - "HPCA2025"
  - "Best of CAL"
---

# eDKM: An Efficient and Accurate Train-Time Weight Clustering for Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Best of CAL。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Best of CAL</p>
</div>

**论文链接**：
**作者**：Minsik Cho (Apple), Keivan A. Vahid (Apple), Qichen Fu (Apple), Saurabh Adya (Apple), Carlo C. Del Mundo (Apple), Mohammad Rastegari (Apple), Devang Naik (Apple), Peter Zatloukal (Apple)
**会议**：HPCA 2025

---

## 中文标题

eDKM：面向大语言模型的高效准确训练时权值聚类

## 英文摘要

Since Large Language Models or LLMs have demonstrated high-quality performance on many complex language tasks, there is a great interest in bringing these LLMs to mobile devices for faster responses and better privacy protection. However, the size of LLMs (i.e., billions of parameters) requires highly effective compression to fit into storage-limited devices. Among many compression techniques, weight-clustering, a form of non-linear quantization, is one of the leading candidates for LLM compression, and supported by modern smartphones. Yet, its training overhead is prohibitively significant for LLM fine-tuning. Especially, Differentiable KMeans Clustering, or DKM, has shown the state-of-the-art trade-off between compression ratio and accuracy regression, but its large memory complexity makes it nearly impossible to apply to train-time LLM compression. In this letter, we propose a memory-efficient DKM implementation, eDKM powered by novel techniques to reduce the memory footprint of DKM by orders of magnitudes. For a given tensor to be saved on CPU for the backward pass of DKM, we compressed the tensor by applying uniquification and sharding after checking if there is no duplicated tensor previously copied to CPU. Our experimental results demonstrate that eDKM can fine-tune and compress a pretrained LLaMA 7B model from 12.6 GB to 2.5 GB (3 b/weight) with the Alpaca dataset by reducing the train-time memory footprint of a decoder layer by 130×, while delivering good accuracy on broader LLM benchmarks (i.e., 77.7% for PIQA, 66.1% for Winograde, and so on).

## 中文摘要

由于大语言模型（LLM）在许多复杂语言任务上展现出高质量性能，人们很有兴趣把这类 LLM 引入移动设备，以获得更快的响应与更好的隐私保护。然而，LLM 的规模（即数十亿参数）需要极为有效的压缩才能放入存储受限的设备。在众多压缩技术中，权值聚类作为一种非线性量化形式，是 LLM 压缩的主要候选方案之一，并受到现代智能手机的支持。但其训练开销对 LLM 微调而言高得难以承受。特别是，可微 KMeans 聚类（DKM）在压缩比与精度回退之间展现出最先进的折中，但其巨大的内存复杂度使其几乎无法用于训练时的 LLM 压缩。本文提出一种内存高效的 DKM 实现 eDKM，借助新技术把 DKM 的内存占用降低数个数量级。对于需保存在 CPU 上以供 DKM 反向传播使用的给定张量，我们在检查此前没有复制到 CPU 的重复张量之后，通过唯一化与分片来压缩该张量。实验结果表明，eDKM 使用 Alpaca 数据集可把预训练的 LLaMA 7B 模型微调并压缩，从 12.6 GB 压到 2.5 GB（每权值 3 bit），同时把解码器层的训练时内存占用降低 130 倍，并在更广泛的 LLM 基准上交付良好精度（即 PIQA 77.7%、Winograde 66.1% 等）。
