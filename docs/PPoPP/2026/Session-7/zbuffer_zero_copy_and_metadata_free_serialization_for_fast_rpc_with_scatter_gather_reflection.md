---
title: "zBuffer: Zero-Copy and Metadata-Free Serialization for Fast RPC with Scatter-Gather Reflection"
description: "PPoPP 2026 Session 7（Cluster and Cloud Computing）：NIC scatter-gather+编译期静态反射，序列化快约 7×、P99 降 21%"
tags:
  - "PPoPP2026"
  - "Session-7"
  - "Cluster and Cloud Computing"
  - "serialization"
  - "RPC"
  - "zero-copy"
authors:
  - "Xiangyu Liu"
  - "Huiba Li"
  - "Shun Gai"
  - "Youmin Chen"
  - "Yiming Zhang"
session: "Session 7: Cluster and Cloud Computing"
session_number: 7
session_chair: "Ruslan Nikolaev"
date: "2026-02-03"
time: "11:50–12:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786426"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# zBuffer: Zero-Copy and Metadata-Free Serialization for Fast RPC with Scatter-Gather Reflection

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出零拷贝、免元数据的序列化库 zBuffer 与 RPC 系统 zRPC，用 scatter-gather 反射把数据聚合卸载到网卡并结合编译期静态反射，消除序列化与传输中的内存拷贝。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 7: Cluster and Cloud Computing</p>
</div>

**作者**：Xiangyu Liu, Huiba Li, Shun Gai, Youmin Chen, and Yiming Zhang — Xiamen University, China; Alibaba Cloud, China; Shanghai Jiao Tong University, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 11:50–12:10 · Session 7: Cluster and Cloud Computing（主席：Ruslan Nikolaev）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786426) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

This paper presents zBuffer, a zero-copy and metadata-free serialization library for high-performance and low-cost RPCs. At the core of zBuffer is scatter-gather reflection, a novel technique that collaboratively (i) leverages the NIC scatter-gather hardware feature to offload the costly data coalescing, and (ii) utilizes the static reflection mechanism of modern programming languages to enable type queries on complex data objects without requiring explicit metadata construction. We leverage C++ language features, mainly including template meta-programming and macros, to realize static reflection at compile time. Based on zBuffer, we design a fast RPC system (called zRPC) which eliminates all RPC memory copy overheads not only in (de)serialization but also in network transmission. Extensive evaluation shows that zBuffer/zRPC significantly outperforms state-of-the-art serialization/RPC mechanisms: zBuffer is approximately 7× faster than Cornflakes in serialization for complex data objects; and zRPC reduces 99th percentile latency by 21% and achieves 62% higher throughput than eRPC on the Masstree key-value (KV) store with the YCSB benchmark.

## 中文摘要

本文提出 zBuffer，一个面向高性能、低成本 RPC 的零拷贝且无需元数据的序列化库。zBuffer 的核心是分散-聚集反射（scatter-gather reflection），这是一种新颖的技术，它协同地（i）利用网卡（NIC）的分散-聚集硬件特性来卸载昂贵的数据合并操作，（ii）利用现代编程语言的静态反射机制，在无需显式构造元数据的情况下对复杂数据对象进行类型查询。我们借助 C++ 语言特性（主要包括模板元编程与宏）在编译期实现静态反射。基于 zBuffer，我们设计了一个快速 RPC 系统（称为 zRPC），它不仅消除了（反）序列化中的所有内存拷贝开销，也消除了网络传输中的内存拷贝开销。大量评估表明，zBuffer/zRPC 显著优于最先进的序列化/RPC 机制：对于复杂数据对象的序列化，zBuffer 比 Cornflakes 快约 7 倍；在 YCSB 基准下针对 Masstree 键值（KV）存储，zRPC 相比 eRPC 将 99 分位延迟降低 21%，并实现高出 62% 的吞吐量。

## 英文关键词

Zero-Copy, Data Serialization, Reflection

## 中文关键词

零拷贝；数据序列化；反射

---

## 一句话总结

> 提出零拷贝、免元数据的序列化库 zBuffer 与 RPC 系统 zRPC，用 scatter-gather 反射把数据聚合卸载到网卡并结合编译期静态反射，消除序列化与传输中的内存拷贝。

## 研究问题

传统序列化需要显式构造元数据并付出昂贵的数据聚合与内存拷贝代价，现有机制在追求高性能、低开销 RPC 时表现不佳。

## 方法简述

- 提出 scatter-gather reflection 技术，将耗时的数据聚合卸载到网卡的 scatter-gather 硬件特性上。
- 采用现代编程语言的静态反射机制，在无需显式构造元数据的前提下对复杂数据对象进行类型查询。
- 利用 C++模板元编程与宏，在编译期实现静态反射。
- 基于 zBuffer 设计快速 RPC 系统 zRPC，消除（反）序列化与网络传输中的全部内存拷贝开销。

## 主要结果

- 对复杂数据对象的序列化，zBuffer 比 Cornflakes 快约 7 倍。
- 在 YCSB 基准下的 Masstree 键值存储上，zRPC 相比 eRPC 将 99 分位延迟降低 21%，吞吐提升 62%。

---

> 所属 Session：[Session 7: Cluster and Cloud Computing](index.md) · 返回 [PPoPP 2026 总览](../index.md)
