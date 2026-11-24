---
title: "BitRed: Taming Non-Uniform Bit-Level Sparsity with a Programmable RISC-V ISA for DNN Acceleration"
description: "ASPLOS 2026 · Session 5B · BitRed：以可编程 RISC-V ISA 驾驭非均匀位级稀疏性实现 DNN 加速"
tags:
  - "ASPLOS2026"
  - "Session 5B"
  - "On-Device & Edge AI"
---

# BitRed: Taming Non-Uniform Bit-Level Sparsity with a Programmable RISC-V ISA for DNN Acceleration

**中文标题：** BitRed：以可编程 RISC-V ISA 驾驭非均匀位级稀疏性实现 DNN 加速

**所属 Session：** [Session 5B](index.md) · [ASPLOS 2026](../index.md)

**作者：** yanhuan liu (ICT), wenming li (ICT), kunming zhang (ICT), yuqun liu (ICT), siao wen (SmarCo Co., Ltd), lexin wang (ICT), tianyu liu (ICT), haibin wu (ICT), zhihua fan (ICT), xiaochun ye (ICT), dongrui fan (SmarCo Co., Ltd), xuejun an (ICT)

**单位：** ICT；SmarCo Co., Ltd

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790132) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The non-uniform and dynamic nature of Bit-Level Sparsity (BLS) poses a critical load-imbalance challenge for parallel hardware accelerators. While the Bit-Interleaving paradigm, represented by state-of-the-art accelerators like Bitlet, shows promise, it is fundamentally constrained by a rigid datapath and severe inter-channel load imbalance. This paper introduces BitRed, an accelerator that embodies a new “programmable adaptive bit-interleaving” philosophy. Rather than a monolithic design, BitRed's core is an Adaptive-Sparse Processing Unit (ASPU) that deconstructs the acceleration process into a set of orthogonal RISC-V ISA extensions for pre-processing (cal.pre), adaptive distillation with dynamic load balancing (cal.adis), and PDP-optimal reduction (cal.red). By transforming a rigid hardware problem into a flexible scheduling problem, this ISA-based approach provides a fundamentally more adaptable and extensible solution. Empirical studies on a broad set of benchmarks highlight the following results (normalized to a SCNN baseline): (1) up to 9.4× speedup over the Bitlet, and 5.6× over the latest bit-serial SOTA BitWave; (2) up to 7.6× higher inference efficiency than Bitlet on representative models; (3) 5.072 mm2 area and scalable power consumption from 550.43 mW (float32) to 495.12 mW (16b) and 457.90 mW (8b) @28nm TSMC; and (4) high versatility across precisions, and up to 18.9×/13.5× higher than NVIDIA A100 and Jetson Orin 32GB, demonstrating significant competitiveness against GPUs.

## 中文摘要

位级稀疏性（Bit-Level Sparsity, BLS）的非均匀与动态特性，给并行硬件加速器带来了严峻的负载不均衡挑战。尽管以 Bitlet 等最先进加速器为代表的位交织（Bit-Interleaving）范式展现出潜力，但它从根本上受限于刚性的数据通路和严重的通道间负载不均衡。本文提出 BitRed，一种体现了全新“可编程自适应位交织”理念的加速器。BitRed 的核心并非单体式设计，而是一个自适应稀疏处理单元（Adaptive-Sparse Processing Unit, ASPU），它将加速过程解构为一组相互正交的 RISC-V ISA 扩展，分别用于预处理（cal.pre）、带动态负载均衡的自适应蒸馏（cal.adis）以及 PDP 最优归约（cal.red）。通过将刚性的硬件问题转化为灵活的调度问题，这种基于 ISA 的方法提供了本质上更具适应性和可扩展性的解决方案。在广泛基准集上的实证研究凸显了以下结果（归一化到 SCNN 基线）：(1) 相比 Bitlet 最高 9.4× 加速，相比最新的位串行 SOTA BitWave 为 5.6×；(2) 在代表性模型上推理效率比 Bitlet 最高提升 7.6×；(3) 面积 5.072 mm2，功耗可从 550.43 mW（float32）扩展至 495.12 mW（16b）和 457.90 mW（8b）@28nm TSMC；(4) 跨精度的高通用性，且相比 NVIDIA A100 和 Jetson Orin 32GB 最高提升 18.9×/13.5×，展现出与 GPU 相比的显著竞争力。

## 英文关键词

Deep Learning Acceleration, Bit-Level Sparsity, RISC-V ISA Extension, Bit-Interleaving, Adaptive Load Balancing

## 中文关键词

深度学习加速；位级稀疏性；RISC-V ISA 扩展；位交织；自适应负载均衡

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790132)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5B](index.md) · [返回 ASPLOS 2026](../index.md)
