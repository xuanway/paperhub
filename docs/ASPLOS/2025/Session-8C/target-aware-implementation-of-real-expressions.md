---
title: "Target-Aware Implementation of Real Expressions"
description: "ASPLOS 2025 · Session 8C · 实数表达式的目标感知实现"
tags:
  - "ASPLOS2025"
  - "Session 8C"
  - "Potpourri 2"
---

# Target-Aware Implementation of Real Expressions

**中文标题：** 实数表达式的目标感知实现

**所属 Session：** [Session 8C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Brett Saiki (University of Washington), Jackson Brough (University of Utah), Jonas Regehr (University of Utah), Jesus Ponce (University of Utah), Varun Pradeep (University of Washington), Aditya Akhileshwaran (University of Washington), Zachary Tatlock (University of Washington), Pavel Panchekha (University of Utah)

**单位：** University of Washington；University of Utah

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707277) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

New low-precision accelerators, vector instruction sets, and library functions make maximizing accuracy and performance of numerical code increasingly challenging. Two lines of work—traditional compilers and numerical compilers— attack this problem from opposite directions. Traditional compiler backends optimize for specific target environments but are limited in their ability to balance performance and accuracy. Numerical compilers trade off accuracy and performance, or even improve both, but ignore the target environment. We join aspects of both to produce Chassis, a target-aware numerical compiler. Chassis compiles mathematical expressions to operators from a target description, which lists the real expressions each operator approximates and estimates its cost and accuracy. Chassis then uses an iterative improvement loop to optimize for speed and accuracy. Specifically, a new instruction selection modulo equivalence algorithm efficiently searches for faster target-specific programs, while a new cost-opportunity heuristic supports iterative improvement. We demonstrate Chassis' capabilities on 9 different targets, including hardware ISAs, math libraries, and programming languages. Chassis finds better accuracy and performance trade-offs than both Clang (by 3.5×) or Herbie (by up to 2.0×) by leveraging low-precision accelerators, accuracy-optimized numerical helper functions, and library subcomponents. Attribution International 4.0 License.

## 中文摘要

新的低精度加速器、向量指令集与库函数，使得最大化数值代码的精度与性能日益困难。传统编译器与数值编译器这两条研究工作路线从相反的方向着手解决这一问题。传统编译器后端针对特定的目标环境进行优化，但在权衡性能与精度方面能力有限。数值编译器在精度与性能之间进行权衡、甚至同时提升二者，但忽略了目标环境。我们融合两者的思想，提出 Chassis——一个目标感知的数值编译器。Chassis 将数学表达式编译为目标描述中的算子，该描述列出了每个算子所近似的实数表达式，并估计其代价与精度。随后，Chassis 使用迭代改进循环来优化速度与精度。具体而言，一种新的模等价指令选择算法能够高效搜索更快的目标特定程序，而一种新的代价-机会启发式则支撑迭代改进。我们在 9 个不同目标上展示了 Chassis 的能力，包括硬件 ISA、数学库与编程语言。通过利用低精度加速器、精度优化的数值辅助函数以及库子组件，Chassis 找到了比 Clang（3.5 倍）与 Herbie（最高 2.0 倍）都更好的精度与性能权衡。

## 英文关键词

Floating point, domain-specific compilation, optimization, equality saturation

## 中文关键词

浮点；领域特定编译；优化；等式饱和

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707277)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8C](index.md) · [返回 ASPLOS 2025](../index.md)
