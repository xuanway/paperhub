---
title: "Revisiting Global Value Prediction: A Resurgent Complement to Local Predictors"
description: "ISCA 2026 · Session 3D · Revisiting Global Value Prediction: A Resurgent Complement to Local Predictors"
tags:
  - "ISCA2026"
  - "Session 3D"
  - "Microarchitexture"
---

# Revisiting Global Value Prediction: A Resurgent Complement to Local Predictors

**中文标题：** 重新审视全局值预测：局部预测器再度崛起的互补方案

**所属 Session：** [Session 3D](index.md) · [ISCA 2026](../index.md)

**作者：** Ling Yang, Libo Huang, Zhong Zheng, Bingcai Sui, Sheng Ma, Yongwen Wang, Li Shen, Junhui Wang, Gang Chen, Qianming Yang, Songwen Pei, Weixia Xu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Value prediction is a microarchitectural technique that improves instruction-level parallelism by speculatively predicting the outcomes of instructions and eliminating data dependencies. While local value predictors have seen substantial progress by exploiting context-sensitive value locality, global value prediction remains relatively underexplored due to practical limitations such as inaccurate prediction, value delay constraint, and excessive hardware cost. This paper revisits global value prediction with a focus on addressing these long-standing challenges and presents EgDiff, a redesigned global predictor that introduces aggressive confidence mechanisms tailored for deep pipelines, performs non-speculative updates using committed values to preserve critical correlations, and employs deferred prediction to avoid premature decisions based on incomplete global history. To reduce hardware overhead, EgDiff uses a distance polling technique that compresses the predictor table by over 95% without sacrificing accuracy. Experimental results show that EgDiff achieves more than 99% accuracy and delivers a 4.37% average IPC speedup. When combined with EVES, a state-of-the-art local predictor, a compact 19KB hybrid achieves a 6.16% speedup, already surpassing 32KB EVES alone (4.81%). With unlimited storage, the hybrid further reaches a 7.02% speedup. These findings demonstrate that global and local value prediction are complementary, and that revisiting global prediction with modern design principles offers practical and significant benefits in processor.

## 中文摘要

值预测是一种微架构技术，它通过推测性地预测指令结果并消除数据依赖来提升指令级并行度。尽管局部值预测器通过利用上下文相关的值局部性取得了长足进展，但由于预测不准确、值延迟约束以及硬件成本过高等实际限制，全局值预测相对而言仍探索不足。本文重新审视全局值预测，聚焦于解决这些长期存在的挑战，并提出 EgDiff，一个重新设计的全局预测器：它引入了针对深流水线定制的激进置信度机制，使用已提交的值进行非推测性更新以保留关键相关性，并采用延迟预测以避免基于不完整的全局历史过早做出决定。为降低硬件开销，EgDiff 使用一种距离轮询技术，在不损失准确率的情况下将预测器表压缩超过 95%。实验结果表明，EgDiff 达到 99% 以上的准确率，并带来平均 4.37% 的 IPC 加速。当与最先进的局部预测器 EVES 结合时，一个紧凑的 19KB 混合预测器取得 6.16% 的加速，已经超过单独的 32KB EVES（4.81%）。在存储不受限的情况下，该混合方案进一步达到 7.02% 的加速。这些发现表明，全局与局部值预测是互补的，并且以现代设计原则重新审视全局预测能为处理器带来实用而显著的收益。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3D](index.md) · [返回 ISCA 2026](../index.md)
