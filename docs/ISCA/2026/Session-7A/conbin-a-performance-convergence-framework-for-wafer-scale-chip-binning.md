---
title: "ConBin: A Performance-Convergence Framework for Wafer-Scale Chip Binning"
description: "ISCA 2026 · Session 7A · ConBin: A Performance-Convergence Framework for Wafer-Scale Chip Binning"
tags:
  - "ISCA2026"
  - "Session 7A"
  - "Emerging Technologies: Chiplet, Wafer-Scale, etc."
---

# ConBin: A Performance-Convergence Framework for Wafer-Scale Chip Binning

**中文标题：** ConBin: 面向晶圆级芯片分档的性能收敛框架

**所属 Session：** [Session 7A](index.md) · [ISCA 2026](../index.md)

**作者：** Huiqing Xu, Mengdi Wang, Yinhe Han, Ying Wang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Wafer-scale chips (WSCs) like the Cerebras Wafer-Scale Engines (WSEs) offer immense on-chip compute and bandwidth for large-scale Artificial Intelligence (AI) workloads, but their massive area makes defect-free fabrication impossible, posing severe yield and cost challenges. The traditional solution is chip binning, which grades chips by frequency or core count, but such metrics fail for WSCs as their performance is not only determined by core number but also heavily influenced by the communication irregularities caused by faults. These fault-induced variations cause large inter-chip performance divergence, forcing conservative binning thresholds that reduce premium-bin yield (i.e. the fraction of chips in the highest-performance bins) and the aggregate guaranteed performance delivered across bins (i.e., the total sellable effective compute capacity, SECC). Therefore, a new binning strategy and performance-convergence mechanisms are essential for the practical commercialization of WSCs. To address these challenges, we first propose Performance Binning, a novel paradigm that grades WSCs by their actual performance on target workloads rather than by core count or frequency. We further develop a Performance-Convergence Framework for WSC Binning (ConBIN) that unifies hardware design, software optimization, and performance binning to converge the inter-chip performance distribution and maximize binning yield. ConBIN employs automated, fault-correlation-aware redundant interconnect design and post-silicon fault repair to reduce inter-chip divergence of core counts and topology structures. It then applies bin-aware workload mapping and fine-grained communication scheduling guided by lightweight pre-binning targets to suppress residual performance variance, which enables tighter chip bin thresholds and higher premium-bin yield, boosting overall SECC. Finally, ConBIN executes performance binning to determine binning thresholds that maximize total SECC. Evaluations show that ConBIN improves premium-bin yield by 2.80× and total SECC by 2.64× over state-of-the-art (SOTA) fault-tolerant methods on 128×136 WSCs.

## 中文摘要

像 Cerebras 晶圆级引擎（WSE）这样的晶圆级芯片（WSC）为大规模人工智能（AI）工作负载提供了巨大的片上算力和带宽，但其庞大的面积使无缺陷制造成为不可能，带来了严峻的良率与成本挑战。传统解决方案是芯片分档（chip binning），即按频率或核心数量对芯片分级，但这些指标对 WSC 并不适用，因为 WSC 的性能不仅取决于核心数量，还深受故障所导致的通信不规则性的影响。这些由故障引起的差异造成芯片间性能的巨大分化，迫使采用保守的分档阈值，从而降低了优质档位良率（即处于最高性能档位的芯片比例）以及跨档位交付的总保证性能（即总可售有效算力，SECC）。因此，新的分档策略与性能收敛机制对于 WSC 的实际商业化至关重要。为应对这些挑战，我们首先提出性能分档（Performance Binning），这是一种新的范式，它依据 WSC 在目标工作负载上的实际表现而非核心数量或频率来对其分级。我们进一步开发了面向 WSC 分档的性能收敛框架（ConBIN），它将硬件设计、软件优化与性能分档统一起来，以收敛芯片间的性能分布并最大化分档良率。ConBIN 采用自动化的、故障相关性感知的冗余互连设计以及硅后故障修复，以减小核心数量与拓扑结构的芯片间差异。随后，它应用由轻量级预分档目标引导的分档感知工作负载映射和细粒度通信调度来抑制残余的性能方差，从而实现更严格的芯片分档阈值和更高的优质档位良率，提升整体 SECC。最后，ConBIN 执行性能分档，以确定使总 SECC 最大的分档阈值。评估表明，在 128×136 的 WSC 上，与最先进（SOTA）的容错方法相比，ConBIN 将优质档位良率提升了 2.80×，并将总 SECC 提升了 2.64×。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7A](index.md) · [返回 ISCA 2026](../index.md)
