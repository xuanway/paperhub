---
title: "Taming the Long-Tail: Efficient Reasoning RL Training with Adaptive Drafter"
description: "ASPLOS 2026 · Session 3B · 驯服长尾：基于自适应草稿模型的高效推理强化学习训练"
tags:
  - "ASPLOS2026"
  - "Session 3B"
  - "Mixture-of-Experts & Efficient Inference"
---

# Taming the Long-Tail: Efficient Reasoning RL Training with Adaptive Drafter

**中文标题：** 驯服长尾：基于自适应草稿模型的高效推理强化学习训练

**所属 Session：** [Session 3B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Qinghao Hu (MIT), Shang Yang (MIT), Junxian Guo (MIT), Xiaozhe Yao (ETH Zurich), Yujun Lin (NVIDIA), Yuxian Gu (NVIDIA), Han Cai (NVIDIA), Chuang Gan (MIT-IBM Watson AI Lab, UMass Amherst), Ana Klimovic (ETH Zurich), Song Han (MIT)

**单位：** MIT；ETH Zurich；NVIDIA；MIT-IBM Watson AI Lab, UMass Amherst

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790231) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The emergence of Large Language Models (LLMs) with strong reasoning capabilities marks a significant milestone, unlocking new frontiers in complex problem-solving. However, training these reasoning models, typically using Reinforcement Learning (RL), encounters critical efficiency bottlenecks: response generation during RL training exhibits a persistent long-tail distribution, where a few very long responses dominate execution time, wasting resources and inflating costs. To address this, we propose TLT, a system that accelerates reasoning RL training losslessly by integrating adaptive speculative decoding. Applying speculative decoding in RL is challenging due to the dynamic workloads, evolving target model, and draft model training overhead. TLT overcomes these obstacles with two synergistic components: (1) Adaptive Drafter, a lightweight draft model trained continuously on idle GPUs during long-tail generation to maintain alignment with the target model at no extra cost; and (2) Adaptive Rollout Engine, which maintains a memory-efficient pool of pre-captured CUDAGraphs and adaptively select suitable SD strategies for each input batch. Evaluations demonstrate that TLT achieves over 1.7× end-to-end RL training speedup over state-of-the-art systems, preserves the model accuracy, and yields a high-quality draft model as a free byproduct suitable for efficient deployment. Code is released at

## 中文摘要

具备强推理能力的大语言模型（LLM）的出现标志着一个重要里程碑，开辟了复杂问题求解的新前沿。然而，训练这些推理模型（通常使用强化学习，RL）会遇到严重的效率瓶颈：RL 训练期间的响应生成呈现出持续的长尾分布，少数极长的响应占据了主要执行时间，浪费资源并推高成本。为解决这一问题，我们提出 TLT，一个通过集成自适应投机解码来无损加速推理 RL 训练的系统。在 RL 中应用投机解码面临挑战，原因在于动态的工作负载、不断演进的目标模型以及草稿模型的训练开销。TLT 通过两个协同组件克服了这些障碍：(1) Adaptive Drafter，一个轻量级草稿模型，在长尾生成期间利用空闲 GPU 持续训练，从而在无额外成本的情况下与目标模型保持对齐；(2) Adaptive Rollout Engine，它维护一个内存高效的预捕获 CUDAGraph 池，并为每个输入批次自适应地选择合适的 SD 策略。评估表明，TLT 相比最先进的系统实现了超过 1.7× 的端到端 RL 训练加速，保持了模型精度，并作为免费的副产品产出一个适合高效部署的高质量草稿模型。代码发布于

## 英文关键词

Large Language Models, Reinforcement Learning, Speculative Decoding, Training Efficiency

## 中文关键词

大语言模型；强化学习；投机解码；训练效率

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790231)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3B](index.md) · [返回 ASPLOS 2026](../index.md)
