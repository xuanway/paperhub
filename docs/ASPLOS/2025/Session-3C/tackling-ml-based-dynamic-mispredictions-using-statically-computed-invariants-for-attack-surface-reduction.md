---
title: "Tackling ML-based Dynamic Mispredictions using Statically Computed Invariants for Attack Surface Reduction"
description: "ASPLOS 2025 · Session 3C · 利用静态计算不变量应对基于机器学习的动态误预测以缩减攻击面"
tags:
  - "ASPLOS2025"
  - "Session 3C"
  - "ML Security"
---

# Tackling ML-based Dynamic Mispredictions using Statically Computed Invariants for Attack Surface Reduction

**中文标题：** 利用静态计算不变量应对基于机器学习的动态误预测以缩减攻击面

**所属 Session：** [Session 3C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Chris Porter (IBM Research), Sharjeel Khan (Georgia Institute of Technology), Kangqi Ni (Georgia Institute of Technology), Santosh Pande (Georgia Institute of Technology)

**单位：** IBM Research；Georgia Institute of Technology

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716276) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Recent work has demonstrated the utility of machine learning (ML) in carrying out highly accurate predictions at runtime. One of the major challenges with using ML, however, is that the predictions lack certain guarantees. For such approaches to become practicable in security settings involving debloating and dynamic control flow monitoring, one must distinguish between mispredictions vs. attacks. In this work, we introduce a low overhead framework for tackling mispredictions of ML-based approaches using static invariants. In particular, we tackle the problem of dynamic function call set prediction encountered in program debloating. We first introduce an ML-based prediction technique that works on the whole application, providing high precision and reducing ∼90% of code-reuse gadgets useful for staging attacks at runtime. We then propose an effective mechanism for dealing with the ML model's mispredictions: a new static relation called the ensue() of a function, which is a set of functions that could legally follow a given function under any dynamic execution. We develop efficient algorithms to statically compute such a set by modeling the relation in a Datalog-based solver. Upon misprediction, the framework invokes a lightweight mechanism to distinguish ack vs. misprediction. We show that the framework triggers misprediction checking in our experiments on a reasonable percentage of predictions invoked at runtime (3.8%, 16%, and 2.3% for SPEC CPU 2017 and low- and highcomplexity applications, respectively), of which all cases are validated to conform to the static call relations. We contend that a low runtime overhead (7.5% for SPEC, 3% for realworld applications) and precise ML mechanism, along with the ability to effectively deal with mispredictions, yields a real-world solution.

## 中文摘要

近期的工作已经证明了机器学习（ML）在运行时执行高精度预测方面的效用。然而，使用 ML 的主要挑战之一在于这些预测缺乏某些保证。要使这类方法在涉及去臃肿（debloating）和动态控制流监控的安全场景中变得可行，就必须区分误预测与攻击。在本工作中，我们引入一个低开销框架，利用静态不变量来应对基于 ML 方法的误预测。具体而言，我们处理程序去臃肿中遇到的动态函数调用集预测问题。我们首先提出一种面向整个应用的基于 ML 的预测技术，它提供高精度并在运行时减少约 90% 可用于发动攻击的代码复用 gadget。随后，我们提出一种有效机制来处理 ML 模型的误预测：一种称为函数的 ensue() 的新静态关系，它是在任意动态执行下可以合法地跟随某个给定函数的一组函数。我们通过在基于 Datalog 的求解器中对该关系建模，开发了高效算法来静态计算这一集合。在发生误预测时，该框架会调用一种轻量级机制来区分确认（ack）与误预测。我们展示了该框架在我们的实验中，对运行时调用的合理比例的预测触发了误预测检查（对 SPEC CPU 2017 以及低复杂度和高复杂度应用分别为 3.8%、16% 和 2.3%），其中所有情形都被验证符合静态调用关系。我们认为，低运行时开销（SPEC 为 7.5%，真实应用为 3%）与精确的 ML 机制，再加上有效处理误预测的能力，构成了一套可在真实世界中落地的解决方案。

## 英文关键词

attack surface reduction, program security, static analysis

## 中文关键词

攻击面缩减；程序安全；静态分析

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716276)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3C](index.md) · [返回 ASPLOS 2025](../index.md)
