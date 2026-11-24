---
title: "Enabling Efficient Mobile Tracing with BTrace"
description: "ASPLOS 2025 · Session 3A · 用 BTrace 实现高效的移动端追踪"
tags:
  - "ASPLOS2025"
  - "Session 3A"
  - "Performance Analysis & Tracing"
---

# Enabling Efficient Mobile Tracing with BTrace

**中文标题：** 用 BTrace 实现高效的移动端追踪

**所属 Session：** [Session 3A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jiawei Wang (Huawei Dresden Research Center,Huawei Central Software Institute), Nian Liu (Huawei Central Software Institute), Arnau Casadevall-Saiz (Huawei Dresden Research Center,Huawei Central Software Institute), Yutao Liu (Huawei Dresden Research Center,Huawei Central Software Institute), Diogo Behrens (Huawei Dresden Research Center,Huawei Central Software Institute), Ming Fu (Huawei Central Software Institute), Ning Jia (Huawei Central Software Institute), Hermann Härtig (Technische Universität Dresden), Haibo Chen (Huawei Central Software Institute,Shanghai Jiao Tong University)

**单位：** Huawei Dresden Research Center,Huawei Central Software Institute；Huawei Central Software Institute；Technische Universität Dresden；Huawei Central Software Institute,Shanghai Jiao Tong University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715994) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

With the growing complexity of smartphone systems, effective tracing becomes vital for enhancing their stability and optimizing the user experience. Unfortunately, existing tracing tools are inefficient in smartphone scenarios. Their distributed designs (with either per-core or per-thread buffers) prioritize performance but lead to missing crucial clues with high probability. While these problems can be overlooked in previous scenarios (e.g., servers), they drastically limit the usefulness of tracing on smartphones. To enable efficient tracing on smartphones, we propose BTrace: a tracing tool that combines the performance benefits of per-core buffers with the capability of retaining longer continuous traces by partitioning a global buffer into multiple blocks, which are dynamically assigned to the most demanding cores. BTrace further gracefully handles unique requirements of modern smartphones, e.g., core oversubscription and resizing. BTrace has been deployed in production, recording an average of 2× continuous traces compared to the current bestperforming tracer (Linux ftrace) and improving performance by 20%. Using BTrace, we successfully identified numerous bugs that require traces of long duration and are challenging to locate with existing tracers.

## 中文摘要

随着智能手机系统日益复杂，有效的追踪对于增强系统稳定性并优化用户体验变得至关重要。遗憾的是，现有追踪工具在智能手机场景中效率低下。它们采用分布式设计（按核或按线程设置缓冲区），虽优先保障性能，却很可能遗漏关键线索。尽管这些问题在此前场景（如服务器）中可以被忽视，但它们极大地限制了追踪在智能手机上的实用性。为实现智能手机上的高效追踪，我们提出 BTrace：一种追踪工具，它通过将全局缓冲区划分为多个块并动态分配给需求最迫切的核，把按核缓冲区的性能优势与保留更长连续追踪的能力结合起来。BTrace 还优雅地处理了现代智能手机的独特需求，例如核的超额订阅与缓冲区缩放。BTrace 已在生产环境中部署，相比当前性能最好的追踪器（Linux ftrace）平均记录 2 倍的连续追踪，并将性能提升 20%。借助 BTrace，我们成功定位了大量需要长时间追踪、且用现有追踪器难以发现的缺陷。

## 英文关键词

Tracing, Software Debugging, Mobile

## 中文关键词

追踪；软件调试；移动端

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715994)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3A](index.md) · [返回 ASPLOS 2025](../index.md)
