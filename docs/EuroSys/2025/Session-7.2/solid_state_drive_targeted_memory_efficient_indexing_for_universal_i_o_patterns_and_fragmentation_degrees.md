---
title: "Solid State Drive Targeted Memory-Efficient Indexing for Universal I/O Patterns and Fragmentation Degrees"
description: "EuroSys 2025 · Storage · Junsu Im (POSTECH), Jeonggyun Kim (DGIST), Seonggyun Oh (DGIST), Jinhyung Koo (P"
tags:
  - "EuroSys2025"
  - "Storage"
---

# Solid State Drive Targeted Memory-Efficient Indexing for Universal I/O Patterns and Fragmentation Degrees

**中文标题：** 面向通用 I/O 模式和碎片程度的固态硬盘内存高效索引

**所属 Session：** [Session 7.2: Storage](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Storage</p>
</div>

**作者**：Junsu Im (POSTECH), Jeonggyun Kim (DGIST), Seonggyun Oh (DGIST), Jinhyung Koo (POSTECH), Juhyung Park (DGIST), Hoon Sung Chwa (DGIST), Sam H. Noh (Virginia Tech), Sungjin Lee (POSTECH)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717478)

## 英文摘要

Thanks to the advance of device scaling technologies, the capacity of SSDs is rapidly increasing. Such increase, however, comes at the cost of a huge index table requiring large DRAM. To provide reasonable performance with less DRAM, various index structures exploiting locality and regularity of I/O references have been proposed. However, they provide deteriorated performance depending on I/O patterns and storage fragmentation. This paper proposes a novel approximate index structure, called AppL, which combines memory-efficient approximate indices and an LSM-tree that has an append-only and sorted nature. AppL reduces the index size to 6∼8-bits per entry, which is considerably smaller than the typical index structures requiring 32∼64-bits, and maintains such high memory efficiency irrespective of locality and fragmentation. By alleviating memory pressure, AppL achieves 33.6∼72.4% shorter read latency and 28.4%∼83.4% higher I/O throughput than state-of-the-art techniques.

## 中文摘要

得益于器件微缩技术的进步，SSD 的容量正快速提升。然而这种提升的代价是需要占用大量 DRAM 的庞大索引表。为在更少 DRAM 下提供合理性能，研究者提出了多种利用 I/O 访问的局部性和规律性的索引结构。但它们的性能会因 I/O 模式和存储碎片而退化。本文提出一种新颖的近似索引结构 AppL，它将内存高效的近似索引与具有仅追加和有序特性的 LSM 树相结合。AppL 将索引大小降至每项 6 至 8 位，远小于通常需要 32 至 64 位的典型索引结构，并且无论局部性和碎片程度如何都能保持这种高内存效率。通过缓解内存压力，AppL 相比最先进技术实现读延迟缩短 33.6% 至 72.4%，I/O 吞吐提升 28.4% 至 83.4%。

**英文关键词：** LSM-tree, learned index, and SSDs

**中文关键词：** LSM 树、学习索引、SSD

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
