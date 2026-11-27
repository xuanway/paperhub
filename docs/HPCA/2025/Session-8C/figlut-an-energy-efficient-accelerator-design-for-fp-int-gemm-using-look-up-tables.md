---
title: "FIGLUT: An Energy-Efficient Accelerator Design for FP-INT GEMM Using Look-Up Tables"
description: "HPCA 2025 · Viva Las Learning Models"
tags:
  - "HPCA2025"
  - "Viva Las Learning Models"
---

# FIGLUT: An Energy-Efficient Accelerator Design for FP-INT GEMM Using Look-Up Tables

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Viva Las Learning Models。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Viva Las Learning Models</p>
</div>

**论文链接**：
**作者**：Gunho Park (POSTECH), Hyeokjun Kwon (POSTECH), Jiwoo Kim (POSTECH), Jeongin Bae (NAVER), Baeseong Park (NAVER), Dongsoo Lee (NAVER), Youngjoo Lee (POSTECH)
**会议**：HPCA 2025

---

## 中文标题

FIGLUT：基于查找表的 FP-INT GEMM 高能效加速器设计

## 英文摘要

Weight-only quantization has emerged as a promising solution to the deployment challenges of large language models (LLMs). However, it necessitates FP-INT operations, which make implementation on general-purpose hardware like GPUs difficult. In this paper, we propose FIGLUT, an efficient look-up table (LUT)-based GEMM accelerator architecture. Instead of performing traditional arithmetic operations, FIGLUT retrieves precomputed values from an LUT based on weight patterns, significantly reducing the computational complexity. We also introduce a novel LUT design that addresses the limitations of conventional memory architectures. To further improve LUT-based operations, we propose a half-size LUT combined with a dedicated decoding and multiplexing unit. FIGLUT efficiently supports different bit precisions and quantization methods using a single fixed hardware configuration. For the same 3-bit weight precision, FIGLUT demonstrates 59% higher TOPS/W and 20% lower perplexity than state-of-the-art accelerator design. When targeting the same perplexity, FIGLUT achieves 98% higher TOPS/W by performing 2.4-bit operations.

## 中文摘要

仅权重量化已成为应对大语言模型（LLM）部署挑战的一种有前景的解决方案。然而，它需要执行 FP-INT 运算，这使得在 GPU 等通用硬件上的实现变得困难。本文提出 FIGLUT，一种基于查找表（LUT）的高效 GEMM 加速器架构。FIGLUT 不再执行传统的算术运算，而是根据权值模式从 LUT 中检索已预计算的值，从而显著降低计算复杂度。我们还提出了一种新颖的 LUT 设计，以解决传统存储架构存在的局限。为了进一步改进基于 LUT 的运算，我们提出半尺寸 LUT 并结合专用的解码与多路复用单元。FIGLUT 能够以单一固定的硬件配置高效支持不同的比特精度与量化方法。在相同的 3 比特权重精度下，FIGLUT 相比最先进的加速器设计实现了高 59% 的 TOPS/W 和低 20% 的困惑度。在追求相同困惑度时，FIGLUT 通过执行 2.4 比特运算实现了高 98% 的 TOPS/W。
