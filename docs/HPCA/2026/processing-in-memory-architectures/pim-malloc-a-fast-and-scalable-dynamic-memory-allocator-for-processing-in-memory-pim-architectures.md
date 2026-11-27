---
title: "PIM-malloc: A Fast and Scalable Dynamic Memory Allocator for Processing-In-Memory (PIM) Architectures"
description: "HPCA 2026 · Processing-in-Memory Architectures"
tags:
  - "HPCA2026"
  - "Processing-in-Memory Architectures"
---

# PIM-malloc: A Fast and Scalable Dynamic Memory Allocator for Processing-In-Memory (PIM) Architectures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Processing-in-Memory Architectures。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Processing-in-Memory Architectures</p>
</div>

**论文链接**：
**作者**：Dongjae Lee KAIST , Bongjoon Hyun Samsung , Youngjin Kwon KAIST , Minsoo Rhu KAIST
**会议**：HPCA 2026

---

## 中文标题

PIM-malloc：面向存内处理（PIM）架构的快速可扩展动态内存分配器

## 英文摘要

The ability to dynamically allocate memory is fundamental in modern programming languages. However, this feature is not adequately supported in current general-purpose PIM devices. To identify key design principles that PIM must consider, we conduct a design space exploration of PIM memory allocators, examining various strategies for metadata placement and management of the allocator. Based on this exploration, we introduce PIM-malloc, a fast and scalable memory allocator for general-purpose PIM that operates on real PIM hardware, achieving a 66× improvement in memory allocation performance. This design is further enhanced with a lightweight, per-PIM core hardware cache, specifically designed for dynamic memory allocation, achieving an additional 31% performance improvement. Finally, we demonstrate the applicability of PIM-malloc by developing several representative PIM workloads, demonstrating its effectiveness in enhancing programmability.

## 中文摘要

动态内存分配能力是现代编程语言的基础，但当前通用 PIM 设备对此支持不足。为厘清 PIM 必须考虑的关键设计原则，我们对 PIM 内存分配器开展设计空间探索，考察元数据放置与分配器管理的各种策略。基于该探索，我们提出 PIM-malloc，一种面向通用 PIM 的快速可扩展内存分配器，它在真实 PIM 硬件上运行，使内存分配性能提升 66 倍。该设计进一步引入专为动态内存分配设计的轻量级、每 PIM 核硬件缓存，额外带来 31% 的性能提升。最后，我们通过开发若干具有代表性的 PIM 负载验证了 PIM-malloc 的适用性，表明它能有效增强可编程性。
