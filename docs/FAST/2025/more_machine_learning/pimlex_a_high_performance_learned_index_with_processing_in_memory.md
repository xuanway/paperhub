---
title: "PIMLex: A High-Performance Learned Index with Processing-in-Memory"
description: "FAST 2025 · More Machine Learning · learned index 搜索层进 PIM、数据层留 DRAM，吞吐增 36.5 倍"
tags:
  - "FAST2025"
  - "More Machine Learning"
  - "processing-in-memory"
  - "learned index"
---

# PIMLex: A High-Performance Learned Index with Processing-in-Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">learned index 执行时间超过 60% 耗在内存停顿上，商用 PIM 每 DIMM 仅 8GB 且缺少浮点硬件。PIMLex 用 PIM 内搜索层加 DRAM 数据层的解耦结构、PIM 友好模型与热度感知复制，在 UPMEM 上吞吐达 PIM 版基线的 36.5 倍、DRAM 版 ALEX 的 2.2 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · More Machine Learning</p>
</div>

**中文标题**：PIMLex：基于存内计算的高性能学习型索引

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/cui](https://www.usenix.org/conference/fast25/presentation/cui)

**论文 PDF**：[fast25-cui.pdf](https://www.usenix.org/system/files/fast25-cui.pdf)

**作者**：Lixiao Cui、Kedi Yang、Yusen Li、Gang Wang、Xiaoguang Liu（College of Computer Science, Nankai University）

**会议**：FAST 2025 · Santa Clara, CA · 第 287–303 页

**Session**：More Machine Learning · 2025-02-26 09:00–10:20 · Chair：Ali R. Butt（Virginia Tech）

**所属 Session**：[More Machine Learning](index.md) · [FAST 2025](../index.md)

**关键词**：processing-in-memory, learned index, UPMEM, load balancing, replication

---

## 英文摘要

The index structures represented by the learned indexes are crucial components of storage systems. However, their performance is restricted by the memory bandwidth/latency wall in conventional computer architectures. Processing-in-memory (PIM) technology is a promising solution by integrating processing units directly into memory devices. In this paper, we propose PIMLex, a well-designed learned index with PIM, to alleviate the memory-bound issue. PIMLex overcomes the capacity limitations of existing PIM hardware by employing a decoupled two-layer structure. This design simultaneously leverages the powerful data processing capabilities of PIM and the large capacity of conventional DRAM. Additionally, a PIM-friendly model structure is incorporated to minimize computational tasks that PIM struggles with. Combined with a hotness-aware replication mechanism that ensures load balancing across numerous PIM modules, PIMLex is able to deliver high performance across various workload patterns. We implement PIMLex on UPMEM, an available commercial PIM. PIMLex achieves 36.5× higher throughput than the PIM-based learned index baseline and 2.2× higher than the DRAM-based ALEX.

## 中文摘要

以学习索引（learned index）为代表的索引结构是存储系统的关键部件，但其性能受限于传统架构的内存带宽与延迟墙。存内计算（processing-in-memory，PIM）把计算单元直接集成进内存器件，是有前景的解法。本文提出 PIMLex，一种精心设计的 PIM 学习索引，以缓解内存受限问题。PIMLex 采用解耦的两层结构，克服现有 PIM 硬件的容量限制；该设计同时利用 PIM 强大的数据处理能力与常规 DRAM 的大容量。此外，本文引入 PIM 友好的模型结构，以尽量减少 PIM 不擅长的计算任务。结合可在众多 PIM 模块间保证负载均衡的热度感知复制机制，PIMLex 能够在各种负载模式下提供高性能。本文在商用 PIM 硬件 UPMEM 上实现 PIMLex。PIMLex 的吞吐达到基于 PIM 的学习索引基线的 36.5 倍，也达到基于 DRAM 的 ALEX 的 2.2 倍。

## 一句话总结

> 按 PIM 的短板改索引结构：搜索层下沉到 PIM，数据层留在 DRAM，用查表代替浮点运算。

## 研究背景与问题

- **内存墙卡住 learned index**：learned index 靠模型预测 key 位置，但模型预测与误差界内的定位都要在 CPU 与内存之间搬运数据；对 ALEX 与 LIPP 的剖析显示，Get 与 Insert 的停顿主要来自 memory bound，执行时间超过 60% 花在内存停顿上。
- **PIM 的机会与错配**：UPMEM 每 DIMM 峰值带宽 80GB/s，HBM-PIM 每 cube 可达 2TB/s，PIM 带宽普遍是常规 DRAM 的 8 倍以上；但商用 PIM 每 DIMM 只有 8GB（常规 DRAM 可达 64GB），UPMEM 的 DPU 是 32 位顺序 RISC 核，浮点运算要靠整数运算模拟。
- **空间与算力双重挤压**：内存系统中索引约占 55% 的内存，部分 learned index 空间放大严重（LIPP 占用空间可超过实际数据的 5 倍）；PIM 模块只有 64KB 的 WRAM 与 64MB 的 MRAM，直接装入大索引不可行。
- **分布式 PIM 的负载倾斜**：PIM 平台由多个独立模块组成，按 key range 分区后倾斜访问会让少数模块过载、其余空闲；BasicLex 在均匀访问下表现尚可，倾斜访问下明显退化。

## 核心贡献

- **解耦两层结构**：PIM 内搜索层只保存从数据层采样的 anchor keys 并据此建模，DRAM 数据层保存全量键值，把大部分内存访问留在 PIM 内，同时绕开 PIM 容量限制。
- **PIM 友好的模型结构**：遵循以更多内存访问换更少计算的原则，只对部分层使用模型预测，并用保存预计算结果的查找表替代浮点运算。
- **热度感知复制（hotness-aware replication）**：按分区访问热度创建不同数量的副本，把热点分区的请求分散到更多 PIM 模块上以均衡负载。
- **真实硬件上的实现与基线**：在商用 UPMEM 上实现原型，并构建 PIM 版 learned index 基线 BasicLex 作为对照。

## 方法与技术要点

- **搜索层与数据层分工**：一次索引操作中，搜索层在 PIM 内完成大多数内存访问以确定目标 key 在数据层中的大致位置，数据层只需少量访问即可定位并操作数据。
- **anchor 采样控制规模**：搜索层不存全量键，只存从数据层采样的 anchor keys；anchor 间隔是空间与性能的旋钮，间隔从 8 增到 32 时 Get 性能下降 15%，但搜索层更小、能容纳更大的数据集。
- **削减 PIM 上的计算量**：不像传统分层 learned index 每层都做一次计算，PIMLex 只选择性地使用模型预测，并用查找表保存预计算结果，规避 PIM 缺失的浮点能力。
- **副本与负载均衡**：搜索层按 key range 分区分布到各 PIM 模块，热度高的分区获得更多副本以分摊请求；副本数调整有正常与快速两种方式。
- **基线 BasicLex 的构造**：按 range 分区把键值对均分到 M 个 PIM 模块，模块内用 PGM 的分层分段线性回归模型（ε 设为 32），模型与键值对都放在 MRAM，评测使用 512 个 PIM 模块与 FB、Osm 数据集。

## 评估与主要结果

- **吞吐**：在商用 UPMEM 上，PIMLex 的吞吐是 PIM 版 learned index 基线（BasicLex）的 36.5 倍，也是 DRAM 版 ALEX 的 2.2 倍。
- **动机量化**：ALEX 与 LIPP 在 FB、Osm 数据集上的执行时间超过 60% 属于内存停顿，这正是把索引搬到 PIM 的直接依据。
- **副本调整的开销权衡**：Osm 数据集上，正常调整方式为 75.8 M ops/s、耗时 0.45 s；快速调整方式 QA(8) 为 53.7 M ops/s、耗时 0.15 s，即用吞吐换调整时间。

[返回 More Machine Learning](index.md) · [返回 FAST 2025](../index.md)
