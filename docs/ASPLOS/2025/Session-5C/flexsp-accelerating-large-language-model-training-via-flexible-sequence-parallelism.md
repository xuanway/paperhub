---
title: "FlexSP: Accelerating Large Language Model Training via Flexible Sequence Parallelism"
description: "ASPLOS 2025 · Session 5C · FlexSP：通过灵活序列并行加速大语言模型训练"
tags:
  - "ASPLOS2025"
  - "Session 5C"
  - "Large Language Models"
---

# FlexSP: Accelerating Large Language Model Training via Flexible Sequence Parallelism

**中文标题：** FlexSP：通过灵活序列并行加速大语言模型训练

**所属 Session：** [Session 5C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yujie Wang (Peking University), Shiju Wang (Beihang University), Shenhan Zhu (Peking University), Fangcheng Fu (Peking University), Xinyi Liu (Peking University), Xuefeng Xiao (ByteDance Inc.), Huixia Li (ByteDance Inc.), Jiashi Li (ByteDance Inc.), Faming Wu (ByteDance Inc.), Bin Cui (Peking University)

**单位：** Peking University；Beihang University；ByteDance Inc.

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715998) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Extending the context length (i.e., the maximum supported sequence length) of LLMs is of paramount significance. To facilitate long context training of LLMs, sequence parallelism has emerged as an essential technique, which scatters each input sequence across multiple devices and necessitates communication to process the sequence. In essence, existing sequence parallelism methods assume homogeneous sequence lengths (i.e., all input sequences are equal in length) and therefore leverages a single, static scattering strategy for all input sequences. However, in reality, the sequence lengths in LLM training corpora exhibit substantial variability, often following a long-tail distribution, which leads to workload heterogeneity. ∗School of Computer Science & Key Lab of High Confidence Software Technologies (MOE), Peking University †Institute of Computational Social Science, Peking University (Qingdao) In this paper, we show that employing a single, static strategy results in inefficiency and resource under-utilization, highlighting the need for adaptive approaches to handle the heterogeneous workloads across sequences. To address this, we propose a heterogeneity-adaptive sequence parallelism method. For each training step, our approach captures the variability in sequence lengths and assigns the optimal combination of scattering strategies based on workload characteristics. We model this problem as a linear programming optimization and design an efficient and effective solver to find the optimal solution. Furthermore, we implement our method in a high-performance system that supports adaptive parallelization in distributed LLM training. Experimental results demonstrate that our system outperforms state-ofthe-art training frameworks by up to 1.98×.

## 中文摘要

扩展 LLM 的上下文长度（即最大支持的序列长度）具有至关重要的意义。为支撑 LLM 的长上下文训练，序列并行已成为一项关键技术，它将每条输入序列分散到多个设备上，并且需要通信才能处理该序列。本质上，现有序列并行方法假设序列长度同构（即所有输入序列长度相等），因而对所有输入序列都采用单一、静态的分散策略。然而在实际中，LLM 训练语料中的序列长度存在很大差异，往往服从长尾分布，从而导致工作负载异构。∗School of Computer Science & Key Lab of High Confidence Software Technologies (MOE), Peking University †Institute of Computational Social Science, Peking University (Qingdao) 在本文中，我们表明采用单一静态策略会造成效率低下与资源利用不足，凸显出需要自适应方法来处理不同序列间的异构工作负载。为此，我们提出一种异构自适应的序列并行方法。在每个训练步中，我们的方法捕获序列长度的变化，并依据工作负载特征分配最优的分散策略组合。我们将该问题建模为线性规划优化问题，并设计了高效且有效的求解器来寻找最优解。进一步地，我们将该方法实现为一个高性能系统，支持分布式 LLM 训练中的自适应并行化。实验结果表明，我们的系统相比最先进的训练框架最高取得 1.98× 的加速。

## 英文关键词

Distributed LLM Training; Sequence Parallelism; Flexible Strategies; Heterogeneous Workloads

## 中文关键词

分布式 LLM 训练；序列并行；灵活策略；异构工作负载

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715998)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5C](index.md) · [返回 ASPLOS 2025](../index.md)
