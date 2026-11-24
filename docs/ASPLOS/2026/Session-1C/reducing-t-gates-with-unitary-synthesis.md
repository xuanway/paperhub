---
title: "Reducing T Gates with Unitary Synthesis"
description: "ASPLOS 2026 · Session 1C · 利用酉综合减少 T 门"
tags:
  - "ASPLOS2026"
  - "Session 1C"
  - "Quantum Computing: Compilation"
---

# Reducing T Gates with Unitary Synthesis

**中文标题：** 利用酉综合减少 T 门

**所属 Session：** [Session 1C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Tianyi Hao (University of Wisconsin-Madison), Amanda Xu (University of Wisconsin-Madison), Swamit Tannu (University of Wisconsin-Madison)

**单位：** University of Wisconsin-Madison

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790210) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Quantum error correction is essential for achieving practical quantum computing but has a significant computational overhead. Among fault-tolerant (FT) gate operations, nonClifford gates, such as 𝑇, are particularly expensive due to their reliance on magic state distillation. These costly𝑇gates appear frequently in FT circuits as many quantum algorithms require arbitrary single-qubit rotations, such as 𝑅𝑥and 𝑅𝑧 gates, which must be decomposed into a sequence of 𝑇and Clifford gates. In many quantum circuits, 𝑅𝑥and 𝑅𝑧gates can be fused to form a single 𝑈3 unitary. However, existing synthesis methods, such as gridsynth, rely on indirect decompositions, requiring separate 𝑅𝑧decompositions that result in a threefold increase in 𝑇count. This work presents TensoR-based Arbitrary unitary SYNthesis (trasyn), a novel FT synthesis algorithm that directly synthesizes arbitrary single-qubit unitaries, avoiding the overhead of separate 𝑅𝑧decompositions. By leveraging tensor network-based search, our approach enables native 𝑈3 synthesis, reducing the 𝑇count, Clifford gate count, and approximation error. Compared to gridsynth-based circuit synthesis, for 187 representative benchmarks, our design reduces the T count by up to 3.5×, and Clifford gates by 7×, resulting in up to 4× improvement in overall circuit infidelity.

## 中文摘要

量子纠错对于实现实用量子计算至关重要，但会带来显著的计算开销。在容错（FT）门操作中，非 Clifford 门（例如 𝑇 门）由于依赖魔法态蒸馏而尤为昂贵。这些昂贵的 𝑇 门在 FT 电路中频繁出现，因为许多量子算法需要任意单量子比特旋转，例如 𝑅𝑥 和 𝑅𝑧 门，而这些旋转必须分解为 𝑇 门与 Clifford 门的序列。在许多量子电路中，𝑅𝑥 和 𝑅𝑧 门可以融合为单个 𝑈3 酉操作。然而，现有综合方法（例如 gridsynth）依赖间接分解，需要分别进行 𝑅𝑧 分解，导致 𝑇 计数增加三倍。本工作提出基于张量的任意酉综合（TensoR-based Arbitrary unitary SYNthesis，trasyn），一种新颖的 FT 综合算法，可直接综合任意单量子比特酉操作，避免分别进行 𝑅𝑧 分解的开销。通过利用基于张量网络的搜索，我们的方法实现了原生 𝑈3 综合，降低了 𝑇 计数、Clifford 门计数与近似误差。与基于 gridsynth 的电路综合相比，在 187 个代表性基准上，我们的设计将 T 计数最多降低 3.5×，Clifford 门最多降低 7×，从而使整体电路不保真度最多改善 4×。

## 英文关键词

quantum computing, fault-tolerant quantum compilation, quantum gate synthesis

## 中文关键词

量子计算；容错量子编译；量子门综合

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790210)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1C](index.md) · [返回 ASPLOS 2026](../index.md)
