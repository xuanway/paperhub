---
title: "Archer: Adaptive Memory Compression with Page-Association-Rule Awareness for High-Speed Response of Mobile Devices"
description: "FAST 2025 · Compression and Deduplication · 按页关联规则做变粒度内存压缩，应用启动快 1.55 倍"
tags:
  - "FAST2025"
  - "Compression and Deduplication"
  - "memory compression"
  - "page association"
---

# Archer: Adaptive Memory Compression with Page-Association-Rule Awareness for High-Speed Response of Mobile Devices

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">移动系统逐页压缩内存，但页粒度压缩浪费 CPU 带宽、上下文切换频繁，频繁压缩时响应延迟可增至 2.31 倍。Archer 挖掘匿名页隐含的关联规则，用 FT-List 与自适应压缩区实现任意粒度成组压缩，应用启动快 1.55 倍，帧率提升 1.31 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Compression and Deduplication</p>
</div>

**中文标题**：Archer：面向移动设备快速响应的页关联规则感知自适应内存压缩

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/li](https://www.usenix.org/conference/fast25/presentation/li)

**论文 PDF**：[fast25-li.pdf](https://www.usenix.org/system/files/fast25-li.pdf)

**作者**：Changlong Li（East China Normal University）；Zongwei Zhu、Chao Wang（University of Science and Technology of China）；Fangming Liu（Huazhong University of Science and Technology and Peng Cheng Laboratory）；Fei Xu、Edwin H. -M. Sha（East China Normal University）；Xuehai Zhou（University of Science and Technology of China）

**会议**：FAST 2025 · Santa Clara, CA · 第 497–511 页

**Session**：Compression and Deduplication · 2025-02-27 09:00–10:20 · Chair：Gala Yadgar（Technion—Israel Institute of Technology）

**所属 Session**：[Compression and Deduplication](index.md) · [FAST 2025](../index.md)

**关键词**：memory compression, page association, association rule mining, LRU, mobile systems, adaptive granularity

---

## 英文摘要

In mobile systems, memory can be compressed page-by-page to save space. This approach is widely adopted because memory data is accessed by page. However, this paper shows that the system response speed is significantly limited by page-grained compression. In this paper, we observe that approximately a quarter of anonymous memory pages are highly correlated, even though the association is implicit. Inspired by this, we propose Archer, an association-rule-aware memory compression framework in mobile systems. Archer demonstrates that memory in mobile devices should be compressed using flexible granularity, rather than relying solely on traditional page compression. To further integrate association-rule mining techniques into system design, we redesign the LRU mechanism and propose an adaptive memory compression region. Experimental results show that the average app launching speed is 1.55x faster when enabling Archer, and the average photographic speed and frame rate increase by 1.42x and 1.31x, respectively, compared to the state-of-the-art.

## 中文摘要

在移动系统中，内存可以逐页压缩以节省空间。这种做法因内存数据按页访问而被广泛采用。然而，本文表明系统响应速度显著受限于页粒度压缩。本文观察到，约四分之一的匿名内存页高度相关，尽管这种关联是隐式的。受此启发，本文提出 Archer——移动系统中一种关联规则感知的内存压缩框架。Archer 表明，移动设备中的内存应采用灵活的粒度进行压缩，而不是只依赖传统的页压缩。为进一步把关联规则挖掘技术融入系统设计，本文重新设计了 LRU 机制，并提出自适应内存压缩区。实验结果表明，相比最先进方案，启用 Archer 后应用平均启动速度提升 1.55 倍，平均拍照速度与帧率分别提升 1.42 倍与 1.31 倍。

## 一句话总结

> 约四分之一的匿名页存在隐性关联，把它们成组压缩比逐页压缩更快，而且不需要改动硬件。

## 研究背景与问题

- **移动内存持续紧张**：AI、AR/VR、Transformer 等内存密集任务抬高需求，系统靠内存压缩（memory compression）处理最不关键的页以腾出空间；页粒度压缩因内存按页管理、可避免读放大而被广泛采用。
- **页粒度压缩拖慢响应**：在 HUAWEI P20 上测量，内存紧张时应用启动延迟增加 68.7%，连拍从每秒 16 张降到 10 张（耗时延长 1.6 倍），短视频帧率从约 50fps 降到 27fps；频繁压缩时响应延迟最多增至 2.31 倍。
- **页与页之间存在隐性关联**：约四分之一的匿名页高度相关，要么一起被访问，要么一起不被访问，但这种关联如同超市里的尿布与啤酒，系统无法直接感知；而 LRU 擅长通用负载，却不适合做数据挖掘。
- **压缩粒度不能固定**：关联页的数量多少不一，固定的大粒度压缩在应用只需 4KB 时反而拉长响应时间。

## 核心贡献

- **量化匿名页关联**：指出约四分之一的匿名页高度相关，这是此前操作系统设计忽略的因素。
- **首次提出移动端大粒度压缩**：不依赖硬件基础设施改动，靠页间关联突破页粒度压缩的性能上限。
- **FT-List 结构**：面向频繁模式树的页管理结构，替代不适合挖掘的 LRU，使关联页的索引与管理变得轻量。
- **ACR 自适应压缩区**：支持任意粒度的压缩与寻址；整个方案对应用透明、无需修改应用代码，并与现有机制兼容。

## 方法与技术要点

- **足迹流生成（FSG）**：把页访问序列转换为可挖掘的足迹流，配合 FT-List 简化关联页的索引与管理。
- **轻量关联挖掘（PAM）**：在移动端资源约束下用滑动窗口（默认宽度 32）与事务缓冲做频繁项集挖掘，避免全量挖掘引发 CPU 争用。
- **LRU 改造**：重新设计 LRU 机制，使页管理既服务回收决策，又能为关联挖掘提供有序的访问流。
- **变粒度压缩区**：重设计地址空间与压缩区，把关联页成组压入、按需解压，缓解小需求触发大粒度解压带来的放大。
- **开销控制**：候选页缓冲上限 128KB，环形队列缓存 128 个项（1KB）、事务缓冲 512 条（128KB），元数据随对应页解压而回收，不会持续累积。

## 评估与主要结果

- **响应速度**：在真实设备上对比现有最优方案，应用平均启动速度提升 1.55 倍，拍照速度提升 1.42 倍，短视频帧率提升 1.31 倍。
- **尾延迟**：内存耗尽时的响应恶化最多缓解 55%。
- **能耗**：两台 Pixel6 同步对照测试 8 轮，开启 Archer 后平均多耗电 0.69%，相当于 12 小时续航仍可用 11.92 小时以上。
- **内存开销**：在 4GB（1,048,576 个）匿名页、30% 高度相关、平均频繁项集为 6.4 的情况下，映射表仅需 384KB。

[返回 Compression and Deduplication](index.md) · [返回 FAST 2025](../index.md)
