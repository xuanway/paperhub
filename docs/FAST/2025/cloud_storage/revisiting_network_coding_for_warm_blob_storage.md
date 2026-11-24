---
title: "Revisiting Network Coding for Warm Blob Storage"
description: "FAST 2025 · Cloud Storage · 小 blob 改用非系统化 MSR 码以避开非连续 I/O，单块修复时间最多降 45.0%"
tags:
  - "FAST2025"
  - "Cloud Storage"
  - "erasure coding"
  - "MSR codes"
---

# Revisiting Network Coding for Warm Blob Storage

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">系统化 MSR 码要保持带宽最优，就得在子块粒度上做非连续 I/O，块小时修复反而被拖慢。NCBlob 让小 blob 走非系统化 MSR 码、按访问局部性组织数据单元，大 blob 仍用系统化码，阿里云实验里单块修复时间最多降 45.0%，读吞吐仅损失 2.1%。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Cloud Storage</p>
</div>

**中文标题**：重新审视温数据 Blob 存储中的网络编码

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/gan](https://www.usenix.org/conference/fast25/presentation/gan)

**论文 PDF**：[fast25-gan.pdf](https://www.usenix.org/system/files/fast25-gan.pdf)

**作者**：Chuang Gan（Huazhong University of Science and Technology）；Yuchong Hu（Huazhong University of Science and Technology and Shenzhen Huazhong University of Science and Technology Research Institute）；Leyan Zhao、Xin Zhao、Pengyu Gong、Dan Feng（Huazhong University of Science and Technology）

**会议**：FAST 2025 · Santa Clara, CA · 第 139–154 页

**Session**：Cloud Storage · 2025-02-25 14:00–15:20 · Chair：Ming Zhao（Arizona State University）

**所属 Session**：[Cloud Storage](index.md) · [FAST 2025](../index.md)

**关键词**：erasure coding, MSR codes, network coding, blob storage, repair I/O

---

## 英文摘要

Minimum-storage regenerating (MSR) codes are repair-optimal erasure codes that minimize the bandwidth for repairing a failed node, while minimizing the storage redundancy necessary for fault tolerance. Recent studies in the literature, both from coding theory and systems communities, mainly examine MSR codes in systematic form, which keeps the original data blocks as part of the encoded blocks for direct access. However, systematic MSR codes manage encoded blocks at the sub-block granularity and access non-contiguous sub-blocks during repairs to achieve bandwidth optimality. Thus, their actual repair performance is impaired by non-contiguous I/Os, especially when the block size is small. In this paper, we explore how non-systematic MSR codes, which generate purely coded blocks based on random linear coding in the classical network coding theory, can improve I/O efficiency in repair for practical warm blob (binary large object) storage systems that are dominated by a large fraction of small blobs. To this end, we design NCBlob, a network-coding-based warm blob storage system that encodes small blobs non-systematic MSR codes to achieve high repair performance, while leveraging the access locality of small blobs to maintain high normal read performance. Experiments on Alibaba Cloud show that NCBlob reduces the single-block repair time by up to 45.0%, and the full-node repair time by up to 38.4%, with as low as 2.1% read throughput loss, compared with state-of-the-art systematic MSR codes.

## 中文摘要

最小存储再生（MSR）码是修复最优的纠删码：它最小化修复失效节点所需的带宽，同时最小化容错所需的存储冗余。近期来自编码理论与系统社区的研究，主要考察系统化形式的 MSR 码——保留原始数据块作为编码块的一部分，以便直接访问。然而，系统化 MSR 码以子块粒度管理编码块，并在修复时访问不连续的子块以保持带宽最优；因此其实际修复性能受到非连续 I/O 的拖累，块较小时尤为明显。本文探讨：在由大量小 blob 主导的实际温数据 blob（二进制大对象）存储系统中，基于经典网络编码理论中的随机线性编码、只生成编码块的非系统化 MSR 码，如何提升修复的 I/O 效率。为此，本文设计 NCBlob——一个基于网络编码的温数据 blob 存储系统，它对小 blob 采用非系统化 MSR 码以获得高修复性能，同时利用小 blob 的访问局部性维持较高的正常读性能。阿里云上的实验表明，相比最先进的系统化 MSR 码，NCBlob 将单块修复时间最多降低 45.0%，整节点修复时间最多降低 38.4%，读吞吐损失低至 2.1%。

## 一句话总结

> 带宽最优不等于修复最快：块小的时候，系统化 MSR 码的非连续 I/O 才是瓶颈，退回非系统化编码反而更快。

## 研究背景与问题

- 纠删码比副本省空间且容错相同，但修复单个块要取同一条带多个块，修复带宽高；MSR 码（minimum-storage regenerating codes，最小存储再生码）把块切成子块混合传输，可在最小存储冗余下把修复带宽压到理论下界。
- 主流 MSR 码都是系统化形式（保留原始数据块以便直接读），Clay codes 是其中最优者：最小冗余、支持任意 (n,k)、磁盘 I/O 总量等于修复带宽且访问最优。
- 但 Clay codes 的子包化层级随条带块数指数增长（α 为 (n−k) 的 ⌈n/(n−k)⌉ 次方），修复时每个节点要读大量子块，形成非连续 I/O，块小时实际修复性能被抵消。
- 温 blob 存储以小对象为主：Facebook f4 中几乎所有照片 blob 小于 1 MB、60% 视频 blob 小于 1 MB，Azure functions 访问的 80% blob 小于 12 KB；温 blob 又占 Facebook 全部 blob 类型的 80% 以上，f4 已用纠删码替代副本。

## 核心贡献

- 提出按 blob 大小分流的混合编码（NCBlob）：大 blob 用系统化 MSR 码，小 blob 用经典网络编码中的非系统化 MSR 码，兼顾直接读与修复效率。
- 基于两类数据访问局部性设计两种非系统化 MSR 编码方案，压低非系统化码在正常读时的读放大。
- 证明在容忍至多三次故障时，NCBlob 对任意编码参数都存在。
- 实现原型并用 ParaRC 式并行化加速修复与读操作，代码已公开。

## 方法与技术要点

- 小 blob 非系统化编码：条带只由随机线性网络编码生成的校验块组成，子包化层级为 n−k，修复为 functional repair——修出的块可与原块不同，只要容错仍成立，因此每个节点只需读少量连续子块。
- 访问局部性分组：把可能被一起访问的数据单元刻意放在同一组，使解码所需子块尽量连续，用局部性换回正常读性能。
- 混合条带布局：按 blob 大小分流，大 blob 走系统化码保留直接访问，小 blob 走非系统化码换取修复时的 I/O 连续性。
- 修复并行化：借鉴 ParaRC 把一次修复拆成多个子操作分发到多节点执行，压低单点最大修复负载而不牺牲修复效率。
- 参数覆盖：在 (6,4)、(9,6)、(12,8)、(14,10) 等编码参数下实现并评估，验证非系统化方案的通用性。

## 评估与主要结果

- 阿里云上的实验，对比最先进的系统化 MSR 码（Clay）：单块修复时间最多降低 45.0%，整节点修复时间最多降低 38.4%，同时读吞吐损失低至 2.1%。
- (n,k) = (14,10) 下把网络带宽从 5 Gbps 变到 15 Gbps：所有方案的读延迟都随带宽下降而上升，而带局部性的 NCBlob 始终保持优势。
- 开销（256 MB 块）：(6,4) 下带局部性的 NCBlob CPU 使用率为 80.1%，比 Clay 高 4.8%；相比不带局部性的版本，带局部性可把内存开销最多降低 56.3%（(14,10) 时）。

## 代码与研究制品

- [代码仓库](https://github.com/YuchongHu/NCBlob)

[返回 Cloud Storage](index.md) · [返回 FAST 2025](../index.md)
