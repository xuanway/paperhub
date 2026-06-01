---
title: "LCI: A Lightweight Communication Interface for Efficient Asynchronous Multithreaded Communication"
description: "SC 2025 · Programming Frameworks · Jiakun Yan; Marc Snir"
tags:
  - "SC2025"
  - "Programming Frameworks"
---

# LCI: A Lightweight Communication Interface for Efficient Asynchronous Multithreaded Communication

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Programming Frameworks。</p>
<p class="paper-seo-summary__tags">SC 2025 · Programming Frameworks</p>
</div>

**作者**：Jiakun Yan; Marc Snir

**会议**：SC 2025 · St. Louis, MO

## 摘要

The evolution of architectures, programming models, and algorithms is driving communication towards greater asynchrony and concurrency, usually in multithreaded environments. We present LCI, a communication library designed for efficient asynchronous multithreaded communication. LCI provides a concise interface that supports common point-to-point primitives and diverse completion mechanisms, along with flexible controls for incrementally fine-tuning communication resources and runtime behavior. It features a threading-efficient runtime built on atomic data structures, fine-grained non-blocking locks, and low-level network insights. We evaluate LCI on both Infiniband and Slingshot-11 clusters with microbenchmarks and two application-level benchmarks. Experimental results show that LCI significantly outperforms existing communication libraries in various multithreaded scenarios, achieving performance that exceeds the traditional multi-process execution mode and unlocking new possibilitie

---

## 一句话总结

> 该工作属于 Programming Frameworks 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Programming Frameworks 领域贡献新的设计范式或评估框架。
