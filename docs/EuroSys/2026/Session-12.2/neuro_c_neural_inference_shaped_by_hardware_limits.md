---
title: "Neuro-C: Neural Inference Shaped by Hardware Limits"
description: "EuroSys 2026 · Edge Computing, IoT & Embedded AI · Diletta Romano (Uppsala University, Sweden; RISE, Sweden), Luca Mottola (Politec"
tags:
  - "EuroSys2026"
  - "Edge Computing, IoT & Embedded AI"
---

# Neuro-C: Neural Inference Shaped by Hardware Limits

**中文标题：** Neuro-C：受硬件限制塑造的神经推理

**所属 Session：** [Session 12.2: Edge Computing, IoT & Embedded AI](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Edge Computing, IoT & Embedded AI。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Edge Computing, IoT & Embedded AI</p>
</div>

**作者**：Diletta Romano (Uppsala University, Sweden; RISE, Sweden), Luca Mottola (Politecnico di Milano, Italy; RISE, Sweden; Uppsala University, Sweden), Thiemo Voigt (Uppsala University, Sweden; RISE, Sweden)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769380)

## 英文摘要

We present Neuro-centric Networks (Neuro-C), a neural network architecture we design to eliminate multiply-accumulate operations for efficient inference on ultra-low-power microcontrollers (MCUs). Although some MCUs include specialized hardware for neural acceleration, many ultra-low-power MCUs do not, requiring neural networks to align with limited compute and memory resources. Rather than compressing existing models or assuming dedicated hardware, Neuro-C integrates hardware constraints directly into the architecture, effectively shaping the network design around the limitations of the target platform. We shift the computational burden from connections to neurons and encode connectivity with a fixed ternary adjacency matrix, overcoming the bottleneck of matrix multiplications and large weight storage. This design enables a specialized inference kernel implementation that reduces memory usage and latency through pointer-based traversal and sparse dynamic memory allocation, complex control flows, and index decoding logic common in sparse or compressed models. Experimental results show that NeuroC achieves accuracy comparable to or better than standard multilayer perceptrons across multiple datasets, while reducing inference latency and program memory usage by up to 90%. Compared to conventional ternary neural networks, Neuro-C provides improved convergence and accuracy under identical architectural settings, with negligible impact on inference latency.

## 中文摘要

我们提出 Neuro-C（以神经为中心的网络，Neuro-centric Networks），这是一种我们设计的神经网络架构，旨在消除乘加运算，以在超低功耗微控制器（MCU）上实现高效推理。尽管部分 MCU 包含用于神经加速的专用硬件，但许多超低功耗 MCU 并不具备，因而要求神经网络与有限的计算和内存资源相匹配。Neuro-C 并非压缩现有模型或假设专用硬件的存在，而是将硬件约束直接融入架构之中，围绕目标平台的局限有效地塑造网络设计。我们将计算负担从连接转移到神经元，并用固定的三值邻接矩阵编码连接性，从而克服矩阵乘法和大规模权重存储的瓶颈。这一设计使专用的推理内核实现成为可能，它通过基于指针的遍历和稀疏动态内存分配，减少内存占用与延迟，并避开稀疏或压缩模型中常见的复杂控制流与索引解码逻辑。实验结果表明，Neuro-C 在多个数据集上取得与标准多层感知机相当或更好的精度，同时将推理延迟和程序内存占用最多降低 90%。在相同的架构设置下，与传统三值神经网络相比，Neuro-C 提供更好的收敛性和精度，且对推理延迟的影响可忽略不计。

**英文关键词：** TinyML, Embedded Systems, Ultra-Low-Power MCUs,Ternary Neural Networks, Cortex-M0

**中文关键词：** TinyML、嵌入式系统、超低功耗 MCU、三值神经网络、Cortex-M0

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
