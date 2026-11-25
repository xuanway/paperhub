---
title: "MegaScale-Data: Scaling DataLoader for Multisource Large Foundation Model Training"
description: "EuroSys 2026 · LLM Training at Scale · Juntao Zhao (The University of Hong Kong), Qi Lu (ByteDance Inc.), Wei Jia (Byte"
tags:
  - "EuroSys2026"
  - "LLM Training at Scale"
---

# MegaScale-Data: Scaling DataLoader for Multisource Large Foundation Model Training

**中文标题：** MegaScale-Data：为多源大基础模型训练扩展 DataLoader

**所属 Session：** [Session 3.1: LLM Training at Scale](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Training at Scale。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Training at Scale</p>
</div>

**作者**：Juntao Zhao (The University of Hong Kong), Qi Lu (ByteDance Inc.), Wei Jia (ByteDance Inc.), Borui Wan (The University of Hong Kong), Lei Zuo (ByteDance Inc.), Junda Feng (ByteDance Inc.), Jianyu Jiang (ByteDance Inc.), Yangrui Chen (ByteDance Inc.), Shuaishuai Cao (ByteDance Inc.), Jialing He (ByteDance Inc.), Kaihua Jiang (ByteDance Inc.), Yuanzhe Hu (ByteDance Inc.), Shibiao Nong (ByteDance Inc.), Yanghua Peng (ByteDance), Haibin Lin (ByteDance Inc.), Chuan Wu (The University of Hong Kong)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803568)

## 英文摘要

Modern frameworks for training large foundation models (LFMs) employ dataloaders in a data-parallel manner, with each loader processing a disjoint subset of training data. When preparing data for LFM training that originates from multiple, distinct sources, two fundamental challenges arise. First, due to the quadratic computational complexity of the attention operator, the non-uniform sample distribution over data-parallel ranks leads to significant workload imbalance among dataloaders, degrading the training efficiency. Second, supporting diverse data sources requires per-dataset file access states that are redundantly replicated across parallel loaders, consuming excessive memory. This also hinders dynamic data mixing (e.g., curriculum learning) and causes redundant access/memory overhead in hybrid parallelism.

We present MegaScale-Data, an industrial-grade distributed data loading architecture for multisource LFMs training, with three key innovations: (1) Disaggregated data preprocessing via role-specific actors (Source Loaders/Data Constructors) to eliminate source and parallelism redundant data access and ensure multisource scalability. (2) Centralized and declarative data plane for load-time multisource orchestration, such as long-short context, multimodality, and curriculum learning. (3) Multi-level auto-partitioning and scaling mechanism for source loaders under heterogeneous preprocessing costs. We also contribute our designs and operational experience in deployment and fault tolerance. MegaScale-Data achieves up to: (1) 4.5× end-to-end training throughput improvement, and (2) 13.5× reduction in CPU memory usage.

## 中文摘要

现代大基础模型（LFM）训练框架以数据并行的方式使用数据加载器（dataloader），每个加载器处理互不相交的训练数据子集。当为来自多个不同数据源的 LFM 训练准备数据时，会出现两个根本性挑战。首先，由于注意力算子的二次计算复杂度，数据并行各 rank 上样本分布的不均匀会导致数据加载器之间出现显著的工作负载不均衡，从而降低训练效率。其次，支持多样化的数据源需要为每个数据集维护文件访问状态，而这些状态会在并行的加载器之间冗余复制，消耗过多内存。这也阻碍了动态数据混合（如课程学习），并在混合并行中造成冗余的访问与内存开销。

我们提出 MegaScale-Data，一种面向多源 LFM 训练的工业级分布式数据加载架构，包含三项关键创新：（1）通过角色特定的 actor（源加载器/数据构造器）实现解耦的数据预处理，以消除源于数据源和并行方式的冗余数据访问，并确保多源可扩展性；（2）集中式、声明式的数据面，用于加载时的多源编排，如长短期上下文、多模态和课程学习；（3）针对异构预处理开销下源加载器的多级自动分区与伸缩机制。我们还贡献了在部署与容错方面的设计与运维经验。MegaScale-Data 实现了：（1）端到端训练吞吐量最高提升 4.5 倍，（2）CPU 内存占用最多降低 13.5 倍。

**英文关键词：** Distributed systems, Multisource Training, Data Loading

**中文关键词：** 分布式系统、多源训练、数据加载

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
