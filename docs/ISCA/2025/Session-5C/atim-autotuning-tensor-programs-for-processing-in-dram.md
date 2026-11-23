---
title: "ATiM: Autotuning Tensor Programs for Processing-in-DRAM"
description: "ISCA 2025 · Session 5C · ATiM: 自调优Processing-in-DRAM张量程序"
tags:
  - "ISCA2025"
  - "Session 5C"
  - "Processing-in-Memory"
---

# ATiM: Autotuning Tensor Programs for Processing-in-DRAM

**中文标题：** ATiM: 自调优Processing-in-DRAM张量程序

**所属 Session：** [Session 5C](index.md) · [ISCA 2025](../index.md)

**作者：** Yongwon Shin, Dookyung Kang, Hyojin Sung

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731096) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Processing-in-DRAM (DRAM-PIM) has emerged as a promising technology for accelerating memory-intensive operations in mod- ern applications, such as Large Language Models (LLMs). Despite its potential, current software stacks for DRAM-PIM face significant challenges, including reliance on hand-tuned libraries that hinder programmability, limited support for high-level abstractions, and the lack of systematic optimization frameworks. To address these limita- tions, we present ATiM, a search-based optimizing tensor compiler for UPMEM. Key features of ATiM include: (1) automated searches of the joint search space for host and kernel tensor programs, (2) PIM-aware optimizations for efficiently handling boundary condi- tions, and (3) improved search algorithms for the expanded search space of UPMEM systems. Our experimental results on UPMEM hardware demonstrate performance gains of up to 6.18×for various UPMEM benchmark kernels and 8.21×for GPT-J layers. To the best of our knowledge, ATiM is the first tensor compiler to provide fully automated, autotuning-integrated code generation support for a DRAM-PIM system. By bridging the gap between high-level tensor computation abstractions and low-level hardware-specific require- ments, ATiM establishes a foundation for advancing DRAM-PIM programmability and enabling streamlined optimization.

## 中文摘要

DRAM存内计算（DRAM-PIM）是一项前景可观的技术，用于加速现代应用（例如大语言模型LLM）中的访存密集型运算。尽管潜力巨大，但当前DRAM-PIM软件栈仍存在诸多难题：依赖人工调优的算子库、可编程性差、高层抽象支持不足，并且缺少系统化的优化框架。针对这些短板，本文提出ATiM，一款面向UPMEM、基于搜索的张量优化编译器。
ATiM核心特性：（1）对主机侧与核函数张量程序的联合搜索空间进行自动搜索；（2）面向PIM的专属优化，高效处理边界条件；（3）改进搜索算法，适配UPMEM系统更大的搜索空间。
在UPMEM硬件上的实验结果表明：各类UPMEM基准算子最高提速6.18倍，GPT-J层最高提速8.21倍。据我们所知，ATiM是首个为DRAM-PIM系统提供全自动、集成自动调优能力的代码生成支持的张量编译器。它打通高层张量计算抽象与底层硬件约束之间的鸿沟，为提升DRAM-PIM可编程性、简化优化流程奠定基础。

## 英文关键词

Processing-in-DRAM, tensor programs, autotuning, compiler optimization

## 中文关键词

DRAM 内处理, 张量编译器, 自动调优, 联合搜索空间

## 代码与研究制品

- [代码仓库](https://github.com/SNU-CODElab/atim)
- [研究制品](https://doi.org/10.5281/zenodo.15379924)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731096)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 5C](index.md) · [返回 ISCA 2025](../index.md)
