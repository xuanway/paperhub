---
title: "Lambda-trim: Reducing Monetary and Performance Cost of Serverless Cold Starts with Cost-driven Application Debloating"
description: "ASPLOS 2026 · Session 8B · Lambda-trim：通过成本驱动的应用去膨胀降低无服务器冷启动的金钱成本与性能代价"
tags:
  - "ASPLOS2026"
  - "Session 8B"
  - "Serverless & Cloud Networking"
---

# Lambda-trim: Reducing Monetary and Performance Cost of Serverless Cold Starts with Cost-driven Application Debloating

**中文标题：** Lambda-trim：通过成本驱动的应用去膨胀降低无服务器冷启动的金钱成本与性能代价

**所属 Session：** [Session 8B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Spyros Pavlatos (University of Pennsylvania), Xuting Liu (University of Pennsylvania), Yuhao Liu (University of Pennsylvania), Vincent Liu (University of Pennsylvania)

**单位：** University of Pennsylvania

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736129) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

**出版标题：** λ-trim: Optimizing Function Initialization in Serverless Applications With Cost-driven Debloating

## 英文摘要

In this paper, we focus on an often-overlooked component of serverless application cold starts: monetary costs and Function Initialization. Traditionally considered the user's responsibility, Function Initialization is billable and accounts for more than 50% of the monetary cost associated with cold starts in real-world machine-learning applications. We introduce 𝜆-trim, a system that optimizes Python serverless applications by eliminating redundant code while maintaining correctness. To maximize cost savings, 𝜆-trim leverages the typical serverless pricing model to prioritize modules that significantly impact latency and memory usage. 𝜆-trim features an automated pipeline comprising a static analyzer, a profiler specialized for the serverless pricing model, and a debloater. The optimized application can be directly deployed on serverless platforms, leading to substantial reductions in both latency and cost for cold starts.

## 中文摘要

在本文中，我们关注无服务器应用冷启动中一个常被忽视的组成部分：金钱成本与函数初始化（Function Initialization）。函数初始化传统上被视为用户的责任，但它需要计费，并且在真实机器学习应用中占冷启动相关金钱成本的一半以上。我们提出 𝜆-trim，一个通过消除冗余代码来优化 Python 无服务器应用并保持正确性的系统。为最大化成本节省，𝜆-trim 利用典型的无服务器定价模型，优先处理对延迟和内存使用有显著影响的模块。𝜆-trim 具备一条自动化流水线，包括静态分析器、专为无服务器定价模型定制的 profiler 以及去膨胀器。优化后的应用可直接部署到无服务器平台上，从而大幅降低冷启动的延迟与成本。

## 英文关键词

Serverless computing, cold starts, debloating

## 中文关键词

无服务器计算；冷启动；去膨胀

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736129)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。
> 论文集印刷标题：「Λ-TRIM: Optimizing Function Initialization in Serverless Applications With Cost-driven Debloating」。

[返回 Session 8B](index.md) · [返回 ASPLOS 2026](../index.md)
