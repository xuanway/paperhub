---
title: "P-PLUS: Prefetch Profiling with Lightweight Unified Sampling"
description: "MICRO 2026 · Session 3B · P-PLUS：通过轻量级统一采样分析预取行为"
tags:
  - "MICRO2026"
  - "Prefetching"
---

# P-PLUS: Prefetch Profiling with Lightweight Unified Sampling

**中文标题：** P-PLUS：通过轻量级统一采样分析预取行为

**所属 Session：** [Session 3B](index.md) · [MICRO 2026](../index.md)

**作者：** Junjie Liu, Fang Su, Yongbin Zhou, Haoqian Wang

**来源：** MICRO 2026，pp. 1084–1098；[DOI](https://doi.org/10.1109/MICRO67795.2026.00085)

## 英文摘要

Prefetching dominates data movement in modern memory hierarchies, yet it remains a critical blind spot for precise profilers. Hardware prefetch requests are autonomous: they carry no program counter and bypass instruction retirement, making them invisible to every existing instruction-centric precise sampling mechanism (e.g., Intel PEBS, AMD IBS, Arm SPE). Without this observability, developers can neither attribute cache behavior to specific prefetch actions nor obtain the fine-grained feedback needed for software-hardware cooperative prefetch optimization. In this paper, we introduce P-PLUS (Prefetch Profiling with Lightweight Unified Sampling), the first prefetch-centric precise profiler that makes prefetch behavior directly observable and attributable. P-PLUS unifies all prefetch streams at the memory subsystem backend, probabilistically sampling requests and tracking them through their full lifecycle. Each sample captures both static context (prefetch source, triggering PC, target address) for fine-grained behavioral classification, and precise lifecycle timestamps (issue, fill, use/eviction) for quantitative evaluation of prefetch utility. P-PLUS requires only 68B of on-chip storage in its minimal configuration and scales gracefully with additional PTR entries to sustain high tracking coverage even under aggressive sampling rates. Each compact 24~B sample keeps runtime data overhead negligible. On SPECint2017, a utility evaluation model built on P-PLUS profiling data eliminates roughly 70% of low-quality prefetch requests, lifting performance speedup from 0.02% to 8.08% for an unmanaged multi-prefetcher and from 2.24% to 7.90% for Alecto. In software prefetch distance tuning, P-PLUS derives the optimal distance in a single pass, matching the speedups of RPG^2's 8-12 iteration search on the CRONO benchmark suite. These results demonstrate that lightweight prefetch-centric profiling can unlock substantial, previously untapped optimization opportunities.

## 中文摘要

预取在现代内存层次结构中主导着数据移动，但它仍然是精确分析器的一个关键盲点。硬件预取请求是自主的：它们不携带程序计数器并绕过指令提交，使它们对每个现有的以指令为中心的精确采样机制（例如，Intel PEBS、AMD IBS、Arm SPE）不可见。如果没有这种可观察性，开发人员既无法将缓存行为归因于特定的预取操作，也无法获得软件-硬件协作预取优化所需的细粒度反馈。在本文中，我们介绍了 P-PLUS（轻量级统一采样预取分析），这是第一个以预取为中心的精确分析器，使预取行为可直接观察和归因。 P-PLUS 统一了内存子系统后端的所有预取流，对请求进行概率采样并在其整个生命周期中对其进行跟踪。每个样本都捕获静态上下文（预取源、触发 PC、目标地址）以进行细粒度行为分类，并捕获精确的生命周期时间戳（发出、填充、使用/驱逐）以定量评估预取效用。 P-PLUS 在其最小配置中仅需要 68B 片上存储，并且可以通过附加 PTR 条目进行优雅扩展，即使在激进的采样率下也能维持高跟踪覆盖范围。每个紧凑的 24~B 样本使运行时数据开销可以忽略不计。在 SPECint2017 上，基于 P-PLUS 分析数据构建的实用程序评估模型消除了大约 70% 的低质量预取请求，将非托管多重预取器的性能加速从 0.02% 提升到 8.08%，将 Alecto 的性能加速从 2.24% 提升到 7.90%。在软件预取距离调整中，P-PLUS 在单次传递中得出最佳距离，与 RPG^2 在 CRONO 基准套件上的 8-12 次迭代搜索的加速相匹配。这些结果表明，以预取为中心的轻量级分析可以释放大量以前未开发的优化机会。

## 中文关键词

性能剖析；预取；性能监测；轻量级采样

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3B](index.md) · [MICRO 2026 主页](../index.md)
