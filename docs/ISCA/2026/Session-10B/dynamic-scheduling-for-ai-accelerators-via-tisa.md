---
title: "Dynamic Scheduling for AI Accelerators via TISA"
description: "ISCA 2026 · Session 10B · Dynamic Scheduling for AI Accelerators via TISA"
tags:
  - "ISCA2026"
  - "Session 10B"
  - "ML Accelerators 2"
---

# Dynamic Scheduling for AI Accelerators via TISA

**中文标题：** 基于 TISA 的 AI 加速器动态调度

**所属 Session：** [Session 10B](index.md) · [ISCA 2026](../index.md)

**作者：** Guanghui Song, Xiaoqiang Dan, Chengke Wang, Fei Liu, Wenyuan Lv, Zhongzhou Jiang, Jianjian Guan, Teng Lu, Lin Tao, Cheng Li, Weixing Pan, Wei Huang, Zirong Shen, Yi Yang, Hui Liu, Jie Zhao

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Modern AI accelerators suffer from low utilization because static compile-time schedules cannot adapt to runtime variability or coordinate heterogeneous units effectively. This paper presents a semantics-aware dynamic tile scheduling framework that restores the missing runtime semantics required for adaptive execution. It co-designs three synergistic components, including a semantics-preserving compiler that maintains operator boundaries and dependency types through lowering, a tile-level instruction set (TISA) that encodes typed dependencies, resource intents, and tile-level memory ranges, and a conflict-aware runtime scheduler that uses these semantics to dynamically reorder tiles, resolve contention, and overlap execution across tensor, vector, and DMA units. This design unifies software semantics and hardware scheduling, enabling cross-operator and cross-iteration parallelism beyond static approaches. Across ResNet50, BERT, GPT-J, and LLaMA2, our work achieves 1.52–1.92× speedups over the baseline, delivering 1.14–1.63× additional improvement over strong static tile-level pipeline scheduling; on FlashAttention-3 (head dim 128), it improves hardware utilization by 26.4% versus the state-of-the-art H100 implementation. Ablation studies further show that semantics preservation alone yields 1.2× gains, confirming the independent value of restoring scheduling information to runtime.

## 中文摘要

现代AI加速器存在利用率低的问题，因为静态编译时调度无法适应运行时变化，也无法有效协调异构单元。本文提出了一种语义感知的动态瓦片调度框架，恢复了自适应执行所需的缺失运行时语义。该框架协同设计了三个组成部分：一个保持语义的编译器，在降级过程中维护算子边界和依赖类型；一个瓦片级指令集（TISA），编码类型化依赖关系、资源意图和瓦片级内存范围；以及一个冲突感知的运行时调度器，利用这些语义动态地重排瓦片、解决冲突并在张量单元、向量单元和DMA单元之间重叠执行。这一设计统一了软件语义和硬件调度，实现了超越静态方法的跨算子和跨迭代并行。在ResNet50、BERT、GPT-J和LLaMA2上，我们的工作相比基线实现了1.52–1.92倍的加速，相比强静态瓦片级流水线调度额外提升了1.14–1.63倍；在FlashAttention-3（head dim 128）上，相比最先进的H100实现将硬件利用率提升了26.4%。消融研究进一步表明，仅语义保持一项就带来了1.2倍的收益，证实了将调度信息恢复到运行时的独立价值。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10B](index.md) · [返回 ISCA 2026](../index.md)
