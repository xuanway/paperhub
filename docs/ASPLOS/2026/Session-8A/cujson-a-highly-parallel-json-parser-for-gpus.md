---
title: "cuJSON: A Highly Parallel JSON Parser for GPUs"
description: "ASPLOS 2026 · Session 8A · cuJSON：面向 GPU 的高度并行 JSON 解析器"
tags:
  - "ASPLOS2026"
  - "Session 8A"
  - "GPU Programming"
---

# cuJSON: A Highly Parallel JSON Parser for GPUs

**中文标题：** cuJSON：面向 GPU 的高度并行 JSON 解析器

**所属 Session：** [Session 8A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Ashkan Vedadi Gargary (University of California, Riverside), Soroosh Safari Loaliyan (University of California, Riverside), Zhijia Zhao (University of California, Riverside)

**单位：** University of California, Riverside

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762222) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

JSON (JavaScript Object Notation) data is widely used in modern computing, yet its parsing performance can be a major bottleneck. Conventional wisdom suggests that GPUs are ill-suited for parsing due to the branch-heavy nature of parsing algorithms. This work challenges that notion by presenting cuJSON, a novel JSON parser built on a new parsing algorithm, specifically tailored for GPU architectures with minimal branching and maximal parallelism. cuJSON offloads three main phases of JSON parsing to the GPU, including (i) UTF validation, (ii) tokenization, and (iii) nesting structure recognition. Each phase is powered by a parallel algorithm optimized for GPUs, leveraging intrinsic GPU functions and high-performance CUDA libraries for acceleration. To maximize parsing speed, cuJSON's output format is also designed to facilitate parallel construction. Finally, cuJSON can break key dependencies in the parsing process, enabling parallel parsing of a single large JSON file effectively. Evaluation shows that cuJSON not only outperforms highly optimized CPU-based parsers like simdjson and Pison but also surpasses existing GPU-based parsers like cuDF and GPJSON, in terms of both functionality and performance. The source code of cuJSON is

## 中文摘要

JSON（JavaScript Object Notation）数据在现代计算中被广泛使用，然而其解析性能可能成为主要瓶颈。传统观点认为，由于解析算法具有分支密集的特性，GPU 并不适合用于解析。本工作通过提出 cuJSON 来挑战这一观念：cuJSON 是一种基于新解析算法构建的新型 JSON 解析器，专为 GPU 架构量身定制，具有最少的分支和最大的并行性。cuJSON 将 JSON 解析的三个主要阶段卸载到 GPU，包括 (i) UTF 验证、(ii) 分词和 (iii) 嵌套结构识别。每个阶段都由针对 GPU 优化的并行算法驱动，利用 GPU 内建函数和高性能 CUDA 库进行加速。为最大化解析速度，cuJSON 的输出格式也被设计为便于并行构建。最后，cuJSON 能够打破解析过程中的关键依赖，从而有效地并行解析单个大型 JSON 文件。评估表明，无论从功能还是性能来看，cuJSON 不仅优于 simdjson 和 Pison 等高度优化的 CPU 解析器，也超越了 cuDF 和 GPJSON 等现有 GPU 解析器。cuJSON 的源代码位于

## 英文关键词

JSON; Parsing; GPU; Parallel Parsing; GPU-based Parsing; UTF Validation; Tokenization

## 中文关键词

JSON；解析；GPU；并行解析；基于 GPU 的解析；UTF 验证；分词

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762222)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8A](index.md) · [返回 ASPLOS 2026](../index.md)
