---
title: "HeteroReason: Heterogeneous FPGA-GPU Acceleration for Disaggregated Speculative Reasoning"
description: "MICRO 2026 · Session 9A · HeteroReason：面向分离式推测推理的 FPGA-GPU 异构加速"
tags:
  - "MICRO2026"
  - "GPU"
  - "FPGA"
---

# HeteroReason: Heterogeneous FPGA-GPU Acceleration for Disaggregated Speculative Reasoning

**中文标题：** HeteroReason：面向分离式推测推理的 FPGA-GPU 异构加速

**所属 Session：** [Session 9A](index.md) · [MICRO 2026](../index.md)

**作者：** Zehuan Zhang, Quan Deng, Zhibo Ren, Hao Mark Chen, Guoyu Li, Xuchun Hu, Jose G. F. Coutinho, Ce Guo, Wayne Luk, Zhiqiang Que, Hongxiang Fan

**来源：** MICRO 2026，pp. 3195–3209；[DOI](https://doi.org/10.1109/MICRO67795.2026.00215)

## 英文摘要

Models (LRMs) have achieved state-of-the-art performance in reasoning tasks by utilizing Chain-of-Thought (CoT) reasoning. To achieve fast execution speed, speculative reasoning techniques have been introduced in prior work, which adopt a lightweight draft model for candidate token generation followed by process reward models (PRMs) for verification and a strong target model for refinements. This paper identifies that the existing speculative reasoning paradigm follows a strictly forward-only reasoning trajectory, which lacks robustness and can lead to severe error propagation if early reasoning steps are suboptimal. Furthermore, executing these disparate inference schemes, including sequential drafting and parallel verification on homogeneous GPU platforms, can lead to severe resource underutilization. To address this, we propose HeteroReason, an algorithm-hardware co-designed heterogeneous FPGA-GPU inference paradigm specifically tailored for LRM speculative reasoning. At the algorithmic level, we introduce a backtracking-enhanced workflow that enables the system to recover from low-quality states and explore alternative reasoning trajectories, significantly improving reasoning robustness. At the system level, the draft model is offloaded to the FPGA while deploying the PRM and target models on GPUs. A specialized workflow is optimized to achieve prefill-decode disaggregation, which exploits shadow synchronization to overlap GPU-side refinements with FPGA-side token updates to effectively hide synchronization latency. To mitigate inherent sequential constraints, we propose a step-ahead speculation and refinement scheduling scheme, transitioning the system from a sequential execution scheme to a parallel pipeline. Experimental evaluations demonstrate that the backtracking mechanism achieves an average reasoning accuracy improvement of up to 4.2% across diverse reasoning benchmarks. Moreover, built on the heterogeneous platforms consisting of AMD U280 or V80 FPGAs, with NVIDIA GeForce RTX 3090 GPU platforms, HeteroReason achieves 1.01x-1.42x latency speedups and 1.25x-1.57x improvements in energy efficiency under different model configurations, compared to homogeneous GPU baselines.

## 中文摘要

模型 (LRM) 通过利用思想链 (CoT) 推理，在推理任务中取得了最先进的性能。为了实现快速执行速度，先前的工作中引入了推测推理技术，采用轻量级草案模型来生成候选词元，然后采用过程奖励模型（PRM）进行验证，并采用强大的目标模型进行细化。本文指出，现有的推测推理范式遵循严格的仅前向推理轨迹，缺乏鲁棒性，如果早期推理步骤不理想，可能会导致严重的错误传播。此外，在同构 GPU 平台上执行这些不同的推理方案（包括顺序起草和并行验证）可能会导致严重的资源利用不足。为了解决这个问题，我们提出了 HeteroReason，这是一种算法-硬件共同设计的异构 FPGA-GPU 推理范式，专为 LRM 推测推理量身定制。在算法层面，我们引入了回溯增强的工作流程，使系统能够从低质量状态中恢复并探索替代推理轨迹，显着提高推理的鲁棒性。在系统层面，草稿模型被卸载到 FPGA，同时在 GPU 上部署 PRM 和目标模型。专门的工作流程经过优化，可实现预填充解码分解，利用影子同步将 GPU 端细化与 FPGA 端词元更新重叠，从而有效隐藏同步时延。为了减轻固有的顺序约束，我们提出了一种超前推测和细化调度方案，将系统从顺序执行方案转变为并行管道。实验评估表明，回溯机制在不同的推理基准上实现了高达 4.2% 的平均推理精度提升。此外，HeteroReason 构建在由 AMD U280 或 V80 FPGA 组成的异构平台上，搭配 NVIDIA GeForce RTX 3090 GPU 平台，与同构 GPU 基准相比，在不同模型配置下实现了 1.01 倍至 1.42 倍的时延加速和 1.25 倍至 1.57 倍的能效提升。

## 中文关键词

大型推理模型；推测推理；异构计算；算法与硬件协同设计；FPGA-GPU 协同

## 代码与研究制品

- 代码仓库：[https://github.com/zehuanzhang/HeteroReason](https://github.com/zehuanzhang/HeteroReason)
- 研究制品归档：[https://zenodo.org/records/22015981](https://zenodo.org/records/22015981)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9A](index.md) · [MICRO 2026 主页](../index.md)
