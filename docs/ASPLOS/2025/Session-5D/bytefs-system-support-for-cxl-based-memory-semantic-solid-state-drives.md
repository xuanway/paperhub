---
title: "ByteFS: System Support for (CXL-based) Memory-Semantic Solid-State Drives"
description: "ASPLOS 2025 · Session 5D · ByteFS：面向（基于 CXL 的）内存语义固态硬盘的系统支持"
tags:
  - "ASPLOS2025"
  - "Session 5D"
  - "CXL Storage"
---

# ByteFS: System Support for (CXL-based) Memory-Semantic Solid-State Drives

**中文标题：** ByteFS：面向（基于 CXL 的）内存语义固态硬盘的系统支持

**所属 Session：** [Session 5D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Shaobo Li (University of Illinois Urbana-Champaign), Yirui (Eric) Zhou (University of Illinois Urbana-Champaign), Hao Ren (University of Illinois Urbana-Champaign), Jian Huang (University of Illinois Urbana-Champaign)

**单位：** University of Illinois Urbana-Champaign；Eric

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707250) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Unlike non-volatile memory that resides on the processor memory bus, memory-semantic solid-state drives (SSDs) support both byte and block access granularity via PCIe or CXL interconnects. They provide scalable memory capacity using NAND flash at a much lower cost. In addition, they have different performance characteristics for their dual byte/block interface respectively, while offering essential memory semantics for upper-level software.Suchabyte-accessible storage device provides new implications on the software system design. In this paper, we develop a new file system, named ByteFS, by rethinking the design primitives of file systems and SSD firmware to exploit the advantages of both byte and blockgranular data accesses. ByteFS supports byte-granular data persistence to retain the persistence nature of SSDs. It extends the core data structure of file systems by enabling dual byte/block-granular data accesses. To facilitate the support for byte-granular writes, ByteFS manages the internal DRAM of SSD firmware in a log-structured manner and enables data coalescing to reduce the unnecessary I/O traffic to flash chips. ByteFS also enables coordinated data caching between the host page cache and SSD cache for best utilizing the precious memory resource. We implement ByteFS on both a real programmable SSD and an emulated memory-semantic SSD for sensitivity study. Compared to state-of-the-art file systems for non-volatile memory and conventional SSDs, ByteFS outperforms them by up to 2.7×, while preserving the essential properties of a file system. ByteFS also reduces the write traffic to SSDs by up to 5.1× by alleviating unnecessary writes caused by both metadata and data updates in file systems.

## 中文摘要

与驻留在处理器内存总线上的非易失性内存不同，内存语义固态硬盘（SSD）可通过 PCIe 或 CXL 互连同时支持字节与块两种访问粒度。它们利用 NAND 闪存以低得多的成本提供可扩展的内存容量。此外，其字节/块双重接口各自具有不同的性能特征，同时为上层软件提供必要的内存语义。这种可字节访问的存储设备为软件系统设计带来了新的含义。本文通过重新思考文件系统与 SSD 固件的设计原语，开发了一个名为 ByteFS 的新文件系统，以同时利用字节与块粒度数据访问的优势。ByteFS 支持字节粒度的数据持久化，从而保留 SSD 的持久性特征。它通过支持字节/块双重粒度的数据访问，扩展了文件系统的核心数据结构。为便于支持字节粒度写入，ByteFS 以日志结构的方式管理 SSD 固件的内部 DRAM，并启用数据合并以减少发往闪存芯片的不必要 I/O 流量。ByteFS 还在主机页缓存与 SSD 缓存之间实现协同数据缓存，以最佳地利用宝贵的内存资源。我们在真实的可编程 SSD 和模拟的内存语义 SSD 上分别实现了 ByteFS，以开展敏感性研究。与面向非易失性内存和传统 SSD 的最先进文件系统相比，ByteFS 的性能最高提升 2.7 倍，同时保留了文件系统的本质属性。ByteFS 还通过缓解文件系统中元数据与数据更新所引起的不必要写入，将发往 SSD 的写流量最高降低 5.1 倍。

## 英文关键词

FileSystem,Byte-addressableSSD,CXL,MemorySemantic Storage

## 中文关键词

文件系统；字节可寻址 SSD；CXL；内存语义存储

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707250)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5D](index.md) · [返回 ASPLOS 2025](../index.md)
