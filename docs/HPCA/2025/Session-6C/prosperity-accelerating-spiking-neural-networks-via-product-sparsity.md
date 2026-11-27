---
title: "Prosperity: Accelerating Spiking Neural Networks via Product Sparsity"
description: "HPCA 2025 · Stacking the Layers (Sparsity)"
tags:
  - "HPCA2025"
  - "Stacking the Layers (Sparsity)"
---

# Prosperity: Accelerating Spiking Neural Networks via Product Sparsity

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stacking the Layers (Sparsity)。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stacking the Layers (Sparsity)</p>
</div>

**论文链接**：
**作者**：Chiyue Wei (Duke University), Cong Guo (Duke University), Feng Cheng (Duke University), Shiyu Li (Duke University), Hao “Frank” Yang (Johns Hopkins University), Hai “Helen” Li (Duke University), Yiran Chen (Duke University)
**会议**：HPCA 2025

---

## 中文标题

Prosperity：通过乘积稀疏性加速脉冲神经网络

## 英文摘要

Spiking Neural Networks (SNNs) are highly efficient due to their spike-based activation, which inherently produces bit-sparse computation patterns. Existing hardware implementations of SNNs leverage this sparsity pattern to avoid wasteful zero-value computations, yet this approach fails to fully capitalize on the potential efficiency of SNNs. This study introduces a novel sparsity paradigm called Product Sparsity, which leverages combinatorial similarities within matrix multiplication operations to reuse the inner product result and reduce redundant computations. Product Sparsity significantly enhances sparsity in SNNs without compromising the original computation results compared to traditional bit sparsity methods. For instance, in the SpikeBERT SNN model, Product Sparsity achieves a density of only 1.23% and reduces computation by 11×, compared to bit sparsity, which has a density of 13.19%. To efficiently implement Product Sparsity, we propose Prosperity, an architecture that addresses the challenges of identifying and eliminating redundant computations in real-time. Compared to prior SNN accelerator PTB and the A100 GPU, Prosperity achieves an average speedup of 7.4× and 1.8×, respectively, along with energy efficiency improvements of 8.0× and 193×, respectively. The code for Prosperity is available at https://github.com/dubcyfor3/Prosperity.

## 中文摘要

脉冲神经网络（SNN）因其基于脉冲的激活而具有极高效率，其天然产生比特稀疏的计算模式。现有的 SNN 硬件实现利用该稀疏模式避免无用的零值计算，但未能充分发挥 SNN 的潜在效率。本研究提出一种新的稀疏范式——乘积稀疏性，它利用矩阵乘法运算内部的组合相似性来复用内积结果并减少冗余计算。与传统比特稀疏方法相比，乘积稀疏性在不改变原始计算结果的前提下显著提升 SNN 的稀疏性。例如在 SpikeBERT SNN 模型中，乘积稀疏性实现仅 1.23% 的密度并减少 11 倍计算，而比特稀疏的密度为 13.19%。为高效实现乘积稀疏性，我们提出 Prosperity，一种应对实时识别与消除冗余计算挑战的架构。与先前的 SNN 加速器 PTB 和 A100 GPU 相比，Prosperity 分别取得平均 7.4 倍和 1.8 倍的加速，能效分别提升 8.0 倍和 193 倍。Prosperity 的代码见 https://github.com/dubcyfor3/Prosperity。
