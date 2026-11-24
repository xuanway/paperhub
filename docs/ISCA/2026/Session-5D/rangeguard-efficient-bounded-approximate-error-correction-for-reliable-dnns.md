---
title: "RangeGuard: Efficient, Bounded Approximate Error Correction for Reliable DNNs"
description: "ISCA 2026 · Session 5D · RangeGuard: Efficient, Bounded Approximate Error Correction for Reliable DNNs"
tags:
  - "ISCA2026"
  - "Session 5D"
  - "Potpourri"
---

# RangeGuard: Efficient, Bounded Approximate Error Correction for Reliable DNNs

**中文标题：** RangeGuard: 面向可靠 DNN 的高效有界近似纠错

**所属 Session：** [Session 5D](index.md) · [ISCA 2026](../index.md)

**作者：** Hanum Ko, Sangheum Yeon, Jong Hwan Ko, Jungrae Kim

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

As DRAM scales in density and adopts 3D integration, raw fault rates increase and multi-bit errors are no longer rare. Such errors can severely impact Deep Neural Networks (DNNs): although DNNs tolerate small numerical perturbations, random bit flips can create extreme outliers that propagate and sharply degrade accuracy. Large Language Models (LLMs) are particularly vulnerable because attention, residual, and normalization layers can amplify and preserve a single corrupted activation across many layers, destabilizing inference. This paper introduces RangeGuard, a metadata-centric error-correcting framework that provides strong reliability and high efficiency based on bounded approximate correction. Instead of protecting raw bits, RangeGuard encodes compact Range Identifiers (RIDs) that capture the numerical range of each value. These compact metadata enable efficient use of limited redundancy and concentrate protection on range changes—which indicate harmful semantic deviations—while ignoring benign intra-range variations. Upon detecting a range change, RangeGuard restores the correct range and substitutes a representative value, ensuring that error magnitudes are bounded within the range. Based on RIDs, RangeGuard can tolerate 64+ bits of error using only 16 bits of parity available in GPU memories without a noticeable accuracy loss. By introducing semantic range protection, RangeGuard enables reliable DNN execution even under frequent memory errors and tight redundancy budgets.

## 中文摘要

随着 DRAM 密度提升并采用 3D 集成，原始故障率上升，多位错误不再罕见。此类错误会严重影响深度神经网络（DNN）：尽管 DNN 能容忍微小的数值扰动，但随机比特翻转会产生极端离群值，这些离群值会传播并急剧降低精度。大语言模型（LLM）尤其脆弱，因为注意力、残差与归一化层会放大并在许多层间保留单个被破坏的激活值，使推理失稳。本文提出 RangeGuard，一个以元数据为中心的纠错框架，基于有界近似纠错提供强可靠性与高效率。RangeGuard 并不保护原始比特，而是编码紧凑的范围标识符（RID），以刻画每个值的数值范围。这些紧凑元数据使有限的冗余得以高效利用，并将保护集中在范围变化上——范围变化表示有害的语义偏移——而忽略良性的范围内变化。一旦检测到范围变化，RangeGuard 便会恢复正确的范围并替换为代表值，从而确保错误幅度被限制在该范围内。基于 RID，RangeGuard 仅用 GPU 存储器中可用的 16 比特校验位即可容忍 64 比特以上的错误，且不会带来明显的精度损失。通过引入语义范围保护，RangeGuard 即便在频繁内存错误与紧张的冗余预算下也能实现可靠的 DNN 执行。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5D](index.md) · [返回 ISCA 2026](../index.md)
