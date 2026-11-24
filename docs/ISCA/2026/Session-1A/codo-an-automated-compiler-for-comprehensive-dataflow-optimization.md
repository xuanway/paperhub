---
title: "CODO: An Automated Compiler for Comprehensive Dataflow Optimization"
description: "ISCA 2026 · Session 1A · CODO: An Automated Compiler for Comprehensive Dataflow Optimization"
tags:
  - "ISCA2026"
  - "Session 1A"
  - "Best Paper Candidate Session"
---

# CODO: An Automated Compiler for Comprehensive Dataflow Optimization

**中文标题：** CODO: 面向全面数据流优化的自动化编译器

**所属 Session：** [Session 1A](index.md) · [ISCA 2026](../index.md)

**作者：** Weichuang Zhang, Yiquan Wang, Xinzhou Zhang, Chi Zhang, Yu Feng, Xiaofeng Hou, Chao Li, Jieru Zhao, Minyi Guo

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

FPGAs are well-suited for dataflow architectures that process data in a streaming or pipelined manner, thus satisfying the high computational and communication demands of emerging applications. However, manually implementing an efficient dataflow architecture for large-scale applications is still challenging, even for specialists who use high-level synthesis (HLS) to simplify FPGA programming. To address this, we introduce CODO, an automated compiler that generates feasible and efficient dataflow accelerators on FPGAs. CODO features a systematic method for detecting and eliminating both coarse-grained and fine-grained dataflow violations. Building on this, CODO performs both on- and off-chip data movement optimizations to maximize transfer efficiency. To guarantee a higher design quality, CODO performs automatic scheduling to generate high-performance dataflow accelerators, ensuring a balanced performance-resource trade-off. Synthesis results show that CODO delivers 1.45× to 4.52× latency speedups on typical computation kernels and 3.7× to 33.8× speedups on DNN models compared to SOTA frameworks. In on-board evaluations, CODO achieves 7.3× average speedup on CNN models and 2.07× average speedup on the GPT-2 model over SOTA frameworks. The compiler is open-sourced at https://github.com/sjtu-zhao-lab/codo-artifact.

## 中文摘要

FPGA 非常适合以流式或流水线方式处理数据的 Dataflow 架构，从而满足新兴应用的高计算和通信需求。然而，即使对于使用高层次综合（HLS）简化 FPGA 编程的专家来说，手动为大规模应用实现高效的 Dataflow 架构仍然具有挑战性。为此，我们引入了 CODO，一种自动编译器，能够在 FPGA 上生成可行且高效的 Dataflow 加速器。CODO 具有一种系统性的方法，用于检测和消除粗粒度和细粒度的 Dataflow 违例。在此基础上，CODO 执行片上和片下的数据搬运优化，以最大化传输效率。为了保证更高的设计质量，CODO 执行自动调度以生成高性能的 Dataflow 加速器，确保性能与资源之间的平衡折衷。综合结果表明，与 SOTA 框架相比，CODO 在典型计算核上实现了 1.45× 到 4.52× 的延迟加速，在 DNN 模型上实现了 3.7× 到 33.8× 的加速。在板载评估中，CODO 在 CNN 模型上实现了平均 7.3× 的加速，在 GPT-2 模型上相对于 SOTA 框架实现了平均 2.07× 的加速。该编译器已在 https://github.com/sjtu-zhao-lab/codo-artifact 开源。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：sjtu-zhao-lab/codo-artifact](https://github.com/sjtu-zhao-lab/codo-artifact)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 1A](index.md) · [返回 ISCA 2026](../index.md)
