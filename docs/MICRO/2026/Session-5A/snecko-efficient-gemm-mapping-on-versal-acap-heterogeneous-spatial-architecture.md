---
title: "SNECKO: Efficient GEMM Mapping on Versal ACAP Heterogeneous Spatial Architecture"
description: "MICRO 2026 · Session 5A · SNECKO：在 Versal ACAP 异构空间架构上实现高效 GEMM 映射"
tags:
  - "MICRO2026"
---

# SNECKO: Efficient GEMM Mapping on Versal ACAP Heterogeneous Spatial Architecture

**中文标题：** SNECKO：在 Versal ACAP 异构空间架构上实现高效 GEMM 映射

**所属 Session：** [Session 5A](index.md) · [MICRO 2026](../index.md)

**作者：** Ilias Papalamprou, Aimilios Leftheriotis, Ioannis Loudaros, George Theodoridis, Francky Catthoor, Dimosthenis Masouros, Dimitrios Soudris

**来源：** MICRO 2026，pp. 1559–1577；[DOI](https://doi.org/10.1109/MICRO67795.2026.00114)

## 英文摘要

Transformer based AI models are increasingly deployed across diverse applications, creating strong demand for high performance and energy efficient execution. Although these models are architecturally diverse, their execution time is dominated by General Matrix Multiplication (GEMM) operations. Spatial accelerators are well suited to these workloads because their architecture can efficiently exploit GEMM parallelism. Among the options available, Versal Adaptive Compute Platform (ACAP) is a strong candidate that integrates AI Engines (AIEs) and programmable logic (PL) in a heterogeneous platform. However, determining the most effective GEMM mapping across these compute substrates remains nontrivial. This challenge is compounded by the need to balance performance and energy efficiency, which prior work often addresses only partially. We present SNECKO, an automated framework for efficient GEMM mapping on Versal ACAP devices. SNECKO combines heterogeneity aware mapping, tiling parameter configuration, and operating frequency adjustment for performance and energy aware GEMM mapping. Driven by ML based surrogate models trained on real experimental data in a two step, data augmented pipeline, SNECKO achieves 8-12% MAPE in latency and power prediction. We evaluate SNECKO on the Versal VCK190, demonstrating geomean improvements of 1.38x (up to 2.73x) in throughput, 1.24x (up to 2.27x) in energy efficiency, and 1.44x (up to 4.59x) in Energy Delay Product over state of the art approaches. Additionally, SNECKO achieves on average 1.17x-2.11x higher throughput than embedded GPUs while achieving 1.18x higher energy efficiency than server grade GPUs.

## 中文摘要

基于 Transformer 的人工智能模型越来越多地部署在各种应用中，对高性能和节能执行产生了强烈需求。尽管这些模型在架构上各不相同，但它们的执行时间主要由通用矩阵乘法（GEMM）运算主导。空间加速器非常适合这些工作负载，因为它们的架构可以有效地利用 GEMM 并行性。在可用的选项中，Versal 自适应计算平台 (ACAP) 是将人工智能引擎 (AIE) 和可编程逻辑 (PL) 集成在异构平台中的有力候选者。然而，确定这些计算基底上最有效的 GEMM 映射仍然很重要。由于需要平衡性能和能效，这一挑战变得更加复杂，而之前的工作通常只能部分解决这一问题。我们推出 SNECKO，这是一种自动化框架，用于在 Versal ACAP 设备上进行高效 GEMM 映射。 SNECKO 结合了异构感知映射、平铺参数配置和操作频率调整，以实现性能和能源感知 GEMM 映射。在基于 ML 的代理模型的驱动下，SNECKO 在两步数据增强管道中对真实实验数据进行了训练，在时延和功率预测方面实现了 8-12% MAPE。我们在 Versal VCK190 上评估 SNECKO，结果表明与最先进的方法相比，吞吐量提高了 1.38 倍（高达 2.73 倍），能效提高了 1.24 倍（高达 2.27 倍），能量时延积提高了 1.44 倍（高达 4.59 倍）。此外，SNECKO 的吞吐量平均比嵌入式 GPU 高 1.17 倍至 2.11 倍，同时能效比服务器级 GPU 高 1.18 倍。

## 中文关键词

矩阵乘法映射；Versal ACAP；异构空间架构；数据流优化

## 代码与研究制品

- 代码仓库：[https://github.com/ipapal/SNECKO](https://github.com/ipapal/SNECKO)（论文提供的地址；2026-11-10 检查返回 HTTP 404）
- 研究制品归档：[https://zenodo.org/records/22712407](https://zenodo.org/records/22712407)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 5A](index.md) · [MICRO 2026 主页](../index.md)
