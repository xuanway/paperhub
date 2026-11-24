---
title: "Bringing Near Data Processing into the Low-Bit Floating-Point Era"
description: "ISCA 2026 · Session 6B · Bringing Near Data Processing into the Low-Bit Floating-Point Era"
tags:
  - "ISCA2026"
  - "Session 6B"
  - "Deep Learning / Memory Acceleration"
---

# Bringing Near Data Processing into the Low-Bit Floating-Point Era

**中文标题：** 将近数据处理带入低比特浮点时代

**所属 Session：** [Session 6B](index.md) · [ISCA 2026](../index.md)

**作者：** Tongxin Xie, Mingyu Gao, Zehao Wang, Zhihao Jia, Yuechen Xi, Bing Li, Mo Guang, Jiale Yan, Kaiwen Long, Xingcheng Zhang, Huazhong Yang, Yuan Xie, Zhenhua Zhu, Yu Wang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Near data processing (NDP) based on DRAM has emerged to be a promising solution to the “memory wall” problem of machine learning models. From the algorithmic perspective, group-wise low-bit floating-point (FP) quantization has become an important trend for both efficient training and inference. Integrating low-bit FP quantization into NDP also notably shrinks the memory footprint of large models, alleviating the memory-capacity constraints of NDP architectures. However, existing NDP compilers struggle to support efficient low-bit FP computation on NDP. First, different quantization configurations exhibit different preferences for NDP compilation strategies. Second, the fine-grained grouping leads to frequent switching between quantized value access and group scale access during computation, increasing the DRAM row-buffer miss rate. Third, fine-grained grouping triggers frequent high-precision dequantization operations, causing significant latency overhead. To address these challenges, this paper proposes FlexQ-NDP, an NDP compiler tailored for general low-bit FP computation. Firstly, we develop an open-source simulation framework to model the low-bit FP computation overhead on NDP. Secondly, we design a scale-value interleaved FP layout, effectively reducing DRAM row-changing overhead. Thirdly, we propose a dequantization-hiding technique based on instruction reordering to reduce the DRAM idle time induced by frequent dequantization operations. Finally, we develop a lightweight compilation-space pruning and search strategy to enable efficient low-bit FP computation on NDP. Extensive experiments show that FlexQ-NDP achieves up to 3.29× speedup over existing compilation strategies on various low-bit FP quantization configurations.

## 中文摘要

基于 DRAM 的近数据处理（NDP）已成为解决机器学习模型“内存墙”问题的有前景方案。从算法角度看，分组低比特浮点（FP）量化已成为高效训练与推理的重要趋势。将低比特 FP 量化集成到 NDP 中还能显著缩小大模型的内存足迹，缓解 NDP 架构的存储容量约束。然而，现有 NDP 编译器难以在 NDP 上支持高效的低比特 FP 计算。首先，不同的量化配置对 NDP 编译策略有不同的偏好。其次，细粒度分组导致计算过程中量化值访问与组缩放因子访问之间频繁切换，增加 DRAM 行缓冲区缺失率。第三，细粒度分组触发频繁的高精度反量化操作，造成显著的延迟开销。为应对这些挑战，本文提出 FlexQ-NDP，一个面向通用低比特 FP 计算定制的 NDP 编译器。首先，我们开发了一个开源仿真框架来建模 NDP 上的低比特 FP 计算开销。其次，我们设计了缩放因子与数值交错的 FP 布局，有效降低 DRAM 换行开销。第三，我们提出基于指令重排的反量化隐藏技术，以减少频繁反量化操作引起的 DRAM 空闲时间。最后，我们开发了轻量级的编译空间剪枝与搜索策略，以在 NDP 上实现高效的低比特 FP 计算。大量实验表明，在各种低比特 FP 量化配置下，FlexQ-NDP 相比现有编译策略最高实现 3.29 倍加速。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：thu-nics/flexq_ndp](https://github.com/thu-nics/flexq_ndp)
- [实验材料归档（Zenodo 19452117）](https://zenodo.org/records/19452117)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6B](index.md) · [返回 ISCA 2026](../index.md)
