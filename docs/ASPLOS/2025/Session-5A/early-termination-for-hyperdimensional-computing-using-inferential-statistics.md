---
title: "Early Termination for Hyperdimensional Computing Using Inferential Statistics"
description: "ASPLOS 2025 · Session 5A · 基于推断统计的超维计算提前终止"
tags:
  - "ASPLOS2025"
  - "Session 5A"
  - "ML Systems 1"
---

# Early Termination for Hyperdimensional Computing Using Inferential Statistics

**中文标题：** 基于推断统计的超维计算提前终止

**所属 Session：** [Session 5A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Pu (Luke) Yi (Stanford University), Yifan Yang (Stanford University), Chae Young Lee (Stanford University), Sara Achour (Stanford University)

**单位：** Luke；Stanford University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707254) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Hyperdimensional Computing (HDC) is a brain-inspired, lightweight computing paradigm that has shown great potential for inference on the edge and on emerging hardware technologies, achieving state-of-the-art accuracy on certain classification tasks. HDC classifiers are inherently error resilient and support early termination of inference to approximate classification results. Practitioners have developed heuristic methods to terminate inference early for individual inputs, reducing the computation of inference at the cost of accuracy. These techniques lack statistical guarantees and may unacceptably degrade classification accuracy or terminate inference later than is needed to obtain an accuracy result. We present Omen, the first dynamic HDC optimizer that uses inferential statistics to terminate inference early while providing accuracy guarantees. To realize Omen, we develop a statistical view of HDC that reframes HD computations as statistical sampling and testing tasks, enabling the use of statistical tests. We evaluate Omen on 19 benchmark instantiations of four classification tasks. Omen is computationally efficient, delivering up to 7.21–12.18× inference speed-ups over an unoptimized baseline while only incurring a 0.0–0.7% drop in accuracy. Omen outperforms heuristic methods, achieving an additional 0.04–5.85× inference speed-up over the unoptimized baseline compared to heuristic methods while maintaining higher or comparable accuracy.

## 中文摘要

超维计算（HDC）是一种受大脑启发的轻量级计算范式，在边缘端推理与新兴硬件技术上已展现出巨大潜力，在某些分类任务上达到了最先进的精度。HDC 分类器天生具有容错性，并支持提前终止推理以近似分类结果。实践者已开发出启发式方法，为单个输入提前终止推理，从而在牺牲精度的代价下减少推理计算量。这些技术缺乏统计保证，可能会不可接受地降低分类精度，或者比获得一个精度结果所需更晚地终止推理。我们提出 Omen，这是首个利用推断统计在提供精度保证的同时提前终止推理的动态 HDC 优化器。为实现 Omen，我们发展出一种 HDC 的统计视角，将 HD 计算重新表述为统计采样与检验任务，从而可以使用统计检验。我们在四个分类任务的 19 个基准实例上评估了 Omen。Omen 计算高效，相较于未优化基线可带来最高 7.21–12.18× 的推理加速，而精度仅下降 0.0–0.7%。Omen 优于启发式方法：与启发式方法相比，在保持更高或相当精度的同时，相对于未优化基线还能额外获得 0.04–5.85× 的推理加速。

## 英文关键词

program optimization, unconventional computing, hyperdimensional computing, emerging hardware technologies, edge machine learning

## 中文关键词

程序优化；非常规计算；超维计算；新兴硬件技术；边缘机器学习

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707254)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5A](index.md) · [返回 ASPLOS 2025](../index.md)
