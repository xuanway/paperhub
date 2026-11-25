---
title: "Scaling LLM Test-Time Compute with Mobile NPU on Smartphones"
description: "EuroSys 2026 · On-Device & Federated Learning · Zixu Hao (Tsinghua University), Jianyu Wei (University of Science and Technology"
tags:
  - "EuroSys2026"
  - "On-Device & Federated Learning"
---

# Scaling LLM Test-Time Compute with Mobile NPU on Smartphones

**中文标题：** 在智能手机上利用移动 NPU 扩展 LLM 测试时计算

**所属 Session：** [Session 4.1: On-Device & Federated Learning](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：On-Device & Federated Learning。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · On-Device & Federated Learning</p>
</div>

**作者**：Zixu Hao (Tsinghua University), Jianyu Wei (University of Science and Technology of China), Tuowei Wang (Tsinghua University), Minxing Huang (Tsinghua University), Huiqiang Jiang (Microsoft Research), Shiqi Jiang (Microsoft Research), Ting Cao (Institute for AI Industry Research (AIR), Tsinghua University), Ju Ren (Tsinghua University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769382)

## 英文摘要

Deploying Large Language Models (LLMs) on mobile devices faces the challenge of insufficient performance in smaller models and excessive resource consumption in larger ones. This paper highlights that mobile Neural Processing Units (NPUs) have underutilized computational resources, particularly their matrix multiplication units, during typical LLM inference. To leverage this wasted compute capacity, we propose applying parallel test-time scaling techniques on mobile NPUs to enhance the performance of smaller LLMs. However, this approach confronts inherent NPU challenges, including inadequate hardware support for fine-grained quantization and low efficiency in general-purpose computations. To overcome these, we introduce two key techniques: a hardware-aware tile quantization scheme that aligns group quantization with NPU memory access patterns, and efficient LUT-based replacements for complex operations such as Softmax and dequantization. We design and implement an end-to-end inference system that leverages the NPU’s compute capability to support test-time scaling on Qualcomm Snapdragon platforms. Experiments show our approach brings significant speedups: up to 19.0× for mixed-precision GEMM and 2.2× for Softmax. More importantly, we demonstrate that smaller models using test-time scaling can match or exceed the accuracy of larger models, achieving a new performance-cost Pareto frontier.

## 中文摘要

在移动设备上部署大语言模型（LLM）面临两难：较小模型性能不足，较大模型资源消耗过高。本文指出，在典型 LLM 推理过程中，移动神经网络处理器（NPU）的计算资源（尤其是其矩阵乘法单元）存在利用不足的问题。为利用这部分被浪费的算力，我们提出在移动 NPU 上应用并行测试时扩展技术，以提升较小 LLM 的性能。然而，该方法面临 NPU 固有的挑战，包括对细粒度量化的硬件支持不足，以及通用计算效率偏低。为克服这些挑战，我们引入两项关键技术：一种硬件感知的分块量化方案，使分组量化与 NPU 内存访问模式对齐；以及针对 Softmax 与反量化等复杂操作的高效 LUT 替代实现。我们设计并实现了一套端到端推理系统，利用 NPU 的算力在高通骁龙平台上支持测试时扩展。实验表明，我们的方法带来显著加速：混合精度 GEMM 最高 19.0×，Softmax 最高 2.2×。更重要的是，我们证明了采用测试时扩展的较小模型可以匹配甚至超过较大模型的准确率，达到新的性能-成本帕累托前沿。

**英文关键词：** Neural Processing Unit, mobile device, Large Language Model

**中文关键词：** 神经网络处理器、移动设备、大语言模型

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
