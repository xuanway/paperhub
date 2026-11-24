---
title: "STEP: Adaptive Spatio-Temporal Expert Prefetching for Low-Latency and Memory-Efficient MoE Inference"
description: "ISCA 2026 · Session 6A · STEP: Adaptive Spatio-Temporal Expert Prefetching for Low-Latency and Memory-Efficient MoE Inference"
tags:
  - "ISCA2026"
  - "Session 6A"
  - "LLM 4"
---

# STEP: Adaptive Spatio-Temporal Expert Prefetching for Low-Latency and Memory-Efficient MoE Inference

**中文标题：** STEP: 面向低延迟与内存高效 MoE 推理的自适应时空专家预取

**所属 Session：** [Session 6A](index.md) · [ISCA 2026](../index.md)

**作者：** Fangxin Liu, Ning Yang, Zongwu Wang, Chenyang Guan, Haomin Li, Yu Feng, Liqiang Lu, Xiang Li, Siran Yang, Jiamang Wang, Lin Qu, Li Jiang, Haibing Guan

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Large language models (LLMs) have driven significant advances in natural language processing, but their substantial memory and computational demands pose challenges for real-time deployment in memory- and bandwidth-constrained systems. Sparse Mixture-of-Experts (MoE) models mitigate these issues by selectively activating a subset of parameters per input, yet their irregular memory access patterns introduce significant latency and memory overhead. We propose STEP, an adaptive inference framework that optimizes MoE inference through spatio-temporal expert prefetching. STEP introduces layer-wise expert allocation to dynamically adjust the number of activated experts based on computational importance, reducing unnecessary computation and memory traffic. Additionally, it employs a predictive expert prefetching mechanism that leverages temporal locality and layer-specific predictability patterns to minimize access latency. By incorporating a token-aware adaptive window mechanism, STEP further enhances prefetch accuracy. Extensive evaluations on representative MoE models demonstrate that STEP achieves up to 3.12× speedup while maintaining model accuracy, outperforming state-of-the-art baselines in latency and memory efficiency under constrained memory budgets.

## 中文摘要

大语言模型（LLM）推动了自然语言处理领域的显著进步，但其巨大的内存与计算需求给在内存和带宽受限系统中的实时部署带来了挑战。稀疏专家混合（MoE）模型通过为每个输入选择性地激活一部分参数来缓解这些问题，但其不规则的内存访问模式引入了显著的延迟与内存开销。我们提出 STEP，一种通过时空专家预取来优化 MoE 推理的自适应推理框架。STEP 引入分层专家分配，根据计算重要性动态调整激活专家数量，减少不必要的计算与内存流量。此外，它采用预测式专家预取机制，利用时间局部性和各层特有的可预测模式来最小化访问延迟。通过引入令牌感知的自适应窗口机制，STEP 进一步提高了预取准确率。在代表性 MoE 模型上的大量评估表明，STEP 在保持模型精度的同时最高实现 3.12 倍加速，在受限内存预算下的延迟和内存效率方面优于最先进基线。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6A](index.md) · [返回 ISCA 2026](../index.md)
