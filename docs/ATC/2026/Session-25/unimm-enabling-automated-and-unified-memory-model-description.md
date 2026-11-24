# UniMM: Enabling Automated and Unified Memory Model Description

**中文标题**：UniMM：实现自动化与统一的内存模型描述

**所属 Session**：[Session 25: Formal Methods and Verification](index.md) · [ATC 2026](../index.md)

**作者**：Chen Gao (Lanzhou University), Xiangwei Meng (Lanzhou University), Fengyuan Ren (Lanzhou University / Tsinghua University)

## 英文摘要
Various instruction set architectures (ISAs) define their proprietary memory model. The precise description of memory models is crucial for both hardware and software developers. The axiomatic models are generally employed to describe memory consistency. Although axiomatic models can precisely describe concurrent behaviors in shared memory, the process of deriving them relies on manual effort by experts, and their complexity imposes challenges for developers to understand them accurately. Additionally, axiomatic models lack compatibility, which hinders autonomous comparison and analysis. This work introduces UniMM, a memory model description framework that uses a unified format called ModelTable to describe memory models automatically. ModelTable is an accurate, readable, comparable, and analyzable format that describes whether any pair of memory accesses is ordered. To demonstrate the broad applicability of UniMM, two practical widgets are developed as case studies. For software developers, a memory model gap-bridging widget is designed to provide correct and high-performance schemes for cross-ISA software migration. For hardware developers, a memory model compliance testing widget is designed to generate a litmus test suite and determine whether a CPU complies with the memory model specification.

## 中文摘要
各种指令集架构（ISA）都定义了自己专有的内存模型。内存模型的精确描述对硬件开发人员和软件开发人员都至关重要。公理模型通常被用于描述内存一致性。尽管公理模型能够精确描述共享内存中的并发行为，但其推导过程依赖专家的人工努力，而且其复杂性给开发人员准确理解它们带来了挑战。此外，公理模型缺乏兼容性，这阻碍了自动化的比较与分析。本工作提出 UniMM，一个内存模型描述框架，它使用一种名为 ModelTable 的统一格式来自动描述内存模型。ModelTable 是一种准确、可读、可比较且可分析的格式，用于描述任意一对内存访问之间是否有序。为展示 UniMM 的广泛适用性，我们开发了两个实用组件作为案例研究。面向软件开发人员，我们设计了一个内存模型差异弥合组件，为跨 ISA 的软件迁移提供正确且高性能的方案。面向硬件开发人员，我们设计了一个内存模型一致性测试组件，用于生成 litmus 测试套件并判定某个 CPU 是否符合内存模型规范。

## 英文关键词
Memory models, Software migration, ISA compliance testing

## 中文关键词
内存模型，软件迁移，ISA 一致性测试

[返回 Session 25](index.md) · [返回 ATC 2026](../index.md)
