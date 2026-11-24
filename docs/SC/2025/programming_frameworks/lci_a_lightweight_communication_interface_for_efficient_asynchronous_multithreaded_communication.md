---
title: "LCI: A Lightweight Communication Interface for Efficient Asynchronous Multithreaded Communication"
description: "SC 2025 · Programming Frameworks · Jiakun Yan; Marc Snir"
tags:
  - "SC2025"
  - "Programming Frameworks"
---

# LCI: A Lightweight Communication Interface for Efficient Asynchronous Multithreaded Communication

**中文标题：** 面向高效异步多线程通信的轻量通信接口

**所属 Session：** [Programming Frameworks](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Programming Frameworks。</p>
<p class="paper-seo-summary__tags">SC 2025 · Programming Frameworks</p>
</div>

**作者**：Jiakun Yan; Marc Snir

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap788&sess=sess294)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The evolution of architectures, programming models, and algorithms is driving communication towards greater asynchrony and concurrency, usually in multithreaded environments. We present LCI, a communication library designed for efficient asynchronous multithreaded communication. LCI provides a concise interface that supports common point-to-point primitives and diverse completion mechanisms, along with flexible controls for incrementally fine-tuning communication resources and runtime behavior. It features a threading-efficient runtime built on atomic data structures, fine-grained non-blocking locks, and low-level network insights. We evaluate LCI on both Infiniband and Slingshot-11 clusters with microbenchmarks and two application-level benchmarks. Experimental results show that LCI significantly outperforms existing communication libraries in various multithreaded scenarios, achieving performance that exceeds the traditional multi-process execution mode and unlocking new possibilitie

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
