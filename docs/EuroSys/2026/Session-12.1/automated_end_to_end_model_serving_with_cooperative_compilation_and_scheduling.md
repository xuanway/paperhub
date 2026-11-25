---
title: "Automated End-to-End Model Serving with Cooperative Compilation and Scheduling"
description: "EuroSys 2026 · ML Model Optimization: Compilers, Quantization & Fine-Tuning · Yikang Zhang (Nanjing University), Junlong Chen (Nanjing University), Wei Wang ("
tags:
  - "EuroSys2026"
  - "ML Model Optimization: Compilers, Quantization & Fine-Tuning"
---

# Automated End-to-End Model Serving with Cooperative Compilation and Scheduling

**中文标题：** 基于协同编译与调度的自动化端到端模型服务

**所属 Session：** [Session 12.1: ML Model Optimization: Compilers, Quantization & Fine-Tuning](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：ML Model Optimization: Compilers, Quantization & Fine-Tuning。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · ML Model Optimization: Compilers, Quantization & Fine-Tuning</p>
</div>

**作者**：Yikang Zhang (Nanjing University), Junlong Chen (Nanjing University), Wei Wang (Nanjing University), Jia Liu (Nanjing University), Nan Hu (Hunan University), Haipeng Dai (Nanjing University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769392)

## 英文摘要

Model serving systems are critical for deep learning inference, managing GPU infrastructure to deliver end-to-end services. Current frameworks typically treat operators as basic compilation and scheduling units, which often fail to maximize GPU utilization due to hardware-unfriendly kernels and coarse-grained scheduling. To address these limitations, we propose a cooperative compilation and scheduling scheme that statically generates multiple kernel variants and dynamically schedules them based on runtime context. We present Infera, a high-performance model serving system that implements this approach. Experimental results demonstrate that Infera improves inference throughput by at least 1.6× compared to state-of-the-art baselines.

## 中文摘要

模型服务系统对深度学习推理至关重要，它管理GPU基础设施以提供端到端服务。当前框架通常将算子作为基本的编译与调度单元，这常常因对硬件不友好的内核和粗粒度调度而无法最大化GPU利用率。为解决这些局限，我们提出一种协同编译与调度方案，静态生成多种内核变体，并根据运行时上下文动态调度它们。我们提出Infera，一个实现该方案的高性能模型服务系统。实验结果表明，与最先进的基线相比，Infera将推理吞吐量至少提升1.6倍。

**英文关键词：** Deep Learning Compiler, Model Serving System, High Performance Computing

**中文关键词：** 深度学习编译器、模型服务系统、高性能计算

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
