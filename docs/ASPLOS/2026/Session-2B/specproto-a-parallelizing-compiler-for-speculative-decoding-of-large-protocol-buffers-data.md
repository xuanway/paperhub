---
title: "SpecProto: A Parallelizing Compiler for Speculative Decoding of Large Protocol Buffers Data"
description: "ASPLOS 2026 · Session 2B · SpecProto：一种面向大规模 Protocol Buffers 数据投机解码的并行化编译器"
tags:
  - "ASPLOS2026"
  - "Session 2B"
  - "Speculative Decoding"
---

# SpecProto: A Parallelizing Compiler for Speculative Decoding of Large Protocol Buffers Data

**中文标题：** SpecProto：一种面向大规模 Protocol Buffers 数据投机解码的并行化编译器

**所属 Session：** [Session 2B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zhijie Wang (University of California, Riverside), Chales Hong (University of California, Riverside), Dhruv Parmar (University of California, Riverside), Shengbo Ma (University of California, Riverside), Zhijia Zhao (University of California, Riverside), Qidong Zhao (Google), Xu Liu (Google)

**单位：** University of California, Riverside；Google

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790225) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Protobuf is a widely used data serialization format, especially in cloud environments. However, existing compilers generate only serial decoders, limiting scalability for large datasets. While parallel parsing has been studied for textual formats (e.g., XML), parallel decoding of binary formats like Protobuf remains unexplored, which present unique opportunities. We propose two techniques to enable parallel Protobuf decoding. First, we leverage the length-prefixed encoding of Protobuf to “skim” the binary and identify decoding tasks. To address inefficiencies caused by many small or imbalanced fields, we further introduce speculative parallelization, which partitions a binary into even segments and predicts decoding states across boundaries. We implement these techniques in SpecProto, a parallelizing compiler that generates parallel decoders for a given Protobuf schema. Experiments on realworld and synthetic datasets show that SpecProto achieves significant speedups by leveraging multiple CPU cores.

## 中文摘要

Protobuf 是一种被广泛使用的数据序列化格式，尤其在云环境中。然而，现有编译器只生成串行解码器，限制了对大规模数据集的可扩展性。尽管并行解析已针对文本格式（如 XML）得到研究，但像 Protobuf 这类二进制格式的并行解码仍未被探索，其中蕴含着独特的机遇。我们提出两项技术以实现并行 Protobuf 解码。首先，我们利用 Protobuf 的长度前缀编码来“略读”二进制数据并识别解码任务。为解决由大量小字段或不均衡字段引起的低效问题，我们进一步引入投机并行化，它将二进制数据划分为大小均匀的段并跨边界预测解码状态。我们在 SpecProto 中实现了这些技术，这是一个为给定 Protobuf schema 生成并行解码器的并行化编译器。在真实世界与合成数据集上的实验表明，SpecProto 通过利用多核 CPU 实现了显著的加速。

## 英文关键词

Protocol Buffers, Parallel Decoding, Binary Data Processing, Multicore Systems, Speculative Parallelization

## 中文关键词

Protocol Buffers；并行解码；二进制数据处理；多核系统；投机并行化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790225)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2B](index.md) · [返回 ASPLOS 2026](../index.md)
