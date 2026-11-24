---
title: "ANVIL: An In-Storage Accelerator for Name–Value Data Stores"
description: "ISCA 2025 · Session 3C · ANVIL: 键值存储的存储内加速器"
tags:
  - "ISCA2025"
  - "Session 3C"
  - "Storage"
---

# ANVIL: An In-Storage Accelerator for Name–Value Data Stores

**中文标题：** ANVIL: 键值存储的存储内加速器

**所属 Session：** [Session 3C](index.md) · [ISCA 2025](../index.md)

**作者：** Ryan Wong, Nikita Kim, Aniket Das, Kevin Higgs, Engin Ipek, Sapan Agarwal, Saugata Ghose, Ben Feinberg

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731000) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Name–value pairs (NVPs) are a widely-used abstraction to organize data in millions of applications. At a high level, an NVP associates a name (e.g., array index, key, hash) with each value in a collection of data. Specific NVP data store formats can vary widely, ranging from simple arrays/dictionaries and lookup tables to key–value stores and data mining workloads. Despite their importance, existing optimizations for NVPs are limited to only a single data store format, as the broad definition of NVPs allows for significant heterogeneity in encoding and implementation. We propose ANVIL, the first end-to-end system that allows pro- grammers to broadly accelerate most formats of NVPs. With a conventional solid-state drive (SSD), large-scale NVP lookups can saturate both external and internal SSD bandwidth, as every NVP in the data store needs to be sent back to the host CPU to check for a matching name. ANVIL makes use of in-storage processing to avoid reading out any data for names that do not match, by performing name match checks directly inside the SSD’s NAND flash chips. We demonstrate that ANVIL can substantially reduce disk I/O, reduce metadata overheads, and provide speedups of 4.0×, 25×, and 14.6% over a conventional SSD, for three different NVP workloads (database transactions, analytics, and graph processing).

## 中文摘要

名值对（NVP）是一种应用广泛的数据抽象，为数百万应用提供数据组织方式。简单来说，名值对为数据集合里的每一个值绑定一个名称（例如数组索引、键、哈希值）。名值对的存储格式差异很大，涵盖简单数组/字典、查找表、键值存储以及数据挖掘负载。尽管其应用十分重要，但现有针对名值对的优化方案通常仅适配单一存储格式；这是因为名值对的定义宽泛，编码与实现方式高度异构。

本文提出ANVIL，首个端到端系统，支持开发者对绝大多数格式的名值对进行通用加速。在传统固态硬盘（SSD）上，大规模名值对查询会打满SSD的外部与内部带宽，原因是存储内的每一条名值对都需要传回主机CPU，才能完成名称匹配校验。ANVIL采用存储内计算，直接在SSD的NAND闪存芯片内部完成名称匹配校验，不匹配的条目无需读出数据。实验表明，针对三类名值对负载（数据库事务、数据分析、图处理），ANVIL能够大幅减少磁盘I/O、降低元数据开销；相比传统SSD，分别实现4.0倍、25倍的加速以及14.6%的性能提升。

## 英文关键词

name–value pairs, in-storage processing, solid-state drives, key–value stores, processing-using-memory, hash indexing

## 中文关键词

名值对, 存储内计算, 固态硬盘, 键值存储, 村内计算, 哈希索引

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731000)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3C](index.md) · [返回 ISCA 2025](../index.md)
