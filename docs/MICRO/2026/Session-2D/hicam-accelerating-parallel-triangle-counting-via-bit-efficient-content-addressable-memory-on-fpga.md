---
title: "HiCAM: Accelerating Parallel Triangle Counting via Bit-Efficient Content Addressable Memory on FPGA"
description: "MICRO 2026 · Session 2D · HiCAM：通过 FPGA 上的比特高效内容寻址存储器加速并行三角形计数"
tags:
  - "MICRO2026"
  - "FPGA"
---

# HiCAM: Accelerating Parallel Triangle Counting via Bit-Efficient Content Addressable Memory on FPGA

**中文标题：** HiCAM：通过 FPGA 上的比特高效内容寻址存储器加速并行三角形计数

**所属 Session：** [Session 2D](index.md) · [MICRO 2026](../index.md)

**作者：** Yao Chen, Feng Yu, Hongshi Tan, Weng-Fai Wong, Bingsheng He, Xuanhua Shi, Hai Jin

**来源：** MICRO 2026，pp. 803–817；[DOI](https://doi.org/10.1109/MICRO67795.2026.00067)

## 英文摘要

Triangle counting is a fundamental primitive in large-scale graph analytics, yet its execution is bottlenecked by irregular memory access patterns and limited parallelism on conventional architectures. Prior FPGA-based CAM accelerators decouple data representation from matching semantics, wasting on-chip resources and requiring decompression before search. We present HiCAM, a software-hardware co-designed FPGA overlay that unifies graph data compression and associative matching into a single compressed-domain pipeline. HiCAM introduces a parameterizable locality-aware tuple encoding that packs multiple sorted vertex IDs into fixed-width entries aligned with the DSP datapath, and co-designs a bit-efficient CAM cell that searches compressed tuples directly, without runtime decompression. To handle the skewed degree distributions of real-world graphs, HiCAM employs run-time adaptive CAM grouping that trades parallelism for storage depth on a per-vertex basis, and a two-level memory-channel-aware partitioning framework for balanced multi-channel execution. Experimental results on a diverse suite of real-world datasets demonstrate that HiCAM achieves up to 10.6x speedup and 5.8x energy reduction over state-of-the-art FPGA baselines, and outperforms optimized 32-core CPU solutions by up to 3.8x in speed and 9.0x in energy efficiency. The HiCAM code is open-sourced at https://github.com/Xtra-Computing/HiCAM.

## 中文摘要

三角形计数是大规模图形分析中的基本原语，但其执行受到不规则内存访问模式和传统架构上有限并行性的瓶颈。先前基于 FPGA 的 CAM 加速器将数据表示与匹配语义分离，浪费了片上资源并且需要在搜索之前解压缩。我们推出了 HiCAM，这是一种软件-硬件共同设计的 FPGA 叠加层，它将图形数据压缩和关联匹配统一到单个压缩域管道中。 HiCAM 引入了可参数化的局部感知元组编码，将多个排序的顶点 ID 打包到与 DSP 数据路径对齐的固定宽度条目中，并共同设计了一个位高效的 CAM 单元，可直接搜索压缩元组，无需运行时解压缩。为了处理现实世界图的倾斜程度分布，HiCAM 采用运行时自适应 CAM 分组，以每个顶点为基础以并行性换取存储深度，并采用两级内存通道感知分区框架来平衡多通道执行。在各种真实世界数据集上进行的实验结果表明，与最先进的 FPGA 基准相比，HiCAM 的速度提高了 10.6 倍，能耗降低了 5.8 倍，并且速度比优化的 32 核 CPU 解决方案高出 3.8 倍，能效提高了 9.0 倍。 HiCAM 代码在 https://github.com/Xtra-Computing/HiCAM 上开源。

## 中文关键词

图处理；三角形计数；现场可编程门阵列；内容寻址存储器；软硬件协同设计

## 代码与研究制品

- 代码仓库：[https://github.com/Xtra-Computing/HiCAM](https://github.com/Xtra-Computing/HiCAM)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21536137](https://doi.org/10.5281/zenodo.21536137)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2D](index.md) · [MICRO 2026 主页](../index.md)
