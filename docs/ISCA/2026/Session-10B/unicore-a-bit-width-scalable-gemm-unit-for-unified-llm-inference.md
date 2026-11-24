---
title: "UniCore: A Bit-Width Scalable GEMM Unit for Unified LLM Inference"
description: "ISCA 2026 · Session 10B · UniCore: A Bit-Width Scalable GEMM Unit for Unified LLM Inference"
tags:
  - "ISCA2026"
  - "Session 10B"
  - "ML Accelerators 2"
---

# UniCore: A Bit-Width Scalable GEMM Unit for Unified LLM Inference

**中文标题：** UniCore: 面向统一 LLM 推理的位宽可扩展 GEMM 单元

**所属 Session：** [Session 10B](index.md) · [ISCA 2026](../index.md)

**作者：** Yonghao Chen, Jiaxiang Zou, Xingyu Chen, Chenxi Xu, Jingyu Guo, Xinyu Chen

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Large Language Models (LLMs) have achieved remarkable success across a broad range of applications but impose extreme computational and memory demands due to their reliance on massive General Matrix–Matrix Multiplication (GEMM) operations. Quantization has emerged as a key approach to improve efficiency by reducing data precision; however, modern LLMs exhibit diverse sensitivities to quantization, requiring multiple precision settings. Existing hardware accelerators fail to efficiently support this diversity: fixed-function accelerators are limited to a few discrete formats, while bit-composable architectures suffer from quadratic resource scaling, leading to severe performance degradation at higher precision. We propose UniCore, a unified GEMM architecture that achieves both bit-width scalability and accuracy preservation through a hardware–software co-design. UniCore introduces Scalable FPMA (S-FPMA), the first composable FPMA primitive that fuses into different precisions using uniform adder slices, maintaining linear hardware scaling. To ensure numerical fidelity, UniCore integrates a lightweight format-conversion and dual-path compensation pipeline that corrects FPMA’s structured approximation error. Complementing the architecture, DynFP, a distribution-adaptive low-bit floating-point format, improves representational accuracy for diverse LLM weight and activation distributions. UniCore delivers 1.24×–3.95× higher area efficiency for W4A4/W4A8/W8A8 and up to 5.26× at W16A16 compared to prior composable-multiplier accelerators, while achieving the highest accuracy in nearly all configurations. UniCore is open-sourced at: https://github.com/CLab-HKUST-GZ/isca53-unicore

## 中文摘要

大型语言模型（LLM）在广泛的应用领域取得了显著成功，但由于其依赖大规模通用矩阵–矩阵乘法（GEMM）运算，因而带来了极高的计算与内存需求。量化已成为通过降低数据精度来提升效率的关键方法；然而，现代 LLM 对量化的敏感度各不相同，需要多种精度设置。现有硬件加速器无法高效支持这种多样性：固定功能加速器仅限少数离散格式，而位可组合（bit-composable）架构则面临资源平方级增长的困境，导致在较高精度时性能严重下降。我们提出 UniCore，一种统一的 GEMM 架构，通过软硬件协同设计同时实现位宽可扩展性与精度保持。UniCore 引入了可扩展 FPMA（S-FPMA），这是首个使用统一加法器切片（uniform adder slices）融合为不同精度的可组合 FPMA 原语，保持线性的硬件扩展。为确保数值保真度，UniCore 集成了轻量级的格式转换与双路径补偿流水线，用于纠正 FPMA 的结构化近似误差。作为对架构的补充，DynFP——一种分布自适应的低位浮点格式——提升了对多样化 LLM 权重与激活分布的表示精度。与先前可组合乘法器加速器相比，UniCore 在 W4A4/W4A8/W8A8 下提供 1.24×–3.95× 更高的面积效率，在 W16A16 下最高达 5.26×，同时在几乎所有配置中取得最高精度。UniCore 已开源于：https://github.com/CLab-HKUST-GZ/isca53-unicore

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：CLab-HKUST-GZ/isca53-unicore](https://github.com/CLab-HKUST-GZ/isca53-unicore)
- [实验材料归档（Zenodo 19449314）](https://zenodo.org/records/19449314)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10B](index.md) · [返回 ISCA 2026](../index.md)
