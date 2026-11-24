---
title: "Forecasting GPU Performance for Deep Learning Training and Inference"
description: "ASPLOS 2025 · Session 5A · 面向深度学习训练与推理的 GPU 性能预测"
tags:
  - "ASPLOS2025"
  - "Session 5A"
  - "ML Systems 1"
---

# Forecasting GPU Performance for Deep Learning Training and Inference

**中文标题：** 面向深度学习训练与推理的 GPU 性能预测

**所属 Session：** [Session 5A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Seonho Lee (Georgia Institute of Technology), Amar Phanishayee (Meta), Divya Mahajan (Georgia Institute of Technology)

**单位：** Georgia Institute of Technology；Meta

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707265) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Deep learning kernels exhibit a high level of predictable memory accesses and compute patterns, making GPU's architecture well-suited for their execution. Moreover, software and runtime system for GPUs further enable optimizations that aim to better utilize the stream multiprocessors, on-chip bandwidth, multiple levels of cache hierarchy, and off-chip high-bandwidth memory. In the context of deep learning, the entire space of models and GPUs is constantly evolving, as newer models emerge with simultaneous upgrades to the device. However, access to newer GPUs is often limited, raising important questions about the performance of new model architectures on existing GPUs, existing models on new GPUs, and new model architectures on new GPUs. To address these questions, we introduce NeuSight, a forecasting framework to predict the performance of a diverse range of deep learning models, for both training and inference, on unseen GPUs, without requiring actual execution of the target model on the target GPU. The framework leverages both GPU hardware behavior and software library optimizations to estimate the end-to-end performance of these models. We observe that prior work in this area suffers from high absolute error percentages when forecasting performance on unseen models and new GPUs, as they attempt to model the complex task of predicting the latency of a deep learning kernel on a GPU directly using a machine learning approach. Instead, with NeuSight, we decompose the prediction into smaller problems, while bounding the prediction through fundamental performance laws. NeuSight decomposes a single deep learning kernel prediction into smaller working sets called tiles, which are executed independently on the GPU. Tile-granularity predictions are determined using a machine learning approach and aggregated to estimate the end-to-end latency. As such, NeuSight outperforms prior work across a variety of deep learning workloads and the most up-to-date GPUs. It reduces the percentage error from Attribution International 4.0 License..4% and 30.8% to 2.3% in predicting the latency of GPT3 model for training and inference on H100, in comparison to state-of-the-art prior work, respectively, where GPT3 and H100 were not used to train any framework.

## 中文摘要

深度学习内核在访存与计算模式上呈现出高度可预测性，因而 GPU 的体系结构非常适合执行这类负载。此外，GPU 的软件与运行时系统进一步支撑了各类优化，以更好地利用流多处理器、片上带宽、多级缓存层次以及片外高带宽内存。在深度学习场景下，整个模型与 GPU 的空间都在持续演进：新模型不断涌现，同时设备也在同步升级。然而，对更新一代 GPU 的获取往往受到限制，这就引出了一些重要问题——新模型架构在已有 GPU 上的性能如何、已有模型在新 GPU 上的性能如何，以及新模型架构在新 GPU 上的性能如何。为解决这些问题，我们提出 NeuSight，一个性能预测框架，能够在不需要目标模型在目标 GPU 上实际执行的前提下，预测多种深度学习模型在未见过 GPU 上的性能（训练与推理）。该框架同时利用 GPU 硬件行为与软件库优化来估计这些模型的端到端性能。我们观察到，该领域先前的工作在预测未见模型与新 GPU 上的性能时存在较高的绝对误差百分比，因为它们试图直接用机器学习方法对预测深度学习内核在 GPU 上的延迟这一复杂任务建模。相反，在 NeuSight 中，我们把预测分解为更小的问题，同时通过基本性能定律对预测加以约束。NeuSight 将单个深度学习内核的预测分解为称为 tile 的更小工作集，这些 tile 在 GPU 上独立执行。tile 粒度的预测由机器学习方法确定，并聚合起来估计端到端延迟。因此，NeuSight 在多种深度学习负载与最新 GPU 上都优于先前工作。在预测 GPT3 模型于 H100 上训练与推理的延迟时，与最先进的先前工作相比，它分别将百分比误差从 4.4% 和 30.8% 降至 2.3%，而 GPT3 与 H100 均未被用于训练任何框架。

## 英文关键词

GPU Performance Forecasting, ML for Systems, Deep Learning, Training and Inference

## 中文关键词

GPU 性能预测；面向系统的机器学习；深度学习；训练与推理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707265)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5A](index.md) · [返回 ASPLOS 2025](../index.md)
