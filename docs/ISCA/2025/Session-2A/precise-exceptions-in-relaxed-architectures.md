---
title: "Precise Exceptions in Relaxed Architectures"
description: "ISCA 2025 · Session 2A · 松弛架构中的精确异常"
tags:
  - "ISCA2025"
  - "Session 2A"
  - "Best Paper Nominees"
---

# Precise Exceptions in Relaxed Architectures

**中文标题：** 松弛架构中的精确异常

**所属 Session：** [Session 2A](index.md) · [ISCA 2025](../index.md)

**作者：** Ben Simner, Alasdair Armstrong, Thomas Bauereiss, Brian Campbell, Ohad Kammar, Jean Pichon-Pharabod, Peter Sewell

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731102) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

To manage exceptions, software relies on a key architectural guarantee, precision: that exceptions appear to execute between instructions. However, this definition, dating back over 60 years, fundamentally assumes a sequential programmers model. Modern architectures such as Arm-A with programmer-observable relaxed behaviour make such a naive definition inadequate, and it is unclear exactly what guarantees programmers have on exception entry and exit.

In this paper, we clarify the concepts needed to discuss exceptions in the relaxed-memory setting – a key aspect of precisely specifying the architectural interface between hardware and software. We explore the basic relaxed behaviour across exception boundaries, and the semantics of external aborts, using Arm-A as a representative modern architecture. We identify an important problem, present yet unexplored for decades: pinning down what it means for exceptions to be precise in a relaxed setting. We describe key phenomena that any definition should account for. We develop an axiomatic model for Arm-A precise exceptions, tooling for axiomatic model execution, and a library of tests. Finally we explore the relaxed semantics of software-generated interrupts, as used in sophisticated programming patterns, and sketch how they too could be modelled.

## 中文摘要

软件管理异常依赖一项核心架构保证：精确性，即异常表现为在指令之间发生。然而，这个已有六十余年历史的定义，本质上建立在顺序编程模型之上。对于Arm-A这类具备程序员可见松弛内存行为的现代架构，该简单定义已经不再适用；程序员在异常进入与退出环节究竟能获得哪些保证，目前尚不明确。

本文厘清了在松弛内存环境下讨论异常所需的一系列概念，这是精确定义软硬件之间架构接口的关键。我们以Arm-A作为现代代表性架构，研究跨越异常边界的基础松弛行为，以及外部中止的语义。本文指出一个数十年来尚未被深入探讨的重要问题：界定松弛内存模型下“异常是精确的”究竟意味着什么。我们描述了任何定义都必须考虑的关键现象；构建了面向Arm-A精确异常的公理模型、公理模型执行工具以及测试用例库。最后，我们研究了复杂编程范式中用到的软件触发中断的松弛语义，并简要说明这类中断同样可以被建模。

## 英文关键词

Computer architecture, relaxed memory, exceptions and interrupts, exception handling, semantics

## 中文关键词

计算机体系结构, 松弛内存模型, 异常与中断, 异常处理, 语义

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731102)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 2A](index.md) · [返回 ISCA 2025](../index.md)
