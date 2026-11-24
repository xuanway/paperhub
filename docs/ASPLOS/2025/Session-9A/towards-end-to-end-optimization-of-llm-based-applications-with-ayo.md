---
title: "Towards End-to-End Optimization of LLM-based Applications with Ayo"
description: "ASPLOS 2025 · Session 9A · Ayo：面向基于 LLM 应用的端到端优化"
tags:
  - "ASPLOS2025"
  - "Session 9A"
  - "ML Compilers"
---

# Towards End-to-End Optimization of LLM-based Applications with Ayo

**中文标题：** Ayo：面向基于 LLM 应用的端到端优化

**所属 Session：** [Session 9A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Xin Tan (The Chinese University of Hong Kong), Yimin Jiang (Unaffiliated), Yitao Yang (The Chinese University of Hong Kong), Hong Xu (The Chinese University of Hong Kong)

**单位：** The Chinese University of Hong Kong；Unaffiliated

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716278) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Large language model (LLM)-based applications consist of both LLM and non-LLM components, each contributing to the end-to-end latency. Despite great efforts to optimize LLM inference, end-to-end workflow optimization has been overlooked. Existing frameworks employ coarse-grained orchestration with task modules, which confines optimizations to within each module and yields suboptimal scheduling decisions. We propose fine-grained end-to-end orchestration, which utilizes task primitives as the basic units and represents each query's workflow as a primitive-level dataflow graph. This explicitly exposes a much larger design space, enables optimizations in parallelization and pipelining across primitives of different modules, and enhances scheduling to improve application-level performance. We build Ayo, a novel orchestration framework for LLM-based applications that implements this scheme. Comprehensive experiments show that Ayo can achieve up to 2.09x speedup over existing systems across various popular LLM applications.

## 中文摘要

基于大语言模型（LLM）的应用同时包含 LLM 组件与非 LLM 组件，二者都会对端到端时延产生影响。尽管在优化 LLM 推理方面已有大量努力，但端到端工作流优化仍被忽视。现有框架采用以任务模块为单位的粗粒度编排，这使优化被局限在每个模块内部，并产生次优的调度决策。我们提出细粒度的端到端编排，它以任务原语（task primitive）作为基本单位，并将每个查询的工作流表示为原语级数据流图。这显式地暴露出大得多的设计空间，使跨不同模块原语的并行化与流水线优化成为可能，并增强调度以提升应用级性能。我们构建了 Ayo，一个实现该方案、面向基于 LLM 应用的新颖编排框架。全面的实验表明，在多种流行的 LLM 应用中，Ayo 相较现有系统最高可获得 2.09 倍的加速。

## 英文关键词

large language model, ML inference, resource scheduling

## 中文关键词

大语言模型；机器学习推理；资源调度

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716278)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9A](index.md) · [返回 ASPLOS 2025](../index.md)
