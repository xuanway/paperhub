---
title: "Chimera: Communication Fusion for Hybrid Parallelism in Large Language Models"
description: "ISCA 2025 · Session 4A · Chimera: 大语言模型混合并行通信融合"
tags:
  - "ISCA2025"
  - "Session 4A"
  - "LLMs"
---

# Chimera: Communication Fusion for Hybrid Parallelism in Large Language Models

**中文标题：** Chimera: 大语言模型混合并行通信融合

**所属 Session：** [Session 4A](index.md) · [ISCA 2025](../index.md)

**作者：** Le Qin, Junwei Cui, Weilin Cai, Jiayi Huang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731025) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Large Language Models (LLMs), exemplified by ChatGPT, have emerged as a predominant workload in current machine learning systems. To achieve efficient training and inference within the con- straints of limited single-NPU memory capacity, deploying LLMs on multi-NPU systems typically adopt a hybrid approach that combines various parallelism patterns. This hybrid parallelism within LLMs introduces a significant amount of diverse collective communica- tions. However, these frequent blocking communications impose a substantial burden on the multi-NPU systems. Overcoming the communication bottleneck is crucial to unlocking the potential of multi-NPU systems for efficient and scalable LLM processing. This paper introduces Chimera, a communication fusion mecha- nism for hybrid parallelism in LLMs. We comprehensively analyze the communication processes of each LLM parallelism pattern, identify the communication redundancy in hybrid parallelism and eliminate redundancy by fusing adjacent communication opera- tors during parallelism transformation. By reordering operations and generating redundancy-free communication operator, Chimera effectively mitigates communication bottleneck in hybrid LLM parallelism. Our results show that Chimera achieves 1.23-7.06× network bandwidth speedup. Additionally, the end-to-end perfor- mance of LLM forward pass and backward pass on different typical multi-NPU systems achieves respective 1.32-1.58×and 1.16-1.36× speedups on average compared with those without communication fusion.

## 中文摘要

以ChatGPT为代表的大语言模型（LLM）已经成为当下机器学习系统中的主流负载。受单块NPU内存容量限制，在多NPU平台部署LLM以实现高效训练与推理，通常采用融合多种并行模式的混合并行方案。LLM中的这类混合并行会产生大量种类繁多的集合通信。然而，这些频繁的阻塞式通信给多NPU系统带来沉重负担。突破通信瓶颈，是释放多NPU系统潜力、实现高效可扩展LLM计算的关键。

本文提出Chimera，一种面向LLM混合并行的通信融合机制。我们全面分析各类LLM并行模式下的通信流程，识别混合并行中的通信冗余；在并行变换阶段，通过合并相邻通信算子消除冗余。Chimera通过重排运算顺序、生成无冗余的通信算子，有效缓解LLM混合并行场景下的通信瓶颈。实验结果表明，Chimera可将网络带宽利用率提升至原来的1.23–7.06倍。在多款典型多NPU系统上，相较于不启用通信融合的基线，LLM前向传播与反向传播的端到端性能平均分别提升1.32–1.58倍、1.16–1.36倍。

## 英文关键词

Collective Communication, Large Language Models, Distributed Training

## 中文关键词

混合并行, 大语言模型, 分布式训练

## 代码与研究制品

- [代码仓库](https://github.com/redbird-arch/isca2025-chimera-artifact)
- [研究制品](https://zenodo.org/records/15233215)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731025)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4A](index.md) · [返回 ISCA 2025](../index.md)
