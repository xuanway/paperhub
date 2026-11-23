---
title: "DX100: Programmable Data Access Accelerator for Indirection"
description: "ISCA 2025 · Session 8C · DX100：面向间接访问的可编程数据访问加速器"
tags:
  - "ISCA2025"
  - "Session 8C"
  - "Domain Specific Accelerators II"
---

# DX100: Programmable Data Access Accelerator for Indirection

**中文标题：** DX100：面向间接访问的可编程数据访问加速器

**所属 Session：** [Session 8C](index.md) · [ISCA 2025](../index.md)

**作者：** Alireza Khadem, Kamalavasan Kamalakkannan, Zhenyan Zhu, Akash Poptani, Yufeng Gu, Jered Benjamin Dominguez-Trujillo, Nishil Talati, Daichi Fujiki, Scott Mahlke, Galen Shipman, Reetuparna Das

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731015) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Indirect memory accesses frequently appear in applications where memory bandwidth is a critical bottleneck. Prior indirect memory access proposals, such as indirect prefetchers, runahead execution, fetchers, and decoupled access/execute architectures, primarily fo- cus on improving memory access latency by loading data ahead of computation but still rely on the DRAM controllers to reorder mem- ory requests and enhance memory bandwidth utilization. DRAM controllers have limited visibility to future memory accesses due to the small capacity of request buffers and the restricted memory- level parallelism of conventional core and memory systems. We introduce DX100, a programmable data access accelerator for indirect memory accesses. DX100 is shared across cores to offload bulk indirect memory accesses and associated address calculation operations. DX100 reorders, interleaves, and coalesces memory re- quests to improve DRAM row-buffer hit rate and memory band- width utilization. DX100 provides a general-purpose ISA to support diverse access types, loop patterns, conditional accesses, and ad- dress calculations. To support this accelerator without significant programming efforts, we discuss a set of MLIR compiler passes that automatically transform legacy code to utilize DX100. Experimental evaluations on 12 benchmarks spanning scientific computing, database, and graph applications show that DX100 achieves performance improvements of 2.6×over a multicore baseline and 2.0× over the state-of-the-art indirect prefetcher.

## 中文摘要

间接内存访问大量出现在内存带宽成为核心瓶颈的应用中。以往针对间接内存访问的方案，例如间接预取器、前瞻执行、取指单元、解耦访存/执行架构，主要思路是在计算之前提前加载数据，以此降低访存延迟；但这些方案仍然依赖DRAM控制器对访存请求重排，提升带宽利用率。由于请求缓冲区容量有限、传统核与存储系统的内存级并行度受限，DRAM控制器难以预知未来的访存序列。

本文提出DX100，一款面向间接内存访问的可编程数据访问加速器。DX100由多个核心共享，承接批量间接访存以及配套的地址计算任务。DX100对访存请求进行重排、交错与合并，提升DRAM行缓冲命中率与内存带宽利用率。DX100提供一套通用指令集，支持多种访存模式、循环结构、条件访问与地址计算。为降低使用门槛，本文配套一组MLIR编译器Pass，能够自动转换已有代码，调度到DX100上执行。 在覆盖科学计算、数据库、图计算的12个基准测试上，DX100相比多核基线性能提升2.6倍，对比前沿间接预取器性能提升2.0倍。

## 英文关键词

Data-Centric Accelerator, Indirect Memory Access, High-Performance Computing

## 中文关键词

以数据为中心加速器, 间接内存访问, 高性能计算

## 代码与研究制品

- [研究制品](https://zenodo.org/records/15103397)
- [代码仓库](https://github.com/arkhadem/DX100)
- [研究制品](https://doi.org/10.5281/zenodo.15103396)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731015)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8C](index.md) · [返回 ISCA 2025](../index.md)
