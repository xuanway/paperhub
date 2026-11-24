---
title: "VectorCDC: Accelerating Data Deduplication with Vector Instructions"
description: "FAST 2025 · Compression and Deduplication · 用 SSE/AVX 加速无哈希 CDC，吞吐比现有向量方案高 21–46 倍"
tags:
  - "FAST2025"
  - "Compression and Deduplication"
  - "content-defined chunking"
  - "data deduplication"
---

# VectorCDC: Accelerating Data Deduplication with Vector Instructions

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">内容定义分块需完整扫描每个文件，是去重的主要瓶颈；已有向量化方案针对哈希型分块，受 gather/scatter 与最小块长跳过失效所限，加速有限。VectorCDC 转向无哈希分块，用树状极值搜索与打包扫描覆盖其公共阶段，吞吐比 SS-CDC 高 21–46 倍且不损空间节省。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Compression and Deduplication</p>
</div>

**中文标题**：VectorCDC：利用向量指令加速数据去重

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/udayashankar](https://www.usenix.org/conference/fast25/presentation/udayashankar)

**论文 PDF**：[fast25-udayashankar.pdf](https://www.usenix.org/system/files/fast25-udayashankar.pdf)

**作者**：Sreeharsha Udayashankar、Abdelrahman Baba、Samer Al-Kiswany（University of Waterloo）

**会议**：FAST 2025 · Santa Clara, CA · 第 513–522 页

**Session**：Compression and Deduplication · 2025-02-27 09:00–10:20 · Chair：Gala Yadgar（Technion—Israel Institute of Technology）

**所属 Session**：[Compression and Deduplication](index.md) · [FAST 2025](../index.md)

**关键词**：content-defined chunking, data deduplication, vector instructions, AVX-512, hashless CDC, throughput

---

## 英文摘要

Content-defined Chunking (CDC) algorithms dictate the overall space savings achieved by deduplication systems. However, due to their need to scan each file in its entirety, they are slow and often the main performance bottleneck within data deduplication. This paper presents VectorCDC, a method to accelerate hashless CDC using SSE/AVX CPU instructions. Our evaluation shows that VectorCDC achieves 21 − 46× higher throughput than existing vector acceleration techniques, without affecting the space savings achieved.

## 中文摘要

内容定义分块（CDC）算法决定了去重系统所能获得的整体空间节省。然而，由于需要完整扫描每个文件，这些算法速度较慢，常常是数据去重中的主要性能瓶颈。本文提出 VectorCDC，一种利用 SSE/AVX CPU 指令加速无哈希 CDC 的方法。评估表明，VectorCDC 的分块吞吐比现有向量加速技术高 21–46 倍，且不影响所达到的空间节省。

## 一句话总结

> 无哈希分块只有两个热点阶段，找窗口极值和范围扫描，都能用整寄存器比较并行化。

## 研究背景与问题

- **分块处在关键路径上**：去重分为分块、块哈希与比较、元数据生成、元数据与块存储四个阶段，其中分块与哈希最耗算力；内容定义分块（content-defined chunking, CDC）在每次数据上传时执行，累计运行数百万次，块大小通常为 1 至 64KB。
- **哈希型分块难以向量化**：基于滚动哈希的分块要靠窗口哈希匹配掩码来确定边界，SS-CDC 用 AVX-512 的 scatter/gather 一次装载 64 个不相邻字节，指令代价高；同时对整个源数据做滚动哈希，抵消了最小块长跳过带来的吞吐收益。
- **既有向量加速比有限**：实测 SS-CRC 为 0.51 GB/s（1.59 倍加速）、SS-Gear 为 1.1 GB/s（1.18 倍加速），远未释放向量宽度。
- **无哈希分块更快但仍需全量扫描**：用局部极值插入边界的无哈希算法比多数哈希型算法快 2 至 3 倍，空间节省略低但差异很小，仍被生产系统采用。

## 核心贡献

- **归纳两个公共阶段**：指出所有无哈希 CDC 算法都由极值字节搜索（Extreme Byte Search）与范围扫描（Range Scan）构成，从而给出统一的加速切入点。
- **树状极值搜索**：把窗口切成子区域，用向量最大值指令两两归约成一棵 m512i 树，最后只顺序检查 64 个候选字节。
- **打包范围扫描**：把 64 个相邻字节装入一个向量寄存器，用一次向量比较生成 64 位掩码来判断边界是否存在，并保留最小块长跳过。
- **可移植实现**：同一套方法在 AVX-512、AVX-256、SSE-128 上分别实现为 VRAM、VRAM-256、VRAM-128，代码以集成进 DedupBench 的形式公开。

## 方法与技术要点

- **极值搜索的树状归约**：按 64 字节打包装入 m512i 变量，用向量最大值指令求成对最大值并写入目标变量，逐层比较归约，直到只剩一个覆盖全区域的向量，再顺序扫描定位最大值。
- **范围扫描的掩码判定**：把目标值与 64 个相邻字节分别装入 m512i，用向量比较指令生成 64 位掩码；掩码大于 0 说明这 64 字节内存在边界并由掩码值定位，等于 0 则直接装载下一批 64 字节。
- **保留最小块长跳过**：边界检测与插入都发生在范围扫描内，因此一旦发现边界即可跳过后续的最小块长字节；SS-CDC 对全量数据预先滚动哈希，反而丢掉了这一收益。
- **算法组合**：RAM 被表达为一次极值搜索加一次范围扫描，AE 同理由这两阶段组成，二者共用同一条向量化路径。

## 评估与主要结果

- **总体加速**：在 Intel Ice Lake 与 AMD EPYC Rome 上，VectorCDC 的分块吞吐比 SS-CDC 的 AVX 方案高 21–46 倍，且不改变无哈希算法取得的空间节省。
- **指令集覆盖**：DEB 数据集、8KB 块下，SSE-128 与 AVX-256 版本分别达到 13.3 GB/s 与 19.5 GB/s，在 Intel 与 AMD 两平台吞吐相近。
- **阶段贡献**：DEB 上仅加速极值搜索的 VRAM-EBS 达到 10 GB/s，再加速范围扫描多出 3 GB/s；LNX 上则为 5.7 GB/s 加 11 GB/s，说明两个阶段都加速才能稳定获益。

## 代码与研究制品

- [代码仓库](https://github.com/UWASL/dedup-bench)

[返回 Compression and Deduplication](index.md) · [返回 FAST 2025](../index.md)
