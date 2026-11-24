---
title: "Bumper: Hinting Instruction Usefulness for Robust Unified Caches"
description: "ISCA 2026 · Session 8B · Bumper: Hinting Instruction Usefulness for Robust Unified Caches"
tags:
  - "ISCA2026"
  - "Session 8B"
  - "Prefetching and Cache 1"
---

# Bumper: Hinting Instruction Usefulness for Robust Unified Caches

**中文标题：** Bumper: 为鲁棒统一缓存提示指令有用性

**所属 Session：** [Session 8B](index.md) · [ISCA 2026](../index.md)

**作者：** Georgios Vavouliotis, Boris Grot, Tom Rollet, Leeor Peled, Davide Basilio Bartolini, Lixia Yang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Contemporary mobile applications exhibit large instruction working sets that overwhelm cores’ front-end structures, leading to frequent pipeline stalls that significantly harm performance. We find that a key contributor to the front-end bottleneck is code pollution in the unified L2 cache (L2C) stemming from a high incidence of fetches and prefetches on the wrong execution path. Such wrong-path allocations waste, on average, ∼20% of a large L2C’s capacity with instruction cache lines that are useless – i.e., lines that are evicted from the cache before any of the instructions they contain ever commits. This work demonstrates that tracking whether a code line contains committed instructions provides a robust foundation for code-aware cache management. Building on this insight, we propose Bumper, a lightweight microarchitectural scheme that dynamically propagates usefulness hints based on commit information to the cache hierarchy and selectively prioritizes useful code lines in the L2C, enabling rapid eviction of useless lines. The principal challenge addressed in the design of Bumper is how to orchestrate the propagation of usefulness hints based on commit information across the CPU pipeline and cache hierarchy, while minimizing microarchitectural overheads. Using an industry-grade simulator, we show that Bumper mitigates the front-end bottleneck of real-world mobile applications by reducing L2C code pollution and improving the lifetime of useful code lines, outperforming state-of-the-art schemes by over 5.4%, on average, at a storage cost of just 422 bytes.

## 中文摘要

当代移动应用呈现出庞大的指令工作集，压垮了核心的前端结构，导致频繁的流水线停顿，严重损害性能。我们发现，前端瓶颈的一个关键成因是统一 L2 缓存（L2C）中的代码污染，它源于错误执行路径上取指与预取的高发。此类错误路径分配平均浪费了大型 L2C 约 20% 的容量，其中存放的是无用的指令缓存行——即在其包含的任何指令提交之前就被逐出的代码行。本工作表明，跟踪一个代码行是否包含已提交的指令，为代码感知的缓存管理提供了坚实的基础。基于这一洞见，我们提出 Bumper，一种轻量级微架构方案，它根据提交信息动态地将有用性提示传播到缓存层次结构，并在 L2C 中选择性地优先保留有用的代码行，从而快速逐出无用行。Bumper 设计中要解决的主要挑战在于：如何在整个 CPU 流水线与缓存层次中协调基于提交信息的有用性提示传播，同时最小化微架构开销。借助工业级模拟器，我们证明 Bumper 通过减少 L2C 代码污染并延长有用代码行的生存期，缓解了真实移动应用的前端瓶颈，平均优于最先进方案 5.4% 以上，而存储开销仅为 422 字节。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 8B](index.md) · [返回 ISCA 2026](../index.md)
