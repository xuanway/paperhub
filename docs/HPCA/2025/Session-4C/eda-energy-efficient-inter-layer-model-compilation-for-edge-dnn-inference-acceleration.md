---
title: "EDA: Energy-Efficient Inter-Layer Model Compilation for Edge DNN Inference Acceleration"
description: "HPCA 2025 · Stacking the Layers"
tags:
  - "HPCA2025"
  - "Stacking the Layers"
---

# EDA: Energy-Efficient Inter-Layer Model Compilation for Edge DNN Inference Acceleration

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stacking the Layers。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stacking the Layers</p>
</div>

**论文链接**：
**作者**：Bo Ren Pao (National Yang Ming Chiao Tung University), I-Chia Chen (National Yang Ming Chiao Tung University), En-Hao Chang (Google), Tsung Tai Yeh (National Yang Ming Chiao Tung University)
**会议**：HPCA 2025

---

## 中文标题

EDA：面向边缘 DNN 推理加速的高能效层间模型编译

## 英文摘要

Modern handheld devices often employ neural processing units (NPUs) to accelerate deep neural network (DNN) inference applications. Unlike the AI accelerator of a data center, the NPU of an edge device has strict price and energy budgets. In an NPU, DRAM memory consumes much energy due to frequent data movement across on-chip and off-chip memory. The inter-layer operator scheduling has been shown to reduce off-chip memory transactions by reusing DNN operator outputs on the on-chip memory space. However, it often deeply traverses operators and substantially increases off-chip memory data traffic when the on-chip memory of an NPU decreases in size. Consequently, this work creates a DNN model compilation framework called EDA that transparently improves the energy efficiency of an NPU by adjusting the operator traversal depth of the inter-layer operator scheduling in a stacked DNN model. First, EDA transforms a DNN model into a tensor-splitting model. Second, EDA breaks the tensor-splitting model graph into multiple subgraphs. Third, the EDA inter-layer cost model quickly determines the depth of each subgraph. Fourth, EDA properly manages the on-chip shared memory space of an NPU to avoid overusing memory space. Finally, EDA devises the operator grouping method to improve the MAC unit and on-chip memory space utilization. EDA improves the geometric means of 2.08× and 2.39×, respectively, in energy efficiency and performance over the NPU with designated memory buffers.

## 中文摘要

现代手持设备常用神经网络处理单元（NPU）加速深度神经网络（DNN）推理应用。与数据中心的 AI 加速器不同，边缘设备的 NPU 有严格的价格与能耗预算。在 NPU 中，由于数据在片上与片外存储间频繁移动，DRAM 消耗大量能量。层间算子调度已被证明可通过在片上存储空间复用 DNN 算子输出来减少片外访存，但当 NPU 片上存储变小时，它往往深度遍历算子并显著增加片外访存数据量。为此本文构建了名为 EDA 的 DNN 模型编译框架，通过调整堆叠 DNN 模型中层间算子调度的算子遍历深度，透明地提升 NPU 的能效。首先 EDA 将 DNN 模型转换为张量拆分模型；其次把张量拆分模型图分解为多个子图；第三，EDA 层间代价模型快速确定每个子图的深度；第四，EDA 合理管理 NPU 的片上共享存储空间以避免过度占用；最后 EDA 设计算子分组方法以提升 MAC 单元与片上存储空间利用率。相比具有指定存储缓冲的 NPU，EDA 在能效与性能上分别取得 2.08× 和 2.39× 的几何平均提升。
