---
title: "Random-Access Hardware Sequence Compression"
description: "ISCA 2026 · Session 6B · Random-Access Hardware Sequence Compression"
tags:
  - "ISCA2026"
  - "Session 6B"
  - "Deep Learning / Memory Acceleration"
---

# Random-Access Hardware Sequence Compression

**中文标题：** 可随机访问的硬件序列压缩

**所属 Session：** [Session 6B](index.md) · [ISCA 2026](../index.md)

**作者：** Nolan Chu, Yoon Lee, Gagandeep Panwar, Xun Jian

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Memory compression is a promising solution to combat the high and rising DRAM cost in modern data centers. Due to providing high compression ratios, page-level sequence compression (e.g., LZ) has become a part of the industry specification for hardware memory compression. Unfortunately, sequence compression suffers from slow decompression. Decompressing a requested memory block in a page incurs 1) high memory access latency to fetch everything prior to the block and 2) long computation latency due to decompressing all the way from the start of the page to the requested block. This is because to maximize compression ratio, each block is compressed using everything prior to the block as a large dictionary, resulting in high access and computation overhead to fetch and reconstruct the large dictionary when decompressing a needed block. To tackle the high access overhead, we propose a randomly-decompressible compression algorithm that drastically shrinks the total dictionary in each page down to 128 B, without sacrificing compression ratio w.r.t. the state-of-the-art hardware. We also design compression and decompression hardware for the new algorithm; ASIC synthesis reports that total decompression computation latency is reduced to 18 ns per needed block vs. 140 ns average latency under the state-of-the-art.

## 中文摘要

内存压缩是应对现代数据中心高昂且不断上升的 DRAM 成本的一种有前景的解决方案。由于能提供高压缩率，页级序列压缩（如 LZ）已成为硬件内存压缩行业规范的一部分。遗憾的是，序列压缩的解压速度很慢。解压页内某个被请求的内存块会带来：1) 获取该块之前所有内容的高内存访问延迟；2) 由于必须从页首一直解压到被请求块而产生的长计算延迟。这是因为为最大化压缩率，每个块都以其前面所有内容作为大字典进行压缩，导致解压所需块时需要获取并重建这个大字典，带来高昂的访问与计算开销。为解决高访问开销问题，我们提出一种可随机解压的压缩算法，将每页的总字典大幅缩减至 128 字节，同时相对于最先进硬件不牺牲压缩率。我们还为新算法设计了压缩与解压硬件；ASIC 综合报告显示，每个所需块的总解压计算延迟降至 18 ns，而最先进方案的平均延迟为 140 ns。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：HEAP-Lab-VT/rst](https://github.com/HEAP-Lab-VT/rst)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6B](index.md) · [返回 ISCA 2026](../index.md)
