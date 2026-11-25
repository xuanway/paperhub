---
title: "RoMeo: Mitigating Dual-dimensional Outliers with Rotated Mixed Precision Quantization"
description: "PPoPP 2026 Session 6（Mixed Precision and Quantization）：旋转把通道离群迁到 token 维，精度 +5.17%、2.10×"
tags:
  - "PPoPP2026"
  - "Session-6"
  - "Mixed Precision and Quantization"
  - "Mixed Precision Quantization"
  - "LLM Serving"
  - "Outlier"
authors:
  - "Qihao Zhang"
  - "MingLiang Tang"
  - "Mingshu Zhai"
  - "Kinman Lei"
  - "Jidong Zhai"
session: "Session 6: Mixed Precision and Quantization"
session_number: 6
session_chair: "Dingwen Tao"
date: "2026-02-03"
time: "11:30–11:50"
room: "Balmoral"
doi: "10.1145/3774934.3786419"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# RoMeo: Mitigating Dual-dimensional Outliers with Rotated Mixed Precision Quantization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出算法-系统协同设计的 RoMeo，用基于旋转的混合精度量化把通道维离群值迁移到 token 维，并应对稀疏计算与动态离群检测挑战，精度提升最高 5.17%。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 6: Mixed Precision and Quantization</p>
</div>

**作者**：Qihao Zhang, MingLiang Tang, Mingshu Zhai, Kinman Lei, and Jidong Zhai — Tsinghua University, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 11:30–11:50 · Session 6: Mixed Precision and Quantization（主席：Dingwen Tao）· Balmoral

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786419) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Mixed precision quantization has been adopted to accelerate large language models (LLMs) serving by leveraging high-throughput low-precision compute units in GPUs while preserving outliers in higher precision to maintain model accuracy. However, existing methods focus on mitigating single-dimensional channel-wise outliers, leading to model accuracy degradation when scaled to 4-bit precision. In this paper, we present an algorithm-system co-design to effectively handle dual-dimensional outliers across both channel and token dimensions in LLMs. We introduce a novel rotation-based mixed precision quantization algorithm that suppresses and migrates channel-wise outliers to the token dimension. Based on this algorithm, we propose RoMeo, an efficient LLM serving system designed to overcome the unique system challenges posed by sparse computation pattern and dynamic outlier detection inherent in token-wise outlier handling. Extensive evaluations across various LLMs demonstrate that RoMeo improves quantized model accuracy by up to 5.17% compared to state-of-the-art methods QuaRot and MixQ, while maintaining efficiency comparable to uniform precision quantizations, achieving up to 2.10× end-to-end speedup over half-precision baseline. RoMeo is available at https://github.com/thu-pacman/RoMeo.

## 中文摘要

混合精度量化已被用于加速大语言模型（LLM）服务：它利用 GPU 中高吞吐的低精度计算单元，同时以更高精度保留离群值以维持模型精度。然而，现有方法聚焦于缓解单一维度的通道级离群值，当扩展到 4 比特精度时会导致模型精度下降。本文提出一种算法–系统协同设计，可有效处理 LLM 中同时跨越通道与 token 两个维度的双重维度离群值。我们引入一种新颖的基于旋转的混合精度量化算法，将通道级离群值抑制并迁移到 token 维度。基于该算法，我们提出 RoMeo，一个高效的 LLM 服务系统，旨在克服 token 级离群值处理所固有的稀疏计算模式与动态离群值检测带来的独特系统挑战。针对多种 LLM 的大量评估表明，与最先进方法 QuaRot 和 MixQ 相比，RoMeo 将量化模型精度最高提升 5.17%，同时保持与均匀精度量化相当的效率，相较半精度基线实现最高 2.10 倍的端到端加速。RoMeo 已在 https://github.com/thu-pacman/RoMeo 公开提供。

## 英文关键词

Large Language Model, Mixed Precision Quantization, Algorithm-System Co-design

## 中文关键词

大语言模型；混合精度量化；算法–系统协同设计

---

## 一句话总结

> 提出算法-系统协同设计的 RoMeo，用基于旋转的混合精度量化把通道维离群值迁移到 token 维，并应对稀疏计算与动态离群检测挑战，精度提升最高 5.17%。

## 研究问题

现有混合精度量化只针对通道维的单维离群值，扩展到 4-bit 精度时会导致模型精度下降。

## 方法简述

- 提出基于旋转的混合精度量化算法，同时处理通道与 token 两个维度的离群值，抑制并迁移通道维离群值到 token 维。
- 设计 LLM 服务系统 RoMeo，克服 token 维离群处理带来的稀疏计算模式与动态离群检测等系统挑战。
- 采用算法-系统协同设计，使量化推理效率与均匀精度量化相当。

## 主要结果

- 在多种 LLM 上相比 SOTA 方法 QuaRot 与 MixQ，量化模型精度最高提升 5.17%。
- 效率与均匀精度量化相当，相对半精度基线端到端最高加速 2.10×。

---

> 所属 Session：[Session 6: Mixed Precision and Quantization](index.md) · 返回 [PPoPP 2026 总览](../index.md)
