---
title: "Einsum Trees: An Abstraction for Optimizing the Execution of Tensor Expressions"
description: "ASPLOS 2025 · Session 9A · Einsum Trees：面向张量表达式执行优化的抽象"
tags:
  - "ASPLOS2025"
  - "Session 9A"
  - "ML Compilers"
---

# Einsum Trees: An Abstraction for Optimizing the Execution of Tensor Expressions

**中文标题：** Einsum Trees：面向张量表达式执行优化的抽象

**所属 Session：** [Session 9A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Alexander Breuer (Friedrich Schiller University Jena), Mark Blacher (Friedrich Schiller University Jena), Max Engel (Friedrich Schiller University Jena), Joachim Giesen (Friedrich Schiller University Jena), Alexander Heinecke (Intel Corporation), Julien Klaus (Friedrich Schiller University Jena), Stefan Remke (Friedrich Schiller University Jena)

**单位：** Friedrich Schiller University Jena；Intel Corporation

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716254) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Einsum is a declarative language for tensor expressions that specifies an output tensor in terms of several input tensors. However, it does not specify how to compute the output tensor from the input tensors. A typical computational backend for the einsum language comprises two parts: First, a contraction path algorithm that breaks down an einsum expression into a sequence of binary tensor contractions. Second, the execution of the binary contractions. For efficient binary contractions, the data layout of the tensors must be optimized. So far, the computation of contraction paths and the optimization of the data layout for single, that is, local, binary tensor contractions have been studied in isolation. For optimizing the overall execution times of einsum expressions, we introduce Einsum Tree IR, an intermediate representation for globally optimizing the data layout for a given contraction path. We illustrate the effectiveness of the approach on a state-of-the-art Arm server processor, an x86 server processor, and an x86 desktop system.

## 中文摘要

Einsum 是一种用于张量表达式的声明式语言，它通过若干输入张量来指定一个输出张量。然而，它并不规定如何由输入张量计算出该输出张量。einsum 语言的典型计算后端由两部分组成：第一，一个收缩路径算法，将 einsum 表达式分解为一系列二元张量收缩；第二，这些二元收缩的执行。为实现高效的二元收缩，必须对张量的数据布局进行优化。迄今为止，收缩路径的计算与针对单个（即局部）二元张量收缩的数据布局优化一直是相互孤立地研究的。为了优化 einsum 表达式的整体执行时间，我们提出 Einsum Tree IR，一种针对给定收缩路径对数据布局进行全局优化的中间表示。我们在最先进的 Arm 服务器处理器、x86 服务器处理器以及 x86 桌面系统上展示了该方法的有效性。

## 英文关键词

tensor compiler; einsum; intermediate representation; dense linear algebra

## 中文关键词

张量编译器；einsum；中间表示；稠密线性代数

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716254)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9A](index.md) · [返回 ASPLOS 2025](../index.md)
