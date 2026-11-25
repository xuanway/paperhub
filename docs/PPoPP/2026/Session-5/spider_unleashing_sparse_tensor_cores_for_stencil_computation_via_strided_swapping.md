---
title: "SPIDER: Unleashing Sparse Tensor Cores for Stencil Computation via Strided Swapping"
description: "PPoPP 2026 Session 5（Stencil and Sparse Matrix Computation）：首个用稀疏张量核加速模板计算，比 cuDNN 快 6.23×"
tags:
  - "PPoPP2026"
  - "Session-5"
  - "Stencil and Sparse Matrix Computation"
  - "Stencil Computation"
  - "Sparse Tensor Cores"
  - "Code Transformation"
authors:
  - "Qiqi Gu"
  - "Chenpeng Wu"
  - "Heng Shi"
  - "Jianguo Yao"
session: "Session 5: Stencil and Sparse Matrix Computation"
session_number: 5
session_chair: "Shoaib Kamil"
date: "2026-02-03"
time: "09:50–10:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786414"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# SPIDER: Unleashing Sparse Tensor Cores for Stencil Computation via Strided Swapping

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 SPIDER，首个利用稀疏张量核加速模板计算的系统，以编译期核矩阵跨步交换配合运行时输入行交换，把模板计算转为 SpTC 兼容运算且运行时零开销。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 5: Stencil and Sparse Matrix Computation</p>
</div>

**作者**：Qiqi Gu, Chenpeng Wu, Heng Shi, and Jianguo Yao — Shanghai Jiao Tong University, China; Shanghai Enflame Technology, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 09:50–10:10 · Session 5: Stencil and Sparse Matrix Computation（主席：Shoaib Kamil）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786414) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Recent research has focused on accelerating stencil computations by exploiting emerging hardware like Tensor Cores. To leverage these accelerators, the stencil operation must be transformed to matrix multiplications. However, this transformation introduces undesired sparsity into the kernel matrix, leading to significant redundant computation. In this paper, we present SPIDER, the first system to turn this unresolved sparsity into an optimization opportunity by exploring the potential of Sparse Tensor Cores (SpTCs) for stencil acceleration. Specifically, SPIDER introduces an efficient and elegant transformation method that integrates two cooperative techniques: an ahead-of-time strided swapping transformation for kernel matrices and an on-the-fly row-swapping mechanism for inputs. This rule-based approach effectively transforms stencil computation into operations compatible with SpTCs, introducing only slight compile-time overhead and zero runtime overhead. Additionally, SPIDER incorporates multiple optimizations to maximize computational efficiency. Experimental evaluations demonstrate that SPIDER outperforms vendor library cuDNN by 6.23× and state-of-the-art (SOTA) Tensor Core-based approaches (ConvStencil, FlashFFTStencil, etc.) by 1.98× on average.

## 中文摘要

近期研究致力于利用 Tensor Core 等新兴硬件来加速模板（stencil）计算。为利用这些加速器，必须将模板运算转换为矩阵乘法。然而，该转换会给核矩阵引入非期望的稀疏性，导致大量冗余计算。本文提出 SPIDER，这是首个通过挖掘稀疏张量核（SpTC）在模板加速方面的潜力，将这一尚未解决的稀疏性转化为优化机会的系统。具体而言，SPIDER 引入一种高效而优雅的转换方法，它融合了两项协同技术：针对核矩阵的提前跨步交换变换，以及针对输入的运行时行交换机制。这种基于规则的方法可有效地将模板计算转换为与 SpTC 兼容的运算，仅带来少量编译期开销与零运行时开销。此外，SPIDER 还集成了多项优化，以最大化计算效率。实验评估表明，SPIDER 比厂商库 cuDNN 快 6.23 倍，比最先进（SOTA）的基于 Tensor Core 的方法（ConvStencil、FlashFFTStencil 等）平均快 1.98 倍。

## 英文关键词

Stencil Computation, Sparse Tensor Core, Structured Sparsity

## 中文关键词

模板计算；稀疏张量核；结构化稀疏

---

## 一句话总结

> 提出 SPIDER，首个利用稀疏张量核加速模板计算的系统，以编译期核矩阵跨步交换配合运行时输入行交换，把模板计算转为 SpTC 兼容运算且运行时零开销。

## 研究问题

模板计算需转为矩阵乘法才能用张量核，但该变换会给核矩阵引入稀疏性、产生大量冗余计算，现有张量核方案未能解决这一未解难题。

## 方法简述

- 提出提前编译期的核矩阵跨步交换（strided swapping）变换。
- 设计运行时的输入即时行交换（row-swapping）机制，与上述变换协同工作。
- 采用基于规则的变换方法将模板计算转化为稀疏张量核兼容的操作，仅需轻微编译期开销、无运行时开销。
- 引入多项优化以最大化计算效率。

## 主要结果

- 平均性能为厂商库 cuDNN 的 6.23×。
- 平均优于 ConvStencil、FlashFFTStencil 等 SOTA 张量核方案 1.98×。
- 变换仅带来少量编译期开销，运行时开销为零。

---

> 所属 Session：[Session 5: Stencil and Sparse Matrix Computation](index.md) · 返回 [PPoPP 2026 总览](../index.md)
