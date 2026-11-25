---
title: "EvoStore: Towards Scalable Storage of Evolving Learning Models"
description: "HPDC 2024 · Session 8 — Communication & Storage"
tags:
  - "HPDC2024"
  - "Session 8"
  - "Communication & Storage"
---

# EvoStore: Towards Scalable Storage of Evolving Learning Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 8 — Communication & Storage（2024年6月7日 14:00–15:40 · Session Chair：Bogdan Nicolae）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 8</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658679)

**作者**：Robert Underwood, Meghana Madhyastha, Randal Burns, Bogdan Nicolae

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 8 — Communication & Storage（2024年6月7日 14:00–15:40 · Session Chair：Bogdan Nicolae）

---

## 英文摘要

Deep Learning (DL) has seen rapid adoption in all domains. Since training DL models is expensive, both in terms of time and resources, application workflows that make use of DL increasingly need to operate with a large number of derived learning models, which are obtained through transfer learning and fine-tuning. At scale, thousands of such derived DL models are accessed concurrently by a large number of processes. In this context, an important question is how to design and develop specialized DL model repositories that remain scalable under concurrent access, while addressing key challenges: how to query the DL model architectures for specific patterns? How to load/store a subset of layers/tensors from a DL model? How to efficiently share unmodified layers/tensors between DL models derived from each other through transfer learning? How to maintain provenance and answer ancestry queries? State of art leaves a gap regarding these challenges. To fill this gap, we introduce EvoStore, a distributed DL model repository with scalable data and metadata support to store and access derived DL models efficiently. Large-scale experiments on hundreds of GPUs show significant benefits over state-of-art with respect to I/O and metadata performance, as well as storage space utilization.

## 中文摘要

深度学习（DL）已在各领域迅速普及。由于训练 DL 模型在时间与资源上都很昂贵，利用 DL 的应用工作流日益需要处理大量派生学习模型，这些模型通过迁移学习与微调获得。在大规模下，数千个此类派生 DL 模型会被大量进程并发访问。在此背景下，一个重要问题是如何设计与开发专门的 DL 模型仓库，使其在并发访问下保持可扩展，同时应对关键挑战：如何按特定模式查询 DL 模型架构？如何加载/存储 DL 模型中的部分层/张量？如何在通过迁移学习相互派生的 DL 模型之间高效共享未修改的层/张量？如何维护溯源并回答祖先查询？最先进工作在应对这些挑战方面仍存在空白。为填补这一空白，我们提出 EvoStore，一个具有可扩展数据与元数据支持的分布式 DL 模型仓库，可高效存储与访问派生 DL 模型。在数百块 GPU 上的大规模实验表明，在 I/O 与元数据性能以及存储空间利用率方面，EvoStore 相比最先进方案具有显著优势。

## 英文关键词

AI, Model Repository, Network Architecture Search, Regulartized Evolution, Distributed, AI for HPC

## 中文关键词

AI，模型仓库，网络架构搜索，正则化演化，分布式，面向 HPC 的 AI

---

[← 返回 Session 8 — Communication & Storage](index.md)
