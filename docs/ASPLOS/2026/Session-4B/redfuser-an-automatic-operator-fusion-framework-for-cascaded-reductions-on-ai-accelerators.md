---
title: "RedFuser: An Automatic Operator Fusion Framework for Cascaded Reductions on AI Accelerators"
description: "ASPLOS 2026 · Session 4B · RedFuser：面向 AI 加速器上级联归约的自动算子融合框架"
tags:
  - "ASPLOS2026"
  - "Session 4B"
  - "ML Compilers & Tensor Programs"
---

# RedFuser: An Automatic Operator Fusion Framework for Cascaded Reductions on AI Accelerators

**中文标题：** RedFuser：面向 AI 加速器上级联归约的自动算子融合框架

**所属 Session：** [Session 4B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Xinsheng Tang (Alibaba Cloud Computing), Yangcheng Li (Alibaba Cloud Computing), Nan Wang (Alibaba Cloud Computing), Zhiyi Shu (Alibaba Cloud Computing), Xingyu Ling (Alibaba Cloud Computing), Junna Xing (Alibaba Cloud Computing), Peng Zhou (Alibaba Cloud Computing), Qiang Liu (Alibaba Cloud Computing)

**单位：** Alibaba Cloud Computing

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790209) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Operator fusion, as a key performance optimization technique in the deployment of AI models, significantly improves execution efficiency and has been widely adopted in modern AI compilers. However, for cascaded reduction operations involving multiple loops with inter-loop data dependencies, such as the safe softmax followed by GEMM within attention mechanisms, existing compilers lack effective automated fusion and kernel generation capabilities. Although some works have addressed specific instances through handcrafted fusion strategies, their solutions are limited in generality and difficult to extend to other similar structures. Given the prevalence of such computational patterns in deep learning models, there remains significant untapped potential in achieving general and automated fusion optimization. In this paper, we present a formal theoretical methodology for analyzing cascaded reductions which can fuse them into a single loop and introduce an incremental computation form. Based on this methodology, we design Reduction Fuser (RedFuser), a framework that automatically identifies supported cascaded reduction patterns and generates optimized fused kernels. Experiments show that RedFuser successfully fuses diverse workloads, achieving up to 2× to 5× speedup over state-of-the-art AI compilers and matching the performance of highly optimized hand-written kernels.

## 中文摘要

算子融合作为 AI 模型部署中的关键性能优化技术，能显著提升执行效率，已被现代 AI 编译器广泛采用。然而，对于涉及多个循环且循环间存在数据依赖的级联归约运算，例如注意力机制中 safe softmax 后接 GEMM，现有编译器缺乏有效的自动融合与内核生成能力。尽管一些工作通过手工设计的融合策略解决了特定实例，但其方案通用性有限，难以扩展到其他类似结构。鉴于此类计算模式在深度学习模型中普遍存在，在实现通用且自动化的融合优化方面仍有显著尚未挖掘的潜力。本文提出一种用于分析级联归约的形式化理论方法，可将级联归约融合为单个循环，并引入一种增量计算形式。基于该方法，我们设计 Reduction Fuser（RedFuser），这是一个能够自动识别所支持的级联归约模式并生成优化融合内核的框架。实验表明，RedFuser 成功融合了多种多样化的工作负载，相对于当前最先进的 AI 编译器取得最高 2× 至 5× 的加速，并达到高度优化的手写内核的性能水平。

## 英文关键词

Automatic Operator Fusion, Cascaded Reductions, GPUs

## 中文关键词

自动算子融合；级联归约；GPU

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790209)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4B](index.md) · [返回 ASPLOS 2026](../index.md)
