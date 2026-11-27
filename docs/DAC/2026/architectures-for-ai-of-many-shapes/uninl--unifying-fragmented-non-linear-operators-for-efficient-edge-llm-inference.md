UniNL: Unifying Fragmented Non-Linear Operators for Efficient Edge LLM Inference
Authors：
[Zhengxuan Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=9135208420643053282)，[zhihua fan](https://63dac.conference-program.com/?post_type=page&p=15&uid=2114510187179282683)，[Shantian Qin](https://63dac.conference-program.com/?post_type=page&p=15&uid=3401221396247158073)，[Yudong Mu](https://63dac.conference-program.com/?post_type=page&p=15&uid=42710744631919108141)，[Wenming Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=180243)，[Xiaochun Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=280243)

## 中文标题

UniNL：统一碎片化非线性算子，实现高效边缘 LLM 推理

## 英文摘要

Deploying large language models (LLMs) on edge devices is critical for user privacy and low-latency inference. However, existing matrix-centric LLM accelerators only provide limited throughput for fragmented non-linear operators under tight edge resource constraints. Moreover, lacking a general fusion mechanism causes severe PE array underutilization. To address these challenges, we propose UniNL, a unified execution framework to efficiently execute LLM non-linear operators. First, an abstraction model decomposes non-linear operators into primitives, leveraging polynomial approximation to enable point-wise execution on the PE array. Second, lightweight microarchitectural extensions efficiently support these primitives. Finally, a primitive-aware fusion mechanism hides nonlinear latency behind matrix operations. Experiments demonstrate that UniNL achieves an average 6.89× speedup and 7.26× higher energy efficiency over a Jetson AGX Orin baseline, and outperforms state-of-the-art designs by 1.46× and 1.35× on average.

## 中文摘要

在边缘设备上部署大型语言模型（LLM）对于用户隐私与低延迟推理至关重要。然而，现有的以矩阵为中心的 LLM 加速器在紧张的边缘资源约束下，对碎片化的非线性算子只能提供有限的吞吐。此外，缺乏通用的融合机制导致 PE 阵列严重利用不足。为应对这些挑战，我们提出 UniNL，一个高效执行 LLM 非线性算子的统一执行框架。首先，一个抽象模型将非线性算子分解为原语，并借助多项式近似使其能在 PE 阵列上逐点执行。其次，轻量级的微架构扩展高效支持这些原语。最后，原语感知的融合机制将非线性延迟隐藏在矩阵运算之后。实验表明，相较于 Jetson AGX Orin 基线，UniNL 平均取得 6.89× 的加速比与 7.26× 的能效提升，并平均优于当前最先进设计 1.46× 与 1.35×。

## 英文关键词

Large Language Model (LLM), Accelerator, Non-Linear Operators

## 中文关键词

大型语言模型（LLM）、加速器、非线性算子
