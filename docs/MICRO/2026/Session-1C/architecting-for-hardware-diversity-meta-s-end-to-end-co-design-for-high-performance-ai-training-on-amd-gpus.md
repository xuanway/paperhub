---
title: "Architecting for Hardware Diversity: Meta's End-to-End Co-Design for High-Performance AI Training on AMD GPUs"
description: "MICRO 2026 · Session 1C · 面向硬件多样性的架构设计：Meta 在 AMD GPU 上实现高性能 AI 训练的端到端协同设计"
tags:
  - "MICRO2026"
  - "GPU"
  - "HW-SW Co-design"
---

# Architecting for Hardware Diversity: Meta's End-to-End Co-Design for High-Performance AI Training on AMD GPUs

**中文标题：** 面向硬件多样性的架构设计：Meta 在 AMD GPU 上实现高性能 AI 训练的端到端协同设计

**所属 Session：** [Session 1C](index.md) · [MICRO 2026](../index.md)

**作者：** Haoyu Zhang, Arshad Rahman, Adnan Aziz, Ajith Prabhudev, Amin Farmahini, Ben Rhoads, Benson Ma, Brian Shi, Cen Zhao, CK Luk, Dingming Wu, Emad El-Haraty, Eric Chen, Frank Li, Gary Huang, Gefei Zuo, Haoran Zhang, Hiwot Kassa, Hongyi Zeng, Jack Taylor, Jeremy Hadidjojo, John Donati, Jonathan Sheffield, Julio Machado Silva, Karthik Ganesan, Kent Russell, KR Kishore, Lei Tian, Liu Ke, Muhammad Osama, Peng Chen, Rakesh Hemnani, Ryan Swann, Saleel Kudchadker, Shankar Yanamandram, Shobhit Kanaujia, Shucai Xiao, Srinath Bayareddy, Srinivas Vaidyanathan, Sudharssun Subramanian, Supadchaya Puangpontip, Taylor Robie, Tianhao Huang, Tyler Hart, Viswesh Sankaran, Weijun Jiang, Wenkai Du, Xiaodong Wang, Xiaohu Guo, Yao Rong, Yinbin Ma, Yue Dong, Yuzhen Huang, Yvonne Liu, Zhan Shu, Dan Rabinovitsj, Ajit Mathews, Chunqiang Tang

**来源：** MICRO 2026，pp. 237–252；[DOI](https://doi.org/10.1109/MICRO67795.2026.00032)

## 英文摘要

Meta deploys a heterogeneous fleet comprising NVIDIA GPUs, AMD GPUs, and proprietary MTIA accelerators to reduce costs and mitigate vendor lock-in. However, the extensive history of NVIDIA-specific optimizations hinders performance portability to other hardware. This paper presents our methods for optimizing alternative accelerators, using AMD Instinct MI350X versus NVIDIA B200 for recommendation model training as a case study. We propose three reusable principles. First, hardware-model co-design is essential: rather than directly porting models from NVIDIA GPUs, revising model structures and software recipes allows full exploitation of accelerator-specific strengths (e.g., MI350X's 1.6× HBM capacity relative to B200). Second, our analytical performance model enables zero-warmup optimal kernel selection across diverse datatypes and matrix shapes in production models, drastically simplifying tuning. Third, increasingly mature agentic workflows have lowered the barrier to porting from the CUDA ecosystem; we extend these workflows for microarchitecture-aware kernel optimizations and custom shim generation. Compared to the directly ported baseline, these methods deliver up to 1.5× improvement in end-to-end training throughput. To our knowledge, this is the first hyperscaler report on productionizing AMD GPUs for large-scale training. Our contributions have been upstreamed to the open-source PyTorch, Triton, and ROCm ecosystems.

## 中文摘要

Meta 部署了由 NVIDIA GPU、AMD GPU 和专有 MTIA 加速器组成的异构队列，以降低成本并缓解供应商锁定。然而，NVIDIA 特定优化的悠久历史阻碍了向其他硬件的性能可移植性。本文介绍了我们优化替代加速器的方法，并使用 AMD Instinct MI350X 与 NVIDIA B200 进行推荐模型训练作为案例研究。我们提出了三个可重用原则。首先，硬件模型协同设计至关重要：不是直接从 NVIDIA GPU 移植模型，而是修改模型结构和软件配方，可以充分利用加速器特定的优势（例如，MI350X 相对于 B200 的 1.6 倍 HBM 容量）。其次，我们的分析性能模型可以在生产模型中跨不同数据类型和矩阵形状进行零预热最佳内核选择，从而大大简化了调整。第三，日益成熟的代理工作流程降低了从CUDA生态系统移植的门槛；我们扩展了这些工作流程，以实现微架构感知的内核优化和自定义填充程序生成。与直接移植的基线相比，这些方法将端到端训练吞吐量提高了 1.5 倍。据我们所知，这是第一份关于生产 AMD GPU 用于大规模训练的超大规模报告。我们的贡献已上游到开源 PyTorch、Triton 和 ROCm 生态系统。

## 中文关键词

加速器；深度学习推荐模型；图形处理器；GPU 内核；机器学习；推荐系统

## 代码与研究制品

论文称相关贡献已合入开源 PyTorch、Triton 与 ROCm 生态，但未提供本文独立仓库或具体提交链接。可从以下上游项目查阅：

- [PyTorch](https://github.com/pytorch/pytorch)
- [Triton](https://github.com/triton-lang/triton)
- [ROCm](https://github.com/ROCm/ROCm)

[返回 Session 1C](index.md) · [MICRO 2026 主页](../index.md)
