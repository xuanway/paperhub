# SynDebug: A Framework to Debug Logic Bugs in Fault-Tolerant Quantum Computing Programs

**中文标题**：SynDebug：调试容错量子计算程序中逻辑缺陷的框架

**所属 Session**：[Session 20: Quantum Computing](index.md) · [ATC 2026](../index.md)

**作者**：Nicholas S. DiBrita (Rice University), Jack Lange (Oak Ridge National Lab), Tirthak Patel (Rice University)

## 英文摘要
Fault-tolerant quantum computing (FTQC) introduces substantial systems-level complexity through quantum error correction (QEC), making debugging FTQC programs challenging. Existing quantum debugging approaches primarily target logical-level circuits and do not naturally support debugging within realistic FTQC execution flows. We present SynDebug, the first systems-level debugging framework for FTQC programs. SynDebug introduces lightweight assertion-based debugging primitives that operate directly within encoded FTQC infrastructures while avoiding additional logical surface area and minimizing temporal overhead. We evaluate SynDebug across multiple QEC code families, code distances, and encoded workloads, including state preparation, entanglement validation, and Shor-style programs. Our results demonstrate that SynDebug enables practical FTQC debugging with an average 1.8% additional circuit depth overhead (0% in most cases) and no measurable increase in the logical error rate, showing that systems-level debugging for large-scale FTQC applications is both feasible and practical.

## 中文摘要
容错量子计算（FTQC）通过量子纠错（QEC）引入了大量的系统级复杂性，使得调试 FTQC 程序颇具挑战。现有量子调试方法主要面向逻辑层线路，无法自然地支持在真实 FTQC 执行流中进行调试。我们提出 SynDebug，首个面向 FTQC 程序的系统级调试框架。SynDebug 引入轻量级的基于断言的调试原语，它们直接在已编码的 FTQC 基础设施中运作，同时避免增加额外的逻辑表面积并尽量减少时间开销。我们在多个 QEC 码族、码距和编码负载上评估 SynDebug，包括态制备、纠缠验证和 Shor 型程序。结果表明，SynDebug 使实用的 FTQC 调试成为可能，平均仅增加 1.8% 的线路深度开销（多数情况下为 0%），且逻辑错误率没有可测的增长，说明面向大规模 FTQC 应用的系统级调试既可行也实用。

## 英文关键词
Fault-Tolerant Quantum Computing, Debugging

## 中文关键词
容错量子计算，调试

[返回 Session 20](index.md) · [返回 ATC 2026](../index.md)
