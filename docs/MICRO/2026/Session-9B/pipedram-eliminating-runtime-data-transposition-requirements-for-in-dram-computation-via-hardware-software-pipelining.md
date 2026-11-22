---
title: "PipeDRAM: Eliminating Runtime Data Transposition Requirements for In-DRAM Computation via Hardware/Software Pipelining"
description: "MICRO 2026 · Session 9B · PipeDRAM：通过软硬件流水线消除 DRAM 内计算的运行时数据转置需求"
tags:
  - "MICRO2026"
  - "DRAM"
---

# PipeDRAM: Eliminating Runtime Data Transposition Requirements for In-DRAM Computation via Hardware/Software Pipelining

**中文标题：** PipeDRAM：通过软硬件流水线消除 DRAM 内计算的运行时数据转置需求

**所属 Session：** [Session 9B](index.md) · [MICRO 2026](../index.md)

**作者：** Geraldo F. Oliveira, Ataberk Olgun, Ismail Emir Yüksel, F. Nisa Bostancı, Pedro H. E. Becker, Mohammad Sadrosadati, Saugata Ghose, Juan Gómez-Luna, Onur Mutlu

**来源：** MICRO 2026，pp. 3274–3296；[DOI](https://doi.org/10.1109/MICRO67795.2026.00220)

## 英文摘要

Processing-using-DRAM (PUD) architectures exploit the ana-log operational properties of DRAM to perform bulk bitwise Boolean and arithmetic operations inside memory arrays by organizing data in a vertical layout, where operand bits are stacked along DRAM columns. However, modern computing systems natively employ a horizontal data layout that pre-serves the cache line abstraction, leverages spatial locality in row buffers, and enables high memory throughput. This fundamental mismatch forces existing PUD architectures to frequently perform data layout transformations between horizontal and vertical formats, incurring significant performance, energy, and system integration overheads. Our goal is to eliminate data transposition overheads in PUD systems at low cost. To this end, we propose PipeDRAM, a PUD architecture that eliminates the need for runtime data layout transformation, enabling PUD operations directly over horizontally laid-out data. PipeDRAM's key ideas are to (i) deterministically reorganize bits inside each memory request to enable a PUD-friendly data placement within a DRAM array in a horizontal data layout, and (ii) employ a pipeline-based execution model that overlaps bit-dependent and bit-independent in-DRAM operations to exploit bit-level parallelism across the memory array. We com-pare PipeDRAM to different computing platforms. PipeDRAM provides (i) 11.8×, 11.8×, and 80.4× higher performance and (ii) 25.4×, 3.0×, and 38.0× lower energy consumption than three state-of-the-art PUD systems. PipeDRAM incurs low area cost on top of a DRAM chip (1.86%) and CPU die (0.05%). To enable further research on PUD systems, we open-source PipeDRAM at https://github.com/CMU-SAFARI/PipeDRAM.

## 中文摘要

使用 DRAM 进行处理 (PUD) 架构利用 DRAM 的模拟操作特性，通过以垂直布局组织数据（其中操作数位沿 DRAM 列堆叠），在内存阵列内执行批量按位布尔运算和算术运算。然而，现代计算系统本身采用水平数据布局，保留高速缓存行抽象，利用行缓冲区中的空间局部性，并实现高内存吞吐量。这种根本性的不匹配迫使现有的 PUD 架构频繁地在水平和垂直格式之间执行数据布局转换，从而产生显着的性能、能源和系统集成开销。我们的目标是以低成本消除 PUD 系统中的数据转置开销。为此，我们提出了 PipeDRAM，这是一种 PUD 架构，无需运行时数据布局转换，从而可以直接在水平布局的数据上进行 PUD 操作。 PipeDRAM 的关键思想是 (i) 确定性地重新组织每个内存请求内的位，以在水平数据布局的 DRAM 阵列中实现 PUD 友好的数据放置，以及 (ii) 采用基于管道的执行模型，该模型重叠位相关和位无关的 DRAM 操作，以利用整个内存阵列的位级并行性。我们将 PipeDRAM 与不同的计算平台进行比较。与三种最先进的 PUD 系统相比，PipeDRAM 的性能 (i) 提高了 11.8 倍、11.8 倍和 80.4 倍，(ii) 能耗降低了 25.4 倍、3.0 倍和 38.0 倍。 PipeDRAM 在 DRAM 芯片和 CPU 裸片上的额外面积开销较低，分别为 1.86% 和 0.05%。为了进一步研究 PUD 系统，我们在 https://github.com/CMU-SAFARI/PipeDRAM 上开源了 PipeDRAM。

## 中文关键词

DRAM 内计算；数据转置；软硬件流水线；比特串行计算

## 代码与研究制品

- 代码仓库：[https://github.com/CMU-SAFARI/PipeDRAM](https://github.com/CMU-SAFARI/PipeDRAM)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21530459](https://doi.org/10.5281/zenodo.21530459)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9B](index.md) · [MICRO 2026 主页](../index.md)
