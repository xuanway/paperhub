---
title: "Ariadne: An Efficient Deadlock-Free Temporal RDA with Local Tags and Interleaved Switching"
description: "MICRO 2026 · Session 9A · Ariadne：采用局部标签与交错切换的高效无死锁时分可重构数据流架构"
tags:
  - "MICRO2026"
---

# Ariadne: An Efficient Deadlock-Free Temporal RDA with Local Tags and Interleaved Switching

**中文标题：** Ariadne：采用局部标签与交错切换的高效无死锁时分可重构数据流架构

**所属 Session：** [Session 9A](index.md) · [MICRO 2026](../index.md)

**作者：** Xiangyu Kong, Yi Huang, Jianfeng Zhu, Liangwei Li, Jinyi Chen, Xiao Li, Mingyu Gao, Guiqiang Peng, Shaojun Wei, Aoyang Zhang, Leibo Liu

**来源：** MICRO 2026，pp. 3210–3225；[DOI](https://doi.org/10.1109/MICRO67795.2026.00216)

## 英文摘要

Reconfigurable dataflow architectures (RDAs) provide an attractive substrate for compute- and control-intensive tasks by tightly coupling computation with communication and triggering execution by data availability. Spatial RDAs deliver high throughput, but suffer from significant overhead in the absence of resource sharing; they frequently require configuration swaps and experience utilization collapse when program sizes grow large. Temporal RDAs ease placement pressure via time-multiplexed execution, yet many rely on compiler-enforced safety and remain vulnerable to deadlock hazards—bounded FIFOs that starve low-priority instructions and shared input channels that accumulate partial matches. These safety gaps ultimately cap efficiency and limit attainable performance. We present a safe and highly efficient temporal RDA that guarantees deadlock-free forward progress for resource sharing, while incorporating scalable tag management and non-blocking instruction switching to attain high efficiency. The core runtime protocol combines priority demotion on backpressure with tag-aware ingress admission, eliminating cyclic waits and half-match stalls. A receiver-local tag namespace bounds the tag space independent of program size, enabling precise matching, multicast, and composable scaling across tiles. A safe pipelining and non-blocking switching scheme for multi-cycle operations allows instructions to yield their issue slots while pending and resume upon completion, exposing fine-grained concurrency and effectively hiding long latencies. Collectively, these mechanisms establish a practical and highly efficient RDA architecture. Evaluated across diverse workloads with highly dynamic trigger behavior, our system sustains high utilization and delivers up to 1.76× execution time speed-up and 1.62× perf/W over state-of-the-art RDAs, with no observed deadlocks.

## 中文摘要

可重构数据流架构 (RDA) 通过将计算与通信紧密耦合并通过数据可用性触发执行，为计算和控制密集型任务提供了有吸引力的基础。空间 RDA 可提供高吞吐量，但在缺乏资源共享的情况下会产生巨大的开销；当程序规模变大时，它们经常需要配置交换并经历利用率崩溃。时序 RDA 通过时分复用执行来缓解放置压力，但许多依赖于编译器强制的安全性，并且仍然容易受到死锁危险的影响——有限的 FIFO 会导致低优先级指令匮乏，而共享输入通道会积累部分匹配。这些安全差距最终会限制效率并限制可达到的性能。我们提出了一种安全高效的时序 RDA，可保证资源共享的无死锁转发进程，同时结合可扩展的标签管理和非阻塞指令切换来实现高效率。核心运行时协议将背压优先级降级与标签感知入口准入相结合，消除了循环等待和半匹配停顿。接收器本地标签命名空间将标签空间限制为独立于程序大小，从而实现跨分块的精确匹配、多播和可组合缩放。用于多周期操作的安全流水线和非阻塞切换方案允许指令在挂起时让出其发出槽并在完成后恢复，从而暴露细粒度并发并有效隐藏长时延。这些机制共同建立了实用且高效的 RDA 架构。通过使用高度动态的触发行为对不同的工作负载进行评估，我们的系统保持了高利用率，并且与最先进的 RDA 相比，执行时间加速高达 1.76 倍，性能/W 提高了 1.62 倍，没有观察到死锁。

## 中文关键词

可重构数据流架构；时序执行；无死锁；标签管理；非阻塞指令切换

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 9A](index.md) · [MICRO 2026 主页](../index.md)
