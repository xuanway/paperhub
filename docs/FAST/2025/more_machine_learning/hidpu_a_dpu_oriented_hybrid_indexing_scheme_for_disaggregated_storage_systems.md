---
title: "HiDPU: A DPU-Oriented Hybrid Indexing Scheme for Disaggregated Storage Systems"
description: "FAST 2025 · More Machine Learning · DPU 上按地址连续性分段做混合索引，内存最多省 92%、查询快 6.3 倍"
tags:
  - "FAST2025"
  - "More Machine Learning"
  - "disaggregated storage"
  - "DPU"
---

# HiDPU: A DPU-Oriented Hybrid Indexing Scheme for Disaggregated Storage Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">分离式存储中 DPU 取数前要回 host 内存查地址映射，软件开销让索引延迟从 4 µs 涨到 5000 µs 以上。HiDPU 按地址连续性分段组合线性索引、PTHash 与 LPTHash，再用多层 learned index 定位段，在华为 Hi1823 上内存最多省 92%、查询性能最高提升 6.3 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · More Machine Learning</p>
</div>

**中文标题**：HiDPU：面向解耦存储系统的 DPU 导向混合索引方案

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/zhu](https://www.usenix.org/conference/fast25/presentation/zhu)

**论文 PDF**：[fast25-zhu.pdf](https://www.usenix.org/system/files/fast25-zhu.pdf)

**作者**：Wenbin Zhu、Zhaoyan Shen、Qian Wei（Shandong University）；Renhai Chen（Tianjin University and Huawei Technologies Co., Ltd）；Xin Yao（Huawei Technologies Co., Ltd）；Dongxiao Yu（Shandong University）；Zili Shao（The Chinese University of Hong Kong）

**会议**：FAST 2025 · Santa Clara, CA · 第 271–285 页

**Session**：More Machine Learning · 2025-02-26 09:00–10:20 · Chair：Ali R. Butt（Virginia Tech）

**所属 Session**：[More Machine Learning](index.md) · [FAST 2025](../index.md)

**关键词**：disaggregated storage, DPU, learned index, perfect hash table, address translation

---

## 英文摘要

Data Processing Units (DPUs) have been deployed in disaggregated storage systems to accelerate data transmission. However, in this paper, we observe that during data access in disaggregated storage, the address translation process incurs significant CPU computation overhead and leads to high system latency. Additionally, in large-scale storage systems, the address indexing structures also consume substantial memory space, incurring high costs.

To address these challenges, we propose HiDPU, a DPU-oriented hybrid indexing scheme optimized for disaggregated storage systems. Our solution introduces a multi-level indexing structure to alleviate the limitations of DPU memory resources, constrained computational power, and the high DPU-host interaction overhead. Mapping entries for the storage space are divided into different kinds of segments (i.e., accurate, PTHash, and LPTHash) to leverage address continuity. A layered learned index is constructed across these segments to enhance memory efficiency. To further reduce DPU-host interactions, small upper-layer indexes and frequently accessed metadata are maintained on the DPU, limiting interactions to a single instance. HiDPU also implements a two-phase asynchronous index update strategy to ensure index consistency between the DPU and host memory, while minimizing performance overhead. Experimental results on Huawei’s Hi1823 DPU demonstrate that HiDPU achieves up to 92% memory savings and improves query performance by up to 6.3 times compared to existing solutions.

## 中文摘要

数据处理单元（DPU）已被部署到分离式存储系统中加速数据传输，但在这种架构下地址转换会带来可观的 CPU 计算开销与较高延迟，大规模系统中地址索引结构还会占用大量内存。HiDPU 是面向分离式存储、为 DPU 优化的混合索引方案：它用多级索引结构缓解 DPU 内存有限、算力受限以及 DPU 与 host 交互开销高的问题，把映射条目按地址连续性划分为 accurate、PTHash 与 LPTHash 等段，并在这些段之上构建分层学习索引以提升内存效率；小体积的上层索引与频繁访问的元数据保留在 DPU 上，使交互限制在一次之内；它还实现两阶段异步索引更新，在保证 DPU 与 host 内存索引一致的同时压低开销。在华为 Hi1823 DPU 上的实验显示，HiDPU 最多节省 92% 的内存，查询性能最高提升 6.3 倍。

## 一句话总结

> 让 DPU 自己查地址映射：按地址连续性分段混合索引，把 DPU-host 交互压到一次。

## 研究背景与问题

- **查表要走一趟 host**：分离式存储把统一逻辑地址空间暴露给计算服务器，映射表存放在 host 控制器的内存里；DPU 虽然能直连闪存阵列，但取数前必须经 PCIe 回 host 查索引，CPU 侧的缓冲分配、线程调度与用户态内核态切换等软件开销随并发迅速放大。
- **延迟量级失配**：实测客户端数增加时索引延迟从 4 µs 升到 5000 µs 以上，超过企业级 NVMe SSD 的 10–200 µs；传输物理地址的延迟可达索引查找本身的 18 到 628 倍。
- **DPU 自身资源受限**：片上内存只有 MB 级（1 PB 闪存阵列按 16KB 页建索引需 64GB），计算核为高吞吐、弱指令集而设计，PCIe 交互又昂贵，照搬 CPU 侧索引结构不可行。
- **已有 DPU 索引方案的不足**：Leed 把外部索引放在 Flash 中，每个键值请求需要两次 NVMe 访问；LearnedFTL 要为每个映射条目维护一位 bitmap，体积过大难以放进 DPU 内存。

## 核心贡献

- **面向 DPU 的混合索引（HiDPU）**：按逻辑地址连续性把地址空间切段，分别用线性索引、线性加完美哈希、完美哈希三类段结构，以地址连续性换内存空间。
- **跨段的多层 learned index**：用小体积的学习索引定位目标段，并把上层索引与高频元数据驻留 DPU，把 DPU-host 交互限制在一次。
- **两阶段异步索引更新**：索引更新交给 host CPU，实时插入被缓冲成批量插入并在后台局部重建，周期性全局重建消除失衡，同时保证 DPU 与 host 内存的索引一致。
- **真实硬件原型**：在华为 Hi1823 DPU 上实现完整原型，并提供可公开访问的 host 版功能原型。

## 方法与技术要点

- **按连续性分段**：索引构建时把统一逻辑地址空间切成段——强连续区用线性索引（accurate），弱连续区用线性加完美哈希（LPTHash），完全随机的区用完美哈希（PTHash，双哈希配合每桶唯一的 pilot 值消解冲突）。
- **分层摆放**：各段的详细索引放在容量更大的 host 内存，DPU 只保留小体积的上层 learned index 与常访问元数据，用很小的空间覆盖大部分查找。
- **DPU 侧缓存**：利用数据局部性实现 pilot 缓存与按需访问，减少对 host 内存的往返次数。
- **更新路径**：实时插入先由 host 缓冲并转换成批量插入，后台以局部重建增量更新索引，再周期性全局重建抑制局部更新造成的不均衡。
- **一致性保障**：采用两阶段异步更新策略，在保证 DPU 与 host 内存索引一致的前提下压低更新开销。

## 评估与主要结果

- **平台**：华为 Hi1823 DPU 上的完整原型，配合公开块 I/O 数据集与多种真实基准测试。
- **内存与查询**：相对传统索引，内存占用最多降低 92%，查询（lookup）效率最高提升 6.3 倍；1.2 PB 存储系统最少只需 23 KB DPU 内存。
- **与 LearnedFTL 对比**：单客户端下 HiDPU 吞吐最高，因为消除了软件开销带来的延迟；HiDPU-H 也略高于 LearnedFTL，后者可能为映射条目发起 I/O，概率虽低至 0.5%，但 I/O 延迟对性能影响明显。

[返回 More Machine Learning](index.md) · [返回 FAST 2025](../index.md)
