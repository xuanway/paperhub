---
title: "CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion"
description: "EuroSys 2025 · LLM Serving · Jiayi Yao (Chinese University of Hong Kong (Shenzhen)), Hanchen Li (University o"
tags:
  - "EuroSys2025"
  - "LLM Serving"
---

# CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion

**中文标题：** 通过缓存知识融合实现面向 RAG 的快速大语言模型服务

**所属 Session：** [Session 1.2: LLM Serving](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Serving。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Serving</p>
</div>

**作者**：Jiayi Yao (Chinese University of Hong Kong (Shenzhen)), Hanchen Li (University of Chicago), Yuhan Liu (University of Chicago), Siddhant Ray (University of Chicago), Yihua Cheng (University of Chicago), Qizheng Zhang (Stanford University), Kuntai Du (University of Chicago), Shan Lu (Microsoft Research and University of Chicago), Junchen Jiang (University of Chicago)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696098)

**获奖：** 最佳论文（春季投稿）（[官方获奖名单](https://2025.eurosys.org/awards.html)）

## 英文摘要

Large language models (LLMs) often incorporate multiple text chunks in their inputs to provide the necessary contexts. To speed up the prefill of the long LLM inputs, one can pre-compute the KV cache of a text and re-use the KV cache when the context is reused as the prefix of another LLM input. However, the reused text chunks are not always the input prefix, which makes precomputed KV caches not directly usable since they ignore the text’s cross-attention with the preceding texts. Thus, the benefits of reusing KV caches remain largely unrealized.

This paper tackles just one challenge: when an LLM input contains multiple text chunks, how to quickly combine their precomputed KV caches in order to achieve the same generation quality as the expensive full prefill (i.e., without reusing KV cache)? This challenge naturally arises in retrieval-augmented generation (RAG) where the input is supplemented with multiple retrieved texts as the context. We present CacheBlend, a scheme that reuses the precomputed KV caches, regardless prefix or not, and selectively recomputes the KV values of a small subset of tokens to partially update each reused KV cache. In the meantime, the small extra delay for recomputing some tokens can be pipelined with the retrieval of KV caches within the same job, allowing CacheBlend to store KV caches in slower devices with more storage capacity while retrieving them without increasing the inference delay. By comparing CacheBlend with the state-of-the-art KV cache reusing schemes on three open-source LLMs of various sizes and four popular benchmark datasets of different tasks, we show that CacheBlend reduces time-to-first-token (TTFT) by 2.2–3.3× and increases the inference throughput by 2.8-5× from full KV recompute without compromising generation quality. The code is available at https://github.com/LMCache/LMCache.

## 中文摘要

大语言模型（LLM）常在其输入中纳入多个文本块，以提供必要的上下文。为加速长 LLM 输入的预填充，可以预先计算某段文本的 KV cache，并在该上下文被复用为另一 LLM 输入的前缀时复用该 KV cache。然而，被复用的文本块并不总是输入前缀，这使得预计算的 KV cache 无法直接使用，因为它们忽略了文本与前文之间的交叉注意力。因此，复用 KV cache 的收益在很大程度上仍未实现。

本文仅解决一个挑战：当 LLM 输入包含多个文本块时，如何快速组合它们预计算的 KV cache，以达到与昂贵的完整预填充（即不复用 KV cache）相同的生成质量？这一挑战自然出现在检索增强生成（RAG）中，此时输入会用多个检索到的文本作为上下文进行补充。我们提出 CacheBlend，该方案复用预计算的 KV cache（无论是否为前缀），并有选择地重新计算一小部分 token 的 KV 值，以部分更新每个被复用的 KV cache。同时，重新计算部分 token 带来的少量额外延迟可以与同一作业内 KV cache 的检索流水化重叠，使 CacheBlend 能够将 KV cache 存储在容量更大但更慢的设备上，并在检索它们时不增加推理延迟。通过在三个不同规模的开源 LLM 和四个不同任务的流行基准数据集上比较 CacheBlend 与最先进的 KV cache 复用方案，我们表明，在不损害生成质量的前提下，CacheBlend 相比完全重新计算 KV 将首 token 时间（TTFT）降低 2.2–3.3 倍，并将推理吞吐提升 2.8–5 倍。代码见 https://github.com/LMCache/LMCache。

**英文关键词：** Large Language Models, KV Cache, Retrieval-Augmented-Generation

**中文关键词：** 大语言模型、KV cache、检索增强生成

## 代码与研究制品

- 代码：[https://github.com/LMCache/LMCache](https://github.com/LMCache/LMCache)

以上链接来自论文现有摘要中的公开资料。

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
