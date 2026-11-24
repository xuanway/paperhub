---
title: "It Takes Two to Entangle"
description: "ASPLOS 2026 · Session 5A · 纠缠需要双方"
tags:
  - "ASPLOS2026"
  - "Session 5A"
  - "Generative Model Serving"
---

# It Takes Two to Entangle

**中文标题：** 纠缠需要双方

**所属 Session：** [Session 5A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zhanghan Wang (New York University), Ding Ding (New York University), Hang Zhu (ByteDance Inc.), Haibin Lin (ByteDance Inc.), Aurojit Panda (New York University)

**单位：** New York University；ByteDance Inc.

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790178) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Distributed machine learning training and inference is common today because today's large models require more memory and compute than can be provided by a single GPU. Distributed models are generally produced by programmers who take a sequential model specification and apply several distribution strategies to distribute state and computation across GPUs. Unfortunately, bugs can be introduced in the process, and a distributed model implementation's outputs might differ from the sequential model's outputs. In this paper, we describe an approach to statically identify such bugs by checking model refinement, that is, can the sequential model's outputs be reconstructed from the distributed model's outputs? Our approach, implemented in Entangle, uses iterative rewriting to prove model refinement. Our approach can scale to today's large models and deployments: we evaluate it using GPT and Llama-3. Further, it provides actionable outputs that aids in bug localization.

## 中文摘要

分布式机器学习训练与推理在如今十分常见，因为当今的大模型所需的内存和计算超出了单个 GPU 所能提供的能力。分布式模型通常由程序员产出：他们取用顺序模型规约，并应用若干分布式策略，在各 GPU 之间分布状态与计算。不幸的是，这一过程可能引入缺陷，分布式模型实现的输出可能与顺序模型的输出不一致。本文描述了一种通过检查模型精化来静态识别此类缺陷的方法，即：顺序模型的输出能否从分布式模型的输出中重建？我们的方法实现在 Entangle 中，使用迭代重写来证明模型精化。我们的方法能够扩展到当今的大模型与部署：我们使用 GPT 和 Llama-3 对其进行评估。此外，它提供了有助于缺陷定位的可操作输出。

## 英文关键词

Formal Verification, Distributed Deep Learning, Equality Saturation, Bug Localization

## 中文关键词

形式化验证；分布式深度学习；等式饱和；缺陷定位

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790178)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5A](index.md) · [返回 ASPLOS 2026](../index.md)
