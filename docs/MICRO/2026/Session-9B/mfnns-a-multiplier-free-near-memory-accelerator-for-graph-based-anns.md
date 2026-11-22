---
title: "MFNNS: A Multiplier-Free Near-Memory Accelerator for Graph-Based ANNS"
description: "MICRO 2026 · Session 9B · MFNNS：面向基于图的近似最近邻搜索的无乘法器近存加速器"
tags:
  - "MICRO2026"
  - "Near-Memory Computing"
  - "Graph Processing"
---

# MFNNS: A Multiplier-Free Near-Memory Accelerator for Graph-Based ANNS

**中文标题：** MFNNS：面向基于图的近似最近邻搜索的无乘法器近存加速器

**所属 Session：** [Session 9B](index.md) · [MICRO 2026](../index.md)

**作者：** Rui Meng, Yonghao Chen, Jiaxiang Zou, Jingyu Guo, Chenyu Zhang, Xinyu Chen

**来源：** MICRO 2026，pp. 3258–3273；[DOI](https://doi.org/10.1109/MICRO67795.2026.00219)

## 英文摘要

Approximate nearest neighbor search (ANNS) is a key primitive in vector databases, but remains inefficient on CPUs due to high memory traffic and wasted computation on non-nearest candidates. Recent near-memory processing (NMP) accelerators reduce data movement by moving distance evaluation near memory and employ early termination (ET) to prune non-promising candidates. However, they still rely on multiplication-heavy datapaths in both distance evaluation and ET, shifting the bottleneck from memory access to rank-side computation. We present MFNNS, a multiplier-free NMP accelerator for graph-based ANNS. MFNNS is built on two key ideas. First, it leverages floating-point multiplication approximation (FPMA) to replace multiplication in distance evaluation, and further specializes the design for the square-dominated structure of ℓ_2 distance, reducing compensation from a generic 2D table to a compact 1D lookup. Second, it exploits exponent-domain information as a lightweight signal for pruning, and redesigns early termination (ET) as order-preserving screening using sign/exponent metadata. This allows many non-promising candidates to be filtered before full-distance evaluation. MFNNS further co-designs the NMP architecture, data layout, and access policy to expose screening metadata early and reduce unnecessary payload accesses. At 90% recall, MFNNS improves energy efficiency by 5.23× over the CPU baseline and 26.06× over the GPU baseline. Compared with the state-of-the-art NMP accelerator, MFNNS delivers 1.8× higher throughput and 3.18× better area efficiency. MFNNS is open-sourced at https://github.com/CLab-HKUST-GZ/micro59-mfnns.

## 中文摘要

近似最近邻搜索 (ANNS) 是矢量数据库中的一个关键原语，但由于内存流量大和非最近候选的计算浪费，在 CPU 上仍然效率低下。最近的近存处理 (NMP) 加速器通过将距离评估移至内存附近来减少数据移动，并采用提前终止 (ET) 来修剪无前途的候选者。然而，它们在距离评估和 ET 中仍然依赖于大量乘法的数据路径，将瓶颈从内存访问转移到排序端计算。我们推出了 MFNNS，一种用于基于图的 ANNS 的无乘数 NMP 加速器。 MFNNS 建立在两个关键思想之上。首先，它利用浮点乘法近似（FPMA）来代替距离评估中的乘法，并进一步专门设计了ℓ_2距离的平方主导结构，将补偿从通用的2D表减少到紧凑的1D查找。其次，它利用指数域信息作为剪枝的轻量级信号，并使用符号/指数元数据将提前终止（ET）重新设计为保序筛选。这使得许多没有前途的候选人可以在全程评估之前被过滤掉。 MFNNS 进一步共同设计 NMP 架构、数据布局和访问策略，以尽早公开筛选元数据并减少不必要的有效负载访问。在召回率为 90% 时，MFNNS 的能效比 CPU 基准提高了 5.23 倍，比 GPU 基准提高了 26.06 倍。与最先进的 NMP 加速器相比，MFNNS 的吞吐量提高了 1.8 倍，面积效率提高了 3.18 倍。 MFNNS 已开源，网址为 https://github.com/CLab-HKUST-GZ/micro59-mfnns。

## 中文关键词

近似最近邻搜索；无乘法器架构；近存处理；图搜索

## 代码与研究制品

- 代码仓库：[https://github.com/CLab-HKUST-GZ/micro59-mfnns](https://github.com/CLab-HKUST-GZ/micro59-mfnns)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21551985](https://doi.org/10.5281/zenodo.21551985)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9B](index.md) · [MICRO 2026 主页](../index.md)
