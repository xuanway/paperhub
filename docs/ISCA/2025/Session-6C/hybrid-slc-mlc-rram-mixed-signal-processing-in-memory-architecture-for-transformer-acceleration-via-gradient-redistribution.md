---
title: "Hybrid SLC-MLC RRAM Mixed-Signal Processing-in-Memory Architecture for Transformer Acceleration via Gradient Redistribution"
description: "ISCA 2025 · Session 6C · 混合SLC-MLC RRAM混信号PIM架构：通过梯度重分布实现Transformer加速"
tags:
  - "ISCA2025"
  - "Session 6C"
  - "Memory Acceleration"
---

# Hybrid SLC-MLC RRAM Mixed-Signal Processing-in-Memory Architecture for Transformer Acceleration via Gradient Redistribution

**中文标题：** 混合SLC-MLC RRAM混信号PIM架构：通过梯度重分布实现Transformer加速

**所属 Session：** [Session 6C](index.md) · [ISCA 2025](../index.md)

**作者：** Chang Eun Song, Priyansh Bhatnagar, ZIHAN XIA, Nam Sung Kim, Tajana S Rosing, Mingu Kang

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731109) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Transformers, while revolutionary, face challenges due to their demanding computational cost and large data movement. To ad- dress this, we propose HyFlexPIM, a novel mixed-signal processing- in-memory (PIM) accelerator for inference that flexibly utilizes both single-level cell (SLC) and multi-level cell (MLC) RRAM tech- nologies to trade-off accuracy and efficiency. HyFlexPIM achieves efficient dual-mode operation by utilizing digital PIM for high- precision and write-intensive operations while analog PIM for high parallel and low-precision computations. The analog PIM further distributes tasks between SLC and MLC PIM operations, where a single analog PIM module can be reconfigured to switch between two operations (SLC/MLC) with minimal overhead (<1% for area & energy). Critical weights are allocated to SLC RRAM for high accuracy, while less critical weights are assigned to MLC RRAM to maximize capacity, power, and latency efficiency. However, de- spite employing such a hybrid mechanism, brute-force mapping on hardware fails to deliver significant benefits due to the limited proportion of weights accelerated by the MLC and the noticeable degradation in accuracy. To maximize the potential of our hybrid hardware architecture, we propose an algorithm co-optimization technique, called gradient redistribution, which uses Singular Value Decomposition (SVD) to decompose and truncate matrices based on their importance, then fine-tune them to concentrate signifi- cance into a small subset of weights. By doing so, only 5-10% of the weights have dominantly large gradients, making it favorable for HyFlexPIM by minimizing the use of expensive SLC RRAM while maximizing the efficient MLC RRAM. Our evaluation shows that HyFlexPIM significantly enhances computational throughput and energy efficiency, achieving maximum 1.86×and 1.45×higher than state-of-the-art methods.

## 中文摘要

Transformer虽然带来革命性突破，但算力开销巨大、数据搬运量高。针对该问题，本文提出HyFlexPIM，一款新型混合信号存内计算（PIM）推理加速器，灵活结合单电平单元（SLC）与多电平单元（MLC）阻变存储器（RRAM），在精度和能效之间做权衡。

HyFlexPIM支持双模式高效运算：高精度、写密集型运算采用数字存内计算；高并行、低精度运算采用模拟存内计算。模拟存内计算进一步在SLC和MLC存内运算之间分配任务；单个模拟PIM模块可低开销（面积与功耗开销均小于1%）地在SLC、MLC两种模式之间切换。重要权重存放在SLC RRAM上保证精度，次要权重分配到MLC RRAM，最大化存储容量、降低功耗与延迟。

即便采用该混合架构，如果直接粗暴映射，收益有限：MLC加速的权重占比有限，精度衰减明显。为充分发挥这套混合硬件架构的潜力，本文提出梯度重分配（gradient redistribution）算法协同优化方案：借助奇异值分解（SVD）对矩阵做分解、按重要性裁剪，再微调模型，将重要性集中到一小部分权重上。优化后，仅有5%–10%的权重拥有主导梯度，适配HyFlexPIM：减少高成本SLC RRAM的使用，充分利用高能效MLC RRAM。评测结果表明，HyFlexPIM大幅提升计算吞吐与能效，对比前沿方案，两项指标最高分别提升1.86倍、1.45倍。

## 英文关键词

Processing-In-Memory, LLM, AI Processor, Accelerators, Transformer, Mixed-Signal, RRAM

## 中文关键词

存内计算, 大语言模型, AI处理器, 加速器, Transformer, 混合信号, 阻变存储器

## 代码与研究制品

- [代码仓库](https://github.com/songchangeun96/HyFlexPIM)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731109)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 6C](index.md) · [返回 ISCA 2025](../index.md)
