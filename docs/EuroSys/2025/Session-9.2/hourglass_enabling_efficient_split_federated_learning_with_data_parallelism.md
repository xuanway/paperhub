---
title: "Hourglass: Enabling Efficient Split Federated Learning with Data Parallelism"
description: "EuroSys 2025 · LLM Training · Qiang He (Huazhong University of Science and Technology), Kaibin Wang (Swinburne"
tags:
  - "EuroSys2025"
  - "LLM Training"
---

# Hourglass: Enabling Efficient Split Federated Learning with Data Parallelism

**中文标题：** 通过数据并行实现高效分割联邦学习

**所属 Session：** [Session 9.2: LLM Training](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Training。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Training</p>
</div>

**作者**：Qiang He (Huazhong University of Science and Technology), Kaibin Wang (Swinburne University of Technology), Zeqian Dong (Swinburne University of Technology), Liang Yuan (University of Adelaide), Feifei Chen (Deakin University), Hai Jin (Huazhong University of Science and Technology), Yun Yang (Swinburne University of Technology)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717467)

## 英文摘要

Federated learning (FL) has emerged as a promising solution for training machine learning (ML) models with privacy preservation. One of the key challenges is the computational burden on clients caused by training large-sized models. To tackle this challenge, researchers are trying to incorporate split learning into federated learning so that an ML model can be partitioned into two parts, one for training on clients and the other on a cloud server or an edge server. In current split FL systems, each client’s server-side model partition is trained with an individual GPU on the fed server before model aggregation. This demands massive GPU resources and does not scale in real-world scenarios. This paper presents Hourglass, a new split FL system that trains clients’ server-side model partitions on multiple GPUs with data parallelism. Unlike existing systems that maintain one model partition for each client and pass clients’ intermediate features through corresponding model partitions, Hourglass maintains model partitions shared by clients and passes their intermediate features through GPUs in groups based on their differences. In this way, Hourglass prevents the overhead incurred by swapping model partitions in and out of GPUs and improves knowledge sharing between clients. Extensive experiments are conducted on four widely-used public datasets to evaluate the performance of Hourglass. The results demonstrate that, compared to state-of-the-art systems, Hourglass accelerates model convergence by up to 35.2x, and improves model accuracy by up to 9.28%.

## 中文摘要

联邦学习（FL）已成为以保护隐私的方式训练机器学习（ML）模型的一种有前景的解决方案。其关键挑战之一是训练大尺寸模型给客户端带来的计算负担。为应对这一挑战，研究者尝试将拆分学习融入联邦学习，使 ML 模型可被划分为两部分，一部分在客户端训练，另一部分在云服务器或边缘服务器上训练。在当前的拆分联邦学习系统中，每个客户端的服务端模型分区在模型聚合之前都在联邦服务器上由单独的 GPU 训练。这需要大量 GPU 资源，在真实场景中无法扩展。本文提出 Hourglass，一种新的拆分联邦学习系统，它以数据并行方式在多块 GPU 上训练客户端的服务端模型分区。与现有为每个客户端维护一个模型分区并让客户端的中间特征通过对应模型分区的系统不同，Hourglass 维护由客户端共享的模型分区，并按差异将它们的中间特征分组送入 GPU。如此，Hourglass 避免了模型分区在 GPU 中换入换出所带来的开销，并改善了客户端之间的知识共享。我们在四个广泛使用的公开数据集上开展了大量实验以评估 Hourglass 的性能。结果表明，相比最先进系统，Hourglass 最多将模型收敛速度加快 35.2 倍，并将模型准确率最多提升 9.28%。

**英文关键词：** Split federated learning, data parallelism, machine learning system

**中文关键词：** 拆分联邦学习、数据并行、机器学习系统

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
