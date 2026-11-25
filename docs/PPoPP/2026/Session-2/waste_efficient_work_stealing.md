---
title: "Waste-Efficient Work Stealing"
description: "PPoPP 2026 Session 2（Scheduling and Load Balancing）：自适应调整活跃线程数，保持渐近时间并给出浪费上界"
tags:
  - "PPoPP2026"
  - "Session-2"
  - "Scheduling and Load Balancing"
  - "Work Stealing"
  - "Task Parallelism"
  - "Runtime"
authors:
  - "Kyle Singer"
  - "Kunal Agrawal"
  - "Tao B. Schardl"
session: "Session 2: Scheduling and Load Balancing"
session_number: 2
session_chair: "V Krishna Nandivada"
date: "2026-02-02"
time: "11:50–12:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786452"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Waste-Efficient Work Stealing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 WEWS，对随机工作窃取的自适应扩展：动态调整活跃线程数，在保持相同渐近运行时间的同时抑制无任务可窃时的资源浪费。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 2: Scheduling and Load Balancing</p>
</div>

**作者**：Kyle Singer, Kunal Agrawal, and Tao B. Schardl — Massachusetts Institute of Technology, USA; Washington University in St. Louis, USA

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 11:50–12:10 · Session 2: Scheduling and Load Balancing（主席：V Krishna Nandivada）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786452) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Although randomized work stealing is effective at automatically load-balancing task-parallel programs, it can waste computational resources when scheduling programs that lack sufficient parallelism to use all available threads. For such programs, threads will waste cycles attempting to steal parallel tasks when none are available. This waste can reduce the machine’s efficiency by wasting computational resources and energy and needlessly burdening the operating system. This paper introduces WEWS, a simple, practical, and provably efficient extension to randomized work stealing that mitigates waste. WEWS dynamically adjusts the number of active threads to reduce the waste of randomized work stealing. WEWS executes a parallel computation with the same asymptotic running time as traditional randomized work stealing while bounding the waste to 𝑂(min  𝑃𝑇∞,𝑇1 + 𝑃2 ) instructions. WEWS also follows the work-first principle to perform well in practice. WEWS requires no special support from the operating system or hardware, which simplifies its implementation. We implemented WEWS within the OpenCilk runtime system and compared it to other common waste-mitigation strategies. Across 10 parallel benchmarks, we find that WEWS has minimal impact on parallel running times while, on programs with limited parallelism, substantially reducing waste.

## 中文摘要

尽管随机工作窃取能够自动地对任务并行程序实现有效负载均衡，但在调度那些并行度不足以占满所有可用线程的程序时，它会浪费计算资源。对这类程序，线程会白白消耗周期去尝试窃取并行任务，而此时并无任务可用。这种浪费会消耗计算资源与能量，并无谓地加重操作系统负担，从而降低机器效率。本文提出 WEWS，一种对随机工作窃取的简单、实用且可证明高效的扩展，用以缓解浪费。WEWS 动态调整活跃线程数，以减少随机工作窃取带来的浪费。WEWS 执行并行计算时的渐近运行时间与传统随机工作窃取相同，同时将浪费限定在 O(min(PT∞, T1) + P²) 条指令之内。WEWS 还遵循 work-first 原则，从而在实践中表现良好。WEWS 无需操作系统或硬件的特殊支持，这简化了其实现。我们在 OpenCilk 运行时系统中实现了 WEWS，并将其与其他常见的浪费缓解策略进行比较。在 10 个并行基准测试上，我们发现 WEWS 对并行运行时间的影响极小，而在并行度有限的程序上则大幅减少了浪费。

## 英文关键词

Cilk, energy, OpenCilk, parallel computing, parallel runtime system, task parallelism, waste, work stealing

## 中文关键词

Cilk；能耗；OpenCilk；并行计算；并行运行时系统；任务并行；浪费；工作窃取

---

## 一句话总结

> 提出 WEWS，对随机工作窃取的自适应扩展：动态调整活跃线程数，在保持相同渐近运行时间的同时抑制无任务可窃时的资源浪费。

## 研究问题

并行度不足时，线程会反复尝试窃取并不存在的任务，浪费计算资源与能量，并给操作系统带来额外负担。

## 方法简述

- 动态调整活跃线程数，以减少无效窃取。
- 保持与传统随机工作窃取相同的渐近运行时间，并给出可证明的浪费上界。
- 遵循 work-first 原则以保持实际性能，且无需操作系统或硬件特殊支持。

## 主要结果

- 在 OpenCilk 中实现，并在 10 个并行基准上与常见减少浪费的策略对比。
- 对并行运行时间影响极小，同时在并行度有限的程序上显著减少浪费。

---

> 所属 Session：[Session 2: Scheduling and Load Balancing](index.md) · 返回 [PPoPP 2026 总览](../index.md)
