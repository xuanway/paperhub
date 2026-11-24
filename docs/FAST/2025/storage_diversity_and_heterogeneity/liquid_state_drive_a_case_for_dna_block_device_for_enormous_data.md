---
title: "Liquid-State Drive: A Case for DNA Block Device for Enormous Data"
description: "FAST 2025 · Storage Diversity and Heterogeneity · 用 SSD 存轻量翻译表，把 DNA 块设备写代价降至 1/2,927"
tags:
  - "FAST2025"
  - "Storage Diversity and Heterogeneity"
  - "DNA storage"
  - "block device"
---

# Liquid-State Drive: A Case for DNA Block Device for Enormous Data

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DNA 密度比磁带高八个数量级，但按块随机更新只能擦除旧链再合成新链，PB 级翻译表与 GC 元数据无法随每次写进入 DNA。LiqSD 把翻译表拆成 DNA 与 SSD 两层，让 GC 元数据随物理块共生、失效推迟到读时处理，写代价降至 1/2,927、读代价降至 1/7。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Storage Diversity and Heterogeneity</p>
</div>

**中文标题**：液态驱动器：面向海量数据的 DNA 块设备探索

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/zhou-jiahao](https://www.usenix.org/conference/fast25/presentation/zhou-jiahao)

**论文 PDF**：[fast25-zhou-jiahao.pdf](https://www.usenix.org/system/files/fast25-zhou-jiahao.pdf)

**作者**：Jiahao Zhou、Mingkai Dong、Fei Wang、Jingyao Zeng、Lei Zhao、Chunhai Fan、Haibo Chen（Shanghai Jiao Tong University）

**会议**：FAST 2025 · Santa Clara, CA · 第 557–571 页

**Session**：Storage Diversity and Heterogeneity · 2025-02-27 10:50–12:10 · Chair：Avani Wildani（Cloudflare and Emory University）

**所属 Session**：[Storage Diversity and Heterogeneity](index.md) · [FAST 2025](../index.md)

**关键词**：DNA storage, block device, dual-layer translation table, garbage collection, out-of-place update, delayed invalidation

---

## 英文摘要

The rapid development of DNA synthesis and sequencing technologies is making the ultra-high-density storage medium DNA to meet the rising demand for enormous data storage. The block storage interface, which is massively employed in storage systems, is the critical abstraction to integrate DNA storage into silicon-based computer systems. In this paper, we explore building block devices on DNA and identify the challenges of petabyte-scale metadata management and high DNA access costs. We propose a holistic DNA block device design called LIQUID-STATE DRIVE to provide low-cost block access to exabyte-scale data with the help of small yet fast SSDs. We adopt the dual-layer translation table to leverage SSDs to decrease the metadata updating cost. We introduce symbiotic metadata and delayed invalidation to reduce the cost of garbage collection and block updating. Our evaluation demonstrates that in microbenchmarks and real-world traces, the write cost reduces up to seven orders of magnitude and 2,927×, and the read cost reduces up to 6,206× and 7×, respectively. We expect our exploration and experience in building DNA block devices to be useful in expediting the advancement of DNA storage and bridging the gap between information technology and biotechnology.

## 中文摘要

DNA 合成与测序技术的快速发展，正使超高密度的存储介质 DNA 能够满足不断增长的海量数据存储需求。块存储接口被存储系统广泛采用，是让 DNA 存储融入硅基计算机系统的关键抽象。本文探索在 DNA 上构建块设备，并识别出 PB 级元数据管理与高昂 DNA 访问代价两大挑战。本文提出一种整体性的 DNA 块设备设计 LIQUID-STATE DRIVE（LiqSD），借助小而快的 SSD 为 EB 级数据提供低成本块访问。本文采用双层翻译表，借助 SSD 降低元数据更新成本；引入共生元数据与延迟失效，以降低垃圾回收与块更新的开销。评估表明，在微基准与真实 trace 中，写代价分别最多降低七个数量级与 2,927 倍，读代价分别最多降低 6,206 倍与 7 倍。本文期望在构建 DNA 块设备上的探索与经验，有助于加速 DNA 存储的发展、弥合信息技术与生物技术之间的差距。

## 一句话总结

> DNA 块设备的难点不是合成速度，而是别让 PB 级元数据跟着每次写进 DNA：轻量翻译表放进 SSD，失效推迟到读。

## 研究背景与问题

- **容量缺口**：2020 年产生 64.2 ZB 数据，预计 2025 年达 181 ZB，而 2020 年全球装机容量只有 6.7 ZB，大量数据因无处存放而流失。
- **DNA 的诱惑与代价**：DNA 密度达 10⁹ GB/mm³，比磁带高八个数量级，寿命可达数百年；但块更新只能擦除旧链、合成新链，擦除粒度比读大 10³ 倍、读粒度比写大 10⁶ 倍。
- **键值式 DNA 存储难扩展**：现有系统只把值放进 DNA，键与映射仍留在硅基介质，数据量一大就受制于索引；块接口更简单通用、支持细粒度访问，但已有 DNA 块工作或缺乏更新支持，或缺少元数据管理、GC、缓存与崩溃一致性设计。
- **元数据难题**：out-of-place 更新需要 LBA 到 PBA 的翻译表，EB 级数据对应 PB 级 DNA Translation Layer，且每次写都要更新；GC 同样需要 PB 级元数据。

## 核心贡献

- **DNA 块设备的整体设计**：系统分析在 DNA 上构建块设备的可行性与工作流，指出 PB 级元数据管理与高昂访问代价两个核心挑战。
- **双层翻译表（dual DTL）**：把 LBA→PBA 的 PB 级 L1 DTL 留在 DNA 中，把 GB 级的 L0 DTL（逻辑段→物理段索引）放在 SSD 上；写时只向 L1 所在的 physical section 追加 patch，并更新 SSD 上的少量元数据。
- **共生元数据（symbiotic metadata）**：把 GC 元数据与每个物理块存在一起，避免单独维护 PB 级集中式 GC 结构。
- **延迟失效（delayed invalidation）**：写时不立即作废旧块，推迟到读旧映射时再失效，并改造 GC 与缓存以容忍由此产生的不一致。

## 方法与技术要点

- **双层翻译**：L1 DTL（PB 级，LBA→PBA）以 physical section 为单位存放在 DNA 中，一个 PS 放进一个 SC（约 24 MiB）；L0 DTL（GB 级，逻辑段→物理段）放在 SSD，用于索引 L1。写入时先查 L0 得到 PS，再向该 PS 追加一条 normal patch（GC 迁移则写 GC patch），并更新写指针、patch 计数等 SSD 侧轻量元数据；读取时先查 L0 定位 PS，再读 DNA 中的 PS 并合并 patch 得到 PBA。
- **共生布局**：把反向翻译表条目写进物理块最后一条链的 OOB（32 字节）空间，把有效位写进块内预留的 invalid strand，GC 时可随块数据一起读出，免去集中式 GC 元数据的额外访问。
- **延迟失效路径**：更新只写新块与新映射，旧块保持有效直到其映射被读取或被 GC 回收，读路径负责识别并处理陈旧块。
- **GC 与缓存适配**：GC 策略与缓存按延迟失效的语义调整，避免把仍可能被读到的块提前回收。
- **模拟器实现**：基于 DNA 存储模拟器实现 LiqSD，用 Alibaba Cloud、MSR 系列与 ECFS 等真实 trace 驱动评估。

## 评估与主要结果

- **写代价**：微基准下最多降低七个数量级，真实 trace 下最多降至 1/2,927。
- **读代价**：微基准下最多降至 1/6,206，真实 trace 下最多降至 1/7；超过 99.3% 的 L1 DTL 读命中缓存。
- **GC 与延迟失效**：GC 使 Alibaba Cloud 与 MSR Prxy 的写放大分别增加约 2.7 倍与 1.3 倍；延迟失效相比立即失效，把最坏与最好情况下的读放大分别降至 1/15,194 与 1/7。
- **空间、块大小与延迟**：全部收益只付出 3.1% 空间开销；块大小 4 kB 时读写性能整体最好；按当前技术估算，读一个块平均约 49 分钟、写一个块约 74 分钟。

[返回 Storage Diversity and Heterogeneity](index.md) · [返回 FAST 2025](../index.md)
