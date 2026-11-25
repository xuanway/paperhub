---
title: "2DIO: Configurable and Cache-Accurate Trace Generation for Storage Benchmarking"
description: "EuroSys 2026 · Storage Systems · Yirong Wang (Northeastern University), Isaac Khor (Northeastern University), Pet"
tags:
  - "EuroSys2026"
  - "Storage Systems"
---

# 2DIO: Configurable and Cache-Accurate Trace Generation for Storage Benchmarking

**中文标题：** 2DIO：面向存储基准测试的可配置且缓存精确的轨迹生成

**所属 Session：** [Session 7.3: Storage Systems](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Storage Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Storage Systems</p>
</div>

**作者**：Yirong Wang (Northeastern University), Isaac Khor (Northeastern University), Peter Desnoyers (Northeastern University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769391)

## 英文摘要

We present 2DIO, a trace generator creating cache-accurate, stressful I/O workloads. While existing tools are limited to generating traces with well-behaved, concave hit ratio curves, 2DIO produces ones with tunable complex cache behaviors, particularly performance cliffs and plateaus.

Our framework encodes a workload as a compact parameter triplet, capturing both short-term recency and long-term frequency. This parsimonious parameterization allows researchers to easily translate individual adjustments into predictable cache effects across various eviction policies, and enables the parameter space to be "swept" for exhaustive exploration of desired cache behavior, or to mimic real traces by calibrating parameters to match observed behaviors.

The tuned parameters are portable, meaning if the scale of the system under evaluation changes, so too will the footprint and length of the trace, while the relative cache behaviors are preserved.

Evaluations demonstrate 2DIO’s ability to generate traces across a continuum of "what-if" cache behaviors and to reproduce real-world ones with high accuracy.

## 中文摘要

我们提出 2DIO，一个能够生成缓存精确、压力型 I/O 负载的轨迹生成器。现有工具只能生成命中率曲线表现良好且呈凹形的轨迹，而 2DIO 可生成具有可调复杂缓存行为的轨迹，特别是性能陡降与平台。

我们的框架将负载编码为紧凑的三参数组，同时刻画短期新近性与长期频率。这种简约的参数化方式使研究者能够轻松地将单个参数调整转化为各种淘汰策略下可预测的缓存效果，并支持对参数空间进行“扫描”，以穷尽探索期望的缓存行为，或通过校准参数以匹配观测行为来模拟真实轨迹。

调优后的参数具有可移植性，即若被评估系统的规模发生变化，轨迹的占用空间与长度也会随之变化，而相对的缓存行为得以保持。

评估表明，2DIO 能够生成覆盖一系列“假设（what-if）”缓存行为的轨迹，并能高精度地重现真实世界的缓存行为。

**英文关键词：** Caching, Trace generation, Performance evaluation, Benchmarking

**中文关键词：** 缓存、轨迹生成、性能评估、基准测试

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
