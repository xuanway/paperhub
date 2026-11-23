---
title: "AMALI: An Analytical Model for Accurately Modeling LLM Inference on Modern GPUs"
description: "ISCA 2025 · Session 8A · AMALI：精确建模现代 GPU 上 LLM 推理的分析模型"
tags:
  - "ISCA2025"
  - "Session 8A"
  - "Performance and Modeling"
---

# AMALI: An Analytical Model for Accurately Modeling LLM Inference on Modern GPUs

**中文标题：** AMALI：精确建模现代 GPU 上 LLM 推理的分析模型

**所属 Session：** [Session 8A](index.md) · [ISCA 2025](../index.md)

**作者：** Shiheng Cao, Zhibin Yu, Junshi Chen, Hong An, Junmin Wu

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731064) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Large language model (LLM) inference applications are surging in recent years, which largely relies on modern GPUs. On the other hand, GPU analytical model is a commonly used tool for archi- tects to precisely identify bottlenecks quickly with deep insights. However, existing GPU analytical models fall short of accurately modeling LLM inference applications on modern GPUs, because of unsuitable tensor core modeling, ignoring constant cache as well as instruction cache modeling and abstracting away important details for LLM inference applications. To address this problem, we propose a novel analytical model dubbed AMALI to accurately model LLM inference on modern GPUs with three innovations. First, we develop an instruction modifier and throughput based tensor core model by accurately capturing the math pipe throttle stalls to enhance the architec- ture modeling for modern GPUs. Second, we propose analytical models for constant cache and instruction cache by developing micro-benchmarks to measure CUDA kernel launching latencies. This significantly improves AMALI’s accuracy compared to real GPU hardware. Finally, we design a multi-warp model by leverag- ing warp instruction number distribution to reflect LLM inference application characteristics. We validate AMALI on an A100 GPU by using typical LLM in- ference applications. The results show that AMALI reduces the MAPE (mean absolute percentage error) from 127.56% to 23.59% compared to the state-of-the-art GCoM model. We further show- case that AMALI can be used to explore architecture design space by designing the tensor core capability of H100. The results show that AMALI accurately predicts the end-to-end performance im- provements with the enhanced tensor core capability.

## 中文摘要

大语言模型（LLM）推理应用近年快速增长，这类业务高度依赖现代GPU。GPU解析模型是体系结构研究者常用工具，能够快速定位瓶颈、提供深度分析。但现有GPU解析模型难以精准刻画现代GPU上的LLM推理负载：张量核心建模不够贴合、忽略常量缓存与指令缓存，并且对LLM推理的关键细节做了过度简化。

针对该问题，本文提出AMALI，一款面向现代GPU、用于LLM推理精准建模的全新解析模型，包含三项创新：第一，构建基于指令修饰符与吞吐的张量核心模型，精准捕捉数学流水线节流阻塞，提升现代GPU架构建模精度；第二，基于微基准测试测量CUDA核启动延迟，建立常量缓存与指令缓存的解析模型，显著提升模型与真实硬件的吻合度；第三，利用warp指令数量分布设计多warp模型，还原LLM推理的负载特征。

本文在A100 GPU上基于典型LLM推理负载对AMALI进行验证。结果表明：对比前沿GCoM模型，AMALI将平均绝对百分比误差（MAPE）从127.56%降至23.59%。我们还以H100张量核心能力配置为例，展示AMALI支持架构设计空间探索；实验证明，该模型可以准确预测张量核心增强带来的端到端性能提升。

## 英文关键词

graphics processing units, performance modeling, interval analysis

## 中文关键词

图形处理器, 性能建模, 区间分析

## 代码与研究制品

- [代码仓库](https://github.com/ShihengCao/AMALi)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731064)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8A](index.md) · [返回 ISCA 2025](../index.md)
