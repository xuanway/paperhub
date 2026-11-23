---
title: "Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures"
description: "ISCA 2025 · Session 9A · 洞察 DeepSeek-V3：扩展挑战与 AI 体系结构硬件反思"
tags:
  - "ISCA2025"
  - "Session 9A"
  - "Industry Track"
---

# Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures

**中文标题：** 洞察 DeepSeek-V3：扩展挑战与 AI 体系结构硬件反思

**所属 Session：** [Session 9A](index.md) · [ISCA 2025](../index.md)

**作者：** Chenggang Zhao, Chengqi Deng, Chong Ruan, Damai Dai, Huazuo Gao, Jiashi Li, Liyue Zhang, Panpan Huang, Shanyan Zhou, Shirong Ma, Wenfeng Liang, Ying He, Yuqing Wang, Yuxuan Liu, Y.X. Wei

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731412) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The rapid scaling of large language models (LLMs) has unveiled critical limitations in current hardware architectures, including con- straints in memory capacity, computational efficiency, and intercon- nection bandwidth. DeepSeek-V3, trained on 2,048 NVIDIA H800 GPUs, demonstrates how hardware-aware model co-design can effectively address these challenges, enabling cost-efficient training and inference at scale. This paper presents an in-depth analysis of the DeepSeek-V3/R1 model architecture and its AI infrastructure, highlighting key innovations such as Multi-head Latent Attention (MLA) for enhanced memory efficiency, Mixture of Experts (MoE) architectures for optimized computation-communication trade-offs, FP8 mixed-precision training to unlock the full potential of hard- ware capabilities, and a Multi-Plane Network Topology to minimize cluster-level network overhead. Building on the hardware bottle- necks encountered during DeepSeek-V3’s development, we engage in a broader discussion with academic and industry peers on po- tential future hardware directions, including precise low-precision computation units, scale-up and scale-out convergence, and in- novations in low-latency communication fabrics. These insights underscore the critical role of hardware and model co-design in meeting the escalating demands of AI workloads, offering a practi- cal blueprint for innovation in next-generation AI systems.

## 中文摘要

大语言模型（LLM）的快速扩容，暴露出现有硬件架构的诸多短板，包括显存容量、计算效率与互联带宽受限等问题。DeepSeek-V3 使用2048张NVIDIA H800 GPU完成训练，展示了面向硬件感知的模型协同设计可以有效应对上述难题，实现低成本、大规模的训练与推理。本文对DeepSeek-V3/R1模型架构及其AI基础设施进行深度剖析，重点介绍多项核心创新：利用多头隐式注意力（MLA）提升显存效率；采用混合专家（MoE）架构，在计算与通信之间取得更优权衡；FP8混合精度训练，充分释放硬件算力潜力；以及多平面网络拓扑，降低集群层面的网络开销。

基于DeepSeek-V3研发过程中遇到的硬件瓶颈，本文和学术界、工业界同行展开更广泛的探讨，展望未来硬件方向，包括高精度低精度计算单元、纵向扩容与横向扩展的融合、低延迟通信架构创新。这些结论凸显了硬件-模型协同设计对承载日益增长的AI负载的重要价值，为下一代AI系统的研发提供了可落地的参考方案。

## 英文关键词

Large Language Model, Mixture-of-Experts, Deep Learning, FP8 Mixed-Precision Training, Multi-Plane Network, Co-Design

## 中文关键词

大语言模型, 混合专家模型, 深度学习, FP8混合精度训练, 多平面网络, 协同设计

## 代码与研究制品

- [代码仓库](https://github.com/deepseek-ai/dualpipe)
- [代码仓库](https://github.com/deepseek-ai/3FS)
- [代码仓库](https://github.com/deepseek-ai/DeepGEMM)
- [代码仓库](https://github.com/deepseek-ai/DeepEP)
- [代码仓库](https://github.com/deepseek-ai/profile-data)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731412)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 9A](index.md) · [返回 ISCA 2025](../index.md)
