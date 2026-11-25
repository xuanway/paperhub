---
title: "FastFold: Optimizing AlphaFold Training and Inference on GPU Clusters"
description: "PPoPP 2024 Session Applications：FastFold：训练 11 天→67 小时，长序列推理提速 7.5~9.5×"
tags:
  - "PPoPP2024"
  - "Session-10"
  - "Applications"
  - "Model Parallelism"
  - "Distributed Deep Learning"
  - "GPU"
authors:
  - "Shenggan Cheng"
  - "Xuanlei Zhao"
  - "Guangyang Lu"
  - "Jiarui Fang"
  - "Tian Zheng"
  - "Ruidong Wu"
  - "Xiwen Zhang"
  - "Jian Peng"
  - "Yang You"
session: "Session 10: Applications"
session_number: 10
session_chair: "Milind Chabbi"
date: "2024-03-06"
time: "11:30–11:50"
room: "Moorfoot"
doi: "10.1145/3627535.3638465"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# FastFold: Optimizing AlphaFold Training and Inference on GPU Clusters

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 FastFold，以动态轴向并行（DAP）与 AutoChunk 为核心，把 AlphaFold 训练从 11 天缩短至 67 小时，长序列推理提速 7.5~9.5×。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 10: Applications</p>
</div>

**作者**：Shenggan Cheng (National University of Singapore); Xuanlei Zhao, Guangyang Lu, Jiarui Fang (HPC-AI Tech); Tian Zheng (Xi’an Jiaotong University); Ruidong Wu, Xiwen Zhang, Jian Peng (HeliXon); Yang You (National University of Singapore)

**会议**：PPoPP 2024 · 2024 年 3 月 6 日 11:30–11:50 · Session 10: Applications（主席：Milind Chabbi）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638465) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Protein structure prediction helps to understand gene translation and protein function, which is of growing interest and importance in structural biology. The AlphaFold model, which used transformer architecture to achieve atomic-level accuracy in protein structure prediction, was a significant breakthrough. However, training and inference of AlphaFold model are challenging due to its high computation and memory cost. In this work, we present FastFold, an efficient implementation of AlphaFold for both training and inference. We propose Dynamic Axial Parallelism (DAP) as a novel model parallelism method. Additionally, we have implemented a series of low-level optimizations aimed at reducing communication, computation, and memory costs. These optimizations include Duality Async Operations, highly optimized kernels, and AutoChunk (an automated search algorithm finds the best chunk strategy to reduce memory peaks). Experimental results show that FastFold can efficiently scale to more GPUs using DAP and reduces overall training time from 11 days to 67 hours and achieves 7.5 ∼9.5× speedup for long-sequence inference. Furthermore, AutoChunk can reduce memory cost by over 80% during inference by automatically partitioning the intermediate tensors during the computation.

## 中文摘要

蛋白质结构预测有助于理解基因翻译与蛋白质功能，在结构生物学中日益受到关注并愈发重要。AlphaFold 模型使用 transformer 架构，在蛋白质结构预测上达到原子级精度，是一次重大突破。然而，AlphaFold 模型的训练与推理因其高昂的计算与内存开销而颇具挑战。在本工作中，我们提出 FastFold，一个用于训练与推理的高效 AlphaFold 实现。我们提出动态轴向并行（DAP）作为一种新的模型并行方法。此外，我们实现了一系列底层优化，旨在降低通信、计算与内存开销。这些优化包括双流异步操作（Duality Async Operations）、高度优化的内核，以及 AutoChunk（一种自动搜索算法，用于找到最佳的 chunk 策略以降低内存峰值）。实验结果表明，FastFold 借助 DAP 可高效扩展到更多 GPU，并将整体训练时间从 11 天缩短至 67 小时，在长序列推理上取得 7.5~9.5× 加速。此外，AutoChunk 通过自动切分计算过程中的中间张量，可将推理时的内存开销降低 80% 以上。

## 英文关键词

Distributed Deep Learning, GPUs, Model Parallelism, Protein Structure Prediction

## 中文关键词

分布式深度学习；GPU；模型并行；蛋白质结构预测

---

## 一句话总结

> 提出 FastFold，以动态轴向并行（DAP）与 AutoChunk 为核心，把 AlphaFold 训练从 11 天缩短至 67 小时，长序列推理提速 7.5~9.5×。

## 研究问题

AlphaFold 借助 transformer 架构在蛋白质结构预测上达到原子级精度，但其训练与推理的计算与内存开销很高，难以高效运行和扩展。

## 方法简述

- 提出动态轴向并行（DAP）这一新的模型并行方法，使 FastFold 能高效扩展到更多 GPU
- 采用双流异步操作（Duality Async Operations）以降低通信开销
- 设计高度优化的内核，降低计算开销
- 设计 AutoChunk，用自动搜索算法找到最佳的 chunk 策略以削减内存峰值

## 主要结果

- 借助 DAP 可高效扩展到更多 GPU，整体训练时间从 11 天缩短至 67 小时
- 长序列推理取得 7.5~9.5× 加速
- AutoChunk 通过自动切分计算过程中的中间张量，可将推理内存开销降低 80% 以上

---

> 所属 Session：[Session 10: Applications](index.md) · 返回 [PPoPP 2024 总览](../index.md)
