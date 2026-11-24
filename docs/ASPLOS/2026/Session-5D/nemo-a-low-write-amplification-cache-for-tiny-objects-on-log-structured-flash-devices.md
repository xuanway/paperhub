---
title: "Nemo: A Low-Write-Amplification Cache for Tiny Objects on Log-Structured Flash Devices"
description: "ASPLOS 2026 · Session 5D · Nemo：面向日志结构闪存设备上小对象的低写放大缓存"
tags:
  - "ASPLOS2026"
  - "Session 5D"
  - "Storage & Caching"
---

# Nemo: A Low-Write-Amplification Cache for Tiny Objects on Log-Structured Flash Devices

**中文标题：** Nemo：面向日志结构闪存设备上小对象的低写放大缓存

**所属 Session：** [Session 5D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Xufeng Yang (Xiamen University), Tingting Tan (Xiamen University), Jingxin Hu (Chongqing University of Posts and Telecommunications), Congming Gao (Xiamen University), Mingyang Liu (Xiamen University), Tianyang Jiang (Huawei Technologies Co., Ltd.), Jian Chen (Tsinghua University), Linbo Long (Chongqing University of Posts and Telecommunications), Yina Lv (Xiamen University), Jiwu Shu (Xiamen University)

**单位：** Xiamen University；Chongqing University of Posts and Telecommunications；Huawei Technologies Co., Ltd.；Tsinghua University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790191) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Modern storage systems predominantly use flash-based SSDs as a cache layer due to their favorable performance and cost efficiency. However, in tiny-object workloads, existing flash cache designs still suffer from high write amplification. Even when deploying advanced log-structured flash devices (e.g., Zoned Namespace SSDs and Flexible Data Placement SSDs) with low device-level write amplification, application-level write amplification still dominates. This work proposes Nemo, which enhances set-associative cache design by increasing hash collision probability to improve set fill rate, thereby reducing application-level write amplification. To satisfy caching requirements, including high memory efficiency and low miss ratio, we introduce a bloom filter-based indexing mechanism that significantly reduces memory overhead, and adopt a hybrid hotness tracking to achieve low miss ratio without losing memory efficiency. Experimental results show that Nemo simultaneously achieves three key objectives for flash cache: low write amplification, high memory efficiency, and low miss ratio.

## 中文摘要

现代存储系统主要使用基于闪存的 SSD 作为缓存层，因为其具有出色的性能与成本效率。然而，在小对象负载中，现有的闪存缓存设计仍然面临高写放大的问题。即使在部署具备低设备级写放大的先进日志结构闪存设备（例如 Zoned Namespace SSD 和 Flexible Data Placement SSD）时，应用级写放大仍然占据主导地位。本工作提出 Nemo，它通过提高哈希冲突概率来提升组填充率，从而增强组相联缓存设计，进而降低应用级写放大。为满足包括高内存效率和低缺失率在内的缓存需求，我们引入一种基于 bloom filter 的索引机制，显著降低内存开销，并采用混合热度追踪，在保持内存效率的同时实现低缺失率。实验结果表明，Nemo 同时实现了闪存缓存的三个关键目标：低写放大、高内存效率和低缺失率。

## 英文关键词

Computer Architecture; Key-value Cache; Flash Memory; Write Amplification Optimization

## 中文关键词

计算机体系结构；键值缓存；闪存；写放大优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790191)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5D](index.md) · [返回 ASPLOS 2026](../index.md)
