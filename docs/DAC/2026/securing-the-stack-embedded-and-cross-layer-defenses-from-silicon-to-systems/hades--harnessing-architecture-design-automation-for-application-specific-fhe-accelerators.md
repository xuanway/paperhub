Hades: Harnessing Architecture Design Automation for Application-Specific FHE Accelerators
Authors：
[Silin Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=82007102512622174181)，[Yinghao Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=87670100045444657801)，[Fuping Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=386143)，[Hang Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=947343)，[Xiaowei Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=614143)

## 中文标题

Hades：利用架构设计自动化构建面向应用的 FHE 加速器

## 英文摘要

With the advancement of fully homomorphic encryption (FHE), encrypted applications exhibit diverse encryption parameters and compute features. However, existing FHE accelerator architectures are fixed, which lacks the flexibility to support the application diversity. The diversity among FHE applications calls for a more flexibile and efficient accelerator design.To address this challenge, we propose Hades, an automated framework for FHE accelerator generation. Hades analyzes the dataflow graph and encryption parameters of a given FHE application, establishes a mapping from the application to hardware architecture, and automatically searches for accelerator configurations optimized for the target workload. The automation capability of Hades allows for flexible hardware realization on FPGAs and also provides design guidance for ASIC-based accelerators. We evaluate Hades on a range of FHE applications with diverse features. Experimental results demonstrate that Hades can exploit application-specific features to automatically generate efficient hardware architectures. We highlight the following results: (1) compared with state-of-the-art FPGA accelerators, Poseidon and FAB, our work achieves a speedup from 1.99× to 6.58× while reducing 50% resource consumption; (2) compared with state-of-the-art ASIC accelerators, SHARP and CraterLake, Hades achieves a speedup of more than 3×; (3) achieves 65%-94% hardware utilization on multiple FHE applications, more than a 2× improvement over manual accelerators.

## 中文摘要

随着全同态加密（FHE）的发展，加密应用呈现出多样化的加密参数与计算特征。然而，现有 FHE 加速器架构是固定的，缺乏支撑应用多样性的灵活性。FHE 应用之间的差异性要求更灵活、更高效的加速器设计。为应对这一挑战，我们提出 Hades，一个用于 FHE 加速器自动生成的框架。Hades 分析给定 FHE 应用的数据流图和加密参数，建立从应用到硬件架构的映射，并自动搜索针对目标工作负载优化的加速器配置。Hades 的自动化能力既支持在 FPGA 上灵活实现硬件，也为基于 ASIC 的加速器提供设计指导。我们在一系列具有多样特征的 FHE 应用上评估了 Hades。实验结果表明，Hades 能够利用应用特定特征自动生成高效的硬件架构。我们强调以下结果：(1) 与现有最优 FPGA 加速器 Poseidon 和 FAB 相比，我们的工作实现了 1.99 倍至 6.58 倍的加速，同时降低 50% 的资源消耗；(2) 与现有最优 ASIC 加速器 SHARP 和 CraterLake 相比，Hades 实现了超过 3 倍的加速；(3) 在多个 FHE 应用上实现 65%–94% 的硬件利用率，相比手工设计的加速器提升 2 倍以上。

## 英文关键词

Fully Homomorphic Encryption, Accelerator, Design Automation

## 中文关键词

全同态加密、加速器、设计自动化
