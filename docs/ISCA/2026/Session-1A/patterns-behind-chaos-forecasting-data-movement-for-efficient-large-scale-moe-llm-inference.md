---
title: "Patterns behind Chaos: Forecasting Data Movement for Efficient Large-Scale MoE LLM Inference"
description: "ISCA 2026 · Session 1A · Patterns behind Chaos: Forecasting Data Movement for Efficient Large-Scale MoE LLM Inference"
tags:
  - "ISCA2026"
  - "Session 1A"
  - "Best Paper Candidate Session"
---

# Patterns behind Chaos: Forecasting Data Movement for Efficient Large-Scale MoE LLM Inference

**中文标题：** 混沌背后的模式：面向高效大规模 MoE LLM 推理的数据搬运预测

**所属 Session：** [Session 1A](index.md) · [ISCA 2026](../index.md)

**作者：** Zhongkai Yu, Yue Guan, Zihao Yu, Chenyang Zhou, Zhengding Hu, Shuyi Pei, Yangwook Kang, Yufei Ding, Po-An Tsai

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Large-scale Mixture of Experts (MoE) Large Language Models (LLMs) have recently become the frontier open-weight models, achieving remarkable model capability similar to proprietary ones. But their random expert selection mechanism introduces significant data movement overhead that becomes the dominant bottleneck in multi-unit LLM serving systems. To understand the patterns underlying this data movement, we conduct comprehensive data-movement-centric profiling across four state-of-the-art large-scale MoE models released in 2025 (200B-1000B) using over 24,000 requests spanning diverse workloads. We perform systematic analysis from both temporal and spatial perspectives and distill six key insights to guide the design of diverse serving systems. We verify these insights on both future wafer-scale GPU architectures and existing GPU systems. On wafer-scale GPUs, lightweight architectural modifications guided by our insights yield a 6.6x average speedup across four 200B– 1000B models. On existing GPU systems, our insights drive the design of a prefill-aware expert placement algorithm that achieves up to 1.25x speedup on MoE computation. Our work presents the first comprehensive data-centric analysis of large-scale MoE models together with a concrete design study applying the learned lessons. Our profiling traces are publicly available at https://huggingface.co/datasets/core12345/MoE_expert_selection_trace.

## 中文摘要

大规模混合专家（MoE）大语言模型（LLM）近期已成为前沿的开源权重模型，实现了与专有模型相当卓越的模型能力。但其随机专家选择机制引入了显著的数据搬运开销，成为多单元 LLM 服务系统中的主要瓶颈。为理解这种数据搬运背后的模式，我们使用超过 24,000 个涵盖多样化工作负载的请求，对 2025 年发布的四个最先进的大规模 MoE 模型（200B-1000B）进行了全面的以数据搬运为中心的性能分析。我们从时间和空间两个角度进行了系统性分析，并提炼出六项关键洞察，以指导多样化服务系统的设计。我们在未来的晶圆级 GPU 架构和现有的 GPU 系统上验证了这些洞察。在晶圆级 GPU 上，由我们的洞察指导的轻量级架构修改在四个 200B-1000B 模型上实现了平均 6.6× 的加速。在现有 GPU 系统上，我们的洞察驱动了一种预填充感知的专家放置算法的设计，在 MoE 计算上实现了高达 1.25× 的加速。我们的工作首次对大规模 MoE 模型进行了全面的以数据为中心的分析，并提供了应用所学经验的具体设计案例研究。我们的性能分析踪迹已在 https://huggingface.co/datasets/core12345/MoE_expert_selection_trace 公开提供。

## 代码与研究制品

论文提供了两个案例研究的实验材料归档链接：

- [实验材料归档（Zenodo 19617713）](https://zenodo.org/records/19617713)（论文或公开检索提供；本次未能在线核实页面）
- [实验材料归档（Zenodo 19617695）](https://zenodo.org/records/19617695)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 1A](index.md) · [返回 ISCA 2026](../index.md)
