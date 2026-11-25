---
title: "COMPSO: Optimizing Gradient Compression for Distributed Training with Second-Order Optimizers"
description: "PPoPP 2025 Session 5（Deep Neural Networks）：二阶优化器专用梯度压缩，压缩比 22.1×、端到端 1.9×"
tags:
  - "PPoPP2025"
  - "Session-5"
  - "Deep Neural Networks"
  - "Gradient Compression"
  - "Second-Order Optimization"
  - "Distributed Training"
authors:
  - "Baixi Sun"
  - "Weijin Liu"
  - "J. Gregory Pauloski"
  - "Jiannan Tian"
  - "Jinda Jia"
  - "Daoce Wang"
  - "Boyuan Zhang"
  - "Mingkai Zheng"
  - "Sheng Di"
  - "Sian Jin"
  - "Zhao Zhang"
  - "Xiaodong Yu"
  - "Kamil A. Iskra"
  - "Pete Beckman"
  - "Guangming Tan"
  - "Dingwen Tao"
session: "Session 5: Deep Neural Networks"
session_number: 5
session_chair: "Wei Niu"
date: "2025-03-03"
time: "17:40–18:00"
room: "Acacia D"
doi: "10.1145/3710848.3710852"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# COMPSO: Optimizing Gradient Compression for Distributed Training with Second-Order Optimizers

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出面向二阶优化器的梯度压缩方法 COMPSO，用随机舍入保持精度、过滤微小梯度提高压缩比，并配合 GPU 优化与性能建模确保端到端收益。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 5: Deep Neural Networks</p>
</div>

**作者**：Baixi Sun (Indiana University); Weijin Liu (Stevens Institute of Technology); J. Gregory Pauloski (University of Chicago); Jiannan Tian, Jinda Jia, Daoce Wang, Boyuan Zhang (Indiana University); Mingkai Zheng (Rutgers University); Sheng Di (Argonne National Laboratory); Sian Jin (Temple University); Zhao Zhang (Rutgers University); Xiaodong Yu (Stevens Institute of Technology); Kamil A. Iskra, Pete Beckman (Argonne National Laboratory); Guangming Tan, Dingwen Tao (University of Chinese Academy of Sciences)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 17:40–18:00 · Session 5: Deep Neural Networks（主席：Wei Niu）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710852) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出面向二阶优化器的梯度压缩方法 COMPSO，用随机舍入保持精度、过滤微小梯度提高压缩比，并配合 GPU 优化与性能建模确保端到端收益。

## 研究问题

二阶优化器在分布式训练中通信开销很高；直接把一阶方法的梯度压缩用于二阶方法，会出现压缩比低、精度下降或压缩开销过大的问题。

## 方法简述

- 采用随机舍入（stochastic rounding）维持模型精度。
- 过滤幅度较小的梯度，以提升压缩比。
- 针对 GPU 优化压缩过程，并建立性能模型以保证不同系统上的端到端加速。

## 主要结果

- 压缩比达到 22.1×，通信时间降低 14.2×。
- 整体性能提升 1.9×，且模型精度没有任何下降。

<details>
<summary>原文摘要（英文）</summary>

Second-order optimization methods have been developed to enhance convergence and generalization in deep neural network (DNN) training compared to first-order methods like Stochastic Gradient Descent (SGD). However, these methods face challenges in distributed settings due to high communication overhead. Gradient compression, a technique commonly used to accelerate communication for first-order approaches, often results in low communication reduction ratios, decreased model accuracy, and/or high compression overhead when applied to second-order methods. To address these limitations, we introduce a novel gradient compression method for second-order optimizers called COMPSO. This method effectively reduces communication costs while preserving the advantages of second-order optimization. COMPSO employs stochastic rounding to maintain accuracy and filters out minor gradients to improve compression ratios. Additionally, we develop GPU optimizations to minimize compression overhead and performance modeling to ensure end-to-end performance gains across various systems. Evaluation of COMPSO on different DNN models shows that This work is licensed under it achieves a compression ratio of 22.1×, reduces communication time by 14.2×, and improves overall performance by 1.9×, all without any drop in model accuracy.

</details>

---

> 所属 Session：[Session 5: Deep Neural Networks](index.md) · 返回 [PPoPP 2025 总览](../index.md)
