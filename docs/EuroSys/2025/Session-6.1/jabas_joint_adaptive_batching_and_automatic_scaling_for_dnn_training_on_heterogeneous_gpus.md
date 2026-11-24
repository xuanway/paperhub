---
title: "JABAS: Joint Adaptive Batching and Automatic Scaling for DNN Training on Heterogeneous GPUs"
description: "EuroSys 2025 · ML systems · Gyeongchan Yun (UNIST), Junesoo Kang (UNIST), Hyunjoon Jeong (UNIST), Sanghyeon "
tags:
  - "EuroSys2025"
  - "ML systems"
---

# JABAS: Joint Adaptive Batching and Automatic Scaling for DNN Training on Heterogeneous GPUs

**中文标题：** 联合自适应批处理与自动扩缩容，支持异构 GPU 上的深度神经网络训练

**所属 Session：** [Session 6.1: ML systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：ML systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · ML systems</p>
</div>

**作者**：Gyeongchan Yun (UNIST), Junesoo Kang (UNIST), Hyunjoon Jeong (UNIST), Sanghyeon Eom (UNIST), Minsung Jang (Samsung SDS), Young-ri Choi (UNIST)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696078)

## 英文摘要

Adaptive batching is a promising technique to reduce the communication and synchronization overhead for training Deep Neural Network (DNN) models. In this paper, we study how to speed up the training of a DNN model using adaptive batching, without degrading the convergence performance in a heterogeneous GPU cluster. We propose a novel DNN training system, called JABAS (Joint Adaptive Batching and Automatic Scaling). In JABAS, a DNN training job is executed on a DNN training framework called IIDP, which provides the same theoretical convergence rate of distributed SGD in a heterogeneous GPU cluster. To maximize the performance of the job with adaptive batching, JABAS employs adaptive batching and automatic resource scaling jointly. JABAS changes a global batch size every 𝑝iterations in a fine-grained manner within an epoch, while auto-scaling to the best GPU allocation for the next epoch in a coarse-grained manner. Using three heterogeneous GPU clusters, we evaluate JABAS for seven DNN models including large language models. Our experimental results demonstrate that JABAS provides 33.3% shorter training time and 54.2% lower training cost than the state-of-the-art adaptive training techniques, on average, without any accuracy loss.

## 中文摘要

自适应批处理是一种有望降低深度神经网络（DNN）模型训练中通信与同步开销的技术。本文研究如何在异构 GPU 集群中利用自适应批处理加速 DNN 模型训练，同时不损害收敛性能。我们提出一种新颖的 DNN 训练系统 JABAS（联合自适应批处理与自动伸缩）。在 JABAS 中，DNN 训练作业运行在名为 IIDP 的 DNN 训练框架上，该框架在异构 GPU 集群中提供与分布式 SGD 相同的理论收敛速率。为借助自适应批处理最大化作业性能，JABAS 将自适应批处理与资源自动伸缩结合起来协同使用。JABAS 在一个 epoch 内以细粒度方式每 𝑝 次迭代改变一次全局批大小，同时以粗粒度方式自动伸缩到下一个 epoch 的最佳 GPU 分配。我们使用三个异构 GPU 集群，针对包括大语言模型在内的七个 DNN 模型评估了 JABAS。实验结果表明，平均而言，JABAS 相比最先进的自适应训练技术缩短了 33.3% 的训练时间、降低了 54.2% 的训练成本，且没有任何精度损失。

**英文关键词：** Distributed Systems, Systems for Machine Learning

**中文关键词：** 分布式系统、机器学习系统

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
