---
title: "History Doesn’t Repeat Itself but Rollouts Rhyme: Accelerating Reinforcement Learning with HistoRL"
description: "ASPLOS 2026 · Session 6A · 历史不会重演，但 Rollout 会押韵：用 HistoRL 加速强化学习"
tags:
  - "ASPLOS2026"
  - "Session 6A"
  - "Neural Network Acceleration"
---

# History Doesn’t Repeat Itself but Rollouts Rhyme: Accelerating Reinforcement Learning with HistoRL

**中文标题：** 历史不会重演，但 Rollout 会押韵：用 HistoRL 加速强化学习

**所属 Session：** [Session 6A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jingkai He (Shanghai Jiao Tong University), Tianjian Li (ByteDance), Erhu Feng (Shanghai Jiao Tong University), Dong Du (Shanghai Jiao Tong University), Qian Liu (ByteDance), Tao Liu (ByteDance), Yubin Xia (Shanghai Jiao Tong University), Haibo Chen (Shanghai Jiao Tong University)

**单位：** Shanghai Jiao Tong University；ByteDance

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790172) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

**出版标题：** History Doesn't Repeat Itself but Rollouts Rhyme: Accelerating Reinforcement Learning with RhymeRL

## 英文摘要

With the rapid advancement of large language models (LLMs), reinforcement learning (RL) has emerged as a pivotal methodology for enhancing the reasoning capabilities of LLMs. Unlike traditional pre-training approaches, RL encompasses multiple stages: rollout, reward, and training, which necessitates collaboration among various worker types. However, current RL systems continue to grapple with substantial GPU underutilization, due to two primary factors: (1) The rollout stage dominates the overall RL process due to test-time scaling; (2) Imbalances in rollout lengths (within the same batch) result in GPU bubbles. While prior solutions like asynchronous execution and truncation offer partial relief, they may compromise training accuracy for efficiency. Our key insight stems from a previously overlooked observation: rollout responses exhibit remarkable similarity across adjacent training epochs. Based on the insight, we introduce RhymeRL, an LLM RL system designed to accelerate RL training with two key innovations. First, to enhance rollout generation, we present HistoSpec, a speculative decoding inference engine that utilizes the similarity of historical rollout token sequences to obtain accurate drafts. Second, to tackle rollout bubbles, we introduce HistoPipe, a two-tier scheduling strategy that leverages the similarity of historical rollout distributions to balance workload among rollout workers. Experimental results demonstrate that RhymeRL achieves up to a 2.6x performance improvement over existing methods, without compromising accuracy or modifying the RL paradigm.

## 中文摘要

随着大语言模型（LLMs）的快速发展，强化学习（RL）已成为增强 LLM 推理能力的关键方法。与传统的预训练方法不同，RL 包含多个阶段：rollout、reward 和 training，这需要多种类型 worker 之间的协作。然而，当前的 RL 系统仍面临 GPU 利用率严重不足的问题，主要原因有两个：（1）由于 test-time scaling，rollout 阶段主导了整个 RL 过程；（2）rollout 长度的不均衡（在同一 batch 内）导致 GPU 气泡。虽然异步执行和截断等先前方案提供了部分缓解，但它们可能为效率而牺牲训练精度。我们的关键洞见来自一个此前被忽视的观察：rollout 响应在相邻训练 epoch 之间表现出显著的相似性。基于这一洞见，我们提出 RhymeRL，一个旨在通过两项关键创新加速 RL 训练的 LLM RL 系统。第一，为增强 rollout 生成，我们提出 HistoSpec，一个投机解码推理引擎，它利用历史 rollout token 序列的相似性来获得准确的草稿。第二，为应对 rollout 气泡，我们引入 HistoPipe，一种两级调度策略，利用历史 rollout 分布的相似性来平衡 rollout worker 之间的工作负载。实验结果表明，RhymeRL 相比现有方法实现了最高 2.6 倍的性能提升，且不牺牲精度，也不修改 RL 范式。

## 英文关键词

Large language models, Reinforcement Learning

## 中文关键词

大语言模型；强化学习

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790172)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6A](index.md) · [返回 ASPLOS 2026](../index.md)
