---
title: "TEMPO: A Tag-Based Framework For Efficient Memory Ordering"
description: "MICRO 2026 · Session 3A · TEMPO：基于标签的高效内存顺序管理框架"
tags:
  - "MICRO2026"
---

# TEMPO: A Tag-Based Framework For Efficient Memory Ordering

**中文标题：** TEMPO：基于标签的高效内存顺序管理框架

**所属 Session：** [Session 3A](index.md) · [MICRO 2026](../index.md)

**作者：** Pranith Kumar, Prasun Gera, Hyojong Kim, Chulhyung Park, Hyesoon Kim

**来源：** MICRO 2026，pp. 878–894；[DOI](https://doi.org/10.1109/MICRO67795.2026.00072)

## 英文摘要

Weak-memory processors rely on ordering instructions for correctness, yet conventional implementations often enforce them more conservatively than the memory model requires. This over-enforcement manifests as drain-induced retirement stalls at ordering instructions and conservative squash/replay of speculative loads, suppressing legal executions and reducing throughput. We present TEMPO, a tag-based framework for precise microarchitectural implementation of ordering instructions. TEMPO assigns lightweight ordering tags to instructions and decomposes enforcement across retirement-time predicates and completion-time store ordering, allowing the core to enforce required ordering without conservative retirement serialization. TEMPO eliminates unnecessary retirement serialization at ordering instructions and speculative-load squash/replay. In our evaluation, TEMPO reduces geometric-mean normalized execution cycles by 7.9% on native four-thread workloads and improves geometric-mean IPC by 15.9% on an instrumented SPEC2017 dynamic binary translation (DBT) proxy for cross-ISA execution (e.g., x86-on-Arm), while adding only 262 bytes per core.

## 中文摘要

采用弱内存模型的处理器依靠内存顺序指令保证正确性，但传统实现施加的约束通常比内存模型本身要求的更保守。这种过度约束表现为：顺序指令需要等待先前操作排空，从而导致指令提交停顿；以及对推测加载进行保守的取消与重放。这些行为限制了本来合法的执行，降低吞吐量。本文提出 TEMPO，一种利用标签精确实现内存顺序指令微架构语义的框架。TEMPO 为指令分配轻量级顺序标签，并将约束实施分解为提交时的谓词检查与完成时的存储排序，使处理器核能够在不保守串行化提交的情况下满足所需顺序。TEMPO 消除了顺序指令处不必要的提交串行化，以及不必要的推测加载取消与重放。评估表明，在原生四线程工作负载上，TEMPO 使归一化执行周期数的几何平均值降低 7.9%；在用于模拟跨指令集执行（例如在 Arm 上执行 x86 程序）的插桩 SPEC2017 动态二进制翻译（DBT）代理工作负载上，IPC 的几何平均值提高 15.9%。每个处理器核的额外存储开销仅为 262 字节。

## 中文关键词

内存一致性；内存屏障；释放一致性；推测执行；处理器微架构

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/pranith/gem5/tree/micro59](https://github.com/pranith/gem5/tree/micro59)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21539206](https://doi.org/10.5281/zenodo.21539206)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 3A](index.md) · [MICRO 2026 主页](../index.md)
