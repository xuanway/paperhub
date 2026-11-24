---
title: "DIAMoND: Dynamic Inference for Adaptive Edge MoE with Heterogeneous In-NAND and Near-DRAM Compute Architecture"
description: "ISCA 2026 · Session 5A · DIAMoND: Dynamic Inference for Adaptive Edge MoE with Heterogeneous In-NAND and Near-DRAM Compute Architecture"
tags:
  - "ISCA2026"
  - "Session 5A"
  - "LLM 3"
---

# DIAMoND: Dynamic Inference for Adaptive Edge MoE with Heterogeneous In-NAND and Near-DRAM Compute Architecture

**中文标题：** DIAMoND: 面向异构 NAND 内与近 DRAM 计算架构的自适应边缘 MoE 动态推理

**所属 Session：** [Session 5A](index.md) · [ISCA 2026](../index.md)

**作者：** Ling Liang, Tianyang Luo, Shuzhang Zhong, Dongxue Zhao, Qichao Ma, Renjie Wei, Jingyu Wang, Meng Li, Guangyu Sun, Zongwei Wang, Yimao Cai

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Among modern large language models (LLMs), the Mixture-of-Experts (MoE) model stands out as a promising approach. Although MoE models activate only small portions of experts during inference, the full model size can reach 50∼100GB, posing challenges for the memory capacity of edge devices. Additionally, single-batch decoding in edge applications places significant memory bandwidth demands for parameter loading, and the dynamic expert selection in MoE models further complicates loading patterns. Previous studies have explored using NAND-Flash-based SSD to provide the large storage capacity needed for holding LLM parameters. However, the performance of near-NAND computing remains limited by the memory data transfer rate, and these studies lack designs to accommodate the complex execution flow of MoE models. To fully release the computational capacity on the memory side while considering memory characteristics, we introduce DIAMoND, a heterogeneous accelerator that integrates in-NAND and near-DRAM computing via a 2.5D package to support all operations in MoE inference efficiently. To address mismatches between varying matrix sizes and the fixed NAND array size, we propose a mask-based mapping method under in-NAND computing. Finally, a dynamic online expert selection scheme based on in-NAND computing is proposed to enhance MoE inference efficiency. Overall, our proposed architecture enables the edge inference of Mixtral-8x7B at a speed of 197.3 tokens/s and a peak energy efficiency of 5.8 tokens/J, with the speed being 9.7× and 2.6∼11.7× better than GPU and ASIC LLM edge accelerators.

## 中文摘要

在现代大语言模型（LLM）中，混合专家（MoE）模型作为一种颇具前景的方案脱颖而出。尽管 MoE 模型在推理时仅激活一小部分专家，但完整模型大小可达 50∼100GB，对边缘设备的存储容量构成挑战。此外，边缘应用中的单批解码对参数加载提出了很高的内存带宽需求，而 MoE 模型中动态的专家选择又进一步使加载模式复杂化。已有研究探索使用基于 NAND Flash 的 SSD 来提供容纳 LLM 参数所需的大容量存储。然而，近 NAND 计算的性能仍受限于存储数据传输速率，且这些研究缺乏适配 MoE 模型复杂执行流程的设计。为在兼顾存储特性的同时充分释放存储侧的计算能力，我们提出 DIAMoND——一种通过 2.5D 封装集成 NAND 内计算与近 DRAM 计算的异构加速器，可高效支持 MoE 推理中的所有操作。针对变化的矩阵尺寸与固定 NAND 阵列尺寸之间的不匹配，我们提出了 NAND 内计算下的掩码式映射方法。最后，我们提出了一种基于 NAND 内计算的动态在线专家选择方案，以提升 MoE 推理效率。总体而言，我们提出的架构使 Mixtral-8x7B 的边缘推理速度达到 197.3 tokens/s、峰值能效达 5.8 tokens/J，其速度分别是 GPU 和 ASIC LLM 边缘加速器的 9.7× 和 2.6∼11.7×。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5A](index.md) · [返回 ISCA 2026](../index.md)
