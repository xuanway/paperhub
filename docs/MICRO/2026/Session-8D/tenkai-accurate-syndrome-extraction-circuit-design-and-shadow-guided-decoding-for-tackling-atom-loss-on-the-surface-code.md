---
title: "Tenkai: Accurate Syndrome Extraction Circuit Design and Shadow-Guided Decoding for Tackling Atom Loss on the Surface Code"
description: "MICRO 2026 · Session 8D · Tenkai：通过精确综合征提取电路设计与影子引导解码应对表面码中的原子丢失"
tags:
  - "MICRO2026"
  - "Quantum Computing"
---

# Tenkai: Accurate Syndrome Extraction Circuit Design and Shadow-Guided Decoding for Tackling Atom Loss on the Surface Code

**中文标题：** Tenkai：通过精确综合征提取电路设计与影子引导解码应对表面码中的原子丢失

**所属 Session：** [Session 8D](index.md) · [MICRO 2026](../index.md)

**作者：** Chenning Tao, Xiaoyi Zhou, Liqiang Lu, Jianwei Yin

**来源：** MICRO 2026，pp. 3117–3131；[DOI](https://doi.org/10.1109/MICRO67795.2026.00210)

## 英文摘要

Atom loss poses a severe reliability challenge for neutral-atom quantum error correction. Unlike Pauli errors that only perturb a qubit's state, a loss event removes the qubit entirely, invalidating all subsequent gates acting on it and corrupting multiple detector outcomes. The loss-aware pipelines evaluated in this work combine circuit modifications that add extra operations or circuit depth with decoder adaptations that treat loss effects as independent events and discard their mutually exclusive detector structure. We identify that each atom loss event gives rise to a set of detector activation patterns determined by the circuit structure. Each pattern is equivalent to a specific Pauli-fault pattern on the loss-free circuit, and we define this detector-level structure as the loss shadow. This loss-shadow perspective enables a unified optimization space for atom-loss handling, guiding the optimization of walking syndrome-extraction sequences toward compact loss shadows and enabling shadow-guided reweighting that exploits the mutually exclusive detector structure induced by loss. Across loss fractions L ∊ {0.25, 0.50, 0.75} and code distances d ∊ {5,7,9,11}, Tenkai consistently outperforms the two evaluated prior pipelines with gains that grow with code distance, reducing logical error rates by 2.2–6.8× at the practical loss fraction L=0.50 while keeping per-shot online modification under 3µs, compared to 77–153µs in those pipelines.

## 中文摘要

原子损失对中性原子量子纠错提出了严峻的可靠性挑战。与仅扰乱量子位状态的泡利错误不同，丢失事件会完全删除量子位，从而使作用于其的所有后续门失效并破坏多个检测器结果。这项工作中评估的丢失感知管道将增加额外操作或电路深度的电路修改与将丢失效应视为独立事件并丢弃其互斥检测器结构的解码器适配相结合。我们发现每个原子丢失事件都会产生一组由电路结构决定的检测器激活模式。每个模式相当于无损电路上的特定泡利故障模式，我们将这种检测器级结构定义为损耗阴影。这种损失阴影视角为原子损失处理提供了统一的优化空间，指导步行综合症提取序列向紧凑损失阴影的优化，并实现利用损失引起的互斥检测器结构的阴影引导重新加权。在损失分数 L ∊ {0.25, 0.50, 0.75} 和码距 d ∊ {5,7,9,11} 上，Tenkai 始终优于两个评估的先前管道，其增益随着码距而增长，在实际损失分数 L=0.50 时将逻辑错误率降低 2.2–6.8 倍，同时将每次在线修改保持在 3μs 以下。这些管道中的时间为 77–153μs。

## 中文关键词

表面码；原子丢失；综合征提取；影子引导译码；量子纠错

## 代码与研究制品

- 代码仓库：[https://github.com/Chenning-Tao/MICRO2026-Tenkai](https://github.com/Chenning-Tao/MICRO2026-Tenkai)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 8D](index.md) · [MICRO 2026 主页](../index.md)
