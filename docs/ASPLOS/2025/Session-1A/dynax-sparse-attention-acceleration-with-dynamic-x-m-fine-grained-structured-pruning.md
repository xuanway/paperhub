---
title: "DynaX: Sparse Attention Acceleration with Dynamic X:M Fine-Grained Structured Pruning"
description: "ASPLOS 2025 · Session 1A · DynaX：基于动态 X:M 细粒度结构化剪枝的稀疏注意力加速"
tags:
  - "ASPLOS2025"
  - "Session 1A"
  - "ML Acceleration"
---

# DynaX: Sparse Attention Acceleration with Dynamic X:M Fine-Grained Structured Pruning

**中文标题：** DynaX：基于动态 X:M 细粒度结构化剪枝的稀疏注意力加速

**所属 Session：** [Session 1A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Xiao Xiong (College of Computer Science, Chongqing University), Zhaorui Chen (College of Computer Science, Chongqing University), Yue Liang (College of Computer Science, Chongqing University), Minghao Tian (College of Computer Science, Chongqing University), Jiaxing Shang (College of Computer Science, Chongqing University), Jiang Zhong (College of Computer Science, Chongqing University), Dajiang Liu (College of Computer Science, Chongqing University)

**单位：** College of Computer Science, Chongqing University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715991) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Owning to the mechanism of self-attention, Transformers have exhibited incredible performance in a wide range of artificial intelligence tasks. With the growth of sequence length, attention computation with quadratic complexity becomes the bottleneck, and dynamic sparsity is an effective technique to alleviate this problem. However, dynamic attention sparsity for long-sequence tasks suffers from two challenges, i.e., irregular sparse patterns and heavy prediction overhead. To this end, this paper proposes DynaX, an algorithm-hardware co-design framework that accelerates attention computation via dynamic X:M fine-grained structured pruning. Different from traditional N:M pruning, DynaX dynamically selects variable 𝑋 (rather than a fixed 𝑁) important scores from a group via a 2-step pruning method, which results in high sparsity and less prediction memory overhead while maintaining pattern regularity to a certain extent. After that, DynaX performs block scheduling to reorganize score blocks into hardware blocks that can perfectly match the size of the processing element array (PEA), resulting in a higher utilization rate. Experimental results show that DynaX can achieve average sparsity of 89.54% and 91.77% for short-sequence tasks and long-sequence tasks, respectively, with less than 1% accuracy loss. Compared to Sanger and SALO2, DynaX achieves a speedup of 1.99 × and 1.50 × on the BERT-base model, and an energy efficiency improvement of 5.16 × and 4.20 ×, respectively.

## 中文摘要

由于自注意力机制，Transformer 在广泛的人工智能任务中展现出惊人的性能。随着序列长度的增长，具有二次复杂度的注意力计算成为瓶颈，而动态稀疏性是缓解该问题的有效技术。然而，长序列任务的动态注意力稀疏性面临两个挑战，即不规则的稀疏模式和沉重的预测开销。为此，本文提出 DynaX，一个通过动态 X:M 细粒度结构化剪枝来加速注意力计算的算法-硬件协同设计框架。与传统 N:M 剪枝不同，DynaX 通过两步剪枝方法动态地从一组中选取数量可变的 X（而非固定的 N）个重要分数，从而在保持一定程度模式规则性的同时，实现高稀疏度和更少的预测内存开销。之后，DynaX 执行块调度，将分数块重组为能够完美匹配处理单元阵列（PEA）尺寸的硬件块，从而获得更高的利用率。实验结果表明，DynaX 在短序列任务和长序列任务上分别能够达到 89.54% 和 91.77% 的平均稀疏度，且精度损失小于 1%。与 Sanger 和 SALO2 相比，DynaX 在 BERT-base 模型上分别实现了 1.99× 和 1.50× 的加速，能效分别提升了 5.16× 和 4.20×。

## 英文关键词

Seft-Attention, Dynamic Sparsity, Acceleration

## 中文关键词

自注意力；动态稀疏性；加速

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715991)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1A](index.md) · [返回 ASPLOS 2025](../index.md)
