---
title: "MinatoLoader: Accelerating Machine Learning Training Through Efficient Data Preprocessing"
description: "EuroSys 2026 · Distributed Training & Collective Communication · Rahma Nouaji (McGill University, Canada), Stella Bitchebe (McGill University, Ca"
tags:
  - "EuroSys2026"
  - "Distributed Training & Collective Communication"
---

# MinatoLoader: Accelerating Machine Learning Training Through Efficient Data Preprocessing

**中文标题：** MinatoLoader：通过高效数据预处理加速机器学习训练

**所属 Session：** [Session 11.1: Distributed Training & Collective Communication](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Training & Collective Communication。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Training & Collective Communication</p>
</div>

**作者**：Rahma Nouaji (McGill University, Canada), Stella Bitchebe (McGill University, Canada), Ricardo Macedo (INESC TEC & University of Minho, Portugal), Oana Balmau (McGill University, Canada)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769376)

## 英文摘要

Machine learning (ML) frameworks, such as PyTorch and TensorFlow, rely on data loaders to preprocess data before feeding it to accelerators. When preprocessing is inefficiently pipelined, GPUs can remain idle over long periods of time, leading to substantial training delays. For example, PyTorch’s default data loaders can cause up to 76% GPU idleness. A key bottleneck is the variability in preprocessing time across samples within the same dataset. Existing data loaders are oblivious to this variability, training all samples uniformly. In this case, a single slow sample can stall the entire batch, causing head-of-line blocking.

We present MinatoLoader, a general-purpose data loader for PyTorch that accelerates training and improves GPU utilization under single-server, multi-GPU settings. It continuously prepares data in background and constructs batches by prioritizing fast-to-process samples, while slower samples are processed in parallel.

Experiments conducted over NVIDIA V100 and A100 GPUs show that MinatoLoader accelerates training by up to 7.5× (3.6× on average) over PyTorch DataLoader and Pecan, and up to 3× (2.2× on average) over DALI. It also increases average GPU utilization from 46% with PyTorch to 90%, while preserving model accuracy and enabling faster convergence.

## 中文摘要

机器学习（ML）框架（如 PyTorch 和 TensorFlow）依赖数据加载器在将数据送入加速器之前进行预处理。当预处理流水线效率低下时，GPU 可能长时间空闲，导致训练大幅延迟。例如，PyTorch 默认的数据加载器可导致高达 76% 的 GPU 空闲。一个关键瓶颈是同一数据集内各样本预处理时间的变异性。现有数据加载器对这种变异性无感知，对所有样本统一处理。在这种情况下，单个慢样本可能拖住整个批次，造成队头阻塞。

我们提出 MinatoLoader，一个面向 PyTorch 的通用数据加载器，在单机多 GPU 环境下加速训练并提高 GPU 利用率。它持续在后台准备数据，并通过优先处理快样本、同时并行处理较慢样本来构造批次。

在 NVIDIA V100 和 A100 GPU 上进行的实验表明，MinatoLoader 相比 PyTorch DataLoader 和 Pecan 最高加速训练 7.5×（平均 3.6×），相比 DALI 最高加速 3×（平均 2.2×）。它还将平均 GPU 利用率从 PyTorch 的 46% 提升至 90%，同时保持模型准确率并实现更快的收敛。

**英文关键词：** ML training, Data loader, Data preprocessing

**中文关键词：** 机器学习训练、数据加载器、数据预处理

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
