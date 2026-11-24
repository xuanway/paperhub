---
title: "Scaling Llama 3 Training with Efficient Parallelism Strategies"
description: "ISCA 2025 · Session 9A · 利用高效并行策略扩展 Llama 3 训练"
tags:
  - "ISCA2025"
  - "Session 9A"
  - "Industry Track"
---

# Scaling Llama 3 Training with Efficient Parallelism Strategies

**中文标题：** 利用高效并行策略扩展 Llama 3 训练

**所属 Session：** [Session 9A](index.md) · [ISCA 2025](../index.md)

**作者：** Weiwei Chu, Xinfeng Xie, Jiecao Yu, Jie Wang, Amar Phanishayee, Chunqiang Tang, Yuchen Hao, Jianyu Huang, Mustafa Ozdal, Jun Wang, Vedanuj Goswami, Naman Goyal, Abhishek Kadian, Andrew Gu, Chris Cai, Feng Tian, Xiaodong Wang, Min Si, Pavan Balaji, Ching-Hsiang Chu, Jongsoo Park

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731410) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Llama is a widely used open-source large language model. This paper presents the design and implementation of the parallelism techniques used in Llama 3 pre-training. To achieve efficient train- ing on tens of thousands of GPUs, Llama 3 employs a combination of four-dimensional parallelism: fully sharded data parallelism, tensor parallelism, pipeline parallelism, and context parallelism. Beyond achieving efficiency through parallelism and model co-design, we also address other equally critical aspects. First, we enhance flexibil- ity—for example, through novel pipeline parallelism that supports evolving batch sizes and heterogeneous model architectures, and innovative context parallelism that enables model innovations such as document-mask attention. Second, we prioritize practicality—for example, by enabling the diagnosis of performance and numerical issues at scale. Finally, drawing on our experience with large-scale training, we provide recommendations for future hardware design.

## 中文摘要

Llama 是应用广泛的开源大语言模型。本文介绍 Llama 3 预训练所采用并行技术的设计与实现。为在数万张GPU上实现高效训练，Llama 3 组合使用四维并行方案：全分片数据并行、张量并行、流水线并行以及上下文并行。

除了通过并行策略与模型协同设计来提升训练效率之外，本文还研究了其他同等重要的问题。首先，提升灵活性：例如，提出新型流水线并行，支持动态变化的批大小与异构模型架构；创新的上下文并行，支持文档掩码注意力等模型创新。其次，重视工程实用性：支持大规模场景下的性能问题与数值异常诊断。最后，基于大规模训练实践经验，对未来硬件设计给出建议。

## 英文关键词

Large Language Model, Training, Parallelism, Distributed System

## 中文关键词

大语言模型, 训练, 并行策略, 分布式系统

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731410)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 9A](index.md) · [返回 ISCA 2025](../index.md)
