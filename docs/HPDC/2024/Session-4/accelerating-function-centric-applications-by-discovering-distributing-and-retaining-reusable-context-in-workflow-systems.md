---
title: "Accelerating Function-Centric Applications by Discovering, Distributing, and Retaining Reusable Context in Workflow Systems"
description: "HPDC 2024 · Session 4 — Software Systems & Workflows"
tags:
  - "HPDC2024"
  - "Session 4"
  - "Software Systems & Workflows"
---

# Accelerating Function-Centric Applications by Discovering, Distributing, and Retaining Reusable Context in Workflow Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 4 — Software Systems & Workflows（2024年6月6日 11:45–13:00 · Session Chair：Massimo Coppola）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 4</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658663)

**作者**：Thanh Son Phung, Colin Thomas, Logan Ward, Kyle Chard, Douglas Thain

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 4 — Software Systems & Workflows（2024年6月6日 11:45–13:00 · Session Chair：Massimo Coppola）

---

## 英文摘要

Workflow systems provide a convenient way for users to write large-scale applications by composing independent tasks into large graphs that can be executed concurrently on high-performance clusters. In many newer workflow systems, tasks are often expressed as a combination of function invocations in a high-level language. Because necessary code and data are not statically known prior to execution, they must be moved into the cluster at runtime. An obvious way of doing this is to translate function invocations into self-contained executable programs and run them as usual, but this brings a hefty performance penalty: a function invocation now needs to piggyback its context with extra code and data to a remote node, and the remote node needs to take extra time to reconstruct the invocation’s context before executing it, both detrimental to lightweight short-running functions. A better solution for workflow systems is to treat functions and invocations as first-class abstractions: subsequent invocations of the same function on a worker node should only pay for the cost of context setup once and reuse the context between different invocations. The remaining problems lie in discovering, distributing, and retaining the reusable context among workers. In this paper, we discuss the rationale and design requirement of these mechanisms to support context reuse, and implement them in TaskVine, a data-intensive distributed framework and execution engine. Our results from executing a large-scale neural network inference application and a molecular design application show that treating functions and invocations as first-class abstractions reduces the execution time of the applications by 94.5% and 26.9%, respectively.

## 中文摘要

工作流系统为用户提供了一种便捷方式，可将独立任务组合成可在高性能集群上并发执行的大型图，从而编写大规模应用。在许多较新的工作流系统中，任务常被表达为高级语言中函数调用的组合。由于必要的代码与数据在执行前并非静态已知，它们必须在运行时被移入集群。一种显而易见的做法是将函数调用翻译为自包含的可执行程序并照常运行，但这会带来沉重的性能损失：函数调用现在需要把额外代码与数据作为上下文一并携带到远程节点，远程节点还需额外时间在执行前重建调用上下文，这两点对轻量短时运行的函数都不利。对工作流系统而言更好的方案是将函数与调用视为一等抽象：同一函数在工作节点上的后续调用只需支付一次上下文建立成本，并在不同调用间复用上下文。剩下的问题在于发现、分发并在工作节点间保留可复用上下文。本文讨论支持上下文复用的这些机制的原理与设计需求，并在 TaskVine（一个数据密集型分布式框架与执行引擎）中实现。执行大规模神经网络推理应用与分子设计应用的结果表明，将函数与调用视为一等抽象分别将应用执行时间减少 94.5% 与 26.9%。

## 英文关键词

Workflow Systems; Serverless Computing; Distributed Storage; Burst Buffers

## 中文关键词

工作流系统；无服务器计算；分布式存储；突发缓冲区

---

[← 返回 Session 4 — Software Systems & Workflows](index.md)
